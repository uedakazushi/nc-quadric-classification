# Cloud Codexで研究を継続する

2026-11-21 / v0.3。研究内容の正本は [研究方針](00_research_plan.md)、継続・保存の指示は [AGENTS.md](AGENTS.md)。数学原稿はv0.4、H2の完全分類は未完成である。

## 起動時の依頼文

このrepoを選んだCloud taskに、次の依頼を渡す。以後の実行単位は研究方針を更新して引き継ぐので、過去の会話は必要ない。

> AGENTS.mdと00_research_plan.mdに従い、H2の完全分類の達成条件F1–F6を満たすまで研究を進めて下さい。研究方針が指定する現在の第一着手から始め、証明・反例・一次文献比較・必要な厳密計算を行い、結果を日本語LuaLaTeXの主原稿と現行ノートへ統合して下さい。一補題・検算・commitを終了条件とせず、保存後も次の課題へ進んで下さい。切りのよいところで随時、長くても前回の成功したpushから約15分以内に通常commitとmainへの反映を行い、研究の区切りにresearch-hubも更新して下さい。他の作業者の変更を保持し、force pushとGitHub Actionsの追加・起動は行わないで下さい。実際の実行上限や不可欠な外部制約に達した場合は、証明境界と次の具体的一手を現行資料へ保存して下さい。

AGENTS.mdは、研究の継続手順と達成条件を与える。実行時間・利用可能な道具・ネットワーク・認証は実際のCloud環境に従う。別taskの自動起動や無期限実行を設定するファイルではない。

## 環境の準備

repoルートで実行する。スクリプト自体は実行場所に依存せずrepoを解決する。

```sh
bash scripts/bootstrap.sh
python3 scripts/check.py doctor
python3 scripts/check.py sources
```

bootstrapは既存のPython 3.9以上とSymPyを利用し、不足する場合にrepo内の`.venv`と`requirements.txt`を使う。システムのPythonパッケージを置き換えない。依存が既に使えれば導入のための通信をしない。別のPythonを探索候補の先頭にする場合は`QUADRIC_PYTHON`に実行ファイルの絶対パスを渡す。bootstrapが表示するPython実行ファイルを使ってcheckerを起動できる。`.venv`がある場合、checkerの計算部分はそのPythonを使う。

LuaLaTeX組版とPDF表示用の依存も導入する場合は、次を用いる。

```sh
bash scripts/bootstrap.sh --with-tex
python3 scripts/check.py all
```

`--with-tex`はDebian/Ubuntuで、既にrootまたは非対話sudo権限がある場合に限り、latexmk・LuaTeX-ja・必要なTeXパッケージ・Popplerの導入を試す。他OSではその環境のTeX Live/MacTeX等を用いる。導入できない場合は`PARTIAL`と表示して終了し、可能な証明・資料比較・原稿編集を続ける。bootstrapの終了コード0は準備処理の終了を表し、全依存の充足や検証成功を意味しない。欠落を隠すために権限や承認設定を変更しない。

Cloudの再利用環境では、このrepoを接続し、Install scriptに上記bootstrapを登録して環境内で試した後、Publishする。setup script欄がある環境でも同じコマンドを使える。既に用意されたTeXを使う環境なら`--with-tex`は不要。軽い再開時確認は`doctor`と`sources`でよく、毎回TeX全体を再導入しない。設定保存とPublish、repo更新と環境再作成は別の操作である。本ファイルの追加だけではCloud環境の作成・Publish・task起動は行われない。

Pythonの導入には環境に応じてPyPI、TeXの導入にはOSのパッケージ配布元への接続が必要になる。一次文献は [文献ノート](notes/literature.md) のURLから必要なものを取得する。GitHub、arXiv、出版社等への接続可否を現行の許可範囲で確認し、取得できない資料の内容を推測しない。導入時の通信と研究実行時の通信を同一視しない。

## 検証コマンド

checker自体はPython標準ライブラリだけで動く。必要な段階を個別に呼び出せる。

| コマンド | 確認すること |
| --- | --- |
| `python3 scripts/check.py doctor` | Python/SymPy、TeX、PDF確認コマンド、現在のGit commit・branchの診断。通信・書込認証は確認しない |
| `python3 scripts/check.py sources` | 必須ファイル、TeXのinput/root・ラベル・引用、設定JSON、ローカルMarkdown参照、Git追跡対象と空白の点検 |
| `python3 scripts/check.py math` | 既存の`computations/verify_quadric.py`による有理数・記号演算 |
| `python3 scripts/check.py build` | repoの`.latexmkrc`を指定したLuaLaTeX組版、最終ログ、PDFとSyncTeX |
| `python3 scripts/check.py all` | sources・math・buildを個別に実行し、いずれかの依存不足だけで他の確認を省略しない |

検証コマンドの終了コードは**PASS=0、FAIL=1、SKIP=2**。一つでもFAILなら全体は1、FAILがなく未実施があれば2となる。doctorの0は診断処理の終了のみを意味する。数学的主張の証明、文献の適用仮定、新規性、全分類の達成、PDFの目視、GitHubへの反映をこのコードだけで判定しない。

組版先は`build/nc-quadric-classification.pdf`と同名の`.synctex.gz`。レイアウトを変更した場合はPDFを表示して確認する。PDF・中間生成物・`.venv`は追跡しない。検算の対象と理論による証明の境界は [研究ノート](notes/research_notes.md#検証範囲と再現手順) に記す。

## 保存と再開

1. 作業開始時にcheckout、未commit変更、`origin/main`との差を確認する。別担当の変更を上書きしない。更新を取得できなければその制約を明記し、利用できる現行資料で独立な課題を進める。
2. **切りのよいところで随時、前回の成功したmainへのpushから長くても約15分以内に**、意味のある一区切りを現在の原稿・ノート・方針・READMEへ統合してpushする。これは保存間隔であり、研究の停止時刻ではない。15分以内に証明が閉じない場合も、証明済みの部分と未完成の部分を区別して中間保存する。長い計算・組版・文献調査を始める前にも保存し、それらの終了を待って保存を先延ばしにしない。次に着手する未解決命題と最初の式・入力を研究方針へ残す。
3. 変更に必要な確認を実行し、自分が扱ったファイルを選んで通常commitする。最新remoteを読み、並行変更を保って必要な統合をしてから`git push origin HEAD:main`する。拒否された場合にforce pushで解決しない。利用可能なGitHub connectorで通常commitを作る方法も使える。
4. remoteのmainに保存commitが含まれることを確認する。公開repoのgit読取成功は書込認証の成功ではない。認証情報をrepoへ記載しない。Cloud上の書込権限が前のtaskから引き継がれるとも仮定しない。
5. 本repoの保存後、research-hubの最新READMEと適用指示を読み、該当項目の到達点・確実性・核心・次の一手・正本を更新する。hubへの権限は別に確認し、Gitの通常統合または最新SHAを条件とした更新で他研究の変更を保持する。
6. 本repoとhubの保存を別々に確認する。hubが未反映でも利用可能な研究は続け、未反映内容と理由を報告する。本repoへの保存自体ができない場合の緊急保存はAGENTS.mdの規則に従う。

完全分類の終了判定は研究方針F1–F6に従う。相対モジュライや全自己同値の計算は、同値類の完全分類と区別する。新しいsessionでは最新mainの研究方針を読み、そこに残した実行単位から再開する。

## 実行環境について参照した公式資料

2026-11-21に公式ガイドを確認した。UIの名称や利用可能な機能は実際の環境を優先する。

- [Cloud environments](https://learn.chatgpt.com/docs/environments/cloud-environments)：再利用環境、Install script、Publishとtaskの関係。
- [Custom instructions with AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)：repoに置く継続指示。
- [Long-running work](https://learn.chatgpt.com/docs/long-running-work)：達成条件・制約・途中保存を伴う長時間の研究作業。
