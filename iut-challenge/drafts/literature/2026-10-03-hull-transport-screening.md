# Local hull transport — completed source assessment

TARGET: Review the determinant-one hull-containment assertion in Dupuy–Hilado §6.1 against IUT IV, Propositions 1.2(ii) and 1.4(iii), to determine whether the local hull estimates require it or instead use log-shell-preserving lattice inclusions.
CHECKED: 2026-10-03
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the initial searches below; completed exact-assertion, polydisc/lattice and correction searches, inspected arXiv version history and both author lists, and traced the displayed proofs. No matching correction was located in this bounded screen; this does not establish its absence.
SOURCE_EVIDENCE: Read arXiv:2004.13108v2, selected passages on printed pp. 17–22, especially Remark 4.3.3 and (6.3)–(6.8); read the April 2020 IUT IV reproduction, printed pp. 9–14 and Theorem 1.10(iv)–(v), pp. 26–28. Versions, read locations and access qualifications are recorded below; the separate Ind3 manuscript remains unread and is not needed for the preapproved local test.
COMPARISON: Native Propositions 1.2(ii) and 1.4(iii) use preserved-lattice inclusions, not the determinant-only hull remark. The auxiliary (6.5)–(6.6) transition uses a hull comparison inside automorphism saturation; a citation to the native enclosure does not verify that sharper transition.
GAP: Verify only the auxiliary rounded-lattice transition on an actual local tensor log-shell, keeping the beta constraints and lattice-preserving automorphisms; do not reprove the native theorem or infer an IUT flaw from an auxiliary failure.
REASON: The proof-use review excludes the broad remark as an essential input to the native local propositions and identifies a distinct suspect transition to test. Known enclosures are citation inputs; verification of the identified difference justifies SPECIALIZE. This turn completes source screening only.
SCOPE: Local finite tensor packets, their actual logarithm lattices, admissible different-based beta and automorphism saturation; covers the explicit test below. Does not cover global pilot identification, formal quotient descent, Ind3 realization, permutations between packets, archimedean images or normalized A/B identification.
COVERED_TARGET: Test Dupuy–Hilado (6.5)–(6.6) for K = Q_2(sqrt(2)), L = K tensor K, and a = 1 tensor sqrt(2), computing the actual tensor log-shell lattice and different-based beta to decide whether the rounded lattice bounds the hull after all lattice-preserving automorphisms.

The initial screening below is preserved as the record preceding step 012. Its pending review and proposed continuation are superseded by the completed assessment at the end; the exact original TARGET is retained.

## Gap, intermediate target and test

The main gap remains finite B ≥ A in the [comparison source record](../../foundations/02-comparison-claim-and-sources.md). The new intermediate target concerns the local numerical enclosures of all permitted images, before their contribution to B can be used. It does not ask whether the L006 defect descends, or which freely chosen marked objects are pilots.

There are two useful possible outcomes. A fully applicable known enclosure should be imported by citation, leaving the separate input/output comparison unresolved. An unsupported or incorrect enclosure could identify a numerical step to investigate, provided it is actually needed by the native argument under the same hypotheses. A problem confined to an auxiliary exposition would not demonstrate an essential IUT flaw.

The discriminating test is the exact hypothesis and use of each transport step: does it use a common preserved lattice and actual inclusion, or require the more general coordinate-hull assertion? Continue toward an IUT objection only if a questionable use can be tied to the native bound with its full assumptions. Park the general remark as an exposition issue if the native estimate uses sufficient stronger data and the remark is unnecessary. Do not replace this test with an unrestricted determinant counterexample.

No new bound is achieved here. Local upper radii, even if justified, do not by themselves give A ≤ B. The existing arithmetic estimate d(G) ≤ d(D) − δ still lacks a pilot identification and the sufficient model sign δ ≥ 0. Neither estimate has been identified with the actual normalized A and B. The remaining global, archimedean, all-image and normalization obligations are not discharged.

## Three mechanisms compared

The exhausted marked-pilot/quotient route is parked in [ATTEMPTS/006](../../ATTEMPTS/006-realified-pilot-and-quotient-source-blockers.md). The following are alternatives for the numerical gap, not renamed attempts to retrieve either blocked source.

| Mechanism | Evidence and limitation | Decision and concrete test |
| --- | --- | --- |
| A common stable logarithm lattice enclosing every automorphism image | Readable native propositions and a numerical exposition give a precise local comparison to screen. It addresses enclosure of image families, rather than determinant tensor exponents or a collapsed quotient. | Select the TARGET above: trace the scope and use of hull transport against the lattice-preserving hypotheses. Cite covered enclosures instead of rederiving them. |
| A uniform Ind3 envelope over log-link changes | The numerical exposition cites an additional log-Kummer result for the initial envelope; the main manuscript was not read. The author listing is not that theorem. | Park dependent envelope work. A valid reopening would require the actual theorem and an exact all-image applicability comparison; do not calculate arbitrary log iterates or repeat old retrievals. |
| Global probabilistic Szpiro inequalities as an independent bridge | Theorem 7.5.1 assumes Corollary 3.12. The paper's introduction also retains an archimedean assumption. | Reject this as an independent proof of the missing comparison. The concrete source test is its assumption list, which has been read; downstream conditional consequences do not certify their premise. |

This comparison yields an actionable source test, not a mathematical advance. The prior exploration sequence remains exhausted at 3/3; any subsequent scheduling or budget renewal belongs to the external runner.

## Searches actually performed

Representative queries on 2026-10-03:

- `Dupuy Hilado probabilistic Szpiro log shell Ind3 hull volume arxiv`;
- `"Ind3" "log-shell" "hull" Mochizuki` and `"Ind3" "bounded" "hull" Mochizuki`;
- `Dupuy "Log-Kummer Correspondences" "Third"`;
- `"Dupuy" "hull" "det" "6.1" correction`;
- `Mochizuki "Proposition 1.4" "hull" "IV"`.

Followed [Dupuy's author list](https://tdupu.github.io/papers.html) to authenticate the separate manuscript leads. Results also included project-formalization pages, alternative expositions and discussion sites. Those were not inspected as theorem sources and establish no mathematical conclusion. No search result establishes novelty or the absence of corrections. The exact standard theorem and errata comparison for the selected target remains to be completed.

## Primary sources actually read

**Dupuy–Hilado, arXiv:2004.13108v2.** The [version record](https://arxiv.org/abs/2004.13108v2) dates v2 to 2020-04-29; the [36-page PDF](https://arxiv.org/pdf/2004.13108v2) prints 2020-04-30. Read the title/introduction, §6.1 (printed pp. 18–19), §6.2 (pp. 19–21), §6.3 (pp. 21–22), and Theorem 7.5.1 (p. 23), cross-checking the [HTML](https://arxiv.org/html/2004.13108v2#S6).

Section 6.1 defines hull by component radii and asserts that, for a Qp-linear T with |det T|p = 1, T(X) ⊆ Y implies hull(X) ⊆ hull(Y). Section 6.2 uses logarithm-lattice automorphisms and notes omitted permutations; Lemma 6.3.1 states a local enclosure. Theorem 7.5.1 is explicitly conditional. These statements are read, not verified here. Equations (6.3)–(6.8) are the bounded proof segment to trace.

The Ind3 justification in §6.2 points to a separate manuscript, appearing as an unresolved reference in the PDF. It was not substituted by the author's linked interpretation-table appendix. No full Ind3 theorem is imported from this reading.

**Mochizuki, IUT IV, author-hosted April 2020 version, 87 pages.** Read [Propositions 1.1–1.2, printed pp. 9–11](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20IV.pdf#page=9), [Proposition 1.4, pp. 13–14](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20IV.pdf#page=13), and [Theorem 1.10, proof step (v), pp. 27–28](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20IV.pdf#page=27). The title page authenticates April 2020; journal pagination is not used.

Proposition 1.2 requires φ to preserve the tensor product of the logarithm submodules. Its proof uses containment in an integer-power-scaled preserved module. Proposition 1.4(iii) states normalized local upper bounds, and step (v) applies them to permitted images. These are supporting native results to compare, not a match for the unrestricted determinant/hull assertion or an independent proof of Corollary 3.12. The construction-to-all-images applicability is not audited in full.

PDF screenshots returned references but no readable image content through this tool, so no visual authentication is claimed. The mathematical passages above were read as continuous extracted PDF text; the source formulations and qualifications are retained without correcting typographical or hypothesis issues by inference.

## Redundancy and scope

ATTEMPTS/001–005 and their cited lemmas remain applicable: a free power map changes normalization; common determinant exponents cancel; a hull collapse can retain an upper-bound test; local markings and morphism compatibility alone supply no defect sign. The new question instead concerns the coordinate geometry of an image family under actual local linear actions and the role of its preserved lattice. No result of those earlier tests decides this source question. No second lemma catalog or dependency graph is created.

This screening does not establish that the §6.1 assertion is false, that its proof uses it essentially, or that IUT shares any defect in it. A complete critique of an auxiliary statement, if later obtained, would still require a separate native relevance test. No essential flaw, candidate resolution or bound beyond the checked literature is claimed.

## Initial classification and assessment boundary

At creation, REVIEW_REQUIRED was intentional: source discovery was useful, but the exact coverage and proof-use comparison was unfinished. The known enclosures were citation candidates; none was added as a mathematical input, reproduced or specialized in that recovery. No derivation, example calculation, lemma or script was added. Its classification was NOVELTY_UNCHECKED.

## Mathlib

Full selected hull-transport statement: **not checked**. Supporting lattice-automorphism, p-adic measure and coordinate-hull coverage: **not checked**. The primary citations support the screening; they do not claim a Mathlib match or formal verification.

## Completed proof-use review, 2026-10-03, step 012

### Source authentication and bounded searches

The [arXiv version record](https://arxiv.org/abs/2004.13108) still lists v2, submitted 2020-04-29, as the latest revision. The [PDF](https://arxiv.org/pdf/2004.13108v2) prints April 30, 2020. Its experimental HTML displayed a different typesetting date and changed equation cross-references; use the PDF's version and numbering. Read the selected definitions and proofs at printed pp. 17–22, not merely search excerpts.

The [native author list](https://www.kurims.kyoto-u.ac.jp/~motizuki/papers-english.html) dates IUT IV to 2020-04-22. Internal reads of the author PDF failed this turn. The [87-page reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%204.pdf) supplied continuous primary text headed April 2020. Its relevant formulations agree with the prior author-PDF readings above; byte identity was not checked. Read Propositions 1.1–1.2, 1.4 and their proofs, plus Theorem 1.10's opening hypotheses and steps (iv)–(v). No source was silently replaced by an earlier formulation.

Additional queries:

- "Dupuy" "Hilado" "hull" "determinant";
- "Probabilistic Szpiro" erratum correction hull and "2004.13108" "correction";
- "Dupuy" "Hilado" "hull" errata;
- "hull" "Q_p" "determinant" polydisc automorphism;
- "log-shell" "automorphism" "hull" "inclusion";
- site:tdupu.github.io "13108" correction;
- site:kurims.kyoto-u.ac.jp/~motizuki "Teichmuller" "IV" "corrections".

Inspected [Dupuy's manuscript list](https://tdupu.github.io/papers.html) and the native list for revision/correction leads. No relevant erratum was found there or in these searches. Formalization repositories, discussion pages and unrelated convex-hull results were discovery hits, not inspected theorem evidence. No claim about the absence of a theorem or certified novelty follows.

Rechecked the [official announcement](https://zen.ac.jp/news/0ul6zqed9-0), dated 2023-07-07, as available on 2026-10-03: its inherent-flaw target and separation of adjudication remain consistent with the source record. The English prize-page URL returned university navigation this turn; no newly verified prize conditions are attributed to it.

### What the proofs actually use

| Source location | Read proof-use evidence |
| --- | --- |
| Dupuy–Hilado §6.1, p. 19 | The determinant-only implication is stated without a proof. |
| §6.2, (6.4)–(6.6), p. 20 | Comparisons are written between hulls after automorphism saturation. The justification of (6.6) invokes scalar-size comparison. |
| (6.7)–(6.8), p. 20; Lemma 6.3.1, pp. 21–22 | Lattice preservation supplies (6.7); the following bound uses Lemma 4.2.3. The actual scenario refers back to this computation. |
| Remark 4.3.3, p. 18 | The source cautions against treating the logarithm lattice as an arbitrary ring-of-integers module. |
| IUT IV Proposition 1.2(ii), pp. 10–11 | Its proof places the fractional maximal order in an integer-power-scaled logarithm lattice preserved by phi, then in a scaled maximal order. |
| Proposition 1.4(iii), pp. 13–14; Theorem 1.10(v), pp. 27–28 | The native estimate imports those genuine inclusions and uses the outer container for the hull bound. |

This is a source-dependency comparison, not a proof that any auxiliary assertion is false. In particular, the source does not explicitly cite the determinant remark at each displayed transition. The unverified obligation is whether its hull-only substitutions are justified under the actual lattice hypotheses. Reading lattice preservation at (6.7) does not finish that obligation.

### Ready scope and discriminating test

The preapproved mathematical test fixes a local field and its tensor packet, rather than using an unrestricted determinant map or freely chosen marked global object. Use Definition 4.3.1's actual log-shell, with the source's normalization, and retain both constraints on beta: its component valuations and its inclusion of the maximal order into the tensor order after multiplication. Do not choose beta solely by matching one valuation.

For this test, obtain an exact lattice description, justified by convergent logarithm/exponential computations or a named theorem. Finite numerical truncation alone cannot certify the lattice or the hull. Compare genuine inclusion before saturation with the claimed coordinate-hull bound after saturation. If inclusion fails, the orbit-hull comparison still needs to be tested; failure of the former alone does not refute the latter. If the fixed packet satisfies the bound, record the limited scope and reassess rather than treating one example as a universal proof.

Import the native enclosures with their full hypotheses. Reproof would duplicate the closest known result. Only the auxiliary rounding/automorphism difference needs an informal mathematical test. This limited test requires neither the unread Ind3 theorem nor a full initial theta-data construction. Extending its outcome to the full IUT image family would require a separate applicability review; that extension is not preapproved.

The plausible downstream use is to decide which local enclosure is usable when testing the numerical output B. A verified failure would challenge an auxiliary estimate and motivate checking its claimed gain against the native container; it would not demonstrate an essential IUT flaw. The native propositions' proof-use trace stops the determinant-only objection as a direct local IUT objection. The pilot, all-image and normalization bridges remain unresolved, and no new achieved bound reaches finite B ≥ A.

### Assessment and continuation decision

**SPECIALIZE:** sufficient coverage for the exact original review and the single COVERED_TARGET, with known native estimates imported by citation and the suspect auxiliary transition reserved for verification. This literature step establishes no new theorem, counterexample, specialization or numerical bound. Its outcome is **NEGATIVE** because the completed native proof-use comparison changes the objection's scope; it is not a repeated stop review or a mathematical discovery.

Classification: **NOVELTY_UNCHECKED**, appropriate to this source review. No result beyond the checked literature is claimed. A later mathematical report must distinguish reproduction/verification from anything potentially beyond the bounded search. The prior pilot/quotient blockers and their exhausted 3/3 sequence remain parked; this review spends no calculation turn and does not modify runner state.

Mathlib coverage for the full rounded-lattice statement and its supporting local-field facts remains **not checked**. The cited native theorem names are primary mathematical references, not a Mathlib match.
