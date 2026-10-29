# Two-height Hardy-jet moments: completed source comparison

TARGET: Assess whether complete second and fourth moments of the paired Hardy jets at t and t+1/log H can rule out a clipped mean of log H/288 in the first jet.
CHECKED: 2026-10-28
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Bounded searches for Hardy shifted second/fourth derivative moments, two-point jet moment laws and clipped Laguerre means located Bettin's exact shifted-second theorem and the already assessed Bui--Hall fourth theorem; compared the local L472/L471 and half-carrier-turn stops and the primary translated-observer result listed below. No inspected theorem decides the six-coordinate clipped-mean feasibility question; no novelty is inferred.
SOURCE_EVIDENCE: Bettin arXiv:1111.0925v1 https://arxiv.org/pdf/1111.0925v1 Theorem 1 p. 2 and small-shift completion pp. 9--10; Bui--Hall arXiv:2304.05178v1 https://arxiv.org/html/2304.05178v1 (1), (6)--(7), Proposition 3, Section 5 Cauchy passage and Section 7; Kösters arXiv:0803.1141v2 https://arxiv.org/pdf/0803.1141v2 Theorems 1.1--1.2 pp. 3--4 and proof opening p. 6; bramble_trace paper 36 displayed v4 https://rstation.ai/problems/riemann_hypothesis/papers/36 Theorem 6 and Corollary 11/(51)--(53), its Theorem 10 hypotheses and localization qualification.
COMPARISON: Bettin fills the previously missing complex-shift second input, and Bui--Hall supplies all four independent small complex shifts with a uniform error; fixed-order Hardy conversion is covered. These inputs specify every paired second/fourth entry without assuming independence. Shifted squares and translated signed observers do not decide the clipped statistic. The six-variable feasibility construction or separator remains mathematical work.
GAP: Specialize the source generators with their Hardy phases to the full 21 second and 126 fourth entries, retain the stricter same-height odd second tolerances, and decide feasibility of E Q>=ell/288. No paired coefficient, positive extension, separator or actual-zeta clipped bound is proved in this literature turn.
REASON: Essential source scope is now accessible and sufficient for one bounded specialization and abstract feasibility test. Import the arithmetic theorems by citation; do not reprove them. The proposed new ready continuation requires separate approval next invocation.
LITERATURE_REASON: The target changes from auditing L472 to paired jets at distinct heights; a complete shifted second-moment input and its comparison with the fourth-moment input have not been assessed.
SCOPE: Fixed ell=log H, t uniform on [H,2H], ordinary jets of orders 0,1,2, and separation exactly 1/ell; fixed bounded complex neighborhoods for Cauchy differentiation only. No growing order, random shift, prescribed error constants, first/cubic constraints, RH or simplicity.

## Original nomination, retained for scope

Use X_0(t)=(Z(t),Z'(t)/ell,Z''(t)/ell^2) and
X_1(t)=(Z(t+1/ell),Z'(t+1/ell)/ell,Z''(t+1/ell)/ell^2).
The proposed observable is Q(X_0)=(x_0 z_0-y_0^2)_+.
The source review must specify the entire degree-two and degree-four
data of the resulting six-coordinate law, with fixed divisors and
all published errors, before any feasibility attempt. No coefficient,
positive representing law or inequality for this new target is derived
here. The threshold is retained from L472, not claimed achievable
under the additional constraints.

Essential local inputs are L472's audited obstruction and L471's
connection of the actual clipped mean to N(H). The former's one-height
positive law need not have the required two-height extension. The
latter's failed ordinary-moment pair summation stays stopped. Before
larger external reads, search the active notebook narrowly for shifted
Hardy-jet correlations and their recorded failures, then retrieve
primary shifted second/fourth statements and their actual hypotheses.
Compare a full matching result or stronger theorem before proposing
any new derivation. Proposition 3's omitted proof remains unaudited.

Continue only if complete source coverage either supplies a relevant
import or defines one independently testable moment-feasibility or
separation target with precise tolerances. Abandon this proposed
discriminator if a known extension result or recorded obstruction
already decides it without new work. Missing essential source coverage
requires source review; persistent access blockers require parking it.
Even complete finite paired-height data do not automatically provide
global analytic realization or individual-height signs. First/cubic
moments, actual clipped mass, higher signs and RH remain unresolved.

## Completed primary-source comparison, 28 October 2026

This is source review only. The preceding request to specify the data
is discharged below by complete index sets, source generators and error
requirements, not by calculating their new paired coefficients. Those
specializations and their feasibility are reserved for research.

### Shifted second input

Sandro Bettin, *The second moment of the Riemann zeta function with
unbounded shifts*, Int. J. Number Theory 6 (2010), no. 8, 1933--1944,
[DOI 10.1142/S1793042110003861](https://doi.org/10.1142/S1793042110003861),
[arXiv:1111.0925v1, 3 November 2011, Theorem 1, p. 2](https://arxiv.org/pdf/1111.0925v1#page=2).
For T>=2, complex a,b with Re a, Re b=O(1/log T), and c=a-b,
the theorem states

    integral_0^T zeta(1/2+a+it) zeta(1/2-b-it) dt
      = integral_0^T [zeta(1+c)+zeta(1-c)
          chi(1/2+a+it) chi(1/2-b-it)] dt
        +O((sqrt(T)+sqrt(|Im a|)+sqrt(|Im b|)) log^2 T).

Here chi is the functional-equation factor, with
zeta(1-s)=chi(1-s)zeta(s). At c=0 the complete bracket has the
pointwise limiting interpretation specified in the theorem. Its two
zeta-pole terms must never be differentiated separately at c=0.
The introduction discusses shifts as large as T^(2-epsilon); only
|a|,|b|<=C/ell for fixed C is needed here. In particular this use
stays in its uniform small-shift range and has error O(sqrt(T)log^2 T).

Read the relevant small-|Im c| proof completion, pp. 9--10: the proof
separates the region where the shifted heights are small, applies its
chi comparison on the complement and integrates by parts before
combining the two main terms. This is the pertinent case for microscopic
shifts, rather than the large-|Im c| oscillatory estimate. This review
does not independently audit the entire arithmetic proof.

For the proposed two heights the source arguments are a=i r/ell and
b=i s/ell, r,s in {0,1}; both source shifts remain fixed when taking
the dyadic difference at T=H and 2H. Small complex circles about these
arguments remain in the same bounded shift class. Uniformity and
holomorphy permit Cauchy differentiation for each fixed order <=2
in each argument. This establishes source scope for all nine cross
second entries. A future application must still keep the Hardy phase
ratio and justify its approximation using Bui--Hall (6)--(7); a theorem
for zeta products alone is not already a theorem for Hardy derivatives.
No derivative of an unspecified real-variable remainder is licensed.

For both same-height blocks, Bui--Hall (1) and its preceding odd-order
display are the stronger direct inputs already imported in L472.
Their antiderivatives can be differenced at H+r/ell and 2H+r/ell,
using the fixed divisor ell throughout. The odd bounds must be retained;
the generic cross-entry tolerance O(1) must not replace them.

### Shifted fourth input and its actual error

H. M. Bui and R. R. Hall, *On the derivatives of Hardy's function
Z(t)*, Bull. Lond. Math. Soc. 55 (2023), 2304--2323,
[arXiv:2304.05178v1, Section 4.2, Proposition 3](https://arxiv.org/html/2304.05178v1#S4.SS2),
states, for four constant complex shifts of modulus <=C/log T,

    J(alpha1,alpha2,beta1,beta2)
      = T(log T)^4/(2 zeta(2)) integral_[0,1]^4 (u1-u2)^2
          T^(-(alpha1+beta1)u1-(alpha2+beta2)u2)
          T^((alpha1-alpha2)(u1-u2)u3
             +(beta1-beta2)(u1-u2)u4) du
        +O(T(log T)^3).

J is the sharp dyadic integral of two positive-height zeta factors with
alpha shifts and two negative-height factors with beta shifts. The
formula is uniform, permits coincident shifts and has no singular
shift denominators in this integral form. The source explicitly omits
its proof. This qualification remains attached to its import; access
to a published theorem statement is sufficient for an application,
but does not turn the omitted proof into an audited argument.

For any four choices r1,...,r4 in {0,1}, the required source evaluation
uses alpha1=i r1/ell, alpha2=i r2/ell, beta1=-i r3/ell,
beta2=-i r4/ell. Each occurrence has its own derivative variable,
including when two occurrences select the same coordinate. Thus all
mixed fourth monomials are covered, including three-versus-one and
four-versus-zero allocations between the two heights. There is no
restriction to the product of two squared values.

Read the source's Section 5 Cauchy passage and the complete Section 7
conversion, as well as (6)--(7). These retain reflection signs for the
negative-height factors, the ordinary Hardy phase and the fixed-order
conversion errors. Cauchy on fixed-radius microscopic circles retains
the normalized one-logarithm-lower fourth error. Applying this to the
two distinct centers, with the fixed divisor ell, is a specialization
to be written out in the subsequent research attempt, not a new
arithmetic moment theorem to reprove. No growing derivative-order or
growing-shift uniformity is required or asserted.

### Exact finite system nominated for a later test

Index coordinates by I={(r,j): r=0,1; j=0,1,2}, writing
Y_(r,j)(t)=Z^(j)(t+r/ell)/ell^j. Define the reference data by the
actual dyadic integrals

    S_ab(H)=H^(-1) integral_H^(2H) Y_a(t)Y_b(t) dt,
    F_m(H)=H^(-1) integral_H^(2H) product_(a in I) Y_a(t)^m_a dt,
                     m_a>=0, sum_a m_a=4.

These are definitions, not evaluations or assumptions about independent
jets. They name every required datum unambiguously before its source
specialization: 21 unordered second entries (six in each same-height
block and nine cross entries) and all 126 fourth multi-indices.
The second source generator is the complete Bettin bracket above,
with the Hardy conversion; the fourth generator is the complete
Proposition 3 integral above with that conversion. This avoids
substituting a two-squared-value theorem for the full tensor.

The proposed law must satisfy, with constants uniform in all
sufficiently large real H,

    E V_a V_b=S_ab(H)+O(1) for all unordered pairs except
       a=(r,0),b=(r,1) or a=(r,1),b=(r,2),
    E V_(r,0)V_(r,1)=O(H^(-2/3)ell^(-1)),
    E V_(r,1)V_(r,2)=O(H^(-2/3)ell^(-3)), r=0,1,
    E product_a V_a^m_a=F_m(H)+O_m(ell^3) for every |m|=4.

The same-height even leading second constants and all their permitted
O(1) errors are exactly L472 (1). For the cross entries the required
source specialization must give S_ab=ell K_ab+O(1); no K_ab has been
calculated here. For quartics it must give F_m=ell^4 q_m+O_m(ell^3),
including any vanishing leading coefficients. No improved error for
odd total derivative order at distinct centers is assumed. The above
reference-integral specification and these leading specifications
are to be compared explicitly in the next research attempt before
claiming success. Constants in the O terms are not prescribed. A
single common onset must serve all the finitely many constraints.

The discriminating threshold is E(V_(0,0)V_(0,2)-V_(0,1)^2)_+>=ell/288.
The law must be positive with total mass one and absolutely integrable
displayed observables. A finite atomic replacement is optional after
feasibility, using the measurable-map corollary precisely cited in
L472 Section 6; it cannot supply feasibility by itself. First and cubic
moments, exact lower quartic coefficients, sample paths and analytic
realization are not constraints of this test. The four tight odd
second entries cannot be erased by a reflection that changes the
cross moments; L472's reflection alone does not prove an extension.

### Stronger-result and duplicate comparison

H. Kösters, *On the occurrence of the sine kernel in connection with
the shifted moments of the Riemann zeta function*, J. Number Theory
130 (2010), 2596--2609,
[arXiv:0803.1141v2, Theorems 1.1--1.2, pp. 3--4](https://arxiv.org/pdf/0803.1141v2#page=3),
uses real shifts 2pi mu/log t and 2pi nu/log t with fixed real mu,nu
and T0>1. Theorem 1.1 is a shifted-second limit; Theorem 1.2 is the
two-squared-value fourth limit, with continuous coincidence values.
Read its fourth proof opening, p. 6, which starts with that restricted
dyadic square-product integral and its approximate functional equation.
These statements are useful classical comparisons, but do not assert
the independent complex-shift derivative theorem and errors needed
for all mixed entries here. No differentiation of those limit
statements, or new reproof of their profiles, is justified.

Reused the prior filtered-positivity comparison in
`2026-10-27-actual-xi-negative-part-mean-coverage.md` and inspected the
more directly related translated-observer statement:
bramble_trace, *Signs and uniform filtered positivity in fourth
moments of Hardy's function*, [paper 36, displayed v4,
21 October 2026 23:18 UTC](https://rstation.ai/problems/riemann_hypothesis/papers/36),
Theorem 6, Corollary 11 and (51)--(53). Corollary 11 fixes p>=0,
0<delta<1/13 and nonnegative nonzero w in C_c^infinity((0,1)); its
smooth window length lies between T^(12/13+delta) and T, its center
between T and 2T, and |h|<=13delta/(10240e log log T). It asserts a
positive signed Laguerre integral against Z(t+h)^2 with the stated
profile and relative O((log log T)^(-2)) error. The qualification
after its proof excludes arbitrary signed observer combinations and
localization on a negative interval. This is a platform-manuscript
comparison, not an independently audited theorem import here. The
version-specific /v4 URL failed; the root URL directly displayed v4.
Its translated-square observation does not assert a clipped-mean bound
or the required six-coordinate law. Its growing-order claims are not
needed. No access blocker remains for the essential moment inputs.

Locally, L472 constructs only the first three coordinates. L471
(7)--(9) explains the downstream connection to N(H), but its ordinary
fourth-moment pair-division stop is unchanged. The recorded
`ATTEMPTS/2026-10-14-half-carrier-turn-frozen-scalar-jets.md` rejects
freezing across a phase half-turn, not retaining two correlated jets
at the present fixed scaled separation one. Narrow searches of the
October 14--28 literature/attempt files found no completed duplicate
of this exact six-coordinate feasibility test. The search was bounded;
several broad Hardy queries were irrelevant, and no absence or novelty
claim follows. Mathlib coverage of the full shifted arithmetic results
and this feasibility test was not checked.

### Decision and bounded continuation

Source coverage permits a separate mathematical invocation after
approval of the newly written continuation assessment. First verify
the source specializations and then test whether the full paired data
still allow the stated clipped mass. A feasible law ends this finite
correlation discriminator; it is not a negative actual-Xi value.
A rigorously uniform separator would justify further investigation
only if it separates the actual permitted errors at the ell/288
threshold. Failure to find a law or a numerical separator is not
infeasibility. A new essential source scope requires review.

The natural first test is the extension of L472's rare/bulk mechanism
while retaining all cross constraints and tight odd errors. This is
established-mechanism development, not a newly invented creative RH
route. Until this test discriminates, there is no justified new central
positivity mechanism to label creative. Actual-law realization,
individual-height signs and higher mixed positivity remain open.
