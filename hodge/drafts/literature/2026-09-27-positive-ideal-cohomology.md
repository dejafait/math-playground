# Positive ideal cohomology — literature assessment

TARGET: Determine whether H^1(X,I_C(rH)) is nonzero for some r>0 for the fixed product polarization H, as the possible obstruction to summand recovery in smooth complete-intersection unions with 0<m<n.
CHECKED: 2026-09-27
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched the exact RM/Dickson correspondence restriction problem, K3 multiplication and normal generation, regularity, and singular ideal-sheaf vanishing; representative queries and inspected statements are recorded below.
SOURCE_EVIDENCE: Stacks Lemma 30.17.1, https://stacks.math.columbia.edu/tag/0B5U; Gallego--Purnaprajna, arXiv:alg-geom/9608008v1, Proposition 2.2 and Corollary 2.3, https://arxiv.org/pdf/alg-geom/9608008v1#page=4; de Fernex--Ein, corrected arXiv:0805.3863v4, Theorem 1.1 and Example 5.7, https://arxiv.org/pdf/0805.3863v4#page=1; further versions, pages and direct links below.
COMPARISON: The inspected results give eventual or conditional vanishing and multiplication on a K3; none determines this correspondence's restriction cokernels for the original ample L in every positive degree. Singular ideal-sheaf theorems are not excluded merely by C being non-lci, but require additional global positivity and generation data.
GAP: Determine the actual ambient restriction image for the fixed L, retaining all three normalization gluing conditions; either exhibit a positive-degree cokernel or justify vanishing in every positive degree, including any range below an effective tail bound.
REASON: Import the known vanishing and multiplication tools and specialize only the unresolved restriction data. This can test the proposed summand-recovery loophole for 0<m<n; no cohomology value, effective cutoff, or transverse lift is derived in this literature turn.

## Hypotheses

Keep the very general S, X=S x S, reduced C and fixed ample L, with
H=L external tensor L. Do not strengthen L to a very ample line bundle
or replace it by a power. The positive-degree support-vanishing result
is [L019](../../lemmas/L019-positive-degree-cubic-support-vanishing.md).
The group governing recovery of the summand inclusion is already
identified in [L018](../../lemmas/L018-high-degree-complete-intersection-unions-retain-obstruction.md).
The m>n>0 unions remain excluded; no exception to that result is proposed.

L was fixed but its numerical class was not specified. A later answer
must retain that class as a parameter or give a uniform argument under
the stated ample hypothesis; selecting a convenient different L would
change the target. Reuse the rational target and primary-source reading
of 2026-09-27 in the [preceding assessment](2026-09-27-positive-degree-normalization-cohomology.md).
No change of the universal conjecture or of the family is proposed.

## Conclusion

The source comparison is complete with decision SPECIALIZE. Known
supporting results should be imported by citation. No full match for
the saved existential question was found in the statements checked;
this is not evidence of novelty. The completed step is LITERATURE /
NOVELTY_UNCHECKED / EXPLORATION, using one exploration turn since
L019's informative negative result. The exact research target is retained.

The proposed downstream use remains summand recovery when 0<m<n.
A nonzero group would identify a possible failure of that sufficient
recovery argument, not a nonzero obstruction to a particular inclusion
and not a transverse union lift. All-positive-degree vanishing would
remove this cohomological escape, subject to checking the rest of the
recovery argument in the reversed ordering. Actual cancellation,
higher-order lifting, algebraization and the universal Hodge gap would
still require separate arguments. The attained cycle span remains 21
on the same family; the stopped representatives permit three RM
directions against four required. No complete candidate exists.

## Proof

This section records source statements and applicability comparisons,
not a proof of a new cohomology or deformation result.

### Restriction, eventual vanishing and regularity

Reread [Stacks Lemma 30.17.1, tag 0B5U](https://stacks.math.columbia.edu/tag/0B5U)
on 2026-09-27. On a proper scheme over a Noetherian ring, an ample
line bundle gives higher-cohomology vanishing for every coherent sheaf
in all sufficiently large twists. It applies directly to I_C on X.
It specifies neither the first vanishing degree nor the existence of
an exceptional positive degree. Reproving eventual vanishing would
repeat the input already used in L018.

Read de Fernex--Ein--Mustata, *Vanishing theorems and singularities in
birational geometry*, author-hosted preliminary draft dated 8 December
2014, [Definition 2.4.1, Remark 2.4.2 and Theorem 2.4.3 (Mumford),
pp. 122--123, PDF pp. 132--133](https://homepages.math.uic.edu/~ein/DFEM.pdf#page=132).
For an ample globally generated bundle A, m-regularity means
H^i(F tensor A^(m-i))=0 for i>0. The theorem propagates regularity,
gives surjectivity of multiplication in the corresponding degrees,
and gives global generation. An actual regularity bound for I_C and
global generation of the chosen A remain hypotheses, not consequences
of ampleness alone. An auxiliary power could organize a tail argument
only if every degree of the original H is retained.

Also read [Stacks Definition 33.35.7 and Lemmas 33.35.10--33.35.12,
tag 08A2](https://stacks.math.columbia.edu/tag/08A2). These give the
projective-space definition, propagation, multiplication and generation
statements. They do not supply a numerical regularity bound for this
ideal or identify X with projective space.

The map requiring a later calculation is restriction from H^0(X,H^r)
to H^0(C,H^r|_C). L018, equation (7), already records the positive
ambient cohomology vanishing used with the ideal sequence. L019 concerns
cohomology and evaluation of sections on the support and its
normalization; it does not calculate this ambient restriction image.

### K3 multiplication and the two distinct pullback systems

Read Gallego--Purnaprajna, *Vanishing Theorems and Syzygies for K3
Surfaces and Fano Varieties*, [arXiv:alg-geom/9608008v1, 7 August 1996,
section 2, equation (2.1.1), Proposition 2.2 and Corollary 2.3,
pp. 2--4](https://arxiv.org/pdf/alg-geom/9608008v1#page=3).
If A on a smooth K3 is globally generated and its general curve is
smooth nonhyperelliptic of genus at least three, Proposition 2.2 gives
H^1(M_(A^p) tensor A^r)=0 for p,r>=1, where M is the evaluation
kernel. Corollary 2.3 recovers normal generation (Saint-Donat--Mayer).
These hypotheses and the complete section spaces must be retained.

This is multiplication on one K3. It is not multiplication of the two
specified pullback subspaces on W followed by descent to C. Neither
normal generation on S nor replacing those subspaces by all sections
on W computes the required restriction rank. The two pullbacks of L
must not be identified without an argument.

Cross-checked Huybrechts, *Lectures on K3 surfaces*, author-hosted
449-page copy accessed 2026-09-27, [Chapter 2, Corollary 2.5 and
Theorem 2.7, pp. 26--27](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=26).
The former states normal generation under the smooth nonhyperelliptic
curve hypothesis. The latter gives global generation of L^k for k>=2
and very ampleness for k>=3 when L is ample in characteristic different
from two. These are comparison statements about S, not surjectivity
onto C in the original degrees. The cited primary Gallego--Purnaprajna
proof supplies the multiplication input; no unproved use of the
inaccessible Saint-Donat original is required.

### Vanishing for singular ideal sheaves

Read de Fernex--Ein, *A vanishing theorem for log canonical pairs*,
[arXiv:0805.3863v4, 13 April 2015, Theorem 1.1, p. 1](https://arxiv.org/pdf/0805.3863v4#page=1).
For a projective lci ambient variety T with rational singularities,
a pure codimension-e subscheme V without embedded components, defined
by divisors of degrees d_1>=...>=d_t in a globally generated bundle B,
and log canonical (T,eV), it gives
H^i(T,omega_T tensor B^k tensor A tensor I_V)=0 for i>0 and
k>=d_1+...+d_e. The corrected hypothesis is that A is ample.

[Example 5.7, p. 14](https://arxiv.org/pdf/0805.3863v4#page=14)
checks log canonicity at isolated transverse double points of projected
smooth varieties, including non-lci images. Thus C's recorded local
model alone does not exclude this framework. A global generation and
degree bound for the actual I_C, and matching the desired twist, still
need verification. No such bound or application at r=1 is made here;
the projective-space regularity corollaries cannot be substituted
unchanged for the theorem on the actual ambient X.

Read Chou, *A vanishing theorem for log canonical pairs after De
Fernex--Ein*, [arXiv:1311.5545v2, 16 January 2014, Theorems 1.1--1.2,
p. 1](https://arxiv.org/pdf/1311.5545v2#page=1).
For (T,Delta;eZ) log canonical, Z reduced and pure, with no component
in Sing(T) or Supp(Delta), the theorem requires nef A and M,
A(-K_T-Delta) ample, and M tensor I_Z^(tensor e) globally generated.
It yields H^i(T,A tensor M tensor I_Z)=0 for i>0. Theorem 1.2 permits
finitely many non-log-canonical points. These broader singularity
hypotheses retain a generation requirement; they do not determine the
small positive twists here. Neither source requires inventing a
vanishing theorem for arbitrary ample twists of an arbitrary ideal.

### Search scope, reused comparisons and access

Representative queries on 2026-09-27 were:

- `"K3" "real multiplication" correspondence "ideal" cohomology`
- `"Dickson" "K3" "projective normality"`
- `"K3" "correspondence" "restriction map" sections`
- `"K3" "correspondence" "normal generation"`
- `"K3" "correspondence" "ideal sheaf" "vanishing"`
- `K3 surfaces projective normality Saint Donat multiplication maps ample line bundles theorem pdf`
- `"Vanishing theorems and syzygies for K3 surfaces and Fano varieties"`
- `Castelnuovo Mumford regularity ideal sheaf restriction sections ample globally generated theorem`
- `de Fernex Ein vanishing theorem log canonical pairs ideal sheaf complete intersection regularity`

Exact-geometry searches did not locate a theorem deciding the saved
question. The [published family paper, sections 4.8--4.9 and 5.3--5.4](https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/on-families-of-k3-surfaces-with-real-multiplication/26D90B781A518CB95969B4473C8852C8)
supplies the correspondence and family scope already assessed in the
[family audit](../../foundations/05-cubic-rm-family.md). Section 4.9
distinguishes these cycles from those needed on maximal RM families.
It does not supply the requested positive ideal cohomology. Reuse the
unchanged linkage and deformation comparisons in the
[complete-intersection assessment](2026-09-27-ample-complete-intersection-union.md).

Saint-Donat's original *Projective Models of K-3 Surfaces*, Amer. J.
Math. 96 (1974), 602--639, [JSTOR record](https://www.jstor.org/stable/2373709),
was an unread lead: neither the record nor PDF attempt exposed the
article. Gallego--Purnaprajna's inspected proof resolves the relevant
normal-generation source need. Its arXiv history lists only v1; an
attempted v2 URL failed, and no v2 theorem is cited. The two original
ideal-vanishing preprints and the regularity statements were readable.
No essential source remains inaccessible. Search snippets, catalogues,
and other papers appearing in references are not counted as inspected
theorems. This is a bounded assessment, not an exhaustive novelty search.

### Remaining specialization and continuation test

The prior m>n>0 exclusion, and the stopped diagonal, fibre, rotation
and sheaf representatives, are preserved. Reversing the degree order
changes L018's summand-recovery group to a positive twist; this is a
different uncomputed group from L019's support vanishing. No previously
failed representative is reopened by relabeling it.

A later research step should test the actual restriction image using
the two specified projections and all three descent conditions, with
the original L retained. A certified nonzero cokernel in one positive
degree answers the existential question for that L. A negative answer
requires vanishing for every r>0, for example a proved finite range
and a justified tail bound. Eventual vanishing, a failed sufficient
positivity test, or section-dimension heuristics decide neither outcome.

Continue toward a union test only if a genuine nonzero recovery group
is found, and give obstruction cancellation its own assessment before
calculating it. If every positive group vanishes, abandon this proposed
cohomological escape. If the calculation remains incomplete, record
the exact remaining range or map without claiming an advance; complete
the continuation decision within the shared three-exploration-turn
budget. This review uses the first turn of that budget.

The pending registration is replaced only by this completed source
assessment. No restriction rank, cohomology value, lattice inequality,
effective threshold, or new lifting statement was derived. Mathematical
lemmas, scripts and the existing unfinished drafts remain unchanged.

## Mathlib

Coverage: **not checked** for the full target or its supporting
restriction, regularity, multiplication and ideal-vanishing statements.
The named results and direct links above are supporting mathematical
references; none is a claimed Mathlib match or a match for the full
existential positive-ideal-cohomology question. No library absence or
originality is inferred from this review.
