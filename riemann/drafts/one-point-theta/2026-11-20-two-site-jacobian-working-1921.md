# Two-site Jacobian attempt1921

20 November 2026. RESEARCH/calculation, REPRODUCTION under unchanged
SPECIALIZE assessment1920. Approved target: certify or refute the
degree-four empirical standardized cubic/quartic Jacobian at sites(0,1),
using full-theta base moments from saved panel0, without a site sweep
or moment refinement. Main gap: actual-Xi all-degree positivity;
possible use: a second local affine-invariant reference adjustment.

Inputs read: L019/L021, C028q, L917 and its accepted audit197, L037;
source-notes1920 supplies imported Gautschi Theorem2.1 and Uvarov
coverage. All selected raw endpoints and the closed panel [0,1/5120]
were inspected. Use probability base moments mu_(2j)=M_(2j)/M_0,
mu_0=1, odd moments0; no factorial or Taylor conversion. Scaling the
modified measure by3 does not change its monic polynomial.

Planned finite specialization: form mixed moments
s_k=mu_k+a^k+b^k through order7. The cited moment formula gives
H*c=-t, H_ij=s_(i+j), t_i=s_(i+4), 0<=i,j<=3,
p_4(x)=x^4+c_3*x^3+c_2*x^2+c_1*x+c_0.
Differentiate this entire finite system in both sites, with
partial_a s_k=k*a^(k-1), partial_b s_k=k*b^(k-1) for k>=1
and zero for k=0. Evaluate at exactly(0,1).

Newton sums P_1,...,P_4 give empirical raw moments R_j=P_j/4;
mean m=R_1, V=R_2-m^2, T=R_3-3*m*R_2+2*m^3,
Q=R_4-4*m*R_3+6*m^2*R_2-3*m^4.
Differentiate all terms. To avoid a square root in the determinant,
write A_x=V*T_x-(3/2)*T*V_x and B_x=V*Q_x-2*Q*V_x;
the desired determinant is (A_a*B_b-A_b*B_a)/V^(11/2).
Only V>0 and strict nonzero numerator certify rank; numerical
Gram divisions must also exclude zero. A zero-containing enclosure
is inconclusive and ends the fixed test. No actual inclusion, degree
uniformity, full residual cost or RH conclusion is asserted.

Completed: the fixed determinant excludes0; the full conditional proof
and exact bounds are canonical in C028t. Producer and independent
checker certificates1921 have empty failures; all1633 trace records,
12 divisors and15 symbolic components pass. No unfinished calculation
remains. A separate proof audit is nominated; actual inclusion and
all-degree cost remain open. No site sweep or input refinement was run.
