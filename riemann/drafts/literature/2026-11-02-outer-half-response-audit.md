# Outer-half response obstruction — source coverage for a separate audit

TARGET: Audit C645t's full-angle outer-half response obstruction, checking the rational pair certificate, contour domains, odd-grid correction and finite-node error against exponent 1/32.
CHECKED: 2026-11-02
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse the exact angular-family searches and primary theorem comparison in 2026-11-02-rotation-averaged-anchor-line-hankel.md, unchanged in family and Fourier/residue methods; the scoped C645n/C645o/C645p and angular failure records were checked for this attempt. No additional external search or novelty claim is made.
SOURCE_EVIDENCE: Reuse BCQ 1501.01161v2 Section 4/(17)--(19); Howell--Mathews Complex Analysis Sections 8.1 Theorems 8.1.5/8.1.7 and 6.2 Theorems 6.2.18--6.2.19, as previously inspected; C645l's exact finite-node identity (23)--(24) and C645n's projection and angular anchor-product estimate were read for the completed attempt.
COMPARISON: The inspected projection and contour rules cover the operations with the stated analytic domains; they do not assert C645t's pair inequality or its quantitative response exponent. The audit must check the new rational certificate and these specializations, not infer correctness from the general identities.
GAP: Independently verify C645t's complete proof and all essential uses of C645g/C645l/C645n, including the half-plane root implication, exhaustive box coverage, finite-n partner shift, contour endpoints and uniform full-output conclusion; no operator-norm upper bound or Xi bridge is asserted.
REASON: Separate literature approval is completed for the unchanged audit target. The primary projection, residue and contour statements cover the proposed tools; the quantitative proof and certificate remain unaudited and are the next research task.
SCOPE: Exactly C645t as stated for odd m>=5, n=3m, radius 27/50, unit residues and the outer-half input; audit or repair its proof within the saved common-pole target, without extending the claim to the full operator or importing a new theorem without review.

This assessment was prepared with the preceding proof attempt and separately
reviewed in the present literature-only turn. Approval here concerns source
scope, not mathematical correctness. The earlier angular comparison is
reused; the cited primary statements were checked narrowly as recorded below.
The changed radius and finite-node parameters are applicability checks
for identities already read, not changed hypotheses of an unread source.

The primary references are L. Baratchart, S. Chevillard and T. Qian,
*Minimax principle and lower bounds in H2-rational approximation*,
J. Approx. Theory 206 (2016), 17--47,
[preprint v2, Section 4, (17)--(19)](https://arxiv.org/pdf/1501.01161v2),
and R. W. Howell and J. H. Mathews, *Complex Analysis*, online edition,
front matter updated 22 August 2025,
[Section 8.1](https://complexanalysis.org/web/sec_residue-thm.html) and
[Section 6.2](https://complexanalysis.org/web/sec_contour-integrals.html),
with the theorem numbers above. The prior assessment records what was
actually inspected; this turn did not reread the external sources.

The audit should examine the complete rational arithmetic algorithm and
certificate, including the prefix partition, rather than a sampled plot
or an inspector preview. The first-pass false n=9 auxiliary inequality
is preserved alongside the final n>=15 theorem. A fresh replay and
independent logical check are appropriate for the audit; numerical
diagnostics cannot establish a uniform bound. Full matching Mathlib
coverage is unchecked. The continuation does not certify novelty.

Continue with the restricted stop only if the claimed full-angle rate
7/200, normalization and hypotheses survive. Otherwise identify and
repair the exact failure, or retract only the unsupported conclusion
while preserving its evidence. Regardless of audit outcome, the general
angular operator estimate and all actual-Xi realization/sign gaps remain
independent unresolved questions.


## Separate source approval — 2 November 2026

LITERATURE_REASON: The supervisor explicitly gated this newly saved continuation for separate approval; this turn checks its exact source applicability, reusing the angular search rather than repeating discovery for a ready family.

The target text and EXPLORE decision are unchanged. Read the parent angular
assessment and the outer-half history/ATTEMPTS record. Read C645t's hypotheses,
conclusion, source scope, contour-domain claims, pair-inequality statement and
finite-node application to identify essential source uses. Read C645g's space
normalization, C645n Sections 1--2 and C645l Section 5/(22)--(24). These are
source-scope reads, not an independent proof audit. Prior failures include the
weaker full-cancellation input and the false n=9 auxiliary bound. They remain
preserved. No duplicate of the exact quantitative obstruction was identified
by the reused bounded assessment; this does not establish novelty.

Primary statements retrieved on 2026-11-02:

- BCQ preprint v2 (24 March 2015), printed pp.7--8, Section 4,
  (17)--(19) and Theorem 2, at the PDF link above: bounded symbols define
  the H2-to-strictly-negative-space operator; continuous symbols yield
  compactness. AAK equates singular values with meromorphic approximation
  distances. It does not evaluate this family's angular response. Its
  H-infinity-domain operator is distinct. No maximizing-vector claim is
  available for the prescribed outer-half input.
- Howell--Mathews Section 8.1, Theorems 8.1.5 and 8.1.7(1), at the link
  above: the first requires a positively oriented simple closed contour
  and analyticity except finitely many interior isolated singularities;
  the second computes simple-pole residues by a limit. Read their proofs:
  disjoint small circles and extended Cauchy--Goursat for the former,
  the Laurent coefficient for the latter. The proposed ellipse has to
  enclose exactly the specified simple nodes; sources do not verify that.
- Howell--Mathews Section 6.2, Theorems 6.2.18--6.2.19, at the link above:
  continuity and finite contour length are essential. Read both proof
  cases of the absolute-value inequality (zero and nonzero integral),
  and the ML proof via parametrization. These justify bounds only after
  the notebook establishes its uniform modulus estimates and domains.

Applicability obligations for the audit: check holomorphy near each closed
region, exclusion of low-grid zeros and the spatial pole, orientation and
branch choice under the lambda parametrization, removable endpoints in the
segment deformation, and the exact factor m in passing from node average
to total output. The projection specialization needs interior a/R and an
input holomorphic near the closed disk; its difference quotient is already
written in C645n. No reproof of the imported general theorems is needed.
The changed r=27/50 and s=13/200 require checking their local geometric
inequalities, not assuming the old numerical ellipse bounds.

Remaining original verification is precisely the saved audit: inspect the
complete rational interval algorithm and partition, the half-plane level-circle
implication, odd-grid shift and both uniform contour bounds. No certificate
was replayed or accepted here. The claimed exponent 7/200 versus 1/32 is
only C645t's pending conclusion. Full matching Mathlib coverage remains
unchecked. EXPLORE authorizes testing this local claim, not importing it as
an established theorem or asserting originality.

The main RH gap remains actual-Xi all-degree mixed positivity and unbounded
height signs. A successful audit would validate a stop for this nominated
input and inform selection of another detector; it would not stop the full
angular operator mechanism. Continue only if the complete proof and exact
certificate survive; otherwise repair or retract the unsupported portion.
Common-pole realization, other poles, census/clearance, an independent upper
bound and actual-Xi signs remain independent unresolved assumptions.

Coverage is ready for the exact unchanged Next action. Proceed to its
conceptual mathematical audit next turn without another source-approval loop,
unless an essential new theorem or changed hypothesis is introduced.
