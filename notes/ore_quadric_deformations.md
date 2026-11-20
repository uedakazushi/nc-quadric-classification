# 定数 bivector 方向の Ore quadric 変形

2026-11-21 / v0.1

## 目的と主張の状態

このノートは、選んだ Serre 根の持上げ障害を、相対的な H2 の族の内部で検討するための具体的な代数族を与える。元の H2 の標識は構造対象のみであり、ここで選んだ根の挙動を調べることと、その pointed exact 分類とは別の問題である。

以下には Ore/PBW 表示、中心正則元、平坦商、quadratic dual の Frobenius 性について**証明稿がある**。作成担当は表示された代数計算を点検し、主担当も手計算の筋を確認した。ただし、**独立した完全な証明監査は未実施**であり、計算機による検算・形式証明器による確認も未実施である。体上の AS 正則性は、通常の Koszul–Frobenius 判定を適用する候補であり、その一次資料の参照箇所の確認を要する。

**Relative CY、relative Serre、および相対 H2 の族であるという結論は未証明である。** 特に、この族を根忘却射の非形式的滑らかさの証明にまだ使用しない。次の具体的な課題は末尾に記す。

## 1. 基礎環と族

$k=\mathbb C$、$K=k[h]$ とする。$h$ は次数零、$x,y,z,w$ は次数一である。$R=k[\varepsilon]/(\varepsilon^2)$ 上の族は $h\mapsto\varepsilon$ で得られる。

$$
\begin{aligned}
A_K={}&K\langle x,y,z,w\rangle/\bigl(
[x,y],[x,z],[x,w],\\
&[z,y]-hx^2,\ [w,y]-hxy,\ [w,z]+hxz\bigr),\\
g={}&xw-zy,\qquad B_K=A_K/(g).
\end{aligned}
$$

ここで $[a,b]=ab-ba$ である。このノートの基底・平坦性の議論は $h^2=0$ を仮定しない。

## 2. Ore 表示と PBW 基底

$A_K$ は反復 Ore 拡大

$$
K[x,y][z;\delta_z][w;\delta_w]
$$

であり、導分は

$$
\delta_z(x)=0,\quad \delta_z(y)=hx^2,\qquad
\delta_w(x)=0,\quad \delta_w(y)=hxy,\quad
\delta_w(z)=-hxz
$$

で与えられる。規約は $za=az+\delta_z(a)$、$wa=aw+\delta_w(a)$ である。

**証明。** $x$ は中心的であるため、$\delta_w$ は $x$ を含む可換関係式を保つ。また

$$
\delta_w(zy)=(-hxz)y+z(hxy)=0,
\qquad
\delta_w(yz)=(hxy)z+y(-hxz)=0.
$$

従って $\delta_w(zy-yz-hx^2)=0$ であり、最初の Ore 拡大上の導分として定義される。Ore 拡大の基底から、$x^ay^bz^cw^d$ が $K$-基底になる。従って

$$
H_{A_K}(t)=(1-t)^{-4}.
$$

## 3. 中心正則元と平坦商

$g=xw-zy$ は中心正則元であり、この正則性は $K$ の任意の可換基底変更後にも成立する。

**証明。** $x$ との可換性は明らかである。他の生成元については

$$
[g,y]=hx^2y-hx^2y=0,\qquad
[g,z]=-hx^2z+hzx^2=0,
$$

および

$$
[g,w]=-[zy,w]
=-z(-hxy)-(hxz)y=0
$$

である。$w$ の次数で見ると $g$ の先頭係数は $x$ である。PBW 基底から $x$ は正則なので、任意の非零 $a$ に対し $ga$ の先頭 $w$ 次数項は非零となる。$g$ は中心的なので左右とも正則である。この議論は基礎環が零因子を持つ場合にも同じである。

さらに $B_K$ の $K$-基底は

$$
\{x^ay^bz^cw^d\mid a,b,c,d\geq0,\ ad=0\}
$$

である。

**証明。** 生成は $xw=zy=yz+hx^2$ により $w$ 次数を下げて得られる。独立性には $ga$ の先頭 $w$ 次数項を使う。その係数は $x$ で割り切れる。一方、上に挙げた標準単項式のうち正の $w$ 次数を持つものの係数は $x$ を含まないので、非零の先頭項同士は一致できない。$ga\ne0$ ならその $w$ 次数は正であり、$w$ 次数零だけの線形結合が像に入ることもない。従って標準単項式は独立である。

各次数は有限自由であり、

$$
H_{B_K}(t)=\frac{1-t^2}{(1-t)^4}
=\sum_{n\geq0}(n+1)^2t^n.
$$

特に $A_R,B_R$ は $R$-flat である。これは $K$ が整域であることだけに依存する平坦性の議論ではない。

## 4. Weyl チャートと一次変形の方向

$x$ は $B_K$ および $B_R$ でも正則である。

**証明。** $x$ は $A$ で正則であり、$g\bmod x=-zy$ は $A/(x)$ で正則である。$xb=ga$ なら、$x$ を法として $\bar g\bar a=0$ となるため $a=xc$ と書ける。従って $x(b-gc)=0$ であり、$b=gc$ を得る。これが商における $x$ の正則性である。

$u=z/x$, $v=y/x$ と置けば、局所化は

$$
B_K[x^{-1}]
\simeq K[x,x^{-1}]\otimes_K
K\langle u,v\rangle/(uv-vu-h),
\qquad w/x=uv
$$

となる。実際、$[u,v]=h$、$g=0$ から $w/x=uv$ であり、残る関係式は

$$
[uv,v]=hv,\qquad [uv,u]=-hu
$$

によって回復する。次数零部分が Weyl 型の代数である。

$h=0$ の Segre 座標を

$$
(x,y,z,w)=(X_0Y_0,X_0Y_1,X_1Y_0,X_1Y_1)
$$

と取れば、$u=X_1/X_0$, $v=Y_1/Y_0$ である。従って $h=\varepsilon$ の変形の bivector 成分は $\partial_u\wedge\partial_v$ となる。ここでは一次積の反対称化による規約を用いる。

## 5. Quadratic dual の完全な表示

$X,Y,Z,W$ を双対生成元とすると、$D_K=A_K^!$ の関係式は

$$
\begin{gathered}
X^2=hYZ,\qquad Y^2=Z^2=W^2=0,\\
XY+YX=hYW,\qquad XZ+ZX=-hZW,\qquad XW+WX=0,\\
YZ+ZY=YW+WY=ZW+WZ=0.
\end{gathered}
$$

これは元の六つの関係式への直交条件を取ることで確認できる。

$E_K=\bigwedge_K(Y,Z,W)$ とし、$\sigma(a)=(-1)^{\deg a}a$ と置く。次数一の $\sigma$-導分を

$$
\delta(Y)=hYW,\quad\delta(Z)=-hZW,\quad\delta(W)=0
$$

で定めると、

$$
D_K=E_K[X;\sigma,\delta]/(X^2-hYZ).
$$

**証明。** $\delta$ は外積代数の関係式を保ち、$\delta^2=0$、$\delta\sigma+\sigma\delta=0$ を満たす。例えば二乗の確認では $W^2=0$ を使うのであり、$h^2=0$ は必要ない。また $q=hYZ$ は $E_K$ の中心元で、$\sigma(q)=q$、$\delta(q)=0$ である。

従って $X^2a=aX^2$ と $Xq=qX$ が成り立ち、$X^2-q$ は Ore 拡大で中心的である。この関係式は $X$ について monic なので、

$$
D_K=E_K\oplus E_KX,
\qquad H_{D_K}(t)=1+4t+6t^2+4t^3+t^4
$$

を得る。

## 6. Frobenius pairing と Nakayama 自動同型

$\lambda_E:E_K\to K$ を $YZW$ の係数、$\lambda:D_K\to K$ を $YZWX$ の係数とする。$a,b,c,d\in E_K$ に対して

$$
\lambda\bigl((a+bX)(c+dX)\bigr)
=\lambda_E\bigl(ad+b\sigma(c)+b\delta(d)\bigr).
$$

**Frobenius 性の証明。** $E_K\oplus E_KX$ に関するこの pairing の上右および下左のブロックは、外積代数の perfect pairing と、それに $\sigma$ を合成したものである。上左ブロックは零なので、全体も perfect である。従って $D_K$ は $K$ 上の graded Frobenius 代数である。この証明は任意の基底変更後にも成立する。

規約 $\lambda(ab)=\lambda(b\nu(a))$ に対し、Nakayama 自動同型は

$$
\nu(X)=-X,\quad\nu(Y)=-Y,\quad
\nu(Z)=-Z,\quad\nu(W)=-W
$$

である。

**証明。** $Y,Z,W$ については外積の符号と $\sigma$ から従う。$X$ については次数三部分を $E_K^3\oplus E_K^2X$ に分ける。$\sigma|_{E_K^3}=-1$、$\delta(E_K^2)=0$ および $X^2=hYZ$ を用いると、任意の次数三の $a$ に対して $\lambda(Xa)=-\lambda(aX)$ を得る。$\lambda$ は次数四以外で零なので、以上で生成元全体について Nakayama の条件を確認したことになる。

## 7. 体上の帰結と相対的な証明の境界

各体への基底変更後、関係式は二次 PBW 系である。Koszul 性と上記 Frobenius 計算を用いて通常の Koszul–Frobenius 判定を適用し、$A$ が Hilbert series $(1-t)^{-4}$、最小分解の型 $(1,4,6,4,1)$ の AS 正則代数であると示すことが次の候補である。ただし、この標準判定の具体的な一次資料の参照箇所と適用条件は未確認なので、ここでは AS 正則性を証明済みの結論として採用しない。

体上のこの主張と、非正則基底 $R$ 上の相対的な主張を区別する。特に、$R$ 上で絶対的大域次元が有限だとは主張しない。

相対的議論の再開に使える候補は、$D_R$ を用いた bimodule Koszul 複体

$$
K_i=A_R\otimes_R(D_{R,i})^*\otimes_R A_R.
$$

ここで $(D_{R,i})^*=\operatorname{Hom}_R(D_{R,i},R)$ の生成元は内部次数 $i$ に置く。各次数で有限自由であり、$\varepsilon=0$ への還元は多項式環の対角の Koszul 分解である。この複体の exactness と Frobenius pairing による自己双対性を、基底変更と左右の符号・twist を含めて示せれば、期待される同型は

$$
\operatorname{RHom}_{A_R\otimes_R A_R^{\mathrm{op}}}
(A_R,A_R\otimes_R A_R^{\mathrm{op}})
\simeq A_R(4)[-4]
$$

である。ただし、**この同型の完全な相対的証明は未完成**である。

さらに中心正則な二次の元による商から相対双対化を導き、$R$-perfect な $\operatorname{qgr}B_R$ に対して

$$
S_R\stackrel{?}{\simeq}(-2)[2]
$$

を証明する必要がある。体上の Serre 公式だけからこの同型を推論してはならない。相対的 smoothness、properness、豊富性、構造対象の条件も、採用する族の定義に照らして確認を要する。

## 8. 根の障害との関係と次の一手

閉ファイバー上の対合 $f(u,v)=(-u,v)$ は、族では $h\mapsto-h$ と同時に

$$
(x,y,z,w)\longmapsto(x,y,-z,-w)
$$

とすれば延びる。しかし、これは $h=\varepsilon$ 上で $R$-線形な延長ではない。

したがって未証明点が解決すれば、標準の根 $(1)$ は延びる一方で

$$
(-\otimes\mathcal O(1,1))\circ f^*
$$

は延びないという、相対 H2 内部の例になる可能性がある。**現段階ではこの最後の結論を主張しない。** 選んだ根の持上げ障害があることと、変形後に別の適合根が存在するかどうかも区別する。

次回はまず、上記の有限な bimodule Koszul 複体について、相対 exactness と自己双対性を左右の規約込みで証明する。その後、中心正則元の商の相対双対化と relative Serre の同定を扱う。相対 H2 の定義に必要な条件をすべて確認するまでは、この候補から根忘却射の性質を結論しない。
