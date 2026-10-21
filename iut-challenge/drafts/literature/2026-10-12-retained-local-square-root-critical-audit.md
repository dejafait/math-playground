# Retained local square-root specialization — critical-audit coverage

TARGET: Critically audit L054's two square-root memberships in unchanged H subset N, including full 2-torsion rationality, same-field Tate representatives, exponent parity and primitive-root order.
CHECKED: 2026-10-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused drafts/literature/2026-10-12-retained-local-square-root-membership.md; inspected all of L054 and the relevant L045 global/local torsion-set and L048 split-Tate passages; checked history/181–183 and ATTEMPTS/027,030 for duplicate audits and stops. No fresh external browsing was necessary.
SOURCE_EVIDENCE: Reuse inspected Milne, Elliptic Curves, second edition (2021), II.6 Proposition 6.3 pp.70–71 and III.3 pp.102–103 after (26), https://www.jmilne.org/math/Books/EC2.pdf; Kedlaya, Introduction: the Tate curve (fall 2004), Theorem 1 p.3 and discussion pp.3–4, https://kskedlaya.org/18.727/tate-curve.pdf. Primary statements and proof qualifications are recorded in the ready membership assessment.
COMPARISON: The inspected characteristic-zero torsion theorem and finite-extension Tate rational-point identification cover the imported inputs of this exact audit; full torsion rationality, exponent parity and primitive-root order remain elementary specialization checks, not uncovered uniformization or descent theorems.
GAP: No essential source gap remains for this narrow audit. Independent verification of the complete L054 specialization remains pending; graph/label, complete native base-field and selected/theta data and original finite B>=A are outside its conclusion.
REASON: Approve the newly proposed audit scope by reusing adequate unchanged theorem coverage; this source comparison neither rederives L054 nor certifies its correctness.

The essential inputs are L054 with L045 and L048, retaining the same
E_0, F, K, fixed embedding, F_u=H and K_w=N, full rational 30-torsion,
M>=max(M_tors,31), q_0 in Q_3 with v_3(q_0)=30 and the pointed
Q_3-defined Tate isomorphism. The earlier assessed theorem statements
are reusable; this file does not give the audit a ready verdict.

The next approval should check whether the existing precise citations
cover all audit obligations without fresh source retrieval. The later
audit must inspect the whole L054 proof, especially whether all four
geometric 2-torsion points are rational, whether representatives lie
in H, and whether exponent parity and exact root order are justified.
Continue if these arguments survive independently; repair or stop the
local claim if they fail. No field enlargement or stronger conclusion
is in scope. All native May 2020 source qualifications, parked graph
source blocker, ATTEMPTS/027,030 and remaining selected/theta,
input/action/pilot/essentiality and finite B>=A gaps remain intact.
Mathlib full matching coverage remains unchecked.

## Completed scope comparison

LITERATURE_REASON: The saved next target is a separate critical audit of newly written L054; compare its precise obligations with existing ready coverage once, without repeating source retrieval.
SCOPE: Exactly TARGET, with unchanged L054 hypotheses and direct mathematical inputs L045,L048; an independent audit may verify or repair its elementary specialization but may not enlarge fields, reselect the curve or infer native graph/label, complete initial data or a numerical comparison.

The proposal paragraphs above retain the selection history. This completed
comparison supersedes their pending-approval language, but not their
requirement for a later independent mathematical audit.

The main gap remains original finite B>=A and actual input/action/pilot/
essentiality. The intermediate target is correctness of L054's two
same-field memberships. Their downstream use is a limited local
prerequisite check in the retained packet; independent global and native
conditions may remain unresolved.

### Coverage mapped to audit obligations

Milne II.6 Proposition 6.3 applies to geometric n-torsion with n prime
to FIELD characteristic. Both algebraic closures used in L045 have
characteristic zero. Its previously proved full-set identification
is the relevant input for the audit of all four local 2-torsion points;
checking only selected points or a cyclic subgroup would be insufficient.
The audit must check L054's application to the same reselected curve
and its embedded completion, rather than reprove the torsion theorem.

Milne III.3 following (26) states the group identification
E_q(L)=L^*/q^Z for finite L/Q_p, q in Q_p^* and |q|_p<1.
L048's retained q_0 and pointed Q_3-defined isomorphism are in that
scope, and H is a finite extension of Q_3. This exact statement covers
same-field representatives, so an additional theorem identifying fixed
representatives from fixed geometric classes is unnecessary. Kedlaya
Theorem 1 gives corroborating Galois-equivariant surjectivity and kernel
coverage. Its proof discussion defers surjectivity to Silverman,
Advanced Topics (1994), V.3.1 and V.4; those sections remain unread.
Importing the named Tate theorem suffices. Retain the prior handout
coefficient-display warning and Milne's standard equation.

The audit obligations involving exponent ambiguity, parity, the number
of classes on each parity branch, and exact order of the primitive
root's power are finite elementary algebra within these imported
statements. No additional analytic, Hensel, native graph or globalization
theorem is being approved. This comparison classifies the obligations;
it does not execute them or give an independent correctness verdict.
Full matching Mathlib coverage remains unchecked, not asserted absent.

### Duplicate and stop comparison; discriminating test

History/182 already approved membership theorem coverage; history/183
records the specialization and proposes, rather than completes, its
independent audit. The reviewed nearby records contain no completed
audit of L054. ATTEMPTS/027 concerns the old exact q=3^30 curve and
ATTEMPTS/030 the rank-two multiplication cover. Neither decides these
two local memberships or licenses any stronger conclusion. Preserve
the native graph-source blocker and all prior stops.

Continue to the independent audit with L054,L045,L048 and established
L042,L044–L047 inputs, same E_0,F,K,Omega,H,N,u,w, full rational
30-torsion, M>=max(M_tors,31), F_u=H,K_w=N and v_3(q_0)=30.
Neither K=N nor q_0=3^30 is assumed. Continue if all four torsion
points, same-field representatives, parity and root order survive
independent checks. Repair a failed local inference; required field
enlargement defeats the unchanged-field claim. An essential source
mismatch requires narrow renewed review. Passing settles only the
local claim, leaving native May 2020 qualifications, complete
base-field/selected/theta data, graph/label and input/action/pilot/
essentiality and finite B>=A unresolved.
