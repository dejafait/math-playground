# First-source ground compression: bounded attempt

Step YM-20261029-543-first-source-ground-compression. The prior EXPLORE
assessment is `literature/2026-10-28-first-source-ground-compression.md`;
the sole target is its exact first-source compression bound. Existing
notebook changes are preserved. No new source theorem is assumed.

Main gap: interacting continuum construction and positive mass remain
open. The target could control the all-ground parts of the two terms
Tr((W_N)_i H_j) in L297(22), independently of other residues. Continue
only with a complete O(N^-1 log(eN)^2) estimate or a precisely saved
uncontrolled residual; an unsuccessful absolute bound is not a disproof.

## Saved reasoning before full verification

L297 gives G_i=G C_12^* diag(h_i) C_12 G. Freeze h_i at the external
row, keeping the actual source insertion before estimating the error.
L298(9)'s kernels suggest that convolution of the two order-three
factors has order-two decay. With one/two additional endpoint curls,
absolute convolution permits logarithmic losses. The source Lipschitz
factor is O((1+distance)/N), which should leave summable complete
internal-cubic row errors after multiplication by the other covariance.

For a row at depth d, compare the constant-insertion convolution to
the full-lattice one by splitting the insertion point at distance O(d).
Prospective bounds are d^-2, d^-3 log(ed), d^-4 log(ed) for zero, one,
two endpoint curls. Complete pair products would then have row error
O(d^-2 log(ed)^2), summable over all face/edge/corner layers.

These are provisional estimates, not yet asserted results. Remaining
checks: every convolution endpoint region and omitted insertion point;
the full labeled product rule; both external-curl placements with inverse
derivatives; differentiability of the frozen row tensor; all relative
endpoint domains and exact ground normalization. Use L287's separate
A/B tensor bounds and L297(10), rather than ignoring external curls.
Density is source independent but remains in the frozen cancellation.

The assessment and ATTEMPTS/047--050 were checked. The stopped generic
orbit, absolute-norm and bare-tail mechanisms are not being repeated.

## Completion

The complete proof is now canonical in
[L300](../lemmas/L300-first-source-ground-compression-rate.md). Its
insertion convolution and source-freezing estimates include all endpoint
regions, and its boundary row defect is O(d^-2 log(ed)^2), summable over
the entire cube. The complete internal-curl plus quartic compression is
O_f(N^-1); the retained external-curl derivative terms are
O_f(N^-1 sqrt(log(eN))+N^-2 log(eN)). Thus the requested rate is reached
under the stated upstream premises. This is local progress within the
approved assessment, not a claim of novelty beyond the sources checked.
The separate conceptual audit remains pending; no complete-solution
candidate or complete heat-tail estimate is claimed.
