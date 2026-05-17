"""
Pipeline registry and chaining logic.

Registered pipelines:
  ghandwa         — implemented
  old-wekwos      — implemented (provisional)
  neo-wekwos      — implemented (provisional); downstream of old-wekwos
  proto-anatolian — implemented
  proto-seldanic  — implemented
  daughter-a/b/c  — not_implemented stubs

Pipeline chaining:
  Neo-Wékʷos is downstream of Old Wékʷos. Its input token stream is the final
  output of the Old Wékʷos pipeline. Re-tokenization does not occur.

  The daughter-language input token stream source is unresolved. Daughter pipelines
  currently accept raw PIE-derived token input (same as ghandwa/old-wekwos).
  This must be revisited before any daughter pipeline is implemented.

Unresolved decisions (flagged per spec):
  - Daughter-language names not finalized.
  - Daughter-language input token stream source unresolved.
  - Late Ghandwa not stubbed; its role is unresolved.
"""

from __future__ import annotations

from .rule import Rule, Context, DerivationResult, run_pipeline
from .tokenize import tokens_to_string


# ── Pipeline registry ──────────────────────────────────────────────────────────

_IMPLEMENTED = {'ghandwa', 'old-wekwos', 'neo-wekwos', 'proto-anatolian', 'proto-seldanic'}
_NOT_IMPLEMENTED = {'daughter-a', 'daughter-b', 'daughter-c'}
ALL_PIPELINES = sorted(_IMPLEMENTED | _NOT_IMPLEMENTED)


def _load_rules(name: str) -> list[Rule]:
    """Lazy-load rules for a named pipeline to avoid import-time side effects."""
    if name == 'ghandwa':
        from .pipelines.ghandwa import RULES
        return RULES
    if name == 'old-wekwos':
        from .pipelines.old_wekwos import RULES
        return RULES
    if name == 'neo-wekwos':
        from .pipelines.neo_wekwos import RULES
        return RULES
    if name == 'proto-anatolian':
        from .pipelines.proto_anatolian import RULES
        return RULES
    if name == 'proto-seldanic':
        from .pipelines.proto_seldanic import RULES
        return RULES
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
      - neo-wekwos chaining → runs old-wekwos first, then neo-wekwos rules
      - all other pipelines → runs rules directly
    """
    if pipeline_name in _NOT_IMPLEMENTED:
        return _not_implemented_result(pipeline_name, tokens, input_form)

    if pipeline_name not in _IMPLEMENTED:
        return _error_result(pipeline_name, tokens, input_form,
                             f'Unknown pipeline: {pipeline_name!r}')

    # Chain: neo-wekwos requires old-wekwos output as its input
    if pipeline_name == 'neo-wekwos':
        return _run_chained(
            upstream='old-wekwos',
            downstream='neo-wekwos',
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
        # Each pipeline gets its own copy of context and tokens
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
        # Upstream blocked or errored — propagate
        up_result.pipeline = downstream  # relabel as the downstream pipeline
        return up_result

    # Chain: pass upstream's final tokens into downstream rules
    down_rules = _load_rules(downstream)
    down_result = run_pipeline(
        pipeline_name=downstream,
        rules=down_rules,
        tokens=up_result.final_tokens,
        context=context,
        input_form=input_form,
        trace_mode=trace_mode,
    )

    # Merge traces: upstream first, then downstream
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
