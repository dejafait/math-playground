# Arbitrary-coordinate cuts — 2026-09-11

Draft checkpoint, initially unproved. For N=2^q restrict both atomic
measures to [N/2,4N], with count T, weighted count a and source mass b.
Exclude radius delta=N/(8T) around every local coordinate, costing at
most N/4 in length. Continuous centered maximal estimates with thresholds
24b/N and 24T/N cost at most N/8 each. A remaining cut t in [N,2N]
has no local endpoint closer than delta. The near-pair shell count is
at most ceil(log2(32T))+1, hence O(q+1) since T<=16WN^2.
Each shell costs at most 16 times the product of maximal functions.
Far pairs vanish by reciprocal-square and source-mass tails. Dyadic
window overlap gives summability of a and b, hence liminf (q+1)ab=0.

Resume audit: prove the finite-measure continuous maximal bound, handle
T=0 or b=0, verify conversion from real cuts to indices tending to
infinity, and apply L121 only after the liminf proof is complete.

Completed audit: the argument is now proved in Lemma 122. The local
count bounds the number of shells by C_W(q+1); zero local mass cases
require no maximal estimate. Real cuts convert to indices tending to
infinity. This draft is retained as the intermediate checkpoint; the
lemma is the authoritative proof.
