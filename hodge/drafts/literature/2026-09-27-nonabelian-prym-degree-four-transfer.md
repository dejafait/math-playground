# Nonabelian Prym degree-four transfer — literature assessment

TARGET: Review whether nonabelian-cover Prym constructions supply algebraic degree-four classes with nontrivial derived Lefschetz-group action and an applicable transfer to the cubic-RM tensor beta_U.
CHECKED: 2026-09-27
DECISION: EXPLORE
SEARCH_EVIDENCE: Searched nonabelian and quaternionic Prym cycle constructions, exceptional degree-four classes, generalized Prym extensions, cover monodromy and Kuga-Satake realizations; the queries, versions and primary passages read are listed below.
SOURCE_EVIDENCE: van Geemen-Verra, arXiv:math/0103111v1, Proposition 2.4, sections 4.3--4.10, Proposition 5.3 and sections 6.5--6.9, https://arxiv.org/pdf/math/0103111v1#page=10; Landesman-Litt-Sawin, arXiv:2401.13906v2, Theorems 1.3 and 1.9 and Corollary 1.10, https://arxiv.org/pdf/2401.13906v2#page=3; additional primary comparisons below.
COMPARISON: No inspected theorem supplies both the required algebraic source class and a compatible transfer containing beta_U. The known cycle construction, conditional exceptional-class results, moduli descriptions and generic monodromy results have different conclusions and cannot be combined into an unconditional transfer.
GAP: An actual source with the required derived-group representation, an algebraic correspondence to A^4, and a certificate that its image contains the whole rational beta_U are still missing; algebraicity of kappa remains separate.
REASON: Complete this bounded source review and stop the current import search on the checked constructions. EXPLORE records noncoverage, not a theorem excluding every nonabelian cover; the next proposed mechanism requires its own review.

## Hypotheses

Keep the very-general data of L031--L034: dim_Q T(S)=18,
End_Hdg(T)=E=Q(zeta_7+zeta_7^(-1)), dim_E T=6, and
H^1(A,Q)=C^+(T,q). The fixed tensor beta_U has Kunneth
multidegree (1,1,1,1) in H^4(A^4,Q). A^4 is the fourth power
of the full Kuga--Satake variety. Keep every spin type and
multiplicity, rational descent, and the separate algebraicity
gap for kappa.

Reuse the [primary target audit](../../foundations/01-target-and-scope.md)
and the [conditional Kuga--Satake assessment](2026-09-27-cubic-rm-kuga-satake-realization.md).
The goal is still rational algebraicity on smooth projective
complex varieties. Reuse the
[generalized-Prym review](2026-09-27-cubic-rm-generalized-prym-transfer.md)
and [determinant-transfer assessment](2026-09-27-higher-genus-prym-lefschetz-transfer.md)
where their assumptions have not changed.

The local gap is algebraic realization of U outside the Dickson
locus. The intermediate target was an algebraic source for beta_U
outside the tested determinant mechanism. It could discharge one
input of the conditional transfer, while algebraic kappa and the
universal fourfold and higher-dimensional problems would remain.
Continue only upon identifying a qualifying source and a concrete
image question; stop this search if the inspected constructions
supply no such data. Exceptionality on a source alone does not
meet the required threshold.

## Conclusion

The exact saved review is complete. No qualifying transfer was
identified. Stop the present source-import search; preserve
nonabelian covers and arbitrary algebraic correspondences as
unresolved possibilities. This is a scoped research decision,
not a new impossibility theorem.

This turn is LITERATURE / NOVELTY_UNCHECKED / EXPLORATION.
The citations below supply known results. No theorem is reproved,
no new derived-group calculation is made, and no result beyond
the checked literature is claimed. The search consumes one
consecutive exploration turn after L034; changing direction
does not reset that count.

The algebraic span remains 21 on the known family, with three
attained RM directions against four required. Neither beta_U nor
kappa has been made algebraic at a very general transverse point.
No complete candidate appears.

## Proof

This section records source statements and their applicability,
rather than a mathematical derivation.

### Quaternionic cycle construction and the conditional spin example

Read van Geemen--Verra, *Quaternionic Pryms and Hodge classes*,
[arXiv:math/0103111v1, 17 March 2001](https://arxiv.org/abs/math/0103111v1):
[Proposition 2.4, p. 5](https://arxiv.org/pdf/math/0103111v1#page=5),
[sections 4.3--4.10, pp. 10--12](https://arxiv.org/pdf/math/0103111v1#page=10),
[Proposition 5.3, p. 13](https://arxiv.org/pdf/math/0103111v1#page=13),
and [Corollary 6.5, Lemma 6.8 and Theorem 6.9, pp. 15--17](https://arxiv.org/pdf/math/0103111v1#page=15).

The etale quaternionic Prym has dimension 4(g-1). Its algebraic
quaternionic classes lie in H^(4(g-1)) and are endomorphism
translates of Weil determinant classes. The nontrivial GL(2)
representation described there is an endomorphism-group action,
not the requested derived Lefschetz-group action. Proposition
5.3 places these classes in the divisor algebra on the specified
Weil-square specialization. The special so(7) eightfold has five
exceptional degree-four directions, but Theorem 6.9 assumes
algebraicity of its degree-four Hodge classes before transferring
them to the Weil fourfold. It does not construct those cycles.

Thus the proved construction and the conditional spin example
must remain separate. No transfer to the saved A is identified.
These statements do not by themselves extend L034 to every
quaternionic source or every algebraic correspondence.

### Ramified quaternionic constructions and Weyl-group covers

Read Donagi--Livne, *Abelian Varieties with Quaternion
Multiplication*, [arXiv:math/0507493v3, 2 December 2005,
Lemma 1, Lemma 3, table (2) and Proposition 4, pp. 3--4](https://arxiv.org/pdf/math/0507493v3#page=3),
and [Corollary 13, p. 15](https://arxiv.org/pdf/math/0507493v3#page=15).
Their dominant quaternionic-cover cases have Prym dimensions
four, six or eight. The indicated four-dimensional moduli
problem is described by Y_0(2)/w_2. These are concrete
parametrizations, with no stated image theorem for beta_U.

Read Alexeev--Donagi--Farkas--Izadi--Ortega,
*The uniformization of the moduli space of principally polarized
abelian 6-folds*, [arXiv:1507.05710v3, 15 March 2018,
Theorem 0.1 and Corollary 0.2, p. 2](https://arxiv.org/pdf/1507.05710v3#page=2).
The W(E_6) construction dominates the moduli of principally
polarized sixfolds. Its displayed cycle consequence is the
curve class 6 theta^5/5!, of degree ten. Neither statement
supplies the degree-four transfer sought here.

For applicability, reuse L032: every nonzero abelian subquotient
of any power of the saved A has dimension at least 32. The
four-, six- and eight-dimensional objects above do not satisfy
that factor threshold. Increasing a power's total dimension is
not a certificate of a new simple factor. This comparison retains
the distinction between homomorphisms and arbitrary higher-degree
correspondences; the latter are not excluded by L032.

### Broader nonabelian-cover theorems describe generic groups

Read Arapura, *Toward the structure of fibered fundamental groups
of projective varieties*, J. Ec. polytech. Math. 4 (2017),
[section 4, Theorem 4.1 and Lemma 4.3, pp. 605--607,
PDF pp. 12--14](https://jep.centre-mersenne.org/item/10.5802/jep.52.pdf#page=12).
The theorem computes the special Mumford--Tate group of each
rational isotypic component for a very general base curve of
genus g>3 and a redundant quotient. Redundancy requires factoring
through a free group with a free generator in the kernel. These
hypotheses cannot be imposed on an unspecified special source.

Read Landesman--Litt--Sawin, *Big monodromy for higher Prym
representations*, [arXiv:2401.13906v2, 12 October 2025,
Theorems 1.3 and 1.9 and Corollaries 1.10--1.11, pp. 3--5](https://arxiv.org/pdf/2401.13906v2#page=3).
For a finite cover group with maximum irreducible complex
representation dimension r, Theorem 1.3 identifies connected
monodromy with the commutator of the symplectic centralizer when
n=0 and g>=2r+2, or for arbitrary n when g>max(2r+1,r^2).
Theorem 1.9 specifies the orthogonal, symplectic or special-linear
groups on individual coefficient spaces. Corollary 1.10 gives
Mumford--Tate containments for a very general cover under those
bounds. These results supply group comparisons, not algebraic
cycles or a transfer from a special source. No new image
exclusion is deduced from them here.

Rechecked Patel--Zhang,
[arXiv:2506.13729v2, 23 May 2026, Theorems 1.1--1.2,
pp. 2--3](https://arxiv.org/pdf/2506.13729v2#page=2).
The hypotheses still specify a finite abelian etale cover and
the constructed Prym subspace is the top exterior space over
the nontrivial group-algebra factors. The prior assessment and
L034 already address that supply. No nonabelian extension is
imported from the title's word “generalized”.

### A recent quaternionic Kuga--Satake comparison

Read Poon, *Kuga--Satake Construction on Families of K3 Surfaces
of Picard Rank 14*, Mathematische Nachrichten 299 (2026),
1894--1916, [section 3.1, Theorems 3.1.1 and 3.1.4 and
Remark 3.1.5](https://onlinelibrary.wiley.com/doi/10.1002/mana.70173).
The modular construction assumes a rank-fourteen polarization
and a square determinant; the generic Kuga--Satake variety
decomposes using two simple eightfolds. The nonsquare case in
the remark uses a sixteenfold. This addresses different lattice
data from the present Picard-four, transcendental-rank-eighteen
problem. The displayed modular mapping is not an algebraicity
theorem for our kappa or beta_U.

### Comparison, redundancy and continuation

The comparison has three outcomes:

1. The proved cycle supply has not produced an identified input
   outside the determinant channel. The full polarization
   centralizer, rather than the covering group or the group of
   endomorphisms, is the relevant group in the saved target.
2. The inspected exceptional degree-four statement leaves
   algebraicity as a hypothesis. Using it here would assume
   an essential missing input.
3. The additional moduli and monodromy theorems supply structural
   information, with no actual source/transfer pair meeting the
   notebook's representation and image requirements.

These are applicability findings, not a classification of all
nonabelian Prym Hodge classes. A universal exclusion would need
a new argument; this literature-only turn does not supply one.
L033 and L034 remain scoped to their stated sources and
operators. No small-factor, determinant, embedded-support or
stable-resolution branch is reopened.

With no actionable source selected, the proposed different
mechanism is an auxiliary CM extension and a half twist. Its
first test concerns the existence of the required effective,
polarized weight-one Hodge structure. If it exists, algebraic
comparison maps back to S would still be necessary. The
[separate assessment](2026-09-27-cubic-rm-auxiliary-cm-half-twist.md)
is REVIEW_REQUIRED. Nothing about that test is derived here;
PROGRESS.md alone records the exact next action.

### Search and access record

Queries on 2026-09-27 included:

- `"nonabelian" "Prym" "Hodge classes"`
- `"non-abelian" "Prym" "algebraic cycles"`
- `Prym nonabelian covers exceptional Hodge classes algebraic quaternionic theorem`
- `"generalized Prym" "Hodge classes" nonabelian`
- `"Prym" "Kuga-Satake" "real multiplication"`
- `"Prym" "Mumford-Tate" "Arapura"`
- `"Prym-Tyurin" "exceptional" "cycles"`
- `"Big monodromy for higher Prym representations"`
- `"Quaternionic Pryms and Hodge classes" correction erratum`
- `"Abelian varieties with quaternion multiplication" arxiv`
- `"uniformization" "A6" "Prym" Alexeev Donagi Farkas Izadi Ortega`

The exact-transfer queries gave no inspected full match.
Versioned arXiv passages resolved access to the relevant cover
and monodromy statements; Poon's published HTML supplied the
numbered statements. The MSP PDF endpoint and the author-hosted
uniformization PDF did not render, so their accessible arXiv
versions were used. Donagi--Livne's 2025 publisher entry was
identified, but the theorem comparison uses only the explicit
2005 v3 text, without assuming the versions coincide.

Abdulali's original 1999 type-III paper could not be read through
the linked publisher endpoint. It is an auxiliary reference:
the van Geemen--Verra statements and their displayed arguments
used above were directly accessible. Read the author's
[errata](https://myweb.ecu.edu/abdulalis/Errata.html) and
[2016 survey, Appendix B, p. 12](https://myweb.ecu.edu/abdulalis/Vancouver.pdf#page=12);
do not use broader uncorrected type-III or CM domination claims.
No conclusion here depends on the inaccessible 1999 paper.
The later W(E_6) Hodge-bundle paper, the original GLLM arithmetic
theorem, and the half-twist lead are not theorem-level inputs
to this assessment.

The earlier Schoen correction and Milne operator/erratum
comparisons are reused through the linked completed assessments.
No essential unread source prevents the stated scope comparison.
Failure to find a match does not establish novelty or impossibility.

## Mathlib

Coverage of the full transfer statement: **not checked**.
The numbered results and direct links above are supporting or
conditional inputs, not a full match. No Mathlib theorem name,
absence claim or new mathematical result is asserted.
