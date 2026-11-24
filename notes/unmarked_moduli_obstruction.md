# 無標識 Abel 圏の分類と対角の非準コンパクト性

2026-11-25 / v1.1。証明の正本は論文B v0.42の[標識忘却節](../papers/moduli/marking_forgetting.tex)にある。一次資料の照合先は[文献比較](literature.md)。

## 定理と仮定

非可算な標数零代数閉体 k 上で、F が H2 から通常の代数スタック M への射で、任意の二つの k-点の像が同型であることと、基礎Abel圏が k-線形exact同値であることが同値なら、M の対角は準コンパクトでない（`thm:unmarked-diagonal`）。特に複素数体上で成り立つ。一般の標数零基礎体では、非可算代数閉拡大上で源の代数スタック表示と点判定が同定される場合に降ろす。元の局所有限型siteで超越拡大体を直接評価する操作は用いない。

## 証明の入力と点検範囲

- **U0**　`lem:constructible-countable-partition`。Noether正規化で真閉集合の可算被覆をアフィン空間に移し、超平面の禁止値を避ける。構成可能な分割片のうち有限個を取り除くと残りの次元が落ちる。可算体ではアフィン直線の閉点分割が反例になる。
- **U1**　`prop:iso-fiber-cardinality`。二つの対角を別々に基底変更し、有限型atlas上で標的の一対象と同型になる点、および源の各同型類を表す点を構成可能にする。Noetherian基底での局所有限表示性、代数空間版Chevalley、非空な局所有限型代数空間の代数閉体上の点の存在を使用する。2-fiberは同型の選択を含むのでその濃度を入力にしない。
- **U2・相対表示**　[有限型性定理](../papers/moduli/h2_smooth_atlas.tex)では、cubic smooth開とnoncubic表示族の準コンパクト性から有限個のsmooth chartを取る。相対反Serre認識の全忠実性によりrelationに全pointed Isomが入り、affine有限表示対角が降下する。[相対定義](../papers/moduli/relative_definitions.tex)のmodule-object基底変更は体上のpointed同値を系に延長する。定数の自然自己同型はpointingで固定される。[cubic atlas](../papers/moduli/cubic_smooth_atlas.tex)が楕円四つ組の反復を実際の k-点として含む。
- **U2・上界**　数値剛性補題で商圏の長さと通常の数値rankが四つのfoundation基底上で一致することを確認した。自己Euler形式が1なのでChern指標は (1,a,b,ab)。同じ類の二対象の間の Ext² はSerre双対と大きな偶数twistのHilbert多項式の比較で消え、非零射の単射性と余核のHilbert多項式の消滅が一意性を与える。従って未知の標識が非可算個ある余地はない。
- **U2・下界**　[二つの内在的foundation](../papers/moduli/foundation_stack.tex)と[反射の証明](../papers/moduli/marking_forgetting.tex)を照合した。右加群の添字移動 T と評価列の核・余核による ruling 交換 R は差をそれぞれ δ−η, 2δ−η に移し、RT は η+δ を与える。η∉ℤδ は正負の反復と中間四つ組の許容条件を保つ。[Aの逆構成](../papers/sections/elliptic_inverse.tex)と添字付き復元を適用すると、非捩れ δ を固定する原点保存自己同型は恒等、次数二線束のずれは [2] の全射性で合わせられる。重複は高々一つの整数反射に限られ、可算無限のpointed類が残る。双方向の判定がこの集合と分類射の一つのファイバーを一致させる。

非捩れ平行移動による E/ℤ は有限型代数空間で、慣性は自明だが atlas 上で対角の引戻しが E の無限非交和になる。本文の例は結論の範囲を示す。三稿全体の独立公表前監査・網羅的新規性確認・形式証明は別に残る。

## 原稿と再現の確認（2026-11-25）

B v0.42 の §31.1（pp. 238–239）に補題31.7、命題31.8、定理31.9、系31.10、例31.11を収録した。リポジトリのルートで `python3 scripts/check.py papers` が三稿のソースと原稿間の参照検査に合格し、`python3 scripts/check.py build --manuscript papers/nc-quadric-surface-moduli.tex` がLuaLaTeX・BibTeXの最終ログ、243頁のPDF、SyncTeXについて合格した。今回の環境では既設のTeX追加ツリーを `TEXMFHOME=/workspace/.quadric-tex/texmf`、キャッシュを `TEXMFVAR` と `TEXMFCACHE` の双方に `/workspace/.quadric-tex/var`として使用した。PDFの1、6、238–240頁をレンダリングして要旨、導入、補題から例までの改頁と数式、結論を確認した。VS Codeの設定と同等のレシピを使い、UIの往復検索は試していない。今回の定理は幾何点と構成可能性の論証で、新しい数値計算を入力に持たない。既存の計算suiteは再実行していない。

## 補助的な幾何的説明：楕円曲線切片

この方法は対角の障害を具体的に説明するための別証明候補であり、上記の証明はこの切片を使わない。

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
