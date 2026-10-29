# Additional primary-source coverage for step515

Checked 2026-10-26. This supplements the retained step513 source record, without replacing its versions or inspected ranges. It is source evidence, not a mathematical audit of L125.

## Essential additional input

[Brian Conrad, *Math 676. Some basics concerning absolute values*](https://math.stanford.edu/~conrad/676Page/handouts/ostrowski.pdf#page=10), 19-page author-hosted PDF, no revision date visible on the first page: inspected Lemma 6.1 and its entire proof, printed p.10, and Theorem 6.4 with its proof, p.11. The former assumes a complete valued base field and an algebraic extension; it states uniqueness, finite-extension completeness and the norm formula. The latter adds existence for a nontrivial base absolute value. Relevant cases read include finite reduction, trivial/nontrivial uniqueness, separable/inseparable norm comparison and nonarchimedean existence. The existence proof invokes Hensel's lemma; its statement on p.12 was inspected, not its entire proof. These named inputs are imported, not reproved. None identifies an algebraic closure with its completion.

[Stacks Lemma 9.10.5, tag 09GU](https://stacks.math.columbia.edu/tag/09GU), and [Lemma 9.10.6, tag 09GV](https://stacks.math.columbia.edu/tag/09GV): inspected statements and full short proofs on live HTML. The first embeds an algebraic extension in an algebraic closure using maximal partial embeddings; its proof extends a partial embedding by adjoining a root. The second treats isomorphism of algebraic closures using algebraic closedness of the image. These cover the standard embedding-extension input; its actual application in L125 remains for the mathematical audit. The reading was initially through Section 9.10, then the stable-tag pages. No local copy or hash is claimed for these web reads.

## Search and reuse boundaries

Queries: `site.kconrad.math.uconn.edu unique extension absolute value complete field algebraic closure finite extension` and `site.stacks.math.columbia.edu algebraic closure extension embedding algebraic extension field embedding`. Search snippets were leads only; the theorem statements and relevant proofs were subsequently opened. Other search hits were not imported. This targeted search was needed because L125 names valuation uniqueness without a precise locator in the reusable assessment; it was not another search for an original norm construction.

Reread from saved step513 extracts: Keith Conrad, *Trace and Norm, II*, Theorem 4.3, pp.5–7, all three cases; Fili–Miner, April 3, 2010, §2.3 finite-orbit construction and (2.2), p.9, plus Lemma 2.14 and its conjugation proof, pp.11–12. Reuse the other theorem and Mathlib coverage in `2026-10-26-variable-norm-sources.md`; no claim of renewed inspection of those endpoints. The global height setting of Fili–Miner is not transferred to local units. The exact scope comparison is in the completed audit assessment.

## Step516: assessment URL recovery

Reopened the direct Stanford PDF endpoint and checked Lemma 6.1's complete-field/algebraic-extension statement (including its finite-degree qualification) and Theorem 6.4's nontrivial-absolute-value existence/uniqueness statement, printed pp.10–11. Reopened Stacks 09GU and 09GV and read their statements and full short proofs. These were endpoint/locator checks, not a fresh proof audit of L125 or a renewed reading of every earlier source. Existing recorded proof coverage is reused. Added direct URLs to the unchanged audit assessment's SOURCE_EVIDENCE field; no new theorem or applicability conclusion was obtained.
