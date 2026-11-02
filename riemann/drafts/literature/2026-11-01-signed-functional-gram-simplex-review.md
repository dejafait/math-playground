# Joint signed-functional Gram/simplex mechanism: completed source comparison

TARGET: Assess source coverage for a positive Gram or simplex representation of L629's complete c=(0,1) signed functional Q_{N,L}, targeting Q_{N,L}(a)>=Gamma/2 uniformly for complex a and N=floor(exp(L/100)) beyond one absolute L0.
CHECKED: 2026-11-01
DECISION: EXPLORE
SEARCH_EVIDENCE: Bounded searches covered Hermite–Genocchi/simplex formulas, HCIZ and amplitude insertions, Gram/determinant integration and signed twisted-fourth-moment positivity; exact queries and local duplicate/failure comparisons are recorded below. No matching arithmetic half-margin theorem was identified; this is not a novelty or exhaustive-absence claim.
SOURCE_EVIDENCE: Inspected Baxter–Brummelhuis arXiv:1006.1996v1 Theorem 4.2 and its induction, Theorem 4.3/Corollaries 4.4–4.5, pp. 8–10; de Boor arXiv:math/0502036v1 Proposition 21, Corollary 28/(29), Section 9; McSwiggen arXiv:1712.03995v3 (2), Theorem 1, Section 3.4 and Theorem 8/Section 4.2; Forrester arXiv:1806.10411v1 (1.7), Sections 2.2–2.3. Screened Durkan–Page arXiv:2606.27323v2 Section 1.2/(1.6), full Theorem 15 and its preceding shift qualifications; its proof is unreviewed. Reused the existing Hughes–Young and filtered-moment assessments.
COMPARISON: These sources provide a representation toolkit, not the requested lower bound. The exact amplitude and differentiated-sign mismatches are detailed below. L630's checked scalar first jet does not control the remaining joint functional.
GAP: Construct and check a coupled representation for the actual six amplitudes and analytic C_N, then prove the extracted form dominates Gamma/2 uniformly in growing N. This is an unresolved mathematical bridge, not a missing essential toolkit source; no such identity or domination is claimed here.
REASON: Adequate source coverage permits one bounded creative identity test retaining the arithmetic amplitudes jointly. Direct scalar-kernel substitution is unsupported. Stop the candidate on a coefficient mismatch or unjustified amplitude insertion; do not repeat the parked absolute budgets.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED continuation changes the essential source scope from a centered first-jet bound to a joint positive representation; this turn supplies that comparison.
SCOPE: L629's complete c=(0,1) functional, arbitrary complex coefficients, N=floor(exp(L/100))>=2, full divisor tail and analytic C_N(q), with the sought bound beyond one coefficient-independent L0. Known formulas may be cited only within their stated hypotheses; a weighted extension is the proposed research, not an imported premise. No other observer or pointwise Xi sign is covered.
COVERED_TARGET: Test a coupled Grassmannian Gram identity for L629's complete c=(0,1) functional, first at constant amplitude and actual N=2 with arbitrary complex coefficients and full tails, toward Q_{N,L}>=Gamma/2 uniformly for N=floor(exp(L/100)).

## Exact prospective object and relevance

Using precisely L629's h_nu and rational weights, the prospective
quadratic form is

    Q_{N,L}(a)=5040 Re sum_(|nu|<=8) w_(nu,2)
                         partial^nu B_N(0;a)/(nu! L^|nu|),
    Gamma=a^*G_N a.

The sum uses L629's pair-symmetric index convention. This notation
only rescales its existing complete c=(0,1) functional; it asserts
no new identity or estimate. The proposed threshold is the one-sided
lower bound Q_{N,L}(a)>=Gamma/2 for all complex a, at the prescribed
length beyond one absolute L0. If proved with the still-qualified
L629 transfer, it would give an averaged derivative-observer margin.
The other observer directions, source/local audits and pointwise Xi
signs would remain unresolved; RH would remain open.

The new idea to assess is whether the complete subset sum admits
an integral of coupled Gram forms, perhaps through an ordered-simplex
or unitary-integral identity, before taking the signed derivatives.
This is not established. In particular B_N(q_I;a) depends on the
chosen subset I; a formula for a plain exponential divided difference
cannot simply be applied to that amplitude. Differentiation can also
destroy positivity. Both are explicit possible obstructions.

## Bounded test to prepare, not perform in the audit turn

First locate and inspect the exact primary formulas and their
amplitude, smoothness, symmetry and repeated-node qualifications.
Compare against L629's actual six terms and derivative operator.
If a candidate identity survives that comparison, a subsequent
creative proof attempt should first check it at B_N(q;a)=Gamma and
at the actual one-prime N=2 form for arbitrary complex coefficients
and admissible L, retaining the full infinite tail and differentiated
normalization. The identity must reproduce the exact L629 coefficients.
A mismatch, loss of Hermitian symmetry, invalid amplitude hypothesis
or an explicit negative direction defeats that proposed positive
representation. A finite success merely admits the all-N test;
it is not proof of the uniform threshold.

The continuation criterion is an applicable primary identity together
with an explicit plan to control its differentiated coupled form
uniformly in N. If coverage supplies only the scalar-amplitude case,
record the missing bridge honestly and do not infer the lower bound.
The old freezing, prefix-inverse, absolute-Cauchy and termwise signed
budget stops remain preserved. No exhausted mechanism is reopened
by changing its name; the proposed coupled representation must pass
its own discriminating identity test.

The paragraphs above preserve the original nomination and its bounded
test. The completed comparison below supersedes their pending source
status. No new theorem, mathematical script or representation was
derived. Matching Mathlib coverage remains unchecked and unknown.
The newly ready COVERED_TARGET receives separate supervisor approval
before mathematical invocation; no second source search is requested.

## Completed primary comparison

### Scalar simplex formula

B. J. C. Baxter and R. Brummelhuis, *Functionals of exponential
Brownian motion and divided differences*,
[arXiv:1006.1996v1, Theorem 4.2/(4.3)–(4.6), pp. 8–9](https://arxiv.org/pdf/1006.1996v1#page=8):
for n>=1, f in C^n(R), and real, possibly repeated x_0,...,x_n,

    f[x_0,...,x_n]=integral_(t_j>=0,sum_(j=1)^n t_j<=1)
                          f^(n)(sum_(j=0)^n t_j x_j) dt_1...dt_n,
    t_0=1-sum_(j=1)^n t_j.

Read the base case and full induction, including t_(n+1)=t_0 tau.
Theorem 4.3 and Corollaries 4.4–4.5, pp. 9–10, give the linear
simplex change and ordered-integral/exponential forms. The measure
is ordinary simplex volume, not a probability normalization. This
is one scalar function evaluated at nodes. It does not supply
L629's six subset-dependent amplitudes. Complex-node continuation
and positivity of a signed differential extraction are not conclusions
of this real-node theorem. No specialization to B_N is performed.

### Products and coincident nodes

C. de Boor, *Divided Differences*, Surveys in Approximation Theory
1 (2005), 46–69,
[arXiv:math/0502036v1, Proposition 21, p. 51; Corollary 28/(29), p. 55](https://arxiv.org/pdf/math/0502036v1#page=6).
Read the polynomial node-continuity proof and the matrix-product
argument for the Leibniz formula

    Delta(t_1,...,t_n)(pq)
      =sum_(j=1)^n Delta(t_j,...,t_n)p Delta(t_1,...,t_j)q.

Here p,q are polynomials; the definitions include confluent nodes.
Section 9, pp. 63–65, also records the classical simplex relation.
Product identities can organize polynomial tests, but supply neither
a conjugate-square structure nor a uniform arithmetic estimate.
The full analytic amplitude needs its own justification. No reproof
of these classical statements is proposed.

### Unitary and Hamiltonian formulas

C. McSwiggen, *A new proof of Harish-Chandra's integral formula*,
[arXiv:1712.03995v3, (2), Theorem 1, Sections 3.4 and 4.2](https://arxiv.org/html/1712.03995v3),
gives, for real diagonal matrices with distinct ordered spectra and
normalized Haar measure,

    integral_U(m) exp(tr(AUBU*)) dU
      =(product_(j=1)^(m-1) j!) det(exp(a_i b_j))/(Delta(a)Delta(b)).

Section 3.4 extends the multiplied identity analytically across
singular Cartan elements; the quotient must use its removable limit.
Section 4.2/Theorem 8 assumes a compact symplectic manifold, a
Hamiltonian torus action and Liouville measure. Read its moment-map
verification and orbit application. Neither statement permits an
arbitrary amplitude insertion by evaluating it at stationary points.
The rank-two repeated-spectrum case is a candidate starting point;
its six-term normalization has not been calculated here. No weighted
localization theorem or differentiated positivity is imported.

### Determinant Gram mechanism

P. J. Forrester, *Meet Andreief, Bordeaux 1886, and Andreev, Kharkov
1882–83*,
[arXiv:1806.10411v1, (1.7), pp. 1–2; Sections 2.2–2.3, pp. 4–5](https://arxiv.org/pdf/1806.10411v1#page=2),
states and proves

    integral_(I^m) det[f_j(x_k)] det[g_j(x_k)] product_k dx_k
      =m! det[integral_I f_j(x)g_k(x) dx].

Read the determinant expansion, row integration and finite
Cauchy–Binet comparison. For any use require absolute integrability
of the expanded products; separate integrability alone does not
justify Fubini. A positive Gram use requires a positive measure and
conjugate-matched factors, for example L2 functions. No such factors
are identified for L629's differentiated extraction. The general
bilinear formula itself asserts no sign.

### Stronger amplified-moment lead and reused overlap

B. Durkan and T. Page, *Amplified moments of the Riemann zeta
function*,
[arXiv:2606.27323v2, Section 1.2/(1.6), Section 1.3/Theorem 15](https://arxiv.org/html/2606.27323v2#S1.SS3),
5 August 2026, uses A(s)=sum_(n<=y)P[n]/n^s with P a real
polynomial and P[n]=P(log(y/n)/log y). Read this setup and the
whole shifted fourth-moment statement, including its domain,
vartheta_k<1/(4k), shift continuation and error qualifications.
It is not a coefficient-uniform positive signed-functional theorem
for arbitrary complex a; it cannot be imported as the present
half-margin. Its proof was not reviewed or used.

Reuse the already inspected source comparison in
[collective arithmetic coverage](2026-11-01-collective-arithmetic-signed-spectrum.md),
especially its bramble_trace paper 36 v4 Theorem 6/Section 7
and paper 41 v4 Theorems 2–2a scope distinctions. The former
arithmetic application is untwisted; the latter retains a fixed
positive Laguerre-order/log-height ratio. Their recorded hypotheses
do not cover this fixed-order arbitrary-amplifier assertion. The
new search rediscovered paper 36; that is overlap, not new evidence
for applicability. Hughes–Young input coverage is reused unchanged.

## Search record and bounded research admission

Queries actually used include: `Hermite Genocchi formula divided
differences exponential simplex integral theorem de Boor`;
`Harish Chandra Itzykson Zuber integral formula Hermitian repeated
eigenvalues determinant exponential positive`; `Harish Chandra
Itzykson Zuber arbitrary amplitude localization Grassmannian
insertion divided differences positivity`; `Andreief integration
formula Forrester proof pdf`; `twisted fourth moment positive Gram`;
`six twisted fourth moment integral arithmetic positivity`;
`Grassmannian Harish-Chandra amplitude positive`; and `divided
differences subset positive Gram`. Searches were bounded; unrelated
scattering-amplitude hits were not treated as mathematical coverage.
Only the primary sources and reusable local assessments above support
the comparison. No failed query establishes novelty.

Local searches were limited to the relevant November 1 full-Gram,
collective-arithmetic and centered-first-jet assessments/working
records and full-Gram ATTEMPTS files. Read L629 completely and
L623/L624's relevant hypotheses, formulas and convergence argument.
The old freezing, prefix-o(1), absolute-Cauchy and termwise-budget
stops are preserved. L630 remains an audited first-jet input;
its estimate is not an iterable higher-jet estimate.

The research choice is one coupled representation, rather than
another absolute norm budget. The candidate should start with the
rank-two unitary-orbit kernel, retaining two arithmetic convolution
vectors and C_N in the same expression before applying the observer.
This describes a construction to attempt, not an identity. Neither
termwise positive B_N nor permission to insert arbitrary amplitudes
is assumed. Importing HG, HCIZ or Andreief only needs their stated
hypotheses; proving the missing amplitude bridge would be new local
work within EXPLORE, without a certified originality claim.

Continue only if a fully specified candidate reproduces L629's
constant-amplitude coefficient and the exact actual N=2 Hermitian
form for all complex a_1,a_2, including the full power-of-two tail
and every normalization derivative. These are diagnostic tests:
N=2 is first a fixed-N specialization, not a claim about the
large-L prescribed growing family. Passing it is necessary for a
universal exact identity, not evidence of uniform all-N domination.
An all-N continuation must identify how a positive measure and
conjugate factors survive the extraction and how the remaining
defect is bounded by Gamma/2 independently of the input vector.
An exact coefficient mismatch, unjustified amplitude rule, or
rigorous negative direction abandons that candidate. Failure to
construct a candidate is inconclusive and must be recorded as such.

L629's reduction and other input conclusions retain their unaudited
qualifications. Even a proved half-margin would leave room for its
O(Gamma/L) transfer error to check, other observers, independent
audits and pointwise Xi signs. No RH candidate is claimed. No lemma,
DAG edge, PROOF argument or mathematical script changed this turn.
