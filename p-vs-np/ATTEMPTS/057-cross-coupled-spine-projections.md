# Attempt 057 — two-stage cross-copy coupling and ordinary projections

Step 540, 2026-10-28. The full graph, finite maps, invariant kernels and
symbolic support bound are canonical in
[L123](../lemmas/L123-cross-coupled-spine-projection-obstruction.md).
The unchanged ready batched-incidence assessment was reused.

**WHY IT FAILS.** Literal constant/x incidences couple the two endpoint
copies and the charged spine. This does change the failed independent
lift's functions: it cancels the b_h residuals and the first spine
prefixes, and removes the leading monomial from each b_f residual.
Both full N=4 maps pass every equation and have a common invariant
zero-final kernel. Nevertheless, the remaining b_f coefficients force
at least 3^k-2^k entries in every Q->A map at N=2^k. Their ratio to
S=16*2^k+20 is unbounded, despite 2g(Q)<=7S. Sparse boundary cancellation
has removed only one coefficient per row from the binomial burden.
This stops the specified two-stage coupled common-source lift, not all
couplings, reverse arrows, freely chosen residual generators or arbitrary
chains. It is distinct from a failure to construct maps and from a ban
on deep ordinary projection kernels. No cancellation/general-G extension
is attempted after the path obstruction. Earlier work remains preserved.
