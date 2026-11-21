# 現行研究ノート：O-marked 非可換 quadric

2026-11-21 / v0.8（数学原稿v1.7）。最初に [研究方針](../00_research_plan.md) を読む。証明の正本は [主原稿](../papers/nc-quadric-classification.tex)、文献確認の正本は [文献比較](literature.md)。本書は作業履歴ではなく、現在有効な知識と再開点を記す。

## 定義と規約

対象は `(C,O)`。`s`とAS4被覆を同時に存在させる。Gabriel–Krullの`C₀`は有限長、`C₁`は`C/C₀`で有限長になる対象の逆像。`qO`が非零単純かつ`Hom(C₁,O)=0`をrank-one torsion-freeと呼ぶ。`GKdim=1`の意味ではない。

右加群を採用し、`B_n=Hom(O,sⁿO)`、`a*b=s^{deg b}(a)∘b`。`Γ_*(M)`の右作用も同じ順序。cubic repoの表示された積と反対なので、外部のNakayama・正規化自己同型の公式を直接コピーしない。

強いH2条件は `B ≅ A/(g)`、`A`は型14641、`g∈A₂`は正則正規。`g`の代表のスカラーは区別せず、最終対象ではambient自体を忘れる。`s²≅S⁻¹[2]`の同型は指定しない。根同型をrigidifyしたmoduliやtrace coherenceは別問題である。

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
| noncubicの Koszul 性と一次全次数平坦性 | 二重平方環の二次 Gröbner（PBW）表示からBはKoszul、偶数VeroneseとZhang twistのRもKoszul。三次の重なりの一次整合はKoszulの次数0 Hochschild 2-cocycle条件に一致し、双対数上の二次関係変形が三次平坦なら全次数平坦 | prop:noncubic-antiserre-koszul, lem:koszul-first-order-degree-three。二次以降の一般Artin族には未拡張 |
| noncubicの内部次数0 Hochschild 次元 | 非交差、一根共有、一致根対でHH¹_0=1,1,2、HH²_0=3,3,5。C¹=81、C²=1400、C³=16072、rank(d¹)=80,80,79、rank(d²)=1317,1317,1316 | thm:noncubic-hh01-hh2。foundation代数のHH≥3消滅とは異なる |
| 横断2/2/3方向の二次持上げ | 三次Hilbert locusの横断部分の各基底ベクトルと二基底の全ての和について、Schur補行列の二次障害を打ち消す有理数補正を計算し整数行列で正確に検査。全横断方向がk[t]/(t³)上で三次成分平坦な2-jetを持つ | prop:noncubic-transverse-second-order。全次数の二次flatness・3次以上の形式積分・相対H2実現は未証明 |
| noncubicのLie接方向と三次Hilbert条件 | disjoint, shared, equalの三点でPGL9軌道+六係数のrank81（軌道80/80/79、交点5/5/4）。三次関係L:V⊗J→(V²/J)⊗Vはrank176、kernel328/cokernel49。法101の全16072線形条件rank1317/1317/1316。標数零で接次元=83/83/84（有理核の全整数検証）、三次条件の接空間を群+係数81方向で割った次元は正確に2/2/3（実際の相対H2変形かは未証明） | prop:noncubic-third-degree-tangent。局所SymPy/NumPy/Numba exact演算を実行。次数4のHilbert条件・実際の内在H2とは未同定 |
| 関係式像の構成可能性と既約閉包 | 2つの有限型chartの像の和はH2の全幾何関係像。Chevalleyで構成可能。cubic枠束像の被約閉包Z₂はPGL9不変既約有限型、全noncubicは反Serre二次族による特殊化で[Z₂/PGL9]に入る | prop:h2-constructible-relations-and-irreducible-closure。Z₂の全点がH2とは未証明。有限表示の内在的X_asとは別 |
| noncubicの相対heart・相対orbit | `R`の`qgr R`を構造対象付きnoetherian Abel heartとして任意のNoetherian基底上に定義。étale局所に`qgr B^σ≃qgr R`。weighted P(1,1,2)上`RHom(B,tⁿB)=B₂ₙ[0]`が全n・底変更に整合（`cor:noncubic-relative-orbit-hom`, `prop:noncubic-relative-heart-veronese`） | 任意の内在的noncubic族のこの相対heartへの帰着、全flat coherent対象の相対双対・AZ/AS等 |
| cubicの相対反Serre環 | smooth proper foundationの逆Serre双加群から`RHom(e₀Λ,tⁿe₀Λ)`。cubic開では全nでrank(2n+1)²局所自由 | 任意のH2族からの相対foundation抽出 |
| 共通Grassmann射と実際の特殊化 | cubic開Cとnoncubic表示[P/G]の双方から`[Gr(56,81)/PGL9]`へ射。各noncubic点へのfoundation直線族も全次数平坦な反Serre環の族を与える | 両chartの相対的な貼合せとfull内在H2との同値 |
| 選んだSerre根の一次変形障害 | 持上げにはHH²類の保存が必要。Q上でs_*u=−uとなる適合根と非零変形を構成 | 別の根の存在や相対H2条件の開性は判定しない |

**修正定義で厳密に得られる stack。** 反Serre関係のG=Gr(56,81)から次数3を作る自然写像 L3:U⊗J→((U⊗U)/J)⊗U は504→225であり、rank176ならR3は49次元局所自由。この正確rankの局所閉部分X3は非被約基底まで含む真正な有限型スキームで、PGL9商はArtin。GL9版が生成元と関係の相対モジュライ、PGL9版が共通次数スカラーのrigidification。普遍Rを無理にPGL torsorから取り出すBrauer障害はdet(R1)^-11 det(R2)^2の重み一の線で消え、R_nをその-n乗で捩って降下する。これらは全次数のflatness、Serre平方根・AZ・AS被覆を**課していない**。対照的に既存のcubic chart Cとnoncubic chart Npresの非交和は全幾何点慣性を再現するが、型を局所定数にしており、見かけの成分数が二になる。これは自然なH2相対スタックの既約性の反例ではない。

**接複体による非同値の検出。** coincidence f1=f2=uv ではX3の普通の一次接次元84・PGL9接軌道79なので、[X3/PGL9]の接複体のH0は5次元。一方Q_fndは滑らか次元3・慣性Lie1なのでH0=4。よって少なくともこの点の形式近傍は同値でない。したがって X3 の余分な方向を排除する、または内在的H2として理解する条件が必要。これが現在の最も短い差分証明である。

**Koszul の低次変形と二次障害。** Rのquadratic Koszul bimodule complexで内部次数0のHochschild cochainはC¹=Hom(V,R₁)、C²=Hom(J,R₂)、C³=Hom(K₃,R₃)、K₃=(V⊗J)∩(J⊗V)である。三次Hilbert条件の線形化がd²であり、degree-3 flatな双対数上の二次関係は全次数flatなgraded algebra first-order deformationを与える。三基準点のd²核83,83,84とd¹像80,80,79からHH²_0=(3,3,5)を得る。HH¹_0はEuler導分を含み=(1,1,2)。これは有限foundation代数の高次HH消滅を言い換えたものではない。

**横断方向の二次持上げ。** L₀の176×176単位行列式小行列Aを取り、L(t)=L₀+tL₁(φ)+t²(L₁(ψ)+L₂(φ))をSchur補行列で展開する。K₀をkernel、Q₃をcokernel基底射影として、Q(φ)=Q₃(L₂(φ)K₀−L₁(φ)i_CA^{-1}(L₁(φ)K₀)|_I)を計算する。全三点で横断基底(2,2,3本)と相異なる二基底の和(1,1,3本)に対しd²ψ=−Q(φ)の有理補正を構成し、整数行列積で厳密に確認した。一致根対では分母2の補正も現れる。Qが二次式であるため、これらの零性から全横断線形結合への補正が構成できる。ただし結論はあくまで **R₃のrank49条件のk[t]/(t³)-平坦性**であり、全次数の二次平坦性、HH³の消滅、正式な相対H2族と混同しない。

**三次関係階数の接空間。** 基準 $\dim V=9,\dim J=56,\dim R_2=25,\dim R_3=49$ に対して $L_J:V\otimes J\to (V^{\otimes2}/J)\otimes V$ のrankが176となる。このrank≤176のdeterminantal locusの接ベクトルは $\phi\in\operatorname{Hom}(J,R_2)$ で $\ker L_J\to\operatorname{coker}L_J$ の線形化が零となるもの。56×9=504、25×9=225、kernel328、cokernel49で、条件行列は16072×1400である。固定pivotで $J$ の affine 座標を取り、法101で三根配置ごとに全行を簡約した階数は1317,1317,1316。整数係数のminorは標数零でも非零なので、まず標数零の接次元は≤83,83,84。さらに法101核基底から83,83,84本の有理ベクトルを復元し、整数係数の線形化行列で全ベクトルの零性を厳密に確認したため、標数零でも接次元は**正確に**83,83,84である。ただし、この2/2/3方向が次数4以降のHilbert条件や内在的H2を満たすかは未確定。PGL9と六係数の接像は、群Gの軌道による上界と法101でのrank81の下界から標数零で正確に81。群商スタックの次元1と、Grassmann内にあるframed接像81を混同しない。次数4の一次平坦性は今回のKoszul一次変形原理から従うので別計算不要。次は次数三以上のobstructionとfoundation横断射、相対heartの認識を検査する。

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

群関係・χ・noncubic局所対合の記号検算は `python3 computations/verify_stack_symmetries.py`。foundation・HH計算、ruling二択、相対交換のcoherenceと幾何点groupoid、pointed慣性、gerbe中立化、および選んだ根の変形障害は独立読取り点検を行った。さらにcubic開部分の稠密性、各noncubic点への特殊化とrelative bar分解も独立に点検し、既存入力を前提として実質的な欠落は見つからなかった。現行v1.5の変更後LuaLaTeX組版は未実施。v1.2の97頁組版は成功しているが、v1.4の確認と混同しない。変更のない記号計算資産の同日PASSを保持する。詳細な実施範囲は末尾の検証節に記す。

相対条件を試す具体的入力として、[定数bivector方向のOre変形](ore_quadric_deformations.md)を置く。中央元g=xw−zyの正則切断、全次数自由な商、quadratic dualのFrobenius pairingまでの証明稿を記し、相対CY・Serre・H2条件は未証明とする。主原稿の非持上げ例を相対H2の内部へ強める際の候補であり、現行定理の入力には用いない。

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

これらの基礎結果の独立した新規性を確定したものではなく、形式証明器も使用していない。全H2対象の被覆と同値類分類は主定理に統合した。全幾何点groupoidと全pointed慣性はQ_fndへの全充満な実現で捉えた。実現集合Yの誘導位相での既約成分・連結成分は各1と証明した。一方、内在的な相対モジュライの位相との一致、族の降下・代数性は別途未証明であり、表示stackの次元三をそのまま全H2の相対次元とはしない。

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

### v1.5 の今回の追加検証

- `computations/verify_noncubic_degree3_tangent.py` をmainに追加。NumPy・Numbaは**オプション依存**（標準math suiteには追加しない）。法101、有限体の整数行基本変形で3つの代表根配置を全て検証する。既存の25 pivotスクリプトを再利用する。実行コマンドは `python3 computations/verify_noncubic_degree3_tangent.py`（必要なら `python3 -m pip install numpy numba`）。
- 今回の作業環境で独立した同等のローカル計算コードを実行し、3点のPGL9 orbit／六係数／合成の階数を(80,6,81)、(80,6,81)、(79,6,81)、三次Hilbert条件の行列を16072×1400として全行rank1317、1317、1316でPASSと確認した。法103で一般点rank1317も照合した。加えて、法101核83,83,84本の分母2以下・分子絶対値5以下の有理数再構成から整数ベクトルを作り、整数係数の全16072×1400行列で積が厳密に零になることを確認した。自由変数の対角成分からそれらは有理数上独立であり、法101の階数下界と併せて標数零の正確な接次元を証明する。これは**厳密な整数計算**であり、数値的近似ではない。
- 公表用命題の標数零での結論は、群作用によるrank81の上界と法101rankの下界、および三次Hilbert条件に対する整数核ベクトルの構成・検証を組み合わせたもの。実際の `\mathfrak H_2` の接空間を証明したわけではない。今回GitHubに保存したスクリプトそのものを独立にcheckoutして再実行したことや、新版全文のLuaLaTeX組版を主張しない。
- v1.4のソース部分に行った静的検査と、v1.2で実施した97頁のPDF組版は、それぞれの当時の確認範囲である。v1.6の全ソースchecker・全math suite・LuaLaTeX組版は未実施。

### v1.6 で加えた数学・検証の射程

- 数学的結果：noncubic R の Koszul 性（PBW、Veronese、Zhang）、三次平坦な一次二次関係変形の全次数平坦性（Koszul双加群解消の次数0 cocycle）、三基準点でのHH¹_0=(1,1,2)およびHH²_0=(3,3,5)、横断方向の三次Hilbert条件の二次持上げ。証明の正本は noncubic_stack.tex の対応ラベルを参照する。
- 新しい再現資産は computations/verify_noncubic_second_order.py。NumPy>=1.24、Numba>=0.60、既存SymPyが必要。順番に python3 computations/verify_noncubic_degree3_tangent.py と python3 computations/verify_noncubic_second_order.py を実行する。両ファイルは重い有限体・整数検算なので標準math suiteの必須依存にしない。
- 同等のローカル探索コードでは、三基準点の横断2/2/3方向の全基底と全二項和について、法101での可解性、法101²と有理数の再構成、**整数係数での残差恒等零**を確認した。二根対一致点の補正で分母2を要する組合せもある。最初に一度ベクトル化の転置規約が不一致になった候補は廃棄し、正しい線型化との一致を確認して検証し直した。
- GitHub上の再現コードはmainへ保存したが、**保存したコードそのものを独立環境へcloneして再実行したことは確認していない。** v1.6全ソースchecker・全文LuaLaTeX組版・PDF表示、既存全math suiteの再実行は未実施。v1.2の97頁PDF組版は旧版の実施記録であり現行版への保証ではない。外部査読・形式証明・包括的新規性判定も未実施。

### v1.7 の構成済み表示と検証境界

- 本文の prop:split-h2-presentation-moduli, prop:truncated-antiserre-moduli-stack, prop:truncated-versus-foundation-tangent に、非交和表示、三次rank176の局所閉表示、重み一線束による普遍環の降下、二根対一致点のH0接次元5対4の違いを直接証明した。
- これは既存のnoncubic接空間計算を入力にする数学的帰結であり、今回新たな巨大な数値計算を実行したことを意味しない。改訂後のTeX新規参照・環境の静的検査は個別に確認する。全文LuaLaTeX組版およびv1.7用PDFは未実施。
- 再開時は三次Hilbert X3 が与える自由な余分の一次方向と相対foundationの接方向の差を認識し、元のH2と構成済み修正stackを混同しない。

## 検証範囲と再現手順

**現行v1.7（2026-11-21）：相対反Serre・Clifford追補の全体組版および既存計算の再実行は未実施。** v1.2の構成確認・97頁LuaLaTeX組版はPASSだったが、現行v1.3のPASSとは扱わない。 証明の読取り点検、記号検算、組版、画像表示、GitHub保存は別々の確認であり、機械チェックを証明認証とは扱わない。

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

2026-11-21の現行確認：全分類定理のD1–D3、有限K、同値判定、根選択独立、全被覆・非交差を独立担当が点検した。standard・non-standardの全帰着、同一支持排除、全退化型のPic・大域自己同型・貼合せ、Serre比較の双加群計算、逆構成から全H2公理までの依存も独立に点検した。追加したfoundation表示・HH消滅、内在的ruling対、相対交換のcoherence、幾何点groupoid、noncubic慣性・good moduli、degree gerbe中立化と選んだ根の持上げ障害も独立読取りで点検した。いずれも既存入力を前提とし、外部査読や形式証明ではない。

v1.2のソース確認は24原稿・168ラベル・137引用出現・主要Markdown7点を対象としてPASS。cubic開部分が実現集合に含まれること、直線上の有限個の除外点、正規化relative bar分解の有限性・射影性・底変更、および内在的相対モジュライへの移行条件を独立に読取り点検した。全代数閉拡大体上の像を合併する定義とし、H2公理一般の底変更安定性を暗黙に仮定していない。v1.2についてLuaLaTeXで97頁のPDFとSyncTeXを生成し、最終ログに警告・未定義参照・欠字・はみ出しはない。v1.2のPDFの1–3頁と82–86頁を画像化して一覧で配置を確認し、新しい命題と移行条件を含む83–85頁は個別表示でも確認した。今回全97頁を画像で再校読したという意味ではない。

v1.3の既存補題については、中心Clifford直和のHilbert級数`(1+2z+z²)/((1-z)²(1-z²))=(1+z)/(1-z)³`、`B₂=9,B₄=25,81−25=56`をSymPyで有理式として照合し、Clifford traceの四元基底積行列式が`−1`であることを記号計算で確認した。相対Serreのweighted stack双対・rigidification・全次数の底変更は本文に証明を追加したが、外部査読・形式証明とは区別する。TeX全文の改訂後組版とソース全体の静的チェックは未実施。

今回のv1.4では新規に computations/verify_noncubic_antiserre_pivots.py を追加した。対象は六係数を独立不定元とした二重平方環のPBW簡約、25 pivotの単位行列式、二つの二乗積からの六係数回収である。同内容のローカルSymPy試作を実行しPASS（25列、行列式±1、六係数回収）と確認した。GitHub上の正式スクリプトをcheckoutして行う全math suite実行、v1.4の全ソースcheckerとLuaLaTeX組版は**未実施**。一般二次Veroneseの相対同型とChevalley・閉包の証明は本文の論理的議論であり、有限検算はそれを認証しない。旧計算資産は変更せず保持した。同日に実行済みの全非整型の三次関係・四次テンソル・周期平方・非被約gridの補正引戻し、およびnoncubicの射影群関係・χ・局所対合と正則切断の記号恒等式はPASSである。この検算は、今回加えた成分・特殊化命題の計算機による証明ではなく、それらは前段の理論的な読取り点検による。

既存の計算・証明の確認範囲には、四周期比較、最初の軌道対象、非cubic例、有限被覆判定、多パラメータskew polynomial分類、Ore切断の正規形・四元数斜体・根の対合・同値判定が含まれる。これらの証明は現行原稿に保持する。外部査読、形式証明、包括的な新規性の確定は行っていない。以前のPDFの表示確認を現在の全頁の確認とは扱わない。

運用checkerはPython 3.12.14／SymPy 1.14.0と既設TeXで実行できる。Python・TeX不足のSKIP、未定義ラベルのFAIL、壊れた既存venvの保持、各段階の独立した継続は確認済み。pip・aptによる新規導入、Cloud環境の作成・Publish・新規task起動、VS Code UI操作はこの確認に含まれない。

GitHubのgit読取が利用できても書込認証は別に必要である。GitHub connectorによる通常コミットも許可された保存手段として使用できる。research-hubの更新は対象repo保存後に最新READMEを読み、並行更新を保持して行う。
