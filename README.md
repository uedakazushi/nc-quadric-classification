# nc-quadric-classification

**構造対象 O のみを指定した非可換 quadric surface の分類。**

2026-11-22 / 運用v1.04、論文A v1.69、論文B v0.39（依存・組版の監査中）、論文C v2.8。まず [研究方針](00_research_plan.md) と [AGENTS.md](AGENTS.md) を読む。GitHub `main` を正本とする。

**現行の作業順序：** [研究方針のP0–P5](00_research_plan.md#現行実行計画と達成基準公表準備から次の比較研究へ) に従い、まずA/Bの証明・先行研究・三稿の参照を監査し、公表用の構成を整える。次の中心研究は、**論文C**で一般cubic領域のquintuple/potential GITと内在的H2の相対比較、その忘却ファイバーと慣性、境界への延長を研究すること。Bは標的となる内在的Artinモジュライの定理を供給し、GIT比較の証明を重複させない。Cのheart/AS適合性とGIT compactification全体への射の未完成な範囲を区別する。

## 公表用原稿：三論文へ再編

| 原稿 | 中心課題 | 状態 |
| --- | --- | --- |
| **A・主原稿** [nc-quadric-classification.tex](papers/nc-quadric-classification.tex) | O-marked非可換二次曲面の全分類とpointed exact同値 | 体上の全分類を中心とする20節を入力。相対主定理はBを引用 |
| **B** [nc-quadric-moduli.tex](papers/nc-quadric-moduli.tex) | 内在的相対H2の代数性とnoncubic境界の幾何 | **相対H2・Artin変形・AS4・Koszul・cubic/noncubic効果性・境界幾何・楕円型忘却の31節を保持。Aの分類入力との残余依存を監査中** |
| **C** [quiver-avatar-moduli.tex](papers/quiver-avatar-moduli.tex) | **O-marked quadric・potential・反標準avatarの同型類全単射／相対射** | v2.8。smooth cubic VdB↔squareの明示式、O保存r1商、OU potential一般4/8次を保持。**noncubic全幾何点**の二根対↔smooth/nodal/I2 square 2torsion avatar↔O-marked全単射を証明。Bの中央二重平方環の可換点曲線からspectral coverとrank-one torsion-free moduleへの相対射も構成。共有根A1で可逆Picard線束への相対延長が不可能な反例を明示。元AS avatar qgrのheart認識、Σ2 elementary transformと全potential groupoidは未解決 | 全noncubic幾何型はΣ₂上の反標準因子D∩S=∅と非零Pic⁰(D)[2]の同型類にも全単射。原AS心の直接同定・相対Picard線束射は未解決 |

論文AのAbstractとIntroductionは分類に焦点を当て、相対結果の分割節は主原稿から外した。Aに残る20節は分類の構成・被覆・同値判定を担う。Bは31節で、楕円型の構造対象忘却と反Serre偏極の変形例も含む。

Aを分類論文、Bをその体上分類を入力とする相対モジュライ論文、Cを有限表示・avatar論文として整理する。Aの先行研究節は体上の分類に絞って整理し、BのIntroductionには相対主定理の見取り図を加えた。Belmansのcubic側の既知HH計算を比較対象に追加した。BからAへの17種類のラベル参照がAの有効な分類20節に定義されていることを確認した。全証明の数学的独立監査は別に必要である。3原稿の独立source検査に加え、A/B/C間の `\cite[\texttt{label}]{...}` の参照先ラベル実在性も検査するよう checker を拡張した。リポジトリ全体のcheckoutができないため、三稿の全checker実行・LuaLaTeX組版は未実施。新規の五頂点bar厳密計算コードは容器内で実行し、GitHub上の同一ファイルであることをGit blob SHAで確認した。 3原稿の構成検査は `python3 scripts/check.py papers`、個別組版は `python3 scripts/check.py build --manuscript papers/<原稿名>.tex` とする。GitHubへのソース反映と組版実行は別々に確認する。

## 論文C：添付v7の幾何的核心を本文に統合（v2.8）

論文Cの新設節 [square / rotated の幾何・有限foundation](papers/quiver-avatar/square_rotated_foundations.tex) と
[canonical複体・全整数周期](papers/quiver-avatar/canonical_helix_complexes.tex) に、
大川--植田の未公刊草稿「非可換二次曲面の二つの反標準avatar」v7（Parts I--II）から
反標準Cartier曲線のPicard消滅、二pencilの再埋込み、4×4・2×2の評価行列によるscheme-theoretic復元、
四つの局所分裂完全列と周期全体の前向きExt消滅を**定義・仮定・証明ごと**組み入れた。
元論文を持たなくてもこれらの有限幾何は追える。
ただし、元の全AS正則Z代数のNoether性、元のO-marked heartの直接同値、
非被約底を含む全AS相対分類を、この追加だけで証明したわけではない。

**新しい研究結果：** [共有根A1の最小解消上の奇偶障害](papers/quiver-avatar/nodal_resolution_obstruction.tex)。
相対spectral反不変moduleを解消上で可逆化すると、
例外P¹上の次数は1であり、既約nodal特殊曲線の垂直Cartier twistでも奇数に保たれる。
ゆえに`同じ一径数基底でA1を最小解消するだけ`では、
通常の多重次数零の相対Picard line-bundle avatarは構成できない。
底変更・compactified Picard・相対モデル変更の可能性は残る。
[局所恒等式の再現コード](computations/verify_nodal_exceptional_parity.py) はmath suiteに登録。
Cの相対心の直接認識と8/10/12矢の全potential groupoidはなお未解決である。

## 論文Bの証明監査と再現

noncubic有限型効果性では、[五頂点barとcanonical tails](papers/moduli/noncubic_local_tails.tex)、[中央Clifford閉部分のPBW・Noetherian貼合せ・AS4延長](papers/moduli/noncubic_finite_type.tex)の依存関係を整理した。可換quadricでの終頂点Torの厳密計算は[五頂点検算](computations/verify_five_window_terminal.py)、Cliffordの任意可換係数環上の書換は[PBW検算](computations/verify_clifford_pbw.py)で再現できる。有限次数の計算と全相対主定理の証明は区別する。

[atlas構成](papers/moduli/quadric_smooth_atlas.tex)に、指定pointed exact同型のArtin持上げからrepresentable smoothを導く独立補題を追加。可換・cubic・noncubic chartの重複論証を統合し、[全体smooth atlas・framed空間](papers/moduli/h2_smooth_atlas.tex)へ接続した。noncubic chartは64次元、atlasの相対次元61、relation scheme125次元、PGL₉枠X_as83次元。相対代数性とframedの証明正本は**論文B**であり、論文Aへの古い参照を訂正した。

今回変更した節のTeX環境バランスと新補題の参照を静的に点検。三稿全体のソースchecker・LuaLaTeX組版はローカルcheckout不能のため未実施。31分割節の一括チェックは接続側の操作数上限で実行できなかった。次の重点はnoncubic境界の相対groupoid、慣性、good/coarse moduli。

## noncubic境界の相対groupoidとgood/coarse moduli

一致根対の形式局所模型についてAHRの刊行定理（2020年Theorem1.2）の全仮定を照合し、全慣性の線型化から三つの二次不変式ac、(x+y)²、(x−y)²を独立計算した。局所good moduliの原点への微分は零である一方、不変式環は滑らかな三次元多項式環となる。この共通étale近傍のgood moduliがH2のZariski開へ降下するかは別問題であり、今後は既存GITのforgetful射のfiber・慣性と合わせて検討する。



[P/G]から内在的被約境界への同値は、標数零の群スキーム慣性、smooth境界chartの相対二形式族への因数分解、相対tilting・反Serre再構成、接空間全射とétale判定を組み合わせる。[境界比較論文Bの節](papers/moduli/noncubic_boundary_comparison.tex)では、正標数のBα_pが幾何点の抽象群単射からのrepresentabilityの反例になることを明示した。一致根対の慣性重みは±2、形式的二変数の不変式はk[[ac]]、good moduli座標χ=1/(1−4ac)は微分零・混合Hessian4である。これらの代数的恒等式は[境界検算](computations/verify_noncubic_boundary.py)と整合する。

表示商全体のgood moduli A¹と、閉gerbeを除くDM開のcoarse A¹は異なる。後者はnon-good、慣性はnonproperである。DM開の任意基底変更に対する粗空間は、有限μ₂局所商を各基底上で再構成して証明する。詳細な証明の依存と未検証箇所は[現行研究ノート](notes/research_notes.md)を参照。

## ローカル組版の最短手順（TeX Live 2026）

**リポジトリ直下**（`README.md` と `.latexmkrc` があるディレクトリ）で、最新版へ更新してから次を実行する。

```sh
git pull --ff-only
latexmk papers/nc-quadric-classification.tex
latexmk papers/nc-quadric-moduli.tex
latexmk papers/quiver-avatar-moduli.tex
```

`papers/` に `cd` して `latexmk nc-quadric-classification.tex` とすると、上位の `.latexmkrc` は自動では読まれず、通常の `latex`（LuaLaTeXではない）が選択される。`papers/` にいる場合は `cd ..` して上記を実行する。既に `papers/` で誤ったエンジンの `.aux` / `.fdb_latexmk` が生成された場合、まず `cd ..` してから上記のルート指定ビルドを行う（別ディレクトリの旧出力は新ビルドで利用しない）。

2026-11-22に受領した実ログでは、旧原稿の `sections/foundation_stack.tex:788` の `Undefined control sequence \mathscr` で最初のLuaLaTeXビルドが停止した。現行主原稿は `mathrsfs` を読み込むのでこのコマンドは定義される。ログの `Citation ... undefined` / `Reference ... undefined` の大半は初回実行時の未解決参照であり、今回の最初の停止原因ではない。**最新版をルートから再ビルドした成功ログはまだ受領していないため、三稿の完全組版成功は未確認。**

## VS Code / LuaLaTeX の組版環境

リポジトリの `.vscode/settings.json` はOSに依存しない `latexmk` コマンドを使う。macOS・Linux・Windowsのいずれでも、TeX Live（または互換するLaTeX環境）を導入し、**VS Codeの拡張機能プロセスから** `latexmk` がPATHで見える必要がある。WindowsではTeX LiveまたはMiKTeXの実行ファイルディレクトリをPATHに登録する。組版にはLuaLaTeX、`ltjsarticle`、latexmk等が必要である。

macOSでFinder/DockからVS Codeを起動した場合、MacTeXが導入されていても `/Library/TeX/texbin` が拡張機能のPATHに含まれないことがある。この場合、**Macだけのローカル対処**として、VS Codeのユーザー設定（リポジトリで共有しない設定）で `latex-workshop.latex.tools` の `latexmk-project` の `command` を `/Library/TeX/texbin/latexmk` に、`latex-workshop.latex.clean.command` も同じ絶対パスに指定する。共有設定の `cwd` と `args` は維持する。あるいは、`/Library/TeX/texbin` をVS Codeの起動環境PATHに追加してから再起動する。Macの `.latexmkrc` はMacTeXのディレクトリが存在する場合にのみ子プロセスのPATHを補うが、**latexmk自体を起動する前のPATH問題は解決しない**。

VS Codeではリポジトリのルートをフォルダとして開き、`papers/nc-quadric-classification.tex`、`papers/nc-quadric-moduli.tex` または `papers/quiver-avatar-moduli.tex` をアクティブにして LaTeX Workshop のビルドを実行する。PDFとSyncTeXは `build/` に出力される。まずターミナルで `latexmk -v` と `lualatex --version` を確認し、ビルドが失敗した場合は LaTeX Workshop のログで `spawn latexmk ENOENT` の有無を確認する。

## Cloud Codexで続ける

[CLOUD_CODEX.md](CLOUD_CODEX.md) に、環境の準備・起動用の依頼文・検証・保存手順を置く。最終目標は研究方針F1–F6を満たす**全H2のpointed exact同値分類**。一補題やcommitで止めず、現行資料を更新しながら次の未解決課題へ進む。

**全H2の分類と、内在的モジュライの有限型smooth Artin性を証明した。** cubic側はlinearデータと、整・被約・非被約を含む全てのVan den Bergh許容四つ組で構成し、四生成環の二次関係に対する有限の代数的判定で重複を除く。noncubic側はP1上の二つの二点集合の非順序対の同時射影同値で分類する。両領域は交わらず、全対象を覆う。統一定理の証明本文は現行原稿に保持し、個別の論理点検と有限次数の厳密計算を行った。全証明の独立監査は未完了である。外部査読・形式証明・包括的な新規性確定とは区別する。組版等の実際の確認範囲は研究ノートを参照。

## 研究の中心目標：O-marked・potential・avatarの三者対応

**求めるもの：** O-marked quadric $(\mathcal C,\mathcal O)$、線形代数的なpotential（8/10/12矢）、反標準avatar $(Y,D,P)$（$Y=\PP^1\times\PP^1$または$\Sigma_2$、$D\in|-K_Y|$、$P\in\Pic^0(D)$）について、**同型類の明示的全単射**またはそれを誘導する**相対モジュライ射**を構成する。標識・頂点・rulingの忘却、古典点の収縮、自己同値・慣性を明示する。

**滑らかな楕円cubic型で達成：** VdB三線束からsquare avatarは $(F_s,G_s,P)=(L_2,L_1L_2L_0^{-1},L_2L_0^{-1})$、逆は $(L_0,L_1,L_2)=(F_sP^{-1},G_sP^{-1},F_s)$。二cubic開のO-marked同型類は$r_1:(F_s,G_s,P)\mapsto(G_sP^{-1},F_sP,P)$の商。$r_0:(F_s,G_s,P)\mapsto(G_s,F_sP,P)$は一般に$\mathcal O$を変えるので割らない。一般potential→avatarは4枚、O-markedまで8枚（[新定理](papers/quiver-avatar/avatar_charts.tex)）。

**滑らかなnoncubic境界の稠密開で達成：** $G_s=F_sP$、$0\ne P\in\Pic^0(E)[2]$のavatarと$\PP^1$上の四つの相異なる根の非順序二根対は、$|F_s|$と非零2捩れ平行移動を用いて全単射。Bのnoncubic分類と合成してO-marked境界の同型類と対応。ただしavatar由来AS $\qgr$を元のO-marked heartと同一視する直接証明はまだない。

**未解決：** 共有根・一致根対・非被約$D$、$\Sigma_2$最深境界、$P=0$古典点の正しい収縮、potentialの全相対群oidと8/10/12矢のstable equivalence、avatarのAS心とO-markedの相対認識。非零Picardのsquare wallは2次元だが内在noncubic境界は1次元なので無条件の全avatar同一視は不可。これらが今後の優先目標であり、個々のminorの追加は従属課題。

**noncubic全境界の幾何avatar分類と相対spectral中間射（C v2.6）。** Bの二つのsquarefree binary quadric $f_1,f_2$から、四次形式$q=f_1f_2$と種数1二重被覆$C_q:y^2=q$を作る。四次の因子分割Sym²(P²)→P⁴は有限一般次数3で、smooth（四単根）、既約nodal（一重複根）、I2（二重根二つ）の三型。各型の被約二根対の分割個数は3/1/1、対応する非零$\operatorname{Pic}^0(C_q)[2]$の個数も3/1/1。$F_s=p^*O(1)$、$G_s=F_sP$で二rulingの$(2,2)$埋込みを作ると、**全noncubic O-marked幾何同型類と、$P=G_sF_s^{-1}\ne O$, $P^2=O$のsquare avatar同型類が全単射**となる。nodal/I2の明示式も[論文Cのavatar節](papers/quiver-avatar/avatar_charts.tex)にある。

**相対射は通常Picardではなくtorsion-free sheafを経由する。** 中央二重平方環$B_f$の可換化の点曲線$E_f=\operatorname{Proj}B_f^{ab}$を同時符号で割ると$E_f\to C_q$が得られ、その反不変部分$M$がrank-one torsion-free degree0 moduleを与える。$p_*M=O(-1)^2$、$yc=f_1d,yd=f_2c$で基底変更と整合する。smoothでは非零2torsion線束だが、共有根では$A=k[[x,s,y]]/(y^2-x(x-s))\simeq k[[c,d]]^{\pm}$という$A_1$表面特異点の非自由reflexive moduleとなり、一般線束は固定$C$族上の可逆線束へは延長できない。**従って全幾何同型類の全単射は証明したが、元のPic⁰ avatar stackへの相対射・AS $\mathbb Z$代数の同定は未証明。** 次はminimal resolution/Σ₂ elementary transformと元のAS qgrからO-marked heartへの認識を完成する。[根対の厳密検算](computations/verify_rootpair_resolvent_spectral.py)は標準math suiteに登録した。

**Σ₂での全noncubic分類を証明：** 負断面Sを避ける反標準因子D∈|−K_{Σ₂}|と0≠P∈Pic⁰(D)[2]の幾何同型類は、全noncubic O-marked quadricの幾何exact同型類と全単射（C thm:qa-all-noncubic-sigma2-anticanonical-avatar-bijection）。H=O(h)|D=F²、F=O(f)|Dを用いるsquare換算はF_s=F,G_s=FP。P非自明2捩れによりDはsmooth、既約nodal、二P¹二節点(I2)の三型だけ。Bの良moduliでχ=1に重なる一根共有と根対一致も、Σ₂のnodalとI2で区別（C cor:qa-sigma2-avatar-separates-special-noncubic-classes）。これは**体上の同型類全単射**で、avatar AS代数の元のqgr heartとO-markedの直接同値、非被約底の通常Pic⁰線束を使う相対射ではない。

## 論文C：既存GITと内在的モジュライの比較

[論文CのGIT比較節](papers/quiver-avatar/git_comparison.tex)では、非線型geometric quintupleから内在的H2への実際の相対群oid射、Gm⁴スカラー慣性のpointed忘却による消滅、剛体化後smooth純3次元、一般forgetful homotopy fiberの自己同型核・剰余集合を証明している。

**OU2014の群比較・spectral Kummer・quintuple曲線（v1.4）。** 原論文§5 (5.3)は四固有値の全置換S4、しかし(5.8)直後の商表示はS3と印刷されていて不整合がある。(5.3)の不変式環から導く**訂正解釈**は **P³/S4_coord→P³/(S4_coord⋉(Z2)³)**。有効符号群はF2²、全有効群は96元。座標S4の作用核Klein四元群を除いたGalois閉包のmonodromyは別のS4（24元）で、一般の次数4射は非Galois。この四重射は線型monodromy S3の変動有限群局所系𝒱のtorsorとして構成できる。OU§4楕円四つ組の二つのE[2]平行移動群の半直積と、**index4部分群を含めて抽象群が一致**することも証明した。この群同型は両表示の幾何的な同変双有理同型をまだ与えない。

**新しい実証結果：** 対角値x_iの二乗を四分岐点とするspectral曲線 y²=∏(t−x_i²)、∞+を原点、P+=(0,∏x_i)としたとき、OU四重射は **[2]^{-1}(P+)** に相対的に同型となる。明示式は t0=−s3/s1、y0=−(t0²+s2t0+s4)。四半点の厳密検算は[専用コード](computations/verify_ou_spectral_halving.py)で再現できる。四つの分岐点自身の半点torsorはOU四重射とmonodromy核が異なり、区別が必要。**さらに対角potential quintupleの点曲線は q(u)=q(Xu)=0 の二quadric完全交叉であり、Jacobianは同じspectral曲線**である。quadric pencilのruling被覆≅Pic²(C)を使い、OU不変量からのj公式を証明した。**さらにHodge対合でP+↔L2のruling符号を確定し、対角の滑らかな稠密開ではOU四重torsorと指定NのPicard[-2]根torsorを同型にした。** 偶数符号・S4置換・スカラーに関してJacobianと指定点がG同変に降下する。正則半単純な非対角potential族には相対HodgeでJacobian・指定点・明示半点を任意底変更と可換に構成した。potentialを選ばない一般quintuple族・GIT全体のuniversal曲線・慣性/pointed fiberは未解決である。


**一般GITから内在H2への比較（C v2.1）。** OU2014一般quintupleのスカラーGm⁴剛体化後にもμ₂²の慣性が残り、点曲線Jac(C)[2]の平行移動としてpointed H2へ忠実に写る。quintupleの16次元表示空間／13次元有効群はsmooth純次元3。Bの[普遍非線型cubic smooth atlas](papers/moduli/h2_smooth_atlas.tex)を使い、剛体化quintuple→内在H2は**全非線型geometric locusでsmooth相対次元0**と示した。正則半単純一般開では慣性単射から表現可能étaleで、Kodaira–Spencerは `k⁴/kx≅HH²(Λ)`、`HH¹(Λ)=0`、`dim HH²(Λ)=3` となる。Bの[二つのnormalized foundation](papers/moduli/foundation_stack.tex)と[楕円ruling交換](papers/moduli/marking_forgetting.tex)の `R:(η,δ)↦(2δ−η,δ)` から、一般 `j≠0,1728, δ∉E[2], η−δ∉E[2], η∉{0,2δ}` で二つのfoundationは非同型。したがって忘却は稠密開で**有限étale次数2**、pointed自己同値の全慣性はμ₂²。別の有効potential→quintuple表示射の一般次数4を合成すると、potential→内在H2は一般次数8となる。これはPicard根四選択やH2のroot付き忘却次数とは異なる。証明は[論文CのGIT比較節](papers/quiver-avatar/git_comparison.tex)の `thm:qa-quintuple-h2-generic-etale`、`cor:qa-quintuple-h2-generic-degree-two`、`cor:qa-potential-h2-generic-degree-eight`。特殊cubic/noncubic点のfiber・慣性・分岐、一般二枚にcanonical S₂ deck対合があり、稠密開では **H2 ≅ [quintuple剛体化表示/S₂]** のArtinスタック同値まで証明した（[商表示定理](papers/quiver-avatar/git_comparison.tex)）。**特殊ruling交換の正確な条件：** j(E)≠0,1728、δ≠0、η∉{0,δ,2δ}なら、二つのnormalized foundationを交換するpointed自己同値が存在することとδ∈E[2]またはη−δ∈E[2]は同値。正則半単純な特別点の全pointed慣性の位数は8。正則半単純特別点ではsourceの同型類が一つでも、Aut_H2/Aut_quintupleの二剰余類により相対2-fiberは二点のまま。既存の表現可能étale性からstack忘却はこの点でも非分岐。二つの二捩れ条件の片方だけが成立する正則半単純・j≠0,1728点では、η−δ∈E[2]非零のtranslation型はC₄×C₂、δ∈E[2]非零の反転型はC₂³と、全pointed慣性群の型も決定した。二条件同時・j=0,1728・粗モジュライの局所分岐と法表現、mutationのcoherentな拡張・全体への延長は未解決。Bのsmooth atlasの全証明は今回全面再検証していない。厳密な有限群・接軌道rankの検算資産：[script](computations/verify_ou_quintuple_inertia.py)。

**特殊二捩れ座の粗分岐と交点（C v1.9）。** $δ,η-δ$ の二捩れ性は、OU対角値の二乗の基本対称式 `e1,e3` と `c=∏xᵢ` で `e3+e1c=0`、`e3−e1c=0`。quintuple GIT不変式 `D±=f2³−3f2f4+2f6±6f2g4` を使うと、`f2g4≠0` かつ滑らかな正則半単純の二cubic開（`j=0,1728`も許す）で、粗忘却の分岐座は `D+D−=0`。片側特別座ではpointed慣性の接法表現は `diag(1,1,−1)` で、局所粗射は `Z=z²`。**両条件の交点** `e1=e3=0` ではquintuple慣性 `C2³`、H2慣性 `D8×C2`（D8は位数8）、粗局所射は `k[[s,a,c]]→k[[s,a,b,c]]/(b²−ac)` と横断A1特異点を持つ。例は `x=(1,2,i,2i)`。粗射が分岐してもスタックの忘却射はétaleのまま。証明正本は[論文Cの比較節](papers/quiver-avatar/git_comparison.tex)、再現は[厳密検算コード](computations/verify_ou_special_reflection.py)（計算は一般証明そのものではない）。j=0,1728・noncubic・全GITへの延長やglobal coarseの存在は未解決。

**複素乗法と一cubic境界（C v2.0）。** 滑らかな楕円四つ組で両normalized rulingがcubicなら、複素乗法が増える`j=0,1728`でも追加の位数3/4/6自己同型は三つの次数二線束を保存せず、ruling交換も誘導しない。従って二捩れの交換判定・反射の粗分岐・交点のA1局所型はCM値にも拡張できる。CMでは`j`自身は曲線変形の座標でなく、フルlevel2のLegendre `λ` を用いる（jの零点は3重、j−1728の零点は2重）。一方、`η=2δ`、`δ∉E[2]` の**一cubic境界**では第二foundationがnoncubicとなり、quintuple→H2はpointed étaleのままfiberが一点になるため、一般の有限étale二重射は延長不可。特に`j=0`、非零3-torsion `δ` が位数3のCM自己同型に固定される例 `E:y²=x³+1, δ=(0,1), η=(0,−1)` では、全pointed慣性`A4=E[2]⋊C3`、三次元接の有効C3重み`(2,1,1)`、局所粗形式環は孤立巡回商特異点`k[[a,u,v]]^{C3}`。証明は[論文Cの比較節](papers/quiver-avatar/git_comparison.tex)、有限群・Legendre計算は[検算スクリプト](computations/verify_ou_cm_automorphisms.py)。Bの相対mutationで欠けたnoncubic sheetを補完することが次の課題。

**全内在的H2の二ruling被覆とfinite foundation開認識（C v2.4）。** Bのfinite type smooth atlasはcubic/noncubicの各chartにflat compact normal foundationを持ち、相対mutationが第二foundationを任意の非被約基底変更と可換に構成する。atlasの関係群oid上で$\operatorname{RHom}(X,X')$の導来fiberが$k[0]$または零となるため、開閉分解から$S_2$-cocycleを作り有限étale次数2の$\mathfrak H_2^{\mathrm{rul}}\to\mathfrak H_2$へfppf降下。さらに相対End代数・反Serre環の全忠実性・Bの有効Artin/étale chartから、$\mathfrak H_2^{\mathrm{rul}}$はfinite foundationの滑らかな表示スタック$\mathfrak F_0$の**開部分$\mathfrak F_{\HH}$**に同型。**全相対スタック同型$\mathfrak H_2\simeq[\mathfrak F_{\HH}/S_2]$** を証明（[論文Cの定理](papers/quiver-avatar/git_comparison.tex)：`thm:qa-global-two-ruling-etale-cover`, `thm:qa-intrinsic-h2-open-in-foundation-stack`）。一cubic境界ではquintuple側の二枚が一枚になるが、内在的選択被覆はnoncubic foundationを含む二枚を維持する。これは$\mathfrak F_0$の全点が実現可能であることや、全avatar・potential群oidとの同値ではない。さらに可換二次曲面のAut $(\mathrm{PGL}_2\times\mathrm{PGL}_2)\rtimes C_2$のfactor交換により、この全被覆には大域的な自己同値不変sectionがない。また実現可能開の$U_0\subset\mathbb A^{64}$への逆像は開なので、有限個の多項式の非同時消滅で判定できることはNoether性から存在証明できる（具体式・次数上界は未計算）。[Cの有限多項式系](papers/quiver-avatar/git_comparison.tex)と可換gerbeの系を参照。次は実現可能開を明示的に計算し、境界と全相対AS認識を調べる。

**cubic幾何部分の明示四次・六次判定。** 2×2×2×2 tensor wの隣接二因子flatteningを4×4行列M_i（i=0,1,2,3）とする。VdB geometric条件は、各iについて det M_i≠0、またはadj(M_i)のある列を2×2へreshapeした行列式が非零、と同値。rank3では核が非分解可能なときだけ許容し、rank≤2は拒否。四次式4つ・六次式16個を使う開条件である（[有限foundation節の補題](papers/quiver-avatar/foundation_charts.tex)）。[検算コード](computations/verify_cubic_geometric_adjugate.py)を標準math checksへ登録。これは全realizable開のexplicit条件ではなく、F可逆のcubic幾何部分に限る。

BのPicard[-2]根はsmooth ellipticでは4点、既約nodalでは2点、cuspidalでは1点。OU楕円z2のE[2]平行移動は四つの根に対応し、**対角滑らかな一般開**ではOU四重torsorとPicard根の一致を証明済み。一般quintuple→内在H2の一般全慣性・接同型・二点fiber、さらに滑らかな楕円型の二捩れ特別座とその局所粗分岐は解決。全H2のnormal foundation二択と有限表示開への比較を得た。次はその実現可能開の計算的有限判定と、noncubic境界での明示的慣性・fiberを調べる。nodalを含む連結基底に有限OU射と非有限Picard根をそのまま同型に延長できない。検算：[有限群](computations/verify_ou_fourfold.py)、[半点・j](computations/verify_ou_spectral_halving.py)、[Hodge符号](computations/verify_ou_hodge_ruling.py)。

## 八本・十本・十二本矢と avatar

独立した公表用草稿 [papers/quiver-avatar-moduli.tex](papers/quiver-avatar-moduli.tex) に、表示モジュライ・反標準 avatar・内在的忘却の関係をまとめた。主論文は全H2のpointed分類と相対認識を、別稿は矢数の層別と幾何的chartを扱う。

| 対象 | 確立した関係 | 留保 |
| --- | --- | --- |
| 有限 foundation | Hom次元 $(2,2,2,4,4,6)$ の結合律 $c(1\otimes a)=d(b\otimes1)$ から有限型Artinスタック $\mathfrak F_{\le12}$ を構成。二つの10本矢開部分の交わりが8本矢部分 | AS条件・滑らかさ・相対H2認識はこの構成に含めない |
| 重み付きQP | 二つの可逆な二次係数で対角pairを消去。Jacobian代数のモジュライでは8→10→12は開埋め込み | 生のright-equivalence商には消去pairの $\mathbb G_m$ 慣性が残る |
| 曲線型avatar | $P\in\operatorname{Pic}^0(D)$、$P\ne\mathcal O_D$。$H\mapsto HP$ による再埋め込みから二つの10本矢開部分と交わりの8本矢部分を構成 | 全相対AS代数とのスタック同値は未証明。AS最小矢数との辞書は明示した未公刊分類入力による |
| 直積型square | 全 $(2,2)$ Cartier因子と非自明な $\operatorname{Pic}^0$ は、一方の非最小10本矢chartに対応 | 最小10本矢はその境界。元のproduct collection自体は有限8生成矢・4関係、relation completionは12本 |
| $\Sigma_2$ 境界 | 負断面 $S$ と交わらない因子は一方の10本矢境界、$S\le D$ は最深12本矢層 | $\Sigma_2$ の出現だけで12本矢とはいえない。$P=\mathcal O_D$ の古典点は別途扱う |
| 内在的忘却 | 相対heart・適合平方根・AZ豊富性・同じ根のAS4被覆を満たす部分から $\mathfrak H_2$ への射。全H2幾何点は10本矢normal foundationを持つ | その適合部分の開性は未証明。$\operatorname{coh}\mathbb P(1,1,2)$ と $\operatorname{coh}\Sigma_2$ の構造対象は強いH2条件を満たさない |

証明は [有限QP](papers/quiver-avatar/qp_presentations.tex)、[有限foundation](papers/quiver-avatar/foundation_charts.tex)、[avatar](papers/quiver-avatar/avatar_charts.tex)、[内在的忘却](papers/quiver-avatar/intrinsic_forgetting.tex) に置く。独立読取り・計算・組版の実施範囲は研究ノートを参照。

## 相対構成の現在地

内在的H2は有限型・smooth・既約・純次元3のArtinスタックで、対角はaffine有限表示。cubic開は稠密で、被約noncubic境界Nはsmooth既約純次元1、正則閉埋込みcodim2である。framed実現空間X_asはsmooth既約83次元スキーム。一致根対ではambient接次元84のため、実現像は開でない。

**被約境界の相対商表示と良モジュライ。** `thm:noncubic-intrinsic-presentation-equivalence` により、局所有限型site上で Npres=[P/G]≃N が対象・pointed exact同型を含めて成立する。境界chartの相対normal tiltingと反Serre再構成から実際の族を比較し、慣性核の消滅・接全射・同次元性から表現可能étale性を証明する。非被約testも含むが、全fiber noncubicだけでNへの因数分解を主張しない。χ:N→A¹はflat有限表示のgood moduliで、χ=0はsmooth被約因子の二重構造、χ=1はsmooth chart上ac=0。全慣性は四根相異χ≠0でD8×C2、χ=0で位数32非分裂拡大、一根共有でD8、一致で((Gm⋊C2)×D8)/μ2（8成分）。一致類はBGの正則閉埋込みcodim2をなし、境界接の重みは±2、全HH²は±2,0,0、横断法二方向には連結慣性が自明に作用する。任意の代数空間へのH2の射は一根共有と一致類を同一視するため、全H2にも幾何同型類を分類する粗モジュライ代数空間は存在しない。証明は `papers/moduli/noncubic_boundary_comparison.tex`。

**DM開の粗モジュライ。** 一致類を除いた N^DM→A¹_χ は任意の代数空間に対する粗モジュライ射であり、任意の底変更後も粗モジュライである。この制限射χ_DMはgood moduliではなく、慣性射はproperでもfiniteでもない。二つの根対を順序付けたchartを [A¹/μ2] に帰着し、有限被覆を持つ商の普遍性で粗モジュライを証明する。非good性はcodim2補集合のHartogs、慣性の非proper性はDVR上で延長しない具体的自己同型による。`thm:noncubic-dm-coarse`。

**一致類に沿う形式対と局所良モジュライ。** 全慣性 H=((Gm⋊C2)×D8)/μ2 の有限成分も含むHH²作用を決定した。トーラスの非零重み部分と零重み部分による標準的分裂を用い、境界接を(a,c)、法方向を(x,y)とすると、トーラスの重みは(2,−2,0,0)、二つの符号は法方向に−Id、u,v交換は(a,c)を交換して法方向に−Id、ruling交換は境界接に−Id・法方向の交換として作用する。ruling交換は相対mutationで全Artin変形上に同定する。非標準的な形式対は ([Spf k[[a,c,x,y]]/H], [Spf k[[a,c]]/H]) で、境界はx=y=0、不変式環は k[[ac,(x+y)²,(x−y)²]]。AHRの共通étale商近傍はsmoothな3次元good moduliを持つ。これはH2のZariski開や全体のgood moduliの存在をまだ意味しない。`prop:noncubic-coincident-full-normal-representation`, `thm:noncubic-coincident-formal-pair`, `cor:noncubic-coincident-polynomial-invariants`。

相対構成の依存は、cubicの普遍Noetherian性・相対Picard根・canonical AS4 hull、noncubicの有限LG認識・非被約normal tilting・全軌道比較・Noetherian貼合せ・中央AS4延長で閉じる。全幾何点でArtin形式H2変形はpointed Abel変形と一致する。各定理の仮定・証明先・確実性は [研究方針](00_research_plan.md#3-到達点と確実性) に集約する。

**残る比較と次の課題。** 境界の相対商表示・DM開の普遍的粗モジュライ・全有限成分の法表現・一致類に沿う形式対は証明した。次は、共通étale近傍のgood moduliをH2の開部分または全体へ降下できるかを調べる。全H2のgood moduli spaceの存在は未確定であり、全H2の粗モジュライ不存在とは別の問題である。X_asの局所閉性と偏極認識方程式、Q_fndとの全体の相対groupoid比較、任意Noetherian基底で素朴に同じAbel公理を課す関手と[U/R]の一致も残る。公表前の一次文献比較・証明監査・組版を続け、包括的新規性・外部査読・形式証明とは区別する。

## モジュライのスタック構成

体上の対象クラスを $\mathcal H_2$、有限型基底上の内在的な相対族の fppf スタックを $\mathfrak H_2$ と書く。**相対族の定義、stack 性、反 Serre 関係式への全忠実性を構成した。全体が有限型で滑らかな純次元3のArtinスタックとなる。** 主な証明は [相対定義](papers/moduli/relative_definitions.tex)・[反Serre認識](papers/moduli/relative_recognition.tex) に置く。

有限foundationと次数移動の可逆perfect双加群表示が得られた基底では、次数移動が反Serre関手と線束twistを除いて一致する条件を、**有限表示局所閉部分スキーム**として構成した。非被約底のminor方程式と評価同型を用い、比較のfppf局所存在そのものを表す。[偏極認識の証明](papers/moduli/polarization_recognition.tex)。任意のX3族にこの有限表示を与えること、平方根・AS被覆の局所存在は引き続き別の課題である。

**Artin基底ではさらに進んだ。** 全flat Abel変形に有限foundationとcanonical反Serre軌道環を構成でき、偏極忘却は右逆を持つ。一次の核はHH¹(Λ)であり、二根対一致点の接次元5対4の差をZhang方向として説明する。HH¹(Λ)=0なら全Artin X3変形はcanonical偏極を持つ。異なる根対の全noncubic点ではX3は滑らかで次元83、商は滑らかで次元3となる。[Artin再構成](papers/moduli/artin_foundation.tex)。可換Qのtensor O(1,1)は全Artin Abel変形へexact ampleなSerre根として持ち上がり、そのMorita同型類は一意である。[根の存在と一意性](papers/moduli/artin_roots.tex)。

**可換点の全Artin変形は相対H2に属する。** 二周期cubic列のcanonical hullをArtin基底上で構成し、標準根の全軌道環に相対AS4被覆と正則正規二次切断を与えた。全有限型基底変更を含む昇格命題と合わせ、可換Qの全flat pointed Abel Artin変形が実際の相対H2対象になる。H2からAbel圏への忘却は、この点を中心とする形式変形groupoidの同値であり、変形は無障害、接次元9・無限小自己同型次元6である。[全Artinのhullと形式変形](papers/moduli/quadric_artin_hull.tex)。一次方向については、Jacobian二重導分と右Zhang twistによる[明示構成と検算](papers/moduli/quadric_first_order.tex)も保持する。全cubic点では相対Picard根とquintuple持上げを用いることで、根のHH²自明作用を追加仮定せず全Artin認識が成立する。noncubic点でも中央被覆の局所延長により全Artin認識が成立する（`cor:noncubic-all-artin-h2`）。全H2の有限型代数性は `thm:global-h2-smooth-finite-type` で成立する。

**標準平方根はétale近傍へ代数化できる。** 有限foundation表示上のMorita自己同値の代数空間と平方写像を使い、可換点の標準根を実際のperfect双加群と平方同型としてétale近傍へ延長した。[根の代数化](papers/moduli/artin_roots.tex)、`prop:quadric-etale-morita-root`。その近傍では、標準foundationに対して根がF0→F2、F1→F3と作用する同型を構成し、全四項窓のfull strong exceptional性、Hom階数2/4/6/9、三次関係rank2・四次重なりrank1の非退化性を任意底変更について証明した（`prop:quadric-etale-finite-window`）。全距離のHomと三次提示は上記の相対解消で解決した。canonical compact/Serre認識は相対cubic tailsの証明で成立した。単一有限型開上の左右Noetherian性と相対H2実現は上記の定理で成立した。相対H2全体の代数性は下記の有限型atlasで成立する。特殊fiberのrankと非退化性の独立な厳密検算は [`verify_quadric_finite_windows.py`](computations/verify_quadric_finite_windows.py) に収録した。

族は基底変更と descent を備えた noetherian Abel 圏と構造対象 O の対である。導来条件には局所的な canonical compact 部分 $D(\operatorname{Ind}\mathcal C)^c$ を用い、特異基底上でそれを全 $D^b(\mathcal C)$ と同一視しない。平方根・根同型・AS被覆は fppf 局所の存在条件であり、標識に加えない。標数零の代数閉体上では元の $\mathcal H_2$ の pointed groupoid を回復する。

| 相対モジュライに関する結果 | 状態・証明の所在 |
| --- | --- |
| $\Phi:\mathfrak H_2\to[X_3/\mathrm{PGL}_9]$ は全忠実 | 相対AZ再構成とpointed二自己同型の自明性。[相対定義節](papers/nc-quadric-moduli.tex) |
| 対角はaffineかつ有限表示 | 表示スタックの対角の引戻し。同節 |
| $X_{\mathrm{as}}=X_3\times_{[X_3/\mathrm{PGL}_9]}\mathfrak H_2$ は不変fppf部分層、$\mathfrak H_2\simeq[X_{\mathrm{as}}/\mathrm{PGL}_9]$ | 有限型smoothスキームX_asによる商表示。dim X_as=83、dim H2=3。`cor:global-xas-smooth-scheme` |
| 全H2の切断環・反Serre環はKoszul | 正則正規二次商とVeroneseの既知定理を適用。[相対Koszul節](papers/moduli/relative_koszul.tex) |
| 三次まで平坦＋全幾何fiberがKoszulなら全次数平坦 | PP2005 Chapter 6 Theorem 7.3を任意の非被約Noetherian基底に適用。相対Koszul解消も任意底変更と整合 |
| H2点の任意のArtin基底上の $X_3$ 変形はflatなpointed Abel変形を与える | noetherian性の持上げと $\operatorname{qgr}$ による構成。同節。表示の次数移動が反Serreになることは別条件 |
| Artin上の根・全軌道AS被覆から、全有限型基底変更を備える相対H2族を構成 | [Artin再構成節](papers/moduli/artin_foundation.tex)、prop:artin-witness-relative-promotion |
| 可換Qの全Artin Abel変形は相対H2、形式変形groupoidの忘却は同値 | 相対canonical hullと全有限型基底変更への昇格。無障害、接HH²(Q)は次元9・無限小自己同型HH¹(Q)は次元6。[全Artin節](papers/moduli/quadric_artin_hull.tex)。大域代数性とは区別する |
| 固定した相対切断環へのAS4被覆は有限表示のincidenceで判定できる | 四次までの元の積・五次までの二次双対・Frobenius条件。[相対被覆節](papers/moduli/relative_as_cover.tex)。任意基底変更のnoetherian性は明示した仮定の範囲で用いる |
| pointed Abel圏が一定で、反Serre表示からは外れる $\mathbb G_m$ 上の二次環族 | [偏極の変形](papers/moduli/antiserre_polarization.tex)。$q=2$ で中心一次部分が消滅し、どのH2のcanonical反Serre環でもない |
| 同族の非零接方向は一定のpointed Abel変形へ写る | 中心元 $u^4,v^4$ の交換子が $16\varepsilon u^4v^4$。計算機に依存しない証明と[厳密検算](computations/verify_antiserre_polarization.py) |

$X_3\subset\mathrm{Gr}(56,81)$ は三次関係行列の階数がちょうど176となる局所閉スキームであり、商は有限型Artinスタックである。その全体を $\mathfrak H_2$ と同一視できないことは、上記の偏極変形で幾何点についても明示した。有限型incidenceのfppf像は一般には代数空間とは限らないため、AS被覆を選ぶ空間の構成だけで存在条件の代数性を結論しない。

既存の foundation 表示 $\mathfrak Q_{\mathrm{fnd}}$ は滑らかな有限型Artinスタックで次元3、ruling交換を忘れる写像は有限étale二重被覆である。全H2幾何点groupoidが全充満に入り、cubic非空開と全noncubic点へのpointed smooth proper dg特殊化を持つ。反Serre環としても全次数平坦な特殊化となるが、これらの族が相対H2の全条件を満たすことは未証明である。[foundation節](papers/moduli/foundation_stack.tex)

noncubic表示商 $\mathfrak N^{\mathrm{pres}}$ は滑らかな有限型Artinスタックで次元1。全幾何点のpointed慣性、符号 $\mu_2^2$ gerbe、good moduli $\mathbb A^1_\chi$、coarse moduli algebraic spaceの不存在を記述した。相対Clifford表示、perfect Serre公式、選択不要な反Serre環とそのnoetherian heartも構成済みである。[noncubic節](papers/moduli/noncubic_stack.tex)

noncubicの三代表点では $\dim HH^1(R)_0=(1,1,2)$、$\dim HH^2(R)_0=(3,3,5)$。関係式の接次元は正確に83,83,84で、群軌道と六係数の和は81次元である。横断2,2,3方向の全二次障害が消え、既存の二次jetは上記Koszul原理により全次数平坦となる。二根対一致点における $X_3$ 商とfoundation商の接次元5対4は、相対H2の接次元は別途Abel変形と比較し、一致根対で4と証明した。

**成分に関する現在の結論：** foundation実現点集合は誘導位相で既約・連結、成分数は各1。cubic/noncubicの表示商の非交和は人工的に2成分になる。内在的 $\mathfrak H_2$ 自身も、実際のcubic族と境界chartによって既約・連結、成分数各1と証明した。foundation表示の誘導位相との同一視はこの証明に使わない。

**Noetherian 性の形式的貼合せ。** 可換Noetherian基底R、各次数成分が有限な中央次数環A、I=(f₁,…,fᵣ)に対し、A/IAと全A[fᵢ⁻¹]が左右NoetherianならAも左右Noetherianとなる。次数ごとのI進完備化で有限生成元の係数を収束させ、R̂_I×∏R[fᵢ⁻¹]の忠実平坦性で降下する。成分の平坦性・有限Krull次元は不要で、一般次数付き加群とZ代数のrow/columnにも成立する。証明 `thm:patch-noetherian`、`thm:patch-z-algebra`。幾何的cubic族では、閉部分と開補集合で実際のNoetherian性を確認して適用する。

**非可換P¹束の対角列の障害。** 滑らかな(2,2)曲線と次数二線束から全隣接縮約が非零のgeometric quintupleを構成した。しかし対応する層対称代数の候補対角列Kₙ=π(O(n)⊗e₋ₙA)は、全ての行からHomが零になる非零coherent対象を持ち、AZ生成条件を満たさない。二次解消を用いて全整数でωπMの成分がO(−2)となることを直接証明した。これは当該模型・軌道列の比較への障害であり、本来のcubic環BのNoetherian性の反例ではない。[対角列の反例の完全な証明](papers/moduli/ruled_diagonal_obstruction.tex)（論文B）。本来のBのNoetherian性は、曲線商・正規拡大とlinear部分の形式的貼合せによって解決した。

## 対象

`(C,O)` を構造とし、`O`はGabriel–Krull rank-one torsion-free exceptional。`Db(C)`はHom有限でSerre関手`S`を持つ。exactな平方根 `s² ≅ S⁻¹[2]` が存在し、同じ`s`について `(O,s)` がArtin–Zhang ample、切断環が

$$
B(C,O,s)\simeq A/(g)
$$

と書けることを要求する。`A`は左右noetherian quadratic Koszul AS-regular型`(1,4,6,4,1)`、`g∈A₂`は左右正則正規。**s、根同型、ambient、方程式、例外列は追加標識ではない。** 分類の同値はOを保つexact同値である。

通常のquadratic envelopeは二次曲面の式も含むので、可換quadricでもambientにはならない。そこでAS正則な二次被覆の**存在**を使う。H2の「2」は超曲面次数であり、可換quadricの反標準次数は8。

## 主結果と構成

- 平方根条件から圏の大域次元2、rank-one torsion-free条件から切断環のdomain性を証明。
- 被覆からHilbert関数`dim B_n=(n+1)²`、二次関係7本を導出。固定Bの被覆は `Gr(6,ker(B1⊗B1→B2))` の許容部分へ還元。
- 同じ可換quadricに対する非可換Ore ambientの族を構成。quotient mapを固定した被覆は非一意。
- 滑らかな射影整曲面として実現される可換対象は`P1×P1`に限られ、rank-one torsion-free exceptional標識は線束。条件に適合する平方根関手はpointed exact共役を除いて4種類であるが、O-marked対象は一つ。
- 複素数体上、無限位数の平行移動を持つ通常の楕円型Sklyanin pencilの滑らかな成員がH2に入ることを確認。`z=τ`の成員は、単純対象の自己Euler特性2により`coh(P1×P1)`とexact同値でない。
- 反Serre切断環は9生成・56次元の二次関係を持ち、その関係空間の線形同値がpointed exact同値の必要十分条件となる。
- 滑らかな無限位数Sklyanin型では、rulingを適切に選ぶとcubic Z-algebraへの比較が得られる。反Serre環の中心から楕円商を回復でき、全て可換quadricとpointed exact非同値である。
- 正規切断の中心性、standard性、ambientの追加条件(*)を要せず、全H2対象は四周期の三次元AS正則Z-algebraとして表せる。non-standardでは二つのrulingを交互に置く。
- 比較先がVan den Berghのcubic型となる条件は、偶数項間の隣接合成の階数が4となること。階数3では距離二の生成元と関係が各一つ加わる。二型とも階数3の対象は別表示も含めてcubic型で覆えない。両領域の構成・全被覆・同値判定を主定理にまとめた。相対モジュライの完成は別問題であり、上記の表示スタックと比較している。

既知結果、初期原稿内の証明、計算、外部監査・形式証明・新規性確認を区別する。正確な範囲は [研究ノート](notes/research_notes.md) と [文献比較](notes/literature.md) を参照。

- 全ての許容四つ組から構造対象と適合根を構成した。整な曲線、被約な二・三・四成分、二重(1,1)、片方または両方が重複したgridで、周期の平方とSerre移動を比較した。一般のeven partのdomain性にはPresottoの定理を使う。
- 二次Koszul環Bが与えられれば、型14641の正則正規被覆の存在は四次までの元の積と五次までの二次双対で判定できる。
- 固定Sklyanin pencilの明示的な開領域では、中心の一次近傍により各切断の比較を高々64候補に絞れる。持上げ変更の単射性は無限位数の場合に自動的であり、この簡約に残る開条件は中心変形写像Δの単射性である。全分類では仮定を要しない四生成判定を使う。厳密計算は `computations/verify_pencil_tangent.py` に収録した。
- 重み付き四周期環の単純分解から周期偶数環のKoszul性が従う。逆構成に残る条件を、分解の完全性、周期、domain性、斉次切断の長さ、有限被覆判定に絞った。

- 四変数の多パラメータskew polynomial環の正規二次切断を完全に分類した。非cubic型一点とcubic族があり、後者はパラメータr²を逆元で同一視する。
- 中央二変数を持つOre環 yx=qxy+h も退化を含めて分類した。可換類と、二つの非退化二次形式の根の対で判定される非cubic族が現れる。

- 全非cubic対象は二つの非退化二次形式を持つ中央二重平方環へZhang同値で帰着する。non-standardな適合表示を持つのは、二つの根対が一致する一点だけである。固定表示内での線形基底変更による中央化とは区別する。

## 現行資料

| ファイル | 役割 |
| --- | --- |
| [papers/moduli/relative_cubic_tails.tex](papers/moduli/relative_cubic_tails.tex) | 普遍cubic解消、canonical導来比較、Noetherian基底での全相対認識 |
| [00_research_plan.md](00_research_plan.md) | 研究一般の原則・保存許可、目標、到達点、次の具体的な着手 |
| [CLOUD_CODEX.md](CLOUD_CODEX.md) | Cloud環境の準備、起動用の依頼文、検証・保存・再開の手順 |
| [scripts](scripts) | 依存の準備と、構成・検算・組版の独立した確認 |
| [papers/nc-quadric-classification.tex](papers/nc-quadric-classification.tex) | 本文のある主論文。日本語LuaLaTeX、著者欄空欄 |
| [papers/quiver-avatar-moduli.tex](papers/quiver-avatar-moduli.tex) | 八・十・十二本矢、avatar、内在的忘却を扱う独立した日本語LuaLaTeX論文 |
| [papers/quiver-avatar](papers/quiver-avatar) | 別稿の有限QP・foundation・幾何的chart・忘却の証明 |
| [papers/sections](papers/sections) | 主分類定理、全被覆、逆構成、同値判定、基準例の証明を収めた分割節 |
| [papers/references.bib](papers/references.bib) | 確認した一次文献の書誌 |
| [notes/research_notes.md](notes/research_notes.md) | 証明状態、障害、再開に必要な知識、検証範囲 |
| [notes/ore_quadric_deformations.md](notes/ore_quadric_deformations.md) | 相対変形を試すOre族の証明稿。相対CY・Serre・H2認識は未証明 |
| [notes/literature.md](notes/literature.md) | 文献の版・仮定・適用範囲・リンク |
| [computations/verify_reducible_quadruples.py](computations/verify_reducible_quadruples.py) | 全非整曲線型の三次関係・四次テンソル・周期平方・必要な貼合せの記号恒等式 |
| [computations/verify_antiserre_polarization.py](computations/verify_antiserre_polarization.py) | 一定qgr・非一定偏極族の接軌道階数と中心一次部分を厳密に検算 |
| [computations/verify_noncubic_second_order.py](computations/verify_noncubic_second_order.py) | 三基準点の横断接方向の二次Schur障害を、全有理補正の整数恒等式として検証（NumPy・Numbaはオプション） |
| [computations/verify_noncubic_degree3_tangent.py](computations/verify_noncubic_degree3_tangent.py) | 法101でPGL9/係数接方向と、三次Hilbert階数条件の全16072線形条件を厳密検算（NumPy・Numbaはオプション） |
| [computations/verify_noncubic_antiserre_pivots.py](computations/verify_noncubic_antiserre_pivots.py) | noncubic反Serre環の9生成元・25 unit pivotと六係数の多項式回収を正確に検算 |
| [computations/verify_stack_symmetries.py](computations/verify_stack_symmetries.py) | noncubic慣性の射影群関係、χの共変性、局所対合・正則切断の記号恒等式 |
| [computations/verify_commutative_quadric_tangent.py](computations/verify_commutative_quadric_tangent.py) | 可換点の関係式接89・軌道74・商接15を整数核と法101のrankで標数零において認証（NumPy/Numbaはオプション） |
| [computations/verify_quadric_first_order_roots.py](computations/verify_quadric_first_order_roots.py) | 一次Jacobian被覆の中心性、affine bracket、九次元制限、四根の固定次元9/3/5/3を厳密検算 |
| [computations/verify_quiver_avatar_charts.py](computations/verify_quiver_avatar_charts.py) | Sigma0・Sigma2・10本矢の有限代数とproduct collectionの矢・関係数を厳密検算 |
| [computations/verify_quadric.py](computations/verify_quadric.py) | Segre積・Ore正規性・低次数階数の厳密演算による再現 |

## 再生成

現行ソースの参照確認、今回の公開計算コードの再実行、組版・画像確認の範囲は [研究ノート](notes/research_notes.md#検証範囲と再現手順) を正本とする。機械チェックは数学的証明や新規性の認証ではない。外部査読、形式証明、包括的な新規性判定は未実施である。

主論文v1.44のsourcesはPASS（50 manuscript files / 610 labels / 288 citation uses / 7 Markdown files）。DM開・全有限慣性作用を含む `verify_noncubic_boundary.py` と `verify_stack_symmetries.py` はPASS。buildは必要なTeX依存不足によりSKIP（終了コード2）で、新しいPDF・画像確認はない。既存v1.40の組版記録は研究ノートに保持する。

repoルートで実行する。

```sh
bash scripts/bootstrap.sh
python3 scripts/check.py doctor
python3 scripts/check.py all
```

別稿は次で個別に確認・組版する。

```sh
python3 scripts/check.py sources --manuscript papers/quiver-avatar-moduli.tex
python3 scripts/check.py build --manuscript papers/quiver-avatar-moduli.tex
python3 computations/verify_quiver_avatar_charts.py
python3 computations/verify_quadric_first_order_roots.py
```

出力は `build/quiver-avatar-moduli.pdf` と同名の `.synctex.gz`。ルートの `latexmk` は両論文を組版する。

Python 3.9以上とSymPy、およびLuaTeX-jaを含むTeX Live/MacTeX、latexmk、BibTeXを用いる。出力は `build/nc-quadric-classification.pdf` と同名の `.synctex.gz`。PDF・組版中間物はGitで追跡しない。

`sources`・`math`・`build`を個別に実行できる。検証の終了コードはPASS=0、FAIL=1、SKIP=2で、未導入の依存による未実施を成功と区別する。`doctor`は診断のみ。bootstrapは不足依存を`PARTIAL`と表示して処理を終え、数学的研究を止めない。TeX導入を試すオプションは`bash scripts/bootstrap.sh --with-tex`。従来どおり`python3 computations/verify_quadric.py`と`latexmk`も使える。

VS Codeではrepo全体を開き、LaTeX Workshopの推奨拡張と既定の `latexmk (LuaLaTeX, project settings)` レシピを使う。設定はresearch-hubの雛形に準拠し、`.latexmkrc`がエンジン・作業ディレクトリ・出力先を統一する。VS Code UIの操作確認とコマンドによる組版確認は区別する。

## 構造対象の忘却

**楕円型の全O標識と有限・無限の忘却。** 滑らかな楕円四つ組でδ≠0、η∉Zδなら、RTと対角根から全Z²のrank-one torsion-free exceptional対象を構成し、数値類ごとの一意性で全てを尽くす。全てがH2の構造対象となる。Uₙ=(E,L₀,L₁⊗(L₂L₀⁻¹)ⁿ,L₂)を代表とし、εδ=δかつε(η+nδ)∈{η+mδ,2δ−η−mδ}という有限楕円自己同型群を含む必要十分条件でpointed重複を判定する。δ非捩れなら可算無限、位数rならZ/rZの有限商となる。余分な自己同型がなく2η∉⟨δ⟩なら正確にr個。証明は `thm:elliptic-marking-lattice-fiber`、`cor:elliptic-torsion-fiber-cardinality`。Z²と二面体作用はKitamura–Okawaの既存announcementと重なるため新規性を主張せず、ここでは指定範囲の独立証明と明示的な忘却判定を与える。η∈Zδ、退化曲線、noncubicの忘却と相対stack射は未解決。

固定圏上の2-fiber（許容構造対象のgroupoid）と、自己同値で割った同型類ファイバーを区別する。証明は [現行節](papers/moduli/marking_forgetting.tex)、仮定と残る問題は [研究ノート](notes/research_notes.md) を参照。

## 関連研究

[research-hub](https://github.com/uedakazushi/research-hub) が研究全体の入口。[nc-cubic-classification](https://github.com/uedakazushi/nc-cubic-classification)とはO標識とAS4表示の考え方を比較するが、その未監査の完全分類定理には依存しない。Serre根一般は [categorical-fano-index](https://github.com/uedakazushi/categorical-fano-index) と関係する。既存のquadric分類・Okawa–Uedaのmoduliとの具体的比較は文献ノートを正本とする。
