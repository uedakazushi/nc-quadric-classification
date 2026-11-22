# 研究リポジトリの作業指示 — nc-quadric-classification

2026-11-22 / v1.13。論文Aはv1.69（20節）、論文Bはv0.39（31節）、論文Cはv3.7。

## 公表用三論文への再編（確定方針）

- A：`papers/nc-quadric-classification.tex` を主原稿とし、構造対象付きの全体上の分類と同値判定を自己完結にする。
- B：`papers/nc-quadric-moduli.tex` は内在的相対モジュライの正本とし、相対Koszul・Artin変形・有限型効果性・境界幾何の証明を保持する。
- C：主原稿 `papers/nc-quadric-avatar.tex` と `papers/quiver-avatar/avatar_charts.tex`・`git_comparison.tex`が**O-marked quadric／potential／anticanonical avatarの同型類全単射・相対射**の正本。smooth cubic VdB↔square線束公式、O保存r1商、potential→avatar4/→H2合成8を保持。**今回、noncubic全幾何点**の二根対↔smooth/nodal/I2の$P=G_sF_s^{-1}\ne0$かつ$P^2=1$であるsquare avatar↔Bのnoncubic O-marked全同型類の全単射をCに証明。$B_f=k[u,v]\langle c,d\rangle/(c^2-f_1,d^2-f_2)$の可換化の点曲線$E_f$と同時符号商$C:y^2=f_1f_2$、反不変rank-one torsion-free spectral module$M$による**実際の相対射**も構成。共有根の節点では$M$は$A_1$表面の非自由reflexiveで、通常Pic0線束に相対延長不可。**集合論的全単射とPicard線束の相対射を混同しない。** 次はminimal resolution/Σ2 elementary transformによる別avatarへ戻す構成と$C_q$・$\Sigma_2$側の$\qgr$ heartの同定、8/10/12 potential stable groupoid。既存H2 finite foundation開・ruling二択、OU慣性・有限多項式・四次六次結果は正本に保持。A/B証明・一次文献・実組版・push・hub各状態を区別。 全noncubic O-marked幾何同型類≅Σ₂のD∈|−K|,D∩S=∅,0≠P∈Pic⁰(D)[2]の同型類もCに証明。Bのχ=1二点はnodal/I2で区別。次は$C_q$・$\Sigma_2$の別avatarのqgr heartとの比較と相対elementary transformを検証する。

**原稿C v3.7のpointed認識上の最重要区別。**
noncubic中央二重平方環の可換点曲線
$E_f:\ c^2=f_1,\ d^2=f_2$と、quartic spectral曲線
$C_q:\ y^2=f_1f_2$は、非共有根では
自由同時符号の商$E_f\to C_q$による
**次数2のétale isogenyで、一般には同型でない**。
$E_f$上には個別符号反転の二conic商から
次数二pencil $F_d,F_c$と非零2torsion
$P_E=F_cF_d^{-1}$があり、square二重壁avatarを作る。
$C_q$上の反不変二捩れ$M_C$は
$r^*:\Pic^0(C_q)\to\Pic^0(E_f)$の核。
$(C_q,M_C)$と$(E_f,P_E)$は双対2-isogenyで交換されるが
次数二pencilとAS finite foundationは自動同定されない。
証明はpapers/quiver-avatar/point_spectral_isogeny.tex、
根の簡単な例で$j(C_q)=35152/9$、
$j(E_f)=28756228/3$、$\Phi_2=0$の厳密算術検算は
computations/verify_rootpair_resolvent_spectral.py。
**重要：C_qの既存avatarをB_fの可換点曲線E_fと同一視して
内在的O-marked心とのpointed同値を導いてはならない。**
**既に証明された比較の範囲：**
分類論文Aのnoncubic normal helixの二つのMCM行列
$M_c,M_d$のpoint-curve上のkernel射は
conic商$Q_c,Q_d$の次数二pencil $F_c,F_d$を回収する
（C prop:qa-point-mcm-matrix-pencils）。
さらにその隣接Hom積の像は
$\im\mu_c=\langle u,v,c\rangle$と
$\im\mu_d=\langle u,v,d\rangle$であり、
二pencilのVeronese対称積像に一致する
（C prop:qa-point-mcm-composition-veronese）。
二像は各階数3で交わりは$\langle u,v\rangle$、
和は$(B_f)_1$全体。
**全noncubic幾何点のpointed認識（C v3.7）。** 二つのsquarefree二次形式の根対は、相異・一根共有・一致をすべて許す。点曲線$E_f=\operatorname{Proj} B_f^{\mathrm{ab}}$は二conicのファイバー積$Q_c\times_{\mathbb P^1}Q_d$で、smooth/nodal/$I_2$の$(2,2)$ Cartier因子になる（C lem:qa-pointed-all-rootpair-geometry）。$X_c,X_d$の可換化によるspinor section moduleと、四頂点Endの全Hom・全合成の同型は三型すべてで成立する（C lem:qa-pointed-abelianization-four-end）。square avatar $(E_f,F_c,F_d,P_E)$の指定mutation後、比較すべき四項は$(H_0,\ldots,H_3)$でなく**$(H_1,\ldots,H_4)$**。この位相でSerre完成・AZを使い、全noncubic $\mathcal H_2(k)$について$(\qgr B_f,\pi B_f)\simeq(\qgr A_{\rm av},\pi e_1A_{\rm av})$という**体上のO-pointed exact同値**を原稿で証明した（C thm:qa-point-all-noncubic-pointed, cor:qa-point-all-noncubic-h2）。$C_q$のspectral avatarや$\Sigma_2$の別avatarとのpointed同値、非被約基底の相対groupoid・慣性・descentは未解決。三型の有理係数モデルで次数1–2の厳密計算をPASSしたが、数学的全証明の独立全面監査・新規性・組版は別状態。

**順序付き分解普遍族の相対有限End（C v3.7）。** $S=k[\ell_i,m_i,(\det\ell\,\det m)^{-1}]$（二組の独立一次形式）上で、四項$(\mathcal B,\mathcal X_c,\mathcal B(1),\mathcal X_d(1))$の有限graded directed Endと$E_S=Q_c\times_{\mathbb P^1}Q_d$上の$(\mathcal O,F,F^2,F^2G)$のEndを、**任意の$S$-基底変更（非被約も含む）と可換な代数同型**として証明した（C prop:qa-point-relative-split-root-end）。被約でsmoothな普遍底で有限表示行列の全幾何fiber階数が一定であることから局所分裂を得て、その後に非被約底へ引き戻す。これは有限Homと全積の相対同型であり、相対$\qgr$ heart・Serre根・AS被覆の同型や、根の順序を忘れるstack降下はまだ証明していない。

**継続指示：** smooth/nodal/$I_2$の三型全てで$(H_1,\dots,H_4)$へ位相を合わせ、$(H_0,\dots,H_3)$と頂点固定で同定しない。次は根の順序を忘れる降下と相対Serre完成、$C_q$・$\Sigma_2$側の別avatarとの比較を個別に検証し、全相対$\qgr$同値を先取りしない。

**論文C v3.7の分類正本（最優先）。**
`papers/nc-quadric-avatar.tex` から
`papers/quiver-avatar/as_helix_classification.tex` と
`papers/quiver-avatar/as10_mutation_classification.tex` を読み込む。
前者の `thm:qa-as-avatar-bijection` は
最小分解型を指定した square/rotated AS正則Z代数と
対応avatar（非被約反標準Dを含む）の頂点保存同型類全単射、
必要AS階数・逆spherical helix・全Serre completion・左右Noether性を扱う。
後者の `thm:qa-as10-global-bijection` は独立定義の最小10本矢ASと
cubic ASとの非交和が全square ASに一致するmutation逆対応、
およびAS10のavatar条件G≅FPを証明する。
**十二本矢は通常八本のfinite foundation＋四本のrelation-dual戻り矢のQP表示で、
任意の十二本矢QP全体をAS正則としない。**
Keller undeformed CY completionとKeller--Yang mutation、Okawa--Uedaの
acyclic spherical helix実現は外部一般定理として明示している。
旧PDFの主張を移管した事実と全証明の独立再検証済みかを混同しない。
体上AS分類・仮定付きrelative perfect AS族と、
元のO-marked H2 heartのpointed同値・全相対QP stack同値は区別する。
次の重点はAS分類の独立監査（特に非被約Pic0とrank forcing、
Ginzburg集中・逆mutation・全整数評価/余評価）とC全文組版。
新数値検算は `computations/verify_as_avatar_euler.py`。
C v3.4ではASsq/ASrsqの四相Euler生成関数を有理関数として
全次数厳密計算し、AS10の偶奇級数も独立検算した。
非被約Dを含むpencil trickにより
$\operatorname{rk}\mu_G=3\iff P=GF^{-1}$を証明した。
Keller--Yang Thm6.2の(c1)loopなし、(c2)mutation頂点を
通る2-cycleなし、(c3)potentialの巡回表示という
各適用条件を元論文と照合。
ASsq/ASrsqのcoherent derived Morita・Serre、
固定mutation先の左右Noether性と$\Qgr/\qgr$同値の
proofもCへ統合した（prop:qa-as-avatar-coherent-morita、
prop:qa-as10-noetherian-qgr）。
**全証明の独立検証済みとせず**、AZ ample corner・
finite projective dimension・Ginzburg次数零集中・
相対完全性の残りの依存を最優先監査。
これはunderlying Abel同値でpointed O-marked同値ではない。

**原稿C v3.4：二重壁と全cubic導来非同値の正本。**
$\mathrm{AS}_{sq}$の二つの最小10矢mutation壁の交点は
$Z=\{0\ne P\in\Pic^0(D)[2],G\simeq FP\}$。
\`papers/quiver-avatar/as10_mutation_classification.tex\` の
\`lem:qa-as10-double-wall-reduced-geometries\` は
非被約二重$(1,1)$、cuspidal、接触型が
非零2捩れを持たないことを証明し、
$Z$をsmooth/nodal/I2に限定する。
新設\`papers/quiver-avatar/cubic_obstruction_all_loci.tex\` の
\`thm:qa-as-cubic-reachability\` は
ASsqがいずれかのcubic ASとQgrの完全Abel同値、
またはDb(qgr)の三角同値を持つ条件が
$A\notin Z$と同値であることを証明する。
滑らかな場合は任意のcubic候補のrank・determinant・
隣接pencilの積の核を使い、nodal/I2では
2捩れtorsorの形式的平滑化・有限End代数上の
exceptional perfect複体の持上げで排除する。
出典は元PDF第19–21節の既存結果。
**二つの特定mutationが失敗することだけで
全cubic foundation不存在を推論しない。**
これはqgr/derivedのunpointed比較であり、
内在的noncubic O-marked H2とのpointed同値は未解決。
再現コード \`computations/verify_avatar_cubic_obstruction.py\`
はSerre数値格子と二捩れparityのみを厳密検算。
GAGA・perfect持上げ・全導来非同値を形式証明したとは扱わない。

**原稿C v3.4のGinzburg／二重壁の局所監査。**
Keller (2011 Thm6.10)のrelation Ginzburg=undeformed
3-CY completionの適用には有限$B$のgldim2と
minimal relationsが矢idealの二乗にあることが必要。
$\Theta=\RHom_{B^e}(B,B^e)[2]$の各$m$次tensor成分は
$\RHom_B(E_i,S_B^{-m}E_j[2m])$で計算し、
$m\ge1$なら$j+4m>i$となる全整数forward Ext消滅を使う。
内部正次数／直積完備化の適合も別に確認する。
Keller–Yang (2011 Thm6.2)はreduced source potentialと
(c1)全quiver loopなし・(c2)mutation頂点の2-cycleなし・
(c3)cyclic representativeの条件を必要とする。
これらはCのAS10節へ明記済み。
smooth $D$上の二つの10矢壁のFitting Cartier条件は
$\eta=P$と$\eta=P^{-1}$で、非零2捩れ点で横断・被約、
固定smooth $D$上3点、nodal/I2上1点ずつ。
新系はprop:qa-as10-double-wall-transversalityと
cor:qa-as10-singular-double-wall-transversality。
固定smooth楕円族では有限étale三次だが
内在O-marked stack同値を意味しない。
次は全AS最小分解へのDG降下、corner/Noether性、
非被約相対ASのperfectness、内在heart pointed比較を独立監査。
局所計算スクリプトのPASSを導来同値全体の形式証明と扱わない。

**論文Cの必須参照と現在の障害。**
添付の大川--植田v7 Parts I--IIで必要な反標準曲線消滅・二pencil・square/rotated変換・
finite directed foundationのscheme復元を `papers/quiver-avatar/square_rotated_foundations.tex`、
四項canonical exact complex・周期式・前向きExt消滅を `papers/quiver-avatar/canonical_helix_complexes.tex` に
証明ごと組み込んだ。全AS Z代数の体上分類・Noether性は新設の分類節で扱い、相対標準heart/O同値は別の未解決課題である。
共有根A1の反不変moduleを同じ基底上で最小解消すると例外曲線への次数が奇数となるため、
垂直Cartier twistだけでは多重次数零の相対Picard線束にできない
（`papers/quiver-avatar/nodal_resolution_obstruction.tex`、検算は `computations/verify_nodal_exceptional_parity.py`）。
さらにCの現行節では、任意基底の二形式族についてspectral反不変層$M$の
二次積$\mu:M\otimes M\to O_C$の像$(f_1,f_2,y)$、欠損余核$O_{V(f_1,f_2)}$
と任意基底変更への適合を証明した（幾何fiberで欠損長0/1/2）。
nodalの極限は$\nu_*O_{\mathbf P^1}(-1)$（単純）、
I2は二つの$O(-1)$の正規化直像（非単純・End $k^2$）で、
積を保つ曲線固定自己同型群はそれぞれ$\mu_2$、$\mu_2^2$。
**simple/fine compactified Picardのみを相対標的に選ばない。**
二次積付きgroupoid $\mathfrak{TF}^{quad}$ は定義済みで、
Bの二形式表示商 $[P/G]$ から任意の基底と可換な
$(C,M,\mu)$ のfppf相対射もCの
prop:qa-spectral-quadratic-stack-mapに構成した。
次はこの射の全忠実性・fiber、標的groupoidのArtin性・finite type条件、
被約・非被約基底の慣性と変形、元H2境界とAS heartのpointed比較、
およびbase change / 相対elementary transformを研究する。
単に射が存在することからstack同値を推論しない。
証明済みの体上全単射を非被約底の相対射へ読み替えない。

現行作業順序は研究方針のP0–P5（A/B公表前監査、文献比較、既存GITとの比較、C相対認識）を優先する。BからAへの17種類のラベル参照はAの現行分類20節に定義されている。これはTeXソース上の依存の監査で、全数学的証明の独立監査ではない。Aの主原稿の相対部分は入力から外したが、未使用の旧相対節ファイルはBに全証明と対応ラベルの保持を確認したうえで整理済み。残るBへの引用・source依存を優先して点検する。`python3 scripts/check.py papers`（A/B/Cの明示的な論文間ラベル参照も検査） を実行して3原稿を別々に検査する。証明移管・数学的検証・組版・GitHub保存・hub更新は別の状態として扱い、外部査読済みとは主張しない。

## Cloud Codexへの継続指示

このrepoの研究継続を依頼された場合の目標は、`00_research_plan.md`の現行の実行単位を完了することである。全H2の分類は「完全分類の達成条件」F1–F6を基準とし、達成済みの場合は方針に記した公表前監査・次の研究課題から進める。計画の作成、一補題、一例、一節、検算成功、commit、pushを終了条件にしない。推進できる未解決課題がある限り、保存後も次の実行単位へ進む。「続けますか」と毎回確認しない。環境の開始方法は `CLOUD_CODEX.md` に置く。

1. 最新のhub該当項目、研究方針、本指示、必要なノート・原稿を読む。既存の未commit変更を調べ、他の作業者の変更を保持する。実際のcheckoutと`origin/main`の差を確認し、研究方針の「次の実行単位」から始める。
2. `python3 scripts/check.py doctor`で道具を診断し、`python3 scripts/check.py sources`で構成を点検する。必要な依存のみ`bash scripts/bootstrap.sh`で整える。依存不足はその検証を未実施とする理由であり、証明検討・原稿編集・利用可能な資料の比較まで止める理由ではない。
3. 一つの実行単位では、必要な仮定と到達する補題を定め、証明・反例・一次資料比較・厳密計算のいずれかを具体的に進める。新しい計算は小さい基準例で規約を確認してから拡大し、入力・乱数seed（使用時）・再現コマンドを残す。低次数の成功を全次数の証明へ昇格させない。
4. 主要な主張は、可能なら独立の読取り担当に仮定・推論・反例を点検させる。並列担当には異なるファイルまたは読取り専用作業を割り当て、主担当が原稿・方針・mainを統合する。subagentがなければ、結論を一度疑って仮定と反例を別の観点で再点検する。
5. 同じ障害に再度当たったら、使えなかった理由・必要な不足補題・最小反例候補を研究ノートに現在形でまとめる。研究方針の代替課題へ切り替える。特定の文献・認証・TeX導入に詰まっても、独立な数学課題へ移る。実質的な進展なしに同じ検索・計算・環境修復を反復しない。
6. **切りのよいところで随時、前回の成功したmainへのpushから長くても約15分以内に**、切りのよい数学的単位で現行の本文・ノート・方針・READMEを整え、必要な検証後に通常commitとmainへのpushを行う。この時間は保存の目安であり、作業を終了する期限ではない。保存後は、次に証明すべき命題・具体的な式・参照箇所を方針に一つ指定し、その課題を続行する。
7. 各検証のPASS/FAIL/SKIPを区別する。`scripts/check.py`の成功は構成・計算・組版の確認であり、証明・新規性・完全分類の認証ではない。必要な検証が未実施なら、その制約をノートと報告に書く。環境修復だけを研究成果として報告しない。
8. 最終終了は、完全分類の達成条件を満たして独立点検・保存を終えた場合、ユーザーが停止・変更を指示した場合、または実行環境の上限や不可欠な外部権限等により本当に継続できない場合に限る。後者では現行一式を保存し、未解決命題・使える結果・次の具体的一手と外部制約を方針へ残す。自動的な別セッション起動や無期限実行をAGENTS.mdで実現したとは扱わない。

全対象の定義・基礎体・同値関係を狭めて完了判定を満たしてはならない。方法の変更、定理候補の訂正、必要な補題の追加は自律的に行い、有効な成果を現行原稿に保持する。全てのambientや全ての平方根を別々に完全分類することは、H2のpointed exact分類に必要だと証明されない限り終了条件に追加しない。

## 入口と正本

- 全体の入口：[research-hub](https://github.com/uedakazushi/research-hub)。再開時に該当研究の概要、他研究との関係、再開先を確認する。
- 最初に読む研究方針：`00_research_plan.md`。続いて本AGENTS.mdの適用される指示と `notes/research_notes.md`、必要な原稿・検証記録を確認する。
- 別稿B：`papers/nc-quadric-moduli.tex`。相対モジュライ・境界の現行証明本文を保持。数学的な独立監査は継続。
- 別稿C：`papers/nc-quadric-avatar.tex`。八・十・十二本矢の表示モジュライ・avatar・内在的忘却を扱う。分割節は `papers/quiver-avatar/`。個別の `sources`・`build` には `--manuscript papers/nc-quadric-avatar.tex` を付ける。
- 主たる公表用原稿：`papers/nc-quadric-classification.tex`。リポジトリ直下からの相対パスであり、本文のある主原稿とする。節のソースを別ファイルから読み込んでもよい。独立した別論文には内容を表す名前を付け、役割をREADMEと研究方針に記す。
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

- 対象は構造対象のみを指定した `(C,O)`。Gabriel–Krull商でrank one torsion-free、exceptionalを要求する。exact平方根 `s² ≅ S⁻¹[2]`、Artin–Zhang豊富性、二次AS正則持上げの存在は性質であり、`s`・根同型・ambient・方程式を追加標識としない。
- 通常のquadratic envelopeはquadric切断式も含むためAS4にはならない。正しい強い条件は orbit環 `B(C,O,s) ≅ A/(g)`、`A` が左右noetherian quadratic Koszul AS-regular型 `(1,4,6,4,1)`、`g∈A₂` が左右正則正規であること。中心性を無条件に課さない。
- 本repoは右加群規約を使う。`a∈B_m, b∈B_n` に対し `a*b=s^n(a)∘b`。cubic repoの表示された積とは逆の規約なので、Nakayama公式を輸入する際は反対環・左右を照合する。
- 分類の最終目標は全H2対象のpointed exact同値分類。graded環の同型、Zhang twist、root付き同値、derived同値を混同しない。既存のcubic Z-algebra/elliptic quadrupleの分類だけで全H2分類済みとしない。
- 候補データからの構成、全H2からの回復、データ上の同値判定、全領域の被覆を別の命題として証明する。「H2を与える表示全体を取る」や未知のAS/admissibilityを条件に残したincidence記述は、全分類の完成ではない。
- GIT商のorbit closure・S-equivalenceをpointed exact同値と同一視しない。反Serre環で同値類を判定できても、graded自己同型群とpointed自己同値群の一致や相対moduliまで自動的に従うとはしない。
- 主原稿の全同値類分類、全H2の有限型代数性、被約境界の相対商表示・全慣性・DM粗モジュライ・一致類の形式対は確立済み。全平方根・ambient忘却ファイバー、Q_fndとの全体の相対比較、偏極認識は別の課題とし、原稿のラベルとnotesの状態表を維持する。
- N^DM→A¹は任意底変更と両立する粗モジュライだがgoodではなく、慣性は非proper。全H2には粗モジュライ代数空間がない。一致類の共通étale商近傍がsmooth3次元good moduliを持つことから、H2のZariski開または全体のgood moduliの存在を無条件に推論しない。
- 他repoは必要な一次資料として参照する。`nc-cubic-classification` の完全分類定理を本repoの既知入力にしない。Serre根についての一般研究は `categorical-fano-index`、tensor/quadruple分類は確認済み文献と役割を区別する。
- 次の着手先は研究方針の優先課題。有限次数の計算だけでAS正則性・smoothness・全次数正則性・全対象の被覆を証明したと報告しない。

