#!/usr/bin/env bash
# Best-effort dependency setup. A PARTIAL environment still permits research.
# Exit 0 means this diagnostic/setup pass finished, not that all checks passed.
set -u

quadric_script_dir=${BASH_SOURCE[0]%/*}
[[ "$quadric_script_dir" == "${BASH_SOURCE[0]}" ]] && quadric_script_dir=.
quadric_root=$(cd -- "$quadric_script_dir/.." && pwd -P) || exit 1
quadric_with_tex=0
for quadric_arg in "$@"; do
    case "$quadric_arg" in
        --with-tex) quadric_with_tex=1 ;;
        -h|--help)
            printf '%s\n' 'Usage: bash scripts/bootstrap.sh [--with-tex]' \
                'Reuse a working Python/SymPy; otherwise try a repository .venv.' \
                '--with-tex permits apt installation on Debian/Ubuntu with existing root or sudo -n access.' \
                'Missing dependencies are reported as PARTIAL; proof and source work can continue.'
            exit 0 ;;
        *) printf 'Unknown option: %s\n' "$quadric_arg" >&2; exit 1 ;;
    esac
done

quadric_python_ok() {
    [[ -x "$1" ]] && "$1" -c 'import sys; raise SystemExit(sys.version_info < (3, 9))' >/dev/null 2>&1
}

quadric_sympy_ok() {
    "$1" -c 'import re, sympy; v=tuple(map(int,re.match(r"(\d+)\.(\d+)",sympy.__version__).groups())); raise SystemExit(not ((1,12) <= v < (2,0)))' >/dev/null 2>&1
}

quadric_python=
quadric_partial=0
if [[ -d "$quadric_root/.venv" ]]; then
    if quadric_python_ok "$quadric_root/.venv/bin/python"; then
        quadric_python="$quadric_root/.venv/bin/python"
    else
        printf '%s\n' 'PARTIAL: existing .venv has no usable Python 3.9+; it was left unchanged.'
        quadric_partial=1
    fi
else
    quadric_fallback_python=
    for quadric_candidate in "${QUADRIC_PYTHON:-}" "$(command -v python3 || :)" \
        "${CODEX_PRIMARY_RUNTIME_PYTHON:-}" "$(command -v python || :)"; do
        if [[ -n "$quadric_candidate" ]] && quadric_python_ok "$quadric_candidate"; then
            [[ -n "$quadric_fallback_python" ]] || quadric_fallback_python=$quadric_candidate
            if quadric_sympy_ok "$quadric_candidate"; then
                quadric_python=$quadric_candidate
                break
            fi
        fi
    done
    [[ -n "$quadric_python" ]] || quadric_python=$quadric_fallback_python
fi

if [[ -n "$quadric_python" ]]; then
    if ! quadric_sympy_ok "$quadric_python"; then
        if [[ ! -d "$quadric_root/.venv" ]]; then
            printf '%s\n' 'SETUP: creating .venv with access to installed site packages.'
            if ! "$quadric_python" -m venv --system-site-packages "$quadric_root/.venv"; then
                printf '%s\n' 'PARTIAL: venv creation failed; no system Python packages were changed.'
                quadric_partial=1
            fi
        fi
        if quadric_python_ok "$quadric_root/.venv/bin/python"; then
            quadric_python="$quadric_root/.venv/bin/python"
            if ! quadric_sympy_ok "$quadric_python"; then
                printf '%s\n' 'SETUP: trying the declared requirements once in .venv.'
                if ! "$quadric_python" -m pip install --disable-pip-version-check \
                    --no-input --retries 1 --timeout 15 -r "$quadric_root/requirements.txt"; then
                    printf '%s\n' 'PARTIAL: requirements could not be installed; continue proof/source work.'
                    quadric_partial=1
                fi
            fi
        fi
    fi
    if quadric_sympy_ok "$quadric_python"; then
        printf 'AVAILABLE: Python/SymPy via %s\n' "$quadric_python"
        "$quadric_python" -c 'import sys, sympy; print("Python",sys.version.split()[0],"; SymPy",sympy.__version__)'
    else
        printf '%s\n' 'PARTIAL: SymPy >=1.12,<2 is unavailable; exact calculations remain unrun.'
        quadric_partial=1
    fi
else
    printf '%s\n' 'PARTIAL: Python 3.9+ is unavailable; proof and TeX-source work can continue.'
    quadric_partial=1
fi

quadric_tex_packages=(ltjsarticle.cls luatexja.sty amsmath.sty amssymb.sty amsthm.sty \
    mathtools.sty geometry.sty booktabs.sty enumitem.sty hyperref.sty fix-cm.sty)
quadric_tex_ok() {
    local quadric_tool quadric_package
    for quadric_tool in latexmk lualatex bibtex kpsewhich; do
        command -v "$quadric_tool" >/dev/null 2>&1 || return 1
    done
    for quadric_package in "${quadric_tex_packages[@]}"; do
        kpsewhich "$quadric_package" >/dev/null 2>&1 || return 1
    done
}
quadric_poppler_ok() {
    command -v pdftoppm >/dev/null 2>&1 && command -v pdfinfo >/dev/null 2>&1
}

if [[ $quadric_with_tex == 1 ]] && { ! quadric_tex_ok || ! quadric_poppler_ok; }; then
    quadric_os_id=
    if [[ -r /etc/os-release ]]; then
        while IFS='=' read -r quadric_key quadric_value; do
            if [[ "$quadric_key" == ID ]]; then
                quadric_os_id=${quadric_value#\"}
                quadric_os_id=${quadric_os_id%\"}
            fi
        done < /etc/os-release
    fi
    quadric_privilege=()
    quadric_can_install=0
    if [[ "$quadric_os_id" == debian || "$quadric_os_id" == ubuntu ]] && command -v apt-get >/dev/null 2>&1; then
        if [[ $EUID == 0 ]]; then
            quadric_can_install=1
        elif command -v sudo >/dev/null 2>&1 && sudo -n true >/dev/null 2>&1; then
            quadric_privilege=(sudo -n)
            quadric_can_install=1
        fi
    fi
    if [[ $quadric_can_install == 1 ]]; then
        printf '%s\n' 'SETUP: trying Debian/Ubuntu TeX and Poppler packages with existing privileges.'
        if "${quadric_privilege[@]}" env DEBIAN_FRONTEND=noninteractive apt-get \
            -o Acquire::Retries=1 -o Acquire::http::Timeout=20 -o Acquire::https::Timeout=20 update; then
            if ! "${quadric_privilege[@]}" env DEBIAN_FRONTEND=noninteractive apt-get \
                -o Acquire::Retries=1 -o Acquire::http::Timeout=20 -o Acquire::https::Timeout=20 \
                install -y --no-install-recommends latexmk texlive-luatex texlive-lang-japanese \
                texlive-latex-extra texlive-fonts-recommended poppler-utils; then
                printf '%s\n' 'PARTIAL: TeX/Poppler package installation failed; existing sources are preserved.'
            fi
        else
            printf '%s\n' 'PARTIAL: package index refresh failed; no further package attempt was made.'
        fi
    else
        printf '%s\n' 'PARTIAL: --with-tex needs Debian/Ubuntu apt and existing root or noninteractive sudo access.'
    fi
fi

if quadric_tex_ok; then
    printf '%s\n' 'AVAILABLE: LuaLaTeX, latexmk, BibTeX and the required TeX packages.'
else
    printf '%s\n' 'PARTIAL: TeX dependencies are missing; manuscript editing can continue without a build claim.'
    quadric_partial=1
fi
if quadric_poppler_ok; then
    printf '%s\n' 'AVAILABLE: Poppler PDF inspection/rendering commands.'
else
    printf '%s\n' 'PARTIAL: Poppler is missing; PDF image inspection is not available through these commands.'
    quadric_partial=1
fi
if [[ $quadric_partial == 0 ]]; then
    printf '%s\n' 'DEPENDENCIES AVAILABLE. Run check.py; no mathematical or build validation has been performed here.'
else
    printf '%s\n' 'PARTIAL ENVIRONMENT. Continue available research; do not report skipped checks as successful.'
fi
if [[ -n "$quadric_python" ]]; then
    printf 'Next diagnostic: "%s" "%s/scripts/check.py" doctor\n' "$quadric_python" "$quadric_root"
fi
exit 0
