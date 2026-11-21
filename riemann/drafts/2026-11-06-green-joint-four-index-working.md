# Green joint test: unfinished construction checkpoint

2026-11-06. Work only on the prior EXPLORE assessment's covered
four-index target. This is a proposed countermodel to the stated
necessary-condition package, not full L868 admissibility or RH.

Use H=1 and arbitrary fixed ell. Let p be an even C1 cutoff, 0<=p<=1,
equal to 1 on [-2,2] and zero outside [-3,3]. Put X=x1-ell, Y=x2-ell
and p1=p(X-12), p2=p(Y), p3=p(X+Y-12), p4=p(X-Y-12).
Take the nonzero Fourier coefficients at e1,e2,e1+e2,e1-e2 to be
p1/2,p2/2,-p3/2,-p4/2 and their conjugates. Let
m=1+2 sum_(i<j) p_i p_j and h=m+p1 cos(y1)+p2 cos(y2)
-p3 cos(y1+y2)-p4 cos(y1-y2).

Proposed checks: writing P=sum p_i and Q=sum p_i^2, h>=m-P
=1+P^2-Q-P>=(P-1)^2>=0. On X=0 and X=Y at most one p_i is
nonzero, so m=1. Opposite-index coefficients have positive density
1-p4 cos(theta) at every radial point. All profiles are bounded by 1/2.
For the C3 B_n relation use the specified Green integral and justify
its split-integral differentiability for these compact C1 profiles;
do not assume boundedness of B_n in the general necessary package.

At x*=(ell+12,ell), all four profiles are centered at zero in the
Green integral. Put kappa=(1/2) integral exp(-|u|)p(u)du. The four
entries become kappa/2,kappa/2,-kappa/2,-kappa/2. Proposed witness
c=(1,-1,-1,1) on E=(0,e1,e2,e1+e2) gives 4-6 kappa. Since
kappa>=1-exp(-2)>6/7, this would give a strict bound <-8/7.

Still to check in full: exact C1 cutoff endpoints, all conjugate
profile signs, supports on both prescribed lines, complete subgroup
positivity, C3 B_n relation and matrix convention. No numerical
eigenvalue or unverified finite preview is a certificate. If valid,
record a canonical counterexample and stop only this sufficiency
implication; leave original closure/domination and period open.

Completed later in this same bounded step: all listed checks are
written out in `lemmas/L869-bounded-profile-green-joint-positivity-counterexample.md`,
with the construction scaled to arbitrary H>0. The witness has
quadratic form <-8H/7. This working checkpoint is retained as
unfinished-work history; the canonical proof, not this proposal,
records the mathematical result. Independent audit remains pending.
