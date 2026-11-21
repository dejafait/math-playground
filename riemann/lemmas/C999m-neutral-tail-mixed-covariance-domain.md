# C999m: Neutral tail coordinates and the exact signed mixed map

## Hypotheses

Use the complete operators D,S,T of C744v, the complete separation14
operator U and restricted neutral form a0 of C744z, and the reference
R of C999k. Thus ell=log(3)/2, L=D+S+256C*C, H0=ker C, and

    V={f: sum_(n>=0)(1+log(2+n))|f_n|^2<infinity},
    V0=V intersect H0.

The inner product in the inherited form statements is first-slot
linear. In coefficient matrices x*Ay uses the usual conjugate transpose;
these conventions give the same real quadratic forms. Every adjoint
below is the ordinary Hilbert adjoint. Endpoints are independent and
complex. Retain the analytic-response, whole-neutral-core and unreplayed
c_* qualifications of C744z and the IEEE754/Decimal qualifications of
C999k/l. No RH or H2 premise, complementary sign or new scalar floor
for A0 is assumed.

Use C999l's EXACT Z_H:C^510->H0, exact Galerkin predictor G:C^1020->V0,
and certified head comparison M_cert, with M_cert>=.000999 I under
its Section7 audit. The predictor is zero on free tail inputs. R has
head0:511 equal to C999k's exact rational H, and diagonal h(k_n)/2
on raw modes n>=512. In particular R is positive with bounded inverse.
All finite head vectors and Gx belong to Dom(L)=Dom(D).

The general closed-form representation and inverse-order theorems are
imported, not reproved: Teschl, *Mathematical Methods in Quantum
Mechanics*, GSM99 author version, 12February2009, Theorems2.13/2.18,
printed pp71-72/77,
[author PDF](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf);
Behrndt–Hassi–de Snoo–Wietsma, arXiv:1403.5704v1, Proposition2.1 p4,
Corollary3.5 p12 and Theorem3.4's nonnegative proof case p11,
[pinned PDF](https://arxiv.org/pdf/1403.5704v1).
Their exact restricted-relation applicability is already established
in C999k/l. Assessment562, approved separately in563, covers the
specialization here. This is REPRODUCTION, not a novelty claim.

## Conclusion

**Audit status, step579:** Section18 upholds Sections12-17's complete
mixed-quarter comparison under the stated inherited contracts. The full
mixed norm is <.497655<1/2, hence G_mix<=M_cert/4. This validates the
previously claimed local bound; it does not improve its constant or prove
endpoint-complement coercivity. The earlier unaudited/open-quarter labels
below record their original step status and are superseded by Section18.

**Historical audit status, step570:** Section11 upholds Sections1-10's domain,
polarization, proxy/output decomposition and five component bounds
under the stated inherited contracts. Earlier statements that those
steps awaited audit describe their original status. The finite FFT
locator and the full quarter inequality remain uncertified.

**Step571, not independently audited:** Section12 improves the complete
input-tail bound for B_tilde^(K) from .25 to .151 by a joint finite
matrix majorant, with every center error and low correction included.
With the unchanged .163 output and .008 predictor allowances, a
certified finite covariance <=.085440 would suffice. The finite
locator is still uncertified; no quarter decision follows.

**Step572, not independently audited:** Section13 certifies the ENTIRE
saved dyadic finite-row proposal, with exact neutral ratios and weights,
by G_center<=.083 M_cert. This is not the finite covariance of the
exact operator: its normalized distance from that proposal is unpaid.
A distance <=.004204 would suffice with Section12's allowances. No FFT
accuracy, quarter pass/rejection or complementary sign is asserted.

**Step573, not independently audited:** Section14 pays the complete
normalized head-inverse error relative to the unchanged saved head
solution by <.001556. It uses outward head-entry enclosures and a full
verified inverse correction. This is one component of (51), not its
total error; the remaining finite arithmetic/FFT connection is unpaid.

**Step574, not independently audited:** Section15 pays the complete
complementary inverse-output error relative to locator565 by
<.000001271423<.000002. Together with Section14 this leaves the
sufficient finite direct-map/FFT allowance .002646. Neither that
remaining error nor the quarter inequality is decided.

**Step575, not independently audited:** Section16 encloses the complete
finite direct action around a saved dyadic center with normalized error
<3.740262e-7<.000001. This leaves the sufficient allowance .002645 for
the exact finite T/T* action on the unchanged complementary inverse
center versus the specified dyadic difference. No FFT accuracy, exact
finite covariance or quarter inequality is certified.

**Step576, not independently audited:** Section17 pays that entire
remaining finite action error by <.000002142174<.002645. Together with
Sections12-16 and the audited earlier allowances this gives finite
covariance <.083901959 M_cert and full mixed norm <.497655<1/2,
hence G_mix<=M_cert/4, under the retained contracts. This supersedes
earlier open-quarter statements as an unaudited local conclusion.
Sections12-17 require separate critical audit. No endpoint-complement
coercivity, full form positivity or RH conclusion follows from this bound.

Let p=n mod2, k_n=n*pi/ell, nu_0=ell^-1/2 and nu_n=sqrt(2/ell)
for n>0. Define, for n>=512,

    r_n=(nu_n/nu_p)(1/4+k_p^2)/(1/4+k_n^2),
    d_n=log(n/(2ell))-2ell^2/(9n^2).

The d_n are positive, increasing and >6.14. Let E be the ordinary
ell2 space on n>=512 and let Y_D have squared norm sum d_n|y_n|^2.
The formula

    (Z_T y)_n=y_n (n>=512),
    (Z_T y)_p=-sum_(n>=512,n mod2=p)r_n y_n (p=0,1),
    (Z_T y)_n=0 (2<=n<512)                              (1)

extends boundedly E->H0 and continuously Y_D->V0. The map
(u,y)->Z_Hu+Z_Ty is a bounded bijection C^510 direct-sum Y_D->V0
with continuous inverse, for the form norm on V0. Finite free tails
are dense in this norm after their exact low corrections are made.
This decomposition is not orthogonal in physical coefficients.

For x=(x_f,x_h), put f_H=Z_Hx_f, h_H=Z_Hx_h, g=Gx and

    rho_H=T f_H+T* h_H-Lg, v=g+R^-1 rho_H,
    W_f x=L f_H-U* h_H-T* v,
    W_h x=L h_H-U f_H-T v.                            (2)

These are bounded maps from the finite head space into L2. For
y=(y_f,y_h) in Y_D direct-sum Y_D define f=f_H+Z_Ty_f,
h=h_H+Z_Ty_h and

    rho=rho_H+T Z_Ty_f+T* Z_Ty_h,
    F(x,y)=Q_actual(f,g,h)-<R^-1 rho,rho>.

All expressions are defined, and C999l's comparison extends to

    Q_min(f,h)>=F(x,y).                               (3)

The exact mixed map, with F(x,y)-F(x,0)-F(0,y)=2Re(x*By), is

    B* x=(Z_T* W_f x,Z_T* W_h x),
    (Z_T* w)_n=w_n-r_n w_p, n>=512.                  (4)

In (4) Z_T* is the ordinary E/L2 adjoint. The weighted adjoint
would include D_tail^-1. In particular B extends boundedly from
E direct-sum E to the head space, and

    G_mix=B D_tail^-1 B*
      =sum_(a=f,h) sum_(n>=512) b_(a,n)b_(a,n)*/d_n  (5)

converges in trace norm. Here b_(a,n)=B e_(a,n); no cross product
inside a signed column is dropped. Under the inherited contracts,
Section17's estimate, audited in Section18, establishes G_mix<=M_cert/4.
The separate complementary lower comparison remains unresolved.

Section6's step565 specialization additionally bounds the ENTIRE
inverse-output truncation error at K=65536 by

    ||M_cert^-1/2 (B-B^(K)) D_tail^-1/2|| < .163,       (12)

where B^(K) is exactly the map of Section4: only R^-1 rho_H is
truncated, and all other operators and input coordinates remain
complete. This includes the exact-predictor correction under the
inherited contracts. It is not an input-tail estimate or a certificate
for the finite numerical locator. The new bound is not independently
audited; it is a local application of the prior tail certificate.

Section7's step566 specialization also pays the complete REMOTE-U
component of the input tail. Define A_U x=(-U*h_H,-Uf_H). With the
projections of Section4 and K=65536, it proves

    ||D_tail^-1/2 J_K diag(Z_T*,Z_T*) A_U M_cert^-1/2||
         < .111319476 < .12.                         (17)

Both orientations, the identity translation, full continuous U and
the neutral low corrections are retained. This is a component norm
bound, not a covariance increment or a bound for the entire W. The
other input terms and finite signed arithmetic remain unpaid. It is
unaudited and has the same inherited qualifications.

Section8 pays the exact-predictor approximation in the mixed map. Let
Y be C999l's exact free Galerkin predictor and Yhat its saved dyadic
proposal. Define B_tilde by replacing G=Z_H Y with Z_H Yhat in (2),
using the SAME exact neutral Z_H, and leaving every other input fixed.
Then, for the complete maps and also their Section4 output truncations,

    ||M_cert^-1/2(B-B_tilde)D_tail^-1/2|| < .008,
    ||M_cert^-1/2(B^(K)-B_tilde^(K))D_tail^-1/2|| < .008. (23)

The directed upper bound is <.007245510. These hold for all free
inputs n>=512, including their low corrections. B_tilde is only a
numerical proxy; M_cert still compares the exact predictor. Finite
entry, basis-conversion, head-solve and FFT errors in the locator are
separate obligations. This is an unaudited standard-method estimate,
not a change to the predictor or a quarter-budget decision.

Section9 pays the complete local/direct-trial part of the INPUT tail
for the same proxy, with exact Z_H and fixed dyadic Yhat. Put

    g_tilde=Z_H Yhat x,
    A_LT x=(L f_H-T* g_tilde, L h_H-T g_tilde).

Then, for K=65536,

    ||D_tail^-1/2 J_K diag(Z_T*,Z_T*) A_LT M_cert^-1/2||
        < .057921770 < .06.                          (27)

The full S, both T orientations, continuous T and both low corrections
are paid. This component is identical in B_tilde and B_tilde^(K).
Section10 bounds the inverse-action input component for B_tilde^(K).
Its complete normalized norm on free inputs n>=65536 is
<.078922337<.08, retaining the inverse head, both T orientations
and both neutral corrections.
The predictor change in(23) is to be paid once for the whole map,
not separately through each component. These estimates are unaudited local
REPRODUCTION under the inherited contracts, not a quarter decision.

## Proof

### 1. Weighted neutral coordinates and density

C999l's directly integrated moment formula is

    C_c(e_n)=nu_n c[(-1)^n exp(c ell)-1]/(1/4+k_n^2),
    c=+/-1/2.

For a fixed parity it gives C_c(e_n)=r_n C_c(e_p). The two
low-mode moment columns are independent: their plus/minus ratios
are exp(ell/2) and -exp(ell/2), respectively, and their entries
are nonzero. Thus (1) annihilates both moments for finite inputs.

For all n>=512, 0<r_n<=2/n^2. Indeed, for odd n its numerator
after division by pi^2/ell^2 is 1+ell^2/(4pi^2)<2; for even n
it is sqrt(2)ell^2/(4pi^2)<2. The denominator is at least n^2.
This uses ell<1 and pi>3. Consequently

    a_p(K)=sum_(n>=K,n mod2=p) r_n^2/d_n
       <=4/[3d_K(K-1)^3], K>=512,                    (6)

by monotonicity of d_n and the integral bound for sum n^-4.
The analogous unweighted sums of r_n^2 also converge. Ordinary or
weighted Cauchy--Schwarz therefore proves absolute convergence and
boundedness of the two low-coordinate functionals. Since raw tail
and raw low supports are orthogonal,

    ||Z_T y||_2^2=||y||_2^2+
              sum_(p=0,1)|sum_(n mod2=p)r_n y_n|^2,
    ||Z_T D_tail^-1/2||^2
       <=1/d_512+max_p a_p(512)=:zeta^2.              (7)

The same symbol D_tail in (7) means the single endpoint diagonal;
the direct sum of two copies has the identical norm bound.

From the displayed formula for d_n,
d_n/(1+log(2+n))->1, and every d_n on n>=512 is positive.
It follows that these two positive weights are bounded above and
below by fixed multiples of one another: choose an eventual ratio
interval [1/2,2] and take extrema over the remaining finite set.
The finite two low weights cause no problem by (6). Hence Z_T
maps Y_D continuously to V. Its finite truncations with the low
corrections recomputed converge in V: the tail weighted series tends
to zero and (6) bounds the difference of each low correction.
The moment map is continuous on L2, so their limit remains neutral.
This proves Z_T:Y_D->V0 and the stated density without asserting
boundary traces for Y_D or neutrality of raw orthogonal projections.

Conversely, for f in V0, take u_n=f_n for 2<=n<512 and y_n=f_n
for n>=512. The equivalence of weights gives y in Y_D. The two
moment series converge (by L2 continuity, or the same Cauchy--Schwarz
bound). Their ratios above and independence at0,1 force exactly the
low coefficients of Z_Hu+Z_Ty. This proves surjectivity and uniqueness.
Coefficient restriction is continuous in the displayed weighted norm,
which is equivalent to the shifted a0 form norm by C744z. The inverse
is therefore continuous. No orthogonality of the low corrections is
asserted.

### 2. Forcing and the extension of the comparison

For x,y as stated, f,h lie in V0 and g is finite and neutral. Thus
g lies in Dom(A0), with A0g=P0Lg, exactly by C999l's strong-domain
argument (or C999j). The bounded T,T* give rho in L2 and

    P0rho=P0Tf+P0T*h-A0g.

C744z's square completion is valid for every f,h in V0, since the
forcing is in H0 and A0^-1 maps H0 into Dom(A0). The restricted
relation has form domain V0, while R has domain V and satisfies
R<=L=a0 on V0. The cited inverse order, already applied in C999k/l,
gives A0^-1P0<=R^-1 on L2. Applying it to this rho proves (3).
No unbounded L is applied to a general tail endpoint; only the
local endpoint form is used there. All terms of F are continuous
in x,y for the product form norm, so finite neutral free sequences
approximate every occurrence of F. The full U is bounded by C744z
and is retained in the original energy.

### 3. Exact polarization and covariance convergence

Write f_T=Z_Ty_f and h_T=Z_Ty_h. In matrix notation the three-cell
energy is

    a0(f,f)+a0(g,g)+a0(h,h)
       -2Re[g*(Tf+T*h)+h*Uf].

The coefficient of the mixed real term between head x and tail y
is therefore

    (L f_H)*f_T+(L h_H)*h_T
       -h_H*U f_T-f_H*U* h_T
       -g*(T f_T+T* h_T)
       -rho_H*R^-1(T f_T+T* h_T).                    (8)

Here a0(head,tail) has the displayed L representative because
the head is in Dom(L) and both vectors are neutral. In particular
this includes the D cross products at0,1 and the entire S; the
penalty is exactly zero on neutral arguments. The middle energy
a0(g,g) contributes only to F(x,0), because the predictor has no
tail dependence. Since R^-1 is selfadjoint, grouping (8) gives
(W_f x)*f_T+(W_h x)*h_T, proving (4) first on finite tails and
then by continuity. This verifies both T orientations and both U
orientations, and retains the signed residual cross product.

The maps LZ_H and LG have finite-dimensional domains with every
column in L2. U,T,T*,R^-1 are bounded. Thus W=(W_f,W_h) is
bounded into L2 direct-sum L2. The ordinary extension Z_T:E->L2
proved above gives B=W*diag(Z_T,Z_T), a bounded map on the
ordinary free-tail Hilbert space. Its adjoint formula follows by
coefficient pairing: each low correction contributes -r_n w_p.
The reality of r_n is essential for this written adjoint formula.

Choose the1020 standard unit head vectors. Each of their images
under B* is in E direct-sum E. Summing their squared norms proves
sum_(a,n)||b_(a,n)||^2<infinity, with only a finite sum over head
vectors. Since d_n>=d_512>0, the traces of the nonnegative rank-one
terms in (5) are summable. The series therefore converges in trace
norm and equals B D_tail^-1 B* by finite truncation and the
coefficient identity. Thus every omitted input-column covariance
is nonnegative, but no omission of an inverse-output contribution
has such a sign.

### 4. Distinct input and inverse-output error bounds

These are applicability bounds for the unchanged K=65536 test,
not numerical quarter-budget enclosures. Let Q_K project raw L2
onto n>=K, P_low onto modes0,1, and let the same symbols act
componentwise on a pair. Let J_K project free input coordinates
onto n>=K. For any bounded finite-head map A into a pair of L2
spaces, (4), the triangle inequality and (6) give

    ||D_tail^-1/2 J_K diag(Z_T*,Z_T*) A||
      <=||Q_K A||/sqrt(d_K)
            +sqrt(max_p a_p(K)) ||P_low A||.          (9)

In fact the first summand is the weighted raw tail. The second
has in each parity squared norm a_p(K) times the squared low
coefficient, so its operator bound is the one displayed. Taking
A=W M_cert^-1/2 bounds the square root of the normalized omitted
INPUT covariance. It requires a bound for the full W, not just
its finite-head or displayed entries.

For OUTPUT truncation put V_R=R^-1 rho_H, a map on the head,
and construct W^(K) by replacing V_R in (2) by (I-Q_K)V_R only.
Let B^(K)=W^(K)*diag(Z_T,Z_T). All other operators are unchanged.
Then the pair W-W^(K) is exactly

    (-T*Q_K V_R,-T Q_K V_R).

Consequently (7) gives the complete error bound

    ||M_cert^-1/2 (B-B^(K)) D_tail^-1/2||
       <=zeta sqrt(2)||T||
                  ||Q_K R^-1 rho_H M_cert^-1/2||.    (10)

Since R equals D/2 on these raw output modes and h(k_n)>=d_n,

    ||Q_K R^-1 rho_H M_cert^-1/2||
       <=sqrt(2/d_K)
          ||Q_K R^-1/2 rho_H M_cert^-1/2||.           (11)

To verify (11), coefficientwise (2/h(k_n))^2 is at most
(2/d_K)(2/h(k_n)); sum these nonnegative inequalities for each
head vector and take the operator norm. Bounds (9)-(11) keep the
two tails separate. C999l's head-residual tail bounds may help
pay (11), with its exact-predictor correction retained. They do
not by themselves pay (9) or the finite signed covariance. No
cross-product orthogonality between terms of a mixed column is
claimed. These elementary specialization bounds are not a reproof
of a standard Schur theorem.

### 5. Diagnostic and limits of this attempt

The saved locator is `scripts/separation-seven/signed-mixed-diagnostic-564.py`;
its complete proposed arrays and record are the same basename with
npz/json extensions. Reproduce with

    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/separation-seven/signed-mixed-diagnostic-564.py

It uses input columns512:1023 and initially retains only raw inverse
outputs0:511. Its diagnostic generalized covariance ratio is about
.0620074133, versus the required upper bound .25. This is neither
an upper nor a lower bound for the actual complete G_mix: complementary
inverse outputs change each signed column before its square. Arithmetic,
exact-predictor errors and those outputs are unpaid. A second saved
diagnostic, `scripts/separation-seven/signed-mixed-output-diagnostic-564.json`,
records the existing output residual covariance relative to M_cert;
it is not a mixed covariance or a certificate. No favorable direction,
unpaid finite range or diagnostic eigenvalue proves the quarter budget.

The useful established input is (1)-(5), with the explicit distinction
(9)-(11), not a sign or a new general theorem. The quantitative test
remains unfinished. No change of predictor, reference, K, allocation or
complementary-sign premise has been made. The result has not received
a separate conceptual audit. Complement coercivity, C744q margin,
H2 slack/existence, non-neutral coverage and global actual-Xi assembly
remain unresolved. This is not an RH candidate or a negative actual
triple, and the prior scalar/prefix/factorization stops are preserved.

### 6. Complete inverse-output allowance and finite locator — step565

**The part certified.** Let C_t denote the exact Hermitian part of
`tail_covariance_upper` in `scripts/separation-seven/neutral-head-covariance-559.npz`.
It is the saved C999l(16) quadratic upper bound, including its matrix
allowance. Let rho_tilde be C999l's residual for the exact neutral
vector Z_H Yhat x, with its unchanged dyadic Yhat. The audited tail
inequality is

    ||Q_K R^-1/2 rho_tilde x||^2 <= x* C_t x.

The new complete factor verification gives

    C_t <= .02 M_cert.                                (13)

Here .02 is an upper bound for an already fixed error contribution;
it changes neither the quarter budget nor the reference or predictor.
To verify (13), the script proposes a factor for
.02 M_cert-C_t-10^-6 I and checks its full1020 by1020 reconstruction.
The observed Frobenius residual is below10^-7, the squared factor
Frobenius norm is below100000, and every involved matrix entry has
absolute value below400. As in C999l Section7, the exact error is
bounded by

    10^-7 + gamma_2048*100000 + 2*10^-7 < 10^-6,
    gamma_j=(j*2^-53)/(1-j*2^-53).

The gamma term bounds the entire matrix product by its factor squared
Frobenius norm. The last term covers operand assembly (including the
exact decimal .02 and Hermitian part of C_t), subtraction and norm
evaluation; the dimensions and magnitudes are within the already
audited C999l ledger. The factor matrix plus its error is therefore
positive after restoring the subtracted10^-6 I. This proves (13),
without relying on a generalized eigenvalue or factorization success.
The original559 matrix/record hashes are checked against audit561;
both saved check lists and audit561's source pin are checked. The
new script does not regenerate or change their matrices.

The predictor is still the exact Galerkin one, not Yhat. C999l(7)
and its audit give ||Y-Yhat||<.000612 and ||Z_H||<1.008. C744w(6),(8),
used also in C999k Section2, give

    ||Q_K L P||=||Q_K (S+256C*C)P|| < .062501906.

This is the COMPLETE tail past65535, and P retains raw modes0:511.
The diagonal D has zero head-to-tail block. As rho_H-rho_tilde
=-L Z_H(Y-Yhat), and R is D/2 on this output range, we obtain

    ||Q_K R^-1/2(rho_H-rho_tilde)M_cert^-1/2||
       <=sqrt(2/d_K)*.062501906*1.008*.000612/sqrt(.000999)
       =: e_pred < .000520253.                        (14)

Use d_K>10.9963070613268 from C999l's audited directed bound.
Equations (13)-(14), by the triangle inequality for the weighted
residual maps, give

    ||Q_K R^-1/2 rho_H M_cert^-1/2||
        <=sqrt(.02)+e_pred < .141941609.               (15)

No independent residual components are squared and added here.
The exact-predictor change is paid before using (11).

For (7), d_512>6.14 and (6) give

    zeta <= sqrt(1/6.14+4/(3*6.14*511^3)) < .403567159.

Apply (10)-(11), with the complete C744v bound ||T||<4.71:

    ||M_cert^-1/2(B-B^(K))D_tail^-1/2||
       <=zeta*sqrt(2)*4.71*sqrt(2/d_K)*(sqrt(.02)+e_pred)
       < .162724526 < .163.                           (16)

The directed80-digit certificate evaluates the whole expression,
not the displayed rounded intermediate decimals. Its14 checks have
no failures. Reproduce with

    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/separation-seven/signed-mixed-output-tail-565.py

The full certificate, factor archive and log share the basename
`scripts/separation-seven/signed-mixed-output-tail-565` with json,
npz and log extensions. The source records the input pins and actual
error interval. This proves only (12), for all free input modes;
it does not bound the still unknown input covariance of B^(K).

**The finite calculation, not certified.** The independent locator
`scripts/separation-seven/signed-mixed-complete-locator-565.py` now
includes every input column512:65535 for both endpoints and every
inverse output0:65535. It retains all334 remote prime powers, both
T orientations, the continuous centers and exact-form low corrections
evaluated in floating point. It gives generalized ratio approximately
.0829002146552, versus the required .25. This is neither an upper
nor a lower bound for the complete G_mix. The earlier .062 locator
used a different, incomplete numerical expression and remains intact.

For reproducibility, here is the finite algebra used by the locator;
it introduces no new operator theorem. Put d_0=1/sqrt(2), d_n=1 for
n>0, P_n=(-1)^n and, for the relevant finite prime list,

    s_+(n)=sum_(delta>0) a_delta sin(k_n delta),
    s_-(n)=sum_(delta<0) a_delta sin(k_n delta).

The exact off-diagonal normalized shift sum is

    (2/pi)d_n d_m[-P_n P_m n s_+(n)+m s_+(m)
                    +n s_-(n)-P_n P_m m s_-(m)]/(n^2-m^2).

This follows by summing C744w's shift antiderivative entry before
forming the numerator. At n=m>0 its exact diagonal is
sum_delta a_delta[(1-|delta|/ell)cos(k_n delta)
-sign(delta)sin(k_n delta)/(ell k_n)]; at n=m=0 omit the sine term.
The zero delay in U contributes its weight times the identity, so it
occurs only in the diagonal. Replacing each delta by -delta gives
the adjoint, or equivalently replaces (s_+,s_-) by (-s_-,-s_+).
For n=0 or m=0 the same off-diagonal formula uses the stated d_0.

The finite inverse-output multiplication uses

    n/(n^2-m^2)=(1/(n-m)+1/(n+m))/2,
    m/(n^2-m^2)=(1/(n-m)-1/(n+m))/2,

only off the diagonal. For a finite vector u on0:K-1 set
H_+u=sum_(m!=n)[1/(n-m)+1/(n+m)]u_m and define H_- with a
minus sign. With v_n=d_n u_n, the prime action is exactly

    (d/pi)[-P s_+ H_+(Pv)+H_-(s_+ v)
                       +s_- H_+(v)-P H_-(P s_- v)] + diag*u.

All products outside H are pointwise. Toeplitz and Hankel convolution
evaluate these finite sums, with the m=n Hankel term removed and the
actual diagonal restored. The continuous part is a separate retained
rank-one-series center. These identities justify what the locator
computes in exact arithmetic; they do not certify the FFT library or
its errors. A64-mode floating replay discrepancy below8e-15 is only
a diagnostic implementation check, not a proof of numerical accuracy.

Reproduce with

    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/separation-seven/signed-mixed-complete-locator-565.py

The complete finite mixed covariance and direction are saved in its
npz archive; its json/log records the actual ratio, all unpaid items
and the digest of every combined signed column. Full raw mixed maps
and finite inverse-output arrays are respectively
`scripts/separation-seven/signed-mixed-columns-565.npy` and
`scripts/separation-seven/signed-mixed-inverse-output-565.npy`.
No finite signed column was dropped or squared before combining its
parts. The locator's failure list refers to what that calculation
alone certifies; the separate result (16) now pays its infinite-output
truncation obligation for the exact maps, while finite arithmetic,
exact-predictor/solve errors and the full input tail remain unpaid.
One cannot add .163 to the displayed squared ratio: (16) is a NORM
allowance and must be combined at norm level with certified bounds.

This is a partial quantitative advance on the existing method, not
a quarter-budget pass, rejection, complement sign, new theorem beyond
the checked sources or RH candidate. The main and independent gaps
listed in Section5 remain. No reference, predictor, K or quarter
allocation was changed, and neither new component has a separate
independent conceptual audit.

### 7. Complete remote-U input tail — step566

This is one partial calculation within the unchanged assessment562
test. The fixed predictor, reference, K and quarter allocation are
unchanged. C744z's scalar/derivative/response-prefix stops were checked;
none determines this signed mixed tail. The source-covered method is
reused. No Schur or inverse-order theorem is reproved, and no FFT
accuracy assumption is used. The geometric-series calculation below
is needed for the constants of this local U-tail specialization;
the assessed sources do not supply those constants.

**All delay cases.** Write a_q=Lambda(q)/sqrt(q) and
delta_q=14ell-log(q), for C744z's complete334 prime powers. The
exact zero-delay term q=2187 is a multiple of the identity. Its
raw output past K on a head vector is zero. It remains present
in the low-coordinate estimate below. Of the other333 terms,
127 have positive delay and206 negative delay. For each sign let
beta_q=|delta_q|/ell, so 0<beta_q<1, and define

    s_sign(n)=sum_(q in that sign) a_q sin(pi n beta_q),
    V_sign=sum_(n>=K) s_sign(n)^2/n^2.

For a nonresonant angle theta, the finite geometric identity gives

    |sum_(n=K)^M exp(i n theta)|<=1/|sin(theta/2)|.

Summation by parts with the decreasing weights n^-2, followed by
M->infinity, therefore gives

    |sum_(n>=K) cos(n theta)/n^2|
         <=1/[K^2 |sin(theta/2)|].                    (18)

To justify the limit, the unweighted partial sums are uniformly
bounded, the terminal weight tends to zero, and the sum of successive
weight differences is K^-2. The weighted series is also absolutely
convergent. No conditional interchange is needed.

For 0<=d<=1, sin(pi d/2)>=d, by concavity and its endpoint values.
Thus, for distinct beta_i,beta_j in one sign group, use the positive
resonance distances

    d_ij^-=|beta_i-beta_j|,
    d_ij^+=min(beta_i+beta_j,2-beta_i-beta_j).

Both distances lie in(0,1]. The diagonal difference is exactly zero
and is treated separately; d_ii^+ remains positive. Expanding the
finite square by 2sin(a)sin(b)=cos(a-b)-cos(a+b), then using(18)
and sum_(n>=K)n^-2<=1/(K-1), proves

    V_sign <= [sum_i a_i^2]/[2(K-1)]
       + [sum_i a_i^2/d_ii^+
          +2sum_(i<j)a_i a_j(1/d_ij^-+1/d_ij^+)]/(2K^2).
                                                               (19)

Every cross product within a prime group is accounted for in(19).
It is an upper bound, not the exact value of V_sign. Negative delays
give the negative of s_negative(n); this has the same square.
Replacing all delays by their negatives swaps the groups for U*,
so the same two bounds cover the adjoint.

The80-digit directed calculation independently enumerates the prime
powers with 3^13<q^2<3^15 by integer trial division and compares the
entire list with audited548. It encloses every beta, every weight,
and all8128 positive-group and21321 negative-group unordered pairs
including diagonals. The smallest certified resonance distances
exceed .00169979 and .00096628, respectively. In particular no
near-resonant pair is replaced by a generic separated-frequency
assumption. Equation(19) gives

    V_positive < .000031514229,
    V_negative < .000034732798.                       (20)

The full pairwise lower distances and contributions are retained
in the JSON certificate. The only exact resonance omitted from
the oscillatory bound is each diagonal difference, already paid
by the first term of(19).

**Head functionals and remainder.** Use C999l Section4's finite
head functionals v_+,v_-, with d_0=1/sqrt(2) and d_m=1 otherwise.
Only head vectors enter these functionals. Let b_j, j=1,...,4,
be their exact rows on x in the order

    v_-(f_H), v_+(f_H), v_+(h_H), v_-(h_H).

For each saved dyadic boundary row bhat_j, a complete1020-square
factor reconstruction verifies

    bhat_j* bhat_j <=144 M_cert.

The proposed factor target is M_cert-bhat_j* bhat_j/144-10^-6 I.
Every observed Frobenius reconstruction residual is below2.49e-14;
each squared factor Frobenius norm is below4834, and all matrix/factor
entries have absolute value below400. The same conservative ledger
as Section6 gives exact error at most

    10^-7+gamma_2048*100000+2*10^-7 <10^-6.

Here the outer product uses one multiplication per entry, division
by144 and subtraction; the four boundary rows together have Frobenius
norm below100. Their operand/product errors are within the2e-7
assembly allowance. The factor reconstruction, not factorization
success or an eigenvalue, proves the matrix inequality.

The exact-Z conversion norm is below10^-14 by C999l. A boundary
functional has coefficient norm below23; its512-term dot products,
the correctly rounded sqrt(2) conversion and stored operand bounds
give row error below10^-7, a deliberately loose allowance. Hence

    ||b_j M_cert^-1/2|| <= q_b
       :=12+10^-7/sqrt(.000999) <12.000003164.         (21)

These are Hermitian inequalities for all complex x. In particular
each paired boundary map has norm at most sqrt(2)q_b after the
same normalization, without assuming endpoint reflection or reality.

For output n>=K and input m<512, C744w's exact shift formula has
leading term -(2/pi)(-1)^n sin(k_n delta)d_m(-1)^m/n for delta>0,
and (2/pi)sin(k_n delta)d_m/n for delta<0. Its subtracted remainder
has absolute entry at most

    (2/pi)d_m/(1-(511/K)^2)*(m^2/n^3+m/n^2).

At m=0 it vanishes. Summing the squared coefficient bounds as in
C999l(11) gives the entire single-shift remainder norm j_rem,
with j_rem<.000147018713. The exact formula is C999l(11) with
N=512,K=65536. The proof uses integral tails of n^-6 and n^-4,
so it covers every remaining output, not a sampled range.

For A_U x=(-U*h_H,-Uf_H), the two sign groups and(20)-(21) give

    ||Q_K A_U M_cert^-1/2||
       <= (2/pi)sqrt(2)q_b(sqrt(V_positive)+sqrt(V_negative))
          +(a14*j_rem+kappa14)*1.008/sqrt(.000999),    (22)

where a14=sum_q a_q<52.201439223, and kappa14 is C744z(8)'s
complete continuous-operator norm. The identity shift has zero raw
head-to-tail remainder; including its weight in a14 only enlarges
this bound. For the pair of independent endpoints the remainder
operator is block off-diagonal and has norm at most a14*j_rem;
there is no additional endpoint covariance assumption. The two
sign contributions, remainder and continuous part are combined by
the triangle inequality before squaring. Their normalized unweighted
bounds in(22) are respectively less than .124321551, .244755738
and .000000225174. No boundary functional is applied to an arbitrary
infinite tail input.

**Exact low corrections and result.** The full low-output map has
norm at most29.813203120*1.008/sqrt(.000999), by C744z's full U
bound. Apply(9) with A=A_U M_cert^-1/2, d_K>10.9963070613268,
and(6). Its extra neutral-coordinate term is less than .000019734332.
Using the full directed expression, not the displayed rounded
summands, gives the bound in(17):

    [(22)'s right side]/sqrt(d_K)
       +sqrt(4/[3d_K(K-1)^3])*29.813203120*1.008/sqrt(.000999)
         < .111319476 < .12.

Reproduce from the notebook with

    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/separation-seven/signed-mixed-remote-input-tail-566.py

The complete JSON, factor NPZ and log share that basename. All34
checks pass. They include every boundary factor, complete prime
enumeration and pairwise sum, source pins, and a full reconstruction
and directed scalar recheck of the separate565 output allowance.
That recheck found no change to its <.163 bound; it is not a separate
conceptual audit of all of C999m.

The new .12 allowance is only the remote-U contribution in the
omitted INPUT columns. Lf_H,Lh_H and both T orientations applied
to g+R^-1rho_H must still be paid with their cross products. One
cannot add its squared allowance to those components' covariances
as though they were orthogonal. The complete finite locator's
arithmetic also remains unpaid. Thus there is no pass, finite-column
rejection, complementary sign or RH candidate. This is a local
standard-method specialization, not progress beyond the checked
sources claimed as original mathematics. The new result awaits a
separate conceptual audit under all retained contracts.

### 8. Complete exact-predictor error by reference cancellation — step567

This calculation remains inside the unchanged assessment562 target,
separately approved563. The intermediate test is a complete normalized
predictor error below .01, useful toward the required full mixed-map
norm at most .5. It neither allocates a new quarter nor changes K.
The scalar/derivative/prefix and automatic-factorization stops do not
decide this error. The assessed source method and C999k/l's audited
representation/inverse applicability are reused, without a new general
theorem or an FFT accuracy premise. All earlier artifacts are preserved.

**Exact cancellation and domain.** Write Z=Z_H and DeltaY=Y-Yhat.
Both ZY and ZYhat have finite raw support and lie in Dom(L). Therefore
all of the following expressions are genuine L2 vectors, uniformly
for the finite-dimensional head x. With the same forcing
b_H=Tf_H+T*h_H, the map v of (2) satisfies

    v=ZY+R^-1(b_H-LZY),
    v_tilde=ZYhat+R^-1(b_H-LZYhat),
    v-v_tilde=E DeltaY, E=(I-R^-1 L)Z.                (24)

Thus the local and U terms cancel in W-W_tilde; its pair of components
is (-T*E DeltaY,-T E DeltaY). This is a signed identity before any
norm bound, not an assumption that its constituent covariances are
independent. Let P be the raw projection onto0:511 and Q=I-P. Since
Z=PZ and R=H on P, D/2 on Q, the two parts of E are

    PE=H^-1(H-PLP)Z,
    QE=-2 D_Q^-1 QW0P Z, W0=S+256C*C.                (25)

No raw projection is asserted to preserve neutrality. The moment
penalty kills Z exactly, but it is harmlessly retained in the complete
operator bounds. In particular (25) requires no boundary trace on an
infinite tail input and does not substitute a projected inverse for A0.

**Entire complementary part.** C999k(3), audited in its Section6,
provides the complete order

    (QW0P)*(QW0P) <= Chat+.0046 I,

where Chat is the exact symmetric dyadic `cov00` in the unchanged
`complete-covariance-532.npz`. Its omitted infinite response and moment
terms, and all their within-column products, are already paid in that
order. The new full512-square factor reconstruction below proves
Chat<=.172 I. Since D_Q>=6.14 I and ||Z||<1.008, it follows that

    ||QE|| <= (2/6.14)*1.008*sqrt(.172+.0046)
            < .137980434.

This covers every raw output n>=512, not just the retained output
array. The factor is used for an upper order; Chat need not be treated
as an exactly nonnegative matrix merely because it approximates a Gram.

**Head defect and complete solve error.** Use C999k's exact rational
H=Mhat-.00024 I-(100/307)(Chat+.0046 I), and the same binary64 center
Hhat as C999l. The audited bounds are

    H>=.239999 I, ||H-Hhat||<10^-8,
    ||PLP-Mhat||<.00024, ||Z-Zhat||<10^-14.

The script proposes the512 by510 matrix Ehat by solving
Hhat Ehat=(Hhat-Mhat)Zhat. It checks the ENTIRE equation, rather than
assuming a numerical solver is accurate. The floating residual norm is
<1.362e-16. Its complete arithmetic ledger below gives the exact dyadic
equation residual bound10^-7. Also ||Ehat||_F<.0174 and
||Hhat-Mhat||_F<1, with norm evaluation paid. Subtract the exact
equation H PE=(H-PLP)Z from the proposed one to obtain

    ||PE-Ehat||
      <=[(10^-8+.00024)*1.008+10^-14+10^-7
                                           +10^-8*.0174]/.239999
      < .001008464.

The terms respectively cover H-Hhat and PLP-Mhat on Z, neutral basis
conversion against Hhat-Mhat, the complete dyadic equation residual,
and Hhat-H acting on Ehat. Hence ||PE||<.018408464<.019. The small
defect in (25), rather than separate bounds on I and H^-1 PLP, is what
makes this quantitative estimate useful. There is no new lower bound
for A0 in this argument.

**Arithmetic certificate.** The script
`scripts/separation-seven/signed-mixed-predictor-error-567.py` checks
the full input hashes against audit561 and the complete check lists
in559/561/557. The required arrays, including Ehat and the full
covariance factor, are stored in its NPZ archive. This is conditional
on the same IEEE754/Decimal contracts as C744w and C999l.

For Chat's upper order the proposed factor target is
.172 I-Chat-10^-6 I. The observed full reconstruction residual is
<4.777e-16, the squared factor Frobenius norm is <87.721, and the
maximum target/factor/Chat entry is <.415. The conservative inherited
ledger gives exact error at most

    10^-7+gamma_2048*100000+2*10^-7 <3.228e-7<10^-6,
    gamma_j=(j*2^-53)/(1-j*2^-53).

Here the first term encloses the observed residual, the gamma term
pays the full factor product, and the last term pays decimal-scalar
assembly, subtraction and norm evaluation. Restoring10^-6 I proves
the claimed upper order. No eigenvalue or Cholesky success is a proof.

For the head equation the observed full norms are
||Hhat||_F<317, ||Hhat-Mhat||_F<.091, ||Zhat||_F<22.584 and
||Ehat||_F<.017310. All operand entries are below400. Allowing
the larger bounds400,1,23,.0174, the Frobenius error of the two
matrix products is at most
gamma_2048*(1*23+400*.0174). An additional10^-8 covers the
subtraction Hhat-Mhat, the final difference and norm evaluation.
For example its first subtraction error is at most
u/(1-u)*(||Hhat||_F+||Mhat||_F), propagated against Zhat; both
matrix norms are below400, giving <3e-12. Product additions and
the final norm error fit within the remaining10^-8. Including the
observed residual gives <10^-7. The norm evaluation of Ehat has
at most261120 squared terms; even the sequential gamma_522240
bound is below6e-11 relative error. The separate10^-7 absolute
allowance therefore proves the deliberately looser .0174 bound.
These estimates include the full matrices, not selected entries.

**Weighted mixed-map estimate.** The ranges P and Q are orthogonal,
so the preceding complete estimates imply

    ||E|| <= sqrt((.0174+e_H)^2
                   +[(2/6.14)*1.008*sqrt(.1766)]^2)
            < .139202988,

where e_H is the displayed directed head-defect error expression,
not its rounded endpoint. C999l/audit561 gives ||DeltaY||<.000612.
Use (7), M_cert>=.000999 I and ||T||<4.71 to get

    ||M_cert^-1/2(B-B_tilde)D_tail^-1/2||
       <= sqrt(1/6.14+4/(3*6.14*511^3))*sqrt(2)*4.71
                         *||E||*.000612/sqrt(.000999)
       < .007245510 < .008 < .01.                    (26)

The two T orientations are both paid by sqrt(2)||T||. The weighted
neutral-coordinate norm includes both low corrections. All bounds
are complex operator bounds; no endpoint reflection restriction enters.
For B^(K), the predictor change in v is (I-Q_K)E DeltaY, because
Q_K Z=0. Orthogonal projection cannot increase its L2 norm, so the
same estimate proves the second inequality in (23).

Reproduce with

    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/separation-seven/signed-mixed-predictor-error-567.py

The full JSON, factor NPZ and log have that basename with their
respective extensions. All23 checks pass. The80-digit directed final
upper endpoint is .00724550991103618372...; it is used only through
the rigorous stated .008 allowance. No certificate check failed.

This completes one previously unpaid approximation obligation in the
approved test. It does not pay the finite locator's entry, head-solve,
basis-conversion or FFT errors, nor the remaining local/T/inverse input
tail. Combine this allowance at norm level, once; it is neither a
covariance increment nor a correction to M_cert. In particular a
certificate comparing B_tilde^(K) to M_cert can later use (23) followed
by Section6's exact-predictor output allowance. No such complete
certificate, complementary sign or RH candidate is claimed here.
The result awaits separate conceptual scrutiny; all original analytic,
whole-core, c_* and execution qualifications remain. This is local
REPRODUCTION, with no progress beyond the checked sources claimed
as mathematical originality.

### 9. Complete local/direct-trial input tail — step568

This is one further quantitative part of the unchanged assessment562
test, approved in563. The intermediate threshold is the norm .06 in
(27), compared with .5 for the full mixed map. It changes neither
the test's quarter allocation, K, reference nor exact predictor.
The existing scalar/derivative/response-prefix/factorization stops do
not decide this component. Reuse C999l Section4's complete response
and shift remainders and Section7's geometric estimate(19); there is
no new general theorem, FFT accuracy premise or literature refresh.
The standard representation/inverse sources in the Hypotheses remain
imports. Their constants do not supply this finite-head tail estimate.

**Scope and decomposition.** Define rho_tilde=b_H-Lg_tilde with
b_H=Tf_H+T*h_H. All of f_H,h_H,g_tilde are finite, exactly neutral
vectors in Dom(L). The complete proxy mixed representative is

    W_tilde=A_LT+A_U+A_R,
    A_U x=(-U*h_H,-Uf_H),
    A_R x=(-T*R^-1 rho_tilde,-T R^-1 rho_tilde).       (28)

For the output-truncated proxy replace R^-1rho_tilde in A_R by its
projection onto raw modes0:65535; the first two components do not
change. These are signed vector identities before squaring. Bound(27)
does not assert that the covariances of these components add. All
their cross products remain chargeable in the complete mixed map.

Write mu=.000999, z=1.008, y=1.320001, d=10.9963070613268.
The audited C999l inputs give M_cert>=mu I, ||Z_H||<z,
||Yhat||<y and d_K>d. Use its finite functionals v_e,v_o,v_+,v_-
with the same constant-mode normalization d_0=1/sqrt(2). Define

    b_L x=(sqrt(2)v_e(f_H),v_o(f_H),
                         sqrt(2)v_e(h_H),v_o(h_H)),
    b_+ x=v_+(g_tilde), b_- x=v_-(g_tilde).

Only finite vectors enter these boundary functionals. No boundary
trace of a general input in Y_D, or of R^-1rho_tilde, is assumed.

**Complete boundary factors and conversion.** The script specified
below constructs dyadic centers bhat_L,bhat_+,bhat_- from the unchanged
Zhat,Yhat in559 and verifies all entries of factors for

    M_cert-bhat_L* bhat_L/144-10^-6 I,
    M_cert-bhat_+* bhat_+/36-10^-6 I,
    M_cert-bhat_-* bhat_-/36-10^-6 I.

All full reconstruction residuals are below2.54e-14; the squared
factor Frobenius norms are below4836. The row, Gram, target, factor
and comparison entries are below6.01 in this execution. For the
conservative ledger the row Frobenius norms are below100, the Gram
entries below10000, and target/factor entries below400. The usual
dot-product bound with gamma_2048=2048u/(1-2048u), u=2^-53, gives
the exact reconstruction allowance

    10^-7+gamma_2048*100000+2*10^-7 <3.228e-7<10^-6.

Here the factor product is paid by its squared Frobenius norm. Each
boundary Gram has inner dimension at most4 and Frobenius norm at
most10000, so its product error is at most gamma_4*10000; division
by36 or144 and subtraction add only basic-operation errors. These,
scalar assembly and full residual norm evaluation fit in2e-7. Restoring
the subtracted10^-6 I proves the three stated upper orders; proposed
factorization success or eigenvalues are not used as certificates.

The exact functionals differ from their dyadic centers in operator
norm by less than10^-7 (for the whole four-row local map, and for
each trial row). To check this conversion, the observed full norms
are ||Zhat||_F<23, ||Yhat||_F<11, ||fl(Zhat Yhat)||_F<11,
||bhat_L||_F<40 and ||(bhat_+,bhat_-)||_F<10. A scalar boundary
coefficient row has norm below23. Pay the complete product Zhat Yhat,
all subsequent row products, the at most four local rows, and the
correctly rounded sqrt(2) constants. A deliberately larger bound is

    gamma_2048*(23*11*23+100*23+100)+10^-8
        <1.187e-8<10^-7.

The10^-8 covers scalar conversions, small additions and norm
evaluation, and C999l's ||Z_H-Zhat||<10^-14 propagated against
||Yhat||<y and the finite row norms. The preceding magnitude checks
have ample slack for the norm-evaluation error; even a sequential
sum over a1020-square array has relative squared-norm error below
gamma_2080800<2.32e-10. Thus, including exact neutral conversion,

    ||b_L M_cert^-1/2||<=q_L:=12+10^-7/sqrt(mu),
    ||b_+ M_cert^-1/2||,||b_- M_cert^-1/2||
                           <=q_g:=6+10^-7/sqrt(mu).   (29)

These are matrix orders on all complex x, without an endpoint
reflection or reality restriction.

**Entire local input range.** For n>=K, D has no head-to-tail entry
and C Z_H=0 exactly, so Q_K LZ_H=Q_K SZ_H. In each parity p,
C999l(13) subtracts (nu_m/nu_p)S_np. Its leading part on a head u
is S_n0 sqrt(2)v_e(u) in even output and S_n1 v_o(u) in odd output.
The four output groups (two parities at each endpoint) are orthogonal.
Since |S_np|<=(1/n+b/n^2), with b=C999l Section4's response constant,
their common coefficient-map norm is at most(1+b/K)/sqrt(K-1).
It follows from(29) and the complete C999l remainder that

    ||Q_K diag(L,L)(f_H,h_H) M_cert^-1/2||
       <= (1+b/K)q_L/sqrt(K-1)+s_rem*z/sqrt(mu),       (30)
    s_rem=sqrt(sum_(m=0)^511(4m+16ell/pi^2)^2)
                                      /sqrt(3(K-1)^3).

The response remainder acts diagonally on the two endpoint spaces;
its operator norm is s_rem, with no additional sqrt(2) loss. The
two terms in(30) are respectively <.046875711 and <.029339878.
The full response series is used, not a finite response prefix.

**Both direct-middle translation tails.** Independently enumerate all
prime powers27<q<81; these are exactly C744v's sixteen active shifts.
Six delays delta_q=7ell-log(q) are positive, ten negative, all strictly
between -ell and ell and nonzero. Set beta_q=|delta_q|/ell and
a_q=Lambda(q)/sqrt(q). Apply(19) separately to the two sign groups.
Its diagonal difference is handled by sum n^-2<=1/(K-1); every
remaining sum/difference resonance is enclosed. The certificate saves
all21 positive-group and55 negative-group pairs, including diagonals.
Their minimum distances exceed .05779782 and .01822150, respectively.
The complete infinite sine-square sums satisfy

    V_+ < .000013770563, V_- < .000017335651.           (31)

For a fixed sign, the two orientations use v_+ and v_- of the SAME
g_tilde, in opposite order, with harmless parity signs on outputs.
Equation(29) therefore bounds the paired leading map by
(2/pi)sqrt(2)q_g(sqrt(V_+)+sqrt(V_-)). Opposite sign groups are
combined by the triangle inequality. Use C999l(11)'s full j_rem,
a=sum_q a_q<7.653878168 and C744v(2)'s complete continuous norm
kappa<.000105742. The translation pair consequently obeys

    ||Q_K(T*g_tilde,Tg_tilde) M_cert^-1/2||
       <= (2/pi)sqrt(2)q_g(sqrt(V_+)+sqrt(V_-))
                    +sqrt(2)(a*j_rem+kappa)*z*y/sqrt(mu). (32)

The leading, prime-remainder and continuous terms are respectively
<.042537166, <.066991733 and <.006295262. All prime-frequency cross
products within a sign group are paid in(19); those between groups
and between leading/remainder terms are paid by norm addition. The
continuous part is its entire operator, in both orientations.

**Low corrections, weighting and conclusion.** The remaining step is
the exact low-coordinate term in(9). The audited finite-head bound
||Mhat Zhat||<6.190001, ||PLP-Mhat||<.00024 and the conversion
errors give

    ||P LZ_H|| <6.190001+.00024*z+400*10^-14+10^-7
                  <6.191.

Here the product error is within10^-7; the complete Mhat magnitude
bound400 is the one in Section8's ledger. Bounded T,T* and(29)'s
underlying ||g_tilde||<=z*y||x|| yield

    ||P_low A_LT M_cert^-1/2||
          <=[6.191+sqrt(2)*4.71*z*y]/sqrt(mu)=:q_0.

The small low correction is nevertheless retained: by(6) and(9),
combine(30) and(32) BEFORE squaring, obtaining

    ||D_tail^-1/2 J_K diag(Z_T*,Z_T*) A_LT M_cert^-1/2||
       <= [(30)'s right side+(32)'s right side]/sqrt(d)
                       +sqrt(4/[3d(K-1)^3])*q_0
       < .057921770 < .06.                            (33)

The final low correction is <.000009885514. The80-digit directed
calculation uses the complete expressions, not rounded displayed
summands. It supplies the upper endpoint .05792176975463970703...
and36 passing checks with no failures. Reproduce with

    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/separation-seven/signed-mixed-local-trial-input-568.py

The complete JSON certificate, factor NPZ and log share the basename
`scripts/separation-seven/signed-mixed-local-trial-input-568`. The
input pins agree with audit561 and its source; the complete inherited
check lists are inspected. This proves(27) conditionally on the stated
contracts. The local specialization has not received a separate audit.

The .06 is a component NORM, not an increment of G_mix and not a
quarter-budget decision. A_R in(28), its interaction with A_LT+A_U,
and the finite signed arithmetic are still obligations. The exact
Y-versus-Yhat change is paid once by(23), including its inverse
residual cancellation; it is not charged again separately here.
Complement coercivity, C744q margin, H2, non-neutral coverage and
global actual-Xi positivity remain independent. This is a useful
local REPRODUCTION, without a claim of progress beyond the sources
checked, a negative actual triple or an RH candidate.

### 10. Fixed-J inverse-action input tail — step569

This is a component calculation within the same ready562 target,
approved563. Keep the exact Z_H, fixed dyadic Yhat, M_cert, R and
K=65536. The auxiliary J=32768 was already specified in working566;
it splits inverse OUTPUTS only, and changes neither the input cutoff
nor the predictor, reference or quarter allocation. The standard
representation and inverse-order results in the Hypotheses are reused,
not reproved. The existing scalar, derivative, response-prefix and
automatic-factorization stops do not settle this component. No FFT
accuracy theorem or new external source is used.

Set V=R^-1 rho_tilde, V_0=P_<J V and V_1=P_[J,K) V. The component
of the proxy with inverse output truncated at K is

    A_R^K x=(-T*(V_0+V_1)x,-T(V_0+V_1)x).             (34)

Both V_0 and V_1 are finite coefficient maps. Boundary functionals
below are applied ONLY to V_0, never to the entire inverse vector
or arbitrary weighted inputs. The calculation encloses

    ||D_tail^-1/2 J_K diag(Z_T*,Z_T*) A_R^K M_cert^-1/2||
                                      < .078922337 < .08. (35)

The detailed directed value and all qualifications are recorded in
the certificate identified below. This is an unaudited local
REPRODUCTION, not a quarter-budget decision. Its downstream use still
requires finite signed-map arithmetic and, independently, complementary
coercivity. A loose scalar sum of component norms is not a rejection
of the actual mixed inequality.

**Direct inverse centers and exact errors.** Regenerate all65024
residual rows512:65535 using exactly C999l Section3's direct formulas,
including both T orientations, full response allowances, the moment
penalty and the continuous terms. The complete ordered byte digest
agrees with audited559/561. This checks the whole row array, not a
sample. Its Frobenius norm is <3, and the sum of the squared raw
factor Frobenius norms is <20. On0:511 use the saved head solution
of C999l, whose entire solve residual was enclosed there.

For n>=512 evaluate the real digamma diagonal center hhat_n using
the exact64-step recurrence and log(z+64)-1/[2(z+64)] with an80-digit
Decimal logarithm, exactly C744w Section3's approximation. The
inherited elementary error is <10^-7. Its cited remainder gives

    |h(k_n)-hhat_n|
       <=sqrt(2)/[6(64.25^2+(512*pi/(2ell))^2)]+10^-7 <10^-6.

All hhat_n>6.14. The true diagonal satisfies h(k_n)>=d_n, by C999l,
so on any range starting at b>=512 its reciprocal-center error is
at most 2*10^-6/[d_b(d_b-10^-6)]. Form the saved center
Vhat_n=(2/hhat_n)rhohat_n. The entire scalar multiplication error
fits10^-7 in operator norm: ||rhohat||_F<3, inverse weights<.326,
and only a bounded number of binary operations occur per entry.
No accuracy of the old locator's inverse or FFT multiplication is
assumed. The new center is saved in full as
`scripts/separation-seven/signed-mixed-inverse-centers-569.npy`.

Write mu=.000999, z=1.008, y=1.320001. For a rectangular residual
range of L rows within512:65535, C999l(9)'s same entry/response proof
gives the operator error

    delta(L)=sqrt(2)*sqrt(512L)*(2.1e-7)*z
                +[.000000181+sqrt(512L)*10^-7]*z*y+10^-7.

Indeed restricting rows cannot enlarge the global analytic response
error .000000181; the elementary entry errors have the displayed
rectangular Frobenius bound. The exact-Z and product allowance is
the same10^-7 as in C999l. Define

    eps_H=(delta_P+s_H)/.239999,
    eps(L,d)=2delta(L)/d+6*10^-6/[d(d-10^-6)]+10^-7,
    eps_0=eps(J-512,6.14), eps_1=eps(K-J,d_J).          (36)

Here delta_P is C999l's complete head residual error and s_H its
head-solve numerator error, before division by .239999. The factor6
uses ||rhohat||_F<3. Thus the exact inverse-center errors on the three
orthogonal ranges0:511,512:J-1,J:K-1 are bounded respectively by
eps_H,eps_0,eps_1. No term in rho has been squared separately.

**Full finite factors.** Put a_m=1 for m>0, a_0=1/sqrt(2), and
W_j=diag((m/(J-1))^j) on0<=m<J, j=1,2. The script proposes and
checks all entries of factors for M_cert-Gram/q^2-10^-6 I,
using the following complete dyadic-center maps and q values:

    sum_(m<J) a_m Vhat_m:                      q=5,
    sum_(m<J) (-1)^m a_m Vhat_m:                q=5,
    Vhat_<J:                                  q=.35,
    W_1 Vhat_<J:                              q=.011,
    W_2 Vhat_<J:                              q=.006,
    Vhat_[J,K):                               q=.007.

Gram here means the full map's adjoint times itself. All1020 complex
head directions are covered. The weighted matrices and boundary rows
are computed by binary operations; their conversion to the displayed
exact functions of the dyadic Vhat costs <10^-7 in operator norm.
For the boundary rows a bound is gamma_(2K)*sqrt(J)||Vhat_<J||_F
plus the scalar sqrt(2) error, well below10^-7 since that Frobenius
norm is <1. For W_j the rational weights and their squares have
uniform elementary error below10u; their full Frobenius error is
also below10^-7. These conversion allowances are paid again below
only for conversion to the stated maps, not for the Gram evaluation.

Each normalized row map used for a Gram has Frobenius norm<100.
Blockwise products and accumulation, including scaling by the stated
q, have total operator error at most

    gamma_(2K)*10000+10^-8,
    gamma_t=t*u/(1-t*u), u=2^-53.

This conservative length bounds every Gram accumulation; the10^-8
pays scalar divisions and additions. The factor squared Frobenius
norms are <100000, all target/factor/Gram entries are <400 in absolute
value, and the observed full reconstruction errors are <10^-7.
Consequently the whole reconstruction and Gram error is at most

    10^-7+gamma_2048*100000+2*10^-7
                    +gamma_(2K)*10000+10^-8 <10^-6.    (37)

The2e-7 includes operand assembly, subtraction and norm evaluation.
Observed full squared-norm sums have relative error bounded by their
gamma length, with ample slack at these magnitude thresholds. Restoring
10^-6 I proves the six orders; factorization success alone is not used.

Let eta=10^-7 and alpha=511/(J-1). From(36)-(37), define

    q_b=5+[sqrt(512)eps_H+sqrt(J-512)eps_0+eta]/sqrt(mu),
    q_0=.35+[sqrt(eps_H^2+eps_0^2)+eta]/sqrt(mu),
    q_1=.011+[alpha eps_H+eps_0+eta]/sqrt(mu),
    q_2=.006+[alpha^2 eps_H+eps_0+eta]/sqrt(mu),
    q_B=.007+[eps_1+eta]/sqrt(mu).                     (38)

These bound, respectively, both boundary maps of V_0 M_cert^-1/2,
V_0 M_cert^-1/2, W_1 V_0 M_cert^-1/2,
W_2 V_0 M_cert^-1/2, and V_1 M_cert^-1/2. The boundary row norms
on the first two disjoint ranges are at most sqrt(512),sqrt(J-512).
The W_j norms on the head are alpha^j and on512:J-1 at most1.
The q_0 error uses orthogonality only of those output ranges.

**Complete input tail.** For output n>=K and m<J, C744w's exact
translation formula and C999l(11)'s subtraction give remainder entry

    <=(2/pi)a_m[m^2/n^3+m/n^2]/theta,
    theta=1-(J-1)^2/K^2>0.

For any complex head x, Cauchy--Schwarz over m bounds the two
weighted absolute sums by sqrt(J)(J-1)^2 q_2||M_cert^1/2 x||
and sqrt(J)(J-1)q_1||M_cert^1/2 x||. Summing the n^-6 and n^-4
tails from K onward and using both T orientations therefore bounds
the complete paired prime remainder by

    E_rem=(2/pi)sqrt(2)*a*sqrt(J)/theta *
       [(J-1)^2 q_2/sqrt(5(K-1)^5)
                    +(J-1)q_1/sqrt(3(K-1)^3)],
    a=sum_(all16 shifts) a_delta.

The two leading boundary maps use precisely the positive/negative
sine sums from Section9(31), with no change in K or shift list.
That complete pairwise geometric bound, including all76 within-sign
pairs and both orientations, gives

    E_lead=(2/pi)sqrt(2)*q_b*(sqrt(V_+)+sqrt(V_-)).

The entire continuous paired operator on V_0 costs
E_cont=sqrt(2)*kappa*q_0. The finite band V_1 requires no boundary
trace or smoothness: its complete paired T/T* cost is
E_band=sqrt(2)*4.71*q_B. All four costs are added in norm, not as
independent covariances. Finally the exact neutral low correction
in(9) is bounded using

    ||P_low A_R^K M_cert^-1/2||
                          <=sqrt(2)*4.71*sqrt(q_0^2+q_B^2).

The last square root uses disjoint inverse-output ranges before T
is applied; it does not assert orthogonality of their T images.
Equations(6),(9) now give the complete bound

    E_R=(E_lead+E_rem+E_cont+E_band)/sqrt(d_K)
          +sqrt(4/[3d_K(K-1)^3])*sqrt(2)*4.71*sqrt(q_0^2+q_B^2).
                                                               (39)

All scalar evaluations are directed80-digit intervals. Reproduce with

    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/separation-seven/signed-mixed-inverse-input-569.py

The complete certificate, six factors/Grams/diagonal centers and log
are `scripts/separation-seven/signed-mixed-inverse-input-569.json`,
the same basename with npz, and the same basename with log. The full
inverse centers have the separate npy path above. The first execution
stopped on unsupported interval exponentiation before scalar completion;
its script/log are retained with `first-pass-569`. This software error
establishes no mathematical obstruction.

The first complete run also failed its proposed boundary caps3 and
residual Frobenius cap2. Its full script/json/npz/log are preserved
as `signed-mixed-inverse-input-first-complete-569.*`. The complete
boundary diagnostics, including the saved head inverse, were about
4.53718 and4.53636; working566's smaller inverse-array diagnostics
did not include that head contribution. The residual squared Frobenius
norm was6.93613. The final run uses the caps5 and3 above and verifies
the entire factors rather than accepting these diagnostic values.
This corrects proposed enclosure caps, not the predictor, reference,
cutoffs, input split or quarter allocation. The failed run's displayed
.074643317 scalar is not a certified bound.

The final run has154 checks with no failures. Its six reconstruction
residuals are <2.532e-14, squared factor Frobenius norms <4835, and
the full Gram/factor allowance(37) is <4.783e-7. Equation(39)'s
directed upper endpoint is
.078922336797158767327653785846576527281720095142213073353855791461330818113363374,
below the predeclared component ceiling .1 and also below .08.
This proves(35) under the retained contracts. No independent audit
of this new specialization has yet been performed.

The scalar component ledger can now include A_U, A_LT and A_R^K for
all free inputs n>=K; it must add their norms before squaring, or
retain their joint operator order. This does not certify the finite
mixed columns. Section8's predictor change is paid once for the whole
map, and Section6's output allowance is separate. Neither a diagonal
inverse center nor the old FFT locator is an exact mixed-map certificate.
The full quarter comparison and independent complementary coercivity
remain unresolved, as do the inherited whole-core/c_* and global gaps.

For an explicit comparison with the required threshold, Sections7,9,10
give rounded component bounds .112,.058,.08, so the entire input
tail of B_tilde^(K), normalized as above, has norm <=.25. This adds
norms before squaring and retains every within-column cross product
by the triangle inequality. Let lambda_fin be a CERTIFIED upper bound
for its finite input covariance on512:65535 against M_cert. Disjoint
input columns, followed by Sections6,8, would give

    ||M_cert^-1/2 B D_tail^-1/2||
              <=sqrt(lambda_fin+.25^2)+.163+.008.     (40)

Thus these scalar allowances would suffice if lambda_fin<=.045741,
since .045741+.0625=.329^2. The saved locator's .0829002146552 is
uncertified and exceeds this sufficient value; it is not a rigorous
lower bound and does not reject the quarter test. Equation(40) makes
the limitation explicit: the component estimates alone do not close
the budget, even though each is paid. A tighter joint operator-order
enclosure and finite arithmetic remain obligations; no such enclosure
or new FFT theorem is claimed here.

### 11. Separate conceptual audit — 12 November2026, step570

**Scope and result.** Reuse unchanged SPECIALIZE assessment562,
approved563, and its primary-source proof coverage. This is an audit
of the existing specialization, not a new general theorem or source-level
novelty claim. Sections1-10 are upheld under their analytic response,
whole-core, unreplayed c_*, IEEE754 and Decimal contracts. The complete
quarter comparison is neither proved nor rejected. This audit does not
extend to the locator's FFT arithmetic or supply complementary coercivity.

**Form domain and ordinary adjoint.** The two parity moment columns
are independent and r_n is real and at most2/n^2. Thus each low correction
is an ordinary ell2 functional and a weighted Y_D functional. The
inequality(6) follows from d_n>=d_K and the integral of4t^-4 from
K-1 to infinity. The weights d_n and1+log(2+n) are equivalent on
n>=512: their ratio tends to1 and the finitely many remaining terms
are strictly positive. This proves the claimed continuous parametrization
and its inverse, including recomputation of both low corrections when
truncating. It does not assert that a raw projection is neutral.

Only finite head/predictor vectors are placed in Dom(L). General tail
endpoints enter the closed form on V0, and their forcing is in L2 by
bounded T,T*. The restricted relation's form domain is V0 subset V;
R<=a0 there and Arel^-1=A0^-1P0. Consequently the already cited
Behrndt et al. Corollary3.5 has the required order and nonnegative
hypotheses, as justified in C999k/l. Teschl's cited representation
theorems and C744z's square completion apply on exactly this domain.
No unrestricted inverse is substituted for the restricted inverse.

In(8), the tail coefficient for f is Lf_H-U*h_H-T*g-
T*R^-1rho_H; for h it is Lh_H-Uf_H-Tg-TR^-1rho_H.
This checks the sign and both adjoint orientations directly against
the original energy. The low-mode D terms are retained; the moment
penalty vanishes on the exactly neutral arguments. Hence(4) uses
the ordinary adjoint w_n-r_n w_p, and the inverse weights enter only
in(5). The finite number1020 of head directions and d_n>=d_512>0
make the positive column Gram series trace summable. This supplies
its operator meaning without a boundary trace of arbitrary Y_D data.

**The two errors and the component split.** Output truncation changes
only R^-1rho_H. Its error is exactly the pair in Section4, and the
coefficient inequality(2/h_n)^2<=(2/d_K)(2/h_n) proves(11).
The Section6 factor controls the entire proxy residual covariance;
the exact-predictor residual change is paid before applying(10).
This validates the output bound for the exact B, rather than treating
an omitted inverse output as a positive covariance contribution.

For the predictor, (24)-(25) hold as identities of L2 vectors because
Z and both predictors have finite support. For its K-truncated version,
Q_KZ=0 gives the difference P_<K E DeltaY, so the same norm bound
applies. Thus the legitimate assembly order is
B -> B^(K) -> B_tilde^(K), paying Section6 then Section8 once.
The small predictor allowance must not be duplicated in the three
input components. Those components are exactly A_LT+A_U+A_R^K;
their covariances are not separate nonnegative debts whose squares
can simply be added. Only disjoint input columns permit exact addition
of the finite and infinite input covariances.

**Complete analytic tails.** For a nonresonant angle the finite
geometric numerator has modulus at most2, giving the bound preceding
(18). Abel summation with n^-2 gives total coefficient mass K^-2,
so(18) includes the first term and the infinite limit. In(19) each
diagonal difference is paid by the nonoscillatory sum, each diagonal
sum frequency is retained, and every unordered off-diagonal pair
occurs twice. All beta values lie strictly between0 and1. The sole
zero delay of U is q=2187; it has zero raw head-to-tail output but
remains in the full low-output norm. Adjoint reversal swaps the two
sign groups and their finite boundary functionals. The resulting
sqrt(2) factors cover both endpoint orientations, with no reality or
reflection assumption.

The C999l shift subtraction applies at m=0 with zero remainder.
Its denominators stay positive at the fixed512/K and J/K splits.
For Section9's response, the even base coefficient is sqrt(2)v_e,
the odd one v_o; four disjoint parity/endpoint ranges justify using
the four-row b_L norm. The response and trial remainders are then
added in norm. Their full continuous kernels and both neutral low
corrections are paid. In Section10 all boundary functionals act on
the finite V_0=P_<J R^-1rho_tilde. Weighted Cauchy--Schwarz gives
sqrt(J)(J-1)^j q_j for j=1,2, and integration of n^-4,n^-6
gives exactly the displayed E_rem. V_1 has no boundary evaluation:
its full paired T/T* norm costs sqrt(2)||T||q_B. The final
sqrt(q_0^2+q_B^2) uses disjoint ranges before applying T, and
does not assume that their T images are orthogonal. These arguments
validate(39) on the complete infinite input range.

**Arithmetic and complete evidence.** Reproduce the audit with

    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/separation-seven/signed-mixed-audit-570.py

The full JSON and log have the same basename. The script reads the
original565-569 artifacts without changing them, checks their source,
input and archive pins and complete original check lists, reconstructs
all15 proposed factors against their full targets, and replays all
six inverse-center Grams and both boundary rows from all65536 rows
of the saved inverse-center array. The head0:511 agrees with C999l's
audited solve; it is not omitted. Replayed Grams/rows agree exactly
with569. All factor residuals are below10^-7 and their squared
Frobenius norms below100000. The ordinary factor allowance is below
3.228e-7; the full inverse Gram/factor allowance is below4.783e-7.
Both fit the restored10^-6 margin. These are complete reconstruction
checks with error allowances, not eigenvalue or Cholesky-success tests.

The inverse centers' exact-error argument remains(36). Restricting
rows does not increase the full response error .000000181; the
elementary rectangle errors have the stated sqrt(512L) factors.
The saved head-solve error is a numerator before division by .239999,
as used in(36). The diagonal recurrence and real logarithm are the
C744w Sections3-4 approximation, with its elementary10^-7 allowance;
its analytic error is largest at512 and is less than1.098e-7.
Hence the deliberately larger10^-6 diagonal allowance is valid.
The reciprocal difference is at most2*10^-6/[d(d-10^-6)]. Multiplying
by the complete residual Frobenius bound3 gives the factor6 in(36).
Full residual rows are not regenerated again in this audit: their
complete matching559/561/569 byte digest and pinned direct-formula
source are inherited explicitly. The independent audit replays the
inverse-center Grams, not a new direct residual computation.

For a Gram of a finite map X, the inherited dot-product error is
bounded in Frobenius norm by gamma times ||X||_F^2. Blocking and
accumulation fit gamma_(2K), and scalar scaling/assembly fits the
separate allowances. Boundary-row conversion uses finite coefficient
norms, the exact-Z error and the stated gamma bound; the weighted
W_j maps have weights at most1. Applying these errors before dividing
by sqrt(mu) gives precisely(38). This pays the full matrices and
their conversion, rather than just selected coordinates.

At110 Decimal digits the audit independently enumerates both complete
prime-power sets and encloses all29525 within-sign pairs (29449 for
U,76 for T). Every saved resonance lower bound and oscillatory upper
bound is checked against the new enclosure. The higher-precision
scalar evaluation gives

    output error              < .162724526 < .163,
    remote-U input            < .111319476 < .112,
    predictor error           < .007245510 < .008,
    local/direct-trial input  < .057921770 < .058,
    inverse-action input      < .078922337 < .08.

All59141 audit checks pass. This count includes the exhaustive
pairwise checks; it is not a count of independent mathematical results.
The bounds remain conditional on the inherited execution and analytic
contracts. No source certificate for c_* or FFT library was replayed.

**Decision.** Equation(40) is valid with its rounded allowances and
requires a certified lambda_fin<=.045741. The saved .0829002146552
locator has no certified upper or lower status, so it cannot prove
failure of that sufficient condition or of the actual quarter budget.
The audit establishes the existing component ledger as a usable local
input, without improving its numerical threshold. Joint operator-order
tail estimates and the finite signed arithmetic remain unresolved;
further scalar-component additions alone cannot certify assembly.
Complement coercivity, C744q, H2/non-neutral coverage and actual-Xi
assembly remain independent gaps. No RH candidate is asserted.

### 12. Joint directional input majorant — step571

**Scope and conclusion.** This is one REPRODUCTION proof attempt under
unchanged assessment562, separately approved563. Reuse the audited
Sections1-11 and their source and failure comparisons. The standard
representation/inverse-order results cited in the Hypotheses remain
imports; this section supplies only the missing local quantitative
combination. No FFT accuracy theorem, new source, complementary sign
or new scalar floor is assumed. The exact predictor, reference,
M_cert, K=65536, J=32768 and quarter allocation are unchanged.

For the same output-truncated proxy, the result is

    ||D_tail^-1/2 J_K (B_tilde^(K))* M_cert^-1/2||
       < .150650426 < .151.                            (41)

It retains both endpoint orientations and all the input modes n>=K.
It is qualified by the inherited analytic response, whole-core,
unreplayed c_*, IEEE754 and directed Decimal contracts. This new
specialization has not received a separate critical audit. It improves
the local allowance without claiming mathematical novelty beyond the
sources checked, a complementary sign or an RH candidate.

**Pointwise majorant before covariance.** Keep Section10's
V_0=P_<J R^-1 rho_tilde and V_1=P_[J,K) R^-1 rho_tilde, and put
g=g_tilde=Z_H Yhat x. Write d=10.9963070613268<d_K, j=j_rem,
s=s_rem, b=b_response, a_7=sum of all sixteen separation7 weights,
a_14=sum of all334 separation14 weights. The full continuous norms
are kappa_7 and kappa_14 from Sections7/9. Let V_{7,+},V_{7,-}
and V_{14,+},V_{14,-} denote the certified upper endpoints for the
four complete sine-square sums in(20),(31), not truncated sums.
Set theta=1-(J-1)^2/K^2 and W_j=diag((m/(J-1))^j) on m<J.

The following ten maps C_i act on the SAME1020-dimensional complex
head space. Finite boundary functionals have exactly the constant-mode
normalization in Sections7/9/10. Their coefficients c_i are first given
as the positive analytic expressions below; the implemented coefficients
are upward dyadic enclosures of them.

| i | C_i x | c_i |
| --- | --- | --- |
| L | b_L x=(sqrt(2)v_e(f_H),v_o(f_H),sqrt(2)v_e(h_H),v_o(h_H)) | (1+b/K)/sqrt((K-1)d) |
| U+ | (v_-(f_H),v_+(h_H)) | (2/pi)sqrt(V_{14,+}/d) |
| U- | (v_+(f_H),v_-(h_H)) | (2/pi)sqrt(V_{14,-}/d) |
| E | (f_H,h_H) | (s+a_14 j+kappa_14)/sqrt(d) |
| Q | (v_+(g+V_0 x),v_-(g+V_0 x)) | (2/pi)(sqrt(V_{7,+})+sqrt(V_{7,-}))/sqrt(d) |
| g | g | sqrt(2)(a_7 j+kappa_7)/sqrt(d) |
| 1 | W_1 V_0 x | (2/pi)sqrt(2)a_7 sqrt(J)(J-1)/(theta sqrt(3(K-1)^3 d)) |
| 2 | W_2 V_0 x | (2/pi)sqrt(2)a_7 sqrt(J)(J-1)^2/(theta sqrt(5(K-1)^5 d)) |
| 0 | V_0 x | sqrt(2)kappa_7/sqrt(d) |
| B | V_1 x | sqrt(2)4.71/sqrt(d) |

In entries Q,g the symbol g denotes the linear function of x defined
above. The table therefore defines linear maps, not additional input
coordinates. Only finite vectors enter any boundary functional.

Here is a direct justification that the table covers the entire raw
input tail. The local response leading term is(30). For each sign
of U, the leading outputs at the two independent endpoints have
coefficient vector C_{U+}x or C_{U-}x; their squared sequence sums
are bounded by(20). Reversing the delay for U* swaps the boundary
functionals as displayed. The local response remainder and the
off-diagonal remote remainder have bounds s and a_14 j on the
endpoint pair, respectively; the remote continuous operator adds
kappa_14. Their sum is paid in c_E, without claiming orthogonality.
The identity remote shift has no raw head-to-tail output and remains
included in the low-coordinate bound below.

For the shared middle terms, use the signed identity

    (-T*g-T*V_0 x, -Tg-TV_0 x)
              =(-T*(g+V_0 x),-T(g+V_0 x)).

The leading expansion of each translation depends only on v_+,v_-
of its finite argument, even though g has support<N and V_0 x has
support<J. For either delay sign, the pair of orientations has the
same norm of those two boundary values, in the opposite order.
Apply(31) and add the two sign groups in norm. This is exactly c_Q
times ||C_Q x||; adding the two boundary rows BEFORE forming their
Gram retains the trial/inverse cross product. Pay the remainders
of g and V_0 separately: the former is c_g||g|| using j for N=512;
the latter uses the two weighted Cauchy--Schwarz bounds in Section10
and gives c_1||W_1 V_0 x||+c_2||W_2 V_0 x||. Their continuous
operators cost the kappa_7 parts of c_g and c_0. Finally, V_1 is
handled by the full paired T/T* bound sqrt(2)4.71, without a boundary
trace. These are precisely all the terms A_LT+A_U+A_R^K in(28),(34).

Replacing each d_n by d for n>=K enlarges these bounds. The remaining
ordinary-adjoint correction -r_n w_p is paid by adding the three
already audited low corrections from(22),(33),(39). Their total is

    e_low < .000029677261.

It is a norm allowance in the M_cert geometry. Consequently, for
every complex head x,

    ||D_tail^-1/2 J_K (B_tilde^(K))* x||
      <= sum_i c_i ||C_i x|| + e_low ||M_cert^1/2 x||. (42)

This is a norm inequality before squaring. The same input coordinates
occur in its different terms, and all their cross products are paid
by the triangle inequality; none is declared an independent covariance.

**One common matrix instead of ten scalar maxima.** Let Chat_i be
the dyadic-center maps retained in566/568/569, with the following
choices. Use the four local rows, the two indicated pairs of remote
rows, diag(Zhat,Zhat), and the raw trial product fl(Zhat Yhat).
For Q, add the two568 trial rows to the two569 inverse boundary rows
by binary arithmetic. For indices1,2,0,B use the finite weighted
inverse-center maps evaluated by569; their complete normalized Grams
were independently replayed in570. Their row counts are J or K-J,
not a displayed prefix. No inverse head row is omitted.

Use, in table order, the fixed positive Cauchy weights

    a_i=(12,17,17,32,16,43,.011,.006,.35,.007).

These are merely weights in Cauchy--Schwarz, not asserted upper
bounds on the exact maps, and were not optimized. Let c_i now be
the exact upward dyadic coefficients saved in the certificate and
S=sum_i c_i a_i. For every x,

    (sum_i c_i ||Chat_i x||)^2
        <= S sum_i (c_i/a_i)||Chat_i x||^2.            (43)

Let q_i=1 for the first six maps and q_i=.011,.006,.35,.007 for
the last four, in order. For each i choose the saved exact dyadic
t_i>=S c_i q_i^2/a_i, with the inequality checked by80-digit
directed arithmetic. Define the exact Hermitian matrix

    Q=sum_i t_i (Chat_i/q_i)*(Chat_i/q_i).             (44)

The star in each product is the ordinary conjugate transpose. Since
every individual Gram is nonnegative, (43) is bounded by x*Qx.
The finite computer matrices are real, but this Hermitian order
covers all complex x. Thus (43)-(44) pay all the interactions among
the ten terms, including those not retained as signed row sums.

**Full arithmetic certificate.** The code is

    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/separation-seven/signed-mixed-joint-input-571.py

Its JSON, NPZ and log share the basename
`scripts/separation-seven/signed-mixed-joint-input-571`. The complete
coefficient enclosures, exact dyadic c_i,t_i, scales, weights, map
errors, comparison matrix, ten full Grams and proposed factor are
saved, with source/input/archive hashes. All570 input hashes and
complete check lists are checked; the complete569 inverse-center
artifact hash is checked as well. The direct residual computation
and inverse Gram replay remain inherited from559/561/569/570,
not claimed to have been rerun in571.

For each newly formed Gram, its row-map Frobenius norm is <100,
its inner dimension is <=1024, and the conservative Gram error is

    e_new=gamma_2048*10000+10^-8 <1.228e-8,
    gamma_t=t*2^-53/(1-t*2^-53).

For the four inherited normalized inverse Grams use the already
audited bound e_old=gamma_(2K)*10000+10^-8<1.556e-7. Each full
Gram has Frobenius norm<10000. After its exact dyadic weight t_i,
the total Gram error sum t_i e_i is <6.834e-10. The sum of the
weighted Gram Frobenius norms is <10000 and ||M_cert||_F<400.
Multiplication by the weights, ten additions, symmetrization,
conversion of .104^2 and the norm evaluations fit the deliberately
larger2e-7 assembly allowance. For example gamma_64 times the
weighted10000 bound plus gamma_64*400 is <7.4e-11; even sequential
1020-square squared-norm evaluation has relative error below
gamma_2080800<2.32e-10, with ample slack in the checked magnitudes.

The numerical generalized eigenvalue .01022474088014413 only
proposed the rounded norm ceiling q=.104. The certificate then
reconstructs EVERY entry of a factor for

    .104^2 M_cert-Qhat-10^-6 I.

Its observed Frobenius residual is <2.113e-16, its squared factor
Frobenius norm is <52.199 and all factor/target entries have modulus
<.255. Using the conservative bounds10^-7 for the full residual and
100000 for squared factor norm, the exact total error is at most

    10^-7+gamma_2048*100000+2*10^-7+sum_i t_i e_i
       <3.235e-7<10^-6.

Restoring the subtracted10^-6 I proves Q<=.104^2 M_cert. The
observed eigenvalue and factorization success alone prove no order.
Together with(43), the reconstructed order proves the simultaneous
dyadic-center norm bound .104.

**Exact-map conversion and low corrections.** Write eta=10^-7,
alpha=511/(J-1), and retain the exact inverse-center error bounds
eps_H,eps_0,eps_1 of(36). Set

    eps_b=sqrt(512)eps_H+sqrt(J-512)eps_0+eta.

In the same table order, valid bounds for ||C_i-Chat_i|| are

    eta, sqrt(2)eta, sqrt(2)eta, 10^-14,
    sqrt(2)(eps_b+eta)+eta, eta,
    alpha eps_H+eps_0+eta,
    alpha^2 eps_H+eps_0+eta,
    sqrt(eps_H^2+eps_0^2)+eta, eps_1+eta.              (45)

The first three use the complete boundary conversion of566/568.
The endpoint pair has the same exact-Z operator error as one copy,
because it is a block diagonal map. The raw trial product costs less
than gamma_512*23*11+10^-14*1.320001 plus scalar/norm allowances,
within eta. The combined boundary map uses eps_b for each inverse
row, eta for each trial row, and another eta for the entire dyadic
two-row addition; the operand Frobenius norms are <100, so its actual
rounding error is much smaller. This gives the fifth term of(45).
The last four terms are precisely the finite inverse map conversions
from(36)-(38), with the weights at most alpha^j on the head and1
on the other low-output rows. Orthogonality is used only for the
two raw ranges in the unweighted V_0 error, before T is applied.

Let delta_i denote(45). M_cert>=mu I, mu=.000999, gives

    sum_i c_i ||C_i x||
      <= (.104+sum_i c_i delta_i/sqrt(mu))||M_cert^1/2 x||.

All coefficients and errors are evaluated by80-digit directed
intervals, giving

    sum_i c_i delta_i/sqrt(mu) < .046620749,
    .104+sum_i c_i delta_i/sqrt(mu)+e_low
      <= .15065042546545599810750329764399308920182739053570490694560354986276936244924068.

The last number is the full saved upper endpoint, not the sum of
rounded displayed components. This proves(41) from(42). All69 checks
pass. Initial software starts failed on an unavailable SciPy import
and a mismatched566 JSON field name; their logs are retained as
`signed-mixed-joint-input-import-failure-571.log` and
`signed-mixed-joint-input-schema-failure-571.log`. They produced no
mathematical bound. The successful code uses NumPy for proposals;
the exact-error proof rests on the complete reconstruction above.

**Budget consequence and remaining gap.** If lambda_fin is a
CERTIFIED upper bound for the finite input covariance of the same
B_tilde^(K) on512:65535 relative to M_cert, disjoint input columns
and the already audited output/predictor bounds give

    ||M_cert^-1/2 B D_tail^-1/2||
         <=sqrt(lambda_fin+.151^2)+.163+.008.          (46)

Thus lambda_fin<=.085440 suffices: .085440+.022801=.329^2.
This improves(40)'s sufficient threshold .045741. The old
.0829002146552 locator is numerically below the new threshold,
but has neither certified upper nor lower status. No finite
entry/basis/head-solve/FFT error is thereby paid, and(46) is not
a quarter pass. The independent complementary lower comparison,
C744q margin, H2 slack/existence, non-neutral coverage and global
actual-Xi positivity remain unresolved. This section is a useful
local specialization of the assessed method, not a complete solution.

### 13. Complete finite dyadic-center certificate — step572

**Scope.** This calculation remains within ready assessment562,
approved563, and is REPRODUCTION using the inherited finite Gram and
factor verification method. The source/duplicate/failure comparison is
unchanged. No additional external theorem or FFT accuracy contract is
used. All actual operators, the exact predictor/reference, K=65536,
J=32768 and the quarter allocation are unchanged. The earlier output,
predictor and joint input allowances retain their qualifications;
Section12 is still unaudited. This section proves a property of a
specific dyadic proposal, not its accuracy as an operator evaluation.

Let W_hat_(a,n) be the EXACT dyadic row of
`scripts/separation-seven/signed-mixed-columns-565.npy`, for a=f,h.
Its full file digest is pinned in the certificate below. Define the
finite map A_c:C^1020->C^(2*65024), with ordinary Euclidean range norm,
by

    (A_c x)_(a,n)=(W_hat_(a,n)-r_n W_hat_(a,p))x/sqrt(d_n),
    512<=n<65536, p=n mod2.                           (47)

Here r_n,d_n are the EXACT numbers in(1), not the locator's floating
values. Every saved combined row is retained in(47). The proved result is

    A_c* A_c <= .083 M_cert.                          (48)

The binary rows in(47) define the center, irrespective of the accuracy
of the FFT which proposed them. In particular, proving(48) does not
certify any entry of B_tilde^(K), or any inverse solve or FFT operation.
The result holds for all complex head vectors because the real
symmetric matrix order extends to Hermitian quadratic forms.

**Coordinates and full Gram.** The script recomputes ell and pi with
the inherited directed80-digit logarithm and Machin arctangent
enclosures. For EVERY one of65024 indices it encloses r_n and d_n,
checks d_n>6.14, and stores dyadic rhat_n and an upward dyadic weight
t_n satisfying

    |rhat_n-r_n|<10^-20, 0<rhat_n<10^-5,
    1/sqrt(d_n)<=t_n<1/2.

The largest actual ratio-conversion error is <3.630e-22. The NPZ
contains all rhat_n,t_n and outward binary endpoints for the complete
d_n,r_n tables; the source rechecks the directed interval inequalities.
No library logarithm, sine or eigenvalue accuracy is presumed.

Let A_u have rows t_n(W_hat_(a,n)-r_n W_hat_(a,p)). Rowwise weighting
gives A_c*A_c<=A_u*A_u. Form the dyadic numerical rows

    Ahat_(a,n)=fl(t_n fl(W_hat_(a,n)-rhat_n W_hat_(a,p))).

The entire raw finite rows together with both low rows have squared
Frobenius norm <15.732; the computed weighted rows have squared norm
<2.243. Their full block magnitude ledger has ample slack to justify
the exact bounds1000 and10, respectively, after norm-evaluation error.
All entries are checked finite. The inherited negligible-underflow
qualification is retained.

With u=2^-53 and gamma_j=ju/(1-ju), the complete row error is bounded by

    ||A_u-Ahat||_F <=
      10^-20 sqrt(65024)*1000/2
      +gamma_8(1000+sqrt(65024)*10^-5*1000)/2+10^-12
      <1.447e-12<10^-9.                               (49)

The first term pays every exact-ratio conversion; the second pays
the subtraction and multiplications of all rows by their Frobenius
majorant. The last covers negligible underflow and conservative scalar
accounting. The low rows are repeated according to parity, so their
total Frobenius contribution is bounded by sqrt(65024) times their
combined norm; no orthogonality of these corrections is assumed.

Accumulate every512-row Gram in both orientations and then symmetrize
the result Ghat. There are254 Gram blocks. The dot-product bound and
the exact weighted-row norm <10 give total error at most

    gamma_1024*100+gamma_512*100+10^-10
        <1.171e-10<10^-8.

Only different input coordinates are added as Grams. Each saved signed
row is combined with its neutral low correction before taking its
outer product. Thus no within-column cross product is dropped. From
(49) and ||Ahat||_F<10, a valid total center-Gram error is

    ||A_u*A_u-Ghat|| <=20*10^-9+10^-18+10^-8
                      =3.0000000001e-8.               (50)

**Full factor verification.** Propose a factor for

    .083 M_cert-Ghat-10^-6 I.

Reconstruct EVERY entry of its1020 by1020 product. The observed
Frobenius residual is <1.688e-15, factor squared Frobenius norm
<399.242, and maximum modulus among comparison/Gram/target/factor
entries is <6.010. Conservative bounds10^-7,100000,400 therefore
apply with slack, as in the audited C999l arithmetic ledger. The
exact decimal .083, the operand assembly, residual subtraction and
norm evaluation are included in2e-7. Combining this with product
rounding and(50) gives total error

    10^-7+gamma_2048*100000+2*10^-7+3.0000000001e-8
        <3.528e-7<10^-6.

Restoring the subtracted10^-6 I proves A_u*A_u<=.083 M_cert,
and hence(48). Factorization success or a numerical eigenvalue alone
would not prove this order.

Reproduce from the active notebook with

    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/separation-seven/signed-mixed-finite-center-572.py

The full JSON certificate, NPZ tables/Gram/factor and log have basename
`scripts/separation-seven/signed-mixed-finite-center-572`. All269 checks
pass. The source checks the complete inherited561 check list and the
audited head-archive/interval-source pins. It reads every required raw
row and records each block's magnitudes and the combined weighted-row
digest. It does not replay the FFT or claim to audit Section12.

**Exact limitation and useful threshold.** Let A_exact be the finite
512:65535 portion of D_tail^-1/2(B_tilde^(K))* with BOTH orientations,
and define the still-unproved error

    eta=||(A_exact-A_c)M_cert^-1/2||.

Equation(48) gives lambda_fin<=(sqrt(.083)+eta)^2. Thus(46) would
close the fixed quarter budget if

    eta<=sqrt(.085440)-sqrt(.083),
    sqrt(.085440)-sqrt(.083)>
       .0042040086853630922643671111795828870182577197845. (51)

In particular the exact threshold .004204 is sufficient. No estimate
eta<=.004204 is established. It must cover the complete finite entry,
neutral-basis, head-inverse, diagonal-inverse and FFT-to-exact-map
differences, not merely the Gram rounding already paid here. None of
those unknown errors can be inferred from the closeness of two floating
calculations. The inherited input/output/predictor allowances concern
the exact proxy and remain separate from eta.

A preliminary head-error sensitivity probe is preserved as
`scripts/separation-seven/signed-mixed-head-error-locator-572.py`
and its JSON/NPZ/log. It used the old locator direction, formed the
complete finite gradient for a rank-one head-inverse perturbation of
size .00196, and obtained the UNCERTIFIED ratio .08343418022<.085440.
It supplies neither a robust-enclosure obstruction nor a bound on the
actual error; no direction or parameter search followed. The probe
is not an input to(48). Its unsuccessful discrimination is retained.

This is local finite-certificate progress, with no novelty claim beyond
the sources checked. The actual finite covariance, quarter inequality,
complementary coercivity and all global RH gaps remain unresolved.

### 14. Complete head-inverse error by a verified defect — step573

The target, K=65536, J=32768, exact Galerkin predictor, reference R,
comparison M_cert and quarter allocation are unchanged. Reuse approved
assessment562/563. This is a direct-entry/inverse-solve specialization
within that test, classified REPRODUCTION. No FFT theorem is used or
proved. The scalar/derivative/prefix stops and the inconclusive572
sensitivity probe do not decide this error; the probe is not repeated.

Let P project onto raw modes0:511, let Xhat be the EXACT dyadic matrix
`head_solution` in the unchanged audited559 archive, and retain the
exact proxy g_tilde=Z_H Yhat from Section8. Define

    rho_tilde,P=P[T Z_H,T* Z_H]-PLP Z_H Yhat,
    E=rho_tilde,P-H Xhat, Delta=H^-1 E.                  (52)

Here H is the SAME exact dyadic/rational reference of C999k(4),
not a new approximation to PLP. Thus Delta is exactly the difference
between the proxy's true inverse head and Xhat. Replace just that head
by Xhat in B_tilde^(K), leaving the exact remaining finite inverse
outputs and all other operators unchanged, and call the result B_h.
The claimed partial payment, on all free input modes n>=512, is

    ||Delta M_cert^-1/2|| < .000578728,
    ||M_cert^-1/2(B_tilde^(K)-B_h)D_tail^-1/2||
         < .001555698867 < .001556.                    (53)

It is not an accuracy assertion about the OTHER entries of locator565.

**Complete entry enclosures.** The script and its JSON/NPZ/log have the
basename `scripts/separation-seven/signed-mixed-head-defect-573`.
It checks the four original hashes against audit561 and that audit's
entire check list. It then encloses every entry of PLP, PTP and H;
there are262144 entries per matrix, with complete lower/upper arrays
saved in the NPZ. It retains all sixteen prime powers, both endpoint
orientations, the moment penalty, the full response allowances and the
continuous T tail. No sampled-entry comparison is an input.

The response identities are exactly C744w(11)-(13). The standard
analytic input is the digamma recurrence and sector remainder from
[DLMF5.11.2](https://dlmf.nist.gov/5.11.E2) and
[5.11(ii)](https://dlmf.nist.gov/5.11#ii), in the same specialization
already justified in C744w Section3 and L744(8). At z=1/4+ik/2 use
the exact4096-step recurrence, and approximate only psi(z+4096) by
log(z+4096)-1/[2(z+4096)]. Since Re(z+4096)>0, the identical remainder
is at most sqrt(2)/[6(4096.25^2+k^2/4)]. Only evaluation accuracy
changes; no source theorem, operator, predictor or cutoff K changes.
The scalar imaginary part uses the100-term arctan series at
|k/(2*4096.25)|<.36, whose omitted magnitude is below
.36^201/201<10^-88. Its real logarithm is enclosed by80-digit Decimal
at both endpoints. Both real and imaginary parts include the FULL
sector remainder. Set b(0)=0 exactly.

For unequal modes use the enclosed divided difference (11). For equal
modes sum all65536 positive diagonal terms and add1/(2c_65536), with
the exact C744w diagonal remainder c_J^-2+
2k^2[1/(6c_J^3)+c_J^-4]. The exponential response uses j=0,...,63
and a10^-30 per-entry remainder after normalization. The cross
continuous response uses j=1,...,7 and its full operator tail<10^-24,
which also bounds each missing head entry. These are the previously
covered complete-series remainders, not finite-prefix substitutions.

For every prime shift, evaluate C744w's signed antiderivative, including
its diagonal and constant-mode cases. The sine/cosine argument is
reduced by an explicitly chosen integer multiple of pi/2; the entire
reduced interval has absolute value<.786. The degree21/20 Taylor
polynomials have remainder<10^-21 there. Pi is enclosed by the same
Machin arctan formula used in572. Ell, prime weights/delays, the moment
constants and square roots use outward80-digit Decimal. No library
sine, cosine, logarithm or digamma accuracy is presumed.

Each array basic operation is enclosed by rounding its endpoint
operations outward to the adjacent binary64 numbers. This covers exact
zeros/underflow as well as normal operands; no overflow occurs. Every
division checks that its whole denominator excludes zero. The response
diagonal's block sums are positive; for a block of length r, divide its
rounded lower sum by1+gamma_(r+2) and upper sum by1-gamma_(r+2), rounding
outward again. Ordinary gamma bounds then cover the complete summation.
All interval orders and finite endpoints are checked. The full radius
Frobenius norms use upward squares, the corresponding positive-sum
bound and outward correctly rounded square root. Thus the dyadic
centers Mhat_573, That_573, Hhat_573 satisfy, in operator norm,

    ||PLP-Mhat_573|| <= e_M < 4.254655652e-7,
    ||PTP-That_573|| <= e_T < 8.441073820e-11,
    ||H-Hhat_573||   <= e_H < 1.200051568e-13.          (54)

These are bounds for the actual operators, including source remainders.
H is enclosed directly from its exact rational formula in the two
original dyadic matrices; it is not replaced by Mhat_573.

**Complete defect and correction.** Let Zhat,Yhat be the unchanged
saved matrices from559, and form the dyadic center

    Ehat=fl([That_573 Zhat,That_573^t Zhat]
                    -Mhat_573 fl(Zhat Yhat)-Hhat_573 Xhat).

C999l's audit gives ||Z_H-Zhat||<=10^-14, ||Z_H||<1.008,
||Yhat||<1.320001 and M_cert>=mu I, mu=.000999. Use Frobenius
norms of the complete stored matrices, not selected columns. With
u=2^-53 and gamma_r=ru/(1-ru), the complete product/addition error is
bounded by

    e_ar=gamma_4096 [sqrt(2)||That_573||_F||Zhat||_F
          +||Mhat_573||_F||Zhat||_F||Yhat||_F
          +||Hhat_573||_F||Xhat||_F+1]
        <3.096258465e-8.

This includes formation of the raw predictor and every subsequent
product; their maximum inner dimension is512 and gamma_4096 dominates
the combined paths. The exact-basis error is at most

    e_Z=[sqrt(2)*4.71+(||Mhat_573||_F+e_M)*1.320001]*10^-14.

Consequently the complete source/assembly error satisfies

    ||E-Ehat|| <= e_E
      =sqrt(2)e_T*1.008+e_M*1.008*1.320001
                         +e_H||Xhat||_F+e_Z+e_ar
      <5.971950794e-7.                               (55)

All terms in a residual column remain combined before any Gram is
formed. The complete observed ||Ehat||_F is <4.437864e-5.

Propose Chat by solving Hhat_573 Chat=Ehat, then verify every entry
of its residual. No solver accuracy assumption is made. With the
inherited EXACT H>=.239999 I, the full residual proof gives

    ||H^-1 Ehat-Chat|| <= e_C
      =[||fl(Ehat-Hhat_573 Chat)||_F+e_H||Chat||_F
        +gamma_2048(||Hhat_573||_F||Chat||_F+||Ehat||_F+1)]/.239999
      <9.590359057e-13.                              (56)

The observed residual norm is <5.652e-20; its smallness alone is not
used without the explicit product error in(56).

For q=.0005 form a proposed full factor of
M_cert-(Chat/q)^t(Chat/q)-10^-6 I. Its reconstruction residual is
<2.402e-14, squared factor Frobenius norm<4838, largest matrix entry
<6.01 and ||Chat/q||_F<.078. The exact total reconstruction error,
including Gram/scaling/assembly errors, is at most

    10^-7+gamma_2048*100000+2*10^-7+gamma_2048*100
        <3.228e-7<10^-6.

The10^-6 restored margin therefore proves
Chat^t Chat<=q^2 M_cert. This is a full matrix certificate, not a
Cholesky-success or eigenvalue test. Real matrix positivity also gives
the stated Hermitian bound for arbitrary complex endpoint coordinates.
Equations(55)-(56) and the finite inverse bound now give

    ||Delta M_cert^-1/2||
      <=q+(e_E/.239999+e_C)/sqrt(mu)
      <.000578727093.                                (57)

Here the elementary inequality ||H^-1||<=1/.239999 is the previously
verified finite-reference input; no new infinite inverse theorem is
proved or assumed.

Finally, (4) shows that replacing only this inverse head changes its
two W components by -T*P Delta and -TP Delta. Equations(7),(10), with
zeta^2<=1/6.14+4/(3*6.14*511^3), therefore bound the normalized change
by zeta sqrt(2)*4.71 times(57). The80-digit directed evaluation gives
<.001555698867, proving(53) for the whole free tail, and hence also
for the finite input range512:65535. No orthogonality of those two
endpoint contributions or of error components was assumed.

**Evidence, failed proposal and remaining obligations.** Reproduce by

    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/separation-seven/signed-mixed-head-defect-573.py

All12 final checks pass. The complete enclosures, defect, correction,
solve residual, Gram, comparison and factor are saved in the NPZ;
the JSON records their hash, source pins, full error intervals and
failures. Full relevant evidence was inspected, not a preview.

The earlier attempt to bound Ehat directly by .0001 M_cert^1/2 did
not produce a Cholesky factor. Its script/arrays/JSON/log are preserved
with `signed-mixed-head-defect-floor-failure-573`. Its printed candidate
upper is NOT certified because that factor check failed. Failure of
this proposal proves neither the opposite inequality nor a quarter
obstruction. The successful correction uses the same H and Xhat;
only the proof of their error changes. A tiny outward-rounding omission
in that first run's diagonal tail center was also corrected before the
successful run; no conclusion uses the failed run.

For the finite map in(51), define eta_rem to be the normalized distance
from B_h's finite portion to the exact saved dyadic center. Then
eta<=.001556+eta_rem. Thus eta_rem<=.002648 would suffice for the
existing threshold .004204. This is an UNPAID continuation threshold,
not an estimate: it still includes finite direct entries/basis errors,
complementary inverse entries/diagonal errors and the FFT-to-operator
connection. The exact-predictor/output/input allowances remain separate
and are not improved here. Section12/13 and this section await separate
audits. Complementary coercivity, whole-core/c_*, C744q, H2 existence,
non-neutral coverage and global actual-Xi positivity remain open.
This is local partial error payment, not a novel source-level theorem,
a quarter pass/rejection or an RH candidate.

### 15. Complete complementary inverse-output accuracy — step574

**Scope and exact comparison.** Reuse ready562/approved563 and the
unchanged source/failure comparison. This is REPRODUCTION of the covered
entry and error-bound method; no new external theorem or FFT accuracy
premise is used. Keep the exact proxy g_tilde=Z_H Yhat, K=65536,
J=32768, R, M_cert, both endpoint orientations and the quarter allocation.
Let Q_c=P_[512,K) act on raw inverse outputs. Write

    V=R^-1[T Z_H,T* Z_H]-R^-1 L Z_H Yhat,
    Vhat_c=Q_c times the exact saved dyadic array
            scripts/separation-seven/signed-mixed-inverse-output-565.npy.

The array has zero head; the head inverse Xhat remains separately in
B_h from Section14. Replace Q_c V by Vhat_c in B_h, leaving every
other term exact, and call this map B_hc. The result proved here is

    ||Q_c V-Vhat_c|| <1.494931e-8,
    ||M_cert^-1/2(B_h-B_hc)D_tail^-1/2||
         <.000001271423<.000002.                      (58)

The norm in the first line is an operator norm from C^1020 into the
raw output space. The second bound holds on ALL free tail inputs
n>=512, hence also on the finite input range in(51). Full U cancels
in this difference; it is not omitted from either mixed map.

**Complete scalar and rectangular enclosures.** The script, JSON,
NPZ and log have basename
`scripts/separation-seven/signed-mixed-complement-inverse-574`.
The entire dyadic inverse-center difference array is separately saved as
`scripts/separation-seven/signed-mixed-complement-inverse-difference-574.npy`.
The script checks the entire inherited audit561 checklist and the
original head/entry-source hashes. No input array is overwritten.

Enclose pi by the existing80-term Machin formula and ell, 3^(1/4),
prime constants and normalizations by directed80-digit Decimal. Use
Section14's outward binary64 array operations. Each division checks
that its interval denominator excludes zero, and square roots are
rounded outward. Positive squared-norm sums use the gamma bound with
two extra rounding operations, followed by an outward square root.
All interval endpoints and orders are checked.

For EVERY mode0<=n<K, evaluate psi(z), z=1/4+ik_n/2, by the exact
4096-step recurrence. The imported remainder is exactly the same
[DLMF5.11.2](https://dlmf.nist.gov/5.11.E2) and
[5.11(ii)](https://dlmf.nist.gov/5.11#ii) specialization proved in
C744w(12) and its Section7 audit: Re(z+4096)>0, |arg(z+4096)|<pi/2,
and therefore

    |psi(z+4096)-log(z+4096)+1/[2(z+4096)]|
       <=sqrt(2)/[6(4096.25^2+k_n^2/4)].              (59)

This changes only the recurrence length used to evaluate the SAME
operator. Both real and imaginary enclosures include the entire(59).
The real logarithm uses Decimal at both interval endpoints. For the
imaginary logarithm put t=(k_n/2)/4096.25 and apply
t -> t/(1+sqrt(1+t^2)) five times. The resulting interval has absolute
value<.05. Twelve alternating arctan terms, multiplied by32, have
remainder at most32*.05^25/25<4e-33. Thus no numerical arctan oracle
or unbounded-argument Taylor series is used. Set b(0)=0 exactly.
The complete lower diagonal enclosure satisfies h(k_n)>6.14 for n>=512.

For each of127 consecutive512-row blocks I in[512,K), enclose all
entries of L_I=Q_I LP, T_I=Q_I TP and S_I=Q_I T*P, where P=P_<512.
There is no diagonal D entry in this disjoint rectangle. Use C744w(11)'s
response divided difference with the enclosed b(k_n), the64-term
exponential response plus its normalized per-entry remainder10^-30,
and the exact256C*C moment contribution. Here n>=512>m, so the exact
denominator (pi/ell)^2(n-m)(n+m) is strictly positive; interval division
also checks this directly. No equal-argument or differentiated
asymptotic formula is needed.

For T_I and S_I use all sixteen prime powers in C744w Section3's
antiderivative, with delays delta and -delta respectively. Reduce every
sine/cosine interval by an integer multiple of pi/2; the checked reduced
absolute argument is<.786, where the degree21/20 Taylor remainder is
<10^-21. Include the complete continuous response: terms1 through7
and the operator tail<10^-24, also valid entrywise. The constant head
mode uses nu_0=ell^-1/2; other normalizations use sqrt(2/ell).
Every response, moment and translation entry in every block is enclosed.

**Propagation through the exact proxy.** Let L_c,T_c,S_c be the
dyadic centers of a block's interval matrices and e_L,e_T,e_S the
Frobenius norms of their radii. These bound the corresponding operator
errors. Write F_L,F_T,F_S for upward Frobenius bounds for the centers,
and F_Z,F_Y for those of the saved Zhat,Yhat. The full saved-factor
checks give F_Z<23, F_Y<10 and ||fl(Zhat Yhat)||_F<10. C999l's audit
gives ||Z_H-Zhat||<=10^-14, ||Z_H||<z=1.008, ||Yhat||<y=1.320001.
Form only the combined residual center

    rho_c=fl([T_c Zhat,S_c Zhat]-L_c fl(Zhat Yhat)).

With u=2^-53 and gamma_r=ru/(1-ru), a complete block residual error is

    e_entry=(e_T+e_S)z+e_L z y,
    e_basis=[F_T+F_S+e_T+e_S+(F_L+e_L)y]10^-14,
    e_ar=gamma_4096[(F_T+F_S)F_Z+F_L F_Z F_Y+1],
    e_rho=e_entry+e_basis+e_ar.                       (60)

The first two terms use operator norms and the triangle inequality.
The last uses full Frobenius product bounds: it includes formation
of the raw predictor, all three matrix products and the subtraction.
Their inner dimensions are at most512 and gamma_4096 dominates the
combined paths. The inherited IEEE754/negligible-underflow contracts
remain in force. No within-column residual contribution is squared
separately, and no orthogonality between residual terms is assumed.

Enclose every scalar a_n=2/h(k_n) in the block, let a_c be its dyadic
center, a_max the maximum upper endpoint and e_a the largest radius.
Put F_rho=||rho_c||_F with upward rounding, and F_old=||Vhat_c|_I||_F.
Compute the full dyadic difference

    D_c=fl(fl(diag(a_c)rho_c)-Vhat_c|_I),
    e_sc=gamma_8[a_max F_rho+F_old+1],
    q_I=||D_c||_F+a_max e_rho+e_a F_rho+e_sc.          (61)

The scalar allowance includes multiplication and subtraction rounding.
The exact block difference has operator norm<=q_I: a_max e_rho uses
the exact inverse weights, while e_a F_rho pays their conversion.
Distinct raw output blocks are orthogonal, so for every complex x

    ||(Q_c V-Vhat_c)x||^2
        =sum_I ||Q_I(V-Vhat_c)x||^2
        <=(sum_I q_I^2)||x||^2.                      (62)

This uses orthogonality only between output ranges. It applies equally
to complex heads because all real matrix error bounds extend to their
complexifications. The directed80-digit sum over EVERY block gives

    sqrt(sum_I q_I^2)<1.494931e-8.

For context, the entire dyadic difference has Frobenius bound
<7.119044e-9. The quadrature of residual-entry bounds is<1.903866e-8
and that of product-rounding bounds is<9.366710e-11; both are already
included through(60)-(62). These numbers are enclosures, not evidence
from a sample or closeness of two floating implementations.

**Mixed propagation and evidence.** By(4), changing this inverse
portion changes the pair W by (-T*(Q_c V-Vhat_c),-T(Q_c V-Vhat_c)).
Use C744v's complete ||T||<4.71, C999l's M_cert>=mu I with mu=.000999,
and(7)'s zeta^2<=1/6.14+4/(3*6.14*511^3). Thus the second line of(58)
is bounded by

    zeta sqrt(2)*4.71 sqrt(sum_I q_I^2)/sqrt(mu)
      <.000001271422513.                             (63)

Reproduce with

    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/separation-seven/signed-mixed-complement-inverse-574.py

All280 checks pass. The complete certificate records all127 block
error ledgers, every check/failure, scalar enclosures and hashes.
The arrays contain every scalar digamma/prime-sine enclosure and
every1020-column dyadic difference row. Inspection checked complete
block coverage, all flags, the source/input/archive hashes and the
directed sum in(62); this is not a separate mathematical audit.
The initial sought component allowance was .0001; the achieved bound
permits the simpler tighter allowance .000002 without altering any
operator, predictor, cutoff or allocation. The JSON's original
.002548 residual budget uses the looser initial allowance and remains
valid; the following sharper deduction uses the actual achieved bound.

Let eta_dir be the normalized distance from B_hc's finite portion to
the exact saved center(47). Equations(51),(53),(58) give

    eta<=.001556+.000002+eta_dir.

Consequently eta_dir<=.002646 is sufficient for eta<=.004204. It is
UNPAID: it still includes the remaining direct L/T/U entries, exact
neutral-basis/raw-predictor conversion and the FFT-to-exact-operator
connection for the saved inverse outputs. The old locator's FFT
accuracy has neither been assumed nor certified. Sections12-15 await
independent audits. The full quarter inequality, independent endpoint
complement coercivity, whole-core/c_*, C744q margin, H2 existence,
non-neutral coverage and global actual-Xi positivity remain unresolved.
This is local error payment within a known method, not a source-level
novelty claim, a quarter rejection/pass or an RH candidate.

### 16. Complete finite direct-action enclosure — step575

**Scope and exact remaining comparison.** Reuse unchanged ready562 and
approval563, with the source/duplicate/failure comparison of Sections14-15.
This is REPRODUCTION of the covered finite-entry and arithmetic method.
No FFT error theorem is imported, proved or assumed. Retain K=65536,
J=32768, the exact predictor, fixed Yhat proxy, R, M_cert and quarter
allocation. Let Z=Z_H and let Xhat be the exact saved dyadic head inverse
from Section14, extended by zero outside modes0:511. Let Vhat_c be
Section15's exact saved complementary inverse array, zero on the head.

Define the direct pair of maps on the1020-dimensional complex head by

    v0=Z Yhat+Xhat,
    D_f=[LZ,-U*Z]-T* v0,
    D_h=[-UZ,LZ]-T v0.                               (64)

Here each rectangular bracket acts on (x_f,x_h), while v0 acts on both
head components. The full L includes D, S and256C*C. In particular its
low rows are not dropped. The pair(D_f,D_h) maps into the two raw
coefficient spaces.

For any pair A of raw-row maps defined on0:65535, write

    (N_K A)_(a,n)=d_n^(-1/2)(A_(a,n)-r_n A_(a,p)),
       a=f,h, 512<=n<65536, p=n mod2.                (65)

The r_n,d_n are EXACT, as in(1); this notation includes both overlapping
low-mode corrections. The full new dyadic center Dhat is the binary array
`scripts/separation-seven/signed-mixed-direct-center-575.npy`, with shape
(2,65536,1020). The proved bound is

    ||N_K((D_f,D_h)-Dhat) M_cert^-1/2||
       <3.740262e-7<.000001.                         (66)

All65536 raw rows and both endpoint orientations are covered, including
the two low rows used in(65). The other head rows are also enclosed,
although (65) does not use them. No entries or signed terms within a
column are discarded, and this is a norm error, not a covariance sum.

**Complete entry enclosures.** The source, JSON, scalar-array NPZ and log
have basename `scripts/separation-seven/signed-mixed-direct-action-575`.
The computation checks all prerequisite flags and source/archive pins
from573/574 and audit561. It reuses Section14's complete interval head
matrix PLP and Section15's complete b(k_n),k_n tables. Their underlying
analytic input is still the precise DLMF5.11.2/5.11(ii) remainder and
4096-step recurrence in(59), under its right-half-plane hypotheses.
They are existing enclosures, not approximate digamma oracle values.

For raw rows n>=512 and columns m<512, build the entire response with
C744w(11)'s divided difference, all64 exponentially weighted terms and
the normalized per-entry remainder10^-30. Add the exact moment penalty.
The disjoint rectangle has no diagonal D term. On0:511 the saved full
head enclosure includes the diagonal response series, its complete tail
and D. Every interval denominator is checked to exclude zero.

Independently enumerate all prime powers with3^(s-1)<q^2<3^(s+1),
s=7,14, by integer primality tests and prime-power iteration up to4000;
4000^2>3^15. The counts are16 and334. For every nonzero delay
delta=s ell-log(q), enclose its sign and |delta|<ell, its exact weight,
and sin(k_n delta),cos(k_n delta) for EVERY0<=n<65536 using the outward
range reduction and degree21/20 Taylor bounds of Section15. For s=14,
q=2187 is exactly the zero translation, retained as its full weighted
identity. The other remote delays have127 positive and206 negative signs.

Aggregate s_+(n)=sum_(delta>0) a_delta sin(k_n delta) and s_-(n)
similarly, with signed negative arguments retained. C744w Section3's
antiderivative, already summed in Section6, gives the normalized
off-diagonal entry

    nu_n nu_m[-P_n P_m k_n s_+(n)+k_m s_+(m)
                   +k_n s_-(n)-P_n P_m k_m s_-(m)]
                  /(k_n^2-k_m^2), P_n=(-1)^n.        (67)

For the adjoint replace (s_+,s_-) by(-s_-,-s_+). For n=m>0 the exact
normalized diagonal is the sum of
a_delta[(1-|delta|/ell)cos(k_n delta)
       -sign(delta)sin(k_n delta)/(ell k_n)].
For n=m=0 omit the sine term. The zero shift contributes its weight
on the diagonal and zero off it. These cases include the nu_0 versus
nu_n normalization; no equal-argument divided difference is used.

Retain the complete continuous kernels of T and U. Their first seven
terms have column factors

    c_j=2j+1/2, e_j=3^(-j-1/4),
    m_j(n)=nu_n c_j(1-P_n e_j)/(c_j^2+k_n^2),
    p_j(n)=nu_n c_j(P_n-e_j)/(c_j^2+k_n^2),
    3^(-(s-1)(j+1/4)) m_j(n)p_j(m), j=1,...,7.

Transpose these factors for the adjoint. C744z(23), the already covered
complete geometric tail, bounds the remainder operator by

    3^(-(s-1)(8+1/4))/[(33/2)(1-3^(-(s-1)))]<10^-24.

This is valid for both s=7 and14 and hence entrywise. The exact neutral
definitions have already removed the separated j=0 cross term; no term
of the defined T or U is omitted. Every128 consecutive512-row rectangle
is enclosed for L,T,T*,U,U*, each with all512 raw head columns.

**Complete product and coordinate errors.** For a rectangle I, let
l,t,s,u,a be the dyadic centers for those five matrices, e_L,e_T,e_S,
e_U,e_A the upward Frobenius bounds for their radii, and F_L,F_T,F_S,
F_U,F_A their upward center Frobenius bounds. These also bound operator
norms and errors. Use C999l's audited z=1.008, y=1.320001 and
||Z-Zhat||<=10^-14. Let F_Z,F_Y,F_X bound the full Frobenius norms of
Zhat,Yhat,Xhat, and put

    vhat0=fl(fl(Zhat Yhat)+Xhat), F_v>=||vhat0||_F,
    e_v=10^-14 y+gamma_1024(F_Z F_Y+F_X+1),
    gamma_j=j*2^-53/(1-j*2^-53).                     (68)

Thus ||v0-vhat0||<=e_v. The stored block of Dhat is

    Dhat_f=fl([fl(l Zhat),-fl(a Zhat)]-fl(s vhat0)),
    Dhat_h=fl([-fl(u Zhat),fl(l Zhat)]-fl(t vhat0)).

The following complete bound q_I applies to the operator norm of the
PAIR of block errors:

    e_entry=(2e_L+e_U+e_A)z+(e_T+e_S)(F_v+e_v),
    e_basis=(2F_L+F_U+F_A)10^-14+(F_T+F_S)e_v,
    e_ar=gamma_4096[(2F_L+F_U+F_A)F_Z+(F_T+F_S)F_v+1],
    q_I=e_entry+e_basis+e_ar.                         (69)

To verify the decomposition, for example LZ-l Zhat=(L-l)Z+l(Z-Zhat),
and T v0-t vhat0=(T-t)v0+t(v0-vhat0), with ||v0||<=F_v+e_v.
Apply the same identities to both remote and T orientations, then use
the triangle inequality for the two output spaces. The coefficient2
pays both local copies; no independence of these errors is assumed.
The dot-product contract with inner dimension512 and gamma_4096 covers
all products and final subtractions. Equation(68) separately pays raw
predictor formation and addition of Xhat. Frobenius evaluations round
their positive squared sums and square roots outward. The inherited
IEEE754, negligible-underflow and directed-Decimal contracts are retained.

**Weighted full row sum and low corrections.** Let q_0 denote(69) for
raw rows0:511; it bounds in particular the PAIR of low-row errors.
For each later block with first index n_I, monotonicity gives
d_n>=d_(n_I). Orthogonality of distinct raw output ranges, applied to
each head vector, therefore bounds the weighted raw-row error by

    e_raw=[sum_(I: n_I>=512) q_I^2/d_(n_I)]^(1/2).

Only output ranges are squared and added here; within-block terms in
(69) were added as norms. By(6), the repeated low-row corrections in(65)
have operator norm at most alpha q_0, where

    alpha=[4/(3*6.14*511^3)]^(1/2).

The triangle inequality, followed by M_cert>=mu I, mu=.000999, proves

    ||N_K((D_f,D_h)-Dhat)M_cert^-1/2||
           <=(e_raw+alpha q_0)/sqrt(mu).             (70)

The complete80-digit directed ledger gives q_0<8.694121e-7,
e_raw<1.178676e-8, alpha q_0<3.507354e-11 and the full right side
<3.740261565e-7. The displayed rounded intermediate values are not
used to obtain the final bound. All128 blocks,350 prime records and
1111 production checks are recorded, with no failures. Reproduce with

    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/separation-seven/signed-mixed-direct-action-575.py
    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/separation-seven/check-signed-mixed-direct-action-575.py

The latter checks every saved block ledger and center-row digest,
all production flags and artifact/input pins, and the complete sum(70).
Its evidence is `scripts/separation-seven/signed-mixed-direct-action-check-575.json`.
It is not an independent entry replay or conceptual audit. The first
script records its initial .00001 component test; the achieved bound
permits the tighter .000001 reservation without any parameter change.

**What remains unpaid.** Write W_hat for the unchanged raw dyadic rows
from565 that define Section13's certified center, and put

    A_V=(T*Vhat_c,T Vhat_c),
    eta_action=||N_K[A_V-(Dhat-W_hat)] M_cert^-1/2||.  (71)

The difference Dhat-W_hat in(71) is an EXACT difference of two dyadic
arrays. A later floating subtraction must pay its rounding. The inverse
head is already in(64), so A_V contains only the complementary inverse
outputs512:65535. In B_hc the finite raw pair is exactly(D_f,D_h)-A_V.
Equations(66),(71), the triangle inequality and Sections14-15 consequently
give

    eta <= .001556+.000002+.000001+eta_action.

Thus eta_action<=.002645 would suffice for eta<=.004204 in(51). This is
a remaining threshold, not an achieved estimate. Direct full T/T* entry
products could test(71) under the existing arithmetic coverage; no FFT
accuracy is licensed by (66). The source and error analysis for any new
FFT theorem would instead need separate review. The new direct center
does not change the old covariance center, predictor, reference or
allocation. Sections12-16 still need independent audits; the exact
finite covariance, quarter inequality, independent complementary lower
comparison, whole-core/c_*, C744q margin, H2 slack/existence, non-neutral
coverage and global actual-Xi positivity remain open. This is local
error payment by a known method, with no source-level novelty claim.

### 17. Complete finite inverse action and mixed quarter bound — step576

**Scope and conclusion.** Continue unchanged ready562/approval563,
using the same source/duplicate/failure comparison. This is REPRODUCTION
of the covered explicit-entry and dot-product method, with no new FFT
theorem or accuracy premise. Retain all of Sections12-16's inherited
qualifications, original predictor/reference, K=65536, J=32768, saved
dyadic centers and fixed quarter allocation. For EXACTLY A_V,Dhat,W_hat
in(71), the new result is

    eta_action<.000002142174<.002645.                 (72)

The actual certificate upper endpoint is below .000002142173654; the
displayed rounded bound is only a readable upper bound. Combining(72)
with the previously recorded allowances gives

    eta <= .001556+.000002+.000001+eta_action
         < .001561142174,
    lambda_fin <= (sqrt(.083)+eta)^2 < .083901959
                  < .085440,
    ||M_cert^-1/2 B D_tail^-1/2||
         <=sqrt(lambda_fin+.151^2)+.163+.008
          < .497655 < 1/2.                           (73)

Thus G_mix<=M_cert/4 under the stated contracts. This is a local
specialization, not progress beyond the checked general method, an
independent audit, or a complete RH candidate. The separate condition
F(0,y)>=||y||_tail^2/4 has not been proved or assumed.

**Complete finite entries.** The production source, JSON and log have
basename `scripts/separation-seven/signed-mixed-inverse-action-576`.
It checks every prerequisite572/574/575 flag and all used source,
archive and saved-array pins. Reuse their complete interval helpers,
exact prime enumeration and all65536-mode sine aggregates. Recompute
the exact sixteen-shift diagonal for EVERY mode using(67)'s diagonal
cases, including n=0. Off diagonal use(67), with the denominator
enclosed as (pi/ell)^2(n-m)(n+m). Here integer products are exact
binary64 integers of modulus<2^53. Every off-diagonal denominator
excludes zero; the diagonal is overwritten by its separate formula.
Every interval endpoint is checked finite and ordered.

Partition raw rows0:65535 into512 consecutive128-row rectangles,
each containing all65536 raw columns. Let C_I be the EXACT dyadic
center of the finite prime-translation rectangle, e_I its upward
Frobenius radius norm and F_I an upward Frobenius center norm. With
C their stacked dyadic matrix, orthogonality of output ranges gives

    e_T=(sum_I e_I^2)^(1/2), F_C=(sum_I F_I^2)^(1/2),
    ||T_prime,K-C||<=e_T, ||C||_F<=F_C.

The entire4,294,967,296-entry matrix is covered. Contributions from
the sixteen shifts are combined within each entry BEFORE forming
its radius or center; no covariance of separate signed terms is used.
The complete directed ledger gives e_T<1.018942e-7.

Let V=Vhat_c be the EXACT unchanged saved array565 and let
F_V>=||V||_F be its full upward Frobenius norm. Its first512 rows
are checked zero. Compute CV in full128-row products. Compute C^t V
by summing C_I^t V_I over every nonzero raw input block. This uses
the same C for both orientations and every1020-column entry. The
prime entry error in either orientation is <=e_T F_V.

**Continuous kernels and complete product arithmetic.** Keep all
seven continuous terms from Section16, as finite rank-one matrices
a_j b_j^t, with the exact prefactor absorbed into a_j. Let a_c,b_c
be dyadic factor centers, e_a,e_b their upward Frobenius radius norms,
and F_a,F_b upward center norms. Expanding
(a-a_c)b^t+a_c(b-b_c)^t proves

    ||a b^t-a_c b_c^t|| <= e_a(F_b+e_b)+F_a e_b.

For each orientation compute every K-term dot b_c^t V or a_c^t V,
then the full outer product. Use u=2^-53, gamma_r=ru/(1-ru), and
charge a per-term error

    q_j=[e_a(F_b+e_b)+F_a e_b]F_V
                  +gamma_(2K+32)(F_a F_b F_V+1).

The prime product charge is gamma_(2K+32)(F_C F_V+1). Indeed the
usual componentwise dot-product bound controls a direct K-term dot;
each transpose path has a128-term dot and at most512 block additions.
Even with all seven later continuous additions, every scalar path has
fewer than2K+32 operations counted by this bound. Taking Frobenius
norms gives the charges above for real matrices and therefore also
their operator norms on complex head vectors. Complete rank-one
products remain combined with the prime contribution in each output.
An additional positive allowance

    gamma_32[(F_C+sum_j F_a,j F_b,j)F_V+1]

provides addition slack. All positive squared sums, square roots and
scalar arithmetic are outward as in Sections14-16. Retain the stated
IEEE754 and negligible-underflow contracts; no library FFT, sine,
logarithm or matrix-inverse accuracy is assumed.

The remaining continuous operator norm is bounded by Section16's
complete geometric tail

    tau_c=3^(-49.5)/[(33/2)(1-3^-6)]<10^-24.

This pays tau_c F_V in either orientation. It is an operator bound
on the entire omitted continuous kernel, not an entrywise remainder
misapplied to infinitely many rows. Let E be the sum of e_T F_V,
the prime product charge, all seven q_j, the addition slack and
tau_c F_V. If Ahat is the resulting complete dyadic pair, then

    ||(T*V,TV)-Ahat|| <= sqrt(2) E.                  (74)

Both terms use the finite raw input/output range0:65535; V is zero
outside512:65535. Thus they are exactly the finite restriction of
A_V in(71), including the low output rows used by N_K.

**Exact-target subtraction and neutral coordinates.** Store Ahat in
`scripts/separation-seven/signed-mixed-inverse-action-center-576.npy`.
The full dyadic differences, including the two low rows, are in
`scripts/separation-seven/signed-mixed-inverse-action-difference-576.npy`.
Compute

    delta=fl(Ahat-fl(Dhat-W_hat)).

For each128-row tail rectangle in each orientation, bound its two
subtraction roundings by

    s_I=gamma_8(F_Ahat,I+F_Dhat,I+F_What,I+1).

Compute the analogous combined low-row bound s_0. Since
1/sqrt(d_n)<1/2 and the repeated low corrections have norm at most
alpha from(70), their complete weighted contribution is bounded by

    E_sub=(1/2)(sum_tail I s_I^2)^(1/2)+alpha s_0.

This pays cancellation in the EXACT dyadic target Dhat-W_hat, rather
than identifying it with an unpaid rounded subtraction.

Use the complete pinned572 tables with |rhat_n-r_n|<10^-20 and
exact upward dyadic weights 1/sqrt(d_n)<=t_n<1/2. For every tail
row compute fl(t_n fl(delta_n-rhat_n delta_p)), p=n mod2. If F_delta
and F_rep bound the full rectangle and its repeated low-row matrix,
its discrepancy from the exact t-weighted neutral row is at most

    c_I=(1/2)[10^-20 F_rep
                    +gamma_16(F_delta+10^-5 F_rep+1)].

The first term pays ratio conversion and the second all row
multiplications/subtractions. The t_n are exact dyadic majorants,
so their use only increases the target weighted Frobenius norm.
Let E_coord=(sum_I c_I^2)^(1/2), and let W be the upward Frobenius
norm of ALL evaluated weighted rows in both orientations. All output
rectangles in these sums are disjoint. No term within a signed column
is discarded. The complete ledger gives W<1.710292e-8.

From(7),(65),(74), M_cert>=mu I with mu=.000999, and the triangle
inequality, the entire desired normalized error is bounded by

    eta_action <= [W+E_sub+E_coord+zeta sqrt(2)E]/sqrt(mu),
    zeta^2<=1/6.14+4/(3*6.14*511^3).                 (75)

The zeta term pays the full action error including its low rows.
The other two terms pay exact-target subtraction and exact neutral
coordinate conversion separately. Neither raw projection neutrality,
orthogonality of low corrections nor an infinite boundary trace is
assumed. Full80-digit directed evaluation gives(72).

**Evidence and consequence.** Reproduce with

    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/separation-seven/signed-mixed-inverse-action-576.py
    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/separation-seven/check-signed-mixed-inverse-action-576.py

All1567 production checks and3596 complete saved-evidence checks pass.
The latter records every input/output hash, all matrix/continuous and
difference ledgers, every saved weighted-difference row, and the entire
directed sum(75) in
`scripts/separation-seven/signed-mixed-inverse-action-check-576.json`.
It is not an independent entry replay or conceptual audit. The exact
full finite covariance bound is <.083901958562 M_cert; (46) then gives
full mixed norm <.497654188036 and proves(73). All earlier input/output
and predictor allowances are charged once in their stated places.

Sections12-17 still need separate critical audit. Whole-core/c_*,
independent complementary coercivity, C744q margin, H2 slack/existence,
non-neutral coverage and global actual-Xi positivity remain unresolved.
Passing the fixed mixed quarter test does not establish any of them.
No new reference, predictor, cutoff, allocation, central mechanism or
RH/H2 premise has been introduced. The earlier scalar and proxy failure
evidence remains intact; historical open-quarter remarks retain their
original evidential meaning and are superseded only by the qualified
local result here.

### 18. Separate mixed-quarter conceptual audit — step579

**Scope and result.** The invocation-start SPECIALIZE assessment577,
separately approved578, covers exactly this audit. Sections12-17 are
upheld under the inherited analytic-response, whole-neutral-core,
unreplayed c_*, IEEE754 and directed-Decimal contracts. Sections1-11's
audited interfaces are reused. No predictor, reference, cutoff, quarter
allocation, source theorem or complementary sign is changed. This is
REPRODUCTION: validation of an existing local quantitative claim, with
no improved bound or mathematical novelty beyond the checked sources.
The form/inverse-order imports in the Hypotheses retain their exact
domains and qualifications; no general Schur theorem is reproved.

**Directional input covariance.** The remote positive-delay pair is
(v_-(f_H),v_+(h_H)); the negative-delay pair reverses both signs.
This agrees with Section7's four-row ordering and the adjoint delay
reversal. For the middle terms the exact leading argument is g+V_0x
in BOTH orientations. Consequently the two trial and inverse boundary
rows must be added before their Gram, as implemented in Section12.
All boundary evaluations are on finite vectors supported below J;
there is no asserted trace of the full inverse or a general Y_D vector.
The remainder maps W_1V_0,W_2V_0 and V_1 cover the remaining prime
terms; the complete continuous kernels and three low corrections are
also paid. The endpoint remainder is a block diagonal/off-diagonal map
on independent endpoints, whereas applying T and T* to the same middle
vector costs the displayed sqrt(2). These facts justify the different
sqrt(2) occurrences in the table, without a reality restriction.

Equation(42) is pointwise in the SAME head vector. Cauchy--Schwarz
with the positive weights a_i gives(43), and every t_i is an upper
enclosure of S c_i q_i^2/a_i. Thus(44) is a genuine common matrix
majorant, not a sum of purported independent error covariances.
The conversion(45) applies before division by sqrt(mu). In particular
the combined boundary error pays both inverse boundary rows, both
trial rows and their addition; the unweighted V_0 conversion alone
uses orthogonality of its two raw output ranges. The replay reconstructs
all ten Grams and the saved full factor, with error <3.235e-7 inside
the restored10^-6 margin. The complete result remains <.150650426,
so the reservation .151 is valid.

**Dyadic center versus exact operator.** Equation(47) defines a map
from exact binary rows; it does not claim those rows evaluate the
operator accurately. Upward positive row weights give A_c*A_c<=A_u*A_u
even with the repeated low rows. The ratio-conversion and arithmetic
bound(49) applies to the entire two-endpoint Frobenius norm. Every signed
row is neutralized before its outer product. The replay regenerates
all65024 coordinate intervals, all254 Gram blocks and their complete
combined digest, and reconstructs the original factor. Its full
error <3.528e-7 is below10^-6, verifying(48) for all complex heads.
No FFT accuracy is inferred from that result or from array agreement.

**Complete finite connection and orientations.** The intermediate maps
are used in the order B_tilde^(K), B_h, B_hc, then the dyadic center.
Only the inverse head is replaced first; only its complementary inverse
outputs512:65535 are replaced second. In B_hc the exact raw pair is
(D_f,D_h)-(T*Vhat_c,T Vhat_c). Equation(64) includes the saved inverse
head Xhat once and the exact proxy ZYhat once. The dyadic target in(71)
is Dhat-W_hat with an EXACT subtraction; Section17 separately pays
both floating subtractions. These identities verify the signs, adjoints
and absence of duplicate head or predictor terms in the comparison.

Section14's source replay recomputes every one of the786432 entries
in the three complete head enclosures and agrees with the saved arrays.
The recurrence stays in Re(z+4096)>0; both components include(59)'s
sector remainder. The separate equal-mode response sum and its full
tail avoid differentiating an asymptotic error. Constant-mode and
diagonal translation cases, moment penalty and continuous tails are
included. The saved correction is tested by its full residual and
factor, using the existing exact H>=.239999I. Thus the true head error
is bounded by(57), not by an assumed solver accuracy or a scalar floor
for A0. Its propagated contribution is <.001555699<.001556.

For Sections15-16 the disjoint response rectangle has no D diagonal.
Its denominator excludes zero. The shift antiderivatives give(67);
replacing delays by their negatives changes (s_+,s_-) to(-s_-,-s_+),
which is exactly the implemented adjoint. At n=m the separate diagonal
formula has the same value for either adjoint; at n=m=0 it has no sine
quotient. The remote zero delay contributes its identity term. The
continuous prefactor is exp[-c_j(s-1)ell], with the two cosine-integral
factors in the stated order, transposed for the adjoint. All sixteen
and334 shifts and both continuous tails remain present.

The product estimates(55),(60),(69) bound the combined signed matrix
errors by Frobenius products and operator-norm triangle inequalities.
They include formation of Zhat Yhat and exact-Z conversion. In(61)
the exact reciprocal maximum multiplies the residual error, while the
reciprocal radius multiplies the center norm. Only disjoint raw output
blocks are squared and added in(62). Similarly(70) sums disjoint raw
rows before adding the repeated low-mode contribution in norm. The
complete127 and128 block ledgers and all saved difference/direct rows
were inspected and their totals recomputed. The contributions are
<.000001271423 and <.000000374027, within .000002 and .000001.

**Full inverse action and arithmetic.** Section17 uses the SAME finite
center C for CV and C^tV. The latter sums C_I^tV_I over all blocks
with nonzero V_I; omission of the first512 rows is legitimate because
Vhat_c is exactly zero there. Every block has all65536 columns, so no
output or inverse-input prefix is substituted for this action. Its
off-diagonal integer denominator (n-m)(n+m) is exact in binary64;
diagonals use the separate formula. Summing squared radius norms over
disjoint output rectangles bounds the full matrix error, also for its
adjoint. Multiplying by the full F_V bounds both action errors.

The seven continuous terms use complete K-term dots. For the prime
transpose path each product uses128 terms followed by at most512 block
additions. These paths and subsequent continuous additions fit inside
gamma_(2K+32). The Frobenius product bound follows by applying the
componentwise dot error to |C||V|, or |C|^t|V|; both are bounded by
F_C F_V. The separate addition slack is conservative. The remaining
continuous tail is used as an OPERATOR bound in(74), before multiplying
by F_V, rather than summing a constant entry error over infinite rows.
Both orientations cost sqrt(2)E. All512 matrix-block and seven
continuous-term ledgers were checked in full.

Every one of the1016 finite difference blocks and both low rows was
recomputed from the saved arrays. The ratio approximation and all
subtraction/product roundings are paid separately. Upward dyadic
weights enlarge the Frobenius norm of the already combined neutral
rows. Raw-row errors can be added in squares because their output
ranges are disjoint; their common low corrections must instead be
added in norm. Equations(74)-(75) use exactly that order. Thus the
complete normalized action error is <.000002142174, below .002645.

**Assembly and complete evidence.** Reproduce from this notebook:

    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/separation-seven/signed-mixed-quarter-audit-579.py

The full audit certificate and log have the same basename with json/log
extensions. All4849 checks pass. The script preserves all original
artifacts, replays complete571/572/573 calculations before their first
artifact writes, reconstructs their saved factors, independently
reassembles all574 ledgers and reruns the entire575/576 evidence checks
without overwriting them. It does NOT independently regenerate the
complete574-576 entry/product computations, in particular the4,294,967,296
prime-matrix entries of576. Their complete production sources, formulas,
case splits and error propagation were reviewed as above; their executed
ledgers, arrays and contracts are retained. This limitation is explicit:
the audit is an informal computational proof review, not formal
verification or an independent second implementation of every entry.

The finite error is <.001561142174 and hence the exact finite covariance
is <.083901958562 M_cert. The finite and remaining input ranges are
disjoint, giving the square root in(46). By the audited Sections6/8,
the assembly B -> B^(K) -> B_tilde^(K) pays .163 and .008 ONCE for
the entire map. Consequently the complete directed result is

    ||M_cert^-1/2 B D_tail^-1/2||
       <.497654188036<.497655<1/2.

This upholds(73) and G_mix<=M_cert/4. It supplies no lower bound for
F(0,y). In particular it cannot be substituted for the independent
condition F(0,y)>=||y||_tail^2/4 in a later Schur assembly. Whole-core/c_*,
C744q margin, H2 slack/existence, non-neutral coverage and global
actual-Xi positivity remain open. No RH candidate or disproof is claimed.

## Mathlib

Full matching coverage for this exact neutral-coordinate specialization
and signed residual covariance is unchecked, not asserted absent.
The form representation and relation inverse-order sources above are
standard mathematical imports, not claims of matching Mathlib theorem
names. The step565 output-tail specialization has no checked full
Mathlib match. Section17's computational certificate for(5)'s quarter
bound uses the stated execution contracts and awaits critical audit;
no formal verification is claimed.
Full matching coverage for step566's oscillatory remote input-tail
specialization is likewise unchecked.
Full matching coverage for step567's exact-predictor cancellation and
quantitative mixed-map error specialization is unchecked as well.
Full matching coverage for step573's interval head-defect specialization
is unchecked; no formal verification is claimed.
Full matching coverage for step574's complementary inverse-error
specialization is unchecked; no formal verification is claimed.
Full matching coverage for step575's complete direct-action enclosure
is unchecked; no formal verification or FFT accuracy theorem is claimed.
Full matching coverage for step576's complete finite inverse action and
mixed-quarter specialization is unchecked; the execution/evidence checks
are not formal verification or a critical audit of Sections12-17.
Full matching coverage for step568's local/direct-trial input-tail
specialization is unchecked; no formal certificate is claimed.
Full matching coverage for step569's fixed-J inverse-input specialization
is unchecked; no formal verification or quarter-budget decision is claimed.
Step570 adds an informal conceptual/certificate audit only. Full matching
Mathlib coverage remains unchecked, and no formal verification is claimed.
Full matching coverage for step571's joint finite-map majorant and
complete input-tail specialization is unchecked; no formal verification
or full quarter-budget certificate is claimed.
Full matching coverage for step572's specific dyadic-center covariance
certificate is unchecked. It is an informal numerical proof under the
stated execution contracts, not formal verification or an exact-operator
covariance certificate.
Step579 adds a conceptual and complete saved-evidence audit of Sections12-17
with the replay limitations in Section18. Full matching Mathlib coverage
remains unchecked; no formal verification is claimed.
