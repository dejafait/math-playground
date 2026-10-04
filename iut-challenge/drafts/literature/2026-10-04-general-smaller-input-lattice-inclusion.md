# General literal-input lattice inclusion — completed source assessment

TARGET: Test whether a(beta^(-1) T union J) is contained in p^floor(v_p(a) - v_p(beta)) I for finite tensor packets with Dupuy–Hilado's log-shell normalization and conductor-based beta, allowing |a|_p <= 1, by genuine lattice inclusion.
CHECKED: 2026-10-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the completed fixed-packet and native proof-use assessments; searched the exact numbered transition, tensor log-shell/conductor inclusion, genuine inclusion, scalar rounding and corrections, including primary-domain searches. No independently justified match for the stronger general inclusion was located; failed searches establish no novelty.
SOURCE_EVIDENCE: Read continuous PDF and auxiliary HTML passages of Dupuy–Hilado arXiv:2004.13108v2, Theorem 2.8.1 and Remark 2.8.2, pp. 9–10; §§4.1–4.3, pp. 16–18; §§6.1–6.3, pp. 18–22, including (6.4)–(6.8) and their justifications. Reused the version-qualified April 2020 IUT IV Proposition 1.2(ii) and Proposition 1.4(iii), and November 2022 RIMS1968 Example 3.5.1(i), already read in the preceding assessments.
COMPARISON: The source's claimed bound compares component hulls after saturation; the proposed pre-orbit inclusion is stronger. Its conductor theorem and log-shell containment lemma cover supporting inputs, while the native theorem gives a differently scaled enclosure on maximal-order input. Neither supplies the sharper general inclusion as an independently justified citation.
GAP: Verify the position of both literal-input branches in the stated integer-power-scaled tensor log-shell for general packets, preserving the distinguished scalar factor and derivative-product beta with a maximal-different factor omitted. The unit-scalar range is a proposed local extension, not a theorem imported from the strict §6.2 hypothesis.
REASON: SPECIALIZE permits verification of this stronger sufficient mechanism against the suspect auxiliary deduction. Import the covered conductor, shell and native enclosure results; derive only the unestablished input placement in a later mathematical turn. No new bound, counterexample or general inclusion is derived in this review.
LITERATURE_REASON: The saved REVIEW_REQUIRED target changes the fixed quadratic packet to general finite packets and replaces the assessed hull comparison by genuine lattice inclusion; exact scalar placement, beta construction and the strongest existing bounds required a separate source comparison.
SCOPE: Any prime p and finite nonempty packet K_1,...,K_m/Q_p; lattice tensors over Z_p, field tensors over Q_p; I_i = (2p)^(-1) log(O_(K_i)^times), I = tensor_i I_i, T = tensor_i O_(K_i), J = tensor_i log(O_(K_i)^times); nonzero a in the distinguished K_m with |a|_p <= 1; beta is the derivative-product conductor element of Theorem 2.8.1 omitting any factor of maximal different valuation, with all field-component valuations equal to sum(d_i)-max(d_i). No coupling of the omitted factor to the scalar factor is assumed. Covers local genuine inclusion and its same-packet full-orbit hull diagnostic; excludes initial theta data, Ind3, inter-packet permutations, global pilot transport and normalized A/B identification.
COVERED_TARGET: Test whether a(beta^(-1) T union J) is contained in p^floor(v_p(a) - v_p(beta)) I for finite tensor packets with Dupuy–Hilado's log-shell normalization and conductor-based beta, allowing |a|_p <= 1, by genuine lattice inclusion.
COVERED_TARGET: For an admissible finite tensor packet violating the proposed genuine inclusion, determine whether the full orbit hull of a(beta^(-1) T union J) still satisfies the rounded component-hull bound.

## Preserved initial assessment boundary

This assessment was created with REVIEW_REQUIRED after step 017. That mathematical turn read no new source and approved no general-packet calculation. This separate literature turn completes the scope comparison while retaining the exact proposed test. It performs no new lattice, orbit or exponent calculation.

## Gap, downstream use and stopping test

The main gap remains finite B >= A at IUT III, Corollary 3.12, step (xi-f), with the original pilot and full image/normalization obligations. A genuine inclusion in an integer-power-scaled I could furnish a reliable local enclosure preserved by the entire I-automorphism group, bypassing the decided enlarged-lattice objection. Even a universal local result would leave those later obligations open.

[The ready fixed-packet assessment](2026-10-03-smaller-good-place-input.md), L007–L009 and [the last mathematical decision](../../history/017-2026-10-04-smaller-good-place-input-test.md) are reused. L009's achieved radii 16 satisfy its required radii 32, but only in its specified quadratic packet. L007 and L008 concern enlarged inputs; their failures do not decide either branch of the general literal input. The earlier marking and formal-quotient mechanisms remain distinct and parked. No decided packet objection is reopened here.

The required threshold is genuine inclusion in p^n I, with n = floor(v_p(a) - v_p(beta)), for both branches and every packet in SCOPE. No achieved general bound is reported. The next mathematical test must either give a proof under these hypotheses or an exact admissible packet and point outside this lattice. Sampled automorphisms or a point lying only in beta^(-1) I do not decide this target. A counterexample stops the universal sufficient mechanism; it does not alone refute the weaker component-hull bound. The conditional COVERED_TARGET allows that same-packet comparison without another source review. No direct inference to a final enclosure failure or essential IUT flaw is authorized.

## Searches and versions actually checked

New queries on 2026-10-04 were:

- `"Dupuy" "Hilado" "6.5" "6.6" log shell`;
- `"tensor" "log-shell" "lattice" "beta" Dupuy Hilado`;
- `"tensor" "log-shell" "conductor" inclusion`;
- `"Dupuy" "Hilado" "genuine" inclusion`;
- `"2004.13108" "lattice" correction`;
- `"log-shell" "different" "inclusion"` and `"log-shell" "tensor" "rounded"`, restricted to arXiv and Kyoto RIMS;
- `"2004.13108" "errata"`, restricted to arXiv and Dupuy's author domain.

The searches returned the assessed paper, discussion pages, manuscript-index hits and a formalization-project README lead; the primary-domain follow-ups returned no matches. Discussion, index snippets and repository summaries were discovery evidence only. No theorem or Mathlib coverage is imported from them. The Yamashita manuscripts and project formalizations were not inspected for this exact statement; they are supplemental unread leads, not essential premises of this local test. The prior correction searches are reused, and no absence of corrections or novelty is inferred.

[The arXiv record](https://arxiv.org/abs/2004.13108) still lists v2, submitted 2020-04-29. The 36-page PDF's April 30, 2020 title date was authenticated in the reused assessments. Printed page and equation numbers below use [that PDF](https://arxiv.org/pdf/2004.13108v2); [the experimental HTML](https://arxiv.org/html/2004.13108v2#S6) is an auxiliary transcription with different equation cross-references. The continuous readings include the displayed chain and its following explanations. No silent correction of displayed constants, typographical issues or normalization is made.

The [official announcement dated 2023-07-07](https://zen.ac.jp/news/0ul6zqed9-0) and [current English prize page](https://zen.ac.jp/en/lp/icp) were read as available on 2026-10-04. They retain the inherent/essential-flaw target and separate discretionary prize review from mathematical correctness. The English page supplied its prize text this turn, unlike the navigation-only retrieval noted on 2026-10-03. No submission or adjudication is part of the notebook step.

## Primary statements and applicability

| Inspected or reused statement | Coverage and difference from the target |
| --- | --- |
| [Dupuy–Hilado Theorem 2.8.1 and Remark 2.8.2, pp. 9–10](https://arxiv.org/pdf/2004.13108v2#page=9) | Give a derivative-product conductor element and permit changing the omitted factor. This covers beta's construction and maximal-order-to-tensor-order inclusion, not the target's sharper input placement. |
| [Definition 4.3.1, Lemma 4.3.2 and Remark 4.3.3, pp. 17–18](https://arxiv.org/pdf/2004.13108v2#page=17) | Fix the exact normalized Z_p-lattice, its integral/logarithmic containment inputs and the warning about O_K-module structure. Arbitrary integral scalar stability is not supplied. |
| [Section 6.2, (6.4)–(6.8), p. 20](https://arxiv.org/pdf/2004.13108v2#page=20) | Claims a rounded full-orbit hull bound via an enlarged lattice. It is a weaker claimed conclusion, not an independently justified genuine-inclusion theorem. |
| [Section 6.3 and Lemma 6.3.1, pp. 21–22](https://arxiv.org/pdf/2004.13108v2#page=21) | Uses a = 1 away from selected bad places and refers back to the toy computation; its full initial-data region and final container differ. It does not establish the proposed uniform range of unit scalars. |
| [IUT IV Proposition 1.2(ii) with Proposition 1.4(iii)](../../foundations/04-native-local-enclosures.md) | Gives genuine preserved-lattice enclosures for scaled maximal-order input with different/logarithm correction terms, then normalized volume bounds. This is a safe supporting enclosure, not a match for the sharper p^n I claim. |
| [November 2022 RIMS1968 Example 3.5.1(i), printed p. 100](https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1968.pdf#page=101) | Supplies integer-power shell preservation for a finite free Z_p-lattice. It does not place the literal input in a particular shell. Its odd-prime single-field parts (ii)–(iii) do not cover all tensor packets here. |

The native results and RIMS example are reused from [the completed proof-use review](2026-10-03-hull-transport-screening.md) and [the canonical-beta review](2026-10-03-good-place-canonical-beta.md). The former read continuous April 2020 IUT IV text, printed pp. 9–14, using an 87-page reproduction when the author-hosted retrieval failed; byte identity with the author's PDF was not checked. Those access and version qualifications remain. No new retrieval of a persistently blocked pilot/quotient or Ind3 source is needed for the independent local target.

## Exact hypothesis interpretation for mathematical reuse

The scalar a is nonzero and acts on the distinguished last field factor, as specified in §6.1–§6.2; it is not presumed to lie in Q_p. Field-component valuations use v_p(p) = 1. The broad |a|_p <= 1 range is retained as the proposed sufficient mechanism: §6.2 assumes strict inequality, and §6.3 explicitly supplies only its particular unit a = 1. Uniform validity for other units remains part of the proposed test.

For beta, use the actual Theorem 2.8.1 construction, with O_(K_i) = W(k_i)[alpha_i] and Eisenstein polynomials f_i over the unramified coefficient rings. After choosing an omitted index s of maximal different valuation, its tensor entries are 1 at s and f_i'(alpha_i) at the other indices. Ties are allowed; the scalar remains on its distinguished factor. This is a conductor element, not an assumption that it generates the entire conductor. The common component valuation condition is the one stated in §6.2 after (6.4). Matching that valuation alone does not make an arbitrary element an assessed derivative-product choice.

Keep the unmodified Definition 4.3.1 lattice I. The source's small-ramification statements in Lemma 4.2.3(2) and Remark 6.2.1(4) have their own hypotheses; they do not authorize replacing I by the tensor order for every packet. Nor does the generally unavailable O_K-module structure authorize multiplication by a/beta inside I. Both branch inclusions must be established for the exact normalization in a mathematical turn. No new logarithm identity, lattice containment or counterexample is established in this assessment.

For comparison, the cited native Proposition 1.2(ii) starts with phi(p^lambda O_L) and encloses it in p^floor(lambda-D-A_0) J, then in its stated outer maximal-order container, under its fractional-scaling and lattice-preservation hypotheses. D and A_0 are the source's sums of different and logarithm correction terms. Its input and exponent differ from the present beta^(-1) T union J and floor(v_p(a)-v_p(beta)); a citation to it therefore does not finish the stronger mechanism. Import that native result rather than reprove it or drop its corrections.

## Assessment and continuation decision

**SPECIALIZE:** coverage is ready for the unchanged TARGET and the conditional same-packet COVERED_TARGET. Known results cover the setup and safe enclosure mechanism; the identified difference is the sharper genuine placement of the literal input. A separate mathematical attempt is justified to verify this mechanism. No essential unread source remains within that scope. If it fails, stop the general inclusion route and assess the already covered weaker bound only on the actual counterexample packet, without recycling the decided enlarged-input failures.

Completed-step classification: **NOVELTY_UNCHECKED**. Outcome: **EXPLORATION**, because this is the first source comparison for the changed strength and packet scope and makes the next test actionable. This review establishes no mathematical advance and no result beyond the sources checked. A later mathematical report may describe a verification as REPRODUCTION or an unmatched result as POTENTIALLY_NEW in the bounded-search sense; neither implies certified originality. The local mechanism retains three informative mathematical negatives and 0/3 uninformative mathematical exploration turns; this literature step spends none. The older defect/quotient sequence stays parked at 3/3.

## Mathlib

Full general literal-input inclusion: **not checked**. Supporting local-field logarithm, conductor, tensor-lattice and automorphism coverage: **not checked**. The named primary statements above distinguish supporting results from a match for the full statement. Search snippets and formalization-project descriptions establish neither Mathlib coverage nor absence, and no formal verification is claimed.
