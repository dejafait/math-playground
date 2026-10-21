# Modular norm critical-audit coverage

TARGET: Critically audit L034's complete modular norm, scalar, fiber specialization and constant-class stop decision.
CHECKED: 2026-10-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact norm/modular-map and Stacks norm/base-change searches recorded in drafts/literature/2026-10-08-five-isogeny-modular-norm.md; read that full assessment, L033 and L034, history/086 and history/087, and ATTEMPTS/008 and ATTEMPTS/009; no fresh external search was necessary for unchanged source hypotheses.
SOURCE_EVIDENCE: Reused the inspected June 10, 2019 FNS manuscript Section 7.2 pp.25–27 and Lemma 7.6 proof p.28, and Stacks 02RT (42.18.1), 0BD2 (31.18.6), 0CCK (53.2.3), 0CCL (53.2.4), 02K9 (29.49.2), with full-proof coverage recorded in the construction assessment.
COMPARISON: The known divisor-pushforward and determinant-base-change theorems cover the audit machinery, including ramified/nonreduced fibers; FNS covers the modular map and full field transport, while L034's explicit scalar, coordinate cancellation and applicability require independent verification rather than citation alone.
GAP: The source gate is complete; the independent arithmetic and logical audit of L034 has not been performed, and no scalar, fiber assertion or stop decision is newly certified by this literature step.
REASON: Approve the newly proposed critical audit using ready coverage, without reopening norm compression or retrieving parked Fisher sources; only the identified explicit specialization needs mathematical checking.
SCOPE: Exactly L034 under L033's positive primitive ordered (3,4,11), 54a1 and degree-twelve K hypotheses, including its generic norm and all specified exceptional/branch fibers; no new descent class data, other twist, cover or signature exclusion.

## Reusable primary coverage and hypotheses

The full ready assessment is drafts/literature/2026-10-08-five-isogeny-modular-norm.md. This turn compares its inspected theorem coverage with the new audit scope; it does not claim to have freshly fetched sources. Its original searches found no matching normalized formula, which is not a novelty determination. The source versions and exact ranges remain unchanged.

[Stacks 02RT, Lemma 42.18.1](https://stacks.math.columbia.edu/tag/02RT) supplies div(N(f)) = j_*div(f) for a dominant proper morphism of integral schemes of equal dimension over the stated dimension-function base. Smooth projective integral curves over Q have the required setting. The recorded proof covers orders and residue-field-degree weights. The audit must check the rational images of T and O and their pushforward weights; this theorem supplies no scalar. Ramification indices must not replace those weights.

[Stacks 0CCL, Lemma 53.2.4](https://stacks.math.columbia.edu/tag/0CCL) covers finiteness of this nonconstant proper curve map to a separated target; [0CCK, Lemma 53.2.3](https://stacks.math.columbia.edu/tag/0CCK) covers flatness with normal target. [02K9, Lemma 29.49.2](https://stacks.math.columbia.edu/tag/02K9) supplies finite local freeness over the locally Noetherian target. The prior assessment read the statements and proofs. Their hypotheses cover E0 to P1 over Q, provided the stated map and degree are correctly identified in the audit.

[Stacks 0BD2, Lemma 31.18.6](https://stacks.math.columbia.edu/tag/0BD2) defines the norm by multiplication determinant and proves compatibility with arbitrary base change for finite locally free maps. Restrict to an open where f is regular (and a unit when a Kummer class is claimed). The recorded proof covers nonreduced fiber algebras. This is sufficient coverage for j=0,1728; it does not permit treating them as twelve distinct points. A pole is outside regular evaluation, and a zero is outside a multiplicative class. The audit must keep those qualifications.

Freitas–Naskręcki–Stoll, *The generalized Fermat equation with exponents 2, 3, n*, Compositio Math. 156 (2020), 77–113, [June 10, 2019 author manuscript](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf), Section 7.2 pp.25–27, supplies the map formula, equation (7.4), cyclic-subgroup transport, irreducible degree-twelve field and Table 5. The previously inspected reconstruction caveat is in Lemma 7.6's proof p.28. This scope includes the field transport without importing GRH-dependent Selmer dimensions. The audit must compare all source coefficients and cannot assume that an eliminated x polynomial presents every exceptional fiber.

L033 is the already audited canonical input for f, its divisor, torsion coordinates and original solution transport. General descent does not need a new reproof here. L032's positivity, fourth-power identity and branch conditions remain retained through L033; they are not replaced by elliptic x being a square. No hypothesis change calls for new literature.

## Exact approved audit and evidence requirements

The certificate schema was inspected with the bounded JSON inspector solely to locate evidence. It has source, polynomials_ascending, residuals, torsion, fiber_at_1, conclusion, checks and failures objects. This preview is not mathematical verification. The implementation was searched to locate its polynomial transcription, resultant routine, complete fiber calculation and checks; it was not run or independently validated in this literature turn.

The next research audit must inspect the complete relevant certificate values, not just the fourteen success flags. In particular inspect every coefficient of a,b1,b2,b,g,d,h,jcoef,F_at_1 and f_numerator_at_1, all three residuals, all four torsion objects, and full fiber_at_1 determinants and bounds. Use selected --full fields with the supplied JSON inspector. Independently verify the load-bearing resultant calculation and its sign/denominator correction, or provide a rigorously justified independent exact check; rerunning the same implementation alone does not audit its algorithm. Mathematical scripts are authorized only in the later research turn.

Check the generic reconstruction and degree argument, full regular j=1 fiber, and scalar normalization. Check the pole fiber O+11(3T), cancellation at 2T, and zero/pole handling separately. Audit the finite locally free applicability, the regular/unit open, and specialization through the whole algebra even at nonreduced branch fibers. For the solution fiber, verify the degree-twelve closed point gives the entire fiber algebra K, not one factor or embedding. Retain 0<j0<1728 and both original solution identities. Finally audit the fifth-power-class inference and compare the actual variation flag with the required true threshold. These are verification tasks within assessed machinery, not authorization to derive an unrelated result.

## Overlap, route decision and limits

ATTEMPTS/008 parks uncertified arithmetic and specialized Fisher access. ATTEMPTS/009 parks norm compression after the completed constant-class calculation. L033's critical audit is not a duplicate of this new L034 audit: it did not check the degree-twelve norm or scalar. A single critical verification of this fresh calculation is justified, but successful verification does not reopen the exhausted compression mechanism. No additional Fisher retrieval, class/unit computation or source retry is needed for this target.

Continue the audit only if every load-bearing assertion can be independently verified or an exact defect can be exhibited and repaired. A confirmed constant class leaves compression parked; an uncovered essential theorem requires a separate literature gate. A future mechanism needs a concrete independently testable target and its own assessment. The original global/local descent intersection, four other twists, and infinitely many signatures remain unresolved. No new lemma or mathematical calculation is made in this source review.

Mathlib: full matching modular-norm, determinant-specialization and FNS map coverage remains not checked. This is unknown availability, not absence.
