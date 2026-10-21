# Lemma 438: one signed intermediate law matches the full three-prime family

## Hypotheses

Use L437's integrated-moment relaxation, exact actual response and
curvature, B(X;t)=b(t)^T X, D(X;t)=X^T J(t)X, and uniform height
marginal dt/H on [H,2H]. Write ell=log H and E_H for this normalized
height integral. Retain every L431/L437 tolerance and the permission
to enlarge qualitative physical constants once, independently of H.
There is no requirement of consistency of laws at different H or of
realizing critical triples as derivatives of a global function.

Let W_3 be exactly L435's continuous signed torus density, renamed
to distinguish it from the response modulus W=|zeta(5/2+it)|^2.
Its normalized Haar cosine moments are g_v/beta for v in Z^3.
Use the fixed beta,gamma_2 of L431 and fixed P,I of L436. In
particular <W_3>=1, <beta W_3 cos(theta_2)>=gamma_2 and
<W_3 P>=I. Brackets denote normalized three-torus Haar integration.
No physical sine theorem or uniformity in growing characters is assumed.

Keep L421's high kernel, L429's response-only cutoff, and L437's
two exact-response supported unit directions. Recompute all remaining
mass, mean and covariance terms after changing the intermediate kernel.
The prior EXPLORE assessment is
`drafts/literature/2026-10-19-full-three-prime-signed-law-feasibility.md`.

## Conclusion

There is one Borel family of probability kernels on an eventual ray
of real H, with the exact height and actual-response marginal, satisfying
every L437 selected constraint and, for every separately fixed v in Z^3,

    E_nu[DB cos(t(v_2 log 2+v_3 log 3+v_5 log 5))]
           =g_v ell^2+o_v(ell^2).                         (1)

The same family retains the stronger three original remainders:

    E_nu DB=beta ell^2+O(ell),
    E_nu[DB cos(t log 2)]=gamma_2 ell^2+O(ell),
    E_nu[DB P(t log 2,t log 3,t log 5)]=beta I ell^2+O(ell). (2)

It has exact E_nu XX^T=ell K and E_nu B=-b0, the original first-D
limit, W^2 x-second correlation and every separately fixed-prime
x-second limit, all 23 quartic coefficients, both third envelopes,
the fourth envelope and fixed physical bounds. Its support avoids
{D>0,B<0}. For every fixed lambda>0, with this same family,

    E_nu[|DB| min(1,|X|/(lambda ell^2))]
         =O(ell)+O_lambda(ell^(3/2))+O_lambda(ell^(1/4))
         =o(ell^2).                                      (3)

Constants and the common onset may depend on the one fixed P and
density W_3, but not on H, the Poisson stage, or a subsequently tested
character or cap. Convergence onsets in (1) and (3) may depend on that
fixed test. The separate step-251 critical audit below validates this
stated selected-law scope. POTENTIALLY_NEW records the original limited source comparison, not
established originality. It establishes a limitation of this full
three-prime diagnostic in the selected relaxation. It supplies no
actual/global realization, actual clipping, capped nondegeneracy,
L413 full-error regulator margin, global mixed positivity or RH result.

## Proof

### Fixed continuous averaging and a nonsingular three-test Gram matrix

Put theta(t)=(t log 2,t log 3,t log 5), f=beta W_3, and

    phi(x)=(1,cos x_2,P(x))^T, d=(beta,gamma_2,beta I)^T.

The known averaging input is E. Kowalski, *Arithmetic Randonnee:
An introduction to probabilistic number theory*, January 19, 2021
manuscript, B.6.3, B.6.5(2), B.6.6(2), printed pp. 146--147,
[continuous-time compact-group criterion and torus specialization](https://metaphor.ethz.ch/x/2021/fs/401-3109-65L/probabilistic-number-theory-fs-2021.pdf#page=150).
It gives convergence for every fixed continuous test to Haar measure
on the orbit closure. Here a nonzero integer character v has frequency
v_2 log 2+v_3 log 3+v_5 log 5 !=0 by unique prime factorization.
The full torus is therefore the orbit closure. The source's [0,X]
average gives the [H,2H] average by twice its [0,2H] average minus
its [0,H] average. Thus for every fixed continuous U on the torus,

    E_H U(theta(t)) -> <U>                               (4)

as real H tends to infinity. This is a qualitative limit, not a rate
for W_3 or a theorem about moving tests. For fixed trigonometric
polynomials, exact exponential integration also gives an O(1/H)
error, with a finite constant depending on their frequencies.

Let G=<phi phi^T>. Its positive definiteness can be checked without
numerically expanding P. Use L437's audited finite projection:
with N=131072, p1=(1-1/N)/sqrt(2),

    Q0=P-1-2p1 cos x_2,
    <Q0>=<Q0 cos x_2>=0,
    V=<Q0^2> >= 2(1-1/N)^2/3 > 0.

For u=(u0,u1,u2) in R^3, orthogonality gives exactly

    u^T G u=(u0+u2)^2+(u1+2p1 u2)^2/2+V u2^2.         (5)

Vanishing forces u2=u1=u0=0. By continuity on the unit sphere,
kappa_G=lambda_min(G)>0. This number is fixed before H.

Define the real symmetric matrix and residual vector

    G_H=E_H[phi(theta(t))phi(theta(t))^T],
    r_H=d-E_H[f(theta(t))phi(theta(t))].

All entries are averages of fixed continuous functions, so (4) and
<f phi>=d give G_H->G and r_H->0. In fact G_H-G=O_P(1/H)
because its entries are fixed polynomials. Choose one eventual onset
such that ||G_H-G||<=kappa_G/2. For every real H beyond it,

    lambda_min(G_H)>=kappa_G/2,
    ||G_H^(-1)||<=2/kappa_G.

### A bounded correction with exact finite-height calibration

On this whole ray set

    a_H=G_H^(-1)r_H,
    F_H(x)=f(x)+a_H^T phi(x).                            (6)

Then a_H->0 and ||F_H-f||_infinity->0. In particular there is a
fixed M<infinity with ||F_H||_infinity<=M for every H on a possibly
shorter eventual ray. We use F_H as a signed cubic calibration, not
as a probability density. The exact algebraic identity

    E_H[F_H(theta(t))phi(theta(t))]=d                    (7)

holds because the added term is G_H a_H=r_H. No convergence rate
is needed for r_H. This is the reason qualitative averaging suffices
without weakening any remainder in (2).

For each fixed v, let C_v(x)=cos(v.x). Then

    |E_H[(F_H-f)(theta(t)) C_v(theta(t))]|
          <=||F_H-f||_infinity ->0,
    E_H[f(theta(t)) C_v(theta(t))] -> <f C_v>=g_v.        (8)

The second line uses (4) for one fixed continuous test. No moving-test
equidistribution or physical sine limit has been used. Equations
(6)--(7) define one F_H for all characters, not a choice depending on v.
After t=Hu, each defining integral is continuous in H>0, by continuity
of its fixed integrand on compact parameter rectangles. Matrix inversion
is continuous on the nonsingular ray. Thus a_H and (H,x)->F_H(x)
are continuous there, in particular Borel. No computed onset or
quantitative bound on its size is asserted.

### Nonnegative probabilities and the complete matrix correction

Import L437's Borel unit directions n_+,n_- at the exact response:
B(n_+),D(n_+)>0 and B(n_-)>0>D(n_-), with

    h_+=D(n_+)B(n_+), h_-=-D(n_-)B(n_-)

both bounded above and below by fixed positive constants uniformly
on the eventual height ray. These include response projection zeros;
their construction divides by no such projection. Keep L421's high
component p delta_Y exactly. Its relevant uniform bounds, as retained
in L437, are p<=1/2 and

    E_H p=O(ell^-8), E_H[p|Y|^2]=O(ell^-2),
    E_H[p|B(Y)|]=O(ell^-5), E_H[p|D(Y)|]=O(ell^-2),
    E_H[p|Y|^3]+E_H[p|DB(Y)|]=O(ell).                    (9)

It preserves each actual homogeneous quartic pointwise and already
avoids the forbidden joint sign. Put R_mid=ell^(3/2), Z_+=R_mid n_+,
Z_-=R_mid n_-, and use the positive and negative parts of the real
number F_H(theta(t)) to define

    k_+=ell^2 (F_H(theta(t)))_+/(R_mid^3 h_+),
    k_-=ell^2 (F_H(theta(t)))_-/(R_mid^3 h_-).            (10)

These are nonnegative Borel probabilities with
k_++k_-=O(ell^(-5/2)) uniformly. Cubic homogeneity gives exactly

    sum_(s=+,-) k_s D(Z_s)B(Z_s)=ell^2 F_H(theta(t)),
    sum_(s=+,-) k_s |D(Z_s)B(Z_s)|=ell^2 |F_H(theta(t))|. (11)

For j=1,2,3,4 their integrated absolute degree-j costs are
O(ell^(-5/2+3j/2)); the constants depend only on M and the fixed
direction margins. No derivative or Fourier norm of F_H is needed.

Define all quantities anew:

    w=1-p-k_+-k_-, W_H=E_H w,
    Q=E_H[pYY^T+sum_s k_s Z_s Z_s^T],
    J_R=E_H[pB(Y)+sum_s k_s B(Z_s)],
    D_R=E_H[pD(Y)+sum_s k_s D(Z_s)].

Then w>=1/4 eventually, w<=1,

    E_H(1-w)=O(ell^(-5/2)), Q>=0, ||Q||=O(ell^(1/2)),
    J_R=O(ell^-1), D_R=O(ell^(1/2)), W_H=1-O(ell^(-5/2)). (12)

Keep exactly L429's cutoff j(H) and its Poisson product P_j. This
product is distinct from P and satisfies ell^(-1/8)<=P_j<=ell^(1/8).
Its response-only averages and every fixed-prime average in L429 (10)
are unaffected by the change to the intermediate kernel. Set

    N_H=E_H(wP_j), g_H=P_j/N_H.

By (12), E_H[(1-w)P_j]=O(ell^(-19/8)), so N_H=1+o(1),
(1/2)ell^(-1/8)<=g_H<=2ell^(1/8), and E_H(wg_H)=1.
For every bounded response test U, the exact normalization identity
implies

    |E_H(wg_H U)-E_H(P_j U)|
       <=||U||_infinity (|1-N_H|+E_H[(1-w)P_j])=o(1).   (13)

Thus every unchanged L429 response limit survives. Full response tails
stay controlled by that input's uniform tail estimates, since wg_H dt/H
is a positive measure of mass one. There is no change of the cutoff.

With L419's exact K>0 and b0, put

    d_H=(-b0-J_R)/W_H, m(t)=d_H b(t)/|b(t)|^2,
    A_H=-(Q+E_H[wmm^T])/W_H,
    Sigma(t)=ell g_H(t)K+A_H.                            (14)

L419 supplies bounded b,J, |b|>=b_min>0 and tr(JK)<=-delta_0<0.
Consequently m=O(1), ||A_H||=O(ell^(1/2)), and

    lambda_min(Sigma)>=c_1 ell^(7/8)-C_1 ell^(1/2)>0,
    ||Sigma||=O(ell^(9/8)),
    tr(J Sigma)<=-c_2 ell^(7/8)+C_2 ell^(1/2).            (15)

Here c_1,c_2 are fixed positive numbers. Apply L419's Borel six-state
matrix realization to Sigma,J, with mean m. Its underlying existence
theorem is the real Schur--Horn theorem in Carlen--Lieb,
*Short proofs of theorems of Horn and Mirsky on diagonals and
eigenvalues of matrices*, arXiv:0904.0734v2,
[pp. 1--2, theorem following (1.1), proof through (1.2)](https://arxiv.org/pdf/0904.0734v2).
The matrix Sigma^(1/2)J Sigma^(1/2) is real symmetric; its constant
trace-average diagonal is majorized by its eigenvalues. Borel dependence
uses L419's explicit finite rotation branches, including equality
branches, rather than an extra assertion of this source theorem.

The resulting centered symmetric atoms +/-xi_i have covariance Sigma,
xi_i^T J xi_i=tr(J Sigma), and |xi_i|<=sqrt(3||Sigma||).
After translation by m all six atoms have

    D(m+/-xi_i)<=-c_2 ell^(7/8)+O(ell^(1/2))
                              +O(ell^(9/16))+O(1)<0.    (16)

Let mu be their equal-probability law and set

    nu_(H,t)=p delta_Y+k_+ delta_Z_++k_- delta_Z_-+w mu.  (17)

All masses are nonnegative and sum to one. The two intermediate
directions have B>0, the bulk has D<0, and the high component has
its imported support. Thus the full law avoids {D>0,B<0} exactly.
All parameter integrals in (12)--(14) are Borel after t=Hu;
the inputs are bounded on compact eventual H intervals and the cutoff
has finitely many stages there. The matrix square root and L419
branches are Borel. This establishes one Borel kernel with the exact
height and response marginal on the full eventual real-H ray.

### All original tolerances and the full character family

The full matrix and mean correction gives exact identities

    E_nu XX^T=Q+ell K+W_H A_H+E_H(wmm^T)=ell K,
    E_nu B=J_R+W_H d_H=-b0.                              (18)

In particular the four even-second errors O(1) and the two odd errors
O(H^(-2/3)ell^-1), O(H^(-2/3)ell^-3) are zero. The first-B allowance
O(ell^-1+H^(-1/2)ell^2) is also met with zero error. Integrated
O(sqrt(ell)) corrections are not charged to these tiny odd tolerances.

For first D, L419's exact response trace is

    tr(JK)=-c^2[W/15-Re(R^2 Z^2)/60]+O(1/log(2+t)),

where Z=zeta(5/2+it) and R is its unit carrier. By (13) and L429,
E_H(wg_H W)=S+o(1), E_H(wg_H R^2 Z^2)=o(1).
The trace remainder costs O(1) after multiplying by ell because
E_H(wg_H)=1. The D_R, A_H and bounded mean terms cost
O(sqrt(ell)). Therefore E_nu D=-c^2 S ell/15+o(ell), the required
-a_* ell+o(ell) with the original coefficient, not an O(1) error.

Let q_H(t) be the full raw x-second density. The rare x-second
contribution is nonnegative with integral at most ||Q||, and K_11=1.
Expanding (14) therefore gives for every bounded complex U

    E_H(q_H U)=ell E_H(wg_H U)+O(||U||_infinity sqrt(ell)). (19)

For U=W^2 or each fixed p^(-it), (13), L429's response limits and
its imported actual second coefficients prove exactly
E_nu(W^2 x^2)=T ell+o(ell) and
E_H[(q_H-f_actual^2)p^(-it)]=o(ell). Here f_actual is the actual
critical scalar, distinct from the signed torus function f. These
claims require no uniform limit for growing p.

For any fixed bounded real test T(t), the high cubic contribution
is bounded by O(||T||_infinity ell) by (9). Centered bulk symmetry
gives the exact conditional identity

    E_mu DB=(b^T m)tr(J Sigma)+2m^T J Sigma b
                                      +(m^T Jm)(b^T m).

Its modulus is at most C(||Sigma||+1). Because
E_H(w||Sigma||)<=ell||K||+W_H||A_H||=O(ell), its weighted signed
contribution is also O(||T||_infinity ell). This is a bound on
the conditional signed expectation, not on E_mu |DB|. Together
with (11) these estimates prove

    E_nu[DB T(t)]=ell^2 E_H[F_H(theta(t))T(t)]
                               +O(||T||_infinity ell). (20)

Taking T=1, cos(t log 2), P(theta(t)) and using the exact identity
(7) proves all three O(ell) remainders in (2). Taking T=C_v(theta(t))
and using (8) proves (1) for every fixed v. The same law works for
all v; only the final qualitative convergence is tested separately.

Every one of the 23 quartics retains its exact actual high integrand.
Their bounded response coefficients give absolute value at most
C|X|^4. The intermediate addition is O(ell^(7/2)) and the bulk
addition is O(ell^(9/4)), both o(ell^4), including signed and zero
leading coefficients. The fourth envelope stays O(ell^4). For
|X|^3 and |B|^3, the high, intermediate and bulk contributions are
O(ell), O(ell^2) and O(ell^(27/16)), respectively, within the
original O(ell^(9/4)) allowance. These use the same fixed M, not
any growing frequency or H-dependent supremum constant.

The exact response annulus, positive C bound, derivative bounds and
curvature are unchanged. High states are of norm ell^3 or fixed
2^(1/4) multiples of the actual triple. Intermediate states have
norm ell^(3/2), and bulk states O(ell^(9/16)). The original physical
conversion has bounded coefficients; ell^3 L(t)^j/T(t)^(1/2)->0
uniformly on [H,2H] for j<=2. Hence a single fixed enlargement of
the qualitative physical constants suffices, as in L437.

Finally the high capped absolute cubic is O(ell). For each fixed
lambda, the intermediate cap is eventually ell^(-1/2)/lambda,
so (11) and ||F_H||_infinity<=M give O_lambda(ell^(3/2)). On
bulk states use min(1,|X|/(lambda ell^2))<=|X|/(lambda ell^2)
and |DB|<=C|X|^3: the bulk fourth bound gives O_lambda(ell^(1/4)).
This proves (3) without signed cancellation and without a family
depending on lambda. All old tolerances and new fixed-character
limits hold simultaneously in this sense. L436's obstruction to a
positive scalar calibration remains valid: (10) implements a signed
calibration with positive probabilities on two different cubic signs.

### Separate critical audit — 2026-10-19, step 251

This RESEARCH / REPRODUCTION / proof_audit uses the prior SPECIALIZE
assessment
`drafts/literature/2026-10-19-full-three-prime-law-critical-audit.md`.
The construction passes in its stated scope. The following checks use
L435's audited continuous density, L436's fixed polynomial, L437's
audited directions/projection, L431's original tolerances, L429's
unchanged cutoff, and L419/L421's matrix/high interfaces. The named
source statements above are imported through their ready assessments;
no additional averaging, moment, selection or realization theorem is
assumed. This verifies a local input, not originality or an RH sign.

**Fixed inputs and exact moving calibration.** L435's absolutely
summable coefficient series makes W_3 a bounded continuous real
function on the compact torus. It has mass one and cosine moment
g_v/beta, with central rather than coordinatewise symmetry. The
fixed-rational formula at v=(1,0,0) is the same gamma_2 retained in
L431; at zero it is beta. L436 gives <W_3 P>=I. Hence <f phi>=d
with precisely the three constants in (7), including the negative
third entry. No sine limit or interchange of infinitely many physical
character limits is involved.

For a nonzero integer vector v, a zero frequency would imply
2^(v_2)3^(v_3)5^(v_5)=1, contrary to unique prime factorization.
Kowalski's cited continuous-time compact-group criterion therefore
applies to each fixed continuous test on the full torus. The identity
E_H U=2(2H)^(-1) integral_0^(2H) U-H^(-1) integral_0^H U proves
(4) on the whole real-H ray. For a fixed polynomial U, its error is
at most 2 H^(-1) sum_(v!=0)|Uhat(v)|/|v_2 log 2+v_3 log 3+v_5 log 5|,
a finite constant. This applies to every entry of phi phi^T, although
it is not a claimed rate for f phi.

L436's exponential coefficient at e_2 is
(1-1/N)cos(a_2)=(1-1/N)/sqrt(2)=p1. Since <cos^2 x_2>=1/2,
subtracting 2p1 cos x_2 removes both e_2 coefficients of P. It
leaves both e_3 coefficients equal to (1-1/N)/sqrt(3). Thus
Q0 is orthogonal to 1 and cos x_2 and its square integral V is at
least 2(1-1/N)^2/3. Expanding u^T phi as
(u0+u2)+(u1+2p1 u2)cos x_2+u2 Q0 proves (5). All three
summands are nonnegative and simultaneous vanishing implies u=0.
Consequently the fixed G has a strictly positive least eigenvalue.
Finite entrywise convergence implies operator-norm convergence, and
the Rayleigh quotient inequality gives the stated kappa_G/2 lower
bound for G_H for every sufficiently large real H.

The residual sign and transpose in (6) are correct:
E_H[phi(a_H^T phi)]=G_H a_H=r_H, so (7) is an exact vector
identity, not an asymptotic replacement. The inverse bound yields
|a_H|<=2|r_H|/kappa_G->0. Since phi is one fixed bounded function,
sup_x|F_H(x)-f(x)|<=|a_H|sup_x|phi(x)|->0. This supplies the
single finite M, independently of the cutoff and every later test.
For each fixed character, (8) follows by this uniform bound and (4)
for f C_v. No O(1/ell) convergence of r_H is needed for (2).
Writing t=Hu proves continuity of G_H and r_H by integration on
[1,2] of fixed continuous integrands on compact parameter sets;
inversion is continuous on the nonsingular ray. This also proves
the asserted Borel dependence of F_H. Constants may be enormous
for the fixed P; neither P nor kappa_G varies with H.

**Positive masses and the unchanged Poisson limits.** L437's two
directions have exact B>0, opposite exact D signs, unit norm and
uniform positive h_+,h_- margins, including both response projection
zeros. Thus (10) has nonnegative masses and exactly the signed and
absolute cubic identities (11). Its degree-j costs have exponents
-1, 1/2, 2, 7/2 for j=1,2,3,4. Uniform boundedness of F_H is all
that these estimates need. L421's unchanged high kernel obeys (9)
on both r=max(ell^3,2^(1/4)|X0|) branches and at X0=0. In particular
p<=1/2, though p need not tend uniformly to zero. These facts give
w>=1/4 eventually and every estimate in (12).

L429's chosen thresholds test only P_j and the actual response,
including each fixed prime character; they do not depend on the new
intermediate masses. Keep those thresholds unchanged. The loss is
bounded by ell^(1/8) E_H(1-w)=O(ell^(-19/8)). Hence N_H=1+o(1)
and both stated pointwise bounds on g_H follow. More explicitly,

    E_H(wg_H U)-E_H(P_j U)
      =(N_H^(-1)-1)E_H(wP_j U)-E_H((1-w)P_j U).

Positivity bounds the first term by |1-N_H| sup|U| because
E_H(wP_j)=N_H, proving (13) also for complex U. The old limits
for W, W^2, R^2 Z^2 and each fixed prime therefore survive. The
positive measure wg_H dt/H has mass one, so uniform response-tail
bounds remain valid independently of j. No new moving-product
averaging theorem or growing-prime actual moment is used.

**Whole covariance, strict support and measurability.** W_H is
bounded below, J_R=O(ell^-1), and |b| is bounded below. Thus d_H,m
are bounded, b^T m=d_H, and ||A_H||=O(ell^(1/2)). From K>0,
tr(JK)<=-delta_0, bounded J and the g_H bounds one obtains exactly
the positive eigenvalue and negative trace margins in (15), using
|tr(JA_H)|<=3||J||||A_H||. Their ell^(7/8) terms dominate the
ell^(1/2) correction. The real Schur--Horn application is at the
real symmetric matrix Sigma^(1/2)J Sigma^(1/2); the constant
trace-average diagonal satisfies its majorization hypotheses.

L419's deterministic two-coordinate implementation supplies the
additional Borel choice. On a strict branch its rotation parameter
solves A eta^2+2e eta-B=0 with A,B>0. The positive root is defined
since e^2+AB>e^2. Equality branches take a coordinate vector;
the complementary restriction has trace twice the trace average,
and either its diagonal entries are equal or strictly straddle that
average. Repeating the rule is exhaustive. Finite deterministic
index choices and these formulas are Borel even across ties.
The vectors remain unit regardless of the rotation parameter's size.

For xi_i=sqrt(3)Sigma^(1/2)u_i the equal signed atoms have centered
covariance Sigma, and each centered quadratic value is tr(J Sigma),
with no extra factor three. Translation adds at most
2||J||||m||sqrt(3||Sigma||)+||J||||m||^2. Its largest displayed
power is ell^(9/16), below ell^(7/8); the trace correction is
O(ell^(1/2)). Thus (16) gives strict exact D<0 for every bulk atom.
Intermediate atoms have B>0, and high support has its old orientation,
so the forbidden joint sign is absent on the complete support.

All parameter integrals defining w,Q,J_R,D_R,N_H,d_H,A_H are Borel
after t=Hu. The inputs are locally bounded on compact eventual-H
intervals, on which only finitely many Poisson stages occur. Positive
matrix square roots and the finite branches just checked are Borel.
Together with the continuous F_H this proves a single Borel kernel
on the whole eventual real-H ray. Fiber masses sum to one exactly;
the height marginal and actual response are consequently unchanged.

**Every original tolerance.** Expanding the full raw second matrix
and substituting A_H gives (18) exactly. The errors in all four even
entries are zero, as are the two odd entries whose allowances are
O(H^(-2/3)ell^-1) and O(H^(-2/3)ell^-3). The identity b^T m=d_H
also makes the first-B error zero, within its original
O(ell^-1+H^(-1/2)ell^2) allowance. No O(sqrt(ell)) perturbation
is charged to either tiny odd tolerance.

For first D, the identity
a^2/20+h^2/12=W/15-Re(R^2 Z^2)/60 checks the coefficient in
the imported trace. Equation (13) and the unchanged response limits
give -c^2 S ell/15+o(ell). The trace remainder costs O(1), because
E_H(wg_H)=1 and ell/log(2+t) is bounded; D_R, A_H and mean
terms cost O(sqrt(ell)). This is precisely the required o(ell)
error. The nonnegative rare x-second mass has integral Q_11,
and both w A_H,11 and w m_1^2 have the stated integrated bounds.
With K_11=1 this proves (19) for every bounded complex test.
Taking U=W^2 and each fixed p^(-it) gives their original o(ell)
tolerances using L429's unchanged actual coefficients.

For the cubic, expand DB at X=m+xi. Centered symmetry cancels
the centered linear and cubic terms. The three remaining terms are
exactly the conditional identity preceding (20), since
E xi xi^T=Sigma and E xi^T J xi=tr(J Sigma). Their modulus is
O(||Sigma||+1). The integrated bound uses
E_H(w||Sigma||)<=ell||K||E_H(wg_H)+W_H||A_H||=O(ell),
rather than the coarser pointwise bound. This is a signed conditional
expectation estimate; no absolute cubic estimate of this size is
asserted. The high absolute cubic is O(ell), so (11) proves (20)
for each fixed bounded test. Exact (7) gives all three old O(ell)
remainders, including the P-weighted one. Uniform convergence in
(8) gives the remaining fixed-character o_v(ell^2) assertions for
the very same law, without a growing-character statement.

Every selected quartic is homogeneous of degree four at the exact
response with bounded coefficients. L421 preserves its high integrand
exactly, including signed and zero leading coefficients. Added
intermediate and bulk costs are O(ell^(7/2)) and O(ell^(9/4)),
both o(ell^4). This accounts for all 23 quartics and the fourth
envelope. The high, intermediate and bulk costs for either absolute
third envelope are O(ell), O(ell^2), O(ell^(27/16)); all fit the
original O(ell^(9/4)) bound. Response, curvature, annulus and the
positive C bound stay exact. High states are either of norm ell^3
or fixed 2^(1/4) multiples of the actual jets; the other states have
smaller powers of ell. Bounded exact conversion coefficients and
ell^3 L(t)^j/T(t)^(1/2)->0 uniformly for j<=2 supply one fixed
enlargement of all qualitative physical constants.

Finally the absolute cap, unlike the signed cubic estimate, needs
no cancellation. The high component is O(ell) before capping.
Intermediate norm ell^(3/2) gives the eventual factor
ell^(-1/2)/lambda multiplying ell^2|F_H|. For bulk,
|DB|<=C|X|^3 and the cap is at most |X|/(lambda ell^2);
its O(ell^(9/4)) fourth cost gives O_lambda(ell^(1/4)). These
are exactly (3). The construction predates both lambda and the
subsequently tested character; only their limit onsets may depend
on those fixed tests.

No mathematical defect, construction repair or missing direct input
was found. The existing DAG edges and argument in PROOF.md do not
change. L436 still excludes a positive scalar calibration; the present
law uses positive probabilities at two different cubic signs. This
validates only the full three-prime diagnostic's limitation in the
selected relaxation. Actual/global realization, actual clipping,
capped nondegeneracy, L413's full-error regulator margin and global
mixed positivity remain unresolved. No RH range changes.

## Mathlib

Full matching coverage of this prescribed-response Borel family and
its asymptotic tolerances has not been checked. The standard inputs
are the named compact-group continuous-time averaging theorem and
real Schur--Horn theorem cited above, with the additional Borel
matrix implementation supplied by L419. The finite-height correction
is ordinary three-dimensional Gram linear algebra; its explicit proof
is needed because the qualitative averaging theorem supplies no
O(1/log H) rate for the full density. No source theorem or Mathlib
availability is inferred merely from terminology or absence of a match.
