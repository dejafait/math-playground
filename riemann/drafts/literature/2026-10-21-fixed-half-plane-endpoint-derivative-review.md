# Changed source hypothesis: endpoint derivative comparison

TARGET: Compare the October 2026 fixed zero-free half-plane input with L330's moving-height logarithmic-derivative threshold and L331's disk criterion, identifying any applicable quantitative theorem before an endpoint proof attempt.
CHECKED: 2026-10-22
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the family 003 assessment and external-input register; searched fixed-half-plane log-zeta/Littlewood terminology and fixed-alpha logarithmic-derivative bounds; inspected Titchmarsh Sections 14.1–14.3 directly. Scoped local checks found the prior L330/L331 classical-envelope failures, not a fixed-half-plane interpolation application. No originality inference follows from this search.
SOURCE_EVIDENCE: Titchmarsh, second edition (1986), Section 14.1 and Theorem 14.2 with proof, pp. 336–337, equations (14.2.1)–(14.2.6); Section 14.3, pp. 338–339, logarithmic convexity and Cauchy transfer to zeta-prime/zeta. Reused the pinned OpenAI September 30 Theorem 1.1 register; Liu improvement is unnecessary for this target. Exact reading and qualifications below.
COMPARISON: The printed Littlewood theorem assumes RH and cannot be imported literally. Its inspected local-logarithm, Borel–Caratheodory and three-circles mechanism supports a bounded specialization to the cited 7/8 half-plane, followed by Cauchy estimates. The proposed fixed-width logarithmic-power bound would meet both exact L330/L331 scales; that bound and its application are research obligations, not results of this source review.
GAP: Prove the changed-half-plane logarithm interpolation with fixed constants, a correctly normalized branch away from the pole, a strict exponent below 1/2 on the complete required neighborhood, and uniform Cauchy transfer. Then check the coupled heights and the whole L331 disk. No endpoint sign, local saddle, reciprocal-series extension or full RH is established here.
REASON: Essential missing quantitative source coverage is now supplied by an inspected primary proof mechanism. A reproof of that limited specialization is necessary because its zero-free boundary differs from the printed RH hypothesis; repeating the half-plane theorem itself is unnecessary.
SCOPE: The exact L330/L331 criteria only; no assertion of an endpoint sign, all-index positivity, critical-line nonvanishing or full RH.

COVERED_TARGET: Specialize Littlewood's logarithm interpolation to the cited 7/8 zero-free half-plane, seeking |zeta-prime/zeta(s)|=O((log t)^(1/3)) uniformly for 63/64<=Re(s)<=65/64 at large t, and test L330 and L331 with d=1/128 on their coupled heights.

## Exact interfaces to compare

L330 fixes r=2n, a_n=sqrt(4*pi^2*exp(4r)-25), sigma=1+1/r,
V_r=log(r)/sqrt(r), and g=zeta'/zeta. Its sufficient target is

    sup_{|u|<=V_r}|g(sigma+i(a_n+u))|=o(sqrt(r)).

The conclusion must hold on this coupled sequence, uniformly in u.
The older available envelopes were O(r) and
O(r^(2/3)(log r)^(1/3)); failure of these envelopes is not a lower
bound on g. The required relative comparison is with B_r first,
not directly with the exponential final error E_r. A theorem about
zeros to the right of 7/8 does not itself state this derivative bound.

L331 centers at sigma_0=1+1/(2r), on the same height a_n.
For 0<d<=1/8, its sufficient criterion is analyticity of g on a
neighborhood of the closed disk of radius 2d and a disk supremum
M<=r*d/4. Its previous d was forced to shrink with the classical
region. Check both the available radius and the quantitative bound
under the new hypothesis; do not retain the old radius by default.

Even satisfying either interface would need a separate mathematical
application and review. A local saddle still requires higher-order
errors and complementary-contour control. A successful endpoint
margin would leave smaller indices and passage to all heights open.
No pure half-plane citation resolves these separate obligations.

The family 003 register's formal verification qualifications remain
in force. Reuse the existing external result rather than rerunning
its research proof; formal-artifact verification is a distinct task.

## Primary-source inspection and reuse decision — 2026-10-22

Read the [1986 primary text, PDF page 173 (printed pp. 336–337)](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf#page=173) and [PDF page 174 (printed pp. 338–339)](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf#page=174), including the proof rather than only its statement. Section 14.1 assumes RH throughout. Theorem 14.2 bounds log zeta by O((log t)^(2-2*sigma+epsilon)), uniformly on sigma_0<=sigma<=1, sigma_0>1/2. Its proof uses an analytic logarithm, a polynomial-growth upper bound, Borel–Caratheodory, then three concentric circles with an inner circle in absolute convergence. Section 14.3 transfers logarithmic powers to the logarithmic derivative using Cauchy. These mechanisms, rather than RH's numerical boundary, are the relevant source coverage. They do not license substituting 7/8 into the printed conclusion without proof.

The named complex-analysis theorems are standard inputs; no new theorem is being approved as already proved. The specialization must use disks entirely above a sufficiently large positive height, so the pole at 1 is absent, and normalize the logarithm by its Euler-series value on the right. The smaller nonvanishing half-plane remains a cited external input with the register's verification qualifications. No new source audit of that input was performed. Its stronger Liu boundary is not needed.

### Proposed application and discriminating test

The covered mathematical target is a **proposed** fixed-strip bound with exponent 1/3, not a conclusion of this literature turn. An explicit fixed-radius interpolation and a reserved Cauchy neighborhood are needed; a bare assertion that nonvanishing implies a small derivative is insufficient. Constants must be independent of height, r and the point in the strip. Absolute convergence on a line strictly right of 1 may be used for the inner bound, but not extended left of 1.

If the proposed estimate is established, compare its complete uniform bound with L330's sqrt(r) threshold and L331's r*d/4 using d=1/128. The latter requires the entire radius-2d disk, not just its horizontal diameter. Any local conclusion must retain the eventual-height qualification. A failure to reserve that neighborhood, or an interpolation exponent not strictly below 1/2, fails this proposed test; record the actual bound before selecting another mechanism. Reciprocal estimates need only retain L330's existing polynomial square lower bound on Re(s)>1, so no new reciprocal Dirichlet series or independent reciprocal-growth theorem is essential here.

A successful application could reopen the endpoint square comparison and the local-saddle criterion. It would not supply a complete saddle asymptotic, all smaller indices, bounded exterior heights, every-height passage or RH. The prior exact nonarithmetic countermodels in L330/L331 remain valid for their stated old envelopes; the new fixed-domain quantitative hypothesis must be proved before distinguishing it from those envelopes.

### Duplicate, trust and continuation qualifications

The source search used the queries `Titchmarsh zero free half plane log zeta O log t power sigma Littlewood theorem 14.2` and `zeta no zeros sigma greater alpha logarithmic derivative log t epsilon Littlewood`. The returned classical-region notes, unrelated derivative papers and unverified proof claims were not used as theorem inputs. The direct book inspection resolves the essential mechanism coverage; it does not certify novelty of the specialization. No claim of exhaustive literature coverage is made.

Reused L330/L331 in full and the overlap assessment's existing screen; searched the scoped endpoint attempts and foundations for Littlewood/interpolation duplicates. The recorded failures concern shrinking classical regions and do not test this fixed-domain specialization. Full matching Mathlib coverage and supporting API names were not checked; absence is not asserted. No lemma, mathematical script, DAG edge or main argument changed.

This assessment approves only the listed specialization attempt. The newly listed continuation remains subject to the supervisor's separate next-turn approval. Its essential local inputs are L330 and L331, with their cited L298/L302/L303/L304 interfaces if endpoint positivity is subsequently assembled. Unresolved assumptions include the still-unproved fixed-strip derivative estimate and the external half-plane trust qualification; a local saddle alone leaves higher-order and complementary-contour obligations open.
