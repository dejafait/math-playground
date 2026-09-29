# Genus-three Prym homomorphisms — literature assessment

TARGET: Test whether genus-three etale abelian-cover Prym factors admit any nonzero homomorphism to or from a power of A, retaining rational descent and all L032 spin constituents, as the prerequisite for transferring their degree-four determinant classes.
CHECKED: 2026-09-27
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched genus-three and abelian-cover Prym/Kuga-Satake homomorphisms, common factors, spin constituents and product Hodge groups; read the primary statements listed below. No inspected theorem states the exact saved homomorphism conclusion.
SOURCE_EVIDENCE: Patel-Zhang, arXiv:2506.13729v2, Theorem 2.4 and Lemma 2.9--Remark 2.11, https://arxiv.org/pdf/2506.13729v2#page=5; Moonen-Zarhin, arXiv:math/9901113v1, sections 1.2 and 3.1, https://arxiv.org/pdf/math/9901113v1#page=7; Borovoi, Proposition (a),(d), https://www.math.tau.ac.il/~borovoi/papers/Hodge-eng.pdf#page=1; Moonen, sections 1.5--1.6 and Corollary 4.5, https://www.math.ru.nl/~bmoonen/Lecturenotes/MTGps.pdf#page=8; the reviewed RM representation inputs are reused through L032.
COMPARISON: Known results supply the rational Prym factors, character multiplicities, endomorphism centralizer, joint-group projections and passage between abelian maps and Hodge morphisms. They support a constituent comparison without assuming a general cover or cover-equivariance of the map; its application to this A remains to be written and checked.
GAP: Apply the known framework to the joint Hodge representation, justify the character projectors and all rational maps, and decide whether a common constituent can occur. Retain the full L032 representation, powers, isogenies and cohomological contravariance; total source dimension is unrestricted.
REASON: Import the general statements and reserve their exact homomorphism specialization for a separate research turn, classified as REPRODUCTION if successful. The prerequisite can decide this transfer channel, but it does not supply beta_U, algebraic kappa or an exclusion of arbitrary correspondences.

## Hypotheses

Retain L032's very-general rank-eighteen cubic-RM data:
T=T(S), End_Hdg(T)=E=Q(zeta_7+zeta_7^(-1)), dim_E T=6, and
the full A with H^1(A,Q)=C^+(T,q). No specialization with a larger
endomorphism algebra is included. A Prym factor P is the abelian
subvariety selected by a nontrivial irreducible rational
representation of the finite abelian group of a connected etale
cover C -> C_0, where C_0 has genus three. The group order and
factor dimension are unrestricted, and C_0 need not be general.

The question concerns Hom(P,A^r) and Hom(A^r,P) for every r>=1,
up to isogeny, without requiring cover-equivariance. Reuse the
[transfer assessment](2026-09-27-cubic-rm-generalized-prym-transfer.md),
the [small-factor assessment](2026-09-27-cubic-rm-kuga-satake-small-factors.md)
and the [primary target audit](../../foundations/01-target-and-scope.md).
The rational Hodge conjecture and the saved intermediate target
are unchanged.

## Conclusion

The source review is complete: SPECIALIZE. The remaining task is
an application of known representation and Hodge-theoretic tools,
not a reproof of the Prym cycle theorem or RM group theorem.
No essential source for that bounded application remains unread.
The exact Hom answer has not been established in this turn.

This step is LITERATURE / NOVELTY_UNCHECKED / EXPLORATION.
Supporting statements are imported by citation; no new result is
derived and no progress beyond the checked literature is claimed.
No homomorphism vanishing, new genus bound, transfer image or cycle
is asserted. The specialization is reserved for a later invocation.

## Proof

This section records inspected statements and applicability
obligations, not a proof of the saved Hom claim. Page references
below use PDF pagination.

### The geometric source and its rational factors

Reread Patel--Zhang, *Algebraicity of Hodge classes on some generalized
Prym Varieties*, [arXiv:2506.13729v2, 23 May 2026](https://arxiv.org/abs/2506.13729v2):
[section 2.2 and Theorem 2.4, pp. 4--5](https://arxiv.org/pdf/2506.13729v2#page=4),
and [Lemma 2.9, Corollary 2.10, Remark 2.11 and section 2.6,
pp. 6--7](https://arxiv.org/pdf/2506.13729v2#page=6).
Rational group-algebra idempotents select abelian isogeny factors.
For the nontrivial part, each character has H^1 multiplicity
h=2g(C_0)-2, and the associated product-of-fields module is free
of rank h. This statement does not assume a general cover.
Only nontrivial factors are used here; Remark 2.11 is not applied
to the invariant Jacobian summand. The determinant cycles remain
the previously reviewed supply, with no transfer to A stated by
these passages.

### Endomorphisms and the joint Hodge group

Read Borovoi, *The Hodge group and endomorphism algebra of an
Abelian variety*, [English translation of the 1981 note,
Proposition (a),(d), pp. 1--2](https://www.math.tau.ac.il/~borovoi/papers/Hodge-eng.pdf#page=1).
For a complex abelian variety the Hodge group is connected
reductive, and its commutant on rational H_1 is End^0.
This includes all algebraic endomorphisms; it does not require
the cover algebra to be the whole endomorphism algebra or its
center. The theorem bounding the number of simple group factors
is not used.

Read Moonen--Zarhin, *Hodge classes on abelian varieties of low
dimension*, [arXiv:math/9901113v1, 26 January 1999,
section 1.2, p. 3](https://arxiv.org/pdf/math/9901113v1#page=3),
and [section 3.1, p. 7](https://arxiv.org/pdf/math/9901113v1#page=7).
The product Hodge group projects surjectively to each factor's
group; powers have the same group acting diagonally. These formal
statements have no low-dimensional hypothesis. They do not assert
that the product group is the full product.
Also read Theorem 3.2 and Lemma 3.4, pp. 7--8. Their stronger
conclusions retain additional divisor-generation/type or
unique-module hypotheses, which are not supplied here. They
are not imported as a ready answer to this Hom question.

Read Moonen, *An introduction to Mumford--Tate groups*, version
11 May 2004, [sections 1.5--1.6, pp. 3--4](https://www.math.ru.nl/~bmoonen/Lecturenotes/MTGps.pdf#page=3),
and [Proposition 4.4, Corollary 4.5 and Lemma 4.6, pp. 8--9](https://www.math.ru.nl/~bmoonen/Lecturenotes/MTGps.pdf#page=8).
Polarizable rational Hodge structures are semisimple. The H_1
functor identifies abelian varieties up to isogeny with the
appropriate rational weight-minus-one structures. In the tensor
category generated by a Hodge structure, its morphisms are exactly
the Mumford--Tate equivariant maps. Lemma 4.6 also states the
surjective projections for direct sums of Hodge structures.
Switching to H^1 requires
duals and reversed arrows. These are not algebraicity statements
for arbitrary higher-degree Hodge correspondences.

### Reuse of the target representation

Reuse Schlickewei's [Theorem 3.3.1 and section 3.5](https://arxiv.org/pdf/0907.2503v1#page=9)
and van Geemen's [section 5.4 and Lemma 5.5](https://arxiv.org/pdf/math/0609839v1#page=16)
through their completed assessment and L032; their hypotheses
have not changed. The notebook already retains all eight complex
spin types, each of dimension 64 and multiplicity 256. These are
existing data, not a new calculation. The rational factor bound
32 stops the earlier dimension-at-most-six recipe, but is not by
itself an answer when dim P is unbounded.

### Difference left for the specialization

The proposed test must use one joint group for the two actual
rational Hodge structures. Comparing modules for unrelated groups
does not decide Hom. The review identifies these checks for the
single test:

1. Establish how the rational cover algebra acts on P and how
   its complex character projectors interact with the joint
   Hodge-group action. Do not require a proposed homomorphism to
   commute with the cover action or treat these projectors as
   rational abelian factors.
2. Use the actual joint-group projection in comparing the complete
   target representation with the source. Account for reducibility
   of source character spaces, additional Prym endomorphisms and
   all target multiplicities. A generic full unitary-group assertion
   about P is not an input to this test.
3. Start with a rational map, justify equivariance and the
   subquotient comparison, and translate back through H^1
   contravariance. Include powers and isogenies. An arbitrary
   complex linear map is not an existence certificate.

The discriminating threshold is a common constituent compatible
with an actual rational Hodge morphism. Establishing that none can
occur would stop just this homomorphism channel. If one survives,
continue only with a rational-map and geometric-source certificate;
the whole beta_U must then lie in the transferred cycle space.
The source formula and L032's data are available, but their Hom
consequence is deliberately not derived here.

Higher-genus degree-changing transfers and arbitrary algebraic
correspondences remain open. Algebraic kappa is a separate input.
The cycle span remains 21 on the known family, with three attained
RM directions against four required; the universal target requires
all rational Hodge classes. No complete candidate appears.
This is the second consecutive exploration turn after L032.
Complete the bounded test and its continuation/stop decision within
the existing three-turn window, without restarting that window.

### Search and access record

Queries on 2026-09-27 included:

- `"Prym" "Kuga-Satake" "homomorphisms"`
- `"genus three" "Prym" "Kuga Satake"`
- `"Kuga Satake" "Prym" "abelian cover"`
- `"Prym" "homomorphisms" "Hodge group"`
- `"Prym" "homomorphisms" "spin"`
- `"abelian varieties" "Hodge group" "Hom" "product" projections surjective`
- `"abelian varieties" "endomorphism" "irreducible constituents" "Hodge group"`
- `"Hodge group" "endomorphism algebra" "centralizer" Moonen Zarhin`
- `Moonen Zarhin "Hodge classes on abelian varieties of low dimension"`

No inspected matching Hom theorem resulted. The comparison rests
on opened primary text, not search snippets. The Utrecht copy of
Moonen--Zarhin failed to open; its versioned arXiv PDF resolved
access. Borovoi's author PDF was read directly. The Moonen notes'
version date is printed on p. 1. Patel--Zhang's arXiv submission
record confirms the reused v2 date.

Specialized hyperelliptic Prym vanishing and spin-bundle papers
returned by searches remain uninspected leads and are not used.
Earlier quaternionic-Prym and low-dimensional Weil comparisons
are reused from their saved assessments. The original
Lange--Rodriguez source behind Patel--Zhang Theorem 2.4 was not
independently read; the explicit theorem there supplies the factor
statement used here. No theorem or originality claim is inferred
from an abstract or from failure to find another source.

## Mathlib

Coverage of the full target: **not checked**. The named results
above are inspected supporting inputs or explicitly reused inputs,
not a claimed match for the complete Hom conclusion. No Mathlib
theorem name or absence claim is asserted.
