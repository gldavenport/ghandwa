"""
Interactive menu for the Ghandwa Toolkit.

Entered automatically when `python -m pie_transformer` is called with no
arguments. All existing CLI subcommands (form, batch, extract-lexicon,
paradigm) remain available when arguments are passed.
"""

from __future__ import annotations
import os
import sys


_BANNER = """\
╔══════════════════════════════════╗
║        Ghandwa Toolkit           ║
╠══════════════════════════════════╣
║  1  Transform PIE form           ║
║  2  Noun paradigm                ║
║  3  Verb paradigm   [stub]       ║
║  4  Batch transform  →  CLI      ║
║  q  Quit                         ║
╚══════════════════════════════════╝"""


def run_interactive() -> None:
    """Drop into the interactive toolkit menu."""
    while True:
        _clear()
        print(_BANNER)
        choice = input('\n> ').strip().lower()

        if choice == '1':
            _menu_transform()
        elif choice == '2':
            _menu_noun_paradigm()
        elif choice == '3':
            _menu_verb_stub()
        elif choice == '4':
            _menu_batch_info()
        elif choice in ('q', 'quit', 'exit', '5'):
            print('Goodbye.')
            break
        else:
            input('Unknown option. Press Enter to continue.')


# ── Shared UI helpers ──────────────────────────────────────────────────────────

def _clear() -> None:
    os.system('clear')


def _submenu(options: list, back_label: str = 'Back to menu') -> str:
    """Display a numbered submenu and return the chosen key.

    Args:
        options: List of (key, label) pairs. Keys must be unique strings.
        back_label: Label for the q / back option.

    Returns:
        The key of the chosen option, or 'q' if back/quit was selected.
    """
    print()
    for i, (_, label) in enumerate(options, 1):
        print(f'  {i}  {label}')
    print(f'  q  {back_label}')

    choice = input('\n> ').strip().lower()

    if choice in ('q', 'quit', 'back', ''):
        return 'q'
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(options):
            return options[idx][0]
    except ValueError:
        pass
    for key, _ in options:
        if choice == key:
            return key
    return 'q'


def _pick_from_list(title: str, items: list, default=None):
    """Present a numbered list and return the chosen item or default on cancel."""
    print(f'\n{title}')
    for i, item in enumerate(items, 1):
        marker = '  *' if item == default else '   '
        print(f'{marker} {i}  {item}')
    print('    q  Cancel')

    choice = input('\n> ').strip().lower()
    if choice in ('q', ''):
        return default
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(items):
            return items[idx]
    except ValueError:
        if choice in items:
            return choice
    return default


def _prompt(label: str, default: str = '') -> str:
    if default:
        val = input(f'{label} [{default}]: ').strip()
        return val or default
    return input(f'{label}: ').strip()


def _save_markdown(content: str, default_stem: str) -> None:
    safe = default_stem.replace('*', '').replace(' ', '-')
    default_name = f'paradigm-{safe}.md'
    fname = _prompt('Filename', default=default_name)
    with open(fname, 'w', encoding='utf-8') as fh:
        fh.write(content)
    print(f'\nSaved to {fname}')
    input('Press Enter to continue.')


# ── Transform ──────────────────────────────────────────────────────────────────

def _run_transform(pie_form: str, pipeline: str, trace):
    from pie_core.normalize import normalize
    from pie_core.tokenize import tokenize, accent_char_pos_to_token_index
    from .rule import Context
    from .pipeline import run
    from .render import render

    norm = normalize(pie_form)
    tokens, char_offsets = tokenize(norm.clean)
    accent_index = accent_char_pos_to_token_index(norm.accent_char_pos, tokens, char_offsets)
    ctx = Context(accent_index=accent_index)
    result = run(pipeline, tokens, ctx, pie_form, trace_mode=trace)
    result.generated_orth     = render(pipeline, 'orth',     result.final_tokens, result.final_accent_index)
    result.generated_citation = render(pipeline, 'citation', result.final_tokens, result.final_accent_index)
    result.generated_ipa      = render(pipeline, 'ipa',      result.final_tokens, result.final_accent_index)
    return result


def _menu_transform() -> None:
    from .pipeline import ALL_PIPELINES
    from .reports import format_terminal

    _clear()
    print('── Transform PIE form ──────────────────\n')

    pie_form = _prompt('PIE form (e.g. *wĺ̥kʷos)')
    if not pie_form:
        return

    pipeline = _pick_from_list('Pipeline:', sorted(ALL_PIPELINES), default='ghandwa') or 'ghandwa'
    trace = 'changed'
    mode = 'orth'

    while True:
        _clear()
        print(f'── Transform: {pie_form}  [{pipeline}] ──\n')
        try:
            result = _run_transform(pie_form, pipeline, trace)
            print(format_terminal(result, mode=mode, show_trace=trace in ('changed', 'full')))
        except Exception as exc:
            print(f'Error: {exc}')
            input('\nPress Enter to return to menu.')
            return

        action = _submenu([
            ('pipeline', 'Change pipeline'),
            ('trace',    f'Change trace  (current: {trace or "none"})'),
            ('mode',     f'Toggle output mode  (current: {mode})'),
            ('save',     'Save as markdown'),
        ])

        if action == 'q':
            return
        elif action == 'pipeline':
            pipeline = _pick_from_list('Pipeline:', sorted(ALL_PIPELINES), default=pipeline) or pipeline
        elif action == 'trace':
            t = _pick_from_list('Trace level:', ['none', 'changed', 'full'], default=trace or 'none') or 'none'
            trace = None if t == 'none' else t
        elif action == 'mode':
            mode = _pick_from_list('Output mode:', ['orth', 'citation', 'ipa', 'tokens'], default=mode) or mode
        elif action == 'save':
            md = format_terminal(result, mode=mode, show_trace=True)
            _save_markdown(md, default_stem=pie_form)


# ── Noun paradigm ──────────────────────────────────────────────────────────────

def _menu_noun_paradigm() -> None:
    from .paradigm_noun import generate, format_table, format_markdown

    def _get_result():
        _clear()
        print('── Noun paradigm ───────────────────────\n')
        print('Auto-detects: ā-stem, o-stem m/n, i-stem, u-stem m/f/n, s-stem.')
        print('Enter Ghandwa orthography with accent marks.\n')
        nom_sg = _prompt('nom.sg')
        if not nom_sg:
            return None
        gen_sg = _prompt('gen.sg')
        if not gen_sg:
            return None
        try:
            return generate(nom_sg, gen_sg)
        except ValueError as exc:
            print(f'\nError: {exc}')
            input('\nPress Enter to return to menu.')
            return None

    result = _get_result()
    if result is None:
        return

    show_ipa = False

    while True:
        _clear()
        print(format_table(result, show_ipa=show_ipa))

        action = _submenu([
            ('ipa',      f'{"Hide" if show_ipa else "Show"} ending IPA'),
            ('markdown', 'Save as markdown'),
            ('new',      'New paradigm'),
        ])

        if action == 'q':
            return
        elif action == 'ipa':
            show_ipa = not show_ipa
        elif action == 'markdown':
            _save_markdown(format_markdown(result), default_stem=result.lemma)
        elif action == 'new':
            show_ipa = False
            result = _get_result()
            if result is None:
                return


# ── Stubs & info ───────────────────────────────────────────────────────────────

def _menu_verb_stub() -> None:
    _clear()
    print('── Verb paradigm ───────────────────────\n')
    print('Not yet implemented.')
    print('Verb paradigm tables are under construction (grammar/verbs.md).')
    input('\nPress Enter to return to menu.')


def _menu_batch_info() -> None:
    _clear()
    print('── Batch transform ─────────────────────\n')
    print('Batch transform is CLI-only.\n')
    print('Usage:')
    print('  python -m pie_transformer batch <input.tsv> --pipeline ghandwa --out <output.tsv>\n')
    print('See:  python -m pie_transformer batch --help')
    input('\nPress Enter to return to menu.')
