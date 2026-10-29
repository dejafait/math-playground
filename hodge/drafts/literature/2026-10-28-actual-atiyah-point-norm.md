# Actual Atiyah point norm — source-approved specialization

TARGET: Evaluate L175's actual point self-pairing using L168–L169's local duality coordinates, and test whether the k-line normal Gram coefficient can vanish for integer 1<=s<=782.
CHECKED: 2026-10-28
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 597 read complete L168/L169/L175 proofs and audits, L174's trace and Gram formulas, L176's complete comparison and audit, and relevant L177 and failure passages; reused the saved assessments and searched actual K3/Atiyah/Serre point pairings, normalized residue traces and Dolbeault-integral trace comparisons. No exact family-specific norm theorem or completed local evaluation was identified; no novelty is inferred.
SOURCE_EVIDENCE: Reuse the point-weight/uniform-weight-audit, actual-Serre-duality, first-factor-point and residual-rank assessments; freshly inspect Cox, Toric Residues, arXiv:alg-geom/9410017v1, Appendix A Proposition A.1 and complete proof, printed pp.19–20, and the Dolbeault comparison in Proposition 6.1, pp.14–15; Nayak–Sastry II arXiv:1903.01783v2, (4.1.2),(4.1.5), Section 5.2 and Proposition 5.2.3 with proof, pp.21–26; Stacks 0FVU Lemma 48.27.1(5),(7), corresponding proof cases, Remarks 48.27.2–3, and 0AX4. Details and version qualifications below.
COMPARISON: L168/L169 give the actual quotient form in fixed coordinates and L175 gives the specified vector through the same top map; Cox supplies the missing general algebraic-trace/Dolbeault-integral comparison, while Nayak–Sastry identifies the standard projective trace normalization. These tools cover the later scalar specialization, but none states its norm, the identification of the notebook's convention scalars, or the integer k-line test.
GAP: The later research turn must evaluate the fixed vector's coordinates, match the relative normalization and base-trace conventions with L174, and only then specialize L176 along the k-line using audited Dk=4k. No point norm, scalar identification, coefficient or nonvanishing is derived in this source review; a precise failed convention comparison is an admissible negative result.
REASON: Separate source comparison now approves exactly the unchanged TARGET as a later REPRODUCTION specialization. The new general trace-comparison input fills the uncovered source scope; general duality/residue results should be cited, with only the actual-coordinate and scalar application proved locally.
SCOPE: The same conditional identical marked K3 family, fixed forms/connection/full character, actual j,r,a,Q,R,T and point vector w_k; reduced nonempty Z for the scalar test, 1<=s<=782 and t<=46. Empty Z must be retained separately without introducing w_k. No metric preservation, section integrability, F existence or point norm is assumed.
LITERATURE_REASON: The new lead pairs L175's evaluated point vector with the earlier local-duality normalization; this scalar evaluation was explicitly outside the ready residual-rank and L177-audit scopes. Reuse their inspected sources and retrieve only essential missing theorem hypotheses or proof cases.

## Nomination and bounded next review

This section preserves step 596's pre-review proposal. Step 597's source
decision is recorded below; its mathematical test remains unperformed.

The completed step 596 is only the critical audit recorded in canonical
L177. The target above is future work, not mathematics attempted or
approved in that step. Its essential local inputs are L111, L116, L165,
L168, L169 and L174–L177. No cross-notebook result is proposed.

The main gap remains primitive realization, with F existence already
unresolved. The downstream use of this scalar is to remove an identified
unknown in L176's actual normal Gram identity, potentially testing a
degeneracy left by the fourteen-direction restriction. This supplies
neither an actual section quadric nor a lower square length by itself.

Read the relevant complete coordinate identities in L168/L169 and
L175, and compare their hypotheses and normalization with the saved
primary assessments before judging readiness. In particular the
coordinates of a bracket and of w_k cannot be identified by name alone.
The trace scalar gamma, residue/base-trace convention, common Atiyah
sign, chi_sigma normalization and actual top-base-change map must all
be retained. Uniform weights in one coordinate system do not by
themselves evaluate this vector's norm in another.

After separate approval, the bounded mathematical test would evaluate
Q_U(w_k,w_k) in the same normalization as L174's Gram form and check
L176's restriction to phi^{-1}(C k), with L177's audited Dk=4k. It must
distinguish an exact scalar formula from mere nondegeneracy of Q_U;
a nonzero vector can be isotropic over C. Continue only with a verified
coefficient or a precise obstruction to determining it. If an essential
source or comparison stays blocked, park that dependent scalar test and
nominate an independently testable target rather than repeating it.

Preserve ATTEMPTS/068,/092–095. In particular ATTEMPTS/093 permits
pointwise isotropic lifts when the complementary vector is unrestricted;
it does not evaluate the prescribed vector w_k. The new test proposes
to evaluate that fixed input, not to rerun unrestricted scalar isotropy.
No division by its unknown self-pairing is allowed. Radical images,
section quadrics, minimum square length and all existence questions
remain independent unresolved data.

Route the next invocation to literature_comparison, standard/high.
This is source comparison for a potential established-route
specialization, not a new creative mechanism. A justified creative
section-bracket test remains blocked by the lack of an independently
evaluable section image or geometric lower-square-length constraint;
do not relabel this normalization problem to meet a routing preference.

## Completed source comparison — step 597

2026-10-28. LITERATURE / EXPLORATION / REPRODUCTION; actual task
literature_comparison. Approve exactly TARGET as SPECIALIZE for a
separate research invocation. This is source readiness, not a
mathematical evaluation or an advance beyond the inspected sources.

### Inspected primary inputs and applicability

David A. Cox, *Toric Residues*,
[arXiv:alg-geom/9410017v1, 19 October 1994](https://arxiv.org/pdf/alg-geom/9410017v1#page=19),
Appendix A, Proposition A.1, printed pp.19–20, states for a compact
orbifold variety of dimension n that the algebraic trace of a class
represented by eta under its Dolbeault isomorphism equals
(-1/(2 pi i))^n integral eta. Read its complete proof: normalization
on the projective-space generator followed by its explicit integral.
Read the connecting-map convention and relevant comparison proof in
Proposition 6.1, pp.14–15; one Cech identity is stated without proof
there. Appendix A does not impose the main text's toric hypothesis.
The smooth projective surface B is a compact orbifold with trivial
local groups, so its scope applies. This is a general trace input,
not the desired fixed-vector evaluation. Import it rather than
recompute its integral. The published 1996 PDF was opened but its
Appendix retrieval timed out; citations here use the inspected v1.

Nayak–Sastry, *Grothendieck Duality and Transitivity II*,
[arXiv:1903.01783v2](https://arxiv.org/pdf/1903.01783v2#page=24),
Section 5.2 and Proposition 5.2.3 with complete proof, printed pp.24–26,
identify the Verdier trace on relative projective space with the
standard trace, normalized on the displayed ordered Cech generator.
Read (4.1.2),(4.1.5), pp.21–22, comparing supported residue and proper
trace. Reuse the already inspected regular-section normalization,
Remark 5.3.3/Theorem 5.4.2, and I's oriented Ext/fraction comparison.
The May 29 author PDF opened, but subsequent targeted requests timed
out; this fresh inspection uses the explicitly March-dated arXiv v2,
without asserting version identity. No essential source is blocked.
For B over C, proper smooth duality applies; each reduced point is
a section over Spec C, with a regular parameter ideal on the surface.
Finite flatness is over C, not over B.

[Stacks 0FVU](https://stacks.math.columbia.edu/tag/0FVU), Lemma
48.27.1(5),(7) and their proof cases, and Remarks 48.27.2–3 were
read live: the pairing is functorial composition followed by the fixed
trace, with shifts respected. Bounded coherent inputs give finite
dimensional perfect pairings. [0AX4](https://stacks.math.columbia.edu/tag/0AX4)
identifies finite trace with evaluation at one for dualizing complexes
normalized over the same base. Reuse the previously inspected relative
and composite-counit coverage, not a fresh proof of duality. Here C is
perfect, V locally free and trace-self-dual, M locally free, and W
finite supported; none of this treats W as locally free on B.

The precise rational target was rechecked in Deligne,
[Clay-hosted statement, Section 1, p.2](https://www.claymath.org/wp-content/uploads/2022/06/hodge.pdf#page=2).
It remains rational cycle realization on smooth projective complex
varieties. This scalar specialization is far short of that target.

### Exact remaining application, duplicates and stopping test

L168's complete proof/audit identifies the quotient adjoint and the
finite-support form; L169's complete proof/audit supplies its common
weight with an explicit base-trace convention scalar. L175's complete
proof/audit specifies w_k through theta_z and the labelled diagonal
generator. These refer to the same top map and fixed trace coordinate,
not to unspecified bases of isomorphic lines. L174 fixes a relative
normalization and defines its scalar gamma by an integral. L176 retains
the norm-dependent rank-one term. L177's audited Dk=4k is already
available for the k-line restriction; its proof need not be repeated.

A later proof must distinguish L174's scalar gamma from L168's sheaf
isomorphism also named gamma. It must specialize the common relative
kappa to L174's actual relative pairing, compare the base trace with
L169's chi_B and Verdier convention using the inspected trace inputs,
and retain the fibre normalization of chi_sigma and Tr(h_0^2)=2.
Cox's sign and Dolbeault convention must be compared with the
notebook's cup/totalization convention; naming two maps 'trace' is
insufficient. No scalar equality is asserted here. These are covered
specialization obligations rather than missing general theorems.
A mismatch must be exhibited, not repaired by an independent point
rescaling. There is no license to replace actual theta_z, omit lower
Tor terms, insert a Hermitian norm, or divide by an unknown self-pairing.

Then, and only then, evaluate the prescribed point vector and use
L176's exact Gram identity on phi^{-1}(C k), with L174's nonzero common
trace scalar and L177's fixed eigenline. Test allowed integer
1<=s<=782 exactly, retaining the root's defining polynomial and
isolating interval. Do not infer a new rank bound merely from a map
having rank one or from a nonzero vector in a nondegenerate complex
bilinear space. Empty Z is a separate zero-space case without w_k.
No integer or coefficient calculation has been performed here.

The duplicate screen reused the prior assessments, history/563,/588,
/596 and ATTEMPTS/093 and inspected the exact unknown-norm passages
in L176/L177. No completed fixed-vector norm evaluation was found
there. ATTEMPTS/093 adjusts an unrestricted complementary lift and
therefore does not answer this prescribed-vector question. Preserve
the section-image, cyclicity and metric-comparison stops of /092–095;
this test supplies none of their missing section or geometric data.

External searches included `"K3" "Atiyah" "point" "Serre" pairing
norm`, `"Grothendieck Duality and Transitivity II" "5.4.2"`,
`"Serre duality" "integration" "Grothendieck residue" "2 pi"`,
`"Verdier" "Dolbeault" "trace"`, and focused follow-ups for Cox's
Appendix A. Search results on analytic Serre duality, lecture notes,
MathOverflow and secondary copies were discovery leads, not theorem
inputs; no family-specific exact or stronger theorem was identified.
The inspected primary arXiv text, not a search snippet, supports the
new trace input. No novelty claim follows from the bounded search.

Continue only with an exact norm/normalization comparison and a
verified integer test, or a precise obstruction showing why these
inputs do not determine it. A surviving essential mismatch parks the
scalar-dependent strengthening; it does not undo L176/L177 or disprove
F. Actual section quadrics, their minimum square length, radical
images, F existence, transport and uniform primitive realization remain
independent gaps. The plausible downstream use is to decide whether the
remaining k-line supplies an additional normal Gram direction; it does
not establish a geometric section bracket or any exclusion in advance.

Full matching Mathlib coverage of this geometric trace/norm comparison
is not checked. Supporting rank declarations retain the precise names
and revisions in the residual-rank assessment; unknown coverage is not
absence. No cross-notebook input is used. No new lemma, mathematical
script, DAG edge or PROOF change is made. Next routing is
calculation/standard/high for this established-route specialization.
A justified creative bracket mechanism remains blocked by the absence
of an evaluable section image or independent geometric lower-square-
length input; normalization must not be relabelled creative.
