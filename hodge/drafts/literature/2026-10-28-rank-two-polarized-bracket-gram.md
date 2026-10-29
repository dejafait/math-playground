# Rank-two polarized bracket Gram test — completed source comparison

TARGET: Test whether the polarized rank-two trace identity and L163's actual factor cup forms force the section-bracket Serre Gram rank above 816 at s=781,t=46.
CHECKED: 2026-10-28
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 605 searched ordinary traceless 2-by-2 four-trace identities, Procesi/Razmyslov trace algebra, graded endomorphism Dolbeault brackets and hyperholomorphic Gram bounds; inspected the primary passages below and the scoped local duplicate/failure screen. No inspected theorem supplies the endpoint rank verdict; this is not novelty evidence.
SOURCE_EVIDENCE: Procesi, Adv. Math. 19 (1976), Section 4, Corollary 4.4(c) with proof and Theorem 4.6 with multilinearization proof, pp.319-323; Vasyutkin–Chupakhin, J. Appl. Ind. Math. 16 (2022), Section 2, equations (1),(4), Assertion 1 with proof and traceless display following (6), pp.357-359; Lepri–Manetti 2102.05016v3 (22 May 2021), Section 2 product/commutator and differential check, pp.3-4, Lemma 2.6/proof, Definition 3.1/(3.2), Example 3.3, pp.6-8. Reuse the three harmonic/actual-cup/semiregularity assessments named below.
COMPARISON: Ordinary polarized trace multiplication and the graded composition/trace framework are covered. L163 supplies the actual two positive forms and common R. None supplies their combined bracket Gram bound; the graded four-input specialization, scalar-cup comparison and rank calculation are the bounded mathematical obligations. F-valued determinant tests and scalar cyclicity do not answer them.
GAP: Determine the exact signed four-input bracket pairing and its rank after transport through L163's actual cups; compare with 816 without assuming harmonicity of products or a multiplicative Leray splitting. No graded quartic formula or rank bound is established by this literature turn.
REASON: Essential tools are accessible and match the locally free rank-two coefficient and fixed common metric. Approve one separate mathematical attempt on unchanged TARGET, stopping on a compatible countermodel or an unsupported comparison rather than repeating L179's finite checklist.
SCOPE: Same conditional identical-marked-K3 family, fixed common metric/triple/forms/connection, locally free product-polystable rank-two F, integral c_1=0 and full ch=2-14e_1-21e_2-tau_D+62P; untwisted V=End_0(F), actual j,r,a and trace maps, reduced split set, s=781,t=46. No independently chosen Hermitian form, factor harmonic action, metric/Leray compatibility or section integrability is allowed.
LITERATURE_REASON: The changed target adds rank-two polarized trace multiplication beyond the finite checklist; this separate review supplies its previously missing primary identity and graded-composition coverage, while reusing adequate harmonic coverage.

## Original nomination — step 604 (preserved)

The completed step-605 review below supersedes this nomination's
REVIEW_REQUIRED gate and prospective source instructions. It approves
the unchanged mathematical test, without performing that test.

### Purpose and separate gate

This file is only the continuation nomination after step 604's completed
L179 audit. Its next invocation is literature-only: compare primary
theorem statements and necessary proof cases before approving any
calculation. Do not derive the proposed trace identity or rank bound
during that source turn. Preserve TARGET as the mathematical test while
assessing it. The audit's outcome is independent of this new nomination.

The main gap remains uniform primitive realization and existence of F.
This intermediate target asks for a necessary global bracket constraint
which L179 deliberately does not model. The bounded threshold is a
Serre Gram-rank lower bound strictly greater than 816 for the actual
map Sym^2 H -> H^2(X,V) at t=46. Such a bound, if later established,
would contradict that endpoint's ambient dimension; failure to reach
it would not exclude F. Neither that lower bound nor any weakening is
asserted here. Other s,t, stable types, transport and general primitive
cycle realization remain independent gaps.

Essential local inputs are L071,L116,L117,L163,L165,L173,L177,L178,L179.
L116 identifies H with actual H^1(X,V) and gives the obstruction-space
dimension; L163 fixes its actual quaternionic operator, both factor
trace forms and their comparison. L165 fixes the Serre form, and
L173/L177 specify the bracket/Atiyah constraints already retained.
L178 supplies the conditional endpoint, while L179 records the exact
finite witness and its omissions. Read only the relevant canonical
passages. No cross-notebook theorem is needed.

## Duplicate and failure boundary

The local screen used the exact trace-identity terms above in
`ATTEMPTS/` and `drafts/literature/`, and read the L163 statement with
its ready harmonic assessment. It found the earlier
`2026-10-11-common-kernel-determinant-cup-square.md` and
`2026-10-24-four-twist-determinant-cup-comparison.md` as comparisons,
not coverage for the changed adjoint trace problem. The next source
review should check their relevant failures before claiming a new
mechanism. An unsuccessful keyword search is no novelty evidence.

Preserve ATTEMPTS/092–096. This is not scalar-isotropy-only exclusion,
cyclicity-only vanishing, a stabilizer-invariance assumption or a claim
that a metric star preserves the Leray splitting. L179's model even
has zero pairings between all its bracket coefficient vectors. That
is a feature of that model, not a consequence proved for every actual
bracket by the old checklist. Merely ruling out that one feature would
not exclude all endpoint data; the proposed decisive test is the
actual Gram rank versus the ambient dimension.

## Approval and abandonment test

Assess the precise trace algebra for traceless rank-two endomorphisms,
its specialization to endomorphism-valued degree-one Dolbeault forms,
and its transport through actual cup products and the fixed Serre trace.
Reuse L163's assessed harmonic facts rather than assign a positive form
or assume independent factor rotations. Distinguish the scalar-valued
trace cups from the trace-free unhalved brackets throughout. Generic
matrix identities, diagonal cyclicity, or a trace formula without its
graded signs are insufficient source coverage.

Approve a later mathematical attempt only if these sources give a
well-defined comparison for pairings between different actual brackets
and a bounded rank test. If the proposal only recovers already imposed
cyclicity, depends on unsupported metric/Leray compatibility, or has no
usable rank comparison, record that limitation and park this mechanism.
If an essential source remains blocked, change to an independent target
under the recovery rules; do not repeat the finite witness test.

After adequate source comparison, the proposed mathematical attempt is
creative in purpose: a new combination of rank-two multiplication with
the actual factor forms, aimed at a central conditional existence gap.
The precise obstruction is the endpoint's 816-dimensional obstruction
space; the bounded test is an actual bracket Gram rank exceeding 816
or a compatible countermodel to that implication. This is prospective
routing only; current next-turn routing is literature_comparison,
standard/high. Matching Mathlib coverage is not checked.

## Completed review — step 605, 2026-10-28

LITERATURE / literature_comparison / EXPLORATION / REPRODUCTION.
This changes source readiness, not the mathematical argument or bounds.
No lemma, mathematical script, DAG edge or PROOF.md change is made.

### Inspected primary statements and proof cases

C. Procesi, *The invariant theory of n x n matrices*, Advances in
Mathematics **19** (1976), 306–381,
[primary paper, Section 4](https://abrochier.org/m2/Procesi.pdf#page=14):
the setup is ordinary matrices over a characteristic-zero field, with
commuting scalar trace polynomials. Corollary 4.4(c), pp.319–320,
identifies the multilinear concomitant identity with polarized
Cayley–Hamilton; its proof checks the characteristic polynomial and
leading term. Theorem 4.6 and its proof, pp.322–323, give generation
by Cayley–Hamilton and explain multilinearization via substitutions.
These are ordinary coefficient identities, not a theorem allowing
ungraded substitution of odd differential forms. Use them by citation;
no reproof of invariant theory is needed. Their generation statement
does not imply that the notebook's cohomology algebra is realized.

S. A. Vasyutkin and A. P. Chupakhin, *Constructing a Minimal Basis of
Invariants for Differential Algebra of 2 x 2 Matrices*, Journal of Applied
and Industrial Mathematics **16** (2022), 356–364,
[DOI 10.1134/S1990478922020156](https://doi.org/10.1134/S1990478922020156),
[author-uploaded primary text](https://www.researchgate.net/publication/365419265_Constructing_a_Minimal_Basis_of_Invariants_for_Differential_Algebra_of_2times_2_Matrices).
Read Section 2, pp.357–359: equations (1),(4), the full three-matrix
Assertion 1 proof and the traceless display after (6). For ordinary
traceless complex matrices the latter explicitly states

    2 tr(abcd) = tr(ab)tr(cd) + tr(ad)tr(bc) - tr(ac)tr(bd).

Equation (4) is polarized Cayley–Hamilton; the proof applies it in
successive matrix orders. This supplies an explicit coefficient formula,
not a graded Dolbeault formula. Its differential-algebra conclusions
are unnecessary. The source credits Sibirskii (1968); that paper's
MathNet bibliographic record was opened, but its proof was not read.
Do not attribute an inspected theorem number to Sibirskii.

E. Lepri and M. Manetti, *Connections and L-infinity liftings of
semiregularity maps*,
[arXiv:2102.05016v3](https://arxiv.org/pdf/2102.05016v3#page=3),
22 May 2021. Read Section 2's finite locally free complex setup,
total-degree convention, composition and commutator formulas and
the differential calculation (2.1), pp.3–4; Lemma 2.6 with its full
local-frame trace calculation, pp.6–7; Definition 3.1, extension
formula and Leibniz rule (3.2), p.7; Example 3.3, p.8. These cover
the Koszul product, graded trace and cyclic coefficient form. Apply
the setup to F concentrated in internal degree zero. Dolbeault degree
still contributes to total degree. The coefficient trace is ordinary
matrix trace in that case; the graded form extension retains exterior
signs. No flatness or integrability of a deformation is required.
The source does not evaluate this product's bracket Gram rank.

These sources together cover tools for a *later* coefficient-by-coefficient
specialization. We have not derived that specialization here. In
particular the ordinary four-trace display must not be copied as an
identity of four odd matrix-valued forms without the Koszul calculation.

### Reused coverage and actual-map boundary

Reuse `2026-10-25-adjoint-factor-cup-sign.md` and
`2026-10-25-adjoint-factor-cup-critical-audit.md` for Verbitsky's
parallel-real harmonic action, Demailly's coefficient Dolbeault/Serre
integration and the actual-cup comparison. L163 was read in full,
including its separate audit: it fixes R, the common normalization,
both strictly positive Q_i when t>0, and Q_1=Q_2(K-,-).
This does not assert that R is a chain-level algebra map or that a
product of harmonic representatives is harmonic.

Reuse `2026-10-27-two-factor-semiregularity-point-quartic.md` for
Buchweitz–Flenner's commutator theorem, actual duality and quadratic-form
tools. Its full-cotangent source comparison was read; no new higher
semiregularity component is requested. Read L116/L117's endpoint
identifications, L165's actual Serre form/decomposition and L179's
precise finite checklist. Here H is the actual H^1(X,V), E is the
actual H^2(X,V), and brackets must be transported by the actual j_1.
L116 gives dim E=724+2t, hence the saved endpoint threshold 816.
This dimension is reused, not a new calculation. W and both actual
trace conventions remain in force throughout.

The scalar degree-two trace cups and their products are to be compared
on X before any Leray interpretation. L163's actual factor forms are
the allowed measurements. Neither partial-factor harmonicity nor a
metric-compatible Leray splitting is an imported hypothesis. Thus
ATTEMPTS/095 remains intact and is not an essential source blocker for
this direct global-cup test.

### Discovery, duplicates and limits

External queries included `traceless 2x2 matrices trace ABCD identity
invariant theory Procesi`, `Procesi invariant theory n by n matrices
1976 trace identities pdf`, `Manetti differential graded Lie algebra
Dolbeault endomorphism forms bracket trace graded cyclic`, quoted
`2tr abcd`, and combinations of `trace`, `bracket`, `Gram` and
`hyperholomorphic`. The three primary texts above were inspected;
search snippets alone were not used as theorem evidence. Procesi's
1984 *Computing with 2 x 2 matrices*, Berele's Grassmann-matrix
invariant theory and Drensky's survey remain unread leads, not inputs.
No essential theorem was located only behind one of those leads.
The already assessed Charles irreducible-base moduli theorem does
not supply a product-case rank bound. No full matching endpoint result
was identified in this bounded search; originality is unverified.

A scoped search of `ATTEMPTS/` and `drafts/literature/` used Fierz,
Cayley–Hamilton, polarized trace, traceless matrices, rank-two trace
and bracket Gram terms. Read the relevant saved determinant assessments
and ATTEMPTS/057,/090,/094,/095,/096. The first two concern determinant
cups with F coefficients and different branches. The cyclicity stop
does not evaluate pairings between distinct brackets; the metric stop
prohibits an unsupported splitting comparison; L179 realizes only
its stated finite constraints. These are failure boundaries, not
duplicate coverage of the new trace-free multiplication test.

### Approved bounded attempt and stopping evidence

DECISION SPECIALIZE covers exactly TARGET with the existing scope.
Source tools are ready; the following are mathematical obligations
for the next invocation, not results of this review:

1. Expand four actual degree-one representatives in local holomorphic
   frames, applying the cited ordinary matrix identity only to their
   degree-zero coefficients. Track every exterior permutation and
   the unhalved bracket, including repeated inputs. Show the resulting
   traced expression descends to actual cohomology.
2. Compare its scalar cups with both actual factor forms using L163's
   single R and normalization. Justify all spectral or polarization
   arguments used; do not assign a convenient K or factor form.
3. Determine the resulting Serre Gram rank on Sym^2 H at t=46.
   Continue toward endpoint exclusion only with a justified lower bound
   strictly greater than 816. A compatible countermodel to the claimed
   implication, a failure to exceed 816, or dependence on unsupported
   compatibility stops this bounded mechanism. A formula yielding only
   old cyclicity does not count as the sought bound.

Ruling out L179's particular coefficient-isotropic construction is
insufficient: the rank assertion must hold for every actual datum
under the stated hypotheses. No result is asserted for other s,t,
other stable decompositions, transport or general Hodge realization.
No new lemma or reproof has been approved as an established fact.
Full matching Mathlib coverage has not been checked; this is not
evidence of absence. The next task is a creative proof attempt combining
these assessed tools, with the endpoint ambient rank as its bounded
test; this source turn claims no progress beyond those tools.
