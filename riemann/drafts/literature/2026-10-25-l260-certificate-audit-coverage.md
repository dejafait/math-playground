# L260 certificate audit — proposed ready scope

TARGET: Critically audit L260's global strict D_1/D_2 certificate, simplicity and even-polynomial construction using L257's coefficient convolution.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Exact-target duplicate review in drafts/literature/2026-10-25-simple-zero-two-level-masking-coverage.md identifies L260 and its historical stop; no new construction is sought.
SOURCE_EVIDENCE: Prior full L260/L257 scope read reused; Cardon https://arxiv.org/pdf/0911.1122v1 Theorems 1.1/2.1 and polynomial proof case, pp. 1–3; Csordas https://arxiv.org/pdf/1309.0055v2 Theorem 2.4 and coefficient identity (2.11), p. 4; primary passages retrieved again on 2026-10-25.
COMPARISON: The exact affirmative certificate is already local in L260. The standard all-order theorem supplies context and normalization, not a reason to redo this example as a discovery.
GAP: Independently verify the existing finite identities and every global/root qualification; no audit is claimed by this assessment.
REASON: A bounded critical audit avoids repeating the missed duplicate. Any reproduction is justified solely as verification of the existing certificate, not as a new lemma.
SCOPE: L260 with 0<ε<b and b=1/4 for the translated even product; L257 only for the coefficient convolution. No higher-level extension, perturbative generalization or actual-Xi assertion is covered.

This continuation received separate source-coverage approval in the
2026-10-25 URL-repair literature turn. This approves scope, not the
certificate's correctness. The allowed task is one audit of the existing proof;
do not derive a different construction or general theorem.

Audit all normalization factors in D_1 and D_2, the explicit polynomial
identities, the strict sign at every real x (including zeros and large
|x|), the root list over C and its distinctness, evenness and the
convolution transfer. L257's general multiplicity result is not needed
beyond that elementary convolution. Exact symbolic arithmetic may be
used if necessary, with a full certificate saved locally; numerical
sampling cannot establish the signs. Do not write tests that simply
assume the displayed identities. No script is required by this review.

Continue reuse if every item checks; if an identity, strictness claim
or root distinction fails, preserve and document the failure and its
exact consequence. Even a successful audit leaves all actual-Xi signs,
all-degree positivity and RH unresolved. Mathlib coverage remains
unchecked; no matching formal theorem has been claimed.

## Separate source-coverage approval and URL repair

LITERATURE_REASON: The supervisor reported missing direct source URLs in
this ready assessment; this turn repairs that specific evidence field
without extending the target or performing the mathematical audit.

Reused the searches and duplicate comparison recorded in
2026-10-25-simple-zero-two-level-masking-coverage.md. No new discovery
search was needed. Retrieved the versioned primary PDFs linked in
SOURCE_EVIDENCE, rather than relying on their abstracts. Cardon's
Theorems 1.1 and 2.1 require a nonzero real entire function of the form
exp(−bz²)f_1, b≥0, with f_1 of genus zero or one. Theorem 2.1 additionally
requires an even auxiliary polynomial with nonnegative real coefficients
and a nonreal root. Both criteria require every index and every real
center. Its converse on p. 3 uses the entire coefficient expansion;
the forward polynomial case uses real linear factors. These cases were
read for scope, not independently rederived or imported as a two-level
converse. Real polynomials lie in the stated function class, so no
growth-hypothesis extension is needed for this audit.

Csordas's Theorem 2.4, p. 4, states the all-index criterion, retaining
the Gaussian-times-genus-zero-or-one hypothesis in its converse.
Remarks 2.5, equation (2.11), explicitly identifies its L_n as the
coefficient of y^(2n) in f(x+iy)f(x−iy), the normalization named in
L260. This is source evidence for the convention; checking L260's
particular identities remains the future audit's job.

Read L260's canonical statement/proof and L257's coefficient-convolution
paragraph (lines 22–26) for the audit boundary. Reused the September 23
stop recorded in ATTEMPTS/2026-09-23-simple-root-masking-test.md:
simplicity cannot by itself repair two-level sufficiency. The audit is
verification of that existing evidence, not a reopened construction.
No mathematical computation, new proof, or lemma change was made here.
Continue if all finite identities, strict signs and complex-root
qualifications verify; on any failure preserve the exact defect and
revise only the affected claim in a subsequent authorized research step.
