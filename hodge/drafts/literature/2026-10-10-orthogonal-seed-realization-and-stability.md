# Orthogonal seed — actual realization and vector stability source comparison

TARGET: Assess analytic realization, acyclicity and exact-h vector stability for L081's formal orthogonal seed deformation.
CHECKED: 2026-10-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Compared complete L080/L081 with the ready existence assessment and ATTEMPTS/053; searched analytic Kuranishi realization, local vector GIT stability, Artin analytic approximation and proper analytic cohomology; inspected primary statements and relevant proof cases recorded below.
SOURCE_EVIDENCE: Buchdahl--Schumacher, Complex Manifolds 9 (2022), 78--113, Theorem 1, Section 2/Proposition 2.6, Corollary 4.3, Theorems 4.7/5.4/8.1; Artin (1968) Theorem (1.2), with directly inspected Rond (2018) Theorem 2.1; Grauert (1960) Section 7, Satz 3/6 and complete 1963 correction; Serre GAGA Section 12, Theorems 1--3; reuse L080's standard surface and L081's formality inputs.
COMPARISON: Fixed-Kahler-metric vector stability has a known local GIT criterion, and finite analytic equations admit convergent approximations preserving a formal first jet. These tools cover general bridges, but no inspected theorem already constructs the specified orthogonal stable acyclic J_5.
GAP: Justify the analytic skew-adjoint Kuranishi restriction and formal-arc comparison, then test the actual underlying-vector harmonic parameter under the full vector automorphism group, retaining the exact h and proving actual cohomology vanishing.
REASON: Coverage is adequate for one separate bounded specialization attempt; the orthogonal restriction and full vector-group test must be proved there. No realization or rank-five existence conclusion is derived in this literature-only review.
LITERATURE_REASON: The prior assessment covered seed existence and a formal model only; essential unread analytic-realization and underlying-vector-stability statements were needed for this changed actual-family scope.
SCOPE: L080's actual marked projective K3 S, fixed real ample h, spherical stable E and oriented quadratic seed J_0=O_S plus E plus E^vee; L081's specified tangent x=y=u_1=1,v_1=-1/2, other coordinates zero. One proof attempt may specialize the inspected analytic slice construction to skew coefficients, retain that first jet by analytic Artin approximation, and check full underlying-vector stability and actual acyclicity. No spin, prescribed obstruction class, generic-integral polarization, common kernel, other image or transport hypothesis is admitted.

## Relevance and continuation test

The main gap remains algebraic realization of every primitive rational
Hodge class, even on arbitrary fourfolds. The intermediate target is
actual realization of this particular orthogonal seed direction with
vector stability at the fixed metric and acyclicity. Its plausible
use is a candidate rank-five building block for L079's surviving
branch. Even a successful construction would leave the other image,
a common F, its full mixed action and transverse transport unproved.

Continue only if an actual quadratic family retains the specified
first jet and its underlying vector harmonic parameter passes the
full vector-group stability test at h. An actual-family lemma alone
would also be useful, with stability expressly unresolved. Stop this
recipe if a load-bearing specialization fails; that would not exclude
all J_5. No repeated characteristic/index test is approved.

Essential local inputs are L080, L081 and L052's exact S,h and line
lattice through L080; L079 supplies the requested block and its audited
necessary-test stop. Preserve ATTEMPTS/043,/045,/053, the independent
t=2 branch and the parked flat (-10,-17) source blocker. Scoped
searches of the relevant recent assessments and these failure records
found no prior Buchdahl--Schumacher/Artin actual-seed comparison.
This is a source-coverage advance, not mathematical novelty or an
existence assertion. No cross-notebook input is used.

## Primary statements and qualifications

**Analytic slice and vector stability.** Nicholas Buchdahl and Georg
Schumacher, *Polystable bundles and representations of their
automorphisms*, Complex Manifolds **9** (2022), 78--113,
[DOI 10.1515/coma-2021-0131, published text](https://d-nb.info/1262812674/34).
Read Theorem 1, pp. 78--79; Section 2, Lemma 2.5, Proposition 2.6
and equation (2.4), pp. 82--84; Corollary 4.3, p. 87; Theorem 4.7
and proof, pp. 89--90; Section 5 and complete Theorem 5.4 proof,
pp. 91--94; Theorem 8.1 and its stable-branch setup, pp. 103--104.
The slice is analytic and equivariant for a polystable bundle on a
fixed compact Kahler manifold. In Proposition 2.6 the correction is
unique on the indicated orthogonal complement, with Sobolev exponent
p>2 dim_C X; its harmonic obstruction defines the integrable locus.
Theorem 8.1 supplies a Hermite--Einstein connection for sufficiently
small GIT-polystable slice parameters; Theorem 5.4 identifies stability
within this locus. Use the full vector group. Scalar automorphisms act
trivially: its proof, p. 93, tests isotropy dimension one, and Section 7,
p. 100, tests ker L_alpha=C id. A finite orthogonal stabilizer alone
is insufficient. No integral-polarization hypothesis occurs here.

The preprint [2002.03548v1, 10 February 2020](https://arxiv.org/pdf/2002.03548)
was used for discovery; the published statements/proof cases above
control the comparison. Its earlier title is *Polystability and the
Hitchin-Kobayashi correspondence*. These are the same source lineage,
not two independent existence results. General principal SO5
stability and asymptotic principal-bundle nonemptiness do not replace
this vector theorem. The prior rank-five assessment already records
their insufficient exact-charge coverage.

**Formal first jet versus actual curve.** Michael Artin, *On the
solutions of analytic equations*, Invent. Math. **5** (1968),
277--291, [Theorem (1.2), p. 277](https://mathweb.ucsd.edu/~toal/artin.pdf).
For finitely many convergent equations f(x,y)=0 over a characteristic-zero
nontrivially valued field, a formal solution y-hat(x) with zero constant
term can be approximated by a convergent solution modulo (x)^c for
every integer c. Over C and one parameter, c=2 retains the first jet.
This is approximation, not convergence of the particular formal series.
The complete original first-page theorem was returned in indexed
primary text; direct PDF text extraction returned zero lines, so the
original proof is not claimed as read. Directly inspected supporting
statement and proof reductions: Guillaume Rond, *Artin approximation*,
Journal of Singularities **17** (2018), 108--192,
[Theorem 2.1, p. 122; proof reductions pp. 124--126](https://www.journalofsingularities.com/volume17/rond.pdf#page=15).
Its characteristic-zero/convergent-equations formulation agrees with
Artin's statement. Neither source supplies finite analytic equations
for this orthogonal bundle without the Kuranishi specialization.

**Actual cohomology.** Hans Grauert, *Ein Theorem der analytischen
Garbentheorie und die Modulraume komplexer Strukturen*, Publ. Math.
IHES **5** (1960), 5--64,
[Section 7, Satz 3, pp. 62--63; Satz 6, p. 64](https://www.numdam.org/article/PMIHES_1960__5__5_0.pdf#page=61).
The setting is a proper surjective holomorphic map to a reduced
complex space and a coherent sheaf flat over it; fibre cohomology is
upper semicontinuous, and its Euler characteristic is constant when
the base is connected. Read the local flatness hypotheses and the
curve-reduction proof of Satz 3, as well as the Satz 6 statement.
Read the complete [1963 correction, pp. 35--36](https://www.numdam.org/item/PMIHES_1963__16__35_0.pdf):
it repairs earlier proof estimates and warns that Section 7 Satz 2's
exceptional set need not be closed. Do not use that erroneous closure
claim. A locally free family on S times a disc fits this cohomological
scope only after its actual construction. Semicontinuity alone does
not turn L081's section obstruction into nearby vanishing.

Reuse the standard equal-slope Hom vanishing, K3 Riemann--Roch and
Serre duality already used in L080. Actual vector stability is a
possible sufficient cohomology bridge at these fixed invariants;
the next proof must check its applicability and all three cohomology
groups on actual fibres. No new cohomology result is proved here.

**Algebraic fibres and form.** Reuse the coherent-cohomology/exactness
coverage in the local L064 critical-audit assessment. Extend its
previously inspected cohomology scope by reading Serre,
*Geometrie algebrique et geometrie analytique*, Ann. Inst. Fourier
**6** (1956), 1--42,
[Section 12, Theorems 1--3, pp. 19--20](https://www.numdam.org/article/AIF_1956__6__1_0.pdf#page=20).
On a projective complex variety these give cohomology comparison,
full faithfulness and existence of an algebraic coherent sheaf for
an analytic coherent sheaf. This covers individual candidate fibres
and their morphisms, subject to checking local freeness and the
perfect symmetric form. It does not assert algebraization of an
entire family over an arbitrary analytic disc. No general principal
SO5 algebraization assertion is needed.

## Exact difference left for the separate proof attempt

The following are obligations, not results established by this review.
Use the named general theorems by citation; do not reprove them.

1. Choose the seed's Hermite--Einstein connection at the unchanged h
   using its actual polystable summands. Verify compatibility with Q
   and that the Hodge/slice operators preserve skew coefficients.
   The explicit elliptic construction in Section 2, rather than a
   principal-simplicity assertion, is the assessed source for this
   specialization. Its form-preserving restriction is not yet proved.
2. Place L081's compatible formal deformation into that finite
   analytic slice with the same first class, justifying the gauge and
   first-jet comparison. Apply Artin only after checking every equation
   and retaining Q; do not assume an analytic formality equivalence.
3. Compute the full vector-group action on the included tangent and
   verify the actual nearby harmonic parameters satisfy the source's
   vector criterion. The full group is L080's (C^*)^3 with its common
   scalar kernel, rather than L081's one-dimensional orthogonal torus.
   No full-group weight or closed-orbit calculation is performed today.
4. Verify actual fibre cohomology and algebraic local freeness/form
   under the cited inputs. If any earlier bridge remains open, record
   only the proved intermediate result. No J_5, image or kernel may
   be inferred from a formal point or a first-order section test.

This unchanged TARGET now has SPECIALIZE coverage for the bounded
attempt above. Its outcome is not predetermined. Unlisted changed
constructions or essential hypotheses need REVIEW_REQUIRED separately.
The main Hodge argument and DAG have not changed; no lemma or
mathematical script was written in this literature-only turn.

Full matching Mathlib coverage for the seed's actual realization and
stability: not checked. Supporting analytic deformation/GIT coverage:
not checked. No absence or formal-verification claim is made.
