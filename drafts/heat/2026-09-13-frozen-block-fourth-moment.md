# Frozen block fourth moment checkpoint — 2026-09-13

Earlier L170 work is complete and preserved. Current step: put
z_n=A_n(c_j)/sqrt(V(c_j/T)), d_k=sum_{mn=k}z_m z_n.
Compact positivity of V gives z_n comparable to N^(-1/2) on [N,2N].
The candidate exact diagonal D=sum d_k^2 is comparable to log N,
by counting mn=pq using (m,p,n,q)=(gr,gs,hs,hr).
The finite log-frequency Hilbert inequality should bound the signed
block off diagonal by O(N^2 D/h), hence give O(T^(1/4)log T).
This is not a T-independent fourth moment and cannot by itself establish
uniform integrability. Neither diagonal growth nor this error bound is
a lower bound for the actual fourth moment.

Resume by proving both counting bounds, checking both Hilbert endpoint
terms and variance normalization, then recording the precise limitation.
All claims in this checkpoint remain draft until audited in a lemma.

Completed: both counting bounds and the signed endpoint estimate were
audited and stored in L171. Uniform integrability remains unproved.
