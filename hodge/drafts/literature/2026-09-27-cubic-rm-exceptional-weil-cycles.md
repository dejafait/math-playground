# Exceptional cycles for the cubic Kuga--Satake tensor — literature assessment

TARGET: Review whether Schoen's algebraic Weil-class constructions or their published extensions supply beta_U on A^4 for the rank-eighteen cubic-RM Kuga-Satake variety, accounting for the nonzero torus-weight component in L031.
CHECKED: 2026-09-27
DECISION: EXPLORE
SEARCH_EVIDENCE: Searched Schoen's original and corrected Weil-class constructions, later fourfold/sixfold results, general CM-field secant sheaves and generalized Prym extensions; primary theorem statements and scope qualifications were read as detailed below.
SOURCE_EVIDENCE: Schoen (1988), Theorem 2.0 and Corollary 3.1, https://www.numdam.org/item/CM_1988__65_1_3_0.pdf#page=10; Schoen (1998), opening Theorem and Proposition 10; Markman, arXiv:2502.03415v2, Theorem 1.5.1 and Corollary 1.6.1, https://arxiv.org/pdf/2502.03415v2#page=9; Markman, arXiv:2509.23079v1, Theorem 1.1.2, https://arxiv.org/pdf/2509.23079v1#page=5; further direct links and locations below.
COMPARISON: Proven supplies include all Weil fourfolds, split Weil sixfolds over imaginary quadratic fields, and specified generalized Pryms; none of the inspected statements identifies this beta_U with its output. The general CM-field secant theorem retains algebraicity under deformation as a hypothesis.
GAP: An applicable abelian source, its field/polarization data and an algebraic transfer whose image contains the whole beta_U have not been identified; the nonzero component in L031 must be reached. Algebraicity of the separate Kuga--Satake correspondence kappa also remains open here.
REASON: The theorem-level review is complete without an unconditional import for beta_U. A bounded applicability test is justified; no failure of algebraicity or novelty follows from this noncoverage. Screen the low-dimensional abelian-factor test separately before calculating it.

## Hypotheses

Retain S, T, E, A, kappa and beta_U from L031 at a very general point
of the NS-fixed cubic RM locus: dim_Q T=18, dim_E T=6,
E=Q(zeta_7+zeta_7^(-1)), with the full Kuga--Satake variety and the
actual transported tensor in H^4(A^4,Q). The rank eighteen belongs
to T, and A^4 denotes a fourth power, not an abelian fourfold.

Reuse the [realization assessment](2026-09-27-cubic-rm-kuga-satake-realization.md)
for Varesco's conditional transfer and the rational target audit.
Reuse the [divisor assessment](2026-09-27-cubic-rm-kuga-satake-divisor-tensor.md)
and L031 for the obstruction. Their hypotheses have not changed;
neither previously assessed this exceptional-cycle supply.

## Conclusion

The exact saved review is complete. Known results are stronger than
the older special-field/fourfold comparison, but no inspected result
supplies beta_U under the saved hypotheses alone. This is a completed
noncoverage assessment, not an exclusion theorem for all transfers.
EXPLORE records that difference without asserting originality.

The step is LITERATURE / NOVELTY_UNCHECKED / EXPLORATION. Named
theorems below are reused by citation; nothing is reproved or claimed
beyond them. No decomposition, new cycle, or mathematical lemma is
derived. The attained span remains 21 on the Dickson family, with
three directions against four required; the universal gap remains.

## Proof

This section records precise citations and their applicability.

### Schoen's construction and its correction

Read Schoen, *Hodge classes on self-products of a variety with an
automorphism*, Compositio Math. 65 (1988),
[Theorem 2.0, p. 11](https://www.numdam.org/item/CM_1988__65_1_3_0.pdf#page=10),
[Corollary 3.1, pp. 24--25](https://www.numdam.org/item/CM_1988__65_1_3_0.pdf#page=23),
and Theorem 3.2, p. 26. Theorem 2.0 uses a cyclic curve cover with
even primitive-character multiplicity and branch exponents paired
as opposites modulo the cover order. Corollary 3.1 transfers the
constructed classes to its primitive Prym factor. This needs an
actual curve cover and identification with the required classes;
a field action alone does not provide those data.

Read Schoen's 1998 *Addendum*, Compositio Math. 114,
[opening Theorem and correction, pp. 329--330](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/D00460E4E67FC245D3C2943B5758216E/S0010437X98000682a.pdf/addendum_to_hodge_classes_on_selfproducts_of_a_variety_with_an_automorphism.pdf#page=1),
and [Proposition 10 and proof, pp. 332--333](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/D00460E4E67FC245D3C2943B5758216E/S0010437X98000682a.pdf/addendum_to_hodge_classes_on_selfproducts_of_a_variety_with_an_automorphism.pdf#page=4).
The correction says the 1988 Theorem 3.2 omitted a polarization
invariant required by its proof. The addendum proves algebraicity
of Weil classes on all fourfolds with balanced Q(zeta_3) action.
Proposition 10 reduces a fourfold of arbitrary discriminant to a
sixfold family of one fixed discriminant by adjoining a Weil surface
and contracting with its divisor classes. It is not a reduction
from arbitrary higher-dimensional abelian varieties to fourfolds.
Pagination here follows the PDF, 329--336.

### Stronger low-dimensional results

Read Markman, [arXiv:2502.03415v2, 8 June 2025,
Theorem 1.5.1 and Corollary 1.6.1, p. 9](https://arxiv.org/pdf/2502.03415v2#page=9),
and the [proof of Theorem 1.5.1, p. 88](https://arxiv.org/pdf/2502.03415v2#page=88).
The theorem supplies Weil classes on polarized abelian sixfolds
over any imaginary quadratic field with discriminant -1. Its
corollary, using Schoen's reduction, proves the Hodge conjecture
for abelian fourfolds without a discriminant restriction. The
paper expressly limits the constructed sheaves' semiregularity
proof to genus three. Thus older restrictions to Q(i), Q(zeta_3)
or discriminant one must not be presented as the current general
fourfold boundary. No suitable source or map to our A is identified.

Also read Floccari--Fu, *The Hodge conjecture for Weil fourfolds
with discriminant 1 via singular OG6-varieties*,
[24-page author PDF, Theorems 1.1--1.3, pp. 2--3](https://irma.math.unistra.fr/~lfu/articles/HCWeilViaOG6.pdf#page=2),
accessed 2026-09-27; published version: J. Math. Pures Appl. 210
(June 2026), 103876, [DOI](https://doi.org/10.1016/j.matpur.2026.103876).
It gives the Hodge conjecture for every power of a Weil fourfold
of discriminant one. Its K3 construction has generic Picard rank
16, as stated there. Neither a fourth power nor a four-dimensional
parameter space identifies the present rank-eighteen setting with
that construction.

### The general CM-field extension retains an algebraicity gap

Read Markman, [arXiv:2509.23079v1, 27 September 2025,
section 1.1 and Theorem 1.1.2, pp. 2--5](https://arxiv.org/pdf/2509.23079v1#page=2),
[section 1.2, pp. 6--7](https://arxiv.org/pdf/2509.23079v1#page=6),
and Lemmas 11.2.8--11.2.9, pp. 42--43. It starts with a CM field
K over a totally real F and specified secant sheaves on an abelian
X with F-action. With a nonzero-rank transform and the nonzero
Weil-projection condition of Proposition 1.1.1, Theorem 1.1.2
keeps its normalized Chern class of Hodge type. Algebraicity of
its transported Weil classes still assumes algebraicity of that
Chern class under deformation. Section 1.2 supplies a quadratic-F
example but explicitly supplies no such sheaf examples for
[F:Q]>2. This is a conditional framework, not an unconditional
cycle construction for our cubic data. Its kappa(E) is a normalized
Chern character, distinct from our Kuga--Satake embedding kappa.

Checked the newer [survey, arXiv:2509.23403v2, 11 February 2026,
Theorem 1.2 and Corollary 1.3, pp. 3--4](https://arxiv.org/pdf/2509.23403v2#page=3),
and [Question 11.4 and section 12, pp. 20--21](https://arxiv.org/pdf/2509.23403v2#page=20).
It retains the fourfold/split-sixfold theorem over imaginary
quadratic fields; Corollary 1.3 states the Hodge conjecture for
all abelian varieties of dimension at most five. The proposed
weaker semiregularity criterion
for higher dimensions and higher-degree CM fields is a question,
not an available deformation theorem. It does not remove the
conditional input above.

### A geometric extension in arbitrary dimension

Read Patel--Zhang, [arXiv:2506.13729v2, 23 May 2026,
Theorems 1.1--1.2 and section 1.3, pp. 2--3](https://arxiv.org/pdf/2506.13729v2#page=2),
and [section 4, pp. 10--13](https://arxiv.org/pdf/2506.13729v2#page=10).
For an etale cover of curves with finite abelian group G and base
genus g>=2, H^1 of its Prym is a module over the
nontrivial part of Q[G]. Its top exterior classes over that algebra,
in degree h=2g-2, are algebraic. Theorem 1.2 also extends to rational
representation factors. This is a geometric extension of
Schoen, so dimension alone does not exclude all reviewed supplies.
Here no such cover, Prym realization or transfer to beta_U is
given. The statement concerns those exterior classes, not every
Hodge class on a Prym or on its powers.

### Comparison with the exact required tensor

L031 supplies a nonzero projected component of beta_U on which a
divisor-fixing torus acts by t^2. That is the existing certificate,
not a new calculation in this review. A proposed exceptional supply
must reach this component and ultimately the whole rational beta_U.
The adjective exceptional only means outside the divisor algebra.
It does not identify beta_U as one of the determinant classes in
any theorem above. L031's complex projectors are not already
algebraic correspondences or rational abelian factors.

For any proposed import the missing applicability data are a
source variety, its required field action and polarization, and
algebraic pullback/pushforward operations with the correct tensor
image. The real field E on T is not by itself the CM-field action
required on a proposed abelian source. Conversely, the absence of
an identification here does not prove one impossible. An arbitrary
Hodge correspondence cannot be declared algebraic to make the
transfer: that would reintroduce the target as a premise.

The most concrete next prerequisite is whether this A has an
abelian subquotient of dimension at most six. If none exists, the
direct supply through homomorphisms from the reviewed low-dimensional
abelian varieties has no such source. A positive answer would still
require the appropriate Weil hypotheses and full tensor image;
factor existence alone would not finish the import. This test does
not exclude generalized Pryms, arbitrary higher correspondences,
or the general CM construction. Its
[separate assessment](2026-09-27-cubic-rm-kuga-satake-small-factors.md)
is pending; no factor-size calculation was performed here.

### Search record, relevance and stopping decision

Queries on 2026-09-27 included:

- `Schoen Hodge classes abelian varieties Weil type algebraic discriminant 1 fourth roots unity cube roots`
- `abelian varieties Weil type Hodge conjecture Markman 2025 2026 Schoen extensions`
- `cubic real multiplication Kuga Satake exceptional Hodge classes Weil classes rank 18`
- `Chad Schoen "Hodge classes" "1998" Proposition 10 Weil`
- `"Schoen" "Addendum" filetype:pdf Hodge`
- `"Algebraicity of Hodge classes on some generalized Prym varieties"`
- `"Kuga-Satake" "2509.23079"`

The original paper and addendum were read, resolving the essential
source gap in the pending assessment. Failed Numdam retrieval of
the addendum was replaced by the publisher PDF. The precise later
statements above were read, including the explicit conditional
qualification. No abstract-only lead is used to claim coverage.
Van Geemen's separate Q(i) construction, the original general
semiregularity papers and the proofs of all low-dimensional
classification inputs were not independently audited; the named
primary theorems above suffice for this scope comparison.

Three supplies were compared: low-dimensional Weil results,
generalized Pryms, and the CM-field secant framework. None supplies
an established transfer here. The bounded continuation selects
the first supply's factor prerequisite because it has a concrete
representation test before new cycle or sheaf construction.
The earlier support, bundle and divisor failures remain scoped
as recorded; this review neither repeats the divisor test nor
reopens the closed doubled-source recipe.

This is the first consecutive exploration turn after L031's
informative negative result. The factor screening and any later
test share the same three-turn allowance; a new target name does
not reset it. Algebraic beta_U would discharge one conditional
transfer input, with algebraic kappa and the universal Hodge target
still unresolved. No complete candidate is asserted.

## Mathlib

Coverage: **not checked**. The named source theorems establish
their stated Weil/Prym results or conditional criteria; none was
found to match algebraicity of this beta_U under the saved
hypotheses alone. That is a literature comparison, not a Mathlib
absence claim. No library theorem name or originality is asserted.
