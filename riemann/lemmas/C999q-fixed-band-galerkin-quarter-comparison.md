# C999q: A fixed-band Galerkin quarter comparison

## Hypotheses

Use C744v/w's complete cosine operators D,S,T, C744z's complete
separation14 operator U and closed neutral form a0 on V0, and C999k's
UNCHANGED reference R. Thus ell=log(3)/2, L=D+S+256C*C, H0=ker C,
R has its exact rational head H on raw0:511, diagonal h(k_n)/2 on
n>=512, and output cutoff K=65536. C999k's audited R<=L on the full
form domain and H>=.239999 I are inputs. Its one-vector numerical
inverse action is not an input here.

Retain all analytic-response and IEEE754 binary64 basic-operation/sqrt,
directed Decimal, whole-neutral-core and unreplayed c_* qualifications
of C744v/w/z and C999k/l. In particular this is not an independent
verification of the original c_*=8.9e-18 source computation. No RH,
H2 existence/slack, endpoint symmetry, old mixed constant, or infinite
endpoint-family positivity is assumed. Invocation-start assessment592,
separately approved593, licenses this REPRODUCTION calculation.

The complete1024-square Mhat=D+S, That,Tshat,Uhat centers are from
C999o's audited `scripts/separation-seven/original-galerkin-586.npz`.
C999p Section2 supplies the assessed extension of the scalar entry
ledger through all output indices below65536 and inputs below1024;
its frozen-vector accumulated errors are not transferred.

Import the general results without reproof: Teschl, *Mathematical
Methods in Quantum Mechanics*, GSM99 author version12February2009,
Theorems2.13/2.18, pp71-72/77,
[PDF](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf);
Behrndt–Hassi–de Snoo–Wietsma, arXiv:1403.5704v1, Proposition2.1 p4,
Theorem3.4's nonnegative sufficient proof case p11 and Corollary3.5 p12,
[pinned PDF](https://arxiv.org/pdf/1403.5704v1). The local application
is the already established C999k/l restricted relation, with form domain
V0 inside V. Dritschel–Rovnyak arXiv:0903.3639v1 AppendixA.1-A.2,
pp28-30, [PDF](https://arxiv.org/pdf/0903.3639v1), is bounded-block
background, not a theorem applied directly to the unbounded D here.

## Conclusion

Let Z:C^1022->C^1024 be the exact neutral completion on raw0:1023:
for 2<=n<=1023 the coefficient is u_n, and for p=0,1 it is

    (Zu)_p=-sum_(2<=n<=1023,n mod2=p) r_n u_n,
    r_n=(nu_n/nu_p)(1/4+k_p^2)/(1/4+k_n^2),
    k_n=n*pi/ell, nu_0=ell^-1/2, nu_n=sqrt(2/ell), n>0.

Let Z_T be its512 columns corresponding to free512:1023, as in C999m.
For independent alpha,beta in C^512 put x=(alpha,beta), f=Z_T alpha,
h=Z_T beta. Set

    A=Z*LZ, B=Z*[TZ_T,T*Z_T], Y=A^-1 B, g_G=ZYx,
    rho_G=Tf+T*h-Lg_G,
    F_G(x)=Q_actual(f,g_G,h)-<R^-1rho_G,rho_G>,
    ||x||_tail^2=sum_(n=512)^1023 d_n(|alpha_n|^2+|beta_n|^2),
    d_n=log(n/(2ell))-2ell^2/(9n^2).

The calculation594 gives, under the retained contracts,

    F_G(x) >= ||x||_tail^2/4 + .000999 ||x||_2^2,
    Q_min(f,h) >= F_G(x).                                  (1)

**Audit status, step596:** Section8 upholds (1) under exactly the retained
contracts, after a separate conceptual audit of the complete family ledger.
It is a standard-method specialization, not a claim beyond the sources
checked or a complete RH candidate. It changes the middle predictor
relative to C999n's stopped zero-middle comparison. C999m's old mixed
constant therefore does NOT transfer. Head/band and band/high mixed
comparisons, higher endpoints, C744q, H2, non-neutral coverage and actual-Xi
assembly remain open.

## Proof

### 1. Exact coordinates, predictor and applicability

Integration gives C_c(e_n)=nu_n c[(-1)^n exp(c ell)-1]/(1/4+k_n^2),
c=+/-1/2. Its ratio to C_c(e_p), p=n mod2, is exactly r_n for both
moments. Thus Z and Z_T kill both moments algebraically. They are not
rounded nullspaces. The two free endpoint vectors are independent and
complex, and every middle free coordinate2:1023 is allowed.

All these finite vectors lie in Dom(D)=Dom(L) and V0. C999l Section1's
strong-trial argument applies unchanged to any such g: testing the form
against every v in V0 gives A0g=P0Lg. Bounded T,T* gives rho in L2 and
P0rho=b-A0g. The C999k relation is A0 on H0 plus the multivalued part
H0-perp on L2. Its inverse is A0^-1P0. The cited form-order theorem and
R<=L on V0 give the correct inverse inequality and hence

    Q_min(f,h)>=Q_actual(f,g,h)-<R^-1rho,rho>.               (2)

No projected unrestricted-inverse identity or scalar replacement for
A0^-1 is used. A>0 is verified below on this finite space, so Y exists
and is exactly the specified Galerkin map. Its finite floor is not a
new coercivity floor for A0. U has no middle variable and therefore
enters Q_actual with its full signed value, not rho.

### 2. Uniform entry bounds on the changed finite ranges

Write J=1024. C744w(12)-(13) give the analytic errors with

    q_n=sqrt(2)/[6(64.25^2+k_n^2/4)].

For same-parity unequal n,m their normalized response error is at most

    (2/pi)(n q_n+m q_m)/|n^2-m^2|.                         (3)

This follows by substituting k_n=n*pi/ell and nu_n nu_m<=2/ell in
C744w(13); the constant-mode normalization only decreases it.
Opposite-parity response entries vanish exactly. On the diagonal the
local D+S error is at most

    q_n+8[c^-2+2k_n^2((6c^3)^-1+c^-4)], c=131072.5.         (4)

The factor8 overbounds 2nu_n^2. Equal indices occur only in0:J.
Neither estimate differentiates a digamma asymptotic.

The script uses the proved rational inequalities
5.719<pi/ell<5.720, pi>3.14159 and sqrt(2)<1.415. Define a positive
entry-radius matrix by replacing q_n with
1.415/[6(64.25^2+(5.719n/2)^2)], 2/pi with2/3.14159 in(3), and
k_n with5.720n in(4), then add1e-7+1e-12 to EVERY entry.
The1e-7 is C744w/C999p's complete elementary local allowance;
1e-12 pays evaluation of these rational bounds themselves. The
arithmetic involves fewer than50 basic operations, positive rational
inputs, and |n^2-m^2|>=1; integers/squares below2^33 are exact. With
the largest unrounded expression below.001, 1e-12 strictly dominates
its rounding error. Symmetrization preserves the symmetric square
radius bound. Every row and column, not a sample, is included.

The Frobenius norms over the complete square0:J and rectangle0:K,
with column0:J, are bounded by

    e_M,J < .000295752,
    e_M,K < .000864931.                                   (5)

The script evaluates all radii, inflates their full sum-of-squares norm
by1.00000001, and adds1e-8. The square includes D; outside it D has no
output. These are uniform matrix/operator bounds, not fixed-vector
L1 bounds. Full T,T*,U entries on the square have error<=1e-6; the same
T,T* allowance holds throughout the rectangle by C999p Section2.
All16 nearest and334 remote shifts, including the exact zero delay2187,
are retained in the source square. Both seven-term continuous
orientations include their complete suffixes. Far output formulas use
the same full local response and complete continuous suffixes.

For the enlarged range, |k_n delta|<207000 and
(n^2+m^2)/|n^2-m^2|<1024 at distinct indices. The worst new rectangle
pair is1024,1023; within the square1023,1022 is smaller. Thus C744w's
explicit elementary ledger applies. Zero input frequency, equal
indices, opposite parity, both delay signs and zero delay retain their
separate formulas. This is why the scalar allowances extend, while
old accumulated covariance constants do not.

### 3. Exact Galerkin map versus the saved dyadic proposal

Write Zhat_T for the saved band subset of Zhat. The locator's saved
Yhat is only a proposed dyadic solution. Rebuild
all its finite products from the pinned complete square, and enclose
all1022 exact moment ratios at80 directed digits using the80-term
Machin enclosure for pi and widened Decimal ln/sqrt. Their total L1
conversion error is <4.170e-18<1e-14. Since Z*Z is I plus one rank-one
matrix in each parity, summing the exact ratios squared gives ||Z||<z=1.008.
The Z_T subset has the same bound. Exact Z, not Zhat, defines every trial.

With the raw square and exact coordinates, the finite matrix errors
about Ahat=fl(Zhat* Mhat Zhat), Bhat=fl(Zhat*[That Zhat_T,Tshat Zhat_T])
and the remote block are bounded by

    eta_A=z^2 e_M,J+1e-6 < .000301503,
    eta_B=sqrt(2)z^2 J*1e-6+1e-6 < .001472418,
    eta_U=z^2 J*1e-6+1e-6 = .001041449536.                  (6)

These include coordinate conversion and product errors. Full proposed
factor reconstructions for Ahat-.77I and .61^2I-Yhat Yhat* certify

    A>=a I, a=.77-eta_A-1e-6 > .769697497,
    ||Yhat||<y=.610001.                                   (7)

All factors, not merely successful factorization flags, are saved.
The free and raw predictor Frobenius norms are each<8. The complete
proposed equation residual, including its arithmetic, gives

    r_G=||Ahat Yhat-Bhat||_F+1e-6+eta_B+eta_A y
           < .001657335,
    ||Y-Yhat||<=delta_Y=r_G/a < .002153229.                (8)

The full trial center Ehat includes both endpoint local forms, the
middle form, both T orientations and signed U. Its error for the
exact-coordinate dyadic trial ZYhat x is bounded by
eta_A(1+y^2)+2eta_B y+eta_U+1e-5. Exact Galerkin orthogonality subtracts
at most r_G^2/a ||x||^2 on changing to g_G. Consequently

    Q_actual(f,g_G,h)>=x*(Ehat-e_trial I)x,
    e_trial<.003265064.                                   (9)

### 4. Every finite residual output and the rational head inverse

For the exact-coordinate dyadic trial g_tilde=ZYhat x form the complete
row map [T Z_T,T*Z_T]-L ZYhat. On0:1023 the center is
[That Zhat_T,Tshat Zhat_T]-Mhat Ghat. This retains the ACTUAL Dg on
512:1023. On1024:65535 use the full response and both forcing
orientations; Dg is zero there. Cg_tilde=0 removes the true moment
penalty exactly. No penalty is subtracted from R's definition.

Combine all terms in each row BEFORE forming any row product. Keep
all cross products between endpoints and predictor. Let C_H be the
symmetrized head inverse-action center and C_M the complete weighted
Gram sum on512:65535. The weights are rounded upward from ALL65024
directed d_n lower endpoints in C999k's audited certificate; they
majorize2/h(k_n) and are <=2/6.14. The head solution Xhat is a proposal:

    e_H=||rhohat_P-Hhat Xhat||_F+1e-8||Xhat||_F+1e-6,
    ||H^-1rhohat_P-Xhat||_F<=e_H/.239999.

Here H is exactly C999k's rational m0-.00024 I-(100/307)(cov00+.0046 I),
and ||H-Hhat||<1e-8 is paid. Multiplying the last bound by
||rhohat_P||_F and adding the product error gives head action-matrix
error <.000001072688<1e-5. The same Frobenius-product estimate bounds
its nuclear error, so the trace used next is also covered. No solver
accuracy premise is used.

Uniform unweighted residual-error bounds on the two output ranges are

    delta_P=sqrt(2NJ)*1e-6 z+e_M,J z y+1e-6
              < .001215045,
    delta_M=sqrt(2(K-N)J)*1e-6 z+e_M,K z y+1e-6
              < .012165043,
    delta_F=sqrt(delta_P^2/.239999+2delta_M^2/6.14)
              < .007372656.                              (10)

Using the square radius bound on the head subset and the entire
rectangle bound on the complementary subset only enlarges these bounds.
They are matrix bounds uniform on all complex x.

The complete finite center trace plus1e-4 is <2.711084442. Norm
expansion, including the unknown cross product with the residual error,
gives the finite covariance majorant

    Cov_finite(rho_tilde)<=C_H+C_M+e_F I,
    e_F=2sqrt(trace_upper)delta_F+delta_F^2+1e-4
          < .024433060.                                  (11)

The1e-4 includes head action/nuclear error, the full Gram/trace rounding
and accumulation. Only orthogonal reference output ranges are added
without cross terms; terms within a row or range were combined first.

### 5. Uniform entire infinite tail

This is C999l Section4's boundary-functional argument with all m<J,
not its old numerical totals. Write t_0=1/sqrt(2), t_m=1 otherwise,
and v_+,v_-,v_e,v_o for sums t_m u_m with respectively no sign,
(-1)^m, the even indicator and the odd indicator. Let a_+,a_- be the
complete separation7 weight sums over positive and negative delays.
All16 signs are checked. For a single shift, subtracting its1/n
boundary term from the exact antiderivative leaves entry bound

    (2/pi)t_m/[1-((J-1)/K)^2]*(m^2/n^3+m/n^2).

Hence for either orientation its full remainder norm is at most

    j_rem=(2/pi)/[1-((J-1)/K)^2]*
      [sqrt(sum_(m=1)^(J-1)m^4)/sqrt(5(K-1)^5)
       +sqrt(sum_(m=1)^(J-1)m^2)/sqrt(3(K-1)^3)]
      < .000418155.                                      (12)

For S subtract the parity-low column as in C999l(13): the difference
is bounded by (4m+16ell/pi^2)/n^2, for each m<J, including the zero
low-column difference. Summing the squared remainder bounds gives

    s_rem=sqrt(sum_(m=0)^(J-1)(4m+16ell/pi^2)^2)
                              /sqrt(3(K-1)^3)<.002603168. (13)

The same decreasing-sum comparison gives the all-m bound
|S_nm|<=1/n+b/n^2, b=4ell[1+(3/2)3^-1/4]/pi^2. For the leading
residual tail use six functionals

    v_-(f), v_+(f), v_+(h), v_-(h), v_e(g_tilde), v_o(g_tilde)

with positive weights

    2a_+/(pi sqrt(K-1)), 2a_-/(pi sqrt(K-1)),
    2a_+/(pi sqrt(K-1)), 2a_-/(pi sqrt(K-1)),
    sqrt(2)(1+b/K)/sqrt(K-1), (1+b/K)/sqrt(K-1).

If V_b is their six-row map and w the weights, weighted
Cauchy–Schwarz bounds the leading-tail covariance by
C_b=(sum w_j)V_b*diag(w_j)V_b. This square of the sum pays all
prime/response/endpoints/predictor cross terms. The full continuous
part is paid by its COMPLETE norm kappa, not a truncated kernel:

    t_rem=sqrt(2)z[(a_++a_-)j_rem+kappa]+s_rem z y
             < .006313785.                               (14)

Using (a+b)^2<=(11/10)a^2+11b^2 and monotonicity of d_n, the full
tail covariance is bounded by the saved matrix

    C_tail=(2/d_K)[(11/10)C_b+11t_rem^2 I]+1e-5 I,
    d_K>10.9963070613268.                                 (15)

The1e-5 pays all six-row conversion, scalar and matrix arithmetic.
No n>=65536 remains unpaid. Dg is exactly zero there. These estimates
use m<=1023 throughout, not a512-column constant reused by name.

### 6. Exact-predictor residual correction and final matrix order

Let C_tilde=C_H+C_M+C_tail+e_F I, symmetrized with its assembly
allowance. Equations(11),(15) imply Cov_R(rho_tilde)<=C_tilde. The
complete saved Frobenius norm plus1e-5 bounds its operator norm by

    c_tilde<1.670760971.                                  (16)

Changing to g_G changes the lifted residual by -LZ(Y-Yhat)x. To bound
this ENTIRE error map, verify a factor for
100I-(Mhat Zhat)*(Mhat Zhat). Together with square entry/coordinate
errors this bounds ||P_<J LZ|| by
m=10.000001+e_M,J z+1e-6. On1024:65535 use the full computed
Frobenius norm of S's raw row map, enlarged by e_M,K and z. On n>=K
use ||S_<J||<=sqrt(J)(1+b/K)/sqrt(K-1); multiply by z. Call the last
two unweighted bounds b_mid,b_far. The reference's inverse on the
whole0:1023 range is <=1/.239999 (on512:1023 this only enlarges2/h).
Therefore

    ||R^-1/2 LZ|| <= b_LZ
      =sqrt(m^2/.239999+(2/6.14)(b_mid^2+b_far^2))
        <20.415951150,
    delta_G=b_LZ delta_Y<.043960215.                       (17)

Exact neutrality removes C*C on every LZ column. D is present in
m and absent only in the strictly higher outputs. All infinite
outputs are included in(17). From(16)-(17),

    Cov_R(rho_G)<=C_tilde+e_G I,
    e_G=2sqrt(c_tilde)delta_G+delta_G^2<.115576619.          (18)

Construct the complete1024-by1024 real symmetric matrix

    M_cert=Ehat-C_tilde-diag(quarter_upper)
                         -(e_trial+e_G+1e-5)I,           (19)

where quarter_upper encloses d_n/4 at both independent endpoints
with directed rounding. The last allowance pays assembly. A full
factor reconstruction for M_cert-.001I has observed residual
<2.259e-14 and complete reconstruction/rounding error<1.236e-8<1e-6.
Consequently M_cert>=.000999 I. This is Hermitian order for EVERY
complex direction; no eigensolver accuracy is used. Combining
(9),(18),(19) gives(1). The diagnostic minimum about.5384417 is
not a proof input and is not promoted to a certified lower bound.

### 7. Arithmetic ledger, reproduction and limitations

All norm bounds inflate binary64 sum-of-squares/sqrt by1.00000001
and add1e-290 for absolute underflow. The largest norm array has
1024^2 entries; the full radius sum has65536*1024 terms, accumulated
in512-row blocks. Even a sequential gamma_(65536*1024)<8e-9 is
below the inflation. Products use gamma_n=nu/(1-nu), u=2^-53;
no BLAS, solve or eigensolver accuracy is assumed.

Finite assembly is covered by1e-6 per A/B matrix and1e-5 for the
trial matrix. For example ||Zhat||_F<32, ||Zhat_T||_F<23,
||Mhat||_F<1000, ||That||_F,||Uhat||_F<100 and ||Yhat||_F<8.
The full two-product A error is bounded by
 gamma_4096*32^2*1000<4.6e-7; B and endpoint products are smaller.
The trial's remaining products, symmetrization and conversion fit
its1e-5 allowance. These magnitude and complete rebuild checks are
in the executable; loaded proposed Y is never assumed exact.

For every factor, reconstruct the full FF* product. The ledger
adds 5e-13*(||F||_F^2+||matrix||_F+1)+1e-8; all dimensions are
<=1024 and gamma_4096<5e-13. The largest factor squared norm is
<66283, all tested matrix entries have modulus<1000, and all total
errors are <1e-6. The extra slack in .610001 and10.000001 also pays
the small Gram-formation errors for their norm tests. Factor positivity
uses FF*>=0, not a factorization library's correctness promise.

For finite residual products, the full bounded-response estimate in
C744v gives ||S||<60, and ||T||,||T*||<8 from the complete prime-weight
sum plus continuous norm. Thus the full raw column Frobenius bounds
are1920 and256 respectively. With ||Zhat_T||_F<23 and ||Ghat||_F<8,
the gamma_2048 bounds for all row-map products, coordinate conversion
and additions are <1e-6. The raw square uses its separately checked
<1000 Frobenius bound, including actual D. These allowances are in
(10). All finite weights are bounded, and the complete weighted-center
trace is<2.712; Gram rounding and127 block accumulations are <1e-6,
well inside the1e-4 matrix/nuclear/trace allowance in(11). The exact
rational H assembly error is paid separately, as stated in Section4.
Tail six-row products have dimension<=1024, row norms<40 and weights
<.012; their product, conversion and scalar errors fit1e-5. Final
assembly is also paid by1e-5. Every generated entry block passes the
<400 magnitude check. There is no unbounded interchange: all finite
products are finite, infinite Gram estimates are dominated by the
explicit square-summable tails(12)-(15).

Reproduce from the notebook:

    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/separation-seven/tail-galerkin-family-locator-594.py
    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/separation-seven/tail-galerkin-family-certificate-594.py

Full certificate: `scripts/separation-seven/tail-galerkin-family-certificate-594.json`.
Full finite matrices, all five factors, comparison, square radii and
six boundary functionals: corresponding `.npz`. The JSON includes all
neutral ratios, uniform bounds, all126 higher row-block records, full
residual digest, input/source/archive hashes and every check/failure.
Every block's residual is reproducible from the script and pinned
inputs; its complete covariance is saved, not a sampled-row estimate.
No failure is recorded. The complete bound fields and the final factor
ledger were inspected, not inferred from a preview or center eigenvalue.
The diagnostic locator is retained and explicitly uncertified. Old
artifacts and C999n's obstruction remain unchanged.

This supplies one finite-band component of a possible revised endpoint
assembly. It proves neither a replacement mixed bound nor a bound on
the endpoint complement above1023. All inherited qualifications remain;
Section8 supplies the separate conceptual audit of the refined entry
radii, uniform family arithmetic, complete tails and exact-predictor
correction. STATUS stays IN_PROGRESS.

### 8. Separate conceptual audit — 12 November 2026, step596

**Decision and scope.** The invocation-start assessment594, separately
approved595, licenses this unchanged audit. Inequality(1) is upheld for
all1024 independent complex endpoint coordinates, with the exact neutral
middle Galerkin map and unchanged R. This establishes the usability of
the proposed local input under its contracts; it is REPRODUCTION, not a
new general theorem or an RH candidate. No band, middle space, predictor,
reference, cutoff, penalty, allocation or threshold was tuned.

**Domains and exact map.** The moment calculation in Section1 holds for
both signs of c and both parities, including the different normalization
at0. The two low moment columns are independent: their ratios of plus
to minus moments are exp(ell/2) and -exp(ell/2). Thus Z gives precisely
the neutral completion for arbitrary complex free coordinates, and Z_T
is its exact band subset. Finite vectors are in Dom(D)=Dom(L). Pairing
against every v in V0 identifies A0g=P0Lg. The representation theorem
is applied on H0, where the whole-neutral-core and coercivity contracts
are retained. The larger-space relation has form domain V0, contained
in R's domain V; R<=L=a0 on V0 has the direction required by Behrndt
et al. Proposition2.1 and Corollary3.5, precisely cited above. Its inverse
is A0^-1P0. These facts give(2) by the established square completion.
The finite A floor proves only A's invertibility. It does not improve
A0's inherited c_* floor, audit that source computation or require an
unrestricted projected-inverse identity.

**Refined entry radii.** For unequal indices C744w(13), after multiplying
by2nu_n nu_m and using nu_n nu_m<=2/ell, gives exactly(3). For n=0
or m=0 the smaller normalization preserves that bound; opposite parity
vanishes before rounding. The diagonal has separate D error q_n and
the direct response-sum remainder times2nu_n^2<8, giving(4). There is
no differentiation of an asymptotic remainder. Exponential/continuous
suffixes and elementary errors remain covered by the stated allowance.
On the new rectangle the worst cancellation ratio is at1024,1023 and
is <1024. The square's1023,1022 ratio is smaller. The unchanged bound
on shift arguments is <207000. Thus the scalar elementary ledger applies
to every entry, without importing an old accumulated matrix bound.

The audit checks all67,108,864 radius entries, not a sample. Independently
rounded outward binary64 operations bound each positive rational expression
in Section2; diagonal rational bounds additionally use110-place integer
outward arithmetic. Every stored/generated radius exceeds that independent
analytic-plus-1e-7 upper bound by more than9.9999996e-13. Integer squares
and their nonzero differences are exact in this range. The complete
nonnegative sum has at most2^26 terms; gamma_(2^26+10)<1e-8 justifies
the norm inflation, including products and square root. Complete square
and rectangular norms fit(5), with every block recorded. Symmetrization
cannot enlarge the symmetric square-radius bound.

**Finite covariance and predictor.** All1022 moment ratios and the full
sparsity/subset identities were checked with independent integer intervals.
The entire A,B,G and trial-energy matrices rebuild from the pinned complete
square. The positive-factor reconstructions establish(7). In exact
coordinates, A(Y-Yhat)=B-A Yhat; hence(8). Orthogonality gives exactly

    Q_actual(f,ZYhat x,h)-Q_actual(f,ZYx,h)
       =x*(Y-Yhat)* A (Y-Yhat)x <= r_G^2/a ||x||^2.

This proves the direction and size of the loss in(9). The original U
occurs in the endpoint energy with its full signed orientation, and
does not enter the middle forcing.

Every residual row is combined before taking its weighted outer product.
The raw512:1023 rows retain actual Dg. All126 higher512-row blocks
partition1024:65535 exactly; both forcing orientations and the complete
response are retained. Exact CZYhat=0 removes only the true penalty,
not any part of R. Independent interval checks cover every one of the
65024 positive d_n lower endpoints and every upward inverse weight.
Both copies of all512 quarter-metric entries round in the required
upper direction. Head, finite complement and infinite tail can be added
without cross terms because their reference output spaces are orthogonal.
No terms within any one output range are treated as orthogonal.

For the trace estimate, use the exact positive Gram matrix of the stored
dyadic row map with true rational H^-1 and the chosen positive weights.
The floating head center need not be assumed positive. If X is the exact
head inverse action and Xhat its proposal, then

    ||rhohat_P*(X-Xhat)||_1
       <=||rhohat_P||_F ||X-Xhat||_F
       <=||rhohat_P||_F e_H/.239999.

Here ||.||_1 denotes nuclear norm. Symmetrization is contractive for
that norm. Thus the bound controls both operator and trace error.
The product-rounding nuclear error is bounded by sqrt(1024) times
its Frobenius error. Together with Gram accumulation and the exact-H
assembly error, the independent total is <.000002074<.0001. The
trace allowance in(11) therefore bounds the exact positive center
trace. Expanding the norm of center plus error gives precisely
2sqrt(trace_upper)delta_F+delta_F^2; no unproved center positivity
or missing mixed covariance is used.

**Every infinite output.** For positive delay the exact normalized shift
entry is (2/pi)t_m[-(-1)^(n+m)n sin(k_n delta)+m sin(k_m delta)]/
(n^2-m^2); for negative delay it is
(2/pi)t_m[n sin(k_n delta)-(-1)^(n+m)m sin(k_m delta)]/(n^2-m^2).
Subtracting the respective1/n term leaves the bound in Section5,
uniformly for m<=1023 and n>=65536. At m=0 the remainder is zero.
Reversing delay swaps the boundary functionals for the adjoint endpoint.
The integral tails from K-1 of n^-6 and n^-4 prove(12).

For the response, with p=m mod2 and matching output parity, the exact
difference from the parity-low column is

    S_nm-(nu_m/nu_p)S_np
      =2nu_n nu_m(k_p^2-k_m^2) sum_(j>=0)
        c_j^2(1-(-1)^n exp(-ell c_j)) /
        [(c_j^2+k_n^2)(c_j^2+k_m^2)(c_j^2+k_p^2)].

Use k_m^2-k_p^2<=k_m^2, the exponential factor<=2, and
c_j^2/(c_j^2+k_p^2)<=1. The decreasing resolvent-sum comparison
gives at most(8ell/pi^2+2m)/n^2, smaller than the bound used in(13).
For m=p, including0, the difference is zero; opposite parities vanish.
The remaining even and odd base coefficients are sqrt(2)v_e and v_o.
The all-m entry bound |S_nm|<=1/n+b/n^2 uses only
c_j^2/(c_j^2+k_m^2)<=1, so it applies to the enlarged support too.
This also justifies the unweighted far LZ bound in(17).

All six functional rows were rebuilt completely. For their complex
values b_j, (sum w_j|b_j|)^2<=(sum w_j)sum w_j|b_j|^2 gives C_b,
including every cross term. The full continuous norm kappa and the
two remainder operators give(14). Young's inequality with epsilon=1/10
gives factors11/10 and11. Since d'(t)=1/t+4ell^2/(9t^3)>0,
2/d_K bounds every remaining inverse weight. Thus(15) includes all
n>=65536; no tested frequency prefix replaces an infinite estimate.

**Entire LZ correction and final order.** The full factor for the local
operator norm bounds the first1024 outputs, including actual D. Its
Gram-formation error fits the10.000001 enlargement. Higher outputs
contain S alone because of finite support and exact neutrality. The
complete finite higher Frobenius sum and the just-checked infinite S
bound give b_mid and b_far. The worst head inverse bound may be used
on0:1023, since it also exceeds2/6.14 on512:1023. This proves(17)
for the entire weighted map. Expanding its perturbation of rho_tilde,
whose complete covariance is bounded by C_tilde, gives(18). The bound
uses the whole covariance Frobenius norm, not a center eigenvalue.

The independent scalar checks give

    e_trial<.003265064, e_F<.024433060,
    t_rem<.006313785, b_LZ<20.415951150,
    delta_G<.043960215, e_G<.115576619.

All finite, six-row, covariance and final comparison assemblies were
checked in full. Under gamma_r=ru/(1-ru), u=2^-53, the independent
arithmetic budgets are <4.667e-7 for A, <6.794e-8 for B, <5.032e-6
for the trial, <1.619e-8 for all residual row products, <1.046e-7 for
the boundary matrix and <1.008e-10 for H assembly. These fit their
respective original allowances, including coordinate conversion. The
complete response bound used in the row-product ledger is legitimate:
3^(-1/4)<.76 gives d_a>.24 and (2ell+2pi)/.24<60 in C744v's
Carleman bound. The complete prime-plus-continuous norm is <8 for
both orientations. Hence the raw column Frobenius caps1920 and256,
slightly enlarged for entry errors, cover the full row-map arithmetic.

All five original factors were reconstructed over every entry. Using
gamma_2048*100000 plus2e-7 for assembly/subtraction/norm errors gives
total error <2.228e-7<1e-6 for each. The additional predictor and LZ
norm enlargements pay their Gram errors separately. In particular the
complete final factor proves M_cert>=.001I-1e-6 I=.000999I.
Equations(2),(9),(18),(19) now imply(1) in Hermitian order for all
complex x, not only the real directions used to store the matrices.

**Artifacts and preserved checker failure.** Reproduce with

    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/separation-seven/tail-galerkin-family-replay-596.py
    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/separation-seven/tail-galerkin-family-audit-596.py

The100-digit replay has separate py/json/npz/log artifacts with basename
`scripts/separation-seven/tail-galerkin-family-replay-596`. All22 arrays
and the complete higher-residual digest match594 bit for bit. The audit
py/json/log basename is `scripts/separation-seven/tail-galerkin-family-audit-596`;
its132532 checks pass, with no failures. Full scalar intervals, every
radius-block record, factors, arithmetic budgets, pins and qualifications
are saved. The selected complete bounds, factors and failure fields were
inspected; no preview or diagnostic eigenvalue establishes the conclusion.

The first audit checker grouped the1e-7 and1e-12 additions before adding
them to the radius, unlike594's two additions. Its exact-byte square
comparison therefore failed in both512-row blocks, although the outward
enclosure checks passed. The original script replay agreed exactly.
The initial checker py/json/log are preserved with basename
`tail-galerkin-family-audit-first-pass-596`. Correcting only the checker's
operation order resolves those failures; every radius must still exceed
the independent outward bound. No source artifact or mathematical
parameter changed, and no sign failure was suppressed.

The audit leaves C999n's zero-middle stop intact. C999m's old mixed
constant cannot be transferred to this predictor. Head/band and band/high
cross terms, higher endpoints, C744q, H2, non-neutral coverage and
actual-Xi assembly remain open, as do all expressly retained source/core
qualifications. No claim of progress beyond the checked methods is made.

## Mathlib

Full matching coverage for this fixed-band numerical comparison and
complete-response operators has not been checked. General Hilbert/form
results are cited precisely above; source coverage is not evidence of a
matching Mathlib theorem or its absence. No formal verification is claimed.
