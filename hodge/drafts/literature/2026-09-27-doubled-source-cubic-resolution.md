# Doubled source in a cubic mixed resolution — literature assessment

TARGET: Assess whether a three-presentation resolution of I_C direct sum I_C using product line bundles with factor classes in L025's W can admit an integral terminal twist stable at Omega with SU(2)-invariant c_1 and c_2.
CHECKED: 2026-09-27
DECISION: EXPLORE
SEARCH_EVIDENCE: Searched direct sums of ideal sheaves, stable resolutions, higher-rank evaluation kernels, prescribed Chern data and hyperholomorphic integrality; followed Mistretta's broader generation results and thesis questions, and a recent surface-stability reference. Exact queries, readings and scope limits appear below.
SOURCE_EVIDENCE: Mistretta, arXiv:math/0310185v2, Theorem 3.1, Lemma 3.4 and Corollaries 3.5/3.10, https://arxiv.org/pdf/math/0310185v2#page=7; his 2006 thesis, Questions 3.1.1--3.1.3, https://www.imj-prg.fr/theses/pdf/ernesto_mistretta.pdf#page=49; Rekuski, arXiv:2303.13459v2, Corollary 4.4 and discussion after Remark 4.5, https://arxiv.org/pdf/2303.13459v2#page=12; other precise citations below.
COMPARISON: Mistretta's stable-terminal theorem has an ideal-sheaf source; its general coherent-sheaf consequences give filtrations and group/category generation. Conditional generation tools allow higher rank, but no inspected theorem supplies the doubled source, restricted mixed terms, integral twist, stability at Omega and invariant full Chern classes together. No full exclusion was matched either.
GAP: Determine whether the exact doubled-source sequence can satisfy integral Chern compatibility and have actual presentation maps with a viable stability argument at Omega; neither a rational tensor nor group generation by stable bundles establishes this.
REASON: Multiplicity is a specific change beyond L028's fixed-coefficient exclusion and is relevant to the rational goal. Permit one bounded feasibility test in a separate research turn, using the cited tools and retaining every geometric requirement; this assessment makes no existence or originality claim.

## Hypotheses

Retain the same S, C, final W=im(A), and metric of L025. Replace
only the source sheaf in the exact three-presentation target by
I_C direct sum I_C. The required terminal object is an actual
locally free positive-rank bundle with an actual integral line
twist, stable for Omega and with invariant full c_1 and c_2.
Direct-summing an earlier terminal bundle is not itself a stability
certificate. No existence or removal of L028's obstruction is
asserted for the changed target.

The required sequence is

\[
0\longrightarrow E\longrightarrow P_2\longrightarrow P_1
 \longrightarrow P_0\longrightarrow I_C\oplus I_C\longrightarrow0.
\]

Each P_i is a finite sum of actual product line bundles whose factor
classes lie in the final W=im(A). The final F=E tensor M must have
positive rank, with M an actual integral line bundle. Stability is
slope stability for Omega=p_1^*omega+p_2^*omega. The two factors use
L025's same metric and its diagonal SU(2) action. The rational chamber
conjugation is not assumed to preserve the integral divisor lattice.

Reuse the adequate unchanged background in the
[single-source assessment](2026-09-27-cubic-subspace-mixed-resolution.md),
[multiple-divisor assessment](2026-09-27-multiple-divisor-stable-resolutions.md)
and [bundle assessment](2026-09-27-compatible-cubic-rm-stable-bundle.md).
Their single-source conclusions are not extended to this sequence.

## Conclusion

The exact saved target has a completed EXPLORE assessment. The source
change loses automatic access to the reviewed ideal-sheaf and rank-one
stable-kernel constructions. General generation results do not restore
the simultaneous hypotheses. This is an applicability comparison;
it does not prove the doubled recipe impossible.

No doubled-source Chern formula, parity calculation, map construction
or stability assertion was derived. Known supporting results should be
used by citation. The remaining feasibility question was not matched
in the bounded search, which establishes no originality. This step is
LITERATURE / NOVELTY_UNCHECKED / EXPLORATION, consuming exploration
turn 1 of 3 after L028's informative negative result.

A viable representative would still leave transverse transport
outside V_D to prove. The attained 21-dimensional span, three
directions against four required, and universal primitive-class
gap are unchanged. No complete candidate for the conjecture appears.

## Proof

This section records source statements and their scope, without a
new mathematical proof or specialization. The original pending scope
and the interim reading checkpoint are incorporated in this assessment.

### Stable resolutions versus generation by stable objects

Reread Mistretta, *Stable vector bundles as generators of the Chow ring*,
[arXiv:math/0310185v2, 15 March 2007, Theorems 3.1--3.2 and
proof, pp. 7--9](https://arxiv.org/pdf/math/0310185v2#page=7).
The terminal stable resolution starts from an ideal sheaf and uses
powers of one ample H. The curve-restriction iteration invokes
Butler's theorem on a stable curve bundle of slope greater than twice
the genus. It does not state a stable-terminal construction for the
present rank-two source or mixed presentation terms.

Read also [Lemma 3.4 and Corollaries 3.3, 3.5 and 3.10,
pp. 10--11](https://arxiv.org/pdf/math/0310185v2#page=10).
The extension to arbitrary coherent sheaves uses filtrations with
quotients admitting polystable resolutions. The resulting Chow,
K-group and derived-category generation statements do not prescribe
one stable terminal bundle with the target's maps or Chern data.
These statements are supporting results, not a match for the doubled
sequence. No direct-sum stability or resolution construction is
inferred from them.

Followed the search lead to Mistretta's thesis, *Some constructions
around stability of vector bundles on projective varieties*, defended
6 December 2006. Read [Questions 3.1.1--3.1.3 and the surrounding
discussion, printed pp. 41--42, PDF pp. 49--50](https://www.imj-prg.fr/theses/pdf/ernesto_mistretta.pdf#page=49).
The author explicitly separates generation of the derived category
from existence of resolutions by polystable bundles, and asks about
stability for proper generating subspaces and higher-dimensional
evaluation kernels. This resolves the apparent broader-resolution
lead; those passages ask questions rather than supply the missing
theorem. They are historical scope evidence, not a claim that these
questions remain unanswered today. The quoted Butler theorem there
is not used as an independent new input.

### Higher-rank kernel results and their limits

Reread Rekuski, *Stability of Kernel Sheaves Associated to Rank One
Torsion-Free Sheaves*, [arXiv:2303.13459v2, 12 May 2023,
Theorem 4.3 and Corollary 4.4, p. 11; Remark 4.5 and following
discussion, pp. 12--13](https://arxiv.org/pdf/2303.13459v2#page=11).
For a fixed very ample H, sufficiently positive rank-one sources
have H-stable full evaluation kernels. The author notes that the
numerical argument is formally broader, but its asymptotic bound
fails for rank at least two in dimension at least two. Thus one may
not apply the rank-one asymptotic corollary to I_C direct sum I_C,
or assert that positivity alone certifies a stable higher kernel.
This is a limitation of that argument, not a nonexistence theorem.
No bound was evaluated for the present target.

Followed Misra, *On instability of Syzygy Bundles*,
[arXiv:2602.06629v1, 6 February 2026, Theorem 1.2 and
preceding references, p. 2](https://arxiv.org/pdf/2602.06629v1#page=2).
Its instability statement concerns surfaces with specified effective
cone generators and some changed ample polarization. It gives no
test of the prescribed Omega on the fourfold X. Its reference to
stronger surface stability was followed to the original statement.

Reread Misra--Ray, *On Stability of Syzygy Bundles*,
[arXiv:2405.17006v1, 27 May 2024, Theorems 1.2--1.3,
p. 2, and Question 3.4, p. 9](https://arxiv.org/pdf/2405.17006v1#page=2).
Theorem 1.3 is printed with an H-semistable globally generated
vector-bundle source on a surface and an H-stable asymptotic kernel
conclusion. The higher-dimensional statement appears as a question.
The surface and local-freeness hypotheses already prevent using it
for the present source. Its unrestricted semistable-to-stable claim,
including decomposable sources, is not independently validated or
imported here. No new counterexample or audit of its proof is made.
The arXiv record lists only v1; the published 2026 text was not
inspected and is not an input. This resolves the interim reading lead
without making the present test depend on that claim.

### Actual generation tools and Chern constraints

Reread Hering--Schenck--Smith, *Syzygies, multigraded regularity and
toric varieties*, [arXiv:math/0502240v2, 9 August 2006,
Theorem 2.1 and Lemma 2.2, pp. 3--4](https://arxiv.org/pdf/math/0502240v2#page=3).
For an arbitrary coherent sheaf, the stated multigraded cohomology
vanishings propagate regularity and imply multiplication surjectivity;
global generation follows when the semigroup of globally generated
line bundles contains an ample bundle. Lemma 2.2 gives a conditional
regularity test for a kernel. These are available for testing actual
maps with a rank-two source. They neither choose terms in W nor
provide exactness and stability for arbitrary matrices or formal
Chern data. Their hypotheses must be checked on each actual kernel.

Read the Stacks Project's current statements on 2026-09-27:
[Lemma 42.40.3, tag 02UI](https://stacks.math.columbia.edu/tag/02UI),
the Whitney formula for exact sequences of finite locally free sheaves;
[Lemma 42.45.2, tag 0F9C](https://stacks.math.columbia.edu/tag/0F9C),
additivity of the Chern character; and
[Remark 42.56.11, tag 0FET](https://stacks.math.columbia.edu/tag/0FET),
the additive character on K-groups of perfect complexes. These support
future bookkeeping for an actual resolution. They are not existence
theorems for a bundle, an integral twist or prescribed Chern classes.
In particular no calculation here establishes that multiplicity two
removes L028's obstruction or clears the denominators of the final W.

Reread Verbitsky, *Hyperholomorphic bundles over a hyperkahler manifold*,
[arXiv:alg-geom/9307008v1, 29 July 1993, Theorem 2.5,
p. 9](https://arxiv.org/pdf/alg-geom/9307008v1#page=9).
It makes an existing stable bundle hyperholomorphic when its first
two Chern classes are invariant for the chosen hyperkahler structure.
It supplies neither that bundle nor invariant Chern data. Reuse the
earlier assessments of invariant forms, Kahler slope vanishing,
monads and transport for their unchanged supporting scope. No new
application of those statements to the doubled source is proved.

### Relevance, previous failures and the bounded test

The gap is a cycle representative that could support transport in
the missing NS-fixed RM direction. L026's single-polarization test,
L027's slope and divisor-span tests, and L028's fixed-coefficient
integrality test remain recorded exclusions with their original
hypotheses. In particular L028 explicitly leaves other coefficients
outside its conclusion. Changing multiplicity is a specific response
to that scope, not evidence that an obstruction has disappeared.

Reread L012's two sufficiently negative presentations and map-recovery
hypotheses. The source change does not itself prove escape from map
recovery or from L022's natural summand-obstruction framework. A
candidate must examine its actual kernels and relevant Ext groups;
no such groups or lifting loci were calculated here.

For the next separate research turn, first recompute the necessary
Chern constraints for the exact doubled sequence using the cited
additivity results. Test integrality in the actual divisor lattice
and existence of an integral terminal twist for the final W. If this
passes, compare candidate integral presentation terms with their
section spaces and actual surjections, retaining stability at Omega
as a separate obligation. Do not treat a doubled virtual class or a
direct sum of earlier terminal bundles as the required stable object.

Continue for a concrete integral presentation candidate with a
justified map mechanism and a bounded remaining stability test, or
for a scoped obstruction that changes the route. A formal rational
solution or failure of a search to find an obstruction is insufficient
to claim an advance. If this next test is unproductive, reassess the
mechanism before more construction work, and finish the continuation
or stop decision within the third exploration turn. Successful bundle
construction would still leave transverse transport and the universal
primitive-class gap unresolved. None of this test was carried out
during this literature turn.

### Search and access record

Queries on 2026-09-27 included:

- `"stable resolution" "direct sum" Mistretta`
- `"ideal sheaf" "direct sum" "stable resolution"`
- `"Mistretta" "resolution" "coherent sheaf" stable`
- `Mistretta "stable" "resolutions" "sheaves"`
- `"syzygy" "semistable" "higher dimensional" kernel sheaves stability`
- `"syzygy" "rank two" "semistable" stable kernel`
- `"On instability of Syzygy Bundles"`
- `"hyperholomorphic" "K3" "real multiplication" bundle`
- `"hyperholomorphic bundles" "real multiplication"`
- `"hyperholomorphic" "multiples" Chern classes bundles`
- `"K3" "prescribed Chern" "product" bundles`
- `"hyperholomorphic" "integrality" bundle`
- `Chern character additive exact sequence site:stacks.math.columbia.edu/tag`

The exact direct-sum searches supplied no matching theorem. Broader
results led to the thesis, higher-rank limitations and surface
comparisons read above. Off-target leads on noncompact hyperholomorphic
line bundles, toric surfaces and Higgs moduli were not imported.
Read primary PDF text and the named Stacks statements; no full audit
of every cited proof is claimed. The necessary sources for the scoped
feasibility test are accessible. The uninspected journal version and
unselected search leads are not essential inputs.

Also reread Deligne's [Clay statement, section 1 and remarks 2(ii),
2(iv)--(vi), pp. 2--3](https://www.claymath.org/wp-content/uploads/2022/06/hodge.pdf#page=2).
It retains rational cycle-class surjectivity on smooth projective
complex varieties. Its discussion of finite vector-bundle resolutions
and integral obstructions does not prescribe a stable representative
or a sufficient fixed multiple. This agrees with the existing
[target audit](../../foundations/01-target-and-scope.md).

## Mathlib

Coverage of the full doubled-source target: **not checked**. No
Mathlib match or absence is asserted. The named, directly linked
results above support generation, Chern bookkeeping and a conditional
hyperholomorphic criterion; none matches the whole target. Library
lookup was not needed to complete this source comparison.
