# Lemma 648: reflection makes the output positive but loses the angular rate

## Hypotheses

Retain the approved angular family: n>=5, x=-d=-5/4, R=11/8,
U=R^2, eta=1/100, t_j=j/n for 0<=j<n, and |u|=1. Let Z be
a common finite set of distinct poles with Re(a)=x, |a|<=R-eta
and x in Z, with positive integer original simple-pole residues r_a
and M=sum r_a<=n/3. The same poles and residues serve every angle.
Define

    B_u(v)=product_(j<n) R*(v-t_j*u)/(U-t_j*v/u),
    q_u(zeta)=sum_a r_a B_u(x)/[B_u(a)*(R*zeta-a)],
    B_u^sharp(z)=conjugate(B_u(2*x-conjugate(z))),
    f_u(zeta)=1/B_u^sharp(R*zeta).

The inverse in the last expression means its rational extension at
poles of B_u^sharp. Use C645g's normalized boundary L2 norm, H^2
with nonnegative modes, H^2_- with strictly negative modes, and the
largest Hankel norm of H_u h=P_-(q_u h). No separation, symmetry,
or positivity of the original complex weighted amplitudes is assumed.
The relation u=i exp(i theta) retains the conjugated denominator angle.

## Conclusion

The reflected input is nonzero and holomorphic on a neighborhood of
the closed unit disk. Its exact complete output is

    H_u f_u=B_u(x) sum_a r_a/[|B_u(a)|^2 (R*zeta-a)].       (1)

Thus its residue weights after removal of the common scalar are
positive. In particular

    ||H_u|| >= 1/[R |B_u(x)| ||f_u||_2].                  (2)

Nevertheless this input cannot establish the approved angular bound.
For the admissible family Z={x}, r_x=1, put

    J_n(u)=||H_u f_u||_2/||f_u||_2,
    C=8 exp(55/4)/sqrt(21).

For every n>=11 and every |u|=1,

    J_n(u) <= C sqrt(n) exp(-n/25).                      (3)

Consequently

    exp(n/32) (mean_u J_n(u)^2)^(1/2)
        <= C sqrt(n) exp(-7*n/800) -> 0.                (4)

The actual operator on this family satisfies ||H_u||>=8/sqrt(21)
at every angle. Therefore (3)--(4) stop only this specified reflected
input, including its complete output and arbitrary scalar normalization.
They are not an operator countersequence, a disproof of the signed
energy comparison E_n>=c exp(-n/16)D_single,n, or a disproof of the
detector. Actual-Xi realization and all-degree signs remain open.

The proof is author-checked and separately unaudited. POTENTIALLY_NEW
records the bounded source comparison, not certified originality.

## Proof

### 1. Source scope and the quantitative test

The unchanged invocation-start
[angular EXPLORE assessment](../drafts/literature/2026-11-02-rotation-averaged-anchor-line-hankel.md)
covers the same family, largest norm, and finite Fourier/residue tests.
The present test was found while investigating complete signed-energy
coercivity. It addresses the same detector by a different input; no
coercivity conclusion follows from it. Scoped searches of the C645
angular results and associated drafts/attempts found no prior use of
reflection across this common pole line as an input. C645o's negative
cross entry, C645n's full-inner-input deficit, L646's minimum exact-output
stop and L647's constant-coercivity obstruction are retained as contrasts.
Only C645g's spaces and C645n's finite-pole projection identity are
local mathematical inputs. None of those method stops is assumed to
be a lower bound or an upper bound for the full angular operator.

Import the Hardy projection convention from L. Baratchart,
S. Chevillard and T. Qian, *Minimax principle and lower bounds in
H2-rational approximation*, J. Approx. Theory 206 (2016), 17--47,
[arXiv:1501.01161v2](https://arxiv.org/pdf/1501.01161v2),
24 March 2015, Section 4, (17)--(19),
[DOI](https://doi.org/10.1016/j.jat.2015.03.004).
Import Fourier orthogonality/Parseval from A. Levitt, *Analyse de
Fourier et applications*, version retrieved 2 November 2026,
[Theorem 1.3/Exercise 1.2 and Theorem 1.11/Corollary 1.12,
printed pp.6,8](https://www.imo.universite-paris-saclay.fr/~antoine.levitt/blog/fourier/article.pdf).
These are the primary statements already inspected in the assessment.
Normalized angular measure makes each circle exponential a unit vector.
The rational specialization and radial estimates below evaluate this
particular input; no Nehari or Parseval theorem is reproved.

### 2. Holomorphy and the positive output

The inverse reflection has the explicit rational expression

    1/B_u^sharp(z)
      =product_(j<n) [U-t_j*u*(2*x-z)]/[R*(2*x-z-t_j/u)]. (5)

Its possible poles z=2*x-t_j/u satisfy

    |z|>=2*d-t_j>3/2>R.

Thus f_u is holomorphic near the closed disk. On the pole line,
2*x-conjugate(a)=a. All original B_u(a) are finite and nonzero:
|a|>=d>1>t_j, and |U-t_j*a/u|>=U-t_j*|a|>0.
Hence f_u(a/R)=1/conjugate(B_u(a)). In particular f_u(x/R) is
nonzero, so its norm is nonzero.

For f holomorphic near the closed disk and |alpha|<1, C645n's
finite-pole identity is

    P_-[f(zeta)/(zeta-alpha)]=f(alpha)/(zeta-alpha).

Indeed subtracting f(alpha) leaves an analytic removable quotient.
Apply this identity term by term to the finite sum defining q_u,
using alpha=a/R and the exact factor 1/R. This proves (1).
The coefficient of zeta^(-1) in (1) is

    [B_u(x)/R] sum_a r_a/|B_u(a)|^2.

Its modulus is at least 1/(R|B_u(x)|), because every summand is
positive and r_x>=1. Parseval and normalization of f_u prove (2).
The geometric series are absolutely uniformly convergent on the
boundary for every fixed family, since |a|/R<=273/275<1.

For the anchor-only family q_u=1/(R*zeta-x). The same projection
identity and the geometric-series norm give exactly

    J_n(u)=1/[sqrt(U-d^2) |B_u(x)| ||f_u||_2],
    ||H_u 1||_2=1/sqrt(U-d^2)=8/sqrt(21).                (6)

This family obeys M=1<=n/3 for every n>=5. It supplies the required
test of the input without any changing poles or fractional residues.

### 3. A uniform radial product gain

Put r=2*d-R=9/8. For r<=s<=d, 0<=t<=1 and c=Re(u), let

    b_(u,t)(v)=R*(v-t*u)/(U-t*v/u),
    A(c)=s^2+t^2+2*s*t*c,
    D(c)=U^2+s^2*t^2+2*U*s*t*c,
    N(c)=s*(U+t^2)+t*(U+s^2)*c,
    K=(s+t)*(U+s*t).

The denominators are strictly positive: s>t and U>s*t. Direct
differentiation of |b_(u,t)(-s)|^2=U*A(c)/D(c) gives

    partial_s log|b_(u,t)(-s)|=(U-t^2) N(c)/[A(c)D(c)]. (7)

We claim this is at least

    g(s,t)=(U-t^2)/[(s+t)*(U+s*t)]>0.                  (8)

Here is a complete sign check. The polynomial
F(c)=N(c)K-A(c)D(c) is concave in c, with quadratic coefficient
-4*U*s^2*t^2. At c=1, N(1)=K and A(1)D(1)=K^2, so F(1)=0.
At c=-1, N(-1)=(s-t)(U-s*t)>0 and A(-1)D(-1)=N(-1)^2.
Moreover K-N(-1)=2*t*(U+s^2)>=0. Thus

    F(-1)=N(-1)[K-N(-1)]>=0.

A concave function on [-1,1] lies above its endpoint chord, so
F(c)>=0 throughout. Dividing by the positive A(c)D(c)K proves
(8), including t=0, where equality holds. This checks all angles,
not only the real direction used in the diagnostic.

Integrate (7)--(8) from r to d and sum at t_j=j/n:

    log(|B_u(-d)|/|B_u(-r)|)
       >= integral_r^d sum_(j<n) g(s,j/n) ds
       >= n gamma,
    gamma=integral_r^d integral_0^1 g(s,t) dt ds.         (9)

The last step follows because g(s,t) decreases in t: its positive
numerator decreases and both positive denominator factors increase.
Thus its left Riemann sum dominates its integral. All integrands
are continuous on the closed rectangle; no limiting interchange is
needed. Also g decreases in s. Subdivide [0,1] into four intervals
and use the lower corner value in both variables to obtain

    gamma >= [(d-r)/4] sum_(k=1)^4 g(d,k/4)
          =2125341605/52856645184
          >1/25>1/32.                                 (10)

In particular the comparison in (9) is uniform in n and u. It is a
lower bound for a product ratio, not a lower bound for a signed sum.

### 4. Convert the radial gain to an input-norm cost

For n>=11 set rho_n=1-1/n. At zeta=-rho_n the reflected point is

    2*x-conjugate(R*zeta)=-r-R/n.

The interval [r,r+R/n] is contained in [r,d], since R/11=d-r.
On that interval every factor has logarithmic derivative bounded by

    |partial_s log b_(u,t)(-s)|
       <=1/(s-t)+t/(U-s*t)
       <=1/(r-1)+1/(U-d)=392/41<10.                     (11)

Equivalently one may integrate the real logarithmic modulus derivative;
all factors are nonzero on the interval, so no global logarithm branch
is assumed. Sum (11) over n factors and integrate a distance R/n.
This yields

    |B_u(-r-R/n)|<=exp(10*R)|B_u(-r)|.                 (12)

The elementary Hardy point-evaluation inequality gives

    ||f_u||_2>=sqrt(1-rho_n^2)|f_u(-rho_n)|
       >=n^(-1/2) exp(-10*R)/|B_u(-r)|.                (13)

For completeness its exact specialization is Cauchy--Schwarz applied
to f_u(zeta)=sum_(k>=0)c_k zeta^k: Parseval gives sum|c_k|^2=||f_u||_2^2,
and sum rho_n^(2k)=1/(1-rho_n^2). The second inequality in (13) uses
1-rho_n^2=2/n-1/n^2>=1/n, (5), and (12).

Multiply (13) by |B_u(x)| and apply (9)--(10). Substitution in (6)
gives

    J_n(u)<=exp(10*R) sqrt(n) exp(-gamma*n)/sqrt(U-d^2)
           <=[8 exp(55/4)/sqrt(21)] sqrt(n) exp(-n/25).

This proves (3). Its bound is uniform on the angular circle, so
integration and 1/25-1/32=7/800 prove (4). No estimate on a selected
input has been used as an upper bound for the largest operator norm.

### 5. Verification and limitations

The exploratory file `scripts/one-sided-hankel/angular-line-reflection-screen.json`
records a sampled continuum cost about 0.05282498, exceeding 1/32.
It has no quadrature or grid error enclosure and is not evidence for
any inequality in this proof. The uniform analytic argument instead
uses the rational lower bound (10), about 0.04020954, and (11).

Reproduce the exact constants with
`python3 scripts/one-sided-hankel/angular-line-reflection-certificate.py`.
The full certificate is `scripts/one-sided-hankel/angular-line-reflection-certificate.json`.
All 12 rational checks passed; the complete selected `/checks` field
was inspected using the shared JSON inspector. This verifies constants,
not independently the analytic argument. The squared-energy comparison
that motivated the attempt remains unproved and unrefuted. A more
general reflected construction with additional factors is not excluded;
it would require a specific new quantitative idea and its own test.

## Mathlib

Full matching coverage for this line-reflected input and its uniform
rate obstruction has not been checked. No absence claim is made.
Supporting ingredients are finite rational Hardy symbols, Fourier
orthogonality, geometric series, Cauchy--Schwarz, elementary differentiation,
and monotone Riemann sums. The inspected primary sources above cover
the projection and Fourier conventions, not the evaluated rate (10).
