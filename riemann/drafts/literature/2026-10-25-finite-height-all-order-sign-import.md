# Finite-height all-order signs — citation-only import coverage

TARGET: Import Sra v1 Theorem 1.3 with Platt–Trudgian Theorem 1 as nonnegative actual-Xi Laguerre signs for every n>=0 on |t|<=3*10^12-1/2, including central multiplicities, without a tail-onset premise.
CHECKED: 2026-10-25
DECISION: IMPORT
SEARCH_EVIDENCE: Reuse 2026-10-25-finite-height-all-order-sign-coverage.md and the initial-sign assessment; exact finite-height theorem identified, with L255 duplicate checked.
SOURCE_EVIDENCE: Sra v1 (20 October 2026), https://suvrit.github.io/papers/riem-xi/riem-xi-v1.pdf, (1.1), (1.5), Theorem 1.3, printed pp. 1–3, Lemmas 4.1–4.2 and complete Theorem 1.3 proof, pp. 9–11; Platt–Trudgian arXiv:2004.09765v1, https://arxiv.org/pdf/2004.09765v1, Theorem 1 and Section 2, printed p. 2. Reuse the completed primary-case review; both PDFs retrieved and theorem statements reconfirmed in the URL-repair turn.
COMPARISON: Direct known-result import; the coefficient convention is L255's D_n and the Xi normalization is L018's. The verified height contains the proposed T. No reproof is justified.
GAP: No missing assumption identified for the proposed finite-height import; global low-order signs and effective tail overlap remain unproved. No independent full-manuscript audit or Mathlib match is claimed.
REASON: Canonicalize source-covered nonnegativity including central zeros, without treating it as new mathematics or extending its finite interval.
SCOPE: Citation-only import of the exact TARGET; no new sign mechanism, numerical certificate, strictness assertion or external half-plane premise.
LITERATURE_REASON: Supervisor recovery requires direct primary URLs in this ready assessment; repair metadata for the unchanged target using the completed source review, without repeating discovery or performing the import.

See [the completed review](2026-10-25-finite-height-all-order-sign-coverage.md)
for primary links, version, exact source locations, successful PDF access,
duplicate comparison and applicability checks. This new continuation is
approved for the unchanged citation-only scope in the separate URL-repair turn; the import has not been executed.

URL repair (2026-10-25): the direct Sra request initially failed, but following
the PDF link from https://suvrit.github.io/papers/riem-xi/ retrieved the complete
25-page v1 PDF. Its (1.1), (1.5) and Theorem 1.3 were reconfirmed; the prior
essential-proof-case inspection remains the coverage basis. The versioned
Platt–Trudgian PDF was retrieved directly and Theorem 1 reconfirmed. There is
no persistent source blocker. This repair supplies no new mathematical result,
independent manuscript audit or Mathlib coverage check.

Essential local input: L018 identifies actual Xi. L255 supplies the local
D_n convention and existing partial result for comparison, not a premise
covering central zeros. L024/L026/L027 are needed only if a later independent
product audit is separately proposed; this import does not reprove the source.
Theorem 1.3 explicitly includes n=0 and central multiplicities; only its
nonnegative conclusion is requested. Platt–Trudgian verifies the requisite
finite zero hypothesis. No assumption of simplicity, a tail onset or
Re(s)>7/8 enters this target. Mathlib coverage remains unchecked.

Downstream use: establish the bounded-height sign input while isolating the
remaining unbounded-height low orders. Continue only if the canonical import
preserves all quantifiers and source qualifications; stop and reassess if any
normalization, endpoint or multiplicity discrepancy emerges. This does not
claim overlap with C465a's existential onset or global mixed positivity.
