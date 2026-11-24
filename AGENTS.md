# 研究リポジトリの作業指示 — nc-quadric-surface

2026-11-25 / v1.74。

## 現行の研究と優先順位

研究固有の目標・確実性・次の着手先は [00_research_plan.md](00_research_plan.md) を正本とし、本書に重複して書かない。A（体上分類）、B（内在的相対モジュライ）、C（指定AS/avatar/QP相対比較）の三論文体制を維持する。S1–S5の原稿上の証明と指定範囲S6の2026-11-24の点検を、全raw比較、形式証明、外部査読、新規性の確定と混同しない。無標識Abel圏を分類する標的の対角の非準コンパクト性は論文Bに統合した。[依存証明の点検記録](notes/unmarked_moduli_obstruction.md) と研究方針の優先順に従い、Aの体上分類から公表前監査を続ける。

cotangent表示群oid上のMorita比較と本文で証明したCY構造の一般化を研究課題・完了条件に加えない。

研究を依頼された場合は、現在の優先課題に実際に着手し、可能な範囲で証明・反例・計算・原稿を進める。単なる計画整理を数学の進展としない。ただし整理・評価・監査を個別に依頼された場合はその範囲を守る。

## 入口と正本

- 全体の入口：[research-hub](https://github.com/uedakazushi/research-hub)。再開時に該当研究の概要、他研究との関係、再開先を確認する。
- 最初に読む研究方針：`00_research_plan.md`。続いて本AGENTS.mdの適用される指示と `notes/research_notes.md`、必要な原稿・検証記録を確認する。
- 別稿B：`papers/nc-quadric-surface-moduli.tex`。相対モジュライ・境界の現行証明本文を保持。数学的な独立公表前監査は継続。
- 別稿C：`papers/nc-quadric-surface-avatar.tex`。八・十・十二本矢の表示モジュライ・avatar・内在的忘却を扱う。分割節は `papers/quiver-avatar/`。個別の `sources`・`build` には `--manuscript papers/nc-quadric-surface-avatar.tex` を付ける。
- 主たる公表用原稿：`papers/nc-quadric-surface.tex`。リポジトリ直下からの相対パスであり、本文のある主原稿とする。節のソースを別ファイルから読み込んでもよい。独立した別論文には内容を表す名前を付け、役割をREADMEと研究方針に記す。
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

- H2の対象は構造対象のみを指定した `(C,O)`。無標識の課題はOを忘れる分類射について別に定式化する。Gabriel–Krull商でrank one torsion-free、exceptionalを要求する。exact平方根 `s² ≅ S⁻¹[2]`、Artin–Zhang豊富性、二次AS正則持上げの存在は性質であり、`s`・根同型・ambient・方程式を追加標識としない。
- 通常のquadratic envelopeはquadric切断式も含むためAS4にはならない。正しい強い条件は orbit環 `B(C,O,s) ≅ A/(g)`、`A` が左右noetherian quadratic Koszul AS-regular型 `(1,4,6,4,1)`、`g∈A₂` が左右正則正規であること。中心性を無条件に課さない。
- 本repoは右加群規約を使う。`a∈B_m, b∈B_n` に対し `a*b=s^n(a)∘b`。cubic repoの表示された積とは逆の規約なので、Nakayama公式を輸入する際は反対環・左右を照合する。
- 既存の体上分類は全H2対象のpointed exact同値分類。無標識モジュライの対角の障害とは仮定・結論を区別する。graded環の同型、Zhang twist、root付き同値、derived同値を混同しない。既存のcubic Z-algebra/elliptic quadrupleの分類だけで全H2分類済みとしない。
- 候補データからの構成、全H2からの回復、データ上の同値判定、全領域の被覆を別の命題として証明する。「H2を与える表示全体を取る」や未知のAS/admissibilityを条件に残したincidence記述は、全分類の完成ではない。
- GIT商のorbit closure・S-equivalenceをpointed exact同値と同一視しない。反Serre環で同値類を判定できても、graded自己同型群とpointed自己同値群の一致や相対moduliまで自動的に従うとはしない。
- 主原稿の全同値類分類、全H2の有限型代数性、被約境界の相対商表示・全慣性・DM粗モジュライ・一致類の形式対は確立済み。全平方根・ambient忘却ファイバー、Q_fndとの全体の相対比較、偏極認識は別の課題とし、原稿のラベルとnotesの状態表を維持する。
- N^DM→A¹は任意底変更と両立する粗モジュライだがgoodではなく、慣性は非proper。全H2には粗モジュライ代数空間がない。一致類の共通étale商近傍の局所良モジュライと、Cで三半不変式から構成した全H2の準射影的good moduliを区別し、両者の局所比較を明示する。
- 他repoは必要な一次資料として参照する。`nc-cubic-classification` の完全分類定理を本repoの既知入力にしない。Serre根についての一般研究は `categorical-fano-index`、tensor/quadruple分類は確認済み文献と役割を区別する。
- 無標識課題の結論は対角の非準コンパクト性とする。非準分離な代数スタックの存在や有限型性そのものを排除したと書かない。分類射の幾何点判定は両方向を要求し、集合論的な同型類ファイバーと2-fiber、自然同型を持つ2圏と通常の1-stackを区別する。
- 次の着手先は研究方針の優先課題。有限次数の計算だけでAS正則性・smoothness・全次数正則性・全対象の被覆を証明したと報告しない。
