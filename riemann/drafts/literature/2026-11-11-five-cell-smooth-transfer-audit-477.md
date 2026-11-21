# Proposed separate audit: constrained five-cell form approximation

TARGET: Critically audit C744h's exact-neutral even modes0-83 smooth approximation, including all six boundary estimates, physical moment scaling, complex reflection and convergence in the shifted complete form.
CHECKED: 2026-11-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step478 reused the exact queries and comparison approved in step476, drafts/literature/2026-11-11-five-cell-exact-neutral-smooth-transfer-475.md, then directly retrieved the two essential primary passages at the URLs below; no repeated discovery search or novelty claim.
SOURCE_EVIDENCE: Step478 read Suzuki arXiv:2606.09096v3 Section3.2 (3.2)-(3.4), including endpoint terms and both frequency cases, https://arxiv.org/html/2606.09096v3#S3.SS2 ; and Hofer-Wysocki-Zehnder JEMS9(2007) Lemma2.12 p846 with its full proof, https://ems.press/content/serial-article-files/31611#page=6 . Reuse C744c Section2, C744e step466, L743(9)-(10) and C744b(1)/(2)/reflection as local methods.
COMPARISON: Step478 separately approves source coverage for the exact audit target: the unchanged finite-vector cutoff and fixed smooth correction mechanisms at the fixed window and physical moments. C744h's internal-boundary and parity specializations remain unaudited; this approval is not their verification.
GAP: Independent verification of C744h's six-boundary variation bound, shifted-form equivalence, scaled right inverse, even complex output space and complete-energy limit remains; no critical audit has occurred. No new sign theorem or general density theorem is included.
REASON: Source reuse covers the mathematical tools for this conceptual audit; separate review must test the claimed domain transfer. This nomination neither audits the proof nor certifies new mathematics beyond the inspected sources.
SCOPE: Exactly C744h at ell=log3/2 and a=5ell/2, complex even modes0-83, all ten original physical moments, the zero-extension logarithmic form and its complete L744(6) shift; no uniform H2 cap, varying window, positivity or whole-domain identification.

## Source reuse and separate approval — step478

This continuation was not authorization present at the start of
step477. The separate literature-only step478 repairs the missing
direct URLs and approves the source comparison for the exact TARGET.
The mathematical audit is deferred to the next turn. A statement
outside SCOPE needs REVIEW_REQUIRED.
The original proof target was approved before step477 and was the
only mathematical target attempted. Its canonical proof is
`lemmas/C744h-five-cell-exact-neutral-smooth-form-approximation.md`.

LITERATURE_REASON: Supervisor recovery identified missing direct source URLs in this ready audit assessment; retrieve the named primary passages and repair traceability without expanding the target or redoing discovery.

### Primary passages retrieved on 11 November 2026

[Suzuki, version 3, 23 September 2026, Section3.2](https://arxiv.org/html/2606.09096v3#S3.SS2)
works at fixed positive window with a lower bounded closed Weil form
and its positive shift. For each fixed exponential mode it estimates
outer-boundary cutoff error using its L1 size and a uniform variation
bound retaining both endpoint jumps. Equations (3.3)-(3.4) feed the
two integrals split at inverse cutoff width, giving squared form error
O(epsilon log(1/epsilon)). This does not cover internal punctures,
exact moments or parity correction. Its endpoint-only cutoff wording
does not alone guarantee compact interior support; retain the genuine
collar requirement already flagged by step476 and C744c.

[Hofer-Wysocki-Zehnder, Lemma2.12, printed p846](https://ems.press/content/serial-article-files/31611#page=6)
assumes a Banach space, a closed subspace with finite dimensional
complement, and a dense linear subspace. It selects a complement
inside that dense subspace through representatives of a basis of the
finite dimensional quotient. The complete proof was retrieved. It
does not establish our moment-map image, its continuity in the form
norm, or the reflection law; those remain local audit obligations.

The prior comparison's general Lipschitz-density source and Li45
remain background, not essential theorem imports for this audit.
Their scope limitations are retained in step476; no new reading of
them is claimed. C744g's half-energy stop remains unrelated to this
domain-only claim. Full matching Mathlib coverage remains unchecked.

## Bounded conceptual test

Inspect C744h in full, then only necessary ranges of L744(6)/(8),
C744b(1)/(2)/reflection, C744c Section2 and L743(9)-(10). Verify
actual compact cell-interior support, both endpoint jumps in the
variation bound and both frequency ranges of the logarithmic integral.
Check that closure membership follows from the approximants, without
silently identifying the full supported weighted space with the core.

Check the physical exp(sigma ell/4) factor, absence of conjugation
in CR=PC, and correction on the symmetric five-dimensional output
space. The fixed smooth inverse must be bounded in the form norm,
not merely L2. Verify all ten exact equations, the global pole
identity, mixed terms controlled by the norm inequality, and
subtraction of the shift in the complete-energy limit.

Accept only if these arguments hold for arbitrary complex coefficients
with exact Cf=0. Otherwise preserve and repair or reject the specific
failure without weakening the target to approximate neutrality. No
numerical certificate is needed or substitutes for the analytic proof.

The main gap remains L030-L032/C032a actual-Xi positivity. This audit
would validate a finite domain bridge; unrestricted middle/distant
couplings, odd signs and all-window propagation remain unpaid. C744g
and L750 are obstructions to other mechanisms, not premises or global
bans. Full matching Mathlib coverage is unchecked. No cross-notebook
input is used.

No justified creative central mechanism was identified in this bounded
specialization. The blocker remains the missing quantitative inequality
for unrestricted middle/cell correlations or window growth; routine
domain work cannot be relabeled creative to meet a scheduling target.
