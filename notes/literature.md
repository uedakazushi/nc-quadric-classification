# 非可換 quadric 分類：現行文献比較

資料確認日：2026-11-21（日本時間）。v0.4。現行の一次資料比較。
以下で「確認」は記載箇所の本文・仮定の照合を意味し、外部論文の全証明を独立に再検証したという意味ではない。

## 研究の位置

本研究の対象は、構造として指定された $(\mathcal C,\mathcal O)$ であり、exact autoequivalence $s$、同型 $s^2\simeq\mathbb S^{-1}[2]$、および orbit algebra の quadratic AS-regular ambient 表示は存在条件として扱う。この区別を保った分類と marking 忘却が課題である。

既知の cubic AS-regular $\mathbb Z$-algebra、geometric quintuple、admissible quadruple の分類や hypersurface embedding を新成果として扱わない。特に、quadratic hull の存在と quadratic envelope による canonical recovery は別の主張である。

## 確認した一次資料

| 文献キー | 確認箇所・版 | 本研究での使い方と制限 |
|---|---|---|
| `AZ1994` | 出版社書誌・abstract。原論文 Theorem 4.5 の全文は今回未取得 | AZ ampleness と再構成の原典。今回の具体的な定義・再構成条件は `MU2021` Definition 2.5 / Theorem 2.6 で照合する。 |
| `VdB2011` | arXiv:0807.3753v3, Proposition 5.1.2, Theorem 5.5.10, Corollary 5.6.2, Theorem 6.1, Proposition 6.6, Corollary 6.7, Theorem 7.1 | cubic regular $\mathbb Z$-algebra の分類、even part の graded 化、quadratic hull、translation principle。標数 $\ne2$ の代数閉体で ambient $D/(g)$ 表示が存在する。選んだ shift の平方が inverse Serre になること、および指定された $\mathcal O$ の保存は別途確認する。 |
| `SVdB2013` | 出版版 §§2.5–2.8, 5、式(2.2)–(2.3)、Theorem 5.6、Corollary 5.8、§§10.1–10.5、Theorem 10.2、p.854 | central quadricのsmoothness、Sklyanin pencilのdomain性、楕円base locus、fat pointの自己Euler特性2。一般Corollary 5.8のstandard性には次行の訂正を反映する。§10の幾何的左加群を反対環で右規約へ移す。 |
| `MU2021` | arXiv:1708.00167v4, Definition 2.5, Theorem 2.6, §5、Definition 5.4、Theorems 5.16–5.17、Appendix Example 6.1 | canonical twist と standard 条件、full geometric helix、non-standard presentation の例。§5 は標数0の代数閉体。non-standard algebra でも tails は standard presentation と同値になり得る。 |
| `MN2025` | 書誌は出版社、本文は arXiv:2307.15253v1, Theorems 6.12–6.13 | noetherian 4-dimensional quadratic AS-regular $S$、central regular $f\in S_2$、$S/(f)$ が domain・graded isolated singularity・standard の場合、dimension 3 / Gorenstein parameter 4 の AS-regular $\mathbb Z$-algebra に移れる。standard 仮定を除いた完全な逆定理ではない。 |
| `Stacks0FZR` | Lemma 56.7.8、Tag0FZR | 有限型、source separated・target reducedのcoh圏同値を幾何学的に記述する。Fano仮定を使わず可換認識に適用。 |
| `EsnaultViehweg1992` | 著者公開全文、Theorem1.2と直後の標数0への拡張（本文p.4） | Kodaira消滅。M=−Kがampleとなった後にMとLに適用する。 |
| `BondalOrlov2001` | arXiv:alg-geom/9712029, Theorem 3.1 | ample canonical/anticanonical bundle を持つ滑らかな射影多様体の導来自己同値。coh(Q)のexact自己同値に適用し、shiftが零であることを確認する。 |
| `OU2014` | arXiv:1403.0713v1, §2、Theorem 1.1 | geometric-quintuple GIT moduli $\mathbb P(2,4,4,6)$、conifold-potential moduli $\mathbb P(1,2,3,4)$、次数4の有限射。これらを $\mathcal O$-marked moduli と同一視するには marking 忘却の追加議論が必要。出版情報は推測せず preprint として引用する。 |
| `BSW2010` | arXiv:0802.0162v3、§7の(7.1)–(7.2)、Proposition 7.1 | 通常の4次元Sklyanin環の自己双対bimodule分解と非捩れCY性。本文どおりk=Cで使い、退化・modified例へ外挿しない。 |
| `RRZ2014` | arXiv:1302.0437v2、Lemma 1.5 | noetherian connected graded AS-Gorenstein環とμ-normalな正則正規元zについて商のNakayama公式。Sklyaninではμ=idかつz中央なので適用できる。 |
| `LS1993` | 出版版§1.1、pp.38–39 | 通常のSklyanin関係と中央二次pencilの対角平方和による表示。反自己同型による左右規約の比較に使う。仮定τ∉E[4]は無限位数の場合に成立。 |
| `MUW2026` | arXiv:2606.24606v1 (2026-06-23)、Introduction、Definition3.1–3.3、Proposition3.5、Lemma3.20、Remark4.4、Theorems4.10,4.12,5.5,5.17 | Mori–Ueyama–Wuの三著者。normal cutのruling・twistのstandard性・中心Sklyaninのsmooth⇒standard。ambientにAuslander正則・Cohen–Macaulay(*)を追加要求。全O-marked H2分類ではない。normal→centralのgraded Morita還元はIntroductionで不明とされる。 |

MU2022 の arXiv v4（Definitions 4.10, 5.9、Lemmas 2.4, 4.13, 5.11, 5.13、Theorem 5.5）は正則正規切断を扱い、ambientの追加条件(*)を課さない。型14641は四次元quantum polynomial algebraの仮定を満たし、H2のdomain性から切断式はhigh rankとなる。主原稿の四周期比較はここから得る二つのMCM型にOrlovの分解とMN2025のhelix定理を適用する。[MU2022](https://arxiv.org/abs/1905.12266v4)・[Orlov](https://arxiv.org/abs/math/0503632)・[Mori–Ueyama 2016](https://arxiv.org/abs/1507.06377)

Van den Bergh 論文の上記定理番号は **arXiv v3** のもの。出版版では番号が異なるため、版を明記せず番号だけを引用しない。

## 平方根と Nakayama twist

`MU2021` §5（arXiv v4 の PDF pp.22–23）では、$B=S/(f)$ の tails において canonical bimodule は
$$
M\longmapsto M_\nu(-2)
$$
で作用する。したがって
$$
\mathbb S^{-1}[2](M)\simeq M_{\nu^{-1}}(2).
$$
通常の次数移動 $(1)$ を要求された平方根として用いるには、誘導された Nakayama twist の自然同型による自明性を確認する必要がある。特定の object に対する $M_\nu\simeq M$ は、関手全体の自明性を意味しない。

`MU2021` Appendix Example 6.1 の non-standard algebra は可換 smooth quadric の Zhang twist である。従って standard/non-standard という一つの graded presentation の挙動を、そのまま $(\mathcal C,\mathcal O)$ の不変量として用いない。

この点は`MUW2026` Theorem4.12でruling保存／交換の必要十分条件として精密化されている。Zhang同値はregular moduleとそのtails像を保存するため、O-marked pairでもstandard性は不変でない。本稿の四根では3型対1型となる。同論文Theorem5.5の幾何型Sklyaninに対するsmooth⇒standardにより、本稿の楕円型例は`MN2025` Theorem6.13の比較に入る。指定O・平方根の具体的対応は prop:standard-pointed。Theorem 6.13 の結論は次元3・Gorenstein parameter 4であり、cubicの一次生成性には別の証明が必要である。

## Ore extension による ambient の検証

直接使える一次資料は `LV2026` **Proposition 2.2**。代数閉体上、多項式環の graded automorphism twist $R$ に対し、$\sigma$ が graded automorphism、$\delta$ が degree-one left $\sigma$-derivation、$\deg y=1$ なら、$R[y;\sigma,\delta]$ は noetherian AS-regular / Auslander-regular domain、Koszul、Cohen–Macaulay であり、$R$ が $n$ 変数なら global dimension $n+1$、Hilbert series $(1-t)^{-n-1}$ を持つ。

古い一般的な補助出典は `LWW2014` **Theorem 3.3**：automorphism 型 Ore extension は twisted Calabi–Yau dimension を1増やす。これだけを引用して noetherianity や Koszul 性まで同時に主張しない。

本研究の具体的な族への適用と正則正規元の計算は、主原稿の `prop:ore-ambient-family` に証明がある。ここでは同じ証明を複製しない。対象は quotient map を固定した被覆であり、unframed ambient の全同型分類は主張していない。

## 直近の比較課題

1. square-root 条件と canonical hull の整合性を、関手と自然同型の水準で照合する。
2. root と ambient の忘却を分け、$(\mathcal C,\mathcal O,s)$ の orbit algebra 表示と $(\mathcal C,\mathcal O)$ の同値関係を整理する。
3. standard locus で `MN2025` を適用し、既存 quadruple/tensor 分類から $\mathcal O$-marked 分類への射を記述する。
4. `OU2014` の次数4射と root 忘却の関係を検証する。現段階で一致・有限性を断定しない。

## 一次資料へのリンク

- `AZ1994`: <https://doi.org/10.1006/aima.1994.1087>
- `VdB2011`: <https://arxiv.org/abs/0807.3753v3>, <https://doi.org/10.1093/imrn/rnq234>
- `SVdB2013`: <https://ems.press/journals/jncg/articles/4781>, <https://arxiv.org/abs/1108.1552>
- `MU2021`: <https://arxiv.org/abs/1708.00167v4>, <https://doi.org/10.4171/JNCG/403>
- `MN2025`: <https://arxiv.org/abs/2307.15253v1>, <https://doi.org/10.1007/s10485-025-09806-2>
- `OU2014`: <https://arxiv.org/abs/1403.0713v1>
- `LV2026`: <https://link.springer.com/article/10.1007/s13366-026-00867-5>
- `LWW2014`: <https://doi.org/10.4171/JNCG/165>, <https://arxiv.org/abs/1205.0893>

- `BondalOrlov2001`: <https://arxiv.org/abs/alg-geom/9712029>, DOI 10.1023/A:1002470302976

- `Stacks0FZR`: <https://stacks.math.columbia.edu/tag/0FZR>
- `EsnaultViehweg1992`: <https://page.mi.fu-berlin.de/esnault/books/esvibuch.pdf>
- `BSW2010`: <https://arxiv.org/abs/0802.0162v3>, <https://doi.org/10.1016/j.jpaa.2009.07.013>。出版書誌確認：<https://eprints.gla.ac.uk/130850/>。
- `RRZ2014`: <https://arxiv.org/abs/1302.0437v2>, <https://doi.org/10.1016/j.aim.2014.07.010>
- `LS1993`: <https://www.numdam.org/article/BSMF_1993__121_1_35_0.pdf>, <https://doi.org/10.24033/bsmf.2200>
- `MUW2026`: <https://arxiv.org/abs/2606.24606v1>, <https://arxiv.org/html/2606.24606v1>
