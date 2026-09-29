# Resolved-lift blowdown and period comparison — source audit

TARGET: Review whether the all-source blowdown and first-order period identification in L043 are supported by the cited map-deformation framework and standard Hodge functoriality.
CHECKED: 2026-10-03
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched point-blowup deformations, prescribed source/target map tangents, functorial infinitesimal periods and Hilbert-scheme incidence; followed Iacono's contraction reference and read the statements below. The exact incidence-specific identification was not matched.
SOURCE_EVIDENCE: Iacono 0705.4532v2, Theorem 5.5, Remark 5.6 and Remark 5.12(7), pp. 9--10,14--15; Grivaux, journal-version author PDF, Section 5.1(5.3), PDF pp. 42--43; Iacono 0707.2454v2, Lemma 4.7, p. 9, and math/0701091v1, Lemma II.6.1 and proof, pp. 53--54; Fiorenza--Manetti, J. Noncommut. Geom. 3 (2009), Proposition 4.5 and Theorem 5.1, pp. 593,595--596; math/0605297v1, Theorems 10.6 and 12.3, Corollary 12.5, pp. 23--24,28; Stacks Tags 0FUU, 07HX and 0FM7. Direct links and exact scope follow.
COMPARISON: The simultaneous-map criterion and central point-blowup pullback used in L043 have named source coverage, and formal period differentiation is available over Artinian bases. Iacono's contraction lemma assumes strict representative compatibility, whereas general map tangents include a homotopy; naturality in the Artin algebra alone does not supply the relative-incidence comparison.
GAP: Critically check L043's passage from a general map cocycle to its cohomological contraction identity and the marked action of the relative incidence map. This is an application question, not a demonstrated error or an imported proof of xi=kappa.
REASON: Resolve the formerly unread framework scope by citation, retain the geometry-specific comparison for a separate critical research step, and keep the resolved-lift recipe provisionally stopped. No new result, calculation, source-blocked essential input or full verification of L043 is claimed.

## Hypotheses

Retain [L043](../../lemmas/L043-resolved-parameter-lift-retains-transverse-obstruction.md)
and its marked first-order setting: B is an iterated point blowup
of the projective K3 surface S, the source B_A is arbitrary, and
the target is S_A^[3] induced by a prescribed NS-fixed RM
deformation. No exceptional configuration or blowdown diagram
is assumed to persist. Reuse the sufficient
[earlier map/relative-Hilbert assessment](2026-10-03-resolved-parameter-hilbert-cube-deformation.md);
this audit screens its two later applications, not a new
representative.

The main local gap is an algebraic representative extending the
cubic action into the fourth RM direction. The intermediate
target is reliable support for L043's all-source exclusion.
Its downstream use is deciding whether this parameter change
really fails before selecting another representative.
An applicable framework plus a valid incidence/contraction
application supports retaining the stop. A missing hypothesis
or a surviving map-motion correction requires qualifying that
part of the exclusion and repairing it. Neither outcome alone
resolves the universal Hodge conjecture.

The numerical comparison remains three attained RM directions
against four required, and span 21 only on the Dickson family.
The rational formulation is unchanged; reread Deligne's
[Clay statement, Section 1, PDF p. 2](https://www.claymath.org/wp-content/uploads/2022/06/hodge.pdf#page=2).

## Conclusion

SPECIALIZE is ready for a bounded critical application of
known inputs. The blowdown framework is supported more
precisely than by the previous placeholder. The period setting
includes dual numbers; it need not be replaced by a result
only about reduced families. No inspected theorem states this
map's entire incidence-period identification or its
fourth-direction exclusion.

This is an EXPLORATION literature step. Supporting results
are imported by citation, not reproduced or presented as
discoveries. The full geometry-specific claim was not matched;
that is not evidence of originality. No new mathematics is
derived and no lemma or mathematical script is changed.

## Proof

This section compares inspected sources; it is not a proof
of L043's conclusions.

### Prescribed source classes and point blowups

Reread Iacono, *L-infinity Algebras and Deformations of
Holomorphic Maps*, arXiv:0705.4532v2 (3 April 2008),
[Theorem 5.5 and Remark 5.6, PDF pp. 9--10](https://arxiv.org/pdf/0705.4532v2#page=9)
and [Remark 5.12, equation (7), pp. 14--15](https://arxiv.org/pdf/0705.4532v2#page=14).
The tangent description allows both manifolds and the map
to vary. Its forgetful image is the kernel of the
df minus pullback map into H^1(f^*T_Y). This matches the
criterion quoted as L043(3). Compactness holds for all
central manifolds involved; immersion or finiteness of the
map is not required. The identification is up to marked
isomorphism, as needed for a prescribed source class.

Read Grivaux, *Infinitesimal deformations of rational surface
automorphisms*, author-hosted journal-version PDF,
DOI 10.1007/s00209-017-1932-x,
[Section 5.1, equation (5.3) and its following discussion,
PDF pp. 42--43](https://jgrivaux.perso.math.cnrs.fr/articles/kummer.pdf#page=43).
The point-blowup paragraphs explicitly give the tangent
sheaf differential sequence with quotient i_*T_E(-1) and
the pullback isomorphism H^i(X,F) -> H^i(Y,pi^*F) for locally
free F. These match the supporting inputs in L043(4)--(5).
The statements concern complex surfaces; the subsequent
rational-surface applications are not hypotheses for these
blowup facts. There is no need to reprove their general
chart calculation.

Also read [Stacks Lemma 50.17.1, Tag 0FUU](https://stacks.math.columbia.edu/tag/0FUU)
and [Lemma 50.17.2 in Section 50.17](https://stacks.math.columbia.edu/tag/0FUC).
They keep a smooth ambient scheme and smooth centre and
provide central differential-form/de Rham blowup inputs.
They are not themselves all-source deformation theorems.
Iteration through L043's chosen point blowups is an
application of the inspected inputs, not a new named theorem
imported from either source.

### Formal periods and the map-motion qualification

Read Fiorenza--Manetti, *A period map for generalized
deformations*, **published version**, J. Noncommut. Geom. 3
(2009), 579--597,
[Proposition 4.5, p. 593](https://ems.press/content/serial-article-files/30459?nt=1#page=15)
and [Section 5, Theorem 5.1 and proof, pp. 594--596](https://ems.press/content/serial-article-files/30459?nt=1#page=16).
For a compact Kahler central manifold the period functor
is defined over local Artinian complex algebras, with
differential given by contraction. This supports the
first-order scope used in L043. Its natural-transformation
claim is in the Artin base; it is not an explicit theorem
about this relative correspondence.

For the cohomology/filtration scope, read Fiorenza--Manetti,
*L-infinity algebras, Cartan homotopies and period maps*,
**arXiv:math/0605297v1 (11 May 2006)**,
[Theorem 10.6, pp. 23--24](https://arxiv.org/pdf/math/0605297v1#page=23),
[Theorem 12.3, Remark 12.4 and Corollary 12.5,
p. 28](https://arxiv.org/pdf/math/0605297v1#page=28).
These identify the formal filtered-cohomology construction
and its period derivative. Kahler central fibres meet the
cohomological hypothesis. L043's own K3 contraction argument
remains its specific local-Torelli application.

Followed Iacono's reference and read
[arXiv:math/0701091v1 (3 January 2007), Section II.6,
Lemma II.6.1 and proof, pp. 52--54](https://arxiv.org/pdf/math/0701091v1#page=53),
as well as [0707.2454v2 (22 June 2010), Lemma 4.7,
p. 9](https://arxiv.org/pdf/0707.2454v2#page=9).
The contraction identity there assumes equality of the
pulled-back and differentiated vector-valued forms.
By contrast, 0705.4532v2 Remark 5.6 retains a third cocycle
component z satisfying the Dolbeault equation
\(\bar\partial z = df(\eta)-f^*(\xi)\).
The general map-motion term must therefore be accounted
for when using the identity in cohomology. L043 says
such changes are coboundaries; this audit identifies the
precise comparison to check, without calculating that term
or asserting that the existing argument is wrong.

Read [Stacks Section 50.2, Tag 07HX](https://stacks.math.columbia.edu/tag/07HX)
and [Definition 50.7.1, Tag 0FM7](https://stacks.math.columbia.edu/tag/0FM7).
They give the relative de Rham pullback and degree
filtration over arbitrary scheme bases. They support the
algebraic filtered-pullback setting, not the entire analytic
incidence/marking claim. The relative Hilbert-cube and
universal-family inputs are already screened in the earlier
assessment; the remaining critical test concerns their
marked cohomological use.

### Search scope, access and redundancy

Queries used included:

- deformations blowing up point surface deformation functor blowdown every deformation
- Iacono 0705.4532 Remark 5.12 deformation holomorphic maps
- Gauss Manin functorial morphism infinitesimal period Kodaira Spencer contraction Hodge filtration
- Manetti Iacono period map infinitesimal deformations compact Kahler functorial Hodge filtration artinian
- infinitesimal holomorphic maps period Hodge functoriality
- Gauss-Manin functorial pullback holomorphic maps Hodge
- Beauville varietes Kahleriennes premiere classe Chern nulle hilbert schema symplectique 1983 proposition 6 incidence

The blowup forum hit was a discovery lead only, not theorem
evidence. Burns--Wahl and original Horikawa/Namba leads remain
unread and unused. Huybrechts' author-hosted K3 PDF and the
Peters period book returned internal errors. Beauville's and
Ran's scans had insufficient extracted text for the sought
statements; screenshot requests did not expose readable
images here. Those missing passages are not counted as
inspected. The readable formal-period and contraction sources
replace these access leads for the bounded check; no essential
claim is attributed to an unread source.

Read the full overview, DAG, L043, its saved assessment,
history 077 and the stopped attempt. L009 and L042 address
different source/support hypotheses; repeating them cannot
certify this all-source application. Reproving Iacono's
complex or the standard point-blowup identities would also
be redundant. No formula for a new support or additional
deformation direction is investigated.

## Mathlib

Coverage: **not checked** for this audit, simultaneous map
deformations, point-blowup deformation maps, formal periods
or relative incidence compatibility. The named primary
statements above cover supporting pieces; none is a Mathlib
match or a citation for L043's complete exclusion. No library
absence or certified novelty is asserted.
