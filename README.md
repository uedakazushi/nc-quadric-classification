# nc-quadric-surface

O-marked 非可換二次曲面の分類、内在的モジュライ、AS/avatar/QPの比較。

2026-11-25 / v1.77。GitHub main が正本。最初に [研究方針](00_research_plan.md) と [AGENTS.md](AGENTS.md) を読む。[research-hub](https://github.com/uedakazushi/research-hub) は研究全体の入口。

## 公表用原稿

| 原稿 | 役割 |
|---|---|
| [A — nc-quadric-surface.tex](papers/nc-quadric-surface.tex) | 主原稿。強いH2の体上の全pointed exact分類、cubic/noncubicの全被覆と同値判定。分割節は papers/sections/。 |
| [B — nc-quadric-surface-moduli.tex](papers/nc-quadric-surface-moduli.tex) | 内在的相対H2の代数性・smooth性・境界・慣性・good/coarse moduli・形式対。分割節は papers/moduli/。 |
| [C — nc-quadric-surface-avatar.tex](papers/nc-quadric-surface-avatar.tex) | 指定AS/avatar/8・10・12矢QPの相対分類と比較、全H2のgood moduli、忘却射・fiber、spectral境界。分割節は papers/quiver-avatar/。 |

A/Bの主結果、CのS1–S5は原稿上証明されている。Cの指定範囲のS6点検を2026-11-24に記録した。全数学的独立監査、網羅的新規性、外部査読、形式証明は別状態である。正確な仮定、既知結果との関係、未解決の核心は研究方針・論文を参照する。CのMorita比較は指定cotangent表示群oidに限る。現行成果の監査と公表準備に集中し、比較やCY構造の一般化は完了条件に含めない。幾何点分類と相対stack、good moduliとcoarse moduliを区別する。

## 現行資料

- [研究ノート](notes/research_notes.md)：補助定理・反例・計算・証明監査と再現性の範囲。
- [文献ノート](notes/literature.md)、[共通BibTeX](papers/references.bib)：一次資料・定理番号・比較。
- [Ore変形の研究ノート](notes/ore_quadric_deformations.md)：別の具体的変形の証明と境界。
- [computations/](computations/)：厳密計算・独立検算。
- [CLOUD_CODEX.md](CLOUD_CODEX.md)：環境と継続実行手順。

## 組版と検証

Python 3.9以上とSymPy、LuaTeX-jaを含むTeX Live/MacTeX、latexmk、BibTeX。PDF表示確認にはPoppler等を用いる。リポジトリのルートで次を実行する。

```sh
bash scripts/bootstrap.sh
python3 scripts/check.py doctor
python3 scripts/check.py papers
python3 scripts/check.py math
latexmk papers/nc-quadric-surface.tex
latexmk papers/nc-quadric-surface-moduli.tex
latexmk papers/nc-quadric-surface-avatar.tex
```

個別原稿の検証は例えば

```sh
python3 scripts/check.py all --manuscript papers/nc-quadric-surface-avatar.tex
```

のように指定する。Aの既定原稿は papers/nc-quadric-surface.tex。出力は build/ 内の同名PDF・synctex.gz。VS Codeではリポジトリのルートを開き、LaTeX Workshopから主原稿または対応するroot指定のある分割節を組版する。macOSではMacTeXの /Library/TeX/texbin を既存設定が補う。papers/ に移動して別のlatexmk設定を誤用しない。

checkerのPASS/FAIL/SKIPは実行した検査の結果のみを示す。Cのビルド再現、計算・文献照合は研究ノートに記載する。Cで用いる四層分類と相対再埋め込み・並進は本文で証明する。PDF・組版中間物・環境キャッシュは追跡しない。

## 保存と更新

研究成果は現行論文・研究ノート・研究方針へ統合し、通常commitでmainへ保存する。保存結果を確認してresearch-hubを更新する。詳細な研究課題や証明はhubへ重複させない。
