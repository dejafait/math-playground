# Corollary 466e: a fixed integer-pole law with a first downward third contact

## Hypotheses

Fix, without varying any factor,
\[
 h_0(s)=\frac{(1+s)((s+3)^2+1)}{10}
              \prod_{n\ge1}(1+s/2^n).
\]
Let \(E_n\) be independent exponentials of rates \(2^n\), let
\(Y=\sum_{n\ge1}E_n\), and let \(g=g_1\) be its density. Set
\[
 f(x)=2e^{-x}-2e^{-3x}\cos x-4e^{-3x}\sin x\quad(x>0),
 \qquad f(x)=0\quad(x\le0),\qquad p=f*g.
\]
For smooth positive-axis functions use
\[
 D_j(u;x)=(-1)^{j(j-1)/2}\det[u^{(r+s)}(x)]_{0\le r,s<j}.
\]
This is an artificial law, not C466a's actual reciprocal-Xi density.
The target and source scope were approved before this attempt in
[assessment899, completion900](../drafts/literature/2026-11-14-integer-pole-contact-diagnostic-899.md).

Precisely imported inputs:

- S. Sra, *On some positivity properties of the Riemann Xi function*,
  [arXiv:2611.02944v1](https://arxiv.org/pdf/2611.02944v1),
  Lemma C.17 proof, (C.49), pp38-39: the inverse of the first real
  factor and conjugate pair is positive for \(q_1<A\), \(b>0\).
  Substitute \(q_1=1,A=3,b=1\), with the normalization above.
  The sufficiently-small-\(b\) finite-window conclusion is NOT used.
- M. Kwaśnicki, *A new class of bell-shaped functions*,
  [arXiv:1710.11023v3](https://arxiv.org/pdf/1710.11023v3),
  Section 6.1, p20: the smooth one-sided geometric exponential
  convolution, at exactly \(m=1\). No large-\(m\) sign-change result
  is imported. C466d's proof also establishes positivity, flatness
  and bounded derivatives for this same \(g\), independently of
  the gamma factor in that lemma.
- F. W. Steutel and K. van Harn, *Infinite Divisibility of Probability
  Distributions on the Real Line*, Marcel Dekker, 2004,
  Chapter V Theorems 2.11/2.16, equation (2.23), including the singular
  canonical-kernel case in Chapter III Theorem 10.4:
  [book text](https://www.nzdr.ru/data/media/biblio/kolxoz/M/MV/Steutel%20F.%2C%20van%20Harn%20K.%20Infinite%20divisibility%20of%20probability%20distributions%20on%20real%20line%20%28Dekker%2C%202004%29%28ISBN%200824707249%29%28546s%29_MV_.pdf).
  Applicability to this same law is checked below.

The elementary transform/convolution conventions are those of
[DLMF 1.14(iii)](https://dlmf.nist.gov/1.14#iii), especially
1.14.17-20 and 1.14.30. The model-specific determinant and error
calculations below are needed because the inspected sources do not
give these joint conditions at the fixed value \(b=1\). They do not
reprove a general positive-inverse or geometric-smoothing theorem.

## Conclusion

The function \(p\) is a probability density in \(C^\infty(\mathbb R)\),
zero on \((-\infty,0]\), flat at zero and positive on \((0,\infty)\),
with Laplace transform \(1/h_0\). All zeros of the entire function
\(h_0\), hence all poles of its reciprocal, are simple.
Its canonical kernel is
\[
 H(t)=e^{-t}+2e^{-3t}\cos t+\sum_{n\ge1}e^{-2^nt}.
                                                               \tag{1}
\]
It belongs to \(C^1(0,\infty)\cap L^1(0,\infty)\), has
\(H>0\), \(H'<0\), and \(\int H=13/5\). For every \(x>0\),
\[
 xp(x)=\int_0^x H(t)p(x-t)\,dt.                         \tag{2}
\]
There is a unique zero \(x_*\) of \(D_3(p;\cdot)\) in
\[
             177/32<x_*<89/16.                         \tag{3}
\]
It is the first positive zero, \(D_3(p;x)>0\) on \((0,x_*)\),
and \(D_3'(p;x_*)<0\). Moreover \(D_1,D_2>0\) on
\((0,179/32]\), so \(\eta=1/64\) meets the requested
\(D_1,D_2>0\) on \((0,x_*+\eta)\), with \(x_*+\eta<16\).

**Review status:** audit903 below accepts the complete analytic argument,
all 189 compact cells and both endpoints, using an independent rational
backend and evaluator in addition to exact replay. It is not
an RH candidate. It supplies no actual-Xi sign, all-order PF theorem,
zero-counting/strip match, propagation, or L030-L032/C032a assembly.
The imported finite inverse is known mathematics; the joint fixed-law
specialization was not supplied by the sources checked. No originality
claim follows from that comparison.

## Proof

### The same law and its canonical kernel

The cited finite-inverse proof applies since \(1<3\) and \(b=1>0\).
It supplies strict positivity of \(f\) on the positive axis. Direct
integration of its displayed three terms gives
\[
 \mathcal Lf(s)=\frac{10}{(s+1)((s+3)^2+1)}
 \quad(s\ge0),\qquad \int f=1.
\]
This checks the specialization and normalization, rather than importing
a sign statement about a differently scaled density. All three terms
are absolutely integrable. Since \(\sum\mathbb E E_n=1\), the sum
\(Y\) is finite almost surely; bounded convergence on the partial sums
gives \(\mathcal Lg(s)=\prod_{n\ge1}(1+s/2^n)^{-1}\).

C466d's geometric-component argument gives
\(g^{(j)}(y)=O_j(e^{-2y})\) for \(y\ge0\), with smooth zero
extension, and \(g>0\) on \((0,\infty)\). That argument uses a
finite exponential head against its remaining probability tail, not
the gamma factor. Thus differentiation of \(f*g\) on the \(g\)
factor is justified at every order by its bounded derivatives and
\(f\in L^1\). This proves smoothness, positive-axis positivity,
flatness, and support endpoint zero for \(p\). Tonelli gives its mass
and transform. The product defining \(h_0\) converges uniformly on
compact sets, because \(\sum2^{-n}<\infty\); away from its displayed
zeros its tail is nonzero by the absolutely convergent logarithmic
product. The distinct zeros are \(-1,-3+i,-3-i,-2^n\), all simple.

Put \(B(s)=\log h_0(s)\) for \(s\ge0\), so \(B(0)=0\).
Differentiating its convergent logarithmic product gives
\[
 B'(s)=\frac1{s+1}+\frac{2(s+3)}{(s+3)^2+1}
                    +\sum_{n\ge1}\frac1{s+2^n}
       =\int_0^\infty e^{-st}H(t)\,dt.                 \tag{4}
\]
The real series is Tonelli-integrable and the cosine term is absolutely
integrable. The series for \(H\) and \(H'\) converge uniformly on
every \([\delta,\infty)\), \(\delta>0\). For \(0<t\le1\),
\(\cos t>0\) and \(3\cos t+\sin t>0\), so both \(H\) and
\(-H'\) are positive termwise after grouping the conjugate pair.
For \(t\ge1\), their possibly negative pair terms are bounded by
\(2e^{-3t}\) and \(2\sqrt{10}e^{-3t}\), respectively. They are
strictly dominated by \(e^{-t}\), since
\(e^2>7>2\sqrt{10}\). The first inequality follows already from
the exponential series through degree four, whose sum is 7, with a
positive remainder. Consequently \(H>0\), \(-H'>0\) everywhere.
Absolute integrability follows from the same bounds, and
\[
 \int_0^\infty H=1+\frac{6}{10}+\sum_{n\ge1}2^{-n}=13/5.
\]
Integrating (4) from zero to \(s\) (Tonelli now applies to \(H>0\))
gives
\[
 B(s)=\int_0^\infty(1-e^{-st})H(t)\,\frac{dt}{t}.       \tag{5}
\]
This is the cited representation with no drift and decreasing canonical
density \(k=H\), for the very same law with transform \(e^{-B}\).
The law is nondegenerate and has left endpoint zero. The cited scalar
theorem therefore gives (2). Its singular-kernel case is necessary:
\(H(0+)=\infty\). The convolution is nevertheless finite and
continuous locally because \(H\in L^1\) and \(p\) is smooth and
bounded; the identity is pointwise. No complete monotonicity of \(H\)
or determinant sign is assumed here.

### A whole endpoint interval, not sampled endpoint signs

Let \(L=1/4\). Expansion of the finite three-exponential formula yields
\[
 D_2(f;x)=20e^{-4x}J(x),\quad
 J(x)=e^{-2x}-\cos x+2\sin x,\qquad
 D_3(f;x)=1000e^{-7x}.                                  \tag{6}
\]
For an explicit check of the latter identity, write the rates as
\(1,3+i,3-i\), with coefficients \(2,-1-2i,-1+2i\).
The determinant of the derivative matrix is their coefficient product
times the squared Vandermonde and \(e^{-7x}\); these constants are
10 and \(-100\), respectively. The minus sign in \(D_3\) gives (6).
The analogous two-rate expansion gives the displayed formula for
\(D_2\). Since \(J(0)=J'(0)=0\) and, for \(0\le x\le L\),
\[
 J''(x)=4e^{-2x}+\cos x-2\sin x
       \ge4(1-2x)-2x\ge3/2,
\]
we have \(J(x)\ge3x^2/4>0\) for \(0<x\le L\).

Here are the required specialization details of C466d's endpoint
composition argument. Define \(A=f'/f\), \(C=f''/f\). Equation (6)
implies
\[
 A'=-D_2(f)/f^2<0,\qquad
 A'C''-A''C'=-D_3(f)/f^3<0,
 \qquad \frac{d^2C}{dA^2}>0\quad(0<x\le L).           \tag{7}
\]
The second identity is the three-function Wronskian after division by
\(f^3\); the last uses \((A')^3<0\). For ordered nodes
\(0<y_1<\cdots<y_j<x\le L\), \(j=2,3\), it follows that
\[
       \det[f^{(i)}(x-y_k)]_{i=0,\ldots,j-1;k=1,\ldots,j}>0. \tag{8}
\]
For \(j=2\), divide columns by \(f\): the \(A\) coordinates
increase with \(y_k\). For \(j=3\), the same division gives rows
\(1,A,C\), whose determinant is positive by the strict convexity
in (7) and increasing secant slopes. No general implication from
confluent signs to arbitrary translation minors is being assumed.

The real exponential convolution supplies the other factor:
\[
 (-1)^{j(j-1)/2}\det[g^{(i)}(y_k)]_{k=1,\ldots,j;i=0,\ldots,j-1}
 \ge0\quad(y_1<\cdots<y_j),\quad j=2,3.                \tag{9}
\]
C466d proves this by finite exponential translation kernels, continuous
Cauchy--Binet, pointwise convergence and confluence. Its tail there is
\(q(y)=2g(2y)\); substituting \(y/2\), with positive row/column
derivative scaling, gives (9) for exactly this \(g\).
For each \(x>0\), strictness holds on a nonempty open subset of the
ordered nodes in \((0,x)\). Otherwise all vectors
\((g(y),\ldots,g^{(j-1)}(y))\) would span dimension less than \(j\).
A nonzero constant-coefficient linear ODE of order at most \(j-1\)
would follow throughout \((0,x)\). Flat zero initial data force its
solution to vanish, contradicting \(g>0\); continuity gives the
open subset. This is the same strictness argument as C466d, with
the scaling and support qualifications now explicit.

Finally \(f(0)=f'(0)=0\), and \(f,f',f''\in L^1\) as zero-extended
weak derivatives. Thus no boundary atom occurs through order two.
Bounded smooth derivatives of \(g\) justify
\[
 p^{(i+k)}(x)=\int_0^x f^{(i)}(x-y)g^{(k)}(y)\,dy
                    \quad(0\le i,k\le2).              \tag{10}
\]
The composition identity applied to (10), and restricted to ordered
nodes, expresses \(D_j(p;x)\) as the integral of (8) times the
signed determinant (9). All terms are absolutely integrable, since
the finite-head derivatives are integrable and the tail derivatives
bounded. The integrand is nonnegative and strictly positive on the
open set just established. Hence
\[
                 D_2(p;x),D_3(p;x)>0\quad(0<x\le1/4). \tag{11}
\]
No gamma-specific endpoint estimate from C466d has been transferred.

### True-law enclosures for the compact interval

The certificate is [contact-certificate-901.py](../scripts/integer-pole/contact-certificate-901.py),
with full output [contact-certificate-901.json](../scripts/integer-pole/contact-certificate-901.json).
This subsection specifies its complete error model. All interval
endpoints are integers divided by \(S=2^{512}\). Rational conversion,
addition, multiplication, division and scaling round outwards using
integer floor/ceiling. Only that generic interval class is reused from
certificate896; no gamma-law evaluator or bound is called.

Let \(p_N\) be the density of the finite product, \(N=128\), and
\(Q_N=e^xp_N\), \(Q=e^xp\). Write \(r_n=2^n\). The exact partial
fraction coefficients of \(p_N\) are
\[
 a_0=2\prod_{n=1}^N(1-1/r_n)^{-1},\quad
 z=(-1-2i)\prod_{n=1}^N(1-(3+i)/r_n)^{-1},
\]
\[
 a_n=\frac{10r_n}{(1-r_n)((3-r_n)^2+1)}
           \prod_{k\ne n,\ 1\le k\le N}(1-r_n/r_k)^{-1}.
                                                               \tag{12}
\]
The residues at the distinct simple poles give, for \(x>0\),
\[
 Q_N(x)=a_0+2e^{-2x}\Re(ze^{-ix})
                 +\sum_{n=1}^N a_ne^{-(r_n-1)x}.       \tag{13}
\]
The transform is proper, so these residues exhaust it. Every real
coefficient and both components of \(z\) are computed as exact
rationals; the finite formula is an inverse of the normalized finite
law, not a hypothetical infinite residue expansion.

To compare with the infinite law, put \(h=p_8\). Its convolution of
11 exponential factors (counting the conjugate pair) vanishes to order
10 at zero. This follows also directly by convolving \(f(x)=5x^2+O(x^3)\)
with eight real exponentials and rescaling their simplex integral.
Its zero extension is therefore \(C^9\). Use (12) at \(N=8\) to
denote its coefficients by \(b_0,b_n,w\). For \(1\le l\le8\),
\[
 \|h^{(l)}\|_\infty\le
 M_l:=|b_0|+\sum_{n=1}^8|b_n|r_n^l
                         +2(|\Re w|+|\Im w|)4^l.      \tag{14}
\]
Indeed \(|3+i|<4\), the exponentials have modulus at most one on
the positive axis, and the derivatives vanish on the negative axis.
Convolving \(h\) with the intervening real exponential probability
law gives \(\|p_N^{(l)}\|_\infty\le M_l\). For \(0\le j\le7\),
\(p_N^{(j)}\) is globally Lipschitz with constant \(M_{j+1}\).
The remaining independent tail \(Z_N=\sum_{n>N}E_n\) has mean
\(2^{-N}\), and \(p^{(j)}(x)=\mathbb E p_N^{(j)}(x-Z_N)\).
Dominated differentiation is justified by the same bounded derivatives.
Thus, on the entire real line,
\[
 |p^{(j)}-p_N^{(j)}|\le2^{-N}M_{j+1}.
\]
Since \(x\le179/32<6\) and \(e<3\), Leibniz gives the uniform
true-law jet error
\[
 |Q^{(j)}-Q_N^{(j)}|
 \le E_j:=3^6 2^{-128}\sum_{k=0}^j\binom jk M_{k+1},
                          \qquad 0\le j\le7.           \tag{15}
\]
These are rational bounds, saved in the certificate. The extra orders
six and seven pay the spatial Taylor remainders, beyond the fifth
derivative needed to evaluate a contact derivative.

Only the first \(K=12\) real modes of (13) are evaluated in each cell.
All remaining finite modes are enclosed, for \(x\ge L=1/4\), by
\[
 T_j=\sum_{n=13}^{128}|a_n|(r_n-1)^j
                                  e^{-(r_n-1)L},\quad 0\le j\le7.
                                                               \tag{16}
\]
The code computes upper intervals for every term of this finite sum;
there is no unbounded or uninspected tail. Equation (15) separately
accounts for all modes beyond the finite law, via its probability tail.
The saved bounds satisfy \(\max E_j<10^{-20}\) and
\(\max T_j<10^{-100}\), as checked on all eight stored orders.

For exponential evaluation at rational \(t\ge0\), if \(t\ge512\)
use \(0\le e^{-t}\le2^{-512}\). Otherwise divide \(t\) repeatedly
by 2 until it is at most 1, use the alternating exponential polynomial
through degree 100 with remainder in \([-t^{101}/101!,0]\), then
square back with outward intervals. For sine and cosine at a rational
center \(c\), use their degree-100 Taylor polynomials, each with
absolute remainder \(|c|^{101}/101!\). On a cell \([c-r,c+r]\),
enlarge each trigonometric interval by \([-r,r]\), since both first
derivatives have modulus at most one. Monotonicity gives each real
exponential interval from its two endpoints. Differentiate (13) up to
order seven: its conjugate coefficient becomes \(z(-(2+i))^j\),
and each real mode gains \((-(r_n-1))^j\). Finally enlarge by
\([-E_j-T_j,E_j+T_j]\). This encloses the derivatives of the true
\(Q\), including rounding, truncation, and spatial variation.

Natural intervals alone were inefficient near the left endpoint.
The stopped initial implementation is retained as
[contact-natural-interval-incomplete-901.py](../scripts/integer-pole/contact-natural-interval-incomplete-901.py);
it produced no completed certificate and supplies no sign evidence.
The final implementation uses spatial Taylor enclosures of the
determinants, as follows, without changing the law or window.

For a jet \(q_j=Q^{(j)}\), define
\[
 A_{ij}=\det\begin{pmatrix}q_i&q_j\\q_{i+1}&q_{j+1}\end{pmatrix},
 \qquad B_{ijk}=\det[q_{u+v}]_{u=0,1,2;\ v\in(i,j,k)}.
\]
Writing \(G=D_2(Q)\), \(F=D_3(Q)\), multilinearity and cancellation
of repeated columns give the exact derivative lists
\[
 (G,G',G'',G''')=
 (-A_{01},-A_{02},-A_{12}-A_{03},-2A_{13}-A_{04}),
\]
\[
 (F,F',F'',F''')=
 (-B_{012},-B_{013},-B_{023}-B_{014},
                    -B_{123}-2B_{024}-B_{015}).         \tag{17}
\]
For \(U=Q,G,F\), enclose \(U,U',U''\) at the center and \(U'''\)
on the entire cell using the jet bounds above. The expression
\[
 U(c)+U'(c)z+\tfrac12U''(c)z^2+\tfrac16U'''(\xi)z^3,
       \quad |z|\le r,\quad \xi\text{ in the cell},     \tag{18}
\]
is enclosed with \(z\in[-r,r]\), \(z^2\in[0,r^2]\),
\(z^3\in[-r^3,r^3]\). For the contact derivative use
\(F'(c)+F''(c)z+\tfrac12F'''(\xi)z^2\).
Taylor's theorem applies because \(Q\) is smooth. This step preserves
the cancellations in the center coefficients; it never treats a
sampled sign as a sign on the cell.

### The complete compact ledger and contact join

The full 189-cell ledger, not a preview, is checked by
[contact-ledger-check-901.py](../scripts/integer-pole/contact-ledger-check-901.py),
with [its output](../scripts/integer-pole/contact-ledger-check-901.json).
It verifies every interval ordering, all shared endpoints, the three
exact domains, both endpoint signs, and every sign inequality below.
It is a ledger check, not an independent proof of the evaluator.
The reproducible commands, relative to this notebook, are:

```sh
python3 scripts/integer-pole/contact-certificate-901.py
python3 scripts/integer-pole/contact-ledger-check-901.py
```

There are 187 contiguous prefix cells, one contact cell and one
additional lower-sign cell, with zero failures. Their rational interval
bounds give
\[
\begin{array}{ll}
 Q>0,\quad D_2(Q)>1/50000 & [1/4,179/32],\\
 F>1/50000 & [1/4,177/32],\\
 F'<-1/200 & [177/32,89/16],\\
 F(177/32)>0,\quad F(89/16)<0.&
\end{array}                                                   \tag{19}
\]
For comparison with the required thresholds zero, the smallest saved
prefix lower bound exceeds \(0.0000290179\), the smallest saved
\(D_2(Q)\) lower bound exceeds \(0.0000208947\), and the contact
derivative upper bound is less than \(-0.00530386\). These rounded
comparisons are weaker than the integer bounds checked in (19).

Exponential multiplication is a triangular derivative change of basis,
so \(D_j(p;x)=e^{-jx}D_j(Q;x)\). Therefore (11) and (19) join at
the common endpoint \(1/4\) and prove the full positive \(D_3\)
prefix. The intermediate value theorem and \(F'<0\) in the contact
cell give exactly one zero there. At that zero
\(D_3'(p;x_*)=e^{-3x_*}F'(x_*)<0\). The lower signs hold to
\(179/32\), which exceeds \(89/16+1/64\), proving all the claimed
joint conditions within the original window. No assertions about later
contacts are needed. Floating diagnostic signs beyond the first bracket
are unused, including visibly unstable late signs from cancellation.

Integer multiplicities therefore do not by themselves repair the
generic scalar barrier obstruction. For actual Xi, signed contact-mass
control, strict forcing, simultaneous-contact handling, propagation and
the final positivity assembly remain independent unresolved steps.

### Independent conceptual and arithmetic audit903

This separate audit uses the unchanged scope approved in assessment901,
approval902. It checks the full same-law proof and error chain, not just
the old ledger's inequalities. The precise external imports above are
reused in their recorded versions; no different source theorem or
actual-Xi premise is added. The only direct local mathematical input
remains C466d's geometric-component and composition argument.

**Analytic checks.** Direct finite integration gives the normalized
transform in the first subsection, with the real pole at \(-1\) and the
pair at \(-3\pm i\). The cited positive-inverse case applies at exactly
\(q_1=1,A=3,b=1\); its small-\(b\) window statement is unnecessary.
The geometric sum has finite mean and support arbitrarily near zero.
For each derivative order, C466d differentiates a sufficiently long
finite head against the remaining probability tail; the head has a
smooth enough zero extension and the tail has finite exponential
moment at rate 2. This proves the needed bounded derivatives and
decay, independently of C466d's gamma factor. Differentiating on this
factor makes \(f*g\) smooth on the whole line; vanishing on the
negative axis then gives every zero derivative at the endpoint.
Strict positivity follows from positivity of both densities on their
positive supports, not just an almost-everywhere assertion.

The real-pole product converges normally, and its nonzero tail away
from the listed poles follows from summability of the logarithms.
The distinct real rates and nonreal pair give precisely simple poles.
For (4)--(5), the cosine term is absolutely integrable and the real
series is integrable termwise. The two intervals \((0,1]\) and
\([1,\infty)\), including their common endpoint, prove \(H>0\) and
\(-H'>0\). The singularity at zero is allowed: \(\int_0^1 H<\infty\)
and \(\int_1^\infty H/t<\infty\) are exactly the required Lévy
integrability, while (5) has no drift. Uniqueness of the Laplace
transform identifies this canonical law with the constructed density.
The cited scalar identity consequently applies to that same law.
Local continuity of its convolution upgrades the identity to all
\(x>0\); no derivative of the singular kernel at zero is used.

For (6)--(11), exact complex rational algebra verifies the two finite
determinants and \((f(0),f'(0),f''(0+))=(0,0,10)\). The bound on
\(J''\) uses \(\cos x\ge0\), \(\sin x\le x\) and
\(e^{-2x}\ge1-2x\) throughout the whole endpoint interval. The
Wronskian quotient in (7) has denominator \(f^3\); division by
\((A')^3<0\) gives strictly positive convexity. Increasing \(y_k\)
means increasing \(A(x-y_k)\), so the shifted-column determinant
has the positive sign asserted in (8).

The confluence sign in (9) is \((-1)^{j(j-1)/2}\): it comes from
increasing translation columns and their negative differentiation
direction. Positive scaling transfers C466d's tail statement to
exactly \(g\). If the determinant vanished on every ordered tuple
in \((0,x)\), all derivative vectors would lie in a proper constant
linear subspace. The resulting constant-coefficient ODE, including
its lower-order cases, has zero initial data by flatness and therefore
zero solution. This contradicts \(g>0\) and proves strictness on
an open set. The finite head has two integrable weak derivatives
and zero boundary data through order one, so (10) incurs no atom.
Each term of the determinant expansion is absolutely integrable.
The factor \(1/j!\) in full-domain Cauchy--Binet disappears exactly
on restricting its symmetric integrand to ordered nodes. Thus (11)
is strict on the entire interval, including its join at \(1/4\).

For the true-law error, \(p_8\) is a convolution of the real positive
\(f\) with eight real exponential densities; the two complex factors
are not treated as probability laws. Its order ten at zero makes the
zero extension \(C^9\). Equations (14)--(15) use only bounded
derivatives through order eight: convolution with the intervening
probability law preserves each bound, and mean \(2^{-128}\) of the
remaining tail pays the global Lipschitz error through order seven.
Leibniz uses all terms, with \(e^x<3^6\) on the stated domain.
There is no interchange with an infinite residue series. The omitted
finite modes and the infinite probability tail are separate errors.

**Arithmetic checks.** The complete reproducible audit is

```sh
python3 scripts/integer-pole/contact-audit-903.py
```

Its full output is
[contact-audit-903.json](../scripts/integer-pole/contact-audit-903.json).
It rebuilds every residue directly from its pole product, without
the triangular-product shortcut in generator901; all coefficients
at \(N=8,128\) agree exactly. It checks every derivative majorant,
all eight true-law errors and all eight omitted-mode bounds. A
formal polynomial differentiation of the determinant expansion is
compared with independently generated column-derivative formulas,
verifying every identity in (17).

The new interval backend performs exact Fraction endpoint operations
and projects outward onto the dyadic grid. Substituting it into the
inspected old evaluator reproduces every stored interval exactly.
A separate evaluator uses exact rational transcendental Taylor sums
before rounding, direct residue scaling, and the generated derivative
lists. The exponential cutoff is valid because \(e>2\); the
alternating remainder after degree 100 and the trigonometric
degree-100 Lagrange remainder have the stated signs and sizes.
Spatial Taylor errors use the whole-cell jet for the last derivative,
not the center alone. This independently encloses the same true law.

All 187 prefix cells, the contact cell, the lower-sign cell, and both
endpoint evaluations pass. Every shared endpoint and interval domain
is checked; there is no skipped row or open join. The independent
enclosures give the conservative bounds
\[
 Q>0.0004015882892554,\quad
 D_2(Q)>0.0000208947916489,\quad
 F>0.0000290179179804\ \text{on the prefix},\quad
 F'<-0.0053038694082775\ \text{on the contact cell}.
\]
These exceed the required zero, \(1/50000\), \(1/50000\), and
\(-1/200\) thresholds in their respective directions. Both endpoint
signs survive independently; the errors remain below \(10^{-20}\)
and \(10^{-100}\). Full integer enclosures and exact extrema, not
these rounded displays, are the evidence.

Two implementation failures are preserved. The first run passed the
cells but could not serialize the large exact complex residue under
Python's default 4300-digit limit; the final script raises only that
serialization limit. A subsequent report failed an unnecessary,
incorrectly guessed display claim \(Q>3/1000\), while all actual
acceptance tests, including \(Q>0\), passed. Its complete output is
`scripts/integer-pole/contact-audit-903-display-failure.json`; the
serialization failure is recorded in `contact-audit-903-first-run.txt`
in the same directory. Displays are now computed by outward rational
rounding. No model, domain, error estimate or required threshold was
changed. The final full rerun has zero failures.

Finally the triangular change under multiplication by \(e^{-x}\)
preserves each determinant up to \(e^{-jx}>0\). At its zero the
derivative gains only this positive factor. The complete analytic
prefix, the closed compact prefix and strict contact derivative
therefore prove the first simple contact claimed in (3).
The lower-sign endpoint \(179/32\) exceeds \(89/16+1/64\).
Audit903 accepts the fixed model, with all original actual-Xi
limitations intact. This is verification of an existing specialization,
not a new general theorem or certified originality.

## Mathlib

Full matching coverage of this fixed-law/contact theorem has not been
checked. No claim of absence is made. Standard transform, determinant,
convolution, Taylor and interval-arithmetic facts support the proof,
but no named Mathlib theorem is asserted to supply this joint result.
