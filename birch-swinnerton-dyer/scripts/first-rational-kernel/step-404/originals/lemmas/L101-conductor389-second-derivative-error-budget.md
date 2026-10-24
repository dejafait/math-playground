# L101 — Fixed second-derivative truncation and finite-error contract

## Hypotheses

Let E/Q be y²+y=x³+x²−2x, with coefficient vector [0,1,1,-2,0].
Use L030's conductor N=389 and associated normalized weight-two newform
f=sum a_n q^n, L031's independently certified a_389=1 and consequent
Fricke eigenvalue −1, and audited L099's rank E(Q)>=2. Only the
arithmetic, sign and elementary parameter-enclosure portions of L031
are used; its twist value, optimality and period normalization are not.
Use modular analytic continuation and the analytic-rank-zero/one theorem
in foundations/02. No published complex order, L035, p-adic order,
published rational basis, Sha assertion or derivative approximation is
an input.

Set c=2*pi/sqrt(389), M=Y=128, and

\[
G_2(x)=\int_1^\infty e^{-xy}\frac{\log y}{y}\,dy,
\qquad J_n(t)=\int_1^{128}e^{-tny}\frac{\log y}{y}\,dy.
\]

The exact L-series here includes every Euler factor. There is no period
division or Manin normalization. All error bounds below concern the
unnormalized L''(E,1), not L''/2! or a completed L-function derivative.

## Conclusion

Put S(t)=4*sum_(n=1)^128 (a_n/n) J_n(t). The following analytic
truncation bound holds at the actual parameter:

\[
\boxed{|L''(E,1)-S(c)|<2^{-43}<2^{-30}.}                 \tag{1}
\]

Both omitted remainders are included: every n>128 and the y>128
portion of each retained kernel. Thus S(c)+[-2^-43,2^-43] encloses
L''(E,1); even this added interval's width 2^-42 is below 2^-30.

There is also a finite-arithmetic contract. Suppose rational endpoints
enclose c in [c_l,c_u] contained in C=[3/10,1/2]. Set
c_*=(c_l+c_u)/2 and delta=(c_u−c_l)/2. Suppose all a_n, 1<=n<=128,
are certified exactly, and valid finite integration enclosures
[l_n,u_n] contain J_n(c_*). Put j_n=(l_n+u_n)/2,
e_n=(u_n−l_n)/2. If a rational s has a certified arithmetic error
eta>=0 relative to 4*sum (a_n/n)j_n, then

\[
\boxed{|L''(E,1)-s|\le
 B:=2^{-43}+200\delta+
       4\sum_{n=1}^{128}\frac{|a_n|}{n}e_n+\eta.}       \tag{2}
\]

For example, the actual checked bounds delta<=2^-50,
e_n<=2^-50 for every n, and eta<=2^-43 imply B<2^-40.
These are sufficient output-width conditions, not working-precision or
integration-tolerance guarantees. No such finite outputs are produced
here. Nonvanishing would require s−B>0 or s+B<0 in a later certificate.

This is REPRODUCTION: a fixed specialization of known formula and
error methods, not a new analytic-order result beyond the sources.
The separate critical audit below passes. No derivative is evaluated,
backend supplied or nonvanishing asserted.

## Proof

**Imported results and exact applicability.** Import Cremona,
*Algorithms for Modular Elliptic Curves*, corrected second edition
(1997), Section 2.13, printed pp.42–44, Proposition 2.13.1 on p.43
and its preceding Mellin proof
([primary chapter](https://johncremona.github.io/book/fulltext/chapter2.pdf#page=36)).
For a normalized weight-two newform of conductor N with Fricke
eigenvalue epsilon=(-1)^(r−1) and analytic order at least r, it gives
L^(r)(f,1)=2*r!*sum_(n>=1) (a_n/n)G_r(2*pi*n/sqrt(N)), where
G_r(x)=1/(r−1)! times the integral of exp(−xy)(log y)^(r−1)/y
from 1 to infinity. The lower-vanishing hypothesis is essential in
passing from the completed function to L itself. This identity is
imported, not reproved.

Import the modularity and Gross–Zagier–Kolyvagin analytic-rank-zero/one
theorem recorded in foundations/02: for E/Q, analytic order zero or one
equals rational rank. Its scope is documented by Wiles's official Clay
description, printed pp.1, 2 and 4
([primary description](https://www.claymath.org/wp-content/uploads/2022/05/birchswin.pdf)).
Analytic continuation makes L holomorphic at one. It is not identically
zero: a_1=1, and absolute Dirichlet convergence with |a_n|<=n implies
L(s) tends to 1 as real s tends to infinity. For instance for s>=3 the
terms n>=2 are dominated by the summable n^-2 and tend individually
to zero. Thus its order m at one is a finite nonnegative integer.
If m were zero or one, the quoted theorem would contradict L099's
rank>=2. Hence m>=2, so L(1)=L'(1)=0. No rank-two converse or
complex/p-adic comparison is assumed.

By L030, f has the exact level 389. L031 certifies a_389=1 independently
by counting the singular reduction on the minimal model. Wuthrich,
*Numerical modular symbols for elliptic curves*, arXiv:1608.06423v2
(24 March 2017 PDF), Section 4.1, printed p.8 (PDF page 9)
([primary version](https://arxiv.org/pdf/1608.06423v2#page=9)), gives
epsilon_N=−a_N at this single semistable prime. Thus epsilon_N=−1,
which is exactly (-1)^(2−1). Cremona's hypotheses hold for r=2, and

\[
L''(E,1)=4\sum_{n\ge1}\frac{a_n}{n}G_2(cn).             \tag{3}
\]

For all n>=1 use the elliptic coefficient bound |a_n|<=n in
Wuthrich v2, Lemma 4 and its proof, pp.6–7
([primary passage](https://arxiv.org/pdf/1608.06423v2#page=7)).
For y>0 use log y<=y−1, NIST DLMF 4.5.4
([equation](https://dlmf.nist.gov/4.5.E4)).
The prior assessment and inspected proof cases are recorded in
`drafts/literature/2026-10-21-fixed-complex-derivative-error-budget.md`
and `drafts/source-notes/2026-10-21-complex-derivative-sources.md`.
The identified specialization below is the two weighted improper
remainders, with their factor four, and the finite-error contract;
neither the Mellin identity nor the general integrator is reproved.

**Positive outward parameter enclosure.** The elementary Machin and
alternating-arctangent enclosures already justified in L031 give

\[
16\left(\frac15-\frac1{375}\right)-\frac4{239}
 <\pi<\frac{16}{5}.
\]

The left endpoint is greater than 3: its difference from 3 is
59/375−4/239>0, since 59*239=14101>1500. Also
19²=361<389<400=20². Consequently
3/10<c<32/95<1/2, proving c belongs to the rational outward C.
This broad C is used only for uniform bounds; later finite evaluation
requires its own narrower enclosure. Refining L031's alternating
arctangent sums and exact squared rational bounds for sqrt(389)
can provide it. No current narrow endpoints are asserted.

**Both full analytic remainders.** Write c_0=3/10, q=exp(−c_0) and
t=exp(−128*c_0). The elementary exponential series gives
exp(c_0)>1+c_0=13/10, hence q<10/13 and
1/(1−q)<13/3. Also

\[
e^3>1+3+\frac92+\frac{27}{6}+\frac{81}{24}
     =\frac{131}{8}>16.
\]

Since 128*c_0=192/5>36 and 129*c_0=387/10>36,
both t and exp(−129*c_0) are less than
exp(−36)<16^-12=2^-48. For y>=1, 0<=log(y)/y<=1;
therefore, for x>0,

\[
0\le G_2(x)\le\int_1^\infty e^{-xy}dy=\frac{e^{-x}}x.
\]

The omitted full Fourier series has absolute error at most

\[
\begin{aligned}
R_F&=4\sum_{n=129}^\infty\frac{|a_n|}{n}G_2(cn)\\
&\le\frac4{129c_0}
       \frac{e^{-129c_0}}{1-e^{-c_0}}
 <\frac{520}{1161}\,2^{-48}<2^{-48}.                    \tag{4}
\end{aligned}
\]

This also proves the absolute convergence needed to split (3).
The sum of the kernel tails of all retained terms has absolute error
at most

\[
\begin{aligned}
R_Y&=4\sum_{n=1}^{128}\frac{|a_n|}{n}
          \int_{128}^\infty e^{-cny}\frac{\log y}{y}dy\\
&\le\frac4{c_0}\sum_{n=1}^{128}\frac{t^n}{n}
 \le\frac{40}{3}\frac{t}{1-t}
 <\frac{80}{3}\,2^{-48},                               \tag{5}
\end{aligned}
\]

where 1/(1−t)<2 follows from t<2^-48<1/2. These estimates hold
uniformly for every c in C, not just a rounded central parameter.
They cover disjoint omitted pieces: n>128 with full kernels, and
y>128 only for 1<=n<=128. Signed coefficients remain untouched in
S. Combining (4)–(5),

\[
|L''(E,1)-S(c)|\le R_F+R_Y
 <\left(1+\frac{80}{3}\right)2^{-48}
 =\frac{83}{3}2^{-48}<32*2^{-48}=2^{-43}.
\]

This establishes (1) without evaluating any retained term.

**Finite parameter propagation.** For real t in C the finite kernel
is continuously differentiable, and differentiation of its smooth
integrand on the compact interval [1,128] gives
J'_n(t)=−n*integral_1^128 exp(−tny)log(y)dy. Thus

\[
\begin{aligned}
|S'(t)|
&\le4\sum_{n=1}^{128}|a_n|
                    \int_1^{128}e^{-tny}\log y\,dy\\
&\le4\sum_{n=1}^{128}n\int_1^\infty y e^{-c_0ny}dy\\
&=4\sum_{n=1}^{128}e^{-c_0n}
             \left(\frac1{c_0}+\frac1{c_0^2 n}\right)\\
&\le4\left(\frac{10}{3}+\frac{100}{9}\right)
                 \frac{q}{1-q}
 <\frac{5200}{27}<200.
\end{aligned}
\]

Here log y<=y was used only to enlarge a positive bound, the displayed
integral is elementary, and q/(1−q)<10/3. No derivative is interchanged
with an infinite series or an improper integral. The real mean value
theorem yields |S(c)−S(c_*)|<=200*delta.

**Finite integration, signs and actual error.** A prospective exact
coefficient certificate must identify every a_n through 128 with f.
L030's good reduction at all primes <=127 allows exhaustive point
counts a_p=p+1−#E(F_p), including p=2. The usual Euler factors then
give a_1=1, coprime multiplicativity and
a_(p^k)=a_p*a_(p^(k−1))−p*a_(p^(k−2)). These are the unchanged
L031 coefficient rules, not new computed data. Every required prime,
factorization, count and recurrence must be checked. There is no
bad-prime Fourier coefficient among n<=128; a_389 is used for the
sign only. Coefficients may instead be imported from an independently
replayed exact certificate explicitly verifying the same identifications.

For a fixed rational c_*, the complex callback
F_n(z)=exp(−c_* n z)Log(z)/z is holomorphic on Re(z)>0 using the
principal logarithm. Its restriction to [1,128] is real and bounded.
Import Johansson, *Numerical integration in arbitrary-precision ball
arithmetic*, arXiv:1802.07942v1, Section 2, pp.2–4
([primary paper](https://arxiv.org/pdf/1802.07942v1#page=2)), and
the FLINT official `acb_calc` finite-integration, callback and accuracy
contracts
([official documentation source](https://raw.githubusercontent.com/flintlib/flint/main/doc/source/acb_calc.rst)).
This mutable source was inspected in the prior assessment on 2026-10-21;
it is not an installed or pinned backend specification.

An implementation using this contract must rigorously enclose the
function on each supplied complex set. Any requested holomorphy
certification must apply to that entire set; restricting acceptance to
sets contained in Re(z)>0 suffices. It must return a nonfinite enclosure
when it cannot certify the request, rather than silently cross zero or
the logarithm branch cut. Only valid finite integration enclosures on
the full finite path are accepted; their real projections contain the
real J_n(c_*). A requested precision or integration tolerance alone
proves neither containment nor the required actual widths. Nonfinite,
uncertified or overly wide outputs do not meet this contract. Improper
tails are supplied by (4)–(5), not by the finite integrator. Another
method would require its own rigorous containment justification.

From the accepted intervals, |J_n(c_*)−j_n|<=e_n. Retaining each
signed rational weight 4a_n/n gives
|S(c_*)−4*sum(a_n/n)j_n|<=4*sum(|a_n|/n)e_n.
The midpoint sum can be performed exactly in rational arithmetic,
giving eta=0. Otherwise eta must bound all final arithmetic and
rounding, or all operations must use outward interval endpoints
(min/max of all endpoint products for signed multiplication).
Triangle inequality with (1) and the parameter bound proves (2).

For the stated sufficient widths, |a_n|/n<=1 gives
4*sum(|a_n|/n)e_n<=512*2^-50=2^-41 and
200*delta<=200*2^-50<2^-42. Hence
B<2^-43+2^-42+2^-41+2^-43=2^-40, as claimed.
Each condition concerns actual verified output; no output or runtime
guarantee follows from this argument. If exact c interval propagation
is used instead, it must contain the full parameter family and its
width contribution replaces, rather than duplicates, 200*delta.

The analytic threshold passes at the original fixed cutoffs. Available
certified software, complete finite evaluation, a zero-excluding signed
interval and its separate audit remain unresolved. Even success there
would reproduce a known fixed analytic-order conclusion with different
evidence. Arbitrary-curve rank comparison, full Sha finiteness and the
refined BSD formula remain open.

**Separate critical audit, 2026-10-21 (step 396).** The prior SPECIALIZE
assessment `drafts/literature/2026-10-21-fixed-derivative-error-budget-audit.md`
covers precisely this proof audit. The full proof passes without a
mathematical repair. The Section 4.1 pagination above is corrected;
the original proof and all its bounds are retained. No finite derivative
or upstream arithmetic replay was executed in this audit.

For applicability, L030's discriminant 389 and unit c_4=112 at that
prime establish the minimal model and single multiplicative conductor
prime. Its modularity input identifies the full elliptic L-series.
L031's separately certified count gives a_389=1; the assessed Wuthrich
single-prime convention then gives Fricke eigenvalue -1, not root
number -1. Audited L099 supplies only the independent rational lower
bound. The analytic-zero/one theorem is applied by contradiction to
each of the two possible orders 0 and 1. The Dirichlet limit argument
above is valid by domination by n^-2 for s>=3, and ensures that the
holomorphic function is not identically zero. Thus its finite order
is at least two, without assuming that it is exactly two.

Cremona's Proposition 2.13.1 and preceding proof were checked at
printed pp.42–43 (PDF pages 36–37). With the source's completion
Lambda(s)=N^(s/2)(2*pi)^(-s)Gamma(s)L(s), lower vanishing removes
both lower-order product-rule terms at s=1. The source formula is
therefore for L'' itself. Its 2*r! factor at r=2 is four and its
1/(r-1)! kernel factor is one. This is an applicability check of the
imported formula, not a reproof or an assumption of nonzero L''.

The elementary outward enclosure checks exactly: the lower pi
endpoint exceeds 3 by 12601/89625; sqrt(389) lies between 19 and
20; and 32/95<1/2 because 64<95. Hence the actual c and every
segment between it and an admissible c_* lie in C. For the tail
exponents, 128*c_0=38.4>36 and 129*c_0=38.7>36 are exact
rational comparisons. The positive exponential partial sum is
131/8>16, so exponentiation gives exp(-36)<2^-48. The geometric
factor estimates use q<10/13 and t<2^-48<1/2, without treating
(10/13)^129 as a substitute for the stronger exponential bound.
Equation (4)'s prefactor is exactly
4*(10/387)*(13/3)=520/1161<1. Equation (5) includes every one
of the 128 kernel tails before enlarging their positive sum to the
infinite geometric sum; its prefactor is 80/3. Thus the combined
bound is <(83/3)*2^-48<2^-43, since 83<96. These disjoint
pieces exhaust the omitted domain. Absolute convergence justifies
the series split; positivity is used on majorants, never to change
the signed finite sum. The resulting radius is <2^-43 and the
chosen enclosing interval has width 2^-42<2^-30.

For parameter propagation, differentiation takes place only in the
128 smooth integrals on a fixed compact rectangle. The factor n
from J'_n cancels the denominator n in S. Integrating the positive
majorant y*exp(-c_0*n*y) gives exactly the displayed two terms.
After |a_n|<=n and 1/n<=1, their geometric sum is bounded by
4*(130/9)*(10/3)=5200/27<200, with positive margin 200/27.
The real mean value theorem therefore supplies 200*delta, including
both signs of c-c_*; no improper differentiation is needed.

For the conditional finite contract, all primes involved in n<=128
are good on L030's actual model. The stated point-count and Euler
rules identify every coefficient, including p=2 and prime powers;
the separate a_389 serves only the sign. None of these finite
outputs is assumed already produced for this derivative certificate.
The finite integration path includes y=1, where Log(1)/1=0 and
there is no singularity. The principal Log is holomorphic throughout
Re(z)>0, as are exp(-c_* n z) and 1/z there. The reopened FLINT
contract, callback and integration/accuracy sections, requires whole
input-set containment even for order-zero interval evaluations and
holomorphy certification for order one. Its default finite integration
uses those two orders only. Restricting accepted holomorphic sets to
Re(z)>0 is sufficient; a nonfinite rejection on other sets is safe
but makes no promise of eventual convergence. The saved Johansson
coverage is reused. No installed version or working callback is
certified by the mutable documentation.

For accepted rational intervals, their midpoints have errors equal
to at most their half-widths. Multiplication by 4*a_n/n preserves
the sign in the center and contributes 4*|a_n|*e_n/n to the
radius, also for negative and zero a_n and zero-crossing intervals.
Taking real projections is valid because J_n(c_*) is real. Adding
the two analytic tails, parameter error, kernel errors and eta gives
(2). A finite return or a success flag alone cannot certify the
required widths. At the proposed sufficient bounds, expressing all
four errors in units of 2^-50 gives
B<=(128+200+512+128)*2^-50=968*2^-50<1024*2^-50=2^-40.
Thus the proposed total interval has width <2^-39; radius and width
are not interchanged. Exact midpoint summation permits eta=0, but
finite containment still has to be established for every kernel.

The audit validates the fixed analytic input and conditional contract
only. It creates no new mathematical dependency: the existing DAG
row retains L030, L031 (only the stated portions), and L099. L035,
L100 and published basis/Sha premises were not used. Narrow c
endpoints, all certified kernel intervals, a backend and complete
finite replay are still absent; zero exclusion and complex order two
are not conclusions of this lemma. Uniform BSD remains unresolved.

## Mathlib

Full matching theorem for this fixed derivative error budget: not
checked. Supporting exponential/logarithm, finite-integral and interval
arithmetic coverage: not checked. No absence claim is made. The named
sources above supply the mathematical inputs; this is an informal proof
specialization, not a Mathlib verification or numerical certificate.
