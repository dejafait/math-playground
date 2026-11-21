# Compact exact branch compatibility — working1268

Approved target: decide the fixed omega=1/4, z=i equation in the
unchanged assessment `drafts/literature/2026-11-17-compact-core-branch-compatibility-review-1266.md`.
Main gap remains L030-L032/C032a actual-Xi all-degree positivity.
This test can stop only the added compact exact transport restriction.

Proposed reduction (not yet audited): put h=f/Psi and a=sigma/8.
The difference is the convolution of h reflected to the negative axis
with k(t)=((1-c)-(1+c)t)exp(at)Psi(t). L016 gives
A(t)-A(-t)=-sinh(t/2), annihilated by 2D^2-1/2, so the full K
should extend evenly to the real axis. Its theta series is holomorphic
on |Im t|<pi/4, hence Psi on |Im t|<pi/2. Compact integration then
makes the convolution holomorphic on that strip; vanishing for u>=0
would give vanishing on all real u. Evenness and L019 should give
k in L1(R). Since k is nonzero, checked Fourier uniqueness gives an
interval where its Fourier transform is nonzero. Compact support makes
the transform of the reflected h entire, so the convolution identity,
the identity theorem, and Fourier uniqueness should force f=0.

Outstanding checks before a result: local normal convergence for theta
at all finite negative real arguments; correct modular derivative
signs and scale Psi=K(./2)/2; continuity and two-sided L1 tails;
compact-support division by Psi; holomorphic parameter integration;
Fubini for convolution; nonzero kernel even for exceptional c; exact
source convention and limits of the compact conclusion. No positivity
or completed-domain conclusion is proposed. No numerical test is needed.

Completion1268: the proposed reduction was carried out in C032e,
`lemmas/C032e-compact-exact-branch-compatibility-obstruction.md`.
Its proof includes all the checks above and uses only one of the
two required branches. The original reasoning is retained here;
the canonical proof, qualifications and citation are in C032e.
Separate conceptual audit pending; no completed-profile or RH claim.
