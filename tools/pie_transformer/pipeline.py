"""
Pipeline registry and chaining logic.

Registered pipelines:
  ghandwa         — implemented
  wekwos-old      — implemented (provisional)
  wekwos-neo      — implemented (provisional); downstream of wekwos-old
  proto-anatolian — implemented
  proto-seldanic  — implemented
  ghandwa-daughter-a — implemented (Stage 2 only; Stage 3 stub)
  ghandwa-daughter-b — implemented (Stage 2 only; Stage 3 stub)
  ghandwa-daughter-c — implemented (Stage 2 + Stage 3)

Pipeline chaining:
  Wékʷos-Neo is downstream of Wékʷos-Old. Its input token stream is the final
  output of the Wékʷos-Old pipeline. Re-tokenization does not occur.

  Daughter pipelines (A, B, C) are all downstream of 'ghandwa'. Input token
  stream is the final output of the ghandwa pipeline. Re-tokenization does not occur.
"""

from __future__ import annotations

from .rule import Rule, Context, DerivationResult, run_pipeline
from pie_core.tokenize import tokens_to_string


# ── Pipeline registry ──────────────────────────────────────────────────────────

_IMPLEMENTED = {'ghandwa', 'wekwos-old', 'wekwos-neo', 'proto-anatolian', 'proto-seldanic', 'ghandwa-daughter-a', 'ghandwa-daughter-b', 'ghandwa-daughter-c'}
_NOT_IMPLEMENTED: set[str] = set()
ALL_PIPELINES = sorted(_IMPLEMENTED | _NOT_IMPLEMENTED)


# ── Pipeline hierarchy ─────────────────────────────────────────────────────────

PIPELINE_PARENTS: dict[str, str | None] = {
    'ghandwa':            None,
    'ghandwa-daughter-a': 'ghandwa',
    'ghandwa-daughter-b': 'ghandwa',
    'ghandwa-daughter-c': 'ghandwa',
    'proto-anatolian':    None,
    'proto-seldanic':     None,
    'wekwos-old':         None,
    'wekwos-neo':         'wekwos-old',
}

_DISPLAY_ROOTS = ['ghandwa', 'proto-anatolian', 'proto-seldanic', 'wekwos-old']

PIPELINE_IS_RECONSTRUCTION: dict[str, bool] = {
    'ghandwa':            False,
    'ghandwa-daughter-a': False,
    'ghandwa-daughter-b': False,
    'ghandwa-daughter-c': False,
    'proto-anatolian':    True,
    'proto-seldanic':     True,
    'wekwos-old':         True,
    'wekwos-neo':         True,
}


def pipeline_display_order() -> list[tuple[str, int]]:
    """Return (pipeline_name, depth) pairs in tree order for --all display."""
    from collections import defaultdict
    children: dict[str, list[str]] = defaultdict(list)
    for name, parent in PIPELINE_PARENTS.items():
        if parent is not None:
            children[parent].append(name)
    for lst in children.values():
        lst.sort()
    result: list[tuple[str, int]] = []
    for root in _DISPLAY_ROOTS:
        result.append((root, 0))
        for child in children.get(root, []):
            result.append((child, 1))
    return result


def _load_rules(name: str) -> list[Rule]:
    """Lazy-load rules for a named pipeline to avoid import-time side effects."""
    if name == 'ghandwa':
        from .pipelines.ghandwa import RULES
        return RULES
    if name == 'wekwos-old':
        from .pipelines.wekwos_old import RULES
        return RULES
    if name == 'wekwos-neo':
        from .pipelines.wekwos_neo import RULES
        return RULES
    if name == 'proto-anatolian':
        from .pipelines.proto_anatolian import RULES
        return RULES
    if name == 'proto-seldanic':
        from .pipelines.proto_seldanic import RULES
        return RULES
    if name == 'ghandwa-daughter-a':
        from .pipelines.daughter_a import RULES_A
        return RULES_A
    if name == 'ghandwa-daughter-b':
        from .pipelines.daughter_b import RULES_B
        return RULES_B
    if name == 'ghandwa-daughter-c':
        from .pipelines.daughter_c import RULES_C
        return RULES_C
    raise ValueError(f'Unknown pipeline: {name!r}')


# ── Public run function ────────────────────────────────────────────────────────

def run(
    pipeline_name: str,
    tokens: list[str],
    context: Context,
    input_form: str,
    trace_mode: str = 'changed',
) -> DerivationResult:
    """
    Run a named pipeline against a token stream.

    Handles:
      - not_implemented pipelines → DerivationResult with status='not_implemented'
      - wekwos-neo chaining → runs wekwos-old first, then wekwos-neo rules
      - all other pipelines → runs rules directly
    """
    if pipeline_name in _NOT_IMPLEMENTED:
        return _not_implemented_result(pipeline_name, tokens, input_form)

    if pipeline_name not in _IMPLEMENTED:
        return _error_result(pipeline_name, tokens, input_form,
                             f'Unknown pipeline: {pipeline_name!r}')

    # Chain: wekwos-neo requires wekwos-old output as its input
    if pipeline_name == 'wekwos-neo':
        return _run_chained(
            upstream='wekwos-old',
            downstream='wekwos-neo',
            tokens=tokens,
            context=context,
            input_form=input_form,
            trace_mode=trace_mode,
        )

    # Chain: daughter pipelines require ghandwa output as their input
    if pipeline_name == 'ghandwa-daughter-a':
        return _run_chained(
            upstream='ghandwa',
            downstream='ghandwa-daughter-a',
            tokens=tokens,
            context=context,
            input_form=input_form,
            trace_mode=trace_mode,
        )

    if pipeline_name == 'ghandwa-daughter-b':
        return _run_chained(
            upstream='ghandwa',
            downstream='ghandwa-daughter-b',
            tokens=tokens,
            context=context,
            input_form=input_form,
            trace_mode=trace_mode,
        )

    if pipeline_name == 'ghandwa-daughter-c':
        return _run_chained(
            upstream='ghandwa',
            downstream='ghandwa-daughter-c',
            tokens=tokens,
            context=context,
            input_form=input_form,
            trace_mode=trace_mode,
        )

    rules = _load_rules(pipeline_name)
    return run_pipeline(
        pipeline_name=pipeline_name,
        rules=rules,
        tokens=tokens,
        context=context,
        input_form=input_form,
        trace_mode=trace_mode,
    )


def run_all(
    tokens: list[str],
    context: Context,
    input_form: str,
    trace_mode: str = 'changed',
) -> dict[str, DerivationResult]:
    """Run all pipelines and return a dict of results keyed by pipeline name."""
    results: dict[str, DerivationResult] = {}
    for name in ALL_PIPELINES:
        import copy
        ctx_copy = copy.deepcopy(context)
        tok_copy = list(tokens)
        results[name] = run(name, tok_copy, ctx_copy, input_form, trace_mode)
    return results


# ── Internal helpers ───────────────────────────────────────────────────────────

def _run_chained(
    upstream: str,
    downstream: str,
    tokens: list[str],
    context: Context,
    input_form: str,
    trace_mode: str,
) -> DerivationResult:
    """
    Run upstream pipeline, then pass its output token stream to downstream.
    Traces from both pipelines are concatenated.
    """
    up_rules = _load_rules(upstream)
    up_result = run_pipeline(
        pipeline_name=upstream,
        rules=up_rules,
        tokens=tokens,
        context=context,
        input_form=input_form,
        trace_mode=trace_mode,
    )

    if up_result.status not in ('ok',):
        up_result.pipeline = downstream
        return up_result

    down_rules = _load_rules(downstream)
    down_result = run_pipeline(
        pipeline_name=downstream,
        rules=down_rules,
        tokens=up_result.final_tokens,
        context=context,
        input_form=input_form,
        trace_mode=trace_mode,
    )

    down_result.trace = up_result.trace + down_result.trace
    return down_result


def _not_implemented_result(pipeline_name: str, tokens: list[str], input_form: str) -> DerivationResult:
    result = DerivationResult(
        pipeline=pipeline_name,
        input_form=input_form,
        status='not_implemented',
        final_tokens=list(tokens),
    )
    result.generated_tokens = tokens_to_string(tokens)
    return result


def _error_result(pipeline_name: str, tokens: list[str], input_form: str, msg: str) -> DerivationResult:
    result = DerivationResult(
        pipeline=pipeline_name,
        input_form=input_form,
        status='error',
        final_tokens=list(tokens),
        error_type='ConfigError',
        error_message=msg,
    )
    result.generated_tokens = tokens_to_string(tokens)
    return result
