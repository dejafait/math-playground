# C212g — Bound the complete cubic-probe derivative correction

## Hypotheses

Use L212's bare fixed-mesh SU(2) expansion in the relative box
(-4,4)^4, admitted even meshes a=8/N, the straight lower-rooted
direction-1 forest, L008's complete displacement, and both actual
L010 probes i=3,6 at tau=1/16. Refinement follows the bare expansion.
All coordinates, norms and adjoints are ordinary dimensionless full
variable-link coordinates, with three colors and every normal end edge.
Fixed boundary links have zero coordinates. Vertex potentials are
pinned on every physical face, including the upper prefix endpoint.

Keep C=D_1, D=D_0, L=C^T C, Delta=L+DD^T, and

    P=I-D(D^TD)^(-1)D^T, S=P Delta^(-1)P,
    H_s=exp(-s Delta/a^2), E_s=exp(-s L/a^2).

Let z have independent colors of covariance S. Retain L018's actual
symmetric A=PAP, with both residual insertion subtractions, and put

    r(z)=sum_c (z^c)^T A z^c, t(z)=2SAz, M=2SAS,
    V=q Phi, F=D Phi,
    b(z)=[z,Vz]/2-[Fz,Vz]/4.                         (1)

The bracket and actual pinned prefix Phi are exactly L212's. In this
file F without subscripts denotes D Phi, not a probe polynomial.
F_(i,3) denotes the entire ambient cubic flowed numerator from L212;
its derivative is taken on full-link fields, not just on im P.
Let B_i, c(z), and K_(i,a)=kappa_0(f_(i,2),r_0) retain L212's meanings.

## Conclusion

For each of the two actual probes,

    |Cov_S(dF_(i,3)(z)[b(z)],r)|
                       <=C_i N^(5/2) log(eN).       (2)

Its a^3-scaled response therefore tends to zero. Combining this with
C212a,b,c,f gives the quantitative reduction

    K_(i,a)=Cov_S(j_(i,2)(Z)+2<B_i z,c(z)>,r)
                              +O_i(N^(5/2)log(eN)), (3)
    |K_(i,a)|<=C_i N^3,                             (4)

where Z is C212c(1)'s full co-closed quadratic-flow jet. For each
fixed 0<delta<=tau/2, Z in (3) can be replaced by Z_delta with an
O_(i,delta)(N^(5/2)log(eN)) error. Thus the complete quartic response
is cubic-bounded, and its possible cubic limit is determined by the
joint initial/initial two-flow square plus the cubic endpoint response.
Neither separate limit nor convergence of their sum is established.

The achieved scaled error is O(N^(-1/2)log(eN)), which tends to zero;
bounded scaled values in (4) are not convergence. Full compensation,
finer powers/logarithms, finite matching, reflected error <=c_box/2,
continuum axioms and infrared finite positive mass remain unresolved.
This is local reproduction/specialization of existing Gaussian and
prefix estimates, without a claim beyond the sources checked.

## Proof

### 1. Differentiate the ambient cubic, retaining undamped gradients

Let T polarize the complete full-link action cubic and T_i polarize
the actual unflowed numerator cubic. Set

    J_s=H_(tau-s) Q_i H_tau.

The full-coordinate formula L181, proof section 3, (10), applies with
the initial full-link field w in place of the forest inclusion:

    F_(i,3)(w)=T_i(E_tau w,E_tau w,E_tau w)
       -(6/a^2) integral_0^tau T(E_s w,E_s w,J_s w) ds. (5)

Indeed its input flow is E_s w; the coordinate quadratic field is
-a^(-2) grad script S_3, and d script S_3(y)[h]=3T(y,y,h).
The outer factor 2 is the quadratic observable derivative. Its
external map equals J_s on the entire space: Q_i=P Q_i P and
E_s P=H_s P, so E_(tau-s)Q_i E_tau=H_(tau-s)Q_i H_tau.
This is the same finite Taylor formula, not a transfer of a forest
jet. It is valid for arbitrary w, which is necessary for its derivative.

At the co-closed z, E_s z=H_s z, but E_s b need not equal H_s b.
Differentiating (5) gives the exact three groups

    O_i(z)=3T_i(H_tau z,H_tau z,E_tau b(z)),
    U_i^short(s,z)=-(12/a^2)T(E_s b(z),H_s z,J_s z),
    U_i^ext(s,z)=-(6/a^2)T(H_s z,H_s z,J_s b(z)),
    dF_(i,3)(z)[b]=O_i+integral_0^tau(U_i^short+U_i^ext)ds. (6)

The two short placements coincide by symmetry of T and have already
been combined in -12. There is no derivative of b in (6): it is a
direction in the derivative of F_(i,3). Its dependence on z remains
in the subsequent covariance, which differentiates both inputs of b.

### 2. A contraction identity for the short placements

Use the normalized Gaussian tilt exp(lambda r) at each fixed mesh,
restricted to im P. For sufficiently small |lambda| it is integrable,
its three colors remain independent with common covariance S_lambda,
and S'_0=M. For example 2|lambda| ||S^(1/2)AS^(1/2)||<1 suffices.
No uniform tilt interval is needed. Finite polynomial Gaussian
domination justifies differentiation; a linear Gaussian representation
handles the singular ambient covariance. The derivative of an
expectation of a fixed polynomial is exactly its covariance with r.

For a full product mode e_l and color c, put

    h_l^c=S e_l in color c, k_l^c=M e_l in color c,
    X_l^c(z)=db(z)[k_l^c]+d^2b[h_l^c,t(z)].          (7)

Zero entries are understood in other colors. All linear maps act
identically on colors. Consequently E_lambda b=0 for every lambda:
each bracket component is a sum of products in two distinct colors.
For any fixed deterministic v, Gaussian integration by parts gives

    E_lambda[(e_l^T z^c) T(E_s b(z),H_s z,v)]
       =E_lambda[T(E_s db(z)[S_lambda e_l^c],H_s z,v)]. (8)

Differentiating the H_s z slot during this integration by parts would
give T(E_s E_lambda b,H_s S_lambda e_l^c,v)=0. This zero holds
throughout the tilt, so its derivative also vanishes; no base-law
projection zero is differentiated as if it persisted.

Differentiate (8) at lambda=0. The derivative of S_lambda e_l^c
gives db(z)[k_l^c]. The remaining expectation is bilinear in two
linear images of z, since db(z)[h] is linear in z. For any such
bilinear expression, its covariance derivative M can be placed
entirely on its first random input, because

    (2SA)S=S(2SA)^T=M.                              (9)

In indices this says d E_lambda[z_alpha z_beta]/d lambda=M_alpha beta
=E[t_alpha z_beta]. It needs no commutation of A and S. Thus this
part is d^2b[h_l^c,t(z)], not half of it and not a second copy.
Equation (8) proves the exact signed response identity

    Cov_S((e_l^T z^c)T(E_s b,H_s z,v),r)
                  =E[T(E_s X_l^c,H_s z,v)].         (10)

This keeps the external covariance derivative and the other covariance
derivative once each. In particular it incorporates all four original
Gaussian input derivatives without applying a spurious single-quartic
factor 1/2 to the already differentiated covariance. It is consistent
with L212(12), where that factor accompanies a different representation.

### 3. Full-prefix bounds for X before projection

L192, proof sections 1–2, supplies the following estimates in precisely
these coordinates. Write ||Y||_G=(E||Y||_ell2^2)^(1/2). For a fixed
polynomial p(l), uniformly over all rows and modes,

    ||h_l||_infinity<=C p(l),
    ||k_l||_infinity<=C a^2 p(l),
    ||z||_G<=CN^2, ||t||_G<=CN^3,
    ||Vz||_G+||Fz||_G<=CN^(5/2),
    ||Vt||_G+||Ft||_G<=CN^(7/2),
    ||Vh_l||_infinity+||Fh_l||_infinity<=CN p(l),
    ||Vk_l||_infinity+||Fk_l||_infinity<=CN^(-1)p(l). (11)

The h_l bound uses the complete relative eigenspace estimate for
P e_l, not a supremum contraction of P. The k_l bound is the smooth
external column M e_l estimate. The trace bounds use the full pinned
prefix covariance, including its upper jump and the constant axial
mode; the deterministic prefix counts allow its full N-row sum.
No smoothness is assigned to t. All assumptions here match L192.

For clarity the actual pre-projection expressions are

    d^2b[h,t]=([h,Vt]+[t,Vh])/2
                       -([Fh,Vt]+[Ft,Vh])/4,
    db(z)[k]=([k,Vz]+[z,Vk])/2
                       -([Fk,Vz]+[Fz,Vk])/4.        (12)

Pointwise bracket bounds and (11) give, in the order written, powers
N^(7/2), N^4, N^(9/2), N^(9/2) in the first line and
N^(1/2), N, N^(3/2), N^(3/2) in the second. Hence

    ||X_l^c||_G<=C p(l)N^(9/2).                     (13)

L192 applies P only after this count. We use the count before P;
no estimate on a projected field is reversed. In particular normal
upper-output rows and the gradient part of X are still present.

### 4. Integrate the complete short response with the full semigroup

L193, proof section 1, (4)–(6), gives the entire external expansion

    J_s=a^2 sum_(k,l) d_(i;kl)(s)e_k e_l^T,
    sup_(0<=s<=tau) sum_(k,l)|d_(i;kl)(s)|p_0(k)p_0(l)<infinity, (14)

for every fixed polynomial p_0. Its regularity proof uses the actual
compact smooth probe stencils, so it includes s=tau without assuming
positive output heat. The same complete relative modes satisfy
||e_k||_infinity<=Ca^2 and ||C e_k||_infinity<=Ca^3 p(k).
Every allowed constant own-direction mode is included.

Insert (14) in U_i^short and apply (10) with v=e_k^c. Exactly,

    Cov_S(U_i^short(s),r)
       =-12 sum_(k,l,c)d_(i;kl)(s)
                         E[T(E_s X_l^c,H_s z,e_k^c)]. (15)

The a^2 in J_s cancels a^(-2) once. T's symmetry has already supplied
the two short placements; the displayed color sum supplies no extra
outside factor.

Put rho=s+a^2. L192(13)'s full-spectrum trace bounds give

    ||H_s z||_G<=Ca^(-1)rho^(-1/2),
    ||C H_s z||_G<=C rho^(-1).                       (16)

On the full space, rather than only im P, singular-value calculus gives

    ||E_s||_op<=1, ||C E_s||_op<=Ca rho^(-1/2).       (17)

For s>0 the second follows by maximizing sigma exp(-s sigma^2/a^2)
over the bounded singular spectrum of C; at zero use ||C||<=C.
The gradient kernel contributes zero only after C. Thus (17) retains
the undamped gradient in the first norm and is valid on X_l^c.

L192(14) proves, for arbitrary full-link fields,

    |T(x,y,v)|<=C{||Cv||_infinity ||x|| ||y||
              +||v||_infinity(||Cx|| ||y||+||x|| ||Cy||)}. (18)

It keeps all three action-circulation placements and all fixed-link
zeros. Apply (18) with x=E_s X_l^c, y=H_s z, v=e_k^c and use
Gaussian Cauchy--Schwarz, not independence. Equations (13),(16),(17)
give

    |E T(E_s X_l^c,H_s z,e_k^c)|
       <=C p(k)p(l)a^(-5/2)[rho^(-1/2)+rho^(-1)].   (19)

Explicitly the three factors outside ||X_l||_G are
a^3 a^(-1)rho^(-1/2), a^2 a rho^(-1/2)a^(-1)rho^(-1/2),
and a^2 rho^(-1), respectively. This checks every circulation
placement and does not require X_l to be co-closed.
Summing by (14) in (15), then integrating the entire interval, yields

    integral_0^tau |Cov_S(U_i^short(s),r)|ds
                         <=C_i N^(5/2)log(eN),      (20)

since the two integrals are 2(sqrt(tau+a^2)-a) and
log(1+tau/a^2). In particular the region s<a^2 is estimated, not
discarded, and no interchange with a mesh limit was used.

### 5. External placement and final observable

Since J_s=J_s P, its expansion (14) on b can use
b_l^c=<(P e_l),b^c>. Put F_k^c(s)=T(H_s z,H_s z,e_k^c).
Both F_k^c and b_l^c are centered bilinear polynomials in the two
colors other than c. This follows from the alternating SU(2) action
tensor and bracket; internal pairings vanish for every S_lambda.
Isserlis' fourth-moment formula therefore leaves only their two
cross pairings. Differentiating these pairings gives exactly

    Cov_S(F_k^c(s)b_l^c,r)
                    =E[F_k^c(s) db_l^c(z)[t(z)]].    (21)

Each of the two b inputs contributes one of the differentiated
cross covariances through (9). There is no positivity assertion for M
and no missing disconnected term. This is the two-polynomial
cross-contraction identity, not a factorless application of the
single-quartic rule.

L191(13),(15) give

    ||db_l^c[t]||_2<=C p(l)N^3,
    ||F_k^c(s)||_2<=C a p(k)m_a(s),
    m_a(s)=ell(s+a^2)^(1/2)
                  +(s+a^2)^(-1/2)ell(s+a^2)^(1/4),
    ell(u)=1+log(1+1/u).                            (22)

The local tensor and spectrum estimates proving (22) apply for all
0<=s<=tau. Their use of an exterior expansion is now justified at
the final endpoint by (14), exactly as in L193(15). L189, proof
section 5, supplies a mesh-independent integrable majorant for m_a.
Equations (14),(21),(22), with the -6 from (6), consequently give

    integral_0^tau |Cov_S(U_i^ext(s),r)|ds<=C_i N^2. (23)

Finally expand one of the two H_tau z factors in O_i using the full
heat basis. Apply (10) with T_i in place of T, s=tau, and v=e_l^c
in place of its arbitrary deterministic argument. The proof of (10)
used only trilinearity, so it applies to T_i as well. Precisely,

    Cov_S(O_i,r)=3 sum_(l,c)exp(-tau lambda_l)
                       E[T_i(E_tau X_l^c,H_tau z,e_l^c)]. (24)

L193, proof section 4, proves (18) for this actual T_i: the triplet
has its complete plaquette cubic and the shear both linear/quadratic
clover orders. At time tau, (16) is O(a^-1), O(1), and (17) is
1, O(a). Thus the expectation in (24) is at most
C_i p(l)^2 a^2 N^(9/2)=C_i p(l)^2 N^(5/2). The full heat sum
converges uniformly by the physical spectral gap and shell count,
giving

    |Cov_S(O_i,r)|<=C_i N^(5/2).                    (25)

All time integrands are finite-mesh polynomials with continuous
coefficients on a compact interval, so covariance commutes with their
time integration at fixed mesh. Equations (6),(20),(23),(25) prove (2).

### 6. Return to the complete target and check the scope

L212(4),(9) contains exactly the co-closed F_(i,4), the correction
estimated here, <b,B_i b>, and 2<B_i z,c>. C212f(3) replaces the
first response by j_(i,2)(Z) with O(N^2 log(eN)) error. C212a(2)
removes the third with O(N^(5/2)) error. Together with (2) these prove
(3). C212b(5) and C212c(2) bound the two retained responses by O(N^3),
proving (4), since log(eN)<=C sqrt(N). C212c(3) separately estimates
both cross rectangles and the complement square when Z is replaced
by Z_delta. Its O_delta(N^2 log(eN)) error proves the stated
fixed-delta version. No delta-uniform removal of the initial square
or separate convergence of these two retained terms is assumed.

Verification is analytic: (8)–(10) and (21) count the differentiated
Gaussian covariance factors exactly, (12) checks both prefix slots
before projection, and (16)–(20) integrate the full spectrum and both
time endpoints. No numerical preview or synthetic fixture supplies
an asymptotic premise. Neither P nor a prefix is commuted through the
tilt or full flow, and no field with an upper jump is declared smooth.
The remaining sum in (3) may require a joint limit even if its separate
limits fail. This result supplies boundedness and a reduction, not
that limit, compensation, or a Yang--Mills construction.

## Mathlib

Full matching result: **not checked**. Supporting coverage of Gaussian
integration by parts, Isserlis' theorem, relative-cochain heat bounds
and finite tensor estimates: **not checked**; unknown is not absence.
The named standard inputs are Gaussian integration by parts and
Isserlis' fourth-moment theorem, with their exact singular-Gaussian,
color and normalized-tilt specializations given in (8)–(10),(21).
The required local flow, smooth-column, prefix and spectrum estimates
are imported under unchanged hypotheses from the cited canonical
results. The reused
[assessment](../drafts/literature/2026-10-16-complete-quartic-probe-jet-scale.md)
approves this bounded attempt within the complete quartic target.
No general flow-renormalization theorem is reproved or imported as
a bound for this selected bare cumulant.
