#!/usr/bin/env bash
# pre-commit: Markdown geändert -> docs/ neu bauen und mit einchecken.
set -e
root=$(git rev-parse --show-toplevel)
if git diff --cached --name-only | grep -qE '\.md$'; then
  python3 "$root/tools/general/wiki_html/src/wiki_html.py" --root "$root" --out "$root/docs" >/dev/null
  git -C "$root" add docs
fi
