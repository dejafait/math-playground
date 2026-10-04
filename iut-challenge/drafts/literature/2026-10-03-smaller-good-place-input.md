# Smaller good-place input — completed source assessment

TARGET: Test whether hull(G(beta^(-1) T union J)) is contained in hull(I/4) at a = 1 and beta = 1 tensor 2sqrt(2) for the same K = Q_2(sqrt(2)) packet, retaining the smaller region from Dupuy–Hilado (6.4).
CHECKED: 2026-10-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the completed hull-transport and canonical-beta searches; searched the exact (6.4) input, smaller-region terminology, tensor log-shell orbit bounds, corrections and primitive-vector orbits. The bounded screen supplied no independently justified match for the fixed smaller-input comparison; failed searches establish no novelty.
SOURCE_EVIDENCE: Read continuous passages of Dupuy–Hilado arXiv:2004.13108v2, Theorem 2.8.1 and Remark 2.8.2, pp. 9–10; Lemma 4.2.3 and §4.3, pp. 17–18; §§6.1–6.3, pp. 18–22, especially (6.3)–(6.8) and Remark 6.2.1. Reused the version-qualified native IUT IV and RIMS1968 readings in the prior assessments; source and access qualifications are below.
COMPARISON: The displayed deduction reaches the smaller-input bound through the enlarged (6.5) region, whose unit-scalar transition L008 disproves. That does not decide (6.4) directly. Known conductor, preserved-lattice and shell statements support an exact verification but do not supply this sharper fixed-packet bound on its own.
GAP: Decide the full G-orbit hull of beta^(-1) T union J against hull(I/4), keeping the literal smaller input and canonical beta. The unit-scalar extension, full U, final enclosure and original normalized A/B remain distinct obligations.
REASON: SPECIALIZE covers verification of the suspect deduction on its smaller input using known definitions and existing packet data. A citation to the failed enlargement is insufficient, and reproof of the native enclosure would duplicate covered results. No smaller-input calculation is performed in this literature turn.
LITERATURE_REASON: The changed input beta^(-1) T union J replaces beta^(-1) I; its exact source scope and strongest known enclosure required assessment beyond the preceding enlarged-lattice coverage.
SCOPE: The same fixed K = Q_2(sqrt(2)), L = K tensor K packet, Definition 4.3.1 log-shell, T = O_K tensor O_K, J = log(O_K^times) tensor log(O_K^times), a = 1, beta = 1 tensor 2sqrt(2), G = Aut(L : I), and field-component hull. Covers the whole-group smaller-input test only; excludes initial-theta-data realization, full Ind3, packet permutations, global transport and normalized A/B identification.
COVERED_TARGET: Test whether hull(G(beta^(-1) T union J)) is contained in hull(I/4) at a = 1 and beta = 1 tensor 2sqrt(2) for the same K = Q_2(sqrt(2)) packet, retaining the smaller region from Dupuy–Hilado (6.4).

## Preserved initial assessment boundary

This file was created on 2026-10-03 with REVIEW_REQUIRED after the mathematical turn changed the input. That turn read no new source and authorized no smaller-input calculation. Its relevance test is retained: determine whether L008's failure affects the smaller region or arises only from enlarging it. The separate screen is completed below; no orbit, new exponent or smaller-input radius is derived here.

## Gap, relevance and required threshold

The main gap remains finite B >= A at IUT III, Corollary 3.12, step (xi-f), as fixed in [the comparison source record](../../foundations/02-comparison-claim-and-sources.md). A correct local enclosure could contribute to control of the output volume, while an auxiliary error would matter only after its necessity to the original argument is established. No local containment by itself supplies pilot identification or the global normalized inequality.

The proposed intermediate target retains the smaller source region instead of repeating the decided enlarged-lattice test. [L007](../../lemmas/L007-tensor-log-shell-rounding-depends-on-beta.md) supplies the exact log-shell, tensor order, conductor admissibility and primitive-vector argument for reuse. [L008](../../lemmas/L008-canonical-beta-rounding-fails-at-unit-scalar.md) supplies the enlarged-lattice failure and the rounded container's already established component radii 32. Its radius 64 is for a superset, not an achieved bound or witness for this target. [ATTEMPTS/008](../../ATTEMPTS/008-canonical-beta-enlargement-at-unit-scalar.md) preserves that limitation. Neither the older marking-defect results nor the nonunit favorable-beta test decides the smaller unit-scalar orbit.

The discriminating mathematical test is an exact whole-group comparison with radius 32 in each K component. A positive answer must cover every g in G; sampled matrices are insufficient. A negative answer requires a point of beta^(-1) T union J itself and a permitted g whose image exceeds the container. A witness lying only in beta^(-1) I is insufficient. Once this fixed test is decided, stop it: success limits the enlargement objection, and failure would motivate a separately justified comparison with the final enclosure. Neither answer demonstrates an essential IUT flaw.

## Search and version record

Reused [the completed unit-scalar assessment](2026-10-03-good-place-canonical-beta.md) and [the native proof-use comparison](2026-10-03-hull-transport-screening.md), including their correction searches and exact named supporting statements. New queries on 2026-10-04 were:

- `"Dupuy" "Hilado" "6.4" hull`;
- `"2004.13108" "beta" "hull"` and `"2004.13108" "6.4" correction`;
- `"Dupuy" "Hilado" "smaller region"`;
- `"log-shell" "smaller" "automorphisms"` and `"log-shell" "automorphisms" "tensor" "hull"`;
- `"GL_n" "Z_p" "orbits" "primitive" vectors`, restricted to arXiv, MathOverflow, Cambridge and EMS for discovery only.

The [arXiv record](https://arxiv.org/abs/2004.13108) still lists v2, submitted 2020-04-29; the PDF title page prints April 30, 2020 and the PDF has 36 pages. Equation numbers and printed page numbers here refer to that PDF. Continuous extracted passages, including the justifications following the display, were read. Requests for PDF-page screenshots returned references without readable images; no visual authentication or silent repair of the source's displayed final-radius formula is claimed.

No applicable exact theorem or correction was located in these additional searches. Discussion sites, mirrors and the LANA IUT repository were discovery hits, not theorem or Mathlib evidence. A [Yamashita institutional manuscript lead dated by its filename 2024-06-25](https://www.kurims.kyoto-u.ac.jp/~gokun/DOCUMENTS/abc2024Jun25.pdf) appeared in the broader enclosure search; opening it returned an internal error. Its statements and version were not inspected, so no theorem is imported from its snippet. This is a nonessential supplemental lead, not a blocker for the independently testable local target. The previously blocked Ind3 and pilot/quotient sources were not retried.

## Inspected statements and applicability comparison

[Dupuy–Hilado v2](https://arxiv.org/pdf/2004.13108v2#page=20), (6.4)–(6.8), printed p. 20, contains the literal union and the intervening enlargement. [Remark 6.2.1(1)–(3)](https://arxiv.org/pdf/2004.13108v2#page=20), pp. 20–21, proposes direct basis/index calculations and a smaller containing region, but supplies no such result. The source's own chain is therefore the closest claimed sharper comparison; its use of the enlarged region cannot be imported as an independent verification after L008.

The supporting conductor statement is [Theorem 2.8.1 with Remark 2.8.2](https://arxiv.org/pdf/2004.13108v2#page=9), pp. 9–10. [Definition 4.3.1 and Lemma 4.3.2](https://arxiv.org/pdf/2004.13108v2#page=17), pp. 17–18, fix the log-shell and its containment inputs. These are cited inputs, not a matching orbit theorem. Lemma 4.2.3(2)'s small-ramification hypothesis fails for this packet. [Section 6.2](https://arxiv.org/pdf/2004.13108v2#page=19) assumes |a|_p < 1 and omits packet permutations. [Section 6.3 and Lemma 6.3.1](https://arxiv.org/pdf/2004.13108v2#page=21), pp. 21–22, use a = 1 elsewhere and refer back to that computation; their initial-data region and final container differ from this test. Agreement of one scalar is not original applicability.

The strongest applicable native supporting result remains **IUT IV, Proposition 1.2(ii), with Proposition 1.4(iii)**, recorded in [the native enclosure citation](../../foundations/04-native-local-enclosures.md). The April 2020 source, printed pp. 9–14, and its proof-use comparison were read in the earlier assessment and are reused without a new retrieval. Its preserved-logarithm-lattice hypothesis matches the packet's local group, as already checked there. Its maximal-order input, fractional-scaling qualifications and native container do not by themselves prove the sharper union-to-hull(I/4) assertion. No new specialization of its exponents is performed. The author's PDF and the readable reproduction were not checked for byte identity; that access qualification is preserved.

The other reused primary input is **Mochizuki, November 2022 RIMS1968, Example 3.5.1(i)**, printed p. 100, [direct source](https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1968.pdf#page=101). It gives preservation of integer-power lattice shells. Parts (ii)–(iii) concern a single field and odd p and do not cover this tensor packet at p = 2. This supplies an orbit constraint, not the position of the smaller region relative to those shells. The preceding assessment records the continuous reading and version; re-reading it would not resolve the changed input.

Thus existing conductor and lattice theorems cover the setup and safe enclosure mechanisms, while the exact placement of the smaller input and its component hull remain to verify. The full statement is not absent from mathematics merely because this bounded search did not locate an adequate match. No new theorem, counterexample or numerical bound is imported, reproduced or established beyond the checked literature in this turn.

## Assessment and continuation decision

**SPECIALIZE:** sufficient coverage for the unchanged TARGET and identical COVERED_TARGET. Verification of the suspect claim on the literal smaller input is justified; reproof of known native estimates and a repetition of L008 are not. No essential unread source is needed within this local scope. The separately blocked full-theory sources remain relevant to any eventual extension, outside this coverage.

The next mathematical attempt may reuse the exact packet data and standard lattice action to decide the full orbit, with an informal proof of the universal bound or a genuine smaller-input witness. It must keep the component hull, the canonical beta and both branches of the union. It must not infer failure of the final Lemma 6.3.1 enclosure, original indeterminacies or finite B >= A from this diagnostic alone.

Completed-step classification: **NOVELTY_UNCHECKED**. Outcome: **EXPLORATION**, because this is the first theorem-level comparison for the changed input and yields ready coverage, not a mathematical advance or repeated stop review. The two informative mathematical negatives and 0/3 uninformative mathematical exploration turns are retained; this literature turn spends none. The older 3/3 defect/quotient sequence stays parked. No candidate resolution is claimed.

## Mathlib

Full smaller-input orbit-hull statement: **not checked**. Supporting local-field, lattice-action and hull coverage: **not checked**. The named primary references above distinguish supporting results from a match for the full statement; neither search hits nor repository descriptions establish Mathlib coverage or formal verification.
