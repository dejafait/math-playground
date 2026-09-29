# Formal quotient and marking defect — source review

TARGET: Test whether L006's defect descends through the (fQ1)/(fQ2) formal quotient in IUT III, Remark 3.9.5(ix), with the identifications used in Corollary 3.12(xi-f).
CHECKED: 2026-09-27
DECISION: SOURCE_BLOCKED
SEARCH_EVIDENCE: Searched the exact fQ1/fQ2 labels, Remark 3.9.5, formal quotient, marking defect, descent, later Mochizuki expositions, and categorical localization; read the relevant primary-paper passages and a newly found conditional-bridge preprint, with queries and versions recorded below.
SOURCE_EVIDENCE: Read May 2020 IUT III, Remark 3.9.5(vii)–(ix), Remark 3.10.2, Corollary 3.12(x)–(xi-g), and Remark 3.12.2(v); reread Scholze–Stix §§2.1–2.2 and Mochizuki (C10), (C12)–(C14); inspected the February 2023 Essential Logical Structure passages below, but could not retrieve the relevant pages of the version listed by the author as 2024-03-24.
COMPARISON: L006 supplies an invariant on compatible marked collections in one arithmetic fiber. None of the inspected statements identifies its finite zigzags with the formal quotient or proves descent of this defect with the required numerical interpretation. The later exposition directly discusses descent and fixed gluing, making its unread current version material to this comparison.
GAP: Read the current exposition's §§3.8–3.10 before deciding which quotient identifications and retained data give the appropriate test of L006, and before relating that test to the distinguished q-pilot and normalized volumes.
REASON: The review adds source-level evidence but does not settle applicability. The original mathematical target is preserved; dependent calculations remain gated until the essential version gap is resolved. Failure to retrieve a source is not evidence against its mathematical claim.

## Scope and relevance

This completes one literature-only assessment with an explicit source blocker. It is not a ready assessment for research. The [preceding ready assessment](2026-09-26-current-target.md) is reused for the fixed arithmetic-fiber construction; this review concerns the subsequent formal quotient and comparison.

The gap is whether the [L006 invariant](../../lemmas/L006-marking-defect-in-realified-localization.md), defined with fixed normalization, identity base maps, and finite support, has a justified role after the formal quotient. The intermediate target is an exact comparison between the retained marked data and the identifications actually used in (xi-f). Its plausible use is to determine whether the defect can constrain that numerical comparison. Remaining steps include the distinguished q-pilot, log-Kummer transport, all allowed output images, the hull, and the normalized volume interpretation.

Continue the defect route only if the sources specify a comparison on the relevant data and a test of invariance, or a justified obstruction to that comparison. Abandon this particular defect as a numerical obstruction if it is discarded while the source's weaker bound-relevant comparison survives. Non-descent alone would not refute IUT. No such calculation or conclusion is made in this turn.

## Search record

Representative queries executed on 2026-09-27:

- `"IUT" "formal quotient" "fQ1"` and `"IUT" "fQ2"`;
- `"Remark 3.9.5" "quotient"` and `"IUT" "marking defect" descent`;
- `Mochizuki "formal quotients" "Alien"`;
- `"Essential Logical Structure" "3.10" "quotient"` and `"Essential Logical Structure" "Mochizuki" pdf 2024`;
- `"IUT" "formal quotient" invariant descent`, restricted to arXiv and the author's institutional domain;
- `site:stacks.math.columbia.edu "Lemma 4.27.8" localization`.

No full match for the saved target was identified in the inspected statements. This limited result does not establish novelty or absence from the literature. Search snippets and discussion posts were not used as theorem evidence.

## Primary sources inspected

**IUT III, May 2020.** Read the primary text through this [199-page copy](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%203.pdf). The [author's publication list](https://www.kurims.kyoto-u.ac.jp/~motizuki/papers-english.html) still lists 2020-05-18; access to the [author-hosted PDF](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20III.pdf) timed out. Passages read: Remark 3.9.5(vii)–(ix), printed pp. 135–144, including (Ob7)–(Ob9), (cQ3)–(iQ5), and (fQ1)/(fQ2); Remark 3.10.2, pp. 151–152; Corollary 3.12(x)–(xi-g), pp. 180–185; Remark 3.12.2(v), pp. 193–195.

Here (fQ1) retains local markings, a global realified object, and localization identifications; (fQ2) replaces the marked local categories with the original Frobenioids. The pair is called a formal quotient. The passage does not supply an ordinary categorical localization universal property. Later stages use log-Kummer transport and numerical volume; (xi-f) asserts the required membership. These are the source's claims under examination, not independent verification of the bound. No theorem about L006's defect is stated in these passages.

**Scholze–Stix and Mochizuki's response.** Read [*Why abc is still a conjecture*, July 16, 2018](https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf), especially §§2.1.4–2.1.9 and §2.2, pp. 7–10. Its degree-line and pilot comparisons do not identify the marked formal quotient with L006's category. Read [Mochizuki's September 2018 comments](https://www.kurims.kyoto-u.ac.jp/~motizuki/Cmt2018-08.pdf), (C10), (C12)–(C14), pp. 3–4: the response distinguishes abstract and concrete representations and emphasizes the effect of indeterminacies on region volumes. Neither passage provides the saved descent statement; neither is treated as a correctness certificate for the disputed inference.

**Essential Logical Structure, February 2023 text.** Read the primary-paper text in this [full-text reproduction](https://www.scribd.com/document/672223806/Inter-universal-Teichmuller-Theory), not the host's generated summary: §3.6 (ExtInd1)–(ExtInd2), printed pp. 106–108; §3.8 (NSsQ), (LVsQ), pp. 131–132; §3.9 and Example 3.9.1, pp. 132–136; §3.10 (Stp2)–(Stp8), (DstMp), (FxGl), (NoCmpIss), (Englf), and Examples 3.10.1 and 3.10.2(i)–(ii), pp. 141–150. The text defines descent by a natural isomorphism with a construction on underlying data. It separates formal quotient diagrams from later numerical extraction and describes enlargement of output possibilities with the gluing fixed. These passages directly constrain what a relevant descent test must compare. They do not establish that the L006 invariant is such a descended construction.

**Higuchi, March 31, 2026 preprint.** Read all six pages of Joaquim Reizi Higuchi's [*A Conditional Bridge for the Passage IUT III 3.11 ⇒ 3.12*](https://www.researchgate.net/publication/403334234_iut_bridge_preprint), DOI 10.13140/RG.2.2.24411.53286. Definitions 2.1–3.1 and Proposition 3.2 use a weaker set-based comparison package. Lemma 4.5 and Theorems 5.1 and 7.1 obtain the numerical conclusion with an additional bridge assumption; §6 leaves its IUT realization open. This overlaps the generic membership diagnostic already recorded in L003. It neither models the marked formal quotient nor supplies an IUT counterexample, so it does not replace the saved target or justify repeating that diagnostic.

**Standard localization.** Read [Stacks Project, Categories, Lemma 4.27.8 (tag 04VG)](https://stacks.math.columbia.edu/tag/04VG), including its proof. For a left multiplicative system, a functor that inverts its arrows factors uniquely through the localization. This is a supporting categorical result, not a full match: applying it here would first require identifying the source's formal pair with that localization and specifying the relevant functor. No such identification is imported or proved here.

## Essential unread source and decision

The author's list dates the current [*Essential Logical Structure of Inter-universal Teichmüller Theory*](https://www.kurims.kyoto-u.ac.jp/~motizuki/Essential%20Logical%20Structure%20of%20Inter-universal%20Teichmuller%20Theory.pdf) to **2024-03-24**. Its 167-page PDF was identified, but requests for the relevant internal pages and text searches repeatedly failed. Thus §§3.8–3.10 of this version are **unread**. The accessible February 2023 reproduction above and the [November 2022 RIMS preprint](https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1968.pdf) are earlier versions; the latter's introduction was inspected, not its relevant internal passages. Neither establishes what the current version says. The *Alien Copies* exposition was also located, but its relevant §3.11(v) was not read in full and is not used to settle this target.

This version gap is material because the older exposition expressly defines descent and explains the numerical comparison. A complete applicability assessment must check that clarification in the current text. The decision is SOURCE_BLOCKED; the [source-recovery assessment](2026-09-27-formal-quotient-source-recovery.md) records the remaining bounded review. No dependent research is authorized by this assessment.

## Redundancy, threshold, and outcome

The existing failures remain relevant: bare power maps do not model the source; a common determinant normalization cancels; loss of an exact degree under a hull operation can coexist with preservation of an upper-bound test; and local marking or global compatibility alone gives no sign bound. The new readings do not undo these conclusions. In particular, a generic quotient example or a restatement of bound-equivalent membership would repeat existing work.

The achieved arithmetic estimate remains d(G) ≤ d(D) − δ. The required conclusion remains finite B ≥ A for the actual q-pilot and all admitted output images. No sign control or identification with those normalized volumes was added. No mathematical result was imported as a new input, reproduced, or claimed beyond the checked literature in this turn. Its outcome is EXPLORATION and its classification is NOVELTY_UNCHECKED. No full candidate is present; lemmas, scripts, the argument overview, and the DAG are unchanged.

## Mathlib

Full quotient-descent statement: **not checked**. Supporting quotient-category and Frobenioid coverage: **not checked**. The Stacks citation is a supporting result from another source and makes no assertion about Mathlib coverage.
