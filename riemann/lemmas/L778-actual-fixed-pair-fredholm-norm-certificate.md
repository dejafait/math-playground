# Lemma 778: actual fixed-pair Fredholm norm certificate

## Hypotheses

Use the actual G and original complex Hilbert norm of L776/L777, with
(r,R)=(2,1024). No zero list, RH, simplicity or coefficient-minor sign is
assumed. Arithmetic relies on Python Decimal's documented directed
arithmetic and correctly rounded nearest exp/sqrt. This computer-assisted
informal calculation passed the separate conceptual audit in step433
below; it is not formal verification or an RH candidate.

## Conclusion

The certificate below gives nonvanishing on |w|=1024 and |w|=1280,
with exactly one zero inside each circle, counted with multiplicity.
That zero is real and simple, and

\[
 -799.161819329547437854196<w_*<-799.161819329547437853328.
\]

For alpha=w_*/1024, F(z)=G(1024z)/(z-alpha) is entire and zero-free
on a neighborhood of |z|<=5/4. L777's complete error certificate gives

\[
 0.84228998371291<\|A_{2,1024}\|<0.84228998371298<1.             \tag{1}
\]

Thus L776 implies D_(2,1)=a_1^2-a_0 a_2>0. The contribution is a
finite-pair original-norm benchmark, not a claim of a new sign theorem
beyond the checked sources. No growing-order estimate, all-degree
positivity or RH conclusion follows. The analytic implementation and
complete numerical evidence were reviewed and replayed in step433,
subject to the stated trusted software contracts.

## Proof

### Established methods and arithmetic

Specialize the standard argument principle, Cauchy formula/estimates,
and L776/L777. Rigorous box integration and argument-principle counting
are established methods: F. Johansson, *Numerical integration in
arbitrary-precision ball arithmetic*,
[arXiv:1802.07942v1](https://arxiv.org/pdf/1802.07942v1), Section2/2.1,
pp.2–4, and Section4, pp.7–8. We implement elementary analytic Taylor
integration rather than reproduce the source's Gaussian algorithm.
Specialization is necessary because the sources give none of this
operator's actual enclosure data. The prior source gate is
`drafts/literature/2026-11-04-actual-fredholm-fixed-pair-norm-test.md`.

The runtime is Python3.15.2, Decimal1.70, libmpdec4.0.1. FLINT is absent;
temporary installation failed because pypi.org could not be resolved.
No numerical claim came from that failure. Finite decimal endpoint
intervals use 75 significant digits and ROUND_FLOOR/ROUND_CEILING.
Exact sign reversal uses copy_negate. Nearest correctly rounded exp/sqrt
are widened by one adjacent decimal on each side, clamping the lower
sqrt bound to zero. The imported contracts are Python **3.15.2**,
[decimal documentation](https://docs.python.org/3.15/library/decimal.html),
Decimal construction, Context arithmetic, exp/sqrt, next_minus/next_plus
and rounding modes; and mpdecimal **4.0.1**,
[Context, Correct Rounding](https://www.bytereef.org/mpdecimal/doc/libmpdec/context.html)
and [Arithmetic Functions, exp/sqrt](https://www.bytereef.org/mpdecimal/doc/libmpdec/arithmetic.html).
The exponential contract requires allcr=1. The assessed
[CPython v3.15.2 source](https://raw.githubusercontent.com/python/cpython/v3.15.2/Modules/_decimal/_decimal.c),
dflt_ctx/context_new/context_init_impl and exp/sqrt dispatch, initializes
that field to 1 and preserves it for these constructors. Exact sign and
absolute-value copies avoid context rounding. Exact integer factorials
and rational checks are used as stated; no ordinary floating-point special
function, FFT or SVD is an input. These software contracts are trusted,
not proved here; the installed binary is not independently attested.

Pi uses the standard Machin formula 16 atan(1/5)-4 atan(1/239).
Each arctangent uses 180 alternating terms, with error <=t^361/361.
All input uncertainty remains in the intervals.

### Entire polynomial evaluator and complete tails

In L017 put x=exp(2u), s=1/2+sqrt(w)/2. L018 then gives

\[
 A(u)=e^{u/2}\sum_{m\ge1}e^{-\pi m^2e^{2u}},\quad
 J(w)=\int_0^\infty A(u)\cosh(\sqrt w\,u/2)\,du,\quad
 G(w)=\frac{1+(w-1)J(w)}{16}.                                \tag{2}
\]

The cosh is its entire power series. Compact absolute domination by
the double-exponential bound of L017 justifies the exchange with the
integral. There is no square-root branch in the evaluator. In particular
I(s)=4J(w) and xi/8 gives exactly the normalization (2).

Retain m=1,...,8 and u in [0,2], and define

\[
 j_n=\int_0^2 e^{u/2}\sum_{m=1}^8 e^{-\pi m^2e^{2u}}
                      \frac{u^{2n}}{4^n(2n)!}\,du\quad(0\le n<96).
\]

These produce a degree96 polynomial P_0 with coefficients
(1-j_0)/16, (j_(n-1)-j_n)/16 for 1<=n<=95, and j_95/16.
P_0 refers to the exact finite integrals; interval coefficients enclose
it and are not arbitrary choices of endpoints.

There are 128 cells with c=(2l+1)/128, h=1/128, 0<=l<128. Integrate
Taylor polynomials through degree24 at c, using analytic radius d=1/8.
An even term of degree j contributes 2h^(j+1)/(j+1) times its coefficient.
Factorial-normalized jets of exp(q) satisfy
f_0=exp(q_0), f_j=j^(-1) sum_(l=1)^j l q_l f_(j-l), where
q(u)=u/2-pi m^2 exp(2u). The monomial jets are updated by multiplication
by u^2/[4(2n+2)(2n+1)]. These finite differentiation identities are
evaluated with directed intervals.

For |z-c|<=d, Re(exp(2z))>=v:=exp(2(c-d))(1-2d^2)>0, since
cos(2 Im z)>=1-2d^2. Using pi>3 and m^2>=1+3(m-1), both the full
and finite-theta functions satisfy

\[
 |A(z)|\le M_A(c):=\frac{e^{(c+d)/2}e^{-3v}}{1-e^{-9v}}.
\]

Cauchy estimates give an error in the nth cell moment integral at most

\[
 2h M_A(c)\frac{(c+d)^{2n}}{4^n(2n)!}
                 \frac{(h/d)^{25}}{1-h/d}.                    \tag{3}
\]

All 128 retained A Taylor jets and all 128*96 errors (3) are saved;
the monomial jets are reproduced by the displayed recurrence. These errors are already
inside the polynomial coefficient intervals and are retained at every
evaluation.

On |w|<=1600, three additional J errors are bounded by

\[
 E_\theta=\frac{2e\,e^{-243}e^{40}}{1-e^{-57}},\quad
 E_u=\frac{2e^{-121}}{303.5},\quad
 E_c=\frac{2e\,e^{-3}}{1-e^{-9}}\frac{40^{192}}{192!}
        \left(1-\frac{1600}{193\cdot194}\right)^{-1}.           \tag{4}
\]

For E_theta use m>=9, m^2>=81+19(m-9), exp(2u)>=1, exp(u/2)<=e
and |cosh|<=exp(40) on [0,2]. For u>=2, the full theta sum is at most
2 exp(-3 exp(2u)); e^4>54 implies exp(2u)>=54(1+2(u-2)). Multiply
by exp((20+1/2)u) and integrate to obtain E_u. For E_c the first omitted
cosh term is 40^192/192!, later ratios are <=1600/(193*194), and
the retained A integral is <=2e exp(-3)/(1-exp(-9)). Hence

\[
 |G-P_0|\le E_G:=\frac{1601}{16}(E_\theta+E_u+E_c)
                 <3.141\cdot10^{-48}\quad (|w|\le1600).       \tag{5}
\]

Bound (5) is additional to, not a replacement for, coefficient widths
from (3). There are no omitted theta or integration tails.

### Complete counts, real zero and residue

For S=1024,1280 parametrize four quarters by
w(t)=S i^q(1+it)/(1-it), 0<=t<=1, q=0,1,2,3. Each quarter has
128 equal parameter intervals. No adaptive subdivision was needed.
For a parameter box evaluate the polynomial by its degree8 Taylor
jet at the midpoint w_0. The disk |w-w_0|<=256 lies within |w|<=1536.
Thus M_P=sum_n sup|[w^n]P_0|1600^n bounds the polynomial there; if
Delta encloses |w-w_0| on the parameter box, the remaining Taylor
terms are <=M_P(Delta/256)^9/(1-Delta/256). Every Delta<256. Add (5).

All 512 image rectangles for each circle exclude zero. Their component
lower bounds give

\[
 \min_{|w|=1024}|G(w)|>0.0000948,\qquad
 \min_{|w|=1280}|G(w)|>0.0000314.                              \tag{6}
\]

Choose the exact decimal midpoints of the endpoint G enclosures as
polygon vertices, and hull them into their segment rectangles. Both
the true curve segment and its polygon edge lie in one convex zero-free
rectangle. Straight interpolation gives a closed nonvanishing homotopy.
Compute the polygon's winding by exact rational signed crossings of the
positive real axis, using y<=0<y' for upward crossings and the reverse
for downward crossings. Shared vertices agree exactly; no crossing
hits zero. Both winding numbers are 1. The argument principle counts
one zero with multiplicity in each disk. G is entire, so no pole
correction is present.

Real interval evaluations at -800 and -799 have strict opposite signs.
Bisection preserving those signs gives the stated root bracket. The
intermediate value theorem supplies a real zero. The inner count makes
it the unique zero and simple; the outer count and (6) show that its
removal makes F zero-free on a neighborhood of |z|<=5/4.

Evaluate P_0' on the whole root interval. Cauchy on a radius100 disk
around the true root adds E_G/100 to its derivative error, since that
disk is inside |w|<1600. L777's simple residue is obtained by the
removable value F(alpha)=1024 G'(w_*), hence d_1=w_*G'(w_*).
The full enclosure gives
-0.001221522142143843<d_1<-0.001221522142143842.
There is no division of a zero ball by another zero ball.

### Laurent coefficients and original-norm certificate

Choose sigma=5/4, a=4/5, rho=9/10; the root enclosure gives |alpha|<a.
On the whole outer circle,

\[
 |F(z)|\ge m_\sigma:=
 \frac{\text{saved outer G lower bound}}{\sigma+a}>0.0000153.
\]

This is a contour enclosure, not a sampled minimum. L777 gives
M_b=(1+a/sigma)/m_sigma for b=(1-alpha/z)/F. Its Laurent series has
only one possible negative power z^(-1), and its positive coefficients
satisfy |beta_n|<=M_b sigma^(-n).

Enclose b(z)=(z-alpha)^2/[z G(1024z)] at L=1024 roots of unity.
Every sampled denominator excludes zero. Trig values use enclosed pi,
Taylor sine/cosine through degrees129/128 on [0,pi/2], errors each
<=2^130/130!, and exact quadrant rotations. Retain all node, root,
evaluation and arithmetic uncertainty. For 1<=n<=N=192, the discrete
Fourier average equals beta_n+sum_(j>=1) beta_(n+jL): averaging the
absolutely convergent Laurent series annihilates other modes and
n<L-1 excludes the sole negative-power alias. Therefore the additional
alias error is at most

\[
 M_b\frac{\sigma^{-(n+L)}}{1-\sigma^{-L}}.                    \tag{7}
\]

Real symmetry makes beta_n real; all imaginary enclosures contain zero.
Take exact decimal midpoint hats and errors enclosing the complete
real intervals including (7). Do the same for alpha and d_1. L777(6)–(8)
then include all quadrature, root, derivative, extraction, rounding and
alias errors. Its T_N(sigma^(-2)) includes all modes beyond N=192,
with the supplied positive m_sigma. No infinite tail is replaced by a
finite Taylor polynomial.

For k=1 the compression is scalar, with both Gram factors retained:

\[
 \widehat U_i=\sum_{h=1}^{N-i+1}\widehat\beta_{i+h-1}
                    \widehat\alpha^{h-1}\ (3\le i\le N),\quad
 G_U=\sum_{i=3}^N|\widehat U_i|^2,\quad
 G_Y=\frac{\widehat\alpha^4}{1-\widehat\alpha^2},\quad
 \|\widehat K\|=|\widehat d_1|\sqrt{G_U G_Y}.
\]

The saved finite norm is in (0.84228998371294085226027736327482,
0.84228998371294085226027736327484). The full L777 product error is

\[
 E=\delta_bh_B+h_b\delta_B+\delta_b\delta_B
   <2.861\cdot10^{-14},
\]

dominated by delta_b h_B. The norm triangle and reverse triangle
inequalities give the complete interval

\[
 [0.842289983712912250413294695808658473846271790481566549699239546179433336335,
  0.842289983712969454107260030740997964832615889870340887145351394354599413654].
\]

This proves (1), subject to the stated arithmetic contracts and the
documented computation, and L776 supplies the one minor sign.

### Reproduction and verification limits

Implementation: `scripts/actual-fredholm/fixed_pair_431.py`.
Full evidence: `scripts/actual-fredholm/fixed-pair-certificate-431.json`.
Run `python3 scripts/actual-fredholm/fixed_pair_431.py --phase <phase>`
for phases coeff, count, norm in order. To replay a coefficient build,
use a copy of the implementation at a fresh output directory; existing
coefficients are deliberately not overwritten. No radius/precision
sweep was performed. All certificate paths are notebook-relative.

`python3 scripts/actual-fredholm/check_saved_431.py` processes every
saved contour segment and endpoint, complete parameter coverage,
nonzero rectangles and exact winding. It checks all 192 coefficient
error records and 1024 sample denominator exclusions. Exact integer/
rational arithmetic checks every hatted U row, both Gram matrices,
the scalar norm and the complete L777 error transfer. The result is
`scripts/actual-fredholm/saved-data-check-431.json`, PASS, no failures.
That finite checker alone does not audit the theta jets, analytic tail
bounds, contour homotopy or Fourier alias argument. The separate step433
review below pays those obligations and replays the full calculation;
it does not supply an independently written transcendental backend or
formal verification. The original files and their PENDING_AUDIT labels
are preserved as historical evidence.

This supports one fixed-pair sufficient norm condition only. Other
orders, admissible radii, tied moduli, uniform factor/reciprocal bounds,
other indices and positivity assembly remain open. Existing shifted-
boundary and scalar-modulus stops remain in force for their approaches.
No Platt–Trudgian zero list or cross-notebook theorem is used.

### Independent conceptual audit, 2026-11-04 (step433)

The pre-existing SPECIALIZE coverage in
`drafts/literature/2026-11-04-actual-fixed-pair-certificate-audit.md`
was reused. The following review checks this same fixed-pair statement;
it does not strengthen it or claim new mathematics beyond the assessed
methods. No mathematical defect was found.

**Normalization, analytic integrals and tails.** Directly substituting
x=exp(2u) into L017 gives I(s)=4J(w). Since s(s-1)=(w-1)/4,
L018's xi/8 gives (2), including the constant term. Compact double-
exponential domination permits the entire cosh series and all retained
moment integrals. For the finite theta sum each cell integrand is
entire. On its closed disk of radius 1/8, Re exp(2z) is at least v>0;
the geometric m bound follows from m^2>=1+3(m-1). Multiplying M_A
by (c+d)^(2n)/(4^n(2n)!) bounds the full moment integrand on that
disk. Summing the Cauchy coefficient remainder for degrees j>=25
and integrating over length 2h gives (3); not exploiting the vanishing
of odd integrals only enlarges the bound. The exp-jet recurrence and
the u^2 monomial update reproduce the factorial-normalized derivatives.

For the omitted theta indices, m^2>=81+19(m-9) gives the e^-243
and ratio e^-57 in (4). For u=2+v with v>=0,
e^(2u)>=54(1+2v); the u-tail integrand is at most
2 exp(-121) exp(-303.5v), including exp(u/2) and the cosh bound.
For n>=96 the cosh-series ratios are bounded by 1600/(193*194)<1.
These three errors concern distinct omitted terms, while the cell
errors already enclose the exact polynomial coefficients. The use of
|w-1|<=1601 in (5) is valid on the full disk of radius 1600. No derivative
error is inferred by differentiating a pointwise real estimate: the
complex uniform analytic remainder is used with Cauchy's formula.

**Interval arithmetic and contour coverage.** Every numerical input is
an integer, finite decimal string or existing Decimal endpoint, converted
without rounding. Derived rational inputs receive directed intervals. Directed addition and the four
endpoint products enclose their real operations; reciprocal order is
correct on both positive and negative nonzero intervals. Squaring handles
intervals crossing zero. Nearest exp/sqrt widened by adjacent values
enclose their exact values under the imported contracts. The Machin
series remainder starts at t^361/361 after 180 terms. Midpoints are
arbitrary exact decimal choices whose subsequent errors are bounded
upward, so they need not equal exact rational interval midpoints.

In each contour segment, the image w_0 of the true parameter midpoint has modulus S,
even though its numerical enclosure is a rectangle. Its radius 256
Cauchy disk lies in |w|<=1536. Interval Horner jets contain the exact
Taylor coefficients of P_0 at that true midpoint; interval subtraction
encloses w-w_0. Thus the saved Delta and geometric remainder bound the
whole arc, with no assumption of independence among interval occurrences.
All 1024 segment records were replayed, with no subdivision, and all
parameter intervals, nonzero rectangles, shared vertices and crossings
were checked exactly. The polygon and true curve are joined pointwise
inside the same convex zero-free rectangle, giving a closed homotopy.
The half-open crossing convention handles vertices on the positive real
axis; a horizontal edge there contributes no crossing. The rectangles
exclude an edge through the origin. Both windings are 1, so the argument
principle gives counts with multiplicity, not counts of sampled roots.

The final strict real bracket, its endpoint signs and the derivative
enclosure were reproduced. One real root in the inner disk, together
with the total multiplicity count 1, establishes simplicity. The equal
outer count and boundary nonvanishing leave no other zero in the larger
disk. Removing the simple root therefore makes F zero-free on a
neighborhood of its closed disk of radius 5/4. The entire root bracket plus
radius 100 stays inside |w|<1600, validating E_G/100 for G'-P_0'.
The residue is d_1=alpha F(alpha)=w_*G'(w_*), with no lost radius factor.

**Fourier extraction and complete norm transfer.** On |z|=sigma,
|z-alpha|<=sigma+a gives the stated lower bound for F from the complete
outer contour, not from sampled values. Since F has no zero in that
disk, b=(1-alpha/z)/F has at most the single negative mode z^-1.
Its positive Laurent coefficients have the stated geometric Cauchy bound.
The series is absolutely convergent on |z|=1, so finite Fourier averaging
may be interchanged with it. The possible congruent indices are n+jL;
for 1<=n<=192 and L=1024, all j<0 give indices below -1. Thus (7) pays
every alias, including exclusion of the negative mode. The sine/cosine
Taylor remainder bound is valid because each true quadrant angle is in
[0,pi/2] and its enclosure is inside [0,2). Interval powers of the
conjugate node contain the exact Fourier factors even though the
enclosing rectangle itself is not confined to the unit circle.

All 1024 samples and all 192 coefficient records were reproduced, retaining
root and function uncertainty. Exact rational checks separately confirmed
every alias bound. With real alpha and d_1, L777's finite compression
reduces to the scalar absolute value |d_hat|sqrt(G_U G_Y). Every U row
and both Gram factors were verified by exact integer/rational arithmetic;
the infinite Y tail starts at i=3 and is alpha_hat^4/(1-alpha_hat^2).
The positive-coefficient tail begins at n=193 and is exactly T_192(q).
The full-product difference, including delta_b delta_B, is bounded by
2.861e-14. Both triangle inequalities therefore give the displayed
complete norm interval, with upper endpoint strictly below 1. This pays
L776's already audited sign implication only at this pair.

**Full replay evidence.** Run
`python3 scripts/actual-fredholm/audit_433.py`.
The complete fresh evidence and audit report are
`scripts/actual-fredholm/audit-433/fixed-pair-certificate-431.json` and
`scripts/actual-fredholm/audit-433/audit-report.json`.
Every evaluation, contour, root and norm field exactly matched step431;
the original evidence hash remained unchanged. The unchanged finite
checker was executed at the fresh output path, and additional exact
rational checks covered all evaluator-domain bounds and alias errors.
The directed and nearest contexts reported only expected Inexact/Rounded
flags, with no overflow, underflow or invalid-operation flag. The report
records hashes, actual/required bounds, all checks and an empty failure
list. This is a complete replay of the reviewed implementation and an
independent analytic review, not a second implementation of the numerical
backend. Uniform orders, other radii, tied moduli, all-degree signs and
the RH conclusion remain unpaid.

## Mathlib

Full matching coverage is not checked; no presence or absence claim is
made for this complete numerical/Fredholm certificate. The named
complex-analysis theorems and L776/L777 are informal inputs. Decimal's
backend and the numerical evidence have not been formally verified.
