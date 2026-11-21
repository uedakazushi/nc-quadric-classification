# nc-quadric-classification

**構造対象 O のみを指定した非可換 quadric surface の分類。**

2026-11-21 / 運用v0.39、主論文v1.38、別稿v0.1。まず [研究方針](00_research_plan.md) と [AGENTS.md](AGENTS.md) を読む。GitHub `main` を正本とする。

## VS Code / LuaLaTeX の組版環境

リポジトリの `.vscode/settings.json` はOSに依存しない `latexmk` コマンドを使う。macOS・Linux・Windowsのいずれでも、TeX Live（または互換するLaTeX環境）を導入し、**VS Codeの拡張機能プロセスから** `latexmk` がPATHで見える必要がある。WindowsではTeX LiveまたはMiKTeXの実行ファイルディレクトリをPATHに登録する。組版にはLuaLaTeX、`ltjsarticle`、latexmk等が必要である。

macOSでFinder/DockからVS Codeを起動した場合、MacTeXが導入されていても `/Library/TeX/texbin` が拡張機能のPATHに含まれないことがある。この場合、**Macだけのローカル対処**として、VS Codeのユーザー設定（リポジトリで共有しない設定）で `latex-workshop.latex.tools` の `latexmk-project` の `command` を `/Library/TeX/texbin/latexmk` に、`latex-workshop.latex.clean.command` も同じ絶対パスに指定する。共有設定の `cwd` と `args` は維持する。あるいは、`/Library/TeX/texbin` をVS Codeの起動環境PATHに追加してから再起動する。Macの `.latexmkrc` はMacTeXのディレクトリが存在する場合にのみ子プロセスのPATHを補うが、**latexmk自体を起動する前のPATH問題は解決しない**。

VS Codeではリポジトリのルートをフォルダとして開き、`papers/nc-quadric-classification.tex` または `papers/quiver-avatar-moduli.tex` をアクティブにして LaTeX Workshop のビルドを実行する。PDFとSyncTeXは `build/` に出力される。まずターミナルで `latexmk -v` と `lualatex --version` を確認し、ビルドが失敗した場合は LaTeX Workshop のログで `spawn latexmk ENOENT` の有無を確認する。

## Cloud Codexで続ける

[CLOUD_CODEX.md](CLOUD_CODEX.md) に、環境の準備・起動用の依頼文・検証・保存手順を置く。最終目標は研究方針F1–F6を満たす**全H2のpointed exact同値分類**。一補題やcommitで止めず、現行資料を更新しながら次の未解決課題へ進む。

**全H2の分類定理の証明を統合した。** cubic側はlinearデータと、整・被約・非被約を含む全てのVan den Bergh許容四つ組で構成し、四生成環の二次関係に対する有限の代数的判定で重複を除く。noncubic側はP1上の二つの二点集合の非順序対の同時射影同値で分類する。両領域は交わらず、全対象を覆う。統一定理と各構成の独立数学点検を完了した。外部査読・形式証明・包括的な新規性確定とは区別する。組版等の実際の確認範囲は研究ノートを参照。

## 八本・十本・十二本矢と avatar

独立した公表用草稿 [papers/quiver-avatar-moduli.tex](papers/quiver-avatar-moduli.tex) に、表示モジュライ・反標準 avatar・内在的忘却の関係をまとめた。主論文は全H2のpointed分類と相対認識を、別稿は矢数の層別と幾何的chartを扱う。

| 対象 | 確立した関係 | 留保 |
| --- | --- | --- |
| 有限 foundation | Hom次元 $(2,2,2,4,4,6)$ の結合律 $c(1\otimes a)=d(b\otimes1)$ から有限型Artinスタック $\mathfrak F_{\le12}$ を構成。二つの10本矢開部分の交わりが8本矢部分 | AS条件・滑らかさ・相対H2認識はこの構成に含めない |
| 重み付きQP | 二つの可逆な二次係数で対角pairを消去。Jacobian代数のモジュライでは8→10→12は開埋め込み | 生のright-equivalence商には消去pairの $\mathbb G_m$ 慣性が残る |
| 曲線型avatar | $P\in\operatorname{Pic}^0(D)$、$P\ne\mathcal O_D$。$H\mapsto HP$ による再埋め込みから二つの10本矢開部分と交わりの8本矢部分を構成 | 全相対AS代数とのスタック同値は未証明。AS最小矢数との辞書は明示した未公刊分類入力による |
| 直積型square | 全 $(2,2)$ Cartier因子と非自明な $\operatorname{Pic}^0$ は、一方の非最小10本矢chartに対応 | 最小10本矢はその境界。元のproduct collection自体は有限8生成矢・4関係、relation completionは12本 |
| $\Sigma_2$ 境界 | 負断面 $S$ と交わらない因子は一方の10本矢境界、$S\le D$ は最深12本矢層 | $\Sigma_2$ の出現だけで12本矢とはいえない。$P=\mathcal O_D$ の古典点は別途扱う |
| 内在的忘却 | 相対heart・適合平方根・AZ豊富性・同じ根のAS4被覆を満たす部分から $\mathfrak H_2$ への射。全H2幾何点は10本矢normal foundationを持つ | その適合部分の開性は未証明。$\operatorname{coh}\mathbb P(1,1,2)$ と $\operatorname{coh}\Sigma_2$ の構造対象は強いH2条件を満たさない |

証明は [有限QP](papers/quiver-avatar/qp_presentations.tex)、[有限foundation](papers/quiver-avatar/foundation_charts.tex)、[avatar](papers/quiver-avatar/avatar_charts.tex)、[内在的忘却](papers/quiver-avatar/intrinsic_forgetting.tex) に置く。独立読取り・計算・組版の実施範囲は研究ノートを参照。

## 相対構成の現在地

**有限型開上の全次数表示と相対AS4被覆。** 可換Qの標準Morita根をétale近傍へ代数化し、四項foundationと三次tensorを構成した。幾何的cubic条件の開性、標準三次解消の相対完全性、Euler複体によるHom比較から、一つの有限型開U°上で全次数のcubic提示・内在Hom・局所自由性・偶数Bの相対Koszul性が成立する。一般のcanonical hull定理から、同じ開上で全次数平坦な相対AS4被覆A/(G)=Bも存在する。`prop:quadric-uniform-cubic-hom-open`、`prop:quadric-zariski-homological-as-cover`、`thm:universal-cubic-hull`。

**任意affine基底でcanonical導来比較が成立。** 幾何的cubic開U°上で、cubic標準解消からtorsion局所化の導来次元と四項tiltingを求め、D(QGr B_T)≃D(Mod Λ_T)、compact≃Perf Λ_Tを証明した。全helixを右規約C_ij=D_{−j,−i}で比較し、次数移動(1)を既存のMorita根sへ対応させる。相対Serre関係と非平坦を含む導来基底変更も整合する。Noetherian性はこの比較の仮定ではない。[相対cubic tails](papers/sections/relative_cubic_tails.tex)。

**左右Noetherian性があれば全相対条件が成立。** Noetherian可換RでB_Rが左右Noetherianなら、全有限型R′においてqgr(B_R′)はHom有限・平坦基底変更・fppf降下・canonical compact・Serre・AZ・同じ根のAS4被覆を満たす（`thm:quadric-noetherian-relative-promotion`）。全χ_qも同じaffine基底で成立する。特にU°の各点を閉点に持つ任意Noetherian局所Rに適用でき、有限Krull次元は不要。局所Rが元の局所有限型k-siteに属さない場合は、有限型R-test上で同じ全公理が成立するという範囲を守る。

**一般coherent対象のHomと基底変更。** この全有限型R′の範囲で、qgrはmodule-object基底変更、対象・射・完全列のfppf降下、構造対象の平坦性を備える。全ての二対象間のHomはR′-有限で、平坦な有限型基底変更と可換する。固定内部次数のtail Homの安定と有限表示による直接証明であり、対象自身の平坦性は要求しない（`lem:chi1-qgr-hom-finite-flat`）。[証明](papers/sections/relative_koszul.tex)。

**任意基底変更・任意係数で構造対象のH⁰とH¹を計算。** 任意affine T=Spec R′→U°と任意R′-加群Nに対して、Hom_QGr(O_T,N⊗O_T(n))≃N⊗(B_T)_n、Ext¹_QGr(O_T,N⊗O_T(n))=0が全nで成立する。各fiberの深さ3、相対Koszul cochainの分裂完全性、Gabriel商の拡大列を使い、B_TのNoetherian性やNの平坦性を必要としない（`cor:relative-depth-three-coefficients`、`cor:quadric-all-basechange-saturated-sections`）。N=R′の場合、元の全切断環を回復する。

**周期を仮定しない普遍Noetherian性とH2効果性。** `thm:relative-geometric-cubic-noetherian` は、全成分が有限projectiveでgeometric cubic表示を持つ族の全row・columnが、任意の可換Noetherian基底変更後にNoetherianであると示す。非線形開では相対point curveとKeelerの消滅、regular normalな四次線族を用いる。線族は頂点ごとの可逆加群twistで自明化でき、無限個の線束の同時開自明化を要しない。linear閉部分でも非退化線を全整数へ伝播し、頂点線twistで標準対称積へ移す。各parityはSegre環と有限生成Segre加群となる。Z代数の次数別形式的貼合せで全基底を扱う。実際の二周期があれば、その偶数graded環Bも左右普遍Noetherianとなる。可換Q近傍では `thm:quadric-finite-type-effectivity` により全相対公理を満たすU°→H2を得る。

**一般二周期族のcanonical AS4被覆。** `thm:universal-cubic-hull` は、geometric cubic族と実際の二周期βから、逆coevaluationの線束値写像Φ_i:S_i→W_i、Φ_i|W_i=2idと階数6の核H_iを構成する。A=T(B₁)/(H₀)は全次数projective、rank Aₙ=C(n+3,3)、双対は階数列(1,4,6,4,1)のKoszul Frobeniusであり、正則正規二次線GによるA/(G)=Bを持つ。任意Noetherian基底変更後も左右Noetherianである。まずE=B!の正規線Nを割ったP=E/(N)をprojectiveにし、PPをPへ適用してA=P!を平坦にするため、非被約基底でfiber次元一定だけに頼らない。AS4被覆は任意のβに成立するが、同じ根のSerre平方条件は独立に確認する。

**cubic領域全体のsmooth Artin開部分。** `thm:cubic-smooth-open` は、全幾何fiberがcubicとなる内在的部分スタックV_cub⊂H2が、有限型で滑らかな純次元3のArtin開部分であると示す。非線形の普遍quintuple上では相対Picard群の[−2]に沿うétale被覆で適合根を構成し、linear点は可換Qのchartで覆う。各chartの全閉点で、指定されたpointed同型を保つArtin持上げを証明する。relation schemeはU×_[X3/PGL9]Uであり、選んだ根やfoundationを保存しない同値も含む。`cor:cubic-formal-h2-abelian` により全cubic点で形式H2変形とpointed Abel変形は同値で、HH≥3=0、dim HH²−dim HH¹=3となる。noncubic境界を含む全H2の代数性と、ambient内での開性は未証明である。

**相対Picard根と全cubic族の認識。** `thm:relative-compatible-root` は非線形のsmooth reduced普遍quintuple基底上で、N=L₂L₀⁻¹の二等分とATVの相対作用から実際の二周期βを構成する。β²はcanonical四周期θにvertex scalarを除いて一致する。同じβに対応するperfect双加群のSerre比較を、有限表示局所閉の比較空間と普遍基底の被約性で証明し、その後に任意の非被約底へ引き戻す。任意の根を最初から変形可能とは仮定しない。`thm:geometric-cubic-relative-effectivity` が普遍Noetherian性・canonical tails・同じ根のAS4被覆から全相対公理を供給する。DDLで五つのhelix対象を持ち上げ、四つの矢空間と四次syzygy直線を回復することで、指定同型を保つquintuple chartのArtin持上げが得られる。

**明示noncubic表示族の全相対認識。** `thm:noncubic-relative-effectivity` は二つの非退化二元二次形式の表示スタックNpres=[P/G]から、実際のH2族を構成する。中央Clifford表示を重み付き射影スタックX=P_R(1,1,2)上の有限局所自由代数へ移す。G=⊕_{i=0}³B~(i)はtiltingではなくcompact generatorであり、そのdg Endとweighted Čechからproper性・任意導来基底変更を得る。中心有限代数上のR-flat加群のfiber-perfect持上げを用いて対角のperfect性を証明し、canonical compactのsmoothnessを確認する。traceによる同じ根のSerre平方、AZ・全軌道、Ore/PBWによる普遍Noetherianな相対AS4被覆を合わせ、全相対公理を満たす。Npresは次元1であり、noncubic点の全横断変形を覆うatlasや相対全忠実性は結論しない。

**全noncubic点の良い根と有限型代数化。** `thm:noncubic-hh-trivial-root` は、根対を交換するtrace零対合から選ぶ適合Serre根が、全foundation変形のHH¹・HH²へ恒等に作用することを証明する。四平面Gr(4,8)の交代Gale双対として根の作用を計算し、接の正負次元(10,6)と有効基底変更Lieの(7,6)を比較する。根対非一致ではHH¹=0・HH²=3、一致ではHH¹=1・HH²=4で、いずれも負のHH部分は零となる。従って全Artin Abel変形へ根が延び、そのMorita類は一意である。`prop:hh2-etale-morita-root` と `cor:noncubic-etale-morita-root` により、全noncubic点の有限型étale近傍上で実際の可逆双加群・Serre平方同型・二項窓の比較を構成できる。これは同じ根のAS4被覆や相対heartの横断認識とは別の結果である。

**残る核心はnoncubic境界の横断効果性である。** 全cubic領域と明示noncubic表示族は相対H2として認識でき、全noncubic点の良い根も全Artin・有限型étale近傍へ延長できた。次は同じ根の全軌道に対するAS4被覆の高次持上げと、有限型近傍上の一様なcanonical tails・Noetherian性・AZを証明する。三有理配置での正規線の一次持上げは、高次の存在証明へ外挿しない。閉noncubic部分と開cubic部分で実際の代数族が得られれば、形式的Noetherian貼合せを適用する。全H2の代数性、X_as全体の表現可能性、内在位相とfoundation表示の位相比較は未解決である。

## モジュライのスタック構成

体上の対象クラスを $\mathcal H_2$、有限型基底上の内在的な相対族の fppf スタックを $\mathfrak H_2$ と書く。**相対族の定義、stack 性、反 Serre 関係式への全忠実性を構成した。全cubic開部分は代数的だが、全体の代数性は未証明である。** 主な証明は [相対定義と認識](papers/sections/relative_moduli.tex) に置く。

有限foundationと次数移動の可逆perfect双加群表示が得られた基底では、次数移動が反Serre関手と線束twistを除いて一致する条件を、**有限表示局所閉部分スキーム**として構成した。非被約底のminor方程式と評価同型を用い、比較のfppf局所存在そのものを表す。[偏極認識の証明](papers/sections/polarization_recognition.tex)。任意のX3族にこの有限表示を与えること、平方根・AS被覆の局所存在は引き続き別の課題である。

**Artin基底ではさらに進んだ。** 全flat Abel変形に有限foundationとcanonical反Serre軌道環を構成でき、偏極忘却は右逆を持つ。一次の核はHH¹(Λ)であり、二根対一致点の接次元5対4の差をZhang方向として説明する。HH¹(Λ)=0なら全Artin X3変形はcanonical偏極を持つ。異なる根対の全noncubic点ではX3は滑らかで次元83、商は滑らかで次元3となる。[Artin再構成](papers/sections/artin_foundation.tex)。可換Qのtensor O(1,1)は全Artin Abel変形へexact ampleなSerre根として持ち上がり、そのMorita同型類は一意である。[根の存在と一意性](papers/sections/artin_roots.tex)。

**可換点の全Artin変形は相対H2に属する。** 二周期cubic列のcanonical hullをArtin基底上で構成し、標準根の全軌道環に相対AS4被覆と正則正規二次切断を与えた。全有限型基底変更を含む昇格命題と合わせ、可換Qの全flat pointed Abel Artin変形が実際の相対H2対象になる。H2からAbel圏への忘却は、この点を中心とする形式変形groupoidの同値であり、変形は無障害、接次元9・無限小自己同型次元6である。[全Artinのhullと形式変形](papers/sections/quadric_artin_hull.tex)。一次方向については、Jacobian二重導分と右Zhang twistによる[明示構成と検算](papers/sections/quadric_first_order.tex)も保持する。全cubic点では相対Picard根とquintuple持上げを用いることで、根のHH²自明作用を追加仮定せず全Artin認識が成立する。noncubic点の全Artin認識と全H2の代数性は未解決である。

**標準平方根はétale近傍へ代数化できる。** 有限foundation表示上のMorita自己同値の代数空間と平方写像を使い、可換点の標準根を実際のperfect双加群と平方同型としてétale近傍へ延長した。[根の代数化](papers/sections/artin_roots.tex)、`prop:quadric-etale-morita-root`。その近傍では、標準foundationに対して根がF0→F2、F1→F3と作用する同型を構成し、全四項窓のfull strong exceptional性、Hom階数2/4/6/9、三次関係rank2・四次重なりrank1の非退化性を任意底変更について証明した（`prop:quadric-etale-finite-window`）。全距離のHomと三次提示は上記の相対解消で解決した。canonical compact/Serre認識は相対cubic tailsの証明で成立した。単一有限型開上の左右Noetherian性と相対H2実現は上記の定理で成立した。相対H2全体の代数性は未証明。特殊fiberのrankと非退化性の独立な厳密検算は [`verify_quadric_finite_windows.py`](computations/verify_quadric_finite_windows.py) に収録した。

族は基底変更と descent を備えた noetherian Abel 圏と構造対象 O の対である。導来条件には局所的な canonical compact 部分 $D(\operatorname{Ind}\mathcal C)^c$ を用い、特異基底上でそれを全 $D^b(\mathcal C)$ と同一視しない。平方根・根同型・AS被覆は fppf 局所の存在条件であり、標識に加えない。標数零の代数閉体上では元の $\mathcal H_2$ の pointed groupoid を回復する。

| 相対モジュライに関する結果 | 状態・証明の所在 |
| --- | --- |
| $\Phi:\mathfrak H_2\to[X_3/\mathrm{PGL}_9]$ は全忠実 | 相対AZ再構成とpointed二自己同型の自明性。[相対定義節](papers/sections/relative_moduli.tex) |
| 対角はaffineかつ有限表示 | 表示スタックの対角の引戻し。同節 |
| $X_{\mathrm{as}}=X_3\times_{[X_3/\mathrm{PGL}_9]}\mathfrak H_2$ は不変fppf部分層、$\mathfrak H_2\simeq[X_{\mathrm{as}}/\mathrm{PGL}_9]$ | 層としての商表示は確立。$X_{\mathrm{as}}$ の有限型代数空間による表現可能性が未解決 |
| 全H2の切断環・反Serre環はKoszul | 正則正規二次商とVeroneseの既知定理を適用。[相対Koszul節](papers/sections/relative_koszul.tex) |
| 三次まで平坦＋全幾何fiberがKoszulなら全次数平坦 | PP2005 Chapter 6 Theorem 7.3を任意の非被約Noetherian基底に適用。相対Koszul解消も任意底変更と整合 |
| H2点の任意のArtin基底上の $X_3$ 変形はflatなpointed Abel変形を与える | noetherian性の持上げと $\operatorname{qgr}$ による構成。同節。表示の次数移動が反Serreになることは別条件 |
| Artin上の根・全軌道AS被覆から、全有限型基底変更を備える相対H2族を構成 | [Artin再構成節](papers/sections/artin_foundation.tex)、prop:artin-witness-relative-promotion |
| 可換Qの全Artin Abel変形は相対H2、形式変形groupoidの忘却は同値 | 相対canonical hullと全有限型基底変更への昇格。無障害、接HH²(Q)は次元9・無限小自己同型HH¹(Q)は次元6。[全Artin節](papers/sections/quadric_artin_hull.tex)。大域代数性とは区別する |
| 固定した相対切断環へのAS4被覆は有限表示のincidenceで判定できる | 四次までの元の積・五次までの二次双対・Frobenius条件。[相対被覆節](papers/sections/relative_as_cover.tex)。任意基底変更のnoetherian性は明示した仮定の範囲で用いる |
| pointed Abel圏が一定で、反Serre表示からは外れる $\mathbb G_m$ 上の二次環族 | [偏極の変形](papers/sections/antiserre_polarization.tex)。$q=2$ で中心一次部分が消滅し、どのH2のcanonical反Serre環でもない |
| 同族の非零接方向は一定のpointed Abel変形へ写る | 中心元 $u^4,v^4$ の交換子が $16\varepsilon u^4v^4$。計算機に依存しない証明と[厳密検算](computations/verify_antiserre_polarization.py) |

$X_3\subset\mathrm{Gr}(56,81)$ は三次関係行列の階数がちょうど176となる局所閉スキームであり、商は有限型Artinスタックである。その全体を $\mathfrak H_2$ と同一視できないことは、上記の偏極変形で幾何点についても明示した。有限型incidenceのfppf像は一般には代数空間とは限らないため、AS被覆を選ぶ空間の構成だけで存在条件の代数性を結論しない。

既存の foundation 表示 $\mathfrak Q_{\mathrm{fnd}}$ は滑らかな有限型Artinスタックで次元3、ruling交換を忘れる写像は有限étale二重被覆である。全H2幾何点groupoidが全充満に入り、cubic非空開と全noncubic点へのpointed smooth proper dg特殊化を持つ。反Serre環としても全次数平坦な特殊化となるが、これらの族が相対H2の全条件を満たすことは未証明である。[foundation節](papers/sections/foundation_stack.tex)

noncubic表示商 $\mathfrak N^{\mathrm{pres}}$ は滑らかな有限型Artinスタックで次元1。全幾何点のpointed慣性、符号 $\mu_2^2$ gerbe、good moduli $\mathbb A^1_\chi$、coarse moduli algebraic spaceの不存在を記述した。相対Clifford表示、perfect Serre公式、選択不要な反Serre環とそのnoetherian heartも構成済みである。[noncubic節](papers/sections/noncubic_stack.tex)

noncubicの三代表点では $\dim HH^1(R)_0=(1,1,2)$、$\dim HH^2(R)_0=(3,3,5)$。関係式の接次元は正確に83,83,84で、群軌道と六係数の和は81次元である。横断2,2,3方向の全二次障害が消え、既存の二次jetは上記Koszul原理により全次数平坦となる。二根対一致点における $X_3$ 商とfoundation商の接次元5対4は、相対H2の接次元を決めるものではない。

**成分に関する現在の結論：** foundation実現点集合は誘導位相で既約・連結、成分数は各1。cubic/noncubicの表示商の非交和は人工的に2成分になる。内在的 $\mathfrak H_2$ の代数性と位相比較が未完成なので、これをその成分数とはしない。

**Noetherian 性の形式的貼合せ。** 可換Noetherian基底R、各次数成分が有限な中央次数環A、I=(f₁,…,fᵣ)に対し、A/IAと全A[fᵢ⁻¹]が左右NoetherianならAも左右Noetherianとなる。次数ごとのI進完備化で有限生成元の係数を収束させ、R̂_I×∏R[fᵢ⁻¹]の忠実平坦性で降下する。成分の平坦性・有限Krull次元は不要で、一般次数付き加群とZ代数のrow/columnにも成立する。証明 `thm:patch-noetherian`、`thm:patch-z-algebra`。幾何的cubic族では、閉部分と開補集合で実際のNoetherian性を確認して適用する。

**非可換P¹束の対角列の障害。** 滑らかな(2,2)曲線と次数二線束から全隣接縮約が非零のgeometric quintupleを構成した。しかし対応する層対称代数の候補対角列Kₙ=π(O(n)⊗e₋ₙA)は、全ての行からHomが零になる非零coherent対象を持ち、AZ生成条件を満たさない。二次解消を用いて全整数でωπMの成分がO(−2)となることを直接証明した。これは当該模型・軌道列の比較への障害であり、本来のcubic環BのNoetherian性の反例ではない。`sec:ruled-diagonal-obstruction`。本来のBのNoetherian性は、曲線商・正規拡大とlinear部分の形式的貼合せによって解決した。

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
- 比較先がVan den Berghのcubic型となる条件は、偶数項間の隣接合成の階数が4となること。階数3では距離二の生成元と関係が各一つ加わる。二型とも階数3の対象は別表示も含めてcubic型で覆えない。両領域の構成・全被覆・同値判定を主定理にまとめた。相対モジュライの完成は別問題であり、上記の表示スタックと比較している。

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
| [papers/sections/relative_cubic_tails.tex](papers/sections/relative_cubic_tails.tex) | 普遍cubic解消、canonical導来比較、Noetherian基底での全相対認識 |
| [00_research_plan.md](00_research_plan.md) | 研究一般の原則・保存許可、目標、到達点、次の具体的な着手 |
| [CLOUD_CODEX.md](CLOUD_CODEX.md) | Cloud環境の準備、起動用の依頼文、検証・保存・再開の手順 |
| [scripts](scripts) | 依存の準備と、構成・検算・組版の独立した確認 |
| [papers/nc-quadric-classification.tex](papers/nc-quadric-classification.tex) | 本文のある主論文。日本語LuaLaTeX、著者欄空欄 |
| [papers/quiver-avatar-moduli.tex](papers/quiver-avatar-moduli.tex) | 八・十・十二本矢、avatar、内在的忘却を扱う独立した日本語LuaLaTeX論文 |
| [papers/quiver-avatar](papers/quiver-avatar) | 別稿の有限QP・foundation・幾何的chart・忘却の証明 |
| [papers/sections](papers/sections) | 主分類定理、全被覆、逆構成、同値判定、基準例の証明を収めた分割節 |
| [papers/references.bib](papers/references.bib) | 確認した一次文献の書誌 |
| [notes/research_notes.md](notes/research_notes.md) | 証明状態、障害、再開に必要な知識、検証範囲 |
| [notes/ore_quadric_deformations.md](notes/ore_quadric_deformations.md) | 相対変形を試すOre族の証明稿。相対CY・Serre・H2認識は未証明 |
| [notes/literature.md](notes/literature.md) | 文献の版・仮定・適用範囲・リンク |
| [computations/verify_reducible_quadruples.py](computations/verify_reducible_quadruples.py) | 全非整曲線型の三次関係・四次テンソル・周期平方・必要な貼合せの記号恒等式 |
| [computations/verify_antiserre_polarization.py](computations/verify_antiserre_polarization.py) | 一定qgr・非一定偏極族の接軌道階数と中心一次部分を厳密に検算 |
| [computations/verify_noncubic_second_order.py](computations/verify_noncubic_second_order.py) | 三基準点の横断接方向の二次Schur障害を、全有理補正の整数恒等式として検証（NumPy・Numbaはオプション） |
| [computations/verify_noncubic_degree3_tangent.py](computations/verify_noncubic_degree3_tangent.py) | 法101でPGL9/係数接方向と、三次Hilbert階数条件の全16072線形条件を厳密検算（NumPy・Numbaはオプション） |
| [computations/verify_noncubic_antiserre_pivots.py](computations/verify_noncubic_antiserre_pivots.py) | noncubic反Serre環の9生成元・25 unit pivotと六係数の多項式回収を正確に検算 |
| [computations/verify_stack_symmetries.py](computations/verify_stack_symmetries.py) | noncubic慣性の射影群関係、χの共変性、局所対合・正則切断の記号恒等式 |
| [computations/verify_commutative_quadric_tangent.py](computations/verify_commutative_quadric_tangent.py) | 可換点の関係式接89・軌道74・商接15を整数核と法101のrankで標数零において認証（NumPy/Numbaはオプション） |
| [computations/verify_quadric_first_order_roots.py](computations/verify_quadric_first_order_roots.py) | 一次Jacobian被覆の中心性、affine bracket、九次元制限、四根の固定次元9/3/5/3を厳密検算 |
| [computations/verify_quiver_avatar_charts.py](computations/verify_quiver_avatar_charts.py) | Sigma0・Sigma2・10本矢の有限代数とproduct collectionの矢・関係数を厳密検算 |
| [computations/verify_quadric.py](computations/verify_quadric.py) | Segre積・Ore正規性・低次数階数の厳密演算による再現 |

## 再生成

現行ソースの参照確認、今回の公開計算コードの再実行、組版・画像確認の範囲は [研究ノート](notes/research_notes.md#検証範囲と再現手順) を正本とする。機械チェックは数学的証明や新規性の認証ではない。外部査読、形式証明、包括的な新規性判定は未実施である。

repoルートで実行する。

```sh
bash scripts/bootstrap.sh
python3 scripts/check.py doctor
python3 scripts/check.py all
```

別稿は次で個別に確認・組版する。

```sh
python3 scripts/check.py sources --manuscript papers/quiver-avatar-moduli.tex
python3 scripts/check.py build --manuscript papers/quiver-avatar-moduli.tex
python3 computations/verify_quiver_avatar_charts.py
python3 computations/verify_quadric_first_order_roots.py
```

出力は `build/quiver-avatar-moduli.pdf` と同名の `.synctex.gz`。ルートの `latexmk` は両論文を組版する。

Python 3.9以上とSymPy、およびLuaTeX-jaを含むTeX Live/MacTeX、latexmk、BibTeXを用いる。出力は `build/nc-quadric-classification.pdf` と同名の `.synctex.gz`。PDF・組版中間物はGitで追跡しない。

`sources`・`math`・`build`を個別に実行できる。検証の終了コードはPASS=0、FAIL=1、SKIP=2で、未導入の依存による未実施を成功と区別する。`doctor`は診断のみ。bootstrapは不足依存を`PARTIAL`と表示して処理を終え、数学的研究を止めない。TeX導入を試すオプションは`bash scripts/bootstrap.sh --with-tex`。従来どおり`python3 computations/verify_quadric.py`と`latexmk`も使える。

VS Codeではrepo全体を開き、LaTeX Workshopの推奨拡張と既定の `latexmk (LuaLaTeX, project settings)` レシピを使う。設定はresearch-hubの雛形に準拠し、`.latexmkrc`がエンジン・作業ディレクトリ・出力先を統一する。VS Code UIの操作確認とコマンドによる組版確認は区別する。

## 構造対象の忘却（調査段階）

\(\mathfrak H_2\) から圏の標識を忘れる場合、固定された圏上の**2-fiber**（許容構造対象のgroupoid）と、圏の同型類への写像のファイバー（自己同値で割る）を区別する。前者は可換quadricでも\(\mathbb Z^2\)個の成分を持つが、後者は一点。cubic型については数値候補\(\mathbb Z^2\)とKitamura–Okawaの2022年の未公刊定理報告を手掛かりに、条件付きで後者を\(\bar H\backslash\mathbb Z\)へ還元した。滑らかな楕円型で二つのruling反射を計算し、非捩れ\(\delta\)、\(2\eta\notin\mathbb Z\delta\)の幾何学的一般点では同型類忘却ファイバーが可算無限となる証明を[主原稿新節](papers/sections/marking_forgetting.tex)に収めた。スタックとしての相対被覆性や全cubic型の一般化は未解決で、新証明は独立監査・組版未実施。[研究ノート](notes/research_notes.md#o-marking-から-abel-圏への忘却幾何点ファイバーの還元条件付き)に仮定と計算を記す。

## 関連研究

[research-hub](https://github.com/uedakazushi/research-hub) が研究全体の入口。[nc-cubic-classification](https://github.com/uedakazushi/nc-cubic-classification)とはO標識とAS4表示の考え方を比較するが、その未監査の完全分類定理には依存しない。Serre根一般は [categorical-fano-index](https://github.com/uedakazushi/categorical-fano-index) と関係する。既存のquadric分類・Okawa–Uedaのmoduliとの具体的比較は文献ノートを正本とする。
