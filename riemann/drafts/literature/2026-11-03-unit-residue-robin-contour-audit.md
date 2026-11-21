# Coverage nomination: critical audit of the unit-residue Robin contour

TARGET: Critically audit L689's unit-residue Robin contour, including the subtracted pole, all four finite edges, main-term lower bound and original-D comparison.
CHECKED: 2026-11-03
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 89 reused the ready inner-spatial comparison and finite-contour source records; read all of L689 and the relevant L661/L664/L666/L673/L681 statements and audit ranges; checked the origin and fixed-angle Taylor stops. No repeated broad novelty search.
SOURCE_EVIDENCE: NIST DLMF online Sections 1.10(iii)-(iv), equations (1.10.7)-(1.10.8), full coefficient/residue hypotheses and positive orientation read 2026-11-03; reuse Howell--Mathews online Sections 8.1 Theorems 8.1.5/8.1.7 and 6.2 Theorems 6.2.18-6.2.19 with complete proofs as recorded in the two-offset-anchor audit. Local audited input scope is compared below, not re-audited.
COMPARISON: The standard sources cover finite residues, simple-pole evaluation, circle coefficient extraction and finite path integral bounds. They do not prove the Robin logarithmic-derivative subtraction, edge constants, positive displaced main term or original-D comparison. These are the necessary family-specific application checks; no standard theorem is reproved.
GAP: Perform the exact critical audit of L689, retaining its artificial pole and every edge and matching the reused product/envelope hypotheses. Source coverage is sufficient; mathematical correctness and the full-cube/H/support/Xi gaps remain unresolved.
REASON: Separate coverage comparison is now complete for the unchanged nominated audit. SPECIALIZE permits one REPRODUCTION conceptual audit of the existing application, not approval of L689 or a stronger theorem.

The main gap is actual-Xi all-degree mixed positivity. L689's proposed
advance is only a lower norm certificate on L673's fixed-1/10,
full-support node family with every original residue one. It does not
cover L666's arbitrary independent shifts or use L681's auxiliary
positive weights as those residues. The audit should decide whether
that subfamily input can be retained, corrected, or withdrawn without
extending it to full-cube coercivity.

Read L689's complete proof, L681's exact simple-zero census and its
audit, L664 Section 3 and the corresponding audit paragraphs, L661's
general diagonal envelope, and L666/L673's exact definitions. Inspect
the already saved primary residue statements only as needed to resolve
a specific missing hypothesis; no source refresh is required merely
because this nomination is new. Do not rerun unrelated numerical
Robin-weight diagnostics or any mathematical certificate whose output
is not an input to L689.

The delicate points are the artificial pole at -rho in
Q'/Q-lambda-1/(z+rho), its sign and location, the two different
factorizations on the vertical sides, the exact phase on both
horizontal sides, and reuse of L664's finite-product estimates on the
same rectangle. Check n>=300, all constants and endpoint inequalities,
the positivity of F(-rho), and Cauchy mean extraction of c_0 from the
small spatial resolvent. The diagonal must remain the original D;
verify the positive exponent margin 1/48-91/5000 and every polynomial
factor. There is no numerical proof or script to replay.

Continuation/abandonment test: retain the stated subfamily result only
if all hypotheses and edges close; repair a local error with its exact
effect on the rate, or withdraw the unsupported claim. A failure would
not be a full-norm countersequence or a disproof of RH. L683's audit,
L657/L658's inherited qualifications, H/support, Xi realization and
actual signs remain independent. Full matching Mathlib coverage is
unchecked; the residue theorem's formal support alone would not certify
the new constants or the norm comparison.

## Completed source comparison — 3 November 2026, step 89

LITERATURE_REASON: Invocation-start REVIEW_REQUIRED requires a separate gate for the newly nominated L689 audit; unchanged rational-response and contour source coverage is reused, with a narrow coefficient-formula extraction to cover Cauchy mean evaluation explicitly.
SCOPE: Exactly TARGET as stated above, for L673's fixed-1/10 symmetric full-support unit-residue family, n=12q+3 and the stated finite n>=300 contour bounds and existential final onset; no arbitrary-displacement extension or audit of L683 is authorized by this assessment.

### Primary imports and precise application boundary

Reused the complete reading records in
`2026-11-02-two-offset-anchor-audit.md` (contour imports) and
`2026-11-02-discrete-robin-quadrature-audit.md` (standard import and
application boundary). Howell--Mathews, *Complex Analysis*, online
edition, [Section 8.1 Theorems 8.1.5/8.1.7](https://complexanalysis.org/web/sec_residue-thm.html)
requires a positively oriented simple closed contour in the relevant
analytic domain, finitely many interior isolated singularities and no
boundary singularity. The inspected proofs use excised circles and the
simple-pole limit. [Section 6.2 Theorems 6.2.18-6.2.19](https://complexanalysis.org/web/sec_contour-integrals.html)
uses a continuous integrand on a finite piecewise smooth path, bounding
the integral by the modulus integral and then length times supremum.
Those proof records are adequate and were not retrieved again.

Directly read [DLMF 1.10(iii)-(iv)](https://dlmf.nist.gov/1.10),
online text retrieved 2026-11-03, equations (1.10.7)-(1.10.8) and
all associated hypotheses and orientation clauses. Equation (1.10.8)
requires analyticity inside and continuity inside/on a simple closed
contour except for finitely many interior singularities, with positive
orientation. Section (iii) defines residue as the Laurent coefficient.
Equation (1.10.7) extracts coefficients on a positively traversed circle
lying strictly within the annulus of analyticity; for a function analytic
on a neighborhood of the closed disk, its Taylor constant coefficient
is the circle mean. This covers the precise standard input used for
L689's spatial evaluation, conditional on its claimed disk clearance.
No infinite-family limit or uniform-in-n convergence is furnished by
these statements. DLMF cites Copson (1935), pp.117-120 for residue
theory; that book passage remains unread and is not an additional input.
An optional Howell--Mathews Cauchy-formula URL failed in the web tool;
the inspected DLMF coefficient formula supplies the needed coverage,
so this is not an essential source blocker. No theorem from that failed
page is imported.

For the proposed F*Q'/Q integral, the audit must match the local zero
census, regularity of F and absence of boundary poles to (1.10.8).
For F/(z+rho), the audit must retain the interior pole and its residue
with the correct sign in the rearranged identity. It must also check
that the constant subtraction integrates to zero. These are ordinary
finite-contour applications requiring exact verification, not additional
unread source theorems. The elementary hyperbolic algebra and explicit
edge rates are local calculations rather than imported estimates.

### Local input scope, duplicates and recorded failures

Read L689 in full to delimit the audit, without certifying its claims.
Read L666's hypotheses/definitions and L673's hypotheses and node
admissibility; L681 Sections 1-2's census statement and the corresponding
Section 6 pole/census audit; L664 Section 3's full product estimates and
Section 7's product/grid/moving-side audit; L661's general envelope
hypotheses, conclusion and Section 2. L661 records L662's separate audit
of this envelope; no replay of its certificate was needed for coverage.
The finite-n restrictions, full j=0 product, angular convention, original
unit residues, pole clearance and original squared-residue D are essential
application hypotheses for the later audit. The prior auxiliary positive
weights are not the original residues. The new rectangle uses the same
moving height and product ranges but a different logarithmic derivative;
previous contour estimates do not by themselves audit it.

The ready `2026-11-03-inner-spatial-rational-response.md` assessment
already compares the exact norm target against rational observation,
norm conversion, power-sum and Cauchy-matrix sources. Its inspected
results do not certify this subfamily estimate or full-cube coercivity.
No new novelty search is warranted for auditing an already written proof.
The step-88 history and the narrow origin-closure and inverse-phase
Taylor ATTEMPTS records were checked: origin evaluation pays a different
exponential cost; the Taylor stop concerns a particular weighted
fixed-angle filter. L689's Section 1 also distinguishes the absolute
perturbation-kernel stop. None of these is an audit or a refutation of
this prescribed unit-residue signed contour. Their qualifications remain.

### Bounded decision and continuation

The main gap is actual-Xi all-degree mixed positivity at unbounded
height. The intermediate target remains exactly TARGET. If retained,
L689 would give a subfamily lower-norm certificate for the possible L683
transfer; that transfer is unaudited, and H/support and Xi realization
are independent. This is a source-coverage advance only, with no new
lemma, proof, calculation, certificate or originality claim.

One subsequent conceptual audit may reproduce the complete argument,
including the artificial pole, both vertical factorizations, both
horizontal phases, all n>=300 inequalities, real positive main term,
spatial disk regularity and the original-D envelope with every polynomial
factor. Retain the result only if those checks close; otherwise repair
the exact failing claim or withdraw its unsupported portion. A failure
is neither a full-cube countersequence nor a disproof of RH. No theorem
application has been verified by this literature gate itself.

Full matching Mathlib coverage remains unchecked. The supporting
contour theory is not a formal verification of L689's constants or
norm specialization. Classification for this literature step is
NOVELTY_UNCHECKED; the subsequent audit is REPRODUCTION under SPECIALIZE.
Mathematical exploration usage and supervisor state are unchanged.
