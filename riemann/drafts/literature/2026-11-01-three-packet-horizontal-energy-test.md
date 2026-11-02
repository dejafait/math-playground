# Three-packet horizontal energy — completed scope review

TARGET: Test E(Z)>=M(Z) for three conjugate packets with distinct real parts in [-2,2], depths in [0,2], and per-label multiplicities in {1,2}.
CHECKED: 2026-11-01
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the two-packet and finite-frequency assessments and scoped L612/L613 failure records; searched sinc/complex/conjugate energy inequalities, three-conjugate-packet inequalities, equal-real-part domination, horizontal multiplicity, and stronger finite-multiset bounds. Followed Lamzouri's v2 and the new consecutive-gap primary source below; no matching three-packet theorem or certified counterexample was identified. Search failure does not certify novelty.
SOURCE_EVIDENCE: Reused Lamzouri https://arxiv.org/html/2609.02882v1 Proposition 2.1/(2.4),(2.10)-(2.21) and BGST https://arxiv.org/html/2501.14545v3 (4.1), rechecking their statements; newly inspected https://arxiv.org/html/2609.02882v2 Proposition 2.1/(2.4)-(2.7), Remark 2.2 and added count proof cases, and https://arxiv.org/html/2610.26841v1 Section 2 hypotheses, Propositions 2.1-2.2 with their cluster/projection proof cases, and Proposition 2.3 statement.
COMPARISON: Known full-energy/simple-real and consecutive-gap bounds do not state this equal-real-part second-moment domination. C614a covers two packets only; reusing self-packet contributions for each pair needs valid accounting. No imported theorem or inspected obstruction settles the changed family.
GAP: Prove or rigorously refute E>=M for precisely the three-packet family below; arbitrary families, zeta weights, charge conversion, exceptional centers and Xi signs remain independent gaps.
REASON: The changed packet number required separate coverage; that comparison is now complete enough for one bounded mathematical test. Import the existing norm/Fourier identities and test only the missing domination, without asserting originality or reproving the known identities.
SCOPE: Fixed sinc kernel, three distinct real parts in [-2,2], depths in [0,2], per-label multiplicities in {1,2}, all ordered algebraic squares and coincident labels retained; no spacing lower bound, term deletion, general-family assertion or zeta realization.

## Exact proposed target and downstream use

Let x_1<x_2<x_3 in [-2,2], 0<=u_j<=2, and m_j in {1,2}.
The finite multiset has m_j copies of each label x_j+i*u_j and
x_j-i*u_j. At u_j=0 the labels coincide and keep their combined
multiplicity. Use K(z)=sin(pi*z)/(pi*z), with its removable value
K(0)=1, and all ordered pairs with multiplicities:

    E(Z)=sum_(z,s in Z) K(z-s)^2,
    M(Z)=sum_(z,s in Z; Re z=Re s) 1.

The square is algebraic. The proposed E>=M is unproved for this
target. No spacing lower bound, thin box, zeta realization or term
deletion is proposed. No mathematical test of this family took place
during the two-packet audit.

Main gap: actual-Xi all-degree signs at unbounded heights. A three-packet
test would probe simultaneous cross-packet interference, which a
two-packet result alone does not control. A general energy/count
comparison could later aid equal-ordinate moment estimates; its zeta
weight-removal and charge-conversion interfaces remain independent.

Essential inputs used in this literature turn are the unchanged
two-packet assessment, its finite-frequency primary-source comparison,
and L614/C614a with the completed audit. Preserve L612/L613's recorded
count-only/fixed-contrast stops and the incomplete first interval cover.
No cross-notebook input is needed. Full/supporting Mathlib coverage
for this changed target is not checked.

The nomination's review test was: inspect exact primary hypotheses for
any matching or stronger finite-family energy/count theorem, compare
multi-packet obstructions, and either approve this precise test or
record a source/blocking reason and choose an independently testable
target. A later rigorous E<M example would stop universal domination;
a proof would settle only this three-packet family. Sampling without
a certificate is not either verdict. The nomination did not authorize
mathematics; the completed comparison is recorded below.

## Completed comparison — 2026-11-01

This invocation performed source review only. It derived no new result,
ran no mathematical test and changed no lemma or mathematical script.
The original mathematical target and all its boundary conventions survive.

### Reused norm input and known local stops

The precise specialization in the ready two-packet assessment remains
valid without a packet-number restriction: use eta equal to the indicator
of [-1/2,1/2], lambda=1, and its normalized real-even L2 Fourier kernel.
The norm and Fourier pair are imported from Lamzouri v1 Proposition 2.1,
(2.10), and BGST v3 (4.1); there is no reason to reprove them.
Conjugation with equal multiplicities is essential. Algebraic pair squares
are retained even though the complete sum has a norm representation.
The cited proposition controls simple-real deficit and distinct elements,
rather than the second moment grouped by real part.

L614 and audited C614a are a local two-packet result, not a three-packet
theorem. No automatic pairwise summation is authorized. Preserve the
first interval cover's work-cap failure; it was neither a counterexample
nor a complete proof. L612's count-only saturation and L613's O(T)
fixed-contrast stop address different observables. They neither settle
nor ban this test. The finite-frequency and charged-pair source reviews
already compare GLSS's remaining gap integral, BGST's thin-box deletion
gate, and Aryan's negative mixed interactions; that coverage is reused.
Negative mixed terms alone do not refute an aggregate inequality.

### Updated simple/real counts

Youness Lamzouri, *A new proof that more than 2/3 of the zeros of the
Riemann zeta function are simple and on the critical line*,
[arXiv:2609.02882v2](https://arxiv.org/html/2609.02882v2),
8 September 2026, Proposition 2.1 (2.4)–(2.7), Remark 2.2.
Its hypotheses remain a nonempty conjugation-invariant finite multiset
and a normalized real-even compactly supported L2 window.
The additional conclusions bound simple-plus-real and simple-or-real
counts; (2.7) assumes E<=A|Z| with 1<=A<2. Inspected added proof cases
use the same nested projection ranges and scalar quadratic bounds.
Neither conclusion is a second moment grouped by real part. The energy
upper bound in (2.7) is a premise, not a consequence available here.
No additional count theorem is imported, and its proof is not independently
audited. Updating to this version does not settle the nominated inequality.

### Nearby triples in the consecutive-gap theorem

Youness Lamzouri, *Isolated zeros of the Riemann zeta function and zeros
of linear combinations of Dirichlet L-functions*,
[arXiv:2610.26841v1](https://arxiv.org/html/2610.26841v1),
19 October 2026, Section 2. Its window/multiset hypotheses agree with
those above. Proposition 2.1 requires tau>0 and
kappa_0=min_{|x|<=2tau}K(x)>=5/6 and bounds the number I_tau of real
points isolated from every other occurrence's real part by
I_tau >= (5/2)|Z|-(3/2)E. Read (2.8)–(2.31): nearby pairs/triples are
clusters of SIMPLE REAL points; repeated-real and nonreal contributions
enter separate projections, while (2.24)–(2.25) bound cluster norms.
These triples are not three arbitrary conjugate packets.
Proposition 2.2, k>=3 and kappa_0>=1-1/(2(k+1)), bounds good k-gap
blocks below by (k+3)|Z|/2-(k+1)E/2+O_k(1). Its cluster-collapse proof
retains the endpoint error. Proposition 2.3's small-tau statement retains
a nonreal correction and O(tau^2|Z|); only its statement was inspected.
None states E>=M. No gap-count theorem, limit in tau or hidden error-free
finite specialization is imported to supply that missing comparison.

### Bounded discovery record and decision

Queries included `"sinc" "complex" "energy" conjugate points inequality`,
`"squared sinc" "conjugate" inequality`,
`"sinc" "three" "conjugate" inequality energy`,
`"Lamzouri" "horizontal multiplicity" inequality`,
`"sinc" "equal real parts" inequality`, and
`"conjugation-invariant" "energy" "multiplicity" inequality`.
Searches did not identify an exact or stronger matching theorem or a
certified three-packet obstruction. Secondary discussions, unrelated sinc
applications and other research notebooks were not used as theorem inputs.
This is bounded coverage, not an assertion that the claim is novel.
No essential source for the fixed norm identity remains inaccessible;
the previously blocked stability lead is unnecessary and stays parked.

DECISION EXPLORE authorizes one separate attempt on exactly TARGET.
An exploratory numerical search must preserve full ordered multiplicities;
any proposed strict counterexample needs exact or directed certified
evaluation before it counts as a negative result. A full positive verdict
must cover all allowed parameters, including depths zero and arbitrarily
small positive real-part separations. A grid alone establishes neither.
If neither verdict is reached, save the unresolved region and discriminate
the mechanism before repeating. A certified E<M abandons universal
domination, not RH; success proves only this bounded family.
General extension, zeta weights, charge conversion, exceptional centers
and all-height Xi signs remain open. Full/supporting Mathlib coverage
for this target has not been checked; no Lean verification is claimed.
