# Lemma 824: actual-theta quartic additive self-convolution factor

## Hypotheses

Use the actual positive theta kernel K of L019 and the finite positive
moments m_j=M_(2j) of L021. In L795's normalization put

\[
 \gamma(j)=\frac{j!m_j}{(2j)!},\qquad R_j=\frac{\gamma(j)}{\gamma(0)},
 \qquad P_4(x)=1-4R_1x+6R_2x^2-4R_3x^3+R_4x^4.
\]

Use L791's audited actual coefficient enclosures through j=4, with
L778's inherited uniform complex-disk error and trusted software
contracts. They are computer-assisted informal inputs, not formally
verified or independently attested transcendental computations.
Neither L791's fitted model nor L823's cubic factor is a premise.
Fix symmetric finite-free additive convolution at degree four in the
Marcus–Spielman–Srivastava convention below. Factors are real monic
quartics, with root multiplicities allowed.

## Conclusion

Define the real quantities

\[
 h=\frac{R_3}{R_4},\quad A=\frac{6R_2}{R_4},\quad
 B=-\frac{4R_1}{R_4},\quad D=\frac1{R_4},
\]
\[
 p=A-6h^2,\quad q=B+2Ah-8h^3,\quad
 r=D+Bh+Ah^2-3h^4.
\]

They are well defined and the centered monic actual quartic is

\[
 C(y)=\frac{P_4(y+h)}{R_4}=y^4+py^2+qy+r.
\]

There is exactly one real monic quartic Q with Q boxplus_4 Q=C:

\[
 Q(y)=y^4+cy^2+ey+f,\qquad
 c=p/2,\quad e=q/2,\quad f=r/2-p^2/48.
\]

Its coefficient-based Hermite matrix is positive definite, and Q has
four distinct real roots. The complete rational certificate and its
qualifications are below. This is a known-method finite specialization
and a local realization result, not a claim of new general root theory,
degree-uniform realization, shifted/mixed signs, all-degree mixed
positivity or RH. The separate step626 audit below passed under the
same inherited contracts.

## Proof

**Imported operation and criteria.** A. Marcus, D. Spielman and
N. Srivastava, *Finite free convolutions of polynomials*,
[arXiv:1504.00350v2](https://arxiv.org/pdf/1504.00350v2),
3 July 2019, Definition1.1, equations(1)–(2), printed pp.2–3, define
for monic degree-d polynomials
u(x)=sum_i(-1)^i a_i x^(d-i), v(x)=sum_i(-1)^i b_i x^(d-i),

\[
 (u\boxplus_d v)(x)=\sum_{k=0}^d(-1)^k x^{d-k}
 \sum_{i+j=k}\frac{(d-i)!(d-j)!}{d!(d-k)!}a_i b_j,
 \qquad a_0=b_0=1.
\]

Their Theorem1.3 (Walsh) preserves real rootedness when both input
polynomials are real rooted; it does not construct an inverse factor.
O. Arizmendi and D. Perales, *Cumulants for finite free convolution*,
[arXiv:1611.06598v2](https://arxiv.org/pdf/1611.06598v2),
7 March 2017, Propositions3.4/3.6, pp.7–8, provide general finite
coefficient/cumulant inversion and additivity. Here only the degree-four
coefficient equations are specialized, to establish the exact identity
and uniqueness without any root-location premise. Section6, especially
Remark6.7, does not justify automatic fractional-power preservation.

M. B. Nathanson, *The Hermite-Sylvester criterion for real-rooted
polynomials*, [arXiv:1911.01745v2](https://arxiv.org/pdf/1911.01745v2),
24 November 2019, pp.1–3, Lemmas1–2/Theorem1 and both proof cases,
states: a real degree-n polynomial has all roots real iff the real
symmetric matrix H=(s_(i+j))_(0<=i,j<n) is PSD, where s_k sums the
kth powers of its complex roots with multiplicity and s_0=n. Repeated
roots and repeated nonreal conjugate pairs are included. P. Parrilo,
MIT6.972, Lecture5, 23 February 2006 (scribe Noah Stein),
[Section6, Lemma15/Theorem16, pp.5-6–5-7](https://ocw.mit.edu/courses/6-972-algebraic-techniques-and-semidefinite-optimization-spring-2006/260460cc36cd5c2c78b0b04f9b3fe7bd_lecture_05.pdf),
gives the finite PSD criterion by all principal minors and the sufficient
positive-definiteness criterion by strictly positive leading minors.
Nonstrict leading minors alone are insufficient. These general results
are imported, not reproved. Their hypotheses apply to the real monic
quartic constructed below, without assuming its roots real. The prior
SPECIALIZE assessment is
`drafts/literature/2026-11-05-theta-quartic-free-square-root-scope.md`.

**Normalization and centering.** L019/L021 give 0<gamma(j)<infinity,
so R_4>0. Dividing P_4 by R_4 gives
x^4-4hx^3+Ax^2+Bx+D. Expanding at x=y+h cancels the cubic term;
the quadratic, linear and constant coefficients are respectively the
stated p,q,r. Centering uses the algebraic mean of the four roots,
which is h by the cubic coefficient, whether or not those roots are real.

L021's even moment expansion identifies the ordinary coefficients of
G(w)=xi(1/2+sqrt(w)/2)/8=sum_j a_j w^j as

\[
 a_j=\frac{m_j}{8\,4^j(2j)!},\qquad
 \gamma(j)=8\,4^j j!a_j.
\]

Thus the gamma intervals in L791 have exactly the required normalization.
In the evaluation gamma(0) cancels, giving
h=gamma(3)/gamma(4), A=6gamma(2)/gamma(4),
B=-4gamma(1)/gamma(4), D=gamma(0)/gamma(4).
No fitted-model coefficient or extra scale factor is used.

**Exact identity and uniqueness.** For a general real monic quartic
Q=y^4+by^3+cy^2+ey+f, the imported coefficient formula specializes to

\[
 Q\boxplus_4 Q=y^4+2by^3+(2c+3b^2/4)y^2
                  +(2e+bc)y+(2f+be/2+c^2/6).
\]

The k=2 cross weight is 3!3!/(4!2!)=3/4. The two k=3 cross
weights are 3!2!/(4!1!)=1/2 each. At k=4 the two outer cross
weights are 3!1!/4!=1/4 each and the middle one is 2!2!/4!=1/6.
The signs (-1)^k agree with the signs of the ordinary coefficient
products, so the displayed formula applies to b,c,e,f as written.
Matching the cubic coefficient forces b=0; the next two force c=p/2
and e=q/2. The constant equation then forces
f=(r-c^2/6)/2=r/2-p^2/48. Substitution proves the exact identity
for the actual coefficients, and the triangular equations prove global
uniqueness among real monic quartics. No uncertain endpoint equality
or preservation theorem is used to infer this identity.

**Complete input and arithmetic certificate.** Reproduction command:

`python3 scripts/central-jacobi/quartic_free_square_root_624.py`

Complete evidence:
`scripts/central-jacobi/quartic-free-square-root-certificate-624.json`.
The script converts all saved decimal endpoints to exact integer
fractions. It verifies the current hashes of step478's audited inputs,
L791's source hash against both saved audits, both inherited PASS/no-failure
statuses, and equality of the complete inherited evaluator record to
step433's audited replay. The complete actual_a/gamma intervals through
j=4 and the original hash record were inspected, not midpoint previews.

For every j=0,...,4 it recomputes the coefficient interval of G by adding
[-E_G/1600^j,E_G/1600^j] to the saved coefficient interval of P_0,
using the saved upper bound of E_G. It checks this lies in actual_a[j],
that multiplication of the entire actual_a interval by 8*4^j*j!
lies in gamma[j], and that all five gamma lower bounds are positive.
L778's audited uniform bound |G-P_0|<=E_G<3.141*10^(-48) on the
complex disk |w|<=1600 gives this coefficient error by Cauchy's estimate.
All cell, theta, integration, cosh-tail and rounding errors remain
included; this is not differentiation of a real pointwise approximation.
The inherited analytic and backend contracts remain premises. No new
quadrature, evaluator, root list or model parameter enters the calculation.

Addition uses endpoint sums, multiplication the extrema of the four
endpoint products, division the reciprocal of an interval first checked
to exclude zero, and squaring includes zero if its argument contains
zero. After calculating c,e,f exactly as rational enclosures, they are
enlarged once to multiples of 10^(-80), by integer floor/ceiling.
The script checks containment of every raw interval in that enlargement.
All subsequent Newton sums and determinants use exact fraction arithmetic
on these enlarged intervals. Repeated occurrences may be correlated;
independent interval enclosure only enlarges the tested set. Printed
six-decimal endpoints are separately checked to contain the exact bounds.

Outward coefficient bounds include

\[
\begin{aligned}
 -839.613651&\le p\le-839.613650,&
 -592.009014&\le q\le-592.009013,\\
 57348.794147&\le r\le57348.794148,&
 -419.806826&\le c\le-419.806825,\\
 -296.004507&\le e\le-296.004506,&
 13987.916197&\le f\le13987.916198.
\end{aligned}
\]

**Hermite signs and multiplicities.** Newton's identities, which do not
require real or distinct roots, give

\[
 s_0=4,\quad s_1=0,\quad s_2=-2c,\quad s_3=-3e,\quad
 s_4=2c^2-4f,\quad s_5=5ce,\quad
 s_6=-2c^3+6cf+3e^2.
\]

For completeness the generic recurrence used for evaluation is
s_k+sum_(j=1)^(k-1) a_j s_(k-j)+k a_k=0 for 1<=k<=4,
and s_k+sum_(j=1)^4 a_j s_(k-j)=0 for k>4, with
(a_1,a_2,a_3,a_4)=(0,c,e,f). The script separately checks all seven
closed forms as exact polynomials in Q[c,e,f]. It constructs

\[
 H=\begin{pmatrix}
 4&0&s_2&s_3\\0&s_2&s_3&s_4\\
 s_2&s_3&s_4&s_5\\s_3&s_4&s_5&s_6
 \end{pmatrix}
\]

from the generic interval recurrence and evaluates determinants by the
complete signed permutation expansion. All 15 nonempty principal minors,
including their full rational bounds and zero thresholds, are saved.
The leading minors have these outward enclosures:

| Order | Lower bound | Upper bound |
| --- | ---: | ---: |
| 1 | 4 | 4 |
| 2 | 3358.454601 | 3358.454602 |
| 3 | 400821153.244638 | 400821153.244639 |
| 4 | 3189834503857790.281381 | 3189834503857790.281382 |

Each lower bound is strictly above the required threshold zero. The full
rational endpoints of all four leading minors were inspected. Thus H is
positive definite by the imported strict leading-minor criterion, hence
PSD; Nathanson's theorem gives all four roots real with multiplicity.
They are distinct: if there were fewer than four distinct roots z,
then H=sum_z multiplicity(z) v(z)v(z)^t, v(z)=(1,z,z^2,z^3)^t,
would have rank less than four, contradicting its positive determinant.
The forward Walsh theorem may now be applied to Q,Q, but it adds no
degree-uniform or shifted/mixed assertion.

The final certificate is PASS with 65 checks and no failures. Its
criteria record also certifies all principal minors nonnegative. The
first run was FAIL because an extra check required the generic interval
enclosure of s_6 to contain the enclosure from its equivalent closed
formula. Such containment is not required for equivalent interval
expressions and need not hold. The original script and full failed
certificate remain at `scripts/central-jacobi/quartic-624/first-pass.py`
and `scripts/central-jacobi/quartic-624/first-pass.json`. The correction
checks the identities symbolically and uses the generic recurrence for
H; no sign failure, input change or precision campaign was concealed.
The original calculation did not claim an independent audit; the separate
audit below now supplies it, with the inherited qualifications retained.

### Separate independent finite audit — 5 November 2026, step626

The unchanged SPECIALIZE scope in
`drafts/literature/2026-11-05-theta-quartic-free-square-root-audit.md`
was separately approved at step625. This audit found no mathematical
defect in the stated finite result. No new factor, degree extension,
general root theorem or transcendental evaluator was introduced.

**Exact algebra and input scope.** Dividing by R_4 and expanding at
y+h gives the displayed p,q,r, with no root-location hypothesis.
The imported convolution weights give successively 2b=0, 2c=p,
2e=q and 2f+c^2/6=r. Thus the proposed real monic Q is both an exact
self-convolution factor and the unique such factor; positivity is not
used to prove existence or uniqueness. The sign convention is correct
because the two ordinary coefficient signs multiply to (-1)^(i+j).
L019/L021 supply positive finite moments, so no leading divisor vanishes.
The relation xi(1/2+sqrt(w)/2)/8=sum_j m_j w^j/[8*4^j*(2j)!]
gives gamma(j)=8*4^j*j!*a_j for every j used, including j=4.

The full five actual_a and gamma intervals, analytic errors and hash
records were inspected. An independent exact-rational check recomputes
each coefficient enclosure from P_0 plus [-E_G/1600^j,E_G/1600^j],
then verifies the entire saved gamma enclosure after normalization.
The radius1600 uniform complex-disk bound includes the circle, so Cauchy's
coefficient estimate applies at j=4 as it does at smaller j. All retained
cell errors and all omitted theta, integration and cosh tails remain
paid by L778; no real-axis derivative estimate is substituted. The
complete inherited evaluator equals the step433 replay, and its hash
matches both that audit and L791/step478. All original source and
certificate hashes remain unchanged. This reuses the audited analytic
input and trusted backend contracts; it does not attest the installed
transcendental backend independently. L791's fitted model and L823 are
not mathematical inputs.

**Independent arithmetic and complete certificate.** Run

`python3 scripts/central-jacobi/audit_626.py`

The full report is `scripts/central-jacobi/audit-626/audit-report.json`.
The original step624 program is replayed into that directory at
`scripts/central-jacobi/audit-626/quartic-free-square-root-replay-624.json`;
its entire parsed certificate equals the original, including all exact
factor intervals, grid enlargements, symbolic Newton identities, matrix
entries and 15 principal-minor bounds. Original artifacts are not
overwritten. Inspection of the old/final program difference confirms
that the first-pass containment failure was not a necessary criterion:
two valid enclosures of the same polynomial value need not contain one
another. The symbolic correction and generic Newton recurrence are valid.
The failed step624 script and certificate remain preserved.

For an independent sign calculation the audit uses a different arithmetic
ordering. Exact rational intervals are rounded outward to multiples of
10^(-90) after operations. For [m-r,m+r] and [n-s,n+s], multiplication
is enclosed by midpoint mn and radius |m|s+|n|r+rs; floor/ceiling
rounding only enlarges the interval. Nonzero interval reciprocals use
the reversed reciprocal endpoints. These operations enclose every exact
coefficient despite correlations. The centering is recomputed in Horner
order, and all three resulting factor intervals remain within the stated
six-decimal bounds above. The calculation uses these recomputed intervals,
not the original factor grid or any approximate roots.

To avoid the original Newton-evaluation ordering, form

\[
 T=\begin{pmatrix}0&0&0&-f\\1&0&0&-e\\
                   0&1&0&-c\\0&0&1&0\end{pmatrix}.
\]

Expanding det(zI-T) gives Q(z). The coefficient-based companion trace
identity, also recorded in Parrilo's cited Lecture5 Section3.1,
equation(2), p.5-2, gives s_k=tr(T^k), including multiplicities and
without a real-root premise. Equivalently, triangularizing T over C
makes its diagonal the roots of Q with algebraic multiplicities; the
trace of every power is their power sum. The audit computes powers
T^0,...,T^6 by interval matrix multiplication, constructs H from these
traces, and evaluates all 15 principal determinants by recursive Laplace
expansion, independently of the original signed-permutation routine.
All are strictly positive. The four leading outward bounds are again
exactly the four six-decimal enclosures in the table above; complete
rational endpoints were inspected, not only a preview or midpoint.

A second sufficient sign check uses symmetric Schur elimination:
starting with H, for pivot a=M_00>0 replace the remaining block by
M_ij-M_i0*M_0j/a. This is the congruence reduction
M ~ diag(a,Schur(M)), so positive pivots certify positive definiteness.
All operations are enclosed on the same rational grid. The four pivots
have outward bounds

\[
 [4,4],\quad[839.613650,839.613651],\quad
 [119346.902299,119346.902300],\quad
 [7958248.904869,7958248.904870].
\]

Every lower bound exceeds the required threshold zero. Either the
independent leading-minor test or this congruence test proves H positive
definite. The imported multiplicity-safe Hermite theorem and the rank
argument above then give four distinct real roots. Nonstrict leading
minors are nowhere used as a PSD criterion.

The final audit report is PASS: 60 checks, no failures. Its first execution
stopped before the mathematical test because step433's check record is a
list of completed-check strings, whereas steps478/624 use named Boolean
objects. The reader was corrected to retain PASS/no-failure checks for
step433 and every Boolean outcome for the latter reports. That initial
program and error record are preserved as `scripts/central-jacobi/audit-626/first-run.py`
and `scripts/central-jacobi/audit-626/first-run.json`; no mathematical sign
failure or precision change occurred. This audit supplies reliable local
finite evidence by known methods, not progress beyond the checked general
theorems or a uniform realization. Shifted/mixed signs and RH remain open.

## Mathlib

Full matching coverage is unchecked, including this actual-theta
coefficient certificate, finite-free factor and Hermite test. Availability
of supporting Newton identities and matrix positivity results has not
been checked here; no theorem absence or formal verification is claimed.
General operation and root criteria are imported by the precise citations
above, and only their approved finite specialization is proved here.
