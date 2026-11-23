# 非可換 quadric 分類：現行文献比較

## 二対称形式pencilの不変式定理（Cの明示good moduliの入力）

Bhargava–Gross–Wang, *Arithmetic invariant theory II: Pure inner forms and obstructions to the existence of orbits*, in *Representations of Reductive Groups*, Progress in Mathematics **312** (2015), pp. 139–171, §4.2, DOI [10.1007/978-3-319-23443-4_5](https://doi.org/10.1007/978-3-319-23443-4_5), [著者版PDF](https://www.math.uwaterloo.ca/~x46wang/Papers/AIT2.pdf), arXiv:1310.7689。**一次PDFの第14頁（節4.2）を確認**：SL_n が二つの対称n×n形式に作用する不変式環は、二形式のdeterminant pencilの n+1 係数で自由に生成される。本研究でn=4を用いる。SO4上の直交第一基本定理で二つの4×4行列をGram二形式へ移し、common character χ0 の重量零条件を抽出して orderedの五生成・一関係と unorderedの四生成多項式環を得る。これは**先行文献にある不変式定理**と、Cでの**新しい適用（全H2の具体的半不変式環・中央chart）**を区別するための参照である。関連証明は [CのGram pencil節](../papers/quiver-avatar/global_h2_invariant_hull.tex)。

資料確認日：2026-11-23（日本時間）。v2.7。現行三論文A/B/Cに対応する一次資料比較。
以下で「確認」は記載箇所の本文・仮定の照合を意味し、外部論文の全証明を独立に再検証したという意味ではない。

## 全H2の共通線形化と大域良モジュライ

Alper, *Good moduli spaces for Artin stacks*, 刊行版の [本文](https://www.numdam.org/article/AIF_2013__63_6_2349_0.pdf) Proposition7.9（印字pp.2379–2380）、Theorem13.2（p.2399）、Theorem13.6（p.2400）を一次確認した。Affineな線型簡約群商の良モジュライ、共通部分の飽和性による貼合せ、線形化からの準射影GIT商が既知入力である。CはSegreの左右kernel条件をP=det、Q=e3(JMᵗJM)へまとめ、指標χ0=detW/(detA detB detC detD)の同じ24乗を持つ三半不変式を構成する。比による飽和性を直接示すことで全H2の準射影的good moduliを得る。一般GITの存在定理を新規な原理とはせず、全H2への具体的適用と範囲を区別する。3本が半不変環を生成すること、全semistable locusとの一致、射影性やsmooth性は未主張。包括的新規性は未確認。

全H2良モジュライの閉境界にはAlper Lemma4.14（印字p.2367）のclosed-image good moduliと、直像の完全性を用いる。境界符号線束の直像零・normalなgood image・一致点のnonCartesianな引戻しは現行Bのruling交換と法表現を入力にCで証明する。

OU2014 [arXiv:1403.0713](https://arxiv.org/pdf/1403.0713) §3 (3.9)–(3.16),(3.19) の k[f2,f4,g4,f6]（通常次数2,4,4,6）を一次確認した。Cubic gaugeのχ0次数は通常次数の半分となるためP(1,2,2,3)のgeometric開と良モジュライを同定する。既存重み付き射影商を新結果とせず、adj(T)の交差縮約による次数12・18の二式と、全H2の大域線形化との一致を本稿の具体化とする。同本文(3.17)のstability主張やstack birationalityの表現はこの適用には用いない。

Cubic開の新しい二式は、OU2014のCartan制限がW(D4)不変式環への同型であることを用いて全行列へ延長する。Newton恒等式により四生成元をe1,e2,d,e3へ置換できる。これにより既存GITの非geometricな被約補集合を二本のP(1,2)と通常節点で記述するが、先行文献に同じ補集合の別表現がないことまで確認したとはしない。

Mori–Okawa–Ueda, *Moduli of noncommutative Hirzebruch surfaces*, [arXiv:1903.06457](https://arxiv.org/pdf/1903.06457), Theorem1.1（p.3）、§5.3 (5.24)–(5.26)（p.25）、Remark7.1（p.30）を一次本文で確認した。Sheaf bimodule・関係式・滑らかなelliptic quadrupleの双有理比較、四因子tensorの自明scalar核、次数(1,1,2) AS Z代数を考える動機は既知である。本稿の全pointed H2の相対groupoid・noncubicを含むgood moduliとは範囲が異なる。

Okawa–Ueda, *Marked Artin–Schelter surfaces of del Pezzo types*, [arXiv:2508.04986v1](https://arxiv.org/abs/2508.04986v1)（2025）、Definition1.1（p.1）とTheorem6.4（p.8）を一次本文で確認した。Very strong helixをmarkingとし固定quiverのpotential stackのAS-regular開を扱う。Elliptic tupleとの比較は双有理であり、固定markingを忘れた全strong H2の相対同値・全境界good moduliをこの定理から推論しない。Potential stackとAS開の考え方は既知結果として引用する。今回確認した範囲だけから新規性の完全調査済みとはしない。

全域OU射ρf,ρgの構成には、Alper刊行Theorem6.6（印字p.2375）のlocally Noetherianなgood moduliの代数空間への普遍性を用いる。随伴tensorの指標ζfと全H2の線形化χ0を同一視せず、まずstackからWPSへの不変射を作ってから降下する。二cubic chartの反転と固定scheme・粗二重射の計算は本文の環計算で証明する。全良モジュライのnonproper性は閉部分A1χから既に従うため、一般GIT理論の新原理として扱わない。

## 全H2開の明示式と通常代数の降下

Van den Bergh, *Non-commutative quadrics*, [arXiv:0807.3753v3](https://arxiv.org/pdf/0807.3753v3), Definition5.3.1、Lemma5.3.3、Theorem5.5.10（印字pp.13–14,20）を一次再確認した。Geometric quintupleの隣接二因子縮約条件とcubic分類にはlinearな古典型も含まれる。Cの新定理は二積の随伴行列による四交差条件へ移し、両rank3壁も直接認識して全H2開を20式以内で記述する。既存のcubic開の存在そのものと区別し、この具体化の包括的新規性は未確認である。

Lieblich, *Moduli of twisted sheaves*, Duke Math.J.138(1)(2007),23–118、[arXiv:math/0411337v2](https://arxiv.org/pdf/math/0411337v2) Lemma2.1.1.13は慣性自明な層の降下を述べる（番号はこの版）。同著者 *Twisted sheaves and the period-index problem*, Compositio144(1)(2008),1–31、[DOI](https://doi.org/10.1112/S0010437X07003144) の刊行本文 Lemma3.1.1.7とProposition3.1.2.1を確認した。Hom/tensorの重みの相殺とtwisted bundleのEndがAzumayaになる原理は既知であり、rank81構成の新原理とはしない。後者のperiod–index同値には節のintegral Noetherian仮定があるため任意底へ外挿しない。

Antieau–Elmanto, *Descent for semiorthogonal decompositions*, Adv.Math.380(2021),107600、[著者最終稿](https://eldenelmanto.com/wp-content/uploads/2021/01/sodnote.pdf) §5.3 Proposition5.7を一次確認した。古典P1×P1の中間ruling blockの降下と、順序付き精密化を妨げる二重被覆は既知である。本稿の内容は、全H2の内在的squareについてO・S2・全許容基底変更を保つ実際のTcanとrank81代数、全次数完成およびpointed tailsを具体化すること。81の最小性や同様の構成の先行不存在を主張しない。一般の圏降下定理を全stack上のunbounded導来圏に無条件適用していない。

## 相対AZ・全整数展開・relation potential

**相対Serre dg形式性と既知のcompletion一般論の区別（2026-11-23）。** Keller, *Deformed Calabi–Yau completions*（[著者本文](https://webusers.imj-prg.fr/~bernhard.keller/publ/KellerCYCompletions.pdf)、§4・§6、[2011年訂正](https://webusers.imj-prg.fr/~bernhard.keller/publ/KellerCorrCYCompletion.pdf)、[2018年erratum](https://webusers.imj-prg.fr/~bernhard.keller/publ/KellerErratumCYCompletions.pdf)）はinverse dualizing bimoduleのtensor dg completionと関係式QP・Ginzburg dg比較の既知基礎である。本研究の`thm:qa-q12-h2-serre-dg-formality`は、**本稿で既に証明した全normal helixの$P_n$次数零集中**とordinary tensor直和のcohomology交換を使い、$H_2$実現可能開で$\Pi_3(\Lambda)\to H^0\Pi_3(\Lambda)=\operatorname{Jac}(Q_{12},\mathcal W)$がdg準同型となることを直接示す。これは標準的な非正dg truncationの帰結を本研究の相対開に適用したもので、新しい一般formality原理の発見ではない。Kellerの通常relation ideal条件とminimality修正を適用範囲から外さず、非最小raw QPのGinzburg dg模型と同一視したとは主張しない。負次数消滅はすべての$H_2$基底変更に成立するが、$H_2$外の任意の有限foundationへの外挿は未確認。包括的新規性未確認。

**幾何fiberのexact $3$-CY構造の一次確認（2026-11-23）。** Kellerの[原論文](https://webusers.imj-prg.fr/~bernhard.keller/publ/KellerCYCompletions.pdf) Theorem 4.8（印字p.20）を本文とPDF画像で確認し、homologically smoothな入力dg代数のordinary $n$-CY completionはhomologically smooth・bimodule $n$-CYであることを照合した。[2018年erratum](https://webusers.imj-prg.fr/~bernhard.keller/publ/KellerErratumCYCompletions.pdf) Theorem 1.1（p.1）の本文と画像を確認すると、undeformed completionはcanonicalな**exact** $n$-CY構造を持つ。一般deformed completionのnegative cyclic parameter問題は本稿のundeformed相対Serre完成へ持ち込まない。Cでは各幾何fiberの有限双加群射影解消により入力$\Lambda_{\bar s}$のsmooth性を個別に確認し、dg形式性$\Pi_3\xrightarrow\simeq J$を介して幾何ordinary Jacobianのexact 3-CYを得る。これをKellerから無条件な相対特異底上のCY降下やraw Ginzburg dgとの同型へ拡張しない。文献キー`KellerDeformedCY2011`, `KellerErratumCY2018`。

**非最小二項dg解消とKeller Proposition 6.8の一次照合（2026-11-23）。** Keller *Deformed Calabi–Yau completions* [著者本文](https://webusers.imj-prg.fr/~bernhard.keller/publ/KellerCYCompletions.pdf) §6.7, **Proposition 6.8（印字p.28）**をPDF画像・本文で確認。任意可換係数環上でcohomological次数$0,-1$の有限自由なdg quiver（微分任意）にMorita equivalentな入力のundeformed $\Pi_3$は、$V^0\oplus(V^{-1})^\vee$上のpotential$\sum v_j^*d(v_j)$による非完備Ginzburg dgと**derived Morita equivalent**。同§6.9のTheorem 6.10はminimal relationsの条件と2011年のordinary ideal訂正が必要で、本研究の二mass非最小関係へそのまま適用しない。Cでは有向四頂点のrank32自由道・rank8関係道（関係同士非合成）および6Rのrank6直和因子から二項準自由dg解消$\mathscr F\to\Lambda$を直接構成し、Prop6.8の仮定を局所枠付きchartで満たすことを証明した。従って非完備$\Gamma_3(Q_{12},\mathcal W)\simeq_{\rm dMor}\Pi_3(\Lambda)$を全非退化二mass有限開で局所的に得る。$H_2$開では別途得た形式性と合成してordinary Jacobianとの局所導来Morita同値になる。**未証明**は全raw QP未剛体化Isom・ruling交換の大域coherent Morita降下とstrict dg準同型であり、このProp6.8を全stack同値と拡大解釈しない。

**Morita不変性と関係idealのdg自然性（2026-11-23）。** Keller *Deformed Calabi–Yau completions*, [arXiv:0908.3499v5](https://arxiv.org/pdf/0908.3499) の**Proposition 4.2（印字p.17）**を本文・PDF画像で確認：Morita functorから$\Pi_n$のMorita functorが自然に得られ、基礎dg圏の包含・射影と可換する。一方**Theorem 4.6（印字p.18）は局所化との整合定理**で、Morita不変性の主引用には不要。Cの`prop:qa-q12-dg-ideal-presentation-strict-naturality`では二mass有限道の関係ideal$I$が$I^2=0$、$d:\mathscr F^{-1}\cong I$、$\mathscr F\cong F\oplus I[1]$を直接示す。全finite presentation Isomのstrict持上げとmass/shearが有限商に誘導する恒等から、Keller Proposition4.2を使ってfinite foundationのMorita像でcoherentな単位作用を得る。これは**本研究の有限表示上の具体的自然性**であって、Keller Proposition6.8の特定の局所$\Gamma_3$比較が全raw QP right-equivalenceに2自然であることまで原典が保証したとは主張しない。全関連する初等線形恒等式の有限再現は[コード](../computations/verify_q12_presentation_dg.py)。

**dg代数kernelの多項式nullhomotopy（標準的ホモトピー形式の具体適用）。** 本研究の二項模型$\mathscr F=F\oplus I[1]$は$I^2=0$ゆえdg ideal $J=I\oplus I[1]$がsquare-zero。商$F/I$上恒等な$(F,I)$の自己同型について$\delta=\varphi^\sharp-id$と$h(f)=\delta(f)[1]$（$h|_{I[1]}=0$）が$dh+hd=\delta$を満たす。標数零の$\Omega^\bullet_{R[z]/R}=R[z,dz]$を用いる$\mathrm{id}+z\delta+dz\,h$は端点で恒等と$\varphi^\sharp$になるdg代数準同型。これはsquare-zero idealとde Rham path objectからの標準的な形式的帰結であり、一般原理の新規性を主張しない。新規性未確認の本研究の具体的寄与は、QPの二mass/非被約壁の全kernelで同一公式を使えること、非平坦基底変更とfinite quotientのcoherent降下に整合させた点。[原稿](../papers/quiver-avatar/cubic_qp_foundation_groupoid.tex) `prop:qa-q12-mass-dg-polynomial-nullhomotopy`。Keller Proposition 6.8から得るGinzburg局所Morita同値のraw right-equivalenceに対する2自然性は、これだけでは確定しない。

**raw右同値のA1経路障害と有限dgホモトピーの区別（2026-11-23、内部の直接証明）。** 非可換道代数の頂点固定右同値は一矢の一次係数を$R[z]^\times$に送る。$P(z)\in R[z]^\times$で$P(0)=1$なら$P(1)-1$は冪零（全素イデアルへの剰余で定数単元のみ）。従って二massゲージの$\mathrm{id}$へのraw A1経路は$\lambda t,\mu s$が共に冪零の場合に限り、逆向きは$g_{zt,zs}$で構成する。これはfaithfully flat被覆でも改善しない。一般の多項式単元の事実と標準的経路構成は既知初等手法であり、一般原理の新規性は主張しない。本研究固有の点は、二mass非最小QPのmass核についてnecessary/sufficientを固定し、有限dg idealの全mass nullhomotopyとの**構造的な差**を厳密に認識したこと。[原稿](../papers/quiver-avatar/cubic_qp_foundation_groupoid.tex) `prop:qa-q12-raw-mass-a1-path-obstruction`。Keller Proposition 6.8の局所Ginzburg Moritaの2自然性は依然未検証で、この障害を隠す経路議論を用いない。

**非正dg複体の普遍Tor完全列（既知手法）。** 任意の非正複体$C$のtruncation三角は$\operatorname{Tor}_2(H^0C,R')\to H^{-1}C\otimes_RR'\to H^{-1}(C\otimes_R^{\mathbf L}R')\to\operatorname{Tor}_1(H^0C,R')\to0$を与える。これは標準的な導来tensorの形式的帰結であり、新規性を主張しない。$H_2$上のSerre dgでは全次数消滅の方が強く、このTor列を独立の未解決目標としない。

Artin–Zhang, *Noncommutative projective schemes*, Adv. Math.109(1994),228–287, [DOI](https://doi.org/10.1006/aima.1994.1087) の刊行書誌とabstractを確認した。Theorem4.5(1)の一般End環への適用仮定は、Okawa–Abdelgadir–Chan–Ueda, *Degenerations of orbifold curves as noncommutative varieties*, Nagoya Math.J.261(2026),e4, [刊行本文](https://www.cambridge.org/core/journals/nagoya-mathematical-journal/article/degenerations-of-orbifold-curves-as-noncommutative-varieties/F7FD772141C9BE8DE3D3DC5B830E48DA)、[DOI](https://doi.org/10.1017/nmj.2025.10067) のDefinition7.1とTheorem7.3（Artin–Zhangの再掲）、式(7.1)–(7.5)で2026-11-23に独立再照合した。**必要条件**は、(i) 構造対象TがNoetherian、(ii) A0=End(T)が右Noetherianかつ全coherent Kに対するHom(T,K)が有限右A0加群、(iii) (T,t)がAZ1/AZ2を満たすこと。Cの相対AZ2では、Tの**どの位置の直和因子にも**構造対象Oを置けるよう命題の仮定自体を修正した。$0\to L\to P\to K$と$0\to L'\to P'\to L$の二段presentation、平坦compact始域に限るExt$^{>2}$消滅、有限Noetherian基底上の有限R加群End(T)から右Noetherianを証明する新補題で全仮定を確定した（[相対AZ証明](../papers/quiver-avatar/relative_square_tails_recognition.tex)）。その結果、一重rank3で反対normal零頂点がH2 pointingでない場合も、反対squareのdual heart内の別の（第二）頂点Q0を基準に左Noether性を証明できる。**既知の再構成定理と本稿の相対Ext/AZ適用・rank3障害の修復を区別**する。AZ1994の原著Theorem4.5本文は現在取得できず、原著を直接読了したとは主張しない。引用キー `AZ1994`, `OACU2026`。

Keller, *Deformed Calabi–Yau completions*, Theorem 6.10 の[著者による2011年の訂正](https://webusers.imj-prg.fr/~bernhard.keller/publ/KellerCorrCYCompletion.pdf)を一次PDFの画像と本文で再確認した。relation QPの比較には、指定したrelationsがarrow-adic完備化でなく**ordinaryな関係ideal**を生成する条件が必要である。本研究のsquare有限代数は最長道長二で、今回の二mass normal finite foundationは最長道長三。後者は二つの短関係と二本の残余長関係が、三段道のrank六kernelを生成し、短関係の全合成を含んだordinary idealを生成することを直接証明した（[短い相対対角解消とJacobian/Serre比較](../papers/quiver-avatar/cubic_qp_foundation_groupoid.tex)）。したがって非最小関係・nilpotent massでもordinary ideal生成の点は確認できる。ただしKeller Theorem 6.10の元来の定式化は**minimal relations**を使い、mass可逆な非最小十二矢表示へそのまま適用できるとは主張しない。今回のJacobian=H⁰Π₃の同型は、そのため**相対短対角解消の直接双対化とcyclic derivativeの計算**を用いる。massを除去したminimal開では訂正済み定理と一致する。さらに[2018年のerratum](https://webusers.imj-prg.fr/~bernhard.keller/publ/KellerErratumCYCompletions.pdf)の冒頭とTheorem 1.1を一次PDF画像で確認した。非零deformation parameterからのCY性にはnegative cyclic classの入力が必要だが、今回の結果は**undeformed** 3-preprojective tensor completionとH0のordinary Jacobian表示であり、この追加CY性の無条件輸入を行わない。二つの訂正の内容・依存は区別する。相対完全性はKellerの一般論だけから推論せず、通常関係idealと非可換普遍導分のconormal列・Euler等式$(68-52+8=24)$を用い，任意の非被約基底上で分裂完全となることを直接証明した（CのEuler--conormal補題）。2026-11-23に2011年著者訂正PDFのordinary ideal条件を本文・ページ画像で再確認した。双対dg複体の$P_2^\vee,P_1^\vee,P_0^\vee$のcohomological次数とcyclic derivativeをC原稿に明示して$H^0$としてのJacobian比較を直接示した。関係liftのcoherent降下・AZ/Noetherの包括的独立監査は別に残る。包括的新規性と全証明の独立監査は未完了。

## 相対heart判定に用いるdg Morita

**C4で必要な二種類の基底変更の区別（2026-11-23、原稿内で直接証明）。** Keller 1994 §8.2 のdg Morita定理はcompact生成から非有界導来同値を与えるが、それだけで標準heartに$t$-exactだとは言わない。Cの`cor:qa-all-square-isom-pointed-heart-descent`では反SerreAZ生成族の両向き保存から$t$-exact性を証明し、さらに`lem:qa-h2-heart-underived-base-change`では非平坦基底変更の通常module-object引戻しを$H^0\mathbf Lb^*$と同一視して2自然性を確認した。$k[\varepsilon]/(\varepsilon^2)\to k$の周期Torは導来引戻し自体の$t$-exact性を否定する標準的反例。別に`lem:qa-q12-hzero-nonflat-base-change`では非正・基底K-flatなSerre tensor dg模型の零次と任意基底変更をtruncation三角で直接交換する。Kellerのordinary ideal訂正は引き続き別条件であり、これらの引戻し補題をKellerやAZ原典の新しい結論として帰属させない。**基底$K$-flat性の外部入力**はStacks Project [Tag 064K, Lemma 15.60.7](https://stacks.math.columbia.edu/tag/064K)の「上に有界な平坦加群複体は$K$-flat」という原文・証明を確認した。$H^0$の任意基底変更公式とTor反例は本稿でtruncation三角・周期自由解消を直接示し、Stacksの新規性は主張しない。原論文AZ1994 Theorem4.5の本文未取得という制約は保持する。


Keller, *Deriving DG categories*, Ann. sci. École Norm. Sup. (4)27(1994),63–102、[著者本文](https://webusers.imj-prg.fr/~bernhard.keller/publ/ddc.pdf) の §4.3 と §8.2 を一次再確認した。Compact生成圏のdg加群表示と、small generatorsに対応する双加群tensorによる非有界導来同値が既知入力である。Cはenhanced Moritaのcolimit保存と相対H2のAZ生成を使い、両構造対象が相手heartに実際に入る条件からt-exactnessを直接証明する。このheart判定を既知Morita定理そのものの結論とはしない。非被約底の全fiber同値だけでt-exactnessを推論しない。一般補題の包括的新規性は未調査。既存キー `Keller1994` を使用。

## 相対乗法束・Fitting閉部分の一次資料

Stacks Project [Tag 0B91](https://stacks.math.columbia.edu/tag/0B91), Lemma36.30.4 はproper finite presentationな射とflat性の下でperfect複体の直像のperfect性と任意底変更を与える。[Tag 07Z6](https://stacks.math.columbia.edu/tag/07Z6), Lemma15.8.4(3)–(4) はFitting理想の任意底変更と有限生成性。[Tag 0E6B](https://stacks.math.columbia.edu/tag/0E6B), Lemma75.26.7 はproper flat fp・全fiberのH0(O)=kの下で構造層直像とunitのétale局所分裂を与える。2026-11-23に一次本文を確認した。これらの一般定理は既知入力であり、二行列式開・普遍壁のscheme構造・rank16からrank24への実際の相対mutationとH2認識が本稿で証明する適用部分である。包括的新規性は未確定。

## 点加群・fat pointと生成障害の先行研究

Smith–Van den Bergh, *Noncommutative quadric surfaces*, J. Noncommut. Geom.7 (2013),817–856, [DOI](https://doi.org/10.4171/JNCG/136) の刊行本文§10.5と、Rogalski–Sierra–Stafford, *Some noncommutative minimal surfaces*, Adv. Math.369 (2020),107151, [DOI](https://doi.org/10.1016/j.aim.2020.107151)、[著者版](https://www.pure.ed.ac.uk/ws/portalfiles/portal/141851809/1807.09889.pdf) のLemma6.6とProposition6.10の証明（印字pp.22,24–25）を2026-11-23に一次確認した。後者は無限位数translationのSklyanin quadricで余剰単純対象のmultiplicityを決定し、MCM line idealの非generator性をtrace quotientの点加群で検出する。通常のpoint moduleとmultiplicity>1のfat pointを区別する必要がある。

楕円base locus外に点加群があることや、trace商で生成性を調べる一般手法を新結果とはしない。Cは中央二重平方表示の全point schemeと交換shift、全標準頂点の反Serre豊富性・H2所属を直接証明する。今回照合した無限位数Sklyanin pencilの結果は、曲線上shiftが恒等となるこの二平方表示をそのまま含む定理ではない。表示が同値な有限中心・Clifford系文献との網羅的照合は未完了で、新規性は未確定である。引用キー `SVdB2013`, `RogalskiSierraStafford2020`。

## Artin targetへの良モジュライ射と構造頂点の障害

Alper, *Good moduli spaces for Artin stacks*, Ann. Inst. Fourier 63(6) (2013), 2349–2402, [doi:10.5802/aif.2833](https://doi.org/10.5802/aif.2833) の [刊行本文](https://www.numdam.org/article/AIF_2013__63_6_2349_0.pdf) を2026-11-23に一次確認した。Remark4.4はArtin targetについてのgood moduli space morphism、Proposition3.10(v)はcohomological affinenessのfaithfully-flat降下、Proposition4.7はbasechange/descent、Example12.9はlinearly reductive affine quotientを扱う。引用キー `AlperGoodModuli2013` を刊行版用に追加し、旧arXiv v3の `Alper2009` の定理番号を変更していない。

Cの具体的な追加は、Frickeの自然な順序付き延長をこの意味の平坦な良モジュライ射と同定し、sourceのDM開へ制限すると直像完全性を失うことを明示する点である。非順序射はgeneric O直像のrankが2なので同じ結論にならない。商・不変式一般論の新規主張とはしない。

Noncubic spinor pointingの排除は、二周期point moduleとh局所化の直接証明を用いる。反Serre生成の必要性は既存の次数1生成・Veronese・AZ再構成を入力とする。今回の具体的な貢献はsquare/rotated/最小AS10の全四位相の判定であり、全分類AS型の標準頂点には、別の頂点ideal判定とcubic逆構成を用いて拡張した。任意の非標準exceptional対象の標識分類へは拡大しない。この排除と既存のpoint-module分類との包括的新規性比較は未完了。

## 境界graph・自由符号商・構造層の入力

2026-11-23に一次本文を確認。Stacks [Section 31.33, Tag 01OF](https://stacks.math.columbia.edu/tag/01OF) のLemmas 31.33.2–31.33.3はRees chartと平坦基底変更、Lemma 31.33.5はblowupの普遍性を与える。任意の非平坦基底変更はこの引用から主張しない。引用キー `StacksBlowups`。

[同Lemma 66.14.2, Tag 07S7](https://stacks.math.columbia.edu/tag/07S7) は射影的scheme上の有限局所自由群の自由作用についてscheme商とtorsorを与える。本稿では群C2がétaleなので被覆もétale。引用キー `StacksFreeQuotients`。[Theorem 30.20.5, Tag 02OC](https://stacks.math.columbia.edu/tag/02OC) はNoetherian基底・proper射・coherent層に対する形式関数定理であり、A1解消の無限小近傍の $\OO_{\PP^1}(2j)$ のcohomology消滅から $Rf_*\OO=\OO$ を導く。引用キー `StacksFormalFunctions`。

古典的なblowup・有理二重点・楕円曲線の加法公式を新結果とはしない。Cの具体的な結論は二traitの指定同型のgraph、二組の交互収縮、自然Fricke像のbalanced TF延長と被約線束境界、一致型の模型同型と四捩れtranslation・conic順序交換の組合せである。証明は [境界模型](../papers/quiver-avatar/spectral_boundary_models.tex)。全G同変な自然Fricke射のbalanced標的への境界降下と全fiberは [大域降下](../papers/quiver-avatar/fricke_boundary_descent.tex) に直接証明した。任意非平坦底でのgraph形成、H2 heartの延長、包括的新規性確認は主張しない。

[Stacks Lemma 55.10.1, Tag 0C6B](https://stacks.math.columbia.edu/tag/0C6B) の正の種数の滑らかな射影曲線の最小正則模型の一意性を2026-11-23に一次確認した。指定generic同型で標識を変えることで全halving補正を最小正則模型へ延長する。原模型の同型やpencilの平方根延長はこの一般定理から従わない。引用キー `StacksMinimalModels`。同日のSilverman第2版III Theorem 10.1（printed p.103）の一次確認により、$j\ne0,1728$ の原点固定自己同型は $\{\pm1\}$ とした。halving四点の具体式・最小分岐・Kummer class・成分回転は原稿の直接計算である。

全Fricke降下は、既知の二同種・二次線束と有限étale被覆の対応に対する具体的な全群作用の計算である。新しい主張の範囲は、二重根を許すbalanced標的への任意基底変更と両立する自然な射、および境界の $[\operatorname{Spec}k[a,b]/(ab)/\mathbb G_m]$ fiberと慣性である。古典的な楕円曲線の加法公式・コンパクト化一般論を新発見とはしない。admissible cover・Prym・spin compactificationとの包括的な文献比較は未完了である。

## Spectral-pointed対応と二同種の一次資料

Silverman, *The Arithmetic of Elliptic Curves*, 2nd ed., GTM 106, Springer, 2009, DOI [10.1007/978-0-387-09494-6](https://doi.org/10.1007/978-0-387-09494-6), Chapter III, Example 4.5, printed p.70 を[第2版の一次本文](https://www.math.ens.psl.eu/~obenoist/refs/Silverman.pdf)（PDF 88頁目）で照合した。$y^2=x(x^2+ax+b)$ と $Y^2=X(X^2-2aX+a^2-4b)$ の双対二同種が明示される。Cで採用したYの符号は同書と逆だが、核と標識付き商は同じである。今回の引用キーは `SilvermanAEC2009`。別版の `SilvermanAEC1986` の当該箇所を再確認したと読み替えない。

二同種の双対化・Atkin–Lehner対合・商の公式は既知結果である。本稿の具体的な追加は、逆pencil構成とAS10の指定一番頂点を介してspectral avatarのpointed H2像を同定し、noncubic不変量で $\chi\mapsto\chi/(\chi-1)$ と書くこと、自己双対二点と二捩れ標識を失う等j反例を示すこと、およびBの閉境界を入力に二退化型でH2族への延長を排除することである。証明正本は [spectral対合と境界](../papers/quiver-avatar/spectral_atkin_lehner.tex)。このpointed適用・延長不能の新規性を網羅的に確定したとは主張しない。

## 節点二次自己双対TF標的の代数性

2026-11-22にStacks Projectの一次本文を確認した。Coh stackのArtin性は [Theorem 99.6.1, 09DS](https://stacks.math.columbia.edu/tag/09DS)、affine有限表示対角と局所有限表示は [Lemmas 108.4.1–108.4.2, 0DLX](https://stacks.math.columbia.edu/tag/0DLX)。Homのaffine有限表示は [Proposition 99.3.10, 08K6](https://stacks.math.columbia.edu/tag/08K6) で、標的層のfinite presentation・基底flat・proper supportを確認する。直像ベクトル束へのfiberwise flatnessは [Theorem 76.23.3, 05X0](https://stacks.math.columbia.edu/tag/05X0)、固定多項式Quotの有限型性は [Lemma 108.6.1, 0DP9](https://stacks.math.columbia.edu/tag/0DP9)。引用キーは `StacksCoherentSheaves`。

Cの具体的な追加は、二重代数のFrobenius双対による自己双対性の有限行列表示、非被約底でのtrace零、被約連結rank-one自己双対層の $h^0\le1$ と二分解型による一様有界性、等方線からの全二形式・同型層の回収である。[証明](../papers/quiver-avatar/torsion_free_spectral_recognition.tex) は全節点標的の有限型Artin性と、balanced開 $[\overline P_{\rm nod}/G]$、元のnoncubicのsquarefree開を与える。既知のCoh/Quot代数性を新成果とはしない。固定被覆のfiberは二次因子分解schemeと交換作用で計算し、境界の非被約構造まで保持する。これは二捩れ・四分岐点の二対分割の古典的関係を具体的なTF標的へ適用するもので、包括的新規性は未確定。非被約spectral曲線全体の有限型性、任意AS heartとの比較、包括的な新規性の確定は未実施。

## 相対spectral gerbe・慣性・特異境界の入力

Stacks Projectの [Lemma 108.9.1, Tag 0DME](https://stacks.math.columbia.edu/tag/0DME) は、相対Picard stackからPicard functorへの射がgerbeとなることを与える。[Section 59.28, Tag 03PK](https://stacks.math.columbia.edu/tag/03PK) のKummer列と [Lemma 59.28.5, Tag 040Q](https://stacks.math.columbia.edu/tag/040Q) は、線束と二乗自明化の組と $\mu_2$-torsorとの対応を与える。これらを2026-11-22に一次本文で確認した。一般基底で $\operatorname{Pic}(S)/2$ を捨てて $H^2(S,\mu_2)$ をBrauer 2-torsionと同一視してはならない。引用キーは `StacksRelativePicard`、`StacksKummer`。

[原稿Cの相対対応](../papers/quiver-avatar/spectral_relative_correspondence.tex) は、この既知一般論を使って順序付き二conic標的上の二次線束gerbeを記述し、入力二被覆との局所逆・射・降下を直接証明する。任意基底変更と両立する射、その $\mu_2$ 核、幾何fiber $2B\mu_2$、一般逆gerbeのindex 4が具体的な結論である。古典的二同種の新発見としない。

[Stacks Lemma 101.6.2, Tag 04YY](https://stacks.math.columbia.edu/tag/04YY) は相対慣性核の自明性によるrepresentability判定を与え、同日に本文を照合した。Cでは一般慣性の中心を具体的に計算し、双対化前後の非同型な二次分裂体がinner formでも残ることから、粗対合を覆う自己同値と一般representable liftを排除する。幾何点の抽象群の同型だけを比較した結果ではない。

境界の無限Extは、Bの任意二形式に対するClifford標準形とweighted projective stackへのsheafificationを入力に、Cで周期解消から証明する。通常のmatrix factorization・dimension shifting・Serre双対性の一般手法と、具体的な退化代数における $\operatorname{Ext}^n=k$ およびH2判別式条件を区別する。公表前にはdouble-cover moduli、marked 2-isogeny、Clifford orderの特異性に関する追加文献比較が必要であり、包括的新規性は未確定。

## 対称Morita降下と相対Serre完成

Keller, *Deformed Calabi–Yau completions*, arXiv:0908.3499v5 の §2.3、Proposition 3.10(e)、§4.1、Proposition 4.2 の一次本文を今回照合した。基礎環は一般可換環で、inverse dualizing complexと直和tensor completionのMorita共変性を入力とする。無限積完備化の非平坦基底変更はこの引用から主張しない。2018年erratum（arXiv:1809.01126）は非零変形パラメータの追加条件に加え、Thm 6.1のrelationsが通常idealを生成する条件も扱う。今回のundeformed Morita共変性のProp 3.10(e)・4.2と混同せず、既存QP/GinzburgのThm 6.10適用は別途監査する。

一般gerbe重み零降下・twisted MoritaはBergh–Schnürer 2021、derived MoritaはKeller 1994の既知入力。Cの新しい具体化は対称spinor四項・全表示群へのrank45降下・指定零頂点と相対Serre角の比較、および二形式交換の符号εの計算である。全次数の次数零集中には既存体上helixのforward Ext消滅を用い、有限数値検算を代用しない。これらの新規性の包括的な調査は未完了。

## OU/noncubicの共通spectral incidenceとKummer類の不一致

一次資料としてOkawa--Ueda (2014, arXiv:1403.0713)の
Theorem 1.1(4)にあるpotential→quintuple有限次数4射、
および論文Cで同文献の§5から再構成した対角固有値表示を使う。
OUのspectral Kummer同型自体はC
thm:qa-ou-spectral-kummerの証明による。既知のOU一般次数4
射の新発見とは主張しない。

四固有値$x_i$の二乗$r_i=x_i^2$を二対分割し、
二対分割の安定化群で割ったincidence基底
$I_{\mathfrak p}=X^\circ/(V\rtimes H_{\mathfrak p})$を構成した。
そこではOU spectral曲線
$E_{\rm sp}:y^2=\prod_i(t-r_i)$とnoncubicの
$C_q:y^2=f_1f_2$は同一の相対四次被覆である。
noncubic点曲線$E_f\to C_q$は非分岐次数2の被覆。
両四重torsorは同じ一般$D_4$-monodromyを持つが、
全固有値を指定した関数体$F=k(z_1,z_2,z_3)$上では
OU側は4つの自明sheet、noncubic側は
$F(\sqrt A)\times F(\sqrt B)$となり非同型。
$A=(1-z_1^2)(z_3^2-z_2^2)$、
$B=(z_3^2-z_1^2)(1-z_2^2)$の独立非平方性は
一次素因子の奇付値から証明した
（C thm:qa-ou-half-period-common-incidence-not-isomorphic）。
同じ$F$上で$J(C_q)[2]$は4点全て有理的だが、
$J(E_f)[2]$は2点しか有理的でない
（他二点は$\sqrt{AB}$を要する、
C prop:qa-ou-half-common-incidence-groups-distinct）。
ゆえに比較する有限\'etale群スキーム自体が異なる。
さらに自然な二同種$\phi=r^*:J(C_q)\to J(E_f)$から
誘導される$\phi[2]$によってOU Kummer類を押し出しても
$\phi[2]_*[Y_{\mathfrak p}]\ne[T_{\mathfrak p}]$
である（C cor:qa-ou-half-isogeny-kummer-classes-distinct）。
証明は全固有値体$F$上で
$[Y]|_F=0$、$[T]|_F\ne0$という
Kummer境界の自然性に基づく。
したがって比較の自然な射まで含めて
Kummer類の不一致を証明した。

これは本研究で証明した比較結果で、先行文献の
Kummer exact sequenceや二同種の一般事実とは区別する。
ただし相対mutation、pointed qgr、別の任意基底変更後での
同値の有無、外部文献全体に対する新規性は未解決。
計算の範囲は
computations/verify_ou_half_common_incidence.py
の四次式恒等式、平方類奇付値、OU halfpointの有理性、
isogenous Jacobianの非分裂2torsion判別式。
原稿に証明があることと独立の数学的全面監査は区別する。

## 二つの有限四重射のmonodromy：D4とS4の射程

Okawa--Ueda, *Noncommutative quadric surfaces and noncommutative conifolds*
(arXiv:1403.0713, 2014)、Theorem 1.1(4)のpotential GIT
からquintuple GITへの次数4有限射を入力とする。
OU §5の四固有値置換をS4と解釈した原稿Cの
prop:qa-ou-fourfold-s4-monodromyは、
有効符号群V=F2²と線型群GL2(F2)からなる
AGL2(F2)≃S4を一般Galois閉包群として計算済み。
OU (5.3) のS4と (5.8) のS3との印刷上の不整合は
C rem:qa-ou-source-s3-s4-discrepancyに明示し、
原論文の印刷式をそのまま引用した主張とは区別する。

本研究のnoncubic側では
$P\in J(E_f)[2]\setminus0$の半周期torsor
$T_P=[2]^{-1}(P)$のmonodromyが
$F_2^2\rtimes GL_2(F_2)_P≃D_4$に含まれる。
三変数部分族$f_1=x(x-a),\,f_2=(x-b)(x-c)$で
$A=c(b-a),B=b(c-a)$と置き、
$b,c$を交換できる基底$K_1=k(a,b+c,bc)$へ戻すと、
分解体$k(a,b,c)(\sqrt A,\sqrt B)$の群が
$(C_2)^2\rtimes C_2=D_4$となり上界達成。
一方root-choice四重射の一般群は$C_2^2$。
原稿C thm:qa-half-period-dihedral-monodromyの証明正本と
computations/verify_half_period_monodromy.pyの有限置換群検算を参照。

OU側でも非零2捩れ≃四分岐点の二対分割を一つ選ぶ
次数3有限étale標識被覆へ引き戻すと、
S4の線型商S3の安定化群がC2に縮み、
一般四重射のmonodromyは$F_2^2\rtimes C_2=D_4$となる
（C prop:qa-ou-fourfold-dihedral-restriction）。
この群の一致は**OUのtorsorとnoncubic $T_P$の同型を意味しない**。
OU側はpotential/quintuple表示の別基底とそのspectral curveの
Kummer section、noncubic側は$C_q$と一般に非同型な
二同種曲線$J(E_f)$の非零2捩れ$P_E$を二等分する。
共通spectral incidenceはC v4.5で構成したが、OU四重torsorとnoncubic半周期torsorはその上で非同型であり、自然な二同種のKummer押出しでも類は一致しない。残るのは相対mutation・pointingとMoritaの降下である。

## 一般biquaternionのindexと楕円曲線の四重被覆

Lam--Leep--Tignol, *Biquaternion algebras and quartic extensions*,
**Publ. Math. IHÉS 77 (1993), 63--102**,
[doi:10.1007/BF02699188](https://doi.org/10.1007/BF02699188),
**Theorem 2.3（論文内p.66）**を一次PDFの該当頁まで確認。
二四元数代数に対応する6次元Albert形式がanisotropicであることと、
当該次数4代数がdivisionであることの同値を使用する。
Lam, *Introduction to Quadratic Forms over Fields*,
AMS Graduate Studies in Mathematics 67 (2005),
[doi:10.1090/gsm/067](https://doi.org/10.1090/gsm/067),
Chapter VI, Proposition 1.9の離散付値の二剰余形式判定を使用する。
書誌情報は出版社で確認。Lamの本の本文全体の独立検証は未実施。

C v4.2は独立一般二次形式のBrauer類
$\\beta=(a_c,\\Delta_c)+(a_d,\\Delta_d)$に対する
6次元Albert形式の二重Laurent付値検査から
$\\operatorname{ind}(\\beta)=4$を導き、
一般noncubic点曲線$E_f$のperiod 2・index 4、
半周期torsor$T_P$の最小次数4でのBrauer差分裂を証明する。
通常の二同種写像公式はWeierstrass変数の直接代入で検証し、
monic split-root族で$T_P$が二つの非自明な二次体に分かれることから
分岐根選択の別の四重被覆と非同型であると証明する。
一般Albert判定と2-isogeny公式そのものは本研究の新発見としない。
この特殊なBrauer差・period-index計算および二被覆比較の
包括的先行研究上の新規性は未確認。
証明正本はCの
thm:qa-generic-point-period-two-index-four、
prop:qa-half-period-conic-isomorphism、
thm:qa-half-period-not-root-choice。
計算再現はcomputations/verify_half_period_fourfold.py
（多項式恒等式のみ、anisotropyやGalois非平方性の形式証明ではない）。

## 相対gerbeとAzumaya-Moritaの一次入力

Daniel Bergh--Olaf M. Schnürer,
*Decompositions of derived categories of gerbes and of families of Brauer--Severi varieties*,
**Documenta Mathematica 26** (2021), 1465--1500,
[doi:10.4171/DM/846](https://doi.org/10.4171/DM/846)
（原稿Cの引用キー BerghSchnurer2021）。
出版社の書誌・概要を確認。Theorem 4.7の対角化可能群gerbeの
QCoh重み分解と重み零の基底降下、Theorem 5.4の導来重み分解、
Theorem 6.2/Remark 6.3のBrauer--Severiに対するtwisted成分の
一般理論を入力とする。本文全証明の独立監査を行ったとは報告しない。

この一般論はCの新規結果ではない。本研究の追加内容は、
noncubic二conicのgerbe上のdeterminant補正
$N_i^2\simeq\mathcal O_{Q_i}(1)\otimes\det(q_{i*}N_i)$、
四線束$(\mathcal O_E,F,H,HG)$の明示重み
$0,(1,0),0,(0,1)$、Brauer類$(0,\alpha_c,0,\alpha_d)$、
各HomをAzumaya双加群へ降下させた合成公式と、
generic ruling交換に頂点固定Morita同値が存在しないという
$\alpha_c\ne\alpha_d$に基づく障害
（C lem:qa-morita-determinant-normalization、
thm:qa-twisted-four-vertex-morita、
cor:qa-morita-ruling-exchange-phase）。
これは有限Endの記述であり、gerbe上の相対AS完成・
相対qgr同値や、ruling交換をmutationしたpointed射の実現は未確認。

## 原稿C v3.4：avatar–AS分類の出典と外部入力

**研究の直接の入力：** 大川新之介・植田一石、
未公刊日本語草稿『非可換二次曲面の二つの反標準avatar』
(`quadric_avatar_classification_parts_I_II_ja_20260916_v7.pdf`)。
定義1.1–1.2、定理1.3、定義2.1、命題2.4、
§§3–8、11–12の体上のsq/rsq分類を
[CのAS-helix節](../papers/quiver-avatar/as_helix_classification.tex)に統合。
定義48.1、補題49.1/命題49.2、定理50.1、51.2、51.4と系51.5、
命題52.2、定理53.2の独立AS10・逆mutation・群oidと相対perfect条件は
[Cのmutation節](../papers/quiver-avatar/as10_mutation_classification.tex)に統合。
元PDFの証明を展開・編集したもので、過去の著者による既存草稿に対する
新規な発見としての優先権を主張しない。

**使用する外部一般定理と適用範囲：**
- Okawa–Ueda, *AS-regular algebras from acyclic spherical helices*
  (arXiv:2007.07620, 2020), **Theorem 5**：
  acyclic spherical helixからexceptional helixへの実現。
  Cでは曲線上のforward Ext消滅・canonical truncationを証明して適用する。
- Bernhard Keller, *Deformed Calabi–Yau completions*,
  J. reine angew. Math. **654** (2011), 125–180,
  [DOI:10.1515/crelle.2011.031](https://doi.org/10.1515/crelle.2011.031)、
  **Theorem 6.10のundeformed case**を有限大域次元2の
  relation Ginzburgと3-CY completionの比較に用いる。
  仮定は有限quiverと矢idealの二乗に入るminimal関係、
  finite-dimensional algebraのglobal dimension$\le2$。
  $W=\sum_r r\rho_r$とし、変形パラメータ$c=0$とする。
  Cでは$\Theta=\RHom_{B^e}(B,B^e)[2]$の
  各tensor冪と全整数helix forward RHomの一致を
  四頂点成分ごとに確認し、$m\ge1$で
  $j+4m>i$を使う。内部正次数の完備化も別に扱う。
  一般のdeformed completionについて訂正文があるため、
  Cの適用をundeformedに限定する。
- Bernhard Keller–Dong Yang, *Derived equivalences from mutations of
  quivers with potential*, Adv. Math. **226** (2011), 2118–2168,
  [DOI:10.1016/j.aim.2010.09.019](https://doi.org/10.1016/j.aim.2010.09.019)、
  **Theorem 6.2**をloop/2-cycleを通らない指定頂点のmutationに適用。
  同論文§6.1は**reduced potential**と完備Ginzburgの
  $H^{\ne0}=0$を先に要求する。
  relation potentialはminimal関係length$\ge2$と
  dual矢を掛けたlength$\ge3$なのでreduced。
  (c1)--(c3)は同論文§2.4の正確な条件であり、
  いずれもCで明記した。dg由来同値だけから
  AS正則性を言わず、Ginzburgの次数零集中と
  通常の単純最小分解への降下を別々に論じる。
- Twisted homogeneous coordinate ringの標準Noether定理を
  ASから得る四次正規正則familyの商に用いる。

**今回確認した原資料箇所と未完の監査。**
元草稿§8の命題8.1は左右Noether性・coherent導来Morita同値・
Serre$\nu[2]$を正規四次familyから導く。
§52の命題52.1は固定mutationの両側Noether性・
$\Qgr A'\simeq\Qgr A$, $\qgr A'\simeq\qgr A$を
共通ample corner・Artin--Zhangに帰着する。
これらをCのprop:qa-as-avatar-coherent-moritaおよび
prop:qa-as10-noetherian-qgrに証明付きで統合した。
Keller--Yang Theorem 6.2の(c1)全quiverのloop禁止、
(c2)mutation頂点を通るoriented 2-cycleの禁止、
(c3)potentialの巡回同値代表の局所条件を
一次資料に照合し、Cで各条件とGinzburg次数零集中を
別々の入力とした。
元資料§15.4の二乗法の階数壁(15.6)を
pencilの評価列と$H^*(GF^{-1}P^{-1})$の消滅から
非被約Dを含めて直接再証明した。
四周期Hilbertの全次数等式もEuler有理級数で独立再計算した。
他方、Artin--Zhangの再構成仮定すべての独立な確認、
AS-Gorenstein性を与えるdg実現の全論理、
Keller--Yangのproof全文と網羅的新規性は未監査。
上記結果の出典は新しい独立発見ではなく原草稿である。

**原PDF §§19–21・42のcubic型到達判定の移管。**
定理21.1は、square型の$Qgr$/導来圏が
いずれかのcubic型のそれと同値であるための
必要十分条件が非零二捩れ二重壁$Z$の外側であるとする。
肯定方向は§18の二mutation chartとample corner、
否定方向は§19のsmooth楕円上での
任意strong exceptional cubic候補の数値rank強制、
realization三角形とdeterminant、
連続二pencilが一致するときの乗法kernelで示す。
§20では$\mu_2$-torsorを保つ形式的平滑化、
有限自由End代数上の$\Ext^2=0$を用いた
perfect複体の持上げによりnodal/I2へ拡張する。
これをC
\`papers/quiver-avatar/cubic_obstruction_all_loci.tex\`に
定義・補題・証明付きで組み込んだ。
さらにCの\`as10_mutation_classification.tex\`では、
二重壁の曲線がsmooth/nodal/I2だけになることを
多重次数とPic^0のconnected groupから直接証明。
一般の非被約$(2,2)$因子、cuspidal曲線、
接する$(1,1)$二成分では非零2torsionが存在しない。
数値Serre行列・2torsion隣接商のparityは
\`computations/verify_avatar_cubic_obstruction.py\`の
独立有限整数計算でPASS。
これらは原PDFの既存結果の移管・検算であり、
新規性や形式的な導来圏の証明器による検証ではない。
完全なカテゴリカル／stack相対化と
内在的O-marked H2へのpointed同値は別の研究課題。

**二重壁の局所scheme構造（C v3.3、独自の局所計算）。**
元PDF§15.4・§42は二乗法の階数壁および
二重壁のsmooth/nodal/I2分類を与える。
Cではさらに、固定した滑らかな楕円曲線と
次数二pencil$F$のパラメータ$\eta=GF^{-1},P$に対し
二壁を$\eta=P,\eta=P^{-1}$という
\emph{scheme-theoretic Fitting条件}として書いた。
自明線束の一次変形の接続写像
$H^0(\OO_D)\to H^1(\OO_D)$が変形類とのcup積であるため
壁は被約Cartier、非零二捩れ点で微分行列式$-2$。
交点のscheme長はsmooth/nodal/I2で$3/1/1$、
smooth楕円曲線族では非零E[2]が有限étale三次となる。
これは固定曲線／標識付きavatar側の結果であって、
論文Bの内在的Artin境界とのstack同型ではない。
本計算の先行研究に対する包括的新規性は未確認。

**noncubic点曲線・spectral曲線の双対2-isogeny（C v3.4）。**
中央二重平方環$B_f$の可換点曲線$E_f$と
quartic-resolvent曲線$C_q$について、
非交差二根対なら自由な同時符号の商$E_f\to C_q$は
有限étale次数2のisogenyである。
二つの個別符号商$E_f\to Q_c,Q_d$はconic上の
次数一線束から二つの次数二pencil$F_c,F_d$を与え、
$P_E=F_cF_d^{-1}\in\Pic^0(E_f)[2]\setminus0$。
反不変線束$M_C=(r_*\OO_{E_f})^-$は
$r^*:\Pic^0(C_q)\to\Pic^0(E_f)$の核を生成し、
$(E_f,P_E)$と$(C_q,M_C)$は双対2-isogenyで交換される。
**この二曲線を混同して内在的O-pointed同値を推論しない。**
$E_f$上の二pencilはnoncubic MCM行列$M_c,M_d$の
right kernelから直接回収できる。
さらにAのnormal helixの二つの隣接乗法の像は
$\langle u,v,c\rangle,\ \langle u,v,d\rangle$であり、
二conicのVeronese対称積像に一致する。
この最後の比較は、全有限directed End代数の
同型やO-pointed qgr同値ではない。
証明正本：
[Cの点曲線・spectral曲線節](../papers/quiver-avatar/point_spectral_isogeny.tex)
（thm:qa-point-spectral-dual-two-isogeny,
prop:qa-point-mcm-matrix-pencils,
prop:qa-point-mcm-composition-veronese）。

**j値と古典modular polynomialの一次確認。**
$f_1=x(x-1), f_2=(x-2)(x-3)$における
$C_q:y^2=x(x-1)(x-2)(x-3)$と
$E_f:z^2=6t^4-7t^2+2$の二quarticの
$I,J$は$(13,-70)$と$(193,-5362)$。
四次形式の$I=12ae-3bd+c^2$、
$J=72ace+9bcd-27ad^2-27b^2e-2c^3$は
[Womackの論文付録](https://johncremona.github.io/theses/womack.pdf)
ならびに
[Cambridgeの文献](https://api.repository.cam.ac.uk/server/api/core/bitstreams/02fb71ba-0e5e-472e-ae84-bbfd55ab5917/content)
に記載される。
$\Phi_2(X,Y)$の古典的な7種の係数は
[MIT Sutherlandのmodular polynomial表](https://klein.mit.edu/~drew/ClassicalModPolys.html)
で確認した。
厳密有理数では$j(C_q)=35152/9$、
$j(E_f)=28756228/3$、$\Phi_2(j(C_q),j(E_f))=0$。
厳密算術の検算は`computations/verify_rootpair_resolvent_spectral.py`に収めた。
同じ式を作業環境で独立に再計算してPASS。
この結果は2-isogenyの幾何証明の整合検査であり、
AS分類やpointed同値を計算で検証したものではない。
二重isogenyのmoduli上の既知性と本件の
MCM演算の具体的貢献の網羅的新規性確認は未実施。

**区別：** 12本矢は8本のfinite foundation矢＋4本の
relation-dual戻り矢であることが多く、
12本矢QPであることだけから独立ASクラスの分類は従わない。
元草稿§43のP(1,1,2)の例はmutation局所仮定の不成立を示す。
Cの分類定理は体上の頂点保存AS代数の同型類についての結果。
`Qgr`のO-marked pointed同値と全基底上の無条件相対ASスタック同値は
他の認識入力を要する。
上記書誌識別子・原PDF中の引用箇所を確認したが、
外部論文の証明全体・版ごとの全仮定の独立照合、
網羅的優先権調査は未完了。

## OU2014 §4–5：座標置換群と楕円四つ組の一次資料

Shinnosuke Okawa and Kazushi Ueda,
*Noncommutative quadric surfaces and noncommutative conifolds*,
[arXiv:1403.0713v1](https://arxiv.org/pdf/1403.0713), 2014。
2026-11-22に印刷p.3 Theorem1.1、p.8 §4 (4.11)–(4.13)、
p.9 §5 (5.8)–(5.10)の一次PDFページを読み直した。
quintuple GITはP(2,4,4,6)、potential GITはP(1,2,3,4)、
potential→quintupleの有限射は次数4（既知）。
§5の対角表示は**P³/S4 → P³/(S4⋉(Z/2)³)**であり、
旧資料のS3座標置換という記載は誤りだったため訂正した。
even sign群の射影的有効商VはF2²、G=V⋊S4は96元、
S4のVへの作用核はKlein四元群K4。
一般Galois閉包の群G/K4はS4_mon（別の置換作用）。
Cでこの群論を証明し、検算コードを更新した。
§4の群はSL2(F2)⋉(Z/2)^4で、z1,z2の独立した二捩れ平行移動を含む。
Cは両群のindex4部分群まで含めた抽象同型
G=(V_sign⊕K4_coord)⋊S3≅(E[2]_{z2}⊕E[2]_{z1})⋊S3
を証明したが、**幾何的な同変双有理同型は未証明**。

Cの四重射は一般の自由作用開で
B=X/G、Y=X/S4を持つ有限étale射となり、
GのVへの線型作用で定めた変動群スキーム
𝒱=X×^G V_linのtorsorであることを証明。
この class [Y]∈H¹_et(B,𝒱) は、滑らかな対角一般開では
spectral Kummer模型と二quadric鉛筆のHodge符号により
Picardの$\delta_{[-2]}(N)$∈H¹_et(S,E[2])に実際に一致する。
正則半単純potentialの非対角族でも相対半点を構成済み。
この比較をpotentialを選ばない一般quintupleの相対groupoidへ
拡張する問題は残る。
OU §4の楕円四つ組(E,O(2o),O(2z1),O(2z2))に対する
半点O(o−z2)⊗E[2]はCで直接計算した。
potential上の同変半点の構成は同型を与える必要十分条件で、
上述の正則半単純一般開では明示的に構成した。
節点退化まで同型を延長することは、
OUの有限射とPicard[-2]のétale根空間の4対2という
fiber数の違いにより不可能と証明済み。
これらは原典の主定理ではなくCの新しい計算・補題である。

Bの相対効果性入力
prop:general-cubic-canonical-tails、
thm:geometric-cubic-relative-effectivity、
lem:picard-halves、
thm:relative-compatible-root はGitHub主原稿で照合した。
非線型geometric quintupleのcanonical tailsと構造対象は、
Picard根の選択前から存在する。
その根とAS4被覆をfppf局所のwitnessとして使い、
Cでquintuple→H2相対射を構成した。
全GIT compactificationへこの射が延長するという主張ではなく、
Bの全数学的証明を今回独立に全面検証したわけでもない。

**一般安定化群の有限部分に関する一次照合。**
同じOU2014の印刷p.3 Theorem1.1(1),(3)には、一般安定化群を
quintupleでGm⁴、potentialでGmとする表現がある。
印刷p.6 §3 (3.6)–(3.9)のSpin4→SO4 と
p.7 (3.10)–(3.19)の左右SO4作用を用いて、
本研究では全幾何慣性を独立に計算し直した。
一方のスカラートーラスを除いても、
非零・二乗固有値相異・trace非零の一般quintupleに
偶数符号行列/全符号反転 ≅ μ₂² の有限慣性が残る。
これは点曲線上のJac(C)[2]平行移動となる。
したがってOU2014の「一般安定化群」を**単位連結成分**
として読む必要があり、全慣性がGm⁴/Gmだけとする主張を
本研究では採用しない。この有限成分の指摘の独立した新規性は未確認。
有効potential・quintupleの正則半単純表示スタック間では
有限慣性同型・接写像同型を証明し、
OU既知の粗GIT有限次数4と合わせて一般有限étale四重射を得た。
これはOU主定理の粗モジュライの次数4を否定するものではない。
さらにVdB2011の幾何的商D→D_geomとcoh(C)の完全忠実埋込から一般μ₂²慣性がpointed忘却へ単射となる。Bの普遍非線型cubicのsmooth atlas `lem:universal-nonlinear-cubic-h2-family` を使うと剛体化quintuple→H2はsmooth相対次元0、一般開でétale、KS同型・HH¹=0・dimHH²=3となる。Bの二つの内在的foundationと楕円ruling交換は一般fiberの二点を与える。ゆえに一般有限étale次数2、potentialの合成では次数8。この相対比較の新規性は未確認で、Bのsmoothness証明全体を今回独立再点検したという意味ではない。詳しい証明はCのprop:qa-ou-generic-quintuple-finite-inertia、thm:qa-ou-rigid-potential-quintuple-generic-etale、prop:qa-ou-generic-inertia-faithful-to-h2。
今回確認したのは一次資料の表現・仮定・正則半単純模型であり、
OU全原稿の網羅的再監査ではない。

## 一般étale忘却と有限二重被覆の一次入力

本研究の論文Bの `lem:universal-nonlinear-cubic-h2-family` は、非線型
geometric quintupleの射影表示開から内在的H2への射が
representable smoothであることを、指定pointed Artin持上げに基づいて証明する。
`cor:cubic-formal-h2-abelian` は形式変形の接・自己同値のLieを
HH²・HH¹に同定し、`thm:global-h2-smooth-finite-type` は
H2がsmooth純次元3であることを示す。これらは未公刊の本研究内入力。
一般quintuple剛体化スタック側もsmooth純次元3であり、
Bの射との合成がsmoothなので、source smooth atlasによる局所判定から
忘却はsmooth相対次元0となる。

Stacks Project
[Tag 075T, Section 101.33](https://stacks.math.columbia.edu/tag/075T)
は代数スタック射のsmoothnessをsmooth source-and-target局所に判定する
定義と合成の性質を記す。これを2026-11-22に公開本文で確認した。
[Tag 0BBA, Lemma 68.21.1](https://stacks.math.columbia.edu/tag/0BBA)
は代数空間のquasi-separated finite type射について、
標的のgeneric point上のfiberが有限であることと、
そのgeneric pointを含む開に縮めてfiniteとなることが同値と示す。
同じく2026-11-22に本文を直接確認した。
本研究ではH2のsmooth atlasへ引き戻して適用し、étale descentで降下する。
この一般的事実と本研究固有の慣性単射・二foundationの復元を区別する。

論文Bの `cor:two-intrinsic-foundations` と
`cor:h2-point-groupoid-foundation` は
指定Oから始まる二つのnormalized foundationの充満な群oid記述、
`lem:elliptic-two-reflections` は
R:(η,δ)↦(2δ−η,δ)の具体的な楕円変換を与える。
CではこれらとVan den Berghのquintuple復元を合わせ、
j(E)≠0,1728、δ∉E[2]、η−δ∉E[2]、η∉{0,2δ}の開で二つのliftが
非同型・一般fiber二点であることを証明した。
有限étale二重射のcanonical involutionは
rank2 finite étale代数でi(a)=Tr(a)−aにより構成され、
幾何点でnormalized ruling交換に一致する。
従って稠密開の相対商H2≃[quintuple/S2]、
potentialの一般合成次数8もC原稿に証明を置く。
これらの一般的な先行研究に対する新規性の網羅的調査は未完了である。

**一般openの仮定の内部訂正と特別座。** R:(η,δ)↦(2δ−η,δ)の二つの四つ組の同型条件を再点検すると、一般二枚の非同型にはη−δ∉E[2]が必要。Cの一般開を修正した。j≠0,1728の許容楕円四つ組について交換自己同値が存在する必要十分条件はδ∈E[2]またはη−δ∈E[2]。正則半単純な該当点の全慣性は位数8。これはこの研究の直接証明であり、OU・VdBの文献に書かれていると推測した主張ではない。群拡大と局所分岐、新規性の網羅的確認は未了。

**特別座の群型の内部証明。** C prop:qa-elliptic-special-inertia-group-typesは片側の二捩れ条件下で全pointed慣性群型をtranslation側C4×C2、反転側C2³と計算した。OU/VdB既知の一般定理として推測・帰属せず、本研究内の幾何的群論証明として扱う。二条件同時やj=0,1728、粗空間分岐の検証は未了。

**二捩れ特別座の局所粗比較と一次資料。**
OU2014 §3の$SO_4\times SO_4\times\mathbb G_m$表示と§5の
$f_2,f_4,f_6,g_4$不変量を既知の入力として使用。
本研究Cでは、spectral曲線のWeierstrass座標から
$\delta\in E[2]\Leftrightarrow e_3+e_1c=0$、
$\eta-\delta\in E[2]\Leftrightarrow e_3-e_1c=0$と証明。
GIT重み6式$D_\pm=f_2^3-3f_2f_4+2f_6\pm6f_2g_4$が
正則半単純開の粗分岐座を表す。
Alper--Hall--Rydh, *A Luna étale slice theorem for algebraic stacks*,
Ann. Math. **191** (2020), 675–738,
DOI 10.4007/annals.2020.191.3.1
[刊行一次PDF](https://annals.math.princeton.edu/wp-content/uploads/annals-v191-n3-p01-s.pdf)
のTheorem 1.2（印刷p.676）を2026-11-22にページ画像で再確認。
必要な仮定はsmoothな**閉点**、線型簡約な**全**stabilizer、
quasi-separated locally finite-type stackとaffine stabilizers。
結論はnormal representation商との共通étale近傍であり、
global good/coarse moduliの存在ではない。
本研究では滑らかなfinite stabilizerのstable局所点に適用し、
formal coarse invariant ringの計算と組み合わせる。
片側二捩れ特別座は反射法表現と$Z=z^2$、
交点$e_1=e_3=0$では$H=C_2^3$、$A=D_8\times C_2$となり
source粗環が$k[[s,a,b,c]]/(b^2-ac)$となる。
これらの特殊群・局所粗式は既存文献の引用主張ではなく、
C本文で証明した本研究の結果（包括的新規性未確認）である。
計算コードはcomputations/verify_ou_special_reflection.py。
ここからj=0,1728やnoncubic境界、全H2へのglobal粗射を推論しない。

**CM elliptic automorphismsとlevel-two局所変形（一次資料）。**
Joseph H. Silverman, *The Arithmetic of Elliptic Curves*,
Graduate Texts in Mathematics **106**, Springer, 1986,
DOI [10.1007/978-1-4757-1920-8](https://doi.org/10.1007/978-1-4757-1920-8),
Chapter III, Theorem 10.1 and Corollary 10.2。
標数零のAut(E,0)がj一般値でC2、j=1728でC4、
j=0でC6となることを直接確認。
参考にA. V. Sutherland, MIT 18.782 Lecture 26 (2013),
[PDF](https://math.mit.edu/classes/18.782/2023sp/LectureNotes26.pdf),
Theorem 26.11 (PDF 0-index p.3)でも一次講義原稿を
ページ画像で確認した。
本研究ではCM環のNorm(1−i)=2、Norm(1−ζ3)=3、
1+ζ3=−ζ3²の単元性から、
二cubic開で追加CM自己同型が三束保存・ruling交換できないことを独立証明。
jはCM点で曲線変形の局所座標でないため、フルlevel-two
Legendre λ（j(λ)はj0で3重・1728で2重）へ置き換える。
この適用範囲の精密化は既存文献の未確認新規結果として推測せず、
本研究の直接証明と既知CM分類とを分ける。

**一cubic境界とj0のA4点（研究内の新しい直接証明）。**
滑らかなη=2δ、δ∉E[2]ではruling交換後の
η'=0で第二foundationがnoncubicとなる。
quintupleから内在H2へのpointed忘却はこの点で
representable étaleだが2-fiberは一点。
一般の有限étale次数2はこの境界へ同じsourceのままでは延長できない。
j=0、0≠δ∈ker(ζ3−1)≅C3、η=2δでは全慣性A4、
接のC3重み(2,1,1)で局所粗形式環は
k[[a,u,v]]^{C3}。これは全noncubic境界の定理ではない。
証明はCのCM補題・A4命題・一cubic境界系にあり、
通常のOU2014やVdB2011の定理として未確認のまま帰属させない。

**Artin変形と相対rulingの内部入力。** Cのprop:qa-ou-formal-two-ruling-liftsは、論文Bのthm:artin-foundation-lift（De Deken--Lowen 2011 Theorem 5.13の適用、flat geometric helixの同型類一意持上げ）と、prop:relative-ruling-involution/prop:ruling-involution-mutation（base change自然なkernel/cokernel mutation）から、全H2点の二normal foundationがArtin形式近傍で互いに非同型に持ち上がることを導く。これは文献の一般的なhelix変形定理の新規主張とは区別する。有限型の非被約基底での選択スタックの代数化、非cubic全境界への群oid同値は引き続き未証明。

**有限étale二択の降下と開埋込：一般理論の一次入力。** Stacks Project [Tag 0BLY, Lemma95.6.1](https://stacks.math.columbia.edu/tag/0BLY) は有限étale morphismのfppf効果的降下を与える。[Tag 0616, Lemma76.16.8](https://stacks.math.columbia.edu/tag/0616) は代数空間の局所有限表示・形式的étaleとétaleの同値、[Tag 05W4, Lemma67.51.2](https://stacks.math.columbia.edu/tag/05W4) はétale universally injective morphismの開埋込性を示す。今回これらの本文を一次web版で確認した。数学的固有入力はBの全H2 smooth atlas・relative perfect Morita/反Serre・Artin foundation deformation/効果的étale chart、およびCで構成した相対Homの二選択の開閉cocycleである。Cに全H2のfinite étale ruling coverと、選択付きH2から有限foundationスタックの実現可能開への開埋込・S2商同型を証明として統合した。**未確認点**：Bの全原稿にわたる相対perfectness/Artin効果性の全面独立監査、非被約基底のKスカラー比較の独立形式検証、有限minorによる実現可能開のexplicitな認識条件。既存の一般定理と本研究固有のH2群oid比較を区別し、結果の新規性は未確認。

**非構成的有限多項式判定と可換gerbeの証明範囲。** U0⊂A64は有限型開、realizable W_Hは開なので、その閉補集合のイデアルがNoether性で有限生成となる。G/Kのrational作用で有限次元安定部分表現を選べる。これはStacksの一般原理と本研究の新しい相対開埋込の形式的帰結で、explicitな演算アルゴリズムではない。可換QのAut=(PGL2×PGL2)⋊C2の因子交換からruling coverの非自明性が従う。C cor:qa-realizable-foundation-finite-open-criterion、cor:qa-ruling-cover-nontrivial-commutative-gerbeに証明。文献の包括的新規性は未確認。

**VdB geometric開の明示多項式化。** Van den Bergh 2011 Definition 5.3.1とB prop:cubic-foundation-openの隣接二因子縮約非退化条件をC lem:qa-explicit-cubic-geometric-adjugateで明示quartic/sexticの計20個の多項式に変換した。rank3のkerがSegreの分解可能座を避けることとadjugate列の2×2det非零を同定する直接線形代数。幾何的cubic開の存在自体はVdBの既知入力で、20式への具体化の包括的新規性は未確認。このcubic補題自体はnoncubic全realizable開に適用しない。全H2開は新しい四交差条件の定理で別に認識した。

**O-marked–potential–avatarの三者比較に使った既知入力・内部資料。**
Michel Van den Bergh, *Noncommutative quadrics*, IMRN 2011,
Theorem 5.5.10 (arXiv:0807.3753v3)：
geometric cubic Z-algebraと許容楕円四つ組の分類。
Okawa--Ueda, *Noncommutative quadric surfaces and
noncommutative conifolds*, arXiv:1403.0713 (2014)：
conifold potentialの既存GITからquadric GITへの有限次数4射。
本研究Bのcor:two-intrinsic-foundationsと
lem:elliptic-two-reflectionsを用い、
CでO-marked同型類のruling反射商を新たに証明。
大川--植田の未公刊日本語草稿 *非可換二次曲面の二つの反標準avatar*
（2026-09-16 v7、内部参考文献AvatarVSeven2026）と
未公刊quadric_synthesis_ja_20261017_v1.pdf の
§§7.12, 8.3に
(A_c,B_c,A_cP)=(F_sP^{-1},G_sP^{-1},F_s)、
r1(F_s,G_s,P)=(G_sP^{-1},F_sP,P)
が記載されていることを今回Libraryの本文で照合した。
これらはAS Z-algebraの標識付き分類であり、
O-marked全同値類・相対heartの定理と
混同しない。
Cの新定理で滑らかな楕円cubicの
この明示式の双方向性・O-markingのr1商を証明。
noncubic側はBの二根対分類から、smooth楕円2torsion avatar壁と
四根相異なるroot-pair同型類を
二重被覆/branch pairingで直接同定した。
Legendre座標では(x,y)→(λ/x,−λy/x²)。
この幾何的同型類の全単射が
avatar AS側から実際のO-marked heartを与える
ことまで証明していない。
P=O_Dを全Dに追加すると可換foundationの
重複計上がある（Cの制限列で直接証明）。
Sigma2古典weighted型はstrong H2に無条件に入らない。
退化因子・潜在的な相対AS認識・全potential安定化の
一次資料/包括的新規性照合は未完了。

**noncubic quartic resolvent・torsion-free spectral avatarの新しい比較。**
既知入力：J. E. Cremona, *Reduction of Binary Cubic and Quartic Forms*,
LMS J. Comput. Math. 2 (1999), 62–92,
DOI 10.1112/S1461157000000073,
§4.3のquartic cubic-resolventと分割三通りを一次刊行PDFで確認。
Cremona (2001)のcorrigendumは別のProposition14への訂正で、
今回のquartic-resolvent式には依存しない。
A. B. Altman and S. L. Kleiman, *Compactifying the Picard scheme*,
Adv. Math. 35 (1980), 50–112,
DOI 10.1016/0001-8708(80)90043-2 は
rank-one torsion-free sheafを使う将来のcompactified Picardの
基本文献として書誌情報を確認（本文全体は未確認）。
本研究で新たに直接証明：noncubicの二根対すべての幾何同型類を
smooth/nodal/I2のP≠O,P²=O square(2,2) avatarと全単射で
比較し、同じC_qに対しcentral-square B_fの可換化の点曲線
E_fの同時符号反不変module Mでtorsion-free spectral相対射を構成。
共有根f1=x(x−1),f2=(x−s)(x−2)では
A=k[[x,s,y]]/(y²−x(x−s))≅k[[c,d]]^{±}、
M=Ac+Adの非自由性から、相対Pic0線束への直接延長を否定。
これらはC本文の証明であり、CremonaやAltman--Kleimanが
今回の分類・相対障害を既に示したという意味ではない。
元avatar AS qgrとO-marked heartの同値、
Σ2 minimal resolution/elementary transform、全potential相対射は未証明。
この未確認点を新規性の推測で埋めない。

**Σ₂での全noncubic分類を証明：** 負断面Sを避ける反標準因子D∈|−K_{Σ₂}|と0≠P∈Pic⁰(D)[2]の幾何同型類は、全noncubic O-marked quadricの幾何exact同型類と全単射（C thm:qa-all-noncubic-sigma2-anticanonical-avatar-bijection）。H=O(h)|D=F²、F=O(f)|Dを用いるsquare換算はF_s=F,G_s=FP。P非自明2捩れによりDはsmooth、既約nodal、二P¹二節点(I2)の三型だけ。Bの良moduliでχ=1に重なる一根共有と根対一致も、Σ₂のnodalとI2で区別（C cor:qa-sigma2-avatar-separates-special-noncubic-classes）。これは**体上の同型類全単射**で、avatar AS代数の元のqgr heartとO-markedの直接同値、非被約底の通常Pic⁰線束を使う相対射ではない。 既知の幾何変換はC cor:qa-square-chartに証明され、Bのnoncubic二形式群oid分類と合成した今回のΣ₂分類は新たなCの直接証明。包括的新規性は未調査。

## 研究の位置

本研究の対象は、構造として指定された $(\mathcal C,\mathcal O)$ であり、exact autoequivalence $s$、同型 $s^2\simeq\mathbb S^{-1}[2]$、および orbit algebra の quadratic AS-regular ambient 表示は存在条件として扱う。この区別を保った分類と marking 忘却が課題である。

既知の cubic AS-regular $\mathbb Z$-algebra、geometric quintuple、admissible quadruple の分類や hypersurface embedding を新成果として扱わない。特に、quadratic hull の存在と quadratic envelope による canonical recovery は別の主張である。

Alper–Hall–Rydh, *A Luna étale slice theorem for algebraic stacks*, Annals of Mathematics **191** (2020), 675–738, DOI [10.4007/annals.2020.191.3.1](https://doi.org/10.4007/annals.2020.191.3.1)。[刊行PDF](https://annals.math.princeton.edu/wp-content/uploads/annals-v191-n3-p01-s.pdf)のTheorem 1.2（印刷p.676）を2026-11-22に本文画像で直接確認した。quasi-separatedな局所有限型Artinスタック、affine stabilizers、閉じたsmooth点、線型簡約な**全**stabilizerが仮定である。normal representationのGIT商へのaffine étale近傍と、それをbasechangeしたquotient stackからのétale写像を与える。affine diagonalなら後者をaffineに選べる。対象の良モジュライ射をZariski開へ無条件に降下させる主張ではない。本研究の一致類ではfull H_eqの線型簡約性、閉点性、smooth・affine diagonalを本文で照合した。

## De Deken–Lowenとatlas・framedの一次資料

Olivier De Deken and Wendy Lowen, *Abelian and derived deformations in the presence of $\mathbb Z$-generating geometric helices*, J. Noncommut. Geom. **5** (2011), no.4, 477–505, DOI [10.4171/JNCG/83](https://doi.org/10.4171/JNCG/83)。
[刊行一次PDF](https://ems.press/content/serial-article-files/30497) pp.501–502のDefinition5.12とTheorem5.13(1)–(4)を2026-11-22に直接確認した。(1)一意なhelix持上げ、(2)flat heart対象のflat持上げ、(3)strong性・四項窓内のHomの平坦性、(4)geometric性・全前向きHomの平坦性を区別する。$D^-_{\mathrm{ffd}}$とflat Grothendieck変形の仮定も必要。BのArtin持上げ補題では(4)を全前向きHomに用いる。

Stacks Project [Tag 02HY](https://stacks.math.columbia.edu/tag/02HY), Lemma 37.12.2：局所Noetherian基底上で局所有限型scheme射のsmooth性をsmall Artin持上げで判定する。有限型$k$-schemeの閉点の剰余体が$k$であることを使い、指定pointed同型を含むliftingを要求する。
[Tag 05W6](https://stacks.math.columbia.edu/tag/05W6), Lemma 76.14.8：locally finite type monomorphism of algebraic spacesはunramified・separated・locally quasi-finite・representableとなる。
[Tag 03XX](https://stacks.math.columbia.edu/tag/03XX), Proposition 67.50.2：schemeへのseparated locally quasi-finiteな代数空間の射は始域のscheme性を与える。
Bのframed実現の原稿引用に一致するが、開あるいは局所閉immersionを結論する入力ではない。
これらは各引用箇所の一次本文の確認であり、本研究の全相対構成の完全な形式検証ではない。

## AS正則 Z-algebra の単純加群双対条件と引用先

Mori–Nyman, A categorical characterization of quantum projective Z-spaces（書誌はMN2025）。
著者公開原稿 [regV8.pdf](https://faculty.nymana.wwu.edu/regV8.pdf) の印刷p.23, Definition 4.2 (ASR1)--(ASR2) を2026-11-22に一次資料として直接確認した。
ASR1は各右単純加群 $S_i$ のprojective dimensionが $d$ であること、
ASR2は
\[
 \operatorname{Ext}_C^q(S_i,P_j)=
 \begin{cases}k&q=d,\ j=i+\ell,\\0&\text{それ以外}\end{cases}
\]
を要求する。五頂点barの(BW-fiber)は、分類論文Aのnormal helixから得る
$d=3,\ell=4$ のAS正則Z-algebraにこれを適用する。
同論文Theorem 4.8はAS正則からASF正則への含意であり、
Proposition 4.11はASF局所コホモロジーとExtの比較である。
この二箇所を単純加群Ext消滅の直接根拠とはしない。
各最小projective解消に現れる $P_{i+4}$ 一個という事実は
論文Aの cor:normal-cubic-defect を別に用いる。
今回は著者稿regV8の該当箇所を確認したもので、arXiv v1や出版版の
定理番号の完全一致まで確認したものではない。

Shelton–Tingey, *On Koszul Algebras and a New Construction of Artin–Schelter Regular Algebras*, J. Algebra 241 (2001), 789–798, DOI [10.1006/jabr.2001.8781](https://doi.org/10.1006/jabr.2001.8781)。刊行版のabstractで「Koszul代数のregular normal quadratic elementによる商はKoszul」を確認（2026-11-22）。論文Bの有限型中央被覆では、各fiberで既にKoszulな$E=B^!$と、独立に証明した中央正則性を使ってこの定理を適用する。Koszul locusの一般的な開性に置き換えることはできない。

## compact 局所化の一次資料

Amnon Neeman, *The connection between the K-theory localization theorem of Thomason, Trobaugh and Yao and the smashing subcategories of Bousfield and Ravenel*, **Ann. Sci. Éc. Norm. Supér.** (4) **25** (1992), no.5, 547–566, DOI [10.24033/asens.1659](https://doi.org/10.24033/asens.1659), [一次PDF](https://www.numdam.org/article/ASENS_1992_4_25_5_547_0.pdf)。
2026-11-22にTheorem 2.1（印刷p.550）の原文・仮定を確認した。
compactly generated三角圏をcompact対象集合で生成されるlocalizing部分圏で割った商はcompactly generatedとなり、商関手はcompact対象をcompact対象へ送る。
本稿Bではまずtorsion核をcompactな頂点単純対象で生成することを独立に証明してから適用する。
この定理だけでは四項のtilting性や相対AS/heartを保証しない。

## Belmansの既知Hochschild計算との対照

Pieter Belmans, *Hochschild cohomology of noncommutative planes and quadrics*, **J. Noncommut. Geom.** 13 (2019), no. 2, 769–795, DOI [10.4171/JNCG/338](https://doi.org/10.4171/JNCG/338), [arXiv:1705.06098v2](https://arxiv.org/abs/1705.06098v2)。2026-11-22に原文のProposition 31、Corollary 32、Table 2と出版社書誌を確認。cubic AS正則Z-algebraからの四項tilting代数は大域次元2であり、高次HHの消滅とdim HH²−dim HH¹=3、および幾何的四つ組の退化型別の表が得られる。これは強いH2のcubic領域に対する既知入力であり、cubic表示を持たないnoncubic領域には無条件に適用しない。

現行Bのcubic foundationの高次HH消滅・数値差はBelmansとの既知の重なりを明記する。全H2の相対効果性、noncubic横断変形、境界の相対groupoid・慣性と形式対は別の主張であり、包括的新規性は未確認。原文の定理の確認と、原稿の全証明の独立検証は別の状態とする。

### Veronese 同値の参照状況（2026-11-21）

A. B. Verevkin, *On a noncommutative analogue of the category of coherent sheaves on a projective scheme*, *American Mathematical Society Translations*, Series 2, **151** (1992), 41–53, DOI [10.1090/trans2/151/02](https://doi.org/10.1090/trans2/151/02)。書誌は Math-Net.Ru の著者書誌と後続論文の参考文献で照合した。**原著 Theorem 4.4 の全文は今回直接閲覧できていない。** 次数一生成された次数環の Veronese が QGr を保つとの定理内容は S. Paul Smith, *Advances in Mathematics* 230 (2012), p.1784（[著者公開PDF](https://sites.math.washington.edu/~smith/Research/QGr-kQ.pdf)）に明示される定理4.4の引用で確認した。現行 noncubic 族で必要な一般 noetherian 底への拡張は、原著の適用範囲に無条件に含めず、次数一生成性からの偶奇成分比較と torsion 商の議論を主原稿 `prop:noncubic-relative-heart-veronese` に書いた。

**局所 Noetherian 性と相対χの参照範囲。** 3次元cubic AS正則環・幾何的quintupleの体上分類は `VdB2011` の既知結果として使う。体上Noetherian性を偶数Veroneseへ移す際のイデアルの有限生成性は主原稿 `prop:weighted-even-koszul` の証明に明記。一般Noetherian特殊fiberへの局所持上げは `lem:local-commutative-fibre-noetherian`（標題・証明は非可換fiberにも拡張）で証明し、有限次元Noetherian局所基底への相対χの持上げは `lem:local-chi-specialization` で証明した。可換Segre環のχは可換Noetherian次数環の標準Ext有限性から従う。体上Noetherian性の正確な参照は `VdB2011` arXiv:0807.3753v3, Corollary 5.5.9(1)（p.20）であり、原文を確認した。同(3)は体上qgrのExt-finiteを述べる。Definition 8.1では相対familyのNoetherian性を仮定しており、この引用から有限型開全体のNoetherian性は導かない。局所基底上の全有限型変更でのχ・AZは、本文の中心変数補題によって別に証明した。

**非可換quadricの体上χの一次資料。** S. Paul Smith–Michel Van den Bergh, *Noncommutative quadric surfaces*, *J. Noncommut. Geom.* **7** (2013), 817–856, [DOI](https://doi.org/10.4171/JNCG/136)。[著者版PDF](https://sites.math.washington.edu/~smith/Research/pencil-nc-quadrics.pdf) の §2.8（著者版p.7）をテキストとページ画像で確認した。Noetherianなquadratic AS正則4次元環の正則正規二次元商には左右χが成立する。体上の既知結果であり、相対基底への拡張は本研究の局所持上げ補題を別に使う。書誌キー `SVdB2013` は既に存在する。

**構造対象の相対depth3と完全saturation。** Smith–Van den Bergh `SVdB2013` §2.8 の体上AS4正規二次商はGorenstein深さ3でExt^j_B(k,B)=0（j<3）。`lem:relative-depth-three-saturation` は相対Koszul cochainの内部次数ごとの分裂完全性から任意基底変更の低次Ext消滅と構造対象の全切断環を回復する。`cor:relative-depth-three-coefficients` では任意係数Nへ拡張し、QGrのYoneda拡大を十分深いtailに沿って引き戻してH¹=0も証明した。体上結果は既知、相対基底での証明は本文に置く。一般論としての新規性は未確認。

**AZ豊富性の証明範囲。** Artin–Zhang [AZ1994, Proposition 4.4] の体上のχ₁⇒ample方向は、複数の後続文献で確認できるが、任意Noetherian係数環への適用範囲を原典から完全には照合していない。本原稿の `lem:relative-chi1-implies-AZ-A2` はそれに依存せず、有限projectiveな各B_nと相対χ₁から、B/B_{≥n}のExt¹がnに依存しない高次数で消えることを直接証明してAZ(A2)を得る。局所相対χ₁によって可換点を閉点とする全Noetherian局所基底でこの条件が適用できる。有限型中心基底変更後のχ₁は `lem:chi-finite-type-basechange` で証明し、一般coherent Hom有限・flat basechangeを `lem:chi1-qgr-hom-finite-flat` で直接導いた。これらの一般補題の独立な新規性は主張しない。

## 二次Veroneseの既知結果と今回の相対適用

A. Polishchuk, L. Positselski, *Quadratic Algebras*, AMS University Lecture Series **37** (2005), Chapter 3, Proposition 2.2(i) は、一次生成・二次・Koszulである環のVeroneseもそれぞれ一次生成・二次・Koszulであることを述べる。AMSの[書誌](https://doi.org/10.1090/ulect/037)を確認し、[公開テキスト](https://djvu.online/file/T1DOlccPNeqX0)で該当命題文を照合した。**これは既知の一般定理であり、本研究の新成果としない。** 本稿の lem:relative-quadratic-veronese は、任意の可換係数環上のtensor商による直接証明とZhang twistへの明示拡張、lem:relative-quadratic-from-fibers はNoetherian基底上の局所自由性とNakayamaによる全次数の相対降下である。これらをcubic・noncubic・特殊化族の反Serre環へ適用したこと、および25 pivotの具体的な閉埋込みが本研究の追加部分（全体的な先行研究に対する新規性は未確定）。

有限型スキームの射の構成可能像にはStacks Project [Tag 054K](https://stacks.math.columbia.edu/tag/054K)（Chevalleyの定理）を使用する。全H2反Serre関係像はcubic・noncubicの二つの有限型表示からの構成可能集合である。関係式の被約閉包Z₂は有限型既約の代数的包絡だが、相対H2の実現部分関手のscheme structureを表すものではない。

## 相対Picard作用と全cubic atlas

M. Artin, J. Tate, M. Van den Bergh, *Modules over regular algebras of dimension 3*, Inventiones Mathematicae **106** (1991), 335–388, [DOI:10.1007/BF01243916](https://doi.org/10.1007/BF01243916)。Göttingen公開原典pp.355–358の本文を確認した。Proposition5.5とCorollary5.7は任意基底上の相対Picard作用を与える。`5.8の符号に従うηについて、Lemma5.10(iii)のη(a)*L=L⊗a^(−deg L)は体上の主張である。相対等式はこの式を無条件に一般化せず、普遍基底の被約性とPicardのdiagonal immersionで証明する。非被約曲線も扱う原典の範囲を保つ。

Stacks Project [Tag 0DMD](https://stacks.math.columbia.edu/tag/0DMD), Lemmas108.9.2/108.9.5と[Tag 0DM9](https://stacks.math.columbia.edu/tag/0DM9), Lemma108.8.5を確認した。proper flat fp、π_*O=Oの普遍性の下でPicardは代数空間となり、diagonalはquasi-compact immersion、相対曲線ではsmoothである。本稿は多重次数零のfiberの連結性から[−2]のétale全射性を得る。 fiberwise identity componentの開性には、Holmes–Molcho–Orecchia–Poiret, *Models of Jacobians of curves*, J. reine angew. Math.801(2023),115–159, [DOI:10.1515/crelle-2023-0031](https://doi.org/10.1515/crelle-2023-0031), Appendix A Lemma A.1（[arXiv v2](https://arxiv.org/abs/2007.10792)）を用いる。quasi-separated・flat・locally finite presentation・幾何fiber被約という仮定と、準コンパクト性を要求しない本文・証明を確認した。Serre比較は既存のperfect双加群比較の局所閉性とsmooth reduced普遍根基底で証明し、任意の非被約底へは実際の同型を引き戻す。quintupleからの全Artin持上げはDDLの既知入力と、本稿のrank7関係核・rank1重なりの有限自由線形代数を組み合わせる。相対化全体の包括的な新規性は未確認である。

## 相対canonical hullと可換点の全Artin変形

K. Bauwens, M. Van den Bergh, *Normalizing Extensions of the Two-Veronese of a Three-Dimensional Artin–Schelter Regular Algebra on Two Generators*, *Journal of Algebra* **205** (2) (1998), 368–390、[DOI:10.1006/jabr.1997.7210](https://doi.org/10.1006/jabr.1997.7210)、[著者公開本文](https://cantate.be/site/kristien.ps)を確認した。文献キーは `BauwensVanDenBergh1998`。Proposition 2.2・式(2.7)・Lemma 2.4は二次VeroneseのKoszul双対とその次数三の直和分解を記述する。Proposition 2.7・式(2.11)は正規化functional、Proposition 3.2は正規拡大との双対的対応、Remark 3.3・式(3.1)はcanonicalな選択と被覆の関係式を与える。**これらは体上の通常の次数付きcubic環についての既知結果である。** そのまま任意のArtin係数環上の存在定理として引用しない。

`VdB2011` の arXiv v3 §5.2は非退化四次tensorと四周期、§6（Theorem 6.1、Lemmas 6.4–6.5）はcanonical hull、§8.3は可換quadricの変形とcubic列との関係を扱う。体上のhullの存在、変形されたcubic列の構成、および指定された二周期から通常の次数付きAS4被覆を相対的に作ることは区別する。特に、二周期cubic $\mathbb Z$-algebraの持上げから通常のcubic graded algebraの一周期性を推測しない。

主原稿 `sec:universal-cubic-hull` は、任意Noetherian基底のgeometric二周期cubic族に対し、この構成を相対化する。式(2.11)はψ(fᵢxⱼ)=η(Λ⁻¹)ⱼᵢ、ψ(xᵢfⱼ)=η(ΛQ⁻ᵗ)ᵢⱼであり、canonical choice Λ=Qᵗは二つの逆coevaluationと一致する。一般Z代数ではVdB Theorem6.1のhullのnormalizerを次数三の第二直和成分へ制限し、F⊗id=id⊗Gからscalar性を得て、φ(w)=2で二側を一致させる。これにより既知hullの関係が実際にker Φであることを同定する。

相対化ではE=B!の次数別projectivityから正規線Nの乗法を局所分裂単射にし、P=E/(N)のflatnessを先に得る。その後PP Chapter6 Theorem7.3をPへ適用してA=P!を全次数projectiveにする。有限projective間のfiber同型判定により、Frobenius pairingと正則正規二次商を基底上で確認する。βとcanonical四周期θを区別し、T=β⁻²θに対してφξ=(ξ∘T)φ、gu=T⁻¹(u)gという向きもtensor式で確かめた。Serre平方条件はこのAS4被覆の構成に含めず、別の双加群比較条件とする。

`sec:quadric-artin-hull` は一般定理を可換Qの全Artin変形へ適用する節である。標準Serre根の持上げと `prop:artin-witness-relative-promotion` によって全相対条件を得る。BV1998・VdB2011の体上の結果は既知入力であり、相対化の包括的な新規性は未確認。証明を独立読取りしたが、形式証明器・外部査読による検証は未実施である。全H2点の全Abel Artin変形への適合根とAS4被覆は、cubic側の相対Picard構成とnoncubic側の中央被覆延長により供給した。全H2の有限型代数性は残る。

## Koszul 性・Hochschild 変形・三次平坦性

二重平方環の PBW 基底と二次 Gröbner 表示から Koszul 性を導く入力は Priddy の quadratic PBW theorem（Polishchuk--Positselski, *Quadratic Algebras*, Chapter 4, Theorem 3.1 にまとめられた既知結果）である。Koszul 性が Veronese で保存されることは同書 Chapter 3, Proposition 2.2(i)、Zhang twist による次数付き自由解消の移送は同値の形式から従う。これらを本研究独自の一般定理とはしない。

同書 **Chapter 6, Proposition 7.1, Proposition 7.2, Theorem 7.3（pp.128–130）** の本文・証明を公開テキストで照合した。係数環は任意のNoetherian局所環であり、被約性・整性・完備性を要求しない。二次環の各次数が有限生成で、一次・二次・三次が自由、剰余体の環がKoszulなら、全次数が自由で、関係部分加群の格子は分配的かつ全商が自由となる。本稿 `lem:relative-koszul-degree-three` はこの既知定理を適用し、交叉の任意底変更と相対Koszul解消を明示する。既存一次補題の直接Hochschild証明は保持するが、二次jetの全次数平坦性も `cor:noncubic-second-order-all-degrees` により確立した。高次Artin持上げ自体・相対H2認識の証明とは区別する。

同書 Chapter 2, Corollary 6.3はKoszul環の正則正規二次商がKoszulであることを含む。本稿 `prop:all-h2-antiserre-koszul` では中心性が不要であることを明記し、二行の環変換Torスペクトル系列による直接証明を併記した。

thm:noncubic-hh01-hh2 の低次 HH の次数零成分の計算は、Hochschild-Koszul cochain C¹=Hom(V,R₁)、C²=Hom(J,R₂)、C³=Hom((V⊗J)∩(J⊗V),R₃) における微分の階数と生成元の基底変更軌道を照合したもの。既存の有限 foundation 代数に関する HH≥3 消滅とは異なる。noncubic の横断法方向で二次障害が消えるという局所計算の先行研究上の新規性は未確定。

## 相対Abel圏と再構成の参照

De Deken–Lowen, *Abelian and derived deformations in the presence of Z-generating geometric helices*, J. Noncommut. Geom.5 (2011),477–505, [DOI:10.4171/JNCG/83](https://doi.org/10.4171/JNCG/83)、[出版版](https://ems.press/content/serial-article-files/30497)の§4.1、Theorem4.5、Proposition4.6、Propositions5.5–5.10、Definition5.12、Theorems5.13/5.15を照合した。元のnormal helixはInd圏でcompactに生成し、geometric性とAZ豊富性からZ-generatingであるため、全flat Abel Artin変形への適用条件を満たす。helixの持上げとAbel/有限代数の変形比較は既知定理。本稿の追加はcanonical偏極の回復、有限m-filtrationによるheart exactness、偏極忘却の接核HH¹と具体Zhang方向の同定であり、新規性の包括的判定は未実施。

Serre根のArtin補正は、近恒等自己同型の有限log/expとperfect双加群複体の曲率を用いて直接証明する。可換Qの四根の一次持上げには、既存の必要条件に加えてToda arXiv:math/0502571v3 Theorem4.7の十分性を用いる。全Artinへの延長はこの一次の定理をそのまま外挿せず、small extensionの合成障害b+s_*bと平方関係の補正を各段で証明する。

Stacks Project [Tag 00IP](https://stacks.math.columbia.edu/tag/00IP) の Krull 交叉定理（Noetherian局所環と有限加群における ∩m^n M=0）は、代数的候補の有限個の閉条件を全Artin厚みから局所環へ確認する一般的な補助手段である。本研究のcanonical hullは普遍的なtensor構成で直接証明し、この手段やArtin近似 [Tag 0CAT](https://stacks.math.columbia.edu/tag/0CAT) は必要としない。

Stacks Project [Tag 0BDH](https://stacks.math.columbia.edu/tag/0BDH), Lemma 36.31.1のperfect複体のBetti数の上半連続性と、Lemma 36.31.4の最低次cohomologyを普遍的に一定階数へする有限表示局所閉部分を本文確認した。`lem:lowest-hom-line-locus` は階数1の場合を実際のminor消去で直接証明する。`thm:bimodule-line-comparison` は普遍的に中心が基底環である可逆双加群にこれを適用し、比較線束の評価coneの消滅により、fppf局所同型の存在部分を有限表示局所閉として構成する。一般のperfect複体の半連続性・rank層別を新成果とはしない。比較定理の包括的な先行研究上の新規性は未確認である。

Lowen–Van den Bergh, *Deformation theory of abelian categories*, Trans. AMS 358 (2006), 5441–5483 の[著者公開本文](https://cantate.be/site/def_submitted.pdf)で、Prop.3.1/Def.3.2のTorのco-effaceabilityによるflatness、Prop.3.6のIndとの両立、§4のmodule-object基底変更、Prop.6.34のExtとfiltered colimitの交換を確認した。これらは既知の一般理論であり、本稿はArtin X3族のqgrと定数族のfield recoveryへ適用する。

同論文のProposition4.7（反対圏でのTor/Ext change-of-ringsも含む）、Theorem7.1（nilpotent Abel変形と局所化の対応）、Proposition8.12（局所化上の変形関手）、Lemma8.13（完全本質的全射によるflatness）も本文確認した。可換quadricの一次Jacobian環について、斉次Ore局所化を明示し、局所環の二コサイクルγ_f/2をAbel変形の局所制限として認識する。

Lowen–Van den Bergh, *Hochschild cohomology of abelian categories and ringed spaces*, Advances in Mathematics **198** (2005),172–221、[DOI](https://doi.org/10.1016/j.aim.2004.11.010)、[著者版](https://cantate.be/site/hochschild_ab.pdf)のTheorem3.1・Remark3.5（体上のAbel変形とHH²/HH³）、Corollaries7.7.2–7.7.3、Theorem7.8.1/Corollary7.8.2、§7.9を確認した。Abel圏のHHとaffine被覆・対角のExtの比較、openへの制限との整合に用いる。これらは既知結果であり、本文 `prop:quadric-jacobian-abelian-class` では局所計算から大域HH²類を認識する。HKRの反対称化に1/2を入れる規約を明示し、指定bivector hにはf=h/2を用いる。一次Jacobian構成と相対H2への適用について、包括的な先行研究上の新規性は未確定である。

Alper–Halpern-Leistner–Heinloth, *Existence of moduli spaces for algebraic stacks*, Invent. Math.234 (2023), 949–1038、[arXiv:1812.01128v5](https://arxiv.org/abs/1812.01128v5) §7.1 Def.7.3/Rem.7.4–7.5を本文確認した。有限型basechangeの局所noetherian性とflat descentについてAZ2001 B6.3/C8.6を明記している。AZ2001原文は未取得であり、再録を確認した状態と区別する。この論文の固定Abel圏内の対象moduliを、変動するH2の代数性に適用したとは主張しない。

AZ1994 Theorem4.5(1)の一般End-ring版は、Okawa–Abdelgadir–Chan–Ueda, *Degenerations of orbifold curves as noncommutative varieties*, Nagoya Math.J.261 (2026), e4、[DOI](https://doi.org/10.1017/nmj.2025.10067)、Theorem7.3の再録本文で確認した。O noetherian、End(O) right-noetherian、全Hom(O,M)有限End(O)、ampleが仮定である。AZ1994原文自体は未取得。fieldのHom有限次元版だけから一般係数版を推測したものではない。

Keller, *Deriving DG categories*, Ann.Sci.ENS(4)27 (1994),63–102の[著者本文](https://webusers.imj-prg.fr/~bernhard.keller/publ/ddc.pdf) §§4.3,8.2をcompact generatorによるMoritaに用いる。Toën2012の導来圏のdescentを、heartの一致だけでcanonical D(Ind C)のdescentと同一視しない。現行定義では導来条件をfppf局所に課し、この大域同定に依存しない。

Zhang, *Twisted Graded Algebras and Equivalences of Graded Categories*, Proc.London Math.Soc.(3)72(2) (1996),281–311、[DOI](https://doi.org/10.1112/plms/s3-72.2.281)の書誌とTheorem3.1の公開原文索引を確認した。本文PDFの直接openは取得制限があった。本稿の係数環上・右規約で必要な同値は `prop:antiserre-polarization-family` にmodule actionと逆構成を明示して直接証明している。一定qgr・非一定表示の具体族と中心交換子による検出を記すが、包括的新規性は未確定である。

## 相対cubic tailsとcanonical導来比較

Bondal–Van den Bergh, *Generators and representability of functors in commutative and noncommutative geometry*, Moscow Mathematical Journal **3** (2003), 1–36, DOI [10.17323/1609-4514-2003-3-1-1-36](https://doi.org/10.17323/1609-4514-2003-3-1-1-36), [arXiv math/0204218v2](https://arxiv.org/abs/math/0204218v2) の§4.1、Lemmas 4.1.3–4.1.7と直後のunbounded導来関手、Lemma 4.2.2を一次PDFで確認した。原典の体上の仮定を一般基底へ無条件に適用せず、現行 `relative_cubic_tails.tex` では、有限projective係数のcubic解消を用いてtorsionのacyclicity・cdτ≤3・cdω≤2・直和整合性を再証明する。局所化の向きはπ⊣Rω、三角はRτX→X→RωπXである。

四項tiltingからのMorita同値はKeller1994 §§4.3,8.2を用いる。体上分類・Noetherian性はVdB2011の別の入力である。相対定理はNoetherian性なしのGrothendieck導来比較と、Noetherian性を仮定したcoherent heartの全相対認識を区別する。全χの証明では、有限presentationとcohomological dimension二から同じ基底全体のSerre消滅を得る。新規性の包括的な文献比較は完了していない。

## 五頂点窓・局所中央被覆・全Artin認識

Stacks Project [Tag 0BDK, Lemma 36.31.3](https://stacks.math.columbia.edu/tag/0BDK) は、perfect複体が所定次数・所定階数の局所自由加群になる開部分を、任意の導来引戻しと両立する普遍性で特徴づける。2026-11-21に原文を確認した。局所環の閉点でこの条件が成立すれば同じ局所環全体で成立する。本稿はこれを全前向きHomごと、および有限bar複体の各成分へ適用する。無限個の開集合の交叉を開とする定理ではない。

noncubicの五頂点非極小bar、中心線と反中心消滅による中央AS4横断延長は本文の直接証明であり、既知文献の定理として引用しない。canonical周期のSerre同定は `lem:cubic-serre-period` に依存する。Mori–Nyman [著者PDF](https://faculty.nymana.wwu.edu/regV8.pdf) Theorem 6.8のASF++仮定を保ち、本文で必要な双加群構造を確認する。De Deken–Lowen [EMS原典](https://ems.press/content/serial-article-files/30497) Theorems 5.13, 5.15によるhelix/thread変形比較は既知入力であり、指定閉fiberの同型を保つ基底選択とétale lift、相対H2への昇格は本文で行う。中央AS4被覆・局所横断構成の包括的な先行研究比較と新規性確定は未完了。

## Noetherian 性の貼合せと非可換P¹束の障害

Stacks Project §10.97（Tags 00MA, 00MB, 031C, 05GH）と§10.39（Tag 00HQ）の一次本文で、有限加群の完備化、完備化の平坦性・商・Noetherian性、忠実平坦性の判定を確認した。次数別完備化を用いる非可換環・Z代数の貼合せは本稿で直接証明し、新規性は未確認である。

Van den Bergh, *Non-commutative P¹-bundles over commutative schemes*, Trans. AMS 364 (2012), 6279–6313、arXiv:math/0102005v3 のTheorem 1.2（Noetherian性）、Lemma 4.1.7（双対）、§5（twist）、Theorem 7.1.2（二次解消）、Lemma 8.1.1（ample sequenceの仮定）を一次本文で確認した。Nyman, *Serre finiteness and Serre vanishing for non-commutative P¹-bundles*, J. Algebra 278 (2004), 32–42 の著者公開本文Theorem 2.5/Corollary 3.3も確認した。Nymanの式は局所自由係数GについてR⁰τ=R¹τ=0、R²τ(G e_a A)_j=0 for j>a−2であり、左右のP¹を固定P¹へ同定しtwistして適用できる。本稿の反例では一般のeventual saturationに頼らず、二次解消から全整数の飽和を直接証明する。

## 相対曲線商と普遍Noetherian性

Van den Bergh arXiv:0807.3753v3 のLemma 5.2.4のlinear tensor標準形、Lemma 5.4.10–5.4.12のlinear/elliptic分離とadmissibility、Proposition 5.4.2とLemma 5.5.3のtame・切断次元、Theorem 5.5.6(1),(3)の核の正規族生成・regular性を一次本文で確認した。本稿では相対隣接行列のkernel線によりpoint-curveのshiftをscheme-theoreticに構成し、有限projective成分間の射のfiber判定で正規族を相対化する。fiberwise同型から非被約基底上の線束同型を推論しない。

正式な刊行訂正は Keeler, Corrigendum to “Ample filters of invertible sheaves”, J. Algebra 507 (2018), 592–598, DOI [10.1016/j.jalgebra.2018.03.024](https://doi.org/10.1016/j.jalgebra.2018.03.024) である。原著Lemma 3.3を訂正し、依存する定理を再検証したことを刊行ページの概要で確認した。全証明の独立再検証とは区別する。

Keeler, *Ample filters of invertible sheaves*, J. Algebra 259 (2003), 243–283、[arXiv:math/0108068v5](https://arxiv.org/abs/math/0108068)、Theorem 1.5と付属Erratum §2（Theorem E2.5）を一次本文で確認した。射影スキームが任意の可換Noetherian基底上にあり、Hがampleなら、固定coherent Fに対してH^q(F⊗H^m⊗N)=0が全nef線束Nに一様なmで成立する。誤りの訂正前のLemma 3.3を使うのではなく、Erratumによる同定理の再検証を含めた形を使う。本稿ではhelixのparity別成分次数からprefix/H^mがrelative nefとなることを確認し、row/column idealの像層安定とこの消滅を組み合わせる。一般のrelative linear/elliptic貼合せの包括的な新規性は未確認である。

## 効果的族からのsmooth atlas

DDLの刊行版§4.1では基底は体に限定されず、coherent可換環の冪零全射R→AとAの有限表示性を仮定している。従ってTheorem 5.13(1)–(4)は任意の局所Artin small extension A′→Aへ直接適用できる。持上げた例外対象のHomはflatで還元と可換し、指定した全Hom framesを延長することができる。指定されたpointed同型はdg Moritaとcanonical反Serre環を経て、既存の全忠実性で戻す。

Stacks [Tag 02HY](https://stacks.math.columbia.edu/tag/02HY), Lemma 37.12.2を一次本文で確認した。判定に使うSpec A′→Tのfinite type条件は、Tがfinite type kでA′がlocal Artinなら剰余体kのtestに帰着する理由を明記した。任意のH2族Tへの基底変更はambientのaffine有限表示対角により実際のschemeになる。[Tag 04X0](https://stacks.math.columbia.edu/tag/04X0), Lemma 94.17.2と[Tag 04TK](https://stacks.math.columbia.edu/tag/04TK), Theorem 94.17.3のsmooth groupoidの商定理も本文確認した。この判定はQのchartと一般quintupleのchartに適用され、全cubicのH2内部の開部分の代数性を与える。ambientの開部分との同一視や全H2代数性ではない。

## 確認した一次資料

| 文献キー | 確認箇所・版 | 本研究での使い方と制限 |
|---|---|---|
| `AZ1994` | 出版社書誌・abstract。原論文 Theorem 4.5 の全文は今回未取得 | AZ ampleness と再構成の原典。体上版は `MU2021` Definition 2.5 / Theorem 2.6、一般End-ring版は `OACU2026` Theorem 7.3の再録で照合する。 |
| `BauwensVanDenBergh1998` | 著者公開本文、Proposition 2.2・式(2.7)、Lemma 2.4、Proposition 2.7・式(2.11)、Proposition 3.2、Remark 3.3・式(3.1) | 体上の二次VeroneseのKoszul双対、正規functional、canonical normalizing extension。Artin係数・二周期Z-algebraへの相対化は主原稿 `sec:quadric-artin-hull` で直接証明する。 |
| `VdB2011` | arXiv:0807.3753v3, Proposition 5.1.2, Theorem 5.5.10, Corollary 5.6.2, Theorem 6.1, Proposition 6.6, Corollary 6.7, Theorem 7.1 | cubic regular $\mathbb Z$-algebra の分類、even part の graded 化、quadratic hull、translation principle。標数 $\ne2$ の代数閉体で ambient $D/(g)$ 表示が存在する。選んだ shift の平方が inverse Serre になること、および指定された $\mathcal O$ の保存は別途確認する。 |
| `Presotto2018` | [出版版](https://ems.press/content/serial-article-files/30740), §2.1 pp.737–738, Theorem 2.8 p.738, Appendix A pp.763–769; arXiv:1607.08383v1 | 全cubic AS正則Z-algebraはZ-domain。Sklyanin、整な曲線、被約曲線に限定されない。任意の二周期で次数付けしたeven partのdomain性に適用する。 |
| `SVdB2013` | 出版版 §§2.5–2.8, 5、式(2.2)–(2.3)、Theorem 5.6、Corollary 5.8、§§10.1–10.5、Theorem 10.2、p.854 | central quadricのsmoothness、Sklyanin pencilのdomain性、楕円base locus、fat pointの自己Euler特性2。一般Corollary 5.8のstandard性には次行の訂正を反映する。§10の幾何的左加群を反対環で右規約へ移す。 |
| `MU2021` | arXiv:1708.00167v4, Definition 2.5, Theorem 2.6, §5、Definition 5.4、Theorems 5.16–5.17、Appendix Example 6.1 | canonical twist と standard 条件、full geometric helix、non-standard presentation の例。§5 は標数0の代数閉体。non-standard algebra でも tails は standard presentation と同値になり得る。 |
| `MN2025` | 出版社書誌、arXiv:2307.15253v1, Theorem 4.8, Proposition 4.11(2), Theorem 4.19, Lemma 6.10, Theorems 6.12–6.13 | ASからASFは従うが、周期性だけからASF+を結論しない。cubic表示の対象上のSerre移動はASFのExt計算とfull exceptional collection、既存H2圏のSerre双対性から直接回復する。一般四周期比較はfull geometric helixからの定理を用いる。 |
| `Stacks0FZR` | Lemma 56.7.8、Tag0FZR | 有限型、source separated・target reducedのcoh圏同値を幾何学的に記述する。Fano仮定を使わず可換認識に適用。 |
| `EsnaultViehweg1992` | 著者公開全文、Theorem1.2と直後の標数0への拡張（本文p.4） | Kodaira消滅。M=−Kがampleとなった後にMとLに適用する。 |
| `BondalOrlov2001` | arXiv:alg-geom/9712029, Theorem 3.1 | ample canonical/anticanonical bundle を持つ滑らかな射影多様体の導来自己同値。coh(Q)のexact自己同値に適用し、shiftが零であることを確認する。 |
| `OU2014` | arXiv:1403.0713v1, §2、Theorem 1.1 | geometric-quintuple GIT moduli $\mathbb P(2,4,4,6)$、conifold-potential moduli $\mathbb P(1,2,3,4)$、次数4の有限射。これらを $\mathcal O$-marked moduli と同一視するには marking 忘却の追加議論が必要。出版情報は推測せず preprint として引用する。 |
| `BSW2010` | arXiv:0802.0162v3、§7の(7.1)–(7.2)、Proposition 7.1 | 通常の4次元Sklyanin環の自己双対bimodule分解と非捩れCY性。本文どおりk=Cで使い、退化・modified例へ外挿しない。 |
| `RRZ2014` | arXiv:1302.0437v2、Lemma 1.5 | noetherian connected graded AS-Gorenstein環とμ-normalな正則正規元zについて商のNakayama公式。Sklyaninではμ=idかつz中央なので適用できる。 |
| `LS1993` | 出版版§1.1、pp.38–39 | 通常のSklyanin関係と中央二次pencilの対角平方和による表示。反自己同型による左右規約の比較に使う。仮定τ∉E[4]は無限位数の場合に成立。 |
| `MUW2026` | arXiv:2606.24606v1 (2026-06-23)、Introduction、Definition3.1–3.3、Proposition3.5、Lemma3.20、Remark4.4、Theorems4.10,4.12,5.5,5.17 | Mori–Ueyama–Wuの三著者。normal cutのruling・twistのstandard性・中心Sklyaninのsmooth⇒standard。ambientにAuslander正則・Cohen–Macaulay(*)を追加要求。全O-marked H2分類ではない。normal→centralのgraded Morita還元はIntroductionで不明とされる。 |

MU2022 の arXiv v4（Definitions 4.10, 5.9、Lemmas 2.4, 4.13, 5.11, 5.13、Theorem 5.5）は正則正規切断を扱い、ambientの追加条件(*)を課さない。型14641は四次元quantum polynomial algebraの仮定を満たし、H2のdomain性から切断式はhigh rankとなる。主原稿の四周期比較はここから得る二つのMCM型にOrlovの分解とMN2025のhelix定理を適用する。[MU2022](https://arxiv.org/abs/1905.12266v4)・[Orlov](https://arxiv.org/abs/math/0503632)・[Mori–Ueyama 2016](https://arxiv.org/abs/1507.06377)

Van den Bergh 論文の上記定理番号は **arXiv v3** のもの。出版版では番号が異なるため、版を明記せず番号だけを引用しない。

## 平方根と Nakayama twist

`MU2021` §5（arXiv v4 の PDF pp.22–23）では、$B=S/(f)$ の tails において canonical bimodule は
$$
M\longmapsto M_\nu(-2)
$$
で作用する。したがって
$$
\mathbb S^{-1}[2](M)\simeq M_{\nu^{-1}}(2).
$$
通常の次数移動 $(1)$ を要求された平方根として用いるには、誘導された Nakayama twist の自然同型による自明性を確認する必要がある。特定の object に対する $M_\nu\simeq M$ は、関手全体の自明性を意味しない。

`MU2021` Appendix Example 6.1 の non-standard algebra は可換 smooth quadric の Zhang twist である。従って standard/non-standard という一つの graded presentation の挙動を、そのまま $(\mathcal C,\mathcal O)$ の不変量として用いない。

この点は`MUW2026` Theorem4.12でruling保存／交換の必要十分条件として精密化されている。Zhang同値はregular moduleとそのtails像を保存するため、O-marked pairでもstandard性は不変でない。本稿の四根では3型対1型となる。同論文Theorem5.5の幾何型Sklyaninに対するsmooth⇒standardにより、本稿の楕円型例は`MN2025` Theorem6.13の比較に入る。指定O・平方根の具体的対応は prop:standard-pointed。Theorem 6.13 の結論は次元3・Gorenstein parameter 4であり、cubicの一次生成性には別の証明が必要である。

## Ore extension による ambient の検証

直接使える一次資料は `LV2026` **Proposition 2.2**。代数閉体上、多項式環の graded automorphism twist $R$ に対し、$\sigma$ が graded automorphism、$\delta$ が degree-one left $\sigma$-derivation、$\deg y=1$ なら、$R[y;\sigma,\delta]$ は noetherian AS-regular / Auslander-regular domain、Koszul、Cohen–Macaulay であり、$R$ が $n$ 変数なら global dimension $n+1$、Hilbert series $(1-t)^{-n-1}$ を持つ。

古い一般的な補助出典は `LWW2014` **Theorem 3.3**：automorphism 型 Ore extension は twisted Calabi–Yau dimension を1増やす。これだけを引用して noetherianity や Koszul 性まで同時に主張しない。

本研究の具体的な族への適用と正則正規元の計算は、主原稿の `prop:ore-ambient-family` に証明がある。ここでは同じ証明を複製しない。対象は quotient map を固定した被覆であり、unframed ambient の全同型分類は主張していない。

## 全分類に用いた既知入力と直接証明

VdBの許容四つ組の必要十分条件（arXiv v3 Proposition5.1.2）とcubic AS正則Z-algebraの分類（Theorem5.5.10）は既知入力である。本文ではD1–D3として条件を列挙し、L0,L1,L2の隣接二束の閉埋込み、多重次数、L0≠L2を要求する。曲線の整性・被約性は要求しない。

全許容四つ組のeven partのdomain性はPresottoのTheorem2.8を直接適用する。二周期の存在はVdB Proposition5.6.1によるが、その平方が反Serreとなることは別に必要である。本稿は四次テンソルの回転と双対化双加群を直接比較し、全退化型のPic・貼合せ・切断基底から適合周期を構成する。AS→ASFだけをASF+へ読み替える引用を避け、局所コホモロジーの双加群構造を示す。MNのTheorem4.8、Proposition4.11(2)、Lemma5.12、Theorem6.8をそれぞれAS双対性、Ext、ampleness、Serreに使う。共通の全公理への還元は `prop:admissible-period-h2` に置く。

cubicから全H2への比較、最初の軌道対象の認識、階数三支持の同時untwist、全noncubic分類、全境界での適合周期、根を忘れる有限同値判定には本文に直接証明がある。これらの組合せが既存のどの主張と重なるかは包括的調査未了であり、新規性確定・公表済み成果とは呼ばない。今回の独立点検は引用の仮定・版・左右規約と本文の推論を対象とし、外部論文全体の証明を再証明したものではない。

## スタックと変形の一次資料

| 文献 | 確認箇所 | 利用範囲と未適用部分 |
| --- | --- | --- |
| `AOU2014` | [arXiv:1411.7770v1](https://arxiv.org/abs/1411.7770v1), Definition 3.5, Proposition 3.6 | 非巡回箙の固定次元関係式はGrassmannian内のideal条件と道代数自己同型群による有限型代数スタック。群は一般に矢への高次path追加も含む。全H2のheart・根忘却を自動的には扱わない。 |
| `OU2014` | Equations (1.7), (2.19)、geometric quintupleの定義、Theorem 1.1 | projective四重2次元tensorの表示stackとそのGIT商を区別する。連続scalar慣性を除いても有限慣性は残り、coarse GIT商との同一視ではない。 |
| `MOU2019` | [arXiv:1903.06457v1](https://arxiv.org/abs/1903.06457v1), §6.1–6.2、Theorem 6.3 | 曲線と3束の相対stack、束のscalar rigidification、smooth-support bimoduleとの比較。主たる関係式stackとの比較はbirationalであり、全非被約境界を含む内在的H2との同値ではない。 |
| `TV2007` | [arXiv:math/0503269v5](https://arxiv.org/abs/math/0503269v5)、[April 2007著者本文](https://www.math.univ-toulouse.fr/~btoen/ttt.pdf)、Theorem 3.6、Corollaries 3.15, 3.17, 3.22, 3.24、Lemma 3.25（著者本文pp.55–57） | perfect-object moduliと自己同値群の代数性。Corollary 3.24の条件(1)は一般基礎環でもHH負次数零・HH⁰=基礎環から局所有限表示の自己同値代数空間を与える。Corollary 3.22は単純対象のétale局所Gm-gerbe、Lemma 3.25は可逆性の開条件。主原稿のétale Morita根代数化に適用した。相対heart・AZや全H2の代数性は別途必要。 |
| `StacksSmoothAtlas` | [02HX](https://stacks.math.columbia.edu/tag/02HX), Lemma37.12.1；[057G](https://stacks.math.columbia.edu/tag/057G), Lemma37.38.5；02HY, 04X0, 04TK。2026-11-21に該当本文を確認 | 局所Noetherian基底上で有限型射の小拡大持上げ判定と、smooth射の指定された分離的閉fiber点を通るétale切片。HH²恒等から根空間のsmoothnessを示し、HH¹作用を仮定せず一つの根をétale代数化するために用いる。HH¹恒等は根空間自体のétale性・一意性に使う。 |
| `DeDekenLowen2011` | [出版版](https://ems.press/content/serial-article-files/30497), §4.1、Theorems 4.5, 5.13, 5.15 | Z-generating geometric helixのGrothendieck categoryのabelian変形とthread algebraの線形変形の比較。coherent ringの冪零拡大に対する定理で、H2の平方根・AS被覆条件の相対開性は含まない。 |
| `Toda2009`、`Lowen2008` | [Toda arXiv v3](https://arxiv.org/abs/math/0502571v3), Proposition 5.6、Lemma 5.8、Theorem 4.7；[Lowen arXiv v1](https://arxiv.org/abs/0707.2602v1), Theorems 1.1, 4.8、Corollary 4.9；Toda §§3–4 の変形圏の構成 | FM核の左右HH作用と持上げ障害を比較し、同一変形への持上げにΦ_*(u)=uが必要。Todaの定理自体は変形間のliftの十分条件であり、必要条件にはLowenの障害同定を使う。可換quadricの特定Serre根の非持上げ例に適用。 |
| `Alper2009` | [arXiv:0804.2242v3](https://arxiv.org/abs/0804.2242v3), Example 8.3、Theorems 13.2, 6.6 | affine/linearly reductive商のgood moduli spaceと、locally noetherianの場合の代数空間への普遍性。noncubic表示のχ商に適用。§2のquasi-separated規約を超える任意の代数空間へのcoarse space不存在は本文の直接証明による。 |
| `StacksModuli` | [0DLS](https://stacks.math.columbia.edu/tag/0DLS)、[06PD](https://stacks.math.columbia.edu/tag/06PD)、[04V2](https://stacks.math.columbia.edu/tag/04V2)、[04XL](https://stacks.math.columbia.edu/tag/04XL)、[0DR5](https://stacks.math.columbia.edu/tag/0DR5) | 商の代数性・滑らかさ、商stack間のgerbe判定、慣性のrigidification、stackの位相とsmooth表示からの成分認識。平方根やambientという対象の選択を忘れる操作は、単に慣性の部分群を除く操作とは限らない。 |

本文のA64 foundation chart、全Artin局所変形の表示、HH消滅、geometric cubic開部分、ruling二択と二短完全列による相対S2交換、全H2の幾何点群oidの全充満な実現、noncubic慣性とχ商、九生成のdegree gerbeの中立化は、これらを踏まえた明示構成である。cubic非空開の稠密性から実現点集合の誘導位相での既約性が従い、任意noncubic点への一次元特殊化は二写像の線形補間で構成する。相対smoothproper性は有向代数の有限長相対bar分解で直接示す。内在的相対fppf stackの再構成・全忠実性・対角の有限表示性はrelative_moduli節で証明した。実現部分層の有限型代数性と内在的位相は `h2_smooth_atlas.tex` で証明した。全foundation商との相対groupoid比較は別の課題である。既知文献との包括的な新規性比較は未完了。

## 八・十・十二本矢と avatar の資料

2026-11-21に原資料の該当箇所を確認。別稿の証明は現行ソースに保持し、旧PDFの取得を再開の前提としない。未公刊資料にある全AS分類の独立検証と新規性の確認は未完了である。

| 引用キー・資料 | 確認箇所と適用範囲 |
| --- | --- |
| `DWZ2008`、Derksen–Weyman–Zelevinsky, *Quivers with potentials and their representations I: Mutations*, Selecta Math. 14 (2008), 59–119, DOI 10.1007/s00029-008-0057-9、[arXiv:0704.0649](https://arxiv.org/abs/0704.0649) | Theorem4.6のsplitting、§5のmutation。一般定理は完備道代数。別稿のweight4の場合は三角変換を直接書き、有限道代数・任意基底で証明する。 |
| `AOU2014`、[arXiv:1411.7770v1](https://arxiv.org/abs/1411.7770v1) | Definitions3.5,4.1・Propositions3.6,4.2。relationsの有限型stackとgroupoidの区別。別稿は四頂点の全Homと結合律を固定する明示モデル。 |
| `AvatarVSeven2026`、大川新之介・植田一石、`quadric_avatar_classification_parts_I_II_ja_20260916_v7.pdf`、114頁 | §38 product有限箙8矢4関係、Theorem39.1のmutation後16−2r矢、Proposition40.3のSchur補元、Theorem51.4/Corollary51.5の全square/非最小10本矢、Proposition52.3の残存scalar、Theorem53.2の仮定付き相対対応。 |
| `Q12Avatar2026`、`q12_avatar_ja_20261014_v1.pdf`、24頁、著者記載なしの未公刊研究資料 | Definition15.2・Theorem15.3の体上AS同型類分類。Remark11.3のCl0/Cl2、Proposition14.1の最深境界の安定性障害。相対stack同値として引用しない。 |
| `Q12Weyl2026`、`q12_weyl_extension_ja_20261014_v1.pdf`、22頁、著者記載なしの未公刊研究資料 | Definition4.1、Lemma5.1、Propositions5.2–5.3、Theorem5.4。$p_*(HP^n)$ による幾何的twist。別稿は非被約因子・垂直成分・相対降下を含めて証明を記す。 |
| `Synthesis2026`、`quadric_synthesis_ja_20261017_v1.pdf`、79頁、未公刊研究資料 | 印刷頁51–54（PDF55–58）、68–69（PDF72–73）。§7.11–7.12の統一avatar、§9の相対操作、§13.3の相対AS/avatar認識・最深Hilbert問題・自己同型/降下の未解決性。 |

square辞書 $H=F_sG_sP^{-1}$ とrotated square $H_r=F_sG_sP$ を区別する。$P=\mathcal O_D$ の古典同型類への特殊化を、Picard零切断のstack上の収縮として扱わない。finite foundation、raw QP、graded algebra、pointed heartはそれぞれ異なる同型と慣性を持つ。

## 公表前と後続の比較課題

1. 全noncubic帰着・全境界の適合周期・有限pointed同値判定の先行研究上の位置を一次資料で精査する。
2. cubic側の有限判定を曲線と束の幾何的変換へ簡約し、既存tensor/quintuple分類との重複を記述する。
3. `OU2014` の次数4射とroot忘却の関係を検証する。可換点の四根だけから一致・有限性を断定しない。
4. 自己同値群、全根・全ambient、相対moduliを扱う場合は、同値類分類とは別に自然同型・降下・底変更を検証する。

## Kitamura–Okawa の cubic Z-algebra 復元報告と忘却

Shinnosuke Okawa (joint work with Takuya Kitamura), “The reconstruction theorem for AS-regular 3-dimensional cubic Z-algebras”, *Oberwolfach Reports* 23/2022, pp. 1271–1273（ワークショップ報告）, DOI [10.4171/OWR/2022/23](https://doi.org/10.4171/OWR/2022/23), [公開PDF](https://oa.tib.eu/renate/server/api/core/bitstreams/c28e6d94-6858-4684-b0bf-be60f80b7e20/content)。当該報告のTheorem 1は同じqgrを持つ三次元cubic AS-regular Z-algebraの同型類が\(D_\infty\)軌道となること、Theorem 3はrank-one torsion-freeかつ\(\chi(L,L)=1\) のline bundlesが \(\mathcal O(a,b)\), \(\mathbb Z^2\) に尽きること、Hom非零による積順序を述べる。論文は当時のReferences [4]で *in preparation* と記される。今回報告本文は確認したが、詳細証明・その後の刊行状況の完全な追跡は未確認。従って本repoの定理の証明入力には昇格せず、条件付き還元と独立課題の出典としてのみ使う。主原稿ではδ≠0・η∉Zδの滑らかな楕円型に対し、VdB復元・内在二foundation・評価列・数値剛性から全Z²標識の強いH2所属と忘却同値式を独立に証明し、今回独立読取りと組版を行った。この制限範囲を越える全cubicの強いH2標識分類や、自己同値群全体の記述はなお別問題である。

## 一次資料へのリンク

- `AZ1994`: <https://doi.org/10.1006/aima.1994.1087>
- `BauwensVanDenBergh1998`: <https://doi.org/10.1006/jabr.1997.7210>, <https://cantate.be/site/kristien.ps>
- `VdB2011`: <https://arxiv.org/abs/0807.3753v3>, <https://doi.org/10.1093/imrn/rnq234>
- `SVdB2013`: <https://ems.press/journals/jncg/articles/4781>, <https://arxiv.org/abs/1108.1552>
- `MU2021`: <https://arxiv.org/abs/1708.00167v4>, <https://doi.org/10.4171/JNCG/403>
- `MN2025`: <https://arxiv.org/abs/2307.15253v1>, <https://doi.org/10.1007/s10485-025-09806-2>
- `OU2014`: <https://arxiv.org/abs/1403.0713v1>
- `LV2026`: <https://link.springer.com/article/10.1007/s13366-026-00867-5>
- `LWW2014`: <https://doi.org/10.4171/JNCG/165>, <https://arxiv.org/abs/1205.0893>

- `BondalOrlov2001`: <https://arxiv.org/abs/alg-geom/9712029>, DOI 10.1023/A:1002470302976

- `Stacks0FZR`: <https://stacks.math.columbia.edu/tag/0FZR>
- `EsnaultViehweg1992`: <https://page.mi.fu-berlin.de/esnault/books/esvibuch.pdf>
- `BSW2010`: <https://arxiv.org/abs/0802.0162v3>, <https://doi.org/10.1016/j.jpaa.2009.07.013>。出版書誌確認：<https://eprints.gla.ac.uk/130850/>。
- `RRZ2014`: <https://arxiv.org/abs/1302.0437v2>, <https://doi.org/10.1016/j.aim.2014.07.010>
- `LS1993`: <https://www.numdam.org/article/BSMF_1993__121_1_35_0.pdf>, <https://doi.org/10.24033/bsmf.2200>
- `MUW2026`: <https://arxiv.org/abs/2606.24606v1>, <https://arxiv.org/html/2606.24606v1>


## 楕円型の全標識と忘却ファイバー

Okawa–KitamuraのOWR2022, pp.1271–1273（doi:10.4171/OWR/2022/23）を一次PDFで再確認。Theorem 1はD∞軌道による全cubicのqgr同値判定、Theorem 3は全line bundleのZ²表示を明記し、二つのmutationによるzigzag構成も記す。詳細稿は同報告当時in preparation。従って格子分類・二面体作用自体を本研究の新成果としない。現行 `thm:elliptic-marking-lattice-fiber` はη∉Zδの範囲で数値一意性と評価列から独立に証明し、楕円自己同型を含むO-marked忘却の必要十分条件と捩れ時の有限濃度を明記する。この精密化の包括的新規性は未確認。

## 有限型効果性と全モジュライの入力

2026-11-22にVdB2011のarXiv:0807.3753v3を再確認した。Definition 5.3.1は四つの隣接縮約の非消滅、Lemma 5.4.12とTheorem 5.5.10はgeometric quintupleから許容四つ組・cubic AS正則Z代数への対応を与える。候補foundationのH2所属・domain性を先に仮定しない。本稿では有限LG条件からこの入力を確認し、既存の逆構成でH2を得る。

Polishchuk–Positselski, *Quadratic Algebras*, Chapter 6, Theorem 2.1 / Corollary 2.2と§6は、有限段階のKoszul条件の開性と、Koszul locus全体の可算交叉・非constructible例を区別する。本稿は一般開性を用いず、同じ基底の全幾何fiberを認識してからChapter 6, Theorem 7.3を局所的に用いる。参照本文は [書籍テキスト](https://djvu.online/file/T1DOlccPNeqX0)、正確な書誌は既存項目PolishchukPositselski2005。

framed実現空間のスキーム性には [Stacks Tag 05W6](https://stacks.math.columbia.edu/tag/05W6), Lemma 76.14.8 と [Tag 03XX](https://stacks.math.columbia.edu/tag/03XX), Proposition 67.50.2の本文と証明を確認した。有限型monomorphismはrepresentable・separated・unramified・quasi-finiteであり、スキームをtargetとするためsourceもスキームとなる。開immersionとは結論しない。

被約noncubic境界については、Stacks Tags [0509](https://stacks.math.columbia.edu/tag/0509)、[050B](https://stacks.math.columbia.edu/tag/050B)、[034E](https://stacks.math.columbia.edu/tag/034E)、[0694](https://stacks.math.columbia.edu/tag/0694)、[063L](https://stacks.math.columbia.edu/tag/063L) の本文を2026-11-22に確認した。被約閉部分の存在と因数分解、smooth topologyでのreducedness、Koszul-regular immersionのfpqc降下、Noetherian表示上の通常のregular immersionとの一致を使う。これらの一般定理と、本稿の二射影行列式の横断性・normal formの証明を区別する。

## 内在的境界の相対比較と粗モジュライ障害

Stacksの一次本文で[0BF6](https://stacks.math.columbia.edu/tag/0BF6) Lemma39.8.2（Cartier）、[02G3](https://stacks.math.columbia.edu/tag/02G3) Lemma29.36.2（微分零によるunramified）、[024T](https://stacks.math.columbia.edu/tag/024T) Proposition41.6.1（unramified射の切断）、[04YY](https://stacks.math.columbia.edu/tag/04YY) Lemma101.6.2（相対慣性によるrepresentability）、[025G](https://stacks.math.columbia.edu/tag/025G)、[0DUD](https://stacks.math.columbia.edu/tag/0DUD) Lemma101.45.7（étale・慣性・幾何groupoidによる同型判定）を2026-11-22に確認した。一般判定は既知入力であり、実際の境界chartの族を二形式模型へ比較する相対tilting・反Serre再構成が本文の追加部分である。

Stacks Project [Tag 0DUP](https://stacks.math.columbia.edu/tag/0DUP) Lemma106.13.4 と [Tag 0DUR](https://stacks.math.columbia.edu/tag/0DUR) Lemma106.13.6 を2026-11-22に一次確認。前者はwell-nigh affine stackのcategorical moduliをaffine schemeの範囲で、後者は任意の代数空間への普遍性へ拡張する。一般のuniform categorical moduliの基底変更は平坦基底変更を意味し、任意の基底変更との整合性まで両Tagだけから主張しない。論文BのDM開では、任意基底Aで有限商の局所モデル Spec A[x]/(x²−s) を再構成し、μ₂の不変式環がAとなることを直接確認して任意基底変更に対する粗空間の普遍性を証明する。

Alper [arXiv:0804.2242v3](https://arxiv.org/pdf/0804.2242v3) のTheorem13.2（affine reductive quotientのgood moduli）、Theorem6.6（代数空間への普遍性）を再確認した。§2の規約はquasi-separatedである。任意の代数空間に対する全H2の粗モジュライ不存在は、この規約を広げず、穿孔直線上でfppf局所定値な族とétale scheme chartを使う本文の直接証明による。χの特殊fiber・全慣性・連結慣性表現の包括的新規性は未確認である。

## DM粗空間と一致点の形式局所商

Stacks [Tag 0DUP](https://stacks.math.columbia.edu/tag/0DUP), Lemma 106.13.4 と [Tag 0DUR](https://stacks.math.columbia.edu/tag/0DUR), Lemma 106.13.6 の本文・証明を2026-11-22に確認した。有限 affine atlas を持つ商の不変式環が、任意の代数空間に対して categorical となることを使う。DM開の証明では [A¹/μ2] のchartを反射とgerbeに沿って貼り合わせ、任意の基底変更後も A[x]/(x²-s) の不変式環がAとなることを確認する。各点の有限慣性だけからKeel–Moriの仮定を結論せず、実際の慣性射がproperでないことを別に証明した。非affine開P°のHartogsによる判定と、Alper `Alper2009` Propositions 3.3, 3.9のcohomological affinenessの合成・Serre判定を用い、χ_DMがgood moduliでないことを示す。

Jarod Alper–Jack Hall–David Rydh, *A Luna étale slice theorem for algebraic stacks*, *Annals of Mathematics* **191** (2020), 675–738, [DOI](https://doi.org/10.4007/annals.2020.191.3.1), [出版社PDF](https://annals.math.princeton.edu/wp-content/uploads/annals-v191-n3-p01-s.pdf), Theorems 1.1, 1.2（特にp.676）を2026-11-22に一次確認した。有限型smoothスタックの閉点、affine対角、線型簡約な安定化群という仮定を本稿の一致点で確認する。Theorem 1.2は接表現商との共通étale近傍を与え、affine対角の下で元のスタックへの射をaffineに取れる。原稿では全HH作用を実際のruling mutationと全Grassmann接空間から計算し、smooth境界のイデアルから同変正則パラメータを選んで対の形式線型化を得る。不変式環k[ac,(x+y)²,(x-y)²]は直接計算する。共通étale近傍のgood moduli spaceがsmooth三次元であることと、H2のZariski開や全体へのgood moduli spaceの降下を区別し、後者は未解決とする。これらの具体的な表現・境界への適用について包括的新規性は未確認である。
