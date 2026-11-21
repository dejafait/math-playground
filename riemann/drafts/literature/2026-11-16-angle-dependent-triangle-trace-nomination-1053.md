# Angle-dependent vertex trace and zero flux — nomination1053 / review1054

TARGET: Test whether C467p's h=0 trace extends to a bounded adjoint on C467k's actual j=0 triangle with angle-dependent vertex trace, initial value f(x)^3, four complex weighted derivatives in L1 and zero vertex flux in the complete cutoff identity.
CHECKED: 2026-11-16
DECISION: EXPLORE
SEARCH_EVIDENCE: Separate review1054 searched characteristic zero-flux transport, BV initial-boundary problems and weighted divergence-measure product rules; compared scoped reverse/triangle reviews and stops, reusing reviews1046/1050/1052. No inspected theorem solves or excludes the unchanged angle-dependent test; bounded search is not a novelty claim.
SOURCE_EVIDENCE: Reuse reviews1046/1050/1052's primary comparisons. Fresh reads: Crippa–Donadello–Spinolo revised author manuscript boundary310.pdf, Thm1.1, Lemma3.3/Def3.4 and Prop3.5 with relevant proofs; Crippa–De Rosa–Inversi–Nesi arXiv HTML labelled2405.11486v2, Def1.3/Thm1.4, Prop3.1/Cor3.3–3.4 and proofs, Thm1.6/Remark1.7, Thm4.5 and Cor4.6. Exact URLs, version qualifications and applicability below.
COMPARISON: Flux-trace and weak-solution theorems do not prescribe the selected entire edge, joint parameter continuity or four separate complex weighted derivatives. C467q excludes a single physical vertex value; it cannot exclude the new angular trace. No theorem is applied to the original field without verifying its hypotheses.
GAP: Construct the unchanged actual-data test with its entire prescribed edge, continuous angle-dependent parameter trace, four complex weighted derivatives and full arbitrary-rate zero-defect identity, or prove incompatibility in precisely that class. These are mathematical obligations; no essential source-access blocker remains.
REASON: Literature-only review1054 completes the essential changed-vertex comparison and permits one bounded creative attempt at the existing TARGET. No new result, adjoint, derivative estimate, flux limit or lemma is derived; the nomination itself did not approve its mathematics.
LITERATURE_REASON: The vertex trace no longer descends to a single continuous value on the physical collapsed triangle. This changes an essential hypothesis outside ready review1052 and review1050; weighted flux/trace coverage for this exact class must be compared separately, reusing adequate existing sources.
SCOPE: Actual n=3 j=0 triangle, R=1/4, a=1/16, T0=1/1920, b=1/4096, X=1/256, original B/beta/H/H0/F, raw time, common minus sign, fixed bump and selected C467p(33)-(35) edge test. Change only the vertex identification requirement, with the zero-flux obligation explicit.

## Proposed bounded test; no mathematical result

Keep the map Z0 of C467k and review1050, with 0<=r,lambda<=1.
Seek a real psi, 0<=psi<=1, continuous on the *parameter* box
[0,tau] x [-X,X] x [0,1]^2 for one common positive tau. Retain

    psi(0,x,r,lambda)=f(x)^3,
    psi(t,x,1,lambda)=phi_p(t,x,1-2lambda,0),

where phi_p is the selected C467p(33)–(35) test and f is the same
fixed bump. Require positive-time interior smoothness for 0<r<1,
including lambda=1/2 and the original x/lambda endpoint neighborhood
extensions. Do not require derivatives at t=0 or r=0 or r=1.

In this changed class psi(t,x,0,lambda) may depend on lambda.
It therefore need not define a continuous scalar on the physical
collapsed vertex. Its continuous parameter trace is still required;
there is no permission to select arbitrary measurable traces elsewhere
or alter the initial/outer-edge data. No proposed formula for this
angle-dependent trace has been proved here.

Impose dpsi wedge Re(-Z0^*Omega)=0 in the same interior, with the
original divisor zeros. For C467k(17)'s unmodified complex coefficients
require absolute integrability on the entire parameter box of

    |A psi_t| + |U psi_x| + |B psi_r| + |V psi_lambda|.

Require the full complex C467k(20) tested identity to pass from
epsilon<=t<=T, eta<=r<=1-zeta to the full domain for arbitrary
independent epsilon,eta,zeta tending to zero. All time, x, angular
and outer radial faces remain. In particular the original r=eta
face integral of psi B must tend to zero with those independent
cutoffs; no vertex distribution or unaccounted corner term is allowed.
The common minus sign changes all terms together. Zero flux and
weighted derivative control remain obligations, not consequences
asserted in this nomination. Reuse the already proved bounds in
C467k(19) when assessing what remains; do not reprove them as new work.

Continue only with an actual function satisfying this whole test or
a precise incompatibility in this class. A failed sufficient estimate
or ansatz is inconclusive. In particular C467q's equation for one
angle-independent vertex value may not be imposed on the new trace.
The test concerns one selected triangle/edge; it does not assume the
other five triangles, their mutual matches or exterior flux payment.

## Relevance, inherited evidence and separate gate

The main gap remains L030–L032/C032a actual-Xi all-degree positivity.
The potential mechanism is to transport the bump using an adjoint
on the parameter space whose angular vertex values differ, while
proving that the original vanishing current gives zero vertex flux.
This may permit one local edge match without the now-excluded physical
vertex continuity. That possibility is unproved; global signed
assembly, all interfaces, exterior payment, realization and other
degrees remain independent gaps even if this test succeeds.

Carry C467e/audit1017's regular coefficient flow, C467k/audit1033's
actual triangle and coefficient bounds, and C467p/C467o/audit1049's
selected edge test and qualifications. C467q/audit1053 supplies the
precise stopped class and reason for changing it; its L018/C466a
external-zero qualification is preserved, not independently certified.
Use C467l/m only where the pair trace construction requires their
estimates, with their audits1037/1041. Preserve stops1000/1009/1023/1043
and stop1051/audit1053. Full matching Mathlib coverage is unchecked.

The next turn is literature_comparison, standard/high, for this exact
TARGET. Reuse the primary statements already inspected in reviews1046
and1050; extract only essential missing hypotheses/proof cases for
angle-dependent traces at a zero-current boundary and the prescribed
whole edge. This nomination does not claim those sources cover it.
If ready comparison permits a genuinely new mechanism, prioritize one
proof_attempt/creative with a bounded test as above. Its proposed
escalation is the audited angular-drift obstruction to a single vertex
value, which prevents this local signed assembly ingredient; decisive
evidence must be an actual matched weighted adjoint with the full
zero-defect identity, or an obstruction surviving the changed trace.
The separate review must choose final research routing and may identify
a known specialization instead. No creative attempt or approval occurs
in this audit turn.

## Separate source comparison1054 — 16 November 2026

The nomination and its test above are preserved. This section is the
separate literature gate, not a mathematical attempt or an extension of
the continuous physical-vertex stop.

### Search, overlap and ready coverage

Fresh queries were `"transport equation" "characteristic boundary"
"zero flux" trace continuous`; `"Initial-boundary value problems"
"BV coefficients" Crippa Donadello Spinolo`; `"divergence measure
fields" "weighted" "product rule" continuous gradient`; and
`"Normal traces and applications to continuity equations" 2024`.
The exact target, its standard transport/normal-trace terminology and
stronger weak-solution conclusions were compared. No adequate matching
theorem was located; this is not evidence of originality.

Scoped searches of November15–16 reverse assessments and November16
triangle attempts/histories found nomination1053 and the stopped
physical-vertex class, not an earlier solution of the changed test.
Read C467k's original (17)–(20), C467p(33)–(37) and C467q's exact
hypotheses, (11)–(16) and audit1053's successive-limit argument.
Review1050 already compares stops1000/1009/1023/1043; audit1053 supplies
the new stop1051. Their hypotheses remain distinct. The old stops are
not applied to the new angular trace, and the valid pair result is kept.

Reuse review1046's primary Boyer Thms3.1/4.1, Chen–Comi–Torres
Prop3.1/Thms3.2/8.4 and Arlotti–Banasiak–Lods Thms3.6/4.2
comparisons. Those require, respectively, appropriate Sobolev velocity,
unweighted Sobolev/BV test control or a regular invariant flow; the
weighted products nominated here have not been identified with those
hypotheses. No new Sobolev/BV upgrade is asserted. Reuse review1050's
Iyer regular-chart characteristics, Imagawa–Kawagoe graph-space inflow
theory and Calvo–Hingant–Yvinec half-line flux comparison. None of
those recorded conclusions includes this entire prescribed edge.

Review1052's Teschl ODE and de Boor interpolation coverage remains
ready within its stated domains. A later characteristic construction
must verify its own open chart, continuation, spatial variation and
boundary-hit compatibility. Smoothness in sqrt(t) alone does not give
a smooth physical-time flow at zero. These sources need no repeated
retrieval for their unchanged supporting statements.

### Fresh primary comparisons

**Crippa–Donadello–Spinolo**, *Initial-boundary value problems for
continuity equations with BV coefficients*, J. Math. Pures Appl.102
(2014),79–98, DOI10.1016/j.matpur.2013.11.002;
[revised author manuscript, pp2,9–14](https://cvgmt.sns.it/media/doc/paper/2119/boundary310.pdf).
Theorem1.1 assumes uniformly Lipschitz boundary, bounded b,div b,c,f,
and b in L1_loc([0,T);BV(Omega_*)) for every bounded open
Omega_* subset Omega, not only relatively compact subsets. Bounded
initial/inflow data give a unique bounded distributional solution.
Definition3.4 prescribes Tr(bu)=g Tr(b) only where Tr(b)<0.
Under these hypotheses Proposition3.5 gives strong L1 convergence of
normal flux traces on Definition2.3's moving graphs.
Read Lemma3.3's zero-extension trace proof, section3.3's
renormalization/Gronwall steps and all three Proposition3.5 proof
steps, including squared traces and BV control of the intervening
strip. Existence's parabolic approximation is referred to [11]; that
external proof was not read here. These conclusions do not construct
the nominated continuous adjoint or its four coordinate products.

**Crippa–De Rosa–Inversi–Nesi**, *Normal traces and applications to
continuity equations on bounded domains*,
[arXiv HTML labelled2405.11486v2, §§1.1,3.1,4](https://arxiv.org/html/2405.11486v2).
For bounded Lipschitz Omega and bounded u with finite-measure
divergence, Theorem1.4 identifies an existing normal Lebesgue trace
with the distributional trace. Definition1.3 requires local averaged
absolute normal-component convergence for every shrinking sequence.
Corollary4.6 assumes bounded u in
L1_loc([0,T);BV_loc(Omega)), div u=0 and zero normal Lebesgue
trace almost every time. Bounded initial data give a unique bounded
distributional transport solution and renormalized zero-boundary-flux
identity. Read Proposition3.1's four-term proof, Corollaries3.3–3.4,
Theorem1.4's cutoff proof, and Theorem4.5's interior/inflow/outflow
proof cases. Remark1.7 separates existence from uniqueness.
These results do not assert pointwise parameter continuity, prescribed
outflow values or separate coordinate derivatives. The retrieved HTML
labels v2,17June2024 but displays24August2026; only that rendered
text is assessed, not an independently checked publisher version.

Access qualification: the Basel2024 PDF retrieval failed; the primary
arXiv text resolved the relevant lead. The publisher XHTML also failed
in the reader and is not cited as inspected. No essential blocked
source remains. Other search hits, including numerical, scattering
and secondary summaries, are unread leads and supply no coverage.

### Applicability and the bounded mathematical gate

The new source comparison is not a theorem application. No
normalized parameter velocity with the cited global regularity and
divergence properties, or an identification of its inflow/outflow,
has been verified on the entire original box. In particular, the
triangle's original complex current and a normalized real transport
velocity must not be conflated. A zero normal trace in a source theorem
is not permission to choose the nominated whole-edge data arbitrarily.
The parameter box retains different values at a collapsed physical
vertex; it is not a continuous scalar on that physical triangle.

C467k(19) supplies already-proved original coefficient bounds, not
unknown-test derivative estimates. Its smooth-test identity cannot
simply be asserted for the new test class. The later attempt must
justify passage through each cutoff, all four complex products, the
original divisor zeros and every face of (20), including the r=eta
term for arbitrary independent cutoffs. No consequence about the
vanishing of that term is derived in this literature turn.

Decision EXPLORE: adequate essential source comparison is now complete
for exactly the saved TARGET, with no matching theorem to import and
no source-established incompatibility. No standard theorem needs a
reproof. Full Mathlib matching coverage is unchecked; prior supporting
ODE/Stokes/DCT coverage does not establish this target.

The next turn may perform one proof_attempt/creative at this unchanged
test: retain the angular parameter trace instead of identifying it at
the physical vertex, and seek a matched actual adjoint or a precise
incompatibility surviving that change. This is a proposed mechanism,
not a formula or proof. Decisive positive evidence is one function on
a common positive interval meeting the entire nominated test, with the
full complex independent-cutoff identity. Decisive negative evidence
excludes this exact class. A failed sufficient estimate, ansatz or
regular-chart extension is inconclusive and must be saved as such.

The relevance is one local matched component toward
L030–L032/C032a; other triangles, mutual interfaces, chamber matches,
exterior payment, realization, other degrees and Xi signs remain open.
Carry C467e/audit1017, C467k/audit1033, C467p/o/audit1049 and
C467q/audit1053, with C467l/m audits1037/1041 where used. Retain
L018/C466a's unreplayed external first-zero qualification. No complete
candidate, lemma, mathematical script, PROOF.md argument or DAG edge
is changed by this review.
