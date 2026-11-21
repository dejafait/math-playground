# C999l: A complete residual majorant for the fixed neutral endpoint head

## Hypotheses

Use C744v/w's complete real cosine matrices D,S,T on L2(0,ell),
ell=log(3)/2, C744z's actual separation14 operator U, moment map C,
H0=ker C, form domain V0 and restricted operator A0. Both complex
endpoints are independent. Keep C999k's exact reference R, with raw
head indices0,...,511, output split K=65536, d0=6.14, complement
fraction1/2 and penalty256. In particular its audited full-domain
order R<=D+S+256C*C and head H>=.239999 I are inputs; its fixed546
inverse-action numbers are not inputs.

Retain the inherited analytic response identity, IEEE754 binary64
basic-operation/sqrt and directed Decimal contracts. Retain the
whole neutral-core qualification of C744z and the unreplayed original
c_*=8.9e-18 source computation. This step neither verifies that source
nor strengthens a scalar lower bound for A0. C744z's closed restriction
and C999j's finite-vector strong-domain argument are used under their
stated qualifications. No RH or H2 assumption is introduced.

Standard representation and inverse order are imported, without reproof:
Teschl, *Mathematical Methods in Quantum Mechanics*, GSM99 author PDF,
12February2009, Theorems2.13/2.18, pp71-72/77,
[PDF](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf);
Behrndt–Hassi–de Snoo–Wietsma, arXiv:1403.5704v1,
Proposition2.1 p4, Theorem3.4's nonnegative proof case p11 and
Corollary3.5 p12, [pinned PDF](https://arxiv.org/pdf/1403.5704v1).
The latter permits non-dense selfadjoint relations. The bounded block
precedent is Dritschel–Rovnyak, arXiv:0903.3639v1, LemmaA.1 pp28-29,
[PDF](https://arxiv.org/pdf/0903.3639v1). Its general theorem is not
reproved or applied directly to the unbounded diagonal. Assessments
553/555 and the invocation-start SPECIALIZE assessment558 cover this
method. What follows certifies only its finite-family specialization.

## Conclusion

Let Z:C^510->C^512 send coefficients u_n, n=2,...,511, to those same
raw coefficients, with

    (Zu)_p=-sum_(n>=2,n mod2=p) r_n u_n, p=0,1,
    r_n=(nu_n/nu_p)(1/4+k_p^2)/(1/4+k_n^2),
    k_n=n*pi/ell, nu_0=ell^-1/2, nu_n=sqrt(2/ell) (n>0).       (1)

All higher raw coefficients vanish. For f=Zalpha,h=Zbeta and
x=(alpha,beta) in C^1020, let g_G be the exact neutral head Galerkin
predictor for Tf+T*h. The calculation below supplies, under the
retained contracts, the proposed bound

    Q_min(f,h) >= .000999 ||x||^2,                            (2)

where Q_min is the original full three-cell energy minimized over
the ENTIRE neutral middle form domain. In particular U is retained.
The separate step561 conceptual audit in Section7 upholds (2)
under exactly these retained contracts. It is a qualified local result,
not an RH candidate or independent validation of the inherited contracts.

Only this fixed endpoint family is covered. Endpoint complements,
other separations, C744q's strict margin, H2 slack/existence,
non-neutral coverage and global actual-Xi assembly remain open.
This is standard-method REPRODUCTION, with no originality claim.

## Proof

### 1. Exact spaces, predictor and inverse applicability

Direct integration gives C_c(e_n)=nu_n c[(-1)^n exp(c ell)-1]/
(1/4+k_n^2), c=+/-1/2. In each parity the ratio to index p is
exactly r_n, independent of c. Formula(1) therefore kills both
moments exactly. Z is injective and parametrizes the entire neutral
raw head: the two parity moment columns at0 and1 are independent,
and the other510 coefficients are free. No numerical nullspace,
reflection relation, real-only or parity restriction is imposed.

Put L=D+S+256C*C and define the finite exact matrices

    A=Z*LZ, B=Z*[TZ,T*Z], Y=A^-1 B, g_G=ZYx.               (3)

The penalty vanishes on ran Z. C744z's coercivity, or the stronger
finite verification below, gives A>0. Thus (3) exists uniquely,
depends complex-linearly on x and is exactly the Galerkin equation
a0(g_G,Zv)=<Tf+T*h,Zv> for every v. All these finite vectors are
in Dom(D)=Dom(L). For v in V0, a0(g_G,v)=<P0Lg_G,v>, so the
representation theorem gives g_G in Dom(A0), A0g_G=P0Lg_G.
Boundedness of T,T* makes

    rho_G=Tf+T*h-Lg_G in L2, P0rho_G=b-A0g_G,
    b=P0Tf+P0T*h.                                           (4)

This is the finite-family applicability of C999j, with no assertion
of causal-generator domain membership or invariance of H0 under L.

Encode A0 on L2 as the orthogonal selfadjoint relation with operator
part A0 on H0 and multivalued part H0-perp. Its form domain is V0
and its inverse is A0^-1 P0. C999k's R has form domain V containing
V0 and R<=L=a0 there. The cited relation inverse order therefore
gives <A0^-1P0rho_G,P0rho_G><=<R^-1rho_G,rho_G>. C744z(6)'s
square completion, valid for this strong trial, yields

    Q_min(f,h) >= Q_actual(f,g_G,h)-<R^-1rho_G,rho_G>.         (5)

No projected unrestricted inverse identity is used. The task is to
bound the two quadratic matrices on the right, uniformly in x.

### 2. Finite exact predictor versus a proposed dyadic matrix

The reproduction script is
`scripts/separation-seven/neutral-head-covariance-559.py`.
It checks the audited archive/source hashes from534/548 and reuses
the unchanged reference from557. Zhat is enclosed coefficient by
coefficient using80-digit directed intervals for(1); its complete
conversion L1 error is <10^-14. Since Z*Z is I plus one rank-one
matrix in each parity, ||Z||<z=1.008 follows from the two sums of
r_n^2. These sums are enclosed, not sampled norms.

Let Mhat, That and Uhat be the saved complete head, separation7
head and remote prime head. Define the saved dyadic centers

    Ahat=fl(Zhat^t Mhat Zhat),
    Bhat=fl(Zhat^t[That Zhat,That^t Zhat]),
    Yhat=the saved proposed solve of Ahat Yhat=Bhat.

The true finite operators obey the following norm bounds, with the
rounding/neutral-basis allowance included:

    eta_A=.00024 z^2+10^-7,
    eta_B=sqrt(2) z^2*512*(2.1e-7)+10^-7,
    eta_U=z^2*(512*10^-7+kappa14)+10^-7,                    (6)
    kappa14=1/[3^16*3^(1/4)*(5/2)*(1-3^-13)].

C744w's full head error proves the first bound; C744z(28) gives
both T orientations in the second; its(29) gives the full U in
the third. The continuous U is enclosed in either sign, not omitted.

Full reconstruction of proposed factors for

    Ahat-.7793 I,
    1.32^2 I-Yhat Yhat^t,
    6.19^2 I-(Mhat Zhat)^t(Mhat Zhat)

has error <10^-6 in each case. Thus the EXACT A>=.779 I,
||Yhat||<y=1.320001 and ||Mhat Zhat||<m=6.190001. This is only
a finite Galerkin floor, not a replacement lower bound for A0.
The complete proposed equation residual has floating Frobenius norm
<10^-9; its exact dyadic residual is covered by10^-7. Consequently

    r_G=eta_B+eta_A*y+10^-7,
    ||Y-Yhat|| <= delta_Y=r_G/.779.                         (7)

Set g_tilde=ZYhat x, with exact Z and dyadic Yhat. Its full trial
matrix is enclosed about the saved real symmetric matrix Ehat by
eta_A(1+y^2)+2eta_B*y+eta_U+10^-6. Galerkin orthogonality gives
Q_actual(f,g_G,h)=Q_actual(f,g_tilde,h)-
<A(Y-Yhat)x,(Y-Yhat)x>. The last loss is at most r_G^2/.779
times ||x||^2, by the equation residual and A>=.779 I. Hence

    Q_actual(f,g_G,h) >= x*(Ehat-e_trial I)x,
    e_trial < .001130587.                                  (8)

Ehat includes both endpoint forms, both T orientations, the full
middle form and the signed U pairing. This is not the head Schur
complement promoted to an infinite inverse.

### 3. Complete finite residual covariance

For g_tilde use the full lifted residual rho_tilde. The saved head
center is [That Zhat,That^t Zhat]-Mhat Zhat Yhat. Every output
row512,...,65535 is regenerated from C744w's response divided
difference, its complete-tail allowances, both signed translation
formulas, both continuous orientations and the moment penalty.
No S prefix is used. The row is [Trow Zhat,T*row Zhat]-W0row Zhat
Yhat, combined BEFORE any product is formed. D has no output here;
the exact penalty kills g_tilde, while its computed roundoff is paid.

Let C_H be the saved symmetric head inverse-action center and C_M
the sum of every weighted complementary row product. The head
inverse is the exact rational H of C999k, not an approximate inverse
accepted on the strength of a solve. The full matrix solve residual
is enclosed, using ||H-Hhat||<10^-8 and H>=.239999 I. If Xhat is
the proposed solve of Hhat Xhat=rhohat_P, then

    ||H^-1rhohat_P-Xhat||_F
       <=(||rhohat_P-Hhat Xhat||_F+10^-8||Xhat||_F+10^-7)
                                                           /.239999.

Multiplying by ||rhohat_P||_F and paying the product error bounds
the difference of the entire head action matrix by <10^-6. The
same product of Frobenius norms bounds its trace/nuclear error.
No accuracy assumption for a library linear solver is needed.

For n>=512 the positive increasing lower comparison is
d_n=log(n/(2ell))-2ell^2/(9n^2). C_M uses upward weights2/d_n
from all65024 saved directed lower endpoints audited in557. This
dominates the true weights2/h(k_n) separately at EVERY row. In
particular the within-range products include the covariance of Tf,
T*h and Sg_tilde, with all complex endpoint cross products.

Put e0=.000000181+sqrt(65024*512)*10^-7. Complete residual-error
operator norms, including coefficient transformation and arithmetic,
are bounded by

    delta_P=sqrt(2)*512*(2.1e-7)*z+.00024*z*y+10^-7,
    delta_M=sqrt(2)*sqrt(65024*512)*(2.1e-7)*z
                                      +e0*z*y+10^-7,
    delta_F=sqrt(delta_P^2/.239999+2delta_M^2/6.14).           (9)

This uses the rectangular operator/Frobenius entry bounds, rather
than applying a fixed-direction L1 error uniformly. If T_F is the
stored finite trace plus10^-5, ||C_center^1/2||_F<=sqrt(T_F)
for the combined head/complement center, with its small head-solve
and Gram errors included. Expansion of the squared norm gives

    Cov_finite(rho_tilde) <= C_H+C_M+e_F I,
    e_F=2sqrt(T_F)delta_F+delta_F^2+10^-5
          < .005266643.                                    (10)

Only orthogonal output ranges are split. All summands within a
range were combined before squaring. The10^-5 slack pays the head
action-matrix error, its trace error and accumulated Gram rounding.

### 4. Uniform analytic infinite tail with boundary functionals

Here are the uniform estimates not supplied by the fixed546 result.
Write d_0=1/sqrt(2), d_m=1 for m>0, and

    v_+(u)=sum d_m u_m, v_-(u)=sum (-1)^m d_m u_m,
    v_e(u)=sum_(m even) d_m u_m,
    v_o(u)=sum_(m odd) d_m u_m.

All sums have m<512. For the separation7 prime weights split
a_+=sum_(delta>0)a_delta and a_-=sum_(delta<0)a_delta.
The script certifies every delay sign and obtains
a_+<3.111758 and a_-<4.542122. For a single normalized shift
entry in output n>=K, the exact C744w antiderivative has leading
term -(2/pi)(-1)^n sin(k_n delta)d_m(-1)^m/n if delta>0,
or (2/pi)sin(k_n delta)d_m/n if delta<0. Subtract it from the
exact denominator n^2-m^2. The remaining absolute entry is at most

    (2/pi)d_m/[1-(511/K)^2]*(m^2/n^3+m/n^2).

Thus its remainder operator norm is at most

    j_rem=(2/pi)/[1-(511/K)^2]*
       [sqrt(sum_(m=1)^511 m^4)/sqrt(5(K-1)^5)
        +sqrt(sum_(m=1)^511 m^2)/sqrt(3(K-1)^3)].           (11)

This is a Hilbert--Schmidt bound, using the integral tails of
n^-6 and n^-4. It applies to either orientation. The whole prime
remainder has norm <=(a_++a_-)j_rem<.001125264. The leading
norm for the two endpoints together is at most

    2/[pi sqrt(K-1)]*(a_+|v_-(f)|+a_-|v_+(f)|
                          +a_+|v_+(h)|+a_-|v_-(h)|).     (12)

The entire continuous part costs kappa(||f||+||h||), with the
unchanged kappa of C744v(2), kappa<.000105742.

For S, use its exact series C744v(9). For p=m mod2 subtract
(nu_m/nu_p)S_np from S_nm. Opposite parities vanish. For m>0
the absolute difference is bounded by

    4nu_n nu_m k_m^2/k_n^2 * sum_j 1/(c_j^2+k_m^2)
       <= (16ell/pi^2+4m)/n^2, c_j=2j+1/2.               (13)

To see the first bound, subtract the two denominators in m,p,
use |1-(-1)^n exp(-ell c_j)|<=2 and
c_j^2/(c_j^2+k_p^2)<=1. Then use the decreasing-sum comparison
sum_j1/(c_j^2+k_m^2)<=1/k_m^2+pi/(4k_m). The displayed second
bound is deliberately loose. For m=p the difference is exactly
zero, including m=0, so(13) covers that case as well. Its full
remainder norm is at most

    s_rem=sqrt(sum_(m=0)^511(4m+16ell/pi^2)^2)
                                /sqrt(3(K-1)^3)<.000919985.

C744w(6)'s |S_np|<=1/n+b/n^2, b=4ell(1+(3/2)3^-1/4)/pi^2,
then bounds the remaining two-parity part by

    (1+b/K)/sqrt(K-1)*(sqrt(2)|v_e(g_tilde)|
                                            +|v_o(g_tilde)|). (14)

This retains signed coefficient sums before taking their magnitudes;
it does not replace each sum by the coefficient L1 norm.

Let V_b be the six rows in(12),(14) applied to
(f,h,g_tilde)=(Zalpha,Zbeta,ZYhat x). Let w_j be their six positive
coefficients. Weighted Cauchy--Schwarz gives the covariance bound
for this whole leading tail

    C_b=(sum_j w_j) V_b*diag(w_j)V_b,
    ||rho_lead(x)||^2 <= x*C_b x.

Both prime orientations, the response and their mutual covariance
are paid by this single squared SUM. The complete remainder has norm

    t_rem=sqrt(2)*z*((a_++a_-)j_rem+kappa)+s_rem*z*y
          < .002978927.                                    (15)

For the full tail use (a+b)^2<=(11/10)a^2+11b^2. Since d_n is
increasing and d_K>10.9963070613268, its complete weighted covariance
is at most

    C_tail=(2/d_K)*[(11/10)C_b+11t_rem^2 I]+10^-6 I.        (16)

The last allowance pays scalar/matrix rounding and exact-Z to
Zhat conversion in the six functionals. All n>=65536 are covered;
no response-prefix increase, frequency sampling or changed allocation
is used. The prime, response and continuous tails were not squared
separately and added as if they were orthogonal.

### 5. Exact-predictor error and final comparison

Define the saved matrix C_tilde=C_H+C_M+C_tail+e_F I. Equations
(10),(16) show Cov_R(rho_tilde)<=C_tilde. Its entire saved matrix
has Frobenius norm<.950907; with the complete norm-evaluation
allowance it is <.951. Thus Cov_R(rho_tilde)<=.951 I. This uses
||C_tilde||_op<=||C_tilde||_F, not a sampled eigenvalue.

Changing from g_tilde to the exact Galerkin predictor changes the
lifted residual by -LZ(Y-Yhat)x. The entire QW0P norm is at most
.586+e0+.062501906, including both output ranges and all moment
covariance. Hence, with m=6.190001 from Section2,

    b_LZ=sqrt((m+.00024*z+10^-7)^2/.239999
                +(2/6.14)*[(.586+e0+.062501906)z]^2)
             <12.641324,
    delta_G=b_LZ*delta_Y<.007736039.

This is an R^-1 weighted norm bound for LZ only. It is neither a
scalar bound for A0^-1 nor a projected-inverse substitution. The
covariance change is therefore bounded above by

    e_G=2sqrt(.951)delta_G+delta_G^2<.015148097,
    Cov_R(rho_G)<=C_tilde+e_G I.                           (17)

The stored real symmetric comparison matrix is

    M=Ehat-C_tilde-(e_trial+e_G)I,

with the scalar endpoints rounded upward and assembly paid by the
preceding allowances. A proposed full1020 by1020 Cholesky factor
for M-.001 I has a checked reconstruction norm<10^-6. Consequently
M>=.000999 I. Its floating smallest eigenvalue, approximately
.0027284175, is diagnostic only and is not a proof input. Combining
(8),(17) with(5) proves the proposed qualified assertion(2) for
every complex x, not just real or reflected test vectors.

### 6. Arithmetic evidence, failure preservation and limits

Reproduce, without modifying earlier artifacts, with

    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/separation-seven/neutral-head-covariance-559.py

The full certificate and matrices/factors are
`scripts/separation-seven/neutral-head-covariance-559.json` and
`scripts/separation-seven/neutral-head-covariance-559.npz`; the log
has the same basename. The JSON records every row-block range and
magnitude, all scalar endpoints, all ratio intervals, hashes, checks
and failures. The NPZ stores the entire1020 by1020 covariance and
comparison matrices, all predictor coefficients, head solves and
complete proposed factors. Finite rows are reproducibly regenerated;
their combined-byte digest is also recorded. No large preview is
substituted for the full matrix operations.

The rounding ledger uses u=2^-53 and gamma_r=ru/(1-ru).
Stored Frobenius norms satisfy ||Mhat||_F<400, ||That||_F<40,
||cov00||_F<1, ||Uhat||_F<60; ||Zhat||_F<23 and
||Yhat||_F,||Zhat Yhat||_F,||Xhat||_F<10. With contractions
of at most1020 terms, gamma_1024<1.2e-13. The bound
||fl(AB)-AB||_F<=gamma_r||A||_F||B||_F makes each finite
transformation/equation residual error <10^-7; the longer trial
assembly is covered by10^-6. The exact rational H assembly error
is <10^-8. All generated rectangular factors together have squared
Frobenius norm<20, checked over all127 row blocks; their transformed
row products have much smaller rounding than10^-7. The weighted
Gram summation has gamma_65536<8e-12 and complete center trace<3,
so its rounding and trace accumulation fit within10^-5, including
the head-action error described in Section3. Upward weight conversion
from the directed d_n endpoints is paid separately by using the
larger converted weights.

For every proposed factor, the full saved reconstruction is tested,
not only factorization success. The largest dimension is1020,
all matrix entries have modulus<400 and every factor squared
Frobenius norm is<100000. The product rounding bound is therefore
<1.2e-8; reconstruction and norm-evaluation errors are smaller than
the remaining10^-6 budget, including the observed residual<10^-7.
Squared norms with at most1020^2 terms use gamma_(1020^2)<1.2e-10;
the norm-evaluation allowance10^-6 is also sufficient for the .951
comparison. Tail scalar operations use directed80-digit intervals;
the10^-6 tail matrix allowance dominates its six-row matrix-product
rounding and <10^-14 basis-conversion errors.

An initial pass used sqrt(trace C_tilde) instead of sqrt(.951) in
(17). Its error allowance was>.043572149 and its final factor
failed; the reported diagnostic minimum was about-.025695635.
This was an inconclusive enclosure, not a rigorous negative value
of the actual reference comparison. That script/certificate/matrix/
log is preserved as `neutral-head-covariance-first-pass-559.*` in
the same directory. Replacing the trace loss by the Frobenius norm
of the same covariance matrix changes no family, predictor, reference,
cutoff or allocation. The final certificate retains every covariance
and error allowance and has no failed checks.

Section7 supplies the separate conceptual audit of this uniform tail,
covariance/operator inequalities, exact-predictor error and finite
arithmetic bridge. The inherited full-core/c_* qualifications remain.
This finite interface leaves all endpoint complements and the global
actual-Xi positivity gap untouched.

### 7. Separate conceptual audit — 12 November2026, step561

**Result and scope.** The unchanged source-approved assessment559
covers this audit. Bound(2) is upheld for all1020 independent complex
coordinates and the entire neutral middle form domain. This validates
the existing standard-method specialization; it asserts no new general
theorem, originality, endpoint-complement sign or RH progress. No
family, predictor, reference, cutoff or allocation was changed.

**Domains and inverse order.** Direct integration of both exponential
moments gives(1). In parity p the two moment entries have the same
ratio r_n. The columns at0,1 are independent: apart from their nonzero
normalizations, their ratios of plus to minus moments are respectively
exp(ell/2) and -exp(ell/2). Thus each free vector has precisely one
neutral completion, for complex coefficients as well as real ones.
The finite solution of(3) exists by the verified A floor. Each finite
neutral vector belongs to Dom(D)=Dom(L); pairing against every V0
gives its A0 representative P0L g. This proves(4), without asserting
invariance of H0 under L or membership in a causal-generator domain.

C999k's R is closed and coercive on the full space, with domain V.
The relation for A0 has form domain V0 subset V and multivalued part
H0-perp; its inverse is exactly A0^-1 P0, zero on H0-perp. On V0,
R<=L=a0 because the exact penalty vanishes. These are precisely the
hypotheses and direction of Behrndt et al. Proposition2.1 and
Corollary3.5 cited above. C744z's square completion on V0 then gives
(5). No inverse of the unsigned triple block enters. The inherited
whole-core and unreplayed c_* qualifications are retained, not audited
away by this finite calculation. The .779 floor remains a bound on
Z*LZ alone.

**Uniform tail, including boundary cases.** For delta>0 the exact
shift entry is (2/pi)d_m[-(-1)^(n+m)n sin(k_n delta)
+m sin(k_m delta)]/(n^2-m^2). Subtracting its stated leading term
leaves a contribution at most
(2/pi)d_m[m^2/n^3+m/n^2]/[1-(511/K)^2]. For delta<0 the
numerator is (2/pi)d_m[n sin(k_n delta)
-(-1)^(n+m)m sin(k_m delta)]; the identical absolute remainder
bound follows. At m=0 the remainder is zero. For the adjoint replace
delta by -delta: the positive-delay weights therefore multiply the
opposite boundary functional on h, exactly as in(12). The sums of
n^-6 and n^-4 are bounded by their integrals from K-1. This proves
(11) for every n>=K, rather than a tested frequency range.

For the response, when n,m,p have the same parity, the exact
difference S_nm-(nu_m/nu_p)S_np equals

    2nu_n nu_m(k_p^2-k_m^2) sum_(j>=0)
      c_j^2(1-(-1)^n exp(-ell c_j)) /
      [(c_j^2+k_n^2)(c_j^2+k_m^2)(c_j^2+k_p^2)].

For m>p, taking absolute values, using k_m^2-k_p^2<=k_m^2,
|1-(-1)^n exp(-ell c_j)|<=2, and
c_j^2/(c_j^2+k_p^2)<=1 proves the first bound(13). The decreasing
resolvent-sum comparison gives at most
(8ell/pi^2+2m)/n^2, which is smaller than the deliberately loose
displayed bound. If m=p (including0), the difference is exactly zero.
Opposite parities are zero before subtraction. The even base coefficient
is sqrt(2)v_e(g); the odd one is v_o(g). Applying C744w(6) separately
to the two base columns and then the triangle inequality proves(14).
Thus the constant mode and the distinct normalization at0 are paid.

The six leading contributions are summed in norm before squaring.
For their possibly complex functional values b_j,
(sum w_j|b_j|)^2<=(sum w_j)sum w_j|b_j|^2. This is the full
Hermitian matrix C_b, not six independent covariance estimates.
The endpoint remainders cost sqrt(2)z times the common prime-plus-
continuous norm, and the response remainder costs s_rem z y.
These prove(15); Young's inequality with epsilon=1/10 gives exactly
the factors11/10 and11 in(16). Finally
d'(t)=1/t+4ell^2/(9t^3)>0, so2/d_K bounds every remaining inverse
weight. This establishes the entire infinite tail and all its mixed
terms, including the complete continuous kernels.

**Finite covariance and exact predictor.** Every finite row contains
both T orientations and full S+256C*C applied to the same predictor.
The residual is formed before its weighted outer product. Splitting
head, finite complement and infinite tail is justified solely by their
orthogonal output supports and R's block diagonal inverse. Within
each range there is no omitted cross term; real matrix formulas define
the same Hermitian bound on complex vectors. Full U occurs in the
trial energy; it has no middle variable and hence no residual term.

For clarity, the square-root/trace argument in(10) uses the exact
positive Gram matrix of the stored dyadic residual with the true H
inverse and the chosen positive complementary weights. The computed
C_H+C_M need not itself be assumed exactly positive. Its action and
trace differences from that Gram matrix are bounded by the head solve
and product ledgers. For the head, the error product has nuclear norm
at most ||rhohat_P||_F times the Frobenius inverse-action error, so
the same estimate controls trace as well as operator error. Product
rounding has nuclear bound at most sqrt(1020) times its Frobenius
bound, below the separately charged10^-7. The complete finite trace
including the allowance is below3. This justifies sqrt(T_F) in(10).

In(7), A(Y-Yhat)=B-A Yhat has norm at most r_G; invertibility of
the exact A gives delta_Y. Galerkin orthogonality gives a loss
r* A^-1 r<=r_G^2/.779 in the trial. For the lifted residual change,
the head of LZ is controlled by m plus its full entry/conversion
allowance, and the entire complementary part by the three terms in
b_LZ. Applying R^-1/2 gives exactly delta_G. Since the verified
whole covariance has Frobenius norm below.951, its operator norm is
also below.951, and expansion of the squared weighted residual norm
gives e_G. A trace bound is not substituted for this operator bound.

**Complete arithmetic evidence.** Reproduce with separate artifacts:

    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/separation-seven/neutral-head-covariance-replay-561.py
    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/separation-seven/neutral-head-covariance-audit-561.py

The100-digit directed replay changes only scalar precision and output
paths. All18 stored arrays, including the four original proposed
factors, agree bit for bit with559. The digest of every combined
residual row agrees;127 complete512-row blocks partition512,...,65535.
All original script, archive and input hashes are checked. The full
replay is saved as `scripts/separation-seven/neutral-head-covariance-replay-561`
with py/json/npz/log extensions; the audit script/json/log has basename
`scripts/separation-seven/neutral-head-covariance-audit-561`.

The independent scalar checker uses the read110-place integer outward
interval implementation from audit552: positive atanh series for ell,
Machin series for pi, integer square roots and widened140-digit Decimal
logarithms. It checks all510 moment-ratio intervals and their entire
basis conversion error, all65024 diagonal lower endpoints and upward
weights, the complete prime-power enumeration and delay signs, and all
tail/predictor error expressions. No preview or selected matrix entry
stands for these complete operations.

All original factors are checked against their full matrices. Their
observed reconstruction Frobenius norms are below3.89e-14. Using the
more conservative gamma_2048 times100000 for product rounding, plus
2e-7 for operand assembly, subtraction and norm evaluation, each
reconstruction error is below2.228e-7<1e-6. The recorded matrix/factor
magnitudes verify this ledger; no factorization-success or eigenvalue
assumption is used. Squared-norm evaluation has at most1020^2 terms.
Finite transformations, exact-neutral conversion, the rational H
assembly and the head solve all fit the preceding1e-7/1e-6 allowances.
The finite Gram and trace error, including nuclear head error, fits
10^-5. The six boundary rows have Frobenius norm<100, each weight<.012
and their sum<.05; their complete assembly and basis errors fit the
tail's10^-6 allowance. All arithmetic statements remain conditional
on the explicitly inherited execution contract.

The independently enclosed upper bounds are

    e_trial < .001130586546, e_F < .005266642371,
    t_rem < .002978926855, e_G < .015148096707.

The whole saved covariance Frobenius norm is below.950906237; adding
its10^-6 allowance still gives less.951. The full comparison factor
therefore proves M>=.001I-10^-6I=.000999I, as required. This proves
(2) through(5), with no use of the diagnostic smallest eigenvalue.

The first-pass artifacts and their failed comparison factor are intact.
That trace-based enclosure was inconclusive, not a negative actual
direction. No failure in the final fixed certificate was found. The
audit adds no endpoint-complement, C744q, H2, non-neutral or actual-Xi
claim and leaves the inherited source/core qualifications explicit.

## Mathlib

Full matching coverage for this fixed1020-dimensional residual
certificate and its logarithmic neutral form has not been checked.
The standard form representation, relation inverse order and finite
positive-factor principles are cited above; they are not assertions
of matching Mathlib declarations. No absence claim is made.
