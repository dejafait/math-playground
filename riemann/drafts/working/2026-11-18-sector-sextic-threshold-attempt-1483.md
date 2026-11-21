# Uniform adjacent-threshold attempt1483

One RESEARCH development attempt under unchanged EXPLORE assessment1478/
review1479. The exact target is the saved arbitrary-quartic sextic count
law. C020u (audited1482) supplies simple J=TR reference roots, K/J'
signs and the conditional count/multiplicity closure; C020p is used only
for its cited Walsh preservation interface. Earlier fixed-family and
coefficient-grid stops remain in force. No new literature is needed.

Test the sufficient inequalities b_i>b_(i+1), all three adjacent pairs,
for arbitrary distinct-root monic R and 1/4<=t<=5/18. Put
s(x)=x+tR(x)/(R(x)+2tR'(x)), so b_i=-2s(alpha_i).
Away from poles, direct differentiation gives
s'=1+2t^2(R'^2-RR'')/(R+2tR')^2>=1.
This does not compare successive J roots: K has a pole between each
such pair. The jump must be controlled, not ignored. At the fourfold
input limit and t=5/18 the two outer nonzero reference roots have
equal thresholds, so a spacing-independent positive gap is not sought.

Continuation test: obtain a uniform positive adjacent gap for distinct
input roots, including the closed t endpoints, or an exact obstruction.
A failed inequality is not a count counterexample. Preserve incomplete
algebra if neither is obtained. Downstream, a proved ordering permits
C020u's four-sign argument and repeated-root closure. Actual-Xi
applicability, paid loss, general symbols/compositions and all degrees
remain independent gaps.

Partial mechanism (not yet independently audited): for a reference root x,
set a=s(x), h=x-a=-tR(x)/K(x), R_j=R/(y-r_j), and
v_j(x)=-tR_j(x)/K(x). These definitions retain shared R/J roots.
Writing delta=4t-1 in [0,1/9], direct polynomial identities give
sum v=-(h/t+1)/2 and ||v||^2=(1+delta h^2/t^2)/4.
Thus each vector lies on the ellipsoid
||v||^2=delta(sum v+1/2)^2+1/4.
For two distinct reference roots with the same a, the divided-difference
identity for R gives v(x).v(z)=-1/2, without division by R.

In coordinates e=(1,1,1,1)/2 and v=Xe+Z, Z perpendicular to e,
the ellipsoid has center A0=delta/(1-4delta), squared longitudinal
radius A2=(1-3delta)/(4(1-4delta)^2), and squared transverse radius
B2=(1-3delta)/(4(1-4delta)). Put M=A2-A0^2
=(1+delta)/(4(1-4delta))<=1/2. Its support function appears to give
v.w>=-M: (M+A0 X)^2-(A2 X^2+B2||Z||^2)
=(M A2/B2-B2)||Z||^2>=0.
The positive square root has no sign ambiguity because
M+A0 X>=sqrt(A2)(sqrt(A2)-A0)>0.
For delta>0 the last coefficient is strictly positive, so equality
requires Z=0; at delta=1/9 this forces every v_j equal and nonzero,
which is incompatible with distinct input roots. At delta=0,
M=1/4 already makes -1/2 impossible.

If these checks survive, threshold collisions are impossible and the
connected-root path from C020t transports its strict ordering. C020u
then gives the count and all repeated-root limits. This is a proposed
completion of the finite count target only, not an RH candidate.

Completed: the full argument is canonical in C020v. The shared-root
identities are polynomial; the square comparison has a positive side;
its endpoint equality forces equal nonzero vector coordinates. These
checks yield no threshold collisions for distinct R, so the audited
initial order transports and C020u's closure gives the count for every
quartic multiplicity. Independent conceptual audit remains pending.
No grid, numerical witness or mathematical script was used. The earlier
wording above preserves the progression of the attempt, not an extra
unresolved hypothesis of the final written proof.
