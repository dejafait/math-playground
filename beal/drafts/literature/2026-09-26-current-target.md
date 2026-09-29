# Boundary fourth-power/cube literature assessment

TARGET: Test whether prime-power allocation in X^4-Y^4=(X^2-Y^2)(X^2+Y^2), accounting for the shared factor 2, yields a height-decreasing descent for the boundary signature (4,3,4).
CHECKED: 2026-09-26
DECISION: IMPORT
SEARCH_EVIDENCE: Exact-equation, generalized-Fermat, and descent queries led to Bennett–Chen–Dahmen–Yazdani Section 5; its explicit reference to Cohen Proposition 14.6.6 was followed to the complete statement and both proof cases, not just a search excerpt.
SOURCE_EVIDENCE: Cohen, Number Theory II (Springer, 2007), Section 14.6.3, Proposition 14.6.6, pp. 484–485, read in a full-text transcription; bibliographic identity checked at https://link.springer.com/chapter/10.1007/978-0-387-49894-2_6; exact access links and supporting reads below.
COMPARISON: Cohen covers the required primitive difference equation at exponent 3 without a height, parity, or base-one exception. This supplies the desired exclusion but does not establish the particular height-decreasing map proposed in the saved action; an independent descent would reproduce an already covered conclusion.
GAP: No source-statement gap remains for the boundary exclusion. Its local applicability and exponent-divisor consequences remain to be assembled; uniform emptiness of the other residual signatures remains missing.
REASON: Stop developing a new descent for this fixed exclusion and import the named theorem. No changed hypothesis, effective constant, or implementation requirement justifies a reproof; the conclusion is known within the sources checked.

## Relevance and stopping test

The main gap is zero positive primitive solutions for every residual signature after L002 and the assembled exclusions. The proposed intermediate target was a descent preserving primitivity and decreasing a positive integer height in the boundary case. Its downstream use would be exclusion of that case and its L002 divisor extensions; it would not settle unrelated mixed signatures or the surviving repeated-cube primes.

The source test was an unconditional result with **zero** nonzero coprime solutions for the difference equation, covering both parity cases. A plus-sign theorem, first-case restriction, or finite-height search would not meet this threshold. A full match warrants citation instead of developing a descent. The read proposition meets that threshold. Whether the particular proposed allocation itself yields a height-decreasing map has not been tested or disproved.

The prior assessment's failed match to Darmon's p >= 11 theorem is retained below. C002a already covers the plus-sign placement but explicitly leaves the even-power sign change unjustified. Attempts 001–004 concern unrestricted congruences and repeated-cube shortcuts; they neither prove nor refute the proposed boundary descent. This is new redundancy evidence, not a repeat of those stops. No exploration calculation or mathematical derivation was performed.

## Search and access record

Representative queries on the check date were `"x^4" "y^4" "z^3" Fermat difference`, `"difference of two biquadrates" "cube"`, `generalized Fermat 4 4 3 equation Euler`, `"Generalized Fermat equations: A miscellany"`, and `"Cohen" "Proposition 14.6.6"`. Initial broad searches were inconclusive. The useful reference chain was the research paper's Section 5 to the numbered book proposition. Search snippets and the MathOverflow discussion returned by the last query were discovery aids, not mathematical premises. No novelty claim follows from the searches.

- **Cohen, exact match read:** Henri Cohen, *Number Theory, Volume II: Analytic and Modern Tools*, first edition, Graduate Texts in Mathematics 240, Springer, 2007, Section 14.6.3, Proposition 14.6.6, pp. 484–485. The statement and complete printed proof were read in a [transcription of the book](https://dokumen.pub/number-theory-volume-2-analytic-and-modern-tools-2-0387498931-9780387498935.html). The [publisher book record](https://link.springer.com/book/10.1007/978-0-387-49894-2) and [chapter record](https://link.springer.com/chapter/10.1007/978-0-387-49894-2_6) confirm edition, volume, and chapter identity; those pages provide metadata, not the theorem text. This is a read of Cohen's text through a mirror, not a claim to have retrieved publisher-hosted full text. Section 14.6.6 is a different subsection; the matching **proposition** is in Section 14.6.3.
- **Reference and scope comparison read:** Michael A. Bennett, Imin Chen, Sander R. Dahmen, and Soroosh Yazdani, *Generalized Fermat equations: A miscellany*, International Journal of Number Theory 11(1) (2015), 1–28, DOI [10.1142/S179304211530001X](https://doi.org/10.1142/S179304211530001X), Section 5, pp. 22–24. Read in a [transcription of the journal version](https://paperzz.com/doc/8355869/generalized-fermat-equations--a-miscellany---ubc-math), bearing the production stamp November 14, 2014 and publication date July 8, 2014. Section 5 explicitly cites Cohen for both signs; Section 5.1 then limits its detailed discussion to the plus sign. Its Lucas attribution discussion is supporting context, not a substitute for the exact minus-sign statement. The [author-hosted PDF](https://www.math.ubc.ca/~bennett/BeChDaYa-IJNT-2015.pdf) timed out on detailed retrieval; the [July 2013 VU preprint](https://www.few.vu.nl/~sdn249/BeChDaYa-misc.pdf) returned 403. Neither inaccessible PDF is represented as read in full.
- **Earlier mismatch reread:** Henri Darmon, *The equation x^4-y^4=z^p*, [author PDF](https://www.math.mcgill.ca/darmon/pub/Articles/Research/10.Fermat-44p/paper.pdf), header dated September 9, 2007, Theorem I, pp. 1–2, and references, pp. 4–5. Its modularity hypothesis, p >= 11, and congruence/parity clauses remain essential; it supplies no p = 3 application. Powell's first-case paper and the original Lucas/Swift texts were not read and are not used as premises.
- **Errata checked:** Cohen's [author-hosted errata](https://www.math.u-bordeaux.fr/~hecohen/deabookerrata.pdf), internally dated November 30, 2008. The Volume II corrections and targeted searches located no entry for pp. 484–485. This reports the checked document's scope, not an assertion that no later correction exists.
- **Target statement rechecked:** [Mauldin's primary formulation](https://sites.math.unt.edu/~mauldin/beal.html) still matches local GOAL.md, including positivity and bases equal to one. The nominated [AMS endpoint](https://www.ams.org/profession/prizes-awards/ams-supported/beal-prize) was inaccessible in this review; its current contents are not claimed to have been read.

## Hypotheses

For the cited proposition, x, y, z are nonzero coprime integers, and either sign in x^4 ± y^4 = z^3 is permitted. These are integer solutions, with no upper bound on their bases.

## Conclusion

Cohen's Proposition 14.6.6 excludes every such triple. Its minus clause is the exact required external input; the plus clause overlaps C002a.

## Proof

Imported by the precise Cohen citation above. The printed proof separates the odd-z difference case (together with the plus case), using rank-zero elliptic curves, from the even-z difference case, using cubic Fermat. Both cases were read. The cited parametrizations and rank computations were not independently reproduced. No new allocation, descent map, valuation calculation, or local corollary is asserted in this literature turn.

## Mathlib

Full statement and supporting results: **not checked**. No matching declaration, absence claim, or formal verification is asserted. The numbered book proposition is a mathematical citation, not a Mathlib reference.

## Assessment decision

The new evidence makes an independent descent unnecessary for the stated downstream goal; it does not show that the descent mechanism fails. The result is known and imported as source content, with no progress beyond the checked literature claimed. The separately [screened import target](2026-09-26-cohen-boundary-import.md) reuses this read without adding a new mathematical mechanism. The local argument and DAG have not yet been extended; PROGRESS.md holds the sole continuation action.
