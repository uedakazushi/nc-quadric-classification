# 現行研究ノート：O-marked 非可換 quadric

2026-11-21 / v0.37（主論文v1.37、別稿v0.1）。最初に [研究方針](../00_research_plan.md) を読む。証明の正本は [主原稿](../papers/nc-quadric-classification.tex)、文献確認の正本は [文献比較](literature.md)。本書は作業履歴ではなく、現在有効な知識と再開点を記す。

## 定義と規約

対象は `(C,O)`。`s`とAS4被覆を同時に存在させる。Gabriel–Krullの`C₀`は有限長、`C₁`は`C/C₀`で有限長になる対象の逆像。`qO`が非零単純かつ`Hom(C₁,O)=0`をrank-one torsion-freeと呼ぶ。`GKdim=1`の意味ではない。

右加群を採用し、`B_n=Hom(O,sⁿO)`、`a*b=s^{deg b}(a)∘b`。`Γ_*(M)`の右作用も同じ順序。cubic repoの表示された積と反対なので、外部のNakayama・正規化自己同型の公式を直接コピーしない。

強いH2条件は `B ≅ A/(g)`、`A`は型14641、`g∈A₂`は正則正規。`g`の代表のスカラーは区別せず、最終対象ではambient自体を忘れる。`s²≅S⁻¹[2]`の同型は指定しない。根同型をrigidifyしたmoduliやtrace coherenceは別問題である。

## 八・十・十二本矢、avatar、内在的忘却

証明の正本は別稿 `papers/quiver-avatar-moduli.tex`。有限foundationの生成矢、relation completion、potentialの非最小表示を区別する。有限foundationではHom次元を $(2,2,2,4,4,6)$ に固定し、積 $a,b,c,d$ の唯一の結合律 $c(1\otimes a)=d(b\otimes1)$ を課す。二つの核に分解可能テンソルを許さず、$(c,d)$ の**合併した写像**の全射性を要求する。個々の $c,d$ の全射を要求する必要はない。$\delta_a,\delta_b\in\{0,1\}$ により生成矢 $6+\delta_a+\delta_b$、関係 $2+\delta_a+\delta_b$、完成矢 $8+2(\delta_a+\delta_b)$ を得る。$b$ 可逆と $a$ 可逆が二つの10本矢open、交わりが8本矢open。最小10本・12本の層をこれらのopenと同一視しない。

product relation QPの一頂点premutationでは4本を追加して16本となり、4×4 mass行列の階数r組を消去して16−2r本を得る。三次minor上ではSchur補元 λ=d−eD⁻¹b が残る係数。別稿 `prop:qa-square-mutation-count` と `prop:qa-square-relative-schur` に有限三角変換の直接証明がある。

weighted QPの二つのmass係数 $\lambda,\mu$ が可逆なら対角pairを消去できる。非被約基底では非零というだけでは不足する。生のright-equivalence商では各pairの $\mathbb G_m$ 自己同型が残るため、代数の同型とQPスタック同値を分ける。有限foundationの頂点scalar剛体化とも別操作である。

曲線型avatarは $D\in|2h|$、fiberwise非自明な $P\in\operatorname{Pic}^0(D)$。直像 $p_*(HP^n)$ と評価で再埋め込みし、幾何的並進 $\mathsf T$ を得る。$\Sigma_0$ 部分 $\mathcal U$ と $\mathsf T^{-1}\mathcal U$ が二つの10本矢open、交わりが8本矢open。最深閉locusは $\Sigma_2$ の負断面 $S$ を含む因子。$S$ を避ける $\Sigma_2$ は10本矢境界である。全square曲線型から奇数側10本矢chartへの辞書は $F=F_s, H=F_sG_sP^{-1}$。rotated squareの $H_r=F_sG_sP$ とは逆の壁を持つ。

$P=\mathcal O_D$ の零切断は本稿の曲線型openに含めない。有限代数の同型類では古典型Cl0/Cl2へ落ちるという既存入力があるが、自己同型・降下を含む収縮は未構成。Cl2はweighted projective stack $\mathbb P(1,1,2)$ であり、$\operatorname{coh}\Sigma_2$ と同一視しない。

相対heart・Serre・豊富なexact平方根・同じ根の全軌道環のAS4被覆を確認した部分から $\mathfrak H_2$ への忘却がある。この部分を定義するだけで開性が証明されたとはしない。weighted projective stackのsign skyscraperは全ての $\mathcal O(-4n)$ から不可視であり、H2で必要な反SerreのAZ豊富性に反する。Sigma2の負断面上の $\mathcal O_S(-1)$ も同様。一方、主論文のnormal helixにより、全H2幾何点は上記の10本矢openにfoundationを持つ。これを任意の相対H2族のlifting定理へ読み替えない。

幾何的再埋め込み・有限線形代数は別稿に直接証明を置いた。全AS分類との辞書は `Q12Avatar2026` 定理15.3等の体上結果を入力とし、未公刊資料の全証明を今回監査済みとは扱わない。具体的な出典・版・節は文献ノートに保持する。

## 相対平坦性の確立した認識

`papers/sections/relative_koszul.tex` に証明を置く。全H2の適合切断環BはKoszul AS4環の正則正規二次商なのでKoszul、反Serre環R=B^(2)もKoszulである。PP2005 Chapter 6 Theorem 7.3は任意のNoetherian局所環に適用できる。三次まで平坦で全幾何fiberがKoszulなら、全次数局所自由性と任意底変更に整合する左右Koszul解消を得る。このため、H2点を中心とする任意のArtin基底上のX3変形と、既存の横断二次jetは全次数平坦である。同節ではさらにArtin基底でnoetherian性を持ち上げ、qgrがflatなpointed Abel変形になることを証明した。canonical反SerreのArtin再構成とAbel変形の無障害性は次節で扱う。適合平方根・AS被覆の存在は別条件である。

## 内在的相対定義と認識

**cubic領域全体のsmooth Artin開部分。** `thm:cubic-smooth-open` は、全幾何fiberがcubicとなる内在的部分スタックV_cub⊂H2が、有限型で滑らかな純次元3のArtin開部分であると示す。非線形の普遍quintuple上では相対Picard群の[−2]に沿うétale被覆で適合根を構成し、linear点は可換Qのchartで覆う。各chartの全閉点で、指定されたpointed同型を保つArtin持上げを証明する。relation schemeはU×_[X3/PGL9]Uであり、選んだ根やfoundationを保存しない同値も含む。`cor:cubic-formal-h2-abelian` により全cubic点で形式H2変形とpointed Abel変形は同値で、HH≥3=0、dim HH²−dim HH¹=3となる。noncubic境界を含む全H2の代数性と、ambient内での開性は未証明である。

**相対Picard根と全cubic族の認識。** `thm:relative-compatible-root` は非線形のsmooth reduced普遍quintuple基底上で、N=L₂L₀⁻¹の二等分とATVの相対作用から実際の二周期βを構成する。β²はcanonical四周期θにvertex scalarを除いて一致する。同じβに対応するperfect双加群のSerre比較を、有限表示局所閉の比較空間と普遍基底の被約性で証明し、その後に任意の非被約底へ引き戻す。任意の根を最初から変形可能とは仮定しない。`thm:geometric-cubic-relative-effectivity` が普遍Noetherian性・canonical tails・同じ根のAS4被覆から全相対公理を供給する。DDLで五つのhelix対象を持ち上げ、四つの矢空間と四次syzygy直線を回復することで、指定同型を保つquintuple chartのArtin持上げが得られる。

**明示noncubic表示族の全相対認識。** `thm:noncubic-relative-effectivity` は二つの非退化二元二次形式の表示スタックNpres=[P/G]から、実際のH2族を構成する。中央Clifford表示を重み付き射影スタックX=P_R(1,1,2)上の有限局所自由代数へ移す。G=⊕_{i=0}³B~(i)はtiltingではなくcompact generatorであり、そのdg Endとweighted Čechからproper性・任意導来基底変更を得る。中心有限代数上のR-flat加群のfiber-perfect持上げを用いて対角のperfect性を証明し、canonical compactのsmoothnessを確認する。traceによる同じ根のSerre平方、AZ・全軌道、Ore/PBWによる普遍Noetherianな相対AS4被覆を合わせ、全相対公理を満たす。Npresは次元1であり、noncubic点の全横断変形を覆うatlasや相対全忠実性は結論しない。

**全noncubic点の良い根と有限型代数化。** `thm:noncubic-hh-trivial-root` は、根対を交換するtrace零対合から選ぶ適合Serre根が、全foundation変形のHH¹・HH²へ恒等に作用することを証明する。四平面Gr(4,8)の交代Gale双対として根の作用を計算し、接の正負次元(10,6)と有効基底変更Lieの(7,6)を比較する。根対非一致ではHH¹=0・HH²=3、一致ではHH¹=1・HH²=4で、いずれも負のHH部分は零となる。従って全Artin Abel変形へ根が延び、そのMorita類は一意である。`prop:hh2-etale-morita-root` と `cor:noncubic-etale-morita-root` により、全noncubic点の有限型étale近傍上で実際の可逆双加群・Serre平方同型・二項窓の比較を構成できる。これは同じ根のAS4被覆や相対heartの横断認識とは別の結果である。

**残る核心はnoncubic境界の横断効果性である。** 全cubic領域と明示noncubic表示族は相対H2として認識でき、全noncubic点の良い根も全Artin・有限型étale近傍へ延長できた。次は同じ根の全軌道に対するAS4被覆の高次持上げと、有限型近傍上の一様なcanonical tails・Noetherian性・AZを証明する。三有理配置での正規線の一次持上げは、高次の存在証明へ外挿しない。閉noncubic部分と開cubic部分で実際の代数族が得られれば、形式的Noetherian貼合せを適用する。全H2の代数性、X_as全体の表現可能性、内在位相とfoundation表示の位相比較は未解決である。

**Artinのfoundationと偏極忘却。** `artin_foundation.tex` で、全H2のnormal geometric helixにDe Deken–Lowenを適用し、全flat pointed Abel変形にrank24のcompact tilting foundationを持ち上げた。閉fiberでheart-exactなMorita同値は、m-adic有限フィルターの各商が閉fiber圏に属することから全変形heartでexactとなる。canonical反SerreはAZ ampleで全軌道環を再構成し、Artin X3からAbel圏への忘却に右逆を与える。一般の提示環から全軌道環への自然射も、各次数が自由で特殊化が同型なので同型である。

接空間は標準的な分裂完全列0→HH¹(Λ)→T[X3/PGL9]→HH²(Λ)→0を持つ。HH³(Λ)=0からpointed Abel変形は無障害。noncubic三基準点でAbel接は3/3/4、偏極付き接は3/3/5であり、一致根対の核は既存の非零Zhang方向。HH¹(Λ)=0ならm^r/m^(r+1)ごとの先頭導分を内部導分で消せるので、任意Artin X3変形のshiftはcanonical反Serreと同型である。これは異なる二根対の全noncubic点（一根共有を含む）に適用できる。小拡大でAbel変形と次数一の枠を持ち上げることで、X3はこれらの点で滑らか、次元83となり、そのPGL9商は滑らかで次元3である。内在的H2の滑らかさ・開性は未結論。四つのfoundation対象の像は例外性により一意に持ち上がるため、それだけでは偏極を区別できず、射への作用のintertwiningが必要である。

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

**残る一様化。** 一つの有限型開U°全体のBの左右Noetherian性が残る。これが成立する基底ではχ/AZ・Hom・canonical compact/Serre・内在相対条件を改めて未解決扱いしない。幾何的曲線商・正規拡大の相対構成を次に調べる。有限foundationの存在だけでheartのNoetherian性は結論せず、別の幾何模型の豊富列と必要なorbitを区別する。

**Gabriel商の生成条件。** `lem:qgr-module-object-basechange` ではBが次数一生成かつB₁有限であることを要求する。この条件なしでは次数torsionは拡大に閉じない。例えばB=k[x₁,x₂,…]、全deg xᵢ=1、I=(xᵢxⱼ:i≠j)+(xᵢ^{i+1})としE=B/I、T=B₊Eと置く。TとE/T=kはtorsionだが、1∈Eは任意に高いxᵢ冪で殺されずEはtorsionでない。現行quadricのBは有限rankのB₁で生成されるため、全ての基底変更後にも必要条件を満たす。

`papers/sections/relative_moduli.tex` が定義・証明の正本である。基底は標数零の代数閉体上の局所有限型scheme。相対族はnoetherian Abel圏の系とOからなり、module-objectによる基底変更、Hom有限性とflat基底変更、fppf descentを指定する。各幾何fiberには元の体上H2条件を課し、fiberの全Db上のSerre条件を明示する。これに加え、局所canonical compact圏のsmooth proper性・導来基底変更・Serreを、fppf chartの全affine基底変更上で要求する。sとAS被覆は局所存在条件であり追加標識でない。`prop:relative-h2-field-recovery` は元の体上groupoidを回復する。

相対AZ再構成、自然自己同型Aut(Id)=A×、pointed二自己同型の消滅から、反Serre関係の射 Φ:H2→[X3/PGL9] は全忠実となる。対角はaffine有限表示であり、framed部分層X_asを用いたH2≃[X_as/PGL9]はfppf stackとして成立する。**未証明なのはX_asの有限型代数空間による表現可能性**である。有限型siteだけで定義した関手を、極限保存を示さずに任意scheme上の関手として扱わない。

正規化に用いるL=(det R1)^−11(det R2)^2について、Rnorm_n=R_n⊗L^−nのshiftは元のt⊗L^−1に対応する。従って普遍正規化環へ大域的に(1)=S^−1[2]を課すのは誤りであり、基底線束twistを許すかfppf局所で比較する。

**大域導来比較の候補（未証明・現行定理の入力ではない）。** heartのdescentだけからcanonicalな非有界導来圏のdescentを推論しない。flatなA→Bについて、まずD(G_B)とD(G)内のB-module対象との比較を、exact induction/forgetful随伴とBarr–Beckで証明する必要がある。その後の線形安定圏のdescentには、A. Mathew, *The Galois group of a stable homotopy theory*, Advances in Mathematics 291 (2016), 403–541, [DOI:10.1016/j.aim.2015.12.017](https://doi.org/10.1016/j.aim.2015.12.017) のCorollary 3.33（有限表示faithfully flat射のdescendability）、Corollary 3.42、Proposition 3.45が候補となる。compact生成・bounded coherent部分との比較は別に確認する。局所compact条件による現行定義は、この未完成の比較を必要としない。

**Noetherian 性の形式的貼合せ。** 可換Noetherian基底R、各次数成分が有限な中央次数環A、I=(f₁,…,fᵣ)に対し、A/IAと全A[fᵢ⁻¹]が左右NoetherianならAも左右Noetherianとなる。次数ごとのI進完備化で有限生成元の係数を収束させ、R̂_I×∏R[fᵢ⁻¹]の忠実平坦性で降下する。成分の平坦性・有限Krull次元は不要で、一般次数付き加群とZ代数のrow/columnにも成立する。証明 `thm:patch-noetherian`、`thm:patch-z-algebra`。幾何的cubic族では両部分の実際のNoetherian性を別に証明して適用する。

**非可換P¹束の対角列の障害。** 滑らかな(2,2)曲線と次数二線束から全隣接縮約が非零のgeometric quintupleを構成した。しかし対応する層対称代数の候補対角列Kₙ=π(O(n)⊗e₋ₙA)は、全ての行からHomが零になる非零coherent対象を持ち、AZ生成条件を満たさない。二次解消を用いて全整数でωπMの成分がO(−2)となることを直接証明した。これは当該模型・軌道列の比較への障害であり、本来のcubic環BのNoetherian性の反例ではない。`sec:ruled-diagonal-obstruction`。本来のBのNoetherian性は、曲線商・正規拡大とlinear部分の形式的貼合せによって解決した。

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

全次数平坦性とArtin qgrのflat Abel変形は解決したため、残る研究資源はcanonical反Serre偏極、平方根、被覆の局所存在に集中する。全次数Hilbert条件を重ねてこの偏極方向を切ろうとしても、族自体が全次数平坦なので解決しない。

## スタック構成の現状

証明の所在は `papers/sections/noncubic_stack.tex` と `papers/sections/foundation_stack.tex`。表示と相対内在的moduliの区別を維持する。

| 結果 | 確立した範囲 | 残る比較 |
| --- | --- | --- |
| noncubic `[P/G]` | smooth finite type Artin、dim1、全幾何点のpointed同値類と慣性。一般D8×C2、共有根D8、一致根対はGmを含む | 任意の内在的族の相対正規形 |
| 根配置への射 | 順序付き局所表示上μ2² gerbe。S2は二因子を交換 | μ2²は真の自己同値であり除かない |
| χによるgood moduli | 不変式環k[χ]。共有根と一致根対はχ=1。全表示stackのcoarse moduli algebraic spaceは存在しない | 全H2の相対stackのcoarse理論へは未外挿 |
| 表示族の局所AS被覆 | étale局所の交換対合、全次数有限自由、中央正則切断とZhang twist。任意底変更と整合 | 相対Serre双対性と任意内在族の認識 |
| foundation `F=[A64/(G/K)]`、K≅Gm³ | smooth finite type、dim3。全H2のfoundationが入る。HH≥3=0、dimHH²−dimHH¹=3 | 内在的H2実現部分の有限表示、相対Serre/AZ条件 |
| rulingとfoundationの二択 | rank-one TF exceptionalと反Serre Hilbert多項式で二rulingを内在認識。normal helixで作るfoundationが二つ | 任意の内在的族における相対存在・底変更・降下 |
| 相対ruling交換とQ_fnd | F0上の二短完全列交換がcoherentなS2作用。Q_fnd=[F0/S2]はsmooth finite type、dim3。F0→Q_fndはrepresentableな有限étale二重被覆 | 内在的H2族のruling被覆との相対同定 |
| 全H2(k)のgroupoid | H2(k)→Q_fnd(k)は全充満。全幾何点のpointed慣性も一致 | 任意基底上の相対全忠実性・本質的全射性 |
| cubic geometric開部分 | `[Gr(2,8)_geo/(PGL2)^3]`、smooth finite type、dim3。幾何点はcubic逆構成に入る | 任意の内在的cubic族の相対認識 |
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
| 横断2/2/3方向の二次持上げ | 三次Hilbert locusの横断部分の各基底ベクトルと二基底の全ての和について、Schur補行列の二次障害を打ち消す有理数補正を計算し整数行列で正確に検査。全横断方向がk[t]/(t³)上で三次成分平坦な2-jetを持つ | prop:noncubic-transverse-second-order。全次数の二次flatnessとflat Abel実現は確立。3次以上の形式積分と相対H2認識は未証明 |
| noncubicのLie接方向と三次Hilbert条件 | disjoint, shared, equalの三点でPGL9軌道+六係数のrank81（軌道80/80/79、交点5/5/4）。三次関係L:V⊗J→(V²/J)⊗Vはrank176、kernel328/cokernel49。法101の全16072線形条件rank1317/1317/1316。標数零で接次元=83/83/84（有理核の全整数検証）、三次条件の接空間を群+係数81方向で割った次元は正確に2/2/3（実際の相対H2変形かは未証明） | prop:noncubic-third-degree-tangent。局所SymPy/NumPy/Numba exact演算を実行。全次数平坦性は相対Koszul節により確立。内在H2の接空間とは未同定 |
| 関係式像の構成可能性と既約閉包 | 2つの有限型chartの像の和はH2の全幾何関係像。Chevalleyで構成可能。cubic枠束像の被約閉包Z₂はPGL9不変既約有限型、全noncubicは反Serre二次族による特殊化で[Z₂/PGL9]に入る | prop:h2-constructible-relations-and-irreducible-closure。Z₂の全点がH2とは未証明。表現可能性未証明の内在的部分層X_asとは別 |
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

この例は**選んだ根**の障害であり、別の根の存在を排除しない。構成したabelian変形が相対的な根・AZ豊富性・AS被覆を備えたH2族であるとも主張しない。従って相対H2 locusの非開性やformal smoothnessの否定は結論しない。実現集合の誘導位相ではcubicからnoncubicへの特殊化があり、両者は別の連結成分ではない。残る核心は、Q_fnd内での内在的H2実現部分関手の有限表示、相対Serre/AZ再構成・降下、および内在的位相との比較である。

群関係・χ・noncubic局所対合の再現資産は `computations/verify_stack_symmetries.py`。現在の独立読取り・計算・組版の実施範囲は末尾の検証節に集約する。

相対条件を試す具体的入力として、[定数bivector方向のOre変形](ore_quadric_deformations.md)を置く。中央元g=xw−zyの正則切断、全次数自由な商、quadratic dualのFrobenius pairingまでの証明稿を記し、相対CY・Serre・H2条件は未証明とする。主原稿の非持上げ例を相対H2の内部へ強める際の候補であり、現行定理の入力には用いない。

## O-marking から Abel 圏への忘却：幾何点ファイバーの還元（条件付き）

**問いと二種類のファイバー。** 相対 \(\mathcal H_2\) の圏を忘却した prestack を、局所H2標識を持つ相対Abel圏と**全てのexact同値**によって定め、必要ならfppf stack化して \(\mathfrak{Ab}_{H_2}\) と書く。任意のAbel圏全体の標準的な代数的モジュライが構成済みという主張ではない。自然な \(F:\mathfrak H_2\to\mathfrak{Ab}_{H_2}\) の固定圏 \(\mathcal C\) における2-fiberは、\(\mathcal M(\mathcal C)=\{L\in\mathcal C:(\mathcal C,L)\in\mathcal H_2\}\) の同型groupoidであって、\(\operatorname{Aut}^{\mathrm{ex}}(\mathcal C)\) で割らない。一方、**幾何点の同型類の写像**のファイバーは \(\operatorname{Aut}^{\mathrm{ex}}(\mathcal C)\backslash\pi_0\mathcal M(\mathcal C)\)。いずれにもroot/ambientを追加標識しない。可換 \(Q=\mathbb P^1\times\mathbb P^1\) では2-fiberは \(\coprod_{\mathbb Z^2}B\mathbb G_m\) だが、同型類のファイバーはPicardのtensor自己同値により一点である。

**数値類の必要条件（本原稿の既存計算から直接従う）。** pointed \((\mathcal C,\mathcal O)\) を一つ選び、\(\texttt{prop:first-orbit-object}\) のEuler形式・\(K_0(Q)\) 同定を使う。任意の許容 \(L\) はGK rank-one torsion-free exceptionalであり、\(\operatorname{ch}[L]=r+aH_1+bH_2+cH_1H_2\) と書けば \(r=1\)、\(a,b\in\mathbb Z\)。同節のRiemann–Roch式 \(\chi(L,L)=r^2+2rc-2ab\) と例外性 \(\chi(L,L)=1\) により \(c=ab\)。従って数値的候補は必ず \(\operatorname{ch}[L]=1+aH_1+bH_2+abH_1H_2=\operatorname{ch}\mathcal O_Q(a,b)\) に属する。この計算だけでは各類の存在・一意性も、候補の全分類も従わない。

**Kitamura–Okawaの2022年報告（引用するが未公刊の証明は未監査）。** Okawa, joint with Kitamura, *The reconstruction theorem for AS-regular 3-dimensional cubic Z-algebras*, Oberwolfach Reports 23/2022, pp.1271–1273, DOI 10.4171/OWR/2022/23, <https://doi.org/10.4171/OWR/2022/23> は、cubic \(\mathbb Z\)-代数の \(\operatorname{qgr}\) に対するrank-one torsion-free \(\chi=1\) 対象が \(\mathcal O(a,b)\), \((a,b)\in\mathbb Z^2\) で尽きる（Theorem 3）、\(\operatorname{Hom}\ne0\) による半順序が積順序になり、同じ \(\operatorname{qgr}\) のcubic表示は \(D_\infty\) 軌道になる（Theorem 1）と**報告**する。そこでの文献[4]は *in preparation*。現時点では公開済みの完全証明を一次照合したわけではない。この結果の仮定は本repoのH2との一致、\(\chi=1\) とexceptionality、GK-rankと先行文献のrankの一致を確認する必要がある。

**群論的還元（以下の三条件の下で証明）。** (i) 許容標識の同型類が \(\mathbb Z^2\) と一対一対応し積順序のHom構造を持つ、(ii) 全 \(\mathcal O(a,b)\) にH2標識を作れる、(iii) 本研究で得た適合根がこの格子上で \((a,b)\mapsto(a+1,b+1)\) と作用する、と仮定する。(ii) は各zigzagのmutationから再び許容cubic表示を得て \(\texttt{thm:all-admissible-inverse}\) を適用することを個別に照合する必要がある。(iii) は標準foundationの四項に対する二項移動と一致する。すると全exact自己同値の格子作用の像 \(H\) は \(\mathbb Z^2\rtimes C_2\) の部分群で対角移動 \(\Delta=(1,1)\) を含む。従って同型類忘却ファイバーは
\[
 H\backslash\mathbb Z^2\cong \bar H\backslash\mathbb Z,\qquad d=b-a,
\]
ただし \(\bar H\subset\mathbb Z\rtimes C_2\) は \(d\mapsto d+n\) と \(d\mapsto-d+n\) 型の像。\(\bar H\) の平行移動部分が零ならこのファイバーは**可算無限**（反射がなければ整数でラベル付き、あれば反射で割ったもの）。非零の \(m\mathbb Z\) を含むなら有限個（高々 \(m\) 個）。これは群作用の初等的帰結でありgenericな \(\bar H\) の決定ではない。スタック射の表現可能性・étale性・『degree \(\mathbb Z\)』も主張しない。

**楕円型の実計算と次の障害。** 許容楕円四つ組の線束を加法的に \(\ell_i=[L_i]\in\operatorname{Pic}^2(E)\) と書く。VdB helix \(\ell_{i+3}=-\ell_i+\ell_{i+1}+\ell_{i+2}\) から \(\delta:=\ell_2-\ell_0=\ell_{i+2}-\ell_i\) は全 \(i\) で一定。\(\eta:=\ell_1-\ell_0\) とすれば添字一移動 \((\ell_0,\ell_1,\ell_2)\mapsto(\ell_1,\ell_2,\ell_3)\) は
\[
 (\eta,\delta)\longmapsto(\delta-\eta,\delta)
\]
となり反射である。これは既存helix漸化式からの直接計算。**もう一方のruling/mutationの反射作用式は未照合**。もしそれが \(\eta\mapsto-\eta\)（適切な規格化）なら合成は \(\eta\mapsto\eta+\delta\) であり、genericなnon-torsion \(\delta\) は無限軌道を生む。しかし作用式の特定、一般点の安定化群、pointed H2とcubic \(\mathbb Z\)-代数の二択との比較を証明するまで、generic \(\mathbb Z\)-to-1は**予想**とする。

**次の具体的一手。** \(\texttt{foundation_stack.tex}\) の二ruling交換を楕円 \(\operatorname{Pic}^2(E)\) 上で計算し、\((\eta,\delta)\) への作用を求める。次に、\(D_\infty\) の一般軌道安定化と、各 \(\mathcal O(a,b)\) のH2適合性を確認する。Kitamura–Okawaの完全原稿が利用可能になればTheorem 1/3の仮定・証明を一次点検する。これは現行の最優先課題であるnoncubic境界の相対効果性とは独立の研究方向である。

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

これらの基礎結果の独立した新規性を確定したものではなく、形式証明器も使用していない。全H2対象の被覆と同値類分類は主定理に統合した。全幾何点groupoidと全pointed慣性はQ_fndへの全充満な実現で捉えた。実現集合Yの誘導位相での既約成分・連結成分は各1と証明した。一方、内在的fppf stackと全忠実な関係射は構成済み。位相の一致・代数性は未証明であり、表示stackの次元三をそのまま全H2の相対次元とはしない。

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

証明は `papers/sections/noncubic_hh_roots.tex`。四項foundationをGr(4,8)の開部分へ移すと、二項移動はL↦{(−Y,X):(X,Y)∈L⊥}となる。trace零対合から選ぶ右根による四つの比較行列は(D₀,−I,D₀,−I)、D₀=diag(1,−1)。従って実際の根の作用はJ=[[0,D_L],[−D_L,0]]、D_L=diag(1,1,−1,−1)による交代annihilator involutionである。直交形式のinvolutionとして扱うと接の正負を誤る。基底変更のLie作用は(a,b,c,k)↦(D₀cD₀,−kᵗ,D₀aD₀,−bᵗ)。自明な三次元中心の正負は(1,2)、有効Lieの正負は(7,6)である。一致根対の一次元慣性は正部分なので、全配置でHH¹/HH²の負部分が消える。本文の一般証明は三有理例からの外挿を使わない。

再現は `python3 computations/verify_noncubic_gale_root.py`。SymPyの厳密有理演算でLagrangian条件、接involution、全基底変更軌道、HH²の正負次元(3,0)/(3,0)/(4,0)を確認する。原稿のbar微分・右Zhang規約とこの計算は独立に読取り確認した。良い根の一つを特定した結果であり、他の全根の作用も自明であるとは主張しない。

## noncubic AS4被覆の一次持上げ計算

`computations/verify_noncubic_cover_tangent.py` は、R=Q上でf₁=uv、f₂=(u−av)(bu−v)、δ²=1−abとし、σ(u)=(u−av)/δ、σ(v)=(bu−v)/δ、σ(c)=d/δ、σ(d)=−δcを用いる。対象は適合根に対応するB_f^σであり、untwisted環と区別する。被覆の関係はcentralityの5本とr_c−r_d/(1−ab)の合計6本である。

| 二根対の配置 | (a,b,δ) | Gr(7,16)内の三次平坦接の次元 | 正規線持上げ行列の階数 | 全基底接を加えた階数 |
| --- | --- | --- | --- | --- |
| 非交差 | (1,−3,2) | 18 | 22 | 22 |
| 一根共有 | (0,−3,1) | 18 | 22 | 22 |
| 一致 | (0,0,1) | 19 | 22 | 22 |

二次双対E=B!のnormal元wに対し、wξ=T(ξ)wをE₃の8次元商で線形化する。未知数はδwの7個とδTの16個であり、商射の変動は理想の変動を引いて計算する。三配置で正規化自己同型はdiag(1,1,−1,−1)、23変数の核1次元はwのscalarのみとなる。したがって選んだ被覆のprojective normal lineは、これらの点で全ての三次平坦な一次方向へ一意に持ち上がる。これは厳密有理数計算による確認であり、一般点・全Artin・有限型近傍への存在定理ではない。一次式の規約と商射補正は独立に読取り点検した。

再現：`python3 computations/verify_noncubic_cover_tangent.py --case generic`、同じコマンドのcaseを`shared`、`coincident`に変更する。各実行は入力と階数を出力しassertで検査する。SymPy以外の追加依存、乱数、外部入力は不要。untwisted B_f!のnormal pencilを、そのまま適合rootでtwistした双対に残るpencilと解釈しない。

## 検証範囲と再現手順

2026-11-21 / 主論文v1.37、別稿v0.1。ローカルcheckoutでdoctorとsourcesを実行した。中心変数のχ保存、一般coherent Hom、任意係数H¹消滅に加え、cubic tailsのunbounded導来局所化・全helix/矢/shiftの比較・一様cohomology・全χ・相対条件への昇格を独立読取りした。旧計算suiteは再実行していない。数学的読取り、厳密計算、組版、保存は別の状態であり、外部査読・形式証明・包括的な新規性判定は未実施である。

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
# NumPy/Numba を入れた場合の独立な接空間証明書
python3 computations/verify_commutative_quadric_tangent.py
python3 scripts/check.py sources --manuscript papers/quiver-avatar-moduli.tex
python3 scripts/check.py build --manuscript papers/quiver-avatar-moduli.tex
latexmk
```

**別稿の論理点検。** QPの消去と慣性、有限foundationの開条件・関係数・重なり、avatarの支持補題・消滅・垂直fiberのTor・非被約基底への直像と降下、weighted stackとSigma2の反Serre障害は独立読取りを行った。全AS同型類分類の再監査、相対AS/avatar同値、適合H2部分の開性の証明は含めない。

**別稿の計算実行。** `computations/verify_quiver_avatar_charts.py` を実行し全PASS。Sigma0/Sigma2のCox単項式でHom次元 `(2,2,2,4,4,6)`、結合律、二つの核の非分解性、短い関係の重なり零を確認した。生成矢・関係・完成矢はSigma0で6/2/8、Sigma2で8/4/12、合成したrank(3,4)の有限代数で7/3/10、product collectionで8/4/12。整数・有理数による有限例の検算であり、合成例のAS正則性、全AS分類、stack開性、相対H2条件を認証するものではない。この軽量スクリプトは通常のmath suiteにも追加したが、今回全旧suiteは再実行していない。

**組版・参照確認。** 主論文v1.37のnoncubic根節は、二項移動のbar複体、実際の右根との四つの比較行列、交代Gale双対、慣性Lieと全HH接空間、指定Artin持上げ、一般étale代数化を独立に読取り点検した。Gale計算の非交差・一根共有・一致の三有理例と、AS4正規線の一次持上げ三例を実行PASS。LuaLaTeX・latexmkで255頁のPDF/SyncTeXを生成した。最終logのWarning・Overfull/Underfull・文字欠落・未定義参照は零、新節を含む選択12頁と主要2頁を画像確認した。sources PASS（44 manuscript files / 532 labels / 256 citation uses / 7 Markdown files）。明示noncubic効果性の選択9頁と主要2頁、cubic認識・相対Picard・smooth atlasの選択21頁と主要2頁の既存確認も保持する。別稿v0.1は変更せず、既存25頁の組版・画像確認を保持する。全頁の個別目視、外部査読、形式証明、新規性の包括的確認は未実施。

既存入力の独立点検範囲は、全分類のD1–D3・有限K・同値判定・根選択独立、standard/non-standard全帰着、退化型のPic・貼合せ・Serre比較、foundation/ruling/慣性・degree gerbe、cubic稠密性・特殊化・relative bar分解である。証明は現行原稿に保持する。既存の有限検算はSegre積、Ore正規性、全非整型四つ組、period square、群関係・χ・局所対合等を対象とするが、今回の新定理の計算機による認証ではない。

導入は [CLOUD_CODEX.md](../CLOUD_CODEX.md) と `bash scripts/bootstrap.sh`、依存は `requirements.txt`。checkerのPASS/FAIL/SKIPは実施成功・失敗・未実施であり、数学的完成を自動判定しない。git読取と書込認証は別であり、CLI pushが認証不足ならGitHub connectorの通常コミットも使用できる。研究repoを先に保存し、最新research-hubを読んで該当項目を反映する。
