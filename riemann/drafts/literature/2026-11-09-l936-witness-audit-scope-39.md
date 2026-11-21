# Source gate for the algebraic witness audit

TARGET: Assess source coverage for a critical proof/code audit of L936's algebraic positive-flux witness, including real-root existence, common-mass membership, quotient inverses, all PSD/contact conditions and the strict flux sign.
CHECKED: 2026-11-09
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step40 reused step37's exact/stronger-result searches and compared the unchanged finite-class assessment, L936, relevant L874/L917 definitions and step38/39 failure records; reopened only two primary PDFs for singular-case applicability. No broad discovery or witness search.
SOURCE_EVIDENCE: Gallier author version24August2019 Proposition4.2/Theorem4.3 pp9-12 https://www.cis.upenn.edu/~jean/schur-comp.pdf statements and relevant singular proof cases; Curto-Fialkow1991 Theorem5.1 printed p625 https://www.math.uh.edu/~hjm/v017n4/0603CURTO.pdf statement, with singular proof coverage reused from step37; L874(2) and L917's hypotheses/log convention inspected locally.
COMPARISON: Standard tools cover verification methods, not the particular root, boxes, equalities or flux. L936 asserts finite-class membership only. Its claimed W positive definiteness must justify its inverse; singular N3 is allowed. No representing-measure converse or quotient irreducibility is needed if every used inverse and evaluation at the existing real root are justified.
GAP: Independently check the original arithmetic and real-root interpretation against every unchanged class condition and the strict positive flux. The producer's 114 checks have not been audited here; actual realization/tilt and the main positivity gap remain unresolved.
REASON: Essential source coverage suffices for one bounded proof/code audit. Construction-specific verification remains; no new general Schur, moment or algebraic-number theorem or reproof is needed. This literature-only review does not accept the witness.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED requests separate coverage comparison for the newly constructed witness audit; reuse ready step37 coverage and inspect only essential primary applicability.
SCOPE: Source comparison only in step40; no arithmetic replay, new lemma, mathematical script or witness/class modification. The exact later audit is nominated in 2026-11-09-l936-independent-witness-audit-40.md for separate next-turn approval.

The completed comparison reuses adequate coverage, distinguishes standard
inputs from original finite arithmetic, and nominates one independent
proof/code audit. Its proposed purpose is proof_audit/routine_audit,
standard/high: real-root IVT and elementary quotient identities,
principal-minor/Schur hypotheses, common-mass membership and exact
flux replay. A subtle unresolved embedding or singular-case issue
would justify conceptual_audit instead; none is assumed resolved merely
by this routing proposal.

Inputs to assess narrowly: canonical L936, L874(2), L917's hypotheses
and finite-log convention; `scripts/heat/contact-s7-root-slice-39.py`
and its full selected certificate records; the unchanged ready
assessment and its inspected Schur scope. L923 is optional bookkeeping
and a comparison, not a dependency. L019/L058 concern actual inclusion,
which the witness does not claim. No cross-notebook theorem is needed.
No full matching Mathlib coverage is claimed.

A later audit should validate the complete root polynomial/bracket and
actual arithmetic operations, not just repeat success booleans. It
should settle or pinpoint any discrepancy in canonical definitions,
all class conditions, and the strict lower flux bound. Do not search
for a new witness, change the panel/class, infer actual realization or
reopen exhausted sign mechanisms in that audit.


## Completed source comparison — step40, 9 November 2026

The main gap remains L030--L032/C032a actual-Xi all-degree mixed
positivity. The intermediate target is acceptance or precise rejection
of the existing finite-data witness. Acceptance would justify the stop
of this sufficient sign mechanism, leaving actual realization, extra
tilt relations, initialization/tangency, other panels/degrees and
global continuation open. Continue only if every original condition
and strict sign survives; otherwise preserve the discrepancy without
replacing the tuple or enlarging the class.

### Primary statements and applicability

Gallier, *The Schur Complement and Symmetric Positive Semidefinite
(and Definite) Matrices*, author version24August2019, Proposition4.2
and Theorem4.3, printed pp9--12, were reopened. For a real symmetric
block [[A,B],[B^T,C]], PSD is equivalent to A PSD, (I-AA^dagger)B=0,
and C-B^T A^dagger B PSD. The proof's null-space linear term explains
why the range identity cannot be dropped. L936 claims A=W positive
definite and scalar Schur complement zero; these claims must be
checked. Singularity of the full block is allowed. Neither an inverse
of singular W nor leading minors alone as a general PSD test is
licensed. This imports a standard criterion without reproof.

Curto--Fialkow, *Recursiveness, positivity, and truncated moment
problems*, Houston J.Math.17(4)(1991),603--635, Theorem5.1, printed
p625, was reopened. For real data gamma0,...,gamma_(2k+1), gamma0>0,
Stieltjes representation requires A(k),B(k) PSD and the extension
column in Ran A(k). At k=3 these are M3,N3 and (y4,y5,y6,y7).
Reuse step37's inspected singular proof cases via Theorem4.1 rather
than retrieve them again. Representation is outside the audit's
conclusion; no added range condition may change the original class.
This is a scope safeguard, not a source of a flux sign.

The intermediate value theorem and Sylvester's criterion are standard
named inputs. The audit must check the actual polynomial's continuity,
endpoint signs and scaling, and strict leading minors where positive
definiteness is asserted. Finite logarithms and quotient identities
are explicit elementary arithmetic in L936, not missing external
results. No assertion that the quadratic quotient is a field is
needed: interpretation at the real root and legitimacy of every used
inverse are the audit obligations. These specify checks without
performing them or establishing new identities.

### Local comparison, failed alternatives and read limits

Read L936 fully and L874's hypotheses, formula(2), and null-row
cancellation. L874's analytic derivative interpretation assumes an
actual family/contact; L936 uses only its named finite functional.
Read L917's arithmetic hypotheses, moment/log convention and saved
audit qualifications. The class uses complete saved rational endpoint
strings. Actual-family inclusion retains L917/L037's library contracts;
abstract membership establishes no actual parameter. No fresh
quadrature or library audit is needed for class membership as defined.

Reuse step37's inspected Laurent moment/feasibility coverage. No new
exact solver, measure reconstruction or stronger sign theorem is
needed for this explicit witness. No uninspected search hit is
imported. Mathlib matching/supporting coverage remains unchecked;
this is not Lean verification. No cross-notebook input is needed.

Read step38's midpoint failure and step39's route-stop history and
attempt records. The midpoint missed the original M12 box, so complete
common-mass membership remains essential. L921's different J test,
L922's inconclusive determinant enclosure and L923's S2=0 comparison
are already covered by step37 and do not validate this audit. No
historical stop is extended to stronger classes. Script function/output
locations were searched only to identify the audit material; neither
the producer nor its certificate was executed or validated.

SPECIALIZE covers standard methods plus construction-specific replay,
classified REPRODUCTION for the later audit. It imports no theorem
asserting the witness valid. The newly saved continuation receives
separate approval. This completed source step is EXPLORATION with
NOVELTY_UNCHECKED: readiness, not new mathematical evidence. PROOF and
DAG remain unchanged because the mathematical argument has not changed.
