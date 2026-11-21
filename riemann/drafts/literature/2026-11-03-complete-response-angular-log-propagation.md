# Source comparison: from the interior peak to an angular logarithmic mean

TARGET: Assess source coverage for converting L723's pointwise subsequential growth into a positive logarithmic mean on one fixed angular arc around u_*.
CHECKED: 2026-11-03
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 204 searched fixed-arc logarithmic means, logarithmic traces on intervals, Cartan/minimum-modulus and analytic Remez bounds; inspected the two primary sources below and reused the named ready spatial-Jensen assessments. Local comparison read L666's rational continuation, L708's fixed-profile conventions, L723's accepted conclusion and exact finite identity, and the exterior-anchor stop. Queries and scope differences are recorded below; no exact matching theorem was identified in this bounded search.
SOURCE_EVIDENCE: Il'yashenko–Yakovenko (1996), Sections 1.1/1.3/1.4, Lemmas 1–3 and complete proofs, printed pp.93–99, https://www.wisdom.weizmann.ac.il/~yakov/jde-95.pdf ; Brudnyi arXiv:math/9908105v1, Theorem 1.1, Definition 2.1/Remark 2.2 and relevant Section 2/4 proofs, PDF pp.2,5–6,9, https://arxiv.org/pdf/math/9908105v1 . Reuse the prior Ash–Novinger/Issa–Lalin/Brunault–Zudilin readings and Sokal scope comparison; exact interfaces and limits below.
COMPARISON: Known local zero-counting, zero-free harmonic and small-value tools cover the proposed proof ingredients, allowing zeros in the original function. None inspected directly supplies the fixed-arc r(b)/4 threshold for this growing rational family. The exterior-anchor relaxation and the spatial-defect arc have different observables. A bound with an unpaid O(n) loss, or planar convergence without trace control, is inadequate.
GAP: Verify one uniform pole-free angular neighborhood and exponential upper bound for the complete response, then control the signed logarithmic trace on a fixed arc along one L723 subsequence, with explicit loss below the required margin. The geometry-dependent loss, integrability and order of arc/subsequence choices remain mathematical obligations.
REASON: Essential general source coverage is available; the bounded search did not identify an exact theorem to import. EXPLORE permits one local zero-factor/harmonic-factor attempt at the preserved threshold, without claiming novelty or deriving that implication in this literature turn. The newly covered continuation receives separate supervisor approval before invocation.
SCOPE: Original fixed L703/L708 profile and full L666 G_n only; n=12q+3, u_*=(3+4i)/10, z=-1, b=sup supp chi and the accepted L723 limsup. Permit verification of local pole exclusion, O(n) logarithmic upper control, finite-n trace integrability and a quantitative fixed-arc transfer or an obstruction to that transfer. Do not replace log by log-plus, shrink eta with n, change masses/moments/profile, assume eventual nonvanishing or propagate from exterior anchors.
COVERED_TARGET: Test whether local zero-factor and harmonic estimates transfer L723's peak to the fixed-arc logarithmic lower bound r(b)/4 for the complete L666 response.
LITERATURE_REASON: The observable changes from one sampled complex value and its generating germ to the signed logarithm integrated along an angular arc. Uniform logarithmic trace control and common-subsequence hypotheses were not covered by the completed L723 assessment.

## Exact proposed intermediate target

The nomination below is preserved as the question assessed in step 204.
Its source gate is now EXPLORE; its mathematical assertions remain open.

Keep the actual fixed L703 profile, all L666 atoms and moments, and
n=12q+3. Let u_theta=(1/2)*exp(i*theta),
theta_*=arg(3+4i), and g_n(u)=G_n(u,-1). The proposed threshold is:
there exists a fixed eta in (0,pi/10) such that

    limsup_(q->infinity) [1/(2*eta*n)]
        *integral_(theta_*-eta)^(theta_*+eta)
                     log|g_n(u_theta)|dtheta >= r(b)/4 > 0.

Here r(b) is the accepted L723 rate, b=sup supp chi, and log(0)=-infinity
at isolated zeros. Finiteness of the integral and nonzero slices on
the relevant subsequence must be justified, not assumed. The arc and
profile are fixed before the subsequence; neither may shrink with n.
The proposed threshold concerns the integral of log, not log^+, a
maximum, an L2 norm, or separate pointwise limsups with unrelated
subsequences. It is not yet known to be true.

Essential local inputs are L666's exact rational definition, L708's
fixed-profile conventions and the now audited L723 pointwise conclusion
with its canonical qualifications. No exterior normalization is a
substitute for the actual peak at u_*. The possible mechanism must
verify pole exclusion and an exponential upper bound on one fixed
complex neighborhood from the complete finite family. Those auxiliary
hypotheses are unresolved for this proposed application; no estimate
has been proved or silently imported in this nomination. No additional
support-edge continuation in u is assumed.

The prospective use is a lower contribution to the angular mean of
log S_n(u), since S_n(u)=max_(|z|<=1)|G_n(u,z)| includes z=-1.
The complementary angular contribution, the spatial Jensen defect,
amplitude/full charge, H/support, Xi realization and actual-Xi
all-degree mixed positivity remain independent unpaid steps. Even a
successful positive arc does not settle their full-circle accounting.

## Reuse, failure comparison and the bounded test

Reuse the primary readings actually documented in
`2026-11-03-fixed-profile-spatial-jensen-defect.md` and
`2026-11-03-spatial-jensen-defect-arc-audit-scope.md` only where their
hypotheses match. Their Poisson-Jensen statements and logarithmic
integrability do not themselves provide the new growing-family arc
estimate. In particular a subharmonic compactness result in planar
area measure requires a separate justification for restriction to the
one-dimensional arc; the new review must inspect this distinction.

The preserved
`ATTEMPTS/2026-11-03-bounded-coefficient-angular-propagation-stop.md`
concerns propagation from exterior anchor values after discarding
correlations in an auxiliary coefficient model. It is a reason to
retain the exact response, not a global ban on angular estimates.
L723's accepted interior-circle peak is a materially different input.
The source review must search for duplicates and counterexamples to
the present local analytic implication, rather than repeat that
already stopped relaxation. No cross-notebook input is proposed.

Continue only after source comparison identifies adequate theorem
hypotheses or a precise bounded specialization capable of the fixed
positive arc threshold. A counterexample satisfying all proposed
local analytic hypotheses would stop that generic implication; it
would not refute the actual L666 family. Merely obtaining an
exponentially shrinking arc, an O(n) loss with no favorable constant,
or an Lp bound does not meet the threshold. Preserve all old stop
evidence. The source review is the sole next action; no new mathematical
claim or script has been produced for this nomination.

## Completed source comparison — 3 November 2026, step 204

### Exact local comparison

The main gap is actual-Xi all-degree mixed positivity. The intermediate
target remains the displayed fixed-arc threshold for the complete
response, as a possible lower contribution to the angular mean of
log S_n. The proof attempt is not permitted to assume that this local
contribution pays the complementary arc or the spatial Jensen defect.

Read L666's hypotheses and Section 2, L708's hypotheses/conclusion and
fixed-profile conventions, and L723's hypotheses/conclusion and Section 1.
Reused L723's supplied accepted status; no repeat audit was performed.
The two named earlier assessments supply their recorded primary readings.
L666 specifies a rational angular continuation with possible poles at
t_j*x/U and a/t_j, after cancellations; its unit-circle quadrature is
not an arc logarithmic lower bound. The intended local neighborhood
must be checked for this actual rational continuation, not for a model
with its denominators removed. L708's accepted cancellation near u=1/2
does not decide a logarithmic arc near u_*. The L706 arc concerns the
spatial norm-versus-mean defect. It is not the present signed-log trace.

The bounded-coefficient stop preserves its exterior-anchor countermodel.
It supplies no counterexample with L723's positive value on the proposed
arc. Conversely L723 is a limsup at one point, not a uniform rate on a
complex neighborhood or an eventual nonvanishing theorem. The new test
must preserve this distinction and one common subsequence. No theorem
from another notebook is used.

### New primary readings and their limits

Yu. Il'yashenko and S. Yakovenko, *Counting Real Zeros of Analytic
Functions Satisfying Linear Ordinary Differential Equations*,
J. Differential Equations **126** (1996), 87–105,
[Sections 1.1, 1.3–1.4, Lemmas 1–3, pp.93–99](https://www.wisdom.weizmann.ac.il/~yakov/jde-95.pdf).
These local lemmas do not require an ODE. For a bounded simply connected
Green domain U, compact K inside U and nonzero f analytic in U and
continuous on its closure, put M=max_cl(U)|f| and m=max_K|f|>0.
If rho=max_(a,t in K)|z_a(t)|<1 for the conformal disk maps z_a(a)=0,
Lemma 1 bounds the multiplicity count on K by log(M/m)/log(1/rho).
Lemma 2 requires f zero-free on the closure and bounds |f| on K below
by M*(m/M)^((1+rho)/(1-rho)). Lemma 3 allows zeros: outside disks of
total diameter <h<1, |f|>=m*(m/M)^(alpha-tau*log h), for positive
geometry-dependent alpha,tau. Read the complete proofs: Jensen with
zero-free comparison circles, Harnack, then division by all zeros in an
intermediate compact region, maximum-principle control and Cartan's
monic-polynomial estimate. No uniform small-arc asymptotic for alpha,tau
or integrated r(b)/4 conclusion is asserted by these statements.

A. Brudnyi, *On Local Behavior of Analytic Functions*,
[arXiv:math/9908105v1, 19 August 1999](https://arxiv.org/pdf/math/9908105v1),
Theorem 1.1, PDF p.2, Definition 2.1/Section 2/Remark 2.2, pp.5–6,
and Section 4's logarithmic-distribution proof, p.9. For f holomorphic
on the complex ball of radius r>1, a real interval I in the unit ball
and measurable E within I of positive length, the theorem gives
sup_I|f|<=(4|I|/|E|)^D sup_E|f| with finite D depending on f,r.
Definition 1.5 names the optimal exponent the Chebyshev degree; Remark
2.2 relates it to a suitable Bernstein index. The proof uses the earlier
local inequality [Br2]; that source was not separately inspected here.
The distribution/rearrangement argument concerns logarithms, including
zeros, but supplies no family-uniform small loss without exponent control.
Do not use Corollary 1.10's literal printed log(dimension) bound in
dimension one; its displayed normalization needs clarification. This
review relies on Theorem 1.1 only as a scope comparison, not that formula
or any sharpened dependence on the neighborhood/interval ratio.

### Reused inputs; why citation alone does not settle the target

Reuse the earlier assessments' precise citations to Ash–Novinger,
*Complex Variables* (2004), Theorem 4.8.3/Lemma 4.8.4, printed pp.33–36,
and Corollary 4.7.4, p.27, for disk Poisson–Jensen and its positive
kernel, with analytic continuation through the closed disk and a nonzero
interior value; their inspected proof explicitly allows boundary zeros.
Reuse Brunault–Zudilin, *Many Variations of Mahler Measures*,
Propositions 1.4–1.5, pp.6–7, and Issa–Lalin arXiv:1203.5379v1,
Remark 3.8/Theorem 4.1/proof, p.7, only for their stated finite-degree
root and logarithmic-integrability interfaces. These are not uniform
estimates for the growing rational family. No general theorem is to be
reproved merely to obtain a local lemma number.

The prior Sokal Theorem 1.5/Lemma 3.7 comparison is reused unchanged:
its fixed finite analytic exponential sum and dominance hypotheses have
not been verified for G_n. It supplies neither this trace estimate nor
permission to restrict planar convergence to the arc. No compactness
result is imported as a one-dimensional trace theorem.

The essential general tools are accessible. What remains is a bounded
mathematical specialization, not an essential unread theorem: use a
complex angular coordinate, verify a common pole-free neighborhood and
an exponential upper bound from the original finite products, and test
local zero-factor and zero-free harmonic estimates. Quantify their loss
relative to the L723 peak on a single subsequence. Any proposed
restriction-to-arc argument needs its own proof; finite-n integrability
alone does not justify a limiting logarithmic integral. No such
specialization, uniform upper estimate or trace theorem was derived here.

### Bounded search and continuation decision

Queries actually submitted:

- `holomorphic functions logarithm L1 convergence real interval subharmonic Cartan lemma`
- `analytic functions logarithm integral interval lower bound value center Cartan Remez Brudnyi`
- `subharmonic functions integral log interval lower bound small interval center value analytic`
- `Brudnyi subharmonic functions lower bounds local behavior logarithm integral interval Bernstein index`
- `"holomorphic" "logarithmic" "interval" "point" "lower bound" Remez`
- `"log" "subharmonic" "line segment" "convergence" L1`
- `"analytic" "logarithmic mean" "arc" "Cartan"`

Search leads on small-interval subharmonic estimates, pluripotential
inequalities and newer Bernstein theory were not inspected and are not
coverage. Search snippets were not used as theorem statements. One
redundant screenshot retrieval timed out; the complete relevant text
of both sources and all Lemma 3 proof pages was accessible. This is
not a source blocker. Full matching Mathlib coverage is not checked;
the supporting analytic tools do not establish a formalization of the
proposed transfer.

Decision EXPLORE, not IMPORT: no inspected theorem states this exact
growing-family threshold, and the constants needed to specialize the
known tools remain unpaid. There is no claim of originality. After
separate supervisor approval, one attempt may test the COVERED_TARGET.
Continue only with a justified fixed eta in (0,pi/10) and the displayed
limsup bound >=r(b)/4, or a more informative estimate with a quantified
remaining gap. Abandon the generic local implication if a counterexample
meets its full analytic hypotheses; that would not refute the actual
family. Shrinking arcs, log-plus estimates, unrelated subsequences or
an uncontrolled O(n) loss do not meet the test. Preserve partial reasoning
and require a refined mechanism before repeating an unproductive attempt.

Outcome EXPLORATION: one completed literature comparison, no new lemma,
mathematical script, counterexample, arc bound or mathematical exploration
attempt. PROOF.md and DAG.md do not change. The sole continuation and
its routing are recorded in PROGRESS.md.
