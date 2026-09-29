# Mixed resolution in the minimal cubic divisor subspace — literature assessment

TARGET: Assess whether a three-presentation resolution of I_C using product line bundles with factor divisor classes in W=im(A) from L025 can realize L027's forced mixed correction and admit a terminal twist stable at omega with SU(2)-invariant c_1 and c_2.
CHECKED: 2026-09-27
DECISION: EXPLORE
SEARCH_EVIDENCE: Searched constrained mixed resolutions, multigraded regularity, K3 syzygy stability and prescribed Chern data; followed the surface-stability references to the stronger rank-one kernel theorem of Rekuski. Exact queries, versions, readings and exclusions are recorded below.
SOURCE_EVIDENCE: Hering--Schenck--Smith, arXiv:math/0502240v2, Theorem 2.1, https://arxiv.org/pdf/math/0502240v2#page=3; Rekuski, arXiv:2303.13459v2, Theorem 4.3, Corollary 4.4 and Remark 4.5, https://arxiv.org/pdf/2303.13459v2#page=11; Fantechi--Miro-Roig, arXiv:2306.05338v1, Example 6.4 and Question 6.6, https://arxiv.org/pdf/2306.05338v1#page=24; further precise comparisons below.
COMPARISON: Multigraded regularity conditionally supplies actual evaluation and multiplication maps, and a stronger theorem gives stable kernels for positive rank-one sources in arbitrary dimension; neither realizes the forced cubic Chern data in an exact three-presentation resolution stable at the specified metric. No full construction or exclusion was matched.
GAP: Reconcile actual presentation maps and exactness with L027's forced correction, an integral terminal twist, and stability at the common metric; positive generation, a stable first kernel and a formal K-class do not establish these simultaneous requirements.
REASON: The minimum surviving divisor case has a concrete map-feasibility test using read supporting tools, but no matching existence theorem. Permit one bounded test in a separate research turn, retaining the exact target and the existing exclusions; this review makes no novelty or bundle-existence claim.

## Hypotheses

Use the same very general S, correspondence C, operator A and ample
omega as in L027. Put X=S x S and Omega=p_1^*omega+p_2^*omega.
The required sequence is an actual exact sequence

\[
0\longrightarrow E\longrightarrow P_2\longrightarrow P_1
 \longrightarrow P_0\longrightarrow I_C\longrightarrow0,
\]

with each P_i a finite sum of product line bundles whose two factor
divisor classes belong to W=im(A). The terminal E must be locally
free of positive rank, and E tensor M must be Omega-stable with
invariant full c_1 and c_2 for an actual line bundle M. The diagonal
SU(2) action uses this same metric on both factors. L027 already
identifies the transcendental ch_2 action as U for this length.

Retain L027's forced correction and rational projections of c_1(M),
including the requirement of at least rank(E)+1 strictly positive
twisted terminal summands. These are necessary conditions, not freely
assignable construction data. W means the final chamber-compatible
image in L025: its rational conjugation is not asserted to preserve
the integral divisor lattice or to be a surface automorphism.

Reuse the adequate [multiple-divisor assessment](2026-09-27-multiple-divisor-stable-resolutions.md)
and [bundle assessment](2026-09-27-compatible-cubic-rm-stable-bundle.md)
for their unchanged statements. The [rational-target audit](../../foundations/01-target-and-scope.md)
remains the scope of the main problem.

## Conclusion

The exact saved target now has a completed EXPLORE assessment.
The new readings provide tools for a test of actual maps and improve
the known scope of first-kernel stability. They do not supply the
requested three-presentation bundle or a theorem excluding every such
bundle. Their statements are available by citation; no reproof,
specialization, Chern calculation or construction was performed here.

The gap addressed is an algebraic representative of U that could
support transport outside the three-dimensional Dickson tangent.
Even a successful bundle construction would leave transport into
the particular missing NS-fixed RM direction to prove. The attained
span is still 21-dimensional, and only three directions against four
required have been attained. Arbitrary primitive fourfold classes
and the higher-dimensional universal target remain unresolved.

This review is LITERATURE / NOVELTY_UNCHECKED / EXPLORATION. It uses
one exploration turn after L027's informative negative result.
There is no new mathematical exclusion or complete candidate, and
no claim of progress beyond the checked literature. The original
pending scope and the interim reading checkpoint are incorporated
below; neither was an unfinished mathematical derivation.

## Proof

This section records source evidence and applicability, not a new proof.

### Tools for actual maps

Read Hering--Schenck--Smith, *Syzygies, multigraded regularity and toric
varieties*, [arXiv:math/0502240v2, 9 August 2006, Theorem 2.1
and proof, pp. 3--4](https://arxiv.org/pdf/math/0502240v2#page=3).
For globally generated B_1,...,B_l on a projective variety, their
regularity hypothesis on a coherent sheaf F is

\[
H^i(X,F\otimes L\otimes B^{-u})=0
\quad(i>0,\ u\in\mathbb N^l,\ |u|=i).
\]

It propagates under nonnegative twists, yields the indicated
multiplication-map surjectivity, and yields global generation if
the generated semigroup contains an ample line bundle. This part
does not require the variety to be toric.

Thus there is a precise conditional tool to check evaluation maps
for I_C and its actual intermediate kernels. The theorem does not
choose divisors in W, prescribe the alternating Chern data, or make
their terminal kernel stable. Regularity must be checked separately
on each relevant coherent sheaf; it is not an assertion about
arbitrary matrices having the desired degrees.

### A stronger stability theorem for the first kernel

Followed the reference in Misra--Ray and Miro-Roig to Rekuski,
*Stability of Kernel Sheaves Associated to Rank One Torsion-Free
Sheaves*, [arXiv:2303.13459v2, 12 May 2023, Theorem 4.3 and
Corollary 4.4, p. 11; Remark 4.5 and following discussion,
pp. 12--13](https://arxiv.org/pdf/2303.13459v2#page=11).
Read also its rank-one and polarization conventions, pp. 1--3.
For a rank-one torsion-free source and a fixed very ample H,
sufficiently positive twists have an H-stable full evaluation kernel.
The statement allows arbitrary Picard rank and dimension at least two;
the explicit bound is expressed through regularity and numerical data.

This covers a potential first evaluation of a positive twist of I_C
by citation. It does not assert local freeness of that first kernel.
The author's subsequent discussion explicitly prevents using the
same asymptotic bound as an automatic higher-rank iteration. Nor does
the statement treat mixed evaluation terms or stability at Omega.
This strengthens the earlier surface/Picard-rank-one comparison without
removing the present realization gap.

### Stability of surface syzygies does not fill the product gap

Read Fantechi--Miro-Roig, *Lagrangian subspaces of the moduli space
of simple sheaves on K3 surfaces*, [arXiv:2306.05338v1, 8 June 2023,
section 6, pp. 23--26](https://arxiv.org/pdf/2306.05338v1#page=23).
Example 6.4 compares two generating subspaces with equal dimensions
and the same line-bundle source but different stability behavior.
Question 6.6 asks when a generating subspace with stable kernel
exists. This rules out treating presentation degrees and simplicity
as a cited stability certificate. It is a surface comparison, not
a nonexistence statement for the present X.

Followed their Proposition 6.3(2) reference to Basu--Pal,
*Stability of Syzygy bundles corresponding to stable vector bundles
on algebraic surfaces*, [arXiv:2105.05433v1, 12 May 2021,
Theorem 1.1 and its setup, pp. 1--2](https://arxiv.org/pdf/2105.05433v1#page=2).
Its positive-twist stability theorem concerns a stable vector bundle
on a smooth projective surface with a fixed very ample divisor.
It does not supply this fourfold iteration.

Read Misra--Ray, *On Stability of Syzygy Bundles*,
[arXiv:2405.17006v1, 27 May 2024, Theorems 1.2--1.3,
p. 2, and Question 3.4, p. 9](https://arxiv.org/pdf/2405.17006v1#page=2).
Their effective criterion retains generation, cohomology,
multiplication and curve-restriction hypotheses on a surface.
The asymptotic theorem allows a semistable globally generated source,
again on a surface. The higher-dimensional vector-bundle question
is posed, not answered, there. This is a statement about that version,
not a claim that no later theorem exists.

Read Miro-Roig, *Stability of syzygy bundles of Ulrich bundles*,
[arXiv:2604.05740v1, 7 April 2026, Theorem 3.8,
p. 6, and Conjecture 3.11, p. 7](https://arxiv.org/pdf/2604.05740v1#page=6).
The theorem gives semistability of the evaluation kernel for an
Ulrich bundle on a K3 surface or a Fano variety with index at least
dimension minus two. These hypotheses and this conclusion do not
give the required stable mixed resolution on the K3 self-product.
No assertion about that paper's conjecture is imported.

### Unchanged tools and previous failures

Reuse, without claiming a fresh reading, Mistretta,
[Theorem 3.1, arXiv:math/0310185v2, pp. 7--9](https://arxiv.org/pdf/math/0310185v2#page=7):
its stable terminal resolution uses powers of one ample polarization.
L026 and [Attempt 017](../../ATTEMPTS/017-single-polarization-stable-resolution.md)
already exclude that recipe for the required invariance, including
terminal twists. L027 and
[Attempt 018](../../ATTEMPTS/018-mixed-resolution-slope-and-small-divisor-spans.md)
exclude the untwisted anti-ample case and all cases with at most
two original factor divisor dimensions.

The previous assessment's read Hoppe criterion, monad comparisons
and Kahler morphism vanishing remain sufficient for their stated
scopes. The withdrawn Shang claim remains excluded. Reuse Verbitsky,
[Theorem 2.5, arXiv:alg-geom/9307008v1, p. 9](https://arxiv.org/pdf/alg-geom/9307008v1#page=9),
only after an actual stable bundle and invariant Chern classes exist.
Its conditional conclusion does not provide that input.

Reread L012's two sufficiently negative presentations and their
map-recovery hypotheses. Neither a third presentation nor the use
of several ample divisors is by itself a certified escape. A proposed
sequence must compare its actual intermediate kernels and Ext groups
with that recovery argument. The current assessment establishes no
vanishing or nonvanishing of those groups.

### One bounded continuation for this exact target

The three screened mechanisms are mixed evaluation maps, iteration
of known stable-kernel constructions, and the previously reviewed
monad constructions. Only the first currently provides a tool for
testing actual maps in the stated scope without assuming the desired
stability theorem. This is a research judgment, not a mathematical
exclusion of the other mechanisms.

In the next separate research turn, test compatibility of L027's
forced equations with the maps of a three-presentation sequence.
Start from the allowable section spaces between actual integral
product line bundles in the final W and from sections generating
I_C; test required ranks and the positive-terminal-summand condition.
If using sequential evaluation, identify the successive kernels and
state the concrete regularity/global-generation conditions that
certify its surjections. Keep the integral twisting class, full
c_1 and c_2, and the fixed Omega throughout.

Continue only for an explicit integral presentation candidate with
a justified map mechanism and bounded remaining checks, or for a
scoped obstruction that changes the route. A formal solution for
the mixed tensor alone does not meet this threshold. In particular
no claimed stability may rest solely on the first-kernel theorem,
genericity of unspecified matrices, or a different polarization.
If only formal data survive, reassess after that second unproductive
turn and complete the continuation/stop decision within the third.
No part of this test was carried out in this literature turn.

### Search, access and coverage record

Queries on 2026-09-27 included:

- '"stable resolution" "mixed" "line bundles"'
- '"K3" "syzygy bundles" "stability" polarization'
- '"multigraded regularity" "resolutions" "ample" line bundles'
- '"real multiplication" "hyperholomorphic" bundles cubic'
- 'Hering Schenck Smith "Syzygies" "multigraded" theorem 2.1'
- '"stable" "kernel" "different degrees" "line bundles" syzygy'
- '"Kähler" "polarisation" "stability" "openness" sheaves Greb Toma'
- '"Lagrangian Subspaces of the Moduli Space of Simple Sheaves" arxiv'
- '"K3" "mixed" "resolution" "stable" bundles'
- '"cubic" "real multiplication" "bundle"'
- '"prescribed Chern classes" "syzygy"'
- '"syzygy bundles" "Rekha" "Theorem 4.3"' and '"syzygy" "R24" stability' (unhelpful follow-ups before identifying the author in the bibliography).
- 'Rekuski "Stability of kernel sheaves" arxiv'
- '"Stability of kernel sheaves associated to rank one" "4.3"'

Exact-title and reference follow-ups led to the pinned primary texts.
PDF text was read at the stated locations. A screenshot request for
Rekuski p. 11 did not yield an image inspected here; no visual check
or full-proof audit is claimed. The arXiv version records were checked.
The bounded search found no full match; this is not evidence of novelty
or a proof of absence from the literature.

The Greb--Toma [journal PDF](https://jep.centre-mersenne.org/item/10.5802/jep.116.pdf)
failed to open. Its search excerpt is not theorem evidence, and no
chosen input relies on that source. Newer multigraded-regularity,
curve-stability and projective-bundle search leads were not inspected
as theorem-level sources and are not inputs. No essential source for
the proposed map test is left unread.

## Mathlib

Coverage of the full realization target: **not checked**. No Mathlib
match or absence is asserted. The named theorem links above identify
supporting generation, kernel-stability and conditional
hyperholomorphic results; none matches the simultaneous target.
No library lookup was needed for this source comparison.
