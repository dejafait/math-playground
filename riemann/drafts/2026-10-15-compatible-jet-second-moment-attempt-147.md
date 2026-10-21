# Enlarged second-moment test — step 147 working record

Approved target: Test whether L415's joint-sign-avoiding relaxation can also match all six critical-jet second-moment asymptotics while retaining every existing constraint.

Main gap: actual negative-Bcal clipping and the full regulator margin,
followed by global mixed positivity. The intermediate test adds six raw
second moments to the already audited finite list. A simultaneous law
would show continued insufficiency; an error-robust separator would
identify useful extra information. A failed restricted ansatz is neither.
The step-146 SPECIALIZE assessment supplies the mixed Hardy moments;
steps 138/144 and L414/L415 supply the unchanged moment/support coverage.
The two October-15 compatible-jet failure records were checked. No
duplicate enlarged construction was found there; no novelty is inferred.

Checkpoint before full verification: retain L414's rare component and
write its second-moment matrix as R=O(1), mass p=O(ell^-4), Delta mean
M=O(1) and Bcal mean J=O(ell^-2). Replace the old bulk atom by a finite
law with independent signs epsilon,eta and k=1/60,1/6 of probabilities
5/9,4/9. Set x=sqrt(ell) epsilon, z=-k x. Their raw block is
ell times [[1,-1/12],[-1/12,1/80]], with determinant 1/180.
Take response (a,h)=(0,s_H). Exact Delta=c^2 s_H^2(xz+r_H x^2)
is strictly negative independently of y. Choose s_H to calibrate the
Delta mean, a small shear of y to cancel both rare odd cross moments,
and a bounded constant in y to calibrate Bcal. These adjustments need
separate checks against all six errors, the annulus and every old moment.
No completed feasibility claim is made by this working checkpoint.

Success/stop test: complete all these checks on one law for every large
real H with fixed constants, or record the failed constraint without
asserting a universal separator. Actual/global realization, uniform
height marginal, clipping for the actual family, regulator margin,
common-zero upper counts and global positivity remain outside this test.

Completed: the simultaneous construction and the precise Bui--Hall
partial-summation specialization are canonical in
[L416](../lemmas/L416-compatible-jet-second-moment-joint-sign-obstruction.md).
Both first means and both odd cross moments are exact; the four even
second moments have O(1) errors. The cubic correction is O(ell), and
all 23 quartic additions are O(ell^2). The strict response-annulus
margin, exact negative bulk discriminant, integrability and fixed bounds
hold for every sufficiently large real H. This is an informative local
obstruction, not new zeta moments or a claim of originality. No solver
or mathematical script was needed. The new critical-audit source-scope
proposal is REVIEW_REQUIRED; no separate audit was performed or approved.
