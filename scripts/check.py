#!/usr/bin/env python3
"""Repository checks using only the Python standard library.

Use Python 3.9+. Exit codes: 0 = performed and passed, 1 = failed,
2 = a requested check was unavailable. Doctor is diagnostic and exits 0.
PASS never certifies a mathematical proof, novelty, or complete classification.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
import gzip
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parent.parent
MAIN = ROOT / "papers/nc-quadric-classification.tex"
TEX_PACKAGES = (
    "ltjsarticle.cls", "luatexja.sty", "amsmath.sty", "amssymb.sty", "amsthm.sty",
    "mathtools.sty", "geometry.sty", "booktabs.sty", "enumitem.sty", "hyperref.sty", "fix-cm.sty",
    "mathrsfs.sty", "tabularx.sty", "array.sty",
)
DISCLAIMER = "PASS covers only the stated checks; it does not certify proofs, novelty or complete H2 classification."


def selected_python() -> Path:
    return ROOT / ".venv/bin/python" if (ROOT / ".venv").is_dir() else Path(sys.executable)


def capture(command: list[str], *, timeout: int | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                          text=True, errors="replace", timeout=timeout, check=False)


def summary(name: str, failures: list[str], skipped: list[str]) -> int:
    for problem in failures:
        print(f"FAIL [{name}]: {problem}")
    for problem in skipped:
        print(f"SKIP [{name}]: {problem}")
    if failures:
        return 1
    if skipped:
        return 2
    print(f"PASS [{name}]")
    return 0


def python_dependencies() -> tuple[bool, str]:
    executable = selected_python()
    if not executable.is_file():
        return False, f"Python executable missing: {executable}"
    probe = (
        "import sys, re; "
        "assert sys.version_info >= (3,9), 'Python 3.9+ required'; "
        "import sympy; "
        "v=tuple(map(int,re.match(r'(\\d+)\\.(\\d+)',sympy.__version__).groups())); "
        "assert (1,12) <= v < (2,0), 'SymPy >=1.12,<2 required'; "
        "print('Python '+sys.version.split()[0]+'; SymPy '+sympy.__version__)"
    )
    try:
        result = capture([str(executable), "-c", probe], timeout=30)
    except (OSError, subprocess.TimeoutExpired) as exc:
        return False, f"Python dependency probe unavailable: {exc}"
    if result.returncode:
        detail = result.stdout.strip().splitlines()
        return False, detail[-1] if detail else "Python/SymPy dependency probe failed"
    return True, f"{executable}: {result.stdout.strip()}"


def missing_tex() -> list[str]:
    missing = [tool for tool in ("latexmk", "lualatex", "bibtex", "kpsewhich")
               if shutil.which(tool) is None]
    if "kpsewhich" not in missing:
        for package in TEX_PACKAGES:
            result = capture(["kpsewhich", package], timeout=30)
            if result.returncode or not result.stdout.strip():
                missing.append(package)
    return missing


def doctor() -> int:
    print(f"Repository: {ROOT}")
    print(f"Checker runtime: {sys.executable} ({sys.version.split()[0]})")
    ok, detail = python_dependencies()
    print(f"{'AVAILABLE' if ok else 'MISSING'} [math dependencies]: {detail}")
    missing = missing_tex()
    print("MISSING [build dependencies]: " + ", ".join(missing) if missing
          else "AVAILABLE [build dependencies]: commands and required TeX package files")
    for tool in ("pdfinfo", "pdftoppm"):
        print(f"{'AVAILABLE' if shutil.which(tool) else 'MISSING'} [optional PDF inspection]: {tool}")
    if shutil.which("git"):
        head = capture(["git", "rev-parse", "HEAD"])
        branch = capture(["git", "branch", "--show-current"])
        if head.returncode == 0:
            print("Git HEAD: " + head.stdout.strip())
            print("Git branch: " + (branch.stdout.strip() or "(detached HEAD)"))
        else:
            print("UNCONFIRMED: Git commit/branch metadata is unavailable.")
    else:
        print("MISSING: git; repository tracking checks cannot run.")
    print("UNCONFIRMED: remote write authentication, remote main and research-hub access; no network probe was made.")
    print("UNCONFIRMED: mathematical proofs, formal verification, rendered PDF appearance and VS Code UI.")
    print("DIAGNOSTIC ONLY: dependencies are not validation results. Continue available proof/source work.")
    return 0


def tex_without_comments(text: str) -> str:
    return re.sub(r"(?<!\\)%[^\n]*", "", text)


def prose_without_code_or_math(text: str) -> str:
    lines = []
    fence = None
    for line in text.splitlines(keepends=True):
        match = re.match(r"^ {0,3}(`{3,}|~{3,})", line)
        if fence:
            if match and match.group(1)[0] == fence[0] and len(match.group(1)) >= fence[1]:
                fence = None
            continue
        if match:
            fence = (match.group(1)[0], len(match.group(1)))
            continue
        lines.append(line)
    text = "".join(lines)
    text = re.sub(r"`+[^`\n]*`+", "", text)
    text = re.sub(r"\$\$.*?\$\$", "", text, flags=re.S)
    text = re.sub(r"\\\[.*?\\\]", "", text, flags=re.S)
    text = re.sub(r"\\\(.*?\\\)", "", text, flags=re.S)
    return re.sub(r"(?<!\\)\$(?:\\.|[^$])*?(?<!\\)\$", "", text)


def sources() -> int:
    failures: list[str] = []
    skipped: list[str] = []
    required = (
        "README.md", "AGENTS.md", "00_research_plan.md", "CLOUD_CODEX.md", "notes/research_notes.md",
        "notes/literature.md", "papers/nc-quadric-classification.tex",
        "papers/nc-quadric-moduli.tex", "papers/nc-quadric-avatar.tex", "papers/references.bib",
        "papers/quiver-avatar/as_helix_classification.tex", "papers/quiver-avatar/as10_mutation_classification.tex",
        "papers/quiver-avatar/cubic_obstruction_all_loci.tex",
        "papers/quiver-avatar/point_spectral_isogeny.tex",
        "papers/quiver-avatar/symmetric_morita_descent.tex",
        "papers/quiver-avatar/relative_serre_completion.tex",
        "papers/quiver-avatar/spectral_atkin_lehner.tex",
        "papers/quiver-avatar/spectral_relative_correspondence.tex",
        "papers/quiver-avatar/torsion_free_spectral_recognition.tex",
        "computations/verify_symmetric_morita.py",
        "computations/verify_spectral_atkin_lehner.py",
        "computations/verify_as_avatar_euler.py",
        "computations/verify_avatar_cubic_obstruction.py",
        "computations/verify_quadric.py", "computations/verify_pencil_tangent.py",
        "computations/verify_reducible_quadruples.py", "computations/verify_noncubic_antiserre_pivots.py",
        "requirements.txt", ".latexmkrc",
        ".vscode/settings.json", ".vscode/extensions.json", "scripts/bootstrap.sh", "scripts/check.py",
    )
    for name in required:
        if not (ROOT / name).is_file():
            failures.append(f"required file missing: {name}")

    labels: dict[str, list[str]] = defaultdict(list)
    references: list[tuple[str, str]] = []
    citations: list[tuple[str, str]] = []
    visited: set[Path] = set()

    def read_tex(path: Path) -> None:
        path = path.resolve()
        if path in visited or not path.is_file():
            return
        visited.add(path)
        display = str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path)
        original = path.read_text(encoding="utf-8")
        for target in re.findall(r"^\s*%\s*!TeX\s+root\s*=\s*(.+)$", original, flags=re.M | re.I):
            root_target = (path.parent / target.strip()).resolve()
            if not root_target.is_file():
                failures.append(f"{display}: missing TeX root {target.strip()}")
            elif root_target != MAIN.resolve():
                failures.append(f"{display}: TeX root does not point to the selected manuscript: {target.strip()}")
        text = tex_without_comments(original)
        # Guard against pasting Markdown and Unicode maths into paper C.
        # The latter can trigger "Missing $ inserted" at an unescaped underscore.
        if MAIN.name == "nc-quadric-avatar.tex":
            for lineno, line in enumerate(text.splitlines(), 1):
                if re.search(r"\*\*[^*\n]+\*\*", line):
                    failures.append(f"{display}:{lineno}: Markdown bold in LaTeX; use \\textbf{{...}}")
                if re.search(r"[∈≠≤≥→←↔]|Σ₂|Pic⁰|χ\s*=", line):
                    failures.append(f"{display}:{lineno}: Unicode maths; use TeX math mode")
        for label in re.findall(r"\\label\{([^}]+)\}", text):
            labels[label].append(display)
        for refs in re.findall(r"\\(?:ref|eqref|pageref|autoref|cref|Cref)\{([^}]+)\}", text):
            references.extend((ref.strip(), display) for ref in refs.split(","))
        for keys in re.findall(r"\\[A-Za-z]*cite[A-Za-z]*\*?\s*(?:\[[^\]]*\]\s*)*\{([^}]+)\}", text):
            citations.extend((key.strip(), display) for key in keys.split(",") if key.strip() != "*")
        for targets in re.findall(r"\\bibliography\{([^}]+)\}", text):
            for target in targets.split(","):
                bib_input = MAIN.parent / target.strip()
                if not bib_input.suffix:
                    bib_input = bib_input.with_suffix(".bib")
                if not bib_input.is_file():
                    failures.append(f"{display}: missing bibliography input {target.strip()}")
        for target in re.findall(r"\\(?:input|include)\{([^}]+)\}", text):
            if "\\" in target or "#" in target:
                skipped.append(f"{display}: dynamic TeX input not resolved: {target}")
                continue
            # latexmk changes directory to papers/, including for nested inputs.
            included = MAIN.parent / target
            if not included.suffix:
                included = included.with_suffix(".tex")
            if not included.is_file():
                failures.append(f"{display}: missing input {target}")
            else:
                read_tex(included)

    read_tex(MAIN)
    for label, locations in labels.items():
        if len(locations) > 1:
            failures.append(f"duplicate label {label}: {', '.join(locations)}")
    for label, location in references:
        if label not in labels:
            failures.append(f"{location}: undefined label {label}")
    bibliography = ROOT / "papers/references.bib"
    if bibliography.is_file():
        keys = set(re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,", bibliography.read_text(encoding="utf-8")))
        for key, location in citations:
            if key not in keys:
                failures.append(f"{location}: undefined citation {key}")
    for name in (".vscode/settings.json", ".vscode/extensions.json"):
        path = ROOT / name
        if path.is_file():
            try:
                value = json.loads(path.read_text(encoding="utf-8"))
                if not isinstance(value, dict):
                    failures.append(f"{name}: expected a JSON object")
            except (ValueError, OSError) as exc:
                failures.append(f"{name}: invalid JSON ({exc})")

    markdown_files = sorted(ROOT.glob("*.md")) + sorted((ROOT / "notes").rglob("*.md"))
    for path in markdown_files:
        text = prose_without_code_or_math(path.read_text(encoding="utf-8"))
        for match in re.finditer(r"!?\[[^\]\n]*\]\(\s*(?:<([^>]+)>|([^\s)]+))(?:\s+[^)]*)?\)", text):
            target = match.group(1) or match.group(2)
            parts = urlsplit(target)
            if parts.scheme or parts.netloc or not parts.path:
                continue
            destination = path.parent / unquote(parts.path)
            if not destination.exists():
                failures.append(f"{path.relative_to(ROOT)}: missing local link target {target}")

    if shutil.which("git") is None:
        skipped.append("git unavailable: tracked PDFs/workflows and diff whitespace not checked")
    else:
        tracked = capture(["git", "ls-files", "-z"])
        if tracked.returncode:
            skipped.append("Git tracking metadata unavailable: tracked PDFs/workflows not checked")
        else:
            for name in tracked.stdout.split("\0"):
                if name.lower().endswith(".pdf") or name.startswith(".github/workflows/"):
                    failures.append(f"forbidden tracked generated file/workflow: {name}")
            whitespace = capture(["git", "diff", "--check"])
            if whitespace.returncode:
                failures.append("git diff --check: " + whitespace.stdout.strip())
            staged = capture(["git", "diff", "--cached", "--check"])
            if staged.returncode:
                failures.append("git diff --cached --check: " + staged.stdout.strip())
    print(f"Source scope: {len(visited)} manuscript files, {len(labels)} labels, {len(citations)} citation uses; "
          f"{len(markdown_files)} Markdown files. Web URLs and VS Code UI were not tested.")
    return summary("sources", failures, skipped)


def math_checks() -> int:
    ok, detail = python_dependencies()
    if not ok:
        return summary("math", [], [detail])
    scripts = ("verify_quadric.py", "verify_pencil_tangent.py", "verify_reducible_quadruples.py", "verify_five_window_terminal.py", "verify_stack_symmetries.py", "verify_noncubic_antiserre_pivots.py",
               "verify_quiver_avatar_charts.py", "verify_quadric_first_order_roots.py",
               "verify_noncubic_gale_root.py", "verify_noncubic_central_hull.py",
               "verify_lagrangian_recognition.py", "verify_clifford_pbw.py",
               "verify_ou_fourfold.py", "verify_ou_spectral_halving.py",
               "verify_ou_hodge_ruling.py", "verify_ou_quintuple_inertia.py",
               "verify_ou_special_reflection.py", "verify_ou_cm_automorphisms.py",
               "verify_cubic_geometric_adjugate.py",
               "verify_avatar_pointed_dictionary.py",
               "verify_noncubic_pointed_end.py",
               "verify_symmetric_morita.py",
               "verify_spectral_atkin_lehner.py",
               "verify_noncubic_root_descent.py",
               "verify_avatar_morita_weights.py",
               "verify_half_period_fourfold.py",
               "verify_half_period_monodromy.py",
               "verify_ou_half_common_incidence.py",
               "verify_rootpair_resolvent_spectral.py",
               "verify_as_avatar_euler.py", "verify_avatar_cubic_obstruction.py", "verify_nodal_exceptional_parity.py",
               "verify_noncubic_boundary.py")
    failures = []
    print(f"Running exact finite checks with {detail}", flush=True)
    for name in scripts:
        script = ROOT / "computations" / name
        if not script.is_file():
            failures.append(f"computations/{name} is missing")
            continue
        result = subprocess.run([str(selected_python()), str(script)], cwd=ROOT, check=False)
        if result.returncode:
            failures.append(f"{name} exited {result.returncode}")
    return summary("math", failures, [])


def build() -> int:
    missing = missing_tex()
    if missing:
        return summary("build", [], ["missing dependencies: " + ", ".join(missing)])
    result = capture(["latexmk", "-norc", "-r", str(ROOT / ".latexmkrc"), str(MAIN)])
    if result.returncode:
        print("\n".join(result.stdout.splitlines()[-35:]))
        return summary("build", [f"latexmk exited {result.returncode}"], [])
    failures = []
    pdf = ROOT / "build" / f"{MAIN.stem}.pdf"
    sync = ROOT / "build" / f"{MAIN.stem}.synctex.gz"
    log = ROOT / "build" / f"{MAIN.stem}.log"
    if not pdf.is_file() or pdf.stat().st_size == 0:
        failures.append("expected PDF missing or empty")
    else:
        with pdf.open("rb") as handle:
            if handle.read(5) != b"%PDF-":
                failures.append("PDF header is invalid")
    if not sync.is_file():
        failures.append("expected SyncTeX file missing")
    else:
        try:
            with gzip.open(sync, "rb") as handle:
                if not handle.readline().startswith(b"SyncTeX Version:"):
                    failures.append("SyncTeX header is invalid")
        except (OSError, EOFError) as exc:
            failures.append(f"SyncTeX gzip unreadable: {exc}")
    if not log.is_file():
        failures.append("final LaTeX log missing")
    else:
        warnings = [line.strip() for line in log.read_text(encoding="utf-8", errors="replace").splitlines()
                    if re.search(r"Warning|Undefined control sequence|Missing character:|"
                                 r"(?:Over|Under)full \\[hv]box|undefined (?:references|citations)", line)]
        failures.extend("final log: " + warning for warning in warnings)
    print("latexmk completed; up-to-date outputs may have been reused. "
          "PDF/SyncTeX presence and final log checked; rendered pages and VS Code UI were not inspected.")
    return summary("build", failures, [])



def cross_paper_labels() -> int:
    """Audit named A/B/C cross-paper citations without needing .aux files."""
    failures: list[str] = []
    roots = {
        "QuadricIntrinsic2026": ROOT / "papers/nc-quadric-classification.tex",
        "QuadricModuli2026": ROOT / "papers/nc-quadric-moduli.tex",
        "QuiverAvatarModuli2026": ROOT / "papers/nc-quadric-avatar.tex",
    }
    sources_by_key: dict[str, dict[Path, str]] = {}
    labels_by_key: dict[str, set[str]] = {}

    for key, main in roots.items():
        sources: dict[Path, str] = {}

        def visit(path: Path) -> None:
            path = path.resolve()
            if path in sources:
                return
            if not path.is_file():
                failures.append(f"{key}: missing input {path}")
                return
            text = tex_without_comments(path.read_text(encoding="utf-8"))
            sources[path] = text
            for target in re.findall(r"\\(?:input|include)\{([^}]+)\}", text):
                if "\\" in target or "#" in target:
                    failures.append(f"{key}: dynamic input cannot be audited: {target}")
                    continue
                child = main.parent / target
                if not child.suffix:
                    child = child.with_suffix(".tex")
                visit(child)

        visit(main)
        sources_by_key[key] = sources
        labels_by_key[key] = {
            label
            for text in sources.values()
            for label in re.findall(r"\\label\{([^}]+)\}", text)
        }

    count = 0
    for origin, sources in sources_by_key.items():
        for path, text in sources.items():
            for label, target in re.findall(
                r"\\cite\[\s*\\texttt\{([^}]+)\}\s*\]\{(QuadricIntrinsic2026|QuadricModuli2026|QuiverAvatarModuli2026)\}",
                text,
            ):
                if target == origin:
                    failures.append(f"{path.relative_to(ROOT)}: self-citation for {label}")
                elif label not in labels_by_key[target]:
                    failures.append(f"{path.relative_to(ROOT)}: cited label {label} absent in {target}")
                count += 1

    print(
        "Cross-paper scope: "
        f"A={len(sources_by_key['QuadricIntrinsic2026'])} TeX files, "
        f"B={len(sources_by_key['QuadricModuli2026'])} TeX files, "
        f"C={len(sources_by_key['QuiverAvatarModuli2026'])} TeX files, "
        f"{count} explicit named cross-paper citation uses."
    )
    return summary("cross-paper labels", failures, [])


def papers() -> int:
    """Check the source graph of A, B and C separately, without compiling them."""
    global MAIN
    original = MAIN
    results: list[int] = []
    try:
        for manuscript in (
            "nc-quadric-classification.tex",
            "nc-quadric-moduli.tex",
            "nc-quadric-avatar.tex",
        ):
            MAIN = ROOT / "papers" / manuscript
            print(f"\nSOURCE AUDIT: {MAIN.relative_to(ROOT)}", flush=True)
            results.append(sources())
    finally:
        MAIN = original
    results.append(cross_paper_labels())
    return 1 if 1 in results else 2 if 2 in results else 0


def main() -> int:
    global MAIN
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("doctor", "sources", "papers", "math", "build", "all"))
    parser.add_argument("--manuscript", default="papers/nc-quadric-classification.tex",
                        help="main TeX file directly under papers/ (default: primary manuscript)")
    args = parser.parse_args()
    selected = (ROOT / args.manuscript).resolve()
    if selected.parent != (ROOT / "papers").resolve() or selected.suffix != ".tex" or not selected.is_file():
        parser.error("--manuscript must name an existing main .tex file directly under papers/")
    MAIN = selected
    commands = {"doctor": doctor, "sources": sources, "papers": papers, "math": math_checks, "build": build}
    results = []
    names = ("sources", "math", "build") if args.command == "all" else (args.command,)
    for name in names:
        try:
            code = commands[name]()
        except (OSError, ValueError, subprocess.SubprocessError) as exc:
            code = summary(name, [f"check could not complete: {exc}"], [])
        results.append(code)
    if args.command != "doctor":
        print(DISCLAIMER)
    return 1 if 1 in results else 2 if 2 in results else 0


if __name__ == "__main__":
    raise SystemExit(main())
