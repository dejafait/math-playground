# L504 clipped strip-Poisson residual: approved critical audit coverage

TARGET: Independently audit L504's clipped strip-Poisson residual obstruction, including the Fourier normalization, positive boundary measure, smooth Fourier tests and uniform norm lower bound.
CHECKED: 2026-10-30
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse the exact-class searches and duplicate/failure checks in drafts/literature/2026-10-30-signed-gap-flux-conditional-bound.md and the approved dual-test assessment; this audit preserves that family and the same quantitative residual question. No matching conditional theorem was found and no originality is inferred.
SOURCE_EVIDENCE: Brevig--Chirre--Ortega-Cerda--Seip, https://arxiv.org/pdf/2210.13922v2, (3.3), Theorems 3.6 and 3.10, Corollary 3.9, printed pp. 12--15; ABR, https://axler.net/HFT.pdf#page=124, second edition, 17 July 2020, Theorem 6.13(a)/Corollary 6.15, printed pp. 119--120. Parent coverage reused; this separate approval retrieved the primary normalization, Corollary 3.9, Theorem 3.10 with its endpoint paragraph/proof, and ABR 6.13(a)/6.15 with their measure-case proofs. These remain comparisons, not premises of L504.
COMPARISON: Known evaluation duality warns that a formal residual need not be bounded, while the positive Poisson representation requires domain positivity. Neither source proves the clipped functional's growing norm. L504 gives an explicit continuum functional and smooth full-space tests; auditing these local claims needs no new external theorem.
GAP: Independently verify or repair L504's exact representation and lower bound c_R L^(R/4)/a^2, and ensure the conclusion stops only its particular full-space norm certificate, not the conditional inequality on the positive cone.
REASON: The new negative result could otherwise prematurely exclude a useful certificate. Separate source-scope approval is now completed for the conceptual audit of its clipping factor, admissible tests and moving-geometry quantifiers. This approves the audit target, not the proof or its claimed obstruction.
SCOPE: Only L504's stated obstruction for fixed R and its comparison with the O_R(a) residual threshold; no new detector, new measure, L503 audit, arithmetic application or conditional counterexample. Separate literature approval completed 2026-10-30; the exact TARGET is ready for a later mathematical audit under EXPLORE.

## Exact audit task and bounded test

The target is the new result in
`lemmas/L504-clipped-strip-poisson-dual-residual-obstruction.md`.
It uses no local theorem as a premise. L503 is prospective downstream
context only and remains unaudited; L502 is not an input. No cross-notebook
theorem, zero-free estimate, zero spacing or simplicity is assumed.

Check the strip kernel's sign, mass and angular transform, the 2pi
frequency conversion, the y=b boundary limit from the unchanged
rectangle hypothesis, absolute convergence at the integrable density
singularities, and the plus sign of the positivity-supported measure.
Check the complete residual identity, the clipped half-factor on a
resonant cosine and the two-integration-by-parts tail with constants
independent of b. Do not treat the cosine as an admissible L1 test.

Independently verify that h(z/a^2)cos(sz), with the specified resonant
s, has a smooth Fourier transform supported in [-R,R] at every
sufficiently large real T. Compare its exact N bound and its uniform
compact approximation error with the claimed exponential main term.
Track fixed-R onsets and verify the divergence relative to a. Distinguish
full-vector-space norm tests from the rectangle-positive admissible cone;
only the former are asserted by the proof. No numerical test is required
unless the analytic replay exposes a specific unresolved calculation.

Pass only if all these checks support the stated scope; otherwise save
the precise failure and repair the canonical result or narrow its
conclusion. The conditional flux inequality, nonvanishing detector cost,
negative actual-zero contributions, moving-test transfer and actual-Xi
initial signs remain independent. Mathlib matching coverage is unchecked.
At nomination no new literature was fetched and no theorem was approved;
the separate source-scope review below completes approval of this exact
audit target without checking its mathematical conclusion.

## Separate source-scope approval: 2026-10-30

LITERATURE_REASON: The newly nominated L504 audit, unlike the prior certificate-construction target, still required the supervisor-mandated separate approval; reuse the completed searches and check the primary endpoint/domain qualifications against the actual canonical statement, without reopening discovery.

Read L504 in full solely to identify its hypotheses, claimed conclusions
and source needs. Read the parent conditional-bound and dual-test reviews,
the clipped-measure attempt record and its dated history. The targeted
first-mode failure references confirm that the earlier stop concerns a
different absolute-norm closure. No sibling notebook was read. L503 is
context, not a premise, so its outstanding audit does not block this one.
This is source comparison and task approval, not a replay of equations
(5)--(18), an audit pass, a new derivation or a fresh novelty search.

The primary Brevig et al. v2 PDF, printed pp. 14--15, was retrieved for
the angular Fourier convention, distributional matching and complete
Theorem 3.10 proof. Its p=1 paragraph allows an unbounded residual
functional; the proof uses Schwartz tests, Holder and density. Thus a
formal representative is insufficient. The result concerns origin
evaluation, not the clipped functional or its moving geometry. Parent
coverage of (3.3)/Theorem 3.6 is reused without re-reading it.

The primary ABR PDF, printed pp. 119--120, was retrieved for 6.13(a)'s
measure representation and weak-star/Poisson-limit proof, and 6.15's
positivity and mass argument. Positivity is assumed on the whole ball.
It does not cover a signed gap outside a known-positive rectangle.
Neither comparison supplies L504's claimed lower bound. Neither is
imported as a mathematical premise, and neither needs reproof here.

L504 instead names Fourier inversion on Schwartz functions and Cauchy's
residue theorem, and contains its kernel normalization calculation.
That short calculation has an explicit normalization purpose; approval
does not certify its correctness. No essential unread theorem is needed
to undertake the local audit. The smooth Fourier class and lack of
uniform derivative bounds match the parent reviewed family. The
full-vector-space norm versus positive-cone distinction is explicit in
the canonical conclusion and must survive the audit. Mathlib matching
coverage remains unchecked and is not an essential source blocker.

Decision EXPLORE is retained for this exact bounded audit, without a
claim of originality. Passing the stated tests would validate only the
recorded certificate obstruction; a failed test requires repair or
narrowing in a later research turn. This approval supplies no new
mathematical evidence, and the completed step is recorded as STALLED
rather than relabeling the previous mathematical NEGATIVE. The next
turn should perform the audit, not repeat this source approval.
