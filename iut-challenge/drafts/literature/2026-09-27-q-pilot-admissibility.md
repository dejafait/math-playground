# Distinguished pilot admissibility — source assessment

TARGET: Review IUT III, Remark 3.12.2(ii), and its cited q-pilot constructions to determine which L006 marked collections can represent the distinguished pilot before quotienting.
CHECKED: 2026-09-27
DECISION: SOURCE_BLOCKED
SEARCH_EVIDENCE: Searched the exact Remark 3.12.2/q-pilot/intertwining labels, q-pilot with splitting/degree, marking, arbitrary degree and admissibility; followed Definition 3.8 to IUT II, Definition 4.9(viii) and Corollary 4.10(i), and their IUT I references; searched current IUT I copies and the Dupuy–Hilado statement paper. Queries and access limits are recorded below.
SOURCE_EVIDENCE: Read May 2020 IUT III, Definition 3.8(i)–(iii), Remark 3.8.1 and Remark 3.12.2(ii); December 2020 IUT II, Definition 4.9(i)–(viii) and Corollary 4.10(i); June 2017 IUT I, Example 3.5(i)–(ii) and Definition 5.2(i)–(iv); Dupuy–Hilado arXiv:2004.13228v1, §§2.5.4–2.5.5 and 3.1–3.4, plus the v2 statement and example passages specified below. The May 2020 IUT I construction passages remain unread.
COMPARISON: IUT II, Definition 4.9(viii), specifies the pilot up to isomorphism from the complete prime-strip data; L006 instead allows an independently chosen global object and object-level markings. These are not an established correspondence, and no inspected statement characterizes the admissible L006 collections.
GAP: Authenticate and read the current IUT I definitions of the underlying prime-strip, its localization data and q-splitting before completing the applicability comparison; then identify the pilot, output target and markings in a common normalized realization. The separate formal-quotient source blocker remains in force.
REASON: The review identifies concrete source constraints but does not finish the exact comparison. Complete the bounded assessment as blocked and stop the exploration sequence at 3/3; retain the target without authorizing another free-degree example or dependent calculation. An older text or an access failure is not evidence of an IUT flaw.

## Scope, required bound and continuation test

The main gap remains finite B ≥ A in Corollary 3.12(xi-f), in the notation of the [comparison source record](../../foundations/02-comparison-claim-and-sources.md). This review tests an independent necessary input: admissibility of the marked collection to which one might later apply L006. A justified correspondence could make that invariant relevant to the pilot; a demonstrated incompatibility could eliminate a proposed model instance. Neither would settle the quotient, log-Kummer transport, hull or final volume comparison.

The achieved estimate is still d(G) ≤ d(D) − δ. The sufficient model threshold δ ≥ 0 has not been obtained for an actual pilot, and d(G), d(D) have not been identified with the normalized A, B. No new bound or defect value is calculated here.

Continue only with a source-compatible identification of the pilot and retained markings, or a precise incompatibility under the same hypotheses and normalization. Stop treating arbitrary variation of G as evidence about a fixed pilot unless that variation is shown to be permitted. This review does not prove that every L006 collection is inadmissible; it supplies no complete test for which ones are admissible. The exact target is preserved above.

## Search record and reused work

Representative queries executed on 2026-09-27:

- `"IUT" "3.12.2" "q-pilot"` and `"IUT" "q-pilot" "intertwining"`;
- `"q-pilot" "splitting" "degree"`, `"q-pilot" "marking"`, `"q-pilot" "arbitrary" degree`, and `"q-pilot" "admissibility"`;
- `Mochizuki "Inter-universal Teichmuller Theory II" "4.10" pdf`;
- `"Inter-universal Teichmuller Theory I" "Definition 5.2" pdf` and `"iu-teich-1-zu-iri.pdf"`;
- `"Inter-universal Teichmuller Theory I" "May 2020" pdf`, including a search excluding the author host and the already tested mirror;
- `"The Statement of Mochizuki" "Corollary 3.12" arxiv`.

Reuse the [realification assessment](2026-09-26-current-target.md), [formal-quotient assessment](2026-09-27-formal-quotient-defect.md), and [source-recovery record](2026-09-27-formal-quotient-source-recovery.md). Their scope and version qualifications are unchanged. Search results also led to the LANA report repository and informal formalization discussions; those leads were not read as theorem sources and support no conclusion here. Failed exact-phrase searches establish no novelty.

The [official challenge page](https://zen.ac.jp/en/lp/icp) was reread on this date. Its mathematical scope still concerns an essential IUT flaw; adjudication is separate from correctness. The existing challenge source note remains applicable.

## Primary passages actually read

**IUT III, May 2020, 199 pages.** Read the [primary-paper copy](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%203.pdf): Definition 3.8(i)–(iii), printed pp. 112–114; Remark 3.8.1, p. 114; Remark 3.12.2(ii), including (a^itw)–(f^itw) and (a^toy)–(f^toy), pp. 187–191. Definition 3.8(i) uses the q-splitting generators and refers to IUT II, Corollary 4.10(i), and IUT I, Example 3.2(iv). Remark 3.12.2(ii)(e^itw)–(f^itw) holds the q-side arithmetic structure fixed while describing the output construction. Its compatibility assertion is part of the disputed argument, not an independently imported proof of the numerical bound. The toy discussion does not supply a pilot-admissibility criterion.

**IUT II, December 2020, 174 pages.** Read the title page and [Definition 4.9(i)–(viii), pp. 153–158, and Corollary 4.10(i), pp. 158–159](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20II.pdf#page=153). Definition 4.9 includes split-Kummer local data and the full global prime-strip. Item (viii) says that the bad-place monoid generators and localization data determine a pilot up to isomorphism, of negative arithmetic degree. Corollary 4.10(i) identifies the constant prime-strip used in the construction with the one from the underlying Hodge theater. These statements supply a necessary comparison constraint; they do not identify L006's category or fix its numerical normalization. Item (viii) expressly retains IUT I, Definition 5.2(iv)(a)–(f), so those conditions cannot be omitted from a full applicability assessment.

**IUT I, June 2017 — earlier version only.** Read [the primary text reproduced at Paperzz](https://paperzz.com/doc/7332829/inter-universal-teichmuller-theory), title/date; Example 3.5(i)–(ii), printed pp. 84–85; Definition 5.2(i)–(iv), pp. 133–134. In this text, the localization maps act on divisor monoids, and Definition 5.2(iv)(f) requires an isomorphism of the entire data collection with the model from Example 3.5(ii). This is useful for locating the comparison obligation, but its agreement with May 2020 has not been authenticated. It is not used to clear the current-version gate or to prove inadmissibility.

**Dupuy–Hilado — distinguish the versions.** The [arXiv record](https://arxiv.org/abs/2004.13228) dates v1 to 2020-04-28 and v2 to 2025-06-19 and records a split of the original paper. Read [v1, §§2.5.4–2.5.5 and 3.1–3.4, pp. 8–10](https://arxiv.org/pdf/2004.13228v1#page=8). Section 3.3 defines the q-pilot divisor from the chosen elliptic curve, bad places and 2l-th roots of Tate parameters; §§2.5 and 3.4 specify degree/volume conventions. Read [v2, introduction and Theorem 1.0.2 statement](https://arxiv.org/html/2004.13228v2#S1), Definition 2.8.1, and the opening of §2.10 through §2.10.5. Theorem 1.0.2 asserts computability of initial theta data and supplies an 11a1 example; its full proof was not audited here. This gives a concrete source lead for a native arithmetic input, but no marking into the output determinant and no full L006 admissibility theorem. No example calculation or initial-data construction is reproduced in this turn.

## Comparison with L006

The comparison below describes missing identifications, not new mathematical conclusions.

| Data in L006 | Source constraint or unresolved correspondence |
| --- | --- |
| An independently chosen global object G | The current IUT II pilot definition prescribes an object from full prime-strip data. A common realization relating the two has not been given. |
| One arithmetic fiber over ℚ, identity base maps | The reviewed IUT II construction includes local split-Kummer structures and comes from initial Θ-data and a Hodge theater. L006 does not encode these. This alone does not rule out a faithful arithmetic projection. |
| Object isomorphisms ι_v and marking orbits [m_v] | The earlier IUT I text describes additional maps ρ_v of divisor monoids. Identifying these with L006's object-level maps would require an argument; the current definition must first be read. |
| Fixed target D with finite marking-divisor support | The required IUT target is the determinant construction recorded in the existing source audit. Finite support of a native q-divisor does not establish finite support or admissibility of these output markings. |

In particular, uniqueness up to isomorphism in the source does not supply a canonical real-valued normalization across different presentations. Nor does negative pilot degree give δ ≥ 0. No sign argument, global comparison arrow, or restriction of the L006 invariant is derived here.

## Essential unread passages and access evidence

For the **May 2020 IUT I** version, the relevant passages are Definition 5.2(ii)–(iv), Example 3.2(iv)–(v), and Example 3.5(i)–(ii). They remain unread as continuous current-version text. The [author PDF](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20I.pdf) and [Neocities copy](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%201.pdf) returned document metadata but failed on the internal reads. A newly located [Niimura copy](https://yosniimura.net/TeX/Inter-universal%20Teichmuller%20Theory%20I.pdf) returned its title page, dated May 2020, with 186-page metadata; internal reads and searches failed there as well. Screenshot requests supplied no readable page content. HTTP/download variants did not resolve access. A single local curl attempt failed at DNS resolution.

The [publisher's article record](https://ems.press/journals/prims/articles/201525) identifies the 2021 publication, pp. 3–207; its PDF link returned the subscription page, not the text. The June 2017 reproduction above is explicitly older. Indexed current-page excerpts were used only as location leads, not as completed source reading.

This is a material source-scope gap because the saved target asks which marked collections qualify, and the current IUT II definition imports these IUT I conditions. The [March 2024 quotient-descent blocker](2026-09-27-formal-quotient-source-recovery.md) is separate and remains unresolved; no renewed retrieval of it was attempted.

## Assessment and bounded stopping decision

**SOURCE_BLOCKED.** The assessment is complete as an account of what can and cannot currently be justified; the exact admissibility comparison is not complete. The source gives more specific construction constraints than the preceding lecture-note lead, but no checked correspondence or counterexample meeting them was obtained. A citation suffices for the known pilot definition, not for the proposed specialization to L006.

Stop this bounded exploration sequence at **3/3**. The readings do not justify another unrestricted G example, a generic quotient-loop argument, or repeated retrieval without a new access method. The scalar, hull-only, local-marking and morphism-compatibility shortcuts in ATTEMPTS/001–005 remain stopped; this is not a global ban on IUT research. The target remains pending for a later source-supported reassessment, with the precise missing passages and the 11a1 source lead retained. Changing targets does not renew the exhausted exploration budget, and no launcher or runner state was changed.

Outcome: **EXPLORATION**; kind: **LITERATURE**; classification: **NOVELTY_UNCHECKED**. This is a new source comparison, not a mathematical advance or a proved negative admissibility result. The cited constructions are known literature; no new mathematical input was added to the argument, no result was reproduced or established beyond the sources checked, and no candidate flaw was obtained. Lemmas, scripts, PROOF.md and DAG.md are unchanged.

## Mathlib

Full pilot-admissibility statement: **not checked**. Supporting Frobenioid, pilot and normalization coverage: **not checked**. The cited papers are source evidence, not a claim of a Mathlib match or formal verification.
