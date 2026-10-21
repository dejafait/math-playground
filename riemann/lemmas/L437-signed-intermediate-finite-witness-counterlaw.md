# Lemma 437: a signed intermediate component retains the finite witness

## Hypotheses

Use precisely L431's integrated-moment relaxation, full actual response,
exact curvature and forms B(X;t)=b(t)^T X, D(X;t)=X^T J(t)X,
uniform height marginal dt/H and original tolerances. Write ell=log H
and E_H=H^(-1) integral_[H,2H]. The constants beta>0 and gamma_2
are those of L409/L430, as retained in L431; rho=gamma_2/beta.
P and I are exactly L436's fixed polynomial and integral, with
n=131071 and I<-1/100. They never depend on H.

Retain L421's high component and L429's slow Poisson cutoff and actual
response limits. Replace only the intermediate component, and recompute
the remaining mass, bulk mean and entire covariance. The qualitative
physical bounds allow one fixed enlargement of their constants.
No conditional actual critical moments, consistency of laws for different
H, actual sine limits, growing-character limits or global critical-function
realization are imposed. All old tolerances, including both tiny odd-second
errors, are retained.

## Conclusion

There is one Borel family of conditional probability laws for all
sufficiently large real H satisfying every L431 selected constraint,
avoiding {D>0,B<0}, and additionally satisfying

    E_nu[DB P(t log 2,t log 3,t log 5)]
       =beta I ell^2+O_P(ell).                             (1)

The unweighted and cos(t log 2)-weighted cubic means are respectively
beta ell^2+O_P(ell) and gamma_2 ell^2+O_P(ell). The response and
height marginal are exact; E_nu XX^T=ell K and E_nu B=-b0 exactly.
The first-D limit, W^2 x-second correlation, every separately fixed-prime
x-second limit, all 23 quartic coefficients, both absolute third envelopes,
the fourth envelope and fixed physical bounds are retained.
For this same family and every fixed lambda>0,

    E_nu[|DB| min(1,|X|/(lambda ell^2))]
       =O_P(ell)+O_(P,lambda)(ell^(3/2))
                    +O_(P,lambda)(ell^(1/4))=o(ell^2).       (2)

Constants may depend on the one fixed witness, but never on H or the
prime cutoff stage. Cap comparison onsets may depend on lambda; the
family does not. Equation (1) matches L436's actual leading coefficient
with discrepancy o(ell^2); no stronger actual remainder is asserted.

This extends the selected-information obstruction to this one additional
finite observable. It does not match the entire three-prime character
family. It supplies no actual clipped statistic, capped nondegeneracy,
global realization, L413 full-error regulator margin, global mixed
positivity or RH conclusion. The separate step-247 critical audit below
validates this selected-law construction. POTENTIALLY_NEW records the
original limited source comparison, not established originality.

## Proof

The prior EXPLORE assessment is
`drafts/literature/2026-10-19-finite-witness-signed-intermediate-feasibility.md`.
It explicitly covers the changed direction, three-test calibration and
all induced corrections. The known moment and matrix inputs are reused.
Richter's theorem is not invoked to infer positive feasibility from signed
moments. L417's antipodal restriction and the earlier radial failure do
not apply to the new critical directions. L436 rules out a nonnegative
cubic calibration, not a positive probability law with both cubic signs.

### A uniformly negative cubic at a positive B value

Use L419's notation a+ih=R zeta(5/2+it), c=1/(4pi). There are fixed
0<s_min<=s_max with s_min<=s=a^2+h^2<=s_max for every eventual t.
The exact response is

    v=c(a,-h/2,-a/4)+O(1/L), e=q/L^2=o(1),
    ell_F(X)=y^2-xz-e x^2,
    C=v_1^2-v_0 v_2-e v_0^2,
    b=(-v_2-2e v_0,2v_1,-v_0), D=B^2-4C ell_F.

All errors are uniform on an eventual height ray; the coefficients are
bounded. At e=0 and the displayed leading response write B_0,D_0,
C_0=c^2 s/4. Define the continuous vector

    U=(a+h,(a-h)/2,-(a+h)/4).

Direct substitution, retaining both a and h, gives

    B_0(U)=c s/2, ell_0(U)=s/2,
    D_0(U)=-c^2 s^2/4,
    |U|^2=(17/16)(a+h)^2+(1/4)(a-h)^2,
    s/2<=|U|^2<=17s/8.                                  (3)

Thus U never vanishes. Set n_-(t)=U/|U|. In particular

    B_0(n_-)>=c sqrt(s_min)/(2 sqrt(17/8))=:b_*>0,
    D_0(n_-)<=-2c^2 s_min/17=:-d_*<0.

The exact b differs from its leading value by o(1), and the exact
quadratic matrix J differs from its leading matrix by o(1), uniformly.
This follows directly from their polynomial coefficient formulas and
the bounded response with e=o(1). Since |n_-|=1, increase the onset
once to obtain

    B(n_-;t)>=b_*/2, D(n_-;t)<=-d_*/2,
    h_-(t):=-D(n_-;t)B(n_-;t) in [h_-min,h_-max],         (4)

where both bounds are fixed positive constants. This uses the exact
forms, not replacement support. No division by a real response projection
occurs. The direction is Borel (indeed continuous on the eventual ray).
Use L421's Borel unit direction n_+ with exact B,D>0 and
h_+=D(n_+)B(n_+) in a fixed positive interval. Reversing n_+ would
give the forbidden orientation; (3) instead changes the direction.

### A bounded signed density matching the three tests

Let angle brackets denote normalized Haar integration on the three-torus,
write x=(x_2,x_3,x_5), C_1(x)=cos x_2, and N=n+1=131072.
The exact finite Fourier expansion of P in L436 gives

    <P>=1, <C_1>=0, <C_1^2>=1/2,
    p1:=<P C_1>=(1-1/N)/sqrt(2).

Indeed its coefficient at the prime-2 unit vector is
(1-1/N)cos(a_2)=(1-1/N)/sqrt(2). Define

    Q_0=P-1-2p1 C_1, V=<Q_0^2>.

Then <Q_0>=<Q_0 C_1>=0. The Fourier coefficient at the prime-3
unit vector is still (1-1/N)cos(a_3)=(1-1/N)/sqrt(3), since
the subtracted terms involve only the prime-2 coordinate. Orthogonality
of the finite exponentials consequently gives

    V>=2(1-1/N)^2/3>0, <P Q_0>=V.                       (5)

The factor two counts the distinct positive and negative prime-3
frequencies. These are finite sums, with no convergence issue. Put

    tau=[beta I-beta(1+2rho p1)]/V,
    F(x)=beta(1+2rho C_1(x))+tau Q_0(x).                  (6)

This is one fixed real trigonometric polynomial with finite supremum
M_F. Equations (5)--(6) prove exactly

    <F>=beta, <F C_1>=gamma_2, <F P>=beta I.              (7)

This elementary finite orthogonal projection is included to justify
the particular calibration; it is not a general moment representation
theorem. Since P>=0 and beta I<0, F cannot be nonnegative everywhere.
Its negative part will determine a positive mass on (4), not a negative
probability. All constants in (6) are well defined; no numerical
approximation of V or of the large polynomial is required.

Let theta(t)=(t log 2,t log 3,t log 5). For each of the three fixed
polynomials F, FC_1, FP, every nonconstant frequency has the form
u=v_2 log 2+v_3 log 3+v_5 log 5 !=0 by unique factorization.
The exact sharp integral satisfies |E_H exp(iut)|<=2/(H|u|).
Each sum is finite, so (7) holds along theta(t) with errors O_P(1/H),
for every real H. Small frequencies may give very large fixed constants;
no uniform estimate as N or a character grows is used.

### Nonnegative intermediate masses and complete corrections

Retain L421's high component p(t) delta_Y(t) verbatim. It has p<=1/2,
preserves each actual quartic integrand exactly, avoids the forbidden
joint sign and satisfies

    E_H p=O(ell^-8), E_H[p|Y|^2]=O(ell^-2),
    E_H[p|B(Y)|]=O(ell^-5), E_H[p|D(Y)|]=O(ell^-2),
    E_H[p|Y|^3]+E_H[p|DB(Y)|]=O(ell).                    (8)

Take R_mid=ell^(3/2), F_+(t)=max(F(theta(t)),0),
F_-(t)=max(-F(theta(t)),0), and define

    Z_+=R_mid n_+, Z_-=R_mid n_-,
    k_+=ell^2 F_+/(R_mid^3 h_+),
    k_-=ell^2 F_-/(R_mid^3 h_-).                         (9)

Both masses are nonnegative and Borel, and k_++k_-=O_P(ell^(-5/2))
uniformly. All intermediate states avoid {D>0,B<0}, and their exact
conditional cubic sum is

    k_+D(Z_+)B(Z_+)+k_-D(Z_-)B(Z_-)=ell^2 F(theta(t)).    (10)

The corresponding absolute sum equals ell^2 |F(theta(t))|. Uniform
boundedness of the exact coefficients and (4) also give, for j=1,2,3,4,

    E_H[k_+|Z_+|^j+k_-|Z_-|^j]=O_P(ell^(-5/2+3j/2)).   (11)

All quantities in the rest of the proof are recomputed. Set

    w=1-p-k_+-k_-, W_H=E_H w,
    Q=E_H[pYY^T+k_+Z_+Z_+^T+k_-Z_-Z_-^T],
    J_R=E_H[pB(Y)+k_+B(Z_+)+k_-B(Z_-)],
    D_R=E_H[pD(Y)+k_+D(Z_+)+k_-D(Z_-)].

Equations (8)--(11) imply eventually

    1/4<=w<=1, E_H(1-w)=O_P(ell^(-5/2)),
    Q>=0, ||Q||=O_P(ell^(1/2)), J_R=O_P(ell^-1),
    D_R=O_P(ell^(1/2)), W_H=1-O_P(ell^(-5/2)).               (12)

The bounds use integrated rarity for p, not pointwise convergence of p.
Use exactly L429's cutoff j(H) and finite Poisson product P_j(t),
distinguished from the fixed witness P. Those response-only limits are
unaffected by (9), and M_j<=ell^(1/8). Define anew

    N_H=E_H(wP_j), g_H=P_j/N_H.

Then E_H[(1-w)P_j]=O_P(ell^(-19/8)), N_H=1+o(1) and

    (1/2)ell^(-1/8)<=g_H<=2ell^(1/8), E_H(wg_H)=1.           (13)

For every bounded response test G,

    |E_H(wg_H G)-E_H(P_j G)|
      <=||G||_infinity (|1-N_H|+E_H[(1-w)P_j])=o(1).    (14)

Thus all L429 limits (10) survive: the tests W, W^2, R^2 Z^2 and
each fixed-prime character, where Z=zeta(5/2+it), W=|Z|^2.
The complete response tails retain their uniform bounds because
wg_H dt/H is a positive measure of total mass one. No new diagonal
limit or actual twist theorem is assumed.

Now put, with exactly the old K,b0,

    d_H=(-b0-J_R)/W_H, m(t)=d_H b(t)/|b(t)|^2,
    A_H=-(Q+E_H[wmm^T])/W_H,
    Sigma(t)=ell g_H(t)K+A_H.                            (15)

L419 supplies K>0, bounded J,b, |b|>=b_min and tr(JK)<=-delta_0.
Consequently m=O_P(1), ||A_H||=O_P(ell^(1/2)), and, writing
kappa_0=lambda_min(K)>0, J_*=sup||J||, one obtains

    lambda_min(Sigma)>=(kappa_0/2)ell^(7/8)-C_A ell^(1/2),
    ||Sigma||<=2||K||ell^(9/8)+C_A ell^(1/2),
    tr(J Sigma)<=-(delta_0/2)ell^(7/8)+3J_*C_A ell^(1/2).    (16)

In particular Sigma is positive definite and its J-trace is uniformly
negative after one fixed onset. Apply L419's Borel six-state construction
to Sigma,J,m. Its pointwise existence input is the real Schur--Horn
theorem in E. A. Carlen and E. H. Lieb, *Short proofs of theorems of
Horn and Mirsky on diagonals and eigenvalues of matrices*,
[arXiv:0904.0734v2, pp. 1--2, theorem after (1.1), proof through (1.2)](https://arxiv.org/pdf/0904.0734v2).
The trace-average diagonal is majorized by the eigenvalues of
Sigma^(1/2) J Sigma^(1/2). Its additional Borel implementation is
L419's two-rotation construction, including equality branches, not an
uncited measurable-selection inference. There is no bounded-covariance
hypothesis in this matrix theorem.

The bulk law mu has six equally weighted states m +/- xi_i with
centered covariance Sigma and xi_i^T J xi_i=tr(J Sigma).
They satisfy |xi_i|=O_P(ell^(9/16)), and hence, for a fixed c_bulk>0,

    D(m +/- xi_i)<=-c_bulk ell^(7/8)+O_P(ell^(9/16))+O_P(1)<0. (17)

Define

    nu_(H,t)=p delta_Y+k_+ delta_Z_++k_- delta_Z_-+w mu.

The masses are nonnegative and sum to one in every fiber. All new
directions and masses are Borel. Parameter integrals in (12)--(15) are
Borel after t=Hu; the inputs are bounded on each compact eventual H
interval, with finitely many cutoff stages there. The positive square
root and L419's branches are Borel. This proves joint measurability and
the exact height/response marginal for every eventual real H.

### Verification of every preserved tolerance

Integration of the complete raw covariance and linear mean gives

    E_nu XX^T=Q+ell K+W_H A_H+E_H(wmm^T)=ell K,
    E_nu B=J_R+W_H d_H=-b0.                              (18)

Thus the four even-second O(1) errors and the two odd errors
O(H^(-2/3) ell^-1), O(H^(-2/3) ell^-3) are all zero. The first-B
tolerance O(ell^-1+H^(-1/2) ell^2) is met with zero error as well.
The full correction, not just two matrix entries, is essential here.

For first D use the exact-response trace estimate of L419,

    tr(JK)=-c^2[W/15-Re(R^2 Z^2)/60]+O(1/log(2+t)).

L429's limits and (14) give E_H(wg_H W)=S+o(1) and
E_H(wg_H R^2 Z^2)=o(1). Multiplying the trace error by ell
costs O(1) because E_H(wg_H)=1. All D_R,A_H,m terms cost
O_P(sqrt(ell)). Therefore E_nu D=-c^2 S ell/15+o(ell),
exactly the required -a_* ell+o(ell), not a stronger constant remainder.

Let q_H be the full raw x-second density and let r_H be its high plus
intermediate contribution. Positivity gives E_H r_H=Q_11=O_P(sqrt(ell)).
Since K_11=1, for every bounded complex G,

    q_H=r_H+w(ell g_H+A_H,11+m_1^2),
    E_H(q_H G)=ell E_H(wg_H G)+O_P(||G||_infinity sqrt(ell)). (19)

Apply this to W^2 and each separately fixed p^(-it). The unchanged
actual targets and response limits imported in L429 give
E_nu(W^2 x^2)=T ell+o(ell) and
E_H[(q_H-f_actual^2)p^(-it)]=o(ell). Here f_actual is L429's
actual critical scalar, not the calibration F. Each fixed prime has
its own convergence onset; no growing-prime uniformity is claimed.

For the cubics use (10) and (7) with their sharp O_P(1/H) errors.
The high component has absolute cubic O(ell). Centered bulk symmetry
gives the exact identity

    E_mu DB=(b^T m)tr(J Sigma)+2m^T J Sigma b
                                      +(m^T Jm)(b^T m).

Its absolute value is at most C_P(||Sigma||+1), and
E_H(w||Sigma||)<=ell||K||+W_H||A_H||=O_P(ell).
Thus its integrated signed conditional expectation has absolute mass
O_P(ell), also after multiplication by 1,C_1(theta(t)), or P(theta(t)).
This does not assert E_mu |DB|=O(ell). These observations prove
all three stated cubic means, since ell^2/H=O(ell).

For every one of the 23 quartics the unchanged high homogeneity
identity is exact at the actual response, including signed and zero
coefficients. Each has absolute value at most C|X|^4. Its new
intermediate addition is O_P(ell^(7/2)) by (11), and its bulk addition
is O_P(ell^(9/4)) by (17). Both are o(ell^4). The fourth envelope
remains O_P(ell^4). For |X|^3 and |B|^3 the high, intermediate
and bulk costs are O(ell), O_P(ell^2), O_P(ell^(27/16)), respectively.
Their sum is O_P(ell^2), within the original O(ell^(9/4)) tolerance.

The actual response annulus, positive C bound, response derivative
bounds and curvature are unchanged. High states have norm ell^3
or are signed 2^(1/4) multiples of the actual critical triple.
Intermediate states have norm ell^(3/2) and bulk states O_P(ell^(9/16)).
The exact physical conversion has bounded coefficients, and uniformly
on [H,2H], ell^3 L(t)^j/T(t)^(1/2) tends to zero for 0<=j<=2.
Thus one fixed enlargement meets every qualitative physical envelope,
as in L431. Both intermediate directions have positive B; the negative
direction and all bulk atoms have negative D. The high support already
avoids the joint sign. This verifies support for the complete law.

Finally the high absolute capped contribution is O(ell). For fixed
lambda, every intermediate state has cap factor ell^(-1/2)/lambda
eventually, so (10)'s absolute counterpart bounds its contribution by
ell^(3/2) E_H|F(theta(t))|/lambda=O_(P,lambda)(ell^(3/2)).
For bulk states min(1,|X|/(lambda ell^2))<=|X|/(lambda ell^2),
and |DB|<=C|X|^3. Their fourth bound gives O_(P,lambda)(ell^(1/4)).
This proves (2) without signed cancellation. Every construction choice
precedes lambda. All claimed constraints hold on one eventual real-H
family; enlarging its onset leaves L429's slow cutoff limits intact.

### Separate critical audit — 2026-10-19, step 247

This RESEARCH / REPRODUCTION / proof_audit uses the prior SPECIALIZE
assessment
`drafts/literature/2026-10-19-signed-intermediate-counterlaw-critical-audit.md`.
The construction passes in its stated scope. The audit checks (3)--(19)
against L419's exact forms and Borel implementation, L421's two imported
components, L429's all-real-height limits, L431's original tolerances,
and L436's exact fixed polynomial. Their ready source coverage is reused;
no new moment theorem, general selection theorem or numerical evidence
is needed. The earlier antipodal and capped-radial failures do not cover
this changed-direction construction. This verifies a local input, not
originality or any actual critical-function realization.

**Uniform direction, including both zero projections.** At leading order
b=c(a/4,-h,-a). Its product with U is
c[a(a+h)-h(a-h)]/2=cs/2. Also
ell_0(U)=[(a-h)^2+(a+h)^2]/4=s/2, so
D_0(U)=c^2 s^2/4-c^2 s^2/2=-c^2 s^2/4.
The coordinates a+h,a-h have squared sum 2s; their two coefficients
in |U|^2 are 17/16 and 1/4. This proves both bounds in (3).
In particular a=0 and h=0 each give |U|^2=21s/16,
B_0(U)=cs/2>0 and D_0(U)=-c^2s^2/4<0. The bounds also cover
a+h=0 or a-h=0. Only the impossible s=0 is excluded by the annulus.

For unit n_-, homogeneity and the upper norm bound give exactly
B_0(n_-)>=c sqrt(s_min)/(2 sqrt(17/8)) and
D_0(n_-)<=-2c^2 s_min/17. The exact matrices are
Fmat=[[-e,0,-1/2],[0,1,0],[-1/2,0,0]],
J=bb^T-4C Fmat. Their polynomial coefficients, the bounded response,
and e=o(1) imply uniform operator-norm convergence to the displayed
leading matrices. Thus both half-margins in (4) hold on one eventual
ray. In particular h_-min can be b_* d_*/4; bounded b,J supply its
upper bound. The direction never divides by a or h. L421's positive
direction uses its two candidate vectors, their exact B comparison,
and a sign reversal only after that comparison; its B,D lower bounds
therefore coexist with (4), with Borel equality branches.

**Finite projection and sharp averaging.** L436's exponential
coefficient is w_v cos(v.a). Consequently the cosine average at e_2
is p1=(1-1/N)/sqrt(2): the two exponential coefficients are averaged,
not added without the cosine factor 1/2. Subtracting 2p1 C_1 removes
both e_2 coefficients, since <C_1^2>=1/2. It removes neither e_3
coefficient. Parseval for this finite real polynomial gives
V>=2(1-1/N)^2/3>0. Orthogonality gives
<P Q_0>=<Q_0^2>=V, and direct substitution in (6) yields all three
equalities (7), with gamma_2=beta rho and no factor-two discrepancy.

Every polynomial here has fixed finite support, even FP. Unique
factorization makes v_2 log 2+v_3 log 3+v_5 log 5 nonzero for every
nonzero integer vector. For any one of these polynomials G, the full
sharp error is at most
2 H^(-1) sum_(v!=0)|Ghat(v)|/|v_2 log 2+v_3 log 3+v_5 log 5|.
This is a finite constant before H is varied. Its possible size changes
the onset, not the asymptotic claim. No growing-degree bound is used.
The negative integral <FP>=beta I is implemented by F_-, not by
negative probability. All signs and normalizations in (9)--(10) follow
from cubic homogeneity and h_-=-D(n_-)B(n_-)>0.

**Mass, normalization and full matrix.** The high component retains
p<=1/2, including its large-actual-jet branch, and all of (8) by
L421's exact degree-four identity. The two intermediate masses have
total O_P(ell^(-5/2)). Their absolute degree-j integrals have exponents
-1, 1/2, 2, 7/2 for j=1,2,3,4 respectively. These give (12),
including positive semidefinite Q and w>=1/4 eventually. Integrated
rarity suffices; p need not tend uniformly to zero.

The retained cutoff depends only on actual response tests, so it is
unchanged. Its upper bound P_j<=ell^(1/8) makes the new lost mass
O_P(ell^(-19/8)). Thus N_H=1+o(1), the two bounds in (13) hold,
and the exact normalization difference is

    E_H(wg_H G)-E_H(P_j G)
      =(N_H^(-1)-1)E_H(wP_j G)-E_H((1-w)P_j G).

The first term has modulus at most |1-N_H| ||G||_infinity, because
wP_j is positive with mass N_H. This proves (14) for every required
bounded test. Positivity and E_H(wg_H)=1 also retain the full-response
tail estimates with constants independent of the cutoff stage.

The recomputed d_H and m are bounded since W_H>=1/4 and |b| is
bounded below. The full A_H, not merely its odd entries, has norm
O_P(ell^(1/2)). Hence (16) follows from K>0, tr(JK)<=-delta_0
and |tr(J A_H)|<=3||J||||A_H||. Its ell^(7/8) positive-eigenvalue
and negative-trace margins dominate the ell^(1/2) correction.
The six centered atoms have norms at most sqrt(3||Sigma||), hence
O_P(ell^(9/16)). For either sign their translated quadratic values
are bounded by

    tr(J Sigma)+2||J||||m||||xi_i||+||J||||m||^2<0.

Here 9/16<7/8, which verifies the strict support margin in (17).
The cited real Schur--Horn theorem applies to the real symmetric
matrix Sigma^(1/2)J Sigma^(1/2); it needs no covariance upper bound.
Measurability instead uses L419's explicit branches. On a strict
branch A=d_j-tau>0, B=tau-d_i>0, and its positive rotation parameter
solves A eta^2+2e eta-B=0. Equality branches use a coordinate vector;
the remaining two-dimensional restriction has trace 2tau and is
handled by the same rule or the equal-diagonal branch. Unit vectors
remain bounded even if eta is large. These cases are exhaustive and
Borel. Parameter integrals after t=Hu are Borel and locally bounded;
L429's thresholds have only finitely many stages on compact H ranges.
Thus the law is Borel and has fiber mass exactly one for every eventual
real H, not only along selected heights.

**Original tolerances, without losing the odd seconds.** Expanding
the whole raw covariance cancels Q and E_H(wmm^T) exactly in (18).
Every even second error is zero, and so are both odd errors with
allowances O(H^(-2/3)ell^-1) and O(H^(-2/3)ell^-3). The identity
b^T m=d_H cancels the first-B error exactly. For first D,
a^2/20+h^2/12=W/15-Re(R^2Z^2)/60, so the normalized response
limits give coefficient -c^2 S/15. The exact O(1/log(2+t)) trace
remainder costs O(1), and the remaining terms cost O_P(sqrt(ell));
the conclusion is the required o(ell), not an O(1) remainder.

In (19), the positive rare x-second mass is O_P(sqrt(ell)); both
the full A_H entry and bounded mean square obey the same integrated
budget. Hence the W^2 test and each separately fixed-prime test retain
their o(ell) errors. Each prime may have its own convergence onset;
one family satisfies all the limits without uniformity in growing p.
No response-conditioned actual covariance is asserted.

Centered symmetry in the six bulk states kills the linear and cubic
centered terms in DB. The three surviving terms are exactly the
displayed identity following (19). Their conditional signed expectation
is O_P(||Sigma||+1), with w-weighted integral O_P(ell).
Multiplication by the fixed bounded P or C_1 retains this estimate.
The high absolute cubic is O(ell), so (7), (10) and the full sharp
errors prove all three cubic asymptotics. This does not use the false
stronger bound E_mu |DB|=O(ell).

All 23 quartics retain the exact high contribution and acquire only
O_P(ell^(7/2)+ell^(9/4))=o(ell^4), including zero and signed
matrix entries. Their absolute fourth envelope remains O_P(ell^4).
Both third envelopes cost O(ell)+O_P(ell^2)+O_P(ell^(27/16)),
within the original O(ell^(9/4)) bound. The polynomial-size states
obey the physical jet envelopes because ell^3 L^j/T^(1/2)->0
uniformly for j=0,1,2; the other high branch is a fixed multiple of
the actual jets. One enlargement of constants handles both branches
and all stages. Exact response, curvature and the positive C bound
are unchanged. High support has its old orientation, both intermediate
directions have B>0, and every bulk atom has D<0. The forbidden joint
sign is therefore absent on the complete support.

Finally, cap the high component by one to obtain O(ell). The intermediate
norm is ell^(3/2), so its absolute cubic ell^2 |F| gains the eventual
factor ell^(-1/2)/lambda. The bulk cap is bounded by |X|/(lambda ell^2),
giving O_(P,lambda)(ell^(1/4)) from its fourth bound. Each term is
o(ell^2), with every construction choice made before lambda. The cap
onset may depend on lambda; no uniform small-lambda statement is used.

No mathematical defect or missing direct input was found. The formulas,
conclusions and DAG edges require no repair. This validates the limitation
of L436's single finite witness as a joint-sign diagnostic within the
selected relaxation. The full three-prime character family is not matched
here. Actual/global realization, actual clipping, capped nondegeneracy,
L413's full-error regulator margin and global mixed positivity remain
unresolved; no RH sign or zero-exclusion range changes.

## Mathlib

Full matching coverage for this conditional counterlaw has not been
checked. The named real Schur--Horn theorem is imported by precise
citation, with L419's Borel implementation. The Poisson and actual
moment inputs are reused through L429/L431; L436 supplies the fixed
kernel and physical coefficient. No absence or formal verification is
claimed. The finite algebra and analytic bounds above require no
numerical certificate or additional mathematical script.
