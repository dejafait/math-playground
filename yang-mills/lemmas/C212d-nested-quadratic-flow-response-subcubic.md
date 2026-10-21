# C212d — Remove the complete nested quadratic-flow response at cubic scale

## Hypotheses

Use L212's SU(2) setting: relative box (-4,4)^4, admitted even
N, a=8/N, the straight lower-rooted direction-1 forest, the complete
displacement and both actual probes i=3,6 at tau=1/16. Take the bare
expansion at fixed mesh before refinement. All coordinates, transposes
and norms are ordinary dimensionless full variable-link coordinates.
Fixed links have zero Taylor coordinates. Include every variable
normal end edge and all physical boundary plaquettes.

As in C212c put C=D_1, L=C^T C, Delta=L+DD^T,
P=I-D(D^T D)^(-1)D^T, S=P Delta^(-1)P,
H_s=exp(-s Delta/a^2), E_s=exp(-s L/a^2). Let z have three
independent colors with covariance S. Keep the actual symmetric
A=PAP, including both residual insertion subtractions, and set

    r(z)=sum_c (z^c)^T A z^c, v(z)=2SAz.

The full coordinate quadratic Wilson-flow field is C212c's
Q_2(y)=-a^(-2) grad script S_3(y). For 0<=s<=tau define

    y_s=H_s z,
    Z_s=integral_0^s E_(s-u) Q_2(y_u) du,
    Y=integral_0^tau E_(tau-s) DQ_2(y_s)[Z_s] ds.      (1)

Thus Y is precisely the entire nested DQ_2 z_2 part of L011(11)'s
third flow jet, on the co-closed input z. It does not include Q_3.
Let j_(i,2)(w)=sum_c (w^c)^T Q_i w^c be the actual unflowed
quadratic numerator, with Q_i symmetric and Q_i D=0. Select the
single complete quartic polynomial

    P_(i,nest)(z)=Dj_(i,2)(H_tau z)[Y].               (2)

It occurs inside F_(i,4)(z) in L212's joint retraction. It is not
the corresponding isolated summand on the forest input Rz.

## Conclusion

For both actual probes,

    |Cov_S(P_(i,nest),r)|<=C_i N^2 log(eN),
    a^3 Cov_S(P_(i,nest),r) -> 0.                     (3)

Useful full-jet estimates, with ||X||_(p,2)=(E||X||_ell2^p)^(1/p),
hold for every fixed 2<=p<infinity, uniformly on 0<=s<=tau:

    ||Z_s||_(p,2)<=C_p a^(-2),
    ||C Z_s||_(p,2)<=C_p a^(-1)(s+a^2)^(-1/2).       (4)

Their derivatives dZ_s(z)[v(z)] satisfy the same bounds multiplied
by N. In particular (4) retains the gradient part of Z_s; it is
not obtained by replacing E_t on this nonlinear field by H_t.

This removes only the selected nested contribution at cubic scale.
C212c's two-quadratic-flow response and C212b's cubic endpoint still
lack limits. Q_3, the other co-closed observable jets and
dF_(i,3)[b] remain outside this bound. No complete quartic response
bound/limit, compensation, finer remainder, finite matching,
interacting reflected estimate <=c_box/2, continuum axioms or
infrared finite positive mass follows. This is a local specialization
of existing finite action, heat and Gaussian estimates, without a
claim of progress beyond the sources checked.

## Proof

### 1. Keep the two full action-derivative pieces

C212c(7),(9)--(10), with its complete plaquette words, gives

    grad script S_3(y)=C^T W(y)+V(y),
    script S_3(y)=sum_p <(Cy)_p,W_p(y)>,              (5)

where W_p is quadratic in the four signed plaquette links, and
V is a finite sum of products of a link and a neighboring circulation.
All local coefficients and row/column incidence counts are uniformly
bounded, including at physical faces. For y_u=H_u z,

    sup_e ||(y_u)_e||_Lp<=C_p a/(u+a^2)^(1/2),
    sup_p' ||(Cy_u)_p'||_Lp<=C_p a^2/(u+a^2),
    ||W(y_u)||_(p,2)<=C_p/(u+a^2),
    ||V(y_u)||_(p,2)<=C_p a/(u+a^2)^(3/2).           (6)

These estimates include u=0, all relative spectral modes and all
normal end rows. The mixed-norm estimates follow by Holder on each
quadratic entry, then Minkowski and the O(a^(-4)) row count, exactly
as in C212c. Use input moments of order 2p for a quadratic product.

L186(12), also used in C212c(8), gives

    Cov(v)=4SASAS<=C N^2 S.                          (7)

Indeed ||S^(1/2)AS^(1/2)||<=C N and its square is positive, even
though the signed covariance tilt 2SAS need not be. Every linear
image of v therefore satisfies the corresponding Gaussian moment
bound for the same image of z, multiplied by C_p N. Differentiating
W(y_u) and V(y_u) replaces each of their two linear inputs in turn
by H_u v; Holder proves their differentiated bounds (6) with the
same additional N. This keeps correlations, both input placements
and both subtractions, without declaring v independent or smooth.

### 2. Two time convolutions bound the full intermediate jet

Singular-value calculus for C, including its gradient kernel, gives
for t>=0, with the bounded branch used at t=0,

    ||E_t||<=1,
    ||E_t C^T||, ||C E_t||<=C min(1,a/sqrt(t)),
    ||C E_t C^T||<=C min(1,a^2/t).                   (8)

The nonzero singular values contribute sigma exp(-t sigma^2/a^2)
and sigma^2 exp(-t sigma^2/a^2). The uniformly bounded incidence
norm supplies the small-t branch. The full E_t is retained in (8).

For clarity the dimensionless time convolutions needed below are,
with T>=0 and k_b(r)=min(1,r^(-b)) (k_b(0)=1),

    F_b(T)=integral_0^T k_b(T-t)/(1+t) dt,
    G(T)=integral_0^T k_(1/2)(T-t)/(1+t)^(3/2) dt.

They obey

    F_(1/2)(T)<=C,
    F_1(T)<=C log(e+T)/(1+T)<=C/(1+T)^(1/2),
    G(T)<=C/(1+T)^(1/2).                             (9)

For T<=2 these follow from boundedness of the integrands. For T>2
split at T/2. The first half of F_b is at most
C T^(-b) log(1+T), and its second half is at most
C T^(-1) integral_0^(T/2) k_b(r) dr. The latter integral is
O(sqrt(T)) for b=1/2 and O(log(eT)) for b=1. This proves both
F bounds, using boundedness of log(e+T)/sqrt(1+T). For G its first
half is O(T^(-1/2)), since integral_0^infinity (1+t)^(-3/2)dt=2.
Its second half is O(T^(-3/2)sqrt(T))=O(T^(-1)), proving (9).

Apply (5)--(8) in (1), using Minkowski in L^p of the Euclidean norm.
Set T=s/a^2 and u=a^2 t. The full jet is bounded by

    ||Z_s||_(p,2)
      <=C_p a^(-2) integral_0^s {
          k_(1/2)((s-u)/a^2)/(u+a^2)
                         +a/(u+a^2)^(3/2)} du
      <=C_p a^(-2) [F_(1/2)(T)+2]
      <=C_p a^(-2).                                 (10)

The second term used only ||E_t||<=1; it includes the entire
undamped gradient component. After circulation the same argument gives

    ||C Z_s||_(p,2)
      <=C_p a^(-2) integral_0^s {
          k_1((s-u)/a^2)/(u+a^2)
          +a k_(1/2)((s-u)/a^2)/(u+a^2)^(3/2)} du
      <=C_p a^(-2)[F_1(T)+G(T)]
      <=C_p a^(-1)(s+a^2)^(-1/2).                   (11)

At s=0 Z_s=0, consistent with these upper bounds.
Using the differentiated (6) proves (10)--(11) for dZ_s[v] with
an extra factor N. Differentiation acts only on the polynomial
inputs, not on the deterministic propagators. All time integrals
are finite-mesh integrals; none is interchanged with a mesh limit.

### 3. Contract the external probe leg before the nested estimate

Put h_s=H_(tau-s) Q_i H_tau z. Since Q_i D=0, this equals
E_(tau-s) Q_i H_tau z, including s=tau. Self-adjointness and (1)
give exactly

    P_(i,nest)(z)
       =-2a^(-2) integral_0^tau
               d^2 script S_3(y_s)[h_s,Z_s] ds.     (12)

The factor 2 is Dj_(i,2); the minus sign and a^(-2) are in Q_2.
There is no additional response or outside color factor in (12).

L193(5)--(7), with its auxiliary time r=0, proves for all fixed
p<infinity, uniformly on the entire closed interval 0<=s<=tau,

    sup_e ||(h_s)_e||_Lp<=C_(i,p) a^3,
    sup_p' ||(C h_s)_p'||_Lp<=C_(i,p) a^4.           (13)

Its compact-stencil proof applies to these exact two Q_i forms:
every fixed physical difference of Q_(i,a)f_l is polynomially
bounded in the input product-mode index l, while the H_tau factor
supplies the full exponentially summable input spectrum. Arbitrarily
many differences give summable output-mode decay even at s=tau,
where no output heat remains. The circulation of each normalized
output product mode gains a factor a, on normal end rows as well.
Thus (13) is actual compact-probe regularity, not an assumption that
all nonlinear outputs are co-closed or smoothed. By (7), h_s(v)
and C h_s(v) obey (13) with an additional factor N.

Differentiating the complete cubic (5) twice gives the exact three
types, with the actual ordered local W unchanged,

    d^2 script S_3(y)[h,Z]
      =sum_p { <(Ch)_p,dW_p(y)[Z]>
              +<(CZ)_p,dW_p(y)[h]>
              +<(Cy)_p,d^2W_p(y)[h,Z]> }.            (14)

These are respectively finite sums of Ch*y*Z, CZ*y*h and Cy*h*Z.
No derivative slot is omitted. Correlation is handled by Holder:
for example E|linear_1 linear_2 quadratic|
<=||linear_1||_4 ||linear_2||_4 ||quadratic||_2.
For any selected shifted rows of a vector X, bounded incidence
multiplicity and Cauchy--Schwarz give

    sum_selected ||X_j||_2 <=C a^(-2)||X||_(2,2).    (15)

Here the number of selected plaquette/edge rows is O(a^(-4));
the finite boundary row sets satisfy the same bound. Consequently,
writing u_s=s+a^2, (6),(13)--(15) yield

    E|d^2 script S_3(y_s)[h_s,Z_s]|
      <=C_i [ a^3 u_s^(-1/2)||Z_s||_(2,2)
              +a^2 u_s^(-1/2)||C Z_s||_(2,2)
              +a^3 u_s^(-1)||Z_s||_(2,2) ].          (16)

Insert (10)--(11) and the a^(-2) in (12). The absolute integrand
is at most

    C_i a^(-1)[u_s^(-1/2)+u_s^(-1)].                (17)

Both closed-interval endpoints are controlled. In particular
integral_0^tau u_s^(-1)ds=log(1+tau/a^2), while
integral_0^tau u_s^(-1/2)ds<=2sqrt(tau). No initial interval
or inner-flow endpoint is discarded. This proves

    E|P_(i,nest)|<=C_i a^(-1) log(e/a).              (18)

### 4. Differentiate the complete polynomial under the signed tilt

At fixed mesh differentiate (12) in direction v(z). The result is
the sum of the three groups replacing y_s by H_s v, h_s by h_s(v),
and Z_s by dZ_s[v], respectively. In the last group both inner
quadratic inputs are differentiated as proved after (11). Since
script S_3 is cubic, its Hessian is linear in y_s, so these groups
exhaust the derivative. Directional differentiation does not
differentiate v itself. Equations (6)--(7),(10)--(11),(13) show that
each differentiated version of (16)--(17) costs at most an additional
factor C N. Holder still applies without independence. Hence

    E|dP_(i,nest)(z)[v(z)]|
       <=C_i N a^(-1) log(e/a).                     (19)

L212(12)'s normalized Gaussian tilt identity, valid also for the
singular ambient covariance, is

    Cov_S(P_(i,nest),r)=(1/2)E[dP_(i,nest)[v]].      (20)

Use (19) and a=8/N to prove (3). The Gaussian factor 1/2 is retained;
no positivity is assigned to A or 2SAS. Multiplying the bound by
a^3 gives O(log(eN)/N), which tends to zero. This is a proof of
the selected response limit, not a limit of either flow jet itself.

Verification is analytic: the exact Hessian split (14), the complete
two convolution estimates (9)--(11), and the full closed-interval
external bound (13) establish all-mesh inequalities. No mathematical
script, finite-mode preview or numerical test is used as evidence.
L212 retains the other observable and gauge-jet terms elsewhere;
no isolated higher forest polynomial has been transferred by a
quadratic quotient argument. The obstruction in L022 therefore
does not apply to the stated co-closed-input specialization.

## Mathlib

Full matching result: **not checked**. Supporting coverage of finite
cochain heat estimates, Gaussian moments and integration by parts,
singular-value calculus and norm inequalities: **not checked**.
Unknown availability is not evidence of absence. The standard inputs
are Holder, Minkowski and Cauchy--Schwarz, finite-dimensional Gaussian
moments and spectral calculus; their needed time convolutions and
specializations are given above. The reused
[assessment](../drafts/literature/2026-10-16-complete-quartic-probe-jet-scale.md)
does not import full renormalized-flow finiteness as a bound on this
bare selected response. No reproof of general flow renormalizability
is proposed.
