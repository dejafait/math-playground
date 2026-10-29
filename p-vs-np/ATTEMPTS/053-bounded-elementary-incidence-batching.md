# Attempt 053 — bounded elementary incidence batching

Step 536, 2026-10-28. The complete restriction, its connection to all five
L115 arrows, original endpoint matrices, arbitrary-length cancelling
family, exact powers and scope are canonical in
[L119](../lemmas/L119-bounded-elementary-incidence-lag-obstruction.md).
The pre-invocation batched-incidence assessment was reused unchanged.

**WHY IT FAILS.** Requiring an arrow X to have a reverse scalar companion
Y with XY=M_U and YX=M_V permits its nilpotency index to change by at
most one, regardless of dimensions, support or arrow orientation. L115's
four outer arrows have these companions and its central arrow is
invertible, even after affine substitution. A longer cancelling branch
gives original F_rG_m/G_mF_r endpoint indices r+m+1 and max(r,m)+1.
The required number of elementary arrows is therefore at least min(r,m),
unbounded on a family with S=10r+6m+34. At r=m=6 the exact nonzero
(f0,u6) entry in M_A^12 contradicts every five-arrow template. The two
previously required fixtures have index gaps 1 and 0; passing those
necessary tests did not establish maps. No ordinary scalar-chain lower
bound follows, since an ordinary singular projection may discard a long
unobservable component without any such companion. A different batching
mechanism must allow that possibility or otherwise abandon bounded lag;
merely enlarging elementary intermediates cannot help. No stopped
receiver, cap, production format or earlier attempt is changed.
