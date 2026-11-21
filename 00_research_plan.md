# 研究方針：O-marked 非可換二次曲面の分類

2026-11-21 / v0.13。**再開時は本書を最初に読む。GitHub `main` が正本。** 主論文はv1.13、別稿はv0.1。体上の全同値類分類と、内在的な相対モジュライの代数性を区別する。

**最優先目標は、Oのみを構造として指定する内在的な相対モジュライ $\mathfrak H_2$ の代数性を証明することである。** 平方根・根同型・AS被覆はfppf局所の存在条件とし、標識に加えない。有限型表示商や幾何点の被約閉包を、そのまま内在的モジュライと定義しない。

**有限foundation上の偏極認識。** 有限局所自由代数Λの中心が任意の基底変更後も基底環であり、次数移動と反Serre関手が可逆perfect双加群P,Qで与えられる場合、fppf局所でP≃Qとなる部分層を有限表示局所閉部分スキームとして構成した。RHom(P,Q)の最低次を普遍的な線束にする実際のminor方程式と、評価射のconeが零となる開条件を用いる。比較線束はdegree-line twistを吸収する。これは `papers/sections/polarization_recognition.tex` の定理であり、任意X3族に必要なfoundation・双加群表示を得ることは別問題である。

**現在の到達点。** 標数零の代数閉体k上、局所有限型k-schemeのfppf siteで、Abel圏のmodule-object基底変更・descent、局所canonical compact導来圏・Serre・AZ・相対AS被覆を明記した定義を与えた。体上では既存の $\mathcal H_2$ のpointed groupoidを回復する。反Serre再構成により $\mathfrak H_2\hookrightarrow[X_3/\mathrm{PGL}_9]$ は全忠実で、対角はaffineかつ有限表示。framed実現部分層 $X_{\mathrm{as}}$ は定義され、層として $\mathfrak H_2\simeq[X_{\mathrm{as}}/\mathrm{PGL}_9]$ である。**$X_{\mathrm{as}}$ の有限型代数空間による表現可能性は未証明。** 定義と証明は `papers/sections/relative_moduli.tex`。

**変形に関する確立した入力。** 全H2の切断環と反Serre環はKoszul。PP2005 Chapter 6 Theorem 7.3から、三次まで平坦で全幾何fiberがKoszulなら、非被約Noetherian基底でも全次数平坦・相対Koszul解消を得る。特にH2点の任意のArtin基底上のX3変形は全次数平坦で左右noetherian、qgrはflatなpointed Abel変形となる。既存の横断2/2/3方向の二次jetにも適用できる。`papers/sections/relative_koszul.tex`。

**Artin変形の内在的再構成。** De Deken–Lowenの仮定を確認し、全flat Abel変形にrank24の有限foundationを持ち上げた。特殊fiberで完全なMorita自己同値は、冪零フィルターにより変形heartでも完全。canonical反Serre関手とAZ軌道環が存在し、偏極忘却は右逆を持つ。接空間の分裂完全列は0→HH¹(Λ)→T[X3/PGL9]→HH²(Λ)→0。Abel変形はHH³(Λ)=0により無障害で、二根対一致点の余分な一次元はZhang方向である。HH¹(Λ)=0なら全Artin X3変形はcanonical偏極を持つ。異なる二根対のnoncubic点ではX3が滑らかで次元83、商が滑らかで次元3となる。`papers/sections/artin_foundation.tex`。

**Serre平方根の持上げと一意性。** 近恒等Morita群はnilpotent Lie代数のBCH群なので一意に2可除である。underlying自己同値が持ち上がれば平方関係を補正できる。small extensionで根の障害bはb+s_*b=0を満たすため、s_*がHH²上恒等なら全Artin段階へ持ち上がる。HH¹上の作用も恒等なら、先頭導分の次数商による帰納法で根のMorita同型類は一意となる。可換Qのtensor O(1,1)は両条件を満たす。平方との同型の選択まで一意という主張ではない。四根の一次固定次元は9,3,5,3。一般のH2点での根存在は未解決。`papers/sections/artin_roots.tex`、`cor:quadric-root-unique-all-artin`。

**可換点の一次変形の相対H2実現。** q=x₀x₃−x₁x₂ と f∈k[x₀,…,x₃]₂/kq に対し、Jacobian二重導分γ_fによる積 ab+εγ_f(a,b)/2 を構成する。全次数PBW、中心正則q、相対AS4双対を証明し、局所Ore計算でAbel変形のHH²類を同定した。平方関係の近恒等補正はZhang twistとして被覆にも作用する。全軌道との一致とArtin表示の昇格命題を合わせ、可換Qの全九次元の一次Abel変形は実際の相対H2対象になる。これは一次方向の明示構成として保持する。`papers/sections/quadric_first_order.tex`。

**可換点の全Artin相対H2実現。** 全flat pointed Abel Artin変形に標準根を持ち上げ、二周期cubic列のcanonical hullからその全軌道環の相対AS4被覆と正則正規二次切断を構成した。Artin witnessの昇格により、全有限型基底変更を備えた実際の相対H2対象を得る。忘却はQを中心とする形式変形groupoidの同値で、HH³=0から無障害、接次元9・無限小自己同型次元6となる。大域的な形式商表示や代数性はこの定理から結論しない。`sec:quadric-artin-hull`、`thm:quadric-all-artin-h2`、`cor:quadric-formal-deformation-equivalence`。

**標準Morita根の有限型代数化。** TV2007の一般基礎環上の自己同値モジュライを用い、有限foundation表示上の根空間Zを局所有限表示の代数空間として構成した。可換Qの標準根の全Artin存在・一意性によりZ→Sはその点でétaleであり、gerbeと比較線束の自明化後に実際のperfect根と平方同型を得る。Abel heart・AZはこの命題の結論に含まれない。`prop:quadric-etale-morita-root`。

**有限型étale近傍の四項窓。** 可換Qの標準Morita根を代数化した近傍では、相対perfect Homの最低次数の消去とperfect Nakayamaにより、根がfoundationの最初の二対象を次の二対象へ送ることを局所的に同定した。Serre rotationを併用し、全ての連続四項は任意基底変更でfull strong exceptional。距離1–4のHomは階数2/4/6/9、三次関係は階数2、四次重なりは非退化な階数1の線束となる。全整数の有限窓を二つのparityの有限条件で制御する。**全距離のHom・無限三次提示・相対tails・AZは未証明**。`prop:quadric-etale-finite-window`。

**Artin表示から相対族への昇格。** exactなSerre根と全軌道環の相対AS4被覆がArtin基底上に与えられれば、全有限型A-代数へのmodule-object基底変更でrelative_h2の全条件を満たす。nilpotent base上のhelix持上げとEndの基底変更からcanonical compact圏を比較する。根・被覆の存在そのものはこの命題の仮定である。`prop:artin-witness-relative-promotion`。

**残る条件を分離する明示例。** 二根対一致点の反Serre環Rを、u↦qu, v↦q⁻¹v, c,d固定でZhang twistすると、pointed qgrが一定のGm族を得る。しかしq=2はどのH2のcanonical反Serre環でもなく、一次方向も非零HH²類となる。従って全次数平坦性・Abel heartだけでは反Serre認識はできない。`papers/sections/antiserre_polarization.tex`。

**固定平方根に対する被覆。** 相対軌道環Bが与えられれば、AS4被覆を選ぶ空間はGr(6,K)内の有限表示局所閉incidenceになる。元の環は四次まで、二次双対は五次までで判定できる。任意底変更のnoetherian性はB_Tの仮定と区別する。有限型incidenceのfppf像は一般には代数空間でなく、これだけでH2の代数性は従わない。`papers/sections/relative_as_cover.tex`。

**既存の幾何入力。** 体上の全同値類分類、foundation商、cubic開部分、noncubic表示商を保持する。実現幾何点集合はfoundationからの誘導位相で既約・連結各1。各noncubic点へのcubic特殊化はsmooth proper dg族と全次数平坦な反Serre環族で構成済みだが、相対H2の全条件と位相比較は未完成である。

**矢数と avatar の比較。** 別稿 `papers/quiver-avatar-moduli.tex` に、有限foundationの結合律スキームと二つの10本矢開部分、重み四QPの消去と残存慣性、反標準avatarの相対再埋め込みと4層をまとめた。全square曲線型は一方の非最小10本矢chartに対応し、8本矢はその開部分。$\Sigma_2$ で負断面を避ける場合は10本矢、含む場合は最深12本矢である。相対heart・根・AS4被覆を満たす部分から内在的忘却があるが、その部分の開性は未証明。重み付き射影stackの古典12本矢点は強いH2に入らない。有限代数の開性、幾何的avatarの開性、相対AS分類、内在的認識を別々に扱う。

検証状態は [研究ノート](notes/research_notes.md#検証範囲と再現手順) に集約する。新しい局所定義のdescendableなglobal compact圏との比較を、定義の局所条件やfppf stack性の証明と混同しない。

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
| Artin witnessの相対H2族への昇格 | 根と全軌道AS4被覆が入力。全有限型基底変更のcompact/Serre/AZ/被覆を確認 | `prop:artin-witness-relative-promotion` |
| 可換Qの標準Serre根の全Artin存在・一意性 | HH²・HH¹への作用が恒等。exact ampleな根のMorita同型類が一意 | `cor:quadric-exact-root-all-artin`, `cor:quadric-root-unique-all-artin` |
| 可換Qの全Artin変形の相対H2実現と形式変形同値 | 二周期canonical hullによる相対AS4切断と昇格。無障害、接9・無限小自己同型6 | `thm:quadric-all-artin-h2`, `cor:quadric-formal-deformation-equivalence` |
| cubic点の条件付き全Artin認識 | ample cubic helixと適合根のHH²自明作用を仮定。一般点でこの根が存在する範囲は未確定 | `prop:cubic-artin-hhtrivial-conditional` |
| 可換Qの全一次変形の相対H2実現 | Jacobian AS4被覆とZhang補正。任意有限次元二乗零理想へ拡張。内在接dim9、偏極付き接dim15、核dim6 | `thm:quadric-all-first-order-h2`, `cor:quadric-intrinsic-tangent` |
| 選んだSerre根の一次変形障害 | 同じ変形へのR線形dg/Morita持上げにはHH²類の保存が必要。Q上に非保存の例 | `lem:autoequivalence-deformation-obstruction`, `prop:chosen-root-does-not-lift` |

最後の障害例は、選んだ根の持上げを否定するものであり、相対H2 locusの非開性、別の根の非存在、全H2の相対moduliの非存在を主張しない。全H2の相対moduliの代数性を証明済みとは扱わない。

原稿の生成・検算・組版の実施状況は [研究ノートの検証範囲](notes/research_notes.md#検証範囲と再現手順) に記す。全同値類の分類、全幾何点groupoidの実現と実現集合の誘導位相での成分数は確立した。内在的な相対fppf stackは定義・構成した。その代数性と、位相がこの誘導位相に一致することは未完成である。

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
| F6 証明と再現 | 主定理から入力補題まで依存を閉じ、一次文献の仮定・規約を確認し、必要な厳密計算・組版・独立点検を終えて現行一式とhubを保存する | 体上の分類と主要な表示・特殊化の証明は独立読取り済み。現行版の参照確認、公開計算コードの実行、組版・画像確認の実施範囲は研究ノートの現行検証節に集約する。内在的相対H2の代数性と表示族の認識は未証明。repoとhubの保存は個別に確認する |

F1–F6が揃うまでは「完全分類」と報告しない。条件付きの還元、一般点の分類、例の族、有限次数のincidence、既存の非標識分類だけでは完了しない。原稿に未証明の核心命題が残っていないことを、異なる観点または独立担当で確認する。checkスクリプトはこの数学的達成を判定しない。

自己同値群・groupoid・相対モジュライを主張する場合は、それに対応する全忠実性、自然同型、降下・底変更・代数性を別途証明する。次数スカラー等の核を調べずに反Serre環のgraded自己同型群とpointed自己同値群を同一視しない。GIT商のorbit closure・S-equivalenceがpointed exact同値と一致するかも別途確認する。これらは重要な後続目標だが、対象のpointed exact同値類の完全分類と混同しない。全ambientや全平方根の個別分類を不必要な終了条件にしない。

## 5. 現在の結論と後続の研究目標

全H2の対象同値類は二領域の非交和として分類した。cubic側はlinearデータと全許容四つ組であり、R0⊗V3+V0⊗R1を二周期で移した七次元関係Kから、二つのGL4行列のtransporterとその有限反復で同値を判定する。noncubic側は中央二重平方環であり、根対の配置が完全不変量である。全ての平方根やambientを列挙する必要はなかった。

cubicの四つ組同型だけでは、平方根・ruling・foundationを忘れたpointed同値を数え切れないため、最初の軌道対象の内在性に基づく有限判定を最終仕様に採用した。これは具体的な必要十分条件で、未知の圏同値や未知のAS条件を言い換えただけではない。抽象的な基礎体上では有限代数的判定であり、機械実行には係数体の有効な表示を要する。

現在はこの同値類分類を、非被約底も含む族と自己同値を保持するスタックへ拡張する。反Serre環の全次数は二次関係から復元でき、noncubic六係数は固定Grassmann affine cellへ局所閉埋込みとなり、全実現点は構成可能な集合として既約包絡[Z2/PGL9]に含まれる。noncubicでは表示商と全幾何点慣性を構成した。finite foundationの開部分F0上ではruling交換を相対的に構成し、coherentなS2商Q_fndを得た。全H2(k)はそのfull subgroupoidとして実現され、全pointed自己同値も捉える。F0→Q_fndは実際に有限étale二重被覆であるが、これを任意の内在的H2族のruling被覆と同定する相対認識は残る。H2実現集合はcubic非空開を含むため誘導位相で既約であり、各noncubic点へのcubicからのpointed smooth proper dg特殊化を構成した。さらに各特殊化について反Serre軌道のperfect複体が次数零の局所自由環に集中し、`[Gr(56,81)/PGL9]` への実際の曲線が得られる。全foundation変形に相対平方根・AS被覆が存在するとは主張しない。

公表前の包括的な先行研究比較と第三者による証明レビューも必要である。既知のVdB分類、PresottoのZ-domain、MCM・helix・AS双対性、関係式stackと変形比較を本研究の新しい成果とはしない。一般の自己同値・根・ambient忘却ファイバーやcubic同値の幾何的簡約も、必要な範囲で扱う。

固定Sklyanin pencilの高々64候補への簡約にはΔの単射性が残るが、その補集合は主定理の四生成判定で既に扱う。Δの全域解析は判定の簡約という別の課題である。可換点の四根とOkawa–Uedaの次数四射の一致も先取りしない。

## 6. 次の実行単位

1. **Artinで得た有限foundationを一般の相対族へ広げる。** `artin_foundation.tex` により全flat Abel Artin変形のfoundation・完全なcanonical反Serre・AZ・全軌道と偏極忘却の分裂は成立した。`polarization_recognition.tex` の有限表示局所閉条件を適用するため、任意有限型基底の族にfoundationとshift双加群を与える。実際のArtin root/AS witnessを全有限型A-代数上のrelative_h2系へ延長する命題は成立した。可換点では `prop:quadric-etale-morita-root` がfoundation表示のétale近傍へMorita根を代数化した。次はこの有限窓tensorを全距離に延ばし、相対cubic Z-代数の三次提示と無限次数の分裂完全な標準解消を証明する。その後tails heartを実現し、全有限型基底変更後のnoetherian性、canonical導来比較、AZを示す。四項窓のfull strong tilting性とEnd=Λはétale近傍で既に得たが、tailsのcanonical heartが一致することは依然として未証明である。非平坦底変更では、単にheartが同じという理由でcanonical導来基底変更を仮定しない。
2. **全Artin hullを一般点と有限型近傍へ拡張する。** 可換Qでは全Artin段階の標準根とAS4被覆、形式変形groupoidの同値は解決した。`prop:cubic-artin-hhtrivial-conditional` により、適合するample cubic helixとHH²に恒等に作用する根があれば一般cubic点でも全Artin認識が成立する。次はその根のHochschild作用を計算し、存在範囲を確定する。helix対象ごとの二周期性から作用の恒等性は従わない（Q上の一因子対合の根が反例）。noncubicの階数3境界で失われるcubic入力も特定する。有限型近傍への代数化・効果性と `relative_as_cover.tex` のincidenceの局所存在を比較する。根は標識でなく、選んだ根の非持上げと全ての根の非存在を区別する。形式的な無障害性や有限型射のfppf像だけで大域代数性を結論しない。
3. **階数3境界の相対正規形を閉じる。** 全H2の二ruling、有限foundation、相対S2交換を入力に、noncubic境界の内在族から局所モデルへ移ることを証明する。既存のcubic→全noncubic特殊化を相対H2族として認識できれば、成分問題の位相比較にも進める。
4. **avatarと相対AS代数の比較を閉じる。** 別稿の $H\mapsto HP^n$ は幾何的stackの自己同値として証明済み。次はavatarからの有限foundationと全周期AS代数を相対的に構成し、底変更と同型層を比較する。元のproduct QP、weighted12本矢、固定構造対象の移動を区別する。$P=\mathcal O_D$ の古典点への収縮は同型類の説明だけでは足りない。内在的忘却に進むときは重み付き古典点の反例を基準にする。
5. **必要な変形計算を選ぶ。** 三次平坦性から全次数平坦性は解決済みなので、次数4のHilbert条件を独立の追加制約として再計算しない。既存の横断二次jetはflat Abel変形になる。高次障害計算をする場合は、canonical偏極・根・被覆のどの残存条件を検証するかを先に明示する。

有限型基底上での代数的表現の目標は、$X_{\mathrm{as}}$ を有限型代数空間として表すことである。局所閉部分スキームとしての構成は十分条件だが必要条件とは主張しない。一般Noetherian基底への連続拡張・極限保存性と、貼り合わせた局所compact圏が大域のcanonical $D(\operatorname{Ind}\mathcal C)^c$ に一致することは別に確認する。

既存のC⊔Npresは全幾何点と慣性の表示であって、型間の特殊化を持たない。Z2は既約な被約閉包であって、相対実現部分層とは別物である。det(R1)⁻¹¹det(R2)²によるdegree gerbeの中立化、両chartの反Serre環の降下、Artin基底上のnoetherian heartは解決済みの入力として用いる。

公表前の包括的な先行研究比較、cubicの有限同値判定の幾何的簡約、一般GL4判定solverの実装、外部査読・形式証明は別課題である。De Deken–Lowenのhelix変形比較やToën–Vaquiéの固定圏の対象moduliを、全H2の代数性として流用しない。Ore変形ノートは相対認識を試す追加候補であり、未証明の相対CY・Serre条件を入力には使わない。

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
