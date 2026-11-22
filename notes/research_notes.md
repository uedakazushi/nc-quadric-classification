# 現行研究ノート：O-marked 非可換 quadric

2026-11-23 / v1.50（A v1.69・20節、B v0.41・31節、C v4.43）。最初に [研究方針](../00_research_plan.md) を読む。体上分類の証明は [論文A](../papers/nc-quadric-classification.tex)、移管済みの相対理論の証明は [論文B](../papers/nc-quadric-moduli.tex)、文献確認の正本は [文献比較](literature.md)。本書は作業履歴ではなく、現在有効な知識と再開点を記す。

## 二massのQP・有限foundation・Jacobian/Serre・H2を結ぶ現行定理

**範囲と主張状態。** 論文CのC1（既存AS/avatar・標準頂点・相対tailsの分類範囲）とC2（全H2 good moduliの明示）は**原稿上達成**。C3も**H2実現可能な明示開全体**では次の比較・glueを原稿上証明したが、H2外の任意AS/avatar/QP表示stack全体の分類とC4の独立数学監査は未完了。[主たる証明](../papers/quiver-avatar/cubic_qp_foundation_groupoid.tex)。

**相対finite groupoidとmass。** 共通十二矢potentialは `W=H+yq+px+vq'+p'u+λyx+μvu`。階数五の二段道束 `D_a,D_b` を短関係 `r_a=q'+μu, r_b=q+λx` で割り、rank12三段道束の短関係四本・残余長関係二本をrank六直和因子として割ると、rank24 directed finite foundationの全積を回収する。QP表示groupoid→finite foundationはfppf局所essentially surjective、Isom全射、kernelは `U_λ×U_μ`、`U_λ=Spec R[t,(1+λt)^(-1)]`、群法則`t⋆s=t+s+λts`。両rank3の特殊幾何点ではGa²、両mass単元でGm²、nilpotent mass上でもsmooth/flat。元のraw `H+εyx`の非平坦な対角scalar慣性は別モデルであり、実際のAS族のsmooth gaugeと同一視しない。

**相対二段対角解消の一般的な独立証明。** 四頂点の有限矢束$V_{\rm fin}$は階数8，関係束$R_{\rm fin}$は階数4（短関係各1、残余長関係2）。自由有向道代数$F$は階数32で，その通常の関係ideal$I=(R_{\rm fin})$の非零成分は$(0,2),(1,3),(0,3)$のみ。短関係二本とその三段合成四本・残余長関係二本がそれぞれ局所直和因子をなし、$I$の階数は$1+1+4+2=8$，商$\Lambda=F/I$は階数24。非可換普遍導分のconormal表示により，$\Lambda\otimes_D R_{\rm fin}\otimes_D\Lambda\to\Lambda\otimes_DV_{\rm fin}\otimes_D\Lambda$の像は後者から$\ker(\Lambda\otimes_D\Lambda\to\Lambda)$への全射の核に一致する。このkernelの階数は$52-(68-24)=8$，関係項も階数8なので両者は同型。**従って一般有限foundation上の相対対角解消は任意非被約基底で局所分裂完全**となり，任意base-changeと両立する。これは前回の四境界型の数値検算に依存しない。[一般Euler--conormal補題とC3の証明](../papers/quiver-avatar/cubic_qp_foundation_groupoid.tex)。$\Lambda^e$相対局所射影性は頂点代数$D=\mathcal O^4$のseparabilityによる。Keller2011の訂正で必要なordinary ideal生成を確認したが，**非最小十二矢QPのdg双対化・cyclic derivative比較，左右Noether/AZ・実際のheart・S₂貼合せは独立に監査する必要がある**。

**非最小QPのdg微分を明示したJacobian/H⁰Π₃比較。** 分裂完全な三項双加群解消$P_2\to P_1\to P_0$を双対化・$[2]$ shiftすると，関係双対$P_2^\vee$がcohomological次数0，矢双対$P_1^\vee$が-1，頂点双対$P_0^\vee$が-2となる。関係束の局所枠$r_\alpha$と逆向き矢$r_\alpha^*$を選び，canonical cyclic contraction$\mathcal W_{\rm rel}=\sum_\alpha(r_\alpha r_\alpha^*)_{\rm cyc}$を作ると，degree -1の矢双対$v^*$の微分は$\partial_v\mathcal W_{\rm rel}$。従って$H^0T_\Lambda(\Theta_\Lambda)=T_\Lambda(R_{\rm fin}^\vee)/(\partial_v\mathcal W_{\rm rel})$であり，$\Lambda=F/(r_\alpha)$を展開するとordinary Jacobian両側idealによる商となる。関係枠の変更は双対枠と相殺し，分裂完全な解消の基底変更と整合する。nonminimalなmass矢があってもこの$H^0$計算は成立するが，Kellerの最小関係版定理を無条件に引用しない。これは**原稿に直接証明を追加し，次数・ideal・base-changeの推論を今回読取り確認した状態**であり，全right-equivalence groupoidとrelation liftのcoherent降下・AZ/Noether/heartの包括的独立監査は残る。[C3のJacobian比較](../papers/quiver-avatar/cubic_qp_foundation_groupoid.tex)。

**残余長関係liftのcoherent right-equivalence（一般係数で証明済み）。** 二つの短関係$r_a=q'+\mu u,\ r_b=q+\lambda x$の三段合成は$K=(W\otimes r_a)\oplus(r_b\otimes U)$という階数4直和因子を作る。残余長関係の二つのliftの差を$\alpha(r_i)=w_i r_a+r_bu_i$と書くと，relation potential$\sum_i t_ir_i+vr_a+yr_b$の変化は$\sum_i t_iw_i r_a+\sum_i t_ir_bu_i$。後半を巡回回転すると$\sum_i u_it_i r_b$なので，重み保存の三角right-equivalence$v\mapsto v+\sum_i t_iw_i,\ y\mapsto y+\sum_i u_it_i$で正確に吸収できる。元の矢・$t_i$は固定され，逆変換は符号反転，合成は加法的である。関係枠GL変換と双対の逆転置を組み合わせると重なりのcocycleは厳密に成立し，nilpotent massを含む任意の非被約基底で成り立つ。これは**同じ有限foundationのrelation liftの変更**に関する結果であり，異なるruling間のmutationを単一raw QP right-equivalenceとして構成したことを意味しない。[C3のshear補題](../papers/quiver-avatar/cubic_qp_foundation_groupoid.tex)。局所liftの自由度は解決したが，massゲージ・頂点scalars・二ruling mutationを同時に含む全Isomとcoherent stack貼合せの独立監査，AZ/左右NoetherとC4組版は未完了。

**massゲージとlift shearの半直積・頂点scalarの中心性（新しく原稿上証明）。** 長関係の局所liftのshearを$\phi_\alpha$とし、$L_y=\sum_i u_it_i$、$L_v=\sum_i t_iw_i$と置く。massゲージ$g_{t,s}$について$a=1+\lambda t$、$b=1+\mu s$とすると、$g\phi_\alpha g^{-1}$は$y\mapsto y+aL_y$、$v\mapsto v+bL_v$であり、rank8加法的lift変更群には$(w_i,u_i)\mapsto(bw_i,au_i)$と作用する。shear後の標準potentialは$p^\alpha=p+\lambda L_y$、$(p')^\alpha=p'+\mu L_v$を持ち、$\phi_\alpha g\phi_\alpha^{-1}$は変更後のpotentialを保つmassゲージに一致する。標数零の双対数$R=k[\varepsilon]/(\varepsilon^2)$、$\lambda=\varepsilon$、$t=1$、$L_y\bmod\varepsilon\ne0$の場合、交換子は$y\mapsto y+\varepsilon L_y$で非自明。特殊fiberでは可換なので、幾何点の群から相対可換性を推論できない。頂点scalarのトーラス$\mathbb G_m^4/\mathbb G_m$は道の始終点比で作用するため全頂点固定right-equivalenceと厳密に可換し、局所二段剛体化の順序は可換。shearは異なる局所liftの間の変換であって固定potentialの慣性そのものではない。これらは$S_2$-ruling mutationの全coherenceやgerbe大域自明性を自動的に与えない。証明は論文Cの prop:qa-q12-mass-shear-compatibility、ex:qa-q12-mass-shear-first-order-commutator、lem:qa-q12-vertex-scalars-central。検算コードcomputations/verify_q12_mass_shear.pyを通常math suiteへ登録した。独立の局所Python記号計算はcyclic potential、shear、共役、target係数、双対数の五群でPASS。GitHub上に保存した同コードのbyte同一再実行、現行C全稿組版、C3/C4全証明の包括的監査は未実施。

**mass kernelの線束値降下とstrict square $S_2$（原稿上証明）。** 短関係$r=q+\lambda x$に対し、一般の局所再標識$x'=dx+h,\ r'=cr$（$c,d$単元、$h$は隣接矢の二段道）では$q'=cq-(c\lambda/d)h,\ \lambda'=(c/d)\lambda$となる。massゲージは$x\mapsto x+tr$なので$t'=(d/c)t$、従って$a=1+\lambda t$はframe不変。線束$\mathscr L=\operatorname{Hom}(\mathscr X,\mathscr R)$、$\lambda\in\Gamma(\mathscr L^\vee)$により$\mathcal U_{\lambda,\mathscr L}=\{t\in\mathbb V(\mathscr L):1+\langle\lambda,t\rangle\ne0\}$という大域滑らかなgroup schemeが**QP表示stack上**に定義される。$\lambda\ne0$上は標準$\Gm$、$\lambda=0$上は$\mathbb V(\mathscr L)$。冪零massの打切り対数も$\mathscr L$値多項式として降下するため、加法群の大域的なline-bundle twistを保持する。これらの線束がfinite foundation側に降下するとは主張しない。別にsquare表示のstrict対合$(A,B,C,D,W;f,g)\leftrightarrow(B,A,D,C,W;g,f)$は頂点scalar核$K_\square$を保ち、$\sigma^2=\mathrm{id}$。二段剛体化後のQP商はsquare開スタックと同値なので、strict作用はcoherentなweak $S_2$作用へ運ばれ、unit/counitの三角恒等式で2-cocycleが閉じる。raw QPの単一right-equivalenceとしてのswapは主張しない。証明位置：[C3の線束値massとstrict square $S_2$](../papers/quiver-avatar/cubic_qp_foundation_groupoid.tex)。独立記号検算：一般再frame式、群法則、nilpotent log、squareのscalar核交換をPASS。GitHubの現行スクリプトを直接実行したとは主張しない。残る監査は全Isomから相対heartへのcoherent降下、反Serre/AZ・左右NoetherとC4公表前検証である。

**normal helixの全次数perfect-fiber監査。** 論文Aのthm:normal-helixを直接確認し、幾何四周期helixで$E_{j+4n}\simeq t^nE_j$、$n\ge1$なら$j+4n\ge i$による全前向き$\operatorname{Ext}^{q>0}(E_i,t^nE_j)=0$、$n=0$はstrong exceptional、負のExtはheartから零と確認した。有限双加群対角解消から$P_n=\Theta_\Lambda^{\otimes_\Lambda^{\mathbf L}n}$は固定した各$n$で基底perfect。全幾何fiberの次数零集中に局所自由模型の可縮対消去を適用し、非被約底でも$H^0(P_n)$の局所自由性・任意非平坦基底変更を得た。Cのlem:qa-q12-all-degree-perfect-fiberに証明。Euler行列$G$で$N=(G^{-1}G^{\mathsf t})^{-1}-I$が$N^3=0$なので階数$64n^2+64n+24$、SymPyで全$n$式と$n=0,\ldots,5$の$(24,152,408,792,1304,1944)$を検算PASS。これらは各次数のflatnessであり、全次数を合わせた環の左右Noether性やpointed heartを数値だけで認証しない。相対AZの二重presentation・非先頭構造対象の仮定・有限End/Hom条件は修正し原稿に証明した。次は全fppf Isomと相対heart貼合せの独立監査、C4全稿組版。

**反対normalの$H_2$障害と左Noetherの正しい相対AZ証明。** Squareの反対対合$(A,B,C,D;f,g)\mapsto(D,C,B,A;g\tau,f\tau)$は全四交差$H_2$開を保存するが，逆順反対\emph{normal}の零番は強いpointingを一般には与えない。具体例$f=I_4,\ g=\left(\begin{smallmatrix}1&0&0&1\\0&1&-1&0\\0&1&1&0\\-1&-1&-1&-1\end{smallmatrix}\right)$は$\operatorname{rk}g=3,\ \det M_f=-1,\det M_g=16$で元の$H_2$開にある一方，反対normalの逆squareでは交差行列が両方階数1となる。[反例と証明](../papers/quiver-avatar/cubic_qp_foundation_groupoid.tex)、[再現計算](../computations/verify_square_h2_open.py)。修復では反対squareの相対heart$\mathcal C^\vee$の構造対象を$Q_0$とし，$Y=(\mathbb DZ_1,Q_0,Q_1,Q_3)$を線束値比較$K=\mathbb D(t^{-1}Z_1)\simeq Z_2^\vee\otimes L$と$t^\vee$の完全性から同じheartのflat compact tilting四項として構成する。$\mathbf RHom(\mathbb DX_i,(t^\vee)^nQ_0)\simeq\mathbf RHom(E_3,t^nX_i)$の$n\ge1$前向きExt消滅を使う。AZ生成の命題は，**最初から$E_a\simeq\mathcal O$となる任意の$a$を許す形に訂正**した。AZ2は$K$とそのkernel $L$への二段の$\mathcal O$-軌道全射，$L'$を二段目のkernelとして$\Ext^1(t^{-n}E_i,K)\hookrightarrow\Ext^2(t^{-n}E_i,L)\hookrightarrow\Ext^3(t^{-n}E_i,L')=0$から得る。最後には基底flat compact始域に対する相対Ext$^{>2}$消滅を使い，特異基底全体のglobal dimension 2を仮定しない。さらに任意のNoetherian affine基底$R$では$A_0=\End(T)$は有限$R$-加群なので右Noetherian，$\Hom(T,K)$も有限右$A_0$-加群である。Artin–Zhang Theorem4.5(1)，OACU Theorem7.3の全条件を明示的に満たし$C(\Lambda^{\rm op})$が右Noether，従って$C(\Lambda)$は左Noether。[AZ補題と有限End検査](../papers/quiver-avatar/relative_square_tails_recognition.tex)・[反対normalの完成](../papers/quiver-avatar/cubic_qp_foundation_groupoid.tex)。**古典模型の独立検算：** $\PP^1\times\PP^1$では$Y=(\OO(0,-1),\OO,\OO(1,0),\OO(1,1))$，第二項が$Q_0=\OO$で，$t^\vee=-\otimes\OO(2,2)$。Künneth公式で全正高Ext消滅，16組のHomの和$64n^2+64n+24$（全$n\ge0$）を計算した。[C3例](../papers/quiver-avatar/cubic_qp_foundation_groupoid.tex)と[厳密検算](../computations/verify_q12_diagonal_euler.py)に収録した。実際の相対heart比較・全fppf Isomの完全な独立監査とC全稿組版は未完了。

**内在的H2上のSerreとpointed heart。** 既存の有限square↔normal foundation相対同値と全H2の明示開を使い、normal full strong `T=⊕E_i` を実際の相対heart内に取る。 `Θ_Λ^{⊗^L n}≃RHom(T,tⁿT)` のforward Ext消滅とperfect-fiber判定により、全 `n≥0` で `Jac(Q12,W)_n≅Hom(T,tⁿT)` と基底変更を得る。Euler行列 `G=[[1,2,4,6],[0,1,2,4],[0,0,1,2],[0,0,0,1]]` の `(G^{-1}Gᵗ)^{-n}` から全階数 `64n²+64n+24`。相対AZ ample・opposite square dualizationから左右Noetherと `(qgr Jac,πe0Jac,(1))≃(C,O,t)` を得る。対応は**H2実現可能開**であり、一般のraw QPには拡張しない。

**二段剛体化とruling交換。** raw QPのmass kernel `U_λ×U_μ`をIsom sheafから剛体化し、さらに頂点scalar `Gm³`を剛体化すると、既証明のfinite square/normal相対groupoidにより `H₂^rul` を得る。coherentな二ruling交換は有限squareの中間頂点交換と相対perfect mutationで実現し、S2商で `H₂` を得る。二cubic正規化 `T,T⁻¹`は一般にはright-equivalenceでない。つまりrulingの貼合せはraw QPの一つの座標変換でなく、選択窓のmutationと同じheartへのAZ認識で行う。

**二mass四境界型と冪零基底の独立した監査。** 有理数上の$q=q'=I_2$（非分解可能）と，三段関係$W_0V_1U_0=W_1V_0U_1=0$を固定し，$\Lambda_{\mathbb Q[\lambda,\mu]}$を構成した。短関係は$q'+\mu u,q+\lambda x$，三段関係の$12\times6$行列は最初の六行が行列式1なので，全二変数族で有限代数は階数24の自由加群。4種類の幾何型 $(\lambda,\mu)=(0,0),(1,0),(0,1),(1,1)$ に対し，二段積・三段積・四項関係・両側の非可換微分を整数行列として実装した。各組で$C_2=\mathbb Q^8\to C_1=\mathbb Q^{52}\to C_0=\mathbb Q^{68}\to\Lambda=\mathbb Q^{24}$，$\partial_1\partial_2=0$と$\operatorname{rank}(\partial_1,\partial_2)=(44,8)$を厳密に検算した。rank下界は法101の消去，rank上界は終項の分裂全射と列数で証明した。これらは浮動小数点近似でない。非零massは対角矢をスカラー倍して1へ移せるので，この**指定された二変数族**の全標数零幾何fiberで複体は完全であり，局所自由項のconstant-rank判定から$\mathbb Q[\lambda,\mu]$上で分裂完全，従って任意の$\mathbb Q$代数への基底変更後も完全となる。この数学的帰結は四標本の数値傾向の外挿ではなく，族の正規化と分裂性の論証に依存する。証明位置：[C3の明示族補題](../papers/quiver-avatar/cubic_qp_foundation_groupoid.tex)、再現：python3 computations/verify_q12_bimodule_diagonal.py。ローカルで同じ代数構成の4型検算は全PASS。GitHubに更新したソースの直接再実行・全既存suiteの再実行は未実施。**指定四境界型の計算だけでは一般stackは認証できないが，上記のEuler--conormal補題が別途一般相対完全性を証明する。**

**冪零massでの慣性群の加法化。** $\lambda^N=0$かつ基底が$\mathbb Q$代数なら$\mathcal U_\lambda=\operatorname{Spec}R[t,(1+\lambda t)^{-1}]$は$z=\sum_{j=1}^N(-1)^{j-1}\lambda^{j-1}t^j/j$で$\mathbb G_a$に同型（逆は$t=\sum_{j=1}^N\lambda^{j-1}z^j/j!$）。$\lambda=\epsilon,\epsilon^2=0$では$z=t-\epsilon t^2/2$。二massがともに冪零なら局所ゲージは$\mathbb G_a^2$となる。これは全mass軸のGm/Ga遷移やgerbeの大域自明化を主張しない。証明は[C3のnilpotent log補題](../papers/quiver-avatar/cubic_qp_foundation_groupoid.tex)。一般係数での相対対角分裂・ordinary idealは一般補題で原稿上証明済み。双対dg模型とcyclic derivativeの明示式もC原稿上追加した。次は関係lift・同型層のcoherent降下、左右Noether/同じheart・ruling mutationをさらに監査する。

**数値検算。** 数値Eulerの16頂点対で総階数(68,52,8)→24、normal Serreの全次数式 `64n²+64n+24` はSymPyの整数・記号計算で独立検算した。[再現コード](../computations/verify_q12_diagonal_euler.py) をGitHubに記録したが、当該GitHubファイルの再取得・同一byte実行は未実施。数値は対角複体の完全性やfppf同値の形式証明ではない。Keller ordinary idealと相対対角の全基底変更・normal反対代数からの左Noetherは現行Cの証明を入口に監査済み。次は全IsomとS2/coherent heartを独立監査し、C4の一次文献比較・LuaLaTeX全稿組版・PDF表示を実行する。H2外の一般AS/avatar表示の分類の追加可能性は独立に評価する。

## 全H2のGram pencil不変式環と明示good moduli

**現行結論（論文Cの定理）。** 二つのGram二次形式 \(S_f=fJf^{\rm t},S_g=gJg^{\rm t}\) の四次pencilの係数を \(F^2,I_1,I_2,I_3,G_0^2\) とし、\(A_2=FG_0,B_2=I_2,X_3=FI_3,Y_3=G_0I_1,D_4=I_1I_3,C_3=X_3+Y_3\) とする。順序付きの半不変式環は \(k[A_2,B_2,X_3,Y_3,D_4]/(X_3Y_3-A_2D_4)\)、非順序は \(k[A_2,B_2,C_3,D_4]\)（重み2,2,3,4）。非順序good moduliは重み付き射影三空間の明示開である。\(L_2=B_2-2A_2,\ \Delta_8=(D_4+4A_2L_2)^2-4L_2C_3^2\) と置けば \(\Delta_8=256P_fP_g\)、中央affine chartは \(D_+(\Delta_8)\)、座標環は重み零局所化。noncubic閉曲線は\(A_2=C_3=0,\ D_4\ne0,\ \chi=B_2^2/(4D_4)\)。特異点は\(p_3=[0:0:1:0]\)の\(1/3(1,1,2)\)と\(p_4=[0:0:0:1]\)の\(1/2(1,1,1)\)だけ。**全証明**は [CのGram pencil節](../papers/quiver-avatar/global_h2_invariant_hull.tex) へ移した。一般の二対称形式pencilの不変式定理はBhargava–Gross–Wang §4.2の既知結果であり、本研究では線形化・ruling交換・H2開・noncubic境界への適用を証明した。包括的新規性は未確認。

**検証・次の核心。** SymPyで四行列の稠密標本と階数三の標本、binary二形式正規形で交差多項式と\(\Delta_8\)、\(\chi\)を厳密算術で検算した。再現コードは `computations/verify_global_h2_pencil_invariants.py`。**GitHub上の同ファイルをGit blob SHA `85c78e1b7eaac07a05b5a8708ee9bc0e1f15dc34` と照合したローカルコピーで実行し、境界記号式・有理数4組（rank3を含む）・Hilbert係数が全てPASS**。これは不変式環の有限生成・相対群oidを形式証明したものではない。C2の大域good moduliの環・中央chart・二特異点の記述は原稿上到達した。**現行優先はC3の独立監査とC4の文献・組版・公表準備である。** 全H2実現可能開の二mass相対QP/foundation、ordinary Jacobian/Serre、二段剛体化とruling mutationはC3原稿上の証明に到達した。外側の全AS/avatar/QP stackとH2の無条件同値を主張せず、一次資料の仮定・一般非被約底・Noether性・coherent descentを検証する。

## 全H2の三半不変式と良モジュライ

**全H2の準射影的良モジュライ。** 左右kernel条件は P(M)=det M、Q(M)=e3(JMᵗJM) の二式へ集約できる。二つの交差行列について s0=(PfPg)³、s1=Pf³Qg²、s2=Qf²Pg³、s3=(QfQg)² とすると同じ指標χ0²⁴を持ち、s1s2=s0s3。非順序H2開は s0,s3,s1+s2 の三非消滅開で覆われる。各開はアフィン商で、重なりは不変な比の非消滅開なので飽和している。全H2と順序付き被覆のgood moduliは半不変環のProjの開となり、分離的・有限型・準射影的なschemeである。幾何同型類を分類するcoarse moduliの不存在と両立する。三式が半不変環を生成するとは主張しない。 [証明](../papers/quiver-avatar/global_h2_good_moduli.tex)。

**構成の根拠。** G=((GL2)^4×GL4)/K、H=G⋊S2、χ0=detW/(detA detB detC detD)。RΓ(χ0)=(k[A32,z])^Γ は有限生成でR0=k、共通重み24の切断hに対して (RΓ[h⁻¹])0=(k[A32][h⁻¹])^Γ。h′/hの不変性から重なりの飽和性が従う。Alper刊行13.2・13.6と7.9の適用を一次確認した。新しい部分は全H2開を覆う具体的半不変式と指標の一致であり、GIT一般論自体の新規性は主張しない。

**再現手順。** `python3 computations/verify_square_h2_semiinvariants.py`。rank3の二変数多項式モデルQ=4st、随伴/Gram恒等式、五因子の指標、K自明、S2交換、共通重み関係式、相殺を許す三開被覆を厳密検算する。

**良モジュライ上のcubic開と境界。** Ordered cubic開は飽和しており、f=1の残余群とχ0次数を比較すると、既存四量子ビット商P(1,2,2,3)の開D+(p_adj)∪D+(q_adj)と同型となる。p_adj=P(Cr(adjT))、q_adj=Q(Cr(adjT))の通常次数は12・18。noncubicのA1χはMへ閉埋込みとなり、cubic/noncubicは同じgood fiberに混在しない。階数因子Dの正規化列の差はruling符号線束で、その直像が零になるため、Dのgood imageは既に正規である。一方、noncubic閉像のscheme逆像は一致点で元のNより厚い。符号慣性が法方向に−Idで作用し、good像が一定の非零横断一次変形を与える。 [cubic比較](../papers/quiver-avatar/global_h2_cubic_git_comparison.tex)・[境界像](../papers/quiver-avatar/global_good_moduli_boundary_images.tex)。

**Cubic開の不変式方程式。** e_i=e_i(JTᵗJT)、d=det T とすると、16p_adj=e3²−4d²e2+8d³、16q_adj=e3³−4d²e2e3+16d⁴e1−8d³e3。Cartan上のHadamard計算と不変式制限の単射性から全行列上で証明した。被約補集合は C0={d=e3=0} と C1={e3=de1, 4e2=e1²+8d} で、両者はP(1,2)、唯一の交点[2:1:0:0]は通常節点となる。高次イデアル自体の被約性を主張せず、この二曲線と全H2内のnoncubic A1χを区別する。 [証明](../papers/quiver-avatar/cubic_geometric_open_invariants.tex)。

**二cubic chartの貼合せと全域GIT射。** 重なりの反転は [e1:e2:d:e3]↦[e3:d²e2:d³:d⁴e1]。両積可逆なordered粗環は k[b,u,v,w]/(uw−v²)、交換はu↔wで、unordered商はA³_(b,s,v)から直線{s=2v,v=4b−8}を除いた開となる。固定schemeは二被約成分、粗二重射はz²=(s−2v)(s+2v)である。全ordered良モジュライから既存WPSへの二つの正則射ρf,ρgを構成したが、noncubic A1χはともにq0=[1:0:0:0]へ収縮される。両射と全良モジュライはnonproper。 [証明](../papers/quiver-avatar/cubic_inversion_global_morphisms.tex)。

**再現手順。** `python3 computations/verify_cubic_adjugate_invariants.py`。Cartan/Hadamard恒等式、rank4・3・2の非対角行列、radical証明の恒等式の16項目を厳密検算する。普遍式の証明は有限例からの推測でなく不変式制限の単射性を用いる。

**貼合せの再現。** `python3 computations/verify_cubic_inversion_global_maps.py`。重み付き対合、逆Gramの相似、rank-one随伴tensorの全記号式、固定scheme、二重射、除外直線、ζf指標の21項目を厳密検算する。ρf/gの降下はχ0と異なる指標の環を同一視せず、Alper Theorem6.6の普遍性を使う。

**次の課題。** 半不変環全体の生成元・関係式、中央affine補完および局所特異性は上のGram pencil節で決定した。これを入力として、最小8/10/12本矢QPのright-equivalenceの慣性と実際の相対AS群oidを比較する。

## 全H2開の四交差条件と二十式

正本は [square_explicit_h2_open.tex](../papers/quiver-avatar/square_explicit_h2_open.tex)。二積 f:C⊗A→W、g:D⊗B→W の随伴合成 Tf=adj(f)g、Tg=adj(g)f を交差縮約し、Mf,Mfᵗ,Mg,Mgᵗ の各kernelがSegre二次曲面を避けることを課す。Mfの係数は (Mf)ab,cd=(Tf)ca,db。各条件は Iker(M)=(det M,Q(adj(M)e1),…,Q(adj(M)e4)) の非零開である。四組それぞれで少なくとも一式が非零、一般基底では各idealが単位idealという条件であり、全20式の同時非消滅ではない。行列式の次数は16、随伴列の二次式は24。座標変更に対してraw idealの一致は主張せず、開部分の一致を使う。

**再現手順。** `python3 computations/verify_square_h2_open.py` はSymPyの整数・有理数・記号計算を使い、添字のKronecker恒等式、古典・三noncubic、rank低下・同一image・aligned反例、次数24の必要例、座標変換と交換を検算する。有限例と恒等式の確認であり、全相対定理の形式認証ではない。

**証明と非被約底。** 片積可逆ではVdB geometric quintupleの四隣接条件に一致する。片積rank3では随伴の交差縮約がKronecker積となって残る二条件を補う。両rank3ではkernelの非分解性・異なる支持超平面・共通平面annihilator上での二conicの非零条件を得て、全積行列をcI+offdiag、dI+offdiagへ正規化し中央二重平方環を回復する。既存相対H2開と全幾何点が一致するため同じ開部分スキームとなり、既存Ξが相対存在・全Isomを与える。fiberwise同値だけからheartを推論していない。Z33=V(det f,det g)上の相対正規形はschemeとして両detが零であることを要し、非零nilpotentの横断族とは区別する。

**有用な反例。** f=g=I4は二積可逆・joint全射を満たすが、交差縮約rank1なのでH2外である。古典squareは相対写像が二因子のflipであり交差縮約が可逆となる。従って二積のrank条件だけでは全H2開を定義できない。

**全域の境界幾何。** 明示H2開上のdet f=0とdet g=0は滑らかなCartier因子で、共通零点では二つの微分が独立である。順序付きH2上でSNC、noncubic交点は滑らかな余次元2となる。非順序和因子の正規化は一方の順序付き因子であり、noncubic上の逆像はruling二重被覆、conductorはschemeとしてnoncubic中心である。任意引戻し後のsmooth/reduced性は主張しない。 [証明](../papers/quiver-avatar/square_rank_boundary_geometry.tex)。

## 有限squareスタックと全H2の通常代数

**全H2の有限square表示とcanonicalなrank81代数。** 四つのrank2束とrank4束への二乗法をパラメータ化するA32の開から、rank16 squareとrank24 normal foundationの全相対stack同値を核・余核で構成した。頂点トーラスKとruling交換S2を含め、Q_fndは((GL2^4×GL4)/Gm³)⋊S2による商になる。H2はその不変開として表され、古典型も同じ有限表示で扱える。二積の合併全射は追加開であり、H2上では成立する。全H2上のTcan=⊕Ei⊗Hom(O,Ei)∨は頂点線束と二rulingの交換を消して降下し、通常のEnd代数はrank81。canonical完成のn次は81(2n+1)²、O角は(2n+1)²で、左右Noether性とpointed tails認識を得る。H2開は二乗法の随伴行列から作る二つの交差縮約とその転置について、kernelがSegreを避ける四条件で完全に判定した。各条件は五生成idealの非零開で、計20式以内（次数16・24）となる。両rank3壁も含み、既存相対開との一致により非被約底でも全groupoidを認識する。四交差条件をさらに同じ指標の三半不変式へまとめ、全H2の分離的・準射影的good moduliを構成した。任意AS/QP族の全比較は別課題である。[有限stack同値](../papers/quiver-avatar/relative_square_foundation_stack.tex)、[全H2のrank81代数](../papers/quiver-avatar/universal_h2_square_morita.tex)。

**明示的な互逆式。** squareの(A,B,C,D,W;f,g)からnormalへは(W1,W2,W3;P,Q)=(B,W,coker αf;D,C∨)、F=g、G=商写像。逆は(A,B,C,D,W)=(kerG,W1,Q∨,P,W2)。K上は(λ1,λ2,λ3)→(λ2,λ3,λ1)、二中間頂点の交換は既存τに一致する。二積がともに[[x0,x1],[x1,x2]]である例は両核に非零分解可能tensorを含まず、U0条件を満たすが、像の和が3次元に留まる。H2の同時全射性はAのnormal-cubic-defectと二つの支持相異系による。一般VgenはH2開より真に大きく、f=g=I4が反例である。

**降下の要点。** Eiの代表をEi⊗Liへ変えるとHom(O,Ei)もLiを得るため、Tcanの各項で相殺する。二rulingは中間二項の和として降下する。対角はOとruling二重被覆からのdegree2 Azumaya直像とdegree4 Azumayaの和で、rank25。局所増幅(1,2,2,4)の各頂点から一コピーを選ぶfull冪等元fは、Oだけのe0と異なる。前者のgraded Moritaで左右Noether性を降下し、後者はcanonical反Serrecornerとpointingを保つ。絶対大域導来圏のdescentは仮定しない。

**回転・第一mutationも同じ相対heartを持つ。** (E1,E2,E3,tE0) と (t⁻¹Z1,E0,E2,E3) の有限Endはともにrank24、完成のn次は64n²+64n+24。双対square heartによって左右Noether性を証明し、全四対象とtを保つtails同値を得た。最小矢の追加成分はcoker μG=O/(δ)であり、階数一の矢束となる条件はδ=0というscheme壁への因子化である。δ=εの一次変形では全幾何fiberがAS10でも最小矢束は平坦でない。この場合も全Hom代数・tailsは平坦に構成できる。[回転・mutationの相対比較](../papers/quiver-avatar/relative_rotated_mutated_tails.tex)。

**双対と非被約壁。** D=RHomΛ(−,Λ)はtを(t∨)⁻¹へ移す。逆順dual mutationの最後のKは、真のnormal第四項Zとのcross-Homが可逆層LになるのでL⊗K≃Z。これはproper perfectと各fiberの例外性を使う評価同型で、任意fiberwise heart条件の検出ではない。δ=εに残るεyxと一次係数nilpotentの関係を消してはいけない。実際の非最小potential解消も構成した。有限Endの7矢3関係表示ではr=δx+qのqに単元係数を残し、0→3の関係核をr⊗H01とrank2商へ分ける。短対角解消の双対からordinary Jacobianを得て、10矢potential単純複体と双対を全componentのperfect-fiber判定で検証する。δが可逆なら奇数位相の同じP_{i−2}間を消去し、δ=0なら最小AS10、δが非零nilpotentなら相対非最小の解消となる。

## 相対square完成の全次数認識

**Canonical squareの全次数代数と相対tailsを認識した。** 基底平坦compactなEに対するExt^{q}(E,K)=0（q>2）を相対Serre双対とinjective cogeneratorから証明し、二段のO軌道被覆でT=⊕EiのAZ2を得た。canonical Serre完成は左右Noetherianで、四頂点展開は全成分・全積と任意scheme基底変更を保つ。係数束を残した実際の単純AS解消と相対Gorenstein双対を構成し、qgrは同じ相対H2 heartと、全標準対象を保って完全同値となる。左右Noether性・heartの基底は本稿の局所有限型siteとし、特異基底での絶対大域次元は主張しない。全幾何fiberが分類済みsquare型である有限族へも適用でき、古典fiberを許す。頂点線束と周期線束は明示的に保持する。[相対AZとtails](../papers/quiver-avatar/relative_square_tails_recognition.tex)、[反対代数と左Noether性](../papers/quiver-avatar/relative_square_opposite.tex)、[全整数展開とAS解消](../papers/quiver-avatar/relative_square_unfolding.tex)。

**証明の依存と射程。** 任意Kに使うSerre随伴はRHom_R(RHom(E,K),I)=RHom(K,SE⊗I)であり、Eのcompactnessと基底平坦性が必要。heart全体の大域次元二とはしない。AZ2は二段のO軌道被覆とExt³消滅を用い、有限fppf被覆からHomのflat base changeで降下する。反対代数の四頂点は3−iで反転し、体上のdual avatar (P⁻¹,FP⁻¹,GP⁻¹)と分類済みfinite-square族の認識から左Noether性を得る。globalなdualcurve族の構成を入力としない。

**再開に必要な規約。** B=C(Λ)、A_{4q+j,4p+i}=e_jB_{q−p}e_i、Pack(M)_ne_i=M_{i−4n}。Λの二段階積の核Rはrank4で、最長道長二の短対角解消から通常のJacobian表示を直接得る。Keller Theorem6.10のordinary relation ideal生成に関する訂正も満たす。全整数の頂点線束変更ではA′_{ba}=L_b A_{ba} L_a⁻¹、単純解消の最左係数はL_i L_{i−4}⁻¹である。canonical族と任意の別AS族を線束無視で同一視しない。

**次の課題。** rank16↔rank24の相対stack同値、全H2開の20式判定、determinant境界の横断性と非順序商の正規化は確立した。半不変式によるaffine開被覆と大域good moduliを構成したので、既存GITの具体的不変式と境界像を比較する。

## 相対行列式開と同じheartの全標準頂点

正本は [行列式開](../papers/quiver-avatar/relative_vertex_determinants.tex) と [相対normal窓](../papers/quiver-avatar/relative_avatar_pointed_recognition.tex)。proper flat fp曲線と実際の線束から二つのrank四乗法を作り、全幾何fiberのH2適合開を $U_0=U_3=T$、$U_1=D(\det\mu_F)$、$U_2=D(\det\mu_G)$ と同定した。Perfect pushforwardのfiber次数集中を使うため非被約・非平坦底変更も含む。局所形は $\operatorname{diag}(I_3,\delta)$、悪い閉部分はFitting理想 $(\delta)$。普遍楕円Picardの二壁 $\eta=P,\eta=P^{-1}$ はCartierかつ横断、交点は非零二捩れ有限étale三次。任意の引戻しではCartierとは限らず、$\delta=\epsilon$ over dual numbersが必要な反例である。全幾何fiberが壁にあるだけではschemeとして壁を経由しない。

局所有限型基底のflat曲線avatarについて、rank16のsquare代数から実際のcone $Z_1=\operatorname{Cone}(E_1\to(p_*G)^\vee\otimes E_3)$ を作ると $(E_0,E_2,E_3,Z_1)$ はrank24のfoundationになる。部分束包含はpencilの大域生成性から直接証明した。全幾何fiberのgenuine normal認識と既存のH2開埋込から、実際の相対H2 heartを構成する。E0を保つcompact Morita同値があり、E3は同じheartの $s\mathcal O$ としてH2構造対象になる。全非負Serre tensor次数と任意基底変更も比較する。

さらに [相対heart比較](../papers/quiver-avatar/relative_avatar_heart_comparison.tex) は、Ui上のnormal窓 $(E_2,E_3,Z_1,tE_0)$ と交換版から実際のH2族Ciを作り、C0と同じheartであることを証明する。鍵は両側の構造対象が相手heartへ実際に入ることである。互いの反Serre AZ生成族もheartに入るため、有限和によるbounded-above解消とbrutal truncationの順方向hocolimで両方向right t-exactを得る。非被約底のfiberwise t-exactnessを仮定していない。この証明は局所canonical compact chartで行い、Abel descentで貼り合わせる。

同節ではUi上の三次関係核Rから四重tensorを構成し、実際のgeometric cubic Z族を復元する。Linear cubicのinverse mutationはclassical squareなので、曲線型sourceからは生じない。全次数平坦・Noether性とcanonical tailsはBの既存相対結果を適用し、C0とのpointed exact同値を得る。

**保持すべき因子と範囲。** 曲線上のZ1は $FG^2\otimes\det(p_*G)^\vee$。Cubicの四次overlap・添字線束を消したstrict周期同一視は主張せず、canonical Serre tensor比較と区別する。全標準頂点のH2条件は同じ相対heart上で完成した。T=⊕EiのAZ2とcanonical square AS qgrの比較は上節で証明した。有限square表示の全stack比較は上節で完成し、全AS/QP群oid同値は別課題である。

## 全標準構造頂点の判定と頂点ideal

正本は [general_vertex_az.tex](../papers/quiver-avatar/general_vertex_az.tex)。$I_i=\sum_q Ae_{i+4q}A$ とすると $(E_i,S^{-1}[2])$ がAZ ampleであることと、全 $e_j(A/I_i)$ が有限次元であることは同値である。有限生成加群の有限標準射影解消と前向きExt消滅から、十分負のjで $M_j=\operatorname{Hom}(E_j,\pi M)$ を証明する。Noether性と左右単純解消を使い、一般のχや個別頂点の豊富性を追加仮定していない。

最小AS10で全偶数頂点を消すと、potential $yq+px+H$ の全関係が消え、奇数頂点を結ぶx,yの無限道だけが残る。従って偶数pointingはH2外。奇数位相を一つ消すと道の長さが有界となりAZ ample。強いH2の肯定方向は別にcubic/noncubic認識で証明する。

| 型 | 位相0 | 位相1 | 位相2 | 位相3 |
| --- | --- | --- | --- | --- |
| square曲線型 | H2 | GP≄F のときH2 | G≄FP のときH2 | H2 |
| rotated曲線型、C=HF⁻² | C≄O のときH2 | C≄P² のときH2 | H2 | H2 |
| 最小AS10 | H2外 | H2 | H2外 | H2 |
| 古典square/rotated | H2 | H2 | H2 | H2 |

非被約曲線を含む体上の全分類AS型に適用する。二つの壁の外では実際のexact mutationが保持する頂点をcubic AS3へ移し、A `thm:all-admissible-inverse` と添字shiftを使う。二重壁は既存のsmooth/nodal/I2 noncubic認識で処理する。一般の反Serre ample対象がH2に属すると主張するものではない。相対行列式開と全標準頂点の同じheartでの認識は上節で構成した。全square AS heartの比較を続ける。

## 全point schemeと表示商上の孤立二点

[spinor_pointing_obstruction.tex](../papers/quiver-avatar/spinor_pointing_obstruction.tex) で $\mathcal P(B_f)=E_f\amalg\{p_c,p_d\}$ をschemeとして証明した。二点座標のmultilinear schemeが曲線上の対角と二点の交換graphであるため、次数0,1,2から全truncationが安定する。M0=Oを固定した族と普遍加群を構成し、任意底変更と比較した。このpoint functorの式だけは任意二形式へ拡張でき、AS/Serreの仮定とは区別する。

表示商上の孤立成分は [P/Gord]→[P/G] という根対の順序付け有限étale二重被覆で、shiftはdeck変換。共通次数スカラーはparameterには自明だが普遍加群の次数nには重みnで作用するので、graded普遍族の通常の降下を主張しない。元のE_fを使ったpencil/finiteEnd比較は曲線成分への制限であり、修正不要である。

## Noncubic avatarの全位相と見えないpoint module

証明正本は [spinor_pointing_obstruction.tex](../papers/quiver-avatar/spinor_pointing_obstruction.tex)。$h=cd+dc$ を中心の次数2元とし、$Q_c$ は $u=v=0$、$e_{2j}c=e_{2j+1}$、$e_{2j+1}d=e_{2j+2}$、残りの作用零で定める。$e_jh=e_{j+2}$ なのでh-torsionfreeな非零point module。$X_c$の表示行列はここでdiag(c,−c)となり、h局所化後の偶数次数でcが単射であることから、全nについてHom(πXc(−2n),πQc)=0。tails Homから局所化Homへの単射も証明した。c,d交換でXdも同様。

反Serreは $t=(-)_\iota(2)$、$\iota(c,d)=(-c,-d)$。$\iota(M_c)=-J M_cJ$ によりspinorはこのtwistで不変となり、上のHom消滅が全反Serre軌道の生成失敗を与える。強いH2でeven軌道の生成が必要なのは、AS4二次切断の軌道環が次数1で生成され、偶数Veroneseが同じqgrを回復するためである。一般のAZ ample pairの二乗に無条件でample性を課してはいない。

| 型 | 0 | 1 | 2 | 3 | H2位相 |
| --- | --- | --- | --- | --- | --- |
| square | B | Xd | Xc | B(1) | 0,3 |
| rotated | Xd | Xc | B(1) | B(2) | 2,3 |
| 最小AS10 | Xd(−1) | B | Xc | B(1) | 1,3 |

各項はπを施したqgr対象。finite Endの頂点対応、Serre完成、実際のMF余評価列により同定し、曲線上の共通tensorだけから推論しない。四周期で全整数に適用する。Q_c,Q_dはcd−dcが±hとして作用するので可換化の曲線E_fには現れない。反Serre角のHilbert数値が同じでも、同じunderlying Abel圏の構造対象としてのH2適合性は異なる。

### 再利用できる二つの補助計算

滑らかな楕円曲線で次数二pencil Fと非自明Pに対し、H⁰(FP)⊗H⁰(FP⁻¹)→H⁰(F²)/Sym²H⁰(F) は非退化な2×2 pairingである。左kernelに非零aがあれば、aH⁰(FP⁻¹)の固定因子はdiv(a)（次数二）となる。一方この二次元部分系はFの二重射によるO(2)の引戻しなので、その次数二固定因子は一つのfiberであり、FP≃Fを強制して矛盾する。右も同様。P²=Oも許すが、非被約曲線へ無条件に外挿しない。主たる頂点判定はこの補題を必要としない。

中央二重平方のspinorでは、既存forward Ext消滅とEuler列からn≥0について dim Hom(Xi,Xi(n))=(n+1)²−(1−(−1)ⁿ)/2、i≠jでは dim Hom(Xi,Xj(n))=(n+1)²−(1+(−1)ⁿ)/2 を得る。初期値はδij、n≥1の漸化式はh(n)+h(n−1)=2n(n+1)。特に通常shiftの次数一はsame型3、cross型4である。もし二型を交換するσがσ²=ιを満たし適合根s=σ(1)を与えるなら、spinor軌道のHilbert数値は全nで(n+1)²となるが、上の生成障害により豊富ではない。ここではそのσの存在・全分類をこの数値式だけから主張しない。

## 順序付きFricke射の良モジュライ性

[大域降下節](../papers/quiver-avatar/fricke_boundary_descent.tex) に実際のalgebraic target atlasを追加した。判別式極化D≠0の開で第二形式をuv、第一をAu²+uv+Bv²へ正規化し、AB=(1−4q)/4が単元であることと全O(uv)同型からtargetをétale局所でBΓ×Tへ同定する。sourceのatlas basechangeは[Spec R[a,b]/(ab−q)/Gm]、weights±2。環のR基底1,a^n,b^nと次数零不変部分により、flat fp surj、O直像O、QCoh直像完全を任意底変更込みで証明する。Alper刊行版Remark4.4のArtin targetへのgood moduli space morphismである。非smooth locusは一致点のみ、Gm慣性があるので非分離・非proper。

一致点を除いたDM開では、D(a),D(b)の二開によるČechでH¹(O)=R[1/q]/R≠0となり、cohomological affinenessを失う。中央μ₂をrigidifyした局所模型は二つのq直線をq≠0で貼った二重原点直線。元のμ₂-gerbeが全域で自明とは主張しない。順序忘却後はgenericで構造層直像がrank2となるので、同じgood-moduli条件は成立しない。

## 全Fricke境界射・pencil・半周期の現在の結論

正本は [全表示groupoid上の降下](../papers/quiver-avatar/fricke_boundary_descent.tex) と [共通模型・pencil・半周期](../papers/quiver-avatar/spectral_boundary_models.tex)。自然な順序付き射は全 $\mathfrak N^{\rm pres}$ から $\mathfrak U=\{\Delta(g_2)\operatorname{Res}(g_1,g_2)\ne0\}\subset\mathfrak T_{\rm bal}^{\rm ord}$ へ延長する。形式表示だけに依存せず、$\chi\ne0$ 上の全fppf Isomと平方根選択を比較し、残るsmooth開と貼り合わせた。

再開用の式は $q=(\chi-1)/(4\chi)=ab$、入力 $(uv,au^2+uv+bv^2)$、出力 $(U^2-4qV^2,V(U+V))$。$\rho^2=1-4q,\ \ell^2=(1+\rho)/2$ の可逆平方根をétale局所で選ぶ。入力交換は $L=\left(\begin{smallmatrix}\ell&b/\ell\\a/\ell&\ell\end{smallmatrix}\right)$、$c_0'=d_0,d_0'=\rho c_0$、$(a,b)'=(-a,-b)$。出力交換は $(U,V,C,D)\mapsto(-U-4qV,U+V,-\rho C,\rho D)$。$\ell$の符号差は入力の同時符号で出力では消え、$\rho$の符号差は $m=\ell\ell',m^2=ab$ によるordered行列 $\left(\begin{smallmatrix}0&b/m\\a/m&0\end{smallmatrix}\right)e_d$ で、出力では同時符号 $\delta'$ に一致する。この等式が三重overlapを含む降下を与える。形式近傍の $\Gamma=\mu_2^3$ を全域の定数bandとは扱わない。

線束境界点とそのframeを固定した2-fiberは $[\operatorname{Spec}k[a,b]/(ab)/\mathbb G_m]$、重み $(-2,2)$。二つの非零軸は各々 $B\mu_2$、原点は $B\mathbb G_m$。慣性写像は一致で $H_{\rm eq}\twoheadrightarrow\mu_2^3$・核 $\mathbb G_m$、一根共有で $D_8\to\mu_2^3$・核 $\mu_2$・像4。smoothの一般核2・非順序付き標的への像8を保つ。これは粗式だけ同じで核8・像2となる弱い共変射とは異なる。

共通I4模型を $(D_+,L_0,D_-,L_\infty)$ の順に並べる。線束がa側へ降下する条件は $\deg L_0=\deg L_\infty=0$、b側へ降下する条件は $\deg D_+=\deg D_-=0$。$a^*F$ のmultidegreeは $(1,0,1,0)$、$b^*H$ は $(0,2,0,2)$ なのでPerfの像は互いに包含しない。$b^*N_0=a^*F(-L_0)$、$b^*N_\infty=a^*F(-L_\infty)$、$N_0N_\infty=N_2^2=H$。第一pencilの線束延長は存在するが、その平方をHにすることはできない。

任意有限分岐 $t=s^e$ 後の最小正則模型は $I_N,N=2re$。入力二捩れの標準延長 $\mathcal O(S_0-S_\infty)$ は $\sum j\deg_{\Gamma_j}\equiv N/2\pmod N$ であり、整数vertical twistはこれを変えない。従って入力二捩れは線束としては延長するが、二乗自明な線束には延長しない。出力商曲線上の二次線束は別のデータで、全族上に存在する。

全halving schemeは $[2]^{-1}(P)=\operatorname{Spec}K[X,Z]/(X^2-t^r,Z^2-1-2X)$、$Y=XZ$。一根共有では二つの $\operatorname{Spec}K(\sqrt t)$、一致では四つの $\operatorname{Spec}K$。一根共有のKummer classは指定基底で $(t,1)$。全交換はこの四点torsorと $\{\pm1\}$ の積。一致では全四translation補正が元模型の同型に延長し、共有根では未修正模型の成分数が異なる。最小正則模型では定義体上の全補正が延長し、成分cycleに四分の一回転で作用する。

今回の範囲では直接証明と相互読取りを完了したが、包括的新規性・形式証明・外部査読を完了したとはしない。noncubic由来の全四位相は上節で判定した。全標準頂点の体上判定は上節で閉じた。次は全square AS heartと既知文献に対する貢献範囲の絞り込みを扱う。

## Fricke境界の共通正則模型と二次線束

正本は [spectral_boundary_models.tex](../papers/quiver-avatar/spectral_boundary_models.tex)。二trait $C_r:y^2=uv(p_ru^2+uv+b_rv^2)$、$(p_1,b_1)=(1,t),(p_2,b_2)=(t,t)$ と出力 $E'_r:c^2=U^2-4t^rV^2,d^2=V(U+V)$ の指定generic同型のgraphは、base ideal $(p_ru^2,b_rv^2,uv,y)$ のblowup。共有根では唯一のA1解消で $X_1=E'_1$、特殊fiber I2。一致型ではI4であり、元の二成分と二例外成分が交互に並び、二つの射は異なる二成分を収縮する。graph閉包自体が正則なので追加正規化・分岐は不要。

$r=2$の主要chartは $t=xs,y=xz,z^2=1+s(1+x^2)$、出力 $[A:B:V:d]=[sx^2:s:1:z]$。これは $AB=t^2$ の標準解消である。両収縮の構造層は $Rf_*\OO=\OO$ であり、Perfの引戻しは全忠実・構造層保存。これを特異AS heartのH2認識に読み替えない。

自然な順序付きFricke像は $(g_1,g_2)=(U^2-4t^rV^2,V(U+V))$ でbalanced標的へtrait延長する。同時符号の共役は $[u:v:y]\mapsto[b_rv:p_ru:-p_rb_ry]$。出力の二形式は互いに共通根を持たないので反不変 $M'_r$ は全族上line、二次積は同型、被覆は有限étale。特殊 $C'_0$ は既約nodalで $M'_0$ はgluing $-1$ の二捩れ線束、固定被覆fiberの追加の被約成分に属する。元Nの非自由成分とは異なり、H2外である。正則化上の符号はI2/I4の半回転、商はI1/I2で、二次線束は商の解消への引戻し。

一致型には $a^2=1+2t,a\equiv1\bmod t$ を使う全R同型
$\Psi=[a^2(u+v)^2-(v-u)^2:(v-u)^2:4ay:a(u+v)(v-u)]$
がある。指定同型との差は $F=\Psi^{-1}\Phi_2=T_Q$、$Q=[1:1:a]$、$2Q=(0,0)$ という四捩れtranslation。$F^2=[v:u:-y]$。$\Phi_2\iota=e_d\Phi_2$ に対し $\Psi\iota=e_c\Psi$ なので、補正は二conicの順序を交換する。共有根の未修正模型は特殊成分数が違い、有限DVR拡大後にも抽象同型にならない。

有限étale二次代数・trace分解・線束の構成は任意非平坦基底変更と可換。graph形成はflat base changeに限定し、$t=s^e$後の節点 $xy=s^e$ を解消するとI$_{2re}$、商I$_{re}$。全G同変な境界射への降下、全境界fiber、半周期の分裂、line bundle/Perf像は上節の結論により決定した。graph形成と解消の任意非平坦基底変更は未主張である。

## 二次積付きTF標的の有限型性と相対認識

正本は [torsion_free_spectral_recognition.tex](../papers/quiver-avatar/torsion_free_spectral_recognition.tex)。幾何fiberがsmooth/nodal/I2となる有限二重被覆 $p:C\to B$ と、各成分rank one・次数零・相対flatな二次自己双対TF層 $(M,\mu)$ の標的 $\mathfrak T_{\rm nod}$ は、有限型Artin、affine有限表示対角を持つ。非被約な**基底**を含むが、非被約spectral**曲線**全体には拡張していない。単純性・安定性は要求しない。

再開に必要な入力は $A=p_*\OO_C=\OO_B\oplus N$、$V=p_*M$、$b=\operatorname{pr}_N\mu$。$V$はrank2ベクトル束で、Frobenius pairingから $p_*\mathcal Hom_C(M,\OO_C)=V^\vee\otimes N$ が任意底変更と可換。自己双対性は $b$ の非退化性と同値である。分岐外の実際のétale rank-one moduleと、branch quarticが普遍非零因子であることから、$N$作用のtraceは非被約底でも零となる。

被約連結fiber上で非零大域切断 $s$ があれば $\mu(s,s)$ は非零定数となり $M\simeq\OO_C$。従って $h^0(M)\le1$、$V$ は $\OO(-1)^2$ または $\OO\oplus\OO(-2)$ の二型だけである。$V(2)$ は一様に大域生成、$H^1=0$、$h^0=4$。固定 $\operatorname{Quot}^{2n+4}(\OO^4)$ に作用と二次積の有限式を加えることで有限型性を証明する。固定Hilbert多項式だけでは有界性は従わず、自己双対性が本質的である。

**Balanced開の正確な表示。**
\[
\mathfrak T_{\rm bal}
=\{h^0(M)=0\}
\simeq[\overline P_{\rm nod}/G],
\quad
\overline P_{\rm nod}
=\{(f_1,f_2): f_1f_2\text{の根重複度が高々2}\}.
\]
この開はsmooth既約・有限型・純次元1。$b$の等方線を順序付ける被覆は底上の有限étale二重被覆であり、二次積から $f_1,f_2$ と全同型を回復できる。局所式 $\mu(c,d)=a+y$ は $Y=\left(\begin{smallmatrix}a&f_2\\f_1&a\end{smallmatrix}\right)$ のtrace零により $a=0$ となる。similitude行列の冪等元分解により、非被約底にも対角・反対角以外の混合はない。$\OO_C\oplus M$ の結合律は明示二形式代数との同型から従う。

元の $\mathfrak N$ は両等方平方の判別式非零の開 $\mathfrak T_{\rm adm}$ に一致し、TF標的への射は全忠実な開埋込みである。二形式間の共有根や一致を含む。実際の $(M,\mu)$ を保持するので同時符号 $\delta$ は消えない。さらに層を忘れて $(C,p)$ のみとすると、nodalでは核 $\langle\delta\rangle=\mu_2$・像 $C_2^2$、I2では核 $\langle\delta,\tau\rangle=\mu_2^2$・像 $(\Gm\rtimes C_2)\times C_2$。この核を、TFへの全忠実な表示射自身の核と混同しない。

**固定した被覆上のscheme-theoretic fiber。** 曲線と二重射を固定し、分岐外に無限遠点を選んで $y^2=h(x)$ をmonicにする。$Z_h$ をmonic二次因子分解 $q_1q_2=h$ の長さ6のschemeとすると、balanced忘却fiberは $[Z_h/S_2]\times B\mu_2$ である。Smoothでは $3B\mu_2$。$Z_2=\Spec k[\epsilon]/\epsilon^2$、$Z_{2,2}=\Spec k[\epsilon,\eta]/(\epsilon^2,\eta^2)$ とすると、nodalでは $(\Spec k\amalg Z_2)\times B\mu_2$、I2では $(\Spec k\amalg[Z_{2,2}/C_2])\times B\mu_2$。$C_2$ は両変数を同時反転する。元Nの境界fiberは各々後者の非自由成分だけである。I2の不変式環にも $k[\epsilon\eta]\simeq k[z]/z^2$ の厚みが残る。幾何点の個数や閉点慣性だけでは、このfiberを記述できない。

**Pencilの役割。** 曲線と $(M,\mu)$ を残してpencilを忘れると、nodalの全慣性は $\Gm\rtimes C_2$、入力D8は $\mu_4\rtimes C_2$。I2の全群は $\Gm^2\rtimes(C_2\times C_2)$、pencil保存群は $t_+^2=t_-^2$ の部分群である。従ってpencilを忘れた標的への写像は慣性単射であっても全射でなく、先の開埋込みの主張には二重射を保持することが必要である。

**Fricke境界の指定同型と曲線修正。** 元の点曲線と同時符号は $\operatorname{Spec}_C(\OO_C\oplus M)$ から全境界で回復する。一方、平坦Fricke出力の点曲線との指定generic同型は
\[
[u:v:y]\dashrightarrow
[p_ru^2+b_rv^2:uv:p_ru^2-b_rv^2:y],
\quad(p_1,b_1)=(1,t),\ (p_2,b_2)=(t,t).
\]
$r=1$では入力特殊曲線はnodal、出力はI2であり族同型に延長しない。$r=2$では双方I2だが、この式が各成分の稠密開を一点へ収縮する。有限trait基底変更でもこの指定式の障害は残る。$r=2$の別のgeneric同型すべてを否定したものではない。このgraph閉包は上記の正則I2/I4模型であり、慣性・pencil・底変更の比較も現行境界節に統合した。

Frobenius/trace・inverse matrix・similitude・node積の厳密恒等式は `verify_spectral_atkin_lehner.py` の15項目へ統合した。Artin性・全忠実性・全基底への降下の証明は原稿で分担・相互点検し、有限計算からは結論しない。

## Cの相対pointed模型と同変Serre

**Cの現行到達点（相対pointed認識）。** 点曲線側のnormal四項を対称な `(B,X_c,X_d,B(1))` へ相対mutationし、全三型で基本Endの階数16、Brauer増幅後の階数30を得た。共通座標表現による最後の頂点の増幅を加えると、二形式交換と共通次数スカラーを含む全商 `[P/G]` 上へ階数45の通常代数が降下する。中二頂点は交換され、構造対象の零頂点は固定される。実際の相対spinor generatorを構成し、任意の局所有限型・非被約基底変更と可換なcompact Morita同値、全次数Serre完成、零頂点の反Serre角による元のpointed heartの回収を証明した。正本は [対称Morita降下](../papers/quiver-avatar/symmetric_morita_descent.tex) と [相対Serre完成](../papers/quiver-avatar/relative_serre_completion.tex)。これは **E_f側の全noncubic相対族** の結果であり、任意のavatar/AS/QP表示stackの同値ではない。

**同変Serreの訂正。** 二形式交換の符号指標を ε とすると canonical反Serre環は `R_n^can=B_{2n}⊗(det W)^(-n)⊗ε^n`。Frobenius traceの交換反不変性からこの符号を証明した。Bの符号を含まない表示は次数線束による正規化として保持し、canonical環との違いを明記した。pointed qgr、射影関係式表示、境界の同値・慣性の結論は変わらない。通常Endの右Yoneda規約と旧上三角双加群表示の反対環も明示して区別した。

再現：`python3 computations/verify_symmetric_morita.py`。三つの有理モデルで中二spinor間のHom消滅、8→4の積と四関係、全次数Euler/Serre恒等式、交換traceの符号を厳密演算で確認した。代数降下とheart同値の証明は原稿による。

## Spectral avatarのpointed像と境界の障害

正本は [spectral対合と延長不能](../papers/quiver-avatar/spectral_atkin_lehner.tex)。標数零代数閉体上、smooth根対のspectral avatar $(C_f,F,FP,P)$ を指定AS10 mutation・一番頂点の構造対象で実現すると、元の $\mathcal H(f)$ ではなく $\mathcal H(f^\vee)$ を得る。これは幾何同型類上の二同種双対化であり、$\chi^\vee=\chi/(\chi-1)$。元とpointed exact同値なのは $\chi=0,2$ に限られる。このsmooth対応の相対groupoidは下のgerbe分解で決定する。noncubic由来のrotated零頂点は上節で強いH2外と判定した。一般Pの標準構造頂点は上節で判定し、全相対avatar/QP表示groupoidは別に残す。

再開に必要な最小式は、$f_1=uv$、$f_2=u^2+a uv+bv^2$、$b(a^2-4b)\ne0$ に対する
\[
(a,b)\longmapsto(-2a,a^2-4b),\qquad
j(C_f)=\frac{64(\chi+3)^3}{(\chi-1)^2},\quad
j(E_f)=\frac{64(4\chi-3)^3}{\chi-1}.
\]
自己双対点の $j$ は1728と8000。$\chi_\pm=(81\pm45\sqrt{-7})/128$ では両曲線の $j=-3375$ が等しいが、二捩れ標識は交換されpointed対象は異なる。このため $j$ 一致だけによる認識は不十分である。逆構成は二pencilのdeck involutionが作る四元群商から二つの分岐二点集合を回収する。

| 退化型 | 二形式族 $f_1=uv$ の第二形式 | 元の $\chi$ | spectral-pointed像の $\chi^\vee$ |
| --- | --- | --- | --- |
| 一根共有 | $u^2+uv+t v^2$ | $1/(1-4t)$ | $1/(4t)$ |
| 根対一致 | $t u^2+uv+t v^2$ | $1/(1-4t^2)$ | $1/(4t^2)$ |

この二族は実際のnoncubic族である。像にH2族としてのtrait延長があれば、論文Bのnoncubic境界の閉性からその全体が $\mathfrak N$ を経由する。しかし正則な $\chi:\mathfrak N\to\mathbb A^1$ に極が生じるため矛盾する。任意の有限分岐trait基底変更でも極は消えない。これは固定spectral曲線上のPicard線束の非延長より強い内在的障害であり、全noncubic境界からH2へのspectral延長を今後の存在目標にしない。

Smooth対応の相対射と同型層・慣性は次節で決定した。節点TF標的のArtin性・有限型性・balanced商・元Nの開埋込みは証明済み。Fricke境界の曲線修正と全groupoid上の射は上記の境界節で構成した。既存の積欠損・節点奇偶障害も入力にする。古典的二同種公式はSilverman第2版III Example 4.5に帰属し、今回のpointed適用の包括的新規性は未確認。

再現：`python3 computations/verify_spectral_atkin_lehner.py` は二同種・対合・二つの $j$ 公式・固定点・等 $j$ 反例・境界極に加え、相対商座標、慣性生成行列と中心の平方類、nonsplit pencilのcocycleをSymPy厳密演算で確認する。閉stack入力・gerbe同値・無限Ext・圏の認識は原稿の証明であり、この計算の認証範囲ではない。

## Smooth spectralの相対gerbeと中心band

証明正本は [相対spectral対応](../papers/quiver-avatar/spectral_relative_correspondence.tex)。入力の非順序二conic被覆 $Q_1,Q_2\to Z$ から、$E=Q_1\times_ZQ_2$、同時符号の商 $C=E/\delta$、反不変二次線束 $(M,\mu)$ を得る。$C\to Z$ のdeck involutionを $\iota$ とすると、$\iota'=t_{[M]}\iota$ との四元群商が順序付き出力を与える。$M$ は実際の線束だが、spectral pencilのPicard類の障害は $\alpha_Z$ であり、線束とは限らない。

射の正確な形は
\[
\mathfrak N^{\rm sm}
\xrightarrow[\text{banded }\mu_2\text{-gerbe}]{\mathscr D^{\rm ord}}
\mathfrak N^{\rm sm,ord}
\xrightarrow[\deg 2]{\mathrm{forget}}
\mathfrak N^{\rm sm}.
\]
第二射は表現可能な有限étale射。幾何fiberは $B\mu_2\amalg B\mu_2$ で、任意の体上で二つのneutral gerbeへ分裂すると主張しない。自然な相対慣性核は同時符号 $\delta$、一般点の像は位数8、全慣性は位数16。出力二形式からrank45の相対pointed認識を適用できる。

逆gerbeは、標的点曲線の二pencil差 $P=F_2F_1^{-1}$ を実際の線束で代表し、その二乗自明化を選ぶgroupoidである。Brauer像は $\beta=\alpha(Q'_2)-\alpha(Q'_1)$。一般基底では $\operatorname{Pic}(S)/2$ の寄与を捨てない。普遍係数体ではindex 4なので、逆構成に必要な有限分裂拡大の最小次数は4。相対Picardの一般gerbe論とKummer対応はStacksの既知入力であり、ここでは被覆groupoidとの逆構成を証明した。

**粗対合を覆う全stack自己同値は存在しない。** $K=k(\chi)$、$b=(\chi-1)/(4\chi)$、$f=(uv,u^2+uv+bv^2)$ とすると、一般慣性 $H_f$ の中心の基礎有限étaleスキームは
\[
\operatorname{Spec}K\amalg\operatorname{Spec}K
\amalg\operatorname{Spec}K(\sqrt b).
\]
対合で引き戻した標的では $b'=1/(4\chi)$。比 $b/b'=\chi-1$ は非平方で、中心は同型でない。gerbe同値がneutral objectをtorsorへ移してもinner twistは中心を変えないため矛盾する。一般点でrepresentableな射も慣性16→16の単射を強いるので存在しない。これは追加慣性のある $\chi=0$ や境界極とは独立の障害である。

**Brauer障害を保つ試験入力。** $K=k(s,t)$ 上の $f_1=u^2+v^2,\ f_2=u^2+t^2v^2$ を、$K(\sqrt s)/K$ と $h(u,v,c,d)=(-tv,u,d,-tc)$ でtwistする。$h^2$ は共通次数スカラー $-t$ であり、基底conicは非零Brauer類 $(s,t)$ を持つ。この入力でも $(M,\mu)$ は実在する。pencilを勝手に線束化した構成を排除する具体例となる。

## 特異境界の平坦模型・無限Ext・弱い共変射

二traitのgeneric像には
\[
B^{(r)}=k[t,(1-4t^r)^{-1}][U,V]\langle c,d\rangle/
(c^2-U^2+4t^rV^2,\ d^2-UV-V^2),\qquad r=1,2,
\]
がある。中央Clifford基底により各次数階数は $(n+1)^2$ で平坦。特殊fiber $B_0$ では、$X=B_0/(c-U)B_0$ と $S=k[V]$（$U=c=0,\ d=V$）に対して
\[
\operatorname{Ext}^n_{\qgr B_0}(\pi X,\pi S)=k
\quad(n\ge0).
\]
証明は左 $R_c=k[U,V,c]/(c^2-U^2)$ 自由性からの交互 $c-U,c+U$ 解消と、重み付き射影**スタック**上の通常点 $[0:1:0]$ への高次cohomology消滅による。$D^b(\qgr B_0)$ の右Serre像は有界でなければならず、この無限非消滅と矛盾する。Perf上のSerre公式は否定しない。

任意の非squarefree第一形式は非零なら $U^2$、零なら0へ帰着し、第二形式の $f_2(0,1)$ の平方根 $\delta$ を選んで $d=\delta V$ とする。同じ二周期、または $c^2=0$ の一周期解消が使える。このため、標数零代数閉体上の**中央二重平方表示族内**では
\[
(\qgr B_f,\pi B_f)\in H2
\iff \Delta(f_1)\Delta(f_2)\ne0.
\]
十分性はBの `thm:noncubic-relative-effectivity`、必要性はCの `cor:qa-double-square-degenerate-not-h2`。共有根・一致根対は引き続き含む。

### 不変式からの別の相対射は自然なspectral延長ではない

$D$ を混合判別式、$J=\Delta_1\Delta_2$、$\ell=\det A/(a_ca_d)$ とする。全表示群 $G$ 上で $\ell$ は共通次数スカラーに自明で、入力二形式の交換にも不変。$D\mapsto\ell^2D,\ J\mapsto\ell^4J$ に対し
\[
g_1=U^2-(D^2-J)V^2,\qquad g_2=UV+DV^2,\qquad
\rho(g)=[\operatorname{diag}(1,\ell^2),1,\ell]
\]
は厳密に同変である。従って全 $\mathfrak N$ から、重根を許す順序付き二形式表示stackへの弱い相対射がある。表示ベクトル束の重みは $W'=\mathcal O U\oplus L^2V,\ c'\in\mathcal O,\ d'\in L$、または共通次数スカラーで同値な $W'=L^{-2}U\oplus\mathcal O V,\ c'\in L^{-2},d'\in L^{-1}$。逆向きの重みを採らない。

直接計算で
\[
\Delta(g_1)=4(D^2-J),\quad \Delta(g_2)=1,\quad
D(g_1,g_2)=-2D,\quad \operatorname{Res}(g_1,g_2)=J.
\]
従って $J$ 可逆の入力では出力は零形式を持たず共通根もなく、smooth域の粗座標は $\chi/(\chi-1)$。$\chi=1$ では第一形式だけが重根を持つ。各次数はClifford基底により平坦で、上の無限Ext障害へ入る。

ただし両出力conicは $V=0,c'=\pm U$ および $V=d'=0$ のsectionを持ち、Brauer類が零になる。自然な $\mathscr D^{\rm ord}$ の第一conicは元の基底 $Z$、第二conicも同じBrauer類であり、上の $(s,t)$ の入力では一致しない。一般安定化群上では $\ell^2=1$、個別符号が $\ell=-1$ を実現するため、この弱い射の慣性像は2・核8。自然な射の像8・核2とも異なる。粗座標の一致から相対射の同一性や自然な境界延長を結論してはならない。この障害を、次のtorsion-free標的の認識で使う。

## 論文C：最小AS分解型とavatarの分類・相対境界

**中心定理（原PDFからCへ証明移管）。**
原資料『非可換二次曲面の二つの反標準avatar』v7の
定理1.3・命題2.4/6.5/7.1/12.1をもとに、
`papers/quiver-avatar/as_helix_classification.tex` の
`thm:qa-as-avatar-bijection` を主定理とする。
指定された四周期最小分解とAS–Gorenstein条件を持つ
square/rotated square型のAS正則Z代数の頂点保存同型類と、
曲線型（非被約Dも許す）・古典型avatarの同型類がそれぞれ一対一対応する。
逆向きは有限directed Endとacyclic spherical helix、
Serre完成による全Z代数復元。
必要方向は単純分解とHilbert増大からのrank forcing、
点表現上のΣ0/Σ2・反標準D・Pic0の抽出。
左右Noether性は正則normal四次元族とtwisted section algebraに帰着。
curve上のcanonical完全列は
`square_rotated_foundations.tex` と
`canonical_helix_complexes.tex` に証明を保持。

**内在的noncubic heartの直接認識に必要な2-isogenyの区別（Cで新証明）。**
中央二重平方環 $B_f$ の可換点曲線を
$E_f=\{c^2=f_1(u,v),d^2=f_2(u,v)\}\subset\PP^3$、
二根対のspectral曲線を
$C_q=\{y^2=f_1f_2\}$とする。
根対が非交差ならともにsmooth genus1だが
$E_f\to C_q,\ y=cd$は同時符号$\mu_2$の
**自由商による2-isogeny**であり、一般に同型ではない。
$E_f$上の二つの個別符号商はsmooth conic
$Q_d=\{d^2=f_2\}$、$Q_c=\{c^2=f_1\}$。
それぞれの次数一線束のpullbackを$F_d,F_c$とすると
$F_d^2=F_c^2=\OO_{E_f}(1)$、
$P_E=F_cF_d^{-1}\in\Pic^0(E_f)[2]\setminus\{0\}$。
$\tau(c,d)=(-c,-d)$は$P_E$によるtranslationなので
$(E_f,F_d,F_c,P_E)$は二重壁のsquare avatar。
一方、$M_C=(r_*\OO_{E_f})^-$は
$C_q$上の非零2torsionで、
$\ker(r^*:\Pic^0(C_q)\to\Pic^0(E_f))
=\{0,M_C\}$。
よって$(C_q,M_C)\mapsto(E_f,P_E)$は
非零2torsion付き楕円曲線の**双対2-isogeny involution**。
（C thm:qa-point-spectral-dual-two-isogeny,
cor:qa-point-spectral-atkin-lehner。）
以前のspectral構成のavatarは$C_q$上であり、
$B_f$の点曲線は$E_f$上。
両者の同型を仮定して有限EndやO-pointingを比較してはならない。

**非同型性の厳密数値例。**
$f_1=x(x-1),f_2=(x-2)(x-3)$なら
$C_q:y^2=x(x-1)(x-2)(x-3)$、
$E_f$は$t=d/(x-3),z=(t^2-1)c$によって
$z^2=6t^4-7t^2+2$へ双有理化される。
二進四次不変式$I,J$はそれぞれ
$(13,-70)$、$(193,-5362)$で、
$j(C_q)=35152/9$、$j(E_f)=28756228/3$。
両者は相異なるが、
$\Phi_2(j(C_q),j(E_f))=0$を厳密整数算術で確認。
MathMIT Sutherlandの古典的modular polynomial $\Phi_2$ の
明示係数を一次webページで確認。
検算はcomputations/verify_rootpair_resolvent_spectral.pyに統合。
これは多項式等式の計算で、相対pointed同値の証明ではない。

**MCM行列のkernelから$E_f$の二pencilを直接復元（証明済み）。**
$f_1=-\ell_1\ell_2,\ f_2=-m_1m_2$について
$M_c=\left(\begin{smallmatrix}c&\ell_1\\\ell_2&-c\end{smallmatrix}\right)$、
$M_d=\left(\begin{smallmatrix}d&m_1\\m_2&-d\end{smallmatrix}\right)$
は$B_f$で平方零、$E_f$上の各点で階数1。
その右kernel直線は$(u,v,c)$および$(u,v,d)$の
smooth conicの標準パラメータを与える。
従って$\ker M_c$の射の$\OO_{\PP^1}(1)$のpullbackは
$F_c$、$\ker M_d$からは$F_d$となる
（C prop:qa-point-mcm-matrix-pencils）。
これは線形matrix factorizationの**pointwise kernel**と
幾何的二pencilの一致である。

**noncubic normal helixの二つの隣接乗法の像も同定（Cで証明）。**
$V=\Hom(\pi B_f,\pi B_f(1))=(B_f)_1$とすると、
Aの\`cor:normal-cubic-defect\`で記述した
$X_c,X_d$の隣接合成像は、MCM行列の四つの成分から
\[
 U_c=\langle c,\ell_1,\ell_2\rangle
     =\langle u,v,c\rangle,\qquad
 U_d=\langle d,m_1,m_2\rangle
     =\langle u,v,d\rangle
\]
となる。一方、点曲線$E_f$上では
$F_c^2=F_d^2=\OO_{E_f}(1)$であり、
$\operatorname{Sym}^2H^0(F_c)$および
$\operatorname{Sym}^2H^0(F_d)$のVeronese積像は
それぞれ$Q_c$、$Q_d$の超平面切断に等しいため、
上の$U_c,U_d$と一致する。
両像は三次元、交わりは$\langle u,v\rangle$、
和は$V$の四次元全体。
証明正本：C \`prop:qa-point-mcm-composition-veronese\`。
これで**二つのrank-three隣接積について
AS側と点曲線pencil側の具体的な積像が一致**した。
この二つのrank-three積像だけでは有限Endの同型は従わないが、Cの次の定理は全Homの制限単射と次元比較を補い、全幾何点でpointed同値を証明する。

**全noncubic幾何点のpointed認識（C v3.7）。** 二つのsquarefree二次形式の根対は、相異・一根共有・一致をすべて許す。点曲線$E_f=\operatorname{Proj} B_f^{\mathrm{ab}}$は二conicのファイバー積$Q_c\times_{\mathbb P^1}Q_d$で、smooth/nodal/$I_2$の$(2,2)$ Cartier因子になる（C lem:qa-pointed-all-rootpair-geometry）。$X_c,X_d$の可換化によるspinor section moduleと、四頂点Endの全Hom・全合成の同型は三型すべてで成立する（C lem:qa-pointed-abelianization-four-end）。square avatar $(E_f,F_c,F_d,P_E)$の指定mutation後、比較すべき四項は$(H_0,\ldots,H_3)$でなく**$(H_1,\ldots,H_4)$**。この位相でSerre完成・AZを使い、全noncubic $\mathcal H_2(k)$について$(\qgr B_f,\pi B_f)\simeq(\qgr A_{\rm av},\pi e_1A_{\rm av})$という**体上のO-pointed exact同値**を原稿で証明した（C thm:qa-point-all-noncubic-pointed, cor:qa-point-all-noncubic-h2）。点曲線側の非被約基底を含む相対pointed認識は対称Morita表示で成立する。smooth spectral側の指定AS10 pointingは上記の二同種対合で決定済みであり、別のrotated標準pointingも体上で判定済みであり、全相対avatar/QP表示groupoidの比較は残る。三型の有理係数モデルで次数1–2の厳密計算をPASSしたが、数学的全証明の独立全面監査・新規性・組版は別状態。

**順序付き分解普遍族の相対有限End（C v3.7）。** $S=k[\ell_i,m_i,(\det\ell\,\det m)^{-1}]$（二組の独立一次形式）上で、四項$(\mathcal B,\mathcal X_c,\mathcal B(1),\mathcal X_d(1))$の有限graded directed Endと$E_S=Q_c\times_{\mathbb P^1}Q_d$上の$(\mathcal O,F,F^2,F^2G)$のEndを、**任意の$S$-基底変更（非被約も含む）と可換な代数同型**として証明した（C prop:qa-point-relative-split-root-end）。被約でsmoothな普遍底で有限表示行列の全幾何fiber階数が一定であることから局所分裂を得て、その後に非被約底へ引き戻す。この有限Homと全積の比較を入力として、対称Morita降下と相対Serre完成の二節で全二形式商上のpointed heart比較を証明した。全avatar/AS/QP表示stackの認識とは区別する。

**四頂点のBrauer重みとAzumaya双加群Morita表示（C v4.1）。** 二conicの普遍次数一線束$N_i$、$V_i=q_{i*}N_i$に対し、相対双対化から$N_i^2\simeq\mathcal O_{Q_i}(1)\otimes\det V_i$を証明。$H=\mathcal O_E(1)$として四項を$(L_0,L_1,L_2,L_3)=(\mathcal O_E,F,H,HG)$へ正規化した。$\Gm^2$-gerbeの慣性重みは$w_i=((0,0),(1,0),(0,0),(0,1))$、非対角$T_{ij}=\pi_*(L_i^{-1}L_j)$の階数は$(2,4,6,2,4,2)$、重みは$(1,0),(0,0),(0,1),(-1,0),(-1,1),(0,1)$（順に01,02,03,12,13,23）。$W_0=W_2=\mathcal O$, $W_1=V_c$, $W_3=V_d$とおくと$\operatorname{End}(W_i)$は重み零で、係数空間上のAzumaya代数$A_i$に降下する。Brauer類は$(0,\alpha_c,0,\alpha_d)$。$T_{ij}\otimes W_i\otimes W_j^\vee$も重み零で、$(A_i,A_j)$-双加群$\mathsf M_{ij}$へ降下し、Morita evaluationによって$\mathsf M_{ij}\otimes_{A_j}\mathsf M_{jk}\to\mathsf M_{ik}$の全合成を得る。これが原稿C thm:qa-twisted-four-vertex-morita。分岐根選択被覆で$V_i$と$\det V_c$を自明化すると元のspinor有限EndのMorita増幅に一致。一般点で$\alpha_c-\alpha_d\ne0$なので二根対交換を**頂点固定Morita自己同値**にすることは不可能（C cor:qa-morita-ruling-exchange-phase）。この位相変更は対称四項への相対mutationで実現し、全商への階数45表示・全次数Serre完成・pointed heartの比較まで証明した。既知のgerbe重み一般論はBergh--Schnürer (2021)に帰属し、本研究の追加は四項の具体的重み・双加群合成とgeneric rulingの障害。

**一般noncubicのperiod-indexと二つの四重被覆の識別（C v4.2）。** 独立な二形式の普遍係数体$K_{12}$で、二conicのBrauer類の差$\beta=\alpha_c-\alpha_d$はAlbert 6次元形式$q=\langle a_c,\Delta_c,-a_c\Delta_c,-a_d,-\Delta_d,a_d\Delta_d\rangle$の二段階Springer剰余判定により**index 4**のdivision biquaternionを表す（C thm:qa-generic-point-period-two-index-four、先行入力 Lam--Leep--Tignol 1993 Thm 2.3、Lam 2005 Ch VI）。一般点曲線$E_f=Q_c\times_{\mathbb P^1}Q_d$の閉点は両conicを分裂させるので次数がすべて4の倍数。一方$E_f\to\mathbb P^1$は次数4、幾何次数二のpencil Picard類が$K_{12}$有理なので、**period(E_f)=2、index(E_f)=4**。smooth半周期torsor$T_P=[2]^{-1}(P)$では平行移動が二deck involutionを共役にし、実際のconic同型$Q_c|_{T_P}\simeq Q_d|_{T_P}$を誘導する。従って$\beta|_{T_P}=0$。index4から一般$T_P$は連結な次数4拡大で、$\beta$の最小次数分裂被覆（C prop:qa-half-period-conic-isomorphism）。**分岐根選択の別の次数4被覆とは非同型**。monic全根分裂族$f_1=x(x-a)$、$f_2=(x-b)(x-c)$ over $K_0=k(a,b,c)$では根選択は4つのsectionを持つ一方、二同種模型の半周期は$\operatorname{Spec}(K_0(\sqrt{c(b-a)})\times K_0(\sqrt{b(c-a)}))$と二つの非自明二次拡大に分かれる（C thm:qa-half-period-not-root-choice）。Brauer類を両方分裂させても半周期のKummer障害は残る。OU四重射とのmonodromy比較は済み、共通incidenceでの被覆同型と二同種Kummer像の一致は否定された（C v4.6）。点曲線側の相対mutation/pointingは対称Morita表示で成立する。SymPyはquartic→cubic、2-isogeny、倍算の多項式恒等式だけPASSし、index4と被覆非同型の数学的証明は原稿依存。

**共通spectral incidence上のOU/noncubic四重torsorの非同型（C v4.6）。** OU対角potentialの四固有値$x_i$、有効群$G=V\rtimes S_4$、二対分割$\mathfrak p=\{12|34\}$の安定化群$H_{\mathfrak p}$を取り、$I_{\mathfrak p}=X^\circ/(V\rtimes H_{\mathfrak p})$という自然な次数3の標識incidence基底を構成。$f_1=(t-x_1^2)(t-x_2^2)$、$f_2=(t-x_3^2)(t-x_4^2)$から、OUのspectral楕円曲線$E_{\mathrm{sp}}$とnoncubicの$C_q:y^2=f_1f_2$は**この基底上で一致**し、点曲線$E_f$はその次数2のétale被覆となる。OU四重射$Y_{\mathfrak p}=X^\circ/H_{\mathfrak p}\to I_{\mathfrak p}$とnoncubic半周期$T_{\mathfrak p}=[2]^{-1}(P_E)$はいずれも一般monodromy$D_4$だが、**有限étale被覆として非同型**（C thm:qa-ou-half-period-common-incidence-not-isomorphic）。全固有値を指定した$F=k(z_1,z_2,z_3)$へ引き戻すとOU側は自明な4点被覆、noncubic側は$F(\sqrt A)\times F(\sqrt B)$、$A=(1-z_1^2)(z_3^2-z_2^2)$、$B=(z_3^2-z_1^2)(1-z_2^2)$であり、$[A],[B]$は独立非平方。さらにOUの$J(C_q)[2]$は$F$で全4点有理的だが、noncubicの$J(E_f)[2]$は$O$と$P_E$の2点しか有理的でなく、残る二点に$\sqrt{AB}$が必要（C prop:qa-ou-half-common-incidence-groups-distinct）。従って同じspectral曲線・同じ$D_4$という群論だけではKummer類も有限群スキームも同一視できない。さらに自然な二同種$\phi=r^*:J(C_q)\to J(E_f)$の$2$-torsion写像を用いても、**$\phi[2]_*[Y_{\mathfrak p}]=\delta_{E_f,2}(\phi(P_+))\ne\delta_{E_f,2}(P_E)=[T_{\mathfrak p}]$** と証明した（C cor:qa-ou-half-isogeny-kummer-classes-distinct）。全固有値体$F$上で前者はOUの有理半点により零、後者は非分裂半周期により非零。自然なKummer類の比較は不一致と確定している。点曲線側の相対Morita mutation/pointingは成立するが、OUを含む全avatar/QP表示groupoidの比較は残る。computations/verify_ou_half_common_incidence.pyは四次式同一性、平方類の付値、OU4点の有理性、非分裂$J(E_f)[2]$判別式をSymPy厳密演算でPASS。数学的降下・新規性・LuaLaTeX組版は別状態。

上三角の双加群を合成した$\mathsf A_{\mathrm{Mor}}=\bigoplus_{i\le j}\mathsf M_{ij}$は係数空間上の**階数54の有限局所自由な通常の代数**で、零番隅は$\mathcal O_{U_2}$。全幾何fiberで階数24の基本有限End代数とMorita同値（C cor:qa-morita-rank54）。Brauer障害は通常代数の存在を排除せず、基本頂点をrank-oneのまま維持する降下を妨げる。

**証明で使う最小データ。** $R=B_f/(cd-dc)$は$E_f$の同次座標環。$X_c\otimes_B R$と$X_d\otimes_B R$はそれぞれ$p_c^*\mathcal O_{\mathbb P^1}(1)$、$p_d^*\mathcal O_{\mathbb P^1}(1)$の全section module。次数0・1には可換化による核がない。四頂点Hom次元は上三角$(1,2,4,6;1,2,4;1,2;1)$、曲線の次数$(0,2,4,6)$と一致。$X_c\to B(1)$の二基底行は$(c,\ell_1)$、$(-\ell_2,c)$で、二段階積は$\left(\begin{smallmatrix}c&\ell_1\\-\ell_2&c\end{smallmatrix}\right)$。全三退化型の全Hom同型は二段階積像だけに依存せず、次数1における制限単射と次元比較から得る。mutationの評価列から$H_0=P^2F^{-1}$、一周期後$H_4=FG^2$。よって$H_1,\ldots,H_4$に共通$P^{-1}$を掛けると$(\mathcal O,F,F^2,F^2G)$となる。**追加幾何：** $E_f=Q_c\times_{\mathbb P^1}Q_d$はsmooth/nodal/$I_2$の$(2,2)$ Cartier因子で、$p_{c*}\mathcal O_E=\mathcal O_{\mathbb P^1}\oplus\mathcal O_{\mathbb P^1}(-2)$が全三型で成立する。各$X_c\otimes_B R$は$F_c$のsection moduleに全次数で一致する。**現在の範囲**：点曲線側の全表示商への相対Serre完成・pointed heart比較は成立し、smooth spectral指定pointingの像も決定した。rotated標準pointingの体上判定は成立し、全potential stackの相対認識は未解決。計算再現は `computations/verify_noncubic_pointed_end.py`（三型の有理係数モデル、低次数に限定）。

**検証したEuler数値と非被約avatarのrank壁（C v3.4）。**
ASsq/ASrsq最小分解の四相Euler漸化式から
$H_r(z)=\sum_{n\ge0}\dim A_{i,i-n}z^n$を作ると、
全位相で
$\frac14\sum_{j=0}^3 H_r(\mathrm i^jz)
 =(1+6z^4+z^8)/(1-z^4)^3$となる。
ゆえに全$m\ge0$で$\dim A_{i+4m,i}=(2m+1)^2$。
AS10の級数は$1/((1-t)^2(1-t^2))$。
SymPyによる有理母関数の四相逆行列・root-of-unity射影と
有限次数整数再帰を独立に実行しPASSを得た。
再現コード：computations/verify_as_avatar_euler.py。
最小射影分解の\emph{完全性}、AS–Gorenstein性、
helixの実現はこの数値計算では検証できない。

square avatarでは$Q=GF^{-1}P^{-1}$とし
$F$のbasepoint-free pencil評価列を$GP^{-1}$でtensorすると
$0\to Q\to H^0(F)\otimes GP^{-1}\to FGP^{-1}\to0$。
$Q$が非自明なら$H^*(Q)=0$で乗法$\mu_G$は階数4、
$Q=O_D$なら$h^0(Q)=h^1(Q)=1$で階数3。
したがって$D$が非被約でも
$\operatorname{rk}\mu_G=3\iff P=GF^{-1}$。
反対側の階数3壁は$P=FG^{-1}$。
両方が階数3の二捩れavatarも許される。
証明正本：C lem:qa-as10-rank-wall-pencils。

**最小10本矢型の独立分類（原PDF第48--53節）。**
`papers/quiver-avatar/as10_mutation_classification.tex` の
`thm:qa-as10-global-bijection` は
ASsq の全体と ASc ⊔ AS10^min の頂点保存同型類の全単射。
AS10^min はmutation像を参照しない最小右射影分解と
AS–Gorenstein条件で定義し、
逆mutationを任意のtargetに適用。
非最小reductionのrank 4/3はcubic 8本/最小10本を分け、
10本側のavatar条件は G≅F P（P≠O_D）である。
全整数の評価・余評価が双方向のinverseを与える。
right-equivalence groupoidのtrivial pair gaugeは
underlying algebraのgroupoidとは異なる。
相対族についてはfinite foundation等のperfect性を課した
局所Noetherian基底に限って基底変更対応を扱う。
**12本矢は通常8本のfoundation矢＋4本のrelation-dual戻り矢のQP表示であり、
一般の12本矢QPに独立ASクラスの全分類は主張しない。**
P(1,1,2)のrelation QPはDWZのmutation頂点を持たない反例。

**二重壁とcubic到達可能性の完全判定（C v3.4）。**
二つの合成$\mu_G,\mu_F$が同時に階数3へ落ちる
$Z=D_F\cap D_G$は
$P^2\simeq O_D,\ P\ne O_D,\ G\simeq FP$と同値。
$P\in\Pic^0(D)$より、$D$の各既約成分のbidegreeは$(a,a)$。
可能な$(2,2)$因子は既約、二つの$(1,1)$、
二重$(1,1)$だけ。
後者の$\Pic^0\simeq G_a$は非零二捩れを持たない。
既約特異$(2,2)$のcuspも$\Pic^0=G_a$、
二つの$(1,1)$の接触型も同様。
したがって二重壁ではDはsmooth/nodal/I2の三型のみ。
非零二捩れの数は3/1/1で、
Cの根対avatar三型と一致する。
証明正本：C lem:qa-as10-double-wall-reduced-geometries,
prop:qa-as10-double-wall-characterization。

**標識付き二重壁のscheme-theoretic局所幾何（今回追加）。**
滑らかな楕円曲線$E$と次数二線束$F$を固定し、
$\eta=GF^{-1}$、$P$を$\Pic^0(E)^2$で動かす。
$P,\eta\ne0$なら$(F,G)$はsquare埋め込みを定める。
二つのmutation壁はそれぞれ$\eta=P$、$\eta=P^{-1}$。
自明線束$Q=\OO_E$の一次変形
$0\to\OO_E\to Q_\epsilon\to\OO_E\to0$の接続は
$H^0(\OO_E)\to H^1(\OO_E)$における$\xi$とのcup積であり、
非零$\xi$なら同型。
Pencil trickの相対行列式はよって
Picard原点で一次の零点を持ち、
二壁は\emph{被約な}Cartier divisorとなる。
非零二捩れ点の局所座標$(u,v)$では接方程式が
$v-u$と$v+u$でJacobian determinantは$-2$。
従って横断的で、固定smooth曲線上の交点は三つの被約点。
曲線が動く滑らかな楕円族においては
$E[2]\setminus\{0\}$が相対有限étale三次となる。
固定nodal/$I_2$では$\Pic^0(D)\cong\Gm$、
非零2捩れ$-1$が一つで同じ横断性が成立。
**交点のscheme長はsmooth/nodal/I2で3/1/1**。
これは標識付き・固定曲線のパラメータの結果であり、
inner H2 stackの慣性・相対scheme同型を与えない。
証明：C prop:qa-as10-double-wall-transversality,
cor:qa-as10-singular-double-wall-transversality。
局所Jacobianと$\Gm[2]$は既存コード
computations/verify_avatar_cubic_obstruction.pyで
SymPy exact計算を実行してPASS。
数学的な局所scheme計算を証明器で検証したわけではなく、
この局所結果の公表新規性は未確認。

**さらに強い主定理（元PDF定理21.1）。**
Cの新設
papers/quiver-avatar/cubic_obstruction_all_loci.tex に
thm:qa-as-cubic-reachabilityを統合。
ASsqがcubic ASのQgr/qgrと完全Abel同値、
またはDb(qgr)と三角同値になるための
必要十分条件は$A\notin Z$。
正方向はどちらかのrank4 chartと
mutationのQgr同値。
否定方向は以下の独立した補題列を必要とする。
- Cubic候補は単に最初のmutation像とは限らず、
  任意の四項strong exceptional＋K0整数基底＋
  cubic Euler行列＋隣接合成二つの同型で定義する。
- $(S_*-1)^2$のrank functionalと
  K0のprimitive交代結合から
  全rankは共通$\pm1$となり、
  四線束の数値第一Chernは
  $(a,b),(a+1,b),(a+1,b+1),(a+2,b+1)$型。
  determinant formula
  $\det\rho X=F^aG^bP^{r-a-b+s}$を使うと、
  二重壁では隣接商は$F,FP$のいずれかで
  最初と最後が異なる。したがって連続する二本が一致し、
  $\operatorname{Sym}^2 H^0(L)$の一次元kernelのため
  cubicの合成同型に矛盾する。
- 特異Dは二捩れ$\mu_2$-torsorの有限étale性と
  形式的存在で、smooth generic fiberへ平滑化する。
  finite directed End代数はR=k[[t]]上有限自由。
  仮に特殊fiberにcubic候補があれば、
  $\Ext^2(Q_i,Q_i)=0$で個々のperfect complexを持ち上げ、
  Homの有限自由複体のminimal reductionで
  strongness、合成同型、K0基底をgenericに保つ。
  smooth generic fiberでの矛盾に帰着する。
- Serre数値作用・二捩れ指数parityは独立の
  SymPyコード computations/verify_avatar_cubic_obstruction.py
  で有限厳密検算PASS。
  これは滑らかな候補不存在全体、形式GAGA、
  exceptional lifting、derived同値の機械的証明ではない。

**重要な比較上の注意。**
二重壁のASsqは任意のcubic ASと導来非同値であるが、
同じavatarを持つBのnoncubic O-marked H2対象との
pointed qgr-heart同値は別途必要。
この定理は原PDFの既存結果を原稿へ移管したもので、
新規発見の主張ではない。
点曲線側のnoncubic族では相対mutationとpointed heartを構成した。
任意のavatar族についての相対認識とDG/Ginzburg集中の
独立全面監査は残る。


**Mutation後のNoether性とAbel/derived比較。**
C prop:qa-as10-noetherian-qgrに、
square側の反Serre四周期$E_0$軌道のcofinal residue
cornerとAZ1/AZ2、mutation後の$H_1=E_0$を含む
$T_H$に対する評価列のExt消滅を用いて、
mutation先の左右Noether性および
$\Qgr m(A)\simeq\Qgr A,\ \qgr m(A)\simeq\qgr A$
のproofを統合した（元PDF命題52.1）。
C prop:qa-as-avatar-coherent-moritaには
Noether性と全単純分解から
$D^b(\qgr A)\simeq D^b(\mathrm{mod}\,B)$、
Serre$\nu[2]$を導くproofを置く（元PDF命題8.1）。
これらはunderlying Abel/derived同値であり、
O-marked structure objectを固定するpointed同値ではない。
一般有限生成graded加群の分解停止、corner道の有界性、
AZ再構成の仮定、Serre transportは独立監査未完了。

**Keller--Ginzburg／Keller–Yangの一次監査。**
有限directed$B$は$\mathrm{gldim}\,B=2$かつ
minimal relationsが矢idealの二乗にある。
Keller (2011, Thm6.10, undeformed case)で
relation QPの$\Gamma(Q,W)$は
$\Pi_3(B)=T_B\Theta$に準同型、$\Theta=
\RHom_{B^e}(B,B^e)[2]$。
各$m$次tensor成分について
$e_j\Theta^{\otimes_B^{\mathbf L}m}e_i
\simeq\RHom_B(E_i,S_B^{-m}E_j[2m])$。
$m=0$は有限代数$B$、$m\ge1$では
$j+4m>i$であるため全整数のforward Ext消滅を適用し、
degree 0集中を得る。
全Ginzburg生成元の内部次数は正、各次数有限なので
内部次数直積とarrow-adic完備化が整合し、
非完備版と完備版の集中を一致させる。
Keller–Yang (2011, Thm6.2)には
源potentialが\emph{reduced}であることも必要。
relation potentialはminimal relation length$\ge2$と
dual矢の積でlength$\ge3$だから満たす。
(c1)全quiver loopなし、
(c2)mutation頂点にoriented 2-cycleなし、
(c3)cyclic representativeが指定頂点から始まらない
という三局所条件も別々に確認。
C lem:qa-as10-ginzburg-concentrationと
lem:qa-as10-keller-yangに詳細を統合。
これは引用定理の適用仮定と各tensor成分の論理点検で、
全AS最小分解へのDG降下・AS--Gorenstein性の全証明の
独立形式検証ではない。

**一般定理・検証の所在。**
外部入力は Okawa–Ueda (arXiv:2007.07620, Theorem 5)
のacyclic spherical helix→exceptional realization、
Keller (2011, Theorem 6.10) の`undeformed` CY completion、
Keller–Yang (2011, Theorem 6.2) のQP mutation、
twisted section algebraのNoether性。
元PDFの分類の証明を現在の原稿に組み直したことと、
今回その全数学的推論を独立に検証したことは区別する。
いずれも原資料著者の結果であり、
この移管を新発見・外部査読済みとは扱わない。
最優先の独立監査は、ASの必要rank forcingの商、
非被約DのPic0判定、Yoneda truncation、DG双加群三角形、
Keller–Yang局所仮定、全整数inverseの自然性。
一方、O-marked内在的H2 heartとのpointed同値と
一般非被約底での無条件相対ASスタック同値は未証明。

**相対spectral境界で既に得た結果と核心。**



**共有根の相対線束障害と奇偶類（Cで証明）。**
$A=k[[a,b,y]]/(ab-y^2)=k[[c,d]]^{\pm}$、
$s=a-b$、反不変加群 $M=Ac+Ad$ とする。
最小解消の chart は $(a,y,b)=(u,ut,ut^2)$ と
$(vw^2,vw,v)$、重なりで $v=ut^2,w=t^{-1}$。
$(\pi^*M)/\mathrm{tors}$ は例外曲線 $E$ 上で
$\mathcal O_E(1)$ に制限する。
既約 nodal 特殊曲線の strict transform $D'$ は
$E$ と二点で交わり、$E^2=-2,\ D'\cdot E=2$ だから、
垂直 Cartier twist による $\deg_E$ の変化は偶数。
同じ一径数基底での A1 最小解消だけでは
多重次数零の相対 $\Pic^0$ 線束にできない。
二traitでは任意有限分岐後の最小正則模型I_Nにも重み付き次数N/2 mod Nが残り、入力二捩れを多重次数零・二乗自明な線束には延長できない。線束自体の延長、非可逆TF層、および別の商曲線上のFricke出力二次線束は区別する。証明は現行の境界模型節を参照。

**二次積の任意基底での scheme-theoretic 欠損（Cで証明）。**
$C:y^2=f_1f_2$ と反不変 torsion-free sheaf $\mathcal M$ に
自然な対称積 $\mu:\mathcal M\otimes\mathcal M\to\mathcal O_C$ がある。
像は局所的に $(f_1,f_2,y)$、余核は
$\mathcal O_{\{f_1=f_2=y=0\}}\simeq
 \mathcal O_{\PP^1_S}/(f_1,f_2)$。
これは非被約底を含む任意基底変更と可換し、
各被約二根対の幾何 fiber 上では欠損長が
smooth/nodal/I2の順に$0/1/2$となる。
積の随伴射 $\mu^\flat:\mathcal M\to\mathcal M^\vee$
は **各squarefree幾何fiber上** で同型だが、
節点では $\mu$ 自体は全射ではない。
通常の line-bundle 二捩れと区別する。

**正規化上の極限と自己同型（Cで証明）。**
- smooth: $\mathcal M$ は非零二捩れ線束、$\End_C(M)=k$。
- 既約 nodal: $\mathcal M=\nu_*\mathcal O_{\PP^1}(-1)$、
  $\End_C(M)=k$（単純）。これは
  $\Pic^0(C)\simeq\Gm$ の非零二捩れ線束（貼合せ値$-1$）とは
  同型でない。
- $I_2$: $\mathcal M=\nu_*(\mathcal O_{\PP^1}(-1)
  \oplus\mathcal O_{\PP^1}(-1))$、$\End_C(M)=k\oplus k$。
  従って underlying sheaf は非単純で、
  simple/fine compactified Jacobian の対象ではない。
  一方、曲線を固定して二次積まで保存する組の慣性は
  smooth/nodal で $\mu_2$、I2 で $\mu_2^2$ となる。
  これは全O-marked avatar stackの慣性計算ではない。

証明正本は papers/quiver-avatar/nodal_resolution_obstruction.tex
（prop:qa-spectral-product-defect、
thm:qa-spectral-three-fiber-limits、
cor:qa-spectral-pair-finite-inertia）。
既知のrank-one torsion-free sheaf・多重次数・compactificationの
一般理論は Altman--Kleiman (1980) と
Christ--Payne--Shen (2023, DOI 10.1090/tran/8875) に依拠する。
二形式からの明示的な積欠損と極限の計算が本稿での追加内容で、
包括的新規性調査は未実施。
計算資産 computations/verify_nodal_exceptional_parity.py は
A1 chart・奇偶に加えて、局所環の平方積関係と
交差根数$0/1/2$の有限多項式検算を含む。
これは数学的な相対groupoid同値の形式検証ではない。

**構成済みの相対二次積groupoid射と次の課題。**
$fppf$ groupoid $\mathfrak{TF}^{quad}$ の対象を、
相対$\PP^1$束 $B/S$、種数一の有限平坦二重被覆
$C\to B$、相対平坦rank-one torsion-free次数零層$M$、
および幾何fiberで自己双対性を誘導する積
$\mu:M\otimes M\to O_C$ と定義する。
論文Bの表示群
$G=((GL(W)\times G_m^2)\rtimes S_2)/D$
は二つの平方根変数の置換・スカラー変更で積を保存し、
対角$D$の作用はProj上自明である。
したがって二形式表示商$[P/G]$から
$(C,M,\mu)$へのfppf相対群oid射が存在する
（C prop:qa-spectral-quadratic-stack-map）。
欠損余核の表示は非被約底を含む任意の基底変更と可換する。

節点曲線のTF標的のArtin性・有限型性、balanced開の表示、全忠実性、fiber・慣性は [標的認識](../papers/quiver-avatar/torsion_free_spectral_recognition.tex) で証明済み。自然なFricke射の大域的境界延長は [降下節](../papers/quiver-avatar/fricke_boundary_descent.tex) に置く。非被約spectral曲線全体の標的と任意AS heartの認識は別の未解決問題である。

## 論文C：OU四重GIT・相対Picard根・内在的forgetful射

**正本と確実性。** 数学的定理・証明は論文C
(papers/quiver-avatar/git_comparison.tex)に置く。
以下は検算規約・相対比較の入力・現在残る核心のみ。
OU2014 §4 (4.11)–(4.13)、§5 (5.3)、(5.8)–(5.10)の一次PDF画像を直接確認した。
**原論文の印刷に不整合がある：** (5.3) は四固有値の全置換S4を明示し、
(5.8)直後の商表示は二箇所S3と印刷している。
(5.3)の対称式環C[f1,f2,f3,f4]と(5.7)のP(1,2,3,4)は
四座標S4を要求する。従って本研究の正しい対角商
P³/S4_coord → P³/((Z/2)³⋊S4_coord)は
**(5.3)からの訂正解釈**であり、原論文(5.8)の文字列そのものではない。
以前の研究資料の「原論文(5.8)にS4と印刷」との断言は訂正した。

**OUの実際の群と四重torsor。**
四座標の偶数符号群の射影的有効商
V={e∈F2^4:∑e_i=0}/<1111>≅F2²、
座標置換H=S4_coordとし、G=V⋊H（位数96）。
HのVへの作用の核は二重互換K4（位数4）で、
像はGL2(F2)≅S3。
coset G/HはVの四元でありGはu↦v+σ(u)と作用する。
Core_G(H)=K4、G/K4=AGL2(F2)≅S4_mon。
よってOU一般四重射は非GaloisでGalois閉包S4_mon。
単なる定数V-torsorではない。
Gが自由に作用する稠密な対角開Xに対しB=X/G,
Y=X/Hは、線型作用による可変有限étale群局所系
𝒱=X×^G V_linの自然なtorsorで、
[Y]∈H¹_et(B,𝒱)となる。
この作用群の有限計算はcomputations/verify_ou_fourfold.py
（even sign 8, V 4, G 96, core 4, image 24、
K4⋊S3=H）で独立に確認し、ソースにassertionsを追加した。
今回の計算検証はOU/Picard両torsor同型の形式証明ではない。

**OU §4の楕円群との強い抽象的整合性。**
H=S4_coordはK4⋊S3_markに分裂するので
G=(V_sign⊕K4_coord)⋊S3_mark。
V_signとK4_coordは同じS3標準二次元表現であり、
OU §4のG_ell=(E[2]_{z1}⊕E[2]_{z2})⋊SL2(F2)と
**index4部分群を含む抽象有限群対として同型**となる。
V_signをz2、K4をz1側と対応できるが、
これは同変双有理写像の存在を証明しない。
四分岐点の偶数部分集合/補集合によって
V_signは四点分岐genus1の2-torsionと標準的に同型。
ただし符号反転が分岐点集合自体を変えるので
そのspectral curveや群スキームを
quintuple曲線のE[2]と無証明に同一視しない。

**OU四重被覆のspectral Kummer模型（Cで証明）。**
二乗座標 a_i=x_i² の四分岐点から
E_sp: y²=∏(t−a_i) を作ると、
無限遠の正のsection O=∞_+ と P+=(0,∏x_i) が
G=V⋊S4_coord の作用を降下する。E_sp の群原点を O とし、
V=even sign/<all signs> は E_sp[2] と同型となる。
四つのsign sheetは [2]^{-1}(P+) の四つの点そのものである。
具体的には、∏(z−x_i)=z⁴−s1z³+s2z²−s3z+c、
q(t)=t²+s2t+c、l(t)=s1t+s3 とすると
q(t)²−∏(t−x_i²)=t l(t)²。
t0=−s3/s1、Q=(t0,−q(t0)) は 2(Q−O)∼P+−O。
偶数符号の四選択は一般に異なる Q を与える（Python厳密検算）。
よってOUのclassはこの *spectral* 曲線に対し
$\delta_{[2]}(P_+)=\delta_{[-2]}(-P_+)$ として明示できた。
分岐点R_iは別のPicard半点torsor（P_-−P_+の半点）をなし、
そのmonodromy核はV、OU側はK4で、両者は異なる。
証明正本はCのthm:qa-ou-spectral-kummerと
prop:qa-ou-spectral-branch-not-sign。
再現は computations/verify_ou_spectral_halving.py。
**点曲線とのJacobian比較も進展した。**
potential Φの縮約線型変換をq-自己随伴Xとして表すと、
point curve C は P³中の {q(u)=q(Xu)=0}。
対角X=diag(x_i)では二次式Σu_i²=Σx_i²u_i²=0となり、
quadric pencil det(tI−X²)=∏(t−x_i²) の二重ruling被覆は
Pic²(C)に同型。∞の二rulingはL0,L1、t=0は
L2とH_C L2^-1、H_C=L0L1。
従ってE_spとJac(C)は**対角potential atlas上で実際に同型**。
さらにOUのf2,f4,f6,g4からe_iをNewton恒等式で作り、
I=e2²−3e1e3+12e4、
J=−2e2³+9e1e2e3−27e3²−27e1²e4+72e2e4、
j=1728·4I³/(4I³−J²)を導出した。
有理点x=(1,2,3,5)でj=3796416/1225をcross ratioと照合。
証明正本はC prop:qa-ou-pointcurve-quadric-pencil と
cor:qa-ou-quintuple-j-invariants。
**Hodge符号と対角一般開のPicard根一致（Cで証明）。**
$q_t=tq-q\circ X$ に対し $a_i=t-x_i^2$、
$y^2=\prod a_i$ とすると、中間外冪のHodge対合は
$J_{t,y}(e_i\wedge e_j)=\epsilon_{ijkl}y/(a_ka_l)e_k\wedge e_l$。
Segre $q=2(ad-bc)$ では第一因子固定のplaneが正、
第二因子固定が負のchiralityを持つ。
$\infty_+$ を $\mathcal L_0$ とすると、
$t=0,y=\det X$ で
$J_{0,\det X}=(\Lambda^2X)^{-1}J_q(\Lambda^2X)$
だから $P_+\leftrightarrow\mathcal L_2$。
$\Theta:E_{sp}\simeq\operatorname{Pic}^0(C)$ で
$P_+\mapsto N=\mathcal L_2\mathcal L_0^{-1}$、
$Q\mapsto-\Theta(Q)$ は$[-2]a=N$を満たす。
偶数符号はtarget側SO4、四座標置換は両側SO4の符号付き置換。
異なる置換liftの差は各rulingに自明に作用するので
Jacobian・指定点・torsorがGの商に降下する。
奇数符号変更では$P_+$/$P_-$と二rulingが交換される。
証明正本：Cのlem:qa-ou-hodge-ruling-sign、
thm:qa-ou-diagonal-picard-torsor。
厳密符号検算：computations/verify_ou_hodge_ruling.py。

**非対角正則半単純potentialの相対版（Cで証明）。**
$q$-自己随伴な$X$の$\det X$および$\operatorname{disc}\det(tI-X^2)$が
可逆な族では、étale局所SO(q)対角化とHodgeの自然性から
$\mathcal E_{sp}\simeq\operatorname{Pic}^0_{C/S}$、
$P_+\leftrightarrow N$が任意の底変更と可換に成立する。
$\det(zI-X)=z^4-s_1z^3+s_2z^2-s_3z+c$の$s_1$可逆開で
$t_0=-s_3/s_1$、$Q_X=(t_0,-(t_0^2+s_2t_0+c))$は
$[2]Q_X=P_+$を満たし、$a_X=-\Theta(Q_X)$は
$[-2]a_X=N$の相対半点。詳しくはCの
cor:qa-ou-relative-regular-semisimple-potential。
potentialを選ぶ前の一般quintupleの全相対groupoid比較までは含めない。

**現行の未解決課題。** この同型は滑らかな対角稠密開で
Jacobian・指定点・torsorについて確立したものであり、
potentialを選ばない一般quintupleの全相対族、粗GIT全域のuniversal曲線、
中心スカラー剛体化後の慣性・微分・pointed fiber、
nodal・cuspidal境界への延長を主張しない。
次はpotentialを選ばない一般quintupleへの相対groupoid降下と慣性・接写像を調べる。

**Picardの半点とnodal境界障害。**
Bのlem:picard-halvesでは根空間
T_N=S×_(N,Pic0,[-2])Pic0はétale全射。
smooth ellipticならE[2]-torsorで幾何fiber4点、
既約nodalではPic0=Gmで2点、cuspidalではPic0=Gaで1点。
OU §4楕円四つ組(E,O(2o),O(2z1),O(2z2))では
N=L2 L0^-1=O(2z2−2o)、
a=O(o−z2)⊗ξ（ξ∈E[2]）。
z2にE[2]を足す操作はこの半点の四選択と一致する。
OU有限GIT射とT_Nが連結基底S上で同型なら
T_Nは有限étale次数4となるが、同じ基底にsmoothとnodalが
ある場合にはfiberが4/2と異なるので**同型は不可能**。
滑らかなgeneric locusでの比較と境界までの
有限compactificationを別課題とする。

**二つの相対torsorを同定する具体的テスト。**
smooth elliptic quintuple基底S→Bにおいて
群局所系𝒱_S≅E[2]を幾何的に構成し、
φ_*[Y_S]=$\delta_{[-2]}(N)$ in H¹_et(S,E[2])を証明すれば、
OU四重torsor≅Picard根torsorとなる。
同値な実践的課題は、OU potential側P=Y×_B S上で
a∈E(P)を構成し、
[-2]a=N|_P、a(p+v)=a(p)+φ(v)を
P×_S𝒱の上の等式として確認することである。
幾何点ごとの半点存在だけでは足りない。
論文Cの cor:qa-ou-picard-h1-criterion、
lem:qa-ou-equivariant-halfpoint-test に証明を保持。
quintuple側の同型は**滑らかな対角一般開では証明済み**。一般非対角族・剛体化後の慣性・境界への拡張は未解決。


**剛体化後も残るquintuple一般慣性とスタック四重射（Cで証明）。**
OU2014 Theorem1.1(1),(3) の「一般安定化群Gm⁴/Gm」を
文字通り全慣性と解釈すると有限成分を見落とす。
quintuple群G̃/K（K=Gm⁴）を
(SO4×SO4×Gm)/Z, |Z|=4 と表す。
正則半単純一般対角X=diag(x_i)では、
λgXhᵀ=Xのtrace条件からλ²=1、中心核でλ=1へ正規化し、
g=h=diag(ε_i), ∏ε_i=1。
全反転−Iを割ると慣性はμ₂²（位数4）となる。
Lie接写像(A,B,α)↦AX−XB+αXのorbit rankは13/16、
接sliceはdiagonal k⁴/kx（dim3）、慣性作用は自明。
点曲線C={Σu_i²=Σx_i²u_i²=0}で二つの−1を持つ
Dは固定点がなく、楕円平行移動の全Jac(C)[2]に一致。
C上の翻訳はPic⁰(C)に自明に作用するので、
四つのPicard根の**同型類**をそれぞれ固定する。
これを根torsorのdeck E[2]（四根に自由推移的作用）と混同しない。
原稿の命題 prop:qa-ou-generic-quintuple-finite-inertia に証明。

有効potential側はP=(SO4×Gm)/⟨(-I,1)⟩、
有効quintuple側はQ=(SO4×SO4×Gm)/Z。
群単射g↦(g,g)とSym²U↪EndUの一般点では
慣性がμ₂²同型、potentialのLie orbit rank7/10、
quintuple側rank13/16で、ともに接slice k⁴/kx。
従って表示スタックの一般四重射は表現可能étale。
OUの有限次数4のGIT射と合わせて、適当な稠密開では
表現可能な有限étale次数4の**スタック射**となる。
これはquadric内在H2への忘却射ではない。
原稿 thm:qa-ou-rigid-potential-quintuple-generic-etale を参照。
再現資産は computations/verify_ou_quintuple_inertia.py。
検算の範囲は有限符号群・有理数での軌道行列rank・固定点障害であり、
厳密な一般記号的証明は論文本文に置く。

**pointed忘却の一般エタール性と幾何次数二（Cで証明）。**
剛体化quintupleの一般μ₂²は、VdBの幾何的商D→D_geomと
coh(C)の点対象の完全忠実埋込により、H2のpointed自己同値へ単射。
非単位の2捩れ翻訳はk(p)を非同型なk(p+ξ)へ移す。
Bの `lem:universal-nonlinear-cubic-h2-family` と
`thm:quintuple-chart-artin-lifting` は、射影化された
15次元の普遍非線型geometric quintuple S_e→H2が
representable smoothであることを示す。
テンソル非零ベクトルのGm-torsor T^nl→S_eを合成し、
T^nl→[T^nl/G_eff]（dim G_eff=13）のsmooth atlasを使って降下すると、
F:[T^nl/G_eff]→H2はsmooth相対次元(16−13)−3=0。
一般μ₂²慣性の単射によりこの開でrepresentable、
従ってétale。接複体同型から内在HH¹=0、
HH²≅k⁴/kx（dim3）を得る。
論文C `thm:qa-quintuple-h2-generic-etale` が証明正本。
これはBの相対smoothness証明を新たに独立再検証した主張ではなく、
既存入力に基づく厳密な帰結である。

**一般fiberは二つのnormalized ruling foundation。**
B `cor:two-intrinsic-foundations` は、固定pointed対象で
(O,X,M,Z)と(O,Y,M,Z')の二つが全てであることを証明。
楕円四つ組 U=(E,L0,L1,L2) の差をη=L1−L0, δ=L2−L0とすると
B `lem:elliptic-two-reflections` のもう一方は
R(U)=(E,L0L1L2^{-1},L2,L1)、差は(2δ−η,δ)。
j(E)≠0,1728、δ∉E[2]、η−δ∉E[2]、η∉{0,2δ} の非空稠密開では
Aut(E,0)={±1}、εδ=δからε=1、εη=2δ−ηから2(η−δ)=0となり、η−δ∉E[2]に矛盾。
二つの四つ組は非同型で、両方cubic型。pointed自己同値に
ruling交換成分がなく、全慣性はμ₂²。
よって忘却の2-fiberは慣性核のない二つの対象からなり、
一般の有限étale次数は2。
有効potential→quintuple表示スタックは一般有限étale次数4なので
合成potential→H2は一般有限étale次数8。
C `cor:qa-quintuple-h2-generic-degree-two` と
`cor:qa-potential-h2-generic-degree-eight` に証明。
この8を4つのPicard Serre根の数や自己同値群の位数と混同しない。
**稠密開でのstack同型。** 表現可能有限étale次数2のquintuple→H2には、任意基底変更と可換なcanonical deck対合がある。étale局所に二つのsheetが分裂するときの交換で、rank2代数上の式i(a)=Tr(a)−aにより一意に構成する。従ってH2の適当な稠密開は剛体化quintuple一般開のS₂商と同値。幾何点では二つのnormalized foundationの交換。C thm:qa-h2-generic-ruling-quotientが証明正本。これは特殊点全体でBの相対mutationが既にH2を表現すると結論しない。

**特殊ruling交換の二捩れ条件（Cで証明）。**
滑らかな許容楕円四つ組でj(E)≠0,1728、δ≠0、η∉{0,δ,2δ}とする。
二つのnormalized foundationを交換するpointed自己同値が存在する必要十分条件は
δ∈E[2]またはη−δ∈E[2]。
楕円自己同型の線型部分ε∈{±1}についてεδ=δ、εη=2δ−η が必要十分。
ε=1なら2(η−δ)=0、ε=−1なら2δ=0。最初の次数二線束は
[2]:E→Eの全射性を使ってtranslationで合わせられる。
Bの二foundation全充満性からpointed自己同値へ昇格。
正則半単純な特別点では指定foundationの慣性μ₂²はindex2、
内在H2の全慣性は位数8。**相対2-fiberはなお二点：** sourceのquintuple同型類は一つでも、Aut_H2（位数8）/Aut_source（位数4）の二剰余類から自明慣性の二対象を得る。pointed忘却は正則半単純開で表現可能étaleなので、この点でstack射は非分岐。Cのprop:qa-special-ruling-two-fiber-no-stack-ramificationに証明。粗モジュライ上の分岐・群拡大の型は未解決。
一般有限étale二重射の稠密openにはδ,η−δ∉E[2]を課す。
証明正本はCのprop:qa-elliptic-ruling-swap-two-torsion。

**片側二捩れ特別座の全慣性群型（Cで証明）。**
正則半単純・j≠0,1728で、η−δ∈E[2]\{0}かつδ∉E[2]なら
ruling交換は位数4の楕円translation t_vで、2v=±(η−δ)。
E[2]と合わせて全pointed慣性はC4×C2となる。
δ∈E[2]\{0}かつη−δ∉E[2]なら、交換はt_v∘[-1]で
二乗恒等、E[2]への共役も恒等であるためC2³となる。
曲線上の作用の忠実性は、foundation保持部分E[2]の忠実性と、
交換成分が曲線恒等ならL0とL0L1L2^{-1}の非同型性
（η≠δ）に反することから従う。
Cのprop:qa-elliptic-special-inertia-group-typesが証明正本。
二条件同時・j=0,1728は対象外、粗空間の法表現・分岐は未解決。

**OU spectral二捩れの方程式と局所粗分岐（Cで証明）。**
E_sp:y²=∏(t−x_i²)、O=∞+、P±=(0,±c)に対し
ruling同型でΘ(P+)=δ、Θ(P−)=η−δ。
e_iをx_i²の基本対称式、c=∏x_iと置けば
δ∈E[2] ⇔ e3+e1c=0、η−δ∈E[2] ⇔ e3−e1c=0。
Weierstrass化 u=y+t²−e1 t/2+(e2/2−e1²/8)、v=tu
によって2v+a1u+a3をP±へ代入する直接証明。
OUの f2,f4,f6,g4 では重み6式
D±=f2³−3f2f4+2f6±6f2g4。
滑らかな正則半単純・f2g4≠0・j≠0,1728の開で
源粗モジュライのramification座はD+D−=0。
片側座のH2慣性はC4×C2またはC2³、sourceμ₂²は
変形(j,η,δ)に自明。交換R(η,δ)=(2δ−η,δ)あるいは
(-1)R(η,δ)=(η−2δ,−δ)の法作用は−1、接固有値(1,1,−1)。
Alper--Hall--Rydh Theorem1.2のsmooth閉点étale sliceで
局所粗germはk[[s,w,z]]→k[[s,w,z²]]（分岐指数2）。
これは局所粗射であり、スタック忘却はétale非分岐。
例x=(1,2,3,−6)とx=(1,2,3,6)がそれぞれ二特別座に属する。
証明正本はC prop:qa-ou-spectral-torsion-divisors、
thm:qa-ou-special-reflection-coarse-branch、
cor:qa-ou-coarse-branch-invariant-equations。

**二捩れ交点の新しい局所型（Cで証明）。**
同時条件はc≠0の下e1=e3=0で、判別式
f(t)=t⁴+e2t²+c²がt↦−t対称となる。
x=(1,2,i,2i), i²=−1が滑らかな例
（x_i²=(1,4,−1,−4)、e2=−17、c=−4、
j=111284641/50625）。
この点のquintuple全慣性H=C2³、
pointed H2全慣性A=D8×C2（位数16）。
源Hは変形座標(s,u,v)に同時符号(-u,-v)、
標的Aはu,vの独立な符号変更で作用する。
形式的な局所粗環は
source k[[s,a,b,c]]/(b²−ac), target k[[s,a,c]]、
粗忘却はa,cを固定する有限平坦次数2（分岐ac=0）。
source粗germに横断A1特異点が発生しtargetは滑らか。
stack忘却は点対象の忠実作用とBのsmooth atlasから
この交点でも表現可能étale。
SO表示ではλ=i、h=(13)(24)、g=i^{-1}DhD^{-1}
（D=diag(1,2,i,2i)）が追加位数2慣性を明示。
証明正本はC thm:qa-ou-double-torsion-intersection-local-modelと
rem:qa-ou-trace-zero-extra-stabilizer。
再現資産computations/verify_ou_special_reflection.py。
実施した独立検算は有理数上のquartic/Weierstrass恒等式・
j・二反射行列・有限抽象群計算で、全相対スタック証明の形式検証ではない。
**残る課題**はj=0,1728、noncubic境界、相対ruling mutationの全降下、
global coarse/good moduliの存在。局所粗同型を大域に延長したと主張しない。

**次の核心：** 特殊cubicのη−δ∈E[2]・δ∈E[2]・
j=0,1728等のruling交換固定点と慣性増大を調べる。
滑らかな二捩れ座の局所粗分岐は確定。次はj=0,1728の楕円追加自己同型とnoncubic境界でのfiber・正規形・有限性、相対ruling mutationの延長を監査する。

**複素乗法点の二cubic開と一cubic例外（Cで証明）。**
滑らかな許容楕円四つ組の差η,δがδ≠0、η∉{0,δ,2δ}を満たすなら、
Aut(E,0)がC4（j=1728）またはC6（j=0）に拡大しても、
η,δの同時固定や(η,δ)↦(2δ−η,δ)のruling交換を生む
ε≠±1は存在しない。
ε=±iではker(ε−1)=ker(ε+1)は位数2なので
η=δまたはη∈{0,δ}を強制して許容性に反する。
位数6のεはε−1がunitでδ≠0に反し、
位数3のεでは1+ε=−ε²がunitなので交換ならη=δ、
三束保存ならker(ε−1)≅C3の非零二点がη=2δとなり
二cubic開から外れる。
従ってjを除外せずにruling交換の必要十分条件
δ∈E[2]またはη−δ∈E[2]が成立し、
既存の片側反射・粗二重分岐・交点A1局所型もCMに拡張した。
ただしjはCM点の局所座標ではない。
Legendre E_λ:y²=x(x−1)(x−λ)のフルlevel2をétale局所に選び、
λを曲線変形座標にする。j(λ)=256(λ²−λ+1)³/[λ²(λ−1)²]で、
j=0は3重、j=1728は2重の分岐を持つ。
証明はCのlem:qa-ou-cm-no-extra-two-cubic-automorphisms、
lem:qa-ou-cm-level-two-deformation-coordinate。
一次資料Silverman, Arithmetic of Elliptic Curves, III.10.1（1986）を確認。

**一cubic境界のfiber一点とA4例外。**
η=2δ、δ∉E[2]なら最初の三束は相異なりcubic。
R(η,δ)=(0,δ)は第一二線束が一致するためnoncubic。
Bの二normalized foundationの全充満性により、
pointed自己同値は唯一のcubic foundationを保つ。
従ってquintuple→H2の2-fiberは自明慣性の一点。
点曲線のfully faithful coh(E)包含により慣性射は単射、
Bのsmooth相対次元零と合わせて忘却はこの点でétale。
一般二cubic locusのfiber二点とは異なるため、
一cubic境界を越えて有限étale次数2を維持できない。
これは分岐ではなく第二sheetがnoncubic foundationへ移る現象。

特にj=0、ρ位数3、0≠δ∈ker(ρ−1)≅C3、
η=2δの例では源・標的の全pointed慣性は
E[2]⋊C3≅A4（位数12）、幾何2-fiberは一点。
E:y²=x³+1、δ=(0,1)、η=(0,−1)が明示例。
E_a:y²=x³+ax+1の3次元変形(a,u,v)上で
有効C3は(ζ³? の記号は使わず)重み(2,1,1) mod3、
すなわち(a,u,v)↦(ζ²a,ζu,ζv)で作用する。
E[2]は変形差を固定するため接作用が自明。
局所粗形式不変式環はk[[a,u,v]]^{C3}で孤立巡回商型1/3(2,1,1)。
論文Cのprop:qa-ou-cm-jzero-one-cubic-a4、
cor:qa-ou-cm-a4-tangent-representation、
cor:qa-ou-one-cubic-fiber-and-nonfinitenessが証明正本。
有限群・Legendre恒等式の検算資産：
computations/verify_ou_cm_automorphisms.py。
この例は*一cubic境界*の現象であり、全H2のnoncubic locusの分類ではない。
Artin形式変形の二normal foundation持上げとmutation交換は解決。次はこれを有限型非被約基底に代数化し、full noncubic境界とのgroupoid比較を完成すること。

**全H2の二normal ruling有限étale選択被覆とfinite foundation開（Cに証明）。**
Bの全H2 smooth atlas U→H2は各成分でfull flat normal foundation
E^X=(O,X,M,Z)を持つ。相対mutation τは
E^Y=(O,Y,M,Z')を任意基底変更と可換に与える。
二者は互いに直交し、Ext^{≠0}(X,X)=0、RHom(X,Y)=0。
R=U×_{H2}U上の普遍pointed exact同型φについて、
P=RHom_R(φ(p1*X),p2*X)はperfect・derived base-change可能で、
全幾何fiberはk[0]または0。perfect性と導来fiberのTor振幅から
Pは局所的にrank1 vector bundle[0]または0へ簡約される。
従ってRは開閉部分R_same⊔R_swapへ分裂し、
三重重なりの二択の置換は代数的なS2-valued cocycle。
U⊔U→Uをこのcocycleでfppf降下させると
representable finite étale次数2のH2^{rul}→H2を得る。
全cubic/noncubic・任意の有限型非被約基底に有効。
そのS2商は全H2である。
一次入力：Stacks Project Tag 0BLY (Lemma95.6.1)、Bの
thm:global-h2-smooth-finite-typeとprop:relative-ruling-involution。
証明正本C thm:qa-global-two-ruling-etale-cover。

**有限foundationスタックの実現可能開。**
BのF0=[U0/(G/K)]は滑らかな有限型3次元Artin stack。
H2^{rul}上の選択四項foundationのEnd代数は
flat rank24でU0のopen minor条件を満たし、
頂点基底の変更・比較同型のスカラーKを剛体化して
Xi:H2^{rul}→F0の相対射を得る。
finite foundation代数同型は相対逆dualizingとorbit Homで
全次数の反Serre環とその二次関係を同一視する。
Bのprop:relative-h2-stack-recognitionの
Phi:H2→[X3/PGL9]の全忠実性からpointed exact同型を唯一復元し、
前段の開閉cocycleで選択foundationを保存することも確認する。
よってXiは相対groupoidで全忠実、monomorphism。
Bのthm:artin-foundation-lift/lem:foundation-artin-deformationと
実際のcubic・commutative・noncubic étale有効chartから
pointed Abel Artin変形とfinite foundation Artin変形が
指定還元・Hom基底・同型を含めて同値となる。
従ってXiは形式的étale。
局所有限表示かつrepresentableなのでétale、
étale monomorphismなのでopen immersion
（Stacks Tags 0616,05W4）。
像W=F_Hはτ不変なopenで、
H2^{rul}≅W、全H2≅[W/S2]⊂Q_fndとなる。
証明正本C thm:qa-intrinsic-h2-open-in-foundation-stack。
**証明状態：** C本文に相対下降・Artin効果性の証明を記載。
Bの相対理論自体の全証明の独立再監査、実LuaLaTeX、
形式証明器検証は未実施。さらにXiがすべての非被約基底で
厳密にfully faithfulとなるためのKスカラー2-cocycleと
相対Morita exactnessの細部を独立再点検する価値がある。
ここで証明した開の**明示的有限判定**は未解決：
relative Serre root、AS4被覆、AZ/Noetherian性など
有限個の検査可能条件へ還元する必要がある。
一cubic境界ではquintuple忘却fiber1でもnormal ruling選択coverは2。
両者を混同しない。

**実現可能開の有限方程式の存在と二重被覆の非自明性。**
F_H⊂F0の逆像W_H⊂U0⊂A^64は不変開部分。
閉補集合のA^64での閉包のイデアルIはNoether性で有限生成。
従って有限個の多項式P_iが存在し、W_H上では少なくとも一つが非零、
補集合は全P_iの共通零点。代数群G/Kの有理作用により
Iは安定で、生成元を有限次元のG/K部分表現に取れる。
これは存在結果だけで、P_iの具体式・次数・計算量は未知。
C cor:qa-realizable-foundation-finite-open-criterionを参照。
可換Q=P1×P1ではpointed自己同値群が
A=(PGL2×PGL2)⋊C2、指定rulingを保つH=PGL2×PGL2。
ruling選択被覆をその慣性gerbe BAへ引き戻すとBH→BA、
非自明な剰余C2が二sheetを交換するため、大域sectionはない。
C cor:qa-ruling-cover-nontrivial-commutative-gerbeに証明。
この二点を実現可能開の明示的判定と混同しない。

**cubic geometric四重テンソルの具体的有限判定。** Fが同型でGが全射のnormal foundationでw∈⊗_{i=0}^3V_iを復元。各隣接2因子の4×4 flattening M_iについて、ker(M_i)に分解可能テンソルがないことがgeometric性。rank4ならdet M_i≠0、rank≤2ならprojective kernelは線を含みSegre quadricと交わるので不許容、rank3ならadj(M_i)の非零列がkernelを張るので、列の2×2 reshapeがfull rankであることが必要十分。detは次数4、adj列2×2detは次数6。四つのiごとに1+4式、計20個の明示非消滅判定。基底変更の下でも不変。C lem:qa-explicit-cubic-geometric-adjugateが証明正本。整数でrank3 entangled/decomposable, rank2, rank4と一般/退化wを検算。computations/verify_cubic_geometric_adjugate.pyを標準math suiteに登録したが、保存スクリプト自体の実行状態と独立数学的全証明監査は別。

**中心の三者対応（O-marked／potential／反標準avatar）。**
最優先研究目標は体上同型類の明示的全単射、または
相対モジュライ射の構成。avatarはY=Σ0又はΣ2、
D∈|-K_Y|（非被約も含む）、P∈Pic0(D)。
potentialには8/10/12矢・trivial pairを許す表示を使う。
個々のGIT慣性・有限minorはこの対応に必要な時だけ優先する。

**滑らかな楕円cubicで得た明示全単射。**
VdBの三線束 L0,L1,L2（各deg2）から
F_s=L2、G_s=L1 L2 L0^{-1}、P=L2 L0^{-1}。
逆 L0=F_sP^{-1}、L1=G_sP^{-1}、L2=F_s。
F_s≠G_s、P≠O、P≠G_s/F_sが必要十分条件。
これらの同型類が対応し、選んだcubic normal foundationを表す。
二rulingともcubicとなる条件 G_s/F_s≠P² の下、
Rがr1(F_s,G_s,P)=(G_sP^{-1},F_sP,P)となる。
r1²=1、O-marked同型類はavatar同型類のr1商。
r0(F_s,G_s,P)=(G_s,F_sP,P)はhelix shift、
一般に構造対象Oを変えるため割らない。
特殊自己同型点は固定軌道を許す。
C thm:qa-elliptic-vdb-square-avatar-bijection、
thm:qa-elliptic-avatar-pointed-quotientに証明。
OU effective potential→quintuple一般4枚、
quintuple↔square avatar、avatar→O-marked一般2枚、
従って一般potential→avatar4、→O-marked8。
C cor:qa-ou-potential-square-avatar-pointed-degrees。
これはPicard平方根4個の新しい標識を数えたものではない。

**滑らかな楕円noncubicの稠密境界。**
wall G_s=F_sPはsmooth avatar同型類で2次元、
内在noncubic境界は1次元。無条件の
quasi-finiteな同型類射は不可能。
非零P∈Pic0(E)[2]を課すと1次元。
F_sの二重被覆π_F:E→P1の四分岐点に対し
Pが定める非零2torsion translationが二組の
二点集合を作る。
逆に互いに素な二つの二点集合B1,B2に対して
四分岐点の二重被覆E、F_s=π*O(1)、
指定分割に対応する非零Pを復元。
Legendre B1={0,∞}、B2={1,λ}なら
y²=x(x−1)(x−λ)、translationは
(x,y)→(λ/x,−λy/x²)。
これはBのnoncubic全根対分類と合成して
**四根相異なるO-marked noncubicの同型類**
との全単射。指定AS10 mutation・一番頂点で実現したavatar側の
pointed AS heartは $\chi^\vee=\chi/(\chi-1)$ の対象であり、
元と一致するのは $\chi=0,2$ に限られる。
C thm:qa-avatar-two-torsion-root-pair-bijection と
thm:qa-spectral-avatar-pointed-involutionを区別する。
共有根・一致根対については以下のspectral曲線・Picard境界で幾何同型類全単射まで完成（相対Picard線束射とは区別）。

**二つの別のwallと古典点。**
η=G_s/F_s、δ=Pとするとη=2δは
最初がcubic・r1後がnoncubicの一cubic境界。
η=δは最初もnoncubic、Σ2十本矢に移る壁。
P=O_Dを全Dで許すと四線束の前向きHom/積は
元の可換Σ0上のcollectionのものと同じで
Dの選択が消える。古典点の収縮が必要。
Σ2の古典weighted stackはstrong H2に無条件には入らない。
C prop:qa-avatar-walls-and-noncubic-dimensionと
prop:qa-avatar-zero-picard-collapse。

**全noncubic根対のquartic resolventとsquare avatar幾何同型類（Cで証明）。**
二つの非退化二次形式の非順序対{f1,f2}からq=f1f2を作る。
全Sym²(P(Sym²W*))→P(Sym⁴W*)は有限全射・一般次数3。
monic q=x⁴+ax³+bx²+cx+dでは分割を表すcubic resolvent
z³−bz²+(ac−4d)z−(a²d+c²−4bd)=0（既知古典理論、
Cremona1999 Section4.3を一次資料確認）。
f_i squarefreeの条件下の三型：
(1,1,1,1) smooth genus1、(2,1,1)既約nodal genus1、
(2,2)二P¹が二節点で交わるI2。全部 connected Gorenstein p_a=1。
C_q:y²=q→P¹を取りF_s=p*O(1)。
smoothでは非零P∈Pic0(C_q)[2]が三個、quartic根の三分割に対応。
nodal・I2ではPic0(C_q)≅Gmなので非零2torsion P=-1が
唯一、squarefree二根対分割も唯一。
G_s=F_sPの完全線形系は全三型で(2,2)閉埋込みを与え、
{非順序二つのreduced二点因子}/PGL2 と
{smooth/nodal/I2のsquare(2,2)反標準因子D、
P=G_sF_s^{-1}≠O,P²=O}/isomの全単射。
さらにBの根対↔H2 noncubic分類を合成して全noncubic
O-marked幾何同型類のavatar分類を得る。ただしこの集合対応は
smooth域の指定AS実現と一致せず、後者は $\chi^\vee$ を与える。
nodalのnormalized t模型 X=t²,Z=(1−t²)/t ⇒ XZ²=(1−X)²；
I2の模型は(Z−X)(Z+X)=0。
正本C thm:qa-noncubic-rootpair-quartic-resolvent、
thm:qa-noncubic-rootpair-all-geometric-square-avatar-bijection、
rem:qa-singular-square-avatar-explicit-models。

**全noncubic根対からの相対torsion-free spectral射とPicard非延長。**
B_f=k[u,v]〈c,d〉/(c²−f1,d²−f2)の可換化の点曲線
E_f=Proj k[u,v,c,d]/(c²−f1,d²−f2)はP¹上四重被覆。
同時符号(c,d)↦(−c,−d)の商はC_q:y²=f1f2、
y=cd。反不変module M=(r_*O_{E_f})^-はC_q上rank1
torsionfree degree0、p_*M=O_{P¹}(-1)^2、
yc=f1d,yd=f2c、行列A=[[0,f2],[f1,0]]はA²=f1f2 I。
このデータはBのnoncubic二形式表示[P/G]の全相対基底変更に
両立するため、finite double coverとtorsion-free sheafの
相対群oidへの射を与える。smoothならMはP≠O,P²=Oで
以前の分割に一致。共有根ではnodalのnodeでM非局所自由、
一致根対ではI2の二節点で非局所自由。
具体例f1=x(x−1),f2=(x−s)(x−2), s→0の
全空間の完成環A=k[[x,s,y]]/(y²−x(x−s))
≅k[[c,d]]^{±}はA1表面特異点。
反不変M=Ac+AdはMCM/reflexive rank1だが最小生成元2で非自由。
特殊C0は既約Cartier(div(s))なので、
generic M_Kを延長するreflexive sheafとの差は特殊fiber整数倍
（主因子）に限られ、可逆な延長Lは存在しない。
従って**特異fiberでP=-1を選ぶ幾何同型類の全単射は、
滑らかなP_tからの通常Pic0 line-bundle相対射としては実現できない**。
この局所Picard障害だけでは別模型を排除しないが、
指定spectral-pointed対応にはさらにH2族への延長不能が成立する。
境界比較はH2外の適切な標的で扱う。正本C
thm:qa-noncubic-rootpair-torsionfree-spectral-module、
cor:qa-noncubic-central-square-point-curve-spectral-avatar、
prop:qa-rootpair-nodal-picard-nonextension。
計算的検算：SymPyでquartic resolvent根、A²=qI、
singular quartic q、nodal(2,2) parametrization、接方向を独立に確認。
verify_rootpair_resolvent_spectral.pyはmath suiteに登録し、
現行保存コードを実行PASS。
以上はAS avatar由来のnoncommutative qgrとO-marked心の同値証明ではない。

**Σ₂での全noncubic分類を証明：** 負断面Sを避ける反標準因子D∈|−K_{Σ₂}|と0≠P∈Pic⁰(D)[2]の幾何同型類は、全noncubic O-marked quadricの幾何exact同型類と全単射（C thm:qa-all-noncubic-sigma2-anticanonical-avatar-bijection）。H=O(h)|D=F²、F=O(f)|Dを用いるsquare換算はF_s=F,G_s=FP。P非自明2捩れによりDはsmooth、既約nodal、二P¹二節点(I2)の三型だけ。Bの良moduliでχ=1に重なる一根共有と根対一致も、Σ₂のnodalとI2で区別（C cor:qa-sigma2-avatar-separates-special-noncubic-classes）。これは**体上の同型類全単射**で、avatar AS代数の元のqgr heartとO-markedの直接同値、非被約底の通常Pic⁰線束を使う相対射ではない。

具体式：Σ₂でH=O(h)|D、F=O(f)|DとするとD∩S=∅よりH=F²。square←Σ₂はF_s=F,G_s=HPF^{-1}=FPで、逆はCの相対幾何変換T^{-1}。p:D→P¹は有限平坦二重被覆、p_*O_D=O⊕O(-2)。非零二捩れがある場合、quartic qの四単根・一重複・二重複二点だけが許される。cuspidal・tacnodal・double sectionのPic⁰は加法型で2捩れは自明。良moduli χ=1の共有根と根対一致はDの既約nodal/I2として区別。この集合対応を元AS代数の心の同定や相対Pic⁰同値として扱わない。

**再開点と主張状態。**
cubicのVdB-square-O-marked対応に加え、全noncubic根対と
nodal/I2を含む2torsion square avatarの幾何同型類全単射、
noncubic線形代数からtorsion-free spectral avatarへの相対射、
共有根A1での通常Pic0線束延長不能をCに証明として統合。
E_f側の相対pointed認識、smooth spectral指定pointingの二同種対合、
二境界でのH2延長不能は証明済み。残るのはsmooth対応の同型層・慣性・降下、
別のrotated pointing、H2外のtorsion-free境界標的、
古典零切断・Σ2最深境界、8/10/12矢potentialの全相対群oid。
旧Q12 avatar草稿・synthesisは内部未公刊入力で、
論文Cに必要な証明を統合していく。
関連出典はnotes/literature.md。A/Bの主結果の独立再監査・
CのLuaLaTeX組版・新規性調査も未完了。
検算はcomputations/verify_avatar_pointed_dictionary.py
（GitHubの保存コード本体実行はまだ未確認）。

**H2忘却の構成済みの範囲。**
非線型geometric quintupleの普遍cubic Z代数Dから
C_ij=D_{-j,-i}を作り、Bの
prop:general-cubic-canonical-tails・
thm:geometric-cubic-relative-effectivityと
Picard étale根構成を使うことで、根を選ばずに
(qgr C,π e0C)∈H2を与える相対群oid射がある。
Gm⁴の中心スカラーは頂点共役としてpointed恒等となり、
剛体化表示スタックはsmooth純3次元でH2の同次元。
四つのPicard根は同じpointed対象のwitnessであり
四つの異なるH2対象ではない。
剛体化後の一般開の慣性・微分・pointed fiber、および滑らかな二捩れ特殊座の局所粗型は決定した。非線型geometric以外の境界の全相対比較は未完成。

**再開する数学的核心。**
全H2のnormal ruling選択被覆とfinite foundation表現開への開埋込はCに証明を記載した。次は相対Isom/K剛体化/Artin効果性を独立に監査し、実現可能開Wを計算可能な有限条件で決める。一般のpointed忘却は表示スタック→H2でsmooth相対次元0、
正則半単純開で有限étale次数2・慣性μ₂²同型・KS同型となる。
さらに稠密開のcanonical S₂ deck商を取れば内在H2そのものに同値。
片側・交点の二捩れ特殊座での局所慣性と粗分岐に加え、j特殊値の二cubic開でのCM障害除去と一cubic境界fiber一点・A4例外を解決。点曲線側のnoncubic相対復元とsmooth spectralのgerbe比較は証明済みであり、自然なspectral射の境界標的・全fiberは証明済みであり、次は一般avatar族のpointed認識と全AS/QPの比較を調べる。粗分岐とstack的étale性の区別を保つ。
`lem:elliptic-two-reflections` と
`cor:two-intrinsic-foundations` の相対化が最も具体的な手掛かり。
A/Bの全公表前監査・一次文献新規性比較・三稿の実組版は未完了。

## 一致類の全慣性・AHR形式対・局所good moduliの二次的性質

**AHR適用の全仮定。** 一致根対の閉gerbe
$\mathcal G=BH_{\mathrm{eq}}$は内在的H2の閉点で、
内在スタックは有限型smooth Artin・affine diagonalを持つ
（Bの thm:global-h2-smooth-finite-type）。
$H_{\mathrm{eq}}$の連結成分は$\mathbb G_m$、非連結成分は有限群で、
標数零なので**全安定化群**が線型簡約。
AHRの刊行一次PDF（Annals of Mathematics 191 (2020), 675–738,
Theorem1.2、印刷p.676）を直接確認した：
smooth closed point、linearly reductive stabilizer、
quasi-separated finite-type Artin stack with affine stabilizersの下で、
$V=\operatorname{HH}^2$のGIT商$V/\!/H$へのaffine étale近傍$U$と
\[
 [W/H]=[V/H]\times_{V/\!/H}U\longrightarrow\mathfrak H_2
\]
のétale射が得られ、affine diagonalなら後者もaffineに取れる。
$H$はsmoothなのでnormal representationは
$\mathfrak H_2$の点の一次変形空間$V$に一致する。
この適用範囲からZariski開のgood moduli降下を結論してはいけない。

**境界を含む形式対。**
Bの prop:noncubic-coincident-full-normal-representationでは
$V=V_{\mathrm b}\oplus V_{\mathrm n}$、
境界方向$(a,c)$のトーラス重みは$(2,-2)$、
法方向$(x,y)$では連結トーラスは自明。
有限生成元$e_1,e_2,r,\tau$は前論文Bの表の通り作用する。
$\mathfrak N$はsmoothな余次元二の閉部分なので、
sliceの完備局所環においてH安定な境界イデアル$I$と
極大イデアル$\mathfrak m$の余接完全列を得る。
Hの線型簡約性でI内の法余接liftと境界方向liftを
同変に選び、$(a,c,x,y)$をregular parametersにできる。
その結果、形式的な対は
$([\operatorname{Spf}k[[a,c,x,y]]/H],
 [\operatorname{Spf}k[[a,c]]/H])$、
境界は$x=y=0$となる。
これは有限次数の接表現だけからの類推ではなく、
AHRのétale sliceと同変正則座標の持上げを使う。

**全群の三つの二次不変式。**
$w=ac$, $p=(x+y)^2$, $q=(x-y)^2$は、
連結トーラス・法同時符号・反射r・ruling交換τの
全生成元によって保存されることを
SymPyの多項式代入で独立確認した。
三元のJacobianのgeneric rankは3であり、
$k[V]^{H_{\mathrm{eq}}}=k[w,p,q]$は
三元の多項式環である（証明はBの
cor:noncubic-coincident-polynomial-invariants）。
四変数を次数1とすると三生成元はすべて二次、
Hilbert級数は$(1-z^2)^{-3}$であり、
原点のgood moduli射の微分は零。
それでも商原点はsmoothな三次元点である。
境界では$p=q=0$、$\chi-1=4w/(1-4w)$で
滑らかな一次元軸に対応する。
この局所計算は形式線型化の有効性と
global good moduliの存在を同一視するものではない。
現行計算のassertionは
computations/verify_noncubic_boundary.py に統合した。
ただし現行全スクリプトのローカルcheckout実行は未実施であり、
今回独立に実行したのは各四つの群作用の多項式恒等式、
Jacobianの非零minorとHilbert数値の確認までである。

**次の数学的課題。** AHR共通étale近傍上のgood moduli射を、
$\mathfrak H_2$のZariski開へ降下できる条件を検討する。
同時に一般cubicのOkawa–Ueda GIT表示から内在H2への
根・四窓・rulingを忘れる射の相対fiberを、
境界と慣性を保って比較する。
A/B公表前の三稿source checker・LuaLaTeX組版、
先行研究との包括的新規性確認、全証明独立監査も残る。

## noncubic 被約境界の相対商・慣性・good/coarse 比較

**幾何点から相対groupoidへ。**
$\mathfrak N=(\mathfrak H_2\setminus\mathfrak V_{\rm cub})_{\rm red}$、
表示商$\mathfrak N^{\mathrm{pres}}=[P/G]$はsmooth純次元1。
Bの thm:noncubic-intrinsic-presentation-equivalence は
幾何点分類だけでなく、char0の相対慣性（有限型群スキームのsmooth性）、
Lagrangian境界smooth chartの二形式族への実際のétale相対標準化、
相対tilting・Serre自然性から全反Serre軌道環の同型、
AZ再構成でのpointed exact同値、
接空間の全射と同次元smooth性からのrepresentable étale性、
幾何groupoidの同値からStacks Tag0DUDによる同型、という順で証明する。
全ての非被約testについての結論は、
この相対**代数スタック同型**から従う。
各命題の出典はBの同節である。

**標数零が本質的。**
char$p>0$の$B\alpha_p\to\operatorname{Spec}k$では
全代数閉拡大体上の抽象自己同型群は自明だが、
相対慣性群スキーム$\alpha_p$は非自明。
従って抽象自己同型群の幾何点での単射性から
representabilityを導くchar0補題は正標数へ拡張できない。
Bの rem:charzero-inertia-faithful-necessity に明示した。

**一致根対の局所形式不変式。**
$f_1=uv$、$f_2=au^2+uv+cv^2$、$1-4ac\ne0$とし、
残余慣性の連結トーラスは
$(a,c)\mapsto(t^2a,t^{-2}c)$と作用する。
有限成分は二つの方向の交換と同時符号変更で積$ac$を保つ。
この二変数の形式的接表現の不変式は$k[[ac]]$である。
good moduli座標$\chi=1/(1-4ac)$に対して
$\partial_a\chi(0)=\partial_c\chi(0)=0$、
$\partial_a\partial_c\chi(0)=4$を
SymPy厳密式で独立確認した。
境界stackの接空間は二次元、慣性Lieは一次元で局所次元1。
good moduliの微分零から境界接空間の消滅を推論しない。
相対同値の接全射性は二形式族へのsmooth chart因数分解に基づく。
内在スタック全体の形式模型は別のAHR線型化定理で扱う。

**goodとcoarseの比較と実際の障害。**
$k[P]^G=k[\chi]$により表示商全体の
$\chi:[P/G]\to\mathbb A^1$はgood moduli。
固定第一形式$uv$では
$\chi=b^2/(b^2-4ac)$であり、
$\chi=\xi$のfiberは
$(1-\xi)b^2+4\xi ac=0$かつ$\Delta\ne0$。
$\xi\ne0,1$ならsmooth、$\xi=0$は二重Cartier divisor、
$\xi=1$は$ac=0$のreduced node。
$P$は整で$\chi$非定数なので$k[P]$は
PID$k[\chi]$上torsion-free、従ってflat。
一致根対の閉gerbeを除くDM開は、
局所的な有限商
$[\mathbb A^1_x/\mu_2]\to\mathbb A^1_\chi$、
$\chi=x^2$を持つ。
任意基底変更$\chi\mapsto s\in A$後も
$A[x]/(x^2-s)=A\oplus Ax$、
$\mu_2$不変式は$A$（標数零）なので、
任意基底変更に両立するcoarse moduliを与える。
Stacks Tags0DUP/0DURの一般のuniform categoricalは
通常flat base changeの主張であり、
任意basechangeへの拡張はこの具体的な有限商の再計算から示す。
DM開はgoodではなく、比例する二形式の余次元二の閉部分を
normal affine$P$から除いた非affine$P^\circ$の非affine性と
cohomological affinenessにより反証する。
またDVR族$f_1=uv$, $f_2=(u-v)(u-t^2v)$上の
一般fiber慣性$A_t$は$\det A_t=-t^4$かつ
係数に単元1を持ち、$\operatorname{PGL}_4$のDVR点へ延長できない。
この行列式と二形式を$t^2$倍する作用をSymPyで独立確認した。
従ってDM開の慣性はproperでない。
全H2の粗空間不存在は別の穿孔直線の特殊化で示す。
以上の式の検算と、普遍的coarse性・相対groupoid同値の
全証明の形式検証を混同しない。

**次に点検すること。**
一致類の全慣性とAHR形式局所模型の仮定・不変式は本ノート冒頭へ統合した。
次は局所good moduliのZariski降下と一般cubic GIT表示との比較を研究する。
A/B/C全source checker・LuaLaTeX組版、全証明独立監査は未実施。

## 指定 Artin 同型の持上げとsmooth atlas・framed実現

**smooth性の独立判定。** 相対反Serre再構成による全忠実な
$\Phi:\mathfrak H_2\to\mathfrak P=[X_3/\operatorname{PGL}_9]$
と$\mathfrak P$のaffine有限表示対角が入力となる。
有限型$U\to\mathfrak H_2$について、局所Artin環のsmall extension
$A'\twoheadrightarrow A$で指定された
$u_A\in U(A)$、$c_{A'}\in\mathfrak H_2(A')$、
pointed exact同型$\alpha_A:q(u_A)\simeq c_{A'}|_A$を
両方とも指定還元に沿って持ち上げられるなら、
\[
 Z_T=U\times_{\mathfrak H_2}T
 \simeq U\times_{\mathfrak P}T
\]
は全有限型affine$T$について有限型スキームとなる。
$k$は代数閉体なので$Z_T$の閉点の剰余体は$k$であり、
Stacks Tag 02HYのArtin小拡大判定を各閉点で適用し、
smoothでない点の閉集合が空であることを得る。
これがBの新しい lem:pointed-artin-lifting-smooth-bridge である。
現時点で全$\mathfrak H_2$の代数性を前提とせず、
開像は$R=U\times_{\mathfrak P}U$によるsmooth groupoidの商となる。
単なる対象のArtin持上げや接次元の一致からsmoothを結論しない。

**De Deken–Lowenの原文。** J. Noncommut. Geom. 5 (2011)
pp.501–502のDefinition5.12、Theorem5.13(1)–(4)を一次PDFで確認。
geometric (4,3)-helixの各対象が$D^-_{\mathrm{ffd}}$に属し、
元の基底からのflat Grothendieck変形があることが入力。
(1)はhelixの一意な持上げ、(2)はflat heart対象の持上げ、
(3)はstrong性と四項窓内のHomの平坦性、
(4)はgeometric性と全前向きHomの平坦性を述べる。
BのArtin持上げ補題では、対象とHomの指定還元基底を延長して
有限foundationの座標を復元し、étaleな$U\to S$から$u_A$を延長する。
持上げた窓のMorita同値は相対Serreと反Serre環を保つため、
$\Phi$の全忠実性で指定された$\alpha_A$へ還元するexact同型を回復する。
導来同値一般を無条件にheart-exactとしていない。

**非cubic chartとframedの数値。**
noncubic chart $U_x$は$\mathbb A^{64}$の開のétale近傍、
全$\mathfrak H_2$の局所次元は原稿主定理で3。
従って$q_x$は相対次元61、
$R_x=U_x\times_{\mathfrak H_2}U_x$は125次元。
他方$X_{\mathrm{as}}$は$\operatorname{PGL}_9$-torsorにより
スタック上相対次元80、総次元83となる。
この二つのrigidificationを混同しない。
Stack Tag 05W6のlocally finite type monoからunramified・
separated・locally quasi-finite・representableが従うこと、
Tag 03XXにより代数空間からスキームへのそのような射で
始域がスキームとなることを確認した。
有限型monoを無条件にopen immersionとはしない。
一致根対のambient非開性はBの主張のまま保持する。

**状態・次の課題。** 今回は原稿Bの可換・cubic・noncubic
smooth atlasのArtin持上げ→smooth性を共通補題へ統合した。
B相対認識節末尾の全Artin・framed結果の誤ったAへの引用を、
B内部の正しい定理・系へ訂正した。
変更対象4節のTeX環境バランスと補題引用の静的点検はPASS。
31分割節の一括GitHub取得検査は接続側の操作数上限で未実施、
全checkerとLuaLaTeX組版、全数学的証明の独立監査も未完了。
noncubic境界の相対groupoid・慣性・good/coarse moduliは
本ノート冒頭の現行整理に統合した。
次は一致根対の形式局所AHR線型化と全非連結慣性を検証する。

## 同じ Serre 根の中央 AS4 被覆：有限条件から全次数へ

論文Bの lem:spread-local-central-hull の入力は、
有限型基底上の相対Koszul軌道環$B$、
$E=B^!$の全次数projectivity、特定点の局所環で
**実際に選んだ同じSerre根に対応する**中央正則二次元
$\phi_{\mathfrak p}\in(E_{\mathfrak p})_2$、
および$P_{\mathfrak p}=E_{\mathfrak p}/(\phi_{\mathfrak p})$の
Frobenius階数列$(1,4,6,4,1)$である。
別のrootの中心二次元を仮定から無断で取り込まない。

相対Koszul性と$\operatorname{rank}B_n=(n+1)^2$から
\[
 h_B(z)=\frac{1+z}{(1-z)^3},\quad
 h_E(z)=\frac{1}{h_B(-z)}=\frac{(1+z)^3}{1-z}.
\]
$E_n$の階数は$1,4,7,8,8,\ldots$。
$\phi$が正則なら
$(1-z^2)h_E(z)=(1+z)^4$となり、
$P$は$(1,4,6,4,1,0,\ldots)$、双対$A=P^!$は
$h_A(z)=(1-z)^{-4}$を持つ。
この三角のHilbert恒等式はPythonの整数係数で第12次まで独立検算した。
数値の一致単独で正則性やKoszul性を証明したとは主張しない。

有限型延長の核心は、
(1) $\phi_{\mathfrak p}$を$E_2$から一つの主開へ延長し、
一次生成空間$E_1$との有限個の交換子を同じ主開で零にする。
(2) $P_n$ ($n\le4$)の局所自由性、$P_5=0$と
Frobenius pairingsの非退化性は有限個の開条件。
$P$は次数一生成なので$P_5=0$は$P_{\ge5}=0$を含意する。
(3) 補題 lem:spread-central-regular-line により、
$E$は中央変数$t$（$\deg t=2$, 作用は$\phi$）の
多項式環$R[t]$上で、$P_0,\ldots,P_4$のliftから有限生成される。
核$K=\ker(E(-2)\xrightarrow{\phi}E)$もNoetherianな$R[t]$上有限生成。
$K_{\mathfrak p}=0$から有限個の生成元の分母を同時に払えば
一つの主開で**全次数の核**が零。
(4) 各短完全列はprojectiveな$P_n$により基底上分裂するため、
任意の非平坦基底変更後も中央正則性が保たれる。

Koszul性は別入力を要する。
全幾何fiberの$E$は先に相対Koszul性からKoszulと分かり、
$\phi$は中央正則二次元と分かったので、
Shelton–Tingey, J. Algebra 241 (2001), 789–798,
doi:10.1006/jabr.2001.8781の
「Koszul代数のregular normal quadratic quotientはKoszul」
を適用する。刊行版のabstractでこの定理の内容を確認した。
次に相対Koszul変形原理とFrobenius pairingで
$P$と$A=P^!$の相対Koszul/AS4型を得る。
$\phi$の中央性は$A$側の二次切断$g$の中央性を与え、
$A_{n-2}\xrightarrow{g}A_n\to B_n\to0$は
projectiveでHilbert階数が一致するため分裂完全となる。
Noetherian性は中央正則切断の次数有界なフィルトレーションから
$B[g]$へ帰着する。これらはBの証明本文を相互依存まで監査した結果であり、
関連するKoszul変形定理の全証明の独立再検証や形式証明ではない。

**再開重点。** finite-type局所族が実際の
内在的$\mathfrak H_2$の全公理を満たす段階で、
境界横断Artin持上げ、指定pointed同型のlift、
smooth finite-type atlasとX_asの降下を再検証する。
公開前の三稿sourceチェッカー・LuaLaTeX組版も未実施である。

## cubic二開と$I$進完備化による普遍Noetherian貼合せ

有限型Lagrangian認識開の基底$R$で
$a=\det M,\ b=\det N,\ I=(a,b)$とする。
$D(a)$では指定したrulingのgeometric cubic helix、
$D(b)$では変異した反対rulingの同様のhelixを使う。
ruling交換は偶数頂点$E_{2i}$と指定された二周期根$s$を
変えないので、両主開で使う偶数軌道環は同じ$C$の局所化である。
thm:relative-geometric-cubic-noetherianは、
全次数projectiveな相対cubic解消、四次syzygyと縮約同型、
全幾何fiberのgeometric quintupleという入力から
row/columnの普遍Noetherian性を導く。
相対point curve上の積を相対豊富な$H_i=L_iL_{i+1}$の冪と
各fiber成分で数値的に自明なnef prefixに分け、
Keeler2003 Theorem 1.5を用いて、全nef prefixに一様な
高次cohomology消滅を得る。
row idealの像層の昇鎖がNoetherian coherent層で安定した後は
固定有限presentationから全ての十分高い次数のidealを生成できる。
linear閉部分は別の相対Segre表示で扱う。
2018年の刊行Corrigendum（doi:10.1016/j.jalgebra.2018.03.024）は
元のLemma 3.3を訂正し、依存する定理を再検証している。
その一次刊行ページでこの範囲を確認し、原稿Bの書誌と引用へ追加した。

中央Cliffordの非被約閉部分$R/I$とcubic二主開$R_a,R_b$の
それぞれで、任意のNoetherian基底変更後の左右Noetherian性を持つ。
形式貼合せの thm:patch-noetherian は、固定内部次数での
$I$進完備化と有限生成の係数liftを使い、
$R\to\widehat R_I\times R_a\times R_b$の忠実平坦性で
元の各row/columnの有限生成を降下する。
$\bigoplus C_n\otimes_R\widehat R_I$を用い、
全内部次数の$I$進逆極限と無条件に同一視しない。
任意のNoetherian$R$-代数$T$にも$I_T=(a,b)T$を用いて
同じ三部分の証明を適用できる。
この点で「幾何fiberごとのNoetherian性」のみから
全体のNoetherian性を推論してはいない。

**残る監査。** 選んだSerre根と同じ中央AS4被覆を
有限型開へ延長する部分。局所中央線$\phi\in E_2$の
全次数正則性から、一つの主開上の正則性を得る
lem:spread-central-regular-lineでは、
$P=E/(\phi)$の$P_5=0$と次数一生成性により$P_{\ge5}=0$、
$E$が$R[t]$上有限生成、乗法核も有限生成となる。
全次数kernelを一つの分母で消す論理とFrobenius・Koszul双対の
基底変更は本ノート冒頭の中央AS4節に条件と依存関係を整理した。
次は相対H2のArtin持上げとsmooth finite-type atlasの効果性を点検する。

## 相対Clifford閉部分のPBWと普遍Noetherian降下

任意の可換係数環$R$、任意の中心二次式$f_1,f_2\in R[u,v]_2$について
$B=R[u,v]\langle c,d\rangle/(c^2-f_1,d^2-f_2)$、
$h=cd+dc$は中心元であり、$B$は中心多項式環
$R[u,v,h]$上の基底$(1,c,d,cd)$を持つ有限自由代数である。
独立な中央変数$h$を持つ表示において
$c^2\to f_1,d^2\to f_2,dc\to h-cd$はmonicな書換規則となり、
長さ三の全重なり$ccc,ddd,dcc,ddc$はそれぞれ
$f_1c,f_2d,f_1d,f_2c$へ両側から帰着する。
長さ+辞書式で終了するため合流し、任意の非被約係数環上でも
中心環の埋込みと自由基底が同時に証明できる。
原稿Bの lem:noncubic-relative-clifford-center に証明を保持する。
厳密記号計算は computations/verify_clifford_pbw.py にある。
この証明は二形式の判別式の可逆性を必要としない（ただし、
その後の$\HH$認識には必要となる）。

$R_0$がNoetherianなら、$B$はNoetherian中心
$R_0[u,v,h]$上有限なので左右Noetherian。
任意のNoetherian$R_0$-代数$T$でも同じ基底が残る。
有限個のaffine étale標準化$R_0\to R_\nu$が基底を覆い、
有限foundationの全indexed Homと相対Serre四周期が
標準族の対応するHomと*環族として*同定されるとき、
$\prod R_\nu$は忠実平坦で、任意のNoetherian底変更後も
有限積のaffine étale被覆であり続ける。
各row/columnの部分加群の有限生成性はこの忠実平坦な被覆から
有限個の頂点同次生成元を降下することで得られる。
補題 lem:closed-clifford-fpqc-noetherian に証明を保持。
幾何点ごとの同型だけでなく、閉部分環$R/(\det M,\det N)$
での実際の相対標準化が必要である。

元の全基底$R$での左右Noetherian性にはさらに
二つのcubic主開部分$D(\det M),D(\det N)$上の
既存のgeometric cubic Noetherian構成を用い、
thm:patch-noetherian の次数別$I$進完備化と
$\widehat R_I\times R_a\times R_b$ の忠実平坦被覆を組み合わせる。
閉・開の形式貼合せは本ノート冒頭に条件を整理した。
次は選んだ根での中央AS4被覆の全次数正則性を重点監査する。

## 非被約基底の幾何的rankとscheme-theoreticなnoncubic境界

論文Bの認識開 $W\subset\operatorname{LG}(4,8)$ 上で
$D=V(\det M,\det N)$ は、Bの
lem:lagrangian-boundary-transverse により
**基礎体上はsmoothな余次元二の閉部分である**。
したがって$D$自身を「非被約でもよい」と記述するのは正確でない。
一方で、$D$を非被約な一般基底へpullbackすると非被約な閉部分となり得る。
相対normal formをその基底上で適用するには$\det M=\det N=0$が
元として成立することが必要であり、各幾何fiberのrankが三であるだけでは足りない。

反例：$R=k[\varepsilon]/(\varepsilon^2)$ 上で
$M_\varepsilon=
\left(\begin{smallmatrix}
0&0&-1&-\varepsilon/2\\0&1&0&0\\-1&0&0&0\\0&0&1&-\varepsilon/2
\end{smallmatrix}\right)$,
$N=
\left(\begin{smallmatrix}
0&0&0&1\\1&0&0&0\\0&-1&0&0\\0&0&0&1
\end{smallmatrix}\right)$
は$M_\varepsilon^tN=N^tM_\varepsilon$を満たす。
特殊fiberの両射影はrank3、交点線の可逆性・二つのcross行列式の
開条件も成立する。しかし$\det M_\varepsilon=\varepsilon\ne0$、
$\det N=0$。cross行列式は$\varepsilon^2-1=-1$と$-1$となり、
したがってnilpotentな横断方向を持つ実際のLagrangian変形である。
本文の ex:lg-nilpotent-transverse-determinant に完全な行列を保持し、
computations/verify_lagrangian_recognition.py に正確な記号計算を収める。

これは**境界と横断変形を識別する具体例**であり、
普遍Noetherian貼合せの反例ではない。
貼合せ自体は$I=(\det M,\det N)$による
scheme-theoreticな閉部分$R/I$と、開部分$R_a,R_b$を使うため、
この例の存在と整合する。
R/I上のétale相対標準化、Serre四周期からの全indexed Hom比較と
Noetherian性のfpqc降下は本ノート冒頭とBの対応補題に整理した。
次は二つのcubic主開での一様Noetherian性と$I$進貼合せを点検する。

## Lagrangian 正規形の cross reshuffling に関する符号と開条件

有限型chartの全幾何点認識に用いる
$\operatorname{Cr}(M)_{ka,bc}=M_{ck,ab}$ という縮約では、
行を$(k,a)$、列を$(b,c)$の辞書式で並べる。
両射影rank3の標準Lagrangian四平面を
$(-E_{21},\alpha E_{12}+\gamma E_{21})$、
$(E_{12},\beta E_{12}-\alpha E_{21})$、
$(-D_0,0)$、$(0,I_2)$で生成させると、
$\alpha^2+\beta\gamma=1$ のもとで
\[
 \det\operatorname{Cr}(N\operatorname{adj}M)=-1,\quad
 \det\operatorname{Cr}(M\operatorname{adj}N)
      =-(\alpha^2+\beta\gamma)^4=-1.
\]
任意のrank-one外積$Y\otimes\nu$でも
$\det\operatorname{Cr}(Y\otimes\nu)=-(\det Y\,\det\nu)^2$。
列添字$(b,c)$を$(c,b)$と交換した別のreshufflingでは、
四列のうち$01$と$10$が入れ替わって行列式の符号が反転するが、
可逆性の判定は不変である。
現行の computations/verify_lagrangian_recognition.py は本文と同じ添字規約を使い、
16添字の定義式もassertで固定している。
二次形式$f_2$の線形因子の行列式も$-(\alpha^2+\beta\gamma)=-1$であり、
rank3正規形の全配置で非退化となる。
差のある旧規約を履歴として残さず、この正しい規約のみを正本にする。
これは記号的な行列式・等方性・接空間微分の検算であり、
全幾何点のheart/AS4の同定と非被約閉基底の相対標準化は
別途原稿の論理的証明を必要とする。

## 全noncubic幾何fiberのBW条件と平坦coherent Hom

論文Bの lem:normal-foundation-BW-fiber では、
各幾何fiberが論文Aのnormal foundationと同定できれば、
Aの cor:normal-cubic-defect により右単純加群の長さ三・五頂点支持の
projective解消と終項 $P_{i+4}$ 一個を得る。
さらにMori–Nyman Definition 4.2 (ASR2)の双対条件により
$\operatorname{Ext}^q(S_i,P_j)=0$ unless $(q,j)=(3,i+4)$ であり、
その例外は $k$ となる。Theorem 4.8はAS⇒ASFであり、
単純Extの直接根拠ではない。
各幾何fiberのnormal foundation認識は
prop:lagrangian-geometric-recognition-open の三分岐
（det M≠0、det N≠0、両rank3）に依存する。
原稿にはその全幾何点認識の証明があるが、今回各分岐の
全推論を独立再検証したとは言わない。

Rを可換Noetherian、Γを中央R上有限な代数とする。
有界な有限Γ加群複体M,Nは有限自由Γ加群の上有界な解消を持ち、
平坦R→R'へのtensorはHom複体とそのcohomologyに可換する。
全qで
\[
 \operatorname{Ext}_{\Gamma}^q(M,N)\otimes_RR'
 \simeq\operatorname{Ext}_{\Gamma\otimes_RR'}^q
 (M\otimes_RR',N\otimes_RR')
\]
が成立し、各Extは有限R加群となる。
論文Bの lem:finite-algebra-flat-hom-basechange に証明がある。
相対四項tiltingのMorita比較によりcoherent対象を
有界有限Γ加群複体に移して適用する。
非平坦な通常Homの基底変更は成立しない。
R=k[t], M=R/(t), N=RではHom_R(M,N)=0であるが
R'=R/(t)への変更後はHom_k(k,k)=kである。
非平坦基底変更はcanonical compactの導来基底変更と区別する。

## 五頂点 bar の終頂点 Tor、四項生成と相対 heart

**相対定理の証明鎖。** 論文Bの lem:five-window-bar-lifting では、全幾何fiber上の五頂点窓で長さ三・終項一個のAS双対解消を仮定し、有限非極小barを任意基底変更で完全な解消へ持ち上げる。
lem:five-window-compact-localization により、導来torsion核は $\operatorname{Loc}\{S_i\}$ と一致し、$\pi P_i$ 全体がcompact生成系である。
prop:five-window-canonical-tails の残りは終頂点 $i+4$ の係数複体
\[
 V_i^{-p}=\bigoplus_{i=i_0<\cdots<i_p=i+4}
 C_{i_0i_1}\otimes_R\cdots\otimes_R C_{i_{p-1}i_p},\quad 1\le p\le4
\]
の計算である。正の向きの性質から
$\operatorname{Hom}_C(P_j,P_{i+4})=0$（$j<i+4$）であり、
$\operatorname{Hom}_R(V_i^\bullet,R)\simeq\mathcal L_i[-3]$。
有限projective複体の双対から
$V_i^\bullet\simeq\mathcal L_i^\vee[3]$ となり、
終頂点の $\operatorname{Tor}_3$ が線束、他のTorが零となる。
barの終頂点での濾過と $\pi S_i=0$ から
$\pi F_i\simeq\mathcal L_i^\vee\otimes\mathcal O_{i+4}[2]$。
$F_i$ の項は前四つのrepresentablesのみなので
$\mathcal O_{i+4}$ はそのthick閉包に入る。
増大解消から次数零項を取り出すと逆向きも得られる。
四項の高次Ext消滅と合わせてcompact tilting generatorの構成となる。

**可換基準例での独立厳密計算。**
$\mathbb P^1\times\mathbb P^1$上の標準四項窓の両parityについて、
モノミアル基底上の微分を整数係数行列として厳密に計算した。
係数複体の階数は$(9,40,48,16)$、微分の階数は$(9,31,16)$、
$d_2d_3=d_3d_4=0$、ホモロジーは$(0,0,1,0)$となる。
再現ソースは computations/verify_five_window_terminal.py。
実行した容器内コードとGitHubにpushしたファイルのblob SHAは
36f1016d14e97083a309d8a456cf28e9d8c56724 で一致する。
さらに標準窓の道(0,1,3,4)上に、二つの因子の外積から得る4項のサイクルを構成し、d3で零かつd4の像に入らないことを厳密行列rankで確認した。可換fiberのTor3の具体的生成線はdet(V)⊗det(W)型である。Bの rem:five-window-commutative-tor-cycle に証明と式を保持し、スクリプトにも非境界性のassertionを追加した。
これは非可換全体のfiberwise BW-fiber仮定の独立計算ではない。

**導来同値とAbel heartは区別する。**
$D(\operatorname{QGr}B_{R'})\simeq D(\operatorname{Mod}\Lambda_{R'})$
は左辺の標準$t$-構造を右辺へ移すが、
通常の $\operatorname{Mod}\Lambda_{R'}$ の標準heartとは一般に一致しない。
実際の相対heartはNoetherianな $\operatorname{qgr}B_{R'}$ と
Grothendieck商 $\operatorname{QGr}B_{R'}$ を独立に構成し、
module-object基底変更で比較する。
非平坦基底変更について任意の対象の導来pullbackを$t$-exactとはしない。
canonical compactとSerre根の検査、Noetherian heart・AZ・全$\chi$・descentの検査は別に行う。

**未解決の監査。** 全noncubic点におけるBW-fiber条件とnormal foundationの具体的対応、
有限型chart上の全次数効果性とNoetherian貼合せ、
一般coherent Homの平坦基底変更とSerreの相対認識を次に精査する。
今回の確認は仮定付き四項生成の論理点検と可換標準fiberの有限計算であり、
論文B全体の証明の独立検証ではない。

## 被約境界七型の周期と五頂点の compact 局所化

全七局所型について、原稿の三次関係を用いて四次 overlap の左右表示を独立に正確な多項式係数で比較した。両 parity で等式が成り立つ。
overlap の $w_i$ と $w_{i+1}$ から抽出した四周期 $\theta_i$ と幾何的二周期の平方の比は、偶・奇順に
横断 $(1,1)+(1,1)$ が $(r,r)$、接する同型が $(1,1)$、
混合 $(2,1)+(0,1)$ 横断型が $(-r^{-1},-1)$、接点型が $(-1,-1)$、
三成分cycleが $(-1,-r)$、三重点が $(-1,-1)$、
四成分gridが $(-r,-1)$。
各非零scalarは頂点スカラー比なので対角同値で消える。
型別表は論文Aの全被約逆構成直前に保持した。
これは有限次数の厳密検算であり、Serre双加群・AS4被覆の全次数や全分類の独立再証明ではない。
既存の再現コードは computations/verify_reducible_quadruples.py。

Bの五頂点barから各単純 $S_i$ がperfectである。
torsion加群は有限頂点支持部分加群のfiltered colimitであり、
有限頂点支持加群は $S_i$ に任意の基底加群をtensorした対象の拡大からなる。
従って derived torsion kernel は $\operatorname{Loc}\{S_i\}$。
Gabriel商の完全性から導来商を得て、Neeman1992 Theorem 2.1を適用すると
各 $\pi P_i$ はcompactで全体を生成する。
これは $\mathbf R\omega$ の直和可換性からの議論と独立する。
四項がtiltingであることには引き続き最終頂点Tor3の一次元性と高次Ext消滅が必要。
この追加補題はBの lem:five-window-compact-localization に証明を置く。

## 退化四つ組と非可換五頂点窓の監査対象

Van den Bergh の一次本文（arXiv:0807.3753v3）では、Proposition 5.6.1 は二周期の存在、
Theorem 6.1 は反Serreに対応するcanonical四周期を指定したhullの存在・一意性、
Lemmas 6.4–6.5 はその周期と移動の可換性・hullへの持上げを述べる。
これらから任意の二周期の平方が自動的に反Serre移動になるとは推論しない。
Aの全退化逆構成の四次テンソル回転の照合が必要である。

非被約境界の二型 C=2V+H0+H∞ と C=2V+2H の双方について、
未定元 d の多項式係数で自由代数の四次テンソルを左右表示し、
両parityの各語の係数が一致することを今回独立計算で確認した。
前者は偶数で beta(x)=x, beta(y)=y-(d/2)x、奇数で恒等、
後者は全添字で恒等であり、theta=-beta²が成り立つ。
頂点スカラー (-1)^i により符号差は自然同型で消える。
現行の再現資産は computations/verify_reducible_quadruples.py の grid_verify。
この確認は二型の低次数の計算であり、全許容四つ組の
全次数AS4被覆・Gabriel–Krull条件・主分類を今回再証明したものではない。

Bでは、可換局所環上のperfect複体の特殊fiberが次数零に集中する場合、
単元minor消去により同じ局所環上で自由加群の次数零へ集中する補題
lem:local-perfect-fibre-concentration を独立に証明した。
全てのi,jに個別に適用できるが、無限個の開集合の交叉を
開とする議論はしていない。有限型開での一様なAS4/heartは別の効果性定理が必要。
四項生成の終頂点Torの詳細は本ノート冒頭とBの prop:five-window-canonical-tails に統合した。
全noncubic点のBW-fiberと有限型chartへの一様化は引き続き独立監査の対象である。

## 有限 foundation の Hochschild 数値と GIT 比較の入口

normal foundation の有向四頂点代数 $\Lambda$ では、
相対正規化 bar コチェインの次元は次数 $0,1,2,3$ で
$(4,80,128,48)$ となる。$A_{12}\otimes A_{23}\to A_{13}$
が同型なので、二次コチェインの $(0,1,3)$ 成分
$\operatorname{Hom}(A_{01}\otimes A_{13},A_{03})$
から三次コチェイン
$\operatorname{Hom}(A_{01}\otimes A_{12}\otimes A_{23},A_{03})$
への微分が全射する。これにより $HH^{\ge3}(\Lambda)=0$。
また $HH^0=k$ と Euler 数
$4-80+128-48=4$ から
$\dim HH^2-\dim HH^1=3$ となる。
今回この有限次元数と全射の理由を独立に読み直した。
証明本体は論文Bの prop:foundation-hochschild に保持する。
cubic AS 正則 $\mathbb Z$-algebra 側の同じ結論は
Belmans2019 に既知であり、一般の noncubic normal foundation
への上記直接証明の適用と区別する。
この検算は全モジュライの代数性や全相対 heart の独立監査ではない。

**次の比較の最小問題。** geometric quintuple の
パラメータ空間は四つの二次元空間のテンソル線の射影空間
$\mathbb P^{15}$ の開部分であり、四つの $GL_2$ による
有効作用の一般的な商次元は3となる。一方で
内在的 $\mathfrak H_2$ も純次元3である。
この一致は同値や有限性を含意しない。
一般 cubic 点で quintuple の基底・ruling・二周期・
構造対象を保持する違いを追跡し、
実際の pointed exact 自己同値との比較射と幾何ファイバーを記述する。
Okawa--Ueda の GIT 次数四射と Serre 根の忘却が同一かどうかは、
全慣性と特殊化を比較するまでは未解決とする。
全 H2 に粗モジュライ代数空間が存在しないことも、
既存の GIT 商との区別に不可欠である。

## 定義と規約

対象は `(C,O)`。`s`とAS4被覆を同時に存在させる。Gabriel–Krullの`C₀`は有限長、`C₁`は`C/C₀`で有限長になる対象の逆像。`qO`が非零単純かつ`Hom(C₁,O)=0`をrank-one torsion-freeと呼ぶ。`GKdim=1`の意味ではない。

右加群を採用し、`B_n=Hom(O,sⁿO)`、`a*b=s^{deg b}(a)∘b`。`Γ_*(M)`の右作用も同じ順序。cubic repoの表示された積と反対なので、外部のNakayama・正規化自己同型の公式を直接コピーしない。

強いH2条件は `B ≅ A/(g)`、`A`は型14641、`g∈A₂`は正則正規。`g`の代表のスカラーは区別せず、最終対象ではambient自体を忘れる。`s²≅S⁻¹[2]`の同型は指定しない。根同型をrigidifyしたmoduliやtrace coherenceは別問題である。

## 八・十・十二本矢、avatar、内在的忘却

証明の正本は別稿 `papers/nc-quadric-avatar.tex`。有限foundationの生成矢、relation completion、potentialの非最小表示を区別する。有限foundationではHom次元を $(2,2,2,4,4,6)$ に固定し、積 $a,b,c,d$ の唯一の結合律 $c(1\otimes a)=d(b\otimes1)$ を課す。二つの核に分解可能テンソルを許さず、$(c,d)$ の**合併した写像**の全射性を要求する。個々の $c,d$ の全射を要求する必要はない。$\delta_a,\delta_b\in\{0,1\}$ により生成矢 $6+\delta_a+\delta_b$、関係 $2+\delta_a+\delta_b$、完成矢 $8+2(\delta_a+\delta_b)$ を得る。$b$ 可逆と $a$ 可逆が二つの10本矢open、交わりが8本矢open。最小10本・12本の層をこれらのopenと同一視しない。

product relation QPの一頂点premutationでは4本を追加して16本となり、4×4 mass行列の階数r組を消去して16−2r本を得る。三次minor上ではSchur補元 λ=d−eD⁻¹b が残る係数。別稿 `prop:qa-square-mutation-count` と `prop:qa-square-relative-schur` に有限三角変換の直接証明がある。

weighted QPの二つのmass係数 $\lambda,\mu$ が可逆なら対角pairを消去できる。非被約基底では非零というだけでは不足する。生のright-equivalence商では各pairの $\mathbb G_m$ 自己同型が残るため、代数の同型とQPスタック同値を分ける。有限foundationの頂点scalar剛体化とも別操作である。

曲線型avatarは $D\in|2h|$、fiberwise非自明な $P\in\operatorname{Pic}^0(D)$。直像 $p_*(HP^n)$ と評価で再埋め込みし、幾何的並進 $\mathsf T$ を得る。$\Sigma_0$ 部分 $\mathcal U$ と $\mathsf T^{-1}\mathcal U$ が二つの10本矢open、交わりが8本矢open。最深閉locusは $\Sigma_2$ の負断面 $S$ を含む因子。$S$ を避ける $\Sigma_2$ は10本矢境界である。全square曲線型から奇数側10本矢chartへの辞書は $F=F_s, H=F_sG_sP^{-1}$。rotated squareの $H_r=F_sG_sP$ とは逆の壁を持つ。

$P=\mathcal O_D$ の零切断は本稿の曲線型openに含めない。有限代数の同型類では古典型Cl0/Cl2へ落ちるという既存入力があるが、自己同型・降下を含む収縮は未構成。Cl2はweighted projective stack $\mathbb P(1,1,2)$ であり、$\operatorname{coh}\Sigma_2$ と同一視しない。

相対heart・Serre・豊富なexact平方根・同じ根の全軌道環のAS4被覆を確認した部分から $\mathfrak H_2$ への忘却がある。この部分を定義するだけで開性が証明されたとはしない。weighted projective stackのsign skyscraperは全ての $\mathcal O(-4n)$ から不可視であり、H2で必要な反SerreのAZ豊富性に反する。Sigma2の負断面上の $\mathcal O_S(-1)$ も同様。一方、主論文のnormal helixにより、全H2幾何点は上記の10本矢openにfoundationを持つ。これを任意の相対H2族のlifting定理へ読み替えない。

幾何的再埋め込み・有限線形代数は別稿に直接証明を置いた。全AS分類との辞書は `Q12Avatar2026` 定理15.3等の体上結果を入力とし、未公刊資料の全証明を今回監査済みとは扱わない。具体的な出典・版・節は文献ノートに保持する。

## 相対平坦性の確立した認識

`papers/moduli/relative_koszul.tex` に証明を置く。全H2の適合切断環BはKoszul AS4環の正則正規二次商なのでKoszul、反Serre環R=B^(2)もKoszulである。PP2005 Chapter 6 Theorem 7.3は任意のNoetherian局所環に適用できる。三次まで平坦で全幾何fiberがKoszulなら、全次数局所自由性と任意底変更に整合する左右Koszul解消を得る。このため、H2点を中心とする任意のArtin基底上のX3変形と、既存の横断二次jetは全次数平坦である。同節ではさらにArtin基底でnoetherian性を持ち上げ、qgrがflatなpointed Abel変形になることを証明した。canonical反SerreのArtin再構成とAbel変形の無障害性は次節で扱う。適合平方根・AS被覆の存在は別条件である。

## 内在的相対定義と認識

**cubic領域全体のsmooth Artin開部分。** `thm:cubic-smooth-open` は、全幾何fiberがcubicとなる内在的部分スタックV_cub⊂H2が、有限型で滑らかな純次元3のArtin開部分であると示す。非線形の普遍quintuple上では相対Picard群の[−2]に沿うétale被覆で適合根を構成し、linear点は可換Qのchartで覆う。各chartの全閉点で、指定されたpointed同型を保つArtin持上げを証明する。relation schemeはU×_[X3/PGL9]Uであり、選んだ根やfoundationを保存しない同値も含む。`cor:cubic-formal-h2-abelian` により全cubic点で形式H2変形とpointed Abel変形は同値で、HH≥3=0、dim HH²−dim HH¹=3となる。noncubic境界を含む全H2の代数性は下記の有限型効果性で証明し、ambient内の開性は一致根対で否定する。

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

**Artinのfoundationと偏極忘却。** `artin_foundation.tex` で、全H2のnormal geometric helixにDe Deken–Lowenを適用し、全flat pointed Abel変形にrank24のcompact tilting foundationを持ち上げた。閉fiberでheart-exactなMorita同値は、m-adic有限フィルターの各商が閉fiber圏に属することから全変形heartでexactとなる。canonical反SerreはAZ ampleで全軌道環を再構成し、Artin X3からAbel圏への忘却に右逆を与える。一般の提示環から全軌道環への自然射も、各次数が自由で特殊化が同型なので同型である。

接空間は標準的な分裂完全列0→HH¹(Λ)→T[X3/PGL9]→HH²(Λ)→0を持つ。HH³(Λ)=0からpointed Abel変形は無障害。noncubic三基準点でAbel接は3/3/4、偏極付き接は3/3/5であり、一致根対の核は既存の非零Zhang方向。HH¹(Λ)=0ならm^r/m^(r+1)ごとの先頭導分を内部導分で消せるので、任意Artin X3変形のshiftはcanonical反Serreと同型である。これは異なる二根対の全noncubic点（一根共有を含む）に適用できる。小拡大でAbel変形と次数一の枠を持ち上げることで、X3はこれらの点で滑らか、次元83となり、そのPGL9商は滑らかで次元3である。内在的H2の滑らかさは全体atlasで確立したが、X3内での実現像の局所閉性と偏極認識は別の問題である。四つのfoundation対象の像は例外性により一意に持ち上がるため、それだけでは偏極を区別できず、射への作用のintertwiningが必要である。

**非被約底でのfiber比較だけではSerre関係は従わない。** R=k[ε]/(ε²)、Γを二頂点二矢x,yのKronecker代数とし、α(x)=x、α(y)=y+εx、α(e_i)=e_iとする。Γ_αとΓはinvertible perfect双加群で、全幾何fiberでは同型だがR上では同型でない。冪等元を保つ内的自己同型は二つの頂点単元の比によって両矢を同じscalarで変換するため、このshearを与えられない。Rは局所環なので基底線束twistでも解消しない。相対Picard根の証明は、smooth reduced普遍根基底上で比較同型を実際に作ってから非被約底へ引き戻す。

**根の平方関係と存在・一意性。** `artin_roots.tex` では、近恒等DPic核をDer¹/ad(mΛ)のBCH群と同定し、一意な平方根によってp²t⁻¹を補正する。small extensionの曲率の合成から根の障害bはb+s_*b=0を満たす。s_*がHH²上恒等なら全Artin段階の障害が消える。さらにK_A^r/K_A^{r+1}はHH¹(Λ)⊗m^r/m^{r+1}へ単射であり、共役は閉fiberのHochschild作用になる。HH¹作用が恒等なら二つの根の差uの先頭項は2ℓ_r(u)=0を満たし、根のMorita同型類は一意となる。中心Z(Λ_A/m^r)=A/m^rによりinner代表の曖昧さを正規化できる。可換Qのtensor O(1,1)は両条件を満たす。根同型そのものの一意性は主張しない。四つの固定根の一次条件は9/3/5/3次元で、因子交換はV⊗Vに負の転置として作用する。一般H2点での根存在とは区別する。`cor:quadric-root-unique-all-artin`。

**Artin witnessの相対昇格。** `prop:artin-witness-relative-promotion` は、Artin上の根と全軌道AS4被覆を、全有限型A-代数上の相対H2系へ延長する。A′→K=A′/mA′で閉じた定数族へ戻し、DDのgeometric helix持上げとnilpotent NakayamaによりEnd(T_A′)=Λ_A⊗A′を示す。bounded add(T_A)複体の各項とcohomologyが平坦であることから、通常tensorが導来基底変更を計算する。これを自己同値双加群と軌道Homに適用し、square関係、全次数軌道、AZ、相対AS被覆とfppf descentを確認する。任意のAbel変形に被覆を新たに作る命題ではない。

**可換点の全一次方向。** `quadric_first_order.tex` では、P=k[x₀,…,x₃]、q=x₀x₃−x₁x₂、f∈P₂/kqに対しγ_f(x_i,x_j)=Σε_ijkl q_k f_lと置き、a⋆b=ab+εγ_f(a,b)/2を使う。PBWと相対Koszul双対性によりAS4被覆、γ_f(q,−)=0により中心正則二次切断を得る。x₀≠0上でz=x₂/x₀,w=x₁/x₀とすると{z,w}=2f(1,w,z,zw)。斉次Ore局所化がAbel変形の局所制限を与えるので、全HH²(Q)を実現する。補正に必要なHH¹(Q)=sl₂⊕sl₂はα=1+εδによる次数付き自己同型で実現でき、右軌道積α^{deg b}(a)bのZhang twistでAS被覆を保持する。上の昇格命題からT_QH2≅HH²(Q)は九次元。平方根・被覆を追加標識にしていない。高次の存在は次のcanonical hullで証明する。

**可換点の全Artin hullと形式変形。** `sec:quadric-artin-hull` では、標準根で二周期化したcubic列の有限自由tensorデータからcanonical hullを構成する。三次関係R_iと一次元の重なりW_iの二つの非退化coevaluationを逆にした評価は、交わりW_i上で一致するため七次元の関係空間S_iへ貼り合わさり、W_iの生成元を2に送る。その核が階数6の相対AS4関係を与える。二周期との整合、正規元、相対Koszul/Frobenius双対と正則二次商を確認し、体上のhull定理を非被約底へ無条件に流用しない。標準根の全軌道環への適用と昇格命題により、可換Qの全flat pointed Abel Artin変形は相対H2になる（`thm:quadric-all-artin-h2`）。忘却は閉fiberの同定を固定した形式変形groupoidの同値（`cor:quadric-formal-deformation-equivalence`）。HH³=0から無障害、接HH²は次元9、無限小自己同型HH¹は次元6である。これはQでのArtin局所の結論であり、大域的な形式商表示、一般点の根・AS被覆、有限型基底上の代数性を主張しない。一般cubic点についても、ample geometric cubic helixとそれを二項移すexact ample根s₀があり、s₀がHH²へ恒等に作用するなら全Artin認識が成立する（`prop:cubic-artin-hhtrivial-conditional`）。cubic解消の次数六の単射で双対の三次直和分解を証明し、特殊fiberの外積代数をVdB canonical hullのFrobenius双対で置き換える。追加のHH¹自明作用は根一意性を与える。ただしQ上の根tensor O(1,1)∘(z,w↦−z,w)*は同じhelixの対象を二項移してもHH²に非自明に作用する。従って対象ごとの周期性だけで作用条件を省けない。この一因子対合は連結群Aut⁰(Q)=PGL₂×PGL₂にも属するため、自己同型群の連結性だけでHochschild作用を自明とする方法も使えない。一般cubic点の存在問題は、相対Picard根とquintupleのArtin持上げによって解決した。ここでの条件付き命題は個々の固定根に対する独立の判定として保持する。

**Hochschild二次に自明なMorita根のétale代数化。** `prop:hh2-etale-morita-root` は、相対smooth properな有限局所自由代数、任意底変更後のHH<0=0・HH⁰=基礎環、Serreとの実際の平方関係を仮定する。TV2007 Corollary3.24の一般基礎環版でMorita自己同値のétale局所同型類の代数空間Gを作り、平方写像と反Serre節のfiber積Zを取る。閉根のHH²作用が恒等なら、指定Artin根の障害b+s*b=0を2の可逆性で消し、近恒等DPicの一意な平方根で平方関係を補正する。Stacks02HXによりZ→Sはsmooth、057Gの切片により指定根を通るétale近傍上に一つの根が存在する。TVのGm-gerbeを局所中立化し、平方比較線束を自明化して実際のperfect双加群と平方同型を得る。HH¹恒等は存在には不要だが、Z自体のétale性とArtin Morita類の一意性を与える。可換Qの標準根は `prop:quadric-etale-morita-root`、全noncubicの良い根は `cor:noncubic-etale-morita-root` に適用済み。相対heart・同じ根のAS4被覆の存在とは区別する。

**有限窓について得た代数化。** `prop:quadric-etale-finite-window` により標準根はétale近傍でF0↦F2、F1↦F3と同定できる。二つの比較Homは閉fiberでk[0]なので局所的に線束になり、恒等を持ち上げた射のperfect coneの消滅で同型を得る。偶数窓は元のprojective foundationの像、奇数窓はSerre rotationからfull exceptional、閉fiberのKünneth消滅を開条件で保ってstrongになる。二周期により無限個の四項窓を有限個の条件で制御できる。距離1–4のHomは階数2/4/6/9で、三重積の核R_iは階数2、四次重なりW_iは非退化な階数1の直和因子となり、任意の基底変更と可換する。閉fiberの二つの窓についてKünnethによるExt次元を直接点検した。さらに `computations/verify_quadric_finite_windows.py` をSymPyの厳密有理演算で実行し、両parityの二重・三重・四重積のrank4/6/9、三次核rank2、四次重なりrank1、二つのpairingの行列式がいずれも±1であることをPASSとした。これは特殊fiberの有限線形代数の確認であり、étale近傍の存在や無限次数の構造を計算機で証明したものではない。

**局所環での全次数提示（定理の証明は主論文）。** `thm:quadric-local-all-degree-cubic` は可換点uの局所環A=O_{U,u}上で全i≤jのRHom(L_i,L_j)がA^{h_{j-i}}[0]であることを、相対smooth properからのperfect性と閉fiberのKünneth消滅による最小自由複体の消去で証明する。各長さのtensor積は閉fiberで全射なのでNakayamaで全射。三次のR_iで割ったZ代数の各成分は有限生成で、剰余体では同色隣接交換からSym^pU⊗Sym^qVに一致し、自由なHomへの全射の核は局所Nakayamaで零。全次数の三次提示は同じ局所環上で成立し、任意底変更と整合する。偶数BはSegreを特殊fiberとし、全次数自由・rank7二次関係・局所PP Koszul変形原理による相対Koszul解消を持つ。さらに全内部次数の標準cubic解消は、W_iの重なりで複体を構成し、特殊fiberでのexactnessと有限自由Nakayamaを各次数で適用して分裂完全となる。ここでも全次数を同時に一つの有限型開に拡張したわけではない。これは局所環の証明だけでは一つの有限型開を保証しないことを示すが、その一様な開は後述の幾何的cubic標準解消とHomの帰納的同定から得る。特殊fiberの別個の有限計算として `computations/verify_quadric_finite_windows.py` に両parityで長さ3〜7の全三次関係の挿入行列を追加した。全ての長さで交換関係が核を生成する数学的証明は原稿の直接議論にあり、この有限検算から無限次数を推論しない。

**幾何的cubic fiberの開条件。** `prop:quadric-geometric-quintuple-open` ではW0,W1の全巡回二covector縮約の零集合を相対P¹×P¹上に置き、そのproper imageを有限個除いた開で全幾何fiberがVdB geometric cubicとなる。W_iとW_{i+1}の二つの非退化coevaluationからV_i≃V_{i+4}を作り、関係式の巡回を確認して体上分類を適用する。これは幾何fiberのAS正則性であり、全次数の相対平坦性を保証しない。

**全次数の相対cubic平坦性と内在Hom。** `lem:relative-geometric-cubic-flatness` は、体上VdB標準解消の次数nについて左三項が距離の短い局所自由成分からなることを利用し、幾何fiber完全性と単元minorを使って局所分裂完全性とn次の自由性を帰納する。これは同じ有限型開上で全次数に働き任意底変更と可換。`prop:quadric-uniform-cubic-hom-open` は可換Qで二つのEuler列のspliceに一致する相対四項Euler複体を、可換点の開近傍で完全にして全iに二項周期で移す。Hom(-,L_j)の帰納によりDpresからRHomへの比較が全次数で同型となる。偶数Bは全次数局所自由、四生成七二次関係の提示を持つ。VdBの一次資料 arXiv:0807.3753v3 Theorem 5.5.7/5.5.10 を確認し、旧引用のTheorem 4.31という異版の番号を訂正した。今回の導出を外部査読または形式証明で検証したわけではない。

**相対Koszul性の範囲。** `cor:quadric-uniform-even-koszul` では奇数頂点のcubic標準解消を偶数へ制限して線形分解を継ぎ、全幾何fiberの偶数環がKoszulであることを得る。既存のPPの局所Koszul変形原理により左右の相対Koszul解消は全内部次数で分裂完全。全次数flatnessだけからKoszulを結論したのではない。Noetherian性はこの議論の結論に含まれない。

**可換近傍の相対AS4被覆。** `prop:quadric-zariski-homological-as-cover` は一般定理 `thm:universal-cubic-hull` の適用である。W₀値の逆coevaluationの核は基底上で定義され、全次数平坦性・正規性・正則性・Noetherian性まで同じ有限型開上で成立する。別の有限判定問題に使える原理として、候補が既に代数的に定義され、有限個の閉条件が全Artin厚みR/mⁿで成立するなら、∩mⁿ=0によりNoetherian局所環R上でも成立する（Stacks Tag 00IP）。本研究のcanonical hullには、このArtin/Krull手順を使う必要がない。

**左右Noetherianな非可換特殊fiberの局所持上げ。** `lem:local-commutative-fibre-noetherian` は標題・主張を強化し、可換性を削除した。gr_m C≃gr_mR⊗κ Cκ において gr_mR は有限生成中心κ代数だから、Cκの左右Noetherian性だけで付随次数環が左右Noetherian。完備局所環での各内部次数内のm進級数による生成元持上げ、一般局所環への忠実平坦降下は同じ。幾何的cubic開U°の各点vではBκ(v)が体上cubic AS正則Z代数の偶数Veroneseで左右Noetherianとなるため、閉点がvへ写る任意Noetherian局所基底のBと正規AS4拡張Aは左右Noetherian。qgr BもNoetherian heartとして存在する。この点ごとの主張から単一有限型開のグローバルNoetherian性を推論しない。体上cubicのNoetherian性はVdB arXiv v3 Corollary 5.5.9(1)からの入力であり、一次資料で番号と仮定を確認した。

**有限型局所基底変更とGabriel商。** `lem:local-finite-type-strong-noetherian` はB_Rの左右Noetherian性から有限型R′=R[t]/IでB_R′が左右Noetherian（中心多項式のHilbert基底定理）になることを証明し、R′が非被約・非平坦でも成立する。`lem:qgr-module-object-basechange` はGr(B_R′)≃(Gr B_R)_{R′}、torsion部分の一致、Gabriel商の完全忠実な右随伴ωのR′作用の持上げからQGr(B_R′)≃(QGr B_R)_{R′}を導く。R′有限型ならNoetherian部分はqgr(B_R′)。`cor:quadric-local-tails-basechange-generation` は任意のNoetherian qgr対象を十分高次数のtruncationで表示してAZ生成条件(A1)を証明する。χ₁/AZ Hom全射(A2)は下記の中心基底変更補題とcubic cohomologyで成立する。強いNoetherian性（任意Noetherian R-代数への変更）とは区別する。

**局所相対tailsのfppf降下と構造対象の平坦性。** `cor:quadric-local-tails-fppf-descent` では R′→R″ faithfully flat f.p. においてQGr(B_R″)≃(QGr B_R′)_{R″}を用い、自由加群対象化F=R″⊗-が完全・保守的な左随伴であることからBarr–Beck降下を適用する。有限型底変更でNoetherian対象は保存され、昇鎖条件はfaithfully flatに検出できるためqgrでも有効なfppf降下が成立。全B_nが局所自由なのでN⊗πBが完全で構造対象は基底上平坦。導来compact圏の降下や内在的H2全条件まで言っていない。

**幾何的cubic開の全局所基底での相対χとAZ。** Smith–Van den Bergh `SVdB2013` §2.8 はNoetherian AS正則4次元環の正則正規二次商が左右χを満たすことを示す。幾何的cubic開の全fiberはhomological AS4被覆と、その偶数cubic環としてのNoetherian性を持つから、幾何点で左右χが全次数成立する。有限斉次自由Koszul解消によるExtの体拡大との交換でκ(v)へ降ろし、`lem:local-chi-specialization` のパラメータtによるKrull次元帰納を適用して、各点vの全有限次元Noetherian局所Rで相対χを得る。`lem:relative-chi1-implies-AZ-A2`と(A1)より局所R上のAZ ampleを得る。任意の局所有限型T→U°の全stalkで成立するが、任意のNoetherian affine基底でBもNoetherianなら、下記のcubic cohomologyから一様χ/AZ(A2)が従う。局所R上の全有限型R′に関する中心基底変更補題も独立に保持する。

**stalkと一様性の障害。** 標数0の無限体k、R=k[t]とし、内部次数n≥1にR/(t-n)を置いたgraded R-加群E=⊕_{n≥1}R/(t-n)を考える。各局所環R_pでE_pは有限生成（genericでは0、閉点t=nでは一つの次数のみ）だが、EはR有限生成でない。従って『全stalkで内部次数付きExtがR_p有限生成』という情報だけでは『全体として一様な高内部次数消滅』は導けない。Eは実際のExt_Bから得た反例ではなく、この推論の一般論的障害を示す例である。

**相対depth3・任意係数の切断とH¹消滅。** `lem:relative-depth-three-saturation` と `cor:relative-depth-three-coefficients` は、全幾何fiberの深さ3と各内部次数の相対Koszul cochainの局所分裂完全性を使う。任意affine底変更と任意係数NでExt^j_B(R,N⊗B)=0（j≤2）。F_nの有限filtrationから任意係数のsaturationとExt¹_Gr(B_{≥n},N⊗B)=0が従う。QGr内の拡大に右随伴ωを適用すると、Bへの像はあるtailを含む。このtailに沿って引き戻せばGr内で分裂し、元のQGr拡大も分裂する。よって全捻りでH⁰=N⊗B_n、H¹=0。高次コホモロジーの一般公式を未証明のまま使う必要はない。

**有限型中心基底変更と一般coherent対象のHom。** `lem:chi-finite-type-basechange` では有限B[t]-加群Mにt次数の補助filtrationを入れる。gr Mのt-power torsionは有限生成で補助次数が上に有界だから、高補助次数ではtが同型となる。有限個のB-加群のχから全補助次数で共通の内部次数上限を得て、最高補助次数を減らす帰納法でExtの消滅を持ち上げる。一般有限型変更は多変数と商で処理する。`lem:chi1-qgr-hom-finite-flat` はtail間のHomがχ₁により安定することと有限表示からHom有限・flat basechangeを証明する。従って局所R上の全有限型R′で、一般coherent対象を含むNoetherian Abel圏の系・AZが完成した（`thm:quadric-local-finite-type-abelian-system`）。

**canonical tailsと全相対認識。** `relative_cubic_tails.tex` が証明の正本。各単純頂点加群S_iの長さ三の有限projective解消から有限truncation F_i,nはperfect・pd≤3、tailはpd≤2。torsion上の導来torsion消滅を有界targetへの高いtailのExt消滅で証明し、cdτ≤3・cdω≤2とunbounded Rωの直和整合性を得る。四項窓はcompact tiltingとなる。右規約C_ij=D_{−j,−i}、πP_i↦L_{−i}を全helixと矢で比較する。S_i解消の像はa=−i−4のEuler複体にW_aをtensorしたものなので零。導来torsion kernel=loc{S_i}を使って比較をtailsに降ろし、(1)↔sと非平坦を含む実際の導来引戻しを確認する。

**Noetherian性から一様cohomologyと全χへ。** 同じaffine基底上のNoetherian対象に対して三段の有限presentationを取り、cd≤2と構造対象間の全Ext公式から有限性と一つのSerre消滅下限を得る。Morita像はDᵇ_fg(Λ)に入り、一般Homの平坦基底変更も従う。有限free presentationと二つの有限kernelでM_d=(ωπM)_d（d≫0）を示し、局所コホモロジーRᵇτM（b=0,…,3）の一様上界と有限幅spectral sequenceから全χ_qを得る。全stalkの有限性を貼り合わせるのではない。`thm:quadric-noetherian-relative-promotion` はmodule-object・fppf・compact/Serre・AZ・orbit/AS4の全条件を確認する。fiberのGabriel–Krull条件と全DᵇのSerreは既存の `thm:all-admissible-inverse` を適用する。局所Rが元のlft k-site外にある場合、H2(R)という未定義の記法で結果を述べない。

**一様性の範囲。** cubic開上の普遍Noetherian性は `thm:relative-geometric-cubic-noetherian` により解決済み。noncubic点でも局所環上の全軌道・Noetherian heart・全Artin認識を得た。残るのは同じ結論を一つの有限型開へspreadする段階である。有限foundationのみからNoetherian性は従わず、無限個の次数の開性を一括する追加の伝播論証が必要。

**Gabriel商の生成条件。** `lem:qgr-module-object-basechange` ではBが次数一生成かつB₁有限であることを要求する。この条件なしでは次数torsionは拡大に閉じない。例えばB=k[x₁,x₂,…]、全deg xᵢ=1、I=(xᵢxⱼ:i≠j)+(xᵢ^{i+1})としE=B/I、T=B₊Eと置く。TとE/T=kはtorsionだが、1∈Eは任意に高いxᵢ冪で殺されずEはtorsionでない。現行quadricのBは有限rankのB₁で生成されるため、全ての基底変更後にも必要条件を満たす。

`papers/nc-quadric-moduli.tex` が定義・証明の正本である。基底は標数零の代数閉体上の局所有限型scheme。相対族はnoetherian Abel圏の系とOからなり、module-objectによる基底変更、Hom有限性とflat基底変更、fppf descentを指定する。各幾何fiberには元の体上H2条件を課し、fiberの全Db上のSerre条件を明示する。これに加え、局所canonical compact圏のsmooth proper性・導来基底変更・Serreを、fppf chartの全affine基底変更上で要求する。sとAS被覆は局所存在条件であり追加標識でない。`prop:relative-h2-field-recovery` は元の体上groupoidを回復する。

相対AZ再構成、自然自己同型Aut(Id)=A×、pointed二自己同型の消滅から、反Serre関係の射 Φ:H2→[X3/PGL9] は全忠実となる。対角はaffine有限表示であり、framed部分層X_asを用いたH2≃[X_as/PGL9]はfppf stackとして成立する。**X_asは有限型・滑らかな83次元スキームとして表される**。有限型siteだけで定義した関手を、極限保存を示さずに任意scheme上の関手として扱わない。

正規化に用いるL=(det R1)^−11(det R2)^2について、Rnorm_n=R_n⊗L^−nのshiftは元のt⊗L^−1に対応する。従って普遍正規化環へ大域的に(1)=S^−1[2]を課すのは誤りであり、基底線束twistを許すかfppf局所で比較する。

**大域導来比較の候補（未証明・現行定理の入力ではない）。** heartのdescentだけからcanonicalな非有界導来圏のdescentを推論しない。flatなA→Bについて、まずD(G_B)とD(G)内のB-module対象との比較を、exact induction/forgetful随伴とBarr–Beckで証明する必要がある。その後の線形安定圏のdescentには、A. Mathew, *The Galois group of a stable homotopy theory*, Advances in Mathematics 291 (2016), 403–541, [DOI:10.1016/j.aim.2015.12.017](https://doi.org/10.1016/j.aim.2015.12.017) のCorollary 3.33（有限表示faithfully flat射のdescendability）、Corollary 3.42、Proposition 3.45が候補となる。compact生成・bounded coherent部分との比較は別に確認する。局所compact条件による現行定義は、この未完成の比較を必要としない。

**Noetherian 性の形式的貼合せ。** 可換Noetherian基底R、各次数成分が有限な中央次数環A、I=(f₁,…,fᵣ)に対し、A/IAと全A[fᵢ⁻¹]が左右NoetherianならAも左右Noetherianとなる。次数ごとのI進完備化で有限生成元の係数を収束させ、R̂_I×∏R[fᵢ⁻¹]の忠実平坦性で降下する。成分の平坦性・有限Krull次元は不要で、一般次数付き加群とZ代数のrow/columnにも成立する。証明 `thm:patch-noetherian`、`thm:patch-z-algebra`。幾何的cubic族では両部分の実際のNoetherian性を別に証明して適用する。

**非可換P¹束の対角列の障害。** 滑らかな(2,2)曲線と次数二線束から全隣接縮約が非零のgeometric quintupleを構成した。しかし対応する層対称代数の候補対角列Kₙ=π(O(n)⊗e₋ₙA)は、全ての行からHomが零になる非零coherent対象を持ち、AZ生成条件を満たさない。二次解消を用いて全整数でωπMの成分がO(−2)となることを直接証明した。これは当該模型・軌道列の比較への障害であり、本来のcubic環BのNoetherian性の反例ではない。`papers/moduli/ruled_diagonal_obstruction.tex`（論文Bの独立節）に完全な証明を保持する。本来のBのNoetherian性は、曲線商・正規拡大とlinear部分の形式的貼合せによって解決した。

**周期を仮定しない普遍Noetherian性とH2効果性。** `thm:relative-geometric-cubic-noetherian` は、全成分が有限projectiveでgeometric cubic表示を持つ族の全row・columnが、任意の可換Noetherian基底変更後にNoetherianであると示す。非線形開では相対point curveとKeelerの消滅、regular normalな四次線族を用いる。線族は頂点ごとの可逆加群twistで自明化でき、無限個の線束の同時開自明化を要しない。linear閉部分でも非退化線を全整数へ伝播し、頂点線twistで標準対称積へ移す。各parityはSegre環と有限生成Segre加群となる。Z代数の次数別形式的貼合せで全基底を扱う。実際の二周期があれば、その偶数graded環Bも左右普遍Noetherianとなる。可換Q近傍では `thm:quadric-finite-type-effectivity` により全相対公理を満たすU°→H2を得る。

**一般二周期族のcanonical AS4被覆。** `thm:universal-cubic-hull` は、geometric cubic族と実際の二周期βから、逆coevaluationの線束値写像Φ_i:S_i→W_i、Φ_i|W_i=2idと階数6の核H_iを構成する。A=T(B₁)/(H₀)は全次数projective、rank Aₙ=C(n+3,3)、双対は階数列(1,4,6,4,1)のKoszul Frobeniusであり、正則正規二次線GによるA/(G)=Bを持つ。任意Noetherian基底変更後も左右Noetherianである。まずE=B!の正規線Nを割ったP=E/(N)をprojectiveにし、PPをPへ適用してA=P!を平坦にするため、非被約基底でfiber次元一定だけに頼らない。AS4被覆は任意のβに成立するが、同じ根のSerre平方条件は独立に確認する。

**Qを含むsmooth Artin開部分。** `cor:quadric-effective-smooth-neighborhood` は、上の効果的族q:U°→H2がスキームで表現可能かつsmoothであり、fppf像V_QがH2の開部分であると示す。V_Q≃[U°/(U°×_[X3/PGL9]U°)]は有限型smooth Artinで、Qにおける次元は9−6=3である。任意の有限型T→H2への基底変更をambientの対角で有限表示schemeとして表し、その全closed pointで指定同型を保つArtin持上げを証明する。DDLの四項窓・全HomのliftとU°→Sのétale性を使い、pointed dg Morita比較からcanonical反Serre環を経て元のH2同型へ戻す。relation schemeは選んだfoundationを保たない同値も含む。Q一点の形式的比較や、任意の導来同値のheart exactnessを外挿していない。V_Qの外側の代数性と、ambient内での開性は結論しない。

## 有限foundation・coherenceだけではNoetherian性は従わない

別の族で同じ推論を繰り返さないため、既知の障害を記す。標数零で
\[
A=k\langle x,y,z\rangle/(xz+zx+y^2)
\]
と置くと、関係行列が可逆なのでglobal dimensionとGorenstein parameterは二で、graded coherentである。coherent tailsはExt有限・hereditary・Serre双対を持ち、その有界導来圏は三本矢Kronecker代数の有界導来圏と同値である。しかし構造対象はNoetherianでない。既知入力はPiontkovski, *Coherent algebras and noncommutative projective lines*, J. Algebra 319 (2008), 3280–3290、[arXiv:math/0606279v2](https://arxiv.org/abs/math/0606279)、Theorems 1.2/4.1, 2.2, Proposition 1.5(b),(d)（一次本文確認済み）。Hilbert級数は(1−3t+t²)⁻¹で指数増大するため、有限GK次元を含める本研究の規約ではこのAをAS正則と呼ばない。

非Noetherian性は右イデアルIₙ=Σ₁≤r≤n(yxʳy)Aで直接見える。商D=A/(z)=k⟨x,y⟩/(y²)におけるIₙの像Jₙは先頭がyxʳy（r≤n）のwordで生成される。全m≥0でyxⁿ⁺¹yxᵐ∉Jₙなので、Jₙ₊₁/Jₙ、従ってIₙ₊₁/Iₙはtorsionでない。ゆえにπI₁⊊πI₂⊊…⊂πAは真の上昇鎖である。各Iₙは有限生成で、graded coherenceにより有限表示である。二側イデアル(z)が右有限生成だとは仮定しない。この例はquadricの多項式増大や全局所基底のNoetherian性まで備える反例ではない。

**他の族に使える条件付き還元。** 有限Krull次元Noetherian R上で各Bₙが有限projectiveとする。全integral closed baseとそのaffine開上で、有限表示graded商がgenerically flatとなり、各generic fiberが右NoetherianならBは右Noetherianである。nilpotent filtrationと有限個のminimal primeでintegral基底へ帰着して次元帰納する。任意の斉次右イデアルIに対し、generic fiberでIを生成する有限生成J⊂Iを選ぶ。Q=B/Jは有限表示であり、Q_fをR_f-flatにすれば(I/J)_fはgeneric fiberで零のtorsion-free加群なので零、従ってI_fは有限生成となる。B/fBは帰納法でNoetherian、f進次数別完備化上も本文 `lem:patch-complete-lifting` でNoetherianである。R_f×R̂_(f)の忠実平坦性からIの有限生成を降下する。左側も同様。この還元ではgeneric-flatnessを独立の仮定とし、有限foundationだけから導かない。現在のquadric証明はこの仮定を使わず、相対曲線商とlinear部分の貼合せで完了している。

## 相対被覆と偏極変形の障害

**有限foundationでの偏極認識は解決した。** `thm:bimodule-line-comparison` は、普遍的中心が基底環である有限局所自由Λと可逆perfect双加群P,Qについて、局所同型の存在を有限表示局所閉部分で表す。K=RHom(P,Q)の負の幾何cohomologyが零、最低次Betti数が1以下となる開集合上で、d0の(r−1)-minorを可逆化しd0=diag(I,v)とする。実際の方程式v=0が普遍的H0線束を作り、その評価射P⊗H0(K)→Qのconeの消滅が残る開条件。幾何点のrankだけでは非被約方向を検出できない。比較線束は基底線束twistを記録する。任意X3族の相対foundation・shift双加群の構成はこの定理の仮定であり、結論ではない。

固定した相対切断環B=T(V)/(K)に対し、`thm:relative-finite-as-cover` はGr(6,K)内にAS被覆を選ぶ有限表示局所閉空間E_Bを構成する。A3,A4の階数20,35、双対D3,D4,D5の階数4,1,0、次数3の左右像の層としての一致、次数1,2での乗法単射、双対の完全pairingを課す。非被約基底で必要なのはscheme-theoreticな条件である。A_TがnoetherianであることはB_Tのnoetherian性と同値だが、任意Noetherian底変更でのB_Tのnoetherian性をB自身から推測しない。

有限型射(a,c)↦(a,ac)のfppf像はb∈aDという部分層であり、原点の接集合は{(u,v):u≠0}∪{0}。線型部分空間でないので代数空間とはならない。これは一般的な方法の障害であり、H2自体の非代数性の証明ではない。

`prop:antiserre-polarization-family` の明示族は、B=k[u,v]〈c,d〉/(c²−uv,d²−uv)、R=(B^(2))^ιから作る。σ_q:u↦qu,v↦q⁻¹v,c,d固定による右Zhang twistは全次数平坦で、pointed qgrはGm基底全体で一定。しかしZ(R)_1にcd−dcがあり、q=2では中心一次部分が零になるため、このfiberはどのH2のcanonical反Serre環でもない。q=1+εの一次類は、中心元U=u⁴,V=v⁴の交換子16εUV≠0で非自明性を検出できる。**u²,v²はι-twist後のRでは中心ではない**ので、この証明で用いない。既存orbit79方向へこの方向を加えると80、六係数も含む81方向へ加えると法101で82になる。

全Artin基底でcanonical反Serre偏極・良い平方根・AS4被覆の存在は証明した。有限型近傍上の一様化は `thm:noncubic-finite-type-effectivity` で成立した。一般の偏極付き表示からcanonical偏極を具体的な方程式で認識する問題は残る。全次数Hilbert条件を重ねてこの偏極方向を切ろうとしても、族自体が全次数平坦なので解決しない。

## スタック構成の現状

証明の所在は `papers/moduli/noncubic_stack.tex` と `papers/moduli/foundation_stack.tex`。表示と相対内在的moduliの区別を維持する。

| 結果 | 確立した範囲 | 残る比較 |
| --- | --- | --- |
| noncubic `[P/G]` | 被約境界Nとの相対同値を証明。smooth finite type Artin、dim1、全pointed慣性を保持 | 全fiberがnoncubicである非被約族がNに因数分解するとは限らない |
| 根配置への射 | 順序付き局所表示上μ2² gerbe。S2は二因子を交換 | μ2²は真の自己同値であり除かない |
| χによるgood moduliとDM粗モジュライ | N→A¹はgood。N^DM→A¹は任意底変更と両立するcoarseだがgoodでない。Nと全H2のcoarse algebraic spaceは存在しない | 共通étale近傍のgood moduliを全H2へ降下できるかは未確定 |
| 表示族の局所AS被覆 | étale局所の交換対合、全次数有限自由、中央正則切断とZhang twist。相対Serre・全相対認識も成立 | 被約境界との相対比較はNpres≃Nで確立 |
| foundation `F=[A64/(G/K)]`、K≅Gm³ | smooth finite type、dim3。全H2のfoundationが入る。HH≥3=0、dimHH²−dimHH¹=3 | 内在的H2実現部分の有限表示、相対Serre/AZ条件 |
| rulingとfoundationの二択 | rank-one TF exceptionalと反Serre Hilbert多項式で二rulingを内在認識。normal helixで作るfoundationが二つ | 任意の内在的族における相対存在・底変更・降下 |
| 相対ruling交換とQ_fnd | F0上の二短完全列交換がcoherentなS2作用。Q_fnd=[F0/S2]はsmooth finite type、dim3。F0→Q_fndはrepresentableな有限étale二重被覆 | 内在的H2族のruling被覆との相対同定 |
| 全H2(k)のgroupoid | H2(k)→Q_fnd(k)は全充満。全幾何点のpointed慣性も一致 | 任意基底上の相対全忠実性・本質的全射性 |
| cubic geometric開部分 | `[Gr(2,8)_geo/(PGL2)^3]`、smooth finite type、dim3。相対認識と全cubic smooth開部分は成立 | noncubic境界を含む一様認識 |
| 実現集合Yの成分 | cubic非空開C⊂Y⊂underlying(Q_fnd)。誘導位相でYは既約かつ連結、各成分数1 | 内在的相対moduliの位相との一致 |
| 全noncubic点へのcubic特殊化 | xと可換Qのcubic foundation点yを結ぶ線の開部分。0以外の全幾何fiberはcubic、0はx | 相対heart・根・AZ・AS被覆を備える強いH2族への昇格 |
| 相対smooth proper dg族 | rank24有限自由代数Λ。正規化relativebar分解が次数3で止まり、対角とe0Λがperfect | 相対的なexact heartの認識 |
| 反Serre慣性 | Aut_gr(R)/Gm_degree≅Aut_pt、pointed二自己同型は自明 | 族の全忠実性 |
| degree gerbeの中立化 | R1 rank9,R2 rank25、detR1^−11 detR2²の重み1。Gr(56,81)全体で中立 | 相対実現locus X_as、下降環とcanonical Serre環の同定 |
| noncubicの選択不要な相対反Serre環 | `B_{2n}⊗(det W)^−n`、`a⋆b=aιⁿ(b)`。σ²=ιなので任意の非被約底変更と両立して剛体化商[P/G]へ降下。各次数rank(2n+1)² | この降下を任意の内在的H2族の再構成と混同しない |
| noncubicの中心Clifford表示 | `h=cd+dc` 中央、`C=A[u,v,h]`（重み1,1,2）、`B=C⊕Cc⊕Cd⊕Ccd`。任意noetherian底でB,R左右noetherian | 相対heartの全対象の完全性は別 |
| noncubicの相対Serre | Clifford trace（cd係数）で`Hom_C(B,C(-4))=B_ι(-2)`。weighted P(1,1,2)上のperfect B対象には`S=(-)_ι(-2)[2]`、局所平方根`(-)_σ(1)` | 全coherent heart上の双対性・相対AZ・AS被覆の認識 |
| 二次Veroneseと相対平坦族 | 任意の二次環BのB^(2)はT(B₂)/(ker(B₂²→B₄))、自己同型twist後も二次。Noetherian底でR_n局所自由かつ全幾何fiberが二次なら族も二次 | 一般事実はPolishchuk–Positselski既知。本研究の相対直接証明はlem:relative-quadratic-veroneseとlem:relative-quadratic-from-fibers |
| 全H2の内在的反Serre環 | R=⊕Hom(O,tⁿO)は全て九生成元・rank56の二次関係だけで表示。cubic/noncubic chart、cubic→noncubic特殊化も全次数で二次提示が基底変更する | cor:h2-intrinsic-antiserre-quadratic, cor:cubic-relative-full-quadratic-presentation, cor:noncubic-relative-full-quadratic-presentation, cor:line-full-quadratic-degeneration |
| noncubic の固定Grassmannセル | u²,uv,v²,uc,vc,ud,vd,cd,dcの9基底。積25列がB₄の交互語PBW基底に符号付き一対一。minor±1。p₀⋆p₀=−u²f₁とq₀⋆q₀=−u²f₂から6係数を回収。A6→固定Gr cellは閉埋込み、非退化Pは局所閉 | prop:noncubic-grassmann-explicit-cell。フレーム付き表示空間の命題でありPGL9群商の閉埋込みではない |
| 型を局所定数にした表示モジュライ | C⊔Npres は有限型Artin、全H2幾何点・慣性を再現するが、cubic→noncubic退化を人工的に除外し、既約・連結成分は2 | prop:split-h2-presentation-moduli |
| 三次までの二次関係モジュライ | X3={rank L3=176}⊂Gr(56,81)は有限型局所閉rank-stratum。 [X3/PGL9] はrankR2=25,R3=49の二次提示のrigidified Artin moduli。detR1^-11 detR2²で普遍全次数環を降下。既知のcubic/noncubic/退化族は入るがその他も入る | prop:truncated-antiserre-moduli-stack |
| 一致根対点での違い | X3商のH0接次元は84−79=5、Q_fndは滑らか次元3+慣性Lie次元1=4。形式近傍は同値でない | prop:truncated-versus-foundation-tangent |
| noncubicの Koszul 性と一次全次数平坦性 | 二重平方環の二次 Gröbner（PBW）表示からBはKoszul、偶数VeroneseとZhang twistのRもKoszul。三次の重なりの一次整合はKoszulの次数0 Hochschild 2-cocycle条件に一致し、双対数上の二次関係変形が三次平坦なら全次数平坦 | prop:noncubic-antiserre-koszul, lem:koszul-first-order-degree-three。一般Artin族への拡張は cor:h2-geometric-family-koszul で確立 |
| noncubicの内部次数0 Hochschild 次元 | 非交差、一根共有、一致根対でHH¹_0=1,1,2、HH²_0=3,3,5。C¹=81、C²=1400、C³=16072、rank(d¹)=80,80,79、rank(d²)=1317,1317,1316 | thm:noncubic-hh01-hh2。foundation代数のHH≥3消滅とは異なる |
| 横断2/2/3方向の二次持上げ | 三次Hilbert locusの横断部分の各基底ベクトルと二基底の全ての和について、Schur補行列の二次障害を打ち消す有理数補正を計算し整数行列で正確に検査。全横断方向がk[t]/(t³)上で三次成分平坦な2-jetを持つ | prop:noncubic-transverse-second-order。全次数の二次flatnessとflat Abel実現は確立。固定jetの表示偏極を保つ高次延長は未検証。underlying pointed Abel変形は全Artin認識でH2に属するが、その偏極がcanonical反Serreであることとは区別 |
| noncubicのLie接方向と三次Hilbert条件 | disjoint, shared, equalの三点でPGL9軌道+六係数のrank81（軌道80/80/79、交点5/5/4）。三次関係L:V⊗J→(V²/J)⊗Vはrank176、kernel328/cokernel49。法101の全16072線形条件rank1317/1317/1316。標数零で接次元=83/83/84（有理核の全整数検証）、三次条件の接空間を群+係数81方向で割った次元は正確に2/2/3（実際の相対H2変形かは未証明） | prop:noncubic-third-degree-tangent。局所SymPy/NumPy/Numba exact演算を実行。全次数平坦性は相対Koszul節により確立。内在H2の接空間とは未同定 |
| 関係式像の構成可能性と既約閉包 | 2つの有限型chartの像の和はH2の全幾何関係像。Chevalleyで構成可能。cubic枠束像の被約閉包Z₂はPGL9不変既約有限型、全noncubicは反Serre二次族による特殊化で[Z₂/PGL9]に入る | prop:h2-constructible-relations-and-irreducible-closure。Z₂の全点がH2とは未証明。smoothスキームとして表現される内在的部分層X_asとは別 |
| noncubicの相対heart・相対orbit | `R`の`qgr R`を構造対象付きnoetherian Abel heartとして任意のNoetherian基底上に定義。étale局所に`qgr B^σ≃qgr R`。weighted P(1,1,2)上`RHom(B,tⁿB)=B₂ₙ[0]`が全n・底変更に整合（`cor:noncubic-relative-orbit-hom`, `prop:noncubic-relative-heart-veronese`） | 任意の内在的noncubic族のこの相対heartへの帰着、全flat coherent対象の相対双対・AZ/AS等 |
| cubicの相対反Serre環 | smooth proper foundationの逆Serre双加群から`RHom(e₀Λ,tⁿe₀Λ)`。cubic開では全nでrank(2n+1)²局所自由 | 任意のH2族からの相対foundation抽出 |
| 共通Grassmann射と実際の特殊化 | cubic開Cとnoncubic表示[P/G]の双方から`[Gr(56,81)/PGL9]`へ射。各noncubic点へのfoundation直線族も全次数平坦な反Serre環の族を与える | 両chartの相対的な貼合せとfull内在H2との同値 |
| 選んだSerre根の一次変形障害 | 持上げにはHH²類の保存が必要。Q上でs_*u=−uとなる適合根と非零変形を構成 | 別の根の存在や相対H2条件の開性は判定しない |

**修正定義で厳密に得られる stack。** 反Serre関係のG=Gr(56,81)から次数3を作る自然写像 L3:U⊗J→((U⊗U)/J)⊗U は504→225であり、rank176ならR3は49次元局所自由。この正確rankの局所閉部分X3は非被約基底まで含む真正な有限型スキームで、PGL9商はArtin。GL9版が生成元と関係の相対モジュライ、PGL9版が共通次数スカラーのrigidification。普遍Rを無理にPGL torsorから取り出すBrauer障害はdet(R1)^-11 det(R2)^2の重み一の線で消え、R_nをその-n乗で捩って降下する。これらは全次数のflatness、Serre平方根・AZ・AS被覆を**課していない**。対照的に既存のcubic chart Cとnoncubic chart Npresの非交和は全幾何点慣性を再現するが、型を局所定数にしており、見かけの成分数が二になる。これは自然なH2相対スタックの既約性の反例ではない。

**接複体による非同値の検出。** coincidence f1=f2=uv ではX3の普通の一次接次元84・PGL9接軌道79なので、[X3/PGL9]の接複体のH0は5次元。一方Q_fndは滑らか次元3・慣性Lie1なのでH0=4。よって少なくともこの点の形式近傍は同値でない。したがって X3 の余分な方向を排除する、または内在的H2として理解する条件が必要。これが現在の最も短い差分証明である。

**Koszul の低次変形と二次障害。** Rのquadratic Koszul bimodule complexで内部次数0のHochschild cochainはC¹=Hom(V,R₁)、C²=Hom(J,R₂)、C³=Hom(K₃,R₃)、K₃=(V⊗J)∩(J⊗V)である。三次Hilbert条件の線形化がd²であり、degree-3 flatな双対数上の二次関係は全次数flatなgraded algebra first-order deformationを与える。三基準点のd²核83,83,84とd¹像80,80,79からHH²_0=(3,3,5)を得る。HH¹_0はEuler導分を含み=(1,1,2)。これは有限foundation代数の高次HH消滅を言い換えたものではない。

**横断方向の二次持上げ。** L₀の176×176単位行列式小行列Aを取り、L(t)=L₀+tL₁(φ)+t²(L₁(ψ)+L₂(φ))をSchur補行列で展開する。K₀をkernel、Q₃をcokernel基底射影として、Q(φ)=Q₃(L₂(φ)K₀−L₁(φ)i_CA^{-1}(L₁(φ)K₀)|_I)を計算する。全三点で横断基底(2,2,3本)と相異なる二基底の和(1,1,3本)に対しd²ψ=−Q(φ)の有理補正を構成し、整数行列積で厳密に確認した。一致根対では分母2の補正も現れる。Qが二次式であるため、これらの零性から全横断線形結合への補正が構成できる。ただし結論はあくまで **R₃のrank49条件のk[t]/(t³)-平坦性**であり、全次数の二次平坦性、HH³の消滅、正式な相対H2族と混同しない。

**三次関係階数の接空間。** 基準 $\dim V=9,\dim J=56,\dim R_2=25,\dim R_3=49$ に対して $L_J:V\otimes J\to (V^{\otimes2}/J)\otimes V$ のrankが176となる。このrank≤176のdeterminantal locusの接ベクトルは $\phi\in\operatorname{Hom}(J,R_2)$ で $\ker L_J\to\operatorname{coker}L_J$ の線形化が零となるもの。56×9=504、25×9=225、kernel328、cokernel49で、条件行列は16072×1400である。固定pivotで $J$ の affine 座標を取り、法101で三根配置ごとに全行を簡約した階数は1317,1317,1316。整数係数のminorは標数零でも非零なので、まず標数零の接次元は≤83,83,84。さらに法101核基底から83,83,84本の有理ベクトルを復元し、整数係数の線形化行列で全ベクトルの零性を厳密に確認したため、標数零でも接次元は**正確に**83,83,84である。全次数Hilbert平坦性は相対Koszul原理により成立する。内在的H2を満たすかどうかは、適合平方根・被覆の存在をなお確認する必要がある。PGL9と六係数の接像は、群Gの軌道による上界と法101でのrank81の下界から標数零で正確に81。群商スタックの次元1と、Grassmann内にあるframed接像81を混同しない。次数4の一次平坦性は今回のKoszul一次変形原理から従うので別計算不要。次は根・AS被覆の持上げと一般有限型族への認識を検査する。

**具体的な25 pivot と完全二次提示。** 二重平方環の交互語PBW基底から $\mathcal R_1$ の九基底 $x_0=u^2,x_1=uv,x_2=v^2,p_0=uc,p_1=vc,q_0=ud,q_1=vd,z=cd,z'=dc$ を取る。$\mathcal R_2=B_4$ の交互語長0,1,2,3,4の基底数は順に5,8,6,4,2。主原稿式(NC-25)の積25個はそれらと符号付きで一致するためminorは±1であり、六係数は$p_0\star p_0=-u^2f_1,q_0\star q_0=-u^2f_2$から復元できる。これは全パラメータの多項式恒等式であり、判別式の非消滅はH2実現部分を選ぶためだけに必要。二次Veronese一般定理の既知性はPolishchuk–Positselski, Chapter 3 Prop.2.2に帰属する（原著の定理文は公開閲覧資料で照合し、相対版は本文で直接証明）。この結果によりGrassmann射がRの**全次数**を規定することは確立したが、Grassmannian上の任意の点に対応するRがH2を実現するとは限らない。

**Z₂ の構成。** cubicの既約開$U_{\mathrm{cub}}\subset\mathbb A^{64}$のrank9反Serre一次束のframe bundleをGr(56,81)へ写し、その像の被約閉包をZ₂とする。frame bundleはGL9が幾何学的既約なので既約で、Z₂も既約。PGL9不変で、[Z₂/PGL9]は有限型Artin。全noncubic点は既存の直線退化をrank9 frameが自明なtrait上でGrassmannianへ持上げることで閉包に入る。ChevalleyによりH2全幾何点の関係像は2 chartの構成可能な和になる。Z₂は**代数的包絡**であり、内在的\mathfrak H₂ではない。次に必要なのは非被約底上での相対実現locusの構成である。

**非cubicの相対heartまで得られた範囲。** 普遍`R`から`(qgr R,πR)`を任意の可換noetherian底の表示に定義でき、`σ`のétale局所選択の下で`(qgr B^σ,πB^σ)`に対応する。weighted projective stack上の中心Clifford orderからperfect Serre公式を得て、相対orbit Hom`RHom(\widetilde B,tⁿ\widetilde B)=B₂ₙ[0]`をweighted Čech計算で確定した。これは表示族の相対heart・Serre orbitの具体構成であって、任意の相対内在的`H2`族をこのchartへ導く`ess. surjectivity`、全flat coherent対象の相対Serre双対やLowen–Van den Bergh平坦性と相対AZ/AS被覆まではまだ含めない。

**具体的な反Serre族の構成。** noncubic普遍表示では`ι(c)=−c,ι(d)=−d,ι|W=id`、`σ²=ι`であるため、選んだZhang twist`B^σ`の偶数部分は選択に依存せず`(B^(2))^ι`となる。次数ごとのD-gerbe重量`2n`を`(det W)^−n`で相殺すると、全次数の普遍環が[P/G]へ降下する（`prop:noncubic-antiserre-descent`）。次数1・2がrank9・rank25で積が全射だから、二次関係はrank56の部分束となる（`prop:noncubic-antiserre-grassmann`）。中心Clifford表示`B=C⊕Cc⊕Cd⊕Ccd`の完全性はHilbert級数と主項で検証し、`C^(4)`が反Serre環の中心に入るのでNoetherian性も従う（`lem:noncubic-relative-clifford-center`、`prop:noncubic-relative-noetherian`）。Clifford trace`tr(cd)=1,tr(dc)=−1`の積行列式は−1で、`tr(ab)=tr(bι(a))`から相対Serre双加群と局所平方根の公式を得る（`prop:noncubic-relative-serre-on-perfect`）。

**cubicと特殊化の反Serre環。** 相対inverse-Serre `t=S^−1[2]`をfoundationのsmooth proper perfect族上で定義すると、全ての`V_n=RHom(O,tⁿO)`はperfectで任意底変更する。cubic開では幾何点のExt消滅によりrank`(2n+1)²`のベクトル束となり、`[Gr(56,81)/PGL9]`への射を与える（`lem:foundation-relative-antiserre-perfect`、`prop:cubic-relative-antiserre-grassmann`）。前回構成した各noncubic点へのfoundation直線族では、全幾何ファイバーがH2なので`V_n`は**特殊点を含む族全体**でベクトル束となる（`prop:line-degeneration-antiserre-algebras`）。つまり実際の全次数平坦な反Serre環族の特殊化が得られるが、相対heart・根・AS被覆まで認めた内在的H2族との同定はまだない。

**相対ruling交換の具体形。** `U0` は `G:Q⊗W2→W3` が全射、`α_F:W1→P*⊗W2` が部分束包含となる開部分で、`F0=[U0/(G/K)]`。`R=ker G`、`C=coker α_F` を取り、`(W1,W2,W3;P,Q)` を `(R,W2,C;Q*,P*)` へ移す。新しい二写像は包含の縮約と商写像である。二つの短完全列を交換する構成なので、任意底変更と整合し、二回交換の自然同型はS2の整合条件を満たす。mutationによる新foundationと一致する。これらは `prop:relative-ruling-involution` と `prop:ruling-involution-mutation` で証明済みであり、未解決のcoherence条件として残さない。

**幾何点の慣性を保つこと。** `cor:h2-point-groupoid-foundation` は、pointed exact同値が内在的二foundationを置換すること、頂点を保つEnd代数同型の比較スカラーがKであること、標準dg/Morita同値とheartの内在性を用いて全充満性を示す。Q_fndの各点に余分なS2自己同値を一律に付けるのではなく、交換成分は実際のruling交換自己同値が存在するときだけ非空となる。これは体上の全groupoidの実現であり、全Q_fnd点のH2実現や任意基底上の比較を意味しない。

**cubicのgeometric開条件。** Fが可逆なら `W2=P⊗W1`、`R=ker G⊂Q⊗P⊗W1` は二次元である。包含から得る四重テンソルについて、隣接する二因子の任意の非零線型形式による縮約が非零となる条件が `Gr(2,8)_geo` を定める。悪い縮約のincidenceは射影束からのproper像なので、その補集合は底変更と整合する開部分である。Fの可逆性とGの全射性だけでは不十分であり、`e0000+e1111` が反例となる。表示と証明は `prop:cubic-foundation-open` を参照する。

**cubicの稠密性と成分。** `U_cub⊂U0⊂A64` はgeometric cubic条件を満たす非空開である。商Q_fndにおける像Cも非空開で、既約なQ_fndの稠密開となる。H2実現集合YはCを含むため、誘導位相で `closure_Y(C)=Y`。Cが既約なのでYも既約であり、既約成分・連結成分は各1である。既約なambientの任意の部分集合についての主張ではなく、既約稠密開を含むという具体的な包含を使う。証明は `prop:h2-component-density`。

**各noncubic点への特殊化。** noncubic点を表すx∈U0(k)と、可換Qのfoundationを表すy∈U_cub(k)を選ぶ。`ℓ(t)=(1−t)x+ty` に対してℓ⁻¹(U_cub)は1を含む開なので、補集合は有限である。そのうち0以外を除いたT⊂A1上で、0は指定noncubic点、0以外の全幾何点はcubicとなる。普遍foundation代数の引戻しΛ_Tはrank24有限自由である。さらにE=O_T⁴、Jを厳密上三角成分とした正規化relativebar分解 `Λ⊗_E J^{⊗_E n}⊗_EΛ` はn>3で零となり、各項は相対包絡代数上で有限射影である。従ってPerf(Λ_T)は構造対象e0Λ_Tを持つ相対smooth proper dg族である。証明は `prop:h2-line-degeneration` と `lem:foundation-relative-smooth-proper`。相対heartと適合根・AZ・AS被覆の存在はこの主張に加えていない。

**単純なOreパラメータ変形の限界。** 固定した中央二変数の表示 `yx=qxy+h(u,v)` でqだけを動かす方法では、q=−1のnoncubic切断 `a x²+b y²+H` を一般点へ延長できない。`prop:ore-normal-quadrics` により一般のq≠±1では許される正規二次式にx²,y²項がなく、整な底上で一般点で消えるその係数は特殊点でも消える。今回の特殊化は、この固定Ore表示へ制限せず、foundationの二写像を動かす。

**点集合から族へ移す際の障害。** Spec(k)→Spec(k[ε]/ε²)は全幾何点を覆うが、底の恒等射はfppf局所にもここへ因子化しない。忠実平坦な拡大では非零εを零にできないためである。したがって全field pointの表示・被約像の構成だけでは相対essential surjectivityは証明できない。同様に、幾何fiberでrank3という条件は4次minorがnilpotentであることしか保証しない。rank3 locusはminorのscheme-theoreticな消滅で定める必要がある。

**変形理論と選んだ根の障害。** foundationのHH³消滅とDe Deken–Lowenのabelian/thread変形比較は、相対H2条件を追加する前の局所入力である。固定した変形類uへの自己同値Φの持上げ障害は、核の左右のHochschild作用を同定すると `u−Φ_*u` となる（Lowen2008 Theorems 1.1, 4.8, Corollary 4.9、Toda2009 arXiv v3 Proposition 5.6, Lemma 5.8）。可換Q上で `f(z,w)=(-z,w)`、`s=(−⊗O(1,1))∘f*`、`π=∂z∧∂w` とすれば、sは適合根だが `s_*[π]=−[π]`。`a⋆b=ab+(ε/2)π(da,db)` が与える固定abelian一次変形へ、このsはR線形dg/Morita自己同値として持ち上がらない。線束tensorのHH²作用が恒等なのは、このQではH¹(T)=H²(O)=0で局所bivector成分だけが残るためである。

この例は**選んだ根**の障害であり、別の根の存在を排除しない。構成したabelian一次変形自体は可換点の全Artin認識によりH2に属し、標準根を選べる。持ち上がらないのはここで指定した別の根である。従って相対H2 locusの非開性やformal smoothnessの否定は結論しない。実現集合の誘導位相ではcubicからnoncubicへの特殊化があり、両者は別の連結成分ではない。全H2の有限型smooth性・既約性・境界の余次元二は別の実際のatlasで成立した。Q_fnd内の相対実現部分との比較・降下、および内在的位相との比較である。

群関係・χ・noncubic局所対合の再現資産は `computations/verify_stack_symmetries.py`。現在の独立読取り・計算・組版の実施範囲は末尾の検証節に集約する。

相対条件を試す具体的入力として、[定数bivector方向のOre変形](ore_quadric_deformations.md)を置く。中央元g=xw−zyの正則切断、全次数自由な商、quadratic dualのFrobenius pairingまでの証明稿を記し、相対CY・Serre・H2条件は未証明とする。主原稿の非持上げ例を相対H2の内部へ強める際の候補であり、現行定理の入力には用いない。


## O-marking から Abel 圏への忘却：楕円型の全標識と同値判定

**楕円型の全O標識と有限・無限の忘却。** 滑らかな楕円四つ組でδ≠0、η∉Zδなら、RTと対角根から全Z²のrank-one torsion-free exceptional対象を構成し、数値類ごとの一意性で全てを尽くす。全てがH2の構造対象となる。Uₙ=(E,L₀,L₁⊗(L₂L₀⁻¹)ⁿ,L₂)を代表とし、εδ=δかつε(η+nδ)∈{η+mδ,2δ−η−mδ}という有限楕円自己同型群を含む必要十分条件でpointed重複を判定する。δ非捩れなら可算無限、位数rならZ/rZの有限商となる。余分な自己同型がなく2η∉⟨δ⟩なら正確にr個。証明は `thm:elliptic-marking-lattice-fiber`、`cor:elliptic-torsion-fiber-cardinality`。Z²と二面体作用はKitamura–Okawaの既存announcementと重なるため新規性を主張せず、ここでは指定範囲の独立証明と明示的な忘却判定を与える。η∈Zδ、退化曲線、noncubicの忘却と相対stack射は未解決。

数値作用はTが構造対象を(1,0)へ移して軸交換、Rが構造対象を固定して軸交換なので、RTは軸を保つ(1,0)移動。適合二周期根は(1,1)移動である。従ってL(a,b)=sᵇL(a−b,0)。差パラメータの一致から三線束の同型を得る際には、[2]:E→Eの全射性でL₀を合わせるtranslationを選ぶ。非捩れでも2η=qδの場合はn↔2−q−nだけが重複し、可算無限性は変わらない。

相対stack射の離散性、étaleなZ被覆、全自己同値群の記述をこの集合論的結果から結論しない。全cubicのZ²分類とD∞作用はOWR2022報告に既に記載され、本稿の証明はその未照合の詳細稿を入力としない。

## 証明状態と依存関係

**分類の有限同値判定に必要な幾何。** `prop:first-orbit-finite-equivalence` の再帰集合 $C_n\subset GL_4$ が有限段で安定する理由は、単なる構成可能集合の下降列の停止ではない。二次関係の transporter $E\subset G\times G$ は閉代数部分群の剰余類であり、剰余類との共通部分・代数群準同型の射影でこの構造が保たれる。従って $C_n$ は空または閉剰余類、かつ下降するので Noetherian 性により停止する。Aの `papers/sections/first_orbit_object.tex` にこの閉性の依存を明記した。今回の点検はこの論点の論理的読取りであり、分類定理全体の独立監査ではない。



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

これらの基礎結果の独立した新規性を確定したものではなく、形式証明器も使用していない。全H2対象の被覆と同値類分類は主定理に統合した。全幾何点groupoidと全pointed慣性はQ_fndへの全充満な実現で捉えた。実現集合Yの誘導位相での既約成分・連結成分は各1と証明した。一方、内在的fppf stackと全忠実な関係射は構成済み。全H2の有限型代数性・純次元三・既約性と、被約noncubic境界のsmooth性・純次元一・余次元二を、実際の族とsmooth atlasから証明した。noncubic境界の相対表示はNpres≃Nで確立し、全体のfoundation表示との相対groupoid比較は別に残る。

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

## noncubic根の交代Gale模型

証明は `papers/moduli/noncubic_hh_roots.tex`。四項foundationをGr(4,8)の開部分へ移すと、二項移動はL↦{(−Y,X):(X,Y)∈L⊥}となる。trace零対合から選ぶ右根による四つの比較行列は(D₀,−I,D₀,−I)、D₀=diag(1,−1)。従って実際の根の作用はJ=[[0,D_L],[−D_L,0]]、D_L=diag(1,1,−1,−1)による交代annihilator involutionである。直交形式のinvolutionとして扱うと接の正負を誤る。基底変更のLie作用は(a,b,c,k)↦(D₀cD₀,−kᵗ,D₀aD₀,−bᵗ)。自明な三次元中心の正負は(1,2)、有効Lieの正負は(7,6)である。一致根対の一次元慣性は正部分なので、全配置でHH¹/HH²の負部分が消える。本文の一般証明は三有理例からの外挿を使わない。

再現は `python3 computations/verify_noncubic_gale_root.py`。SymPyの厳密有理演算でLagrangian条件、接involution、全基底変更軌道、HH²の正負次元(3,0)/(3,0)/(4,0)を確認する。原稿のbar微分・右Zhang規約とこの計算は独立に読取り確認した。良い根の一つを特定した結果であり、他の全根の作用も自明であるとは主張しない。


**noncubic変形の具体的なétale表示。** `prop:noncubic-lagrangian-etale-slice` により、Lagrangian Grassmannian LG(4,8)の開部分を7次元群で割った商から、全noncubic点を含むfoundation変形の開部分への表現可能なétale射を得る。法軌道写像の行列式はPlücker O(3)の切断で、正規形では−32α。根対一致では対角L₀を選ぶ必要があり、別のtrace零交換根にはHH²の負方向が1次元残る。この有限代数の表示を、全fiber認識と全軌道比較を経て、下記の内在H2のatlasへ接続する。

正規化L₀=[[α,β],[γ,−α]]、α²+βγ=1で法軌道写像qのdetは−32α。α=0の場合は根対が一致し、off-diagonal選択ではHH¹の負部分1、HH²の正負次元(3,1)となる。これが全一次持上げを妨げる具体例。証明と6×6行列は主原稿、再現は `python3 computations/verify_noncubic_gale_root.py`。

## noncubic中央被覆と全Artin認識の要点

本文は `noncubic_central_hull.tex` と `noncubic_local_tails.tex`。中央線χ=UV−VUの正則性はχ²(p²+θ⁻²q²)=(p+q)⁴と既存Ore双対のp+qの正則性による。一般係数の有限検算が全次数の証明を代用しない。twist後の中心と反中心をα=σ⁻ᵗの固有値1,−1,i,−iに分け、p/(p+q),q/(p+q)の二つのClifford成分で比較する。

**generic cubicの符号を省略しない。** Serreに適合する根であってもcanonical normalizerはscalar±1までしか従わない。良いnoncubic閉fiberで反中心が零であるため、局所基底のgeneric fiberでも−1を排除できる。中心交換写像の6次minorが単元、7次minorが整域上で零となり、中心線が直和因子として延びる。その後は既知自由加群Eₙ₋₂→Eₙの特殊fiber単射性だけで全次数のsplit単射・自由商を得る。未知の商のfiber次元一定から平坦性を推論しない。

**五頂点の非極小化が必要な理由。** noncubicの最小解消に現れる距離二の追加項はcubic generic fiberでは消える。barの固定複体なら、この追加二項が可縮になることを許す。末頂点係数の階数は次数1–4で9,40,48,16、Tor₄=0から最後の項をsplit消去する。導来torsion kernel=loc{Sᵢ}を確認して、Pᵢ↦E₋ᵢが全軌道・shift・実際のMorita根を保つ比較へ降りる。

**中心正則性は一つの開に広がる。** `lem:spread-central-regular-line` は、P=E/(φ)の次数0–4がfinite projective、P₅=0なら、一次生成性からEが中央R[t]（deg t=2、t=φ）上有限となることを使う。乗法核は有限R[t]加群なので、指定局所環での消滅を一つの分母で全次数同時に消せる。得た開上で次数付きR[t]-加群としてEはP₀,…,P₄の持上げから作る直和（非標準的）となり、全Eₙのprojectivityと任意底変更後の正則性が成立する。この有限化補題は独立読取り済み。

**有限型伝播における循環の回避。** 有限Frobenius商Pの存在だけではKoszul性やA=P!・B_finの全次数flatは従わない。`thm:relative-finite-as-cover` は全Bₙ平坦・全fiber Koszul・Noetherianを仮定し、PPも各局所環のspecial fiber Koszulを要するため、指定点一つのKoszul性を開全体へ供給する定理として使わない。有限型伝播は `thm:noncubic-finite-type-effectivity` で有限LG認識→全fiber比較→全軌道projectivity→Noetherian貼合せ→中央AS4延長により解決した。この依存順序を保持する。

**Artin認識の依存。** DDLで指定還元同型に沿うfoundationを持ち上げ、基底を選んでsmooth chartへ写す。étale近傍の指定点を保つliftは局所環を経由する。局所中央被覆をpullbackし、heart-exactness・AZと `prop:artin-witness-relative-promotion` を使う。根や被覆を追加標識にはしない。全H2点の形式認識に加え、有限型効果性と全体のsmooth Artin性を証明した。

再現：`python3 computations/verify_noncubic_central_hull.py`。QQ(a,b)と非交差・一根共有・一致の三特殊化で、次数2–5の双対商次元6,4,1,0、Frobenius pairing、χの恒等式、二次中心1・反中心0を厳密演算する。形式証明器は用いない。

## 被約noncubic境界の相対表示と局所幾何

本文 `noncubic_boundary_comparison.tex` に証明を集約する。正規形で有限foundationを同定しただけではheart比較にならないため、構造対象を保つ相対tilting→Serre→全次数反Serre環→pointed AZを通す。相対慣性核は、標数零で全幾何fiberがreduced一点となることから微分零、単位切断が全射開埋込みとなり、非被約底も含めて消える。これとsmooth chartの因数分解を組み合わせる。

χ=1の一根共有から一致への特殊化は、穿孔直線上でfppf局所定値である。任意代数空間への射がその二点を識別できないことは、étaleなscheme chartを使って直接証明した。Alper2009 §2のquasi-separated規約を任意の代数空間へ無条件に広げない。DM開の慣性がproperでないことは、uv,(u−v)(u−t²v)のDVR族で、generic自己同型の行列式が−t⁴となりPGL4上に延長できない例で証明した。粗モジュライはKeel–Moriからではなく、二つのchartと有限商 [A¹/μ2] の普遍性で構成する。任意底変更後も不変式環は基底環に等しい。非good性はPからcodim2の一致部分を除いた非affine開とHartogsを用いる。

一致類の連結慣性のHH²重みは±2,0,0。交代形式を正確に保つトーラスであることを確認したため、法束の同定にconformalな指標補正はない。有限成分も含む作用と、H2・被約境界の形式対は `prop:noncubic-coincident-full-normal-representation` と `thm:noncubic-coincident-formal-pair` で確立した。ruling交換を閉点の行列作用だけで済ませず、相対mutationにより全Artin変形上で同定する。AHRが与えるのは共通étale商近傍であり、その局所計算だけから大域化はしない。全H2のgood moduliはCの明示GIT開で別に構成した。ambient X3の偏極まで含む形式近傍の同定も別に残る。

## 一致根対の局所偏極構造：次の認識問題

X_asはsmooth83次元、対応するX3の接次元は84である。余分な方向は `cor:artin-polarization-retraction` のHH¹であり、H2自体の障害ではない。次は、Artin基底の偏極をcanonical反Serreと閉fiberで恒等となるpointed自己同値の合成として表し、偏極忘却の形式近傍を慣性の恒等切断の形式近傍と比較する方法を調べる。この比較は未証明で、接空間の分裂だけから高次方程式・成分数・局所閉性を推論しない。非被約境界の二行列式と、既存の有限双加群比較空間が具体的な入力となる。

## 固定Ore被覆の一次持上げ計算

`computations/verify_noncubic_cover_tangent.py` は、R=Q上でf₁=uv、f₂=(u−av)(bu−v)、δ²=1−abとし、σ(u)=(u−av)/δ、σ(v)=(bu−v)/δ、σ(c)=d/δ、σ(d)=−δcを用いる。対象は適合根に対応するB_f^σであり、untwisted環と区別する。被覆の関係はcentralityの5本とr_c−r_d/(1−ab)の合計6本である。

| 二根対の配置 | (a,b,δ) | Gr(7,16)内の三次平坦接の次元 | 正規線持上げ行列の階数 | 全基底接を加えた階数 |
| --- | --- | --- | --- | --- |
| 非交差 | (1,−3,2) | 18 | 22 | 22 |
| 一根共有 | (0,−3,1) | 18 | 22 | 22 |
| 一致 | (0,0,1) | 19 | 22 | 22 |

二次双対E=B!のnormal元wに対し、wξ=T(ξ)wをE₃の8次元商で線形化する。未知数はδwの7個とδTの16個であり、商射の変動は理想の変動を引いて計算する。三配置で正規化自己同型はdiag(1,1,−1,−1)、23変数の核1次元はwのscalarのみとなる。したがって選んだ被覆のprojective normal lineは、これらの点で全ての三次平坦な一次方向へ一意に持ち上がる。これは固定Ore被覆の厳密有理数による一次確認であり、この特定の被覆の高次存在は主張しない。同じ根に対する別の中央AS4被覆は上の一般定理で全Artinへ延長した。一次式の規約と商射補正は独立に読取り点検した。

再現：`python3 computations/verify_noncubic_cover_tangent.py --case generic`、同じコマンドのcaseを`shared`、`coincident`に変更する。各実行は入力と階数を出力しassertで検査する。SymPy以外の追加依存、乱数、外部入力は不要。untwisted B_f!のnormal pencilを、そのまま適合rootでtwistした双対に残るpencilと解釈しない。

## 論文の責任範囲と検証を要する依存

Aの主論文 `papers/nc-quadric-classification.tex` は体上の強いH2の構成・完全分類・pointed exact同値判定を中心とし、20の分類分割節を読み込む。Bの `papers/nc-quadric-moduli.tex` は相対定義・変形・有限型効果性・Noetherian性・Serre根・境界の群商と慣性・good/coarse moduli・楕円型忘却の証明本文を31分割節に保持する。Cはquiver/QP/avatarの表示と相対適合性の未解決範囲を扱う。

**依存の核心。** BがAの体上分類・normal helix・有限同値判定を使うのはよい。BからAへの残余ラベル参照17種類はAの現行20節に実在することを確認した。Aから外した相対節はBの同名節（相対定義は分割された二節）に定理ラベルと証明数を照合し、未使用の重複sourceを現行一式から外してある。数値・例・計算的証拠と全体の相対認識・代数性の証明を混同しない。

## 検証範囲と再現手順

**現行C v4.21の確認範囲（2026-11-23、日本時間）。** 今回は二traitのRees graph・全blowup chart・交互収縮・最小性・自由符号商、自然な順序付きFricke像の二次線束延長、一致型の模型同型・四捩れ補正、構造層の高次順像とPerf引戻しを分担し、統合内容を相互読取りした。Stacksのblowup・有限自由作用の商・形式関数定理を一次本文で照合した。`verify_spectral_boundary_models.py` は12項目の厳密計算PASS。全halving式・pencil多重次数・全群作用と平方根overlapも含む。大域降下、二収縮のPerf像、全有限分岐後の平方根障害、全halving torsorの証明も相互読取りした。さらに代数的target chart・flat good-moduli性・DM開の非完全直像、およびspinorの反Serre生成障害と全四位相を独立読取りした。Alper刊行版の定義・fpqc降下を一次確認した。 全point schemeのscheme論的計算・任意底の普遍族・孤立二点の順序被覆、頂点idealの必要十分判定、全AS型の標準頂点分類を二名が独立に読取りした。Aのcubic逆構成は適用範囲と結論を再確認し、内部証明全体を再監査したとはしない。RSS2020のLemma6.6とProposition6.10の証明を一次照合した。 相対行列式開・普遍Cartier壁・非被約底の反例、rank16から24へのcone・K内部共役降下・E3の同じheartでの認識を独立読取りし、Stacks 0B91・07Z6・0E6Bの一次本文を照合した。 中間二頂点の実normal窓、相互AZ生成による同heart判定、実際のcubic族回復とlinear除外を独立読取りした。Keller1994 §§4.3,8.2のcompact生成・双加群Moritaを一次確認し、Bの普遍cubic平坦性・Noether性の適用範囲も確認した。基底平坦compactのExt次元・四対象のAZ生成・opposite認識・左右Noether性・packing・係数束付きAS解消を独立読取りした。OACU2026 Theorem7.3とKeller Theorem6.10の著者訂正を一次照合した。finite square↔normalの核・余核、K/S2、joint全射の反例、全H2のrank81降下、回転/mutationの双対heartと非被約scheme壁を独立読取りした。`python3 computations/verify_symmetric_morita.py` には回転/mutationのGram行列と全次数式、rank81の全次数式を追加し、7群の厳密計算をPASSした。七矢三関係の非最小有限表示、短対角解消、ordinary Jacobian、δを残す相対AS解消も独立読取りした。全H2開の四交差条件・両rank3正規形・20式判定と全域境界の正規化を独立読取りし、VdBの定義5.3.1・補題5.3.3・定理5.5.10を一次照合した。`verify_square_h2_open.py` は9群の厳密計算PASS。Lieblichの重み零降下とAntieau–Elmantoの古典ruling blockも一次本文で比較した。三半不変式、共通χ0の飽和貼合せ、全H2の準射影good moduli、cubicの12/18式と既存GIT開、境界の符号直像消滅・正規像・nonCartesian一次厚みを独立読取りした。`verify_square_h2_semiinvariants.py` は7群PASS、20式検算9群も再実行PASS。Alper刊行7.9・13.2・13.6・4.14とOU2014 §3の不変環を一次確認した。Cartan不変式、二補曲線のradical、唯一の交点と通常節点を三名が独立に読取りした。`verify_cubic_adjugate_invariants.py` は16項目PASS。MOU2019 Theorem1.1・§5.3とOU2025 Definition1.1・Theorem6.4を一次資料で比較した。反転貼合せ・重み二を含む固定scheme・A³の直線の補・全域GIT射・非proper性を独立読取りし、`verify_cubic_inversion_global_maps.py` の21項目をPASSした。Alper刊行Theorem6.6のlocally Noetherian仮定と代数空間への普遍性を一次確認した。B v0.41の変更はCへの結果の案内と日付で、Bの既存証明を変更していない。`python3 scripts/check.py papers` はPASS（A:22ファイル・139ラベル・137引用、B:32・501・225、C:41・720・224、明示的な論文間参照145件）。新スクリプトは通常math suiteへ登録したが全既存suiteは再実行していない。前回確認した相対Morita/Serre、spectral gerbe、TF認識と四本の検算（spectral15項目）の結果は保持し、今回再実行したとはしない。現行LuaLaTeX buildは依存不足でSKIP、PDFの生成・表示確認は未実施。形式証明・外部査読・A/B全証明の再監査・網羅的新規性照合は未実施。


**現在の再編の検査境界（2026-11-22）。** Aの主原稿は分類20節、Bは相対モジュライ31節である。Bに移動した節のTeX root・主要environment対応・文献キーは節ごとに確認したが、現行3原稿で `scripts/check.py papers` は実行PASS、LuaLaTeXの実組版は依存不足により未実施である。再現用に `scripts/check.py papers` コマンドを追加した。AからBへの証明移管を、移動先の全数学的独立監査や新規定理の形式証明と読み替えない。検算済みの具体的な多項式恒等式は以下の既存の厳密計算の範囲に限る。

**現行版の追加検証（2026-11-22）。** 境界の相対表示・特殊fiber・全慣性・任意代数空間への非分離に加え、DM開の粗モジュライの任意底変更、Hartogsによる非good性、DVRによる慣性の非proper性、全有限成分の法表現、相対ruling mutation、AHRを用いる形式対と局所不変式環を独立読取りした。`verify_noncubic_boundary.py` の既存検算に、DVR自己同型、fiberの微分、全16次元Grassmann接空間・rank12の軌道・4次元HH²と有限成分の作用の厳密検算を統合してPASS。`verify_stack_symmetries.py` も再実行してPASS。全旧suiteは再実行せず、形式証明器も用いていない。

**既存の有限型代数性の検証範囲。** 主論文v1.44の有限LG認識、非被約閉部分の正規形、全fiberからの全軌道比較、普遍Noetherian貼合せ、中央AS4延長、全体atlas、普遍cubic族の降下と既約性、被約境界の余次元2とsmooth降下、ambient非開性を独立読取りした。`verify_lagrangian_recognition.py` は一般係数の多項式恒等式としてisotropy、rank(3,3)、二つのcross行列式1と(α²+βγ)⁴、階数一outer productのcross行列式(det Y det ν)²を厳密検算しPASS。有限線型代数の補助検算であり、全次数定理やstackの形式認証ではない。新規性の包括的確定・形式証明器の確認は未実施。

**現行版の組版制約。** 現在の環境ではLuaTeX-ja等の必要TeXファイルを利用できず、`bootstrap.sh --with-tex` は既存root/sudo権限不足により導入できなかった。C v4.21のbuildはSKIP（終了コード2）で、新しいPDFの生成・画像確認は未実施である。過去版の組版記録を現行原稿の確認と読み替えない。三稿のソース参照確認は現行版でPASS。新しいClifford作用行列の多項式恒等式、および全Lagrangian接空間上の二行列式の微分q33と(α²+βγ)q22の独立性もPASS。

**現行追加部分の確認。** Lagrangian slice、楕円全標識と忘却判定、中央AS4被覆、局所中心線の延長と指定同型付き全Artin認識を独立読取りした。五頂点bar解消・末項の消去・導来torsion kernel、局所Noetherian持上げと全有限型基底変更へのArtin昇格も適用仮定を照合した。Gale計算は三例、off-diagonal反例、一般係数6×6行列を厳密SymPyで検算PASS。中央被覆はQQ(a,b)と三特殊化で双対商次元・pairing・中心/反中心を厳密検算PASS。両スクリプトを通常math suiteへ登録したが、全旧suiteは再実行していない。形式証明・外部査読・包括的新規性確認は未実施。

**既存入力の検証範囲。** 2026-11-21にローカルcheckoutでdoctorを実行した。中心変数のχ保存、一般coherent Hom、任意係数H¹消滅に加え、cubic tailsのunbounded導来局所化・全helix/矢/shiftの比較・一様cohomology・全χ・相対条件への昇格を独立読取りした。旧計算suiteは再実行していない。数学的読取り、厳密計算、組版、保存は別の状態であり、外部査読・形式証明・包括的な新規性判定は未実施である。

**主論文の既存入力の点検。** 全H2のKoszul性・PPによる相対全次数平坦性、Artin基底のnoetherian持上げとqgrのflatness、相対AS被覆の有限判定、fppf像の反例、Zhang族の中心・一次交換子は独立読取りを行った。相対定義は局所canonical compact条件に整理し、大域canonical導来降下の未閉鎖な比較を依存から外した。体上回復はfoundationのcompact generator、有限段Ext計算、flat Hom基底変更、標準hull/Oreの体拡大を点検した。接次元5対4の既存証明は、接複体の[-1,0]切断と代数群としての慣性Lie比較を補強した。体上分類全体の再監査は今回の作業には含めない。

**Artin再構成と一次構成の証明の点検。** 有限foundation上の局所閉比較、DDのArtin適用条件、Morita持上げのheart exactnessとAZ、偏極忘却のHH¹核、HH¹=0点の関係式空間の滑らかさ、近恒等DPicの平方根補正と曲率障害を独立読取りした。Artin witnessの全有限型基底変更への昇格はEnd・可逆双加群・軌道Homの基底変更を個別に確認した。可換点の一次AS構成はPBW、Koszul/Frobenius、斉次Ore恒等式とHKR係数、flat qgrと全軌道の飽和、右Zhang twistの符号、相対族への昇格まで点検した。二乗零理想I全体への拡張とmodule-object系の一意性により、内在的な一次接空間の同定も確認した。これらは人間による査読や形式証明器での検証ではない。

**全Artin hullと根一意性の点検。** 二周期cubic列の相対hullについて、逆coevaluationの貼合せ・二周期との整合、正規性のtensor縮約、相対双対性と正則商、全有限型基底変更への昇格を独立読取りした。近恒等DPicの次数商と中心の帰納法、根の先頭差の消去による一意性も独立点検した。一般cubicへの条件付き拡張では、添字付きcubic解消の次数六と特殊fiberのcanonical hullを原典に照合した。これに基づく全Artin相対H2実現と形式変形groupoidの比較を原稿へ統合した。これは数学的な読取りであり、形式証明器の認証ではない。

**一次構成の有限記号計算。** `computations/verify_quadric_first_order_roots.py` を実行し、一般の十係数二次式に対するγ_f(q,x_i)=0、{x₂/x₀,x₁/x₀}=2f/x₀²、Segre制限のrank9と核kq、四根の固定次元9/3/5/3をSymPyの厳密演算で確認した。相対AS性・圏の平坦性・相対H2所属は、この有限計算の認証範囲には含めない。軽量な通常math suiteに登録したが、今回全旧suiteを再実行していない。

**可換点の独立な接空間証明書。** オプションの `computations/verify_commutative_quadric_tangent.py` を実行PASS。O(2,2)のtoric単項式から三次制約の16072×1400整数行列を直接構成した。法101で制約rank1311、PGL9軌道と九つのJacobian・六つのZhang方向を順に加えたrankは74/83/89。全95列が整数のまま全制約を解くことを確認したため、標数零でも制約rank1311、接次元89となる。さらに軌道の六つの独立な整数依存関係により軌道rank74の上界も確認したので、商の接次元15は厳密である。固定長整数の積には桁あふれの上界検査があり、残差の絶対和上界は44800<2³¹。これは内在接dim9・偏極核dim6の証明とは独立な有限線形代数による照合である。NumPy/Numbaを要するため通常suiteへは追加しない。

**主論文の既存計算の確認範囲。** GitHub mainから取得した `computations/verify_noncubic_second_order.py` をそのまま実行してPASSした。importにより25 unit pivot、六係数回収、全16072×1400線型条件の階数、標数零の有理核83/83/84も再実行される。横断2/2/3方向の基底と全二項和について3/3/6個の二次補正を検証し、二根対一致の場合の分母は2,1,2,2,1,1。残差は整数演算で厳密に零である。全次数の平坦性はこの有限計算ではなく、PPの定理と本文の適用による。新しい `computations/verify_antiserre_polarization.py` も実行PASSで、中心一次部分dim1→0とorbit rank79→80を標数零で確認した。全て有理数・整数・有限体による計算で、浮動小数点近似を用いない。

実行環境はPython3.12.14、SymPy1.14.0、NumPy2.3.5、Numba0.68.1。NumPy/Numbaは重い検算のオプションで、標準math suiteの必須依存にはしない。別稿の作成に伴う全旧math suiteの再実行はしていない。

```sh
python3 scripts/check.py doctor
python3 scripts/check.py sources
python3 computations/verify_noncubic_second_order.py
python3 computations/verify_antiserre_polarization.py
python3 computations/verify_quiver_avatar_charts.py
python3 computations/verify_quadric_first_order_roots.py
python3 computations/verify_quadric_finite_windows.py  # 両parityの長さ3〜7も検算
python3 computations/verify_noncubic_gale_root.py
python3 computations/verify_lagrangian_recognition.py
python3 computations/verify_noncubic_boundary.py
python3 computations/verify_noncubic_central_hull.py
# NumPy/Numba を入れた場合の独立な接空間証明書
python3 computations/verify_commutative_quadric_tangent.py
python3 scripts/check.py sources --manuscript papers/nc-quadric-avatar.tex
python3 scripts/check.py build --manuscript papers/nc-quadric-avatar.tex
latexmk
```

**別稿の論理点検。** QPの消去と慣性、有限foundationの開条件・関係数・重なり、avatarの支持補題・消滅・垂直fiberのTor・非被約基底への直像と降下、weighted stackとSigma2の反Serre障害は独立読取りを行った。全AS同型類分類の再監査、相対AS/avatar同値、適合H2部分の開性の証明は含めない。

**別稿の計算実行。** `computations/verify_quiver_avatar_charts.py` を実行し全PASS。Sigma0/Sigma2のCox単項式でHom次元 `(2,2,2,4,4,6)`、結合律、二つの核の非分解性、短い関係の重なり零を確認した。生成矢・関係・完成矢はSigma0で6/2/8、Sigma2で8/4/12、合成したrank(3,4)の有限代数で7/3/10、product collectionで8/4/12。整数・有理数による有限例の検算であり、合成例のAS正則性、全AS分類、stack開性、相対H2条件を認証するものではない。この軽量スクリプトは通常のmath suiteにも追加したが、今回全旧suiteは再実行していない。

**組版・参照確認。** 2026-11-21に主論文v1.40のLuaLaTeX・latexmk組版を実行し、273頁のPDFと同じ出力先のSyncTeXを確認した。最終logにWarning・Overfull/Underfull・文字欠落・未定義参照はない。Lagrangian表示、中央被覆、五頂点窓、局所AS4、全Artin認識、楕円忘却の選択21頁（234–250、266–269）を画像確認し、そのうち239・243・247・248・249・250・268頁を個別表示で詳細確認した。sourcesはPASS（47 manuscript files / 567 labels / 262 citation uses / 7 Markdown files）。既存全頁の個別目視とVS Code UI操作は今回行っていない。別稿v0.1は変更せず、既存の組版・画像確認の範囲を維持し、今回の再組版は行っていない。

既存入力の独立点検範囲は、全分類のD1–D3・有限K・同値判定・根選択独立、standard/non-standard全帰着、退化型のPic・貼合せ・Serre比較、foundation/ruling/慣性・degree gerbe、cubic稠密性・特殊化・relative bar分解である。証明は現行原稿に保持する。既存の有限検算はSegre積、Ore正規性、全非整型四つ組、period square、群関係・χ・局所対合等を対象とするが、今回の新定理の計算機による認証ではない。

導入は [CLOUD_CODEX.md](../CLOUD_CODEX.md) と `bash scripts/bootstrap.sh`、依存は `requirements.txt`。checkerのPASS/FAIL/SKIPは実施成功・失敗・未実施であり、数学的完成を自動判定しない。git読取と書込認証は別であり、CLI pushが認証不足ならGitHub connectorの通常コミットも使用できる。研究repoを先に保存し、最新research-hubを読んで該当項目を反映する。
