# Fifth-power/nineteenth-power import assessment

TARGET: Import Dahmen–Siksek's Theorem 1 to exclude all three placements of (5,5,19), including their exponent-divisor extensions through L002.
CHECKED: 2026-10-03
DECISION: IMPORT
SEARCH_EVIDENCE: Searched "Dahmen" "Siksek" "19" "Theorem 1" and "x^5+y^5=z^19" solutions; reused the earlier exact-title correction search and followed the primary match to the publisher PDF and arXiv v2. The read scope and bounded-search limits are recorded below.
SOURCE_EVIDENCE: Dahmen–Siksek, Acta Arithmetica 164(1) (2014), 65–100, DOI 10.4064/aa164-1-5; Theorem 1, p. 67, and its ell=19 proof components in Section 3, pp. 69–78, inspected at https://www.impan.pl/shop/publication/transaction/download/product/83637 ; statement cross-checked at https://arxiv.org/html/1309.4030v2#Thmtheorem1 .
COMPARISON: The signed coprime classification has only zero-coordinate solutions and meets the required zero-nonzero-solution threshold at ell=19, with unrestricted bases, base-one cases, both branches at 5, and no GRH hypothesis. The prior ell=7 assessment alone did not authorize this target; the additional source-scope check now does.
GAP: The notebook application to all three placements and the L002 divisor extensions remains unwritten. Uniform emptiness of the other residual signatures remains missing. This review changes source readiness, without adding an assembled (5,5,19) exclusion.
REASON: Import the published theorem with an explicit applicability argument next turn. No changed hypotheses, effective constants, or independent computation require reproducing the genus-nine or modular proof.
SCOPE: Only the ell=19 clause of Theorem 1, with signed coprime nonzero integer coordinates, all positive base-one cases, all three placements, and their L002 exponent-divisor extensions. The next research turn must write the placement and primitivity checks; no other signature in the paper is approved here.
COVERED_TARGET: Import Dahmen–Siksek's Theorem 1 to exclude all three placements of (5,5,19), including their exponent-divisor extensions through L002.

## Relevance and continuation test

The main gap is zero positive primitive solutions uniformly over the residual signatures in S^3. The intermediate target is the zero-solution conclusion at the three placements of (5,5,19), with unrestricted bases. Its downstream use is removal of original signatures whose corresponding exponents have these divisors, using L002. That limited conclusion would leave infinitely many mixed signatures and the constrained repeated-cube complement unresolved.

The discriminating source test requires a complete, unconditional signed classification covering both 5 dividing z and 5 not dividing z. A first-case theorem, a conditional rank bound, fixed-signature finiteness, or a height-limited search would fall short. The inspected statement and proof-case coverage pass this test, so the concrete application is approved. A mismatch in signed, nonzero, coprime, or divisor scope during the future applicability proof would stop that application.

L002, C002a, L013, the overview, and Attempts 001–004 were checked for overlap. The assembled exclusions do not yet contain this signature. The prior failures concern unrestricted local tests, a single factor, exceptional-prime lifting, and primitive-divisor multiplicity; none prevents importing this separate global classification. The fifth-cyclotomic descent proposed earlier remains untested. Reproving that descent is unnecessary for this limited exclusion.

## Exact primary statement and version

Sander R. Dahmen and Samir Siksek, *Perfect powers expressible as sums of two fifth or seventh powers*, **Acta Arithmetica 164(1) (2014), 65–100**, **Theorem 1, p. 67**, [DOI](https://doi.org/10.4064/aa164-1-5), [publisher PDF](https://www.impan.pl/shop/publication/transaction/download/product/83637).

For ell=19, the theorem lists the coprime signed solutions of x^5+y^5=z^ell as (±1,∓1,0), (±1,0,±1), and (0,±1,±1), with corresponding signs. All have a zero coordinate. The definitions on p. 65 use nontrivial to mean xyz nonzero. No base-height or first-case restriction occurs in this statement.

The [arXiv record](https://arxiv.org/abs/1309.4030) identifies v2, revised 26 January 2014, incorporating referee comments. Its [numbered theorem](https://arxiv.org/html/1309.4030v2#Thmtheorem1) agrees. The journal version supplies page numbers. Theorem 3's GRH qualification concerns different exponents.

## Proof-case audit and qualifications

Lemma 3.1 and Proposition 3.2, pp. 69–70, cover 5 not dividing z via C_19: Y^2=20X^19+5. Section 3.1, pp. 70–73, supplies its rational-point classification. Table 1, p. 71, and the rank conclusion, p. 72, give rank one without GRH or a finiteness assumption on Sha; Remark 3.4 is separate.

Proposition 3.3, p. 70, covers 5 dividing z. Section 3.2, pp. 73–76, uses modularity, level lowering, and trace comparisons. The exponent-19 case is included; the exceptional modular exponent there is 17.

Section 3.3, pp. 76–78, discusses the alternative curve D_19. Its Table 2 rank bound is conditional on GRH, and p. 78 explains the unresolved obstacles to that alternative. It is not the proof used for the required branch. Import Proposition 3.3 there, rather than a purported completed D_19 Chabauty argument.

These are supporting components of the full matching Theorem 1. The rank, integral, and trace computations are part of the cited published proof. External MAGMA files, including Chabauty55l.m and Modular55l.m, and the referenced algorithms were not independently inspected or rerun; no computational reproduction is claimed. The earlier assessment had read Section 3 for ell=7. This review reuses that coverage and inspects the ell=19 statement, rank and modular coverage, and conditional-alternative distinction specifically.

## Search record and notebook applicability

The two target-specific queries above identified the primary paper. Search snippets and secondary summaries were used only for discovery. The prior exact-title searches with "erratum" and "correction" found no correction; that bounded evidence is reused while the source version is unchanged, without claiming that no correction can exist. No novelty follows from this search.

The publisher PDF and arXiv text were accessible. The author-hosted PDF's earlier HTTP 403 and the earlier shell DNS failure were not retried: neither blocks the accessible primary theorem. No essential source for this citation-based application remains unread. Further signatures in Sections 4–5 are outside this assessment.

The theorem permits the signed coordinates used by L013's existing odd-fifth-power placement method. The equation's existing primitivity convention and L002's prime-support preservation retain coprimality and positive base-one cases. This screens the proposed application; its three explicit identities and divisor argument belong to the next research turn. No ell=19 applicability proof, descent, factor allocation, calculation, or lemma is derived in this turn.

This first target-specific scope review records **EXPLORATION** and **KNOWN_IMPORTED**: a known result is screened for import, with no mathematical assembly gain or claim beyond the checked literature. It is not another review of a stopped approach. Exploration usage remains 0/3 because this literature turn spends no calculation turn. The ready assessment covers the unchanged saved action, so the next turn defaults to that mathematical application.

## Mathlib

Coverage of the full intended exclusion and supporting results: **not checked**. Theorem 1 matches the external signed classification; the numbered proof components support that theorem. The citations and links do not identify matching Mathlib declarations or claim formal verification.
