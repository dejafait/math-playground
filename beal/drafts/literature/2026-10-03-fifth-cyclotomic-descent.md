# Fifth-cyclotomic descent literature assessment

TARGET: Test whether the complete cyclotomic factor allocation for a^5+b^5=c^7, including the shared prime 5, yields a height-decreasing descent for primitive positive solutions.
CHECKED: 2026-10-03
DECISION: IMPORT
SEARCH_EVIDENCE: Searched "x^5 + y^5 = z^7", "generalized Fermat" "(5,5,7)", and fifth-cyclotomic descent variants; followed the Dahmen–Siksek match to the publisher's full paper, then searched its exact title with "erratum" and "correction". Queries, read scope, and access qualifications are recorded below.
SOURCE_EVIDENCE: Dahmen–Siksek, Acta Arithmetica 164 (2014), 65–100, DOI 10.4064/aa164-1-5; publisher PDF https://www.impan.pl/shop/publication/transaction/download/product/83637 ; Theorem 1, p. 67, Lemma 2.2 and Section 3, pp. 69–78, read; numbered statement cross-checked in https://arxiv.org/html/1309.4030v2 .
COMPARISON: Theorem 1 reaches the required zero-solution threshold at (5,5,7), including the shared-prime case, without a height bound or conditional hypothesis. It does not certify the proposed height-decreasing map; an independent descent would reproduce an already covered exclusion.
GAP: The citation-backed notebook application, its placement checks, and L002 divisor consequences remain unwritten. Uniform emptiness of all other residual signatures remains missing. The proposed descent itself has neither been constructed nor refuted.
REASON: The read primary classification suffices for the saved target's downstream exclusion. Replace the proposed reproof with the screened application; no changed hypotheses, effective constants, or independent computational implementation are needed for that application.
SCOPE: Import only the ell=7 clause of Theorem 1 for signed coprime integer coordinates, retaining nonzero coordinates and all positive base-one cases; approve the three placements and their L002 divisor extensions, with explicit sign and primitivity checks in the research turn.
COVERED_TARGET: Import Dahmen–Siksek's Theorem 1 to exclude all three placements of (5,5,7), including their exponent-divisor extensions through L002.

## Relevance and discriminating test

The main gap remains uniform emptiness of residual signatures. Excluding positive primitive solutions at the displayed signature would close one different part of that gap and would transfer to original signatures with 5 dividing both summand exponents and 7 dividing the right-hand exponent through L002. Other placements would need their own sign and positivity checks; none is preapproved by this target.

The proposed intermediate result is a map from every putative primitive positive solution at this signature to another such solution with strictly smaller positive integer height H=max(a,b,c), or a contradiction within the complete allocation. A complete map would justify infinite descent. A single factor being a seventh power, local restrictions, or mere restatement as ideal powers would not meet this threshold. A bounded test must expose the missing descent relation if it cannot produce the required map; changing route names or repeating allocation alone cannot renew the exploration budget.

The mechanism would use the fifth-cyclotomic factors and their shared prime 5, rather than the already stopped isolated quadratic-factor or exceptional-prime tests for repeated cubes. Those failures remain relevant cautions: all factor conditions must be retained simultaneously. No fifth-cyclotomic factorization, valuation lemma, class-number assertion, or descent calculation is derived in this literature turn.

The source test was an unconditional classification with zero nonzero coprime integer solutions, unrestricted bases, and both cases at 5. A first-case theorem, isolated factor-power constraint, fixed-signature finiteness, or finite-height search would fall short. The inspected classification meets this test. A citation suffices for the limited exclusion, while no inspected result is claimed to provide the particular descent map. Do not continue that reproof without a distinct useful target and its own assessment.

## Primary source and read scope

Sander R. Dahmen and Samir Siksek, *Perfect powers expressible as sums of two fifth or seventh powers*, **Acta Arithmetica 164(1) (2014), 65–100**, [DOI](https://doi.org/10.4064/aa164-1-5), [publisher PDF](https://www.impan.pl/shop/publication/transaction/download/product/83637). Read the introductory definitions and Theorems 1–3, pp. 65–67, Lemma 2.2 and its proof, p. 69, and the complete Section 3, pp. 69–78. These are the published page numbers, not PDF page indices.

For ell in {7,19}, Theorem 1 classifies coprime signed solutions of x^5+y^5=z^ell as (1,-1,0), (-1,1,0), (1,0,1), (-1,0,-1), (0,1,1), and (0,-1,-1). Each has a zero coordinate. Theorem 3's GRH qualification concerns different exponents.

Lemma 2.2 retains the possible common factor 5 and its exact valuation in H_5. Lemma 3.1 and Proposition 3.2 handle 5 not dividing z through C_7: Y^2=20X^7+5 and Chabauty–Coleman. Proposition 3.3 handles 5 dividing z by a modular argument; Lemma 3.12 supplies an alternative for ell=7. Thus neither branch is an unread essential case. Rank and trace computations use MAGMA and are not independently rerun here. Remark 3.4's conditional discussion is not an added hypothesis of Theorem 1.

The [arXiv record](https://arxiv.org/abs/1309.4030) identifies v2, submitted 26 January 2014, as incorporating referee comments; its [HTML theorem statement](https://arxiv.org/html/1309.4030v2#Thmtheorem1) was cross-checked. The [publisher landing page](https://www.impan.pl/pl/wydawnictwa/czasopisma-i-serie-wydawnicze/acta-arithmetica/all/164/1/83637/perfect-powers-expressible-as-sums-of-two-fifth-or-seventh-powers) confirms the bibliographic identity. The journal text is the source used for page numbers and proof-case coverage.

## Search record and qualifications

Initial exact-equation and signature queries returned this paper directly. Follow-up queries were `"Perfect powers expressible" "Theorem 1"`, `"x^5+y^5=z^7" "descent"`, `"x^5+y^5=z^7" "cyclotomic"`, and the full title paired separately with `"erratum"` and `"correction"`. No correction to the imported clause was identified in this bounded search; this is not a guarantee that no correction exists, or a novelty claim.

The author-hosted [PDF lead](https://www.few.vu.nl/~sdn249/SumsOfPowers.pdf) returned HTTP 403, but the complete publisher PDF was accessible. An attempted shell download of the publisher copy failed DNS resolution; the web retrieval supplied the text. Neither failure blocks the inspected theorem. Search excerpts, secondary summaries, unrelated coefficient equations, and the equation x^5+y^5=7 over rationals are not theorem evidence for this target.

The paper's external MAGMA scripts and the references underlying its descent and modular computations were not independently inspected or executed. The application imports the published theorem, so an independent reproduction is not required; none is claimed. Sections 4–5 and their additional signatures are not imported or preapproved by this assessment.

## Notebook comparison and continuation decision

L002, C002a, foundations/01-target-and-scope.md, and Attempts 001–004 were reread. The Cohen boundary import and the repeated-cube exclusions do not cover this signature. C002a explicitly calls (5,5,7) residual only relative to its own assembled inputs. The local-solubility, single-factor, exceptional-prime, and primitive-divisor failures remain preserved and do not undermine this different global theorem.

The screened application requires the direct placement, an odd-fifth-power sign change when the singleton seven is a summand, and a summand swap. The cited source permits signed coordinates. The equation's existing primitivity convention and L002's preservation of prime support supply the other applicability checks; the actual application will be written during research. No additional exponent or placement is silently imported from the paper.

This review supplies new overlap evidence and changes the route from an independent descent to a known-theorem application. Record **NEGATIVE** for redundancy of that reproof, not for failure of every descent or for a disproof of Beal. The mathematical assembly has not changed this turn. A subsequent imported exclusion would close the limited signature gap while leaving unrelated mixed signatures and the repeated-cube complement unresolved. Exploration usage remains 0/3; literature review has spent no calculation turn.

## Mathlib

Coverage of the full target and supporting fifth-cyclotomic, Chabauty, and modular results: **not checked**. The named paper results and direct links above identify mathematical sources, not matching Mathlib declarations or formal verification. No library absence claim is made.
