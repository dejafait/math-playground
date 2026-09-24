# Excluded-pair mass checkpoint — 2026-09-13

The preceding L164 step is complete; existing changes are preserved.
For I=[N,2N] and amplitudes between c/sqrt(N) and K/sqrt(N),
L162 gives D3-W=3 S D2-2 S^3. Candidate collision bound:
S=O(1), D2=O(log N), obtained from the unique parametrization
u=gr, x=gs, v=hs, y=hr with gcd(r,s)=1. For j=max(r,s),
there are at most 2j pairs and at most (2N/j)^2 choices of (g,h).
Thus the quadruple count is at most 8N^2 H_floor(2N).
Together with L164 this should give W/D3=1+O((log N)^(-3)).

Resume by checking normalization and Gaussian uniformity before promotion:
write t=Tu, n=Nx, N=sqrt(T/(2pi)); the normalized amplitude is
sqrt(N) A_n=c0(2pi)^(3/4)x^(-2) exp(-(log x-log(u)/2)^2).
On x,u in [1,2] this has fixed positive lower and upper bounds.
No claim about a signed cutoff average is yet proved here.

Completed as L165: the collision bound and uniform Gaussian comparison
prove fourth-power growth of W and relative loss O((log N)^(-3)).
The signed cutoff correlation remains unproved.
