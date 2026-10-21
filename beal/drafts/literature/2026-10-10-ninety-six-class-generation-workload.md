# 96a1 unconditional class-generation workload — continuation for separate approval

TARGET: Measure the unconditional class-generation workload for FNS's degree-36 96a1 two-descent field using certified field or order discriminant bounds.
CHECKED: 2026-10-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: The certificate-scope review located the exact primary field models, searched 96a1/Selmer/unconditional/certification/discriminant terms, and inspected standard discriminant and Minkowski results; no field-specific unconditional verification bound was inspected.
SOURCE_EVIDENCE: FNS final manuscript June 10, 2019, Section 7.2 and Table 5, printed pp.25-28; section7.magma lines 315-334; Milne ANT v3.08 Remark 2.25 and its proof p.34 and Theorem 4.3 p.70; Magma V2.29 ClassGroup/MinkowskiBound documentation; Elsenhans-Voight October 2, 2025 Sections 4,7-8.
COMPARISON: Standard results supply the discriminant-index relation and an unconditional bound for class representatives; the unperformed difference is an exact workload bound for this specific degree-36 field, without treating a polynomial order as maximal or inferring class completeness.
GAP: No exact field/order discriminant, signature, rounded bound or bounded naive-verification feasibility result is yet computed; missing backend access does not prevent an exact order-trace calculation but prevents assuming a full class/unit implementation.
REASON: Quantify one necessary certification workload before attempting an unavailable full Selmer replay; this is distinct from local nonexistence and finite element-box searches.
SCOPE: One exact field/order trace-discriminant and generation-bound calculation, including model and rounding checks; no class/unit computation, Selmer upper image, point classification or signature exclusion. Newly written continuation requires separate next-turn approval.

The main gap is unconditional emptiness of the surviving ordered (3,4,11)
branches and other residual signatures. The intermediate target measures
whether the elementary class-generation verification route has a bounded
entry point. Its downstream use is a go/park decision for a specified
certification mechanism, not a new obstruction on solutions.

Essential inputs: L050's K96 polynomial; L032's retained 96a1 disk;
the source specification in
[the completed review](2026-10-10-ninety-six-unconditional-selmer-certificate-scope.md).
L034 is only context for the complete modular map. L033's field and
L045's quotient classes are not arithmetic inputs. No cross-notebook use.

Use FNS's degree-36 L96, adjoining the two-torsion coordinate. The source
code's integral generator T has polynomial T^3-4T^2-160T-1264, and its
map to the division-polynomial algebra is T -> 4 theta. K96 is the
degree-twelve field defined in L050. Preserve these coordinates exactly.
If using an order basis, establish its integrality, independence and full
rank in the cited field before applying a discriminant bound; report an
order discriminant as such. A direct exact trace matrix avoids relying
on a guessed resultant model or an uncertified maximal-order computation.
No degree-36 defining polynomial has been constructed in this review.

Milne, *Algebraic Number Theory*, v3.08, July 19, 2020,
[primary PDF](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
defines discriminants by the trace matrix on p.33. Remark 2.25, p.34,
states the square-index identity for a full-rank integral submodule of
the ring of integers and proves it by basis change. Theorem 4.3, p.70,
states that for a degree-n number field with 2s nonreal embeddings and
field discriminant Delta, ideal classes have integral representatives of
norm at most (n!/n^n)(4/pi)^s sqrt(abs(Delta)). These are cited inputs;
their application to a computed order and the explicit rounded bound
remain the research work. Retain the actual signature or certify a
conservative uniform choice. Use exact rational enclosures for every
rounding decision; decimal previews cannot establish the bound.

Continue toward naive prime-ideal generation verification only if the
certified norm cutoff is at most 10^6 and a rigorous ideal backend can
be identified. This cutoff bounds the proposed enumeration mechanism;
it is not a mathematical threshold for Beal. A larger order-based cutoff
parks enumeration at that cutoff and leaves maximal-order refinements
unresolved; it gives no lower complexity bound or proof of infeasibility.
If neither a field nor an order bound can be certified in one bounded
attempt, save the exact obstruction and choose an independent target.
Do not install software, enlarge element-search boxes, or start a long
class-group run. No field-specific certificate is assumed.

The current absence of magma, gp and sage on PATH is recorded evidence,
not a search of all libraries. No GRH, class/unit completeness, Selmer
dimension, rank, Sha or integer solution is assumed. All other branches
and residual signatures remain independent gaps. Mathlib coverage is
not checked. This proposal contains no new field-specific calculation.
