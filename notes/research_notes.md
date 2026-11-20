# 現行研究ノート：O-marked 非可換 quadric

2026-11-21 / v0.3（数学原稿v1.1）。最初に [研究方針](../00_research_plan.md) を読む。証明の正本は [主原稿](../papers/nc-quadric-classification.tex)、文献確認の正本は [文献比較](literature.md)。本書は作業履歴ではなく、現在有効な知識と再開点を記す。

## 定義と規約

対象は `(C,O)`。`s`とAS4被覆を同時に存在させる。Gabriel–Krullの`C₀`は有限長、`C₁`は`C/C₀`で有限長になる対象の逆像。`qO`が非零単純かつ`Hom(C₁,O)=0`をrank-one torsion-freeと呼ぶ。`GKdim=1`の意味ではない。

右加群を採用し、`B_n=Hom(O,sⁿO)`、`a*b=s^{deg b}(a)∘b`。`Γ_*(M)`の右作用も同じ順序。cubic repoの表示された積と反対なので、外部のNakayama・正規化自己同型の公式を直接コピーしない。

強いH2条件は `B ≅ A/(g)`、`A`は型14641、`g∈A₂`は正則正規。`g`の代表のスカラーは区別せず、最終対象ではambient自体を忘れる。`s²≅S⁻¹[2]`の同型は指定しない。根同型をrigidifyしたmoduliやtrace coherenceは別問題である。

## スタック構成の現状

`papers/sections/noncubic_stack.tex` に、非退化二次形式対Pと五次元群Gによる `[P/G]` を構成した。滑らかな有限型Artinスタック、次元1、根配置スタックへの局所μ2² gerbe、全次数平坦な普遍表示を証明する。`f1=uv, f2=u(v−tu)` は一根共有軌道が根対一致軌道へ特殊化する族であり、通常のGIT商はこの二つのpointed類を区別しない。

現在の構成は表示スタックである。非被約基底上の相対正規形、相対Serre/AZ再構成、慣性の全忠実な比較、全H2への貼合せは別の証明を要する。特にP上の普遍graded環はdegree scalarを剛体化したstackへ通常の環束として直ちに降下しない。

今回追加したv1.1の組版・独立監査は進行中であり、以下に記すv1.0の検証結果から自動的に検証済みとは扱わない。

## 証明状態と依存関係

| 主張 | 依存する事実・仮定 | 状態・所在 |
| --- | --- | --- |
| `gldim C=2` | Serre双対、heart上exactな平方根 | 原稿に直接証明。`prop:gldim-two` |
| 非零 `O→sⁿO` は単射、Bはdomain | Gabriel–Krullのrank-one purity、exact性 | 原稿に直接証明。`lem:sections-monic` |
| Bは二次、`H_B=(1−t²)/(1−t)^4` | 正則正規二次商の完全列 | 原稿に直接証明。`prop:quadric-hilbert` |
| 負切断0、AZ再構成 | 上記単射・Hilbert、`MU2021` Thm2.6(2) | 原稿に証明・適用仮定。`prop:reconstruction` |
| 被覆候補は7次元K内の超平面 | B二次、Hilbert、A型14641 | 原稿に直接証明。`prop:ambient-hyperplane` |
| 左右の三次乗法rank4で正規性、Hilbertで正則性 | AS条件を先に仮定。J₃は4次元 | 原稿に直接証明。AS条件の有限検査を証明したものではない |
| Ore族 `A_a/(xy−uv)=B_Q` | `a≠0`、Ore拡大定理`LV2026` Prop2.2と表示計算 | 原稿に適用確認。`prop:ore-ambient-family` |
| 滑らかな射影整曲面上のrank-one torsion-free exceptionalは線束、H¹O=H²O=0 | Serre双対、二重双対、Riemann–Roch | 原稿に直接計算。`lem:commutative-marking-line` |
| 滑らかな可換対象はQ | 一次生成・AZ・B1=4,B2=9、coh自己同値記述、Kodaira/RR/Hodge/Nakai | 原稿に証明。`thm:commutative-recognition` |
| Q上の適合する根は4共役類 | `BondalOrlov2001` Thm3.1、Aut(Q)とPic(Q)の計算 | 原稿に証明。`thm:commutative-four-roots` |
| 四根のAS4被覆 | 符号型skew polynomial、skew Koszul複体、Segre twist | 原稿に証明。`prop:commutative-twist-covers` |
| 滑らかな楕円型Sklyanin対象はH2に属する | k=C、τ無限位数、z+τ∉E[2]。`BSW2010`, `RRZ2014`, `SVdB2013`, `MU2021` | 全切断環・Serre根・exceptionality・AZ・Gabriel–Krull条件の証明。`prop:sklyanin-h2` |
| z=τの対象はcoh(Q)とexact同値でない | `SVdB2013` §10.5の単純対象Fとχ(F,F)=2 | 既知の構成を適用。`prop:sklyanin-genuinely-noncommutative` |

これらの主張は研究開始時の基礎結果であり、独立した新規性を確定したものではない。形式証明器は使用していない。全H2対象の被覆と同値類分類は主定理に統合した。一般点のモジュライ次元、成分、全自己同値、族の降下・代数性は別途未証明。

## Quadratic envelope の障害

通常の `QEnv(B)=T(B₁)/(ker(B₁⊗B₁→B₂))` は二次関係を全て課す。quadric環はそれ自体が二次なので `QEnv(B)=B`。可換Qでも `dim B₁=4, dim B₂=9`、関係は7本となる。型14641のambientは `dim A₂=10`、関係6本であり一致しない。

この障害はcubicの方法をそのまま適用できない理由であるが、AS正則被覆の存在を妨げるものではない。定義の段階で二次被覆を存在条件へ替え、元の「Oだけを標識する」目標を保つ。

## 可換認識の要点

主原稿の`thm:commutative-recognition`は、全AS条件より弱い一次生成・B1=4・B2=9で成立する。一次生成とAZ(A1)から評価`s⁻¹O`の有限直和→Oが全射となり、奇数shiftを偶数shiftで置き換えて反SerreのAZ豊富性を得る。Oを線束として正規化し、`s=φ*⊗L`、`M=−K`と書くと、Mはample、Lは大域生成。Kodaira/RRからM²=8、M.L=4、L²=2。HodgeからL≡M/2がampleとなり、|L|は有限双有理射で正規な整二次曲面へ写すため同型になる。滑らかな射影整曲面という仮定を省略した認識はこの定理に含めない。詳細証明は複製せず本文を参照する。

## 固定Bの次の計算

`V=B₁, K=ker(V⊗V→B₂)`、`dim K=7`。`R∈Gr(6,K)=P(K*)`を選び `A_R=T(V)/(R)` とする。`g_R`は`K/R`の非零元。

1. `A_R`が型14641であることを証明または既知の分類定理の正確な仮定に照合する。
2. `A_R`の三次関係 `R⊗V+V⊗R` を用い、`g_R V`と`V g_R`の階数を計算する。
3. 両方rank4なら `g_R V=V g_R=ker((A_R)₃→B₃)`。正規性が全次数へ延び、Hilbert級数から左右正則性が従う。

条件1を低次数のdim一致で代用しない。現在は許容集合の開性・既約性・次元や分類の有限性を証明していない。quotient mapを固定した被覆同型は次数1で恒等となるので、固定B上ではRが被覆を区別する。Bの自己同型も許す場合はその作用をさらに割る必要がある。

## 忘却を区別するための基準例

固定可換環 `B_Q=k[x,y,u,v]/(xy−uv)` に対し、`a∈k×`のOre族

$$
A_a=k\langle x,y,u,v\rangle/(u,v\text{ central},\ yx=a xy+(1-a)uv)
$$

は型14641で、`g=xy−uv`は正則正規、全て `A_a/(g)=B_Q`。異なるaは固定Bへの被覆として異なるが、同じroot付き圏・O-marked圏を与える。unframedなambient全同型分類は未実施。

同じ`(coh Q,O_Q)`上で、適合する平方根は `s_φ=φ*⊗O(1,1)` の4種類：恒等、一因子対合、両因子対合、因子交換。4個の別の曲面を意味しない。一般の根忘却fiberが4点、有限、あるいは既存Okawa–Uedaの次数4射に一致するとは結論しない。

`MUW2026` Theorem4.12の既知判定を使うと、最初の3型の切断環はstandard、因子交換型はnon-standard。twistの積の左右規約を同型で照合した証明は `rem:commutative-standard`。従ってstandard性は同じO-marked pair上でも変わり得る。

因子交換と`O(2,0)`の組は平方根+AZ ampleでも一次切断数3で、AS4被覆条件を満たさない。同じO-marked対象には適合する別の根が存在する。従って「ある根が良い」と「全ての根が良い」も区別する。

## 楕円型の確立した入口

複素数体上の通常の4次元Sklyanin環Tと中央二次pencilを用いる。`SVdB2013`は§2の右規約と§10の幾何的左表示が併用されるため、右規約で `A=T^op`、`B_z=(T/(g_z))^op` とし、`lem:sklyanin-opposite`で中央pencilを固定する反自己同型を確認して両側の結果を移送する。τは無限位数とし、`z+τ∉E[2]` がsmooth条件。`BSW2010`のCY性と`RRZ2014`の商公式でNakayama twistが恒等となり、次数shiftがSerre平方根である。深さ3と局所コホモロジーで全次数切断環とexceptionalityを確認する。

Gabriel–Krull条件は商体rankだけで代用しない。Hilbert多項式が定数／一次ならそれぞれC0／C1に入ることを示し、もう一つの中央元hによるOの下降列の商がcoh(E)の可逆層であることからO∉C1を得る。非零右イデアルにfBが含まれることからrank-one purityが従う。全文は主原稿の `prop:sklyanin-h2` を参照する。

`z=τ`では既知の単純対象Fの自己Euler特性は2。coh(Q)の全単純対象は閉点の層で自己Euler特性0なのでexact非同値性を得る。この証明は全てのsmooth pencil成員の非同値性や一般体への拡張を含めない。Sklyanin環とfat pointの構成自体を本研究の新成果とはしない。

`MUW2026` Theorem5.5で滑らかな中心Sklyanin quadricはstandardと判明しており、ここではSVdBの一般standard性の誤りに依存しない。`MN2025` Theorem6.13の三次元AS正則Z-algebraへの比較は適用可能。指定OとSerre根は prop:standard-pointed で追跡した。Sklyanin型の二つのrulingのうち、cubicとなる条件は prop:sklyanin-cubic-ruling を参照。

## Serre・standard性・既存分類の残る障害

- 根条件は関手の自然同型。`MU2021`の中心切断の仮定では `S⁻¹[2]=(−)_{ν⁻¹}(2)`。次数シフト(1)の平方根性には誘導されたNakayama twistの自明性が必要であり、元の環自己同型`ν=id`までは主張しない。
- VdBのeven partがgraded化できること、canonical hullがあることと、指定shiftがinverse Serreの平方根であることは別の命題。periodicityだけから根条件を結論しない。
- MN2025 Theorem6.13はcentral・domain・smooth・standardを仮定する。主原稿 thm:normal-helix はMU2022の正規切断の安定圏を使い、non-standardでは奇数項を交互に選ぶことで、中心性・standard性・ambientの(*)なしに全H2の標識付き四周期AS正則Z-algebraを構成する。
- 比較先は次元3・parameter4で、cubicとなるには偶数項間への隣接合成の階数4が必要。cor:normal-cubic-defect により可能な階数は3と4。二型とも階数3の場合は、どの適合根・pointed cubic表示によってもこの欠損を除けない（`thm:cubic-coverage`）。
- `MU2021`のnon-standard例は可換quadricのZhang twistでもある。一つの表示に対するspinorのsyzygy挙動を、そのままO-markedカテゴリーの不変量としない。
- graded同型、root付き同値、O-marked exact同値、derived同値は異なる。同じderived categoryというだけで本研究の対象を同一視しない。
- 全H2のpointed exact同値を反Serre環の二次関係空間で判定できる。主原稿 thm:antiserre-invariant、prop:antiserre-quadratic。実現軌道は主定理のcubicデータと中央二重平方族で全て覆った。Sklyanin型では中心が一次元で生成され、その商から楕円曲線を回復する。
- GIT商のorbit closure・S-equivalenceとpointed exact同値は同じとは限らない。既存moduliの点をそのままH2の同値類と読む前に、実際の同値作用と許容領域を確認する。

固定ambientでの自己同型Zhang twistによる中心化条件と、誘導シフトの平方根性の条件は異なる。両立にはnormalizerが次数スカラーであることが必要で、Ore族では失敗する。主原稿 prop:central-twist-obstruction、ex:ore-central-twist。別ambientによる中心表示の存在は未解決である。

## cubic 被覆と逆向き構成

最初の軌道対象は全適合根で同型となる。これを用いてcubicからの偶数成分の制限を識別し、二型の階数がともに3ならどの標識付きcubic表示も排除した。具体例は中心商のKoszul双対が M₂×M₂ となる skew polynomial 切断をZhang twistして得る。主原稿 thm:cubic-coverage と prop:nonstandard-rank-three-example。

全許容四つ組で、五つ組の巡回写像を双対化双加群と比較し、平方根つきの逆構成を閉じた（`thm:all-admissible-inverse`）。整な曲線、被約な二・三・四成分、二重(1,1)、片方または両方が重複したgridが全(2,2)型を尽くす。全even partのdomain性はPresotto2018 Theorem 2.8から従う。幾何商の零因子は元のcubic環の零因子を意味しない。非被約の場合も純一次元Cartier因子の可逆層は有限長でなく、Gabriel–Krull条件の証明が通る。

主分類のcubic入力はD1–D3の具体的幾何条件であり、未知のAS条件は残さない。K=(1⊗β01⁻¹)(R0⊗V3+V0⊗R1)は七次元で、四次全切断乗法の核（八次元）とは異なる。後者を使うと曲線への追加商を誤って課す。二次関係のGL4 transporterに対する有限反復は剰余類の閉性とNoetherian性で停止し、両側indexed同型とpointed exact同値を必要十分に判定する。係数体が有効に与えられた場合には消去計算として実行できる。有限停止の証明は与えたが、任意入力を処理する一般solverは実装・実行していない。βの違いは同じ偶数Z-algebraと指定対象を与えるので、この同値判定に吸収される。


距離二・三の関係の形は prop:rank-three-relations。四周期単純分解を偶数成分へ制限すると、奇数表現可能加群が線形分解を持つ。これと偶数頂点の分解を合わせるとBのKoszul性が従う。GK条件は、domainならある正次数fの切断がtailsで非有限長であることに還元される。fの正規性は不要。逆構成の残る仮定は prop:weighted-inverse-reduction を参照。固定skew ambientの中央切断は cor:skew-rank-three-central-locus で退化も含めて判定した。全四変数符号型の正規切断では、中央の場合に符号変更と対角化を行い、非中央の場合にnormalizerを対角化して双線形ブロックに分けた。thm:sign-quadric-normal の三標識類へ分類した。混合符号の非中央代表は二つのrank4行列分解を持ち、偶数切断環は非可換なので、他の二標識類と異なる。 交換係数が任意の非零元でも、正規二次式は指標のブロックごとに標準化できる。使われない変数は双対の次数零局所化に平方零イデアルを与える。残る切断を非cubic一点とcubic族に分類し、後者で同値になる条件は定理 thm:multiparameter-quadric-classification に示した。

中央二変数を持つOre環 yx=qxy+h（h≠0）では、PBW最高指数から正規化自己同型を制限し、全正規二次式を求めた。q=−1の中央式 a x²+b y²+H 以外でH2を与えるのは、xy=h/(1−q) で得られる非退化な可換型だけである。反交換の中央式は B=k[u,v]⟨c,d⟩/(c²−f₁,d²−f₂) に帰着し、f₁,f₂の非退化だけでdomain性とsmoothnessが従う。根の対を交換する対合から適合根を構成した。二つの対の配置が標識同値判定を与え、全ての対象は非cubicである。主原稿 prop:ore-normal-quadrics、thm:ore-anticommuting-central。


## 全非cubic領域の分類

二型の階数がともに3のH2対象は、standard・non-standardのいずれでも中央二重平方環へZhang同値で帰着する（`thm:noncubic-classification`）。その二つの根対の配置がpointed exact同値を完全に判定する。証明では同一支持をtwisted conicと二変数二次式行列の因子分解で排除し、異なる支持の交わりWを量子/Jordan平面として回復する。基点を持つpencilはBを有理曲線の斉次商環へ埋め込んでしまい、Hilbert関数(n+1)²に反する。

二つのconicの周期はW上でスカラーまで一致し、貼り合わせた自己同型によるtwistで両方を同時に可換にする。non-standardの適合根条件をさらに課すと、二つの二次形式が同じ一次元固有空間に入り比例するため、根対が一致する一点しか残らない（`thm:w-compatible-singleton`）。固定表示のWを線形基底変更だけで中央化できるという誤った方法は用いない。

## 逆構成と比較に使う補題

被約な二つの(1,1)成分では、直線束の貼り合わせ係数を t₂ₙ=a rⁿ、t₂ₙ₊₁=b rⁿ と書く。許容条件は a,b,r≠0、a≠b、b≠ar、r≠1。二周期の切断上の作用は diag(1,√r)、四次テンソルの回転は diag(r,r²) となり、その差は対角型自己同型である。証明は `lem:i2-parameters`、`prop:i2-period-square`、`thm:i2-inverse`。接する二成分では t₂ₙ=a+nd、t₂ₙ₊₁=a+q+nd、q d(q−d)≠0 と書け、βは y↦y+(d/2)x、θは y↦y+dx となる。被約な(2,1)+(0,1)と因子交換型でも偶奇別に計算して全被約二成分を扱った。二重(1,1)ではO⊕Ω¹の分裂と微分による自己同型を使い、moving basisでβ²=θ=idとなる。三成分cycle・通常三重点・四成分gridでも全切断を記述し、周期平方を確認した。非被約gridでは長さ二／四の交点の貼合せを使う。片重複型のEの引戻しには2V側の自明化補正1−dε/2が必要で、cycle/gridでも次数零成分の倍率を明記した。これらは記号恒等式と独立の大域幾何点検を組み合わせて確認した。

cubic表示の構造対象上の反Serre移動は `lem:cubic-serre-objects` を使う。MNのTheorem 4.19はASF+の周期化についての定理であり、ASだけからの引用に代えない。既存H2圏のSerre双対性と四項のfull exceptional collectionにより、対象の像を左直交から特徴付けられる。

Sklyanin pencilの持上げ変更 ∂ の単射性は `lem:pencil-lift-injective` で証明した。非零 f∈ker∂ は二次性から D→k[z] を与える。その単純tails対象はshiftで不変な閉点となり、非零平行移動に固定点がないことに矛盾する。高々64候補への簡約で未解決の開条件は中心変形写像 Δ の単射性だけである。主分類はこの条件を使わない四生成の判定を全領域で用いる。

## 検証範囲と再現手順

実行環境：Python 3、SymPy 1.14.0。依存の許容範囲は `requirements.txt`。計算は全て有理数または記号演算で、浮動小数点近似や外部データを使用しない。

```sh
bash scripts/bootstrap.sh
python3 scripts/check.py doctor
python3 scripts/check.py sources
python3 scripts/check.py math
python3 scripts/check.py build
```

導入・再開の手順は [CLOUD_CODEX.md](../CLOUD_CODEX.md)。checkerのPASS/FAIL/SKIPはそれぞれ実施成功・失敗・未実施を表し、証明や分類の完了を判定しない。doctorとbootstrapの終了コード0は診断・準備処理の終了である。TeXや文献取得に制約があればその検証を未実施とし、独立な証明課題へ進む。

計算器が検証する範囲：Segreの二次積9×16行列のrank9・核7、三次積16×64行列のrank16、二次核の明示生成元、Ore関係の記号的正規性恒等式、a=1での可換性、a=2と−1における二次関係rank6/7・三次dim20/16・左右の乗法と像の和のrank4。

有限次数計算はAS正則性・全次数Hilbert級数・smoothness・全分類の証明を代替しない。これらのうちAS正則性等は原稿中の理論と確認した文献を入力とする。

2026-11-21の現行確認：全分類定理のD1–D3、有限K、同値判定、根選択独立、全被覆・非交差を独立担当が点検した。standard・non-standardの全帰着、同一支持排除、全退化型のPic・大域自己同型・貼合せ、Serre比較の双加群計算、逆構成から全H2公理までの依存も独立に点検した。重大な残存ギャップは見つからず、必要な自明化補正等を本文へ反映した。全非整型の三次関係・四次テンソル・周期平方・非被約gridの補正引戻しは記号恒等式として再現してPASS。v1.0の構成・参照確認（22原稿、138ラベル、119引用出現）と厳密計算はPASS。LuaLaTeXで76頁のPDFとSyncTeXを生成し、最終ログに警告・未定義参照・欠字・はみ出しはない。全76頁を画像化して一覧で配置を確認し、分類データ・主定理・standard帰着・共通逆構成・非被約grid・全逆構成の頁（6、7、55、60、71、72）を個別表示でも確認した。全頁の本文を画像で再校読したという意味ではない。


既存の計算・証明の確認範囲には、四周期比較、最初の軌道対象、非cubic例、有限被覆判定、多パラメータskew polynomial分類、Ore切断の正規形・四元数斜体・根の対合・同値判定が含まれる。これらの証明は現行原稿に保持する。外部査読、形式証明、包括的な新規性の確定は行っていない。以前のPDFの表示確認を現在の全頁の確認とは扱わない。

運用checkerはPython 3.12.14／SymPy 1.14.0と既設TeXで実行できる。Python・TeX不足のSKIP、未定義ラベルのFAIL、壊れた既存venvの保持、各段階の独立した継続は確認済み。pip・aptによる新規導入、Cloud環境の作成・Publish・新規task起動、VS Code UI操作はこの確認に含まれない。

GitHubのgit読取が利用できても書込認証は別に必要である。GitHub connectorによる通常コミットも許可された保存手段として使用できる。research-hubの更新は対象repo保存後に最新READMEを読み、並行更新を保持して行う。
