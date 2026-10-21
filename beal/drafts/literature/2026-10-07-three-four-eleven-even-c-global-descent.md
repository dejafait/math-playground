# Completed even-C global descent source comparison

TARGET: Assess an unconditional global descent for L032's 54a1 branch of A^3+B^4=C^11 with C even, seeking a fourth-power restriction beyond the completed residue filters.
CHECKED: 2026-10-08
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the completed exact-signature comparison and searched fourth-power, even-C, 54a1, covering and isogeny-descent variants; specific queries and duplicate/failure checks are in drafts/2026-10-08-even-c-global-descent-source-review.md.
SOURCE_EVIDENCE: Read FNS final author PDF Section 7.2 pp. 25–27, the ramified 54a1 proof case pp. 32–33 and Remark 7.13 p. 33; Siksek–Stoll revised July 4, 2011 manuscript Section 2/Theorem 2.1 pp. 3–6 and Section 3 setup pp. 6–7; Schaefer–Stoll June 13, 2001 long manuscript Proposition 4.6 p. 7, Section 5 pp. 8–10 and Section 9's construction/Lemma 9.1 pp. 21–23.
COMPARISON: No inspected source supplies a fourth-power restriction or unconditional emptiness for this branch; partial hyperelliptic descent needs an unprovided model, whereas general cyclic-isogeny descent gives a different explicit construction test on the existing elliptic target.
GAP: Direct fourth-power cover feasibility and emptiness remain unresolved; a proposed 5-isogeny Kummer map must first verify its torsion, dual orientation, function divisor, exceptional evaluations, original-solution transport and finite class-data requirements.
REASON: The direct-cover continuation test was not met; the newly read general isogeny-descent construction permits an independently testable target without repeating residue filters, importing conditional Selmer dimensions or relying on Fisher's inaccessible specialized formulas.
SCOPE: Completed literature-only comparison for the positive primitive ordered (3,4,11) 54a1 branch; no mathematical specialization or new lemma is approved as completed work.

The main gap is unconditional global emptiness, with the other four non-CM twists and infinitely many signatures independent. The intermediate target was an explicit global construction retaining X=B^2; its downstream use would be a stronger necessary condition or elimination of this branch. L032 already proves C even, B odd, A=7 mod 8, A=1 mod 3, B^2=1 or 4 mod 9, d in {1,-3}, 0<j<1728 and (1728-j)C^11/1728=B^4. It does not prove global emptiness. No cross-notebook input or conjectural premise is used.

LITERATURE_REASON: Essential coverage of the proposed fourth-power global descent was missing; the ready finite-filter audit had already been completed and was reused without repetition.

## Primary comparison and exact source scope

Full source evidence, queries and access qualifications are in [the source-review record](../2026-10-08-even-c-global-descent-source-review.md). The previous [classification assessment](2026-10-07-three-four-eleven-classification-coverage.md) is reused for unchanged signature/theorem coverage. FNS: [final author PDF](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf), Compositio Math. 156 (2020), 77–113, DOI 10.1112/S0010437X19007693. New locators here use printed footer numbers, correcting earlier notes' occasional zero-based PDF indices. Section 7.2's transport to a degree-12 field and its curve model precede the GRH-dependent 2-Selmer computation. The 54a1 ramified local expansion does not independently replace that global computation. Remark 7.13 supplies no working smaller-field model.

Siksek–Stoll: [July 4, 2011 author manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/345-revised.pdf), Bull. London Math. Soc. 44 (2012), 151–166, DOI 10.1112/blms/bdr086. Theorem 2.1 requires a squarefree even-degree binary form and its hyperelliptic curve, plus the preceding partition/component setup. Its known (3,4,5) application and Edwards parametrization do not supply such a model at eleven. Missing applicability is not a theorem that no suitable cover exists.

The different mechanism uses the general isogeny-descent source recorded canonically in [foundations/15-schaefer-stoll-isogeny-descent.md](../../foundations/15-schaefer-stoll-isogeny-descent.md). Its theorems have no GRH assumption but do not certify arithmetic inputs or emptiness. Fisher's indexed specialized 5-isogeny formulas remain unread leads after full-source retrieval failures; they are parked and are not required for the general construction test. No rank-zero theorem over a cyclotomic field is transferred to the degree-12 FNS field.

## Route decision

Park the unspecified fourth-power cover and the conditional 2-Selmer elimination. A bounded 5-isogeny function/applicability test on the existing X0(11) model is materially different and can use the read general theory. Its separate [specialization assessment](2026-10-08-three-four-eleven-five-isogeny-construction.md) awaits supervisor approval next turn; no construction has been derived here.

Continue that alternative only if it gives a verified nonconstant descent function, correctly oriented necessary global Kummer classes and a concrete description of arithmetic data needed to intersect them with the full fourth-power condition. A generic Selmer identity or renewed residue filtering alone does not justify a large computation. If the construction does not yield a usable independent test, preserve the evidence and park it. Even a successful function construction leaves class/unit certification and global emptiness unresolved. Mathlib coverage is not checked; mathematical exploration remains 1/3.
