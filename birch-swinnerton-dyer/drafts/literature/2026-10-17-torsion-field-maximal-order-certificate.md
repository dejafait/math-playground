# Exact arithmetic-order certificate — completed source comparison

TARGET: Assess an exact maximal-order and field-discriminant certificate for L067's degree-48 torsion field as preparation for complete S-unit and S-class computations.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched maximal-order/round-two/radical-multiplier-ring certificates, PARI nonmonic basis certification, Dedekind p-maximality criteria, and exact conductor-389 degree-48 seven-torsion/discriminant terminology; compared L067, L066 item 2, ready Section 5 coverage and ATTEMPTS/034/036. Sources and cases are recorded in drafts/2026-10-17-maximal-order-source-review.md; no matching inspected field computation was located and no novelty is inferred.
SOURCE_EVIDENCE: Direct primary PDF https://www.impan.pl/shop/en/publication/transaction/download/product/82018 ; Del Corso--Dvornicich--Simon, Acta Arith. 120 (2005), Section 2/Proposition 4 pp. 232--234 and Section 4/Proposition 9/Theorem 2 pp. 238--240, including the homogeneous leading-prime case and gcd/enlargement proof; Stein Theorem 4.3.5 with its incomplete proof distinguished; PARI stable manual nfbasis/nfcertify/nfdisc/nfinit; SymPy 1.14.0 basis.py lines 10--85,176--232 and root-scaling documentation, inspected 2026-10-17.
COMPARISON: Known nonmonic-order and radical--idealizer theorems cover a full certificate framework; remaining work is fixed-field construction and independent replay. Prefer a complete starting-order/trace-discriminant test before maximal-order production; Round 4/Buchmann--Lenstra are alternatives, not existing local certificates. A 7-maximal order is not approved as a replacement for complete S-integer arithmetic.
GAP: No starting order, order discriminant, index-prime coverage, maximal overorder or field discriminant has been computed. Complete S-unit/S-class data, faithful classes, functions/local evidence and the main rank gap remain independent.
REASON: Essential source comparison is complete for the framework and a bounded first implementation test; no new mathematics or arithmetic script was produced. Retrieval failures affect optional leads only. The separately saved continuation requires next-turn supervisor approval.
SCOPE: L067's entire degree-48 field and primitive nonmonic H=343h, retaining rational transports; source-based certificate design only. No assumption that t is integral, selected factor, cross-notebook input, stopped-column resumption, 7-only global certificate or conditional completeness.

The full citations, inspected proof cases, source limitations, global/local
comparison and finite contract are in [the source review](../2026-10-17-maximal-order-source-review.md).
The first test implements known mathematics; no maximality-theorem reproof
is needed. It stops before index-prime coverage and must not name its output
a field discriminant. Preserve all prior arithmetic and stopped evidence.

The prospective support S={7,389} remains only a later descent input.
Neither S-unit completeness nor absence of auxiliary function support is
inferred. An order localized away from S remains an unapproved alternative
requiring an exact group comparison. Mathlib coverage is not checked.
No argument change, lemma, mathematical script or BSD candidate is supplied.
