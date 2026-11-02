# Uniform resonant packet test: working checkpoint

Approved target: Test the uniform-frequency resonant packet mixture with A,C,D in [0,4] for nonnegative spectral completion, exact L473 (6), bounded stationary paired derivatives and clipped mean at least 1/288.

Prior ready EXPLORE coverage: `drafts/literature/2026-10-31-resonant-stationary-packet-review.md`, exact COVERED_TARGET. Only L473 (6) is an input; L576/L577 are contrasts, with their stopped independent models preserved. Startup overview/DAG and scoped existing changes inspected. No further literature is needed for this test.

The gap is actual-Xi positivity; the intermediate test concerns only a stationary bounded bulk. Fourth-tensor completion, derivative-preserving rare correction and actual-Hardy transfer remain separate. Continue on a certified passing choice, stop this subfamily on a uniform strict upper bound, otherwise record exploration.

Partial derivation saved before final proof: phase averaging gives packet spectral density A^2 on [-1/4,1/4] plus C^2/2 on [-1/2,1/2]. Nonnegative completion to density one requires p(A^2+C^2/2)<=1. The single-wave remainder has zero clipped mean. For theta=Ux+B,

    PP''-(P')^2=U^2[-A^2-4C^2-(AC/2)(9cos(theta+phi)+cos(3theta+phi))].

Since A^2+4C^2>=4AC, its positive part is bounded by U^2 AC times the indicator cos(theta+phi)<-7/9. This arc has normalized length <2/9: cos(2pi/9)<7/9 by the increasing triple-angle polynomial on [1/2,1]. Thus E Q< pAC/216 when pAC>0. Spectral domination gives pAC<=1/sqrt(2), so the proposed bound is 1/(216sqrt(2))<1/288. Cases pAC=0 give zero. This is analytic, not a grid certificate.

An exploratory floating grid (not proof or an input) found best sampled saturated value about 0.00099853 near A/C=1.78, phi=0; required 0.00347222. No parameter exclusion is inferred from that grid. Complete proof must check expansion signs, normalization, all selector/zero-remainder cases, full K, stationarity and support before recording NEGATIVE.

Completed this attempt: all listed proof cases are written in canonical
`lemmas/L578-resonant-packet-mixture-clipped-obstruction.md`. The initial
analytic proof gives a uniform strict threshold failure, pending separate
audit. No certificate or mathematical script is required by this analytic
argument. The exploratory grid is not a dependency. The next assessment
nominates one independent application audit with unchanged hypotheses;
newly written coverage needs separate approval. Unrelated work is intact.
