# Ramified dyadic two-descent image — source comparison

TARGET: Certify the full two-descent Kummer image of L033's E0 over H2=Q2(2^(1/11)) using Bruin–Stoll LocalImage, with complete terminal-disk and square-class certificates.
CHECKED: 2026-10-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the rational-cubic dyadic assessment; compared the exact local data in L069–L071/L076 and stops ATTEMPTS/034–036; searched ramified dyadic local-image, LocalImage/SquareClasses, the BPT ramification clauses and exact-field/exact-curve variants; primary passages and actual queries are recorded below.
SOURCE_EVIDENCE: Bruin–Stoll author manuscript dated 14 March 2008, Remark 2.1 p.3 and Section 4 pp.6–10, including Lemma 4.4 and all SquareClasses/LocalImage proof cases; BPT arXiv:2001.02263v3, Section 1 pp.3–4, Definition 1.6(i)/(iv), Theorem 1.8 field proof p.5, Lemmas 1.3/1.5 p.4 and Theorem 1.11 first-claim proof p.7.
COMPARISON: The complete Bruin–Stoll algorithm includes ramified dyadic bases; BPT's independent field-algebra clause is the relevant replacement for L070's unramified good-reduction clause. These known results cover a complete certificate method, but do not supply this field's image representatives or its global restriction rank.
GAP: Essential method coverage is ready; a certified arithmetic model, actual image representatives, exhaustive disk evidence and exact equality tests remain to be constructed. No local image, new global direction, class-kernel value or integer exclusion is computed in this source review.
REASON: Specialize established complete methods to the saved ramified-base membership problem; keep the separation searches parked and do not reprove the general local-image or image-size theorems.
SCOPE: The exact full local membership problem and its necessary field-model, precision, exceptional-point, image-completeness and square-class certificates; no global-unit basis, global independence claim, localized class calculation, rank bound or integer exclusion.
COVERED_TARGET: Construct an exact membership test for the full two-descent Kummer image over L046's degree-eleven dyadic completion H2=Q2(2^(1/11)).
LITERATURE_REASON: Essential primary coverage for a changed ramified-base hypothesis was missing at invocation; this completes that review, rather than repeating literature on the exhausted separation target.

## Exact target, inputs and relevance

The reviewed saved action is retained as COVERED_TARGET above; TARGET
makes its next certificate attempt concrete. Use precisely

    E0: y²+y=x³−x²−10x−20,
    g(X)=X³−4X²−160X−1264,
    J2=H2[X]/(g), with distinguished generator θ.

L069 supplies the origin-preserving cubic coordinates X=4x, Y=8y+4.
L046 supplies H2, its Eisenstein model and residue field. L071 supplies
the rational cubic model and the exact change of generator. L076,
“Every dyadic factor”, proves that J2 is the ENTIRE degree-33 field,
not a selected factor. These are existing inputs, not newly proved
claims. The target is membership in δ(E0(H2)/2E0(H2)) inside J2*/J2*²,
with no scalar quotient. L033's five-isogeny singleton is a different
map. No cross-notebook input is used.

The main gap is primitive integer emptiness. A complete test at this
other base place could support further global filtering of L074's V_S.
L077 currently gives an upper bound fourteen, while eleven is the
desired unit threshold; the localized class contribution is also
unknown. Even a complete local answer would still need actual global
classes and independence from L077's two directions before improving
that bound. No such improvement is inferred from a local index.

## Primary statements and essential proof cases

Nils Bruin and Michael Stoll, *Two-cover descent on hyperelliptic
curves*, Math. Comp. **78** (2009), 2347–2370,
[DOI](https://doi.org/10.1090/S0025-5718-09-02255-8).
Numbering and pages here refer to the inspected
[author manuscript, 14 March 2008](https://mathe2.uni-bayreuth.de/stoll/papers/twocoverdescent.pdf).
Remark 2.1 uses square classes without scalar quotient for odd degree.
Section 4 assumes a characteristic-zero complete discretely valued
field with finite residue field and a square-free integral polynomial
with full irreducible factorization; it imposes no unramified-base
condition. Lemma 4.3's odd-residue shortcut is inapplicable here.

Lemma 4.4 assumes that the coefficient-minimum valuation of
h(x0+επ^e)−h(x0) exceeds v(h(x0)), with h irreducible. It proves
square-class constancy on x0+π^(e+v(4))O. Its norm argument and
square-neighborhood proof were read. SquareClasses includes square
feasibility, extra dyadic digits, empty residual-factor and linear-root
termination cases, with actual realization and finite termination.
LocalImage adds Weierstrass values, infinity, and the reciprocal chart
z=1/x with map z(1−zθ). Both pseudocode routines and all their
correctness cases, pp.8–10, were inspected, not merely Lemma 4.4.

Daniel Barrera Salazar, Ariel Pacetti and Gonzalo Tornaría,
*On 2-Selmer groups and quadratic twists of elliptic curves*,
Math. Res. Lett. **28** (2021), 1633–1659,
[DOI](https://doi.org/10.4310/MRL.2021.v28.n6.a1);
numbering refers to [arXiv:2001.02263v3, 17 September 2020](https://arxiv.org/pdf/2001.02263v3).
Section 1 uses the same monic-cubic Kummer map. Definition 1.6(i)
requires its entire algebra to be a field; unlike (iv), it does not
require an unramified base. L076 supplies exactly that field input.
Theorem 1.8's entire field-case proof was read: it treats either
unramified or totally ramified cubic extensions and obtains maximal-unit
representatives from even valuation. Remark 1.4 specifies maximal rings.

Lemma 1.3 gives |δ(E(F))|=[O_F:2O_F]|E(F)[2]| for any finite
F/Q_p. It cites Brumer–Kramer, *The rank of elliptic curves*, Duke
Math. J. **44** (1977), 715–743, Lemma 3.1; that original proof was
not newly inspected. Lemma 1.5 and Theorem 1.11's first-claim proof
give index 2^[F:Q2] under Definition 1.6. These provide an independent
completeness check, not representatives. Their general statements are
imported by citation; no new specialized cardinality or index is
established here. The separate U4 theorem and global class hypotheses
are unnecessary for this target.

## Certificate obligations for the approved specialization

The future attempt must retain the fixed θ throughout. Its output
must make membership decidable, rather than report an ambient size.
Save exact defining data and maps, every terminal or rejected disk,
the valuations and square-feasibility evidence justifying it, the
represented classes, and the comparisons identifying collisions.
Account separately for both coordinate charts and all exceptional
values, even when existing irreducibility removes a case. Every claimed
representative needs a point-existence certificate; a necessary residue
condition or a finite precision sample is insufficient.

The valuation is normalized at the actual base uniformizer, so the
source's v(4) must be evaluated in H2, not copied from Q2. Square
comparison takes place in the entire J2. A power order is not silently
the maximal ring, and L076 proves a field identification, not a maximal
integral basis. The attempt may construct and certify a suitable local
model, or use a certified local-field implementation; it must justify
the precision and every square/nonsquare decision used. The rational
cubic basis alone is insufficient as a maximal H2-integral basis.
Import the general methods; a new general local theory is unnecessary.

An optional implementation search found the official Magma handbook's
[general local fields](https://magma.maths.usyd.edu.au/magma/handbook/text/562)
and [element operations](https://magma.maths.usyd.edu.au/magma/handbook/text/569).
Only search-indexed excerpts were readable; subsequent page queries
did not expose the requested entries. These are **uninspected software
leads**, not essential theorem inputs. No backend availability, actual
version or computation is certified. This optional access issue does
not block the fully read mathematical algorithm and is not a reason
to repeat retrieval. Any implementation must report its own arithmetic
model and precision evidence. No service, API key or purchase is needed.

## Duplicates, recovery comparison and bounded test

Reuse `drafts/literature/2026-10-14-rational-cubic-unit-dyadic-pruning.md`
for the unchanged Simon Kummer interface and its prior local-algorithm
review. The additional work here is exact ramified-base comparison and
inspection of the relevant primary proof cases. L070/L071 decide the
rational base only; L076 identifies the other full field but computes
no image. The targeted records contain no duplicate membership test.

Three mechanisms were compared. The global supported-principal-element
search has exhausted its affine, quotient and fixed-basis tests:
[ATTEMPTS/034](../../ATTEMPTS/034-mixed-affine-supported-unit-list.md),
[035](../../ATTEMPTS/035-saved-affine-quotient-list.md) and
[036](../../ATTEMPTS/036-fixed-eleven-ideal-basis-search.md)
preserve the exact failures, without asserting nonexistence of a unit.
Computing L074's localized class-norm kernel would address an independent
contribution but does not supply missing unit restrictions and needs
unavailable certified global class data. The selected local-image
mechanism has complete primary method coverage and is independently
testable without principal generators or global unit completeness.
Do not enlarge the three parked searches.

Continue if one bounded attempt certifies the complete image, or saves
a concrete model/precision milestone toward it. Stop the particular
implementation if it cannot certify its arithmetic or complete coverage;
preserve its exact blocker and partial evidence. A resource cutoff is
not nonmembership, and a matching image-size check without certified
point images and exact class independence is not a membership test.
No global restriction rank, filtered dimension, class contribution or
integer lifting is assumed. A completed local image can be followed
only by a separately assessed global comparison, not by an automatic
claim that fourteen has decreased.

Actual searches included `"two-cover descent" "LocalImage" "SquareClasses"`,
`"2-descent" "ramified" "local image" elliptic`,
`Barrera Pacetti Tornaria 2001.02263 Theorem 1.8 ramified`,
`"H2" "2^(1/11)" elliptic descent` and
`"11a1" "ramified" "2-descent"`. The inspected sources cover the
general method; no exact-image classification for this field was located.
This is not a novelty claim. Simon's original quartic method and later
hyperelliptic generalizations are not needed beyond the reused interface;
search leads do not become imported theorem inputs.

The accessible [Mauldin primary statement](https://sites.cos.unt.edu/~mauldin/beal.html)
was rechecked: all six integers are positive, all exponents exceed two,
and the three bases share a prime. The nominated AMS page failed web
retrieval; no current prize-rule content is asserted. This matches the
existing target audit and changes no mathematical assumption.

This is a literature-only completion of method coverage, not a new
lemma or a computed local restriction. Mathlib matching and supporting
coverage for the ramified membership specialization: **not checked**.
PROOF.md and DAG.md need no change. The supervisor retains its separate
approval of a newly written ready continuation; no research calculation
was invoked during this review.
