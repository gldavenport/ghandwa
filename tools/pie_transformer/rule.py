"""
Rule model and pipeline runner.

Rule:
  id       — stable machine-readable identifier
  name     — human-readable rule name
  stage    — human-readable stage label for traces and reports
  requires — list of metadata keys that must be present for the rule to execute;
             in v1 the only supported value is "accent"
  apply    — function(tokens: list[str], context: Context) -> list[str]

Context:
  accent_index — zero-based token index of the accented segment, or None if unknown.
                 Rules that insert or delete tokens before the accented position
                 are responsible for updating this field.
  options      — dict of pipeline-specific toggle flags; checked by rules via
                 ctx.options.get('flag-name', default).

All exceptions during rule execution are caught, logged, and result in status='error'
for that derivation. In batch mode, processing continues with the next item.
"""

from __future__ import annotations

import traceback
from dataclasses import dataclass, field
from typing import Callable


# ── Context ────────────────────────────────────────────────────────────────────

@dataclass
class Context:
    accent_index: int | None = None
    options: dict = field(default_factory=dict)


# ── Rule ───────────────────────────────────────────────────────────────────────

@dataclass
class Rule:
    id: str
    name: str
    stage: str
    requires: list[str]
    apply: Callable[[list[str], Context], list[str]]


# ── Trace ──────────────────────────────────────────────────────────────────────

@dataclass
class TraceRow:
    pipeline: str
    stage: str
    rule_id: str
    rule_name: str
    before_tokens: list[str]
    after_tokens: list[str]
    changed: bool
    status: str  # 'ok' | 'blocked' | 'error'
    message: str = ''


# ── Derivation result ──────────────────────────────────────────────────────────

@dataclass
class DerivationResult:
    pipeline: str
    input_form: str           # original raw input
    status: str               # 'ok' | 'blocked_missing_accent' | 'error' | 'not_implemented'
    final_tokens: list[str] = field(default_factory=list)
    trace: list[TraceRow] = field(default_factory=list)
    generated_surface: str = ''
    generated_ipa: str = ''
    generated_tokens: str = ''
    blocked_stage: str = ''
    blocked_rule: str = ''
    blocked_form: str = ''
    error_type: str = ''
    error_message: str = ''
    final_accent_index: int | None = None   # token index of accented segment in final_tokens


# ── Runner ─────────────────────────────────────────────────────────────────────

_SUPPORTED_REQUIRES = {'accent'}


def run_pipeline(
    pipeline_name: str,
    rules: list[Rule],
    tokens: list[str],
    context: Context,
    input_form: str,
    trace_mode: str = 'changed',  # 'changed' | 'full'
) -> DerivationResult:
    """
    Execute an ordered list of rules against a token stream.

    trace_mode:
      'changed' — record only rules that changed the token stream
      'full'    — record every rule

    Returns a DerivationResult.
    """
    from .tokenize import tokens_to_string  # avoid circular import

    trace: list[TraceRow] = []
    current = list(tokens)

    for rule in rules:
        # Check requires
        for req in rule.requires:
            if req not in _SUPPORTED_REQUIRES:
                # Unknown requirement type: skip silently (v1 only supports "accent")
                continue
            if req == 'accent' and context.accent_index is None:
                # Blocked: accent required but unknown
                form_at_block = tokens_to_string(current)
                trace.append(TraceRow(
                    pipeline=pipeline_name,
                    stage=rule.stage,
                    rule_id=rule.id,
                    rule_name=rule.name,
                    before_tokens=list(current),
                    after_tokens=list(current),
                    changed=False,
                    status='blocked',
                    message='accent required but not present in context',
                ))
                result = DerivationResult(
                    pipeline=pipeline_name,
                    input_form=input_form,
                    status='blocked_missing_accent',
                    final_tokens=list(current),
                    trace=trace,
                    blocked_stage=rule.stage,
                    blocked_rule=rule.name,
                    blocked_form=form_at_block,
                )
                result.generated_tokens = tokens_to_string(current)
                return result

        # Execute rule
        before = list(current)
        try:
            after = rule.apply(list(current), context)
        except Exception as exc:
            form_at_error = tokens_to_string(current)
            trace.append(TraceRow(
                pipeline=pipeline_name,
                stage=rule.stage,
                rule_id=rule.id,
                rule_name=rule.name,
                before_tokens=before,
                after_tokens=list(current),
                changed=False,
                status='error',
                message=f'{type(exc).__name__}: {exc}',
            ))
            result = DerivationResult(
                pipeline=pipeline_name,
                input_form=input_form,
                status='error',
                final_tokens=list(current),
                trace=trace,
                blocked_stage=rule.stage,
                blocked_rule=rule.name,
                blocked_form=form_at_error,
                error_type=type(exc).__name__,
                error_message=str(exc),
            )
            result.generated_tokens = tokens_to_string(current)
            return result

        changed = after != before
        current = after

        if trace_mode == 'full' or changed:
            trace.append(TraceRow(
                pipeline=pipeline_name,
                stage=rule.stage,
                rule_id=rule.id,
                rule_name=rule.name,
                before_tokens=before,
                after_tokens=list(current),
                changed=changed,
                status='ok',
            ))

    result = DerivationResult(
        pipeline=pipeline_name,
        input_form=input_form,
        status='ok',
        final_tokens=list(current),
        trace=trace,
        final_accent_index=context.accent_index,
    )
    result.generated_tokens = tokens_to_string(current)
    return result


# ── scan() helper (used by pipeline rule functions) ────────────────────────────

def scan(
    tokens: list[str],
    fn: Callable[[str, int, list[str]], str | list[str] | None],
) -> list[str]:
    """
    Walk a token stream, apply fn(token, index, tokens) to each token.
    fn may return:
      - a string (replacement token)
      - a list of strings (replacement tokens, may be 0 or many)
      - None (delete the token)
    """
    out: list[str] = []
    for i, tok in enumerate(tokens):
        r = fn(tok, i, tokens)
        if r is None:
            continue
        elif isinstance(r, list):
            out.extend(r)
        else:
            out.append(r)
    return out
