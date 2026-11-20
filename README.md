# nc-quadric-classification

**構造対象 O のみを指定した非可換 quadric surface の分類。**

2026-11-21 / 運用v0.3、数学原稿v1.0。まず [研究方針](00_research_plan.md) と [AGENTS.md](AGENTS.md) を読む。GitHub `main` を正本とする。

## Cloud Codexで続ける

[CLOUD_CODEX.md](CLOUD_CODEX.md) に、環境の準備・起動用の依頼文・検証・保存手順を置く。最終目標は研究方針F1–F6を満たす**全H2のpointed exact同値分類**。一補題やcommitで止めず、現行資料を更新しながら次の未解決課題へ進む。

**全H2の分類定理の証明を統合した。** cubic側はlinearデータと、整・被約・非被約を含む全てのVan den Bergh許容四つ組で構成し、四生成環の二次関係に対する有限の代数的判定で重複を除く。noncubic側はP1上の二つの二点集合の非順序対の同時射影同値で分類する。両領域は交わらず、全対象を覆う。統一定理と各構成の独立数学点検を完了した。外部査読・形式証明・包括的な新規性確定とは区別する。組版等の実際の確認範囲は研究ノートを参照。

## 対象

`(C,O)` を構造とし、`O`はGabriel–Krull rank-one torsion-free exceptional。`Db(C)`はHom有限でSerre関手`S`を持つ。exactな平方根 `s² ≅ S⁻¹[2]` が存在し、同じ`s`について `(O,s)` がArtin–Zhang ample、切断環が

$$
B(C,O,s)\simeq A/(g)
$$

と書けることを要求する。`A`は左右noetherian quadratic Koszul AS-regular型`(1,4,6,4,1)`、`g∈A₂`は左右正則正規。**s、根同型、ambient、方程式、例外列は追加標識ではない。** 分類の同値はOを保つexact同値である。

通常のquadratic envelopeは二次曲面の式も含むので、可換quadricでもambientにはならない。そこでAS正則な二次被覆の**存在**を使う。H2の「2」は超曲面次数であり、可換quadricの反標準次数は8。

## 主結果と構成

- 平方根条件から圏の大域次元2、rank-one torsion-free条件から切断環のdomain性を証明。
- 被覆からHilbert関数`dim B_n=(n+1)²`、二次関係7本を導出。固定Bの被覆は `Gr(6,ker(B1⊗B1→B2))` の許容部分へ還元。
- 同じ可換quadricに対する非可換Ore ambientの族を構成。quotient mapを固定した被覆は非一意。
- 滑らかな射影整曲面として実現される可換対象は`P1×P1`に限られ、rank-one torsion-free exceptional標識は線束。条件に適合する平方根関手はpointed exact共役を除いて4種類であるが、O-marked対象は一つ。
- 複素数体上、無限位数の平行移動を持つ通常の楕円型Sklyanin pencilの滑らかな成員がH2に入ることを確認。`z=τ`の成員は、単純対象の自己Euler特性2により`coh(P1×P1)`とexact同値でない。
- 反Serre切断環は9生成・56次元の二次関係を持ち、その関係空間の線形同値がpointed exact同値の必要十分条件となる。
- 滑らかな無限位数Sklyanin型では、rulingを適切に選ぶとcubic Z-algebraへの比較が得られる。反Serre環の中心から楕円商を回復でき、全て可換quadricとpointed exact非同値である。
- 正規切断の中心性、standard性、ambientの追加条件(*)を要せず、全H2対象は四周期の三次元AS正則Z-algebraとして表せる。non-standardでは二つのrulingを交互に置く。
- 比較先がVan den Berghのcubic型となる条件は、偶数項間の隣接合成の階数が4となること。階数3では距離二の生成元と関係が各一つ加わる。二型とも階数3の対象は別表示も含めてcubic型で覆えない。両領域の構成・全被覆・同値判定を主定理にまとめた。相対モジュライは別の未解決問題である。

既知結果、初期原稿内の証明、計算、外部監査・形式証明・新規性確認を区別する。正確な範囲は [研究ノート](notes/research_notes.md) と [文献比較](notes/literature.md) を参照。

- 全ての許容四つ組から構造対象と適合根を構成した。整な曲線、被約な二・三・四成分、二重(1,1)、片方または両方が重複したgridで、周期の平方とSerre移動を比較した。一般のeven partのdomain性にはPresottoの定理を使う。
- 二次Koszul環Bが与えられれば、型14641の正則正規被覆の存在は四次までの元の積と五次までの二次双対で判定できる。
- 固定Sklyanin pencilの明示的な開領域では、中心の一次近傍により各切断の比較を高々64候補に絞れる。持上げ変更の単射性は無限位数の場合に自動的であり、この簡約に残る開条件は中心変形写像Δの単射性である。全分類では仮定を要しない四生成判定を使う。厳密計算は `computations/verify_pencil_tangent.py` に収録した。
- 重み付き四周期環の単純分解から周期偶数環のKoszul性が従う。逆構成に残る条件を、分解の完全性、周期、domain性、斉次切断の長さ、有限被覆判定に絞った。

- 四変数の多パラメータskew polynomial環の正規二次切断を完全に分類した。非cubic型一点とcubic族があり、後者はパラメータr²を逆元で同一視する。
- 中央二変数を持つOre環 yx=qxy+h も退化を含めて分類した。可換類と、二つの非退化二次形式の根の対で判定される非cubic族が現れる。

- 全非cubic対象は二つの非退化二次形式を持つ中央二重平方環へZhang同値で帰着する。non-standardな適合表示を持つのは、二つの根対が一致する一点だけである。固定表示内での線形基底変更による中央化とは区別する。

## 現行資料

| ファイル | 役割 |
| --- | --- |
| [00_research_plan.md](00_research_plan.md) | 研究一般の原則・保存許可、目標、到達点、次の具体的な着手 |
| [CLOUD_CODEX.md](CLOUD_CODEX.md) | Cloud環境の準備、起動用の依頼文、検証・保存・再開の手順 |
| [scripts](scripts) | 依存の準備と、構成・検算・組版の独立した確認 |
| [papers/nc-quadric-classification.tex](papers/nc-quadric-classification.tex) | 本文のある主論文。日本語LuaLaTeX、著者欄空欄 |
| [papers/sections](papers/sections) | 主分類定理、全被覆、逆構成、同値判定、基準例の証明を収めた分割節 |
| [papers/references.bib](papers/references.bib) | 確認した一次文献の書誌 |
| [notes/research_notes.md](notes/research_notes.md) | 証明状態、障害、再開に必要な知識、検証範囲 |
| [notes/literature.md](notes/literature.md) | 文献の版・仮定・適用範囲・リンク |
| [computations/verify_reducible_quadruples.py](computations/verify_reducible_quadruples.py) | 全非整曲線型の三次関係・四次テンソル・周期平方・必要な貼合せの記号恒等式 |
| [computations/verify_quadric.py](computations/verify_quadric.py) | Segre積・Ore正規性・低次数階数の厳密演算による再現 |

## 再生成

repoルートで実行する。

```sh
bash scripts/bootstrap.sh
python3 scripts/check.py doctor
python3 scripts/check.py all
```

Python 3.9以上とSymPy、およびLuaTeX-jaを含むTeX Live/MacTeX、latexmk、BibTeXを用いる。出力は `build/nc-quadric-classification.pdf` と同名の `.synctex.gz`。PDF・組版中間物はGitで追跡しない。

`sources`・`math`・`build`を個別に実行できる。検証の終了コードはPASS=0、FAIL=1、SKIP=2で、未導入の依存による未実施を成功と区別する。`doctor`は診断のみ。bootstrapは不足依存を`PARTIAL`と表示して処理を終え、数学的研究を止めない。TeX導入を試すオプションは`bash scripts/bootstrap.sh --with-tex`。従来どおり`python3 computations/verify_quadric.py`と`latexmk`も使える。

VS Codeではrepo全体を開き、LaTeX Workshopの推奨拡張と既定の `latexmk (LuaLaTeX, project settings)` レシピを使う。設定はresearch-hubの雛形に準拠し、`.latexmkrc`がエンジン・作業ディレクトリ・出力先を統一する。VS Code UIの操作確認とコマンドによる組版確認は区別する。

## 関連研究

[research-hub](https://github.com/uedakazushi/research-hub) が研究全体の入口。[nc-cubic-classification](https://github.com/uedakazushi/nc-cubic-classification)とはO標識とAS4表示の考え方を比較するが、その未監査の完全分類定理には依存しない。Serre根一般は [categorical-fano-index](https://github.com/uedakazushi/categorical-fano-index) と関係する。既存のquadric分類・Okawa–Uedaのmoduliとの具体的比較は文献ノートを正本とする。
