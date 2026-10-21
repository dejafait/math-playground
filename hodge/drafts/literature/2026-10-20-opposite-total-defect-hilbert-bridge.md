# Opposite total defect — completed bridge source review

TARGET: Assess the finite-support and Hilbert-constant bridges needed to turn L137's fixed embedding and Hoa's bounds into a total normalization-defect bound.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the ready Hoa/determinant assessment; searched Stacks for finite unramified singleton-fibre closed immersion and Hilbert polynomial/Euler characteristic, then read the primary statements and relevant proofs below. Compared L120/L121/L137 and ATTEMPTS/070,073,078; no repeat discovery search for general regularity bounds.
SOURCE_EVIDENCE: Newly inspected Stacks 41.7.3 (04DG), 30.14.3 (0AG7), 30.14.1 (01YS), 33.35.14 (08AC), 33.33.2 (08AA), 33.33.3 (0AYT) and 30.2.4 (089W), statements and relevant proofs, accessed 2026-10-20: https://stacks.math.columbia.edu/tag/04DG , https://stacks.math.columbia.edu/tag/0AG7 , https://stacks.math.columbia.edu/tag/01YS , https://stacks.math.columbia.edu/tag/08AC , https://stacks.math.columbia.edu/tag/08AA , https://stacks.math.columbia.edu/tag/0AYT , https://stacks.math.columbia.edu/tag/089W . Hoa arXiv:math/0608118v1 Theorems 0.2/4.1, pp. 2/15–16, reused from 2026-10-20-opposite-image-projective-degree-defect.md, https://arxiv.org/pdf/math/0608118v1 .
COMPARISON: The local finite-unramified theorem covers singleton complex fibres; the graded-to-sheaf comparison, eventual Serre vanishing, Euler polynomial and finite-support cohomology theorems cover the required constant-term translation. No normality, CM property or untwisted cohomology vanishing of the original image is required by these sources.
GAP: The family-specific finite-support argument, evaluation of Hoa's whole binomial polynomial at zero and resulting length inequality remain for a separate calculation. No bound, effective projective choices or useful contradiction is established by this review.
REASON: Essential additional bridge coverage is now available. Specialize the cited general theorems without reproof in one separately approved calculation using the fixed L137 embedding.
LITERATURE_REASON: The start-of-turn REVIEW_REQUIRED target asks for two bridges expressly outside the ready parameter audit; this review adds only their missing source coverage and reuses Hoa unchanged.
SCOPE: Hypothetical L071/L118 equality F with integral c_1=0 and ch_2=-14e_1-21e_2-tau_D; L120's finite birational unramified normalization of the original integral reduced image, L121's finite possibly empty off-diagonal coincidence scheme, audited L137's fixed embedding. Arbitrary finite multiple fibres and possible linear degeneracy are allowed.

## Gap, intermediate target and decision test

The main gap is universal primitive rational Hodge realization. The
intermediate target is a bound for the total length of the actual
normalization quotient Q=nu_*O_B/O_Z in L120's original image.
Its plausible downstream use is comparison with actual collision
geometry. F existence, collision existence/counts, a useful lower
comparison and transverse transport remain independent gaps.

Continue for one calculation if the retained finite-map hypotheses
and fixed projective data suffice under the cited sources. Park the
bound if an additional singularity or cohomology assumption is needed,
or if its parameters must depend on Q. A finite fixed-parameter bound
alone is no contradiction. This review passes the source-coverage
test, without performing that calculation.

## Finite-support source and applicability scope

[Stacks Lemma 41.7.3](https://stacks.math.columbia.edu/tag/04DG)
assumes a finite unramified morphism, a singleton fibre and a purely
inseparable residue extension; it gives a closed immersion over a
neighborhood of the target point. Read its full proof: the fibre
algebra and going-up identify the relevant localization, Nakayama
gives surjectivity, and finite generation extends it to a neighborhood.
No normal-target or flatness hypothesis occurs. This is the needed
input, rather than birationality alone or an assertion that every
unramified map is an embedding.

L120 supplies finiteness/unramifiedness for B -> Z itself, not only
for B -> M. L121 supplies a finite off-diagonal scheme; its proof
retains a clopen diagonal and permits empty collisions. Since Z -> M
is a closed immersion, the two fibre products over Z and M agree.
For the proposed application at a closed singleton fibre, both
residue fields are C, satisfying the source's residue hypothesis.
The later proof must explicitly use the defining injection
O_Z -> nu_*O_B to upgrade the cited closed immersion to an
isomorphism on that neighborhood. It must also use coherence and
the Jacobson property of finite-type complex schemes to pass from
closed singleton points to support contained in the finite collision
image. Merely checking fibres or birationality is insufficient.
This is an applicability checklist, not a new finite-support lemma.

## Hilbert convention and finite-normalization comparison

[Stacks 30.14.3](https://stacks.math.columbia.edu/tag/0AG7)
assumes a graded ring generated by finitely many degree-one elements
over a noetherian degree-zero ring and a finite graded module. The
canonical graded-piece/global-section map is an isomorphism in high
degrees. Its proof kills the sheafification-zero kernel and cokernel
in high degrees, using finite generation and powers of the degree-one
generators. This covers the coordinate ring in L137's actual P^N,
including a linearly degenerate image. Projective normality is not
assumed or needed for this eventual comparison.

[Stacks 30.14.1(4)](https://stacks.math.columbia.edu/tag/01YS)
gives eventual higher-cohomology vanishing for coherent sheaves on
projective space over a noetherian ring. Read its descending-induction
proof using sums of line bundles. Apply only to sufficiently positive
twists; this does not revive ATTEMPTS/073's untwisted vanishing claim.
[Stacks 33.35.14](https://stacks.math.columbia.edu/tag/08AC)
states polynomiality of the Euler function for every integral twist;
its hyperplane-difference proof was read. These inputs permit comparing
the coordinate Hilbert polynomial with the Euler polynomial, then
evaluating that polynomial at zero, even when small-degree Hilbert
functions differ.

Reuse Hoa's exact convention from the ready assessment:

    P_S(t)=sum_{i=0}^{d-1}(-1)^i e_i binom(t+d-1-i,d-1-i).

The desired Euler constant is P_S(0), not automatically the last
binomial coefficient. The separate calculation must evaluate the
whole expression with ring dimension three, retaining all signs and
lower coefficients. Hoa's bounds and their proof cases were already
inspected; no additional extraction or search is needed.

[Stacks 33.33.2](https://stacks.math.columbia.edu/tag/08AA)
gives Euler additivity on a proper scheme, and
[Stacks 30.2.4](https://stacks.math.columbia.edu/tag/089W)
identifies all cohomology with affine pushforward. Read the long-exact
sequence and affine-Leray proofs respectively. They cover the finite
normalization comparison. [Stacks 33.33.3](https://stacks.math.columbia.edu/tag/0AYT)
gives the stalk decomposition, higher-cohomology vanishing and
rank-multiplicative Euler formula for a coherent sheaf of support
dimension at most zero on a proper scheme. Its proof uses the affine
Artinian scheme-theoretic support; thus finite-support thickness is
retained, not replaced by the number of support points. Over C,
composition factors at closed points have dimension one. K3's
structure-sheaf Euler characteristic is the standard value two;
no new RR computation or vanishing of O_Z is proposed here.

## Reuse, limitations and continuation

ATTEMPTS/070 concerns failure of minimal local defect from pairwise
branch data; the present global Hilbert-coefficient bound does not
assert minimality. ATTEMPTS/073's automatic coherent vanishing and
ATTEMPTS/078's uncontrolled ordinary Hom Euler term remain parked.
The new source supplies neither such vanishing nor that Hom estimate.
The order-five route is untouched. General bounds are known results;
this review establishes coverage, not novelty or new Hodge algebraicity.
Full matching Mathlib coverage was not checked; no absence is asserted.

No lemmas or mathematical scripts were written. PROOF.md and DAG.md
are unchanged because the argument is unchanged. The separately saved
[next calculation assessment](2026-10-20-opposite-total-defect-bound-specialization.md)
is newly ready coverage; its approval belongs to the next invocation.
