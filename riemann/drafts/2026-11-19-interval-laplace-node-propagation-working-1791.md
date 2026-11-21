# Interval-to-node propagation working record1791

19 November 2026. Approved target: assessment1790's explicit finite-node
bridge, with no Gaver extension or observable evaluation. This records
unfinished reasoning before the canonical proof is written.

Normalize f=F/M and q=epsilon/M in (0,1). Finite variation gives
holomorphy and |f|<=1 on Re z>0, via dominated convergence and
Morera/Fubini, without moments at zero.

Candidate seed: Z(w)=3/2+(2^w+2^(-w))/4 on 0<Re w<1.
Its image lies in Re z>=7/8; the left boundary maps onto [1,2].
Trefethen Lemma2.1 should give |f(Z(w))|<=q^(1-Re w).
At Re w=1/2, Z traces an ellipse with semiaxes
3/(4 sqrt(2)), 1/(4 sqrt(2)). Maximum modulus fills its interior;
the closed disk centered at 3/2 of radius 1/8 lies inside. Thus the
candidate seed exponent is 1/2. Need explicitly check uniform boundary
limits and that the filled ellipse lies in the positive half-plane.

Candidate propagation: m_*=min({3/2} union S),
r=min{1/8,m_*/8}; N_s=ceil(|s-3/2|/r). For N_s>0, take equally
spaced centers from 3/2 to s. Their real parts are >=m_*, steps <=r.
At each center, the radius-4r disk stays in Re z>=m_*/2>0.
Scale Trefethen Theorem3.1 to grow radius r to 2r, halving the
smallness exponent; the next radius-r disk is included. Expected
common exponent alpha=2^(-1-max_s N_s)>0. Zero-step nodes use the
initial seed. No numerical test is needed to establish finiteness.

Remaining proof checks: full closed disks and radius endpoints;
uniform strip-boundary limit; no branch choice hidden in 2^w;
epsilon=0 by identity theorem; epsilon>=M and theta=0 separately;
no unsupported replacement of real interval by complex disk.

Downstream limitations: this alone gives no cap-V Gaver witness,
coefficient/deconvolution payment, d(V) rate, or actual-Xi transfer.
Inherited notebook qualifications are not premises for the generic
statement and must return in any later application.

Completion1791: the proposed construction, all listed checks and the
zero/trivial-error cases are now written in canonical
[C033v](../lemmas/C033v-explicit-interval-to-finite-node-laplace-propagation.md).
The initial sketch above is preserved; it is superseded as proof by
that complete write-up. A later independent conceptual audit is pending.
