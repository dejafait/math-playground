# Degree-only total opposite normalization defect — source comparison

TARGET: Test whether L129's local length estimate and L140's ordered-count bound give a degree-only total normalization-defect bound sharper than L138.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the ready arbitrary-branch and projection assessments; searched surface normalization-length/multiple-point bounds and higher-dimensional delta invariants; inspected Fulton (1978) Theorem 2/Remark 2.4 and Greuel--Pfister arXiv:2107.07012 Definition 6/Theorem 35; scoped local searches found no completed L129/L140 aggregation.
SOURCE_EVIDENCE: Canonical L129 including its audit, L138 finite-support/polynomial proof, L139 count identity and L140 hypotheses/conclusion were read; Stacks 04DG and 0AYT statements and complete proofs were read online; saved primary arrangement and Fulton residual coverage is reused as detailed below.
COMPARISON: Known tools and audited local results cover the normalization quotient, finite sum of lengths and ordered count; inspected conductor and semicontinuity results do not supply the proposed uniform count-to-defect comparison. No matching combined theorem was identified, without a novelty claim.
GAP: A later mathematical step must give an explicit finite-sum bound using L129/L139/L140, eliminate unknown fibre sizes, and compare it with L138 for every admissible fixed parameter set, including empty collisions; no such calculation is performed here.
REASON: Essential coverage is sufficient for one bounded specialization of existing local results and elementary finite-sum inequalities; no general theorem needs reproof and no extra geometric restriction on fibres is authorized.
SCOPE: Exact TARGET under unchanged L071/L118 assumptions, L120 normalization, L121 reduced ordered scheme, L129 local bound, L137 fixed degree, L138 finite support/threshold, L139 fibre-sum identity and audited L140 count; arbitrary finite fibre partitions and the empty case.
LITERATURE_REASON: First source comparison for the newly registered global aggregation target; existing ready assessments cover its local and projection inputs but not this combined scope.

## Proposed scope, not a mathematical conclusion

The main gap is universal primitive rational Hodge realization. F
existence and a contradictory lower count or defect estimate remain
independent gaps. The proposed intermediate target is an upper bound
for the original total normalization length depending on L137's degree
delta alone, to be compared explicitly with L138's ambient-dimension
dependent bound. A better defect threshold could support a later
comparison using the original image's Euler characteristic. It would
still supply only upper control, not an exclusion or existence theorem.

Essential inputs are L120's actual normalization, L121's finite reduced
ordered coincidences, L129's full local length estimate, L137's original
fixed embedding and degree, L138's finite support and saved threshold,
L139's ordered fibre count, and audited L140's projection bound.
The full hypothetical L071/L118 assumptions remain: identical marked
K3 factors, common metric, actual locally free Omega-polystable rank-two
F with integral c_1=0 and ch_2=-14e_1-21e_2-tau_D. No existence of F or
collisions, minimal gluing, normality/CM, coherent vanishing, effective
values of the projective choices, or lower estimate may be assumed.

The source review should retrieve the exact ready local-defect
assessment and canonical L129, rather than rederive its branch
linearization or arrangement calculation. It should verify the
finite-support passage and distinguish an upper estimate for each
actual local quotient from sharpness among flat model arrangements.
Preserve ATTEMPTS/070,073,078; their failures concern respectively
minimal gluing, automatic coherent vanishing and the uncontrolled
ordinary middle-Hom Euler term. None is a proposed input.

Continue only if the checked sources and unchanged hypotheses permit
a concrete finite-sum comparison retaining every fibre size and zero
collisions. The later mathematical test should state the actual bound
and compare it with L138's required threshold for every admissible
fixed parameter set. Park this aggregation if it adds no better
control or needs an unsupported geometric restriction on fibre sizes.
Do not infer actual attainment from any extremal integer partition.

No combined formula, new lemma or calculation has been produced in
this registration, and no readiness decision is claimed. Full matching
Mathlib coverage for the proposed combination is not checked.

## Completed review — step 440, 2026-10-20

The preceding registration records the pre-review state. This section
approves the exact TARGET for a subsequent research turn; it establishes
no combined inequality. The main gap, possible downstream Euler use,
conditional assumptions and continuation/abandonment test above remain
unchanged.

### Reused canonical results and hypotheses

The complete L129 proof and its separate step-391 audit were read.
Its estimate concerns the entire algebraic stalk Q_z, not just a tangent
jet or a conductor. It applies to the entire r-preimage fibre for every
r>=1 and every tangent span; sharpness among formal flat arrangements
does not assert an actual K3 collision. Reuse the SPECIALIZE assessment
`2026-10-18-arbitrary-branch-sharp-normalization-defect.md`, including its
inspected Stacks 01QX union exactness and 00MA exact-completion inputs.
Neither its arrangement calculation nor branch linearization needs
reproof for the proposed aggregation.

L138's finite-support and polynomial-comparison proof was read through
its fixed-parameter substitution. Its Q is supported only at the finite
multiple-value set, and its threshold is
U=2+delta/2+(3/2)delta^(N-2)(delta(delta+1)/2)^4.
It retains N>=3 and delta>=8. These restrictions follow in that canonical
proof from the original image embedding and the integral K3 ample
square; they are comparison inputs, not new conclusions of this review.

L139's statement identifies P with the sum of r_z(r_z-1) over the
original multiple-value set, using L121's actual reduced ordered scheme.
L140's hypotheses and conclusion retain exactly that P, not a count
of singular values or unordered pairs. Its upper bound is
(delta-4)(delta-6), with L137's same degree. Reuse the completed
`2026-10-20-opposite-projection-double-point-bound.md` and
`2026-10-20-opposite-projection-count-critical-audit.md` assessments and
step 439's audit verdict. No projection or residual proof is repeated.

### Exact primary bridge imports

[Stacks, Lemma 41.7.3, tag 04DG](https://stacks.math.columbia.edu/tag/04DG),
statement and entire proof as served 2026-10-20, requires a finite
unramified map, a singleton fibre and a purely inseparable residue
extension. It gives a closed immersion near that value. Over C the
closed-point residue extension is trivial; L138 uses the normalization
injection to obtain local equality. The finite-module Nakayama proof
does not require a normal target.

[Stacks, Lemma 33.33.3, tag 0AYT](https://stacks.math.columbia.edu/tag/0AYT),
statement and entire proof as served 2026-10-20, applies to a coherent
sheaf with zero-dimensional support on a proper scheme over a field.
Global sections are the direct sum of its stalks and higher cohomology
vanishes. Its proof uses the scheme-theoretic support's decomposition
into Artinian local spectra. Here Z is projective and L138 supplies the
support condition; all residue fields are C. This justifies reusing the
sum of local lengths, including a zero sheaf, without a vanishing
assumption on O_Z. General sheaf or normalization results need no reproof.

### Multiple-point and stronger-result screen

[Fulton, *A note on residual intersections and the double point formula*,
Acta Math. 140 (1978), 93–101](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6234-11511_2006_Article_BF02392305.pdf),
Theorem 2 and Remark 2.4, printed pp. 94–96, were inspected again for
this comparison. The residual must have expected codimension. The
three-plane example distinguishes conductor degree nine from ordered
double-point degree six. Theorem 3's conductor identity concerns a
curve mapping birationally to a surface. Neither result identifies the
normalization quotient here with a double-point or conductor cycle.
L140's separately covered source residual remains the applicable count
input; the proposed defect comparison must instead use L129.

[Greuel--Pfister, *The Delta Invariant and Simultaneous Normalization
for Families of Isolated Non-Normal Singularities*,
arXiv:2107.07012](https://arxiv.org/pdf/2107.07012), inspected 26-page
arXiv PDF, Definition 6, printed p. 5, and Theorem 35 with its proof,
printed p. 23, cover higher-dimensional isolated nonnormality.
Definition 6 agrees with normalization-quotient dimension for a reduced
positive-dimensional local ring. Theorem 35 assumes a flat map of
characteristic-zero k-algebras from a PID, a finite-type k-algebra,
finiteness over the base of its specified normalization kernel and
cokernel, and finitely many nonnormal points in the relevant fibres.
Its conclusion compares defects under specialization; the proof invokes
the earlier algebraic comparison and generic regularity. No such flat
deformation is supplied here, and it is not a degree/ordered-count bound.
This is a scope comparison only; that theorem is not imported as an
inequality for Z. The failed journal-PDF request was replaced by the
accessible arXiv text, so it is not an essential blocker. The journal
version is an unread version, not silently identified with this PDF's
numbering.

The saved arrangement assessment already screens Derksen--Sidman
regularity, Derksen's transversal-series scope and skew lines on a
quadric. Those do not add a global count-to-defect theorem. No stronger
applicable combined result was identified in this bounded search.
Search failure is not evidence of originality. Curve genus formulas,
normal surface singularity invariants and unrelated numerical-search
hits are not theorem inputs.

Queries included `surface normalization defect length multiple points r
branches double point formula upper bound`; `normalization delta invariant
isolated surface singularity union planes binomial branches double points`;
`Fulton residual intersections double point formula Remark 2.4 conductor
three planes`; `"normalization" "length" "multiple points" "surface" bound`;
and `"delta invariant" "branches" "higher dimensional" inequality`.
Relevant primary statements were retrieved rather than treating search
snippets as evidence.

### Duplicate/failure check and approved mathematical difference

The scoped search of `history/430–439` and
`drafts/literature/2026-10-20-*` found the registered target and earlier
degree/Hilbert and projection assessments, not a completed aggregation.
The three named ATTEMPTS files were read. ATTEMPTS/070 rejects minimal
gluing, ATTEMPTS/073 parks automatic coherent vanishing, and ATTEMPTS/078
parks an uncontrolled ordinary middle-Hom Euler term. None is reopened
or used as a premise. Existing unfinished work is preserved.

The approved difference is elementary finite-sum control of L129's
known local estimate using L139's count identity and L140's count upper
bound, followed by a symbolic comparison with L138's U. A later proof
must explicitly control every finite fibre size from the available
count, preserve all fibres and the empty case, and state a bound solely
in delta. It need not claim an optimal integer partition or actual
attainment. If the result fails to improve U for some admissible fixed
parameters, record that limitation or failure; do not impose double-only
fibres, generic arrangements, minimal gluing or collision existence to
obtain a favorable comparison. No new general theorem or reproof of
the imported tools is warranted.

This is sufficient coverage for one separate RESEARCH attempt on the
unchanged TARGET, classified REPRODUCTION unless its exact result
requires a further uncovered mechanism. No combined formula, mathematical
script, lemma or mathematical advance beyond these sources is asserted
in this literature turn. Essential continuation input IDs are L120,
L121, L129, L137, L138, L139 and L140; retain the full hypothetical
L071/L118 F assumptions stated above. F existence, a contradictory
lower defect/count and universal primitive Hodge realization remain
unresolved. Full matching Mathlib coverage is not checked.
