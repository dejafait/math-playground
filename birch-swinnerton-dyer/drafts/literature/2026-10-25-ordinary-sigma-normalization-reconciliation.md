# Ordinary sigma normalization reconciliation — replacement coverage

TARGET: Reconcile Harvey's and Stein--Wuthrich's ordinary sigma and E_2 conventions on a general minimal Weierstrass model, determining whether L119's sign-only height conversion is valid or needs a certified correction.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused finite-certificate discovery and local duplicate/failure coverage; bounded exact sigma/b_2/E_2/errata searches and author publication/archive checks located MST06's canonical pairing construction but no authoritative SW correction. Queries, unsuccessful accesses and inspected passages are in drafts/source-notes/2026-10-25-ordinary-sigma-normalization-review.md.
SOURCE_EVIDENCE: Read Mazur--Stein--Tate (2006), publisher pagination pp.578--581 equation (1.1), Theorem 1.3 and (1.7)--(1.9), Sections 2.1/2.6--2.8 pp.582--587, and 3.1/3.2 pp.588--591; reinspected Harvey v1 pp.1--4 and Section 5 pp.11--12; SW Sections 3.5/4/4.1/4.4 and author preprint Section 4.1. No inspectable PDF images or direct MT91 proof were obtained.
COMPARISON: MST explicitly constructs the canonical cyclotomic pairing with sigma constant (b_2-E_2)/12; Harvey explicitly declares its 2p normalization relative to MST. These supply a replacement input without assuming the disputed SW exponential agrees on general models. The literal sign-only SW conversion is still uncertified.
GAP: A later mathematical step must apply the imported canonical-pairing identity to L119's polarization and absolute balls and justify the regulator use in foundations/04; no repair, curve data, uniform producer or complex-order comparison is supplied here.
REASON: Newly inspected primary construction changes the route from guessing an SW correction to importing an explicit canonical cyclotomic replacement and checking only its local scalar/precision specialization.
SCOPE: L119's same global minimal integral model, differential and good ordinary p>=5; no p=3 extension, new height algorithm, curve computation or change to the sharp Selmer threshold.
LITERATURE_REASON: Changed evidence from L119 equations (13)--(14) required the previously unread MST construction and a bounded errata comparison; this review supplies that coverage without repeating the completed general audit.

The full failed comparison remains canonical in
[L119](../../lemmas/L119-finite-selmer-height-vanishing-certificate.md).
Do not repeat its determinant or Kummer audit. L001, L003 and audited L118
remain the arithmetic inputs, with foundations/03/04; finite Sha and
ordinary height nondegeneracy must not become assumptions of a claimed
unconditional finite certificate.

The main gap is rational rank versus complex analytic order for arbitrary
E/Q. The intermediate target is a source-supported ordinary-regulator
handoff for L119, potentially enabling L003/L118 when sharp full Selmer
and height certificates are supplied. The continuation test was a precise
conversion or replacement; the replacement branch has source coverage.
The literal SW reconciliation branch is parked, not silently corrected.

Full citations, actual hypotheses, source formulas, essential construction
cases, failed accesses and the duplicate/failure comparison are in
[the source review](../source-notes/2026-10-25-ordinary-sigma-normalization-review.md).
The source statements are known results, not new mathematical discoveries.
In particular, naming both heights canonical is replaced by an explicit
construction and an explicit normalization statement. No theorem is
reproved, and no local polarization or precision repair is derived today.

Original-layout inspection failed because no image data reached the
tools; no author-issued SW erratum was located. These limitations remain
essential for correcting SW itself but do not block the alternative MST
input. Direct MT91 proof access remains unavailable; its uniqueness
statement is inspected through MST Theorem 1.3. No claim about the exact
intended SW correction is made.

The separately scoped
[replacement assessment](2026-10-25-canonical-cyclotomic-height-replacement.md)
is newly written and requires approval on a later turn. Until its
mathematical specialization is completed, L119's positive-rank hold and
the rank/Sha and k=0 audit results remain unchanged. No lemmas, scripts,
PROOF.md or DAG.md were changed. Mathlib matching coverage is not checked.
