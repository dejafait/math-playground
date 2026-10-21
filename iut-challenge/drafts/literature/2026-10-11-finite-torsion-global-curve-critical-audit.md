# L044 critical-audit coverage — completed source comparison

TARGET: Assess source coverage for a critical audit of L044's cubic approximation and exact embedded finite-torsion field preservation.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the ready finite-torsion assessment; narrowly searched L044, its working note, histories 138–140 and ATTEMPTS/027 for overlap and scope failures, then retrieved the primary theorem and required model/Picard passages. No broader discovery search was needed for unchanged hypotheses.
SOURCE_EVIDENCE: Bisatt–Dokchitser, Math. Ann. 381 (2021), 1439–1453, Theorem 2.2 and complete proof p.1441, https://doi.org/10.1007/s00208-021-02173-y, repository PDF p.3 https://d-nb.info/1235382842/34; Milne EC2 (2021), I.4 formula (6)/Proposition 4.10 pp.32–33 and (8) p.36, III.3 (23)–(26) pp.102–103, https://www.jmilne.org/math/Books/EC2.pdf; L042 and its separate audit retain the embedded local packet and full-coordinate convention.
COMPARISON: Inspected coverage applies to the unchanged Q_3 integral cubic and full m=210 Galois module, including 3-primary torsion. Model and pointed-group passages cover the remaining standard inputs; subgroup restriction and the fundamental theorem of Galois theory are the recorded elementary specialization obligations, not new constancy claims.
GAP: Coverage is ready, but L044 has not been critically audited. Check every cubic sign, convergence/integrality, nonsingularity including infinity, same-degree integer approximation, geometric genus/irreducibility, pointed Jacobian identification, restriction to the actual G_H and complete fixing-kernel equality.
REASON: Separate approval of the new audit target is justified by a theorem-by-theorem comparison with L044's actual hypotheses. It authorizes a later proof audit only; no mathematical verdict or new result is obtained here.
SCOPE: The fixed closure, q=3^30, k=Q(zeta_60), H and N of L042; the existential Q_3-model approximation at m=210 and subsequent restriction to H. No effective precision, general H-coefficient theorem, global rational 30-torsion or original IUT realization.
COVERED_TARGET: Critically audit L044's cubic approximation and exact embedded finite-torsion field preservation under the fixed L042 hypotheses.

LITERATURE_REASON: The supervisor required separate coverage approval for the newly saved critical-audit target. The prior ready construction assessment is reused; primary retrieval is limited to checking its fit to the written proof, including the genus input and the pointed Galois qualification.

## Source comparison and audit boundary

The main gap remains the original finite B>=A comparison. The intermediate
target is an independent audit of the different-curve finite-torsion
replacement in L044. A valid local replacement could support a later
global initial-data screen; it supplies neither that screen nor an
essential IUT flaw. This turn reviews sources, without reproducing the
cubic calculation or deriving the torsion-field equality.

Bisatt–Dokchitser Theorem 2.2, version of record published 2021-04-27,
was retrieved at repository PDF index 2 (printed p.1441), including
its entire short proof. It assumes a prime ell and a squarefree
polynomial in Z_ell[x] defining a hyperelliptic curve. For every
integer m>=1 a sufficiently close same-degree polynomial has
isomorphic complete Jacobian m-torsion as a G_Q_ell-module. Its proof
explicitly ensures squarefreeness in a same-genus family and cites
Kisin Theorem 5.1(1). Neither a prime-to-ell nor a good-reduction
assumption is imposed. The paper's other tame-torsion theorems are
not substituted for this local statement. Kisin remains uninspected;
import the published special case without reproof. No essential
source blocker remains for this audit.

Milne EC2 was retrieved at PDF indices 36–37, 40 and 106–107.
The Tate passages (23)–(26) fix the signs and series labels, state
integer coefficients and convergence for q in Q_p with 0<|q|_p<1,
and give the discriminant product. I.4 (6) supplies the smooth-plane
curve genus formula. Proposition 4.10's proof treats injectivity,
surjectivity and the group law of P -> [P]-[O]; the p.36 passage
explicitly makes this identification Galois-compatible when O is
base-rational. These are coverage inputs, not a verdict that L044
has checked its specific models correctly. The b_i series labels
must not be confused with general Weierstrass invariants.

The cited theorem concerns Jacobians, not embedded torsion fields.
The audit must check the pointed identifications before using it
on elliptic torsion. It must retain the actual subgroup G_H of
G_Q_3 in the specified closure, all subgroups killed by 30 and 7
inside the 210-torsion, and the pointwise action on every torsion
point. The standard fundamental theorem of Galois theory covers
comparison of finite separable coordinate fields via their fixing
subgroups. L042 already uses that convention and records its own
separate audit. Neither a chosen cyclic subgroup, an x-coordinate
field, equal degrees nor abstract field isomorphism replaces this
obligation. The next turn must inspect the full relevant argument,
not use this coverage approval as a correctness certificate.

## Overlap, failures and continuation test

The ready assessment
`drafts/literature/2026-10-11-finite-torsion-preserving-global-approximation.md`
already covers the same construction. Histories 139–140 distinguish
its coverage from its mathematical specialization; no separate
L044 audit is recorded. History 138 and ATTEMPTS/027 stop exact-curve
globalization, not preservation of finite torsion by a different curve.
The fixed-field stops ATTEMPTS/022,025,026 remain preserved as recorded
in L044 and the prior assessment; they are not reopened or rederived.
No cross-notebook theorem input is used.

Continue to the covered audit only if every model hypothesis and
complete embedded fixing-kernel claim can be justified. A failure
must identify a precise repair or stop; degree equality alone fails
the test. Essential inputs are L042, the published local-constancy
theorem and the model/pointed-group passages. L043 is a contrast only.
Global rational 30-torsion, the F/F_0 degree condition, selected-place
realization, native/actual input/action, pilot transport, essentiality
and the original finite B>=A remain unresolved assumptions or gaps.

Full matching Mathlib local-constancy/global-approximation coverage
has not been checked. No absence or novelty claim is made. No lemma,
mathematical script, PROOF assembly or DAG change is made this turn.
The newly ready audit continuation receives separate next-turn
approval before mathematical work.
