# nc-quadric-classification

**構造対象 O のみを指定した非可換 quadric surface の分類。**

2026-11-23 / 運用v1.41、論文A v1.69、論文B v0.41（依存・組版の監査中）、論文C v4.30。まず [研究方針](00_research_plan.md) と [AGENTS.md](AGENTS.md) を読む。GitHub `main` を正本とする。

**最上位目標：論文Cの完成。** [研究方針C1–C4](00_research_plan.md#最上位目標論文cの完成2026-11-23) に従う。**C1・C2は原稿上達成。C3はH2実現可能開全体のQP→finite foundation→Jacobian/Serre→pointed heartと二ruling mutation商まで原稿上到達。H2外の全AS/avatar/QP stack分類は未完、C4の独立監査・新C全稿LuaLaTeX組版も未完了。** C3では二massに沿う滑らかなゲージ群 `U_λ×U_μ` と相対対角解消から、ordinary Jacobianをcanonical Serre completionと全次数・非被約基底を含めて比較した。二段剛体化の後の相対商はruling付きH2と一致し、ruling交換はright-equivalenceでなくcoherentな相対mutationにより貼り合う。今後はまず新C3定理の独立数学監査、Keller訂正条件とAZ/Noether/非被約base-change、次にC4の先行研究比較・組版を最優先する。A/Bは必要な論理的入力として扱う。

**Cの現行到達点。** 点曲線 $E_f$ 側は、全二形式商 $[P/G]$ 上のrank45対称Morita代数・相対spinor tilting・全次数Serre完成により、非被約局所有限型底を含む元のpointed H2族と同定した。Smooth spectral側の指定pointingは $\chi\mapsto\chi/(\chi-1)$ を与え、自己双対点は0,2。一根共有・根対一致へ退化する二族の像は、有限分岐基底変更後にもH2族へ延長できない。相対射はμ₂-gerbeと有限étale二重被覆に分解し、中心の分裂体によりstack自己同値は不可能である。境界の平坦代数模型では全高次Extの非消滅を証明し、この表示族内のH2条件を各形式のsquarefree性と同定した。詳しい適用範囲と証明先は下の論文C節に置く。

**Canonical Serreの同変構造。** 二形式交換の符号指標を $\varepsilon$ とすると $R_n^{\mathrm{can}}=B_{2n}\otimes(\det W)^{-n}\otimes\varepsilon^n$。符号を含まないBの表示は次数線束による正規化であり、同じpointed qgrと射影関係式表示を与える。境界の同値・慣性の結論も保持する。通常Endは右Yoneda規約を用い、上三角双加群表示との反対環の関係を明記する。

## 公表用原稿：三論文へ再編

| 原稿 | 中心課題 | 状態 |
| --- | --- | --- |
| **A・主原稿** [nc-quadric-classification.tex](papers/nc-quadric-classification.tex) | O-marked非可換二次曲面の全分類とpointed exact同値 | 体上の全分類を中心とする20節を入力。相対主定理はBを引用 |
| **B** [nc-quadric-moduli.tex](papers/nc-quadric-moduli.tex) | 内在的相対H2の代数性とnoncubic境界の幾何 | **相対H2・Artin変形・AS4・Koszul・cubic/noncubic効果性・境界幾何・楕円型忘却の31節を保持。Aの分類入力との残余依存を監査中** |
| **C** [nc-quadric-avatar.tex](papers/nc-quadric-avatar.tex) | **指定AS分解とavatarの分類、pointed認識と相対比較** | v4.30。sq/rsq・独立AS10・二重壁とcubic障害。全noncubic商上のrank45相対 $E_f$ 認識とcanonical Serre符号を証明。Smooth spectralの指定pointed像はFricke対合、二境界型の像は有限基底変更後にもH2へ延長不能。相対μ₂-gerbe・二重被覆、stack自己同値の不存在、境界無限Extを証明。節点TF標的の有限型Artin性、balanced商と元Nの開埋込みも証明。全Fricke境界射・全fiberと有限分岐後の二次線束障害を証明。全分類AS型の標準頂点を判定。全相対AS/QP群oidは残る |

論文AのAbstractとIntroductionは分類に焦点を当て、相対結果の分割節は主原稿から外した。Aに残る20節は分類の構成・被覆・同値判定を担う。Bは31節で、楕円型の構造対象忘却と反Serre偏極の変形例も含む。

Aを分類論文、Bをその体上分類を入力とする相対モジュライ論文、Cを有限表示・avatar論文として整理する。Aの先行研究節は体上の分類に絞って整理し、BのIntroductionには相対主定理の見取り図を加えた。Belmansのcubic側の既知HH計算を比較対象に追加した。BからAへの17種類のラベル参照がAの有効な分類20節に定義されていることを確認した。全証明の数学的独立監査は別に必要である。3原稿の独立source検査に加え、A/B/C間の `\cite[\texttt{label}]{...}` の参照先ラベル実在性も検査するよう checker を拡張した。現行checkout上で三稿のsource・相互ラベル検査を実行してPASS。LuaLaTeX依存が不足するため現行三稿の組版は未実施。新規の五頂点bar厳密計算コードは容器内で実行し、GitHub上の同一ファイルであることをGit blob SHAで確認した。 3原稿の構成検査は `python3 scripts/check.py papers`、個別組版は `python3 scripts/check.py build --manuscript papers/<原稿名>.tex` とする。GitHubへのソース反映と組版実行は別々に確認する。

## 論文C：AS/avatar分類とpointed認識（v4.30）

**全H2の準射影的良モジュライ。** 左右kernel条件は P(M)=det M、Q(M)=e3(JMᵗJM) の二式へ集約できる。二つの交差行列について s0=(PfPg)³、s1=Pf³Qg²、s2=Qf²Pg³、s3=(QfQg)² とすると同じ指標χ0²⁴を持ち、s1s2=s0s3。非順序H2開は s0,s3,s1+s2 の三非消滅開で覆われる。各開はアフィン商で、重なりは不変な比の非消滅開なので飽和している。全H2と順序付き被覆のgood moduliは半不変環のProjの開となり、分離的・有限型・準射影的なschemeである。幾何同型類を分類するcoarse moduliの不存在と両立する。三式が半不変環を生成するとは主張しない。 [証明](papers/quiver-avatar/global_h2_good_moduli.tex)。

**良モジュライ上のcubic開と境界。** Ordered cubic開は飽和しており、f=1の残余群とχ0次数を比較すると、既存四量子ビット商P(1,2,2,3)の開D+(p_adj)∪D+(q_adj)と同型となる。p_adj=P(Cr(adjT))、q_adj=Q(Cr(adjT))の通常次数は12・18。noncubicのA1χはMへ閉埋込みとなり、cubic/noncubicは同じgood fiberに混在しない。階数因子Dの正規化列の差はruling符号線束で、その直像が零になるため、Dのgood imageは既に正規である。一方、noncubic閉像のscheme逆像は一致点で元のNより厚い。符号慣性が法方向に−Idで作用し、good像が一定の非零横断一次変形を与える。 [cubic比較](papers/quiver-avatar/global_h2_cubic_git_comparison.tex)・[境界像](papers/quiver-avatar/global_good_moduli_boundary_images.tex)。

**Cubic開の不変式方程式。** e_i=e_i(JTᵗJT)、d=det T とすると、16p_adj=e3²−4d²e2+8d³、16q_adj=e3³−4d²e2e3+16d⁴e1−8d³e3。Cartan上のHadamard計算と不変式制限の単射性から全行列上で証明した。被約補集合は C0={d=e3=0} と C1={e3=de1, 4e2=e1²+8d} で、両者はP(1,2)、唯一の交点[2:1:0:0]は通常節点となる。高次イデアル自体の被約性を主張せず、この二曲線と全H2内のnoncubic A1χを区別する。 [証明](papers/quiver-avatar/cubic_geometric_open_invariants.tex)。

**二cubic chartの貼合せと全域GIT射。** 重なりの反転は [e1:e2:d:e3]↦[e3:d²e2:d³:d⁴e1]。両積可逆なordered粗環は k[b,u,v,w]/(uw−v²)、交換はu↔wで、unordered商はA³_(b,s,v)から直線{s=2v,v=4b−8}を除いた開となる。固定schemeは二被約成分、粗二重射はz²=(s−2v)(s+2v)である。全ordered良モジュライから既存WPSへの二つの正則射ρf,ρgを構成したが、noncubic A1χはともにq0=[1:0:0:0]へ収縮される。両射と全良モジュライはnonproper。 [証明](papers/quiver-avatar/cubic_inversion_global_morphisms.tex)。

**全H2の有限square表示とcanonicalなrank81代数。** 四つのrank2束とrank4束への二乗法をパラメータ化するA32の開から、rank16 squareとrank24 normal foundationの全相対stack同値を核・余核で構成した。頂点トーラスKとruling交換S2を含め、Q_fndは((GL2^4×GL4)/Gm³)⋊S2による商になる。H2はその不変開として表され、古典型も同じ有限表示で扱える。二積の合併全射は追加開であり、H2上では成立する。全H2上のTcan=⊕Ei⊗Hom(O,Ei)∨は頂点線束と二rulingの交換を消して降下し、通常のEnd代数はrank81。canonical完成のn次は81(2n+1)²、O角は(2n+1)²で、左右Noether性とpointed tails認識を得る。H2開は二乗法の随伴行列から作る二つの交差縮約とその転置について、kernelがSegreを避ける四条件で完全に判定した。各条件は五生成idealの非零開で、計20式以内（次数16・24）となる。両rank3壁も含み、既存相対開との一致により非被約底でも全groupoidを認識する。四交差条件をさらに同じ指標の三半不変式へまとめ、全H2の分離的・準射影的good moduliを構成した。任意AS/QP族の全比較は別課題である。[有限stack同値](papers/quiver-avatar/relative_square_foundation_stack.tex)、[全H2のrank81代数](papers/quiver-avatar/universal_h2_square_morita.tex)。

**全域の境界幾何。** 明示H2開上のdet f=0とdet g=0は滑らかなCartier因子で、共通零点では二つの微分が独立である。順序付きH2上でSNC、noncubic交点は滑らかな余次元2となる。非順序和因子の正規化は一方の順序付き因子であり、noncubic上の逆像はruling二重被覆、conductorはschemeとしてnoncubic中心である。任意引戻し後のsmooth/reduced性は主張しない。 [証明](papers/quiver-avatar/square_rank_boundary_geometry.tex)。

**回転・第一mutationも同じ相対heartを持つ。** (E1,E2,E3,tE0) と (t⁻¹Z1,E0,E2,E3) の有限Endはともにrank24、完成のn次は64n²+64n+24。双対square heartによって左右Noether性を証明し、全四対象とtを保つtails同値を得た。最小矢の追加成分はcoker μG=O/(δ)であり、階数一の矢束となる条件はδ=0というscheme壁への因子化である。δ=εの一次変形では全幾何fiberがAS10でも最小矢束は平坦でない。この場合も全Hom代数・tailsは平坦に構成でき、七矢三関係の有限End表示から非最小十矢potentialの実際の相対AS解消・双対を得る。[回転・mutationの相対比較](papers/quiver-avatar/relative_rotated_mutated_tails.tex)。

**Canonical squareの全次数代数と相対tailsを認識した。** 基底平坦compactなEに対するExt^{q}(E,K)=0（q>2）を相対Serre双対とinjective cogeneratorから証明し、二段のO軌道被覆でT=⊕EiのAZ2を得た。canonical Serre完成は左右Noetherianで、四頂点展開は全成分・全積と任意scheme基底変更を保つ。係数束を残した実際の単純AS解消と相対Gorenstein双対を構成し、qgrは同じ相対H2 heartと、全標準対象を保って完全同値となる。左右Noether性・heartの基底は本稿の局所有限型siteとし、特異基底での絶対大域次元は主張しない。全幾何fiberが分類済みsquare型である有限族へも適用でき、古典fiberを許す。頂点線束と周期線束は明示的に保持する。[相対AZとtails](papers/quiver-avatar/relative_square_tails_recognition.tex)、[反対代数と左Noether性](papers/quiver-avatar/relative_square_opposite.tex)、[全整数展開とAS解消](papers/quiver-avatar/relative_square_unfolding.tex)。

**一般square族の全標準頂点を同じ相対heartで認識した。** 二つのpencil乗法から $U_0=U_3=T$、$U_1=D(\det\mu_F)$、$U_2=D(\det\mu_G)$ を構成し、任意の非被約底変更と整合させた。局所有限型底の実際のflat曲線avatarのrank16 Endから、coneとSerre移動によるrank24 normal窓を作る。両heartの反Serre生成対象が互いのheartに実際に入ることから、AZ解消でcompact Moritaのt-exactnessを証明した。従って各Uiは、同じ相対heartのEiが強いH2構造対象となる条件そのものを表す。Ui上の実際の全次数cubic族とcanonical tailsも復元した。普遍楕円Picard上の二壁はCartier・横断、任意引戻しではFitting閉部分。canonical square完成のqgr比較は証明済み。別途与えた全AS/QP群oidとの同一視は別課題である。[行列式開](papers/quiver-avatar/relative_vertex_determinants.tex)、[相対normal窓](papers/quiver-avatar/relative_avatar_pointed_recognition.tex)、[heart比較とcubic回復](papers/quiver-avatar/relative_avatar_heart_comparison.tex)。

**標準構造頂点のH2所属を全分類AS型で判定した。** Square曲線型では位相0,3は常に所属し、位相1は $GP\not\simeq F$、位相2は $G\not\simeq FP$ のときに限り所属する。Rotatedでは $C=HF^{-2}$ として位相0は $C\not\simeq\mathcal O$、位相1は $C\not\simeq P^2$、位相2,3は常に所属する。最小十本矢型は奇数位相だけが所属し、古典型は全位相が所属する。非被約曲線も含む体上の定理である。頂点ideal商の全標準右射影の有限次元性と反Serre豊富性の同値を証明し、肯定側には実際のcubic/noncubic pointed認識を使う。[全標準頂点の判定](papers/quiver-avatar/general_vertex_az.tex)。

**全point schemeと孤立二点。** 中央二重平方環では全point schemeは $E_f\amalg\{p_c,p_d\}$、shiftは曲線上で恒等、付加二点を交換する。multilinear schemeを自己同型のgraphとして計算し、全truncationの安定化、任意底変更と普遍族を確認した。表示商上の孤立二点は根対の順序付け二重被覆として降下する。graded普遍加群の次数スカラーgerbeは区別する。[証明](papers/quiver-avatar/spinor_pointing_obstruction.tex)。

**Noncubic由来の構造頂点を全四位相で判定した。** 同じ $\qgr B_f$ の二spinor $\pi X_c,\pi X_d$ は、二周期point moduleへの全反Serre軌道からのHomが零となるため、強いH2の構造対象にはならない。H2に属する位相はsquareで0,3、rotatedで2,3、最小十本矢型で1,3であり、全整数へ四周期化する。特にrotated零頂点・最小十本矢型零頂点は除外された。曲線上のpencil辞書や同じHilbert数値だけではこの障害を検出できない。[構造頂点と生成障害](papers/quiver-avatar/spinor_pointing_obstruction.tex)。

**順序付きFricke延長は平坦な良モジュライ射である。** 実際の代数的target atlas上で $[\operatorname{Spec}R[a,b]/(ab-q)/\mathbb G_m]\to\operatorname{Spec}R$ と表示し、平坦・有限表示・全射、構造層の直像同型とquasi-coherent直像の完全性を証明した。Artin targetを許すAlper Remark 4.4の意味でのgood moduli space morphismであり、任意底変更後も成立する。非smooth locusは一致根対に限られ、射は非分離・非proper。一致点を除くDM開では直像の完全性が失われ、中央μ₂を剛体化した局所模型は原点を二重にした直線となる。順序忘却後の射は一般fiberが二つなので、この良モジュライ性を持たない。[証明](papers/quiver-avatar/fricke_boundary_descent.tex)。

[論文C](papers/nc-quadric-avatar.tex)は、指定した最小分解型のAS正則Z代数とavatarの分類を中心に、有限QP・既存GIT・内在的H2を比較する。現在の要点は、**点曲線側は全noncubic相対族で元のpointed heartを認識でき、spectral側の指定pointingはsmooth領域でも一般に別のH2対象を与える**ことである。

### 二massのQPから全H2への相対groupoidと反Serre完成

共通十二矢potential `W=H+yq+px+vq'+p'u+λyx+μvu` の全fppf群oidからrank24 finite foundationの全積を復元する。余剰慣性は滑らか・平坦な `U_λ×U_μ`（`U_λ=Spec R[t,(1+λt)^(-1)]`）であり、両rank3壁ではGa²、両mass可逆でGm²。相対短対角解消のEuler階数は(68,52,8)→24で、ordinary relation idealを生成することを確認し、訂正済みKellerのrelation QP表示から `Jac(Q12,W)≅H⁰Π₃(Λ)` を導いた。**全H2実現可能開**ではnormal tiltingと反Serreの全次数forward Ext消滅により `Jac_n≅Hom(T,tⁿT)`、階数 `64n²+64n+24`、左右Noether性、同じpointed `qgr` heartの認識を得る。massゲージと頂点Gm³を順に剛体化すれば`H₂^rul`、coherentなruling mutationのS₂商が`H₂`。両cubic chartは一般にright-equivalenceで直接貼れない。**H2外のraw QPのAS正則性は主張せず、全AS/avatar stackの無条件比較にも拡張しない。** [主証明](papers/quiver-avatar/cubic_qp_foundation_groupoid.tex)、[対角・Euler検算](computations/verify_q12_diagonal_euler.py)。新C3の独立数学監査・全稿組版は未実施。


### Gram pencilによる大域good moduliの明示表示

非順序の全H2 good moduliは\(\mathbb P(2,2,3,4)\)の明示開で、全半不変式環は\(k[A_2,B_2,C_3,D_4]\)（重み2,2,3,4）。中央affine chartは\(\Delta_8=(D_4+4A_2(B_2-2A_2))^2-4(B_2-2A_2)C_3^2\ne0\)、その環は重み零局所化であり、noncubic閉像は\(A_2=C_3=0,\ \chi=B_2^2/(4D_4)\)。二商特異点の解析型は\(1/3(1,1,2)\)、\(1/2(1,1,1)\)。[全証明](papers/quiver-avatar/global_h2_invariant_hull.tex)、[検算コード](computations/verify_global_h2_pencil_invariants.py) はGit blob SHA一致のコピーを実行し全PASS（記号的noncubic境界・有理数4例・Hilbert係数）。一般二対称形式の不変式環は既知入力。C3の全相対AS/QP群oid比較とC4の公表前監査・全稿組版は未完成。

### 点曲線側の相対認識とspectral側の像

中央二重平方環 $B_f=k[u,v]\langle c,d\rangle/(c^2-f_1,d^2-f_2)$ には、点曲線 $E_f=\{c^2=f_1,d^2=f_2\}$ とspectral曲線 $C_q=\{y^2=f_1f_2\}$ がある。四根相異なる場合、$E_f\to C_q$ は同時符号の商であるétale二重isogenyで、二つの非零二捩れ標識は双対isogenyで交換される。一般に二曲線は同型でない。

| 比較対象 | 現在の結論 | 証明先 |
| --- | --- | --- |
| $E_f$ の二conic pencilからのavatar | 正しいshift後の構造頂点で、全noncubic幾何点の有限Endと全積を同定 | [点曲線とspectral曲線](papers/quiver-avatar/point_spectral_isogeny.tex) |
| $E_f$ 側の相対pointed heart | 対称窓 $(B,X_c,X_d,B(1))$ のrank45代数を全商 $[P/G]$ へ降下。実際のspinor tilting、全次数Serre完成、零頂点cornerにより元のH2族とpointed exact同値。局所有限型の非被約底、非平坦引戻し、fppf降下を含む | [対称Morita降下](papers/quiver-avatar/symmetric_morita_descent.tex)、[Serre完成とheart](papers/quiver-avatar/relative_serre_completion.tex) |
| Smooth $C_q$ 側の指定AS実現 | 古典的Fricke対合 $\chi\mapsto\chi/(\chi-1)$ を与える。元のpointed対象との同値は固定点 $\chi=0,2$（$j=1728,8000$）に限る | [spectral対合](papers/quiver-avatar/spectral_atkin_lehner.tex) |
| Smooth $C_q$ 側の相対射 | 順序付き標的へのbanded $\mu_2$-gerbeと順序忘却の有限étale二重被覆。幾何fiberは $B\mu_2\amalg B\mu_2$。一般慣性の核2・像8 | [相対構成と逆gerbe](papers/quiver-avatar/spectral_relative_correspondence.tex) |
| 粗対合を覆うstack自己同値 | 存在しない。一般慣性の中心の二次分裂体が双対化で変わり、inner twistでも一致しない。一般点でrepresentableなliftも不可能 | [中心bandの障害](papers/quiver-avatar/spectral_relative_correspondence.tex) |
| H2の外側の平坦模型 | 両境界で共通の重根代数へ退化。固定二対象間に全次数で $\operatorname{Ext}^n=k$ があり、$D^b(\qgr B_0)$ の右Serre関手は存在しない。この表示族内のH2条件は $\Delta_1\Delta_2\ne0$ | [境界の無限高次Ext](papers/quiver-avatar/spectral_relative_correspondence.tex) |
| 一根共有・根対一致へのspectral像の延長 | 二つの明示族で像の $\chi$ に極が生じるため、有限分岐基底変更後にもH2族へ延長不能。Bのnoncubic境界の閉性を使用 | [境界延長不能](papers/quiver-avatar/spectral_atkin_lehner.tex) |

Canonical Serreの同変構造には、二形式交換の符号指標 $\varepsilon$ が入り、$R_n^{\mathrm{can}}=B_{2n}\otimes(\det W)^{-n}\otimes\varepsilon^n$ となる。符号を除いた次数線束正規化は同じpointed heartを与えるが、canonical構造としては区別する。Rank45 Serre完成の各次数階数は $196n^2+196n+45$、零頂点cornerは $(2n+1)^2$。Cornerは9生成・56二次関係を持つ。有限Morita同値だけからAbel同値を推論せず、実際のtiltingと反Serre再構成を用いる。

Spectral側の不変量は、$f_i=a_i u^2+b_iuv+c_iv^2$ に対して

$$
\chi=\frac{\bigl(b_1b_2-2(a_1c_2+a_2c_1)\bigr)^2}
{(b_1^2-4a_1c_1)(b_2^2-4a_2c_2)},\qquad
\chi^\vee=\frac{\chi}{\chi-1}
$$

である。例えば $f_1=x(x-1),f_2=(x-2)(x-3)$ では $\chi=49$ が $49/48$ へ移る。$j(C_q)=35152/9$、$j(E_f)=28756228/3$ なので、この場合は曲線自体も異なる。$j$が等しくても二捩れ標識が異なる例があり、pointed同値を$j$だけでは判定できない。

境界の試験族 $f_1=uv$、$f_2=u^2+uv+tv^2$ と $f_2=tu^2+uv+tv^2$ では、対応先の不変量がそれぞれ $(4t)^{-1}$、$(4t^2)^{-1}$ となる。したがって全noncubic境界からH2へのspectral対応の延長は研究目標にしない。境界を含む比較には、H2の外側で二次積付きtorsion-free spectral対象などを受けるcompactificationが必要である。

### 二次積付きtorsion-free標的の認識

幾何fiberがsmooth/nodal/I2となる有限二重被覆と二次自己双対TF層の標的 $\mathfrak T_{\rm nod}$ は、有限型Artinスタックでaffine有限表示対角を持つ。$H^0(M)=0$ の開は、積の根重複が高々二となる二形式対の商 $[\overline P_{\rm nod}/G]$ と同値である。二次積のtrace-zero成分の二等方線が元の生成線を回復するため、任意非被約底でも同型層まで認識できる。固定被覆への忘却fiberでは、共有根に長さ2、一致根対に長さ4の非被約因子分解schemeが現れ、後者には交換対合が作用する。

この中で両形式がsquarefreeとなる開は、元のnoncubic $\mathfrak N$ そのものである。従って実際の $(M,\mu)$ と二重射を保持するTF標的への射は、境界を含め全忠実な開埋込みとなる。smooth Fricke射のμ₂核は二次線束の自己同型を忘れる段階に生じ、この全忠実性と矛盾しない。[証明と境界慣性](papers/quiver-avatar/torsion_free_spectral_recognition.tex)。

$\OO_C\oplus M$ は元の点曲線・同時符号を回復する。指定generic同型のgraphは二traitで正則I2/I4模型、その自由符号商はI1/I2となる。出力二次線束は全族上line。一致型の全四半周期補正は元模型間に延長し、共有根型のhalvingには最小二次分岐を要する。共通I4模型への二つのPerf像は全忠実・構造層保存だが互いに包含しない。入力二捩れは線束には延長するものの、任意の有限分岐後の最小正則模型でも二乗自明な線束には延長しない。[共通模型・pencil・半周期](papers/quiver-avatar/spectral_boundary_models.tex)。

**自然なFricke射を全noncubic境界へ延長した。** 順序付きbalanced標的の開 $\mathfrak U=\{\Delta(g_2)\operatorname{Res}(g_1,g_2)\ne0\}$ へ、$\overline{\mathscr D}^{\rm ord}:\mathfrak N^{\rm pres}\to\mathfrak U$ を構成した。$\chi\ne0$ 上で $q=(\chi-1)/(4\chi)$、入力 $(uv,au^2+uv+bv^2)$、$ab=q$、出力 $(U^2-4qV^2,V(U+V))$ とする。補助平方根 $\rho^2=1-4q,\ \ell^2=(1+\rho)/2$ の全選択・全Isomを比較し、smooth射との貼合せと任意基底変更を証明した。線束境界上の全2-fiberは $[\operatorname{Spec}k[a,b]/(ab)/\mathbb G_m]$、重み $(-2,2)$。二つの穿孔枝は各々 $B\mu_2$、一致点は $B\mathbb G_m$ である。特殊出力はH2外であり、H2延長不能の結論を保持する。[大域降下と境界fiber](papers/quiver-avatar/fricke_boundary_descent.tex)。

### AS分類・矢数・幾何avatarの到達範囲

| 主題 | 証明した内容と適用範囲 |
| --- | --- |
| Square/rotated-squareとAS | 指定最小分解からのavatar抽出、acyclic spherical helixによる全整数の逆構成、相互逆性、左右Noether性。[AS/avatar分類](papers/quiver-avatar/as_helix_classification.tex)、[canonical helix](papers/quiver-avatar/canonical_helix_complexes.tex) |
| 独立AS10とmutation | Mutation像を定義に用いないAS10クラスと、squareからcubic/AS10への相互逆分類、全整数の評価・余評価、Noether性とqgr比較。[AS10分類](papers/quiver-avatar/as10_mutation_classification.tex) |
| 8・10・12本矢の意味 | Square有限foundationは8生成矢・4関係、relation QPは12本矢。指定mutationのreduction階数4/3がcubic8/最小AS10を分ける。任意の12本矢QPのAS正則性は主張しない。[有限QP](papers/quiver-avatar/qp_presentations.tex)、[有限foundation](papers/quiver-avatar/foundation_charts.tex) |
| 二重壁とcubic障害 | $0\ne P\in\operatorname{Pic}^0(D)[2],\ G\simeq FP$ が二壁の交点。Smooth/nodal/I2の全型、壁のscheme-theoretic横断性、cubic型へ到達できる範囲を扱う。[二重壁](papers/quiver-avatar/as10_mutation_classification.tex)、[cubic障害](papers/quiver-avatar/cubic_obstruction_all_loci.tex) |
| 幾何avatarとnoncubic分類 | 二根対とsmooth/nodal/I2の非零二捩れsquare avatar、負断面を避ける $\Sigma_2$ avatarの幾何同型類が全単射。$Σ_2$のnodal/I2は、同じ $\chi=1$ に属する二つの根対型を区別する。[avatar辞書](papers/quiver-avatar/avatar_charts.tex) |
| 全相対表示との区別 | 有限foundationの二つの10矢開と8矢交わり、任意基底のQP消去、残る消去pairの $\mathbb G_m$ 慣性を証明。全AS/avatar/potential stack同値は未証明。$\operatorname{coh}\mathbb P(1,1,2)$ と $\operatorname{coh}\Sigma_2$ の通常の構造対象は強いH2条件を満たさない。[内在的忘却](papers/quiver-avatar/intrinsic_forgetting.tex) |

全noncubic幾何同型類とspectral avatarの集合論的対応は、元のH2対象とのpointed同値を意味しない。$\Sigma_2$からsquare辞書を経て今回と同じmutation・pointingを選べばspectral対合の結論が適用される。noncubic由来のrotated零頂点は生成障害により強いH2外と判定した。一般P・非被約曲線・古典型を含む体上の標準頂点は一般判定節で扱い、相対全標準頂点を同じheartで認識した。別定義の全square AS heart比較を次に扱う。

### 相対比較に残る障害とGITの成果

| 主題 | 現行成果・参照先 |
| --- | --- |
| Brauerと半周期 | 一般点曲線のperiod/indexは2/4。二conicのBrauer類、gerbe上のpencil、四頂点のMorita重み、半周期の最小分裂被覆を決定。半周期四重被覆と分岐根選択四重被覆は非同型。[根降下](papers/quiver-avatar/root_descent_brauer.tex)、[Morita重み](papers/quiver-avatar/twisted_morita_weights.tex)、[半周期](papers/quiver-avatar/half_period_ruling.tex) |
| OU/半周期の不一致 | 同じspectral曲線を持つ共通incidence上でも、OU四重torsorとnoncubic半周期は有限étale被覆として非同型。二捩れ群スキームと自然な二同種によるKummer像も一致しない。[共通incidenceの比較](papers/quiver-avatar/half_period_ruling.tex) |
| Spectral境界の相対構成 | 根対から二次積付きrank-one torsion-free moduleへの相対射は構成済み。入力二捩れのPic0・二次線束としての延長に、全有限分岐後の最小正則模型でも障害がある。[avatarの相対構成](papers/quiver-avatar/avatar_charts.tex)、[節点解消の障害](papers/quiver-avatar/nodal_resolution_obstruction.tex) |
| 滑らかなcubicの辞書 | VdB三線束とsquare avatarの双方向式、Oを保つ $r_1$ 商を証明。一般potential→avatarは次数4、potential→H2は次数8であり、根を選ぶ忘却次数とは異なる。[avatar辞書](papers/quiver-avatar/avatar_charts.tex) |
| OU四重射とPicard根 | 対角の滑らかな一般開でOU四重torsorをspectral曲線の指定半点torsorと同定し、Hodge符号を含めPicard $[-2]$ 根と比較。正則半単純族へ相対Hodge構成を延長。[GIT比較](papers/quiver-avatar/git_comparison.tex) |
| Quintuple→H2 | スカラー剛体化後、非線型geometric locusでsmooth相対次元0、一般開で表現可能étale・次数2。二捩れ特別座の全慣性・反射分岐、交点のA1型、CM・一cubic境界を記述。全GITへの延長とは区別。[GIT比較](papers/quiver-avatar/git_comparison.tex) |
| 全H2の二rulingと有限表示 | 内在的有限étale二ruling被覆、foundation実現可能開との比較、その $S_2$ 商を証明。全foundationが実現可能とは主張しない。Cubic幾何部分の四次・六次判定は明示済みで、全実現可能開の具体式・次数上界は未計算。[GIT比較](papers/quiver-avatar/git_comparison.tex)、[有限foundation](papers/quiver-avatar/foundation_charts.tex) |

### 次の研究と検証の状態

**Cの完成に直結する次の実行単位は、新C3の独立証明監査とC4の公表用編集です。** 相対二段対角の各頂点成分、Kellerの訂正済みordinary ideal条件、全次数のperfect-fiber判定、normal oppositeからの左Noether、非被約底上のIsom・慣性、二段剛体化とS₂-coherent mutationを独立に点検する。続いてCの全source・reference・BibTeXとLuaLaTeX/SyncTeX・PDF表示を確認し、既存結果との差をIntroductionで正確に比較する。H2実現可能開の外側にある一般AS/avatar/QPの全相対群oidは本稿の無条件結論とせず、具体的なAS-regularityとpointingの欠如を調べる独立課題とする。独立証明監査・全稿組版・包括的新規性確認は未完了。


## 論文Bの証明監査と再現

noncubic有限型効果性では、[五頂点barとcanonical tails](papers/moduli/noncubic_local_tails.tex)、[中央Clifford閉部分のPBW・Noetherian貼合せ・AS4延長](papers/moduli/noncubic_finite_type.tex)の依存関係を整理した。可換quadricでの終頂点Torの厳密計算は[五頂点検算](computations/verify_five_window_terminal.py)、Cliffordの任意可換係数環上の書換は[PBW検算](computations/verify_clifford_pbw.py)で再現できる。有限次数の計算と全相対主定理の証明は区別する。

[atlas構成](papers/moduli/quadric_smooth_atlas.tex)に、指定pointed exact同型のArtin持上げからrepresentable smoothを導く独立補題を追加。可換・cubic・noncubic chartの重複論証を統合し、[全体smooth atlas・framed空間](papers/moduli/h2_smooth_atlas.tex)へ接続した。noncubic chartは64次元、atlasの相対次元61、relation scheme125次元、PGL₉枠X_as83次元。相対代数性とframedの証明正本は**論文B**であり、論文Aへの古い参照を訂正した。

三稿全体の `python3 scripts/check.py papers` をローカルcheckoutで実行し、構成・ラベル・引用・明示的な論文間参照はPASS。noncubic境界の相対groupoid・慣性・good/coarse moduliの証明はBに保持し、その包括的な独立監査は継続する。LuaLaTeX全文組版は必要パッケージを利用できず未実施。

## noncubic境界の相対groupoidとgood/coarse moduli

一致根対の形式局所模型についてAHRの刊行定理（2020年Theorem1.2）の全仮定を照合し、全慣性の線型化から三つの二次不変式ac、(x+y)²、(x−y)²を独立計算した。局所good moduliの原点への微分は零である一方、不変式環は滑らかな三次元多項式環となる。全H2のgood moduliはCで明示的な飽和GIT開から別に構成した。今後はこの局所模型との同定と、既存GITのforgetful射のfiber・慣性を比較する。



[P/G]から内在的被約境界への同値は、標数零の群スキーム慣性、smooth境界chartの相対二形式族への因数分解、相対tilting・反Serre再構成、接空間全射とétale判定を組み合わせる。[境界比較論文Bの節](papers/moduli/noncubic_boundary_comparison.tex)では、正標数のBα_pが幾何点の抽象群単射からのrepresentabilityの反例になることを明示した。一致根対の慣性重みは±2、形式的二変数の不変式はk[[ac]]、good moduli座標χ=1/(1−4ac)は微分零・混合Hessian4である。これらの代数的恒等式は[境界検算](computations/verify_noncubic_boundary.py)と整合する。

表示商全体のgood moduli A¹と、閉gerbeを除くDM開のcoarse A¹は異なる。後者はnon-good、慣性はnonproperである。DM開の任意基底変更に対する粗空間は、有限μ₂局所商を各基底上で再構成して証明する。詳細な証明の依存と未検証箇所は[現行研究ノート](notes/research_notes.md)を参照。

## ローカル組版の最短手順（TeX Live 2026）

**リポジトリ直下**（`README.md` と `.latexmkrc` があるディレクトリ）で、最新版へ更新してから次を実行する。

```sh
git pull --ff-only
latexmk papers/nc-quadric-classification.tex
latexmk papers/nc-quadric-moduli.tex
latexmk papers/nc-quadric-avatar.tex
```

`papers/` に `cd` して `latexmk nc-quadric-classification.tex` とすると、上位の `.latexmkrc` は自動では読まれず、通常の `latex`（LuaLaTeXではない）が選択される。`papers/` にいる場合は `cd ..` して上記を実行する。既に `papers/` で誤ったエンジンの `.aux` / `.fdb_latexmk` が生成された場合、まず `cd ..` してから上記のルート指定ビルドを行う（別ディレクトリの旧出力は新ビルドで利用しない）。

**現行原稿の組版確認状況（2026-11-23）。** C v4.21のbuildは必要TeXファイルを利用できずSKIP（終了コード2）。LuaTeX-jaを含む依存を揃えた環境で、上記の三稿を再組版する必要がある。Cの数式モード、Markdown記号の混入、未定義演算子 `\Spin`・`\SL`・`\Br` は訂正済みで、構成・ラベル・引用・環境の静的検査はPASS。現行PDF全体の生成・表示確認は未実施であり、断片の組版や過去版の成功を代用しない。未解決引用はBibTeXと必要な再実行が完了したログで判定する。

## VS Code / LuaLaTeX の組版環境

リポジトリの `.vscode/settings.json` はOSに依存しない `latexmk` コマンドを使う。macOS・Linux・Windowsのいずれでも、TeX Live（または互換するLaTeX環境）を導入し、**VS Codeの拡張機能プロセスから** `latexmk` がPATHで見える必要がある。WindowsではTeX LiveまたはMiKTeXの実行ファイルディレクトリをPATHに登録する。組版にはLuaLaTeX、`ltjsarticle`、latexmk等が必要である。

macOSでFinder/DockからVS Codeを起動した場合、MacTeXが導入されていても `/Library/TeX/texbin` が拡張機能のPATHに含まれないことがある。この場合、**Macだけのローカル対処**として、VS Codeのユーザー設定（リポジトリで共有しない設定）で `latex-workshop.latex.tools` の `latexmk-project` の `command` を `/Library/TeX/texbin/latexmk` に、`latex-workshop.latex.clean.command` も同じ絶対パスに指定する。共有設定の `cwd` と `args` は維持する。あるいは、`/Library/TeX/texbin` をVS Codeの起動環境PATHに追加してから再起動する。Macの `.latexmkrc` はMacTeXのディレクトリが存在する場合にのみ子プロセスのPATHを補うが、**latexmk自体を起動する前のPATH問題は解決しない**。

VS Codeではリポジトリのルートをフォルダとして開き、`papers/nc-quadric-classification.tex`、`papers/nc-quadric-moduli.tex` または `papers/nc-quadric-avatar.tex` をアクティブにして LaTeX Workshop のビルドを実行する。PDFとSyncTeXは `build/` に出力される。まずターミナルで `latexmk -v` と `lualatex --version` を確認し、ビルドが失敗した場合は LaTeX Workshop のログで `spawn latexmk ENOENT` の有無を確認する。

## Cloud Codexで続ける

[CLOUD_CODEX.md](CLOUD_CODEX.md) に、環境の準備・起動用の依頼文・検証・保存手順を置く。最終目標は研究方針F1–F6を満たす**全H2のpointed exact同値分類**。一補題やcommitで止めず、現行資料を更新しながら次の未解決課題へ進む。

**全H2の分類と、内在的モジュライの有限型smooth Artin性を証明した。** cubic側はlinearデータと、整・被約・非被約を含む全てのVan den Bergh許容四つ組で構成し、四生成環の二次関係に対する有限の代数的判定で重複を除く。noncubic側はP1上の二つの二点集合の非順序対の同時射影同値で分類する。両領域は交わらず、全対象を覆う。統一定理の証明本文は現行原稿に保持し、個別の論理点検と有限次数の厳密計算を行った。全証明の独立監査は未完了である。外部査読・形式証明・包括的な新規性確定とは区別する。組版等の実際の確認範囲は研究ノートを参照。

## 相対構成の現在地

内在的H2は有限型・smooth・既約・純次元3のArtinスタックで、対角はaffine有限表示。cubic開は稠密で、被約noncubic境界Nはsmooth既約純次元1、正則閉埋込みcodim2である。framed実現空間X_asはsmooth既約83次元スキーム。一致根対ではambient接次元84のため、実現像は開でない。

**被約境界の相対商表示と良モジュライ。** `thm:noncubic-intrinsic-presentation-equivalence` により、局所有限型site上で Npres=[P/G]≃N が対象・pointed exact同型を含めて成立する。境界chartの相対normal tiltingと反Serre再構成から実際の族を比較し、慣性核の消滅・接全射・同次元性から表現可能étale性を証明する。非被約testも含むが、全fiber noncubicだけでNへの因数分解を主張しない。χ:N→A¹はflat有限表示のgood moduliで、χ=0はsmooth被約因子の二重構造、χ=1はsmooth chart上ac=0。全慣性は四根相異χ≠0でD8×C2、χ=0で位数32非分裂拡大、一根共有でD8、一致で((Gm⋊C2)×D8)/μ2（8成分）。一致類はBGの正則閉埋込みcodim2をなし、境界接の重みは±2、全HH²は±2,0,0、横断法二方向には連結慣性が自明に作用する。任意の代数空間へのH2の射は一根共有と一致類を同一視するため、全H2にも幾何同型類を分類する粗モジュライ代数空間は存在しない。証明は `papers/moduli/noncubic_boundary_comparison.tex`。

**DM開の粗モジュライ。** 一致類を除いた N^DM→A¹_χ は任意の代数空間に対する粗モジュライ射であり、任意の底変更後も粗モジュライである。この制限射χ_DMはgood moduliではなく、慣性射はproperでもfiniteでもない。二つの根対を順序付けたchartを [A¹/μ2] に帰着し、有限被覆を持つ商の普遍性で粗モジュライを証明する。非good性はcodim2補集合のHartogs、慣性の非proper性はDVR上で延長しない具体的自己同型による。`thm:noncubic-dm-coarse`。

**一致類に沿う形式対と局所良モジュライ。** 全慣性 H=((Gm⋊C2)×D8)/μ2 の有限成分も含むHH²作用を決定した。トーラスの非零重み部分と零重み部分による標準的分裂を用い、境界接を(a,c)、法方向を(x,y)とすると、トーラスの重みは(2,−2,0,0)、二つの符号は法方向に−Id、u,v交換は(a,c)を交換して法方向に−Id、ruling交換は境界接に−Id・法方向の交換として作用する。ruling交換は相対mutationで全Artin変形上に同定する。非標準的な形式対は ([Spf k[[a,c,x,y]]/H], [Spf k[[a,c]]/H]) で、境界はx=y=0、不変式環は k[[ac,(x+y)²,(x−y)²]]。AHRの共通étale商近傍はsmoothな3次元good moduliを持つ。この局所計算のみでは大域化しないが、全体のgood moduliはCの三半不変式による飽和GIT開で別に構成した。`prop:noncubic-coincident-full-normal-representation`, `thm:noncubic-coincident-formal-pair`, `cor:noncubic-coincident-polynomial-invariants`。

相対構成の依存は、cubicの普遍Noetherian性・相対Picard根・canonical AS4 hull、noncubicの有限LG認識・非被約normal tilting・全軌道比較・Noetherian貼合せ・中央AS4延長で閉じる。全幾何点でArtin形式H2変形はpointed Abel変形と一致する。各定理の仮定・証明先・確実性は [研究方針](00_research_plan.md#3-到達点と確実性) に集約する。

**残る比較と次の課題。** 境界の相対商表示・DM開の普遍的粗モジュライ・全有限成分の法表現・一致類に沿う形式対は証明した。全H2の準射影的good moduliはCで構成した。次はその不変式環・noncubic境界像・既存GITとの具体的比較を進める。全H2の粗モジュライ不存在とは両立する。X_asの局所閉性と偏極認識方程式、任意AS/QP表示の全相対groupoid比較、任意Noetherian基底で素朴に同じAbel公理を課す関手と[U/R]の一致も残る。公表前の一次文献比較・証明監査・組版を続け、包括的新規性・外部査読・形式証明とは区別する。

## モジュライのスタック構成

体上の対象クラスを $\mathcal H_2$、有限型基底上の内在的な相対族の fppf スタックを $\mathfrak H_2$ と書く。**相対族の定義、stack 性、反 Serre 関係式への全忠実性を構成した。全体が有限型で滑らかな純次元3のArtinスタックとなる。** 主な証明は [相対定義](papers/moduli/relative_definitions.tex)・[反Serre認識](papers/moduli/relative_recognition.tex) に置く。

有限foundationと次数移動の可逆perfect双加群表示が得られた基底では、次数移動が反Serre関手と線束twistを除いて一致する条件を、**有限表示局所閉部分スキーム**として構成した。非被約底のminor方程式と評価同型を用い、比較のfppf局所存在そのものを表す。[偏極認識の証明](papers/moduli/polarization_recognition.tex)。任意のX3族にこの有限表示を与えること、平方根・AS被覆の局所存在は引き続き別の課題である。

**Artin基底ではさらに進んだ。** 全flat Abel変形に有限foundationとcanonical反Serre軌道環を構成でき、偏極忘却は右逆を持つ。一次の核はHH¹(Λ)であり、二根対一致点の接次元5対4の差をZhang方向として説明する。HH¹(Λ)=0なら全Artin X3変形はcanonical偏極を持つ。異なる根対の全noncubic点ではX3は滑らかで次元83、商は滑らかで次元3となる。[Artin再構成](papers/moduli/artin_foundation.tex)。可換Qのtensor O(1,1)は全Artin Abel変形へexact ampleなSerre根として持ち上がり、そのMorita同型類は一意である。[根の存在と一意性](papers/moduli/artin_roots.tex)。

**可換点の全Artin変形は相対H2に属する。** 二周期cubic列のcanonical hullをArtin基底上で構成し、標準根の全軌道環に相対AS4被覆と正則正規二次切断を与えた。全有限型基底変更を含む昇格命題と合わせ、可換Qの全flat pointed Abel Artin変形が実際の相対H2対象になる。H2からAbel圏への忘却は、この点を中心とする形式変形groupoidの同値であり、変形は無障害、接次元9・無限小自己同型次元6である。[全Artinのhullと形式変形](papers/moduli/quadric_artin_hull.tex)。一次方向については、Jacobian二重導分と右Zhang twistによる[明示構成と検算](papers/moduli/quadric_first_order.tex)も保持する。全cubic点では相対Picard根とquintuple持上げを用いることで、根のHH²自明作用を追加仮定せず全Artin認識が成立する。noncubic点でも中央被覆の局所延長により全Artin認識が成立する（`cor:noncubic-all-artin-h2`）。全H2の有限型代数性は `thm:global-h2-smooth-finite-type` で成立する。

**標準平方根はétale近傍へ代数化できる。** 有限foundation表示上のMorita自己同値の代数空間と平方写像を使い、可換点の標準根を実際のperfect双加群と平方同型としてétale近傍へ延長した。[根の代数化](papers/moduli/artin_roots.tex)、`prop:quadric-etale-morita-root`。その近傍では、標準foundationに対して根がF0→F2、F1→F3と作用する同型を構成し、全四項窓のfull strong exceptional性、Hom階数2/4/6/9、三次関係rank2・四次重なりrank1の非退化性を任意底変更について証明した（`prop:quadric-etale-finite-window`）。全距離のHomと三次提示は上記の相対解消で解決した。canonical compact/Serre認識は相対cubic tailsの証明で成立した。単一有限型開上の左右Noetherian性と相対H2実現は上記の定理で成立した。相対H2全体の代数性は下記の有限型atlasで成立する。特殊fiberのrankと非退化性の独立な厳密検算は [`verify_quadric_finite_windows.py`](computations/verify_quadric_finite_windows.py) に収録した。

族は基底変更と descent を備えた noetherian Abel 圏と構造対象 O の対である。導来条件には局所的な canonical compact 部分 $D(\operatorname{Ind}\mathcal C)^c$ を用い、特異基底上でそれを全 $D^b(\mathcal C)$ と同一視しない。平方根・根同型・AS被覆は fppf 局所の存在条件であり、標識に加えない。標数零の代数閉体上では元の $\mathcal H_2$ の pointed groupoid を回復する。

| 相対モジュライに関する結果 | 状態・証明の所在 |
| --- | --- |
| $\Phi:\mathfrak H_2\to[X_3/\mathrm{PGL}_9]$ は全忠実 | 相対AZ再構成とpointed二自己同型の自明性。[相対定義節](papers/nc-quadric-moduli.tex) |
| 対角はaffineかつ有限表示 | 表示スタックの対角の引戻し。同節 |
| $X_{\mathrm{as}}=X_3\times_{[X_3/\mathrm{PGL}_9]}\mathfrak H_2$ は不変fppf部分層、$\mathfrak H_2\simeq[X_{\mathrm{as}}/\mathrm{PGL}_9]$ | 有限型smoothスキームX_asによる商表示。dim X_as=83、dim H2=3。`cor:global-xas-smooth-scheme` |
| 全H2の切断環・反Serre環はKoszul | 正則正規二次商とVeroneseの既知定理を適用。[相対Koszul節](papers/moduli/relative_koszul.tex) |
| 三次まで平坦＋全幾何fiberがKoszulなら全次数平坦 | PP2005 Chapter 6 Theorem 7.3を任意の非被約Noetherian基底に適用。相対Koszul解消も任意底変更と整合 |
| H2点の任意のArtin基底上の $X_3$ 変形はflatなpointed Abel変形を与える | noetherian性の持上げと $\operatorname{qgr}$ による構成。同節。表示の次数移動が反Serreになることは別条件 |
| Artin上の根・全軌道AS被覆から、全有限型基底変更を備える相対H2族を構成 | [Artin再構成節](papers/moduli/artin_foundation.tex)、prop:artin-witness-relative-promotion |
| 可換Qの全Artin Abel変形は相対H2、形式変形groupoidの忘却は同値 | 相対canonical hullと全有限型基底変更への昇格。無障害、接HH²(Q)は次元9・無限小自己同型HH¹(Q)は次元6。[全Artin節](papers/moduli/quadric_artin_hull.tex)。大域代数性とは区別する |
| 固定した相対切断環へのAS4被覆は有限表示のincidenceで判定できる | 四次までの元の積・五次までの二次双対・Frobenius条件。[相対被覆節](papers/moduli/relative_as_cover.tex)。任意基底変更のnoetherian性は明示した仮定の範囲で用いる |
| pointed Abel圏が一定で、反Serre表示からは外れる $\mathbb G_m$ 上の二次環族 | [偏極の変形](papers/moduli/antiserre_polarization.tex)。$q=2$ で中心一次部分が消滅し、どのH2のcanonical反Serre環でもない |
| 同族の非零接方向は一定のpointed Abel変形へ写る | 中心元 $u^4,v^4$ の交換子が $16\varepsilon u^4v^4$。計算機に依存しない証明と[厳密検算](computations/verify_antiserre_polarization.py) |

$X_3\subset\mathrm{Gr}(56,81)$ は三次関係行列の階数がちょうど176となる局所閉スキームであり、商は有限型Artinスタックである。その全体を $\mathfrak H_2$ と同一視できないことは、上記の偏極変形で幾何点についても明示した。有限型incidenceのfppf像は一般には代数空間とは限らないため、AS被覆を選ぶ空間の構成だけで存在条件の代数性を結論しない。

既存の foundation 表示 $\mathfrak Q_{\mathrm{fnd}}$ は滑らかな有限型Artinスタックで次元3、ruling交換を忘れる写像は有限étale二重被覆である。全H2幾何点groupoidが全充満に入り、cubic非空開と全noncubic点へのpointed smooth proper dg特殊化を持つ。反Serre環としても全次数平坦な特殊化となるが、これらの族が相対H2の全条件を満たすことは未証明である。[foundation節](papers/moduli/foundation_stack.tex)

noncubic表示商 $\mathfrak N^{\mathrm{pres}}$ は滑らかな有限型Artinスタックで次元1。全幾何点のpointed慣性、符号 $\mu_2^2$ gerbe、good moduli $\mathbb A^1_\chi$、coarse moduli algebraic spaceの不存在を記述した。相対Clifford表示、perfect Serre公式、選択不要な反Serre環とそのnoetherian heartも構成済みである。[noncubic節](papers/moduli/noncubic_stack.tex)

noncubicの三代表点では $\dim HH^1(R)_0=(1,1,2)$、$\dim HH^2(R)_0=(3,3,5)$。関係式の接次元は正確に83,83,84で、群軌道と六係数の和は81次元である。横断2,2,3方向の全二次障害が消え、既存の二次jetは上記Koszul原理により全次数平坦となる。二根対一致点における $X_3$ 商とfoundation商の接次元5対4は、相対H2の接次元は別途Abel変形と比較し、一致根対で4と証明した。

**成分に関する現在の結論：** foundation実現点集合は誘導位相で既約・連結、成分数は各1。cubic/noncubicの表示商の非交和は人工的に2成分になる。内在的 $\mathfrak H_2$ 自身も、実際のcubic族と境界chartによって既約・連結、成分数各1と証明した。foundation表示の誘導位相との同一視はこの証明に使わない。

**Noetherian 性の形式的貼合せ。** 可換Noetherian基底R、各次数成分が有限な中央次数環A、I=(f₁,…,fᵣ)に対し、A/IAと全A[fᵢ⁻¹]が左右NoetherianならAも左右Noetherianとなる。次数ごとのI進完備化で有限生成元の係数を収束させ、R̂_I×∏R[fᵢ⁻¹]の忠実平坦性で降下する。成分の平坦性・有限Krull次元は不要で、一般次数付き加群とZ代数のrow/columnにも成立する。証明 `thm:patch-noetherian`、`thm:patch-z-algebra`。幾何的cubic族では、閉部分と開補集合で実際のNoetherian性を確認して適用する。

**非可換P¹束の対角列の障害。** 滑らかな(2,2)曲線と次数二線束から全隣接縮約が非零のgeometric quintupleを構成した。しかし対応する層対称代数の候補対角列Kₙ=π(O(n)⊗e₋ₙA)は、全ての行からHomが零になる非零coherent対象を持ち、AZ生成条件を満たさない。二次解消を用いて全整数でωπMの成分がO(−2)となることを直接証明した。これは当該模型・軌道列の比較への障害であり、本来のcubic環BのNoetherian性の反例ではない。[対角列の反例の完全な証明](papers/moduli/ruled_diagonal_obstruction.tex)（論文B）。本来のBのNoetherian性は、曲線商・正規拡大とlinear部分の形式的貼合せによって解決した。

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
| [papers/moduli/relative_cubic_tails.tex](papers/moduli/relative_cubic_tails.tex) | 普遍cubic解消、canonical導来比較、Noetherian基底での全相対認識 |
| [00_research_plan.md](00_research_plan.md) | 研究一般の原則・保存許可、目標、到達点、次の具体的な着手 |
| [CLOUD_CODEX.md](CLOUD_CODEX.md) | Cloud環境の準備、起動用の依頼文、検証・保存・再開の手順 |
| [scripts](scripts) | 依存の準備と、構成・検算・組版の独立した確認 |
| [papers/nc-quadric-classification.tex](papers/nc-quadric-classification.tex) | 本文のある主論文。日本語LuaLaTeX、著者欄空欄 |
| [papers/nc-quadric-avatar.tex](papers/nc-quadric-avatar.tex) | 指定AS分解・avatar分類、相対pointed認識、QP・GIT比較を扱う独立した日本語LuaLaTeX論文 |
| [papers/quiver-avatar](papers/quiver-avatar) | CのAS分類・有限QP・foundation・幾何的chart・pointed認識と相対比較の証明 |
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

主論文v1.44のsourcesはPASS（50 manuscript files / 610 labels / 288 citation uses / 7 Markdown files）。DM開・全有限慣性作用を含む `verify_noncubic_boundary.py` と `verify_stack_symmetries.py` はPASS。buildは必要なTeX依存不足によりSKIP（終了コード2）で、新しいPDF・画像確認はない。既存v1.40の組版記録は研究ノートに保持する。

repoルートで実行する。

```sh
bash scripts/bootstrap.sh
python3 scripts/check.py doctor
python3 scripts/check.py all
```

別稿は次で個別に確認・組版する。

```sh
python3 scripts/check.py sources --manuscript papers/nc-quadric-avatar.tex
python3 scripts/check.py build --manuscript papers/nc-quadric-avatar.tex
python3 computations/verify_quiver_avatar_charts.py
python3 computations/verify_quadric_first_order_roots.py
```

出力は `build/nc-quadric-avatar.pdf` と同名の `.synctex.gz`。ルートの `latexmk` は両論文を組版する。

Python 3.9以上とSymPy、およびLuaTeX-jaを含むTeX Live/MacTeX、latexmk、BibTeXを用いる。出力は `build/nc-quadric-classification.pdf` と同名の `.synctex.gz`。PDF・組版中間物はGitで追跡しない。

`sources`・`math`・`build`を個別に実行できる。検証の終了コードはPASS=0、FAIL=1、SKIP=2で、未導入の依存による未実施を成功と区別する。`doctor`は診断のみ。bootstrapは不足依存を`PARTIAL`と表示して処理を終え、数学的研究を止めない。TeX導入を試すオプションは`bash scripts/bootstrap.sh --with-tex`。従来どおり`python3 computations/verify_quadric.py`と`latexmk`も使える。

VS Codeではrepo全体を開き、LaTeX Workshopの推奨拡張と既定の `latexmk (LuaLaTeX, project settings)` レシピを使う。設定はresearch-hubの雛形に準拠し、`.latexmkrc`がエンジン・作業ディレクトリ・出力先を統一する。VS Code UIの操作確認とコマンドによる組版確認は区別する。

## 構造対象の忘却

**楕円型の全O標識と有限・無限の忘却。** 滑らかな楕円四つ組でδ≠0、η∉Zδなら、RTと対角根から全Z²のrank-one torsion-free exceptional対象を構成し、数値類ごとの一意性で全てを尽くす。全てがH2の構造対象となる。Uₙ=(E,L₀,L₁⊗(L₂L₀⁻¹)ⁿ,L₂)を代表とし、εδ=δかつε(η+nδ)∈{η+mδ,2δ−η−mδ}という有限楕円自己同型群を含む必要十分条件でpointed重複を判定する。δ非捩れなら可算無限、位数rならZ/rZの有限商となる。余分な自己同型がなく2η∉⟨δ⟩なら正確にr個。証明は `thm:elliptic-marking-lattice-fiber`、`cor:elliptic-torsion-fiber-cardinality`。Z²と二面体作用はKitamura–Okawaの既存announcementと重なるため新規性を主張せず、ここでは指定範囲の独立証明と明示的な忘却判定を与える。η∈Zδ、退化曲線、noncubicの忘却と相対stack射は未解決。

固定圏上の2-fiber（許容構造対象のgroupoid）と、自己同値で割った同型類ファイバーを区別する。証明は [現行節](papers/moduli/marking_forgetting.tex)、仮定と残る問題は [研究ノート](notes/research_notes.md) を参照。

## 関連研究

[research-hub](https://github.com/uedakazushi/research-hub) が研究全体の入口。[nc-cubic-classification](https://github.com/uedakazushi/nc-cubic-classification)とはO標識とAS4表示の考え方を比較するが、その未監査の完全分類定理には依存しない。Serre根一般は [categorical-fano-index](https://github.com/uedakazushi/categorical-fano-index) と関係する。既存のquadric分類・Okawa–Uedaのmoduliとの具体的比較は文献ノートを正本とする。


### 境界模型の再現と確認範囲

`python3 computations/verify_spectral_boundary_models.py` は、二traitのblowup chart、符号共役、固定点排除、一致型の模型同型・四捩れ補正・conic順序、分岐節点のtoric式を厳密演算で検算する。2026-11-23に12項目PASS。全halving式、I4のpencil次数、重み付き次数の有限例、Fricke全群作用と補助平方根のoverlap恒等式も含む。一般のgraph同定・最小性・スタック降下・新規性は有限計算の認証対象ではなく、原稿の証明と読取りに分ける。三原稿の参照検査は `python3 scripts/check.py papers`。LuaLaTeXは必要依存を利用できず、現行PDFの生成・表示確認は未実施。
