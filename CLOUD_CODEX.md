# Cloud Codexで全相対AS/avatar/QP stack分類を進める

2026-11-23 / v0.24。研究の正本は [研究方針](00_research_plan.md)、repoの指示は [AGENTS.md](AGENTS.md)、現行論文Cは [papers/nc-quadric-surface-avatar.tex](papers/nc-quadric-surface-avatar.tex) v4.68。論文A v1.69、B v0.41は論理的入力。Codexは**従来C1–C4のみで終了せず**、下の全相対stack分類のS1–S6を目標に研究を続ける。

## 最上位目標と完了条件

標数零代数閉体上の本研究の**指定型**（square/rotated square/cubic/独立最小AS10と対応avatar、重み付き8/10/12本矢QP）について、非被約基底を含む全相対fppf stackの対象・同型層・慣性・族の完備性・全周期AS再構成を分類する。QP right-equivalenceの全慣性と適切なrigidification後の比較、群oidの2-coherence、mutation/ruling、$H_2$への忘却射・像・ファイバー・外側の領域まで決定し、C原稿に証明付きで統合する。**「全QP」は任意の箙やpotential全体という意味ではなく、指定8/10/12重み付き表示の全対象・相対族を表す。** raw QP・AS・avatarのスタックが直接同値だと仮定しない。

**完了判定：研究方針のS1–S6を全て満たし、主張の依存・一次文献・数式・TeX/PDFを独立監査したときのみ。** C1–C3は既存の原稿上達成点、C4はS6の一部。体上AS分類、$H_2$実現可能開、有限foundationの一chartの成功は「全分類」の完了ではない。研究計画の変更が必要な場合は、元の目標の未解決点を保持し、勝手に完了条件を弱めない。

## 次に実行する数学的作業（着手順は方針が正本）

1. **AS/avatar/QPの相対stackを厳密に定義する**：型ごとの標準AS整数添字、線束・root/frame、相対可逆性・perfect条件、raw QPの同型とrigidified同型を分ける。どの定義が非被約局所有限型基底上で有効かを調べる。
2. **foundationからの全族回復・全射性**：`papers/quiver-avatar/as_helix_classification.tex`、`as10_mutation_classification.tex` の `thm:qa-as10-relative-families`、`relative_square_foundation_stack.tex` を突き合わせる。相対AS10のperfect/局所自由仮定が指定AS族から自動的に従うかを、$k[\varepsilon]/(\varepsilon^2)$・rank3壁・古典squareで証明または反例化する。正しい相対Isom sheaf（pointingとperiodの線束含む）を記述し、体上同型類の全単射から全stack同値を推論しない。
3. **全QPの許容部分と慣性**：`qp_presentations.tex` と `cubic_qp_foundation_groupoid.tex` を使い、8/10/12本矢の全right-equivalence、$mathbb G_m$可縮pair・二mass・頂点scalars、nilpotent nonminimal relationと非cotangent射を調べる。QP表示がASになる必要十分条件・余分なQP族・剛体化後の対象と射を分類する。
4. **全比較図式・$H_2$と外側**：AS↔avatar↔QPの射のIsom/full faithfulness/essential surjectivity/fiberを検査し、局所mutationとruling S2、特異・noncubic/spectral境界の既知障害と整合させる。canonical CY classの高次降下は、この比較への必要性を見定め、独立問題ならCノートへ分離して保持する。
5. **証明監査と公表準備**：上記と並行してC4の独立証明監査、一次文献の原文照合、sources/math/build（利用可能ならPDF/SyncTeX表示）を進める。確定結果のみC主原稿へ統合し、計算・原稿上証明・今回の独立検証を混同しない。

**続行ルール。** 一補題・計算成功・章追加・commitで停止しない。証明が閉じなければ最小反例・残余補題・別chartを研究ノートに整理して次の優先課題へ進む。切りのよいところで、前回の成功したpushから**おおむね15分以内**に現在有効な論文C・研究ノート・研究方針・README/AGENTSを通常commitし、最新mainを確認してfast-forward push。続けて次の研究課題へ着手する。更新した研究成果をrepo mainへ保存した後、research-hubの最新READMEを読み、該当項目を通常commitで更新する。並行作業・force push禁止・Actions追加/起動禁止・PDF追跡禁止。外部資源不足は正しく報告し、可能な数学的作業を続ける。

## Cloud Codex taskの起動依頼文

Cloud Codexで `uedakazushi/nc-quadric-surface` の `main` を対象に新しいtaskを作り、以下を渡す（以後の細かい再開点は常に最新 `00_research_plan.md` に従う）。

> [最上位目標] 本repoのAGENTS.md・00_research_plan.md・CLOUD_CODEX.mdとresearch-hubの対象項目を読み、論文C `papers/nc-quadric-surface-avatar.tex` に、指定square/rotated/cubic/minimal AS10型・対応する幾何avatar・重み付き8/10/12本矢QPの**全相対fppf stack分類**を完成させてください。終了条件は方針の**S1–S6すべて**です。既存のC1–C3やH2実現可能開だけで終えず、全相対族、非被約基底、全Isom・慣性、raw QPと剛体化後の区別、groupoidの2-coherence、mutation/ruling、H2の内外の対象と比較射の像・ファイバーを証明してください。全raw QPのAS性や三stackの直接同値を先取りせず、反例や部分成立条件を明示してください。
>
> [最初の一手] `as_helix_classification.tex`、`as10_mutation_classification.tex`、`relative_square_foundation_stack.tex`、`qp_presentations.tex`、`cubic_qp_foundation_groupoid.tex` を照合し、全AS/avatar/weighted-QP相対stackの対象とIsomを定義して、`thm:qa-as10-relative-families` のperfect/平坦性仮定が全指定AS族から導けるかをまず解決してください。$k[\varepsilon]/(\varepsilon^2)$・rank3壁・古典例を調べ、全族foundation被覆の本質的全射性とIsomの必要な不足補題を定理・証明または具体的反例として進めてください。
>
> [実行と保存] 研究方針と主原稿・研究ノートを現在有効な内容へ更新し、日本語LuaLaTeX原稿に十分な証明を追加してください。既存の全成果・先行研究引用・再現資産を保持し、定理の仮定と証明状態を明確化してください。検証可能な範囲でsources/math/latexmkのチェックを行い、結果は実行事実だけを記録してください。一つの成果だけで停止せず、進行可能な限り次のS1–S5へ進んでください。15分程度ごとに切りのよいところで通常commitしてmainへfast-forward pushし、研究の区切りにはrepo保存確認後にresearch-hubを更新してください。並行変更を維持し、force push・GitHub Actions追加/起動をせず、実行環境の限界なら現行資料に次の証明作業を残してください。

**このファイルのGitHub保存はCloud Codexのtask作成・実行やInstall scriptのPublishとは別。** taskの実行開始は利用者がCodex UIから行う。AGENTS.mdはCodexがrepoを読む際に適用される作業指示となる。

## 環境の準備

repoルートで実行する。スクリプト自体は実行場所に依存せずrepoを解決する。

```sh
bash scripts/bootstrap.sh
python3 scripts/check.py doctor
python3 scripts/check.py sources --manuscript papers/nc-quadric-surface-avatar.tex
```

bootstrapは既存のPython 3.9以上とSymPyを利用し、不足する場合にrepo内の`.venv`と`requirements.txt`を使う。システムのPythonパッケージを置き換えない。依存が既に使えれば導入のための通信をしない。別のPythonを探索候補の先頭にする場合は`QUADRIC_PYTHON`に実行ファイルの絶対パスを渡す。bootstrapが表示するPython実行ファイルを使ってcheckerを起動できる。`.venv`がある場合、checkerの計算部分はそのPythonを使う。

LuaLaTeX組版とPDF表示用の依存も導入する場合は、次を用いる。

```sh
bash scripts/bootstrap.sh --with-tex
python3 scripts/check.py papers
python3 scripts/check.py all --manuscript papers/nc-quadric-surface-avatar.tex
```

`--with-tex`はDebian/Ubuntuで、既にrootまたは非対話sudo権限がある場合に限り、latexmk・LuaTeX-ja・必要なTeXパッケージ・Popplerの導入を試す。他OSではその環境のTeX Live/MacTeX等を用いる。導入できない場合は`PARTIAL`と表示して終了し、可能な証明・資料比較・原稿編集を続ける。bootstrapの終了コード0は準備処理の終了を表し、全依存の充足や検証成功を意味しない。欠落を隠すために権限や承認設定を変更しない。

Cloudの再利用環境では、このrepoを接続し、Install scriptに上記bootstrapを登録して環境内で試した後、Publishする。setup script欄がある環境でも同じコマンドを使える。既に用意されたTeXを使う環境なら`--with-tex`は不要。軽い再開時確認は`doctor`と`sources`でよく、毎回TeX全体を再導入しない。設定保存とPublish、repo更新と環境再作成は別の操作である。本ファイルの追加だけではCloud環境の作成・Publish・task起動は行われない。

Pythonの導入には環境に応じてPyPI、TeXの導入にはOSのパッケージ配布元への接続が必要になる。一次文献は [文献ノート](notes/literature.md) のURLから必要なものを取得する。GitHub、arXiv、出版社等への接続可否を現行の許可範囲で確認し、取得できない資料の内容を推測しない。導入時の通信と研究実行時の通信を同一視しない。

## 検証コマンド

checker自体はPython標準ライブラリだけで動く。必要な段階を個別に呼び出せる。

| コマンド | 確認すること |
| --- | --- |
| `python3 scripts/check.py doctor` | Python/SymPy、TeX、PDF確認コマンド、現在のGit commit・branchの診断。通信・書込認証は確認しない |
| `python3 scripts/check.py sources --manuscript papers/nc-quadric-surface-avatar.tex` | 必須ファイル、TeXのinput/root・ラベル・引用、設定JSON、ローカルMarkdown参照、Git追跡対象と空白の点検 |
| `python3 scripts/check.py papers` | A/B/Cの3原稿のソース・引用・原稿間ラベル・指定型の接続を一度に点検（数学的証明そのものではない） |
| `python3 scripts/check.py math` | 既存の`computations/verify_quadric.py`による有理数・記号演算 |
| `python3 scripts/check.py build --manuscript papers/nc-quadric-surface-avatar.tex` | repoの`.latexmkrc`を指定したLuaLaTeX組版、最終ログ、PDFとSyncTeX |
| `python3 scripts/check.py all --manuscript papers/nc-quadric-surface-avatar.tex` | sources・math・buildを個別に実行し、いずれかの依存不足だけで他の確認を省略しない |

検証コマンドの終了コードは**PASS=0、FAIL=1、SKIP=2**。一つでもFAILなら全体は1、FAILがなく未実施があれば2となる。doctorの0は診断処理の終了のみを意味する。数学的主張の証明、文献の適用仮定、新規性、全分類の達成、PDFの目視、GitHubへの反映をこのコードだけで判定しない。

論文Cの組版対象は`papers/nc-quadric-surface-avatar.tex`、出力先は`build/nc-quadric-surface-avatar.pdf`と同名の`.synctex.gz`。論文A/Bも必要な依存検査のときは各主原稿を指定して組版する。レイアウトを変更した場合はPDFを表示して確認する。PDF・中間生成物・`.venv`は追跡しない。検算の対象と理論による証明の境界は [研究ノート](notes/research_notes.md#検証範囲と再現手順) に記す。

## 保存と再開

1. 作業開始時にcheckout、未commit変更、`origin/main`との差を確認する。別担当の変更を上書きしない。更新を取得できなければその制約を明記し、利用できる現行資料で独立な課題を進める。
2. **切りのよいところで随時、前回の成功したmainへのpushから長くても約15分以内に**、意味のある一区切りを現在の原稿・ノート・方針・READMEへ統合してpushする。これは保存間隔であり、研究の停止時刻ではない。15分以内に証明が閉じない場合も、証明済みの部分と未完成の部分を区別して中間保存する。長い計算・組版・文献調査を始める前にも保存し、それらの終了を待って保存を先延ばしにしない。次に着手する未解決命題と最初の式・入力を研究方針へ残す。
3. 変更に必要な確認を実行し、自分が扱ったファイルを選んで通常commitする。最新remoteを読み、並行変更を保って必要な統合をしてから`git push origin HEAD:main`する。拒否された場合にforce pushで解決しない。利用可能なGitHub connectorで通常commitを作る方法も使える。
4. remoteのmainに保存commitが含まれることを確認する。公開repoのgit読取成功は書込認証の成功ではない。認証情報をrepoへ記載しない。Cloud上の書込権限が前のtaskから引き継がれるとも仮定しない。
5. 本repoの保存後、research-hubの最新READMEと適用指示を読み、該当項目の到達点・確実性・核心・次の一手・正本を更新する。hubへの権限は別に確認し、Gitの通常統合または最新SHAを条件とした更新で他研究の変更を保持する。
6. 本repoとhubの保存を別々に確認する。hubが未反映でも利用可能な研究は続け、未反映内容と理由を報告する。本repoへの保存自体ができない場合の緊急保存はAGENTS.mdの規則に従う。

体上のH2完全分類F1–F6はAにおける既存到達点であり、**本研究の現在の終了判定は論文CのS1–S6全相対stack分類**に従う。相対AS/QP群oidと同値類・慣性・heartの比較は別々の主張として検証する。新しいsessionでは最新mainの研究方針を読み、そこに残した実行単位から再開する。

## 実行環境について参照した公式資料

2026-11-21に公式ガイドを確認した。UIの名称や利用可能な機能は実際の環境を優先する。

- [Cloud environments](https://learn.chatgpt.com/docs/environments/cloud-environments)：再利用環境、Install script、Publishとtaskの関係。
- [Custom instructions with AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)：repoに置く継続指示。
- [Long-running work](https://learn.chatgpt.com/docs/long-running-work)：達成条件・制約・途中保存を伴う長時間の研究作業。
