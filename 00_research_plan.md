# 研究方針：O-marked 非可換二次曲面の分類

2026-11-21 / v0.8。**再開時は本書を最初に読む。GitHub `main` が正本。** 数学原稿はv1.7。全同値類の分類定理の証明を統合し、独立数学点検を完了した。

**最優先目標は内在的相対モジュライ $\mathfrak H_2$ の具体的な有限型商表示と、全pointed exact同値・降下・相対再構成を証明することである。** 現行の $\mathcal H_2$ の体上分類は完成済みだが、$\mathfrak H_2$ は未構成であり、foundation表示 $\mathfrak Q_{\mathrm{fnd}}$ や関係式の閉包 $\mathfrak Z_2$ と同一視しない。cubic の比較例は、指定された相対条件付きの $\mathfrak H_3=[X^{\mathrm{H3}}/\mathrm{PGL}_4]$ である。

**今回の到達点：** 反Serre環の偶数Veroneseに対して任意の基底上の二次提示を直接証明し、全 $\mathcal H_2$ 対象・cubic/noncubic両chart・各noncubic点への平坦な特殊化族で、九生成元・五十六二次関係から**全次数**を復元できるようにした。noncubicの二形式六係数は、九生成元の積から常に単位となる25個のminorを使い、Grassmannianの固定affine cellへ多項式的に**局所閉埋込み**となる。六係数の回収式を直接示し、厳密検算を追加。cubicの関係式像の被約既約閉包 $Z_2$ を取り、有限型Artin商 $[Z_2/\mathrm{PGL}_9]$ を構成した。幾何点の全H2実現集合はこの中で構成可能であり、cubicが稠密、noncubic全点はその閉包に入る。以前のnoncubic中心Clifford・相対Serre・相対qgr heartの結果を保持する。

**今回の接空間検算と証明：** noncubicの二形式六係数が固定Grassmann cellに閉埋込みとなることを使い、PGL9の80次元Lie作用と六係数の接像を比較した。非交差基準点・一根共有点・二根対一致点で、両者の和は標数零で正確に81次元（軌道次元は80,80,79、交わりは5,5,4）。三次Hilbert階数49の条件は $L_J:V\otimes J\to(V^{\otimes2}/J)\otimes V$ のrank176であり、kernel328/cokernel49の線形化を1400変数・16072行として法101で全行検証した。その条件の接次元は法101で83,83,84。さらに法101の核83,83,84本を分母2以下の有理数へ復元し、整数係数の全線形化行列に対する零性と独立性を確認した。従って標数零でも接次元は**正確に**83,83,84である。三次Hilbert条件の接空間を既知の81方向で割った商は正確に2,2,3次元。ただしこれらは相対H2の実変形と同一視していない。これは内在的H2の接空間ではなく、三次Hilbert条件のdeterminantal locusについての結果である。証明・計算は prop:noncubic-third-degree-tangent と computations/verify_noncubic_degree3_tangent.py（numpy・numbaを用いるオプション検証）を参照する。

**Koszul 理論と二次持上げの進展：** noncubic の二重平方環は中央二変数と二乗関係の二次 Gröbner 基底を持つため Koszul であり、偶数 Veronese と Zhang twist による反Serre環も Koszul。Koszul 双加群解消から、三次Hilbert条件を満たす一次二次関係変形は、双対数上で**全次数平坦**な次数付き代数変形となる。これにより三基準点の内部次数零 Hochschild コホモロジーを $HH^1=(1,1,2)$、$HH^2=(3,3,5)$ と決定した。さらに三次条件の横断接空間 $2,2,3$ の基底および各基底二項和について、二次Schur complement障害に対する厳密な有理数補正を構成。したがって各横断方向は $k[t]/(t^3)$ 上で三次Hilbert階数49を保って持ち上がる。今回の厳密な同等ローカル計算は、法101の候補を有理数・整数へ復元し、整数係数の線形化行列で零性を全検査した。GitHub の再現スクリプト computations/verify_noncubic_second_order.py は追加したが、その公開版を別環境で実行したとは報告しない。**内在的H2の平坦Abel変形とこれらの次数付き代数変形の同一視、三次以上の障害、全相対moduliの構成は未完成。**

**定義を弱めて証明済みのモジュライ表示（v1.7）：** (1) 型を基底上で局所定数とした表示族の非交和
$\mathfrak H_2^{\mathrm{split,pres}}=\mathfrak C\amalg\mathfrak N^{\mathrm{pres}}$
は有限型 Artin スタックで、全 $\mathcal H_2$ の幾何点・pointed 慣性と一致する。ただし二既約・連結成分となりcubic→noncubic退化を除外する。(2) 普遍関係 $J\subset U^{\otimes2}$（rank56、$\dim U=9$）の三次関係行列 $L_3:U\otimes J\to (U^{\otimes2}/J)\otimes U$ の正確なrank176を課す局所閉スキーム $X_3\subset\operatorname{Gr}(56,81)$ とその商 $\mathfrak H_2^{(3),\mathrm{pres}}=[X_3/\operatorname{PGL}_9]$ は、rank R2=25、rank R3=49の二次提示族の真正な有限型 Artin モジュライである。度数スカラーgerbeは重み一の $\det(R_1)^{-11}\det(R_2)^2$ で中立化され、普遍次数付き環も存在。cubic/noncubicの両相対反Serrechartと既知の退化族がそこへ入るが、高次 Hilbert・相対H2の条件を課さず余分な点・変形を持つ。**二根対一致点では** $T_x\mathfrak H_2^{(3),\mathrm{pres}}$ の同型類の次元は5、滑らかな $\mathfrak Q_{\mathrm{fnd}}$ では4なので形式近傍も非同値。証明は prop:split-h2-presentation-moduli, prop:truncated-antiserre-moduli-stack, prop:truncated-versus-foundation-tangent。これらを無条件の内在的 $\mathfrak H_2$ の構成と記載しない。

**未解決の核心：** $Z_2$ にはH2でない点が混入し得る。相対H2のheart・全flat coherent対象のSerre双対・AZ豊富性・AS正則被覆の存在、任意の内在的族の局所正規形、およびcubic/noncubic chartの相対全忠実性・貼合せ・有限表示を証明する。これらを閉包の構成や体上の関係式判定で代用しない。相対moduli自身の既約成分数も未確定である。詳細は第3・5・6節、証明は主原稿、検算は研究ノートを正本とする。

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
| 選んだSerre根の一次変形障害 | 同じ変形へのR線形dg/Morita持上げにはHH²類の保存が必要。Q上に非保存の例 | `lem:autoequivalence-deformation-obstruction`, `prop:chosen-root-does-not-lift` |

最後の障害例は、選んだ根の持上げを否定するものであり、相対H2 locusの非開性、別の根の非存在、全H2の相対moduliの非存在を主張しない。全H2の相対moduliを証明済みとは扱わない。

原稿の生成・検算・組版の実施状況は [研究ノートの検証範囲](notes/research_notes.md#検証範囲と再現手順) に記す。全同値類の分類、全幾何点groupoidの実現と実現集合の誘導位相での成分数は確立した。内在的な相対モジュライの構成とその位相がこの誘導位相に一致することは、別の未完成な比較問題である。

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
| F6 証明と再現 | 主定理から入力補題まで依存を閉じ、一次文献の仮定・規約を確認し、必要な厳密計算・組版・独立点検を終えて現行一式とhubを保存する | 体上の分類定理、スタック拡張、cubic開部分の稠密性・特殊化・相対smooth proper性の主要証明を独立点検した。現行v1.2の構成確認・97頁LuaLaTeX組版はPASS。変更のない計算資産の同日厳密検算PASSを保持する。内在的な相対H2モジュライとの同定は未証明。現行一式をmainへ保存し、その内容をhubへ反映する運用は継続。保存成功はそれぞれの操作結果で別に確認する |

F1–F6が揃うまでは「完全分類」と報告しない。条件付きの還元、一般点の分類、例の族、有限次数のincidence、既存の非標識分類だけでは完了しない。原稿に未証明の核心命題が残っていないことを、異なる観点または独立担当で確認する。checkスクリプトはこの数学的達成を判定しない。

自己同値群・groupoid・相対モジュライを主張する場合は、それに対応する全忠実性、自然同型、降下・底変更・代数性を別途証明する。次数スカラー等の核を調べずに反Serre環のgraded自己同型群とpointed自己同値群を同一視しない。GIT商のorbit closure・S-equivalenceがpointed exact同値と一致するかも別途確認する。これらは重要な後続目標だが、対象のpointed exact同値類の完全分類と混同しない。全ambientや全平方根の個別分類を不必要な終了条件にしない。

## 5. 現在の結論と後続の研究目標

全H2の対象同値類は二領域の非交和として分類した。cubic側はlinearデータと全許容四つ組であり、R0⊗V3+V0⊗R1を二周期で移した七次元関係Kから、二つのGL4行列のtransporterとその有限反復で同値を判定する。noncubic側は中央二重平方環であり、根対の配置が完全不変量である。全ての平方根やambientを列挙する必要はなかった。

cubicの四つ組同型だけでは、平方根・ruling・foundationを忘れたpointed同値を数え切れないため、最初の軌道対象の内在性に基づく有限判定を最終仕様に採用した。これは具体的な必要十分条件で、未知の圏同値や未知のAS条件を言い換えただけではない。抽象的な基礎体上では有限代数的判定であり、機械実行には係数体の有効な表示を要する。

現在はこの同値類分類を、非被約底も含む族と自己同値を保持するスタックへ拡張する。反Serre環の全次数は二次関係から復元でき、noncubic六係数は固定Grassmann affine cellへ局所閉埋込みとなり、全実現点は構成可能な集合として既約包絡[Z2/PGL9]に含まれる。noncubicでは表示商と全幾何点慣性を構成した。finite foundationの開部分F0上ではruling交換を相対的に構成し、coherentなS2商Q_fndを得た。全H2(k)はそのfull subgroupoidとして実現され、全pointed自己同値も捉える。F0→Q_fndは実際に有限étale二重被覆であるが、これを任意の内在的H2族のruling被覆と同定する相対認識は残る。H2実現集合はcubic非空開を含むため誘導位相で既約であり、各noncubic点へのcubicからのpointed smooth proper dg特殊化を構成した。さらに各特殊化について反Serre軌道のperfect複体が次数零の局所自由環に集中し、`[Gr(56,81)/PGL9]` への実際の曲線が得られる。全foundation変形に相対平方根・AS被覆が存在するとは主張しない。

公表前の包括的な先行研究比較と第三者による証明レビューも必要である。既知のVdB分類、PresottoのZ-domain、MCM・helix・AS双対性、関係式stackと変形比較を本研究の新しい成果とはしない。一般の自己同値・根・ambient忘却ファイバーやcubic同値の幾何的簡約も、必要な範囲で扱う。

固定Sklyanin pencilの高々64候補への簡約にはΔの単射性が残るが、その補集合は主定理の四生成判定で既に扱う。Δの全域解析は判定の簡約という別の課題である。可換点の四根とOkawa–Uedaの次数四射の一致も先取りしない。

## 6. 次の実行単位

**本命の表示を明確化：** $X_3$ は三次までの局所閉rank-stratumであり、既約閉包 $Z_2$ とは異なる代数的環境である。最終的に目指すのは、$\HH$ の相対認識条件を与える有限表示の $X_{\mathrm{as}}\subset X_3$ を構成し、$\mathfrak H_2\simeq[X_{\mathrm{as}}/\operatorname{PGL}_9]$ を証明すること（必要なら代わりに $\mathfrak Q_{\mathrm{fnd}}$ 内の適切な相対部分関手と同定する）。局所定数型の非交和は幾何点と慣性の保全用で、最終の貼合せには用いない。特に二根対一致点でX3にはQ_fndより一つ余計な一次方向があるので、これを切る高次条件か内在的条件を検出することを優先する。

**直近の具体的P0：** 三次の接空間計算（標数零で83,83,84）、Koszul 性と一次全次数平坦性、さらに横断2,2,3方向の三次Hilbert条件の二次持上げは完成。**次数4の一次平坦性を別途独立の必要条件として再計算しない。** 次に（a）横断2,2,3方向の三次以上の持上げ障害を Schur complement で求め、特に二根対一致点の余分な法方向が実際の基底上の代数変形へ積分するか判定し、（b）foundation の実際のsmooth proper/反Serre環変形から得られる接像と照合し、（c）相対 qgr heart・Serre平方根・AZ豊富性・AS被覆の存在および非被約底での局所正規形の認識を証明する。完全な局所構成が困難なら、既存の Koszul deformation principle の Artin 小拡大版を一次資料に即して検証し、今回の2-jetが全次数平坦となる適用範囲を明確にする。

**内在的な相対H2実現locusの有限表示と相対heart/AZ再構成を第一課題とする。** 共通反Serre環の全次数は既に二次提示で決まるので、今後は二次関係だけで表現できない条件（flat coherent heart・Serre・AZ・AS被覆・降下）に証明資源を集中する。 noncubic 表示上の `qgr R` heart の構成と `Perf` 上の相対Serreは既に得たので、これらを再び無条件の未解決問題に戻さない。次は全flat coherent対象の相対双対・AZ/AS条件および任意の内在的族の相対正規形を明示する。 出発点は `papers/sections/foundation_stack.tex` のQ_fndである。ruling交換とS2の整合性、有限étale二重被覆、cubicのgeometric開部分 `[Gr(2,8)_geo/(PGL2)^3]`、実現集合の誘導位相での既約性と全noncubic点へのdg特殊化は構成済みなので再び未解決課題に戻さない。cubic・noncubic の双方で相対反Serre環のGrassmann射を構成済みなので、次に両射とfoundation特殊化に一致する有限表示の反Serre実現locusを同定する。特にH2のheart・Serre根・AS被覆を持つ部分関手を非被約底上でも定義し、有限表示の開または局所閉部分になるかを調べる。体上の分類が与える集合の被約像だけを相対locusと定義して済ませない。

到達基準は次の三点である。

1. **族の対象を明示する。** Oを指定した相対圏の族に対して、適合するsとAS4被覆はfppf局所に存在する性質とし、選択を標識へ加えない。全幾何ファイバーがH2という条件との一致は別に検証する。
2. **局所表示と同値を族で認識する。** 内在的M=sOとruling対X,Yの存在・底変更・降下、相対Serre/AZ再構成、pointed exact同値の相対全忠実性と本質的全射性を証明する。F0上の交換と有限étale二重被覆は入力として使い、任意の内在的族からこの表示へ移れることを別に確認する。
3. **反Serre環を通じて族と位相を比較する。** 構成済みのcubicから全noncubic点への有限自由foundation族と全次数平坦な反Serre環の特殊化を入力として、階数3境界を含む相対heart・根・AZ・AS被覆の認識を閉じる。実現集合の誘導位相ではcubicが稠密で既約成分は一つである。内在的stackの位相との一致を別に示し、点集合のcubic/noncubic非交和を開閉分解と読み替えない。

代替の統一表示は `[X_as/PGL9]`。Z2⊂Gr(56,81)は構成済みの既約な被約閉包、X_asはそのうち実際に相対H2を実現する未構成の有限表示locusである。構成可能な幾何点集合と閉包Z2を、非被約底上のX_asと取り違えない。degree-scalar gerbeのBrauer障害は `det(R1)^−11 det(R2)^2` で解消済みなので、同じ障害を再調査しない。noncubicでは `B_{2n}⊗(det W)^{-n}` と積 `a⋆b=aι^n(b)` により全次数の降下が完成し、cubicでも相対Serreから同じGrassmann商への射が完成した。残るのは両chartの相対的な貼合せとcanonical内在族との比較であり、既に証明した降下を再度未解決としない。

De Deken–Lowenのhelix変形比較は冪零拡大におけるabelian変形とfoundation代数変形を結ぶが、H2の根・AS被覆条件の相対開性は含まない。可換Q上でも、選んだ根sのHH²作用がuを−uへ送れば、その固定一次変形へsはR線形dg/Morita自己同値として持ち上がらない。これは別の根の存在を排除せず、構成した変形がH2族であるとも主張しないため、H2 locusの非開性を意味しない。Toën–Vaquiéの対象stackも固定dg圏に対する結果である。適用範囲を `notes/literature.md` で確認する。

相対条件の具体的検証には [Ore変形ノート](notes/ore_quadric_deformations.md) の中央正則切断を使える。noncubic表示の中心 Clifford trace により perfect 圏での相対Serre公式は確立したので、次はそれを全coherent heartの相対Serre・AZ・相対AS被覆に拡張する。Ore変形ノートの別族についてはbimodule Koszul複体のexactnessと自己双対性をなお検証する。

先行研究上の新規性比較、一般GL4判定solverの実装、外部査読・形式証明は未完了。主定理に誤りが見つかれば、本文・概要・方針・hubを訂正する。

## 7. 正本・依存関係・再開

- 主論文：[papers/nc-quadric-classification.tex](papers/nc-quadric-classification.tex)。独立した別論文は現時点ではない。
- 現行知識・障害・再現：[notes/research_notes.md](notes/research_notes.md)。文献仮定・版・リンク：[notes/literature.md](notes/literature.md)、書誌：[papers/references.bib](papers/references.bib)。
- 計算：[computations/verify_quadric.py](computations/verify_quadric.py)。`python3 -m pip install -r requirements.txt` 後、repoルートで `python3 computations/verify_quadric.py`。
- Cloudの導入と検証：[CLOUD_CODEX.md](CLOUD_CODEX.md)、`bash scripts/bootstrap.sh`、`python3 scripts/check.py doctor`。構成・検算・組版を個別に実行でき、欠落依存が独立な数学作業を止めないようにする。
- 組版：repoルートで `latexmk`。PDFとSyncTeXは`build/`。LuaTeX-jaを含むTeX Live/MacTeX、latexmk、BibTeXが必要。VS Codeはrepo全体を開いてLaTeX Workshopの既定レシピを使う。
- cubic側の定義比較は `nc-cubic-classification` のcommit `5393766744bdae887a374b6853ff4daf53d971b5`、`papers/nc-cubic-classification.tex` のrank定義・`def:14641-intrinsic` を確認した。その完全分類定理は本研究の入力にしていない。
- `categorical-fano-index` はSerre根一般の関連研究。現時点で同repoの未確認結果を輸入していない。既知quadric文献を優先する。
- GitHub更新には対象repo・research-hubそれぞれの書込み権限が必要。前の実行で使えた認証や接続が次のCloud taskにもあるとは仮定せず、読取と書込を別に確認する。研究資料の再開に会話履歴は不要。
