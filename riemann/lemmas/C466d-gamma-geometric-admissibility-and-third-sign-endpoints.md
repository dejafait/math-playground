# Corollary 466d: fixed gamma/geometric admissibility and third-sign endpoints

## Hypotheses

Let \(E_n\), \(n\ge1\), be independent exponential random variables of
rates \(\lambda_n=2^n\), and set \(Y=\sum_{n\ge1}E_n\). Let \(g=g_1\)
be its density. Independently let \(G\) have the gamma density
\[
 f(u)=\frac{u^{1/2}e^{-u}}{\Gamma(3/2)}1_{\{u>0\}}.
\]
Fix \(p=f*g\); neither the shape, rates nor smoothing scale varies.
Write \(a=3/2\), \(\beta=a-1=1/2\), and
\[
 H(t)=a e^{-t}+\sum_{n\ge1}e^{-\lambda_n t},\qquad
 D_j(p;x)=(-1)^{j(j-1)/2}
           \det[p^{(r+s)}(x)]_{0\le r,s<j}.
\]
The first-contact test asks for \(D_3'(x_*)<0\) at its first zero.
The endpoint join in attempt897 completes the model proof;
critical audit898 below validates the assembled analytic argument
and replays its full finite certificate. This is a generic law, not the actual
reciprocal-Xi density in C466a/C466b. Those results and C466c motivate
the test but supply no mathematical premise here.

Source inputs, within the prior
[fixed-model assessment892](../drafts/literature/2026-11-14-gamma-geometric-third-contact-test-892.md):

- M. Kwaśnicki, *A new class of bell-shaped functions*,
  [arXiv:1710.11023v3](https://arxiv.org/pdf/1710.11023v3),
  Section 6.1, p.20, constructs the smooth one-sided infinite
  exponential convolution \(g_m\). We take exactly \(m=1\).
  Its excess-sign-change example and unspecified large smoothing
  parameter are not imported.
- F. W. Steutel and K. van Harn, *Infinite Divisibility of Probability
  Distributions on the Real Line*, Marcel Dekker, 2004, Chapter V,
  Theorems 2.11/2.16, equation (2.23), including the singular canonical
  kernel case of Chapter III, Theorem 10.4:
  [book text](https://www.nzdr.ru/data/media/biblio/kolxoz/M/MV/Steutel%20F.%2C%20van%20Harn%20K.%20Infinite%20divisibility%20of%20probability%20distributions%20on%20real%20line%20%28Dekker%2C%202004%29%28ISBN%200824707249%29%28546s%29_MV_.pdf).
  The nondegenerate positive self-decomposable law with left endpoint
  zero and canonical density \(H\) satisfies \(xp=H*p\).
  Applicability to this fixed law is checked below; no determinant
  sign is part of the imported theorem.
- The continuous Cauchy–Binet composition formula for totally
  nonnegative translation kernels, in the order-two case, as
  inspected in S. Sra,
  [*On some positivity properties of the Riemann Xi function*, author v3](https://suvrit.github.io/papers/riem-xi/riem-xi-v3.pdf),
  Section C.8, p.29, through assessment883. Only this standard
  composition formula is used, not any actual-Xi theorem or finite
  zero certificate.

The assessed Khare gamma finite-PF distinction is comparison evidence
only. Non-PF3 is not used to infer a negative confluent determinant.
The calculations below are necessary fixed-model specializations:
the cited sources do not state these joint endpoint/contact assertions.

## Conclusion

The function \(p\) is a probability density in \(C^\infty(\mathbb R)\),
zero on \((-\infty,0]\), positive on \((0,\infty)\), and flat at zero.
The specified \(H\) belongs to \(C^1(0,\infty)\), is positive and
strictly decreasing, and has integral \(5/2\). The pointwise identity
\[
 xp(x)=\int_0^x H(t)p(x-t)\,dt\qquad(x>0)                 \tag{1}
\]
holds, including the integrable singularity of \(H\) at zero.
Moreover,
\[
 D_1(p;x)>0,\qquad D_2(p;x)>0\qquad(x>0).                \tag{2}
\]
There exist \(0<\epsilon<R<\infty\) such that \(D_3(p;x)>0\)
for \(0<x<\epsilon\) and \(D_3(p;x)<0\) for \(x>R\).
More precisely, with
\[
 M=\prod_{n\ge1}\frac{\lambda_n}{\lambda_n-1},
 \qquad C=\frac{M}{\Gamma(3/2)}>0,
\]
one has
\[
 D_3(p;x)=-\frac{C^3}{4}e^{-3x}x^{-9/2}
                      \bigl(1+O(x^{-1})\bigr)
                 \quad(x\longrightarrow\infty).        \tag{3}
\]
Consequently a smallest positive zero \(x_*\) of \(D_3\) exists,
with \(D_3>0\) on \((0,x_*)\) and \(D_3'(x_*)\le0\).
The lower signs (2) hold through every neighborhood of \(x_*\).

Attempt896 supplies the rational interval certificate
proved below: \(D_3(p;x)>0\) for every
\(x\in[1/32,139/32]\), and there is exactly one zero
\(x_c\in(139/32,35/8)\), with \(D_3'(p;x_c)<0\).
Attempt897 proves \(D_3(p;x)>0\) on \((0,1/32]\), so \(x_*=x_c\)
is the first zero, \(D_3>0\) on \((0,x_*)\), and
\(D_3'(p;x_*)<0\). Together with (1)-(2), this supplies the joint
fixed-model conditions in assessment892; for example take \(\eta=1/64\),
since the lower signs hold globally.

**Audited fixed-model diagnostic (audit898):** the complete argument
below and every compact enclosure pass the separate critical review.
This is not an RH candidate and supplies no actual-Xi sign, PF transfer,
or resolution of L030-L032/C032a.

## Proof

### Admissibility and the canonical kernel

Since \(\sum_n\mathbb E E_n=\sum_n2^{-n}=1\), \(Y\) is finite
almost surely. Its Laplace transform is the specified infinite
product, by bounded convergence applied to the partial sums.
The cited Kwaśnicki construction gives the smooth zero extension
of \(g\). The following finite-head observation additionally verifies
the decay needed later, rather than merely assuming it from smoothness.

For fixed \(j\ge0\), take an integer \(m\ge j+2\). The density \(h_m\)
of \(E_1+\cdots+E_m\) is a finite linear combination of
\(e^{-\lambda_n u}\), \(1\le n\le m\), for \(u>0\): this follows
from partial fractions of its rational Laplace transform with
distinct poles. At zero it has order \(u^{m-1}\), as follows by
scaling its convolution integral over the positive simplex.
Hence its zero extension is \(C^j\) and
\[
 |h_m^{(j)}(u)|\le A_{m,j}e^{-2u}\quad(u\ge0).
\]
For \(Z_m=\sum_{n>m}E_n\), the product for
\(\mathbb E e^{2Z_m}\) converges since all its rates exceed 2
and \(\sum_{n>m}2/\lambda_n<\infty\). Differentiating this finite
head against the tail probability measure gives
\[
 |g^{(j)}(y)|
 \le A_{m,j}e^{-2y}\mathbb E e^{2Z_m}=O_j(e^{-2y})
 \qquad(y\ge0).                                        \tag{4}
\]
The differentiation is justified by bounded continuous head
derivatives and dominated convergence. This also gives a direct
check of the required smoothness orders and flat endpoint.

The law of \(Y\) has support arbitrarily near zero. Indeed, for
any \(b>0\), take a sufficiently late finite head so the remaining
tail has mean below \(b/4\); Markov's inequality gives positive
probability that the tail is below \(b/2\). Independently every
term of that finite head can be small enough that its sum is
below \(b/2\), with positive probability. The same argument applies
to \(Z_m\). Since \(h_m(u)>0\) for every \(u>0\),
\(g(y)=\mathbb E h_m(y-Z_m)>0\) for every \(y>0\).

Convolution of the probability density \(f\) with \(g\) now gives
the asserted positivity, support, normalization and smoothness of
\(p\). For all derivative orders use \(p^{(j)}=f*g^{(j)}\) and (4).
The global smooth zero extension makes every derivative vanish
at zero. In particular the left endpoint of its law is zero.

Let \(F(s)=\mathbb E e^{-s(G+Y)}\) and \(B(s)=-\log F(s)\) for
\(s\ge0\). Then
\[
 B(s)=a\log(1+s)+\sum_{n\ge1}\log(1+s/\lambda_n)
     =\int_0^\infty(1-e^{-st})\frac{H(t)}t\,dt.          \tag{5}
\]
For the last equality each exponential term has the indicated
logarithmic integral (differentiate in \(s\) and use its zero value
at \(s=0\)); nonnegative terms permit Tonelli's theorem.
All defining series and their derivatives converge uniformly on
\(t\ge\delta>0\), so \(H\in C^1(0,\infty)\), \(H>0\), and
\[
 H'(t)=-a e^{-t}-\sum_{n\ge1}\lambda_n e^{-\lambda_n t}<0.
\]
Tonelli gives \(\int H=a+\sum_n\lambda_n^{-1}=5/2\).
Thus (5) has no drift and has the decreasing canonical density
required by the cited self-decomposability criterion. The law is
nondegenerate and has left endpoint zero as checked above.
Steutel–van Harn's scalar equation therefore gives (1).
Its singular-kernel case is relevant: \(H(0+)=\infty\), although
\(H\) is integrable. The integral in (1) is finite because \(p\)
is bounded on compact intervals and \(H\in L^1\).

### Strict second sign, not just weak log-concavity

An exponential density, extended by zero, has a totally
nonnegative translation kernel of order two. After positive
row/column exponential factors are removed, its two-by-two
minors are those of \(1_{\{x_i>y_j\}}\) with increasing \(x_i,y_j\);
they are zero or one. The cited composition formula therefore
makes every finite convolution \(h_m\) PF2.

These densities converge pointwise to \(g\). For example fix the
first two summands as a bounded uniformly continuous density
\(h_2\), and convolve it with the increasingly long remaining
partial sums. Those partial sums converge almost surely to their
tail limit, so bounded convergence proves pointwise convergence
of the resulting densities. Nonnegative two-by-two minors pass
to this limit. Taking symmetric increments gives
\(g(y)^2\ge g(y-h)g(y+h)\) inside its positive support;
continuity and positivity imply log-concavity there.
Consequently \(b(y)=(\log g)'(y)\) is nonincreasing.
It cannot be constant on an entire interval \((0,x)\), since that
would give \(g(y)=K e^{cy}\) there with \(K>0\), contradicting
continuity and \(g(0)=0\).

The zero extension of \(f\) is absolutely continuous with
\(f'\in L^1(\mathbb R)\); its only derivative singularity at zero
is integrable, of order \(u^{-1/2}\). Thus, without differentiating
the gamma factor twice,
\[
 p'=f'*g=f*g',\qquad p''=f'*g'.                         \tag{6}
\]
Fix \(x>0\) and use the probability density
\(f(u)g(x-u)/p(x)\) on \(0<u<x\). Under this probability write
\[
 A(u)=\frac{f'(u)}{f(u)}=\frac{\beta}{u}-1,\qquad
 Q(u)=b(x-u).
\]
Equation (6) gives
\[
 (\log p)''(x)=\mathbb E(AQ)-\mathbb E(A)\mathbb E(Q)
             =\operatorname{Cov}(A,Q).                \tag{7}
\]
All terms are absolutely integrable: after multiplication by the
probability density they are bounded by integrals of
\(|f'|g\), \(f|g'|\), or \(|f'g'|\) on \((0,x)\).

For two independent copies \(U,V\) of this conditional variable,
\[
 \operatorname{Cov}(A,Q)
 =\tfrac12\mathbb E[(A(U)-A(V))(Q(U)-Q(V))]<0.           \tag{8}
\]
Indeed \(A\) is strictly decreasing and \(Q\) is nondecreasing.
The latter is continuous and nonconstant on \((0,x)\), so there
are two separated open subintervals on which its values differ
strictly. The conditional density is positive on both; their
product gives a strictly negative contribution. All other
contributions are nonpositive, and the absolute integrability
just checked also justifies the double-expectation identity.
It follows that
\(D_2=(p')^2-pp''=-p^2(\log p)''>0\), proving (2).

### Positive third sign on an entire interval next to zero

For \(s>0\) tilt the law by \(e^{-sx}\), with density
\[
 p_s(x)=e^{B(s)-sx}p(x),\quad
 \mu_s=B'(s)=\frac a{s+1}+\sum_{n\ge1}\frac1{s+\lambda_n},
 \quad
 \sigma_s^2=-B''(s)=\frac a{(s+1)^2}
                         +\sum_{n\ge1}\frac1{(s+\lambda_n)^2}.
\]
These are its mean and variance, either by differentiating the
Laplace transform or by independence of the tilted gamma and
exponential factors. All differentiations converge absolutely.
Put \(N=\lfloor\log_2 s\rfloor\) for \(s\ge2\). The first \(N\)
exponential rates are at most \(s\), while the remaining squared
reciprocals have a geometric bound. Hence
\[
 \frac N4\le s^2\sigma_s^2
 \le N+a+\frac43<N+3,\qquad
 0<\mu_s\le\frac{N+a+2}s.                              \tag{9}
\]
In particular \(\mu_s\downarrow0\) continuously and strictly, since
\(\mu_s'=-\sigma_s^2<0\).

Let \(r_s(z)=\sigma_s p_s(\mu_s+\sigma_s z)\).
Set \(w_0=1/(\sigma_s(s+1))\) and
\(w_n=1/(\sigma_s(s+\lambda_n))\), \(n\ge1\).
Its centered characteristic function is
\[
 \phi_s(t)=
 \exp(-it\mu_s/\sigma_s)(1-itw_0)^{-a}
                          \prod_{n\ge1}(1-itw_n)^{-1}.
\]
Use weights \(a\) for index zero and 1 for the others.
Their weighted sum of \(w_n^2\) is 1, their maximum is at most
\(2/\sqrt N\), and their weighted cubic sum is at most
\(2/\sqrt N\). Taylor expansion of \(-\log(1-itw_n)\), for
fixed \(t\) and sufficiently large \(N\), therefore gives
\(\log\phi_s(t)=-t^2/2+O_t(N^{-1/2})\).
The weighted linear terms cancel the displayed centering phase.
Absolute convergence of the quadratic and remainder sums justifies
this expansion of the infinite product.

Pointwise characteristic-function convergence alone would not
justify derivative determinants. For each of the first \(N\)
exponential factors \(w_n\ge1/(2s\sigma_s)\), so (9) gives
\[
 |\phi_s(t)|
 \le \left(1+\frac{t^2}{4s^2\sigma_s^2}\right)^{-N/2}
 \le \left(1+\frac{t^2}{16N}\right)^{-N/2}
 \le \left(1+\frac{t^2}{256}\right)^{-8}\quad(N\ge16).
                                                               \tag{10}
\]
The last inequality uses the monotone increase in \(n>0\) of
\((1+u/n)^n\), for \(u\ge0\). The last function in (10) is
integrable after multiplication by \(|t|^j\) for \(0\le j\le4\).
Fourier inversion and dominated convergence therefore imply
\[
 r_s^{(j)}(0)\longrightarrow\varphi^{(j)}(0)
       \quad(0\le j\le4),
 \qquad \varphi(z)=(2\pi)^{-1/2}e^{-z^2/2}.
\]
This also verifies all differentiations used in this local limit.
For \(c=(2\pi)^{-1/2}\) the limiting raw derivative matrix is
\[
 \begin{pmatrix}c&0&-c\\0&-c&0\\-c&0&3c\end{pmatrix},
 \qquad D_3(\varphi;0)=2c^3>0.                         \tag{11}
\]
Multiplication by an exponential acts on derivative matrices by
triangular row/column transformations with diagonal one;
rescaling contributes the powers of \(\sigma_s\). Explicitly,
for \(k=3\),
\[
 D_3(p;\mu_s)
   = e^{3(s\mu_s-B(s))}\sigma_s^{-9}D_3(r_s;0)>0
\]
for all sufficiently large \(s\). The factors are strictly positive.
Because \(\mu_s\) maps a late half-line onto a full interval
adjacent to zero, this is positivity for every point of that
interval, not just for a sequence. No effective endpoint is claimed.

### Negative third sign at infinity

The moment \(M=\mathbb E e^Y\) is the finite product stated above:
each rate exceeds 1 and the logarithmic product converges.
Define the probability density \(w(y)=e^y g(y)/M\), extended by
zero. By (4) and the product rule, for every fixed \(j\)
\[
 w^{(j)}(y)=O_j(e^{-y})\quad(y\ge0),                    \tag{12}
\]
and all these derivatives are flat at zero. In particular \(w\)
has finite moments of every order.
For \(q(x)=e^x p(x)\) one has
\[
 q(x)=C\int_0^x u^\beta w(x-u)\,du,\qquad
 q^{(j)}(x)=C\int_0^x u^\beta w^{(j)}(x-u)\,du.
                                                               \tag{13}
\]
The second formula for \(0\le j\le4\) follows by differentiating
the smooth flat factor. On compact \(x\)-intervals the integrand
is bounded by a constant times the integrable function \(u^\beta\);
the upper endpoint terms vanish.

For large \(x\), split the second integral at \(u=x/2\). Its lower
half is \(O_j(x^{\beta+1}e^{-x/2})\) by (12).
Integrate the upper half by parts \(j\) times, moving derivatives
from \(w(x-u)\) onto \(u^\beta\). At \(u=x\) all boundary terms
vanish by flatness; at \(u=x/2\) every boundary term is a power of
\(x\) times \(O_j(e^{-x/2})\). Thus, writing
\((\beta)_{\underline j}=\beta(\beta-1)\cdots(\beta-j+1)\),
\[
 q^{(j)}(x)=
 C(\beta)_{\underline j}\int_0^{x/2}
           (x-y)^{\beta-j}w(y)\,dy
 +O_j((1+x)^{\beta+j+1}e^{-x/2}).                     \tag{14}
\]
For \(j=0\) the same expression follows directly from the split.
For each of these fixed exponents, on \(0\le y/x\le1/2\),
\((1-y/x)^{\beta-j}=1+O_j(y/x)\).
The normalization and finite first moment of \(w\), together
with its exponentially small tail, now give
\[
 q^{(j)}(x)=C x^{\beta-j}
              \bigl((\beta)_{\underline j}+O_j(x^{-1})\bigr),
 \qquad 0\le j\le4.                                  \tag{15}
\]
This avoids the invalid differentiation of \(u^{1/2}\) twice
at its singular endpoint.

Factor \(C x^\beta\) from each row of the three-by-three derivative
matrix and \(x^{-r}\), \(x^{-s}\) from rows and columns. At
\(\beta=1/2\) the remaining leading matrix is
\[
 A=\begin{pmatrix}
  1&1/2&-1/4\\
  1/2&-1/4&3/8\\
  -1/4&3/8&-15/16
 \end{pmatrix}.
\]
Subtracting half of its first row from its second and adding a
quarter of its first row to its third leaves the lower block
\(\begin{pmatrix}-1/2&1/2\\1/2&-1\end{pmatrix}\), of determinant
\(1/2-1/4=1/4\). Hence
\[
 D_3(q;x)=-C^3 x^{3\beta-6}(1/4+O(x^{-1})).
\]
The exponential triangular transformations already used above
give exactly \(D_3(p;x)=e^{-3x}D_3(q;x)\).
Since \(3\beta-6=-9/2\), this proves (3), with a nonzero
negative leading coefficient. It proves eventual negativity,
not a numerical onset or a root-isolation certificate.

### What the endpoint signs do and do not imply

Continuity and the opposite signs just proved give a zero between
a sufficiently small positive point and a sufficiently large one.
There are no zeros in the initial positive interval. The zero set
in the remaining closed bounded interval is nonempty and compact,
so it has a smallest element \(x_*>0\), which is also the first
positive zero. Absence of earlier zeros and continuity imply
\(D_3(p;x)>0\) throughout \((0,x_*)\). The left difference quotients
at \(x_*\) are nonpositive, giving \(D_3'(x_*)\le0\).
Nothing in this argument makes that inequality strict.
Global (2) supplies all required lower signs, but a tangential
first zero or a higher-order crossing remains possible.

The endpoint-sign argument alone thus gives a law-level failure of
global third confluent positivity under the scalar admissibility
premises, but does not give the stipulated simple first contact.
The effective join at the end supplies the missing exclusion of earlier
zeros using the compact certificate. None of these model conclusions can
be substituted for actual \(H\), actual cofactor weights, or the
independent sign/transfer assumptions in the RH notebook. ∎

### Explicit evaluation formula and omitted-series bound (attempt895)

This subsection supplies a compact-interval evaluation formula for the
same fixed density. It does not strengthen the first-contact conclusion.
Finite partial fractions were already used in (4); explicit coefficients
and derivative bounds are needed here to distinguish truncation error
from the separate numerical-evaluation and interval-coverage obligations.
No additional source theorem or model premise is imported.

Put
\[
 K=\prod_{m\ge1}(1-2^{-m})^{-1},\quad b_n=2^n-1,\quad
 d_n=\frac{(-1)^{n-1}2^n}{\prod_{m=1}^{n-1}(2^m-1)},\quad
 Q(x)=\frac{\Gamma(3/2)}K e^x p(x).
\]
The empty product equals one. For \(x>0\) define
\[
 J_b(x)=\int_0^x u^{1/2}e^{-b(x-u)}\,du.
\]
Then, with locally uniform convergence of every derivative on
\((0,\infty)\),
\[
 Q^{(j)}(x)=\sum_{n\ge1}d_nJ_{b_n}^{(j)}(x),\qquad j\ge0.       \tag{16}
\]
For \(j\ge1\), an explicit formula is
\[
 J_b^{(j)}(x)=(-b)^jJ_b(x)+
   \sum_{r=0}^{j-1}(-b)^{j-1-r}(1/2)_{\underline r}x^{1/2-r}.   \tag{17}
\]

Here is a full convergence justification. Partial fractions for the
finite-head density \(h_m\) give, for \(y\ge0\),
\[
 h_m(y)=\sum_{n=1}^m c_{n,m}e^{-2^ny},\qquad
 c_{n,m}=2^n\prod_{\substack{1\le k\le m\\k\ne n}}
                 \frac{2^k}{2^k-2^n}
         =d_n\prod_{k=1}^{m-n}(1-2^{-k})^{-1}.
\]
The value at zero agrees with the continuous density for \(m\ge2\).
The last product is at most \(K<\infty\), and
\(|d_{n+1}|/|d_n|=2/(2^n-1)\). Consequently
\(\sum_n|d_n|2^{nj}<\infty\) for every fixed integer \(j\ge0\).
The pointwise convergence \(h_m\to g\) established above and dominated
convergence of this coefficient series yield
\[
 g(y)=K\sum_{n\ge1}d_ne^{-2^ny}\quad(y\ge0).
\]
The series and its derivatives converge uniformly on \([0,\infty)\).
Convolving with the gamma density and multiplying by
\(\Gamma(3/2)e^x/K\) gives (16) for \(j=0\); interchanging the sum
and integral is justified by
\(0\le J_{b_n}(x)\le(2/3)x^{3/2}\) and \(\sum|d_n|<\infty\).
The identity \(J_b'=\sqrt{x}-bJ_b\) follows by differentiation of
its defining integral. Iterating it proves (17).

Fix \(0<\ell\le x\le r<\infty\), and write
\[
 B_j(b;\ell,r)=\frac23 r^{3/2}b^j+
 \sum_{v=0}^{j-1}b^{j-1-v}|(1/2)_{\underline v}|
              \max\{\ell^{1/2-v},r^{1/2-v}\}.                   \tag{18}
\]
For \(j=0\) the sum is empty. Formula (17) bounds
\(|J_b^{(j)}(x)|\) by \(B_j\). The preceding summability therefore
proves uniform derivative convergence on this compact interval,
justifying the remaining claims in (16) by termwise differentiation.
For a truncation after \(N\) terms, let
\(\rho_{N,j}=2\,3^j/(2^{N+1}-1)\). If \(\rho_{N,j}<1\), then
\[
 \sup_{\ell\le x\le r}\left|
 Q^{(j)}(x)-\sum_{n=1}^N d_nJ_{b_n}^{(j)}(x)\right|
 \le\frac{|d_{N+1}|B_j(b_{N+1};\ell,r)}{1-\rho_{N,j}}.          \tag{19}
\]
Indeed \(b_{n+1}/b_n\le3\); the polynomial in (18) has nonnegative
coefficients and degree at most \(j\). Successive majorants in the
omitted series have ratio at most
\(2\,3^j/(2^n-1)\le\rho_{N,j}\) for \(n\ge N+1\).
Summing this geometric majorant proves (19). These are exact analytic
bounds; rounded evaluations of their right sides are not enclosures.

One exact, convergent evaluation formula, with \(t=bx\), is
\[
 J_b(x)=\frac{\sqrt{x}}b\left[
 1-e^{-t}\sum_{k\ge0}\frac{t^k}{k!(2k+1)}\right].              \tag{20}
\]
Integration by parts reduces \(J_b\) to the integral of
\(u^{-1/2}e^{bu}\). The substitution \(u=xv^2\), followed by the
uniformly convergent exponential power series on \(0\le v\le1\),
gives (20). No singular derivative of the original gamma density is
being integrated here.

For later sign checking set \(F=D_3(Q;\cdot)\) and \(Z=F/Q^3\).
Since \(Q>0\), these share their zeros. Exponential conjugation gives
\(D_3(p;x)=(K/\Gamma(3/2))^3e^{-3x}F(x)\); at a zero their
derivatives have the same sign. Differentiating the determinant gives
\[
 F'(x)=-\det\begin{pmatrix}
 Q&Q'&Q''\\Q'&Q''&Q'''\\Q'''&Q^{(4)}&Q^{(5)}
 \end{pmatrix},\qquad
 Z'=F'/Q^3-3FQ'/Q^4.                                       \tag{21}
\]
Only the derivative of the last row remains: the other two differentiated
rows duplicate a row already present. At a zero, \(Z'=F'/Q^3\).

The script `scripts/gamma-geometric/contact-diagnostic-895.py` records a
**noncertified diagnostic**, using (16)-(17) and (20) for moderate \(bx\),
and a truncated large-\(bx\) expansion otherwise. Its JSON records every
sample, the proposed contact, the analytic omitted-series expressions,
and all failures. Decimal rounding and the finite evaluation/large-\(bx\)
remainders are not enclosed. Agreement at higher precision is not an
error proof. Formula (19) controls only the omitted exponential series,
not these other errors or any unsampled points. In particular, no
effective positive endpoint interval has been joined to the grid,
and an earlier tangency has not been excluded by this diagnostic.
At attempt895 the strict first-contact conclusion therefore remained open;
the later certificate and endpoint join below resolve that obligation.

### Rigorous compact evaluation method (attempt896)

This continues exactly the fixed model in (16). No new theorem input is
needed: the following are finite Taylor, geometric-tail and Cauchy
estimates for the already established analytic expression. They replace
the diagnostic's unbounded evaluation errors; they do not make the
near-zero limit (11) effective.

For a positive rational center \(c\), put \(t=bc\). In (20), let
\[
 E_k=\sum_{v=0}^k\frac{t^v}{v!},\qquad
 S_k=\sum_{v=0}^k\frac{t^v}{v!(2v+1)},\qquad
 T_k=\frac{t^{k+1}}{(k+1)!}\frac1{1-t/(k+2)}.
\]
When \(k+2>t\), the successive omitted exponential terms have ratio
at most \(t/(k+2)<1\). Thus both omitted positive tails are at most
\(T_k\), and
\[
 e^t\in[E_k,E_k+T_k],\qquad
 \sum_{v\ge0}\frac{t^v}{v!(2v+1)}\in[S_k,S_k+T_k].       \tag{22}
\]
Interval division of the second enclosure by the first encloses the
product with \(e^{-t}\) in (20). This avoids rounding a tiny exponential
before multiplying it by a large sum. The implementation uses (22) for
\(t\le1024\), stopping after \(k>2t\) and an enclosed relative term
test; correctness uses the explicit \(T_k\), not the stopping test.

For larger \(t\), change variables in the defining integral to obtain
\[
 J_b(c)=\frac{\sqrt c}{b}I(t),\qquad
 I(t)=\int_0^t e^{-v}(1-v/t)^{1/2}\,dv.
\]
Write \(a_k=(-1)^k(1/2)_{\underline k}/k!\). For \(m\ge1\),
the absolute values of the nonconstant binomial coefficients decrease.
On \(0\le z\le1/2\), the Taylor remainder of \((1-z)^{1/2}\)
after degree \(m-1\) is therefore at most \(2|a_m|z^m\).
Integrating over \(0\le v\le t/2\) bounds that error by
\(2|(1/2)_{\underline m}|t^{-m}\). If \(t\ge4m\), integration
by parts in the integer gamma tail gives, for \(0\le k<m\),
\[
 \int_{t/2}^\infty e^{-v}v^k\,dv
 =e^{-t/2}(t/2)^k\sum_{r=0}^k
                  (k)_{\underline r}(t/2)^{-r}
 \le2e^{-t/2}(t/2)^k.
\]
The polynomial's omitted tail is consequently bounded by
\(2e^{-t/2}\sum_{k<m}|a_k|2^{-k}<4e^{-t/2}\), since
\(|a_k|\le1\). The true integral's tail from \(t/2\) to \(t\)
is at most \(e^{-t/2}\). Combining all three errors proves
\[
 \left|I(t)-\sum_{k=0}^{m-1}
              \frac{(-1)^k(1/2)_{\underline k}}{t^k}\right|
 \le \frac{2|(1/2)_{\underline m}|}{t^m}+5e^{-t/2}
 \le \frac{2|(1/2)_{\underline m}|}{t^m}
                 +5\,256!(2/t)^{256}.                    \tag{23}
\]
The last inequality follows from the single positive term of the
exponential series \(e^{t/2}\ge(t/2)^{256}/256!\).
The code uses \(m=160\) only when \(t>1024>4m\), so every
quantity in this error bound is rational. Equation (23) is not an
uncontrolled asymptotic expansion.

Center derivatives through order 16 follow from (17), with all
intervals retained during the recurrence. Sum the first 48 terms in
(16) and add the symmetric remainder (19), separately for each order
\(0\le j\le16\), with \(\ell=r=c\). Its hypothesis
\(2\,3^j/(2^{49}-1)<1\) holds for all these orders and is checked
by exact rational comparison. In particular, higher derivatives used
to propagate the cells also include the infinite-series tail.

For completeness, the complex estimate used for whole-cell coverage
does not assume anything about the zero set. On \(\Re z>0\) define
\[
 J_b(z)=z^{3/2}\int_0^1 u^{1/2}e^{-bz(1-u)}\,du
\]
using the analytic branch positive on the positive axis. It agrees
with the real integral and satisfies \(|J_b(z)|\le(2/3)|z|^{3/2}\).
From the exact coefficients in (16),
\[
 \sum_{n\ge1}|d_n|
 \le\frac{66}7+\frac{32}{315}\frac1{1-2/31}<10.
\]
Here the first four terms sum to \(66/7\), and the subsequent ratios
are at most \(2/31\). The sum defining \(Q(z)\) thus converges
uniformly on compact subsets of the half-plane and is analytic.
On the disk \(|z-c|\le R=c/2\),
\[
 |Q(z)|\le\frac{20}3(3c/2)^{3/2}<13c^{3/2}=:M_c.        \tag{24}
\]
For its Taylor coefficients \(A_k=Q^{(k)}(c)/k!\), Cauchy's
estimate gives \(|A_k|\le M_c R^{-k}\).

Let \(0\le\delta<R\), \(\theta=\delta/R\), and use the center
jet through order \(m=16\). For \(|h|\le\delta\) and
\(0\le j\le5\), termwise differentiation of the analytic Taylor
series, followed by its absolutely convergent tail, gives
\[
 Q^{(j)}(c+h)=\sum_{k=0}^{m-j}
       \frac{Q^{(j+k)}(c)}{k!}h^k+\mathcal E_j,
\]
\[
 |\mathcal E_j|\le
 M_c R^{-j}\frac{(m+1)!}{(m+1-j)!}
 \frac{\theta^{m+1-j}}
 {1-\theta(m+2)/(m+2-j)}.                              \tag{25}
\]
The displayed denominator is required to be positive. Indeed, the
first omitted coefficient in the differentiated tail has precisely
the displayed prefactor, and subsequent majorants have ratio at most
\(\theta(m+2)/(m+2-j)\); these ratios decrease with the index.
The code starts cell evaluation only when \(\delta\le c/256\),
so this condition holds. Interval Horner evaluation on
\(h\in[-\delta,\delta]\), enlarged by (25), covers every point
of the closed cell, not only its center.

The implementation is `scripts/gamma-geometric/contact-certificate-896.py`.
All arithmetic enclosures use pairs of arbitrary-size integers, whose
represented values are the endpoints multiplied by \(2^{-512}\).
An exact rational is enclosed by integer floor/ceiling division.
Addition/subtraction use endpoint formulas; multiplication and division
use the extrema of the four endpoint combinations, rounded outward.
Division asserts that the denominator interval excludes zero. Scaling
by an exact rational rounds only after multiplication by its numerator
and division by its denominator. This matters for the very small
coefficients \(d_n\). Square roots use integer square roots of the
scaled endpoints, with one integer added to the upper bound unless it
is already exact. Repeated multiplication, Horner evaluation and every
error addition preserve inclusion by induction. No floating-point or
special-function evaluation participates in a proof decision.

For each cell, the enclosed derivatives are inserted into the exact
determinant expressions (21) for \(F,F'\), and then into
\(Z=F/Q^3\) and \(Z'=F'/Q^3-3FQ'/Q^4\), after checking
the lower endpoint of \(Q\) is positive. Positive-prefix cells
must have \(\inf Z>0\); decreasing-contact cells must have
\(\sup Z'<-1/5000\). Failed cells are bisected, with explicit
failure and iteration limits, rather than silently accepted. The
certificate records every accepted closed cell and its enclosures,
every unresolved cell, and endpoint evaluations. Sorting the accepted
cells and checking equality of all consecutive rational endpoints
verifies the claimed coverage. No observation from diagnostic895 is
an input to these acceptance tests.

The actual cell implementation uses the following conditioning step,
including its effect on (25). Freeze any real rational \(a\) on a
given cell and set \(P_a(z)=e^{-a(z-c)}Q(z)\). Its center jet is
\[
 P_a^{(j)}(c)=\sum_{k=0}^j\binom jk(-a)^{j-k}Q^{(k)}(c).
                                                               \tag{26}
\]
Triangular row and column transformations of the derivative matrix
give \(D_3(P_a;x)=e^{-3a(x-c)}D_3(Q;x)\). Thus
\(D_3(P_a;x)/P_a(x)^3=Z(x)\) throughout the cell, and differentiating
this identity gives exactly the same \(Z'\). No hypothesis on the
accuracy of \(a\) is needed. The code chooses it as the ratio of
the sums of the endpoints of the center enclosures of \(Q'\) and
\(Q\), so that it is exact rational and cancels most of the center's
first logarithmic derivative; the denominator is positive.

For (25) applied to \(P_a\), replace \(M_c\) by
\[
 M_{c,a}=3^{\lceil |a|R\rceil}M_c.                         \tag{27}
\]
Indeed \(|e^{-a(z-c)}|\le e^{|a|R}\le3^{\lceil |a|R\rceil}\),
including \(a=0\). The elementary bound \(e<3\) follows by
bounding the exponential series tail using \(k!\ge2^{k-1}\) for
\(k\ge2\), with strict inequality for \(k\ge3\). Formula (26)
is evaluated with the entire enclosed order-16 jet before interval
Horner evaluation. Inserting the resulting derivatives of \(P_a\)
in (21) therefore bounds the invariant \(Z,Z'\) with (27) paying
for the exponential conditioning. Every cell records its exact tilt.
In the certificate's cell records, `Q_tilt` encloses \(P_a\) and `F`
encloses \(D_3(P_a)\); endpoint records use the unmodified \(Q\).
Only the common \(Z,Z'\) bounds determine acceptance.

### Certified compact signs (attempt896)

Run, from the active notebook directory,

    python3 scripts/gamma-geometric/contact-certificate-896.py
    python3 scripts/gamma-geometric/contact-ledger-check-896.py

The full enclosure artifact is
`scripts/gamma-geometric/contact-certificate-896.json`.
It uses 944 accepted cells covering \([1/32,139/32]\) and one
cell covering \([139/32,35/8]\); no failed or unprocessed cell
remains. The full-cell ledger check and exact rational threshold
comparisons are saved in
`scripts/gamma-geometric/contact-certificate-ledger-check-896.json`.
The latter checks every saved cell, rather than a preview or sample;
it is not an independent replay of the analytic enclosure computation.
The recorded outward bounds imply
\[
 Z(x)>\frac1{4\,000\,000}\quad(1/32\le x\le139/32),
 \qquad
 Z'(x)<-\frac{213}{10^6}<-\frac1{5000}
                  \quad(139/32\le x\le35/8),             \tag{28}
\]
and the separately enclosed endpoint values satisfy
\[
 \frac{5694}{10^9}<Z(139/32)<\frac{5695}{10^9},\qquad
 -\frac{2495}{10^9}<Z(35/8)<-\frac{2494}{10^9}.           \tag{29}
\]
All strict comparisons in (28)-(29) are integer/rational comparisons
against outward interval endpoints, including the positive margin
on the entire compact prefix. The proof of their inclusion is
(16)-(19), (22)-(27), and the arithmetic induction just specified.
The earlier diagnostic, its approximate zero and precision replay
are not used to certify these inequalities.

The intermediate value theorem applied to (29), and strict decrease
from (28), now give exactly one zero \(x_c\) in
\((139/32,35/8)\), with \(Z'(x_c)<0\). Positivity on
\([1/32,139/32]\), together with strict decrease to that zero,
excludes all zeros in \([1/32,x_c)\). As in (21),
\[
 D_3'(p;x_c)
 =\left(\frac K{\Gamma(3/2)}\right)^3
       e^{-3x_c}Q(x_c)^3 Z'(x_c)<0.
\]
Thus the compact certificate supplies a local simple downward contact.
By itself it leaves \((0,1/32)\) uncovered: (11) gives no effective
endpoint. The following argument closes exactly that interval.
The canonical analytic proofs and computer-assisted extension pass
critical audit898 below. There is no actual-Xi identification
or transfer.

### Effective endpoint join by a finite head (attempt897)

Set \(L=1/32\). Split the *same* law as
\[
 p=h*q,\qquad h=f*k_2,\qquad
 k_2(x)=2e^{-2x}1_{\{x>0\}},
\]
where \(q\) is the density of \(\sum_{n\ge2}E_n\).
In particular \(q(x)=2g(2x)\). Hence \(q\) is smooth and flat at
zero, is zero on \((-\infty,0]\), is positive on \((0,\infty)\),
and all its derivatives are bounded by (4). The estimates below concern
this factorization only; neither the density nor its parameters change.
No Gaussian-limit rate or extrapolation of the compact certificate is
used. The finite-head estimates, strictness and support qualifications
are supplied explicitly because the source inputs do not state them.

For \(x>0\), direct convolution gives
\[
 h(x)=\frac{2}{\Gamma(3/2)}e^{-2x}x^{b}\mathcal A(x),\qquad
 b=\frac32,\qquad
 \mathcal A(x)=\int_0^1 t^{1/2}e^{xt}\,dt.                 \tag{30}
\]
Let \(T\) have density \(t^{1/2}e^{xt}/\mathcal A(x)\) on \((0,1)\).
Differentiation under this bounded-support integral gives
\[
 \kappa_2=(\log\mathcal A)''=\operatorname{Var}(T),\quad
 \kappa_3=(\log\mathcal A)'''=\mathbb E(T-\mathbb ET)^3,
\]
\[
 \kappa_4=(\log\mathcal A)''''=
 \mathbb E(T-\mathbb ET)^4-3\operatorname{Var}(T)^2.
\]
For completeness these identities follow successively from
\((\mathbb E_x F(T))'=\mathbb E_x(TF(T))-
\mathbb E_xT\,\mathbb E_xF(T)\) for an \(x\)-independent \(F\),
and the product rule for the central moments. Thus
\[
 0\le\kappa_2\le1,\qquad |\kappa_3|\le1,\qquad
 |\kappa_4|\le4.                                        \tag{31}
\]
These coarse bounds hold uniformly in \(x\), since
\(|T-\mathbb ET|\le1\).

For any positive \(C^4\) function \(h\), writing \(\ell=\log h\),
direct determinant expansion yields
\[
 \frac{D_2(h)}{h^2}=-\ell'',\qquad
 \frac{D_3(h)}{h^3}=(\ell''')^2-\ell''\ell''''-2(\ell'')^3.
                                                               \tag{32}
\]
One can verify the latter by multiplying by an exponential to make
\(\ell'=0\) at the point: the normalized derivative matrix then has
first row \((1,0,\ell'')\), second row
\((0,\ell'',\ell''')\), and last entry
\(\ell''''+3(\ell'')^2\). Such exponential multiplication is a
triangular row/column operation and leaves the normalized determinant
unchanged.

Put \(u=x^2\kappa_2\), \(v=x^3\kappa_3\), \(w=x^4\kappa_4\).
Equation (30) gives
\(x^2\ell''=-b+u\), \(x^3\ell'''=2b+v\), and
\(x^4\ell''''=-6b+w\). With \(b=3/2\), (32) becomes
\[
 x^6\frac{D_3(h;x)}{h(x)^3}
 =\frac94-\frac92u+6v+v^2+(b-u)w+9u^2-2u^3.
\]
For \(0<x\le L\), we have \(0\le u\le x^2\le1/1024\),
\(|v|\le x^3\), and \(|w|\le4x^4\). In particular
\(0<b-u\le b\) and \(9u^2-2u^3\ge0\). Consequently
\[
 \frac{D_2(h;x)}{h(x)^2}\ge\frac{1535}{1024x^2}>0,
\qquad
 x^6\frac{D_3(h;x)}{h(x)^3}
 \ge\frac94-\frac92x^2-6x^3-6x^4
 \ge\frac94-\frac{4806}{1048576}>2.                     \tag{33}
\]
The final comparison is exact: \(4806<1048576/4=262144\).
This is an effective finite-head sign on the entire required interval.

To transfer it, the confluent signs must first be converted to signs
of the shifted derivative columns actually appearing in composition.
On \((0,L]\) define
\(A=h'/h\) and \(B=h''/h\). We have
\(A'=-D_2(h)/h^2<0\). Factoring \(h\) out of the three functions
in their Wronskian gives
\[
 A'B''-A''B'=-D_3(h)/h^3<0,\qquad
 \frac{d^2B}{dA^2}=\frac{A'B''-A''B'}{(A')^3}>0.         \tag{34}
\]
Thus \(B\), as a function of the strictly monotone coordinate \(A\),
is strictly convex. For \(0<y_1<y_2<y_3<x\le L\), the points
\(x-y_k\) decrease and \(A(x-y_k)\) strictly increase. Strictly
increasing secant slopes of this convex graph give
\[
 \det[ h^{(i)}(x-y_k)]_{\substack{0\le i\le2\\1\le k\le3}}>0.
                                                               \tag{35}
\]
Indeed divide its columns by the positive \(h(x-y_k)\); the result
has rows \(1,A,B\). Subtract its first column from the other two.
Its determinant is the product of the two positive \(A\)-increments
and the positive difference of the corresponding secant slopes.
This proves (35) without assuming any general preservation theorem
from local confluent positivity.

The needed tail sign is
\[
 \det[q^{(j)}(y_i)]_{\substack{1\le i\le3\\0\le j\le2}}\le0
 \qquad (y_1<y_2<y_3).                                  \tag{36}
\]
Here are the finite-kernel, limit and confluence checks. Each exponential
translation kernel \(k_\lambda(r-s)\) has nonnegative minors of orders
at most three (in fact all orders). After positive exponential row and
column factors are removed, its matrix is \([1_{\{r_i>s_j\}}]\)
with increasing nodes. Each row is an initial string of ones followed
by zeros; the row lengths are nondecreasing. A square determinant
vanishes if a row has length zero or two rows have equal length.
Otherwise the row lengths are \(1,2,\ldots,m\), giving determinant one.

Finite convolutions preserve these minor signs. The required continuous
Cauchy--Binet identity follows by expanding the two determinants in
\[
 \det\left[\int K(r_i,z)L(z,s_j)\,dz\right]
 =\frac1{m!}\int_{\mathbb R^m}
       \det[K(r_i,z_k)]\det[L(z_k,s_j)]\,d\mathbf z.      \tag{37}
\]
Fubini and relabeling integration variables give the displayed equality.
For finite exponential convolutions all these terms are absolutely
integrable: each separated integral is a finite convolution value,
and the one-sided support restricts the relevant variable to a bounded
interval between the outer nodes. The product of determinants is
symmetric in the \(z_k\), so its sign can be read on ordered nodes.
This supplies the order-three identity and its applicability directly;
no additional source theorem about the present model is imported.

The densities of finite tail sums converge pointwise to \(q\).
To check this, keep the first two tail exponentials (rates 4 and 8)
as a bounded continuous density and convolve it with the remaining
partial sums. These sums converge almost surely. Bounded convergence
gives convergence at every real argument, including the zero extension.
Thus their nonnegative translation minors pass to \(q\).
Apply a third-order minor to increasing row nodes \(y_i\) and column
nodes \(0,\varepsilon,2\varepsilon\). Subtract column one from
column two, and replace column three by its second finite difference.
Taylor expansion, using the smoothness of \(q\), then gives
\[
 \varepsilon^{-3}\det[q(y_i-(j-1)\varepsilon)]_{i,j=1}^3
 \longrightarrow -\det[q^{(j)}(y_i)]_{i=1,2,3; j=0,1,2}.
\]
The left side is nonnegative for every \(\varepsilon>0\), proving (36).

For every \(x>0\), (36) is *strict* at some ordered triple in \((0,x)\).
Otherwise the vectors \((q(y),q'(y),q''(y))\), \(0<y<x\), would
span a space of dimension at most two. There would be a nonzero constant
triple \((c_0,c_1,c_2)\) such that
\(c_0q+c_1q'+c_2q''=0\) throughout that interval. If \(c_2\ne0\),
this is a homogeneous constant-coefficient first-order system for
\((q,q')\), with zero initial data at zero by flatness. Multiplying
by the matrix exponential of the negative coefficient matrix shows
that its solution is zero. If \(c_2=0\), the identical first-order
argument, or \(c_0q=0\), applies. Every case contradicts \(q(y)>0\).
Hence such a triple exists; continuity supplies an open set of triples
on which the determinant in (36) is strictly negative.

Finally all derivatives and integrals in the composition with \(h\)
are legitimate despite its singular second derivative at zero.
The zero extensions obey
\(h'=2f-2h\) and \(h''=2f'-2h'\) in the weak sense and classically
away from zero. Since \(f,f'\in L^1\), all of \(h,h',h''\) lie
in \(L^1\). Also \(h(0)=h'(0)=0\), so these weak derivatives have
no boundary atom. The bounded smooth derivatives of \(q\) therefore
give the classical identity
\[
 p^{(i+j)}(x)=\int_0^x h^{(i)}(x-y)q^{(j)}(y)\,dy,
                 \qquad 0\le i,j\le2.                  \tag{38}
\]
It follows either by differentiation of convolution in distributions,
followed by continuity, or by integration by parts with the stated
vanishing boundary data. Each integrand is absolutely integrable.
Expansion of (37) remains valid here: every product term is a product
of three such absolutely integrable one-variable terms.
Restricting to ordered nodes gives
\[
 D_3(p;x)=\int_{0<y_1<y_2<y_3<x}
   \det[h^{(i)}(x-y_k)]_{i=0,1,2; k=1,2,3}
   \bigl(-\det[q^{(j)}(y_k)]_{k=1,2,3; j=0,1,2}\bigr)
   \,d\mathbf y>0\quad(0<x\le1/32).                    \tag{39}
\]
The integrand is nonnegative by (35)-(36) and positive on the open set
just proved to exist. This establishes strict positivity, not merely
nonnegativity or a sign at sampled points.

Joining (39) to (28)-(29) proves that the unique local downward zero
\(x_c\in(139/32,35/8)\) is the first positive zero \(x_*\), with
\(D_3'(p;x_*)<0\). The global lower signs (2) supply the requested
neighborhood condition. The claimed model witness now has a complete
written argument, validated by audit898 of both the analytic proof
and the finite certificate. No estimate or positivity statement has
been transferred to actual Xi. ∎

### Critical audit898: analytic review and full arithmetic replay

The 14 November 2026 review reuses assessment892's unchanged source
coverage and the precise imports above. It checks the whole argument,
including the auxiliary asymptotics, rather than inferring correctness
from the diagnostic or the saved ledger. The analytic checks below are
complete, and the full replay898 also passes as recorded below.

For (1)-(8), finite-head differentiation has bounded continuous
derivatives and a finite tail exponential moment. This gives smoothness,
flatness and the asserted derivative decay independently at each order.
The support argument gives strict positivity, not just almost-everywhere
positivity. The canonical kernel is decreasing and integrable even though
it diverges at zero; the cited singular-kernel scalar theorem applies.
In the covariance argument both scores and their product are absolutely
integrable. Strict negativity follows on a product of two open intervals;
no unjustified second differentiation of the gamma density is used.

For (9)-(15), the common Fourier majorant remains integrable after four
derivatives, and the tilted means cover a whole interval next to zero.
At infinity all integrations by parts take place away from the singular
gamma endpoint; flatness and exponential decay pay both boundary terms.
The leading determinant is (1/4), with the outer minus sign in D3.
These checks validate the preserved asymptotic conclusions, although
the effective first-contact proof uses (28)-(39) instead.

For (16)-(29), the review checks the finite partial-fraction coefficients,
locally uniform derivative series, omitted-series ratio for every order
through 16, both finite-evaluation remainder regimes, and the analytic
disk estimate. The differentiated Taylor tail has exactly the ratio
in (25). The exact rational tilt preserves Z and Z', while (27) pays
its complex exponential factor. The reviewed code implements these
bounds, including every center derivative and the infinite-series tail.
The source's diagnostic root, floating-point computations and sample
agreement supply no input to this proof.

For (30)-(39), the constants in (33) are checked as rational inequalities.
Strict convexity in (34) proves the needed shifted-column sign, which
does not follow merely by naming local confluent positivity. The tail's
third-order confluence has the minus sign in (36) and no missing
factorial. If all its minors vanished on an initial interval, the
resulting constant-coefficient ODE and flat initial data would force
q=0 there, contradicting its strict positivity. This gives a strict
minor on an open set. The finite head has two L1 weak derivatives and
h(0)=h'(0)=0, so (38) has no boundary atom. Absolute integrability of
each separated product pays Fubini in the determinant composition.
The factor 1/3! in (37) is removed exactly by restricting to ordered
nodes. Thus (39) gives strict positivity throughout the entire open
endpoint interval, including its join to 1/32.

The separate replay is run with

    python3 scripts/gamma-geometric/contact-audit-replay-898.py

Its full output is `scripts/gamma-geometric/contact-audit-replay-898.json`.
The new backend performs endpoint operations as exact Python Fractions
and rounds outward to the dyadic grid; it also checks both integer
square-root inequalities. It reuses the inspected generator896 formulas,
so this is an independent arithmetic implementation, not a second
independent derivation of the analytic remainder bounds. Every saved
cell and both endpoint enclosures are recomputed, compared exactly,
and tested against the claimed rational margins. Historical artifacts896
are preserved, including their then-unresolved endpoint flags.

Audit result: PASS. All 945 closed cells and both endpoints reproduce
the saved intervals exactly; the complete traversal finds no coverage
gap, unresolved cell or failed inequality. The replay also verifies the
original ledger's certificate hash and cell counts. The fully inspected
summary records Z>1/4000000 on the compact prefix, Z'<-213/1000000
on the contact interval (required Z'<-1/5000), and the endpoint intervals
(5694,5695)/10^9 and (-2495,-2494)/10^9. The complete recomputed
enclosures, exact extrema and empty failure list are retained on disk.

The analytic positivity on (0,1/32] and the closed prefix coverage join
without a gap. Strict decrease and the opposite endpoint signs give
exactly one zero in (139/32,35/8); there is no earlier zero. At that
zero the positive factors in (21) transfer Z'<0 to D3'(p)<0, while
(2) supplies both lower signs on every required neighborhood. This
accepts the fixed-model witness and discharges its candidate label.
It establishes a limitation of a generic scalar first-contact barrier,
not a sign for actual Xi or a claim of progress beyond the literature
checked. No mathematical premise from C466a, C466b or C466c is used
in this model proof; the empty C466d row in the DAG remains correct.

## Mathlib

Full matching coverage for this fixed model, its strict curvature
and its third-determinant endpoint signs has not been checked.
Fourier inversion, convolution differentiation, determinants and
probability transforms are supporting topics; no matching theorem
name or formal verification is asserted for the joint statement.
The earlier assessed compact-support convolution declarations alone
do not cover the noncompact argument: the needed derivative bounds
and dominating functions are explicitly supplied above.
Matching Mathlib coverage for (16)-(21) has not been checked; no formal
verification is claimed for the evaluation formula or the diagnostic.
Matching coverage for the interval bounds and conclusions (22)-(29) is also unchecked.
The integer certificate is not a Lean proof; its acceptance depends on
the explicit analytic estimates and the recorded implementation.
Full matching coverage for the effective head bound, strict composition
and first-contact join (30)-(39) is unchecked. The standard determinant
composition identity is supporting mathematics; it alone does not give
the model's strictness, endpoint bounds or certified compact signs.
