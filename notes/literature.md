# 非可換 quadric 分類：現行文献比較

資料確認日：2026-11-22（日本時間）。v1.52。現行三論文A/B/Cに対応する一次資料比較。
以下で「確認」は記載箇所の本文・仮定の照合を意味し、外部論文の全証明を独立に再検証したという意味ではない。

## OU2014 §4–5と相対Serre根の比較資料

OU2014 arXiv:1403.0713v1の印刷p.8 (4.11)–(4.13)と
p.9 (5.8)–(5.10) を2026-11-22に一次PDFの各ページ画像で確認。
§4は(E,O(2o),O(2z1),O(2z2))の楕円四つ組を与え、
z1とz2それぞれに独立のE[2]平行移動を使う。
§5はpotential→quintupleの有限GIT次数4を
P³/S3→P³/(S3⋉(Z/2)³)の表示と同時符号反転の自明性で証明する。
OU側の有効群Γ=F₂²、全群Γ⋊S3≅S4、
一般四重射のS4 Galois閉包という群論は本稿Cでの新しい演繹。
Bの相対Picard rootの式a^-2=NとOUのL2/L0を比較すると
a=O(o−z2)⊗E[2]となることも本稿Cの直接計算である。
ただしOU potential coverとz2のE[2] root coverそのものの同型は未証明。

論文Bの相対cubic理論
prop:general-cubic-canonical-tails、
thm:geometric-cubic-relative-effectivity、
lem:picard-halves、
thm:relative-compatible-root を2026-11-22に直接再読した。
非線型geometric quintupleのcanonical tails・Oは
Picard根を選ぶ前に基底上にある。
相対Serre根とAS4被覆はfppf局所の存在条件なので、
quintupleから内在的H2への相対射が根の選択なしで定まる
というCの新定理を証明する。
これはBの有限型相対効果性を引用した結果であって、
OUのGIT半安定化全体にH2への射があるという意味ではない。
なおB自身の全主定理の独立な全面検証は未完了。

## 論文CのOkawa--Ueda GIT比較と慣性の一次資料

Shinnosuke Okawa and Kazushi Ueda, *Noncommutative quadric surfaces and noncommutative conifolds*, [arXiv:1403.0713v1](https://arxiv.org/pdf/1403.0713), 2014。
2026-11-22に一次PDFの印刷p.3・Theorem1.1(1)--(4)をページ画像で確認した。
quintuple表示の生のmoduli stackのgeneric stabilizerはGm^4で、
その後のGIT商はP(2,4,4,6)、
conifold potential側の生stackのgeneric stabilizerはGm、
そのGIT商はP(1,2,3,4)。
potential GITからquintuple GITへの有限射は**次数4**である。
これらは既知の結果であり、本研究の新成果ではない。
同定理は構造対象Oだけを指定した本研究のH2への
忘却射の次数や、二つのGIT商と内在的H2がスタック同値であるとは述べない。

Cの新補題 prop:qa-ou-scalar-gerbe は、
quintuple群∏GL(V_i)×GL(W)に含まれる
中心K≅Gm^4が関係テンソル全体に自明に作用し、
さらにquintupleから作るZ代数の頂点共役を通じて
pointed tailsの恒等自然変換へ落ちることを示す。
この慣性核が消えない生の表示商からH2への射は
表現可能ではあり得ない。
これは既知のgeneric stabilizerの記述と
本研究のpointed比較を明示的につなぐ確実な命題であるが、
全quintuple上の適合H2族の存在・相対開性は未解決。
Cの prop:qa-forgetful-homotopy-fiber は
Aut群の剰余集合と相対慣性を区別する一般groupoid補題。
GITのdegree4から内在的Serre根の個数は推定しない。


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
