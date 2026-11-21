# Lemma 792: central index-five signed residual and collision margins

## Hypotheses

Use L018/L021/L776's actual completion and normalization
G(w)=xi(1/2+sqrt(w)/2)/8=sum a_j w^j,
gamma(j)=8*4^j*j!*a_j and R_j=gamma(j)/gamma(0).
Use L791's exact positive Banach solution (A,B,C) in its entire original
radius10^(-15) box, its fixed D=B_J/2, degree5 model p(y)=sum p_j y^j,
and S=B R_1. Its exact matching F_j=R_j for j<=4 is an input.
Use the coefficient intervals and complex analytic error of L778's
audited degree96 evaluator, including all retained quadrature widths and
its trusted software contracts. There is no RH or actual-root premise.

The finite certificate is computer-assisted informal evidence, not
formally verified arithmetic. It passed the separate step483 audit below,
subject to the inherited analytic and software contracts.
Its rational operations use Python integer/Fraction arithmetic and
outward rounding on the 10^(-100) grid from the step478 audit.

## Conclusion

Put t_m=-p_5>0 and t_a=R_5/S^5>0. The signed coefficient residual
delta=(-t_a)-p_5=t_m-t_a satisfies

2.94347417497914061298e-10 < delta < 2.94347417514615466953e-10.

Define f(x)=x^5+p_1*x^4+p_2*x^3+p_3*x^2+p_4*x. Its four critical
points are simple positive numbers x_1<x_2<x_3<x_4. The exact interval
of t for which f(x)-t has five real roots, counted with multiplicity,
is [L,U], where

L=f(x_2), U=f(x_1),
2.613486880358151681436165e-6 < L < 2.613486880800946664045556e-6,
2.623019569357062518698362e-6 < U < 2.623019569681543916731915e-6.

The actual magnitude is strictly inside this interval, with

4.989815097205280861414e-9 < t_a-L < 4.989815540002532575702e-9,
4.542873458908304686494e-9 < U-t_a < 4.542873783391971824945e-9.

These conservative bounds hold at the exact solution, retaining its
full parameter/data uncertainty. The actual central scaled Jensen
polynomial J^{5,0}(-y/S)/gamma(0) has five simple positive roots.
That qualitative low-degree hyperbolicity is already covered by the
literature; this calculation adds a local signed residual and quantitative
distances for this fixed pencil, not a new general sign theorem.
No other degree, shift, multiplier estimate, all-degree mixed positivity
or RH conclusion follows. Production and the subsequent finite audit
are recorded separately below.

## Proof

**Known criterion and exact specialization.** Rajesh Pereira,
[*Which quartic polynomials have a hyperbolic antiderivative?*,
arXiv:1901.08156v2](https://arxiv.org/pdf/1901.08156v2), 17 April2019,
pp.1–2, Lemma1.1 (the Souroujon–Stoyanov criterion and its Rolle/IVT
proof), gives the exact constant interval for a polynomial with prescribed
real-rooted derivative. Apply it to the monic quartic q=f'/5, using
P=f/5 and constant c=t/5. The factor5 scales both the constant and the
critical values and hence cancels from the inequalities. With critical
points in ascending order, the criterion reads

max(f(x_2),f(x_4)) <= t <= min(f(x_1),f(x_3)).

Weak endpoints allow multiple roots; simple critical points and strict
inequalities give simple roots. The source's descending enumeration
has odd indices x_4,x_2 and even indices x_3,x_1, so the signs here
agree with its statement. No new inverse-Rolle theorem is asserted.

Jonathan Holland, [arXiv:2608.08682v1](https://arxiv.org/html/2608.08682v1),
9 August2026, equations(66)–(71)/Lemma6.2 give the matching normalization,
already instantiated and audited in L791. In the same scale S=B R_1,
the actual polynomial has coefficients
(-1)^j binom(5,j)R_j/S^j. They equal p_j for j<=4, and the fifth is
-R_5/S^5=-t_a, since binom(5,5)=1. Thus reciprocal reversal gives

x^5 [J^{5,0}(-1/(Sx))/gamma(0)]=f(x)-t_a.

The model reversal is f(x)-t_m. This is a constant pencil; no eventual
shift or new source hypothesis is invoked at n=0.

**Actual coefficient enclosure.** The program
`scripts/central-jacobi/signed_residual_480.py` reads only the audited
L778 evaluator certificate and the saved L791 model certificate; both
input SHA256 values are retained in the output. For j=0,...,5 it adds
the symmetric Cauchy error E_G/1600^j to the entire inherited polynomial
coefficient interval before multiplying by 8*4^j*j!. This is justified
by L778's complex bound (5), not a real-axis approximation. The sixth
polynomial coefficient is not treated as an exact coefficient of G.
All six positive gamma intervals, ordinary coefficients, ratios, original
box, D, S, model coefficients and signed residual appear in
`scripts/central-jacobi/signed-residual-certificate-480.json`.
Some conservative outward bounds, with extra decimal rounding, are

1.753923091213315303489e-9 < gamma(5) < 1.753923091213315303490e-9,
.266624456637090190929190401245 < S < .266624456637090237139176632086,
2.618476695898151944906970e-6 < t_a < 2.618476695898154214011868e-6,
2.618771043315652128073166e-6 < t_m < 2.618771043315666560373924e-6.

Every rational operation is rounded outward: floor(10^100*l)/10^100
and ceil(10^100*u)/10^100. This encloses the exact result inductively.
Positive denominator intervals are checked before division. The whole
original box and D interval are kept; no center-only evaluation, parameter
refinement, new solution, precision increase or model rescue is used.
Treating correlated data as independent intervals enlarges the tested
set and includes the exact correlated solution. Directed interval
evaluation of t_m-t_a gives the claimed positive residual.

**Complete critical-point and critical-value evidence.** Form f and its
literal derivative, whose leading coefficient is exactly5. A fixed
j/1000 grid, 0<=j<=200, identifies four sign brackets. Rational bisection
to width below10^(-12) preserves strict opposite signs throughout the
entire parameter box. The final exact brackets are

| i | left | right | signs of f' at endpoints |
|---|---|---|---|
| 1 | 50218208479/1073741824000 | 313863803/6710886400 | +,- |
| 2 | 33354338651/536870912000 | 66708677303/1073741824000 | -,+ |
| 3 | 93616060701/1073741824000 | 46808030351/536870912000 | +,- |
| 4 | 16164792849/107374182400 | 161647928491/1073741824000 | -,+ |

The complete rational f' endpoint intervals and f evaluations on all
four closed brackets are stored under `critical_points`. The brackets
are disjoint and positive. IVT gives four distinct roots of the quartic
f'; degree4 shows that these exhaust its roots and each is simple.
Evaluating f on the entire brackets encloses the exact critical values.
Conservative rounded bounds are

| i | lower bound for f(x_i) | upper bound for f(x_i) |
|---|---|---|
| 1 | 2.623019569357062518698362e-6 | 2.623019569681543916731915e-6 |
| 2 | 2.613486880358151681436165e-6 | 2.613486880800946664045556e-6 |
| 3 | 2.640829182651894807223633e-6 | 2.640829183378282748565444e-6 |
| 4 | 1.731205359955270255291876e-6 | 1.731205362087381916741088e-6 |

These separated intervals show f(x_2)>f(x_4) and f(x_1)<f(x_3).
They identify the exact active boundaries L and U, rather than merely
sufficient bounds. Applying the cited criterion proves the assertion
about the complete closed real-rootedness interval. Interval subtraction
using the same uncertain t_a gives both claimed strictly positive
distances. Subtracting U and L from t_m also gives

4.248526041395958324439e-9 < U-t_m < 4.248526365891788658749e-9,
5.284162514705464027610e-9 < t_m-L < 5.284162957514878937758e-9.

Equivalently, the admissible signed residual delta lies in
[t_m-U,t_m-L]; its actual value is the positive number above.
The residual moves the magnitude toward the lower boundary and leaves
strict room on both sides. No prescribed residual sign was assumed.

Since L>0, all t in [L,U] are positive. For x<=0 every nonconstant
term of f(x) is nonpositive, by its alternating coefficient signs, and
-t<0. Thus f(x)-t has no nonpositive root. At t_a it has five simple
positive roots, and inversion preserves positivity and simplicity.
At t=L or U a critical point is also a root, giving a finite collision.
The separate coefficient-zero/degree-drop boundary is t=0; its distance
from the actual coefficient is t_a>2.618476695898151944906970e-6.
It is not confused with either finite collision boundary.

**Reproduction and limits.** Run
`python3 scripts/central-jacobi/signed_residual_480.py`.
The output is `CERTIFIED_STRICT_INTERIOR`, 140 checks, no failures;
complete rational enclosures and actual/required bounds are saved at the
certificate path above. Existing evaluator/model files are hash-checked
and unchanged. The script imports only the rational interval class from
the step478 audit and does not run that audit or its model replay.
No transcendental integrator is rebuilt. This inherits its analytic and
software assumptions explicitly and does not attest the runtime binary.

The first run is preserved in
`scripts/central-jacobi/signed-residual-first-pass-480.json`.
Its only failed check incorrectly demanded a negative signed residual;
both strict interior checks had passed. The check was corrected to
require a certified nonzero sign, as the approved diagnostic asks for
the actual sign without prescribing a direction. The final positive
sign and interval margins use identical input data and numerical results.
The final record additionally stores coefficient/residual intervals and
their summary, and replaces the inactive `upper_x3: false` diagnostic
with the active `upper_x1: true` diagnostic. Thus the entire certificate
records are not identical. These differences were checked in step483.

For comparison, Griffin–Ono–Rolen–Thorner–Tripp–Wagner,
[*Jensen polynomials for the Riemann xi-function*,
arXiv:1910.01227v3](https://arxiv.org/html/1910.01227v3),
17 December2020, Theorem1.2/Corollary1.3 and Section5, already give
unconditional hyperbolicity in a much larger degree range including5
at every shift. Their gamma differs by a common factor8, irrelevant to
ratios and roots. That theorem is overlap, not an input to this numerical
certificate; it supplies no distance in this fixed coefficient pencil.
The new local enclosure is a reproduction/specialization of known methods,
not evidence of an all-degree mechanism or a novelty claim.

### Separate finite audit, 5 November 2026 — step483

Used the preexisting SPECIALIZE assessment
`drafts/literature/2026-11-05-central-signed-residual-audit.md` for precisely
this fixed pencil. Run `python3 scripts/central-jacobi/audit_483.py`.
The full exact evidence is in
`scripts/central-jacobi/audit-483/audit-report.json`: PASS, 173 checks,
no failures. This does not rebuild the transcendental evaluator or
reaudit L791's Banach proof; both remain audited premises with their
stated software contracts. Source/model hashes agree with the inherited
audit and the production certificate, and all original inputs are preserved.

The independent checker uses unrounded exact Fraction intervals rather
than the production grid arithmetic. It checks every retained quadrature
interval plus E_G/1600^j for j=0,...,5 and the factor8*4^j*j!. It forms
model coefficients from complete Pochhammer products, independently of
the production recurrence, and checks containment in the saved intervals.
The algebraically cancelled expression gamma(5)*gamma(0)^4 /
[B^5*gamma(1)^5] independently verifies the actual fifth magnitude.
The binomial factor is1. Matching indices0..4 therefore gives exactly
the constant-pencil reversal displayed above. Applying Pereira to f'/5
divides both primitive and constant by5, so no factor is lost.

All eight derivative endpoint intervals are checked against independent
expanded polynomial sums, with the strict signs in the table. Exact
interval Horner evaluation over each full bracket verifies every saved
critical-value enclosure; independently expanded whole-bracket values
are also retained. The four disjoint sign brackets exhaust the quartic
derivative and give simple critical points for every polynomial in the
original parameter box. In particular they apply simultaneously at the
exact L791 solution. Strict separation verifies the active extrema x2
and x1, hence the necessary and sufficient interval, rather than just
a sufficient subinterval. All printed rational brackets, decimal bounds,
signed coefficient/residual intervals, four actual/model distances and
the t=0 degree-drop distance pass exact comparisons. The positivity and
exterior-ray argument above then gives the stated simple positive roots.

The complete common mathematical fields of both production certificates
agree, including coefficients, parameter data, all critical-point
records, collision bounds and distances. The sole changed check is the
negative-sign assertion replaced by a nonzero-sign assertion; both
interior checks already passed in the first run. The additional fields
and changed active-bound diagnostic described above are checked explicitly;
the inactive first diagnostic asserted no false inequality. The original
first-pass program source was not retained, so the audit verifies its
saved mathematical data, not an unavailable source diff. No source-history
claim is inferred solely from equal output values.

The audit's own first run is preserved as
`scripts/central-jacobi/audit-483/audit-first-pass.json`. Its failed tests
were overly strict record comparisons: decimal/rational string equality
for unchanged parameters and an assumption that the two production
records had identical fields. Numeric rational equality and the explicit
field-difference checks above repair those tests without altering either
production certificate or any mathematical enclosure. This is a verified
local specialization of known methods, with no advance beyond the checked
literature's general hyperbolicity range and no uniform signed estimate.

## Mathlib

Full matching coverage for the constant-pencil criterion and this finite
specialization is unchecked. Supporting named ingredients are Cauchy's
coefficient estimate and the intermediate value theorem. No absence or
formal-verification claim is made.
