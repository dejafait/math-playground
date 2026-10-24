# Step 459 — fixed actual-principal Rayleigh attempt

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-24-actual-principal-fixed-rayleigh-test.md`.
Main gap: arbitrary-center safety at 67/68 agreements. Intermediate
target: exactly the approved v_B=1_(0 in B)-1_(1 in B) test on L120's
actual lower block C, A={0,...,67}, full W. A negative rigorous upper
endpoint rejects this assignment only; nonnegative or straddling
evidence parks this vector/estimate. No second vector or refinement.

Essential inputs: L021,L098,L112,L113,L114,L120 and foundations/09,12,13,14.
The supplied assessment checks duplicates and ATTEMPTS/098–100; their
stops remain. No new literature is necessary. Retain every root datum.

Counting plan saved before computation: only supports containing exactly
one marked anchor point contribute. At distance i their positive class
has n_i=binom(66,67-i)binom(956,i) elements (5<=i<=67); the i=68 class
has zero vector entries. Fix positive B. Its unmarked anchor parts have
sizes 67-i and i-1; outside parts have sizes i and 956-i. A positive C
at distance j chooses a,b,p,q points from these parts, where
b=67-j-a, q=j-p. Its opposite distance is h=67-a-p. A negative C has
the same unmarked choices but opposite distance h+1. Thus complete
ordered signed counts are 2*n_i*(f_ij(h)-f_ij(h-1)), where f is the
four-binomial occupancy sum and out-of-range f vanishes. Coincidence
h=0 must contribute c_i, separately from products; distances 1–4
contribute zero. Collect all permitted signed counts into sorted cubic
monomials before evaluating unchanged positive endpoints. An independent
verifier will reconstruct ordered counts by first choosing intersection
cells globally, check complete counts and endpoints, and directly exhaust
a small universe to test both marked cases. No sign has been computed.

Unresolved: other modes, full/excluded PSD, stronger distributions,
global uniqueness, measures, packing, RS realization and the 955–957
boundary. This saved plan is unfinished reasoning, not a proof verdict.

Completed in step 459: the full proof and exact straddling endpoints
are now canonical in L120, “Fixed actual-principal Rayleigh test”.
The constructor and independent verifier completed with zero failures;
898,038 independent checks pass. ATTEMPTS/101 records the prescribed
stop. No sign, PSD or boundary conclusion follows; no refinement or
second vector was attempted. This paragraph supersedes the plan's
historical unfinished status without discarding it.
