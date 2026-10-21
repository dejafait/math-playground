# Uniform-scalar coarse enclosure — completed scope assessment

TARGET: Assess whether the separate post-chain coarse enclosure in Dupuy–Hilado arXiv:2004.13108v2 §6.2 contains the full orbit of a(O_K union log(O_K^times)) for every a in K with 0 < |a|_3 < 1, keeping K = Q_3(pi), pi^9 = 3, beta = 1 and G = Aut_(Z_3)(log(O_K^times)/6).
CHECKED: 2026-10-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the fixed-endpoint and native-enclosure assessments; searched the paper identifier with scalar/enclosure and hull/errata terminology, plus log-shell scalar enclosure, with primary-domain follow-ups. No independent full match or correction was found; search failure does not establish novelty.
SOURCE_EVIDENCE: Read arXiv:2004.13108v2 PDF §§4.2–4.3 and 6.1–6.2, printed pp. 17–20, especially Lemmas 4.2.3/4.3.2, Remark 4.3.3, (6.3)–(6.8), the unnumbered coarse enclosure, and Remark 6.2.1(1); reused the version-qualified IUT IV Proposition 1.2(ii)/1.4(iii) record. The arXiv record still lists v2 dated 2020-04-29.
COMPARISON: The toy scalar hypothesis covers arbitrary strict nonunits, but the coarse assertion is justified by the same transport chain already under audit. Supporting log-image and native order-input enclosures do not independently establish this exact uniform saturated-union bound. Remark 4.3.3 specifically cautions against treating the log image as an O_K-module.
GAP: Independently verify uniform coarse containment for both literal branches and the whole lattice group, including arbitrary unit factors and scalar-floor boundaries; L013 covers only a = pi.
REASON: Import covered definitions and supporting estimates, then specialize only the missing uniform comparison using L012's exact field/lattice data. This is a scope change with a concrete independent test, not a reproof of an adequate theorem or a claim that the source's coarse assertion has already been refuted.
LITERATURE_REASON: The scalar quantifier changed from a = pi to every strict nonunit; the prior assessment expressly excluded higher scalar powers and did not screen arbitrary units.
SCOPE: Fixed one-factor K = Q_3(pi), pi^9 = 3, beta = 1, J = log(O_K^times), I = J/6, full Q_3-linear extension of Aut_(Z_3)(I), and all nonzero a of strict norm below one. Covers independent coarse containment only; excludes changes of field, conductor, packet, original theta data, Ind3 identification, full IUT images, formal quotients and normalized A/B.
COVERED_TARGET: Assess whether the separate post-chain coarse enclosure in Dupuy–Hilado arXiv:2004.13108v2 §6.2 contains the full orbit of a(O_K union log(O_K^times)) for every a in K with 0 < |a|_3 < 1, keeping K = Q_3(pi), pi^9 = 3, beta = 1 and G = Aut_(Z_3)(log(O_K^times)/6).
COVERED_TARGET: Prove or refute uniform containment of G(a(O_K union log(O_K^times))) in the separate post-chain coarse enclosure of Dupuy–Hilado arXiv:2004.13108v2 §6.2 for every a in K with 0 < |a|_3 < 1, using K = Q_3(pi), pi^9 = 3, beta = 1 and G = Aut_(Z_3)(log(O_K^times)/6), and explicitly controlling arbitrary unit factors.

## Source version, search and reuse

The [arXiv record](https://arxiv.org/abs/2004.13108) lists v1 on April 27 and v2 on April 29, 2020. The [36-page v2 PDF](https://arxiv.org/pdf/2004.13108v2) prints April 30, 2020. All numbering here is its printed numbering. Continuous extracted PDF statements were read; no new visual authentication is claimed. An attempted experimental HTML opening supplies no additional evidence used in this assessment.

Queries included `"2004.13108" "scalar" enclosure`, `"Dupuy" "Hilado" "enclosure" correction`, and primary-domain queries `"2004.13108" "hull" "errata"` and `"log-shell" "scalar" "enclosure"` restricted to arXiv, UVM and/or Kyoto RIMS. Broad results were irrelevant or discussion threads and supply no mathematical inputs; primary-domain follow-ups were empty. No absence of corrections or certified originality follows. The [completed endpoint assessment](2026-10-04-odd-prime-final-container.md) supplies adequate previous challenge-scope and supporting source coverage; the parked Ind3 and March 2024 exposition interiors are not premises for this independent local question.

## Exact comparison and known coverage

[Section 6.2, printed pp. 19–20](https://arxiv.org/pdf/2004.13108v2#page=19), permits a scalar in the last finite extension with strict norm below one. It defines its automorphisms by extending normalized Z_p-lattice automorphisms Q_p-linearly. The one-factor specialization and beta = 1 conductor choice were already screened; changing only the scalar does not add an original initial-theta-data realization.

The relevant container is the unnumbered post-chain prescription on [printed p. 20](https://arxiv.org/pdf/2004.13108v2#page=20):

\[
C_{\rm coarse}(a)=D_L\left(0,\frac{\prod_i e_i}{|2p|_p}p^{-\lfloor v_p(a)+\|\mathrm{diff}\|_\infty-\|\mathrm{diff}\|_1\rfloor}\right).
\]

This is a transcription, not a new specialization or proof. Retain its p-adic denominator and floor, separately from (6.2) and the literal (6.8). L013 already establishes equality with this container at a = pi, with achieved and required coarse radius 27; its literal terminal radius 54/(exp(1) ln3) is smaller. That equality does not answer the uniform scalar quantifier.

The source presents its coarse conclusion after (6.3)–(6.8), rather than with a separate proof bypassing the transport under audit. Citing that assertion as the justification for this audit would assume the disputed comparison. Conversely, failure of the stronger rounded step is not a refutation of the larger coarse container. The next test must use the actual union and its full orbit, not the enlarged aI input as a substitute.

[Lemma 4.2.3(1), p. 17](https://arxiv.org/pdf/2004.13108v2#page=17), provides a general log-image disc bound. Its small-ramification part (2) is outside this wild packet's hypotheses. [Definition 4.3.1 and Lemma 4.3.2, pp. 17–18](https://arxiv.org/pdf/2004.13108v2#page=17), supply shell normalization and containment of the order and log image. These support the setup, not the saturated scalar-union comparison. Remark 4.3.3, p. 18, expressly distinguishes Z_p-module structure from O_K-module structure; no arbitrary field-unit preservation of J or I may be assumed. Ordinary scalar homogeneity of unsaturated hulls in §6.1 likewise does not justify commuting a field scalar through every Q_p-linear lattice automorphism.

The [native citation record](../../foundations/04-native-local-enclosures.md) retains IUT IV Proposition 1.2(ii) and Proposition 1.4(iii), April 2020 formulation, printed pp. 9–14, as previously read in a version-qualified reproduction. They enclose images of scaled maximal orders with different/logarithm corrections. That is supporting coverage for an order branch, with corrections intact, not a matching uniform theorem for the literal log branch and this coarse radius. No new application or computation of their exponents is made here. No new essential source is unread within the present local scope.

## Relevance, bounded test and stopping decision

The main gap remains finite B >= A under the original IUT III Corollary 3.12 hypotheses. The intermediate target is robustness of the auxiliary surviving coarse enclosure in this one field. A proof would park this field's coarse-bound objection while preserving L013's literal-endpoint failure. A violating scalar with an exact witness would strengthen the local diagnostic. Neither closes original theta-data, pilot transport, complete-image, essentiality or normalization bridges.

This differs from the stopped universal sharp-rounding mechanism and the completed fixed endpoint comparison. L007–L011 concern other inputs or fields, and L012–L013 provide exact reusable data only in this field at the fixed scalar. No new logarithm computation or repeated search for those known inputs is needed.

The next mathematical step may seek a uniform lattice enclosure from the existing exact logarithm ideal and valuation bounds, then compare its G-saturation with the printed coarse container. A reduction by rational powers of 3 or to finitely many valuation intervals is permitted only with a proof that covers every unit factor; testing pure pi-powers alone cannot settle the quantifier. An exact upper bound covering both branches and all g proves containment; a literal-input point, I-preserving automorphism and strict radius violation refute it. Either result ends this fixed-field uniform diagnostic. If an exact sharp orbit is unnecessary for containment, do not enlarge the task to computing it.

## Completed-step boundary

This review approves the exact listed mathematical target as SPECIALIZE. It derives no scalar enclosure, orbit, radius or new lemma. Outcome is EXPLORATION: the first uniform-scope comparison resolves the gate and identifies the unit-module trap and a bounded independent test. Classification is NOVELTY_UNCHECKED; known definitions and supporting statements are reused, and no progress beyond the checked literature is claimed. The seven informative mathematical negatives and 0/3 uninformative mathematical exploration count are unchanged; literature spends no calculation budget.

## Mathlib

Full uniform-scalar statement and supporting library coverage: **not checked**. The named primary results are supporting citations, not matching Mathlib theorems or formal verification. No absence from Mathlib is inferred.
