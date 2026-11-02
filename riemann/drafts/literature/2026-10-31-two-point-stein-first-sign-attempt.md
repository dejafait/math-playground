# Two-point Stein route to the first Fourier Laguerre sign

TARGET: Attempt the monotone-Stein-to-first-Laguerre implication for positive even smooth rapidly decaying densities through a two-point Stein identity, stopping at a rigorous sign transfer or a precise uncontrolled oscillatory remainder.
CHECKED: 2026-10-31
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse the exact/stronger Stein, characteristic-function, real-zero and Laguerre searches in 2026-10-31-theta-stein-monotonicity-transfer-review.md; its full completed comparison was read this turn. The mathematical criterion and density hypotheses below are unchanged; no new search or novelty claim is made.
SOURCE_EVIDENCE: Direct primary PDFs rechecked 2026-10-31: https://arxiv.org/pdf/1804.03926v3 and https://www-users.cse.umn.edu/~bobko001/preprints/BD_Spherical.covariance.identities.pdf . The reused assessment inspected Saumard arXiv:1804.03926v3 Section 2 (5)-(6), pp. 3-4, and Theorem 6/full proof, pp. 9-10; Bobkov--Duggal author PDF Section 16 (16.4)-(16.8), pp. 34-35; Csordas arXiv:1309.0055v2 Theorems 4.1/4.2/4.5/4.6 and Open Problem 4.7, pp. 10-12; Bagnoli--Bergstrom 4 March 2004 manuscript Theorem 3/Corollary 2 and Appendix 8.2 Lemma 4, pp. 4,25. Exact URLs, hypotheses and edition qualifications remain in that assessment.
COMPARISON: The imported results give Stein identities, spatial shape facts and weighted variance bounds, without the requested pointwise Fourier Laguerre sign. L233 supplies a negative first sign, but C233b now certifies failure of its monotone-Stein premise. The criterion itself remains unrefuted and unproved; neither its truth nor originality is inferred.
GAP: Obtain a signed representation controlling every oscillatory term from Stein nonincrease alone, or identify the exact term that prevents that mechanism from deciding the sign; actual-theta applicability and higher signs remain independent gaps.
REASON: The fixed diagnostic has given a decisive negative. Attempting a sign-transfer mechanism for the already assessed unchanged criterion is materially different from varying that failed model, repeating a source search or citing a variance inequality as a Fourier theorem.
SCOPE: Only the generic first-sign criterion for strictly positive even smooth densities on R whose every derivative decays faster than every exponential, with tau nonincreasing on (0,infinity). A two-point use of the inspected Stein identity is the proposed proof technique, not a newly imported theorem. No parameter search, actual-theta calculation, stronger density hypothesis or all-degree claim is covered.

## Exact inputs and reuse

For such a density p define

\[
F(x)=\int_R p(u)e^{ixu}\,du,\qquad
\tau(u)=\frac{\int_u^\infty v p(v)\,dv}{p(u)}.
\]

Ask whether nonincrease of tau for positive u implies
\(F'(x)^2-F(x)F''(x)\ge0\) for every real x. This is precisely the
criterion compared in the completed
[transfer assessment](2026-10-31-theta-stein-monotonicity-transfer-review.md).
That file supplies the query record, direct primary-source links,
source versions, theorem hypotheses and inspected proof cases. The
[fixed-model assessment](2026-10-31-l233-stein-monotonicity-diagnostic.md)
supplies the separately approved Stein-definition applicability check.
No theorem beyond those inspected inputs is assumed. Unread leads in
the old comparison remain unread, and no absence theorem is asserted.

The exact negative comparison is L233, with C233b now deciding its
previously unchecked hypothesis. Neither is an affirmative premise for
the desired transfer. L019 is needed only for a future actual-theta
application and is not assumed to satisfy the new premise. No
cross-notebook input is proposed. Full-result Mathlib coverage remains
not checked.

## Bounded proposed attempt and main-gap relevance

Try a two-point use of the inspected Stein integration-by-parts
identity, with the aim of controlling the Fourier determinant's
oscillatory terms by monotonicity of tau. Write every resulting term
and justify every boundary limit and differentiation. Do not replace
a signed square by an absolute square or use the weighted Poincare
bound as if it signs a frequency-local quantity. The exponentially
decaying density controls polynomial moments and tails; any assertion
involving growth of tau itself still needs justification from its
defining product tau*p, not an unstated bound on tau.

The bounded test is whether one complete proposed representation
has a provably nonnegative total under exactly the stated hypotheses.
A positive identity would establish the generic first-sign implication;
an explicitly unsigned remainder identifies a mechanism obstruction,
not a counterexample to the criterion. An inconclusive manipulation
must be saved and stopped after this one attempt, without silently
assuming the desired Fourier sign or changing the model family.
Only a density satisfying all the premises with a certified negative
first sign could refute the criterion.

Downstream, a proved transfer plus an independently established
actual-theta Stein hypothesis would address the first Xi sign through
L233's actual-theta identity. The latter hypothesis and all higher
mixed signs remain open. Thus this is useful intermediate work with
independent gaps explicitly retained, not a proposed complete RH proof.

This is a proposed creative proof mechanism at the first-sign gap,
not a routine specialization of a stated probability inequality. Its
precise obstruction is the absence of a frequency-local sign transfer
from the inspected spatial Stein identities. Expected research
classification is POTENTIALLY_NEW, meaning only that the recorded
search did not establish coverage, with no originality certification.

The separate literature approval on 2026-10-31 retains EXPLORE for the
exact unchanged target. Direct source URLs and their qualifications are
recorded below. No two-point calculation, sign identity or approval of
newly derived mathematics was performed in this approval turn.


## Separate source-URL recovery and approval, 31 October 2026

LITERATURE_REASON: The supervisor requires a direct source URL in the ready assessment; this bounded review repairs that omission and checks the essential identity hypotheses without repeating the completed discovery search.

Directly retrieved [Saumard v3](https://arxiv.org/pdf/1804.03926v3),
Section 2, printed pp. 3-4, equations (5)-(6). The identity requires
connected density support, finite absolute first moment, integrability
of both terms and vanishing endpoint product. These conditions must be
checked for each test function; no bound on tau alone is imported.
The supplied density class is the unchanged proposed application, not
a new theorem established in this review.

Directly retrieved [Bobkov--Duggal, author PDF](https://www-users.cse.umn.edu/~bobko001/preprints/BD_Spherical.covariance.identities.pdf),
Section 16, printed pp. 33-35, Proposition 16.1 and (16.1)-(16.8),
including the Gaussian-characterization proof. The two-point identity
extends to locally absolutely continuous complex tests subject to the
two displayed absolute derivative-product integrals against the Hoeffding
measure. Finite second moment makes that measure finite. The
characteristic-function formula (16.4) excludes zero frequencies;
limits at zero require justification. The marginal identity requires
convergence and a positive density on its support interval. Retain the
existing qualification: Proposition 16.3's first-moment wording does
not authorize finite total marginal mass here. The author-copy edition
remains undated in the inspected passages. A screenshot of printed p. 34
timed out; its complete relevant text and the adjacent passages were
retrieved through the PDF text, so no essential source blocker remains.

These are identity inputs only. Their positive-measure and
positive-definiteness statements do not assert pointwise Fourier
Laguerre positivity. The earlier variance/shape comparisons and query
record are reused, with no expanded search or novelty claim. C233b's
fixed-model failure is preserved in its canonical file and
`ATTEMPTS/2026-10-31-l233-stein-monotonicity-model-stop.md`; the proposed
two-point mechanism is distinct and has not yet been attempted.

Approval: adequate source coverage for one bounded attempt on exactly
TARGET under SCOPE. Retain every oscillatory term and verify endpoint,
Fubini and differentiation conditions before invoking an identity.
A precise unsigned remainder stops this mechanism without refuting
the criterion. Actual-theta applicability and all higher signs remain
unresolved. No lemma or mathematical script changed; full-result
Mathlib coverage remains not checked. This is a process repair, not
new mathematical evidence or an advance beyond the inspected sources.
