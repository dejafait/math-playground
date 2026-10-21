# Lemma 431: a fixed trigonometric recalibration matches both cubic means

## Hypotheses

Use L429's integrated-moment relaxation, full actual response, exact
forms B(X;t)=b(t)^T X and D(X;t)=X^T J(t)X, uniform height marginal
dt/H, and every original selected tolerance and qualitative envelope.
Write ell=log H and E_H=H^(-1) integral_[H,2H]. The positive constants
beta=beta_* and gamma_2 are exactly the audited series of L409 and
L430, respectively. No actual conditional critical law or consistency
of the kernels for different H is required. Qualitative pointwise
constants may be enlarged once, independently of H.

Retain L421's high component p delta_Y, its intermediate unit direction
n(t), radius R_mid=ell^(3/2), and h(t)=D(n;t)B(n;t) in a fixed
positive interval. Permit only a fixed bounded nonnegative
trigonometric polynomial F(t log 2), independent of H, multiplying
the original intermediate probability. Recompute the remaining mass,
normalization, mean and full covariance using L429's Poisson mechanism.
All limits are on an eventual ray of real H, not a subsequence.

## Conclusion

The exact coefficient ratio is

    rho=gamma_2/beta=1161 sqrt(2)/1786,
    0<rho<12/13<1.                                           (1)

One permissible fixed multiplier is

    K_12(theta)=|sum_(j=0)^12 exp(ij theta)|^2/13,
    alpha=13 rho/12,
    F(theta)=1-alpha+alpha K_12(theta).                       (2)

It is strictly positive and at most 13. With the full corrections
specified below, the resulting law satisfies every L429 constraint and
also

    E_nu DB=beta ell^2+O(ell),
    E_nu[DB cos(t log 2)]=gamma_2 ell^2+O(ell).                (3)

It retains exact E_nu XX^T=ell K and E_nu B=-b0, the original first-D
and W^2 x^2 tolerances, every fixed-prime x-second limit, all 23
quartic coefficients, both absolute third envelopes and the fourth
envelope, fixed physical bounds and exact response/curvature. It
avoids {D>0,B<0}. For every fixed lambda>0 the same family satisfies

    E_nu[|DB| min(1,|X|/(lambda ell^2))]
       =O(ell)+O_lambda(ell^(3/2))+O_lambda(ell^(1/4))
       =o(ell^2).                                          (4)

This local specialization extends a selected-information obstruction;
the sources checked do not supply this complete construction, but
originality is not established. The separate step-220 critical audit
below validates this stated integrated-moment scope.
L430's separation of the unchanged law, L427's fixed-mixture stop and
L428's uniformly bounded density obstruction remain valid. There is no
actual/global critical-function realization, actual clipping evaluation,
capped nondegeneracy, L413 full-error regulator margin, new sign or
zero-exclusion range, or RH conclusion.

## Proof

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-18-prime-cubic-intermediate-recalibration.md`.
Its primary-source and duplicate/failure comparisons are reused. The
new work is the exact arithmetic ratio and preservation of the entire
law after this bounded intermediate-mass change. The already audited
analytic cubic asymptotics in L409/L430 are imported, not reproved.

### Exact prime-2 ratio

Put kappa=17c^3/20160, c=1/(4pi), and
A_u=u^(-2) sum_(a=1)^u gcd(a,u), with A_1=1. For coprime u,v,
the Chinese remainder bijection and
gcd(a,uv)=gcd(a,u)gcd(a,v) prove A_(uv)=A_u A_v. For d>=1,
there are 2^(d-b-1) residue classes of valuation b for 0<=b<d,
and one zero residue class. Thus the gcd sum is
d 2^(d-1)+2^d, and including d=0 gives

    A_(2^d)=2^(-d)(1+d/2).                                (5)

Write m=2^a m_o, n=2^b n_o, k=2^c k_o with odd m_o,n_o,k_o.
Set s=a+b. For each s there are s+1 choices (a,b). The numerator
of mn/k has 2-valuation max(s-c,0); those of 2mn/k and mn/(2k)
have 2-valuations max(s+1-c,0) and max(s-1-c,0). Their odd
numerators are identical. Therefore define

    T_odd=sum_(m_o,n_o,k_o odd) (m_o n_o)^(-2) k_o^(-3)
                                      A_num(m_o n_o/k_o),
    B_j=sum_(s,c>=0) (s+1)4^(-s)8^(-c)
                                      A_(2^max(s+j-c,0)),
                 j=-1,0,1.

All summands are nonnegative, A_u<=1, and the original power-sum
majorants converge. Tonelli and unique 2-adic decomposition consequently
give these exact finite positive products, with T_odd>=1:

    beta=kappa T_odd B_0,
    gamma_2=(kappa T_odd/2)(sqrt(2) B_1+B_(-1)/sqrt(2)).      (6)

There is no formal division of infinite Euler products.

For completeness evaluate the three local sums without truncation.
Let x=1/4, y=1/8, q=xy=1/32, D_0=1-q=31/32. The weight
of d=s-c>=0 and that of d=-j<0 are respectively

    sum_(c>=0)(d+c+1)x^(d+c)y^c
       =x^d(1+D_0 d)/D_0^2,
    sum_(s>=0)(s+1)x^s y^(s+j)=y^j/D_0^2.                  (7)

For negative d all three A factors in B_j are 1. For d>=0,
(5) makes their factors respectively
2^(-d)(1+d/2), 2^(-d)(3/4+d/4), and
2^(-d)(1+d) for j=0,1,-1; the last formula includes d=0,
where max(d-1,0)=0 and its value is 1. Set z=x/2=1/8 and

    S_0=1/(1-z), S_1=z/(1-z)^2,
    S_2=z(1+z)/(1-z)^3, U=y/(1-y).

These are the sums of z^d, d z^d, d^2 z^d and the negative-d
tail, respectively; differentiation of the geometric series is
justified inside its radius of convergence. Equations (5)--(7) give

    B_0=[S_0+(D_0+1/2)S_1+(D_0/2)S_2+U]/D_0^2
          =571520/329623,
    B_1=[(3/4)S_0+(3D_0/4+1/4)S_1+(D_0/4)S_2+U]/D_0^2
          =425088/329623,
    B_(-1)=[S_0+(D_0+1)S_1+D_0 S_2+U]/D_0^2
          =635904/329623.                                (8)

Cancelling the positive common factor in (6) yields
rho=sqrt(2)(B_1+B_(-1)/2)/(2B_0)=1161 sqrt(2)/1786.
Both sides of the desired upper bound are positive, and exactly

    rho^2=1347921/1594898,
    (12/13)^2-rho^2=1866663/269537762>0.                    (9)

Thus (1) holds. The standalone exact-Fraction check
`python3 scripts/discriminant/prime_cubic_recalibration.py`
records all rational values and checks in
`scripts/discriminant/prime_cubic_recalibration_certificate.json`.
It uses no decimal approximation, finite prime truncation or numerical
tail estimate; the convergent sum reduction above is the proof.

### Imported fixed nonnegative polynomial and sharp period means

Use the classical nonnegative Fejer kernel, as stated in R. Andreani
and D. K. Dimitrov, *An extremal nonnegative sine polynomial*, Rocky
Mountain J. Math. 33 (2003), 759--774,
[p. 760, (1.1)--(1.4)](https://www.ime.unicamp.br/~andreani/papers/andr.pdf).
Its square expression in (2) fixes the convention at degree 12. The
constant Fourier coefficient is 1 and the coefficients at +1 and -1
are 12/13: the square has 13 diagonal pairs and 12 ordered pairs
at each first difference. With normalized circle measure this means

    <K_12>=1, <K_12 cos theta>=12/13.

The factor two in the real cosine coefficient does not change this
last average. By (1), 0<alpha<1, so (2) is a convex combination
with 1 and satisfies 1-alpha<=F<=13. It has

    <F>=1, <F cos theta>=rho.                             (10)

This imports the standard kernel and checks only its needed coefficient
normalization; it is not a new factorization or extremal theorem.
Because F and F cos theta have finitely many fixed integer harmonics,
and |E_H exp(ij t log 2)|<=2/(H |j| log 2) for j!=0,

    E_H F(t log 2)=1+O(H^-1),
    E_H[F(t log 2) cos(t log 2)]=rho+O(H^-1).              (11)

Both sharp endpoints and every real H are covered by this explicit
integral. No response phase independence is used.

### Modified masses and full normalization

Retain the high kernel p delta_Y exactly and put

    k_F(t)=F(t log 2) beta ell^2/(R_mid^3 h(t)),
    Z_mid(t)=R_mid n(t), w(t)=1-p(t)-k_F(t).               (12)

All symbols w,Q,J_R,D_R below refer to this changed law. The old
ones are not silently reused. Since F<=13 and h>=h_min>0,
k_F=O(ell^(-5/2)) uniformly, so eventually k_F<=1/4 and
1/4<=w<=1, using p<=1/2. The high estimates of L421 remain
unchanged. Multiplying each nonnegative intermediate absolute bound
there by at most 13 gives

    E_H(1-w)=O(ell^(-5/2)),
    Q=E_H[p YY^T+k_F Z_mid Z_mid^T]>=0,
    ||Q||=O(ell^(1/2)),
    J_R=E_H[p B(Y)+k_F B(Z_mid)]=O(ell^-1),
    D_R=E_H[p D(Y)+k_F D(Z_mid)]=O(ell^(1/2)).            (13)

Take the same slow cutoff j(H) and finite Poisson products P_j
from L429. Its conclusions (10) about E_H P_j, P_j W,
P_j W^2, P_j R^2 Z^2 and every fixed-prime character depend
only on the actual response, not on the rare masses. They still hold,
and M_j<=ell^(1/8). Define anew

    N_H=E_H(wP_j), g_H=P_j/N_H, W_H=E_H w.

By (13), 0<=E_H[(1-w)P_j]<=C ell^(-19/8), so N_H=1+o(1),
eventually 1/2<=N_H<=2, E_H(wg_H)=1, and

    (1/2)ell^(-1/8)<=g_H<=2ell^(1/8).                    (14)

For any bounded complex test G, the exact normalization identity gives

    |E_H(wg_H G)-E_H(P_j G)|
       <=||G||_infinity (|1-N_H|+E_H[(1-w)P_j])=o(1).   (15)

This retains all L429 full-response and fixed-prime limits. Its complete
response tail bounds also persist: wg_H dt/H is a positive measure of
exact total mass one, so a uniform tail bound integrates unchanged.
No pointwise smallness of p, stronger cutoff rate, increasing actual
twist theorem or new interchange of limits is assumed.

### Full covariance and strict translated support

Recompute, with the exact b,J of the actual response,

    d_H=(-b0-J_R)/W_H, m(t)=d_H b(t)/|b(t)|^2,
    A_H=-(Q+E_H[wmm^T])/W_H,
    Sigma(t)=ell g_H(t)K+A_H.                             (16)

L419 supplies bounded b,J, |b|>=b_min>0, K>0 and
tr(JK)<=-delta_0<0. Thus m=O(1) and ||A_H||=O(ell^(1/2))
uniformly; every symmetric entry, including both odd entries, is
included in (16). Put kappa_0=lambda_min(K) and J_*=sup||J||.
Equations (14)--(16) imply

    lambda_min(Sigma)>=(kappa_0/2)ell^(7/8)-C_A ell^(1/2),
    ||Sigma||<=2||K||ell^(9/8)+C_A ell^(1/2),
    tr(J Sigma)<=-(delta_0/2)ell^(7/8)+3J_* C_A ell^(1/2). (17)

The positive-definite and negative-trace margins dominate the full
subtraction after one fixed onset. Apply the real Schur--Horn theorem
from E. A. Carlen and E. H. Lieb, *Short proofs of theorems of Horn
and Mirsky on diagonals and eigenvalues of matrices*,
[arXiv:0904.0734v2, pp. 1--2, Horn theorem following (1.1), proof
through (1.2)](https://arxiv.org/pdf/0904.0734v2). Its applicability
is the trace-average diagonal, majorized by the eigenvalues of the real
symmetric matrix Sigma^(1/2) J Sigma^(1/2). L419's explicit Borel
two-rotation implementation, including equality branches, supplies the
basis u_i with that constant diagonal; no measurable eigenbasis or
fixed upper bound on g_H is required. Give probability 1/6 to each

    m +/- xi_i, xi_i=sqrt(3) Sigma^(1/2)u_i, i=1,2,3,

and call this conditional law mu_(H,t). It has centered symmetry,
mean m, covariance Sigma, |xi_i|<=C ell^(9/16), and

    D(m +/- xi_i)<=-c ell^(7/8)+C ell^(9/16)+C<0.          (18)

Here xi_i^T J xi_i=tr(J Sigma), and the other two terms are bounded
by bounded J,m. Thus all translated bulk states are strictly negative,
not merely negative in expectation, with |X|<=C ell^(9/16).

Define nu_(H,t)=p delta_Y+k_F delta_Z_mid+w mu_(H,t).
Its masses are nonnegative and sum to one in every fiber. F is
continuous and all old directions/zero conventions are Borel. The
integrals in (13)--(16) are Borel in H after t=Hu; on compact eventual
H intervals the inputs are bounded and only finitely many cutoff stages
occur. L419's branches and the positive matrix square root are Borel.
This proves joint measurability and the exact uniform height marginal.
At each fixed H all required integrals are finite. Enlarging the onset
does not change j(H)->infinity or introduce any lambda dependence.

### Every original tolerance and both cubic means

Integrate the complete mean and raw covariance in (16). Exactly,

    E_nu XX^T=Q+ell K+W_H A_H+E_H(wmm^T)=ell K,
    E_nu B=J_R+W_H d_H=-b0.                              (19)

The four even-second O(1) tolerances, odd-second allowances
O(H^(-2/3)ell^-1) and O(H^(-2/3)ell^-3), and first-B allowance
O(ell^-1+H^(-1/2)ell^2) all have zero error.

Write Z=zeta(5/2+it), R=exp(i phi), W=|Z|^2 and
a+ih=RZ. L419's exact trace estimate gives

    tr(JK)=-c^2[W/15-Re(R^2 Z^2)/60]+O(1/log(2+t)).

By L429's unchanged Poisson limits and (15),
E_H(wg_H W)=S+o(1) and E_H(wg_H R^2 Z^2)=o(1), where
S=zeta(5)zeta(3)^2/zeta(6) and a_*=c^2 S/15. The integrated
trace error, after multiplication by ell, is O(1), using the exact
normalization. All remaining terms from D_R,A_H,m are
O(sqrt(ell)). Hence E_nu D=-a_* ell+o(ell), the original
tolerance rather than an asserted stronger constant-term remainder.

For the entire raw x-second density q_H, let
r_H=p Y_1^2+k_F (Z_mid)_1^2. It is nonnegative and
E_H r_H=Q_11=O(sqrt(ell)). Since K_11=1,

    q_H=r_H+w(ell g_H+A_H,11+m_1^2),
    E_H(q_H G)=ell E_H(wg_H G)+O(||G||_infinity sqrt(ell)). (20)

Apply (20) to the bounded complete W^2 and to each fixed prime
character p^(-it). L429's limits and its imported actual fixed-prime
second moments give E_nu(W^2 x^2)=T ell+o(ell) and
E_H[(q_H-f^2)p^(-it)]=o(ell) for every fixed prime. This uses the
complete raw density, including the mean and both rare components;
no conditional target or growing-prime uniformity is claimed.

For cubics, (12) gives the exact conditional intermediate identity

    k_F D(Z_mid)B(Z_mid)=beta ell^2 F(t log 2).             (21)

Its two height integrals have coefficients beta and beta rho=gamma_2
by (11), with errors O(ell^2/H). The unchanged high contribution
has absolute integrated cubic O(ell). The centered bulk symmetry
gives exactly

    E_mu DB=(b^T m)tr(J Sigma)+2m^T J Sigma b
                                      +(m^T Jm)(b^T m).

Consequently |E_mu DB|<=C(||Sigma||+1), and
E_H(w||Sigma||)<=ell||K||+W_H||A_H||=O(ell).
Thus its integrated conditional expectation has absolute mass O(ell),
also after multiplication by cosine. This does not assert the stronger
and unnecessary E_mu |DB|=O(ell). Adding the three components proves
(3), since ell^2/H=O(ell). By the actual L409/L430 asymptotics both
target discrepancies are o(ell^2).

For every selected quartic, the unchanged high component still equals
the actual integrand exactly by L421's degree-four homogeneity identity.
Each of the 23 full-response quartics has absolute value at most
C|X|^4, uniformly on the response graph. The intermediate addition is
O(ell^(7/2)), using F<=13; the bulk addition is O(ell^(9/4)).
Both are o(ell^4), retaining every signed and zero leading coefficient.
The fourth envelope is O(ell^4). For each of |X|^3 and |B|^3,
the three costs are O(ell), O(ell^2) and O(ell^(27/16)),
respectively. Their sum is O(ell^2), within the original O(ell^(9/4))
allowance. All constants are fixed independently of H and the prime stage.

### Pointwise envelopes, joint signs and the fixed cap

The response, its derivatives, annulus, positive Ccal bound and exact
curvature are unchanged. High states have norm ell^3 or are signed
2^(1/4) multiples of the actual critical triple. Intermediate states
still have norm ell^(3/2), and bulk states have norm O(ell^(9/16)).
Bounded exact conversion coefficients and
ell^3 log(2+t)^r/T(t)^(1/2)->0 uniformly on [H,2H], 0<=r<=2,
give one fixed set of physical envelope constants, exactly as in L429.
Changing masses adds no new support on either rare component.
The high support keeps its original sign orientation; the intermediate
support has B,D>0; (18) gives D<0 on every bulk atom. Thus the joint
event {D>0,B<0} is absent.

The high absolute capped contribution is at most O(ell), without any
assumption that its states lie below the cap. For fixed lambda>0 the
intermediate factor is eventually ell^(-1/2)/lambda, so (21) gives
its nonnegative contribution as
beta ell^(3/2) E_H F(t log 2)/lambda=O_lambda(ell^(3/2)).
All bulk states are eventually below the cap. Their contribution is
at most C E_H[w E_mu |X|^4]/(lambda ell^2)
=O_lambda(ell^(1/4)). This proves (4) without cancellation. No parameter
of the law depends on lambda; only the eventual below-cap comparisons
do. All constraints hold simultaneously on one eventual real-H ray.

### Separate critical audit — 2026-10-18, step 220

This RESEARCH / REPRODUCTION / proof_audit uses the prior SPECIALIZE
assessment `drafts/literature/2026-10-18-prime-cubic-recalibration-critical-audit.md`.
The construction passes in its stated scope. This independently checks
the local specialization, not originality or an actual conditional law.
The complete proof above was checked against L409/L430's exact series,
L421's rare components, L429's full construction and original tolerances,
and L419's exact trace and measurable matrix implementation. The source
coverage and duplicate/failure comparison are reused; neither named
general theorem is reproved.

**Infinite arithmetic and period normalization.** For any u, the u gcd
terms are each at most u, so 0<A_u<=1. Thus each coefficient series,
including its odd restriction and fixed sqrt(2) weights, is absolutely
summable by zeta(2)^2 zeta(3). CRT makes the gcd sum multiplicative,
including residue zero, and the positive odd factor is at least its
(1,1,1) term. Cancellation in (6) is therefore legitimate. Removing
the powers of two from a reduced numerator leaves the same odd
numerator for all three rational arguments, even when m_o n_o and
k_o share factors.

For d=s-c<0, d+j<=0 for j=-1,0,1, including d=-1,j=1;
all three factors are A_1=1. For d=0 the j=-1 factor is also A_1,
and 2^(-d)(1+d)=1 gives the claimed value. For d>=1 the three
expressions in (8) follow from (5) with exponents d,d+1,d-1.
The sum over c for d>=0 is
x^d[(d+1)/(1-q)+q/(1-q)^2], exactly (7); for d=-h<0
the sum is y^h/(1-q)^2. Hence the entire two-sided difference
range, with no omitted transition term, gives (8). Replaying the
saved Fraction script reproduces all three values, rho/sqrt(2)=1161/1786,
rho^2=1347921/1594898 and the positive squared margin
1866663/269537762 against (12/13)^2. Its certificate has no failures.
This checks rational arithmetic; the convergent decomposition supplies
the infinite-sum proof.

The cited degree-12 Fejer kernel has 13 diagonal terms and 12 terms
at each first Fourier difference. Thus its circle mean is one and
its cosine-weighted mean is 12/13, not 24/13. The strict ratio margin
makes 0<alpha<1 and 1-alpha<=F<=13. The fixed polynomial and its
cosine product contain only finitely many integer harmonics. Exact
integration of each nonzero harmonic gives the O(1/H) errors in (11)
for both sharp endpoints and every real H. No response independence
is needed for this intermediate conditional identity.

**All changed masses and moving normalization.** L421's pointwise
quartic identity and its integrated high bounds survive unchanged.
Multiplying its intermediate mass by F changes each absolute bound by
at most 13. In particular w>=1/4 eventually, E_H(1-w)=O(ell^(-5/2)),
Q>=0 with norm O(ell^(1/2)), J_R=O(ell^-1) and
D_R=O(ell^(1/2)). These statements use integrated rarity for the high
component, not the false stronger premise that its mass is uniformly
small. L429's old cutoff concerns only the actual response tests.
It remains valid after this change, with M_j<=ell^(1/8) and
E_H[(1-w)P_j]=O(ell^(-19/8)). Therefore the newly computed N_H
tends to one and (14) holds. Subtracting the two normalized integrals
gives exactly (15), since |E_H(wP_j G)|<=N_H||G||_infinity.
Every required response or fixed-prime test is bounded. The measure
wg_H dt/H is positive of mass exactly one, so L429's uniform response
tails retain their full bounds independently of the growing prime stage.

The old thresholds B_j control every real H in their stage. Enlarging
the final onset for the new factor-13 constants does not change this
property or j(H)->infinity. Each fixed prime eventually belongs to
every stage; the onset may depend on that prime. No convergence rate,
uniformity over growing primes or infinite critical Euler product is used.

**Full matrix correction and strict support.** The new W_H is bounded
below, |b| is bounded below and b,J are bounded. Thus the new d_H,m
are bounded and the entire new A_H has norm O(ell^(1/2)). Formula
(16) subtracts Q and the mean square as full matrices; neither odd
entry is dropped. Positive definiteness of K and L419's exact uniform
negative trace give (17), using |tr(J A_H)|<=3||J||||A_H||.
The ell^(7/8) lower margins dominate this ell^(1/2) subtraction.
The largest covariance is O(ell^(9/8)), so every centered atom has
norm O(ell^(9/16)); its bounded-mean translation costs at most
O(ell^(9/16))+O(1), strictly smaller than the negative trace margin.
This proves exact D<0 on each atom, including at response projections
that vanish, since division is only by |b|^2.

The cited real Schur--Horn theorem applies to the real symmetric
matrix Sigma^(1/2)J Sigma^(1/2); the constant trace-average diagonal
is majorized by its eigenvalues. Measurability comes from L419,
not from an unstated selection theorem: on a strict branch its
rotation solves (d_j-tau)eta^2+2e eta-(tau-d_i)=0 with positive
denominator and radicand greater than e^2. Equality branches use a
coordinate vector. The remaining restriction has trace 2tau and the
same two-dimensional rule finishes the basis. These branches exhaust
all cases and are Borel even at repeated eigenvalues. Unit-vector
bounds do not depend on the size of the rotation parameter. The new
F is continuous; parameter integrals are Borel after t=Hu and locally
bounded on compact eventual H intervals. There are only finitely many
prime stages on each such interval. All fiber masses are nonnegative
and sum to one, giving the exact uniform height marginal.

**Every tolerance and the cap quantifiers.** The complete raw covariance
and first B integral are exactly (19). Thus all four even errors,
both smaller odd errors and the first-B error are zero. The first-D
trace identity has coefficient -c^2 S/15; its integrated coefficient
error is o(1), its exact O(1/L) remainder costs O(1) after multiplication
by ell, and all other D corrections cost O(sqrt(ell)). This meets
o(ell), without imposing a stronger first-D tolerance. In (20) the
rare raw density is nonnegative with mass O(sqrt(ell)); the mean square
and A_H,11 have the same or smaller integrated budget. Hence the
complete W^2 and each fixed-prime x-second error is o(ell), with
all response tails retained. This uses L429's imported actual fixed-prime
target only at each fixed prime.

Expanding D(m+xi)B(m+xi) under centered symmetry leaves exactly the
three terms displayed after (21). Their conditional signed expectation
has absolute value O(||Sigma||+1), whose w-weighted integral is O(ell)
by E_H(wg_H)=1. This also holds after multiplication by cosine; it
does not claim an O(ell) absolute third moment. The intermediate
identity and (11) give both cubic coefficients with O(ell^2/H) error,
and the high cubic costs O(ell). Thus (3) and the original o(ell^2)
comparison with the actual functions both hold.

For every one of the 23 quartics, including signed and zero leading
coefficients, the high part is exactly the actual quartic and the other
absolute contributions are O(ell^(7/2)) and O(ell^(9/4)), both
o(ell^4). The fourth envelope stays O(ell^4). Both absolute third
envelopes cost O(ell)+O(ell^2)+O(ell^(27/16))=O(ell^2), inside
the original O(ell^(9/4)) allowance. The support norms and exact
physical conversion admit one fixed enlargement of the qualitative
jet constants, independently of H or prime stage. No smaller numerical
envelope constants were imposed by the hypotheses.

The high support keeps its orientation; the intermediate direction
has B,D>0; all bulk atoms have D<0. Thus the excluded joint sign is
absent. The absolute capped high term is bounded by its full absolute
cubic O(ell); no high-state below-cap assertion is needed. For each
fixed lambda the intermediate norm is eventually below the cap and
costs O_lambda(ell^(3/2)). The full bulk fourth bound divided by
lambda ell^2 gives O_lambda(ell^(1/4)). All three are o(ell^2).
The family and its constraint construction do not depend on lambda;
the below-cap onset may depend on lambda. Neither uniformity as
lambda tends to zero nor a single onset for all prime tests is claimed.

No defect or missing direct input was found; no construction formula
or DAG edge needs repair. L427/L428/L430's narrower stops remain valid.
This verification establishes only the selected-information obstruction.
Actual/global realization, actual clipping, capped nondegeneracy,
L413's full-error regulator margin and global mixed positivity remain
unproved. There is no RH candidate or new zero-exclusion range.

## Mathlib

Full matching Mathlib coverage for this recalibrated counterlaw has not
been checked. The Fejer kernel and real Schur--Horn theorem are imported
by the precise primary citations above; L419 provides the separate Borel
implementation. The local prime-2 calculation is exact and its arithmetic
is independently reproducible by the saved Fraction script. Step 220
completes an informal critical audit; no claim of Mathlib absence or
formal verification is made.
