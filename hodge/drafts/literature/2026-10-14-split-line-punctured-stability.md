# Split-line complex family — punctured stability source comparison

TARGET: Assess exact-h punctured stability of L101's two-parameter complex family using the full vector automorphism action.
CHECKED: 2026-10-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the inspected rank-five assessment; searched the published source for Theorems 5.4/8.1 and their uniformity and scalar-isotropy proof cases; compared L101 and L094 with the prior realization scope and ATTEMPTS/061,/046 and history/261. No new broad search or novelty inference is claimed.
SOURCE_EVIDENCE: Buchdahl--Schumacher, Polystable bundles and representations of their automorphisms, Complex Manifolds 9 (2022), 78--113, DOI 10.1515/coma-2021-0131, published PDF https://d-nb.info/1262812674/34; Theorem 3 and scalar convention p. 79; Theorem 5.4 and complete proof pp. 93--94; Theorem 8.1 and stable-branch setup pp. 103--104; Lemma 8.3 and uniform closure argument p. 106, with Lemma 8.4 statement and matrix/torus reduction pp. 106--107.
COMPARISON: The published fixed-metric theorem covers integrable sufficiently small harmonic slice parameters uniformly and uses the full vector automorphism group modulo common scalars; it does not establish the required orbit and higher-term estimates for this particular two-parameter family.
GAP: Prove that both off-diagonal projections of L101's actual harmonic parameter remain nonzero uniformly on a sufficiently small punctured C^2 ball, prove closed orbit and scalar-only isotropy for the full vector action, and identify the actual slice bundle before applying the imported theorem.
REASON: Essential source coverage is complete for one bounded specialization of the unchanged target; the remaining tasks are finite-dimensional orbit and analytic remainder checks, not an uncovered quaternionic integration theorem.
LITERATURE_REASON: The target changes from determinant-fixed complex realization to exact-h stability on a whole punctured C^2 germ; the prior rank-five coverage required comparison of its action and uniformity with this changed family.
SCOPE: One mathematical attempt on audited L101's actual integrable slice family and prescribed first jet, with L094's e_1,e_2,v,W and L071's retained S,I,g,h,k,E. No quaternionic parameter family, global kernel, nonempty reducible locus, separation, reconstruction, transport or global mixed action is covered.

## Relevance and stopping test

The main gap is universal algebraic realization of primitive rational
Hodge classes, already unresolved on arbitrary fourfolds. The intermediate
target is exact-h stability of every noncentral fibre of the actual
complex family in L101, on one punctured two-dimensional neighborhood.
It could supply a local stable holomorphic prerequisite and distinguish
ordinary vector stability from the still unresolved fixed-metric
quaternionic integration problem. It supplies no common product F.

Continue only if both actual weight projections admit positive linear
lower bounds in the parameter norm that dominate the analytic remainder,
and the full orbit meets the cited vector criterion throughout that
neighborhood. A disc-by-disc radius is insufficient. If this test fails,
record precisely the offending projection, orbit or slice hypothesis and
restrict or abandon the punctured-neighborhood claim. No result of this
mathematical test is established in this literature-only step.

## Inspected source and qualifications

Use Nicholas Buchdahl and Georg Schumacher, *Polystable bundles and
representations of their automorphisms*, Complex Manifolds **9** (2022),
78--113, [published text](https://d-nb.info/1262812674/34).
Theorem 8.1, p. 103, assumes a fixed Hermite--Einstein reference
connection and a GIT-polystable harmonic parameter in the analytic slice;
its radius depends only on that connection. Integrability is additionally
required to obtain a holomorphic bundle. Theorem 5.4, pp. 93--94,
identifies vector stability once bundle polystability is obtained.
The scalar convention, p. 79, quotients the full automorphism group by
common nonzero scalars. The complete proof of 5.4 checks both the stable
case and the equal-slope splitting case through parallel endomorphisms.
Section 8 explicitly repairs Section 7's direction-dependent radius.
Its stable-branch setup, pp. 103--104, and Lemma 8.3/closure argument,
p. 106, remove directional dependence; Lemma 8.4 uses the matrix
blocks of the polystable splitting and a torus reduction, pp. 106--107.
No integral polarization, fixed parameter dimension, smooth quotient
or irreducible central bundle is required. These theorems are imported;
no reproof of their elliptic or uniformity arguments is proposed.

The source hypotheses fit L101's fixed compact Kähler surface and its
actual direct-sum Hermite--Einstein reference connection. Its proof
constructs the family using precisely the Proposition 2.6 slice and
complete obstruction equations, so comparison does not require a new
analytic normal-form theorem. The slice membership and smallness still
must be cited and checked on the actual parameters in the next attempt.
The metric and real h remain unchanged throughout; replacing h by a
nearby integral class is neither necessary nor approved.

L101's audited proof already records full Aut(E)=(C*)^2, and L094 records
the off-diagonal weight spaces and their dimensions. Common scalars are
ineffective. Using only determinant-one automorphisms would retain a
finite central kernel and would require accounting for it; it must not
replace the source's full vector-group convention. The next attempt must
explicitly check the full conjugation action and its effective quotient.

## Exact obligations left to mathematics

L101 supplies an actual analytic harmonic parameter alpha(s,t), solving
the complete slice equations and retaining ell(s,t)=s B(v)+t B(Jv)
modulo (s,t)^2. L094 supplies v=e_1+Je_2, Jv=Je_1-e_2 and orthonormal
positive-weight vectors e_1,e_2, with J exchanging the weight sectors.
These are existing inputs, not a new orbit computation in this review.

1. Identify the positive and negative projections of ell using precisely
   that harmonic/Dolbeault identification; check their kernels and obtain
   uniform norm bounds. Injectivity of the total first jet alone does not
   suffice for both projections.
2. Control both projections of alpha-ell by a quadratic bound on one
   neighborhood. The constants and resulting radius may depend on the
   chosen actual analytic family. No common radius for all possible Artin
   approximations is sought. All nonzero parameter directions, including
   both coordinate axes, must be covered.
3. Prove closed orbit and scalar-only isotropy for these actual points
   under full Aut(E). First-order orbit stability alone is insufficient.
4. Shrink into the fixed slice and Theorem 8.1 neighborhoods, use actual
   integrability to obtain polystability, then apply Theorem 5.4 for strict
   vector stability at h. This does not identify a quaternionic family or
   prove smooth dependence of a unitary gauge through the central fibre.

## Reuse, failures and limits

The rank-five [assessment](2026-10-10-orthogonal-seed-realization-and-stability.md)
provides the same published theorem lineage. L082 is a comparison only:
its different vector action and one-parameter conclusion are not inputs.
The earlier L101 realization assessment expressly excludes stability,
so this comparison fills a real source-coverage gap rather than repeating
a ready stability decision. No matching rank-two family theorem was
identified in the sources checked; this is not a novelty claim.

Preserve ATTEMPTS/061's second-order stop, ATTEMPTS/046 and history/261's
separation stops, and the parked quaternionic-integration route. They
are method-specific evidence and are not global nonexistence theorems.
Essential continuation inputs are audited L101 and L094; L071's retained
surface and metric enter through those hypotheses. No F, nonempty
reducible set, identification W=r(TB), quaternionic germ, reconstruction,
global mixed action or transport is assumed. These remain independent
unresolved steps even if the stability attempt succeeds.

Matching Mathlib coverage of this local analytic vector-stability theorem
and the specialized punctured family: not checked. Unknown coverage is
not absence. No lemma, mathematical script, DAG edge or argument-overview
change is made in this source step. SPECIALIZE approves a separate
mathematical attempt on the unchanged TARGET; it does not prove stability.
