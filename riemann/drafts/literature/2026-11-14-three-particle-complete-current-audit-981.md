# Complete three-particle current — audit nomination981

TARGET: Independently audit C466y's complete localized three-particle Stokes identity, checking the exact outer buffer, degree-three/four weighted minors, monotone-weight cutoff support and full collision/initial-diagonal flux at all intersections.
CHECKED: 2026-11-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse review980 and invocation-start assessment980's exact/stronger search and local duplicate/failure comparison; attempt981 checked C466x, C466u, C466t and closure979 and searched the same local route for the full-weight cutoff. No new external discovery, exhaustive absence or novelty claim.
SOURCE_EVIDENCE: Reuse TNV https://arxiv.org/pdf/1706.03822v2 AppendixB(B.1)-(B.5), p22; Teschl https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf Lemma2.14/Corollary2.15 p52, Theorem6.1/proof pp189-190; WKM https://arxiv.org/pdf/2008.10321v2 Section3.1(29), Theorem4/Proposition5 and complete proofs pp8-9, assessed in review980 for all needed exterior degrees. No new primary retrieval is claimed.
COMPARISON: The same compact-survivor ODE and arbitrary-k compound tools cover the exact unchanged class; C466x supplies the collective force estimate and pair spectra. C466y now writes the additional buffer, complete minors and full-weight cutoff proof; the inspected sources did not supply that stopped identity directly. This nomination is not an independent audit of the new proof.
GAP: Verify every load-bearing step and quantifier of C466y or isolate a precise error, especially interior support without a regular lifetime, fractional damping and the full four-form error across intersecting initial/collision loci.
REASON: Separate literature approval982 confirms that retained primary-source coverage suffices for the exact unchanged conceptual audit. Attempt981 supplies neither independent review nor a source theorem for its boundary identity; no fresh discovery or mathematical verification is claimed.
SCOPE: C466y's exact three-particle fixed-data statement only, with whole-B Hermitian M_1/M_2 bounds, unit-flat raw time, first maximal lifetime and sqrt(3)a+M_1 T_0<R; no symmetry, spacing restriction, unique endpoint, restart, trace, sign, global equality or actual-Xi hypothesis.

## Exact continuation and input qualifications

Read C466y's complete proof and the required C466x input passages.
Retain arbitrary holomorphic H on B={|z_j|<R} in C^3, H(0)=H_0,
||grad H||<=M_1 and ||D^2H||_op<=M_2 throughout B. Keep
Delta=product_(i<j)(z_j-z_i), F=Delta^2 exp(-H),
dot X=conjugate(grad(-2 log Delta+H)), X(0,u)=iu for distinct
u in (-a,a)^3, and the first maximal lifetime in B minus {Delta=0}.
The proposed result covers every chi in C_c^infinity(B), full
beta=Psi^*(chi F dz_1 wedge dz_2 wedge dz_3) and
gamma=Psi^*(dchi wedge F dz_1 wedge dz_2 wedge dz_3), with
coefficientwise zero extension to Q=(0,T_0) times (-a,a)^3.
It claims no first outer exit <=T_0, L^infinity coefficients and
d bar(beta)=bar(gamma), including triple/initial intersections.

C466x is the mathematical input for the triangle force inequality,
real symmetric pair spectra, weight identity and determinant/volume
comparison. Its audit979 is available; do not reopen its completed
mass-audit loop. C466u is only a method comparison. C466t remains
the obstruction without an outer buffer, not a refutation under it.
The primary tools and their hypotheses are already inspected in
[review980](2026-11-14-three-particle-complete-current-review-979.md)
and recorded in
[assessment980](2026-11-14-three-particle-complete-current-attempt-980.md).
No new source hypothesis or uninspected removability theorem is needed
to audit this direct cutoff construction. Any genuinely changed
target or newly essential source mismatch requires REVIEW_REQUIRED.

## Bounded conceptual test

Check the collective radial identity (9) and compact buffer (10)
without post-exit continuation or a bound on the full speed. Verify
the common-frame trace bound in degrees three/four and applicability
of the known compound inequality to velocity and parameter columns.
Check all coefficients in (18), the retained fractional damping
(19), and integrability of w_0^(3/4)||v(iu)|| at every initial
coincidence, with all constants and real/complex norm conventions.

The most delicate check is (21): a sequence in the nonzero cutoff
support must have its entire earlier paths in a single compact subset
of U, and this must force its limiting point to remain a survivor
without assuming any regularity of tau. Then verify the full ambient
d|F| wedge Omega calculation, the monotone-shell energy bound log2
including flat and truncated shells, the O(epsilon^(1/4)) full
four-form error, and the orientation and dominated limit in (26).
Do not replace the full differential by its time derivative, assume
independent pair coordinates, omit gamma, or infer sign from a modulus.

Continue only if the entire stated result survives. If a step fails,
preserve the precise error and distinguish a failed sufficient proof
from an admissible counterexample. This is an audit, not a second
proof attempt, extension of the hypothesis class or novelty assessment.
No numerical script is needed unless a concrete issue makes one useful.
Matching Mathlib coverage remains unchecked, not absent.

The main gap is still L030-L032/C032a actual-Xi all-degree positivity.
A validated identity could pay one intersecting-divisor boundary
step; actual-H realization, phases, global signed assembly and
all-order signs remain unresolved. No justified central creative
bridge is specified by this result; its essential conceptual review
takes priority over inventing one for scheduling purposes.

Nominate proof_audit/conceptual_audit, deep_research/xhigh, with
expected completed classification REPRODUCTION. Separate source-scope
approval982 is complete; the mathematical audit remains unperformed.


## Separate literature approval982 — 14 November 2026

LITERATURE_REASON: The supervisor requires separate approval of the newly
written audit nomination981; reuse review980 rather than repeat discovery
for the identical fixed-data statement.

Compared C466y's hypotheses, conclusion and imported-tools passage with
assessment980's exact statement, review980's primary hypotheses and proof
cases, and the retained rechecks965/976. This is source-scope comparison,
not an examination of C466y's estimates or proof. Teschl's compact
continuation is available only within the smooth open ODE domain;
TNV Appendix B concerns real initial variations with both Hessian and
variation conjugated; WKM Proposition5 covers continuous real variational
matrices and all exterior degrees, without a negative-measure assumption
for its upper bound. The cited versions, theorem numbers and primary URLs
in SOURCE_EVIDENCE are retained. No fresh external retrieval is claimed.

The audit's dimension-six, degree-three/four use lies within this recorded
source scope on compact survivor intervals. Its compactness, weighted
endpoint control, velocity-column applicability, shell estimate and
zero-extension passage remain explicit mathematical obligations. They
are not imported by this approval. No additional removability or trace
theorem is necessary for checking the proposed direct proof. HP and
Harvey–Lawson retain their recorded unmet hypotheses and comparison-only
status; their old access qualifications do not block this audit.

Reused review980's exact/stronger searches and duplicate comparison;
closure979 closes only C466x's completed mass audit. C466t still supplies
the no-buffer obstruction, while C466u has different single-divisor
hypotheses. The strict buffer and all intersection cases must therefore
be retained in the next audit. No new theorem, source overlap, failure,
novelty finding or mathematical advance is established in approval982.
Mathlib full matching coverage remains unchecked.

SPECIALIZE is retained solely as the gate for independently reviewing
the written specialization with known tools. The exact TARGET above is
approved for one conceptual audit, classified REPRODUCTION. Accept only
if every stated coefficient bound and distributional limit survives;
otherwise isolate the error without equating a failed estimate with a
counterexample. Do not repeat this approval or reopen the completed mass
audit. The main actual-Xi positivity gap and independent realization,
phase and global-assembly gaps remain unchanged.
