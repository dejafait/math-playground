# Nine-union common-coordinate locator — completed scope review

TARGET: Determine exactly when L041's tau=1 local converse has a persistent locator at its common coordinate, retaining arbitrary extension-field weights and original finite parameters.
CHECKED: 2026-10-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed five narrow common-root, Hankel-pencil, persistent-locator and modified-syndrome searches; compared L010, L011, L016 and L041 and ATTEMPTS/008–009; no inspected exact arbitrary-triple persistence theorem was located.
SOURCE_EVIDENCE: Reused Hall Theorem 5.1.1, printed pp. 63–64, and Marquez-Corbella–Pellikaan section 5, printed pp. 7–8; freshly inspected Hall Modifying Codes section 6.2, Theorem 6.2.1, Proposition 6.2.2 and its full proof and J-syndrome algorithm, printed pp. 82–84; checked the live Chojecki author source's DR2 statement/proof and existing compiler coverage, citations below.
COMPARISON: L041 already gives all gated local weights and nonzero D at the three selected parameters; L010 gives the actual determinant locator. L016 supplies the fixed-triple analytic antecedent, while L011 bounds a pencil after persistence is assumed. Standard puncturing/recurrence inputs do not classify persistence in L041's three free shared-coordinate parameters.
GAP: Obtain an exact necessary-and-sufficient common-locator criterion in the local weight parameters, beyond the tautological vanishing of its coefficients, retaining full-weight and original-chart degeneracies. Completion and universal extraction remain independent.
REASON: Essential algebraic and coding ingredients are covered, so one bounded specialization is justified; no new persistence relation or mathematical calculation was derived in this literature-only review.
SCOPE: Exact TARGET only: F=F_(97^20), H order sixteen in F_97, k=8, pinned cell, eight shifted moments, L041 tau=1 supports with one common coordinate and one double-only coordinate, singleton counts (2,2,3) up to permutation, arbitrary F weights and three distinct original finite parameters, lambda and all present weights nonzero, unrestricted excluded [v]. The local converse is not assumed to satisfy sixteen-count equality or common-locator nonvanishing.
LITERATURE_REASON: This changed local persistence target was REVIEW_REQUIRED after the L041 audit; fresh coverage compares erasure-modified syndromes and exact recurrence tests with its free-weight scope, reusing adequate general coding and MCA assessments.

## Main gap, intermediate use and bounded test

Arbitrary sixteen-error equality remains the main gap: the global interval
is 11/q–16/q against allowable fifteen. The precise intermediate target
is TARGET. A criterion would distinguish local tau=1 triples admitted
to L010's nonpersistent branch from triples instead controlled by L011.
It would not establish universal extraction, any completion to sixteen,
challenge-level ABF26 identification or global fifteen.

Continue only if an explicit condition in the three shared-coordinate
weight parameters can be established in both directions, with every
full-weight gate and original finite parameter difference retained.
A factorization, reduced rank condition or finite set of explicit relations
is useful only if its equivalence and exceptional cases are proved.
Merely copying the definition ell_common(T)=0, checking samples or counting
roots without proving polynomial identity is not an advance. If the
bounded attempt cannot go beyond that tautology, preserve its evidence and
reassess this mechanism; an essential uncovered theorem requires another
scope review. No calculation or persistence formula is asserted here.

## Primary sources and exact overlap

J. I. Hall, *Notes on Coding Theory*, undated author-hosted
[GRS chapter](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
Theorem 5.1.1 and proof, printed pp. 63–64. Reuse the full extraction in
`2026-10-05-two-block-moment-obstruction.md`: over any field, distinct
points and nonzero multipliers with 0<k<=n give dimension k and distance
n-k+1. F, H and the unit multipliers satisfy these hypotheses.

I. Marquez-Corbella and R. Pellikaan, *A characterization of MDS codes
that have an error correcting pair*, FFAA 40 (2016), 224–245,
[DOI](https://doi.org/10.1016/j.ffa.2016.04.004), accepted manuscript dated
2016-02-29, section 5, Definitions 5.1–5.2, Lemma 5.3 and following
unnumbered GRS shortening formula, printed pp. 7–8. Reuse the precise
extraction and applicability checks in
`2026-10-07-nine-coordinate-triple-compatibility.md` and L041.
They already cover the one-dimensional shortened kernel and multipliers;
no shortening or distance reproof is needed.

Hall, [Modifying Codes chapter](https://users.math.msu.edu/users/halljo/classes/codenotes/Mod.pdf),
section 6.2, Theorem 6.2.1 and Proposition 6.2.2 with complete proof,
printed pp. 82–83, and J-syndrome algorithm, printed p. 84, freshly read
2026-10-08. Distinct evaluation points and nonzero multipliers define
GRS over a field. Puncturing g positions retains dimension k when enough
points remain. The dual multipliers change from u_i to
L_erased(alpha_i)u_i; simple deletion is insufficient. The proof uses
L=L_retained L_erased and the reciprocal evaluation derivative formula.
The theorem corrects g erasures and e errors if g+2e<=n-k.
One deletion from n=16,k=8 and e=3 meets that hypothesis. The modified
syndrome uses those adjusted multipliers, truncated at redundancy minus g.
This covers supporting punctured-code conventions only. Translating to
L010's shifted moments and polynomial in X, and deciding persistence as
T varies, remains the next mathematical task; no such relation is derived
here. A reciprocal decoder locator must not be silently identified with
L010's locator.

[Chojecki, live RS_MCA_Paving_v9.2.tex](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex),
source dated July 17, 2026, inspected 2026-10-08; mutable and not certified
identical to an ePrint version. Read `drc:lem-locator-recurrence`, DR0–DR2
and complete proof, source lines 2785–2842. Weighted distinct Vandermonde
columns and a fixed error support of size t give span membership exactly
by the R-t recurrence equations. Its annihilator proof uses MDS rank and
multiplication by the monic support polynomial. This is a fixed-support
test, not a persistence criterion for a varying pencil. Reuse the exact
compiler comparison already read in the nine-coordinate assessment:
it determines finite transverse support intersections, not common locator
identity. A literal search of this live source for “persistent” found no
match; that textual absence establishes neither mathematical absence nor
novelty. No challenge-definition correspondence is imported.

## Local duplicates, recorded failures and search limits

Read L041's complete criterion, converse and common-coordinate qualification,
L010's determinant definition and pointwise proof, L011's full persistent
transfer proof, and L016's analytic parameterization, gates, quotient
reduction and fixed-certificate scope. L041 already proves nonzero D at
all three parameters and rules out every noncommon persistent coordinate.
The new task is solely its remaining common-coordinate gate. L016 uses
supports {1,8,12,18}, {1,8,22,27}, {1,33,47,50} at 0,1,2; its count five
requires a fixed-label certificate and is not imported. L011 assumes
persistence; its twelve bound does not determine when persistence occurs.
No duplicate exact arbitrary-support criterion was found locally.

ATTEMPTS/008 records why determinant-only enumeration misses the
zero-syndrome kernel and why prime-field samples do not exhaust extension
weights. ATTEMPTS/009 stops the completed fixed-triple sixteen generator.
This target uses L041's full kernel and changes the support scope; it does
not rerun that generator or override its stop. Preserve ATTEMPTS/017,
/019, /020 and /021 as recorded in the reused nine-coordinate assessment;
none supplies universal extraction or licenses support-only completion.

Queries actually issued on 2026-10-08:

- `"Reed Solomon" "affine" "common root" syndrome locator`
- `"Hankel pencil" "common" "root"`
- `"Reed-Solomon" "persistent locator"`
- `"Reed-Solomon" "modified syndromes" erasure locator Hall`
- `"affine" "syndrome pencil" locator common coordinate`

Results included signal-processing Hankel methods, decoder patents,
error-erasure syndrome varieties and a coset-leader key-equation article.
These were search leads, not inspected matching theorems or premises.
No inference of novelty follows from their snippets. The named primary
Hall passage was inspected instead of adopting an implementation formula.
Parked ABF26/Jo access issues are independent of this frozen-model target
and were not retried. No cross-notebook input is used. Mathlib coverage
of the exact persistence criterion is not checked; neither absence nor
formal verification is claimed.

## Ready continuation

Approve one bounded REPRODUCTION attempt on the unchanged TARGET under
SPECIALIZE. Essential inputs are L010 and L041. Use L016's analytic
antecedent and L011's persistent branch only within their stated scope.
Known puncturing and recurrence statements should be cited; the difference
requiring proof is exact dependence on arbitrary labels, extension-field
weights and original finite parameters, including every degeneracy.
Do not impose a rational chart or use L016's count. A coordinate-elimination
or determinant manipulation is justified only to resolve this gate; no
new decoder theorem is needed. If a later continuation changes this scope,
it requires its own assessment. This approval is the separate literature
step requested by checkpoint 086; no lemmas or mathematical scripts were
written, and the global argument is unchanged.
