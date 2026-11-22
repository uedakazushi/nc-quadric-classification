# 研究方針：O-marked 非可換二次曲面の分類

2026-11-22 / v1.20。**再開時は本書を最初に読む。GitHub `main` が正本。** 論文Aはv1.69（分類の20節）、論文Bはv0.39（相対理論の31節）、論文Cはv4.4。体上の全同値類分類と、内在的な相対モジュライの代数性を区別する。

**内在的な相対モジュライ $\mathfrak H_2$ の有限型代数性の証明を完成した。全体の既約性と被約noncubic境界のsmooth性・余次元2も証明した。被約境界を二形式商として相対的に同定し、その良モジュライ射・全慣性と全H2の粗モジュライ不存在まで証明した。DM開の任意底変更と両立する粗モジュライ、一致類に沿う全慣性作用と形式対も証明した。現在の優先事項は、A・Bの公表前監査と先行研究比較を先に完了すること、その次に既存GITとの相対比較・偏極認識を進めることである。局所good moduliの降下もこの比較の一部として扱う。** 平方根・根同型・AS被覆はfppf局所の存在条件とし、標識に加えない。有限型表示商や幾何点の被約閉包を、そのまま内在的モジュライと定義しない。

## 現行実行計画と達成基準（公表準備から次の比較研究へ）

**順序は A/B の公表前監査を維持しながら、Cで既存GIT・有限箙・avatarの表示と内在的H2の比較を研究する。** GIT比較の証明正本はCとし、Bは内在的相対モジュライの標的の性質を提供する。 Bの全H2代数性・境界同値は原稿に証明があり、現時点の研究目標としては完成扱いである。ただし全面独立再検証・外部査読・網羅的新規性照合・三稿組版は未完了。旧重点「全H2代数性未完」は採用しない。

**P0：公表に必要な整合性（最優先）。** 三論文の責任を維持する。Aは体上の強いH2のcubic/noncubic全被覆とpointed exact同値、Bは相対H2・有限型効果性と境界幾何、Cは**最小分解を指定したAS正則Z代数とavatarの分類を中心に**、有限quiver/QP表示と相対比較を扱う。Aに残る相対tailsやArtin基底の技術解説はBを参照する短い説明に集約する。CからBへ移管された主張の定理ラベル参照を正し、checkerをA/BだけでなくCからの明示的引用にも拡張する。三稿のsource/reference/BibTeX・再現手順を点検する。依存不明の旧PDFは現行原稿の未公刊入力と明記し、必要な有効証明をCに統合するまでは相対同値を主張しない。

**P1：Aの独立証明監査。** (i) normal helixと最初の軌道対象の認識、(ii) cubic被覆の必要十分性、(iii) 全許容四つ組の退化型ごとの二周期の平方＝反SerreとAS4 hull、(iv) standard/non-standard双方の同時untwistとnoncubic全被覆、(v) 反Serre環・GL9有限判定とGL4反復の有限停止を検討する。各主張の仮定、左右・反対環、文献定理の版・番号、全次数と有限次数の区別を記録する。既存の11本の厳密計算PASSは数学的な全証明検証とは区別する。全被覆・逆構成・同値判定に依存した本質的ギャップが零であり、残る留保を明記した時点をAの公表準備の達成基準とする。

**P2：Bの独立証明監査。** (i) 相対定義・module-object基底変更と反Serre再構成、(ii) five-window canonical tailsと相対Noetherian貼合せ、(iii) Artin持上げ・良いSerre根・同じ根のAS4被覆の有限型効果性、(iv) smooth atlasの指定pointed同型持上げ、(v) noncubic被約境界の二形式相対groupoid同値と慣性、(vi) AHRを用いる一致根対の形式対を順に検証する。証明に使う有限型・Noetherian・非被約底の条件を監査し、未証明の「全基底で素朴なAbel公理」「X_asの局所閉認識」「H2開上のgood moduli降下」は主定理から分離する。BはAを引用する一方向依存に保つ。

**P3：文献比較と公表編集。** Belmans, *Hochschild cohomology of noncommutative planes and quadrics*（JNCG 13 (2019), 769–795, doi:10.4171/JNCG/338）を主にcubic側の既知HH計算として明記する。VdB、Mori–Nyman、Mori–Ueyama、Kitamura–Okawa OWR2022、Okawa–Ueda 2014の既知の分類・line-bundle格子・GITを本研究の追加成果から区別する。AのIntroductionは分類・忘却・noncubicに、Bは四つの主定理群（代数性、境界相対同値、good/coarse moduli、形式局所構造）に焦点を当て、必要な証明を削らず本文を読みやすく再配置する。LuaLaTeX/latexmkで三稿ごとにPDF・SyncTeXと表示を確認し、未実施なら明記する。新規性の包括調査・第三者査読は別状態とする。

**P4：まずAS正則Z代数とavatarの分類（論文C v4.4）を主結果とし、その後にO-marked quadric・potentialとの相対比較を完成する。** 目標は**同型類の明示的全単射**またはそれを誘導する**相対モジュライの射**。滑らかな楕円cubicではVdB三線束とsquare avatarの双方向式(F_s,G_s,P)=(L2,L1 L2 L0^{-1},L2 L0^{-1})、Oを保つr1:(F_s,G_s,P)↦(G_sP^{-1},F_sP,P)の商を証明。OU potential→avatarは一般次数4、→O-markedは8（別の表示次数）。**今回noncubicの全幾何点へ拡張：** Bの被約二根対 {f1,f2} に対してq=f1f2の四次resolventを作る。全二次因子分割の射Sym²(P²)→P⁴は有限一般次数3（古典的quartic resolvent）。qの(1,1,1,1)/(2,1,1)/(2,2)はそれぞれsmooth genus1/既約nodal genus1/二P¹が二節点で交差するI2型。これらのC_qのPic⁰[2]\{0}は3/1/1点で、対応する被約二根対の分割も3/1/1通り。F_s=p*O(1)、G_s=F_sPを用いて全型を(2,2) anticanonical divisorとして埋め込み、**noncubic根対全同型類↔P²=O,P≠OかつG_s=F_sPを満たすsquare avatar全幾何同型類↔Bの全noncubic O-marked同型類**を証明（C thm:qa-noncubic-rootpair-all-geometric-square-avatar-bijection）。nodalとI2の(2,2)式も明示。**相対射とその障害：** Bの中央二重平方環B_f=k[u,v]〈c,d〉/(c²-f1,d²-f2)の可換化の点曲線E_f=Proj B_f^{ab}に同時符号μ₂を作用させ、E_f→C_q:y²=f1f2と反不変rank-one torsion-free degree0 module Mを得る。p_*M=O(-1)²、yc=f1d,yd=f2cというmatrix factorizationで任意基底変更に整合する相対射（C thm:qa-noncubic-rootpair-torsionfree-spectral-module、cor:qa-noncubic-central-square-point-curve-spectral-avatar）。smooth fiberではMは非零2torsion線束だが、共有根では節点で非局所自由。具体的f1=x(x-1),f2=(x-s)(x-2)では全空間A=k[[x,s,y]]/(y²-x(x-s))≅k[[c,d]]^{±}がA1型、反不変Mは非自由reflexiveで、一般2torsion線束はこの固定C族のinvertible sheafへ延長不能と証明。**ゆえに幾何同型類の全単射と通常Pic⁰を用いる相対スタック射は異なる**。Σ2へのelementary transformやrank-one torsion-free compactified avatarが次の候補。既存の全H2 normal ruling finite étale double cover・finite foundation実現可能開のS₂商、OU慣性・局所粗分岐、cubic quartic/sextic判定は入力として維持。**未決定：** $C_q$または$\Sigma_2$由来の別avatarのAS qgrがBのO-marked heartと一致する直接認識、同型類全単射を誘導する元のPic⁰ avatar stackの相対射、Σ2最深・非被約/他の境界・P=0古典型、8/10/12矢potentialの安定同値を含む全相対群oid。
**Σ₂での全noncubic分類を証明：** 負断面Sを避ける反標準因子D∈|−K_{Σ₂}|と0≠P∈Pic⁰(D)[2]の幾何同型類は、全noncubic O-marked quadricの幾何exact同型類と全単射（C thm:qa-all-noncubic-sigma2-anticanonical-avatar-bijection）。H=O(h)|D=F²、F=O(f)|Dを用いるsquare換算はF_s=F,G_s=FP。P非自明2捩れによりDはsmooth、既約nodal、二P¹二節点(I2)の三型だけ。Bの良moduliでχ=1に重なる一根共有と根対一致も、Σ₂のnodalとI2で区別（C cor:qa-sigma2-avatar-separates-special-noncubic-classes）。これは**体上の同型類全単射**で、$\Sigma_2$側avatarのAS qgr heartとO-markedの直接同値、および非被約底の通常Pic⁰線束を使う相対射は含まない。$E_f$側のpointed同値はC v3.6で全幾何点に拡張した。

**原稿Cの中心定理の自己完結化（2026-11-22 / C v3.4）。**
元PDFの定義2.1・定理1.3・命題2.4/6.5/7.1/12.1と第48--53節を踏まえ、
`papers/quiver-avatar/as_helix_classification.tex` にsquare/rotated square型AS正則Z代数の最小右射影分解・AS--Gorenstein条件、数値・Serre復元、AS側の評価行列からのavatar必要条件、avatar側のacyclic spherical helixからのAS逆構成、全Z代数の相互逆性、左右Noether性の証明を統合した（C `thm:qa-as-avatar-bijection`）。
`papers/quiver-avatar/as10_mutation_classification.tex` にmutation像によらない独立の最小10本矢ASクラス、relation QPのGinzburg次数零集中とKeller--Yang保存、逆mutation、全整数での評価・余評価、ASsq≅ASc⊔AS10^minの全単射（C `thm:qa-as10-global-bijection`）および10本矢avatar条件G=FPを移管した。
**12本矢は主として8本の有限foundation矢＋4本のrelation-dual戻り矢のQP表示**であり、任意の12本矢QPが正則という独立の分類定理は主張しない。P(1,1,2)の12矢QPはmutation条件を満たさない例として保持。
体上の分類の正本はCの当該二節である。外部入力はOkawa--Uedaのacyclic spherical helix実現（arXiv:2007.07620 Thm5）、Kellerのundeformed 3-CY completion（Thm6.10）、Keller--Yangのmutation保存（Thm6.2）、twisted section algebraのNoether性である。
**原稿内に証明を移管したことと、今回すべての段階を独立に再検証したことは区別**する。10本矢groupoid/相対perfect族は仮定付きであり、全QP right-equivalence stackとの同値、AS由来qgrのO-marked心とのpointed同値は未証明。
**今回の独立監査で確かめた範囲（C v3.4）。**
(1) ASsq/ASrsqの右最小分解の四位相Euler漸化式を
4×4の有理関数線型系として解き、各位相で
$\sum_{m\ge0}\dim A_{i+4m,i}\,u^m=(1+6u+u^2)/(1-u)^3$、
従って全$m\ge0$で$(2m+1)^2$と代数的に証明。
最小10矢型のHilbert級数は
$1/((1-t)^2(1-t^2))$（偶奇を含む）。
これは**分解の完全性を仮定した数値帰結**であり、
AS–Gorenstein性・実現の検証とは異なる。
独立SymPy有理母関数計算はPASS。
(2) square avatarの二pencilの評価列から、
非被約$D$も含め
$\operatorname{rk}\mu_G=3\iff P\simeq GF^{-1}$
（反対側は$P\simeq FG^{-1}$）を独立証明。
両方が階数3でも分類から除外しない
（C \`lem:qa-as10-rank-wall-pencils\`）。
(3) Keller–Yangの一次資料Theorem 6.2の
(c1) loopなし、(c2)mutation頂点を通る2-cycleなし、
(c3)potentialの巡回表示の局所仮定を確認して
Cの \`lem:qa-as10-keller-yang\` に明示。
(4) 原PDF命題8.1・52.1に沿い、
ASsq/ASrsqのNoether性からcoherent導来Morita同値
（C \`prop:qa-as-avatar-coherent-morita\`）、
固定mutation先の左右Noether性と
$\Qgr A'\simeq\Qgr A$, $\qgr A'\simeq\qgr A$
（C \`prop:qa-as10-noetherian-qgr\`）の証明を追加。
**これはAbel圏同値であり、選んだ構造対象を保つ
O-marked pointed同値を自動的には与えない。**
Noether/qgrの証明は原PDFの論証を取り込んだもので
完全な独立再検証済みとはせず、
cornerのcofinalityとAZ再構成の仮定は次の詳細監査対象。

**二重mutation壁とcubic導来非同値の完全判定（C v3.4）。**
原PDFの§§15.4・19--21・42を
\`papers/quiver-avatar/as10_mutation_classification.tex\` の
\`lem:qa-as10-double-wall-reduced-geometries\`,
\`prop:qa-as10-double-wall-characterization\` と、
新設の \`papers/quiver-avatar/cubic_obstruction_all_loci.tex\` の
\`thm:qa-as-cubic-reachability\` に統合した。
二標準mutationがともに最小10矢となる交点
$Z=D_F\cap D_G$は、$0\ne P\in\Pic^0(D)[2],\,G\simeq FP$と同値。
多重次数零から全既約成分の$(a,b)$が$a=b$となり、
非零2捩れの存在から二重$(1,1)$、cuspidal、
接する二成分を排除するので、$D$はsmooth/nodal/I2の三型だけ。
**二つの壁のscheme-theoretic横断性（C v3.4、今回の補強）。**
滑らかな$D=E$と次数二$F$を固定し、
$\eta=GF^{-1}$、$P$を$\Pic^0(E)^2$の変数とすると
二壁は$\eta=P$、$\eta=P^{-1}$という被約Cartier因子である。
二捩れ点での接方程式$v-u,v+u$のJacobian行列式は$-2$。
従って交点は横断・被約で、滑らかな楕円族では非零$E[2]$による
有限étale三次被覆を与える（C prop:qa-as10-double-wall-transversality）。
固定されたnodal/I2曲線でも$\Pic^0(D)=\Gm$ゆえ
交点は各一つの被約点で横断的である
（C cor:qa-as10-singular-double-wall-transversality）。
これは標識付きavatarの固定曲線パラメータでのscheme主張であり、
内在O-markedスタックとの全忠実比較は未証明。
幾何上の結果自体の優先権・新規性は未確認。
この幾何同型類は既存のnoncubic二根対avatarの全幾何同型類と一致するが、
元AS $\qgr$と内在O-marked H2 heartの同値は別問題。
より強く、**ASsqの商Abel/導来圏がどれかのcubic ASと同値となるための
必要十分条件は$Z$の外側にあること**。
滑らかな$Z$では任意のcubic候補foundationを
Serre数値格子・determinant・線束乗法の非可逆性で排除し、
nodal/I2では$\mu_2$-torsorを保つ平滑化と
有限自由End代数上のexceptional perfect複体の形式持上げを用いる。
この証明は2つの特定mutationの不可能性だけからは得られない。
Serre数値作用$(S-1)^2$と2捩れの隣接乗法のparityは
\`computations/verify_avatar_cubic_obstruction.py\`で有限exact計算を実行してPASS。
当該全候補排除・平滑化の証明は原PDFから移管したものであり、
網羅的な独立再監査・外部新規性判定は未実施。
**Ginzburg完備化・mutationの一次監査（C v3.4）。**
有限大域次元二のdirected$B$について
Keller (2011, Thm 6.10) のundeformed CY completion
$\Pi_3(B)=T_B(\Theta)$とrelation Ginzburgの準同型を
厳密な適用範囲で再確認した。
$\Theta=RHom_{B^e}(B,B^e)[2]$の各$m$次tensor成分は
$RHom_B(E_i,S_B^{-m}E_j[2m])$に対応し、
$m\ge1$なら$j+4m>i$なので全整数の前向きExt消滅を
利用できる。内部正次数による完備化は次数ごとの直積となる。
Keller--Yang (2011, Thm 6.2)には
入力potentialが**reduced**である条件も必要であり、
relation-dualの長さ三以上からこれをCに明記した。
(c1) loopなし、(c2)指定mutation頂点の2-cycleなし、
(c3)cyclic representativeの条件と
Ginzburgの集中を別々に検査。
これらは引用する定理の適用と局所DG argumentの監査であり、
全AS正則性・全QP相対stackの形式証明ではない。
次の重点は既存AS分類のDG/Ginzburg比較の残る詳細監査、
本定理の非被約底・全QP stackへの相対化と、
AS $\qgr$から内在O-marked心へのpointed認識。

**従来の曲線上の幾何・境界障害は以下に保持する。**
添付の大川--植田「非可換二次曲面の二つの反標準avatar」v7（Parts I--II）から、Cの比較に不可欠な曲線上の理論を
`papers/quiver-avatar/square_rotated_foundations.tex` と
`papers/quiver-avatar/canonical_helix_complexes.tex` に証明付きで統合した。
反標準Cartier因子の部分曲線・Picard消滅、二pencilによるsquare/rotated相互再埋込み、
4×4・2×2の評価行列と有限directed foundationの余核復元、
四つのcanonical exact complex・全整数周期の線束式と曲線上の前向きExt消滅を含む。
これらの曲線上の証明と、新設したAS-helix分類・mutationの証明を組み合わせた。**元のO-marked heartのpointed同値はなお別問題**であり、全相対分類・独立全面検証も未完了。
新命題 `prop:qa-nodal-resolution-odd-exceptional-degree`（`papers/quiver-avatar/nodal_resolution_obstruction.tex`）で、
共有根の相対A1商上の反不変reflexive moduleは最小解消の例外P1上で次数1になり、
垂直Cartier twistでも次数の奇偶が保たれると示した。
したがって**同一一径数基底上でのA1最小解消だけでは、多重次数零の相対Picard線束化は不可能**である。
局所chartと奇偶恒等式は `computations/verify_nodal_exceptional_parity.py` に保存した。
**相対spectral二次積の精密化（C v3.4）。** 二形式族の反不変層 $M$ とその積
$\mu:M\otimes M\to O_C$ について、任意の基底（非被約底を含む）で
$\operatorname{im}\mu=(f_1,f_2,y)$、$\operatorname{coker}\mu\simeq O_{V(f_1,f_2)}$ を証明。
各squarefree幾何fiberで積欠損長はsmooth/nodal/I2の順に $0/1/2$、
積の随伴射 $M\simeq M^\vee$ は同型である。
nodal極限は $\nu_*O_{\mathbf P^1}(-1)$（単純）、I2極限は
$\nu_*(O_{\mathbf P^1}(-1)\oplus O_{\mathbf P^1}(-1))$（非単純、End=$k^2$）。
曲線固定で二次積まで保存すると自己同型はそれぞれ
$\mu_2,\mu_2^2$（C prop:qa-spectral-product-defect、
thm:qa-spectral-three-fiber-limits、cor:qa-spectral-pair-finite-inertia）。
**したがって simple sheaf の fine compactified Jacobian のみでは I2 を受けられない。**
さらに相対groupoid $\mathfrak{TF}^{quad}$ を
曲線束・有限二重被覆・相対平坦rank-one torsion-free層・
fiberwise自己双対な二次積の組として定義し、
論文Bの二形式表示商 $[P/G]$ から
$\mathfrak{TF}^{quad}$ への fppf 相対射を構成した
（C prop:qa-spectral-quadratic-stack-map）。
係数スカラー群・二形式交換・同時斉次スカラー $D$ に対する
同変性を確認した。標的のArtin性・finite type性や
この射の全忠実性、O-marked heartとの同値は未証明である。
次はこの相対射のfiber・慣性・変形・偏極条件と
noncubic O-marked stack を比較する。
既知の一般 compactified Jacobian 理論（Altman--Kleiman,
Christ--Payne--Shen）と明示積計算を区別し、新規性の包括確認は未実施。
次の実際の研究は、base change後のsemistable model・compactified Picard・elementary transformのどれで
正しい相対groupoidへ到達するかを絞り、有限foundationのSerre作用・元のAS qgr heartの比較を優先する。
この追加結果の数学的な独立全面監査、公開一次文献との包括比較、Cの全組版は未実施であり、コード・静的参照検査と区別する。

**P4のpointed認識に必要な曲線の区別（C v3.4、今回の独立結果）。**
noncubic中央二重平方環
$B_f=k[u,v]\langle c,d\rangle/(c^2-f_1,d^2-f_2)$の
可換点曲線$E_f=\{c^2=f_1,d^2=f_2\}\subset\PP^3$と、
これまで二根対avatarの構成に用いた
$C_q=\{y^2=f_1f_2\}$を区別する。
四根相異なるとき同時符号の自由対合による
$r:E_f\to C_q$は有限étale次数2のisogeny。
$E_f$には$c$符号反転・$d$符号反転のconic商から
次数二pencil $F_d,F_c$があり、
$0\ne P_E=F_cF_d^{-1}\in\Pic^0(E_f)[2]$、
$F_c^2=F_d^2=\OO_{E_f}(1)$。
一方$M_C=(r_*\OO_{E_f})^-$は非零$\Pic^0(C_q)[2]$、
$\ker r^*=\{\OO_{C_q},M_C\}$で、
$(E_f,P_E)$と$(C_q,M_C)$は双対2-isogenyを介して交換される
（C \`thm:qa-point-spectral-dual-two-isogeny\`,
\`cor:qa-point-spectral-atkin-lehner\`）。
**両曲線は一般に同型ではない。**
$f_1=x(x-1),f_2=(x-2)(x-3)$では
$j(C_q)=35152/9$、$j(E_f)=28756228/3$であり、
古典的$\Phi_2(j(C_q),j(E_f))=0$を厳密算術で確認
（C \`ex:qa-point-spectral-j-distinction\`、
\`computations/verify_rootpair_resolvent_spectral.py\`）。
これは独立な点曲線とspectral曲線の比較であり、
**AS normal helixから抽出されるavatarがどちらかを
まだ直接同定したものではない**。
従来の「二根対↔C_q avatar」の体上全単射と、
$B_f$の\emph{pointed} qgrとの直接同値は依然別問題。
**noncubic MCMから点曲線avatarの二pencilまでは直接認識できた。**
$f_1=-\ell_1\ell_2,\ f_2=-m_1m_2$として
$M_c=\left(\begin{smallmatrix}c&\ell_1\\\ell_2&-c\end{smallmatrix}\right)$、
$M_d=\left(\begin{smallmatrix}d&m_1\\m_2&-d\end{smallmatrix}\right)$
を取ると、$B_f$で$M_c^2=M_d^2=0$。
点曲線$E_f$上のrank-one右kernelから
$\kappa_c,\kappa_d:E_f\to\PP^1$が定まり、
それぞれのconic商$Q_c,Q_d\simeq\PP^1$と一致する。
従って$\kappa_c^*\OO(1)=F_c$、
$\kappa_d^*\OO(1)=F_d$を直接証明
（C \`prop:qa-point-mcm-matrix-pencils\`）。
**二つのrank-three隣接積の像も直接同定した。**
noncubic normal helixの隣接合成
$\mu_c,\mu_d$の像は、それぞれ二つのconic商
$F_c,F_d$の対称積
$\operatorname{Sym}^2H^0(E_f,F_c),\operatorname{Sym}^2H^0(E_f,F_d)$の
$H^0(E_f,\OO_{E_f}(1))$内の像と一致し、
\[
  U_c=\langle u,v,c\rangle,\quad
  U_d=\langle u,v,d\rangle,\quad
  U_c\cap U_d=\langle u,v\rangle,\quad
  U_c+U_d=(B_f)_1
\]
を得た（C \`prop:qa-point-mcm-composition-veronese\`）。
Aの\`cor:normal-cubic-defect\`のmatrix-factorizationによる
積の計算を利用しており、両隣接積の階数3と
conic Veronese像の一致は明示的に確認した。
**全noncubic幾何点のpointed認識（C v3.7）。** 二つのsquarefree二次形式の根対は、相異・一根共有・一致をすべて許す。点曲線$E_f=\operatorname{Proj} B_f^{\mathrm{ab}}$は二conicのファイバー積$Q_c\times_{\mathbb P^1}Q_d$で、smooth/nodal/$I_2$の$(2,2)$ Cartier因子になる（C lem:qa-pointed-all-rootpair-geometry）。$X_c,X_d$の可換化によるspinor section moduleと、四頂点Endの全Hom・全合成の同型は三型すべてで成立する（C lem:qa-pointed-abelianization-four-end）。square avatar $(E_f,F_c,F_d,P_E)$の指定mutation後、比較すべき四項は$(H_0,\ldots,H_3)$でなく**$(H_1,\ldots,H_4)$**。この位相でSerre完成・AZを使い、全noncubic $\mathcal H_2(k)$について$(\qgr B_f,\pi B_f)\simeq(\qgr A_{\rm av},\pi e_1A_{\rm av})$という**体上のO-pointed exact同値**を原稿で証明した（C thm:qa-point-all-noncubic-pointed, cor:qa-point-all-noncubic-h2）。$C_q$のspectral avatarや$\Sigma_2$の別avatarとのpointed同値、非被約基底の相対groupoid・慣性・descentは未解決。三型の有理係数モデルで次数1–2の厳密計算をPASSしたが、数学的全証明の独立全面監査・新規性・組版は別状態。

**順序付き分解普遍族の相対有限End（C v3.7）。** $S=k[\ell_i,m_i,(\det\ell\,\det m)^{-1}]$（二組の独立一次形式）上で、四項$(\mathcal B,\mathcal X_c,\mathcal B(1),\mathcal X_d(1))$の有限graded directed Endと$E_S=Q_c\times_{\mathbb P^1}Q_d$上の$(\mathcal O,F,F^2,F^2G)$のEndを、**任意の$S$-基底変更（非被約も含む）と可換な代数同型**として証明した（C prop:qa-point-relative-split-root-end）。被約でsmoothな普遍底で有限表示行列の全幾何fiber階数が一定であることから局所分裂を得て、その後に非被約底へ引き戻す。これは有限Homと全積の相対同型であり、相対$\qgr$ heart・Serre根・AS被覆の同型や、根の順序を忘れるstack降下はまだ証明していない。

**四頂点のBrauer重みと相対Azumaya-Morita表示（C v4.1）。** 二conicの次数一束$N_i$と階数二の$V_i=q_{i*}N_i$から、相対双対化により$N_i^2\simeq\mathcal O_{Q_i}(1)\otimes\det V_i$を証明。$H=\mathcal O_{E_f}(1)$とし四項を$(\mathcal O_E,F,H,HG)$へdeterminant正規化すると、$\Gm^2$-gerbeの重みは$((0,0),(1,0),(0,0),(0,1))$。したがって頂点のAzumaya Brauer類は**$(0,\alpha_c,0,\alpha_d)$**。各$T_{ij}=\pi_*(L_i^{-1}L_j)$に対し、重み零の$T_{ij}\otimes W_i\otimes W_j^\vee$を係数空間$U_2$へ降下させると、全合成を持つ$(A_i,A_j)$-双加群$\mathsf M_{ij}$を得る（C lem:qa-morita-determinant-normalization, thm:qa-twisted-four-vertex-morita）。全三退化型・任意基底変更に対応し、分岐根選択の分裂被覆ではspinor finite EndのMorita増幅と局所一致する。さらに一般点で$\alpha_c-\alpha_d\neq0$だから、二根対交換は**頂点固定のMorita自己同値には降下しない**（C cor:qa-morita-ruling-exchange-phase）。適切なmutationとpointing調整は必要条件だが、その相対的存在は未証明。先行入力はBergh--Schnürer 2021の一般gerbe重み分解・twisted Morita、今回の新しい部分は特定四項の重み・双加群合成と障害の適用。有限End・相対AS completion・相対pointed qgr・全stack群oidを区別する。整数重み・Morita積の有限計算は実行PASS。全数学的独立全面監査・LuaLaTeX組版・新規性網羅調査は未実施。

**一般noncubicのperiod-indexと二つの四重被覆の識別（C v4.2）。** 独立な二形式の普遍係数体$K_{12}$で、二conicのBrauer類の差$\beta=\alpha_c-\alpha_d$はAlbert 6次元形式$q=\langle a_c,\Delta_c,-a_c\Delta_c,-a_d,-\Delta_d,a_d\Delta_d\rangle$の二段階Springer剰余判定により**index 4**のdivision biquaternionを表す（C thm:qa-generic-point-period-two-index-four、先行入力 Lam--Leep--Tignol 1993 Thm 2.3、Lam 2005 Ch VI）。一般点曲線$E_f=Q_c\times_{\mathbb P^1}Q_d$の閉点は両conicを分裂させるので次数がすべて4の倍数。一方$E_f\to\mathbb P^1$は次数4、幾何次数二のpencil Picard類が$K_{12}$有理なので、**period(E_f)=2、index(E_f)=4**。smooth半周期torsor$T_P=[2]^{-1}(P)$では平行移動が二deck involutionを共役にし、実際のconic同型$Q_c|_{T_P}\simeq Q_d|_{T_P}$を誘導する。従って$\beta|_{T_P}=0$。index4から一般$T_P$は連結な次数4拡大で、$\beta$の最小次数分裂被覆（C prop:qa-half-period-conic-isomorphism）。**分岐根選択の別の次数4被覆とは非同型**。monic全根分裂族$f_1=x(x-a)$、$f_2=(x-b)(x-c)$ over $K_0=k(a,b,c)$では根選択は4つのsectionを持つ一方、二同種模型の半周期は$\operatorname{Spec}(K_0(\sqrt{c(b-a)})\times K_0(\sqrt{b(c-a)}))$と二つの非自明二次拡大に分かれる（C thm:qa-half-period-not-root-choice）。Brauer類を両方分裂させても半周期のKummer障害は残る。OU次数4射との同型・monodromyおよび相対mutation/pointingは未解決。SymPyはquartic→cubic、2-isogeny、倍算の多項式恒等式だけPASSし、index4と被覆非同型の数学的証明は原稿依存。

**共通spectral incidence上のOU/noncubic四重torsorの非同型（C v4.4）。** OU対角potentialの四固有値$x_i$、有効群$G=V\rtimes S_4$、二対分割$\mathfrak p=\{12|34\}$の安定化群$H_{\mathfrak p}$を取り、$I_{\mathfrak p}=X^\circ/(V\rtimes H_{\mathfrak p})$という自然な次数3の標識incidence基底を構成。$f_1=(t-x_1^2)(t-x_2^2)$、$f_2=(t-x_3^2)(t-x_4^2)$から、OUのspectral楕円曲線$E_{\mathrm{sp}}$とnoncubicの$C_q:y^2=f_1f_2$は**この基底上で一致**し、点曲線$E_f$はその次数2のétale被覆となる。OU四重射$Y_{\mathfrak p}=X^\circ/H_{\mathfrak p}\to I_{\mathfrak p}$とnoncubic半周期$T_{\mathfrak p}=[2]^{-1}(P_E)$はいずれも一般monodromy$D_4$だが、**有限étale被覆として非同型**（C thm:qa-ou-half-period-common-incidence-not-isomorphic）。全固有値を指定した$F=k(z_1,z_2,z_3)$へ引き戻すとOU側は自明な4点被覆、noncubic側は$F(\sqrt A)\times F(\sqrt B)$、$A=(1-z_1^2)(z_3^2-z_2^2)$、$B=(z_3^2-z_1^2)(1-z_2^2)$であり、$[A],[B]$は独立非平方。さらにOUの$J(C_q)[2]$は$F$で全4点有理的だが、noncubicの$J(E_f)[2]$は$O$と$P_E$の2点しか有理的でなく、残る二点に$\sqrt{AB}$が必要（C prop:qa-ou-half-common-incidence-groups-distinct）。従って同じspectral曲線・同じ$D_4$という群論だけではKummer類も有限群スキームも同一視できない。比較には二同種の非同型な$2$-torsion写像と、相対AS mutation/pointingを保持する必要がある。全群oid・相対$qgr$同値はなお未解決。computations/verify_ou_half_common_incidence.pyは四次式同一性、平方類の付値、OU4点の有理性、非分裂$J(E_f)[2]$判別式をSymPy厳密演算でPASS。数学的降下・新規性・LuaLaTeX組版は別状態。

上三角の双加群を合成した$\mathsf A_{\mathrm{Mor}}=\bigoplus_{i\le j}\mathsf M_{ij}$は係数空間上の**階数54の有限局所自由な通常の代数**で、零番隅は$\mathcal O_{U_2}$。全幾何fiberで階数24の基本有限End代数とMorita同値（C cor:qa-morita-rank54）。Brauer障害は通常代数の存在を排除せず、基本頂点をrank-oneのまま維持する降下を妨げる。

**P5：三者対応の相対化と境界認識。** (i) 構成済みの根対→spectral $(C,M,\mu)$ fppf相対射の全忠実性・慣性・変形と対象となるtorsion-free二次積stackの代数性を解析し、元のsquare/Σ2上の反標準avatarへelementary transformで移せるか証明する。(ii) 非cubic平方根環B_fのAS qgrとavatar由来AS代数のheartが同じO-marked対象になる必要十分条件・自己同値群/慣性を検証する。(iii) 8/10/12本矢の統一potentialの消去可能pairとスカラー慣性を正しく商に組み込み、相対モジュライ射を作る。(iv) cubicのVdB↔squareとの境界接合、P=0可換点の収縮、Σ2最深のO-marked適合性を解決する。 **Σ₂の幾何全単射をavatar由来AS代数のqgr heartの直接同定で検証すること、および節点で非自由なspectral moduleをelementary transform/compactified Picardで相対可逆化することを最優先にする。**

**直ちに着手する一手：** 共通incidence基底でOU/half-period四重被覆が非同型と確定したため、torsor同一視の試行は終了する。次は二同種$J(C_q)\to J(E_f)$の$2$-torsionにおける非同型な群スキーム写像を用い、二つのKummer classの間に残る正しい比較（pushout/connecting morphism）を特定する。加えて既構成Azumaya有限Moritaのbase-line twistsとruling交換の相対mutation・$e_0$-pointingを検証する。並行してnodalのA1反不変reflexive sheafをelementary transformしてΣ₂側Pic⁰の相対線束へ移す構成を研究する。三者対応の射・慣性に直結しない周辺計算は優先度を下げる。

## 公表用原稿の三論文体制（2026-11-22に確定）

- **A・分類：** `papers/nc-quadric-classification.tex` を主原稿として維持する。体上の全H2の定義、cubic/noncubicの構成・被覆・pointed exact同値判定と、それに必要なSerre根・AS4被覆の完全な証明を中心に据える。最初に公表可能な論文として完成させる。
- **B・内在的相対モジュライ：** `papers/nc-quadric-moduli.tex` を独立原稿として新設した。相対H2、全Artin形式認識、有限型効果性、smooth既約Artin性、framed実現、noncubic境界の相対商・慣性・good/coarse moduliと形式局所構造を扱う。Aの体上分類を引用する一方向依存を原則とする。
- **C・AS代数／avatar分類とO-marked／potential比較：** C v4.4。最小AS分解型sq/rsqとavatarの体上全単射、および独立最小AS10のmutation逆分類を中心定理として証明付きで移管。十二矢QP表示とASクラス、相対perfect族と全非被約基底、同型類と内在心のpointed同値を区別。滑らかな楕円cubicのVdB↔square公式とO保存r1商、potential→avatar一般次数4・→H2次数8を保持。noncubicの四根相異なる開の同型類全単射を共有根・一致根対にも拡張し、root pair↔smooth/nodal/I2の非零2torsion square avatar↔Bの全noncubic幾何同型類全単射を証明。中央二重平方環の可換点曲線からspectral double cover・rank-one torsion-free moduleへの相対射を明示。共有根A1で通常Pic0線束への相対延長が不可能な具体例を証明し、形式的な集合対応と相対射を区別。$C_q$・$\Sigma_2$側の別avatar qgrとの直接同値、Σ2 elementary transform、全potentialの相対groupoidが核心的未解決。 全noncubicはΣ₂のD∈|−K|, D∩S=∅, 0≠P∈Pic⁰(D)[2]の幾何同型類と全単射まで達成。元AS heartの直接比較と相対Pic⁰射は未証明。

**公表用原稿の現在の責任範囲。** 論文Aの主原稿 `papers/nc-quadric-classification.tex` は体上の強いH2の全分類・逆構成・pointed exact同値判定を中心に構成し、分類に必要な20の分割節だけを `\\input` する。論文B `papers/nc-quadric-moduli.tex` は相対H2・Artin変形・cubic/noncubic有限型効果性・Noetherian貼合せ・適合Serre根・境界相対商・慣性・good/coarse moduliと形式対、および楕円型の構造対象忘却を扱い、31の分割節を読み込む。論文Cは八・十・十二本矢、QPとavatarの表示を担当する。Aで読まない相対節の重複sourceは、Bで証明ブロック数とラベルが保持されていることを確認して整理済み。Bの相対定義節は章ラベル `sec:moduli-relative` を使用する。

**現在の検証実装。** `scripts/check.py papers` はA/B/Cそれぞれのsources検査に加え、AとBで明記した相手原稿の定理ラベルが実際の `\input` 系に存在することを確認する。ソースの実行検査およびLuaLaTeX組版は現環境で未実施。分類の有限判定では輸送子の閉剰余類性を明記し、有限停止に必要な仮定を強調した。

**依存監査の確定範囲。** BからAへの残余の17種類の定理・補題・式ラベルはAの現行分類20節に定義されている。Aの分類主定理の証明はB固有の主定理には依存しない原稿構成とした。これはソース依存の確認で、全数学的証明の独立監査とは異なる。

**次の最優先実行単位。** C v4.4では共通spectral incidence基底・四重torsorの非同型・2-torsion局所系の非同型を証明した。次はOU torsor classを二同種のKummer長完全列へ移す際の正確な障害、$T_P$上の有限Morita gluingと相対mutation/O-pointing、Serre完成を順に検証する。$C_q$・$\Sigma_2$側の別avatar比較も別課題として維持する。その上で原稿C v4.4に統合したAS↔avatar分類の残る依存を原PDFの一次証明と照合し、特に非被約D上のPic0、AS側のrank-forcing、spherical helix実現定理の適用、10矢逆mutation・Keller--Yangの仮定、相対perfect base changeを独立監査する。三稿の組版とC→B引用を修正、Belmans等の一次文献比較をA/Bへ反映、Aの退化四つ組逆構成・Bのfive-window/境界比較の監査を進める。`python3 scripts/check.py papers` と可能な環境での三稿別組版を行い、未実施は未実施と記す。P4はA/Bを公表できる状態に整えつつ、一般cubic開で具体的な比較fiberから開始する。


## 現在の到達点と未解決の核心

**体上の分類と、相対モジュライ全体の有限型代数性の証明を原稿に統合した。** cubic側はlinearデータと被約・非被約を含む全Van den Bergh許容四つ組、noncubic側はP¹上の二つの被約二点集合の非順序対で分類する。四生成・七二次関係の有限同値判定を持ち、両領域が全対象を覆う。これらは既知入力を明示した本文の証明であり、包括的な新規性確定・外部査読・形式証明とは区別する。

**内在的fppf stackと代数性の還元。** 局所有限型k-scheme上のmodule-object基底変更・descent、canonical compact圏・Serre・AZ・相対AS4被覆を定義に含める。反Serre再構成はH2↪[X3/PGL9]を全忠実にし、対角はaffineかつ有限表示。framed部分層X_asを用いてH2≃[X_as/PGL9]だが、X_as全体は有限型・滑らかな83次元スキームとして表される。`papers/moduli/relative_definitions.tex` および `papers/moduli/relative_recognition.tex`（論文B）。

**cubic領域全体のsmooth Artin開部分。** `thm:cubic-smooth-open` は、全幾何fiberがcubicとなる内在的部分スタックV_cub⊂H2が、有限型で滑らかな純次元3のArtin開部分であると示す。非線形の普遍quintuple上では相対Picard群の[−2]に沿うétale被覆で適合根を構成し、linear点は可換Qのchartで覆う。各chartの全閉点で、指定されたpointed同型を保つArtin持上げを証明する。relation schemeはU×_[X3/PGL9]Uであり、選んだ根やfoundationを保存しない同値も含む。`cor:cubic-formal-h2-abelian` により全cubic点で形式H2変形とpointed Abel変形は同値で、HH≥3=0、dim HH²−dim HH¹=3となる。noncubic境界を含む全H2の代数性は下記の有限型効果性で証明し、ambient内の開性は一致根対で否定する。

**局所代数性を支える有限型効果性。** 標準Morita根を有限型étale近傍へ代数化し、二周期cubic列の全Hom・普遍解消・相対Koszul性・homological AS4被覆を同じ開U°上に構成した。任意affine基底でD(QGr B)≃D(Mod Λ)、compact≃Perf Λ、shift≃Serre根となる。相対point curveとKeelerの消滅、regular normal族、linear閉部分の厳密なSegre表示、次数別完備化による貼合せから、任意Noetherian基底変更後のBとAの左右Noetherian性を証明した。一般Hom有限・flat basechange・fppf・AZ・全χ・全軌道と同じ根のAS4被覆が揃う。証明は `relative_cubic_tails.tex`、`relative_noetherian_patching.tex`、`relative_cubic_noetherian.tex`。元のsite外の局所環については有限型R-test上の同じ公理という範囲を守る。

**Artin変形の確立した入力。** 全H2の切断環・反Serre環はKoszul。三次まで平坦でfiberがKoszulなら全次数平坦・相対Koszulとなる。全flat Abel Artin変形にはrank24のfinite foundationとcanonical反Serre軌道環があり、偏極忘却の接核はHH¹、Abel変形はHH³=0により無障害。可換Qの標準根は全Artin変形に存在しMorita類が一意、canonical hullのAS4被覆を持つ。形式H2＝Abel、接次元9・慣性次元6。異なる根対のnoncubic点でX3はsmooth・次元83、商は次元3となる。内在H2との全Artin比較は下記の中央被覆と局所tailsによる。`relative_koszul.tex`、`artin_foundation.tex`、`artin_roots.tex`、`quadric_artin_hull.tex`。Jacobianによる全一次方向の明示構成も保持する。

**noncubic変形の具体的なétale表示。** `prop:noncubic-lagrangian-etale-slice` により、Lagrangian Grassmannian LG(4,8)の開部分を7次元群で割った商から、全noncubic点を含むfoundation変形の開部分への表現可能なétale射を得る。法軌道写像の行列式はPlücker O(3)の切断で、正規形では−32α。根対一致では対角L₀を選ぶ必要があり、別のtrace零交換根にはHH²の負方向が1次元残る。この有限代数の表示を、全fiber認識と全軌道比較を経て、下記の内在H2のatlasへ接続する。

**方法上の障害と補助定理。** 非可換P¹束の候補対角列には、全行からHomが消える非零coherent対象を持つgeometric quintupleの反例がある。これはその模型と軌道列の比較を妨げるが、BのNoetherian性を否定しない。`papers/moduli/ruled_diagonal_obstruction.tex`（論文Bへ移管済み）。有限foundationやgraded coherenceだけではNoetherian heartは従わないことも研究ノートに具体例で記した。偏極認識の有限表示局所閉条件、固定BのAS4被覆incidence、χの有限型基底変更、任意係数の構造H⁰/H¹は独立の一般補題として保持する。

**一般二周期族のcanonical AS4被覆。** `thm:universal-cubic-hull` は、geometric cubic族と実際の二周期βから、逆coevaluationの線束値写像Φ_i:S_i→W_i、Φ_i|W_i=2idと階数6の核H_iを構成する。A=T(B₁)/(H₀)は全次数projective、rank Aₙ=C(n+3,3)、双対は階数列(1,4,6,4,1)のKoszul Frobeniusであり、正則正規二次線GによるA/(G)=Bを持つ。任意Noetherian基底変更後も左右Noetherianである。まずE=B!の正規線Nを割ったP=E/(N)をprojectiveにし、PPをPへ適用してA=P!を平坦にするため、非被約基底でfiber次元一定だけに頼らない。AS4被覆は任意のβに成立するが、同じ根のSerre平方条件は独立に確認する。

**相対Picard根と全cubic族の認識。** `thm:relative-compatible-root` は非線形のsmooth reduced普遍quintuple基底上で、N=L₂L₀⁻¹の二等分とATVの相対作用から実際の二周期βを構成する。β²はcanonical四周期θにvertex scalarを除いて一致する。同じβに対応するperfect双加群のSerre比較を、有限表示局所閉の比較空間と普遍基底の被約性で証明し、その後に任意の非被約底へ引き戻す。任意の根を最初から変形可能とは仮定しない。`thm:geometric-cubic-relative-effectivity` が普遍Noetherian性・canonical tails・同じ根のAS4被覆から全相対公理を供給する。DDLで五つのhelix対象を持ち上げ、四つの矢空間と四次syzygy直線を回復することで、指定同型を保つquintuple chartのArtin持上げが得られる。

**明示noncubic表示族の全相対認識。** `thm:noncubic-relative-effectivity` は二つの非退化二元二次形式の表示スタックNpres=[P/G]から、実際のH2族を構成する。中央Clifford表示を重み付き射影スタックX=P_R(1,1,2)上の有限局所自由代数へ移す。G=⊕_{i=0}³B~(i)はtiltingではなくcompact generatorであり、そのdg Endとweighted Čechからproper性・任意導来基底変更を得る。中心有限代数上のR-flat加群のfiber-perfect持上げを用いて対角のperfect性を証明し、canonical compactのsmoothnessを確認する。traceによる同じ根のSerre平方、AZ・全軌道、Ore/PBWによる普遍Noetherianな相対AS4被覆を合わせ、全相対公理を満たす。Npresは次元1であり、noncubic点の全横断変形を覆うatlasではない。被約境界との相対全忠実性は `thm:noncubic-intrinsic-presentation-equivalence` で別に証明する。

**全noncubic点の良い根と有限型代数化。** `thm:noncubic-hh-trivial-root` は、根対を交換するtrace零対合から選ぶ適合Serre根が、全foundation変形のHH¹・HH²へ恒等に作用することを証明する。四平面Gr(4,8)の交代Gale双対として根の作用を計算し、接の正負次元(10,6)と有効基底変更Lieの(7,6)を比較する。根対非一致ではHH¹=0・HH²=3、一致ではHH¹=1・HH²=4で、いずれも負のHH部分は零となる。従って全Artin Abel変形へ根が延び、そのMorita類は一意である。`prop:hh2-etale-morita-root` と `cor:noncubic-etale-morita-root` により、全noncubic点の有限型étale近傍上で実際の可逆双加群・Serre平方同型・二項窓の比較を構成できる。このMorita根を、下記の局所環上の全軌道・中央被覆の構成へ使う。

**良いnoncubic根の中央AS4被覆。** `thm:noncubic-central-hull` は、二形式f₁=uv、f₂=(u−av)(bu−v)、θ=1−ab≠0の全配置で、従来のOre被覆とは別の六関係環A₀を構成する。g₀=uv−vuはuntwisted環で正則正規、良い根によるtwist後に中央となる。二次双対のχ=UV−VUを割ったKoszul Frobenius環のpairing行列式はθ⁴/4と−θ⁸/16。twist後の二次中心は一次元、二次反中心は零である。一般係数の厳密検算と全次数の構造証明を区別する。

**noncubic局所環上の効果性と全Artin認識。** 五頂点の非極小bar解消により、極小Betti数の変動を許して、同じ局所環上の全前向きHom・全軌道・canonical tails・Noetherian heartを構成した。二次双対の反中心消滅はgeneric cubic canonical線のnormalizerが−1となる可能性を排除し、中心直線を直和因子として延長する。閉fiberの正則性と単元minorから全次数の中央AS4被覆が延びる。指定還元同型付きArtin変形をétale foundation chartへ持ち上げると、全noncubic点で形式H2変形＝pointed Abel変形となる。非一致根対では接3・慣性0、一致では接4・慣性1、いずれも無障害。既存cubic結果と合わせ、全H2幾何点でArtin形式認識が成立した。証明は `thm:noncubic-local-tails-effectivity`、`thm:noncubic-local-central-hull`、`cor:noncubic-all-artin-h2`。

**noncubic境界を横断する有限型効果性。** `thm:noncubic-finite-type-effectivity` は、全noncubic点に実際のH2族を持つ有限型étale近傍を構成する。Lagrangian四平面の二射影M,Nに対し、Segreとの交点を除き、Cr(N adj M)とCr(M adj N)の行列式を可逆化する。全幾何fiberをcubicまたは二形式normal foundationへ認識し、同じ四項とSerre四周期から全Homを有限projectiveにする。非被約閉部分V(det M,det N)のétale相対正規形と二つのcubic開から普遍Noetherian性を貼り合わせる。全fiber Koszulを先に確認し、局所中央線をspreadして同じ根の中央AS4被覆を得る。一般のKoszul開性や無限個の開の交叉は使わない。証明は `papers/moduli/noncubic_finite_type.tex`。

**内在的な全モジュライの有限型代数性。** `thm:global-h2-smooth-finite-type` により、局所有限型k-schemeのsite上のH2は、有限型・滑らか・純次元3のArtinスタックにより表され、対角はaffine有限表示である。指定されたpointed同型を保つArtin持上げで各効果的近傍をsmooth chartとし、実際のnoncubic表示族の準コンパクト性から有限個を選ぶ。relationはU×_[X3/PGL9]Uで、根・被覆・foundationを保存しない全pointed同値を含む。X_asは有限型・滑らか・既約・純次元83のスキームとなる。一致根対では接次元が内在側4・ambient側5（framedでは83・84）なので、X_as→X3は開immersionではない。証明は `papers/moduli/h2_smooth_atlas.tex`。

**内在的な既約性とnoncubic境界。** `prop:global-h2-irreducible` は、根を選ぶ前の普遍cubic Z代数のtailsを使って実際の族を降下し、cubic開の既約性と全H2内での稠密性を証明する。したがって全H2は既約・連結である。`thm:noncubic-boundary-smooth-codim-two` により、被約noncubic境界N=(H2\V_cub)_redは有限型・smooth・既約・純次元1で、H2への正則閉埋込みの余次元は2。LGの接空間Sym²L*上で二行列式の微分は交点二線ℓ,mへのq(ℓ,ℓ),q(m,m)であり独立となる。smooth共通chartでこのscheme-theoreticな閉部分をNの引戻しと同定する。非被約testでは全fiberがnoncubicというだけではNへの因数分解は従わない。

**被約境界の相対商表示と良モジュライ。** `thm:noncubic-intrinsic-presentation-equivalence` により、局所有限型site上で Npres=[P/G]≃N が対象・pointed exact同型を含めて成立する。境界chartの相対normal tiltingと反Serre再構成から実際の族を比較し、慣性核の消滅・接全射・同次元性から表現可能étale性を証明する。非被約testも含むが、全fiber noncubicだけでNへの因数分解を主張しない。χ:N→A¹はflat有限表示のgood moduliで、χ=0はsmooth被約因子の二重構造、χ=1はsmooth chart上ac=0。全慣性は四根相異χ≠0でD8×C2、χ=0で位数32非分裂拡大、一根共有でD8、一致で((Gm⋊C2)×D8)/μ2（8成分）。一致類はBGの正則閉埋込みcodim2をなし、境界接の重みは±2、全HH²は±2,0,0、横断法二方向には連結慣性が自明に作用する。任意の代数空間へのH2の射は一根共有と一致類を同一視するため、全H2にも幾何同型類を分類する粗モジュライ代数空間は存在しない。証明は `papers/moduli/noncubic_boundary_comparison.tex`。

**DM開の粗モジュライ。** 一致類を除いた N^DM→A¹_χ は任意の代数空間に対する粗モジュライ射であり、任意の底変更後も粗モジュライである。この制限射χ_DMはgood moduliではなく、慣性射はproperでもfiniteでもない。二つの根対を順序付けたchartを [A¹/μ2] に帰着し、有限被覆を持つ商の普遍性で粗モジュライを証明する。非good性はcodim2補集合のHartogs、慣性の非proper性はDVR上で延長しない具体的自己同型による。`thm:noncubic-dm-coarse`。

**一致類に沿う形式対と局所良モジュライ。** 全慣性 H=((Gm⋊C2)×D8)/μ2 の有限成分も含むHH²作用を決定した。トーラスの非零重み部分と零重み部分による標準的分裂を用い、境界接を(a,c)、法方向を(x,y)とすると、トーラスの重みは(2,−2,0,0)、二つの符号は法方向に−Id、u,v交換は(a,c)を交換して法方向に−Id、ruling交換は境界接に−Id・法方向の交換として作用する。ruling交換は相対mutationで全Artin変形上に同定する。非標準的な形式対は ([Spf k[[a,c,x,y]]/H], [Spf k[[a,c]]/H]) で、境界はx=y=0、不変式環は k[[ac,(x+y)²,(x−y)²]]。AHRの共通étale商近傍はsmoothな3次元good moduliを持つ。これはH2のZariski開や全体のgood moduliの存在をまだ意味しない。`prop:noncubic-coincident-full-normal-representation`, `thm:noncubic-coincident-formal-pair`, `cor:noncubic-coincident-polynomial-invariants`。

**残る比較と次の課題。** 境界の相対商表示・DM開の普遍的粗モジュライ・全有限成分の法表現・一致類に沿う形式対は証明した。次は、共通étale近傍のgood moduliをH2の開部分または全体へ降下できるかを調べる。全H2のgood moduli spaceの存在は未確定であり、全H2の粗モジュライ不存在とは別の問題である。X_asの局所閉性と偏極認識方程式、Q_fndとの全体の相対groupoid比較、任意Noetherian基底で素朴に同じAbel公理を課す関手と[U/R]の一致も残る。公表前の一次文献比較・証明監査・組版を続け、包括的新規性・外部査読・形式証明とは区別する。

**別稿と研究間の関係。** `papers/nc-quadric-avatar.tex`（v0.1）は有限foundationの8/10/12矢chart、重み四QP、反標準avatarを扱う独立論文である。体上の表示と相対H2の実現条件を区別する。cubicから全noncubic点へのsmooth proper dg特殊化と全次数平坦反Serre族は構成済みだが、個々の既存dg特殊化の内在H2認識は、その族ごとに確認する。詳細な主張状態は下の表と研究ノートを正本とする。

検証範囲・再生成手順は [研究ノート](notes/research_notes.md#検証範囲と再現手順)、文献の仮定・規約は [文献比較](notes/literature.md) に集約する。

## 1. 恒常的な研究原則と保存許可

この節は研究一般の原則であり、第2節以降の研究固有の計画と区別する。

1. 数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性から研究全体の価値を最大化する。方針は柔軟に変更し、変更理由と元の目標の達成部分・残存部分を、現時点で有効な説明へ書き換える。履歴を蓄積しない。
2. 証明済み、追加仮定付き、証明未完成、予想、計算的観察を区別する。主要主張の仮定・依存結果・証明箇所・未解決点を明記する。原稿に証明があること、今回その論理を点検したこと、計算・形式証明器を実行したこと、新規性を確定したことは別である。誤りは依存する本文・要約・方針・hubにも反映する。
3. 重要な文献は一次資料で仮定・適用範囲・書誌を確認し、Introductionで既知結果と本研究の関係を具体化する。未確認の文献内容や新規性を推測しない。他研究の結果を使う際は定理、仮定、出典と必要なcommitを記す。文献PDFや検索結果を大量収録しない。
4. 原稿は原則日本語LuaLaTeX。主原稿は本文のある `papers/nc-quadric-classification.tex` とし、research-hubのテンプレートと組版設定を参照する。有効な公表価値のある成果と必要な証明を論理的な順序で統合する。未完成箇所は明示し、追記式の版別原稿や重複本文を増やさない。独立論文を分ける場合は役割を説明する。
5. 研究ノートには論文外の着想、例、反例、計算、失敗した方法の本質的障害、文献比較、再取得困難な情報を整理する。本文に十分な証明がある事項は参照する。作業日誌、旧会話、試行履歴、解決済みtodoは不要である。
6. 現行の方針・ノート・論文と最小限のコード・入力・文献・再現手順から自己完結して再開できるようにする。旧bundleや会話を再開の前提にしない。数学的内容や検証可能性を損なってまでファイル数・容量を減らさない。旧ZIP、旧版原稿、バックアップ、ログ、cache、組版中間物は追跡しない。必要な証明書・再取得不能な入力は保持する。Git履歴を改変しない。
7. 研究の区切りごとに承諾なく通常コミットし、`main` へ反映する。長時間作業でも前回の成功したmainへのpushから長くても約15分以内に保存する。切りのよいところでは早めにpushし、証明途中でも確定部分と未解決箇所を明示して保存する。他の作業者の変更を保持し、force push・GitHub Actionsの追加や起動は行わない。PDFは原則追跡せず、LuaLaTeX・latexmk・SyncTeX・VS Code設定を保持する。改名時はinput、文献、root指定、README、方針、設定を整合させる。GitHub保存が成功すればLibraryへの定常的な二重保存やZIP作成はしない。失敗時の緊急保存または別途依頼時のみLibraryを使い、既存Libraryファイルを無断で削除しない。
8. 日付・版と参照・記法・主張状態を一致させる。必要な範囲の組版・計算・参照点検を行い、生成、論理点検、計算、組版、GitHub反映、Library保存、hub更新を別々に確認する。先に本repoを保存し、その内容に基づいてresearch-hubの該当項目を更新する。最新hubと並行変更を保持し、概要・主要到達点・確実性・核心・次の一手・依存関係・正本・実際の資料確認日を反映する。詳細todoや証明を複製しない。hub更新に失敗しても成果は保存し、未反映内容と理由を報告する。

実行規則は [AGENTS.md](AGENTS.md)、全体の入口は [research-hub](https://github.com/uedakazushi/research-hub)。日常todoは本研究と分ける。

## 2. 研究固有の目標と対象

**最終目標：強いクラス H2 の全対象を、構造対象を保つ exact 同値で分類する。** 対象は `(C,O)` のみ。`O` はGabriel–Krull商でrank one torsion-freeかつexceptional。`Db(C)`はHom有限でSerre関手`S`を持つ。次を同時に満たすexact自己同値`s`とambientが**存在**することを要求する。

$$
s^2\simeq S^{-1}[2],\qquad (O,s)\text{ is Artin--Zhang ample},
\qquad B(C,O,s)\simeq A/(g).
$$

`A`は左右noetherian quadratic Koszul AS-regular、global dimension・Gorenstein parameterともに4、解消型`(1,4,6,4,1)`。`g∈A₂`は左右正則正規。`s`、根同型、`A`、`g`、商表示は追加標識としない。H2の添字は超曲面次数2を表し、可換quadricの反標準次数は8である。

**定義上の修正理由。** cubicのquadratic envelopeをそのまま使うと、quadric方程式自身が二次関係に含まれる。標準可換例でも二次関係は7本で、AS4の6本と一致しない。そのため、通常の二次包絡のAS正則性を、二次AS正則被覆の存在へ置き換えた。元の目標である「Oだけを指定し、sとambientは存在する性質」は保持する。この意味で被覆と平方根を忘れた全分類を、主定理で与える。

右加群規約：`a∈B_m,b∈B_n` の積は `a*b=s^n(a)∘b`。cubic原稿の表示された積とは反対の規約であり、Nakayama公式等を無検査で移植しない。

## 3. 到達点と確実性

以下は主原稿に証明を置く結果。既存文献の一般定理を明示して適用している。新規性の包括的確認、外部査読、形式証明は未実施。

| 結果 | 仮定・範囲 | 主原稿の所在 |
| --- | --- | --- |
| 反SerreのAZ豊富性 | 一次生成と元のAZ豊富性から偶数部分列へ | `lem:ample-square-from-generation` |
| 大域次元2 | heart上exactなSerre平方根が存在 | `prop:gldim-two` |
| 切断環はdomain、負切断は零、Hilbert関数 `(n+1)^2` | H2公理。domainはrank-one purityから、Hilbertは被覆から | `lem:sections-monic`, `prop:reconstruction` |
| 通常の二次包絡はambientにならない | 任意の型14641環の正則正規二次商 | `cor:quadric-envelope-fails` |
| 固定Bの被覆を `Gr(6,K)=P(K*)` に還元 | B二次、quadric Hilbert級数。AS条件の下で三次の左右乗法rank4が正規性と同値 | `prop:ambient-hyperplane` |
| 固定可換B上に非一意なambient | `a∈k×` のOre族。quotient mapを固定した被覆が異なる | `prop:ore-ambient-family` |
| 滑らかな可換対象はQに限られ、Oは線束 | 滑らかな射影整曲面。一次生成とB1=4,B2=9だけで認識 | `lem:commutative-marking-line`, `thm:commutative-recognition` |
| 可換Q上の適合する平方根は4種類 | 代数閉体・標数0、根同型は固定しない | `thm:commutative-four-roots` |
| 平方根+ampleだけでは四生成性が出ない | 因子交換と `O(2,0)` の例では一次切断数3 | `ex:commutative-unbalanced-root` |
| 滑らかな楕円型Sklyanin quadricはH2に属する | k=C、通常の4次元Sklyanin、τ無限位数、z+τが非2捩れ。全切断環・Gabriel–Krull条件まで確認 | `prop:sklyanin-h2` |
| 可換Qの圏と同値でないH2対象が存在する | 上記pencilのz=τ。既知の単純対象の自己Euler特性2を使用 | `prop:sklyanin-genuinely-noncommutative` |
| 全H2のpointed exact同値判定 | 反Serre環のGL9軌道、または四生成の関係に対する有限で停止するGL4剰余類反復。追加の開条件なし | thm:antiserre-invariant、prop:first-orbit-finite-equivalence |
| 全H2の分類 | linear・全許容四つ組の有限同値商と、非cubicの二点集合対のPGL2商との非交和 | thm:complete-h2-classification |
| 中心standard表示の比較 | 構造対象は添字0、平方根は二添字移動。Sklyanin型は適切なrulingでcubic | prop:standard-pointed、prop:sklyanin-cubic-ruling |
| 固定ambientの中心化の障害 | 適合根を保つ自己同型Zhang twistでの中心化にはnormalizerが次数スカラーであることが必要。Ore族で失敗 | prop:central-twist-obstruction、ex:ore-central-twist |
| Sklyanin型の内在的な楕円商 | 反Serre環の中心一次部分から楕円商を回復 | prop:sklyanin-antiserre-center |
| 構造対象を保存する導来同値はexact | 反Serreの負シフトからの導来Homで標準heartを認識 | cor:pointed-derived-exact |
| 全H2の四周期AS正則Z-algebraによる表現 | 正規切断から標識と反Serre関手を移送。中心性、standard性、(*)は不要 | thm:normal-helix |
| cubic型の判定と残る場合 | 隣接合成が階数4ならcubic。階数3の場合は偶数添字から距離二の生成元と関係が一つずつ加わる | cor:normal-cubic-defect |
| 最初の軌道対象とcubic被覆 | 最初のシフト先は内在的。二型とも階数3のH2例はどのcubic表示でも被覆不能 | prop:first-orbit-object、thm:cubic-coverage |
| 全許容四つ組の逆構成 | 整・被約・非被約の全(2,2)曲線型。二周期の平方と反Serre移動を比較し、全H2公理を確認 | thm:all-admissible-inverse |
| 全cubic表示のeven partのdomain性 | PresottoのZ-domain定理を適用。曲線の整性・被約性は不要 | prop:all-quadric-even-domain |
| 固定BのAS被覆の有限判定 | Bが左右noetherianな二次Koszul。四次以下の積と二次双対の次元・Frobenius性を判定 | thm:finite-ambient-test |
| 固定Sklyanin pencilの有限比較 | Δの単射性の開領域。∂の単射性は無限位数で自動的。厳密有理数一点で非空性を検証 | prop:pencil-finite-candidates、prop:pencil-tangent-generic |
| 重み付き四周期環からの逆向き還元 | 仮定した単純分解から偶数環のKoszul性を証明。root・domain・非有限長の切断・有限被覆判定に還元 | prop:weighted-even-koszul、prop:weighted-inverse-reduction |
| 四変数多パラメータskew polynomialの正規二次切断 | 退化込み。非cubic一点と、パラメータ r² を逆元で割ったcubic族 | thm:multiparameter-quadric-classification |
| 全非cubic対象の分類 | standard・non-standardとも同時Zhang twistで中央二重平方環へ帰着。二点集合の非順序対で同値判定 | thm:noncubic-classification |
| non-standard適合表示の制約 | 両階数3の場合、二つの根対が一致する一点だけ | thm:w-compatible-singleton |
| 交差項を持つOre環の正規切断 | 退化込み。可換類と、二つの二点集合で判定される非cubic族 | prop:ore-normal-quadrics、thm:ore-anticommuting-central |

スタックに関する結果は、次の範囲で証明済みである。

| 結果 | 仮定・範囲 | 主原稿の所在 |
| --- | --- | --- |
| noncubic表示商、慣性、μ2² gerbe、good moduli | Npres≃被約境界N、smooth finite type、dim1。Nのcoarse algebraic spaceは存在しない。非被約testで全fiber noncubicというだけではNに因数分解しない | `prop:noncubic-presentation-stack`, `prop:noncubic-sign-gerbe`, `prop:noncubic-good-moduli`, `thm:noncubic-intrinsic-presentation-equivalence` |
| noncubic表示族の局所正則切断 | étale局所に適合根の代数表示を構成。全次数有限自由・底変更整合 | `prop:noncubic-relative-regular-cut` |
| finite foundationとHochschild計算 | F=[A64/(G/K)]はsmooth finite type、dim3。HH≥3=0、dimHH²−dimHH¹=3 | `prop:foundation-stack`, `prop:foundation-hochschild` |
| cubic geometric開部分 | `[Gr(2,8)_geo/(PGL2)^3]`、smooth finite type、dim3。隣接二因子の縮約条件が必要 | `prop:cubic-foundation-open` |
| 内在的二rulingと相対交換 | 全H2の二foundationを認識。F0上で二短完全列の交換がcoherentなS2作用を与える | `prop:intrinsic-ruling-pair`, `prop:relative-ruling-involution`, `prop:ruling-involution-mutation` |
| Q_fndと全幾何点groupoid | Q_fnd=[F0/S2]はsmooth finite type、dim3。F0→Q_fndは有限étale二重被覆。H2(k)→Q_fnd(k)は全充満 | `cor:h2-point-groupoid-foundation` |
| 実現集合Yの成分とcubicの稠密性 | Y⊂underlying(Q_fnd)はcubic非空開Cを含む。誘導位相で既約・連結各1 | `prop:h2-component-density` |
| 各noncubic点へのcubic特殊化 | アフィン直線から有限個の点を除く。rank24有限自由代数族、全幾何fiberがH2由来。もう一端は可換Qを選べる | `prop:h2-line-degeneration` |
| foundation族の相対smooth proper性 | 有向四頂点の有限な相対bar分解で対角がperfect。構造対象e0Λも相対perfect | `lem:foundation-relative-smooth-proper` |
| 二次Veroneseの相対提示 | 一般の二次環の偶数Veroneseは全次数で二次。相対平坦で全幾何fiberが二次なら族も二次。H2の反Serre環は九生成元・五十六二次関係 | lem:relative-quadratic-veronese, cor:h2-intrinsic-antiserre-quadratic, lem:relative-quadratic-from-fibers |
| cubic・noncubic・退化の完全二次提示 | 両表示chartとcubic→全noncubic退化のR全次数が二次関係から復元、任意底変更に整合 | cor:cubic-relative-full-quadratic-presentation, cor:noncubic-relative-full-quadratic-presentation, cor:line-full-quadratic-degeneration |
| noncubicの固定Grassmann affine cell | 二形式の6係数をGr(56,81)の1つのcellへ局所閉埋込み。固定25列のminorは±1、残り56列から係数を多項式で回収 | prop:noncubic-grassmann-explicit-cell; computations/verify_noncubic_antiserre_pivots.py |
| 型別の表示stack（同じ幾何点） | C⊔Npres は有限型Artin、全H2幾何点と慣性を持つがcubic→noncubicを特異化できず、成分数が人工的に2 | prop:split-h2-presentation-moduli |
| 三次Hilbert値だけを課す相対stack | rank(L3)=176の局所閉X3⊂Gr(56,81)。[X3/PGL9]が有限型Artinで、全H2反Serrechart・退化族の射を受ける。det正規化で普遍環も降下 | prop:truncated-antiserre-moduli-stack |
| 二根対一致点の形式的相違 | X3商のH0接は84−79=5、Q_fndはdim3+Lie慣性1=4。両者の形式近傍は非同値 | prop:truncated-versus-foundation-tangent |
| noncubic 反Serre環のKoszul性と一次変形 | 二重平方環は二次 Gröbner (PBW) ⇒ Koszul。偶数Veronese・Zhang twistもKoszul。Koszul Hochschild双加群解消から三次平坦な一次二次関係変形は全次数平坦 | prop:noncubic-antiserre-koszul, lem:koszul-first-order-degree-three |
| HH¹/HH²の厳密な計算 | 内部次数0で三基準点のHH¹=1,1,2、HH²=3,3,5。一般Euler次数導分はHH¹に残るがPGL9で除く | thm:noncubic-hh01-hh2 |
| 三次Hilbert条件の2-jet | 横断部分2,2,3次元の二次障害が恒等零。基底・基底二項和への有理補正を全整数検証。任意横断方向がk[t]/t³へ三次Hilbert flatに持上がる | prop:noncubic-transverse-second-order; computations/verify_noncubic_second_order.py |
| noncubicの接空間と三次Hilbert条件 | 三代表点でPGL9軌道＋六係数接像は標数零でrank81。三次Hilbert階数rank176の線形化は法101でrank1317,1317,1316。有理核の整数検証により標数零で接次元=83,83,84 | prop:noncubic-third-degree-tangent; computations/verify_noncubic_degree3_tangent.py |
| H2関係像の構成可能性・既約包絡 | cubicのframed関係像の被約閉包Z2は既約PGL9不変有限型。H2全幾何点は[Z2/PGL9]に含まれ、cubic像が稠密。Z2の全点がH2とは未主張 | prop:h2-constructible-relations-and-irreducible-closure |
| pointed慣性とdegree gerbe | Aut_gr(R)/Gm_degree≅Aut_pt。rank9・rank25の行列式線束でgerbe中立化 | `lem:pointed-degree-scalar`, `prop:antiserre-gerbe-neutral` |
| 全Artin Abel変形のfoundation・canonical反Serre・AZ | DDのgeometric helix変形定理と有限冪零フィルター。偏極忘却の接核はHH¹、Abel変形は無障害 | `thm:artin-foundation-lift`, `cor:artin-polarization-retraction` |
| 非一致根対の関係式空間の滑らかさ | 一根共有も含む。X3はdim83で滑らか、PGL9商はdim3で滑らか。H2適合部分の開性は別 | `cor:artin-noncubic-relations-smooth` |
| 局所基底上の全有限型tailsとHom | 全有限型変更で左右Noetherian・全χ・AZ・fppf降下・全coherent Hom有限とflat basechange | `thm:quadric-local-finite-type-abelian-system` |
| 任意affine基底のcanonical導来比較 | Noetherian性不要。四項tilting、全helix・矢・shift・Serre・導来基底変更 | `prop:quadric-canonical-cubic-tails` |
| Noetherian基底上の全相対認識 | Bが左右Noetherianなら全有限型変更で相対H2の全公理。全局所Rにも適用、siteの範囲を区別 | `thm:quadric-noetherian-relative-promotion` |
| 一般cubic族の普遍row/column Noetherian性 | 二周期不要。任意可換Noetherian基底変更、正規線族の頂点twist、linear/nonlinearの形式的貼合せ | `thm:relative-geometric-cubic-noetherian`, `thm:patch-normal-family` |
| 一般二周期cubic族の相対canonical AS4被覆 | 任意の実際の二周期β。逆coevaluationの核、全次数projective・左右普遍Noetherian。Serre平方条件は別 | `thm:universal-cubic-hull` |
| 一様cohomologyと全χ | 同じNoetherian affine基底でHom有限・Serre消滅・AZ・全χ_q | `lem:relative-cubic-coherent-cohomology`, `lem:relative-cubic-global-chi` |
| 任意係数の構造対象コホモロジー | 任意affine底変更・任意NでH⁰=N⊗B_n、H¹=0（全n） | `cor:relative-depth-three-coefficients` |
| Artin witnessの相対H2族への昇格 | 根と全軌道AS4被覆が入力。全有限型基底変更のcompact/Serre/AZ/被覆を確認 | `prop:artin-witness-relative-promotion` |
| 可換Qの標準Serre根の全Artin存在・一意性 | HH²・HH¹への作用が恒等。exact ampleな根のMorita同型類が一意 | `cor:quadric-exact-root-all-artin`, `cor:quadric-root-unique-all-artin` |
| 可換Qの全Artin変形の相対H2実現と形式変形同値 | 二周期canonical hullによる相対AS4切断と昇格。無障害、接9・無限小自己同型6 | `thm:quadric-all-artin-h2`, `cor:quadric-formal-deformation-equivalence` |
| 全cubic点の形式H2＝Abelとsmooth開部分 | 相対Picard根とquintuple Artin持上げ。有限型・smooth・純次元3。noncubicは含めない | `thm:cubic-smooth-open`, `cor:cubic-formal-h2-abelian` |
| noncubic全変形のLagrangian étale表示 | LG(4,8)の開と7次元群の商。全noncubic点を含むfoundation開への表現可能étale射。根対一致での良い選択と反例を分離 | `prop:noncubic-lagrangian-etale-slice`, `rem:noncubic-offdiagonal-root` |
| 楕円型の全O標識と忘却判定 | δ≠0、η∉Zδ。全Z²標識、有限自己同型群を含む同値式。非捩れで可算無限、捩れで有限 | `thm:elliptic-marking-lattice-fiber` |
| 全noncubic点の良い根とétale代数化 | trace零交換根のHH¹・HH²恒等作用、全Artin Abel変形への一意延長、有限型étale近傍上の実際のMorita根。被覆の全Artin認識は下記の別定理 | `thm:noncubic-hh-trivial-root`, `cor:noncubic-root-all-artin`, `cor:noncubic-etale-morita-root` |
| 良いnoncubic根の中央AS4被覆 | θ≠0の全配置。六関係の新しいambient、twist後に中央、二次中心1・反中心0 | `thm:noncubic-central-hull`, `lem:noncubic-no-quadratic-anticenter` |
| 五頂点窓と局所canonical tails | 同じNoetherian局所基底上で全軌道自由・Noetherian heart・任意導来基底変更。極小Betti数の固定を不要にする | `lem:five-window-bar-lifting`, `prop:five-window-canonical-tails`, `thm:noncubic-local-tails-effectivity` |
| 局所中央被覆と全noncubic Artin認識 | regular local foundation chartのgeneric cubicを使って中心線を延長。全Artinで形式H2＝Abel、無障害。有限型開への延長は `thm:noncubic-finite-type-effectivity` | `thm:noncubic-local-central-hull`, `cor:noncubic-all-artin-h2` |
| 中央二次元の全次数正則性の有限型一様化 | P=E/(φ)の次数0–4が有限projective、P₅=0、指定局所環でφ正則。EはR[φ]上有限で、一つの開で全次数正則・projective。Koszul性は未主張 | `lem:spread-central-regular-line` |
| noncubicを横断する有限型効果性 | 有限LG認識、全fiberから全Homのprojectivity、非被約閉部分のnormal tilting、Noetherian貼合せ、同じ根の中央AS4延長 | `thm:noncubic-finite-type-effectivity` |
| 全内在的H2の有限型代数性 | 有限型smooth Artin、純次元3、affine有限表示対角。指定pointed Artin同型を保つatlas | `thm:global-h2-smooth-finite-type` |
| 全H2と被約noncubic境界の幾何 | H2は既約、cubic開が稠密。Nはsmooth既約純次元1、正則閉埋込みcodim2 | `prop:global-h2-irreducible`, `thm:noncubic-boundary-smooth-codim-two` |
| 被約境界の相対商表示 | Npres=[P/G]≃N。非被約testの対象とpointed exact同型を含む | `thm:noncubic-intrinsic-presentation-equivalence` |
| 境界の良モジュライと全慣性 | χはflat有限表示。0は二重因子、1はnode。一致を除きDM。全慣性と一致点HH²重み±2,0,0 | `prop:noncubic-good-moduli-fibers`, `prop:noncubic-all-stabilizers`, `prop:noncubic-coincident-torus-weights` |
| 全H2の粗モジュライ不存在 | 任意の代数空間への射は一根共有と一致類を同一視する | `cor:global-h2-no-coarse-space` |
| 境界DM開の普遍的粗モジュライ | χ:N^DM→A¹は任意底変更後も粗モジュライ。goodではなく、慣性は非proper・非finite | `thm:noncubic-dm-coarse` |
| 一致類の全慣性表現と形式対 | HH²=V_boundary⊕V_normal、全有限成分の作用を決定。形式対は四変数商とx=y=0 | `prop:noncubic-coincident-full-normal-representation`, `thm:noncubic-coincident-formal-pair` |
| 一致類の局所良モジュライ | 不変式はac,(x+y)²,(x−y)²。共通étale商近傍のgood moduliはsmooth3次元。H2全体への降下は未証明 | `cor:noncubic-coincident-polynomial-invariants` |
| framed実現スキームと非開性 | X_asはsmooth純次元83。一致根対でambient接次元84のため開immersionでない | `cor:global-xas-smooth-scheme`, `prop:global-h2-not-ambient-open` |
| 可換Qの全一次変形の相対H2実現 | Jacobian AS4被覆とZhang補正。任意有限次元二乗零理想へ拡張。内在接dim9、偏極付き接dim15、核dim6 | `thm:quadric-all-first-order-h2`, `cor:quadric-intrinsic-tangent` |
| 選んだSerre根の一次変形障害 | 同じ変形へのR線形dg/Morita持上げにはHH²類の保存が必要。Q上に非保存の例 | `lem:autoequivalence-deformation-obstruction`, `prop:chosen-root-does-not-lift` |

最後の障害例は、選んだ根の持上げを否定するものであり、相対H2 locusの非開性、別の根の非存在、全H2の相対moduliの非存在を主張しない。全H2の代数性はこの障害例からではなく、`thm:global-h2-smooth-finite-type` の実際のatlasで証明した。

原稿の生成・検算・組版の実施状況は [研究ノートの検証範囲](notes/research_notes.md#検証範囲と再現手順) に記す。全同値類の分類、全幾何点groupoidの実現と実現集合の誘導位相での成分数は確立した。内在的な相対fppf stackは定義・構成した。有限型代数性・既約性・被約境界の余次元二は内在的に証明した。noncubic境界の相対表示はNpres≃Nで確立し、全体のfoundation表示との相対groupoid比較は別に残る。

### 別稿の到達点と依存範囲

| 結果 | 証明の所在・確実性 |
| --- | --- |
| 有限型Artin $\mathfrak F_{\le12}$ と二つの10本矢開部分、交わりの8本矢部分 | `prop:qa-foundation-stack`, `thm:qa-foundation-open-diagram`。結合律128変数48式、核の非分解性と合併乗法の全射性を使用 |
| 最小完成矢数 $8+2(\delta_a+\delta_b)$ | `prop:qa-foundation-arrow-count`。quadratic関係の重なり零と残る2本のcubic関係を証明 |
| QPの任意基底上の消去、残る慣性、代数モジュライの開性 | `prop:qa-relative-elimination`, `prop:qa-stabilized-inertia`, `thm:qa-open-algebra-stacks`。生のQP商と代数の同型を区別 |
| 幾何的並進 $H\mapsto HP^n$ と二つのopen、square辞書 | `thm:qa-translation`, `thm:qa-open-charts`, `cor:qa-square-chart`。非被約因子・非被約基底・垂直成分・Picard類の降下を含む直接証明 |
| 最小8/10/12というAS側の意味 | `Q12Avatar2026` 定理15.3の体上分類を入力とする。全AS分類の独立再監査・相対stack同値は未完了 |
| 適合部分からの内在的忘却と全H2幾何点の10本矢被覆 | `prop:qa-compatible-forgetting`, `prop:qa-h2-normal-ten-chart`。相対適合部分の開性・任意H2族のfoundation持上げは未証明 |
| 古典12本矢とSigma2構造対象の除外 | `ex:qa-weighted-not-h2`, `ex:qa-hirzebruch-not-h2`。反Serre軌道から見えない対象によって全ての適合根を排除 |

## 4. 完全分類の達成条件

標数零の代数閉体上の、主原稿 `def:h2` の全対象を分類する。最終成果は、具体的な代数的・幾何学的データP、明示的なadmissibility、データ上の同値関係を与え、

$$
P/{\sim}\;\longleftrightarrow\;
\{(\mathcal C,\mathcal O)\in\mathcal H_2\}/{\text{pointed exact equivalence}}
$$

の全単射を証明する定理である。有限個の模型や単一のGIT商になることは先取りしない。同値関係はデータ上の作用・変換・必要十分不変量として記述し、「圏が同値なら同一視する」と言い直すだけにしない。

| 必須の証明 | 完了とする条件 | 現在の状態 |
| --- | --- | --- |
| F1 データと許容条件 | 全パラメータ領域とadmissibilityを具体化し、未知のAS条件や「H2を与える」という循環的条件を残さない | 完了。linearとD1–D3の全許容四つ組、非cubicの被約二点集合対。未知のAS条件なし。`def:classification-admissible` |
| F2 構成の正しさ | 各許容データからO付き圏を構成し、GK rank・exceptionality・Serre根・AZ・全次数AS表示を確認する | 完了。全曲線型の適合周期・標準hullと中央二重平方族で全公理を確認。`thm:all-admissible-inverse`、`thm:ore-anticommuting-central` |
| F3 全被覆 | 任意のH2対象から許容データを回復する。追加仮定を使う場合はH2からの導出か、補集合を覆う別の証明を付す | 完了。内在的階数判定でcubic/noncubicに分け、VdB分類と同時untwistで全被覆。`thm:cubic-coverage`、`thm:noncubic-classification` |
| F4 同値判定 | 二つのデータが同じO-marked対象を与える必要十分条件をデータ上で証明する | 完了。cubicの明示7関係とGL4有限反復、非cubicのPGL2同時作用。根・基底・束表示の選択独立も証明。`thm:complete-h2-classification` |
| F5 全領域と基礎体 | 一般点だけでなく、退化・特殊自己同型・例外領域を含め、各領域を構成、既収録領域へのpointed exact同値による帰着、またはH2不適合の証明で処理する。k=Cだけの議論には適切な体の拡張・降下を補う | 完了。被約・非被約を含む全(2,2)型、全noncubic配置を扱い、標数零の任意の代数閉体で成立。Sklyanin開条件を主定理に使わない |
| F6 証明と再現 | 主定理から入力補題まで依存を閉じ、一次文献の仮定・規約を確認し、必要な厳密計算・組版・独立点検を終えて現行一式とhubを保存する | 体上の分類と主要な表示・特殊化の証明は独立読取り済み。現行版の参照確認、公開計算コードの実行、組版・画像確認の実施範囲は研究ノートの現行検証節に集約する。内在的相対H2の有限型代数性は証明済み。現在の版の組版状況は検証節を参照。repoとhubの保存は個別に確認する |

F1–F6が揃うまでは「完全分類」と報告しない。条件付きの還元、一般点の分類、例の族、有限次数のincidence、既存の非標識分類だけでは完了しない。原稿に未証明の核心命題が残っていないことを、異なる観点または独立担当で確認する。checkスクリプトはこの数学的達成を判定しない。

自己同値群・groupoid・相対モジュライを主張する場合は、それに対応する全忠実性、自然同型、降下・底変更・代数性を別途証明する。次数スカラー等の核を調べずに反Serre環のgraded自己同型群とpointed自己同値群を同一視しない。GIT商のorbit closure・S-equivalenceがpointed exact同値と一致するかも別途確認する。これらは重要な後続目標だが、対象のpointed exact同値類の完全分類と混同しない。全ambientや全平方根の個別分類を不必要な終了条件にしない。

## 5. 現在の結論と後続の研究目標

全H2の対象同値類は二領域の非交和として分類した。cubic側はlinearデータと全許容四つ組であり、R0⊗V3+V0⊗R1を二周期で移した七次元関係Kから、二つのGL4行列のtransporterとその有限反復で同値を判定する。noncubic側は中央二重平方環であり、根対の配置が完全不変量である。全ての平方根やambientを列挙する必要はなかった。

cubicの四つ組同型だけでは、平方根・ruling・foundationを忘れたpointed同値を数え切れないため、最初の軌道対象の内在性に基づく有限判定を最終仕様に採用した。これは具体的な必要十分条件で、未知の圏同値や未知のAS条件を言い換えただけではない。抽象的な基礎体上では有限代数的判定であり、機械実行には係数体の有効な表示を要する。

この同値類分類を、非被約底も含む族と自己同値を保持する有限型smooth Artinスタックへ拡張した。反Serre環の全次数は二次関係から復元でき、noncubic六係数は固定Grassmann affine cellへ局所閉埋込みとなり、全実現点は構成可能な集合として既約包絡[Z2/PGL9]に含まれる。noncubicでは表示商と全幾何点慣性を構成した。finite foundationの開部分F0上ではruling交換を相対的に構成し、coherentなS2商Q_fndを得た。全H2(k)はそのfull subgroupoidとして実現され、全pointed自己同値も捉える。F0→Q_fndは実際に有限étale二重被覆であるが、これを任意の内在的H2族のruling被覆と同定する相対認識は残る。H2実現集合はcubic非空開を含むため誘導位相で既約であり、各noncubic点へのcubicからのpointed smooth proper dg特殊化を構成した。さらに各特殊化について反Serre軌道のperfect複体が次数零の局所自由環に集中し、`[Gr(56,81)/PGL9]` への実際の曲線が得られる。全H2点の適切な有限型近傍には相対平方根と同じ根のAS4被覆が存在する。foundation表示全体との相対同値は別に検討する。

公表前の包括的な先行研究比較と第三者による証明レビューも必要である。既知のVdB分類、PresottoのZ-domain、MCM・helix・AS双対性、関係式stackと変形比較を本研究の新しい成果とはしない。一般の自己同値・根・ambient忘却ファイバーやcubic同値の幾何的簡約も、必要な範囲で扱う。

固定Sklyanin pencilの高々64候補への簡約にはΔの単射性が残るが、その補集合は主定理の四生成判定で既に扱う。Δの全域解析は判定の簡約という別の課題である。可換点の四根とOkawa–Uedaの次数四射の一致も先取りしない。

**楕円型の全O標識と有限・無限の忘却。** 滑らかな楕円四つ組でδ≠0、η∉Zδなら、RTと対角根から全Z²のrank-one torsion-free exceptional対象を構成し、数値類ごとの一意性で全てを尽くす。全てがH2の構造対象となる。Uₙ=(E,L₀,L₁⊗(L₂L₀⁻¹)ⁿ,L₂)を代表とし、εδ=δかつε(η+nδ)∈{η+mδ,2δ−η−mδ}という有限楕円自己同型群を含む必要十分条件でpointed重複を判定する。δ非捩れなら可算無限、位数rならZ/rZの有限商となる。余分な自己同型がなく2η∉⟨δ⟩なら正確にr個。証明は `thm:elliptic-marking-lattice-fiber`、`cor:elliptic-torsion-fiber-cardinality`。Z²と二面体作用はKitamura–Okawaの既存announcementと重なるため新規性を主張せず、ここでは指定範囲の独立証明と明示的な忘却判定を与える。η∈Zδ、退化曲線、noncubicの忘却と相対stack射は未解決。

## 6. 次の実行単位

1. **局所good moduliの降下を調べる。** 一致類の共通étale商近傍と不変式環 k[ac,(x+y)²,(x−y)²] を入力とする。stabilizer-preserving条件、飽和開、重なり上の比較を確認し、H2のZariski開または全体へ降下できる範囲と障害を切り分ける。N^DMの粗モジュライ射χ_DMは任意底変更と両立するが、この制限射はgoodではなく、慣性も非properである。これを全体のgood moduliの存在・不存在に直結させない。
2. **framed実現像と偏極認識を具体化する。** X_asはsmooth83次元スキームで、一致根対ではX3の接次元84との相違がある。`cor:artin-polarization-retraction` の余分なHH¹方向と、今回決定した全慣性表現・形式対を用い、局所閉性や具体的な偏極認識方程式を調べる。開性を目標にしない。
3. **Q_fndとの相対groupoid比較を進める。** 全幾何点での全充満性と全Artin認識に加え、実際の族のruling被覆・相対heart・降下を比較する。境界上で既証明のNpres≃Nを利用し、全体の相対同値を幾何点比較だけから結論しない。
4. **公表前監査を仕上げる。** 有限LG条件→全fiber認識→全軌道→Noetherian貼合せ→中央AS4被覆と、指定Artin同型を保つatlasを点検する。境界の粗・良モジュライ、相対ruling mutation、AHRの適用範囲も監査する。既知のVdB・DDL・PP・Stacks・Alper・AHRの入力と本研究の成果を分け、新規性比較と不足TeX依存を解消した環境での組版を行う。

全スキーム上の商[U/R]は元の有限型site上のH2を延長する。任意Noetherian基底で同じAbel公理を課した関手との一致、および一般のcanonical非有界導来圏の大域descentは別に確認する。

体上の分類、全Artin形式認識、局所環上の効果性、有限型効果性を未解決へ戻さない。cubic有限同値判定の簡約、一般GL4判定solver、全根・全ambientの列挙、外部査読・形式証明は独立の後続課題である。

## 7. 正本・依存関係・再開

- 論文A・主原稿：[papers/nc-quadric-classification.tex](papers/nc-quadric-classification.tex)。全H2のpointed分類。相対節の証明は移管完了まで保持する。
- 論文B：[papers/nc-quadric-moduli.tex](papers/nc-quadric-moduli.tex)。内在的相対モジュライ・境界幾何。移管途中の未完成稿。
- 別稿：[papers/nc-quadric-avatar.tex](papers/nc-quadric-avatar.tex)。八・十・十二本矢の表示モジュライ、反標準avatar、内在的忘却。主論文の分類証明を重複させない。
- 別稿の組版：`python3 scripts/check.py build --manuscript papers/nc-quadric-avatar.tex`。同じ指定で `sources` も実行できる。
- 現行知識・障害・再現：[notes/research_notes.md](notes/research_notes.md)。文献仮定・版・リンク：[notes/literature.md](notes/literature.md)、書誌：[papers/references.bib](papers/references.bib)。
- 計算：[computations/verify_quadric.py](computations/verify_quadric.py)。`python3 -m pip install -r requirements.txt` 後、repoルートで `python3 computations/verify_quadric.py`。
- Cloudの導入と検証：[CLOUD_CODEX.md](CLOUD_CODEX.md)、`bash scripts/bootstrap.sh`、`python3 scripts/check.py doctor`。構成・検算・組版を個別に実行でき、欠落依存が独立な数学作業を止めないようにする。
- 組版：repoルートで `latexmk`。PDFとSyncTeXは`build/`。LuaTeX-jaを含むTeX Live/MacTeX、latexmk、BibTeXが必要。VS Codeはrepo全体を開いてLaTeX Workshopの既定レシピを使う。
- cubic側の定義比較は `nc-cubic-classification` のcommit `5393766744bdae887a374b6853ff4daf53d971b5`、`papers/nc-cubic-classification.tex` のrank定義・`def:14641-intrinsic` を確認した。その完全分類定理は本研究の入力にしていない。
- `categorical-fano-index` はSerre根一般の関連研究。現時点で同repoの未確認結果を輸入していない。既知quadric文献を優先する。
- GitHub更新には対象repo・research-hubそれぞれの書込み権限が必要。前の実行で使えた認証や接続が次のCloud taskにもあるとは仮定せず、読取と書込を別に確認する。研究資料の再開に会話履歴は不要。
