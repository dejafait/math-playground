# L134 — Two negative torus scalars and two physical heat forms determine E

## Hypotheses

Import L101(4)--(5)'s established coefficient K_(i,E), with L097's
exact plane paths z_v and curvature projection S. Use both actual L010
probes i=3,6, SU(2), the straight lower-rooted direction-1 forest,
D=(-4,4)^4 with all-face relative fixed links, tau=1/16, and the bare
small-coupling coefficient at fixed mesh before refinement. This lemma
contracts the established continuum functional; it takes no new mesh
limit. Retain all real relative exterior modes, both displacement sectors,
the full lower prefix including its constant axial mode, and L101's
moving-cut endpoint term. No outside color or factor 3 is included.

Write V_k=v_k for L097/L080's physical transverse forest columns and
c_(i;kl)=exp[-(lambda_k+lambda_l)/16]q_i(A_k,A_l), with
A_k=f_k/sqrt(lambda_k). The f_k, lambda_k and q_i are exactly L080
and L008's normalized relative modes and full-displacement probe forms.
All transverse indices run over 2,3,4. Put

    W_a(x)=integral_(-4)^(x_1) partial_a u_a(t,x_T) dt,
    U_i=sum_(k,l)c_(i;kl) integral_D u_1 V_k dot V_l,
    W_i=sum_(k,l)c_(i;kl) integral_D sum_a W_a V_(k,a)V_(l,a). (1)

The distinction between W_a and the scalar heat form W_i is by index.
Use L132's already justified full-probe bounds N_3=6050,
N_6=1640736, mode-amplitude bound |V_(k,a)|<=1/2, and L081's
coefficient and Gaussian heat-sum bounds. They are applied below to
the different physical weights (1), with a separate support count.

## Conclusion

There are two universal real constants beta_E, alpha_E such that

    K_(i,E)=beta_E U_i+alpha_E W_i,
    -1<beta_E<0,  -7/4<alpha_E<0.                         (2)

Here are complete scalar integrals. With normalized torus measure,
X=4 sin^2(theta_2/2), Y=4 sin^2(theta_3/2),
Z=4 sin^2(theta_4/2), and L=X+Y+Z, set

    beta_E=-integral [(L^2-2 X Z)/(2 L)]
                                  (1-X/4)(1-X/L),
    alpha_E=-integral (X-Y)^2 Z(Z+4)/(8 L^2).              (3)

Set both integrands to zero at L=0. Both are bounded, absolutely
integrable, and tend to zero there. The formulas retain the moving-cut
u_1 term through beta_E; they do not remove it as a boundary term.
The strict signs in (2) are signs of universal constants, not signs
of K_(i,E), since U_i and W_i are signed actual-probe contractions.

The exact finite rectangular-cutoff forms U_i^[K], W_i^[K] have the
tensor/double-Laplace representation in proof section 4. Define

    H(K)=2(4*12^4)(16*12^3)*512/(9K)*exp(-9K^2/1024),
    C_U=160380, C_W=13783770.

Then the complete omitted-spectrum bounds are

    |U_i-U_i^[K]|<=C_U N_i H(K),
    |W_i-W_i^[K]|<=C_W N_i H(K),
    |K_(i,E)-beta_E U_i^[K]-alpha_E W_i^[K]|
                                <=(C_U+7 C_W/4)N_i H(K). (4)

At K=96 the last error is strictly below 10^-12 for both probes.
These are spectral omission errors only: neither universal scalar nor
retained physical heat form is numerically enclosed here. The axial
antiderivative R in section 3 needs its own retained spatial integration
justification; L133's saved moment table is not asserted to cover it.

This is local RESEARCH / REPRODUCTION progress under the unchanged ready
complete other/other assessment. L124's other coefficients ax,-Q,G,R
remain unevaluated. No sign or value of the full K_(i,oo)+4 gamma D_i,
compensation, finer remainder/logarithm, other response jets, finite
matching or interacting error <=c_box/2 follows. Continuum field axioms,
reflection positivity, infrared control and finite positive mass remain
independent gaps. No Yang--Mills candidate exists.

## Proof

### 1. Contract the actual paths on gradient inputs

Let d_a=2 sin(theta_a/2), eta_a=cos(theta_a/2), lambda=sum_a d_a^2.
Let Zc have rows -d_nu e_mu^T+d_mu e_nu^T in planes (23),(24),(34).
Thus P=dd^T/lambda and S=Zc Zc^T/lambda. Expansion of L097's
paths, without changing their phases, gives

    (z_v)_(mu nu)=-2 eta_nu v_nu e_mu^T
                          +2 eta_mu v_mu e_nu^T+i v_mu (Zc)_(mu nu).

The imaginary row annihilates d. Consequently

    z_v d=f(v)=-2 Zc diag(eta)v,
    z_v P=f(v)d^T/lambda,
    S f(v)=f(v).                                         (5)

Indeed Zc^T Zc=lambda I-dd^T, and Zc d=0, so S Zc=Zc.
For real physical v,w the complete path trace is therefore

    Tr[P z_v^* S z_w P]=f(v)^T f(w)/lambda
                      =4 v^T diag(eta)(I-P)diag(eta)w.    (6)

No path, plane, component, or covariance frequency has been omitted.
This is an exact contraction within the imported L101 functional,
not a deletion of a differentiated base-law projection zero.

Put X_a=d_a^2, lambda=sum X_a, and

    p_j=(t_j^2-d_j^2)/lambda-cos(theta_j)/2
       =-1/2+X_j/4-X_j^2/(4 lambda),
    q=(sum_j t_j^2)/(2 lambda)-1
       =-1/2-(sum_j X_j^2)/(8 lambda),
    h_a=eta_a^2(1-X_a/lambda),

where t_j=sin(theta_j). L101's multiplier divided by lambda is
exactly sum_j W_j p_j+u_1 q, including its endpoint contribution.
Every p_j,q is even in each angle. The off-diagonal physical entry
of (6) has a factor eta_a eta_b d_a d_b/lambda, a!=b, which is
odd in theta_a. Its integral against each of these multipliers is
zero by reflection of that angle. All entries are bounded, so this
parity argument uses absolutely integrable functions.

Coordinate permutations of the complete torus show that

    e_parallel=4 integral p_a h_a,
    e_perp=4 integral p_j h_a (j!=a),
    e_0=4 integral q h_a                               (7)

are independent of the chosen equal or distinct indices. Inserting
(6)--(7) into L101(5) gives the full physical expression

    sum c integral_D sum_a V_(k,a)V_(l,a)
        [e_perp sum_j W_j+(e_parallel-e_perp)W_a+e_0 u_1]. (8)

L008's actual displacement is divergence free, and u_1 vanishes at
the lower face. Thus sum_j W_j=-u_1 exactly. Equation (8) proves
(2) with beta_E=e_0-e_perp and alpha_E=e_parallel-e_perp. The heat
and amplitude bounds used in section 5 justify all full mode sums;
alternatively the calculation may first be made at finite K.

### 2. Keep the endpoint contribution and prove the scalar signs

Take a=2 and j=3 in (7), and use X,Y,Z,L from (3). Direct algebra gives

    q-p_3=-(X^2+Y^2+Z^2+2Y(X+Z))/(8L)
         =-(L^2-2XZ)/(8L).

Hence beta_E=4 integral(q-p_3)h_2 is exactly (3). The numerator
is strictly positive almost everywhere, as are h_2 and L. Thus
beta_E<0. Also

    beta_E=-integral (L/2)h_2+integral (XZ/L)h_2.

Independent angle averages give integral X=integral Y=integral Z=2
and integral(1-X/4)=1/2. Since L h_2=(Y+Z)(1-X/4), the first
term is -1. The second is strictly positive, proving beta_E>-1.
This computation includes q; dropping the moving-cut endpoint would
change q and invalidate both the scalar formula and its bounds.

For alpha_E, exchange angles 2 and 3 in one copy of its integral:

    alpha_E=2 integral (p_2-p_3)(h_2-h_3).

The exact differences are

    p_2-p_3=(X-Y)Z/(4L),
    h_2-h_3=-(X-Y)(Z+4)/(4L).

Their product proves the second formula in (3). It is strictly negative
after integration, since the positive integrand is nonzero on an open
set. Moreover (X-Y)^2/L^2<1 almost everywhere. The independent
single-angle moments integral Z=2, integral Z^2=6 follow by expanding
Z=2-2 cos(theta_4). Therefore

    0<-alpha_E<integral Z(Z+4)/8=(6+8)/8=7/4.

Near L=0, h_2<=1 and (L^2-2XZ)/(2L)<=L/2, so the beta integrand
tends to zero. The alpha integrand is bounded above by Z(Z+4)/8,
which also tends to zero. This proves the corner qualification and
absolute convergence in (3) without numerical quadrature.

### 3. Actual cumulative weights, including their upper axial tail

Set r=rho, f(x)=x rho(x), and R(x)=integral_(-4)^x r(t)dt.
L008/L132's complete displacement is

    u_1=f tensor r tensor f' tensor r,
    u_2=r tensor f tensor r tensor f',
    u_3=-f' tensor r tensor f tensor r,
    u_4=-r tensor f' tensor r tensor f.

Integrating the actual diagonal strains along direction 1 yields

    W_2=R tensor f' tensor r tensor f',
    W_3=-f tensor r tensor f' tensor r=-u_1,
    W_4=-R tensor f' tensor r tensor f'=-W_2.           (9)

Here integral f'=f because f(-4)=0. Neither Psi_13 nor Psi_24 has
been removed from the probes or from (9). R need not vanish above 3:
it is constant there and is retained through x_1=4. Thus W_2,W_4
are not assumed compactly supported in the axial coordinate. Their
transverse support remains in [-3,3]^3. No integration by parts at
the upper axial face, bulk-prefix replacement, or boundary-domain
identification is used. The sum in (9) confirms sum_a W_a=-u_1.

### 4. Exact finite tensor and double-Laplace representation

At rectangular cutoff K retain every allowed component-labeled relative
mode with coordinate indices <=K, as in L080/L132, including k_1=0
on component 1. Let L_F map a smooth one-form to its transverse lift
A_T-grad_T integral_(-4)^(x_1) A_1. This L_F is a physical mode map,
distinct from the torus scalar L in (3). Define real symmetric matrices

    (M_U,K)_kl=integral_D u_1 (L_F f_k) dot (L_F f_l),
    (M_W,K)_kl=integral_D sum_a W_a(L_F f_k)_a(L_F f_l)_a,
    (Q_i,K)_kl=q_i(f_k,f_l),
    (F_K)_kk=exp(-lambda_k/16)/lambda_k.

Both full probe displacement sectors occur in Q_i,K. Scaling each
of the two fields in both q_i and M by 1/sqrt(lambda) proves

    U_i^[K]=Tr(M_U,K F_K Q_i,K F_K),
    W_i^[K]=Tr(M_W,K F_K Q_i,K F_K).                  (10)

No factor 2, 3 or 6 is supplied by this finite trace identity. It
contracts the already normalized E coefficient of L101 and L124.

Every M entry has an exact finite separable expansion: use (9) for
W and the displayed u_1 for U. A lift row has its direct component-a
mode and its negative component-1 prefix row, whose axial functions are

    p_0(x_1)=(x_1+4)/sqrt(8),
    p_n(x_1)=sin(n pi(x_1+4)/8)/(2 n pi/8), n>=1,

and whose direction-a transverse factor is v'_n. The other factors
are L080's ordinary normalized e_n or v_n. Multiply both lift rows
for each a and retain all four direct/prefix pairings. There is no
extra ell=x_1+4 multiplying the physical weights in (1); it occurs
only inside the constant prefix p_0. Use L132 proof section 2's full
curvature-row and polarization instructions for Q_i,K without its
physical H weights. Each signed coefficient product has matrices

    (I_j)_mn=integral_(-4)^4 weight_j(x)
                               left_(j,m)(x)right_(j,n)(x) dx,

with weights from (9), u_1, and the full q_i. These include R where
it appears. They specify every component-block term of (10) as an
ordinary tensor product. No stored numerical table substitutes for
these exact one-dimensional integrals.

Insert exp(-lambda/16)/lambda=integral_(1/16)^infinity exp(-t lambda)dt
on both sides of Q. The relative eigenvalue gap is >=3 pi^2/64.
Each matched component-block term is therefore an absolutely convergent
double integral of the product of four one-dimensional traces, exactly
as in L132 proof section 2. This provides a finite evaluable tensor,
retaining both inverse factors, every mode below K and every prefix.
Retained spatial/time and arithmetic errors require a later enclosure.

### 5. Complete exterior spectral tail for these different weights

L081's coefficient bounds give |u_1|<=165. Also 0<=R<=6, because
0<=r<=1 and its support has length 6. With |f'|<=55 and |r|<=1,
(9) implies |W_2|,|W_4|<=18150 and |W_3|<=165. The support of
u_1 has volume <=1296. All W_a vanish for x_1<-3 and outside the
transverse cube [-3,3]^3, so their joint support in D has volume
<=7*6^3=1512. This larger axial support is included explicitly.

For each normalized pair k,l, |V_(k,a)|<=1/2 from the complete
length-eight prefix estimate in L081/L132. Consequently the absolute
physical integrals in (1) are bounded by

    1296*165*3/4=160380=C_U,
    1512*(18150+165+18150)/4=13783770=C_W.            (11)

L132's full probe norm bound gives |c_(i;kl)|<=N_i times the two-label
heat weight. L081 proof section 4 bounds the complete one-label heat
sum by 4*12^4 and its cutoff complement by
16*12^3*512/(9K)*exp(-9K^2/1024). The union where either label is
omitted gives exactly H(K). Multiplying these bounds by (11) proves
the first two inequalities in (4), absolute convergence, and the
justified full-sum manipulations above. Bounds (2) then prove the third.

At K=96, H(K)=2717908992 exp(-81). The positive Taylor series gives
e^3>20, so exp(-81)<20^-27. Even with the larger N_i, the third
bound is strictly less than the exact rational number

    [(160380+7*13783770/4)*1640736*2717908992]/20^27
       < 10^-12.                                     (12)

The rational comparison is recorded in
scripts/combined-ward-response/e-physical-tail-arithmetic-certificate.json.
It uses exact integer/fraction arithmetic; it is not a retained torus
or physical numerical evaluation and invokes no IEEE model. The strict
scalar signs and effective spectral tail make E a two-form evaluation
problem, without resolving its signed value or the full comparison.

Reproduce the exact polynomial and rational checks from the notebook with

    python3 scripts/combined-ward-response/check_e_physical_reduction.py

All three polynomial identities pass with zero coefficient differences;
the rational bound in (12) is 40338318568383/50000000000000000000000000,
approximately 8.067663714e-13, below 10^-12. The complete selected
polynomial and tail certificate records were inspected. These checks
support the displayed algebra and arithmetic; the path projection,
scalar signs, physical support and full-spectrum proof are given above.

## Mathlib

Full matching physical E reduction and spectral-tail theorem: **not checked**.
Supporting finite matrix traces, projection identities, reflection/permutation
symmetry of integrals, finite tensor products, Laplace transforms and
Gaussian tails: **not checked**. Unknown availability is not absence.
