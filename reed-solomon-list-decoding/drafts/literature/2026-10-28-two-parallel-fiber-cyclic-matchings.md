# Two parallel fibers with six cyclic matchings — source comparison

TARGET: Test whether two parallel auxiliary lines can both have coefficient-image affine dimension two while satisfying all six transverse evaluation matchings in the pinned L030 labeling.
CHECKED: 2026-10-28
DECISION: EXPLORE
SEARCH_EVIDENCE: Bounded searches for cyclic matching rigidity, direction networks, finite-field variants and polynomial-evaluation rank found no inspected theorem covering the reduced model; exact queries and local duplicate/failure checks appear below. No novelty is inferred.
SOURCE_EVIDENCE: Read Streinu–Theran arXiv:0712.0031v4, Theorems C/D and Section 4, especially Lemmas 11–14 and both cases of Theorem C; Malestein–Theran arXiv:1304.0398v2, Section 1.3 equations (5)–(6), Theorem 3 and Sections 3.1–3.3. Reuse the prior inspected collineation, concatenation, planarization and generic-RS comparisons with their recorded limitations.
COMPARISON: Generic real direction-network rank and equivariant cyclic realizations do not cover arbitrary distinct subgroup labels with repeated quadratic assignments. The cyclic index pairings supply no realized linear or projective action. Full-sheet collineation/net comparisons do not add the missing hypotheses after restriction to two fibers.
GAP: Decide whether both retained fiber images can have affine dimension two for some permitted labels and K, or prove that at least one has dimension at most one uniformly in the pinned model.
REASON: Essential theorem-level comparison for the unchanged reduced target is complete enough for one bounded mathematical attempt; no matching import, impossibility result, permitted witness or novelty certification was obtained. This literature-only turn performs no calculation or derivation.
LITERATURE_REASON: The completed one-point test leaves global coupling as the obstruction. The new target retains two full parallel fibers and their cyclic matchings instead of the full sheet, a scope not assessed by the ready full-sheet literature record.
SCOPE: Pinned L030 q,T,E,F,H,k, arbitrary actual 61-core and bijection, K=E or F, two distinct complete parallel auxiliary lines, quadratic assignments with repetitions and all six transverse matching equalities; no extension to the other auxiliary points is assumed.

## Exact proposed reduced model

Use q=137, T={16,64,70,102,112,118,121}, E=F_65537,
F=F_(65537^28), H=<19139> of order 1024 and k=64. Let C be any
61-subset of H and sigma any bijection from (T times F_137)
disjoint union four dummy points to H minus C. Put x_(t,y)=sigma(t,y).
Take K=E or F and a in T. After an auxiliary translation, the two
selected lines are u+a v=0 and u+a v=h, with h!=0 in F_137.
This translation reindexes the labels and does not act on their field.

Assign degree-at-most-two polynomials R_w and S_z, allowing repetitions,
to the points (-aw,w) and (h-az,z), respectively. Require R_w(x_(a,0))
to be independent of w and S_z(x_(a,h)) to be independent of z.
For every r in T minus {a} and every w in F_137, require

\[
 R_w(x_{r,(r-a)w})
   =S_{\,w-h/(r-a)}(x_{r,(r-a)w}).
\]

The displayed pairing is obtained by intersecting the same auxiliary
r-line with the two selected lines. These are all six matchings, each
with 137 pairs; the original injective labeling is retained. No
polynomials at other auxiliary points or values on their full lines
are postulated. Ask whether both {R_w} and {S_z} can have affine
dimension exactly two over K. A witness must use permitted actual
labels and verify every displayed equality, both within-fiber
constancies and both affine dimensions. A proof of impossibility must
cover all C,sigma,a,h and both fields.

## Relevance, limits and source task

The main gap is arbitrary-center 67/68 safety. A two-fiber obstruction
could restrict coexistence of rank-two fibers in the full-sheet model;
it would leave a lone exceptional fiber, global collapse, partial
retention, compatible laws and RS transfer unresolved. A compatible
two-fiber example would stop only this stronger reduced obstruction,
not disprove the full-sheet fiber assertion or the RS target.

Before research, compare primary results on two planar point families
with cyclic correspondences, finite incidence rigidity and maps induced
by projectivities. Check whether any theorem actually supplies a map
between coefficient points; evaluation-plane intersections are lines,
and neither injectivity, conic containment nor a projective group action
may be presumed. Same-field and characteristic assumptions must be
retained. Reuse adequate prior comparisons rather than repeat a general
net search. Import a matching theorem only with exact hypotheses and
source passages, or record a bounded EXPLORE decision if no match is
found. Unread leads are not inputs.

Essential local inputs are L030 for the model and the unfinished
reasoning in drafts/2026-10-28-span-three-fiber-working.md for the
failure motivating this refinement. L135–L137 are comparisons only.
No cross-notebook result is needed. The review below completes the
previously required literature-only step. It assesses this exact target,
without extending its scope to the full sheet or supplying a lemma.
Mathlib full/supporting coverage has not been checked.

## Primary statements and their limits

### Direction-network rank and collapse

Ileana Streinu and Louis Theran, *Slider-pinning Rigidity: a
Maxwell-Laman-type Theorem*, Discrete & Computational Geometry 44
(2010), 812–837, [arXiv:0712.0031v4](https://arxiv.org/pdf/0712.0031v4),
11 August 2010. Read Theorems C/D, printed p. 3, and Section 4,
pp. 12–15, including the realization equations, Lemmas 11–14 and both
directions of Theorem C. Theorem C concerns generic direction vectors
in R² on an n-vertex, (2n−3)-edge graph: faithful realization is unique
up to translation and scaling precisely for Laman graphs. Theorem D
gives unique faithful generic direction-slider realizations for
looped-Laman graphs. Lemma 11's collapse conclusion explicitly requires
rank 2n−2. Lemma 14 requires full rank both before and after every edge
contraction; its proof excludes finitely many algebraic exceptional sets.

Thus graph counts or distinct labels alone do not verify these rank
hypotheses. Our evaluation equalities concern coefficients in K³, with
two prescribed evaluation-plane constraints, over finite fields. A
reduction to the theorem's planar direction system, its genericity or
its contraction ranks is not supplied. Repeated polynomials remain
allowed. These results provide a comparison and suggest what a rank
certificate would need to check; they supply no imported target bound.

### Cyclic symmetry is an extra realization condition

Justin Malestein and Louis Theran, *Frameworks with forced symmetry I:
Reflections and rotations*, [arXiv:1304.0398v2](https://arxiv.org/pdf/1304.0398v2),
14 March 2015. Read Section 1.3, printed pp. 3–4, equations (5)–(6),
Theorem 3, and Sections 3.1–3.3, pp. 9–11. The theorem characterizes
generic cone direction networks with unique faithful realization up to
scaling by cone-Laman quotient graphs. Its model imposes a free cyclic
graph action, symmetric directions and an equivariant placement in R²
under a specified finite rotation group. Equation (6) is the placement
equivariance condition, independent of the edge equations. Section 3.2
retains genericity; Section 3.3's obstruction cases use cone-(2,2) rank
or an ordinary (2,2) block. The faithful sufficiency case refers to an
earlier proof, not read here as a new input.

Our auxiliary index shifts do not impose equation (6) on coefficient
points or any compatible action on arbitrary actual labels. Repetitions
and both finite coefficient fields must be retained. The theorem cannot
be invoked merely because the matching permutations are cyclic.
Neither an equivariant finite-field extension nor the required placement
is imported. No essential source is blocked: the missing issue is
applicability, not access to these statements.

### Reused comparisons; no repeated general net search

The [full-sheet assessment](2026-10-28-span-three-line-fiber-rigidity.md),
“Primary statements and applicability,” already records inspected
Artstein-Avidan–Slomka arXiv:1604.01762v1, Theorems 1.3/1.4 and 2.7,
Remark 2.8; Khare–Tikaradze arXiv:2212.02429v3, Theorems 1.3/1.8;
and Petrushchenko–Timorin (2015), Section 1 and Main Theorem.
These comparisons remain adequate for excluding direct use: they
require injective line maps, affine-linear restrictions, or smooth/analytic
all-line planarizations. The two retained plane-supported families
do not establish those hypotheses. The earlier Laguerre/net comparison
is reused only within its recorded scope; L135–L137 remain comparisons,
not inputs to a two-fiber rigidity theorem. No injectivity or conic
containment is inferred from affine dimension two.

For evaluation-rank terminology, reuse the [earlier source record](2026-09-26-current-target.md),
“New primary readings,” for Brakensiek–Gopi–Makam,
[arXiv:2206.05256v4](https://arxiv.org/pdf/2206.05256v4), 28 August 2024,
Theorem 1.13, Corollary 1.15, Theorem 1.16 and Proposition 4.5.
Its generic/random RS conclusions do not certify every prescribed
subgroup labeling. The current search rediscovered that paper; its
41-page proof was not reread. No conversion of the two-fiber constraints
to higher-order MDS is asserted. No result is being reproved.

## Bounded search, duplicate and failure record

Queries issued on 2026-10-28 included:

- `direction networks rigidity theorem generic directions unique faithful realization Malestein Theran`
- `bipartite graph polynomial evaluation constraints rank quadratic finite field arbitrary labels rigidity`
- `cyclic direction networks finite order symmetry non generic directions rigidity`
- `Streinu Theran Slider Pinning Rigidity arxiv 0712`
- `Malestein Theran generic rigidity frameworks rotational symmetry direction networks cone theorem cyclic arxiv`
- `"polynomial" "evaluation" "rigidity" "bipartite" finite field`
- `"projectivity" "two" "point sets" "cyclic" finite geometry`
- `"Reed-Solomon" "generic" "higher order MDS" theorem arbitrary evaluation points`
- `"cyclic" "matchings" "projectivities" geometry point sets`
- `"quadratic" "polynomials" "cyclic matchings"`
- `"two" "parallel lines" "direction network"`
- `"finite field" "direction networks" rigidity`
- `"projective" "cyclic correspondences" conic`

Exact-description searches supplied no inspected matching theorem.
Broader results led to the primary direction-network comparisons above
and the already assessed generic-RS literature. Search snippets and
secondary summaries were not theorem inputs. A result on linearly
constrained real bar-joint frameworks (Cruickshank–Guler–Jackson–Nixon,
2018) was only a search lead; its full theorem/proof is uninspected and
is not an essential dependency. General conic/projectivity search hits
are likewise not inputs; conic containment and projective transport
are not hypotheses of this target.

Notebook-local searches for two-fiber, parallel-fiber, cyclic-matching,
direction-network and projectivity terminology found the saved target,
the full-sheet assessment and earlier projective-transport comparisons,
not a recorded solution of this reduced problem. Read L030's hypotheses
and model construction, the saved span-three working record's scope and
initial reduction, ATTEMPTS/110 and history/538. ATTEMPTS/110 explains
why one off-fiber point is insufficient and why its patch is not a
full-sheet counterexample. ATTEMPTS/109's residual-rank route and the
older omission failures remain parked; none is reopened by this review.
No sibling notebook was searched or used.

## Decision and bounded continuation

DECISION EXPLORE covers exactly TARGET and SCOPE above. The primary
comparisons leave the simultaneous two-fiber compatibility unresolved;
they neither force a projectivity nor furnish a permitted example.
This is completed source coverage for a bounded attempt, not progress
beyond the checked mathematical sources and not proof of originality.

Continue only by retaining all six complete matchings, both within-fiber
constancies, permitted distinct actual labels, repetitions and K=E or F.
The decisive positive evidence is a permitted exact two-fiber assignment
with both affine dimensions two, checking every equality and both ranks.
That would abandon only the proposed universal two-fiber obstruction.
The decisive negative evidence is an impossibility proof uniform in
C,sigma,a,h and both fields; it could restrict coexistence in the full
sheet, but would leave a lone rank-two fiber and the independent RS gaps.
A generic-rank assertion, sampled failure to find a witness, arbitrary
nonpermitted labels or an imposed projective action decides neither case.
If one bounded attempt gives neither, save the unfinished compatibility
conditions and reassess under the existing exploration budget. No
mathematical calculation, lemma or script was performed in this review.
