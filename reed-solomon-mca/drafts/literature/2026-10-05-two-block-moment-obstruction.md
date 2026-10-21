# Two-block moment realizability: completed source comparison

TARGET: Assess whether the standard RS distance/injective-restriction argument excludes realization of L023's two-block support family by a pencil satisfying L010; distinguish this exact obstruction from arbitrary moment-compatible support families.
CHECKED: 2026-10-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Targeted RS minimum-distance, affine-syndrome fixed-support and MDS sparse-representative searches; inspected Hall Theorem 5.1.1 and proof, compared L010 and L023 with the local two-block and incidence failures; exact queries and limits below.
SOURCE_EVIDENCE: J. I. Hall, Notes on Coding Theory, author-hosted GRS chapter, undated online copy retrieved 2026-10-05, Theorem 5.1.1 and proof, printed pp. 63–64, and interpolation discussion p. 65; reused the October 3 persistent-root assessment for general proximity-gap scope; read L010 through its kernel/distance argument and L023 in full.
COMPARISON: The RS distance theorem and L010's eight-column moment invertibility cover the required linear-code inputs. No inspected source states the full doubled-cyclic-family obstruction; its affine-parameter and support-pattern passage remains a separate mathematical specialization.
GAP: Check that restriction to each eight-coordinate block gives affine error-coordinate functions for every parameter, then test whether their coordinate zeros can accommodate the eight prescribed full-weight supports in that block; do not assume this passage or its conclusion.
REASON: Essential source coverage is now adequate for one bounded proof attempt using existing MDS/moment facts; a full obstruction is neither imported nor proved in this literature turn, and no originality is inferred.
SCOPE: The original TARGET and the COVERED_TARGET below only, over every field and subgroup allowed by L010, for any bijective labeling of L023's vertices by H and sixteen distinct finite parameters satisfying L010's equality conditions. No arbitrary-support classification, normalization to L022, or challenge-definition correspondence is covered.
COVERED_TARGET: Prove or refute that no bijective labeling of L023's two-block support family by H can be the sixteen full-weight error supports of an affine pencil satisfying L010, using eight-coordinate restriction and coordinate root counting.

## Gap, intermediate target, and decision test

The pinned four-omission interval remains 11/q–16/q, whereas fifteen
parameters are allowable at q=97^20. The intermediate target excludes
one fully specified abstract family from equality, for every coordinate
labeling and extension-field choice of weights. It could support a later
classification of moment-compatible families; it would not force a disjoint
triple or improve the uniform sixteen bound by itself.

Continue if the existing distance/kernel inputs justify an affine lift on
each eight-coordinate block and a rigorously incompatible coordinate-zero
pattern. Abandon this proposed exclusion if a compatible pencil is found;
if the lift or root-count passage has a missing hypothesis, record that
failure rather than claiming a bound. The next step must prove or refute
the precise obstruction, not merely sample labelings. No such passage is
derived here.

## Primary theorem and applicability

[Hall's author-hosted GRS chapter](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf)
is an undated 13-page PDF, printed pp. 63–75, retrieved October 5, 2026.
Read §5.1's definition, Theorem 5.1.1, its full proof on pp. 63–64,
and the interpolation discussion on p. 65. The theorem allows any field,
distinct evaluation points, nonzero column multipliers, and 0 < k <= n;
it gives dimension k and minimum distance n-k+1. Its proof uses the
polynomial root bound and supplies an explicit degree-(k-1) product
attaining the distance, so neither the Singleton bound nor an unread
appendix is essential to that equality argument. The interpolation
paragraph states uniqueness from k distinct evaluations.

For L010 take n=16, k=8, evaluation points H, and all multipliers one.
These meet every hypothesis and the distance is nine, independently of
the extension degree. This is a direct parameter specialization of the
cited theorem, not a new distance proof. L010 already proves ker(sigma)=C
and invertibility of any eight moment columns using nonzero H labels.
The next attempt may use that existing proof; it need not reprove RS
minimum distance, build a decoder, or invoke dual multiplier formulas.
The remaining affine-lift and coordinate-pattern inference is not a
statement of Hall's theorem and must be justified separately. This is why
SPECIALIZE, rather than IMPORT of the full desired obstruction, is used.

## Searches, overlap, and limits

Queries on October 5, 2026:

- `Reed Solomon codes minimum distance n k 1 lecture notes theorem evaluation injective Vandermonde`
- `Reed Solomon affine line sparse error supports fixed block injectivity syndrome`
- `"affine" "syndrome" "fixed support" Reed Solomon`
- `Reed Solomon MDS sparse representatives affine line common support distance`

Opened M. O'Sullivan's author-hosted Math 696 RS notes and the
Guruswami–Rudra–Sudan book chapter 5 as supporting leads. The retrieved
O'Sullivan Theorem 1.2.1 gives the classical cyclic RS distance statement
and points to a Vandermonde exercise. Those cyclic parameter conventions
are unnecessary here; no essential input is taken from that exercise.
The book's retrieved Definition 5.2.1 states distinct evaluation points
and k <= n <= q. Its distance proof was not selected for further reading
because Hall covers the needed statement and proof with arbitrary fields.
These are supporting leads, not additional independent obstruction proofs.

Searches also returned support-constrained generator-matrix/GM-MDS
papers and the rs-mca author repository. Those hits were not read as
full-statement matches and are not used as premises. Choosing a generator
matrix's zero pattern is a different question from placing sixteen sparse
coset representatives on one prescribed syndrome line. No novelty claim
follows from search absence. The existing October 3 persistent-root
assessment supplies the already inspected general MCA/proximity-gap
scope; no unchanged July source retrieval or general MCA audit is repeated.
No essential source for this selected elementary restriction test is blocked.

## Local duplicates and recorded failures

L010's uniqueness and equality conditions are essential inputs, not the
conclusion being sought. L023 supplies the exact two copies of eight
supports and their coordinate incidence. Its cyclic intersection theorem
and finite tables are reused without a new combinatorial proof.
L013 and ATTEMPTS/006 exclude only L008's prescribed inputs with two
five-point blocks and a six-point complement. They neither duplicate nor
approve this arbitrary-labeling, two-eight-coordinate-block question.
ATTEMPTS/016 stops incidence alone; the present target adds actual RS
compatibility and does not reopen that implication. L022 is only a contrast:
no reduction to its saved triple or parameter normalization is assumed.

## Continuation and qualifications

Essential local inputs: L010 and L023. Unresolved assumptions to test:
existence of a bijection V -> H, sixteen distinct finite parameters,
nonzero error weights on the prescribed edges, and one actual affine
syndrome pencil with L010's nonpersistent equality conditions. These are
hypothetical realization data, not established objects. The proposed
coordinate functions must be justified even at parameters not assigned
to that block, and identically zero functions must be treated explicitly.
No locator nonvanishing may be inferred from incidence alone.

The COVERED_TARGET is a newly written ready continuation for separate
supervisor approval before the next mathematical invocation. Arbitrary
moment-compatible families, L022 normalization, and July ABF26
correspondence remain unresolved even if it succeeds. Mathlib coverage
of the exact obstruction and supporting statements is not checked;
no absence or theorem-name claim is made. No lemma, mathematical script,
DAG edge, or argument overview is changed by this literature review.
