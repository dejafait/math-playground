# Rational dyadic index application — audit coverage approved

TARGET: Critically audit L070's rational dyadic inclusion and index-two theorem application, including maximal-unit conventions and good-reduction hypotheses.
CHECKED: 2026-10-14
DECISION: IMPORT
SEARCH_EVIDENCE: Reused the prior dyadic application search; narrowly checked L070, relevant L033/L046/L069 passages, ATTEMPTS/032 and histories 217–218; reopened the primary BPT local definitions, theorem and essential good-reduction proof case for audit scope.
SOURCE_EVIDENCE: Barrera Salazar–Pacetti–Tornaría arXiv:2001.02263v3 (17 September 2020), Section 1 p.3, Remark 1.4 and Lemmas 1.3/1.5 p.4, Definition 1.6(iv)/Theorem 1.8 pp.5–6, and Theorem 1.11 first assertion/proof p.7; https://arxiv.org/pdf/2001.02263v3.
COMPARISON: The exact local inclusion/index is covered by a named theorem; auditing the existing specialization requires checking its model, good reduction and maximal-unit identification, not reproving local-image theory or computing classes.
GAP: The source gate is complete; independent critical verification of L070's application is still pending, and global-unit localization and rank pruning are outside coverage.
REASON: Separate approval now supplies the precise source/hypothesis checklist for the saved audit target without repeating its mathematical application.
SCOPE: Only critical application audit of L070 over Q2 using L033, L046 and L069; IMPORT permits KNOWN_IMPORTED. No ramified-base extension, global localization, explicit image algorithm or rank bound is approved.
LITERATURE_REASON: The supplied audit assessment was REVIEW_REQUIRED; separate audit scope approval was missing despite ready application coverage.

## Primary source comparison

Daniel Barrera Salazar, Ariel Pacetti and Gonzalo Tornaría,
*On 2-Selmer groups and quadratic twists of elliptic curves*,
[arXiv:2001.02263v3](https://arxiv.org/pdf/2001.02263v3),
17 September 2020; Math. Res. Lett. **28** (2021), 1633–1659,
[DOI](https://doi.org/10.4310/MRL.2021.v28.n6.a1).
Numbering refers to the arXiv version; no publisher-version equivalence
or independent audit of the cited Brumer–Kramer proofs is asserted.

Section 1 uses the whole cubic square-norm Kummer target without a
scalar quotient. Remark 1.4 uses maximal integer rings of all factors.
Definition 1.6 requires a monic integral square-free cubic and permits
unramified dyadic good reduction as an alternative to polynomial-order
maximality. Theorem 1.8 supplies inclusion. Its good-reduction proof
handles supersingular reduction via Brumer–Kramer Proposition 3.4 and
ordinary reduction via Proposition 3.6. Theorem 1.11's first assertion
supplies index 2^[K:Q2]; its proof invokes Theorem 1.8 and Lemmas
1.3/1.5. These passages were inspected. The source's counterexamples
on p.6 warn against dropping its hypotheses. The U4 assertion and
global narrow-class assumptions are unnecessary inputs here.

## Local audit checklist and limits

The main gap remains primitive integer emptiness. The intermediate
target remains critical audit of the necessary local condition in L070.
An accepted cut could be used in a later certified global descent;
it cannot itself certify that a global unit direction is lost.

Read the complete L070 application and the relevant input passages:
L033's original model and discriminant, L046's rational place and good
reduction, and L069's origin-preserving cubic change and nonzero
discriminant. Their recorded values are inputs to be independently
checked in the next audit, not new calculations in this source review.

The audit must check the change X=4x, Y=8y+4 and origin, the recorded
cubic g=X³−4X²−160X−1264, and original discriminant −11^5. Distinguish
the original smooth integral model from the changed cubic's integral
model. Check maximal-unit square-class injection and the base unit norm
convention, retaining all factors and the abstract Kummer map at O and
two-torsion. Establish inclusion before using the index; do not infer
inclusion from cardinalities. The unramified premise is solely over Q2,
not over L046's ramified degree-eleven factor.

ATTEMPTS/032 stops only the unfiltered global ambient bound.
Histories 217–218 already record source coverage and theorem application;
this review approves an independent audit, not a second application
or an explicit image computation. The prior assessment's bounded search
and source-access qualifications remain reusable. No new discovery or
literature-wide novelty claim follows. Mathlib matching and supporting
coverage remain not checked.

Accept the existing local inclusion/index only after all application
checks pass; otherwise record a precise correction or essential source
gap. Even acceptance leaves global localization, class coverage, other
places, rank, subgroup indices/cosets, other classes and integer lifting
unresolved. No GRH, polynomial-order maximality, narrow-class premise,
localization surjectivity or global codimension decrease is assumed.
No lemma or mathematical script was changed in this literature turn.
