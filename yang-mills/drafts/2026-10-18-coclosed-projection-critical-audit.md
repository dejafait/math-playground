# L226 — separate critical audit, work record

Approved target: Assess whether L090's complete co-closed/co-closed rough-sector trace T_hh is O(N^(5/2) log(eN)^2) for both actual probes.

Reuse the unchanged ready EXPLORE assessment
`literature/2026-10-17-coclosed-sector-quantitative-remainder.md`.
This is one RESEARCH / REPRODUCTION proof_audit restricted to L226.
The main gap remains interacting reflected error <=c_box/2, continuum
axioms and finite positive mass. Intermediate target: verify L226's
uniform projection error, including the physical collar. Its downstream
use is the comparison needed to combine L228's bulk bound and L229's
boundary transfer with L225's mass removal. Other response rates and
interacting control remain independent gaps.

Acceptance test: check the complete transverse shell count for both
N sqrt(delta)>=1 and <1, the row-product estimate for matrices not
annihilating gradients, all projection occurrences and both generator
orientations before the entire heat sum. Acceptance requires the error
C_i[N^3 delta^(3/4)epsilon^(-1/2)+N^(5/2)sqrt(log(eN))]. A failed
placement or collar estimate withholds the comparison and records its
precise loss; it would not prove signed growth or disprove the target.

Essential inputs: L088 L089 L090 L225 L226; inherited L003 L009 L018
L026 L028 L085 L086. L225's mass-removal result is imported, not audited
in this step. L088's heat expansion and L090's relative spectrum,
coefficient estimates and actual generator are also imported. The new
audit checks their stated applicability to L226, without a recursive
audit. History/298 and /304 identify this as the pending separate check.
ATTEMPTS/029 and /030 retain the termwise-commutation and fixed-mass
warnings; neither route is reopened. No source refresh is needed.

The preliminary record above was saved before completing the checks.
The completed audit is canonical in
[L226, proof section 6](../lemmas/L226-coclosed-weighted-projection-error.md).
It accepts the uniform projection comparison relative to the stated
inputs. The full shell count, arbitrary-matrix row-product estimate,
positive collar comparison, both surviving curl placements and all
twelve projection replacements across the two orientations satisfy
the asserted error. The eight grouped telescoping terms account for
all twelve occurrences. No mathematical defect or stronger rate was
found; this is validation of an existing specialization, without a
novelty claim. No new lemma, script, DAG edge or proof-assembly change
is made. Mathlib coverage remains not checked.

Continue the exact approved sector target by separately critically
auditing L225's uniform mass-removal comparison. Check its complete
four-dimensional resolvent-difference shell sum, including masses
epsilon<N^-2, its staggered collar estimate and all four covariance
replacements in both original generator orientations before the full
heat sum. Acceptance requires
Tr(Delta_E J_epsilon^2)<=C N^4 epsilon and the resulting error
C_i[N^3 sqrt(epsilon)+N^(5/2)sqrt(log(eN))]; otherwise withhold
the comparison and record the failed estimate or exact loss.

Essential continuation IDs: L088 L089 L090 L225, with inherited L003
L009 L018 L026 L028 L085 L086. L226's accepted section 6 imports
L225 and does not audit it. L227--L229's accepted separate audits
likewise do not audit L225. Retain both actual probes, all relative
normal end rows, axial levels, component constant modes, coincident
plaquettes, both residual subtractions through L089 and the complete
external heat sum. No positive residual, coefficient commutation,
smooth upper extension or varying-mass fixed-parameter limit is
assumed. Independent complete-response rates, interacting reflected
error <=c_box/2, continuum axioms and finite positive mass remain
unresolved. Reuse the unchanged ready assessment; no new target or
assessment is selected, and no supervisor state is changed.
