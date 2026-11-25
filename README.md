# nc-quadric-surface

O-marked 非可換二次曲面の分類、内在的モジュライ、AS/avatar/QPの比較。

2026-11-25 / v1.84。GitHub main が正本。最初に [研究方針](00_research_plan.md) と [AGENTS.md](AGENTS.md) を読む。[research-hub](https://github.com/uedakazushi/research-hub) は研究全体の入口。

## 到達点と次の課題

論文B v0.45 の定理28.12は、反Serre環の関係部分束 $J$ と構造対象を保つ自己同値 $g$ から $(g^{-1}\otimes1)J$ を取る写像が、三次表示空間 $X_3$ への開埋込みであることを示す。この開近傍で有限 foundation と次数移動の双加群が得られ、標準偏極の実現空間 $X_{\mathrm{as}}$ は恒等切断 $g=1$ として局所閉になる。[開埋込みの証明](papers/moduli/h2_smooth_atlas.tex)・[一致根対の形式方程式](papers/moduli/noncubic_boundary_comparison.tex)。

A v1.71、B v0.44、C v4.70 の序論で、添字付き代数、次数付き加群圏、構造対象付き・無標識の tails、表示の GIT 商の比較対象を明示した。古典 conifold の像で Okawa–Ueda の次数四射のファイバーは長さ一の点と長さ三の非被約点になる。可換二次曲面の四種類の適合平方根とは幾何点の数が異なる。[古典点の比較](notes/research_notes.md#可換二次曲面と古典ポテンシャルの四重射)・[一次資料の対応表](notes/literature.md#三稿の序論で比較する分類問題2026-11-25確認)。

C v4.69では、滑らかな連結射影曲線の冪零肥厚上で、指定AS族がfppf局所に四周期標識を持つ必要十分条件を得た。全整数の双対線束を被約曲線に制限した類が、Picard群の有限生成部分群を生成することである。条件が成立すれば一つの有限Zariski開被覆で足りる。[周期化の系と反例](papers/quiver-avatar/as10_mutation_classification.tex)・[Cの指定四項目の点検](notes/research_notes.md#論文cの相対比較の点検)。

B v0.43では、五頂点の bar 解消から非有界導来局所化の核を決定し、非被約基底上の指定 pointed 同型の持上げを反Serre環の二次関係から判定した。相対定義から有限型 smooth atlas、一致類の形式対までの[公表前内部監査](notes/research_notes.md#論文bの内在的相対理論の点検)を完了した。

論文B v0.42で、非可算な標数零代数閉体上、構造対象を忘れたAbel圏の線形exact同値を正確に分類する射の標的は準コンパクトな対角を持ち得ないことを証明した。一般の同型類ファイバーの濃度の命題と、非共鳴楕円型の標識付き同型類の計数を用いる。[証明本文](papers/moduli/marking_forgetting.tex)・[仮定と依存証明の点検範囲](notes/unmarked_moduli_obstruction.md)。

論文A v1.70では、二つの適合切断環の関係空間を可逆な四次行列の対で両順に移せることが pointed exact 同値の必要十分条件となる。Segre 環の符号 twist は行列二つが必要となる例を与える。[系14.7・例14.8](papers/sections/first_orbit_object.tex)・[公表前監査の範囲](notes/research_notes.md#論文aの体上分類の点検)。

## 公表用原稿

| 原稿 | 役割 |
|---|---|
| [A — nc-quadric-surface.tex](papers/nc-quadric-surface.tex) | 主原稿。強いH2の体上の全pointed exact分類、cubic/noncubicの全被覆と同値判定。分割節は papers/sections/。 |
| [B — nc-quadric-surface-moduli.tex](papers/nc-quadric-surface-moduli.tex) | 内在的相対H2の代数性・smooth性・境界・慣性・good/coarse moduli・形式対。楕円型の標識忘却と無標識モジュライの対角の障害。分割節は papers/moduli/。 |
| [C — nc-quadric-surface-avatar.tex](papers/nc-quadric-surface-avatar.tex) | 指定AS/avatar/8・10・12矢QPの相対分類と比較、全H2のgood moduli、忘却射・fiber、spectral境界。分割節は papers/quiver-avatar/。 |

Aの体上分類の公表前内部監査F6を2026-11-25に完了した。Bの指定七項目の点検記録は同日付。Cの指定四項目の内部監査と一次資料照合を完了した。三稿の先行結果との比較を序論に収録した。Bの主結果、CのS1–S5は原稿上証明されている。Cの指定範囲のS6点検を2026-11-24に記録した。全数学的独立監査、網羅的新規性、外部査読、形式証明は別状態である。正確な仮定、既知結果との関係、未解決の核心は研究方針・論文を参照する。CのMorita比較は指定cotangent表示群oidに限る。比較やCY構造の一般化は完了条件に含めない。幾何点分類と相対stack、good moduliとcoarse moduliを区別する。

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
