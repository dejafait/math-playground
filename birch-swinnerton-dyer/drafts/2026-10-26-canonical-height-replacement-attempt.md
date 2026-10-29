# Canonical cyclotomic height replacement — step 497 working record

Approved target: Repair L119's positive-rank regulator handoff by importing the Mazur--Stein--Tate canonical cyclotomic pairing, checking Harvey's scalar normalization and absolute precision while preserving the unresolved printed Stein--Wuthrich discrepancy.

Prior SPECIALIZE assessment: drafts/literature/2026-10-25-canonical-cyclotomic-height-replacement.md (separately approved in step 496). This is a mathematical specialization, not a new literature search or a reproof of canonical heights.

Main gap: rank versus arbitrary complex analytic order. Intermediate target: identify L119's matrix with a nonzero scalar multiple of the canonical ordinary cyclotomic pairing. Downstream use: supply the nonzero full regulator premise of L003, then the vanishing conclusion in L118. Test: retain the positive-rank claim only if the scalar, admissible-multiple extension, torsion/zero cases and absolute precision all match without new arithmetic hypotheses.

Reused source record: drafts/source-notes/2026-10-25-ordinary-sigma-normalization-review.md. Inputs are L119 (1)--(6), L001, L003, audited L118 and foundations/03/04. Duplicate/failure coverage is reused, especially step 494 and ATTEMPTS/057. The failed SW sign-only comparison is not reinstated.

Working calculation: q=-h_H=-2p h_MST. Since C(P,Q)=h_MST(P)+h_MST(Q)-h_MST(P+Q), L119's half-polarization gives B=p C. The scalar has valuation 1 and is nonzero. For any common nonzero integer n making P,Q,P+Q admissible, quadraticity and bilinearity extend the identity after division by n^2. Torsion is killed by some nonzero integer, so its quadratic height and all pairings vanish; zero is never evaluated by the sigma formula.

Keep the certificate in Harvey units. No division by p or by ell=log_p(kappa(gamma)) is needed for testing det H != 0. If a canonical C entry is actually produced by division by p, its absolute error exponent is N_ij-1; dividing additionally by ell costs v_p(ell). A determinant ball divides by p^k and loses k in its exponent. The final canonical proof must state these conversions explicitly.

No actual curve data, sigma implementation, finite Sha assumption, nondegeneracy assumption or complex-order comparison is supplied. The full mathematical argument will be written in L119; this working record is not a second canonical proof.

Completed: the full specialization is canonical in L119 (15)--(17), with
its foundations/04 convention update. The scalar/extension/precision test
passes in this attempt; no independent audit verdict is claimed. Outcome
ADVANCE / RESEARCH / REPRODUCTION is local interface repair using known
inputs. Prior failure evidence is preserved. The new audit-coverage target
is REVIEW_REQUIRED for a separate next-turn literature approval.
