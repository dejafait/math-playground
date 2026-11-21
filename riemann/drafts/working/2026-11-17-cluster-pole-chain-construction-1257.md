# Cluster detector construction1257 — working checkpoint

Completion note: the reasoning below is preserved as the intermediate
checkpoint. Its full statement, citations and proof now reside in
[C032b](../../lemmas/C032b-enclosure-only-cluster-polynomial-detector.md);
independent conceptual audit is pending. The canonical proof includes
the explicit complementary-path check and all rounding cases.

Gate: review1256 SPECIALIZE, exact COVERED_TARGET; one mathematical
attempt. L032/L895/L030 and nomination1255 have been read. The existing
direct-constants stop is retained. No actual-Xi data or signs are assumed.

Provisional construction, not yet a verified result: approximate the
piecewise analytic function f=0 on E0, f=i/z on E+, f=-i/z on E-.
Let y=Im(w), d=min(r1,y-r1,|w|-r0-r1)/8, rho=r1+d,
m=|w|-rho, H=4(B+1). Circles of radius rho around w and its conjugate
have distance at least d from the complete support. An upper contour
pole follows its circle to the top, then vertically to height H, then
horizontally to iH; reflect for lower poles. All paths have clearance d.
Subdivision by arclength d/4 gives at most
J=ceil(4(2*pi*rho+H+B)/d)+3 moves, with stationary padding allowed.

Cauchy quadrature derivative bound:
L=rho^2/(m^2*d)+rho/(m*d)+rho^2/(m*d^2).
With epsilon=min(1/(8A),1/(2*sqrt(A*B))), use
n=max(1,ceil(4*pi*L/epsilon)) samples on each circle. Total rational
coefficient mass is at most W=2*rho/m; quadrature error <=epsilon/2.

For each unweighted kernel (z-a)^(-1), start K=1,T=1.
At each of J moves choose N=max(0,ceil(log2(4*W*J*T*F^K/epsilon))),
F=max(1,2/d). Expand every inverse power through increment N.
Tail <=T*F^K*2^(-N)<=epsilon/(4*W*J).
Update K to K+N and T to T*2^K_old*(N+1)*max(1,d/2)^N.
At +/-iH use Taylor degree M=max(0,ceil(log2(4*W*T/epsilon))).
Tail <=T*2^(-M); coefficient norm <=T since H>4.
Total polynomial coefficient norm <=W*T, total error <=epsilon.
Coefficientwise real symmetrization preserves both estimates.

Full-sum budget to verify: ideal contribution is minus the number of
cluster node copies, at least two and finite. Absolute Q error is
<=2*A*epsilon+A*B*epsilon^2<=1/2, so Q<=-3/2.
Boundary nodes and arbitrarily colliding nodes are included. Canonical
proof must check all geometry, kernel signs, higher-pole expansions,
rounding cases, symmetry and full infinite-sum convergence.

Continuation within this attempt: finish the explicit proof and review
the inequalities; if it survives, store it canonically as C032b and
nominate a separate conceptual audit. No separate approval of new
mathematics is being performed in this construction turn.
