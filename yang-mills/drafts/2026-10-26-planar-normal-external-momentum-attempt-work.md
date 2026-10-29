# Planar normal response at nonzero external momentum — work record

Approved target: Establish or refute continuity at zero tangential external momentum of the complete normal-field planar surface response defined by L292's slab subtraction, retaining the external-curl cubic terms.

Turn-start coverage: `drafts/literature/2026-10-26-planar-normal-external-momentum.md`, EXPLORE, reused unchanged. This is one mathematical attempt; no new literature import or novelty claim is intended.

The main gap is the interacting continuum construction. The immediate use of this test would be to remove or expose an obstruction to extending L292's frozen normal-field cancellation to tangentially varying sources below the N^2 scale. Depth-varying source control, the remaining groups and boundary strata, a full-box o(N) error and the uniform higher remainder remain independent gaps.

Inputs inspected: L292's exact half-space/slab kernels and zero-momentum cancellation; L280's complete density and ambient Wilson tensors; L287's exact differentiated vertex and both Gaussian crossings. The official scope is retained from the versioned foundation. ATTEMPTS/007 and 047–049 do not address the proposed shifted-kernel estimate and remain preserved.

## Initial reduction, not yet a result

For paired external momenta q and -q the two cubic internal lines carry p and p+q (up to reversal of integration coordinates). The exact split is DV=A+B; the external-curl part has a factor bounded by a constant times the torus distance of q to zero. No part of A, B or their crossing terms may be omitted. The density product also shifts its two internal momenta. Quartic contractions remain local in depth, with finite external phase factors.

The proposed bounded test is a complete, depth-summed half-space-minus-bulk kernel estimate, followed by the prescribed finite-area and growing-slab limits. Both shifted soft regions and their merger must be controlled. The slab's constant normal mode at nonzero internal momentum has covariance 1/(M s); only the three exactly harmonic modes at internal momentum zero are removed. It must not be assigned a uniform gap.

No nonzero-q surface limit, uniform estimate, or continuity assertion is established at this checkpoint. If the complete infrared/depth estimate cannot be justified, preserve the exact unresolved estimate here instead of inferring it from L292's pointwise q=0 identity or L287's insufficient o(N^2) error.

## Completed attempt

The full argument is now canonical in L293. The shifted products give
an integrable bound by C(kappa(p)^-2+kappa(p+q)^-2) after complete
bulk subtraction and summation over every depth. Keeping the external
curl factors is essential: the triangle inequality for the two internal
momenta absorbs their additional denominators. Separate soft/soft,
soft/hard and hard/hard slab estimates retain the normal 1/(M s) mode
and establish the prescribed limit. No exact nonzero-q cancellation
or rate for the actual box is claimed.

The attempt reaches the approved continuity threshold under its stated
inputs. It is recorded as a partial ADVANCE pending a separate conceptual
audit, with no claim of originality beyond the inspected sources. The
new audit assessment remains REVIEW_REQUIRED. Full proofs are in the
canonical lemma; this draft preserves the initial unfinished checkpoint.
