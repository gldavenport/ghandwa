"""
Entry point for python -m pie_transformer.

Called with arguments → CLI mode (existing subcommands: form, batch,
extract-lexicon, paradigm).
Called with no arguments → interactive menu.
"""

import sys

if __name__ == '__main__':
    if len(sys.argv) == 1:
        from .interactive import run_interactive
        run_interactive()
    else:
        from .cli import main
        sys.exit(main())
