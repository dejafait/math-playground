# Split-line local classifying germ — completed source comparison

TARGET: Assess finiteness and generic degree at most two for the local coarse classifying germ of L101/L102 via full-group invariants.
CHECKED: 2026-10-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Exact/stronger-result discovery checked analytic GIT quotients, finite holomorphic germs, local algebra, generic degree and multiplicity projection formulas; narrowly compared ATTEMPTS/046,/061, histories/261,/265,/274 and the saved analytic-integration assessment. Primary finite-germ and multiplicity tools are accessible; no inspected theorem directly gives the actual L101/L102 degree bound.
SOURCE_EVIDENCE: Inspect Buchdahl--Schumacher (2022) Corollaries 4.6/4.8/4.9; 2008.04625v3 Definition 1 and Theorems 1/2/3/5/6/8 with quotient proof cases; 2108.03255 Section 6 Theorem 1 and weak-normality qualification; Mond--Nuño-Ballesteros (2020) Appendix C Lemma C.1/Corollaries C.1/C.2 and Appendix D Theorems D.5/D.6/D.7, Lemma D.2 and Corollaries D.6--D.8; Huneke--Swanson (2006, author revision February 2023) Theorem 11.2.7 and Proposition 11.2.9(1), including proofs.
COMPARISON: Known results provide the analytic classifying quotient, full orbit comparison, finite-germ criterion, fraction-field degree and finite-extension multiplicity formula. Remaining work is the explicit full effective-C* invariant specialization on the actual convergent alpha and its image local ring, retaining every higher coefficient. Punctured stability alone is no degree theorem.
GAP: Establish the actual invariant map and its isolated central fibre; compute the pulled-back maximal ideal, then compare the minimal-generator bound and Hilbert--Samuel multiplicity formula to test generic degree at most two. Qualify the reduced analytic quotient versus the weakly normal coarse space. No local finiteness or degree conclusion is established in this review.
REASON: Essential coverage for the unchanged saved target is now ready. A mathematical specialization can test the bound without reproving analytic GIT, analytic finiteness or general multiplicity theory; the universal Hodge and quaternionic/global existence gaps remain independent.
SCOPE: One chosen actual L101 family, audited L102 and L094 at the unchanged S,I,g,h,k,E; target a finite holomorphic germ onto its reduced image with generic degree at most two, without asserting that bound or degree one in advance.

## Purpose and test

The main gap remains universal primitive rational Hodge realization.
This intermediate target would measure local parameter identification at
the split fibre, a prerequisite for comparing an eventual compatible
family with a surface germ in a coarse moduli space. It is not global
separation for a hypothetical F and cannot establish quaternionic
integration or transport.

The proposed mechanism is the full effective C* representation's
invariant map, applied to the actual harmonic alpha(s,t), and local
analytic finiteness/multiplicity. The exact hypotheses of those tools
must first be checked. Continue only if source coverage supports testing
finiteness and the stated degree bound for every fixed analytic family
with the retained jet; if higher terms or quotient hypotheses prevent
that conclusion, identify the precise missing condition or a concrete
countertest. A first-jet calculation alone is not an actual fibre or
covering-degree computation. No such calculation or conclusion is
made in this proposed assessment.

The prior separation stop tested global tangent coincidence and a
relative-Hom first-order model. This target instead concerns the actual
local two-parameter family and its full-group invariant map. The parked
quaternionic integration route requires structure-preserving analytic
input; no such input is assumed here. Preserve those stops and all
unfinished work.

Essential local inputs are L094, L101 and L102. No common F, nonempty
reducible set in a global family, identification W=r(TB), quaternionic
map, smooth central unitary gauge, prescribed global mixed tensor,
reconstruction or transport is assumed. Matching Mathlib coverage is
not checked. The comparison below completes source coverage for this
same target; it supplies no new lemma or application to the actual germ.

## Inspected primary inputs

**Orbit comparison.** Nicholas Buchdahl and Georg Schumacher,
*Polystable bundles and representations of their automorphisms*,
Complex Manifolds 9 (2022), 78--113, DOI 10.1515/coma-2021-0131,
[published PDF](https://d-nb.info/1262812674/34), Corollary 4.9 p. 91.
For sufficiently small integrable harmonic slice parameters, bundle
isomorphism is exactly the Aut(E) orbit relation. Read its full proof,
the final injectivity paragraph of Corollary 4.6 p. 89 (arbitrary
isomorphisms become parallel for the reference connection and intertwine
harmonic parameters), and Corollary 4.8(2) pp. 90--91 for the reverse
implication. Compact Kähler and reference polystability are retained.
L101/L102 use this actual slice; their norm comparison and shrinking
must precede use of the criterion. The effective group must be the full
ratio character, not just a selected subgroup. No global F is involved.

**Analytic quotient.** Buchdahl--Schumacher, *An Analytic Application of
Geometric Invariant Theory*,
[2008.04625v3, 26 February 2021](https://arxiv.org/pdf/2008.04625v3),
Definition 1 pp. 4--5; Theorems 1--3 pp. 4--8, 5--6 p. 11, 8 p. 15.
A reductive linear action with a restricted invariant analytic zero locus
is saturated to a closed analytic subset. Its image in the affine GIT
quotient is analytic with the reduced structure; holomorphic functions
are invariant functions. Read saturation, minimum-norm compactness and
the general invariant-sheaf proof, which avoids assuming weak normality.
Theorem 6 applies to a polystable bundle on a fixed compact Kähler
manifold. L101's complete equations, not their quadratic truncation,
must provide the restricted zero locus. The ambient quotient need not
be smooth, and semi-properness of the ambient quotient is not finiteness
of our parameter map.

The sequel, *An Analytic Application of Geometric Invariant Theory II:
Coarse Moduli Spaces*, [2108.03255](https://arxiv.org/pdf/2108.03255),
Section 6, Theorem 1 pp. 15--16, gives coarse moduli with distinguished
topology **in the category of weakly normal spaces**. Read its category
qualification and proof outline: uniqueness uses generic filtrations
and extension on weakly normal spaces. It must not be invoked to identify
an ordinary reduced image scheme with its weak normalization. A next
proof should first state its concrete reduced analytic-GIT classifying
map; any passage to the weakly normal coarse space needs its natural
lift and birational degree comparison explicitly justified. No comparison
with an arbitrary algebraic Gieseker moduli germ is covered here.

**Finite analytic germs and degree.** David Mond and Juan J.
Nuño-Ballesteros, *Singularities of Mappings*, Grundlehren 357,
Springer (2020), DOI 10.1007/978-3-030-34440-5,
[primary back matter](https://link.springer.com/content/pdf/bbm:978-3-030-34440-5/1).
Theorem D.5 p. 522 equates module finiteness, finite central-fibre
colength, an isolated central fibre and a finite analytic representative.
Read its Nullstellensatz/module argument and local-parametrization
qualification. Theorem D.6 p. 523 makes the image analytic of equal
dimension, with kernel-ideal proof. Lemma D.2 p. 525 identifies generic
degree with the fraction-field degree for finite surjective irreducible
germs. Theorem D.7 and Corollaries D.6--D.8 pp. 526--527 concern maps
to a smooth equal-dimensional target: colength equals degree only for
Cohen--Macaulay source. They cannot identify colength with degree onto
our possibly singular image. Appendix C, Lemma C.1/Corollaries C.1/C.2
pp. 491--492, supplies Nakayama and the minimal-generator count; read
the proofs. The actual image must be reduced and irreducible before
using its fraction field.

**Finite-extension multiplicity.** Craig Huneke and Irena Swanson,
*Integral Closure of Ideals, Rings, and Modules*, LMS Lecture Note
Series 336, Cambridge (2006),
[author PDF, February 2023 revision](https://www.math.purdue.edu/~iswanso/book/SwansonHuneke.pdf),
Theorem 11.2.7 p. 228. For a finite extension of Noetherian local
domains A subset B, maximal-primary I and fraction fields K subset L,
the formula is
\[
 [L:K]e_A(I)=
 \sum_{Q\in\operatorname{Max}B,\ \dim B_Q=\dim A}
 [B/Q:A/\mathfrak m_A]e_{B_Q}(IB_Q).
\]
Read its generic-rank and semilocal length proof. In a local analytic
application, localness, equal dimension and residue field C must be
verified; no target Cohen--Macaulay hypothesis is needed. Proposition
11.2.9(1) p. 229 gives e(I^r;M)=r^(dim A)e(I;M), with its complete
Hilbert--Samuel proof; Example 11.1.11 p. 225 gives regular-ring
multiplicity one. These suffice to plan an independent multiplicity
check. The general multiplicity-one converse is unnecessary; no
unmixedness or image smoothness is silently assumed. No actual local
ideal, colength, multiplicity or degree is computed in this turn.

## Discovery, overlap and bounded continuation

Queries included `Buchdahl Schumacher local moduli polystable bundles
analytic quotient 2022 Corollary 4.9`, `holomorphic map germ finite
isolated zero fiber multiplicity degree local analytic algebra theorem`,
`finite analytic map degree image multiplicity projection multiplicity
product theorem`, `Mond Nuño Ballesteros Singularities Mappings pdf
Theorem D.5 multiplicity D.6`, and `Huneke Swanson Integral Closure
book pdf multiplicity 11.2.4`. Search snippets were discovery only.
Kleiman, [1507.08865](https://arxiv.org/pdf/1507.08865), Theorem 5 and
Remark 8, was read as an alternative finite-extension projection formula;
its Buchsbaum--Rim generality is unnecessary once the direct textbook
formula is available. The inspected matrix-singularity paper's Appendix
A.3.3 requires Cohen--Macaulay hypotheses and does not supply our bound;
it led to the directly inspected Mond--Nuño-Ballesteros appendix.
Dolgachev's torus-invariant chapter is an unread lead: inaccessible
author links were not treated as theorem evidence. There is no essential
source blocker, and no novelty inference from the search.

Audited L102 already fixes both nonzero weight projections and the full
effective action. No local degree conclusion occurs in the scoped prior
failure records. ATTEMPTS/046 tests global relative Hom; ATTEMPTS/061
tests necessary ASD quadratics; histories/261 and /265 park tangent
coincidence and an unevaluated curvature mechanism. None is reapplied
or erased. The saved integration/stability reviews remain adequate for
L094/L101/L102; the new reads address precisely the previously missing
quotient/finite-local-algebra coverage.

The approved mathematical difference is explicit invariant-coordinate
and local-ring work, not a reproof of the imported general theorems.
The monomial calculation is needed to identify the full quotient and
its pullback ideal; any proof must retain arbitrary convergent higher
coefficients using local algebra rather than treating the family as
its first jet. Compare the resulting generator/rank bound with the
finite-extension multiplicity formula to test the required degree at
most two. Continue if these checks establish the threshold for the
fixed actual family; otherwise record the failed hypothesis or actual
countertest. Do not infer degree one, a literal parameter involution,
quaternionic integration, global separation, a common F or transport.
This unchanged TARGET is now ready for a separate mathematical turn;
no newly invented mathematical target is approved and attempted here.
