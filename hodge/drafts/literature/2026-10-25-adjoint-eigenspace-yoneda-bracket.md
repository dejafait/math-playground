# Adjoint eigenspace Yoneda bracket — source comparison and parked test

TARGET: Test whether the quadratic adjoint Yoneda bracket vanishes between distinct eigenspaces of L163's actual K.
CHECKED: 2026-10-25
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 540 searched exact eigenspace/Yoneda, product-base Kuranishi, mixed-bracket and stronger deformation-decomposition terms; inspected the primary passages below and compared L116/L117/L163, ATTEMPTS/016,/069,/089,/090,/091 and the saved normal-curvature/formality assessments. No inspected theorem supplies the specified mixed-block vanishing.
SOURCE_EVIDENCE: Verbitsky alg-geom/9307008v1 (29 July 1993), Definition 6.2, Theorem 6.2 and Theorem 7.1 with the opening obstruction-equation proof, PDF pp. 21-22,25,27; Meazzini-Onorati 2204.04075v2 (26 July 2022), Remark 1.14, Section 1.2, Proposition 3.13, Question 3.15/Proposition 3.16 and Section 4.2/Theorem 4.3, pp. 7-8,16-17,19; their 2509.03180v1 (3 September 2025), Section 5.1, Definition 5.1/Remark 5.3, Theorem 5.5 and complete proof, p. 20; Bottini 2608.24860v1 (25 August 2026), Theorem 1.1 and Section 4 cases below. These supply formality/obstruction scope, not compatibility with the actual K.
COMPARISON: The 2025 theorem explicitly allows compact hyperkahler products and its trivial-twist case covers the ambient End(F) complex using L071's metric connection; irreducibility is therefore not the decisive blocker. Formality retains the cohomological bracket and provides no K-equivariance, multiplicative Leray splitting or mixed-eigenspace zero statement.
GAP: The actual map Sym^2 H -> H^2(X,End_0(F)) and its compatibility with K remain unevaluated. No source-covered discriminating test of these mixed blocks was identified; positivity, quadraticity and smooth surface-fibre moduli do not fill this gap.
REASON: Park the proposed mixed-eigenspace test by its stated continuation test. EXPLORE records completed bounded discovery, not an applicable vanishing theorem or authorization to repeat the spectral mechanism without new bracket-compatible input. No new mathematical result or script is produced.
SCOPE: Exactly L071/L116/L117/L163's hypothetical rank-two F on the identical marked K3 product with the common metric/triple, integral c_1=0 and ch=2-14e_1-21e_2-tau_D+62P; untwisted V=End_0(F), actual j,r,J,Phi_1,K, full W_0 and unknown t. No smoothness, unobstructedness, formality or moduli-product decomposition is assumed.

LITERATURE_REASON: The invocation-start REVIEW_REQUIRED target adds an actual quadratic bracket to the ready linear harmonic comparison; primary product-base formality and bracket scope were essential unread coverage. Reuse the existing linear and normal-curvature assessments rather than repeating their proofs.

## Invocation-start proposal (historical)

The following proposal is preserved. Step 540's source comparison below
supersedes its pending-approval instructions and parks this target.

### Exact proposed question and relevance

Use H=H^0(B,M_0) and L163's actual j_1:H -> H^1(X,V).
For distinct eigenvalues lambda and mu of the positive self-adjoint K,
let E_lambda and E_mu be their complex eigenspaces. The proposed
statement to assess is

    [j_1u,j_1v]=0 in H^2(X,V)
    for all u in E_lambda, v in E_mu, lambda != mu.

Here the bracket is the degree-one graded commutator induced by
composition of endomorphism-valued Dolbeault forms, equivalently the
polarization of the determinant-fixed quadratic Yoneda obstruction.
It is an actual cohomological map, not a freely assigned matrix or
an assumed obstruction equation. This document asserts no value
for that map and does not derive the displayed vanishing.

The main gap remains uniform primitive Hodge realization. A mixed-block
vanishing statement could separate parts of this hypothetical kernel's
quadratic deformation constraints; a failure could rule out that use
of the spectral restriction. Neither outcome by itself supplies a bound
on t, exclusion or existence of F, higher-order integrability, transport,
or algebraic realization. When t=0 or K has only one eigenvalue, this
particular mixed-eigenspace test is vacuous; no such spectrum is assumed.

### Separate approval obligations

Reuse the completed L163 audit and its harmonic/Serre sources. Search
the exact statement, stronger product-decomposition or deformation
results, standard terminology and counterexamples. Retrieve primary
theorem hypotheses and essential proof cases for the compact product
and parallel-real End_0(F) coefficient. Quadraticity/formality alone
must not be substituted for vanishing of specified mixed brackets.
Likewise two positive forms do not by themselves make K parallel on
a moduli space or a derivation of its deformation complex. Keep the
possibly obstructed global deformation space distinct from smooth
stable-bundle moduli on either surface.

The earlier normal-curvature assessment leaves pointwise brackets and
connection-dependent Green pairings uncontrolled. This proposal asks
first for a cohomological mixed-bracket statement; it authorizes no
return to those unevaluated analytic quantities. ATTEMPTS/016 concerns
two specific rotation sheaves and is not this rank-two adjoint input.
ATTEMPTS/069,/089,/090,/091 remain preserved in their stated scopes.
No new theorem, reproof, mathematical script, or approved calculation
is created here. Matching Mathlib coverage has not been checked.

Continue only if the separate source comparison imports the statement
or identifies a concrete, source-covered test of the actual bracket.
If available theorems merely give a quadratic local model, need an
irreducible base, or require uncontrolled bracket/Green data, record
that distinction and park this proposed mixed-block vanishing test.
Do not repeat the positive-operator audit or assign K eigenvalues.

## Completed comparison — step 540

2026-10-25. LITERATURE / EXPLORATION / REPRODUCTION; actual task
literature_comparison. The source comparison changes the route without
establishing the truth value of the displayed vanishing. No counterexample in the stated
rank-two K3-product family, exclusion of F, or progress beyond the sources
checked is claimed. The mathematical exploration counter is unchanged.

### Primary hypotheses and essential proof cases

1. M. Verbitsky, *Hyperholomorphic bundles over a hyperkahler manifold*,
   [alg-geom/9307008v1](https://arxiv.org/pdf/alg-geom/9307008v1),
   Definition 6.2/Theorem 6.2, PDF pp. 21-22, describes the stable local
   deformation germ by its Yoneda quadratic cone. In Theorem 7.1, p. 25,
   the harmonic input already satisfies the zero Yoneda-square condition;
   the proof starts with equation (7.3) and its quadratic recursion on
   p. 27. This constructs deformations conditional on the obstruction
   vanishing; it does not determine particular mixed brackets. The
   symbol K used for a local map on p. 26 is unrelated to L163's K.

2. F. Meazzini and C. Onorati, *Hyper-holomorphic connections on vector
   bundles on hyper-Kähler manifolds*, Math. Z. 303 (2023), article 17,
   DOI 10.1007/s00209-022-03176-4, primary version
   [2204.04075v2](https://arxiv.org/pdf/2204.04075v2),
   Remark 1.14/Section 1.2, pp. 7-8, distinguish formality from triviality
   of the cohomology bracket. Proposition 3.13, p. 16, verifies derivations
   for composition. Section 4.2 explicitly starts with an irreducible
   holomorphic symplectic base; Theorem 4.3, p. 19, derives associative
   formality from the two-differential lemma and that derivation property.
   Question 3.15/Proposition 3.16, pp. 16-17, cannot supply missing
   homotopy abelianity. These statements do not identify L163's K with
   any operation on the deformation complex.

3. Meazzini and Onorati, *Deformations of twisted sheaves and formality
   results*, [2509.03180v1](https://arxiv.org/html/2509.03180v1#S5),
   Section 5.1, Definition 5.1, Remark 5.3, Theorem 5.5 and its entire
   proof (PDF p. 20). The base is compact hyperkahler, defined by its
   metric and quaternionic triple; no irreducibility is imposed. A
   projectively hyperholomorphic locally free twisted bundle has formal
   endomorphism Dolbeault DG Lie algebra. The proof checks the derivation,
   two differential identities and strong differential lemma. The
   Hermitian/metric hypothesis is explicit.

   Applicability comparison: X has exactly the diagonal product triple
   and compact metric required; F is locally free, the twist is trivial,
   and L071 supplies the actual metric hyperholomorphic connection, hence
   the required projective connection. This avoids extending the 2022
   irreducible-base statement ourselves. It supplies the ambient End(F)
   formality framework, not the requested bracket value. The target uses
   its trace-free Lie coefficient, not the associative algebra End(V).
   No new trace-free formality proof, algebra splitting, or formal-chart
   compatibility with j, r, factor cups or K is asserted or needed for
   this stopping decision.

4. A. Bottini, *The tangent bundle of a generalized Kummer fourfold is
   obstructed*, [2608.24860v1](https://arxiv.org/html/2608.24860v1),
   25 August 2026, Theorem 1.1. The preprint gives a stable
   hyperholomorphic tangent bundle with a nonzero Yoneda square on a
   Kum_2-type fourfold. Inspected Section 4, Lemmas 4.1-4.2, Corollary
   4.3 and the final proof: a free-locus commutator calculation, detection
   on a complete abelian surface for a product abelian input, then twistor
   transport. The displayed commutator obstruction is trace-free.
   This is a source-reported obstruction example, not an independent
   audit of its transport argument. Its rank-four tangent bundle and
   irreducible base do not meet our rank-two K3-product hypotheses or
   specify two eigenvalues of our K. Thus it warns against inferring
   unobstructedness from hyperholomorphicity, and does not refute our
   narrower mixed-eigenspace statement.

### Discovery, duplicates and scope of the negative decision

Queries actually run included `hyperholomorphic bundles Yoneda bracket
eigenspaces Lefschetz operator formality product hyperkahler Meazzini
Onorati`, `"hyperholomorphic" "formality" "mixed" bracket`,
`"hyperholomorphic" "eigenspaces" "Yoneda"`, `hyperholomorphic
"product" "Kuranishi" bracket`, `"hyperholomorphic" "mixed" "bracket"
deformation`, `"Yoneda" "bracket" "eigenvalues" bundle`, and
`"hyperholomorphic" "symplectic forms" "decomposition" moduli product`.
No matching theorem was established; this is not a novelty claim or a
proof of nonimplication for every possible geometric input.

Reused `2026-10-14-equality-split-line-analytic-integration.md` and
`2026-10-14-equality-stable-normal-curvature-test.md` in this directory,
with the actual statements of L116/L117/L163. ATTEMPTS/016 concerns
different rotation sheaves; /069 retains a global cup entry; /089-/091
concern other spectrum, determinant and line-twisted sign mechanisms.
None evaluates this adjoint bracket. The normal-curvature source needs
pointwise brackets/Green pairings; we import neither those unknown values
nor a claimed obstruction. Surface-fibre smoothness supplies no smooth
moduli assumption on X.

Uninspected search leads include broader derived/standard-conjecture and
modular-sheaf results. They are not theorem coverage for this target and
are not grounds for extending the search indefinitely. The shell PDF
download failed DNS; the essential primary passages were readable through
web access, so this is no persistent source-access blocker.

The continuation threshold was an applicable mixed-block theorem or a
source-covered test of the actual bracket. Only the quadratic framework
and unevaluated bracket remain. Park this proposed test; reopening needs
specific geometric bracket compatibility with the actual K or evaluated
mixed-block data, not another formality search. L163 remains valid in its
audited scope. Mathlib coverage for the exact bracket/formality statement
was not checked; no absence is claimed. Deligne's Clay-hosted Hodge
statement, Section 1, p. 2, was rechecked and retains the rational smooth
projective target recorded in `foundations/01-target-and-scope.md`.

### Separate continuation, not approved here

The proposed replacement uses L116's actual projection to W_0, rather
than K eigenvalues: isolate the finite-support component of the adjoint
quadratic obstruction on the full global section space. Its exact target
and unresolved base-change/product obligations are in
`2026-10-25-adjoint-point-obstruction-projection.md`, with
REVIEW_REQUIRED. No value of that component is asserted in this turn.
