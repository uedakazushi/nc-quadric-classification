# Cloud Codexで研究を進める

2026-11-25 / v0.26。研究の正本は [研究方針](00_research_plan.md)、実行指示は [AGENTS.md](AGENTS.md)。本ファイルは実行環境と運用の手引きであり、最新の数学的優先順位・完了条件は研究方針を参照する。

## taskの起動依頼文

Cloud Codexで uedakazushi/nc-quadric-surface の main を対象にする。

> AGENTS.mdと00_research_plan.md、research-hubの該当項目を読み、現在の優先課題を具体的に進めてください。現行三稿の定理の射程を固定し、既存成果の監査・訂正・文献比較・公表用編集に集中してください。cotangent Morita比較やCY構造の一般化には着手しないでください。A/B/Cの役割、既存の証明・反例・計算資産を保持し、原稿上の証明、独立点検、計算、組版、新規性の状態を区別してください。公表前の主定理の仮定・証明依存・文献比較を検査し、誤りがあれば依存先を修正してください。研究の区切りに通常commitでmainへ保存し、並行変更を保持してresearch-hubを更新してください。詳細な再開先・達成条件は最新の研究方針に従い、計画を作るだけで終了しないでください。ただし個別依頼の範囲と実行環境の限界を守ってください。

このファイルの保存はCloud Codexのtask作成・実行やInstall scriptのPublishとは別。

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


## 実行環境について参照した公式資料

2026-11-21に公式ガイドを確認した。UIの名称や利用可能な機能は実際の環境を優先する。

- [Cloud environments](https://learn.chatgpt.com/docs/environments/cloud-environments)：再利用環境、Install script、Publishとtaskの関係。
- [Custom instructions with AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)：repoに置く継続指示。
- [Long-running work](https://learn.chatgpt.com/docs/long-running-work)：達成条件・制約・途中保存を伴う長時間の研究作業。
