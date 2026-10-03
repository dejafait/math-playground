# Good-place scalar with canonical beta — completed source assessment

TARGET: Test the same K = Q_2(sqrt(2)) tensor packet with the good-place scalar a = 1 and canonical beta = 1 tensor 2sqrt(2), determining whether Dupuy–Hilado (6.5)–(6.6) still bounds the full log-shell automorphism orbit.
CHECKED: 2026-10-03
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the completed hull-transport searches and native proof-use comparison; searched the changed scalar, exact quadratic packet, rounding/orbit terminology and corrections, checked the arXiv version record and author lists, and followed the lattice-shell lead to RIMS1968, Example 3.5.1. No inspected source settles the exact changed-scalar test; failed searches establish no novelty.
SOURCE_EVIDENCE: Read arXiv:2004.13108v2, Theorem 2.8.1, pp. 9–10; §§4.1–4.3, pp. 16–18; §§6.1–6.3, pp. 18–22; and §1, p. 2. Read November 2022 RIMS1968, Example 3.5.1(i)–(iii), pp. 100–101. Reuse the version-qualified April 2020 IUT IV readings and native enclosure citation from the completed hull assessment.
COMPARISON: Known shell preservation and native enclosures do not identify the orbit hull of the auxiliary enlarged lattice with the rounded hull. L007 supplies the exact lattice and beta admissibility for reuse, but its tested scalar differs. The changed packet remains a local diagnostic rather than an established initial-theta-data instance.
GAP: Verify the fixed canonical-beta transition at a = 1 after the full local lattice-automorphism orbit, distinguishing an intermediate rounding failure from failure of a final enclosure or the original normalized comparison.
REASON: The scalar is outside §6.2's strict hypothesis, but §6.3 explicitly uses it and refers back to that computation. This supports testing the extension locally without asserting full §6.3 applicability. Import the covered inputs; only the changed-scalar verification remains mathematical work for a later turn.
LITERATURE_REASON: Changed hypothesis a = 1 replaces the nonunit a = 1 tensor sqrt(2), aligning with the source's other-place scalar while leaving the log-shell and canonical beta fixed; §6.2 and §6.3 have different scalar hypotheses whose applicability must be compared.
SCOPE: The fixed K = Q_2(sqrt(2)), L = K tensor K packet, Definition 4.3.1 log-shell normalization, canonical beta, its two previously checked constraints, and G = Aut(L : I). Covers verification of the displayed intermediate hull comparison. Does not cover realization in initial theta data, Ind3, permutations between packets, a final all-image enclosure, global pilot transport or normalized A/B identification.
COVERED_TARGET: Test the same K = Q_2(sqrt(2)) tensor packet with the good-place scalar a = 1 and canonical beta = 1 tensor 2sqrt(2), determining whether Dupuy–Hilado (6.5)–(6.6) still bounds the full log-shell automorphism orbit.

## Relevance, redundancy and required threshold

The main gap is still finite B ≥ A in the [comparison source record](../../foundations/02-comparison-claim-and-sources.md). An exact enclosure of the relevant local image family could help control the output contributing to B; an auxiliary error would matter only after its necessity and original applicability are established. This review supplies no new radius, volume inequality or candidate essential IUT flaw.

The [preceding assessment](2026-10-03-hull-transport-screening.md) and [L007](../../lemmas/L007-tensor-log-shell-rounding-depends-on-beta.md) are reused. The analytic logarithm lattice, tensor decomposition and both constraints on this beta are already established locally; repeating them is unnecessary. [ATTEMPTS/007](../../ATTEMPTS/007-beta-only-saturated-rounding-objection.md) stops a failing beta choice as an objection to an existential estimate. Fixing the source's derivative choice removes that ambiguity from this one test, while changing a avoids repeating the completed packet. It does not exclude other favorable choices in a final existential bound.

The exact future test is hull(G(a beta^(-1) I)) contained in hull(G(p^floor(v_p(a) - v_p(beta)) I)), with the hull taken in the field components and G the whole local lattice-automorphism group. This is the source's intermediate comparison, not the complete region U or finite B ≥ A. No exponent, matrix, orbit or hull for the changed scalar is computed here.

## Search and version record

The bounded search on 2026-10-03 included:

- `"Dupuy" "Hilado" "a = 1" hull` and `"Q_2" "sqrt(2)" "log-shell"`;
- `"2004.13108" "log-shell" automorphism correction` and `"Probabilistic Szpiro" "hull" correction`;
- `"log-shell" "automorphisms" "rounding"`, `"log-shell" "lattice" "orbit" "Mochizuki"`, and `"log-shell" "small" ramification`;
- `"Dupuy" "Hilado" "Szpiro" "errata"` and an arXiv/author-domain search for `"2004.13108" correction`;
- an institutional-domain search for `Mochizuki "Example 3.5.1" "log-shell" automorphism`.

Many results were irrelevant, discussion pages or copies. They were not used as mathematical evidence. The last query supplied a readable primary lattice example. The [arXiv record](https://arxiv.org/abs/2004.13108) still lists v2, submitted 2020-04-29; the PDF prints April 30, 2020. [Dupuy's manuscript list](https://tdupu.github.io/papers.html) links this paper without a separate correction. No relevant erratum was located in this screen or the reused assessment; this is not evidence of its absence.

## Primary statements read and their coverage

[Dupuy–Hilado v2](https://arxiv.org/pdf/2004.13108v2#page=19), §6.2, assumes |a|_p < 1 and uses all I-lattice automorphisms. Its footnote 7 excludes packet permutations from that model. [Section 6.3 and Lemma 6.3.1](https://arxiv.org/pdf/2004.13108v2#page=21) set a = 1 away from the selected bad multiplicative places and refer the proof back to §6.2 with specialized a and beta. Thus the saved test concerns that extension; it is outside the literal §6.2 hypothesis.

[Theorem 2.8.1 and Remark 2.8.2](https://arxiv.org/pdf/2004.13108v2#page=9) provide the derivative-based conductor element and allow choosing the omitted factor. [Definition 4.3.1, Lemma 4.3.2 and Remark 4.3.3](https://arxiv.org/pdf/2004.13108v2#page=17) supply the normalization and inclusions but caution against assuming an O_K-module structure. Section 4.1.2 and Lemma 4.2.3(2) use the small-ramification condition e < p - 1; it does not apply to the saved packet. [Section 1, footnote 1](https://arxiv.org/pdf/2004.13108v2#page=2) excludes residue characteristic 2 from the selected bad places. Equality of the scalar with the other-place value establishes no initial-data realization.

Read [Mochizuki, RIMS1968, Example 3.5.1(i)–(iii), printed pp. 100–101](https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1968.pdf#page=101), as continuous primary text. Its title and cover specify **November 2022**: 156 printed pages plus an institutional cover, 157 PDF pages. Part (i) states, for a finite free Z_p-lattice M, that its automorphisms preserve every shell U(M,n) = p^n M minus p^(n+1) M. Parts (ii)–(iii) give field-dependent bounded valuation discrepancy for a single-field log-shell, with **p odd**. These are supporting known results, not an exact uniform rounding theorem for the tensor packet at p = 2. Shell preservation alone supplies neither the coordinates of the enlarged lattice nor its field-component hull. Cite the covered statement rather than present shell preservation as a new finding.

This reading uses only the older example for its qualified elementary statement. The [author's list](https://www.kurims.kyoto-u.ac.jp/~motizuki/papers-english.html) still dates the Essential Logical Structure update 2024-03-24. The older PDF is not substituted for those current quotient passages; the [parked quotient assessment](2026-09-27-formal-quotient-source-recovery.md) remains blocked and was not retried.

The strongest applicable native container remains [IUT IV, Proposition 1.2(ii), with Proposition 1.4(iii)](../../foundations/04-native-local-enclosures.md), under the preserved-logarithm-lattice hypotheses and the source's allowed fractional exponents. Their version-qualified proof-use comparison is already complete in the preceding assessment. They bound the input a O_L; they do not prove the proposed bound on the auxiliary a beta^(-1) I. Import these named estimates by citation, without reproof. No specialized native bound at the changed scalar is derived this turn.

The [official July 7, 2023 announcement](https://zen.ac.jp/news/0ul6zqed9-0) was rechecked. Its inherent-flaw target agrees with the existing challenge record. Eligibility and adjudication supply no mathematical input.

The PDF passages were read as continuous extracted text. Screenshot requests supplied references without readable image content; no visual authentication or silent correction of the other displayed formulas is claimed. No essential unread source gates this local comparison. The separate Ind3 manuscript and full initial-data realization are outside its ready scope.

## Decision and continuation test

**SPECIALIZE:** source definitions, admissibility inputs, shell preservation and native bounds are covered. The remaining work verifies the exact changed-scalar auxiliary transition, rather than reproving those inputs or assuming the disputed transition as a theorem. No inspected result is a full match for this test, and the bounded search warrants no novelty claim.

Continue with the saved calculation under this assessment. Success would settle this one extension and limit the earlier objection's scope. Failure with the fixed canonical beta would identify an intermediate numerical issue, but would not automatically refute Lemma 6.3.1's final enclosure: its input region and final container must be distinguished from the enlarged intermediate lattice and rounded hull. Neither outcome establishes original initial-theta-data applicability, transport of the distinguished pilot, the full indeterminacy family or normalized B ≥ A. Stop this fixed-packet test once its exact orbit comparison is decided; further claims require their own applicability evidence.

STEP classification for this completed review: **NOVELTY_UNCHECKED**. Known statements are retained by citation; no changed-scalar specialization, reproduction or result beyond the checked literature is established. Outcome: **EXPLORATION**, a completed new source screen with ready mathematical coverage, not an ADVANCE or a repeated stop review. This literature turn consumes no mathematical exploration turn, and the older blockers remain parked.

## Mathlib

Full changed-scalar tensor-orbit statement: **not checked**. Supporting p-adic logarithm, different, tensor decomposition and lattice-action coverage: **not checked**. The direct named citations above distinguish supporting results from a match for the full statement; they are not claims of a Mathlib theorem or formal verification.
