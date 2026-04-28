#!/usr/bin/env bash
# references/migrate.sh
# Run once from the repo root to restructure references/ into per-work subdirectories.
# After running: commit all changes, then confirm PDFs are gitignored before pushing.
#
# Usage:
#   cd /path/to/ghandwa
#   bash references/migrate.sh

set -e
REFS="references"

echo "=== Ghandwa references migration ==="

# ── Works with existing subdirectories: move flat PDFs in ──────────────────────
echo "Moving PDFs into existing subdirectories..."

for work in deuffic-2021 ringe-2017 swanenvleugel-2021 van-sluis-et-al-2023; do
  pdf="$REFS/$work.pdf"
  if [ -f "$pdf" ]; then
    mv "$pdf" "$REFS/$work/"
    echo "  moved $pdf → $REFS/$work/"
  else
    echo "  (skip) $pdf not found"
  fi
done

# ── Flat works: move .md and .pdf into new subdirectories ─────────────────────
echo "Moving flat works into subdirectories..."

# eska-2018
if [ -f "$REFS/eska-laryngeal-realism.md" ]; then
  cp "$REFS/eska-laryngeal-realism.md" "$REFS/eska-2018/eska-2018.md"
  rm "$REFS/eska-laryngeal-realism.md"
  echo "  moved eska-laryngeal-realism.md → eska-2018/eska-2018.md"
fi
if [ -f "$REFS/eska-laryngeal-realism.pdf" ]; then
  mv "$REFS/eska-laryngeal-realism.pdf" "$REFS/eska-2018/"
  echo "  moved eska-laryngeal-realism.pdf → eska-2018/"
fi

# matasovic-2009
if [ -f "$REFS/matasovic-2009-frontmatter.md" ]; then
  cp "$REFS/matasovic-2009-frontmatter.md" "$REFS/matasovic-2009/matasovic-2009-frontmatter.md"
  rm "$REFS/matasovic-2009-frontmatter.md"
  echo "  moved matasovic-2009-frontmatter.md → matasovic-2009/"
fi

# weiss-2020
if [ -f "$REFS/weiss-2020-p175-179.md" ]; then
  cp "$REFS/weiss-2020-p175-179.md" "$REFS/weiss-2020/weiss-2020-p175-179.md"
  rm "$REFS/weiss-2020-p175-179.md"
  echo "  moved weiss-2020-p175-179.md → weiss-2020/"
fi

# witczak-2024
if [ -f "$REFS/witczak-2024.md" ]; then
  cp "$REFS/witczak-2024.md" "$REFS/witczak-2024/witczak-2024.md"
  rm "$REFS/witczak-2024.md"
  echo "  moved witczak-2024.md → witczak-2024/"
fi
if [ -f "$REFS/witczak-2024.pdf" ]; then
  mv "$REFS/witczak-2024.pdf" "$REFS/witczak-2024/"
  echo "  moved witczak-2024.pdf → witczak-2024/"
fi

# hyllested-2010: PDF only
if [ -f "$REFS/hyllested-precursors-celtic-germanic.pdf" ]; then
  mv "$REFS/hyllested-precursors-celtic-germanic.pdf" "$REFS/hyllested-2010/"
  echo "  moved hyllested-precursors-celtic-germanic.pdf → hyllested-2010/"
fi

# ── Clean up the stub eska-2018.md written during planning ────────────────────
# (the cp above wrote the full canonical version; nothing else to clean)

echo ""
echo "=== Migration complete ==="
echo "Next steps:"
echo "  1. Verify structure:  find references -type f | sort"
echo "  2. Stage all changes: git add -A references/"
echo "  3. Commit"
echo "  4. Confirm .gitignore is active: git status | grep pdf"
