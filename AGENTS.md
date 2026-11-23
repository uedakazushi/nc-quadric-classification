# 研究リポジトリの作業指示 — nc-quadric-classification

2026-11-23 / v1.69。論文Aはv1.69（20節）、論文Bはv0.41（31節）、論文Cはv4.63。

## 公表用三論文の役割

- A：`papers/nc-quadric-classification.tex` を主原稿とし、構造対象付きの全体上の分類と同値判定を自己完結にする。
- B：`papers/nc-quadric-moduli.tex` は内在的相対モジュライの正本とし、相対Koszul・Artin変形・有限型効果性・境界幾何の証明を保持する。
- C：`papers/nc-quadric-avatar.tex` はAS代数・potential・anticanonical avatarの分類と内在的H2への比較の正本。分割節は `papers/quiver-avatar/`。体上AS分類、E_f側の全noncubic相対pointed認識、smooth spectral avatarの双対対応と境界延長不能を区別して記述する。任意のAS/avatar/QP表示stack全体とH2との相対同値は主張しない。

## 最上位目標：論文Cの全相対スタック分類（Codexの固定終了条件）

**最上位目標を2026-11-23に変更した。** `papers/nc-quadric-avatar.tex` に、指定最小AS分解型（square/rotated square/cubic/独立AS10）、その幾何avatar、重み付き8/10/12本矢QPの**全相対fppfスタック**を、非被約基底・同型層・自己同型/慣性・無限周期AS再構成・相対heart・rigidification/gerbe・mutation/rulingの貼合せ・内在的 $H_2$ への適合/非適合部分まで**正確に分類した原稿上の証明**を完成させる。任意のAS/QPという表現は指定型内の全対象を指し、無条件に全次元・任意箙へ拡張する意味ではない。都合のよいperfect/smooth/$H_2$族だけに対象を狭めて全分類と判定しない。

**達成条件は研究方針のS1–S6すべて**。従来のC1–C3（体上AS/avatar、$H_2$開QP/foundation/heart/GIT）は重要な原稿上の成果であってS1–S5の全体ではない。従来C4は独立監査・文献・組版を扱う新S6の一部。これら旧C1–C4だけを達成しても停止しない。新しい主張のない計画整理・反例候補・計算PASS・一つの補題・commitも終了条件にしない。

**比較対象を混同しない。** 未修正QPとAS/avatarのstackは通常同値ではない（可縮pairの $B\mathbb G_m$、二mass核、頂点scalar、mutation時のright-equivalence障害）。全raw QPのAS性を仮定せず、AS適合軌跡と未適合部分、rigidification後の比較、同型層の核と余剰慣性を求める。各主張の範囲（幾何fiber/flat family/任意非被約底/任意raw right-equivalence）を明示する。既証明のspectral境界の $H_2$ 延長不能・stack自己同値不存在と矛盾する無条件の同値は主張しない。

**最初の研究単位（開始時に必ず優先）。** `as_helix_classification.tex` の体上分類、`as10_mutation_classification.tex` の相対perfect条件、`relative_square_foundation_stack.tex` の相対foundation、`qp_presentations.tex` のQP慣性、`cubic_qp_foundation_groupoid.tex` の二mass比較を読み、AS/avatar/QP各相対stackの対象とIsomを現行Cで定義し、`thm:qa-as10-relative-families` のflat/perfect条件が全AS族で自動かを判定する。第一検査は双対数 $k[\varepsilon]/(\varepsilon^2)$ とrank3壁（nilpotent massを含む）、古典squareを使う。必要なrelative lemmaを証明し、反例があれば原稿に適用範囲を訂正して正確な代替atlasを作る。ここで同型層・基底変更・全相対AS復元の最初の未完成な矢印を閉じる。終了するまで漫然とC4の公表前編集だけを繰り返さない。

**Codexの継続規則。** 成果を論文C本文に証明付き統合し、現在有効な研究ノートと方針・READMEを置換更新する。主張状態を「証明済み／追加仮定付き／未証明／計算観察」に区別する。根本的障害で一課題が詰まっても、役立つ反例・不足補題を記録し次のS1–S5課題へ移る。15分以内を目安に通常commitとmainへのfast-forward pushを行い、成功確認後も実行環境の限界まで研究を続ける。研究の区切りには対象repoを先に保存してからresearch-hubの該当項目を更新する。force push、GitHub Actionsの追加・起動、旧版ファイルの累積はしない。認証・組版不足は未実行と正しく記し、研究そのものを停止する言い訳にしない。

## Cの現在の到達点と比較範囲

**C3追加：相対finite foundationのHH/HC/HC^-複体のfppf Čech homotopy降下を原稿上証明（C v4.62）。** `prop:qa-q12-fppf-cyclic-complex-descent`、`cor:qa-q12-finite-foundation-cyclic-complex-descent`。有限foundation Isomに自然で、mass/shearは有限側の複体上で恒等。ただしcanonical Casimir cyclic primitive / negative cyclic CY classの指定元のhomotopy-coherent群oid降下は**未証明**。ruling交換・raw QP比較も未解決。一般非平坦底変更のHC^-同型とfppf Čech降下を混同しない。C4のv4.61時点の全稿静的集計はv4.62更新後の再検証ではない。今回の局所的な新ラベル・引用参照点検を、全稿`scripts/check.py`・LuaLaTeX組版・独立証明監査・形式証明器での確認に読み替えない。


**最優先：論文CのC1–C4完成。** $H_2$実現可能開では`thm:qa-q12-h2-serre-dg-formality`により全tensor次数のcohomologyが次数零に集中し、ordinary Serre dg完成はJacobianへ準同型。非最小二mass有限foundationでは二項準自由dg解消（rank32自由道/8関係道、6R split条件）を直接構成し、Keller Proposition6.8から非完備Ginzburg dgとの**局所導来Morita同値**も原稿上証明（`prop:qa-q12-semifree-ginzburg-morita`）。H2上でordinary Jacobianとの局所導来Morita同値（`cor:qa-q12-h2-ginzburg-jacobian-morita`）を得る。有限道と関係idealの二項dg模型は$\mathscr F\simeq F\oplus I[1]$とintrinsicに同定され、有限関係表示の全Isomがstrictに持ち上がる（`prop:qa-q12-dg-ideal-presentation-strict-naturality`）。massゲージは有限$\Lambda$上恒等、lift shearは$(F,I)$不変なのでfinite Morita像でcoherentに単位となる。さらに全有限表示kernelの$\delta=\varphi^\sharp-\mathrm{id}$はsquare-zero idealを値に持ち、$h(f)=\delta(f)[1],h|_{I[1]}=0$で$dh+hd=\delta$。多項式de Rham形式上の明示dgホモトピーが成り立つ（`prop:qa-q12-mass-dg-polynomial-nullhomotopy`）。個々のホモトピーと群の高次coherenceを同一視せず、後者はfinite quotientから得る。raw Ginzburg dg側の各right-equivalenceとの2自然同定は未証明のまま保持する。raw massゲージの恒等からの多項式$\mathbb A^1$右同値経路は$\lambda t,\mu s$が冪零な場合に限る（`prop:qa-q12-raw-mass-a1-path-obstruction`）。非自明な可逆massの$\Gm$ゲージでは経路は存在せず、有限dgの$\mathrm{id}+z\delta$をraw右同値の経路と同一視してはならない。非線形massゲージ・relation-lift shear・線形frameを含む**全多項式right-equivalence**について、Keller–Yang Lemma2.9の逆道Fox微分で非完備Ginzburg dgへのstrict持上げと全合成・基底変更cocycleを原稿上証明した（`prop:qa-q12-ginzburg-polynomial-right-equivalence`）。旧線形frameは系。mass/shear/frameと有限relation表示のdg持上げで生成される**cotangent表示groupoid**に限れば、Keller Proposition3.7/6.6のCuntz--Quillen双対模型を用いたGinzburg--Serre完成のzigzagを2自然に構成し、Keller Prop4.2によるMorita比較の合成・非平坦基底変更cocycleも証明した（`thm:qa-q12-cotangent-keller-pseudonatural`）。$H_2$開ではJacobianまで2自然（`cor:qa-q12-h2-ky-keller-morita-pseudonatural`）。**任意raw QPの非cotangent右同値**やruling間の単一right-equivalenceには拡張しない。これをdg代数のstrict準同型や未剛体化QP全群oidに対する大域coherent降下とは扱わない。$H^{-1}$以下はすべて零であり、その平坦性・基底変更を別の未解決問題としない。**任意非被約局所Noetherian基底上のrelative exact 3-CYは原稿上証明済み**：rank24有限foundationの相対smooth性とKeller 2018 erratumの任意可換係数環上のTheorem1.1から、全二mass有限開の$\Pi_3(\Lambda)$はrelative exact 3-CY。$H_2$実現可能開ではordinary Jacobianもrelative exact 3-CY（`thm:qa-q12-relative-exact-three-cy`）。幾何fiber旧系は帰結。Keller2018のcanonical exact CYは双加群解消の恒等射からreduced cyclic $HC_2$のCasimir primitiveを作り、そのConnes像が$HN_3$のclassとなる。全finite foundation Isomと非平坦base-changeでprimitiveは自然、mass/shearは有限商で恒等ゆえMorita値mixed complexの慣性作用も自明（`prop:qa-q12-exact-cy-primitive-isom-inertia`）。未剛体化全QP stack上のhomotopy-coherent negative cyclic class高次降下、任意raw Ginzburgのcanonical CY class比較は別課題とする。C4では最新mainの全43 TeXをGitHub接続経由で直接読み、ラベル868・相互参照947・引用キー使用241（bib91キー）の静的監査を実施。新ラベル衝突・未解決参照・環境不均衡は検出されない。`scripts/check.py papers`とLuaLaTeX全稿組版・PDF/SyncTeX表示・数学的独立監査は未実行のままとし、成功扱いにしない。全finite Isomと非平坦基底変更の整合を含むが、任意raw QPのGinzburg dg準同型や$H_2$外のAS/avatar stack全体の同値とは別。C1・C2は原稿上達成。C3は`papers/quiver-avatar/cubic_qp_foundation_groupoid.tex`で、二mass十二矢QPの全finite foundation gerbeと余剰smooth gaugeに加え、短い相対対角解消、ordinary Jacobian=H⁰Π₃(Λ)、全H2実現可能開での反Serre全次数・左右Noether/pointed heart、mass/頂点scalarsの二段剛体化とruling S₂-mutation商まで原稿上証明した。**非平坦基底変更の境界を精密化した。** `lem:qa-q12-hzero-nonflat-base-change`は非正dg完成の$H^0$と任意底変更を、`lem:qa-h2-heart-underived-base-change`は通常heart引戻しを$H^0\mathbf Lb^*$とする全Isom2自然比較を原稿上証明。導来引戻し自体は一般に$t$-exactでない（双対数の無限Tor）。**全finite square Isomから相対heartへの$t$-exactな2自然降下は`cor:qa-all-square-isom-pointed-heart-descent`に原稿上証明した。零番の基底線束$M_0$と選んだpointingを区別し、ruling交換は剛体化後のみ主張する。第一優先はこの新C3の独立証明監査と、C4の先行研究比較・全C LuaLaTeX組版であり、C全体を完成したとは扱わない。** 一般QP全体のAS正則性・H2外の全AS/avatar stack比較は未解決。旧raw `H+εyx` の非平坦対角scalarと、actual AS familyの滑らかなmassゲージを混同しない。

**全H2の準射影的良モジュライ。** 左右kernel条件は P(M)=det M、Q(M)=e3(JMᵗJM) の二式へ集約できる。二つの交差行列について s0=(PfPg)³、s1=Pf³Qg²、s2=Qf²Pg³、s3=(QfQg)² とすると同じ指標χ0²⁴を持ち、s1s2=s0s3。非順序H2開は s0,s3,s1+s2 の三非消滅開で覆われる。各開はアフィン商で、重なりは不変な比の非消滅開なので飽和している。全H2と順序付き被覆のgood moduliは半不変環のProjの開となり、分離的・有限型・準射影的なschemeである。幾何同型類を分類するcoarse moduliの不存在と両立する。三式が半不変環を生成するとは主張しない。 [証明](papers/quiver-avatar/global_h2_good_moduli.tex)。

**良モジュライ上のcubic開と境界。** Ordered cubic開は飽和しており、f=1の残余群とχ0次数を比較すると、既存四量子ビット商P(1,2,2,3)の開D+(p_adj)∪D+(q_adj)と同型となる。p_adj=P(Cr(adjT))、q_adj=Q(Cr(adjT))の通常次数は12・18。noncubicのA1χはMへ閉埋込みとなり、cubic/noncubicは同じgood fiberに混在しない。階数因子Dの正規化列の差はruling符号線束で、その直像が零になるため、Dのgood imageは既に正規である。一方、noncubic閉像のscheme逆像は一致点で元のNより厚い。符号慣性が法方向に−Idで作用し、good像が一定の非零横断一次変形を与える。 [cubic比較](papers/quiver-avatar/global_h2_cubic_git_comparison.tex)・[境界像](papers/quiver-avatar/global_good_moduli_boundary_images.tex)。

**Cubic開の不変式方程式。** e_i=e_i(JTᵗJT)、d=det T とすると、16p_adj=e3²−4d²e2+8d³、16q_adj=e3³−4d²e2e3+16d⁴e1−8d³e3。Cartan上のHadamard計算と不変式制限の単射性から全行列上で証明した。被約補集合は C0={d=e3=0} と C1={e3=de1, 4e2=e1²+8d} で、両者はP(1,2)、唯一の交点[2:1:0:0]は通常節点となる。高次イデアル自体の被約性を主張せず、この二曲線と全H2内のnoncubic A1χを区別する。 [証明](papers/quiver-avatar/cubic_geometric_open_invariants.tex)。

**二cubic chartの貼合せと全域GIT射。** 重なりの反転は [e1:e2:d:e3]↦[e3:d²e2:d³:d⁴e1]。両積可逆なordered粗環は k[b,u,v,w]/(uw−v²)、交換はu↔wで、unordered商はA³_(b,s,v)から直線{s=2v,v=4b−8}を除いた開となる。固定schemeは二被約成分、粗二重射はz²=(s−2v)(s+2v)である。全ordered良モジュライから既存WPSへの二つの正則射ρf,ρgを構成したが、noncubic A1χはともにq0=[1:0:0:0]へ収縮される。両射と全良モジュライはnonproper。 [証明](papers/quiver-avatar/cubic_inversion_global_morphisms.tex)。

**全H2の有限square表示とcanonicalなrank81代数。** 四つのrank2束とrank4束への二乗法をパラメータ化するA32の開から、rank16 squareとrank24 normal foundationの全相対stack同値を核・余核で構成した。頂点トーラスKとruling交換S2を含め、Q_fndは((GL2^4×GL4)/Gm³)⋊S2による商になる。H2はその不変開として表され、古典型も同じ有限表示で扱える。二積の合併全射は追加開であり、H2上では成立する。全H2上のTcan=⊕Ei⊗Hom(O,Ei)∨は頂点線束と二rulingの交換を消して降下し、通常のEnd代数はrank81。canonical完成のn次は81(2n+1)²、O角は(2n+1)²で、左右Noether性とpointed tails認識を得る。H2開は二乗法の随伴行列から作る二つの交差縮約とその転置について、kernelがSegreを避ける四条件で完全に判定した。各条件は五生成idealの非零開で、計20式以内（次数16・24）となる。両rank3壁も含み、既存相対開との一致により非被約底でも全groupoidを認識する。四交差条件をさらに同じ指標の三半不変式へまとめ、全H2の分離的・準射影的good moduliを構成した。任意AS/QP族の全比較は別課題である。[有限stack同値](papers/quiver-avatar/relative_square_foundation_stack.tex)、[全H2のrank81代数](papers/quiver-avatar/universal_h2_square_morita.tex)。

**全域の境界幾何。** 明示H2開上のdet f=0とdet g=0は滑らかなCartier因子で、共通零点では二つの微分が独立である。順序付きH2上でSNC、noncubic交点は滑らかな余次元2となる。非順序和因子の正規化は一方の順序付き因子であり、noncubic上の逆像はruling二重被覆、conductorはschemeとしてnoncubic中心である。任意引戻し後のsmooth/reduced性は主張しない。 [証明](papers/quiver-avatar/square_rank_boundary_geometry.tex)。

**回転・第一mutationも同じ相対heartを持つ。** (E1,E2,E3,tE0) と (t⁻¹Z1,E0,E2,E3) の有限Endはともにrank24、完成のn次は64n²+64n+24。双対square heartによって左右Noether性を証明し、全四対象とtを保つtails同値を得た。最小矢の追加成分はcoker μG=O/(δ)であり、階数一の矢束となる条件はδ=0というscheme壁への因子化である。δ=εの一次変形では全幾何fiberがAS10でも最小矢束は平坦でない。この場合も全Hom代数・tailsは平坦に構成でき、七矢三関係の有限End表示から非最小十矢potentialの実際の相対AS解消・双対を得る。[回転・mutationの相対比較](papers/quiver-avatar/relative_rotated_mutated_tails.tex)。

**Canonical squareの全次数代数と相対tailsを認識した。** 基底平坦compactなEに対するExt^{q}(E,K)=0（q>2）を相対Serre双対とinjective cogeneratorから証明し、二段のO軌道被覆でT=⊕EiのAZ2を得た。canonical Serre完成は左右Noetherianで、四頂点展開は全成分・全積と任意scheme基底変更を保つ。係数束を残した実際の単純AS解消と相対Gorenstein双対を構成し、qgrは同じ相対H2 heartと、全標準対象を保って完全同値となる。左右Noether性・heartの基底は本稿の局所有限型siteとし、特異基底での絶対大域次元は主張しない。全幾何fiberが分類済みsquare型である有限族へも適用でき、古典fiberを許す。頂点線束と周期線束は明示的に保持する。[相対AZとtails](papers/quiver-avatar/relative_square_tails_recognition.tex)、[反対代数と左Noether性](papers/quiver-avatar/relative_square_opposite.tex)、[全整数展開とAS解消](papers/quiver-avatar/relative_square_unfolding.tex)。

### 点曲線側の全noncubic相対pointed認識

二つのsquarefree二次形式の根対は相異・一根共有・一致をすべて許す。点曲線 `E_f = Proj(B_f^ab)` は二conicのファイバー積で、smooth/nodal/I2の三型を取る。体上の二根対・square avatar・noncubic H2のpointed分類と、MCM行列からのpencil回収・有限Hom積比較は [point_spectral_isogeny.tex](papers/quiver-avatar/point_spectral_isogeny.tex) に保持する。非対称helixの比較には `(H_1,...,H_4)` の位相と一番頂点のpointingが必要である。

現在の相対比較には対称squareを使う。実際のspinor評価列によってnormal四項を `(B,X_c,X_d,B(1))` へ相対mutationし、全三型で基本Endの階数16、Brauer増幅後の階数30を得る。最後の頂点を共通座標表現で増幅すると、二形式の交換、GL2座標変換、因子スカラー、共通次数スカラーを含む全商 `[P/G]` 上へ階数45の通常代数が降下する。中二頂点は交換され、構造対象の零頂点は固定される。実際の相対spinor generatorにより、局所有限型・非被約基底を含む任意の基底変更と可換なcompact Morita同値を構成した。正本は [symmetric_morita_descent.tex](papers/quiver-avatar/symmetric_morita_descent.tex)、特に `prop:qa-symmetric-square-relative-mutation`、`thm:qa-unordered-rank45-morita-descent`、`prop:qa-symmetric-spinor-relative-tilting`。

有限対角解消と全幾何fiberの前向きExt消滅を用いて、全tensor次数の相対Serre完成を証明した。零頂点の反Serre角は元のpointed heartを回収する。正本は [relative_serre_completion.tex](papers/quiver-avatar/relative_serre_completion.tex)、特に `prop:qa-relative-serre-tensor-base-change`、`cor:qa-rank45-all-degree-serre`、`thm:qa-symmetric-relative-pointed-heart`。この結果はE_f側の全noncubic相対族に適用し、有限次数の検算や全幾何点上の同値だけから相対同値を推論したものではない。

**左右と同変構造。** 本repoは右加群規約を用いる。新しい有限代数は通常の合成による `A=End(T)` とし、右Yonedaで `P_i=e_iA`、`Hom(P_i,P_j)=e_jAe_i` とする。旧上三角双加群表示の階数54代数は、この規約と比較するとき反対環を取る。階数だけの一致から対象対応を同定しない。二形式交換の符号指標を ε とするとcanonical反Serre環は `R_n^can=B_{2n}⊗(det W)^(-n)⊗ε^n`。交換元そのものと指標 ε を区別する。Bの符号を含まない表示は次数線束による正規化であり、canonical環との違いを明記する。pointed qgr、射影関係式表示、境界の同値・慣性の結論は保持する。

### Spectral側の双対対応と境界延長不能

点曲線 `E_f` とspectral曲線 `C_f: y²=f_1f_2` は、根を共有しない場合に二重étale isogenyで結ばれ、一般には同型でない。二捩れ標識付きの両曲線は双対2-isogenyで交換される。spectral square avatarから指定mutation・一番頂点のpointingを用いてAS商圏を作ると、元のH2対象の一般的な同定にはならず、幾何同型類上のAtkin–Lehner対合になる。

標数零の代数閉体上で、この対応は `χ ↦ χ/(χ−1)`。smooth域の自己双対pointed同型類は正確に `χ=0,2` である。曲線のj値だけで判定せず、非零二捩れ標識も保存する。正本は [spectral_atkin_lehner.tex](papers/quiver-avatar/spectral_atkin_lehner.tex)、`thm:qa-spectral-avatar-pointed-involution`、`prop:qa-spectral-atkin-lehner-chi`。

一根共有と根対一致へ退化する二つの明示trait族では、対応先のχがそれぞれ一位と二位の極を持つ。Bのnoncubic境界の閉性と全域正則なχを用い、対応先はH2族へ延長できず、有限分岐trait基底変更でも障害が残ることを証明した（`cor:qa-spectral-involution-no-h2-extension`）。従ってこのsmooth対応を全noncubic境界からH2への射に延長することはできない。同じ指定square変換・mutation・pointingによるspectral Σ2実現にもこの結論を適用する。noncubic由来のrotated零頂点は強いH2外と判定済みであり、一般Pを含む全標準頂点の体上判定は成立した。smooth spectral対応には以下の相対射があるが、粗対合を覆うstack自己同値は存在しない。

### Smooth相対gerbeと特異境界

正本は [spectral_relative_correspondence.tex](papers/quiver-avatar/spectral_relative_correspondence.tex)。smooth域の自然な射 $\mathscr D$ を、順序付き標的へのbanded $\mu_2$-gerbe $\mathscr D^{\mathrm{ord}}$ と、順序忘却の表現可能な有限étale二重被覆に分解した。任意基底変更と両立し、幾何fiberは $B\mu_2\amalg B\mu_2$。相対慣性核は同時符号 $\mu_2$、一般像は全慣性16に対して位数8である。逆gerbeのBrauer像は二conicの類の差で、一般係数体ではindex 4。二次線束 $(M,\mu)$ は実在してもspectral pencilはBrauer障害を持ち得る。

粗対合を覆うstack自己同値、さらに一般点でrepresentableな射は存在しない。一般慣性の中心の二次分裂体は $k(\chi)(\sqrt{(\chi-1)/(4\chi)})$、双対後は $k(\chi)(\sqrt{1/(4\chi)})$ で、inner twistでは一致しない。この否定と、構成済みの非忠実な相対射を混同しない。

二つの境界traitのgeneric像には $g_1=U^2-4t^rV^2,\ g_2=UV+V^2$（$r=1,2$）という全次数平坦な中央二重平方モデルがある。特殊fiberの二周期解消から固定二対象間の $\operatorname{Ext}^n=k$ を全 $n\ge0$ で証明し、$D^b(\qgr B_0)$ の右Serre関手の不存在を得た。任意の重根・零形式にも拡張でき、この表示族内のH2条件は各二次形式の判別式が非零であることと同値。二形式の共有根・一致根対は排除しない。Perf上のSerre公式の不存在や、自然な境界射の構成はこの結果から主張しない。

### 二次積付きTF標的の代数性と全忠実な認識

[境界標的の認識](papers/quiver-avatar/torsion_free_spectral_recognition.tex) で、幾何fiberがsmooth/nodal/I2となる二重被覆と二次自己双対rank-one TF層の標的 $\mathfrak T_{\rm nod}$ の有限型Artin性、affine有限表示対角を証明した。各成分でrank one、曲線の幾何被約性・連結性、有限表示を仮定する。自己双対性から $h^0(M)\le1$、$p_*M$ の分解型を二型に制限し、固定Quotで有界性を示す。非被約spectral曲線全体へ外挿しない。

Balanced開 $h^0(M)=0$ は積の根重複が高々二の二形式商 $[\overline P_{\rm nod}/G]$ と同値。tracezero成分の非退化二次形式の等方線から二形式と全同型を回復し、任意非被約底への降下を含む。元のNは両平方sectionのsquarefree開であり、TF標的への射は全忠実な開埋込み。実際の $(M,\mu)$ を保持するため同時符号は消えない。層を忘れると固定曲線上の核はnodalでμ₂、I2でμ₂²となる。固定被覆へのforget fiberは $[Z_h/S_2]\times B\mu_2$、$Z_h$ は長さ6のmonic二次因子分解scheme。nodalの非自由成分はdual numbers、I2は二変数の平方零環を同時符号で割る。閉点慣性だけでfiberを同定しない。

元の点曲線と符号は $\OO_C\oplus M$ で全境界から再構成できる。[二traitの境界模型](papers/quiver-avatar/spectral_boundary_models.tex) では、指定generic同型のgraphを正則I2/I4模型、自由な符号商をI1/I2模型として構成した。Fricke出力の二次線束は全族上lineで、自然なsmooth射の二trait上のbalanced標的への延長を与える。特殊対象は追加の被約線束成分であり、H2外である。一致型では四捩れ補正による別の元模型同型が存在し、同時符号を保つがconic順序を交換する。構造層を保つPerfの全忠実引戻しから、非可換H2 heartの同値を推論しない。

### 全noncubic上のFricke境界射

**自然なFricke射を全noncubic境界へ延長した。** 順序付きbalanced標的の開 $\mathfrak U=\{\Delta(g_2)\operatorname{Res}(g_1,g_2)\ne0\}$ へ、$\overline{\mathscr D}^{\rm ord}:\mathfrak N^{\rm pres}\to\mathfrak U$ を構成した。$\chi\ne0$ 上で $q=(\chi-1)/(4\chi)$、入力 $(uv,au^2+uv+bv^2)$、$ab=q$、出力 $(U^2-4qV^2,V(U+V))$ とする。補助平方根 $\rho^2=1-4q,\ \ell^2=(1+\rho)/2$ の全選択・全Isomを比較し、smooth射との貼合せと任意基底変更を証明した。線束境界上の全2-fiberは $[\operatorname{Spec}k[a,b]/(ab)/\mathbb G_m]$、重み $(-2,2)$。二つの穿孔枝は各々 $B\mu_2$、一致点は $B\mathbb G_m$ である。特殊出力はH2外であり、H2延長不能の結論を保持する。[大域降下と境界fiber](papers/quiver-avatar/fricke_boundary_descent.tex)。

入力二捩れは線束自体としては延長するが、全有限分岐後の最小正則模型でも二乗自明には延長しない。共通I4の二つのPerf像は互いに包含せず、O保存だけからheartを同一視しない。半周期torsorの一根共有での最小分岐二・一致での全四補正の延長を保持する。形式表示だけから大域射を推論せず、fricke_boundary_descent.texの全平方根overlapと全Isomの降下を使う。

**順序付きFricke延長は平坦な良モジュライ射である。** 実際の代数的target atlas上で $[\operatorname{Spec}R[a,b]/(ab-q)/\mathbb G_m]\to\operatorname{Spec}R$ と表示し、平坦・有限表示・全射、構造層の直像同型とquasi-coherent直像の完全性を証明した。Artin targetを許すAlper Remark 4.4の意味でのgood moduli space morphismであり、任意底変更後も成立する。非smooth locusは一致根対に限られ、射は非分離・非proper。一致点を除くDM開では直像の完全性が失われ、中央μ₂を剛体化した局所模型は原点を二重にした直線となる。順序忘却後の射は一般fiberが二つなので、この良モジュライ性を持たない。[証明](papers/quiver-avatar/fricke_boundary_descent.tex)。

**一般square族の全標準頂点を同じ相対heartで認識した。** 二つのpencil乗法から $U_0=U_3=T$、$U_1=D(\det\mu_F)$、$U_2=D(\det\mu_G)$ を構成し、任意の非被約底変更と整合させた。局所有限型底の実際のflat曲線avatarのrank16 Endから、coneとSerre移動によるrank24 normal窓を作る。両heartの反Serre生成対象が互いのheartに実際に入ることから、AZ解消でcompact Moritaのt-exactnessを証明した。従って各Uiは、同じ相対heartのEiが強いH2構造対象となる条件そのものを表す。Ui上の実際の全次数cubic族とcanonical tailsも復元した。普遍楕円Picard上の二壁はCartier・横断、任意引戻しではFitting閉部分。別定義の全square AS qgr・全AS/QP群oidとの比較は別課題である。[行列式開](papers/quiver-avatar/relative_vertex_determinants.tex)、[相対normal窓](papers/quiver-avatar/relative_avatar_pointed_recognition.tex)、[heart比較とcubic回復](papers/quiver-avatar/relative_avatar_heart_comparison.tex)。

**標準構造頂点のH2所属を全分類AS型で判定した。** Square曲線型では位相0,3は常に所属し、位相1は $GP\not\simeq F$、位相2は $G\not\simeq FP$ のときに限り所属する。Rotatedでは $C=HF^{-2}$ として位相0は $C\not\simeq\mathcal O$、位相1は $C\not\simeq P^2$、位相2,3は常に所属する。最小十本矢型は奇数位相だけが所属し、古典型は全位相が所属する。非被約曲線も含む体上の定理である。頂点ideal商の全標準右射影の有限次元性と反Serre豊富性の同値を証明し、肯定側には実際のcubic/noncubic pointed認識を使う。[全標準頂点の判定](papers/quiver-avatar/general_vertex_az.tex)。

**全point schemeと孤立二点。** 中央二重平方環では全point schemeは $E_f\amalg\{p_c,p_d\}$、shiftは曲線上で恒等、付加二点を交換する。multilinear schemeを自己同型のgraphとして計算し、全truncationの安定化、任意底変更と普遍族を確認した。表示商上の孤立二点は根対の順序付け二重被覆として降下する。graded普遍加群の次数スカラーgerbeは区別する。[証明](papers/quiver-avatar/spinor_pointing_obstruction.tex)。

**Noncubic由来の構造頂点を全四位相で判定した。** 同じ $\qgr B_f$ の二spinor $\pi X_c,\pi X_d$ は、二周期point moduleへの全反Serre軌道からのHomが零となるため、強いH2の構造対象にはならない。H2に属する位相はsquareで0,3、rotatedで2,3、最小十本矢型で1,3であり、全整数へ四周期化する。特にrotated零頂点・最小十本矢型零頂点は除外された。曲線上のpencil辞書や同じHilbert数値だけではこの障害を検出できない。[構造頂点と生成障害](papers/quiver-avatar/spinor_pointing_obstruction.tex)。

### 保持する分類・障害・再開先

| 内容 | 現行の証明・参照先 |
| --- | --- |
| 最小分解型を指定したsquare/rotated AS正則Z代数とavatarの体上分類、全Serre completion、左右Noether性 | [as_helix_classification.tex](papers/quiver-avatar/as_helix_classification.tex)、`thm:qa-as-avatar-bijection` |
| 独立定義の最小10本矢ASとcubic ASからsquare ASへのmutation逆対応、AS10の条件 `G≅FP` | [as10_mutation_classification.tex](papers/quiver-avatar/as10_mutation_classification.tex)、`thm:qa-as10-global-bijection` |
| 非零二捩れ二重壁のsmooth/nodal/I2への限定と全cubicへの到達不能 | [cubic_obstruction_all_loci.tex](papers/quiver-avatar/cubic_obstruction_all_loci.tex)、`thm:qa-as-cubic-reachability` |
| 非対称四項のBrauer重み `(0,α_c,0,α_d)`、階数54の有限Morita代数、一般ruling交換の頂点固定障害 | [twisted_morita_weights.tex](papers/quiver-avatar/twisted_morita_weights.tex)。対称squareで中二頂点を交換する降下と、この頂点固定障害を混同しない |
| 一般点曲線のperiod 2・index 4、半周期によるconic同型と最小次数分裂、分岐根選択四重被覆との非同型 | [half_period_ruling.tex](papers/quiver-avatar/half_period_ruling.tex)、[root_descent_brauer.tex](papers/quiver-avatar/root_descent_brauer.tex) |
| 共通spectral incidenceでもOU四重torsorとnoncubic半周期torsorは非同型、2-torsion群スキームと自然な二同種Kummer像も不一致 | [half_period_ruling.tex](papers/quiver-avatar/half_period_ruling.tex)、`thm:qa-ou-half-period-common-incidence-not-isomorphic`、`cor:qa-ou-half-isogeny-kummer-classes-distinct` |
| 全二形式族から二次積付きtorsion-free spectral groupoidへの相対射、共有根でのPicard延長障害、最小解消後の奇数次数障害 | [nodal_resolution_obstruction.tex](papers/quiver-avatar/nodal_resolution_obstruction.tex)、`prop:qa-spectral-quadratic-stack-map` |
| 反標準曲線の二pencil、square/rotated変換、finite foundationのscheme復元、canonical四項完全列と全整数前向きExt消滅 | [square_rotated_foundations.tex](papers/quiver-avatar/square_rotated_foundations.tex)、[canonical_helix_complexes.tex](papers/quiver-avatar/canonical_helix_complexes.tex) |
| smooth cubic VdB↔square公式、O保存r1商、potential→avatar 4重・H2合成8重、H2 foundation開とruling二択、OU慣性と有限多項式 | [avatar_charts.tex](papers/quiver-avatar/avatar_charts.tex)、[git_comparison.tex](papers/quiver-avatar/git_comparison.tex)、[foundation_charts.tex](papers/quiver-avatar/foundation_charts.tex) |

十二本矢は通常八本のfinite foundationに四本のrelation-dual戻り矢を加えたQP表示であり、任意の十二本矢QP全体をAS正則としない。二つの特定mutationが失敗することだけで全cubic foundationの不存在を推論しない。OUと半周期の同じD4 monodromyから被覆・有限群スキーム・Kummer類を同一視しない。

## Cの残課題と検証方針

- E_f側の相対mutation、全商降下、Serre完成、pointed heart回収、およびsmooth spectral相対射・gerbe分解を未解決へ戻さない。stack自己同値とH2境界延長は不存在が証明済みであり、単なる証明不足と記さない。境界の具体的な平坦代数モデルを出発点とし、自然な射の延長先とその同型層を調べる。
- 任意のAS/avatar/QP表示stack全体のright-equivalence groupoid、一般cubic域の表示忘却fiber・慣性、既存GITとの相対比較は別に検証する。体上AS分類や特定noncubic族の相対認識から全表示stack同値を推論しない。
- 節点曲線上の二次積付きTF標的の代数性・有限型性、balanced開・元Nの全忠実な開埋込み・全慣性は証明済み。二traitのgraph閉包・半安定修正に加え、自然Fricke射の全表示群同変な境界降下と全fiberも証明済み。全分類AS型の標準頂点を体上で判定した。二つの乗法行列式開と同じ相対heartのpointed認識も証明済み。finite squareとnormal foundationの全相対stack比較、およびH2開の20式判定も成立した。全域determinant境界と大域good moduliも構成した。境界像とcubic開の飽和性も確立した。Gram二形式pencilによる全半不変式環・中央affine chart・二商特異点はC v4.22で原稿上解決済み。rank3壁でのQP右同値・heart・mutation貼合せはC3原稿上達成。相対対角とKellerのordinary ideal条件はEuler--conormal判定によって一般非被約底まで原稿上直接証明済み。非最小QPの双対dg微分・Jacobian/H⁰Π₃の具体式も原稿上明示済み。残余長関係のlift変更に加えてmassゲージとの半直積・変更後potentialへの輸送・双対数の非可換例・頂点scalarsの中心性も原稿上証明済み。全mass frame変更の線束値群への降下、冪零logの線束加法化、strict square対合からの二段剛体化後$S_2$-coherenceもC原稿上証明済み。さらに全nのnormal四周期helix前向きExtとperfect-fiber判定から反Serre tensorの各次数局所自由性・全基底変更を補題化した。今回、反対squareのstrict involutionと四交差開の不変性を証明した。一重rank3の反対normal零番は強いH2外となる明示反例を発見し、誤ったopposite-normal pointed AZの適用を修正した。反対squareのdual heartで逆順双対normalの**第二頂点$Q_0$**を基準に相対AZ2を適用し、非被約底を含む左Noether性を原稿上再証明した。一般AZ命題の仮定を非先頭構造対象も含む$E_a=\mathcal O$へ訂正し、二段Ext消滅・Noetherianな一般End環とcoherent Hom有限性を補題として直接証明した。古典quadric上の第二項Oを持つ反対normalを独立検算。主原稿と全42節の主要環境・各節内ラベル、計235件の引用キーとbib90キーを静的確認（いずれも検出異常なし）。反対normalのheart所属は相対評価coneの双対から直接導き，幾何fiber比較を可逆層$L$で全非被約底へ持ち上げた（C3・相対mutation節を修正）。頂点可逆層変更の下では評価cone・$Z_1$が同じ線束で捩れ，そのHom線束$L$は不変，反対側は全て逆線束で捩れるのでこの範囲のfppf 2-cocycleは証明済み。有限squareの全頂点固定Isomについて評価cone・相対Serre・dual normalの2自然性をCで証明し，指定mass/shearが有限商に恒等を誘導することからheart比較の余剰慣性は作用しない。C主原稿＋42節で818ラベル一意・868参照全解決・235引用はbib90キー内，禁止Unicode数式矢印を1箇所訂正。scripts/check.py papers実行・全稿LuaLaTeX組版は未実施。次はraw QPの残るIsomとruling/t-exactnessの厳密な適用範囲，C4の実組版・一次文献比較を優先する。非被約spectral曲線全体や別AS heartへの認識は未解決。I2極限は非単純なのでsimple/fine compactified Picardだけに制限しない。
- AS分類の独立監査では、非被約D上のPic0とrank forcing、逆spherical helix実現、全整数評価・余評価、逆mutation、AZ ample cornerと相対perfectnessを一次証明と照合する。Kellerのrelation Ginzburg=3-CY completionには有限代数のgldim 2とminimal relations、Keller–Yang Thm 6.2にはloopなし・mutation頂点の2-cycleなし・potentialの巡回表示を確認する。既に適用条件を記したことと全依存の独立監査完了を区別する。
- 各実行単位は研究方針の現行優先順位に従って選び、本文・ノート・方針・READMEの状態を同期する。低次数・有理係数モデルの検算PASSを全次数定理、降下、GAGA、全導来非同値、新規性の証明と扱わない。旧PDFからの証明移管、今回の数学的点検、一次文献照合、厳密計算、LuaLaTeX組版、GitHub保存、hub更新は別々に報告する。

**最優先目標は論文Cでの指定AS/avatar/8・10・12本矢QPの全相対stack分類**（`papers/nc-quadric-avatar.tex`）。`00_research_plan.md` の**S1–S6**が唯一の完了判定であり、既存のC1–C4は研究の入力・検証単位である。中央affine・全有限QP/foundation群oid・二mass・H2実現可能開のJacobian/Serre/heartとS₂-mutation商は原稿上決着。次はまず全相対AS/avatar/weighted-QP stackの定義・coverage、AS10 relative perfectの自動性、全Isom・QP慣性と非被約基底での比較を進める。既存C3の数学的独立監査、Keller訂正条件、先行研究・LuaLaTeX実組版も並行して進める。A/B監査・文献比較は有効な入力として維持するが、Cの未解決核心を放置してA/Bの公表作業を優先しない。BからAへの17種類のラベル参照はAの現行分類20節に定義されている。これはTeXソース上の依存の監査で、全数学的証明の独立監査ではない。Aの主原稿の相対部分は入力から外したが、未使用の旧相対節ファイルはBに全証明と対応ラベルの保持を確認したうえで整理済み。残るBへの引用・source依存を優先して点検する。`python3 scripts/check.py papers`（A/B/Cの明示的な論文間ラベル参照も検査） を実行して3原稿を別々に検査する。証明移管・数学的検証・組版・GitHub保存・hub更新は別の状態として扱い、外部査読済みとは主張しない。

## Cloud Codexへの継続指示

このrepoの研究継続を依頼された場合の最優先目標は、`00_research_plan.md`の**S1–S6を満たして指定AS/avatar/8・10・12本矢QPの全相対stack分類を論文Cに完成すること**である。C1–C4の達成だけで終了しない。全H2の分類は「完全分類の達成条件」F1–F6を基準とし、達成済みの場合は方針に記した公表前監査・次の研究課題から進める。計画の作成、一補題、一例、一節、検算成功、commit、pushを終了条件にしない。推進できる未解決課題がある限り、保存後も次の実行単位へ進む。「続けますか」と毎回確認しない。環境の開始方法は `CLOUD_CODEX.md` に置く。

1. 最新のhub該当項目、研究方針、本指示、必要なノート・原稿を読む。既存の未commit変更を調べ、他の作業者の変更を保持する。実際のcheckoutと`origin/main`の差を確認し、研究方針の「次の実行単位」から始める。
2. `python3 scripts/check.py doctor`で道具を診断し、`python3 scripts/check.py sources`で構成を点検する。必要な依存のみ`bash scripts/bootstrap.sh`で整える。依存不足はその検証を未実施とする理由であり、証明検討・原稿編集・利用可能な資料の比較まで止める理由ではない。
3. 一つの実行単位では、必要な仮定と到達する補題を定め、証明・反例・一次資料比較・厳密計算のいずれかを具体的に進める。新しい計算は小さい基準例で規約を確認してから拡大し、入力・乱数seed（使用時）・再現コマンドを残す。低次数の成功を全次数の証明へ昇格させない。
4. 主要な主張は、可能なら独立の読取り担当に仮定・推論・反例を点検させる。並列担当には異なるファイルまたは読取り専用作業を割り当て、主担当が原稿・方針・mainを統合する。subagentがなければ、結論を一度疑って仮定と反例を別の観点で再点検する。
5. 同じ障害に再度当たったら、使えなかった理由・必要な不足補題・最小反例候補を研究ノートに現在形でまとめる。研究方針の代替課題へ切り替える。特定の文献・認証・TeX導入に詰まっても、独立な数学課題へ移る。実質的な進展なしに同じ検索・計算・環境修復を反復しない。
6. **切りのよいところで随時、前回の成功したmainへのpushから長くても約15分以内に**、切りのよい数学的単位で現行の本文・ノート・方針・READMEを整え、必要な検証後に通常commitとmainへのpushを行う。この時間は保存の目安であり、作業を終了する期限ではない。保存後は、次に証明すべき命題・具体的な式・参照箇所を方針に一つ指定し、その課題を続行する。
7. 各検証のPASS/FAIL/SKIPを区別する。`scripts/check.py`の成功は構成・計算・組版の確認であり、証明・新規性・完全分類の認証ではない。必要な検証が未実施なら、その制約をノートと報告に書く。環境修復だけを研究成果として報告しない。
8. 最終終了は、完全分類の達成条件を満たして独立点検・保存を終えた場合、ユーザーが停止・変更を指示した場合、または実行環境の上限や不可欠な外部権限等により本当に継続できない場合に限る。後者では現行一式を保存し、未解決命題・使える結果・次の具体的一手と外部制約を方針へ残す。自動的な別セッション起動や無期限実行をAGENTS.mdで実現したとは扱わない。

指定型の全対象の定義・基礎体・同値関係を都合よく狭めて完了判定を満たしてはならない。方法の変更、定理候補の訂正、必要な補題の追加は自律的に行い、有効な成果を現行原稿に保持する。全てのambientや全ての平方根を別々に完全分類することは、H2のpointed exact分類に必要だと証明されない限り終了条件に追加しない。

## 入口と正本

- 全体の入口：[research-hub](https://github.com/uedakazushi/research-hub)。再開時に該当研究の概要、他研究との関係、再開先を確認する。
- 最初に読む研究方針：`00_research_plan.md`。続いて本AGENTS.mdの適用される指示と `notes/research_notes.md`、必要な原稿・検証記録を確認する。
- 別稿B：`papers/nc-quadric-moduli.tex`。相対モジュライ・境界の現行証明本文を保持。数学的な独立監査は継続。
- 別稿C：`papers/nc-quadric-avatar.tex`。八・十・十二本矢の表示モジュライ・avatar・内在的忘却を扱う。分割節は `papers/quiver-avatar/`。個別の `sources`・`build` には `--manuscript papers/nc-quadric-avatar.tex` を付ける。
- 主たる公表用原稿：`papers/nc-quadric-classification.tex`。リポジトリ直下からの相対パスであり、本文のある主原稿とする。節のソースを別ファイルから読み込んでもよい。独立した別論文には内容を表す名前を付け、役割をREADMEと研究方針に記す。
- 本研究の現行ソース・入力・再現資産の正本はGitHubの `main`。研究以外の日常todoは別に管理する。

共通原則の参照先は [CHATGPT_CUSTOM_INSTRUCTIONS.md](https://github.com/uedakazushi/research-hub/blob/main/CHATGPT_CUSTOM_INSTRUCTIONS.md)。実行に必要な規則は以下にも記載し、hubへ接続できない場合にも対象研究の既存資料に基づく作業と保存を進める。未確認のhub情報は推測しない。

## 研究と執筆

1. 数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性から研究全体の価値を最大化する。方針は現在有効な目標、到達基準、成果、核心、次の具体的な課題へ書き換える。一般原則・保存許可と研究固有の計画を分ける。
2. 証明済み、追加仮定付き、証明未完成、予想、計算的観察を区別する。仮定、依存結果、証明の所在、未解決箇所を示す。原稿中の証明、今回の点検、計算、形式証明器、新規性の確認を混同しない。
3. 重要な既知結果と文献情報は一次資料で確認し、Introductionで既存結果との関係を具体的に説明する。他研究から用いる定理にも仮定と出典を付す。未確認の文献内容や新規性を推測しない。
4. 別指定がなければ日本語LuaLaTeXで書く。[論文テンプレート](https://github.com/uedakazushi/research-hub/blob/main/papers/paper-template.tex) と [導入手順](https://github.com/uedakazushi/research-hub/blob/main/papers/README.md) を参考にし、説明文・例を研究内容に置き換える。公表価値のある内容と十分な証明を現行論文に統合し、軽量化のために削らない。主原稿の改名・移動時は分割原稿のroot指定、input、文献、README、研究方針、ビルド・エディタ設定も更新する。
5. 研究ノートは現在有効な知識を整理する。論文外の着想、計算、例、反例、失敗した方法の本質的な障害、再取得困難な情報を保持し、論文の証明は参照する。旧会話、日誌、更新履歴、重複原稿を蓄積しない。
6. 誤りが判明したら、依存する主張と本文・要約・方針を訂正する。有用な反例や障害はノートに保持する。訂正をhubにも反映する。

## 保存と再現

- 現行資料だけで研究を再開できるようにする。必要なソース、入力、証明書、文献情報、依存関係、再現手順を保持する。元資料だけが持つ有用な内容を移行・検証前に失わない。
- 研究の区切りでは、追加の承諾を求めず、必要な通常コミットと `main` へのpushを行う。**長時間作業でも前回の成功したpushから15分を超えないことを原則とし、切りのよいところではそれより早く保存する。** 証明途中でも、成立済み部分・未完成部分・次の具体的一手を明示して保存する。組版・長時間計算・文献調査・独立監査の完了を待ってpushを遅らせない。最新内容と並行変更を保持し、force pushとGitHub Actionsの追加・起動は行わない。
- research-hubの [.latexmkrc](https://github.com/uedakazushi/research-hub/blob/main/.latexmkrc)、[settings.json](https://github.com/uedakazushi/research-hub/blob/main/.vscode/settings.json)、[extensions.json](https://github.com/uedakazushi/research-hub/blob/main/.vscode/extensions.json) を参考に、既存の有効な設定を保持して本研究に合わせる。LuaLaTeX・latexmkとVS CodeのLaTeX Workshopから組版できるようにし、PDFの出力先とSyncTeXを整合させる。program magic commentによるレシピの迂回にも注意する。設定の検査、レシピ相当コマンドの実行、VS Code UIの操作を区別して検証結果を報告する。生成PDF、組版の中間ファイル、キャッシュ、旧版ZIPは原則Gitで追跡しない。数学的内容や検証可能性を損なう削除はしない。
- GitHub管理中はLibraryへの定常的な二重保存やZIP作成は不要。pushできない場合は現行成果を失わないよう緊急保存し、未反映の変更と理由を報告する。Libraryへの別途保存依頼には従う。既存Libraryファイルの削除は明示的な指示なしには行わない。
- 日付・版、ファイル名、参照、記法、主張の状態を整合させる。必要な範囲の組版・検算・参照確認を行い、生成、論理点検、計算、組版、pushの成否を別々に報告する。

## 研究の区切りにresearch-hubを更新する

1. 先に本repoの原稿・研究ノート・研究方針・READMEを現在の内容へ更新して保存する。
2. [research-hub](https://github.com/uedakazushi/research-hub) の最新READMEと適用される指示を読み、本研究の該当項目を更新する。主要到達点、主張の確実性、未解決の核心、次の一手、依存関係、正本・再開先、実際の資料確認日を反映する。誤りの訂正や重要な障害の発見も対象とする。
3. 詳細なtodo・証明・作業履歴をhubへ重複させず、概要と参照先を保つ。実質的な変化がなければ形式的な書換えや日付だけの更新はしない。文書の編集日、コミット日、数学的な検証日を区別する。
4. 他研究の記述と並行変更を保持し、必要な範囲を通常コミットでhubの `main` に反映する。保存された本repoの内容とhubの要約を対応させ、未保存の成果を反映済みと記さない。
5. 本repoの保存とhub更新の成否を別々に確認する。hubにアクセスできない場合や更新が失敗した場合も研究成果を保存し、未反映項目と理由を報告する。指定された公開範囲を維持する。

## 研究固有の規則

- 対象は構造対象のみを指定した `(C,O)`。Gabriel–Krull商でrank one torsion-free、exceptionalを要求する。exact平方根 `s² ≅ S⁻¹[2]`、Artin–Zhang豊富性、二次AS正則持上げの存在は性質であり、`s`・根同型・ambient・方程式を追加標識としない。
- 通常のquadratic envelopeはquadric切断式も含むためAS4にはならない。正しい強い条件は orbit環 `B(C,O,s) ≅ A/(g)`、`A` が左右noetherian quadratic Koszul AS-regular型 `(1,4,6,4,1)`、`g∈A₂` が左右正則正規であること。中心性を無条件に課さない。
- 本repoは右加群規約を使う。`a∈B_m, b∈B_n` に対し `a*b=s^n(a)∘b`。cubic repoの表示された積とは逆の規約なので、Nakayama公式を輸入する際は反対環・左右を照合する。
- 分類の最終目標は全H2対象のpointed exact同値分類。graded環の同型、Zhang twist、root付き同値、derived同値を混同しない。既存のcubic Z-algebra/elliptic quadrupleの分類だけで全H2分類済みとしない。
- 候補データからの構成、全H2からの回復、データ上の同値判定、全領域の被覆を別の命題として証明する。「H2を与える表示全体を取る」や未知のAS/admissibilityを条件に残したincidence記述は、全分類の完成ではない。
- GIT商のorbit closure・S-equivalenceをpointed exact同値と同一視しない。反Serre環で同値類を判定できても、graded自己同型群とpointed自己同値群の一致や相対moduliまで自動的に従うとはしない。
- 主原稿の全同値類分類、全H2の有限型代数性、被約境界の相対商表示・全慣性・DM粗モジュライ・一致類の形式対は確立済み。全平方根・ambient忘却ファイバー、Q_fndとの全体の相対比較、偏極認識は別の課題とし、原稿のラベルとnotesの状態表を維持する。
- N^DM→A¹は任意底変更と両立する粗モジュライだがgoodではなく、慣性は非proper。全H2には粗モジュライ代数空間がない。一致類の共通étale商近傍の局所良モジュライと、Cで三半不変式から構成した全H2の準射影的good moduliを区別し、両者の局所比較を明示する。
- 他repoは必要な一次資料として参照する。`nc-cubic-classification` の完全分類定理を本repoの既知入力にしない。Serre根についての一般研究は `categorical-fano-index`、tensor/quadruple分類は確認済み文献と役割を区別する。
- 次の着手先は研究方針の優先課題。有限次数の計算だけでAS正則性・smoothness・全次数正則性・全対象の被覆を証明したと報告しない。

