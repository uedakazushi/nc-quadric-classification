# 研究方針：O-marked 非可換二次曲面の分類

2026-11-22 / v0.42。**再開時は本書を最初に読む。GitHub `main` が正本。** 主論文はv1.41、別稿はv0.1。体上の全同値類分類と、内在的な相対モジュライの代数性を区別する。

**内在的な相対モジュライ $\mathfrak H_2$ の有限型代数性の証明を完成した。現在の優先事項は、有限型atlasの証明監査と、foundation表示・境界幾何との比較である。** 平方根・根同型・AS被覆はfppf局所の存在条件とし、標識に加えない。有限型表示商や幾何点の被約閉包を、そのまま内在的モジュライと定義しない。

## 現在の到達点と未解決の核心

**体上の分類と、相対モジュライ全体の有限型代数性の証明を原稿に統合した。** cubic側はlinearデータと被約・非被約を含む全Van den Bergh許容四つ組、noncubic側はP¹上の二つの被約二点集合の非順序対で分類する。四生成・七二次関係の有限同値判定を持ち、両領域が全対象を覆う。これらは既知入力を明示した本文の証明であり、包括的な新規性確定・外部査読・形式証明とは区別する。

**内在的fppf stackと代数性の還元。** 局所有限型k-scheme上のmodule-object基底変更・descent、canonical compact圏・Serre・AZ・相対AS4被覆を定義に含める。反Serre再構成はH2↪[X3/PGL9]を全忠実にし、対角はaffineかつ有限表示。framed部分層X_asを用いてH2≃[X_as/PGL9]だが、X_as全体は有限型・滑らかな83次元スキームとして表される。`relative_moduli.tex`。

**cubic領域全体のsmooth Artin開部分。** `thm:cubic-smooth-open` は、全幾何fiberがcubicとなる内在的部分スタックV_cub⊂H2が、有限型で滑らかな純次元3のArtin開部分であると示す。非線形の普遍quintuple上では相対Picard群の[−2]に沿うétale被覆で適合根を構成し、linear点は可換Qのchartで覆う。各chartの全閉点で、指定されたpointed同型を保つArtin持上げを証明する。relation schemeはU×_[X3/PGL9]Uであり、選んだ根やfoundationを保存しない同値も含む。`cor:cubic-formal-h2-abelian` により全cubic点で形式H2変形とpointed Abel変形は同値で、HH≥3=0、dim HH²−dim HH¹=3となる。noncubic境界を含む全H2の代数性は下記の有限型効果性で証明し、ambient内の開性は一致根対で否定する。

**局所代数性を支える有限型効果性。** 標準Morita根を有限型étale近傍へ代数化し、二周期cubic列の全Hom・普遍解消・相対Koszul性・homological AS4被覆を同じ開U°上に構成した。任意affine基底でD(QGr B)≃D(Mod Λ)、compact≃Perf Λ、shift≃Serre根となる。相対point curveとKeelerの消滅、regular normal族、linear閉部分の厳密なSegre表示、次数別完備化による貼合せから、任意Noetherian基底変更後のBとAの左右Noetherian性を証明した。一般Hom有限・flat basechange・fppf・AZ・全χ・全軌道と同じ根のAS4被覆が揃う。証明は `relative_cubic_tails.tex`、`relative_noetherian_patching.tex`、`relative_cubic_noetherian.tex`。元のsite外の局所環については有限型R-test上の同じ公理という範囲を守る。

**Artin変形の確立した入力。** 全H2の切断環・反Serre環はKoszul。三次まで平坦でfiberがKoszulなら全次数平坦・相対Koszulとなる。全flat Abel Artin変形にはrank24のfinite foundationとcanonical反Serre軌道環があり、偏極忘却の接核はHH¹、Abel変形はHH³=0により無障害。可換Qの標準根は全Artin変形に存在しMorita類が一意、canonical hullのAS4被覆を持つ。形式H2＝Abel、接次元9・慣性次元6。異なる根対のnoncubic点でX3はsmooth・次元83、商は次元3となる。内在H2との全Artin比較は下記の中央被覆と局所tailsによる。`relative_koszul.tex`、`artin_foundation.tex`、`artin_roots.tex`、`quadric_artin_hull.tex`。Jacobianによる全一次方向の明示構成も保持する。

**noncubic変形の具体的なétale表示。** `prop:noncubic-lagrangian-etale-slice` により、Lagrangian Grassmannian LG(4,8)の開部分を7次元群で割った商から、全noncubic点を含むfoundation変形の開部分への表現可能なétale射を得る。法軌道写像の行列式はPlücker O(3)の切断で、正規形では−32α。根対一致では対角L₀を選ぶ必要があり、別のtrace零交換根にはHH²の負方向が1次元残る。この有限代数の表示を、全fiber認識と全軌道比較を経て、下記の内在H2のatlasへ接続する。

**方法上の障害と補助定理。** 非可換P¹束の候補対角列には、全行からHomが消える非零coherent対象を持つgeometric quintupleの反例がある。これはその模型と軌道列の比較を妨げるが、BのNoetherian性を否定しない。`ruled_diagonal_obstruction.tex`。有限foundationやgraded coherenceだけではNoetherian heartは従わないことも研究ノートに具体例で記した。偏極認識の有限表示局所閉条件、固定BのAS4被覆incidence、χの有限型基底変更、任意係数の構造H⁰/H¹は独立の一般補題として保持する。

**一般二周期族のcanonical AS4被覆。** `thm:universal-cubic-hull` は、geometric cubic族と実際の二周期βから、逆coevaluationの線束値写像Φ_i:S_i→W_i、Φ_i|W_i=2idと階数6の核H_iを構成する。A=T(B₁)/(H₀)は全次数projective、rank Aₙ=C(n+3,3)、双対は階数列(1,4,6,4,1)のKoszul Frobeniusであり、正則正規二次線GによるA/(G)=Bを持つ。任意Noetherian基底変更後も左右Noetherianである。まずE=B!の正規線Nを割ったP=E/(N)をprojectiveにし、PPをPへ適用してA=P!を平坦にするため、非被約基底でfiber次元一定だけに頼らない。AS4被覆は任意のβに成立するが、同じ根のSerre平方条件は独立に確認する。

**相対Picard根と全cubic族の認識。** `thm:relative-compatible-root` は非線形のsmooth reduced普遍quintuple基底上で、N=L₂L₀⁻¹の二等分とATVの相対作用から実際の二周期βを構成する。β²はcanonical四周期θにvertex scalarを除いて一致する。同じβに対応するperfect双加群のSerre比較を、有限表示局所閉の比較空間と普遍基底の被約性で証明し、その後に任意の非被約底へ引き戻す。任意の根を最初から変形可能とは仮定しない。`thm:geometric-cubic-relative-effectivity` が普遍Noetherian性・canonical tails・同じ根のAS4被覆から全相対公理を供給する。DDLで五つのhelix対象を持ち上げ、四つの矢空間と四次syzygy直線を回復することで、指定同型を保つquintuple chartのArtin持上げが得られる。

**明示noncubic表示族の全相対認識。** `thm:noncubic-relative-effectivity` は二つの非退化二元二次形式の表示スタックNpres=[P/G]から、実際のH2族を構成する。中央Clifford表示を重み付き射影スタックX=P_R(1,1,2)上の有限局所自由代数へ移す。G=⊕_{i=0}³B~(i)はtiltingではなくcompact generatorであり、そのdg Endとweighted Čechからproper性・任意導来基底変更を得る。中心有限代数上のR-flat加群のfiber-perfect持上げを用いて対角のperfect性を証明し、canonical compactのsmoothnessを確認する。traceによる同じ根のSerre平方、AZ・全軌道、Ore/PBWによる普遍Noetherianな相対AS4被覆を合わせ、全相対公理を満たす。Npresは次元1であり、noncubic点の全横断変形を覆うatlasや相対全忠実性は結論しない。

**全noncubic点の良い根と有限型代数化。** `thm:noncubic-hh-trivial-root` は、根対を交換するtrace零対合から選ぶ適合Serre根が、全foundation変形のHH¹・HH²へ恒等に作用することを証明する。四平面Gr(4,8)の交代Gale双対として根の作用を計算し、接の正負次元(10,6)と有効基底変更Lieの(7,6)を比較する。根対非一致ではHH¹=0・HH²=3、一致ではHH¹=1・HH²=4で、いずれも負のHH部分は零となる。従って全Artin Abel変形へ根が延び、そのMorita類は一意である。`prop:hh2-etale-morita-root` と `cor:noncubic-etale-morita-root` により、全noncubic点の有限型étale近傍上で実際の可逆双加群・Serre平方同型・二項窓の比較を構成できる。このMorita根を、下記の局所環上の全軌道・中央被覆の構成へ使う。

**良いnoncubic根の中央AS4被覆。** `thm:noncubic-central-hull` は、二形式f₁=uv、f₂=(u−av)(bu−v)、θ=1−ab≠0の全配置で、従来のOre被覆とは別の六関係環A₀を構成する。g₀=uv−vuはuntwisted環で正則正規、良い根によるtwist後に中央となる。二次双対のχ=UV−VUを割ったKoszul Frobenius環のpairing行列式はθ⁴/4と−θ⁸/16。twist後の二次中心は一次元、二次反中心は零である。一般係数の厳密検算と全次数の構造証明を区別する。

**noncubic局所環上の効果性と全Artin認識。** 五頂点の非極小bar解消により、極小Betti数の変動を許して、同じ局所環上の全前向きHom・全軌道・canonical tails・Noetherian heartを構成した。二次双対の反中心消滅はgeneric cubic canonical線のnormalizerが−1となる可能性を排除し、中心直線を直和因子として延長する。閉fiberの正則性と単元minorから全次数の中央AS4被覆が延びる。指定還元同型付きArtin変形をétale foundation chartへ持ち上げると、全noncubic点で形式H2変形＝pointed Abel変形となる。非一致根対では接3・慣性0、一致では接4・慣性1、いずれも無障害。既存cubic結果と合わせ、全H2幾何点でArtin形式認識が成立した。証明は `thm:noncubic-local-tails-effectivity`、`thm:noncubic-local-central-hull`、`cor:noncubic-all-artin-h2`。

**noncubic境界を横断する有限型効果性。** `thm:noncubic-finite-type-effectivity` は、全noncubic点に実際のH2族を持つ有限型étale近傍を構成する。Lagrangian四平面の二射影M,Nに対し、Segreとの交点を除き、Cr(N adj M)とCr(M adj N)の行列式を可逆化する。全幾何fiberをcubicまたは二形式normal foundationへ認識し、同じ四項とSerre四周期から全Homを有限projectiveにする。非被約閉部分V(det M,det N)のétale相対正規形と二つのcubic開から普遍Noetherian性を貼り合わせる。全fiber Koszulを先に確認し、局所中央線をspreadして同じ根の中央AS4被覆を得る。一般のKoszul開性や無限個の開の交叉は使わない。証明は `papers/sections/noncubic_finite_type.tex`。

**内在的な全モジュライの有限型代数性。** `thm:global-h2-smooth-finite-type` により、局所有限型k-schemeのsite上のH2は、有限型・滑らか・純次元3のArtinスタックにより表され、対角はaffine有限表示である。指定されたpointed同型を保つArtin持上げで各効果的近傍をsmooth chartとし、実際のnoncubic表示族の準コンパクト性から有限個を選ぶ。relationはU×_[X3/PGL9]Uで、根・被覆・foundationを保存しない全pointed同値を含む。X_asは有限型・滑らか・純次元83のスキームとなる。一致根対では接次元が内在側4・ambient側5（framedでは83・84）なので、X_as→X3は開immersionではない。証明は `papers/sections/h2_smooth_atlas.tex`。

**残る比較と次の課題。** 全H2の代数性とX_asの表現可能性は証明した。有限foundationのruling商Q_fndとの相対同値・位相比較、境界の幾何と成分の記述、任意Noetherian基底で素朴に同じAbel公理を課す関手と[U/R]の一致は別の課題である。公表前の先行研究比較と広い証明監査も続ける。新規性の包括的確定・外部査読・形式証明は未実施である。

**別稿と研究間の関係。** `papers/quiver-avatar-moduli.tex`（v0.1）は有限foundationの8/10/12矢chart、重み四QP、反標準avatarを扱う独立論文である。体上の表示と相対H2の実現条件を区別する。cubicから全noncubic点へのsmooth proper dg特殊化と全次数平坦反Serre族は構成済みだが、個々の既存dg特殊化の内在H2認識は、その族ごとに確認する。詳細な主張状態は下の表と研究ノートを正本とする。

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
| noncubic表示商、慣性、μ2² gerbe、good moduli | smooth finite type、dim1。coarse algebraic space不存在。任意内在族の相対正規形は未証明 | `prop:noncubic-presentation-stack`, `prop:noncubic-sign-gerbe`, `prop:noncubic-good-moduli` |
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
| 可換Qの全一次変形の相対H2実現 | Jacobian AS4被覆とZhang補正。任意有限次元二乗零理想へ拡張。内在接dim9、偏極付き接dim15、核dim6 | `thm:quadric-all-first-order-h2`, `cor:quadric-intrinsic-tangent` |
| 選んだSerre根の一次変形障害 | 同じ変形へのR線形dg/Morita持上げにはHH²類の保存が必要。Q上に非保存の例 | `lem:autoequivalence-deformation-obstruction`, `prop:chosen-root-does-not-lift` |

最後の障害例は、選んだ根の持上げを否定するものであり、相対H2 locusの非開性、別の根の非存在、全H2の相対moduliの非存在を主張しない。全H2の相対moduliの代数性を証明済みとは扱わない。

原稿の生成・検算・組版の実施状況は [研究ノートの検証範囲](notes/research_notes.md#検証範囲と再現手順) に記す。全同値類の分類、全幾何点groupoidの実現と実現集合の誘導位相での成分数は確立した。内在的な相対fppf stackは定義・構成した。その有限型代数性は成立した。foundation表示の誘導位相との比較は別に残る。

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

現在はこの同値類分類を、非被約底も含む族と自己同値を保持するスタックへ拡張する。反Serre環の全次数は二次関係から復元でき、noncubic六係数は固定Grassmann affine cellへ局所閉埋込みとなり、全実現点は構成可能な集合として既約包絡[Z2/PGL9]に含まれる。noncubicでは表示商と全幾何点慣性を構成した。finite foundationの開部分F0上ではruling交換を相対的に構成し、coherentなS2商Q_fndを得た。全H2(k)はそのfull subgroupoidとして実現され、全pointed自己同値も捉える。F0→Q_fndは実際に有限étale二重被覆であるが、これを任意の内在的H2族のruling被覆と同定する相対認識は残る。H2実現集合はcubic非空開を含むため誘導位相で既約であり、各noncubic点へのcubicからのpointed smooth proper dg特殊化を構成した。さらに各特殊化について反Serre軌道のperfect複体が次数零の局所自由環に集中し、`[Gr(56,81)/PGL9]` への実際の曲線が得られる。全foundation変形に相対平方根・AS被覆が存在するとは主張しない。

公表前の包括的な先行研究比較と第三者による証明レビューも必要である。既知のVdB分類、PresottoのZ-domain、MCM・helix・AS双対性、関係式stackと変形比較を本研究の新しい成果とはしない。一般の自己同値・根・ambient忘却ファイバーやcubic同値の幾何的簡約も、必要な範囲で扱う。

固定Sklyanin pencilの高々64候補への簡約にはΔの単射性が残るが、その補集合は主定理の四生成判定で既に扱う。Δの全域解析は判定の簡約という別の課題である。可換点の四根とOkawa–Uedaの次数四射の一致も先取りしない。

**楕円型の全O標識と有限・無限の忘却。** 滑らかな楕円四つ組でδ≠0、η∉Zδなら、RTと対角根から全Z²のrank-one torsion-free exceptional対象を構成し、数値類ごとの一意性で全てを尽くす。全てがH2の構造対象となる。Uₙ=(E,L₀,L₁⊗(L₂L₀⁻¹)ⁿ,L₂)を代表とし、εδ=δかつε(η+nδ)∈{η+mδ,2δ−η−mδ}という有限楕円自己同型群を含む必要十分条件でpointed重複を判定する。δ非捩れなら可算無限、位数rならZ/rZの有限商となる。余分な自己同型がなく2η∉⟨δ⟩なら正確にr個。証明は `thm:elliptic-marking-lattice-fiber`、`cor:elliptic-torsion-fiber-cardinality`。Z²と二面体作用はKitamura–Okawaの既存announcementと重なるため新規性を主張せず、ここでは指定範囲の独立証明と明示的な忘却判定を与える。η∈Zδ、退化曲線、noncubicの忘却と相対stack射は未解決。

## 6. 次の実行単位

1. **有限型atlasの公表前監査を仕上げる。** `noncubic_finite_type.tex` の有限LG条件→全fiber認識→全軌道→Noetherian貼合せ→中央AS4被覆の依存を点検する。特に閉基底上のnormal foundationの相対tilting、右軌道積、同じ根との比較を保つ。`h2_smooth_atlas.tex` の指定Artin同型と有限部分被覆を点検する。新規性は既知のVdB・DDL・PP・Stacksの入力と分けて調査する。
2. **内在的な境界と成分を記述する。** 既存cubic表示の既約な有限型基底からH2への実際の相対射を確認し、noncubic atlasのcubic開との接続から既約性を検討する。foundationの誘導位相だけで結論しない。次にQ_fndとの相対比較に必要なrulingの降下を切り分ける。
3. **framed実現像の局所幾何を調べる。** X_asはsmooth83次元スキームで、一致根対ではX3の接次元84との相違がある。`cor:artin-polarization-retraction` の余分なHH¹方向を用い、局所閉性や具体的な偏極認識方程式を調べる。開性を目標にしない。

全スキーム上の商[U/R]は元の有限型site上のH2を延長する。任意Noetherian基底で同じAbel公理を課した関手との一致、および一般のcanonical非有界導来圏の大域descentは別に確認する。

体上の分類、全Artin形式認識、局所環上の効果性、有限型効果性を未解決へ戻さない。cubic有限同値判定の簡約、一般GL4判定solver、全根・全ambientの列挙、外部査読・形式証明は独立の後続課題である。

## 7. 正本・依存関係・再開

- 主論文：[papers/nc-quadric-classification.tex](papers/nc-quadric-classification.tex)。全H2のpointed分類と相対認識。
- 別稿：[papers/quiver-avatar-moduli.tex](papers/quiver-avatar-moduli.tex)。八・十・十二本矢の表示モジュライ、反標準avatar、内在的忘却。主論文の分類証明を重複させない。
- 別稿の組版：`python3 scripts/check.py build --manuscript papers/quiver-avatar-moduli.tex`。同じ指定で `sources` も実行できる。
- 現行知識・障害・再現：[notes/research_notes.md](notes/research_notes.md)。文献仮定・版・リンク：[notes/literature.md](notes/literature.md)、書誌：[papers/references.bib](papers/references.bib)。
- 計算：[computations/verify_quadric.py](computations/verify_quadric.py)。`python3 -m pip install -r requirements.txt` 後、repoルートで `python3 computations/verify_quadric.py`。
- Cloudの導入と検証：[CLOUD_CODEX.md](CLOUD_CODEX.md)、`bash scripts/bootstrap.sh`、`python3 scripts/check.py doctor`。構成・検算・組版を個別に実行でき、欠落依存が独立な数学作業を止めないようにする。
- 組版：repoルートで `latexmk`。PDFとSyncTeXは`build/`。LuaTeX-jaを含むTeX Live/MacTeX、latexmk、BibTeXが必要。VS Codeはrepo全体を開いてLaTeX Workshopの既定レシピを使う。
- cubic側の定義比較は `nc-cubic-classification` のcommit `5393766744bdae887a374b6853ff4daf53d971b5`、`papers/nc-cubic-classification.tex` のrank定義・`def:14641-intrinsic` を確認した。その完全分類定理は本研究の入力にしていない。
- `categorical-fano-index` はSerre根一般の関連研究。現時点で同repoの未確認結果を輸入していない。既知quadric文献を優先する。
- GitHub更新には対象repo・research-hubそれぞれの書込み権限が必要。前の実行で使えた認証や接続が次のCloud taskにもあるとは仮定せず、読取と書込を別に確認する。研究資料の再開に会話履歴は不要。
