# Arbitrary literal tail allocation — working record, step 255

Approved target: the exact arbitrary-tail early-support question in
`literature/2026-10-16-arbitrary-tail-literal-early-support.md`.
Inputs being used: L051 endpoint/domain/J definitions, L055 indexed
pairs and positive Lambda enclosure, L064 exact logarithm constants and
23 finite rejecting margins. No changed-tail growth premise is imported.

Proposed uniform comparison (not yet certified at this save): assume all
guards and endpoints. Put n_i=s_i-23/11>=47. The cyclic mass identity
gives Lambda=sum log(1+eta_i/n_i). For i>=1, J_i>=15 and the J guard
gives n_i>=(4*2^60-23)/11. Hence the other 24 summands total less than
E=24*23/(4*2^60-23). With lambda_-=10584/10^14,
n_0<(23/11)/(lambda_- - E), prospectively giving s_0<20*10^9.

At the first j<=22 with b_j>=1 all earlier tails equal 2. Their shifted
offsets are negative. At row j the endpoint is decreasing in its tail,
because its pre-tail bracket is positive on the domain; bounding it by
tail 20 also gives a negative offset since H_j>=40. Thus log s_(j+1)
is below 24 plus the unchanged prefix log multipliers minus 18 log2.
These are exactly the 23 finite L064 rejecting comparisons. Check the
root bound, offset bound, signs and every margin before asserting a result.

This would exclude the whole early-support simplex, without assuming a
minimum, H/seed, integer realization or any growth in arbitrary later rows.
Universal descent, nonliteral orders and integer realization remain open.

Completed: the proposed comparisons were certified and the full proof is
canonical in L073. The certificate contains 26 rational and five integer
checks, with no failures; all 23 first-recipient guard upper margins are
below -9.32. This saved pre-completion reasoning is preserved; it is not
a second proof or current next-action record. Separate critical audit remains.
