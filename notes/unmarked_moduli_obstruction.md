# 無標識 Abel 圏のモジュライと対角射の準コンパクト性

2026-11-25 / v1.0。最優先課題の証明アウトライン。研究方針は [00_research_plan.md](../00_research_plan.md)、公表本文の統合先は論文Bの [標識忘却の節](../papers/moduli/marking_forgetting.tex)。

## 目標・現在の状態・終了範囲

**最優先目標は、強い H2 の構造対象を忘れた exact 同値類を正しく表すモジュライについて、対角射が準コンパクトであることへの障害を論文Bで証明することである。** 無標識モジュライ全体を構成することは、この課題の前提でも完了条件でもない。

以下は証明計画であり、最終的な適用定理はまだ原稿化・独立検証されていない。既存の全標識分類・可算無限ファイバー・H2の有限型代数性には原稿上の証明があるが、その必要な依存箇所をこの用途で再点検する。一般論の補題は既知の構成可能性の手法であり、新規性を主張しない。

完成時には「準分離な無標識モジュライの限界」を到達点とする。準分離性を外した商、全無標識2スタック、全退化型の忘却ファイバー、任意raw QPやCY構造の一般化へ研究を拡張することは要求しない。A/B/Cの有効な既存結果と証明を保持する。

## 1. 証明すべき主張を先に固定する

まず非可算な標数零代数閉体 k、特に k=ℂ 上で証明する。候補は通常の代数的 **1-stack** M と射

\[
F:\mathfrak H_2\longrightarrow M
\]

であって、幾何点の同型判定が

\[
F(\mathcal C,\mathcal O)\simeq F(\mathcal C',\mathcal O')
\quad\Longleftrightarrow\quad
\mathcal C\simeq\mathcal C'
\quad\text{（k-linear exact 同値）}
\]

を満たすものとする。証明する結論は、**この F を持つ M の対角射は準コンパクトではない**、従って準分離な M、特に affine diagonal を持つ M は存在しない、という形である。

M 自体や F の有限型性、F の表現可能性・全射性・平滑性は仮定しない。非可算拡大後にも同じ幾何点判定が成立する自然なモジュライ問題については、対角射の準コンパクト性の基底変更安定性から一般の標数零基礎体への系を検討する。ただし現行の局所有限型siteで使う体拡大と、代数スタックとしての基底変更を確認してから述べる。少なくとも ℂ 上の完全な定理を先に閉じる。

構造対象を外すと自然自己同型のscalarが再び現れる。圏・同値・自然同型からなる2圏を、説明なしに通常の1スタックと同一視しない。自然同型で割った射やstackificationを使うならその意味を定義する。主証明には全無標識スタックの構成を使わず、上の F と幾何点判定を候補モジュライに要求する性質として明示すればよい。

## 2. 最短の主証明：有限型atlasと構成可能性

会話での楕円曲線切片の方法に先立ち、こちらを最初に点検する。現行Bの集合論的ファイバーを直接使え、無標識族の大域的構成や2-fiberの記述を追加で要求しない。

### U0. 構成可能集合の可算分割補題

非可算な代数閉体 k 上の有限型スキーム V の構成可能部分集合 S について、S(k) が互いに素な非空の構成可能部分集合の k-点集合の可算和であれば、その分割は有限であることを証明する。

論証の核は次の通り。

1. 既約な有限型多様体の k-点全体は、可算個の真閉部分集合の k-点の和では覆えない。非空affine開とNoether正規化で affine空間へ帰着し、座標の一つを固定する超平面を可算個の禁じられた値から外して選び、次元で帰納する。この短い論証を本文に書く。
2. S を有限個の既約局所閉部分に分ける。各最高次元部分では、可算分割の少なくとも一つが稠密でなければ 1 に反する。
3. 稠密な構成可能集合は非空開集合を含む。最高次元の有限個の部分で選んだ分割片全体を除くと、残りは構成可能で次元が下がる。次元帰納法で有限個の分割片しか残らない。

これは k-点についての主張である。「generic point はどの真閉集合にも入らない」という位相だけの議論で 1 の代用をしない。可算体では成り立たない。

### U1. 同型類ファイバーの一般障害

X を k 上有限型で準コンパクトな対角射を持つ代数スタック、Y を準コンパクトな対角射を持つ任意の代数スタックとする。任意の射 f:X→Y と y∈Y(k) に対し、

\[
\{[x]\in\operatorname{Iso}X(k):f(x)\simeq y\}
\]

は可算無限にはなり得ない、という補題を証明する。空または有限、あるいは非可算である。

**論証案。**

- 有限型スキームによるsmooth全射 atlas p:V→X を一つ取る。Xの有限型性から有限個のaffine chartを選べることを記す。k が代数閉体なので各 k-対象は V の k-点で代表できることも確認する。
- V 上の相対同型空間
  \[
  I_Y=\operatorname{Isom}_Y(f\circ p,y_V)\longrightarrow V
  \]
  を取る。対角射は局所有限型であり、Δ_Y の準コンパクト性を加えると有限型になる。Noetherianな基底 V 上でChevalleyを適用し、その像 S は構成可能。
- 普通の同型類ファイバーが可算無限であると仮定し、代表を x_1,x_2,… とする。各
  \[
  I_i=\operatorname{Isom}_X(p,(x_i)_V)\longrightarrow V
  \]
  も Δ_X の準コンパクト性により有限型であり、その像 S_i は構成可能。
- 非空の有限型 k-代数空間には k-点があるので、S(k) は互いに素な非空の S_i(k) の和である。U0に反する。

両方の対角射の準コンパクト性がどこで使われるかを明記する。Xの有限型性だけで結論しない。Chevalleyには代数空間版を用い、局所有限型から局所有限表示への移行では基底のNoetherian性を使う。

これは **同型類集合上のファイバー** の議論である。X×_Y Spec(k) の同型類や、固定圏上の標識の群oidと同一視する必要はなく、同一視してはならない。

### U2. 現行Bの結果を代入する

X=H2 とする。次を定理と仮定の単位で確認する。

- Bの H2 は有限型で、対角射はaffine有限表示である。有限型atlasと準コンパクト対角という U1 の入力を満たす。
- 滑らかな楕円四つ組で δ≠0、η∉ℤδ、δ非捩れを選ぶ。k=ℂ ならこのような点の存在は容易だが、存在の一文を省かない。
- 固定した underlying 圏 C に対し、許容される O を exact 自己同値で割った **pointed同型類の忘却ファイバー** が可算無限であることを、現行Bの定理から確認する。
- 主張1の F の同型判定により、この集合が Iso H2(k)→Iso M(k) の一つのファイバーに正確に一致する。U1により Δ_M が準コンパクトという仮定と矛盾する。

必要な依存証明を監査するが、A/B/C全体の包括的監査をこの定理完成の前提にしない。既存入力の誤りが見つかった場合は、その依存先と要約も修正し、成立する仮定・範囲を明記する。ここまでで目標定理を証明できれば、次節の別証明の完了を待って公表用統合を遅らせない。

## 3. 補助的な幾何的説明：楕円曲線切片

この方法は対角の障害を具体的に説明するための別証明候補であり、U0–U2で主定理が閉じれば必須ではない。

Eを原点付き楕円曲線とし、Pic⁰(E)≃E と同定する。次数二の L₀ と、非捩れ δ を表す D∈Pic⁰(E) を固定し、L₂=L₀⊗D とする。正規化Poincaré束 P を用いて L₁,η=L₀⊗P_η を動かす。許容な基底は

\[
U=E\setminus\{0,\delta\}
\]

である。現行Bの相対cubic族・Noetherian性・Picard根・相対効果性を用い、実際の h:U→H2 を構成する。根や基底の局所frameは witness とし、標識へ追加しない。根chartが必要なら有限型étale曲線chartまたはその非空開を使い、chartの準有限性と無限軌道が残ることを確認する。全体への降下が主定理に不要なら、それを別の大目標にしない。

η₀∉ℤδ を固定する。必要なのは、C_η≃C_η₀ となる **全パラメータ集合** が可算無限であること。

- 下からは RT:η↦η+δ により無限個の相異なる点 η₀+nδ を得る。
- 上からは、固定C内の標識の数値類による可算性と、Uからpointed同型類への写像の有限ファイバー性を使う。後者は二つの内在的foundationとVdBの復元から示す。未知の追加同値を排除せずに、既知の無限軌道だけから可算性を結論しない。
- 全標識分類を直接使う場合は
  \[
  \{\eta:\mathcal C_\eta\simeq\mathcal C_{\eta_0}\}
  =(\eta_0+\mathbb Z\delta)\cup(-\eta_0+\mathbb Z\delta)
  \]
  という完全な式を検討できる。構造対象の像を L(a,b) にし、Serre根の対角移動で L(n,0) に戻し、二つのfoundationの復元で必要性を示す。δを固定する原点保存自己同型が恒等であることと、次数二のL₀をtranslationで合わせる箇所も確認する。主定理にはこの完全な式までは必要ない。

f:U→M が得られたら、I=Isom_U(f,f(η₀)_U)→U を考える。Δ_M が準コンパクトなら I→U は有限型で、像は構成可能。しかし既約曲線上の無限な構成可能集合は非空開を含み、非可算個のk-点を持つので矛盾する。

**非共鳴 locus E\ℤδ は Zariski開ではない。** それを開chartと見なさず、上の U 全体で一つの非共鳴点の同値類を調べる。

## 4. 使う現行証明と一次資料

| 入力 | 正本・確認するラベル |
| --- | --- |
| H2の有限型性・対角 | [論文B](../papers/nc-quadric-surface-moduli.tex)、thm:global-h2-smooth-finite-type とその依存証明 |
| 標識の数値剛性・全標識・可算無限ファイバー | [marking_forgetting.tex](../papers/moduli/marking_forgetting.tex)：lem:forgetting-numerical-rigidity、lem:elliptic-two-reflections、thm:elliptic-marking-lattice-fiber、thm:generic-elliptic-unpointed-fiber |
| 二つのfoundation | [foundation_stack.tex](../papers/moduli/foundation_stack.tex)：cor:two-intrinsic-foundations、prop:ruling-involution-mutation |
| 族・1射・2射の規約 | [relative_definitions.tex](../papers/moduli/relative_definitions.tex)：def:relative-abelian-system、def:relative-h2、lem:relative-h2-flat-center |
| 切片による別証明の相対入力 | [relative_cubic_families.tex](../papers/moduli/relative_cubic_families.tex)：thm:geometric-cubic-relative-effectivity。[relative_picard_roots.tex](../papers/moduli/relative_picard_roots.tex)：thm:relative-compatible-root、cor:finite-type-root-chart。[relative_cubic_noetherian.tex](../papers/moduli/relative_cubic_noetherian.tex)：thm:relative-geometric-cubic-noetherian |
| 代数スタックの定義 | [Stacks Project, 026N](https://stacks.math.columbia.edu/tag/026N)：対角の準コンパクト性を定義に含めない流儀 |
| Isom・対角の局所有限型性 | [Stacks Project, 04XQ](https://stacks.math.columbia.edu/tag/04XQ)：Lemmas 101.3.1、101.3.3 |
| Chevalley | [Stacks Project, 0ECX](https://stacks.math.columbia.edu/tag/0ECX)：Theorem 67.29.2。Noetherian基底上で適用条件を確認 |
| 準分離性 | [Stacks Project, 04YV](https://stacks.math.columbia.edu/tag/04YV)：対角の準コンパクト性・準分離性との関係 |
| 無限群の商という反例 | [Stacks Project, 02Z0](https://stacks.math.columbia.edu/tag/02Z0)：Lemma 65.14.3、Example 65.14.8。[06E9](https://stacks.math.columbia.edu/tag/06E9)：有限型でも非準分離な A¹/ℤ |

上のStacks資料は2026-11-25に内容を確認。番号だけに依存せずtagと主張を論文の文献に記す。既存の [references.bib](../papers/references.bib) と [文献ノート](literature.md) に統合し、重複entryは作らない。VdB2011のarXiv v3 Theorem 5.5.10と、OkawaKitamura2022OWRの既存announcementとの関係は現行の引用を一次資料で再照合する。未照合の詳細稿を入力にしない。

## 5. 結論を過大にしないための確認

- 「ℤが無限だから代数スタックは存在しない」「有限型の商は存在しない」と書かない。非捩れ平行移動の E/ℤ は準分離性を要求しなければ代数空間であり、E×_{E/ℤ}E≃∐_ℤ E から対角の非準コンパクト性が分かる。
- 無限軌道、無限の安定化群、無限個のpointed同型類、2-fiberを区別する。E/ℤの例の安定化群は自明である。
- 有限型atlasのk-点が可算かどうかを直接議論しない。必要なのは構成可能な同型類部分集合による分割である。
- H2自身のcoarse moduli不存在、Cでのgood moduli存在、今回の無標識対象の対角の障害は別の主張である。GITの軌道閉包やS-equivalenceでexact同値を置き換えない。
- 一つの滑らかな楕円例が障害を与えれば全体への結論には十分。torsion δ、η∈ℤδ、退化曲線、noncubicの全分類を追加の完了条件にしない。

## 6. Cloud Codexの実行順序と完了条件

1. U0–U2を独立に点検し、まず最短の主証明を閉じる。必要な既存入力の仮定・証明箇所・左右規約を監査する。別証明は理解を深める範囲で扱う。
2. 論文Bの標識忘却節へ、一般障害補題、適用定理、定義の範囲、無限群商の反例を論理的な順に統合する。新しい独立論文や過去版の補遺を増やさない。完成後にabstract・Introduction・結論の記述を揃える。
3. 証明済み部分と残る仮定を分ける。最終定理を「集合論的ファイバーが無限だから」で済ませず、一般補題の全仮定と同型判定の接続を閉じる。成立しなければ正確な障害・反例と最強の正しい主張を保存する。
4. 一次文献・引用・ラベル・相互参照を点検し、変更したBをLuaLaTeXで組版する。A/Cは変更・依存が及ぶ範囲を確認する。一般の全計算suiteや無関係なCの全面再監査を完了の前提にしない。
5. 研究方針・ノート・README・必要な文献を現在の状態に揃えて通常commitでmainへ保存し、その実際の結果からresearch-hubを更新する。15分を目安とする途中保存、並行変更保持、Actions不使用等はAGENTS.mdに従う。
6. 最終報告では、得た定理と仮定、依存証明の点検範囲、新規性の確認範囲、組版、対象repo保存、hub更新を別々に報告する。計画を書いただけ、一般補題を書いただけではこの研究課題の完成としない。

**今回の設定作業の状態：** 優先順位と論証案を整備した段階。公表原稿への新定理の追加、依存証明の包括的検証、LuaLaTeX再組版は未実施。
