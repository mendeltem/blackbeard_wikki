"""Baut eine kleine synthetische Wiki und prüft Seiten und Links. Aufruf: python test_build.py"""
import re, sys, tempfile
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
import wiki_html

def make_wiki(root: Path):
    (root / "knowledge/demo/findings").mkdir(parents=True)
    (root / "knowledge/demo/rules").mkdir()
    (root / "tools/general/x/src").mkdir(parents=True)
    (root / "updates").mkdir()
    (root / "README.md").write_text("# Regeln\n\nSiehe [INDEX](INDEX.md).\n")
    (root / "INDEX.md").write_text("# Wiki\n\n[knowledge](knowledge/INDEX.md)\n")
    (root / "TODO.md").write_text("# TODO\n\n- [x](knowledge/demo/findings/a.md)\n")
    (root / "updates/LOG.md").write_text("# Log\n\n- 2026-10-11 | test | `knowledge/demo/` | Eintrag\n")
    (root / "knowledge/INDEX.md").write_text("# knowledge\n\n| Thema | Inhalt | Stichwörter | Kurzstand |\n|---|---|---|---|\n| [demo](demo/INDEX.md) | Probe | eins, zwei | [SUMMARY](demo/SUMMARY.md) |\n")
    (root / "knowledge/demo/INDEX.md").write_text("# demo\n\nEinleitung.\n\n| Typ | Eintrag | Inhalt | Status |\n|---|---|---|---|\n| befund | [a](findings/a.md) | Inhalt von a | getragen |\n| regel | [r](rules/r.md) | Inhalt von r | vorschlag |\n")
    (root / "knowledge/demo/SUMMARY.md").write_text("# demo: Kurzstand\n\nKurz. Siehe [a](findings/a.md) und [Regeln](../../README.md).\n")
    (root / "knowledge/demo/findings/a.md").write_text("---\nid: a\ntyp: befund\nstatus: getragen\nthema: knowledge/demo\nstand: 2026-10-11\nherkunft: Test\nverweist_auf: [r, fehlt]\n---\n\n# Befund A\n\n## Aussage\nZahl 0,5 mit [Regel](../rules/r.md) und [Quelle](../../../tools/general/x/src/x.py).\n")
    (root / "knowledge/demo/rules/r.md").write_text("---\nid: r\ntyp: regel\nstatus: vorschlag\nthema: knowledge/demo\nstand: 2026-10-10\nherkunft: Test\nverweist_auf: []\n---\n\n# Regel R\n\n## Aussage\nText.\n")
    (root / "tools/INDEX.md").write_text("# tools\n\n| Ordner | Inhalt |\n|---|---|\n| [general/](general/INDEX.md) | allg |\n")
    (root / "tools/general/INDEX.md").write_text("# general\n\n| Tool | Zweck |\n|---|---|\n| [x/](x/README.md) | x |\n")
    (root / "tools/general/x/README.md").write_text("---\nid: x\n---\n\n# Werkzeug X\n\nSiehe [INSTALL](INSTALL.md).\n")
    (root / "tools/general/x/INSTALL.md").write_text("# Installation\n\nnichts.\n")
    (root / "tools/general/x/src/x.py").write_text("print(1)\n")

def main():
    with tempfile.TemporaryDirectory() as d:
        root, out = Path(d) / "wiki", Path(d) / "docs"
        root.mkdir(); make_wiki(root)
        assert wiki_html.main(["--root", str(root), "--out", str(out)]) == 0
        for p in ["index.html", "demo/index.html", "demo/findings/a.html", "demo/rules/r.html",
                  "tools/index.html", "tools/general/x/index.html", "tools/general/x/install.html",
                  "rules.html", "todo.html", "log.html", "search.js", "index.json"]:
            assert (out / p).exists(), p
        dead = []
        for p in out.rglob("*.html"):
            for href in re.findall(r'href="([^"]+)"', p.read_text()):
                if re.match(r"^(https?:|mailto:|#)", href):
                    continue
                if not (p.parent / href.split("#")[0]).resolve().exists():
                    dead.append((p.name, href))
        assert not dead, dead
        a = (out / "demo/findings/a.html").read_text()
        assert 'href="../rules/r.html"' in a, "Link auf Regel nicht umgeschrieben"
        assert "github.com" in a and "x.py" in a, "Quelltext-Link nicht auf GitHub"
        assert "Verwiesen von" in (out / "demo/rules/r.html").read_text(), "Rückverweis fehlt"
        assert "Inhalt von a" in (out / "demo/index.html").read_text()
        assert '"id": "a"' in (out / "index.json").read_text()
        print("test_build: bestanden")

if __name__ == "__main__":
    main()
