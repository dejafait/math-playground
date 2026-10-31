# Boundary commutator obstruction — conceptual audit nomination

TARGET: Critically audit L529's boundary-packet commutator divergence, including killed-domain membership, the compact-resolvent remainder and every signed endpoint contribution.
CHECKED: 2026-10-30
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused 2026-10-30-l522-periodic-commutator-hypothesis-test.md and its failure comparison; searched "logarithmic Laplacian" "commutator" boundary periodic and "logarithmic Laplacian" "compact" "Dirichlet" Chen Weth on 2026-10-30. No matching signed killed boundary-packet theorem was inspected; no novelty inference.
SOURCE_EVIDENCE: Directly read Moller--Westrich arXiv:1006.0410v2 https://arxiv.org/html/1006.0410v2 Definition 1.1 and bounded-form criterion; Teschl GSM 99 (12 February 2009) https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf Section 2.2 (2.35)--(2.39), printed pp.62--63; Chen--Weth arXiv:1710.03416v6 (3 June 2019) https://arxiv.org/html/1710.03416v6 Section 3, (3.2)--(3.8), Theorem 3.1 and its complete two-case proof. Read L514 normalization/comparison, L515 bounded signed perturbation and L522 exact model; no full manuscript audit.
COMPARISON: The known criterion and periodic domain are reused; they do not prove L529's application. The new argument uses explicit seam packets and compactness of the full resolvent, not a periodic replacement or an unproved resolvent trace.
GAP: Source scope is approved for a separate conceptual audit of L529 (4)--(18); operator-domain membership, weak residual convergence, compact-resolvent remainder, two-sided expansion, boundary signs and equality atoms remain unverified application steps.
REASON: Separate literature approval now covers the unchanged audit target; standard inputs do not settle its signed killed application. Reuse this assessment next turn for mathematics; the obstruction remains unaudited.
SCOPE: Exactly TARGET for fixed 0<a<A and ell=2a>log(2), the full L522 operator and h(s)=s/(1+s^2). No nullvector existence, trace/nonresonance, H1 eigenstate, higher regularity, local Mourre estimate, sign, family rate or Xi transfer is assumed or concluded.

## Original nomination boundary (retained; approval below supersedes pending-source language)

The main gap remains actual-Xi all-degree positivity. L529 would
eliminate one concrete operator-regularity implementation; it does
not close L516/L522's missing upper sign. Its downstream use is
route selection rather than a positive arithmetic estimate.

Essential local inputs are L529's complete application proof, L514's
finite-energy/core-domain identification and L515's bounded signed
perturbation/self-adjointness argument. L522 fixes the measure,
including both prime shifts, equality atoms and the negative pole
density. The previous assessment
`2026-10-30-l522-periodic-commutator-hypothesis-test.md` supplies the
already inspected C1 criterion and generator. Reuse it unless the
audit finds a changed hypothesis or an essential unread source.

The decisive test is whether all four explicit packet families belong
to the killed operator domain and have bounded, weakly vanishing
(A_I-log(1/epsilon)) residuals. Compactness must then justify the
o(log^-2) matrix remainder for the actual signed resolvent. Finally
check the integration-by-parts sign and the positive constant from
the endpoint jump kernel, with every other term estimated or shown
zero under the stated fixed-data small-epsilon conditions. A formal
expansion, an L2 trace assertion or a finite-matrix preview is not
enough. The complete canonical proof is the evidence to inspect.

Continue only if the divergence survives these checks, or repair a
specific flaw with a complete argument. Otherwise retain the failed
claim and identify the exact missing estimate; do not promote the
result to an RH obstruction. Mathlib matching is unchecked. No
cross-notebook input is used. The requested audit is conceptual,
not a routine arithmetic replay or a candidate-RH audit.

No protected creative sign target follows from this operator stop.
The immediate blocker to a fresh nomination is the necessary review
of the new boundary obstruction; the actual signed estimate and
realization/transfer gaps remain independent. A later discovery step
should select a different, independently testable mechanism rather
than repeat this fixed regularization/generator.


## Separate source-scope approval, 2026-10-30

LITERATURE_REASON: The saved audit nomination was REVIEW_REQUIRED; essential
audit-specific domain coverage needed separate approval before mathematics.
This review approves exactly TARGET, without checking or repairing its proof.

### Inspected source scope

[Chen--Weth v6](https://arxiv.org/html/1710.03416v6), Section 3,
Theorem 3.1, assumes a bounded Lipschitz domain and gives smooth-core
density in its zero-exterior short-range energy space. Equation (3.2)
controls L2. Its proof first treats nonnegative data via boundary
cutoffs (3.8), using the killing-weight bounds (3.4)--(3.7), then
mollifies compactly supported data; positive/negative parts cover real
data. L514 records the complexification and kernel-norm comparison
for a bounded interval. Those are the specialization to retain, rather
than identifying the two multipliers. Density alone supplies no
operator-domain membership or endpoint trace. Equation (3.3) also
records compact embedding, citing another paper; that reference was
not followed and is not imported as an independent justification of
L529 (10)--(11). Audit its written Fourier compactness argument.

[Moller--Westrich v2](https://arxiv.org/html/1006.0410v2), Definition
1.1 and its following criterion, applies to bounded B and self-adjoint
D on complex Hilbert space: bounded extension of the displayed form
on Dom(D) pairs characterizes C1(D). For the audit, B is the bounded
real spectral function h(A_I); no domain invariance may be assumed
from that definition. The previously inspected higher-regularity and
Mourre theorem is not applied.

[Teschl, GSM 99](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf),
Section 2.2 (2.35)--(2.39), printed pp.62--63, distinguishes the
initial C1 periodic domain from its self-adjoint H1 periodic closure.
The adjoint calculation includes the endpoint pairing. The existing
interval-rescaling specialization changes only D, not A_I.

L515's bounded real-even signed-measure perturbation is the needed
local self-adjointness input. Its smoothing/renewal machinery and
L522's nullvector hypotheses are outside this test. L529 supplies
its own packet, compactness and remainder arguments; auditing them
is justified application work, not a reproof of the C1 criterion.

### Duplicate/failure comparison and decision

Reused the prior commutator review and the recorded boundary stop in
`ATTEMPTS/2026-10-30-killed-periodic-commutator-boundary-stop.md`.
The focused searches above gave no inspected matching theorem for
this full signed operator. Results on fractional-logarithmic, Hardy,
Ahlfors-space and extension operators remain unread leads, not inputs
or evidence of originality. They do not replace the saved exact audit.
No source-access blocker remains for that audit.

Decision: EXPLORE for the unchanged TARGET. Continue if the independent
audit verifies all four packet domains, bounded weak residuals, the
actual signed compact-resolvent remainder and positive endpoint
coefficient with both shifts and equality cases. Otherwise preserve
the failed step and qualify the stop; do not infer a favorable sign.
This is source readiness, not verification of L529 or mathematical
progress beyond the inspected literature. Mathlib matching remains
unchecked. No lemma, mathematical script, DAG or proof overview changes.
The essential audit still blocks a justified creative sign nomination;
no new mechanism is invented to meet the scheduling preference.
