# Realified localization: literature assessment

TARGET: Express the (cQ3) localization data using Frobenioids II, Example 5.6(iii)–(iv), and determine whether its realification and localization isomorphisms preserve or remove the total marking defect of L005.
CHECKED: 2026-09-26
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched Mochizuki "Frobenioids II" "5.6" realification localization; Frobenioid realification arithmetic line bundle degree perfection principal divisors; "Geometry of Frobenioids I" "Proposition 5.3" "closure"; "Frobenioids" "marking defect"; "cQ3" "localization" "realifications"; followed Example 5.6 to Definitions 2.4 and 5.3, Proposition 5.3, Theorems 5.1, 5.2 and 6.4, and the author's correction sheets.
SOURCE_EVIDENCE: Read Mochizuki's June 2008 author texts through https://www.researchgate.net/publication/267018843_THE_GEOMETRY_OF_FROBENIOIDS_II_POLY-FROBENIOIDS (Example 5.6, pp. 62–65; Definition 5.3, pp. 54–56; Remarks 5.3.3 and 5.6.1–5.6.3) and https://www.researchgate.net/publication/41753550_THE_GEOMETRY_OF_FROBENIOIDS_I_THE_GENERAL_THEORY (Proposition 5.3, p. 103; Theorem 6.4, pp. 114–116, and definitions below); read the February 2019 and January 2024 corrections; read Scholze–Stix §2.1.4 and Mochizuki (C12)–(C14); reuse the previously read May 2020 IUT III (cQ3) source record.
COMPARISON: Known results supply realification, localization functors and a surviving global arithmetic degree line. They do not identify L005's marked category or its Δ with an invariant of the (cQ3) collections. The global degree statement is a supporting result, not a match for the full saved target or Corollary 3.12.
GAP: Give the source-compatible correspondence for the local markings and localization isomorphisms, then test what data representing Δ remains; a scalar coefficient or an ordinary connected component cannot be assumed to survive unchanged.
REASON: Import the established Frobenioid results and specialize only the marked-data comparison. The essential realification/localization source passages are now read; this literature-only turn performs no such specialization and leaves the exact target unchanged.

## Scope and discriminating test

The main gap remains finite B ≥ A in IUT III, Corollary 3.12(xi-f). The intermediate target concerns the status of L005's obstruction under the cited source construction. If that obstruction has a source-compatible realization, it could test the later transport of the distinguished q-pilot. The full indeterminacy family, hull and normalized volume comparison would still remain unresolved.

L005 supplies only the model bound d(Λ) ≤ B − δ within a defect component, with all real degrees possible across components. Its sufficient threshold δ ≥ 0 has not been established for an IUT object. This review supplies no improved bound. The test justifying continuation is an explicit correspondence that respects the local marking orbits and global localization data. Failure of that correspondence, or dependence on choices discarded by the source, would stop use of this particular defect as an IUT diagnostic. Merely finding another ordinary category with unbounded degrees would repeat the stopped test.

## Source versions and passages actually read

The [author's publication list](https://www.kurims.kyoto-u.ac.jp/~motizuki/papers-english.html) lists the main Frobenioid texts as 2008-06-11. Both author-uploaded full texts above bear June 2008. All page numbers here use their 126-page and 72-page pagination, respectively, rather than the journal's pp. 293–400 and 401–460.

- **Frobenioids I:** Definition 2.4(i)–(ii), pp. 47–48; Theorem 5.1(i)–(ii), pp. 96–97; Theorem 5.2(i)–(ii), pp. 100–101; Proposition 5.3 and Corollary 5.4, pp. 103–104; Proposition 5.5, pp. 104–105; Example 6.3, pp. 112–114; Theorem 6.4(i)–(iv), pp. 114–115, including the degree argument on pp. 115–116. The precise inputs used here are recorded by citation in [the foundation note](../../foundations/03-realification-and-arithmetic-degree.md).
- **Frobenioids II:** Example 1.1 and Theorem 1.2's statement, pp. 7–9; Example 3.3(i)–(v), pp. 27–29; Definition 5.3(i)–(vi), pp. 54–56; Remarks 5.3.1–5.3.3, pp. 56–57; Example 5.6(i)–(v), pp. 62–65; Remarks 5.6.1–5.6.3, p. 65. Example 5.6 supplies a global contact functor to the coproduct completion of an auxiliary local category and a local contact functor into that category. The former is GC-admissible; the latter is LC-unit-admissible. These are different functors.
- **Corrections:** Read the [February 2019 Frobenioids II comments](https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Geometry%20of%20Frobenioids%20II%20%28comments%29.pdf), especially (3), (8), (10), (12), (15), and the [January 2024 Frobenioids I comments](https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Geometry%20of%20Frobenioids%20I%20%28comments%29.pdf), especially (24)–(29). Retain the corrected archimedean sign, the named constant functor Φ_v^cnst, and the added birational hypotheses whenever those results are used. No counterexample is inferred from an already corrected statement.
- **IUT III:** Reuse [the source record](../../foundations/02-comparison-claim-and-sources.md) for Remark 3.9.5(ix)(cQ3), printed pp. 141–142, in the May 2020 version. That assessment already reads (lc-gl1)–(lc-gl3) and the arrow compatibility condition; its target and assumptions have not changed.

Access was resolved through the author's full-text uploads after the author-hosted main PDFs and journal page requests timed out. The accessible [RIMS1530 preprint](https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1530.pdf) was inspected as an access lead, but its older 69-page text is not the version used for the completed comparison. No local mathematical script or downloaded-source program was added.

## Coverage and remaining specialization

The foundation note imports the known global degree statement. It is therefore unnecessary to reprove the product formula or the arithmetic Picard computation to investigate this target.

The stronger scale-one conclusion of Theorem 6.4(iv) requires an equivalence of the original arithmetic Frobenioids. That extra hypothesis has not been established for the comparison under investigation.

For the local side, Example 1.1(i) identifies the basic realified p-adic category with an elementary Frobenioid. Remark 5.3.3 gives equivalences after realification for LC-admissible functors; Definition 5.3(v) handles the componentwise construction. Conversely, Remark 5.6.1 explicitly allows noninjective divisor maps for heterogeneous arrows. None of these statements identifies an ordinary finite zigzag with the formal quotient in (cQ3).

The comparison must distinguish three kinds of data already separated in the notebook's source record: the local markings, the global object, and the isomorphisms between its localizations and the realified local objects. L005 fixes canonical localization identifications and rational global scalars. It has not been supplied with the Frobenioid structure required to apply Proposition 5.3 directly to C_D. The justified specialization is to express these data in the cited local and global Frobenioids and check the marked collections there. It is not enough to replace integer exponents by real ones in L005.

This is why the decision is SPECIALIZE rather than IMPORT. The existence and behavior of the global degree line are covered; the relationship between that line and Δ after retaining the (cQ3) markings is not supplied by any inspected statement. In particular, this assessment establishes neither preservation nor disappearance of the full L005 defect. Those alternatives remain the saved mathematical test.

## Prior overlap and limits

[Scholze–Stix, July 16, 2018, §2.1.4, p. 7](https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf#page=7), already describes global realified data using an ordered degree line. The notebook must not present that reduction as new. [Mochizuki, September 2018, (C12)–(C14), pp. 3–4](https://www.kurims.kyoto-u.ac.jp/~motizuki/Cmt2018-08.pdf#page=3), distinguishes this scalar structure from concrete pilot representations and the geometry-dependent effect of indeterminacies on volumes. Neither account is used as a correctness certificate for the disputed comparison.

L001–L005 and ATTEMPTS/001–005 exclude repeating the bare power-map, determinant-factor, unmarked quotient, local-marking-existence and category-axiom shortcuts. The additional source input narrows the remaining test but does not validate an ordinary-model substitute for the q-pilot.

The wider base-category reconstruction arguments and the full IUT initial-data construction have not been independently audited. IUT I, Example 3.5, was found as a further source lead but not fully read in this turn; no new claim depends on it. These are later scope limits, not missing passages of the Frobenioid results imported here. The unsuccessful exact-phrase searches establish no novelty. The completed work imports known inputs; it proves no result beyond the checked literature.

## Mathlib

Full marked-localization target: **not checked**. Supporting Frobenioid, arithmetic Picard and degree results: **not checked**. No absence or formal verification is claimed.
