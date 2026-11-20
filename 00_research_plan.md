# 研究方針：O-marked 非可換二次曲面の分類

2026-11-21 / v0.3。**再開時は本書を最初に読む。GitHub `main` が正本。** 数学原稿はv0.2で、完全分類は未完成である。

**現在の実行単位はT1（第6節）：内在的な反Serre切断環によるpointed exact同値の還元を証明する。** 完了したらT2へ進む。実行環境と起動用の依頼文は [CLOUD_CODEX.md](CLOUD_CODEX.md)、継続・保存・停止の規則は [AGENTS.md](AGENTS.md) を参照する。

## 1. 恒常的な研究原則と保存許可

この節は研究一般の原則であり、第2節以降の研究固有の計画と区別する。

1. 数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性から研究全体の価値を最大化する。方針は柔軟に変更し、変更理由と元の目標の達成部分・残存部分を、現時点で有効な説明へ書き換える。履歴を蓄積しない。
2. 証明済み、追加仮定付き、証明未完成、予想、計算的観察を区別する。主要主張の仮定・依存結果・証明箇所・未解決点を明記する。原稿に証明があること、今回その論理を点検したこと、計算・形式証明器を実行したこと、新規性を確定したことは別である。誤りは依存する本文・要約・方針・hubにも反映する。
3. 重要な文献は一次資料で仮定・適用範囲・書誌を確認し、Introductionで既知結果と本研究の関係を具体化する。未確認の文献内容や新規性を推測しない。他研究の結果を使う際は定理、仮定、出典と必要なcommitを記す。文献PDFや検索結果を大量収録しない。
4. 原稿は原則日本語LuaLaTeX。主原稿は本文のある `papers/nc-quadric-classification.tex` とし、research-hubのテンプレートと組版設定を参照する。有効な公表価値のある成果と必要な証明を論理的な順序で統合する。未完成箇所は明示し、追記式の版別原稿や重複本文を増やさない。独立論文を分ける場合は役割を説明する。
5. 研究ノートには論文外の着想、例、反例、計算、失敗した方法の本質的障害、文献比較、再取得困難な情報を整理する。本文に十分な証明がある事項は参照する。作業日誌、旧会話、試行履歴、解決済みtodoは不要である。
6. 現行の方針・ノート・論文と最小限のコード・入力・文献・再現手順から自己完結して再開できるようにする。旧bundleや会話を再開の前提にしない。数学的内容や検証可能性を損なってまでファイル数・容量を減らさない。旧ZIP、旧版原稿、バックアップ、ログ、cache、組版中間物は追跡しない。必要な証明書・再取得不能な入力は保持する。Git履歴を改変しない。
7. 研究の区切りごとに承諾なく通常コミットし、`main` へ反映する。長時間作業では15〜30分を目安に保存する。他の作業者の変更を保持し、force push・GitHub Actionsの追加や起動は行わない。PDFは原則追跡せず、LuaLaTeX・latexmk・SyncTeX・VS Code設定を保持する。改名時はinput、文献、root指定、README、方針、設定を整合させる。GitHub保存が成功すればLibraryへの定常的な二重保存やZIP作成はしない。失敗時の緊急保存または別途依頼時のみLibraryを使い、既存Libraryファイルを無断で削除しない。
8. 日付・版と参照・記法・主張状態を一致させる。必要な範囲の組版・計算・参照点検を行い、生成、論理点検、計算、組版、GitHub反映、Library保存、hub更新を別々に確認する。先に本repoを保存し、その内容に基づいてresearch-hubの該当項目を更新する。最新hubと並行変更を保持し、概要・主要到達点・確実性・核心・次の一手・依存関係・正本・実際の資料確認日を反映する。詳細todoや証明を複製しない。hub更新に失敗しても成果は保存し、未反映内容と理由を報告する。

実行規則は [AGENTS.md](AGENTS.md)、全体の入口は [research-hub](https://github.com/uedakazushi/research-hub)。日常todoは本研究と分ける。

## 2. 研究固有の目標と対象

**最終目標：強いクラス H2 の全対象を、構造対象を保つ exact 同値で分類する。** 対象は `(C,O)` のみ。`O` はGabriel–Krull商でrank one torsion-freeかつexceptional。`Db(C)`はHom有限でSerre関手`S`を持つ。次を同時に満たすexact自己同値`s`とambientが**存在**することを要求する。

$$
s^2\simeq S^{-1}[2],\qquad (O,s)\text{ is Artin--Zhang ample},
\qquad B(C,O,s)\simeq A/(g).
$$

`A`は左右noetherian quadratic Koszul AS-regular、global dimension・Gorenstein parameterともに4、解消型`(1,4,6,4,1)`。`g∈A₂`は左右正則正規。`s`、根同型、`A`、`g`、商表示は追加標識としない。H2の添字は超曲面次数2を表し、可換quadricの反標準次数は8である。

**定義上の修正理由。** cubicのquadratic envelopeをそのまま使うと、quadric方程式自身が二次関係に含まれる。標準可換例でも二次関係は7本で、AS4の6本と一致しない。そのため、通常の二次包絡のAS正則性を、二次AS正則被覆の存在へ置き換えた。元の目標である「Oだけを指定し、sとambientは存在する性質」は保持する。被覆を忘れた完全分類は未解決である。

右加群規約：`a∈B_m,b∈B_n` の積は `a*b=s^n(a)∘b`。cubic原稿の表示された積とは反対の規約であり、Nakayama公式等を無検査で移植しない。

## 3. 初期到達点と確実性

以下は主原稿に証明を置く初期結果。既存文献の一般定理を明示して適用している。新規性の包括的確認、外部査読、形式証明は未実施。

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

原稿の生成・検算・組版の実施状況は [研究ノートの検証範囲](notes/research_notes.md#検証範囲と再現手順) に記す。全H2の完全分類や全成分の記述は未完成である。

## 4. 完全分類の達成条件

標数零の代数閉体上の、主原稿 `def:h2` の全対象を分類する。最終成果は、具体的な代数的・幾何学的データP、明示的なadmissibility、データ上の同値関係を与え、

$$
P/{\sim}\;\longleftrightarrow\;
\{(\mathcal C,\mathcal O)\in\mathcal H_2\}/{\text{pointed exact equivalence}}
$$

の全単射を証明する定理である。有限個の模型や単一のGIT商になることは先取りしない。同値関係はデータ上の作用・変換・必要十分不変量として記述し、「圏が同値なら同一視する」と言い直すだけにしない。

| 必須の証明 | 完了とする条件 | 現在の状態 |
| --- | --- | --- |
| F1 データと許容条件 | 全パラメータ領域とadmissibilityを具体化し、未知のAS条件や「H2を与える」という循環的条件を残さない | 未完成。quadruple/tensor比較と固定Bの超平面還元が入口 |
| F2 構成の正しさ | 各許容データからO付き圏を構成し、GK rank・exceptionality・Serre根・AZ・全次数AS表示を確認する | 可換型と限定したSklyanin型に証明あり。一般は未完成 |
| F3 全被覆 | 任意のH2対象から許容データを回復する。追加仮定を使う場合はH2からの導出か、補集合を覆う別の証明を付す | 未完成。central化、standard表示、ambientの(*)が残る |
| F4 同値判定 | 二つのデータが同じO-marked対象を与える必要十分条件をデータ上で証明する | 滑らかな射影整曲面として実現される可換対象は完了。一般はT1とT4から着手 |
| F5 全領域と基礎体 | 一般点だけでなく、退化・特殊自己同型・例外領域を含め、各領域を構成、既収録領域へのpointed exact同値による帰着、またはH2不適合の証明で処理する。k=Cだけの議論には適切な体の拡張・降下を補う | 未完成。smoothは圏の大域次元の条件であり、幾何データの退化を一律には排除しない |
| F6 証明と再現 | 主定理から入力補題まで依存を閉じ、一次文献の仮定・規約を確認し、必要な厳密計算・組版・独立点検を終えて現行一式とhubを保存する | 初期結果は確認済み。全分類の証明はまだ存在しない |

F1–F6が揃うまでは「完全分類」と報告しない。条件付きの還元、一般点の分類、例の族、有限次数のincidence、既存の非標識分類だけでは完了しない。原稿に未証明の核心命題が残っていないことを、異なる観点または独立担当で確認する。checkスクリプトはこの数学的達成を判定しない。

自己同値群・groupoid・相対モジュライを主張する場合は、それに対応する全忠実性、自然同型、降下・底変更・代数性を別途証明する。次数スカラー等の核を調べずに反Serre環のgraded自己同型群とpointed自己同値群を同一視しない。GIT商のorbit closure・S-equivalenceがpointed exact同値と一致するかも別途確認する。これらは重要な後続目標だが、対象のpointed exact同値類の完全分類と混同しない。全ambientや全平方根の個別分類を不必要な終了条件にしない。

## 5. 核心と優先課題

### 優先0：平方根を忘れた内在的な完全不変量

主原稿で証明した反SerreのAZ豊富性を利用し、`t=S⁻¹[2]` の切断環Rへ同値問題を還元する。T1に下記の具体的な候補を置く。Rが不変量として使えても、Rの明示的な許容族の全被覆は別に必要である。9生成環の無差別な列挙を始めず、既存quadricデータを構成に使い、Rを忘却後の比較に使う方針を優先する。

### 優先1：既知のquadric分類との、Oと平方根を保つ比較

VdBのcubic AS-regular Z-algebraのeven partとcanonical quadratic hullに対し、構造対象、次数シフト、Serre関手を同じ規約で書く。可換型と通常の滑らかなSklyanin型で確立した例を基準に、一般の楕円型・退化型へ広げる。最初の具体的課題は、Sklyanin pencilの標識Oと二つのrulingをgeometric quintupleへ移し、選んだshiftに対応する自然同型 `s²=S⁻¹[2]` を比較すること。`MU2021`の`M_ν(-2)`公式は中心切断の仮定の下で用い、対象ごとの不変性を関手の自明性へ読み替えない。次に、非自明Nakayama twistがある場合に根を存在させる自己同型のnorm方程式を得る。

### 優先2：standard locusの認識と非standard表示

`MUW2026` Theorem 5.5により滑らかな中心Sklyanin型はstandardであり、`MN2025` Theorem 6.13の仮定を満たす。この既知結果を入口にOと根を追跡する。一般H2ではdomain・heartの大域次元2は初期補題から得られるが、中心表示の存在・standard表示・指定Oの対応は別の課題である。`MUW2026`の一般理論はambientのAuslander正則性・Cohen–Macaulay性(*)を別仮定とするため、H2のAS条件から無断で導かない。(*)を確認できる範囲では同論文Proposition3.5・Lemma3.20の二つのMCM型とrulingを使い、`Ω(1)`の作用を比較する。同論文Introductionでもnormal→centralのgraded Morita還元は不明とされる。可換四根のうち保存型3つはstandard、交換型はnon-standard（同論文Theorem4.12）なので、non-standardな一表示を見ただけでO-marked対象を除外しない。

### 優先3：二段階の忘却と具体的なパラメータ

固定Bで `K=ker(B1⊗B1→B2)` を計算し、`P(K*)`内のAS被覆と正規性を判定する。可換BのOre直線を基準例とし、非可換楕円Bへ移る。次にroot付き圏からO-marked圏への自己同値作用を調べる。既存のOkawa–Uedaのquintuple GIT商・potential商との対応は、実際に標識の忘却を構成してから述べる。可換点の4根と既存の次数4射の一致は未検証。

### 優先4：全対象の被覆・境界・相対化

全H2の必要十分なadmissibility、pointed exact同値の全矢、自己同値、成分・境界へ進む。相対Serre、根の降下、orbit環の底変更、次数別平坦性を明示する。有限次数incidenceだけで代数stackや全分類を宣言しない。全AS4環の完全分類の完了を作業開始の前提にせず、二次切断と平方根の条件で対象を絞る。

## 6. 次の実行単位

以下は進行順と切替先を兼ねる現行の課題表であり、作業履歴ではない。原稿に統合して閉じた課題は主要到達点へ移し、この節には未解決部分だけを残す。数学的内容が変わらない限り、毎回新しい計画・台帳・日誌を作らない。

### T1：反Serre環とpointed exact同値（現在の第一着手）

**状態：証明候補。以下の同値と二次表示はまだ主原稿の定理ではない。** 既存の `prop:reconstruction`、`lem:ample-square-from-generation` を読み、

$$
t=S^{-1}[2],\qquad
R(\mathcal C,\mathcal O)=\bigoplus_{n\ge0}\operatorname{Hom}(\mathcal O,t^n\mathcal O)
$$

を右加群の積で定義する。候補は、任意の適合根sについて `R≅B(C,O,s)^(2)` となり、pointed exact同値類がRの次数付き同型類で判定できるというもの。次を順に証明する。

1. tがheart上exactであること、Serre関手と根同型の選択を替えてもRの次数付き同型類が変わらないこと。自然同型の反復と積の整合性を明示する。
2. 偶数Veroneseのnoetherian性とAZ再構成を確認し、OをπR、tを次数shiftへ送る同値を書く。
3. pointed exact同値がSerre関手とOを保つことからRの同型を作り、逆向きはqgr再構成で示す。単なるderived同値へ拡張しない。
4. `dim R_n=(2n+1)^2`、`H_R=(1+6t+t²)/(1−t)^3` を検算する。二次環Bの語を二文字ずつ区切る証明から、`U=B₂`、`R≅T(U)/(ker(U⊗U→B₄))`、`dim U=9`、二次関係56本を導けるか確認する。

**成果物：** 主原稿に選択独立性・両方向の証明・依存を備えた命題を統合し、必要な小さい検算のみ既存コードへ追加する。証明できない箇所は正確な不足補題としてノートへ置く。この還元が成立しても、「H2由来の56次元関係空間のGL9軌道全体」を書くだけでF1–F3が済んだとはしない。

### T2：既存の標識を追跡する比較

T1と独立に一次文献の比較を進められる。`MU2021`、`MN2025` Theorem6.13、`VdB2011`のeven part/hullに対し、同じ右規約で、O、二つのspinor/MCM対象、選ぶfoundation、次数shift、Serre関手の像を表にする。Sklyanin型では`MUW2026` Theorem5.5を入力に使う。

**最初の式：** 比較関手Fについて、`F(O)`、`F(sO)`、`F(s²O)` と、それぞれへのHom積を書く。`Fs≅s'F` または反Serre環の同型に必要な自然同型を検査する。文献がOやsを保存すると述べていなければ、自分で証明する。

**成果物：** 一つの明示的なpointed比較定理、または失敗する条件と最小の障害。quintupleの基底変更と平行移動が同じO-marked対象を与えるかを次の問いとして残す。必要な本文を取得できなければT1/T3へ移る。

### T3：全被覆の不足仮定を埋める

H2で未確認の条件を、ambientのAuslander正則・Cohen–Macaulay性(*)、compatibleなcentral表示、standard表示の存在に分ける。各条件につき、H2からの証明、条件を使わない代替定理、H2内の反例のどれを目指すか決める。反例が出てもH2の定義からその対象を削除しない。

**最初の式：** `MUW2026` Remark4.4の規約 `af=fν(a)`、`σ(f)=f`、twist後のnormalizer `ρ=σ⁻²ν` を使い、`σ²=ν` のambientへの持上げと、誘導されるSerre根との整合性を調べる。ここでνはnormalizerであり、Nakayama自己同型と同一視しない。文献の積と本稿の積の変換を書く。

**成果物：** 全被覆に必要な一つの不足仮定の解決、または適用範囲を正確に切り分ける反例・障害。central化に行き詰まればnormal cutのままのMCM/ruling理論を使う。全AS4分類を先に終える方針へ無条件に転換しない。

### T4：構成データの許容域と忘却後の同値判定

T2で得たデータに対し、H2へ入る必要十分条件を求める。固定Bでは `prop:ambient-hyperplane` のK、R、三次の左右rankを使い、AS条件そのものは定理で確認する。T1が成立した後は、二つの表示の偶数Veroneseが次数付き同型になる条件をデータ上で記述する。

**基準例：** 可換quadric上の四根が同じRを与えること、Ore族の異なるambientが同じ対象を与えること、可換圏に非同値なSklyanin例が可換Rと同型にならないことを確認する。既存の次数4射やroot fiberの有限性を先取りしない。

**成果物：** 一つの族のadmissibilityと同値判定を対で証明する。一般点だけでなく例外パラメータを別の領域として扱い、構成・既収録領域へのpointed exact同値による帰着・H2不適合の証明で閉じる。独立な領域は並列化できる。

### T5：全領域の統合と最終監査

F1–F5を満たす候補定理を一つ書き、各矢印に対応する証明箇所を付す。各候補領域を、H2対象の構成、既収録領域へのpointed exact同値による帰着、またはH2不適合の証明によって処理する。未被覆のH2対象を残したまま領域を除外しない。未確認の外部入力、左右・shift・標識の不一致、k=Cへの限定が残れば対応する課題へ戻る。

主定理を独立担当に渡して反例・仮定漏れを探索し、文献比較と公表上の貢献を確定する。必要な再現・組版・現行一式の整合を確認してmainとhubへ保存した時点で、完全分類の達成を報告できる。相対モジュライは、対象の同値類分類の達成と分けて次の研究目標を定める。

## 7. 正本・依存関係・再開

- 主論文：[papers/nc-quadric-classification.tex](papers/nc-quadric-classification.tex)。独立した別論文は現時点ではない。
- 現行知識・障害・再現：[notes/research_notes.md](notes/research_notes.md)。文献仮定・版・リンク：[notes/literature.md](notes/literature.md)、書誌：[papers/references.bib](papers/references.bib)。
- 計算：[computations/verify_quadric.py](computations/verify_quadric.py)。`python3 -m pip install -r requirements.txt` 後、repoルートで `python3 computations/verify_quadric.py`。
- Cloudの導入と検証：[CLOUD_CODEX.md](CLOUD_CODEX.md)、`bash scripts/bootstrap.sh`、`python3 scripts/check.py doctor`。構成・検算・組版を個別に実行でき、欠落依存が独立な数学作業を止めないようにする。
- 組版：repoルートで `latexmk`。PDFとSyncTeXは`build/`。LuaTeX-jaを含むTeX Live/MacTeX、latexmk、BibTeXが必要。VS Codeはrepo全体を開いてLaTeX Workshopの既定レシピを使う。
- cubic側の定義比較は `nc-cubic-classification` のcommit `5393766744bdae887a374b6853ff4daf53d971b5`、`papers/nc-cubic-classification.tex` のrank定義・`def:14641-intrinsic` を確認した。その完全分類定理は本研究の入力にしていない。
- `categorical-fano-index` はSerre根一般の関連研究。現時点で同repoの未確認結果を輸入していない。既知quadric文献を優先する。
- GitHub更新には対象repo・research-hubそれぞれの書込み権限が必要。前の実行で使えた認証や接続が次のCloud taskにもあるとは仮定せず、読取と書込を別に確認する。研究資料の再開に会話履歴は不要。
