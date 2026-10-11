# Installation

Abhängigkeit: Python >= 3.9 und `markdown` (geprüft 3.11).

```
pip install markdown
```

Geprüfte Umgebung: Ubuntu 24.04, Python 3.12.3 (System), markdown 3.11, 2026-10-11.

## Haken für den automatischen Bau

Einmal je Clone, damit `docs/` bei jedem Commit mit geändertem Markdown mitkommt:

```
cp tools/general/wiki_html/src/pre-commit.sh .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
