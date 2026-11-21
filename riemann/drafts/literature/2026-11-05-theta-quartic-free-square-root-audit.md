# Quartic additive-factor audit — reused source coverage

TARGET: Independently audit L824's quartic additive square root, including the inherited j=4 input, exact coefficient identity and full Hermite-minor certificate.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed step623 quartic comparison and step620 inversion/preservation comparison; no changed mathematical hypotheses, new search or extra source claim. Step624's certificate and preserved first-pass failure identify the concrete audit scope.
SOURCE_EVIDENCE: https://arxiv.org/pdf/1504.00350v2 Definition1.1/(1)–(2), Theorem1.3 pp.2–3; https://arxiv.org/pdf/1611.06598v2 Propositions3.4/3.6 pp.7–8; https://arxiv.org/pdf/1911.01745v2 pp.1–3 Lemmas1–2/Theorem1, both proof cases; https://ocw.mit.edu/courses/6-972-algebraic-techniques-and-semidefinite-optimization-spring-2006/260460cc36cd5c2c78b0b04f9b3fe7bd_lecture_05.pdf Section6 Lemma15/Theorem16 pp.5-6–5-7; L791 step478 and L778 step433 audited coefficient/complex-error contracts. Direct primary access confirmed in step625; earlier full comparisons reused.
COMPARISON: The existing complete real-root/multiplicity criterion and convolution operation cover this same fixed d=4 specialization. An independent proof/arithmetic audit needs no new mathematical theorem or fractional-power extension. Original-polynomial hyperbolicity and fitted model roots remain irrelevant premises.
GAP: Independently check L824's normalization, exact identity/uniqueness, all five inherited coefficient enclosures and hashes, rational grid enlargement, Newton identities, determinant expansion and strict Hermite-minor signs. No independent replay or audit has been completed yet.
REASON: Ready source coverage is reused for one bounded independent audit, not a new discovery or automatic approval of L824. This newly saved continuation receives separate gate approval next turn before the audit is invoked.
SCOPE: Only L824 and scripts/central-jacobi/quartic_free_square_root_624.py plus their exact load-bearing inherited evidence. No degree sweep, new evaluator, general divisibility theorem, uniform realization or shifted/mixed extension.

The source record and complete theorem qualifications remain in
[step623](2026-11-05-theta-quartic-free-square-root-scope.md).
This assessment reuses that adequate coverage; it does not repeat
browsing or claim independent review has occurred. General finite
inversion and forward preservation do not imply the inverse factor
hyperbolic. The audit must verify the actual inverse coefficients first,
then the complete sufficient sign test, retaining possible multiplicities.

Canonical evidence is L824 and
`scripts/central-jacobi/quartic-free-square-root-certificate-624.json`.
The input is the actual P_4 of L019/L021/L795 and L791 coefficients
through j=4 under L778's analytic/backend contracts, not its Jacobi model
or L823. Retain E_G/1600^j from the uniform complex disk. Check the
complete inherited intervals and original-hash/replay matches; invalid
input must block sign use. No transcendental backend attestation is
claimed, and full matching Mathlib coverage remains unchecked.

The first failed run is preserved in
`scripts/central-jacobi/quartic-624/first-pass.py` and `first-pass.json`.
Its extra interval-containment assertion was invalid for two equivalent
expressions; the final script replaces it with symbolic Newton identities
and uses the generic recurrence for the Hermite matrix. The independent
audit should verify this correction and all load-bearing signs using an
independent ordering or method. Its pass threshold is the exact identity
and uniqueness together with valid inherited inputs and strictly positive
leading Hermite minors (or a complete multiplicity-safe PSD alternative).
An identified defect must be repaired or explicitly qualify/withdraw the
affected conclusion; a straddling interval alone is inconclusive.

This is ordinary finite proof/arithmetic replay, appropriately routed as
proof_audit/routine_audit at high effort after separate scope approval.
It is not a new central mechanism. Uniform factor realization and all
shifted/mixed sufficient-sign transfer remain open, so the main RH gap
is unaffected. No cross-notebook result is used.

## Separate gate approval — step625, 5 November 2026

LITERATURE_REASON: Supervisor recovery identified missing direct source URLs in this ready assessment. Repair source traceability for the unchanged audit; reuse adequate theorem comparisons rather than repeat discovery.

The exact TARGET above is approved for one subsequent research audit.
The earlier nomination language describes the state before this separate
approval. This turn supplies source traceability, not arithmetic validation
or a new mathematical result. DECISION remains SPECIALIZE.

Direct primary access confirmed the cited versions: MSS v2 (3 July 2019),
Arizmendi–Perales v2 (7 March 2017), Nathanson v2 (24 November 2019),
and Parrilo's 23 February 2006 lecture. Rechecked Nathanson's theorem and
both proof cases on pp.2–3, including multiplicities and nonreal pairs;
Parrilo Section6 on p.5-6 explicitly separates strict leading-minor
positivity from the all-principal-minor nonnegative test. Rechecked MSS
Theorem1.3's degree-d real-rooted input hypotheses and located the
monic degree-d hypotheses of Arizmendi–Perales Propositions3.4/3.6.
The full coefficient inversion/preservation comparison and proofs remain
reused from steps620/623; no larger source extraction was needed.

These sources justify the audit methods, not the actual coefficient
intervals or signs. No reproof is needed: the later audit specializes
fixed real monic degree four and must validate its own normalization,
identity, uniqueness and certificate. The complete multiplicity-safe
criterion remains available if strict signs cannot be reproduced;
straddling intervals alone are inconclusive. Forward preservation still
cannot certify an inverse factor. The recorded first-pass containment
failure and prior automatic-Gram/inverse/Favard stops remain unchanged.
Mathlib full matching coverage is unchecked. No mathematical script or
lemma was changed, and no certificate was replayed in this source turn.
