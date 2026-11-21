# Joint complex-evaluation attempt1278 — working checkpoint

Approved exact target: review1276's simultaneous complex-evaluation
nonmembership test for C032f(20). Reuse its SPECIALIZE coverage and
review1275/completed1276's inspected source statements. This is a
research proof attempt, not another source review or an audit of C032f.

Main gap: L030-L032/C032a actual-Xi all-degree positivity. A nonmembership
certificate could test the fixed Douglas witness only after C032f's
reduction is audited; source metric and the signed Xi bridge remain open.

Inputs inspected: C032f(12)-(25), C032e's full-theta continuation/tails,
the supplied review1276, omitted review1275's full source comparison,
and stops1272/1273/1276. Existing notebook work is preserved.

Use H=L2((0,infinity),C^2), inner product linear in its first variable,
F(z)=2Xi(2iz), a=1/8, alpha=1-c, beta=1+c,
d_sigma(z)=alpha F(z+sigma a)-beta F'(z+sigma a), and
R(z)=(F(z+a)+F'(z+a))/(z+1), Re z>0. No norm cap is imposed.

Plan within the approved test: derive the representing vectors and Gram
matrix; handle common-zero points and nullspaces exactly. Then test
whether finite incompatibility or a controlled divergence follows.
The expected representer is conjugate(d_sigma(z))*exp(-conjugate(z)u)
and the expected Gram entry is sum_sigma d_sigma(z)conjugate(d_sigma(w))
divided by z+conjugate(w). These formulas are provisional until checked.
Distinct exponential functions may force finite invertibility whenever
the coefficient vector is nonzero, so finite ill-conditioning alone is
not a certificate. No bounded multiplier normalization is assumed.

Continue only on exact finite incompatibility or rigorous divergence of
minimum preimage norms. If only the criterion and finite fits result,
park this test and require materially new input. The two earlier branch
explorations remain counted; this step cannot reset that budget merely
by writing a specialization. No numerical experiment is planned absent
a controlled family with a decisive threshold.

## Analytic boundary-family test selected during the attempt

Test fixed N distinct w_j with Re w_j>0 at z_j=i*tau+epsilon*w_j,
epsilon down to zero and fixed real tau. This is a joint complex family,
not the stopped independent positive-real point test. Preliminary algebra:
F is even and real under conjugation, so at z0=i*tau, writing v=a+i*tau,
d_-(z0)=alpha*conjugate(F(v))+beta*conjugate(F'(v)) and
d_+(z0)=alpha*F(v)-beta*F'(v). Since alpha,beta>0, a common zero
on this boundary means F(v)=F'(v)=0. If its multiplicity is m>=2,
both d coefficients vanish to order p=m-1 and R to that same order.
Otherwise take p=0 and the nonzero coefficient vector at z0.

For local coefficients d_sigma(z0+h)=D_sigma*h^p+O(h^(p+1))
and R(z0+h)=r*h^p+O(h^(p+1)), the anticipated finite Gram scaling is
G_epsilon=epsilon^(2p-1)*W*(||D||^2*C+O(epsilon))*W*,
where W=diag(w_j^p), C_ij=1/(w_i+conjugate(w_j)). Thus the minimum
squared preimage norm should be epsilon*(|r|^2/||D||^2)*1*C^-1*1
+O(epsilon^2), hence tend to zero, not infinity. Verify all complex
conventions, positivity, Taylor orders and the singular common-zero
case before accepting this negative result. This would park precisely
fixed finite boundary clouds, not growing clouds, interior common zeros,
or global membership. No assertion is made yet about those cases.

## Completed1278

The full proof is now canonical in C032g. The boundary-family calculation
was completed with the explicit orders and matrix perturbation bound;
the required divergent norm is instead O(sqrt(epsilon))->0. Record
NEGATIVE for this specific obstruction family, REPRODUCTION rather than
a novelty claim. Global membership, interior common zeros and growing
families remain open. Park the tested family; nominate one independent
conceptual audit. No numerical or mathematical script was run. The
main proof assembly is unchanged; only the canonical DAG gains C032g.
