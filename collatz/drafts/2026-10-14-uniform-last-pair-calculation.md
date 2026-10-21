# Uniform last-pair calculation — completed

Approved input assessment:
`drafts/literature/2026-10-14-uniform-last-pair-tail-redistribution.md`
(SPECIALIZE, unchanged at invocation). Main gap: universal eventual descent.
Target: the saved full integer interval's domain and own-input J guards only.

Essential inputs: L051 exact shifted endpoints and J guard; L055 literal
table, positive Lambda enclosure, t=0; L064 j=23, t=1. Existing method
stops and fixed-allocation exclusions do not answer this interval.

Reasoning to certify: write x=2^(-18t), C=C_24(0),
A=sum_(j<24) eta_j/C_j(0), D=exp(Lambda)-1. Then
B(t)=A+eta_24/(Cx), n_0(t)=B(t)/D, and
n_24(t)=eta_24/D+C A(1+D)x/D. Thus inputs 0 through 23 increase
with t and input 24 decreases. Check this algebra from full closure,
not from fixed-tail prefix growth. For every t the lower bound
eta_0>2, eta_24>=eta_0 and D<lambda_+/(1-lambda_+) gives the
domain even after the row-23 multiplier ceases to grow.

The intended discriminating test is the own-input row-24 J upper
margin at t=2. At this particular t only, all first 24 tails are at
most 38 and their multipliers still exceed 2; this permits a separate
normalized height bound. A strict failure plus the monotonic formula
would classify every t>=2. Existing t=0,1 passing evidence would then
complete the target. If this comparison is inconclusive, record the
remaining threshold, without testing other row pairs or other guards.

No full real-system, H/seed, integer/parity/valuation or primitive
realization follows; other allocations and all universal gaps remain.

Boundary calculation: the exact upper row-24 margin at t=2 is
`-474883782659/125000000000`, which is below -3.79. An unnecessary
initial request for margin<-4 failed; this stronger request is preserved
in the certificate's diagnostic_probes. The load-bearing negative sign
passed on the first run and supplies the intended threshold test.

The completed canonical proof is L068. All permitted t satisfy the domain;
exactly t=0,1 pass all J guards. The written monotonicity proof covers all
rejected parameters after the exact t=2 boundary test. One bounded attempt
is complete; a separate audit, with REVIEW_REQUIRED scope, is next.
