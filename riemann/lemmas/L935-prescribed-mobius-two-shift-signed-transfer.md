# Lemma 935: prescribed Mobius two-shift transfer and the unpaid eigenvalue margin

## Hypotheses

Use the actual real Hardy function Z, Xi gauge A and signed density W
of L637, with the analytic extension and phase of L622. Thus

    Z=-Xi/A,
    W=(Xi'^2-Xi Xi'')/A^2
      =Z'^2-Z Z''-(log A)'' Z^2.

Fix w>=0 in C_c^infinity((0,1)), integral w=1. Let T tend to infinity,
L=log T, T<=X<=2T and w_XT(t)=w((t-X)/T). Keep exactly

    N=floor(T^(1/5)),
    q(n)=mu(n)(log(N/n)/log N)^2, 1<=n<=N,
    b_N^2=sum_(n<=N)q(n)^2/n,
    P_N(t)=sum_(n<=N)q(n)n^(-1/2-it),  M_N=P_N/b_N,
    V_a(t)=a_- Z(t-1/L)+a_+ Z(t+1/L),
    |a_-|^2+|a_+|^2=1,
    I_a(T,X)=integral w_XT W |M_N V_a|^2 dt.

The scalar pair is complex and may depend on T,X. It is held fixed
under shift differentiation, as are all coefficients of P_N. Only
N>1 is used. No RH, simplicity, sign of W, normalization asymptotic
or prescribed size of I_a is assumed.

Import S. Bettin, H. M. Bui, X. Li and M. Radziwill, *A quadratic
divisor problem and moments of the Riemann zeta-function*, JEMS 22
(2020), 3953--3980, [arXiv:1609.02539v1, Theorem 1.1 and its
holomorphy remark, printed pp2--4](https://arxiv.org/pdf/1609.02539v1#page=2).
Its arithmetic theorem and cited complete-sum holomorphy theorem are
named imports, not rederived or independently audited manuscript proofs.
L622 Sections1--4 supply the exact analytic phase and zero-safe
curvature interface. L619 Section3 and its H=T application audit
supply the bounded-real-shift absolute fourth moments used below.

The invocation-start source assessment is
drafts/literature/2026-11-09-prescribed-mobius-signed-test-32.md,
SPECIALIZE, separately reviewed in step33. This is the prescribed
application only, not the arbitrary-coefficient problem parked in
step31. L934 is a dictionary/realization contrast, not a sign input.

## Conclusion

There is an explicitly defined real symmetric two-by-two main matrix
G(T,X), given in (2)--(4), such that for every fixed 0<eta<1/20,
uniformly in X and all unit complex pairs a,

    |I_a(T,X)-b_N^(-2) a^*G(T,X)a|
      <= C_(w,eta) b_N^(-2)
           [T^(19/20+eta)L^2+(N/T)L^4].                  (1)

All six source terms, both orientations, every gcd multiplicity and
the exact Hardy phase remain in G. The constant and onset are
existential. No finite-height sign certificate is asserted.

Normalization is positive and satisfies 1<=b_N^2<=1+log N. More
importantly, it cancels exactly from the signed margin comparison.
Put e_eta(T)=T^(19/20+eta)L^2+(N/T)L^4. A negative eigenvalue of G
with magnitude/e_eta(T) tending uniformly to infinity would give
a negative average along its unit eigenvector eventually. A uniform
positive smallest eigenvalue with the same separation would give
positive averages for every unit pair. Neither separation is proved.

This is a local REPRODUCTION of a known moment-theorem application,
written in step34 on 9 November 2026. Sections 1--4 and (1) passed
the separate conceptual application audit in step36 below, under the
named arithmetic and holomorphy imports.
It establishes the changed-length transfer and its complete error,
not a new arithmetic theorem or a signed eigenvalue decision. The
bounded sign attempt ends at (10) below; the profile is parked without
changing its parameters. Pointwise transfer, realization, higher
mixed signs and RH remain unresolved. There is no RH candidate.

## Proof

### 1. Exact main expression and coefficient accounting

Let S_hk(t;alpha,beta,gamma,delta) be exactly the complete six-term
sum in L622 (3), with its prime-power factors defined immediately
before that equation. In particular, for p^e||h the second divisor
factor is incremented, and for p^e||k the first is incremented. This
is the orientation in BBLR Theorem1.1. Use its holomorphic complete
value at collisions; no individual polar summand is differentiated
there. The agreement of the BBLR and Hughes--Young main expressions
is also stated in the source's second remark after Theorem1.1.

For dimensionless complex shifts z=(z1,z2,z3,z4), set

    alpha=i z1/L, beta=i z2/L, gamma=-i z3/L, delta=-i z4/L,
    Phi(t,z)=exp(i[theta(t+z1/L)+theta(t+z2/L)
                          -theta(t+z3/L)-theta(t+z4/L)]),
    H(z)=sum_(g,h,k>=1; (h,k)=1; gh,gk<=N)
            q(gh)q(gk)/(g h k)
            * integral w_XT(t) Phi(t,z)
                  S_hk(t;alpha,beta,gamma,delta) dt.       (2)

There is no b_N factor in H. The reduced-twist factor 1/sqrt(hk)
and original half-line coefficients q(gh)/sqrt(gh), q(gk)/sqrt(gk)
combine to 1/(g h k), as in BBLR. Every original pair (m,n) occurs
once with g=gcd(m,n), h=m/g, k=n/g, including all diagonal pairs.
In particular no extra coefficient sum is to be multiplied into
the already coefficient-averaged BBLR error.

Define

    Q=partial_1 partial_2-(partial_1^2+partial_2^2)/2,
    D_sr=L^2 [Q H(z)]_(z1=z2=0,z3=s,z4=r),  s,r in {-1,1}, (3)
    G_sr=(Re D_sr+Re D_rs)/2.                              (4)

Thus G is real symmetric, hence Hermitian also on complex vectors.
The symmetrization retains both observer orientations. It avoids
assuming that a complex source approximation is exactly real.

Since |q(n)|<=1 and q(1)=1, b_N^2>=1. Integral comparison gives
b_N^2<=sum_(n<=N)1/n<=1+log N. These elementary inequalities make
the definitions legitimate; neither is used as an asymptotic.

### 2. Uniform source windows, length and exact phase

Choose once and for all finitely many nonnegative smooth functions
chi_j on (0,infinity), summing to one on [1,3], with
support chi_j compactly contained in (c_j,2c_j), where each c_j>0
is fixed. Such a partition exists: the intervals (c,2c), c>0,
form an open cover of [1,3], take a finite subcover and a smooth
partition on a neighborhood of this compact interval. Compact
supports within these open intervals permit extension by zero.
Set Y_j=c_j T and write w_XT=sum_j w_XT chi_j(t/T).

For |z_i|<=2, L622 Section2 proves uniformly on [T,3T]

    |Phi(t,z)|<=C, |partial_t^j Phi(t,z)|<=C_j T^(-j)
                                                     (j>=1). (5)

The same estimates hold on a slightly larger complex shift domain.
This is an exact-phase estimate from analytic gamma branches; no
phase is frozen and no O(1/L) approximation is amplified. For each
piece the source weight, in its dimensionless variable v=t/Y_j, is

    f_(j,z)(v)=w((Y_j v-X)/T) chi_j(Y_j v/T) Phi(Y_j v,z).

It is supported in (1,2). Every fixed v-derivative is O_(j,k,w)(1),
uniformly in X/T in [1,2] and z, by (5) and the product rule.
Thus the source derivative bounds are satisfied uniformly. If a
real nonnegative weight interpretation is required, use L622's
four-weight decomposition: for the nonnegative base w_XT chi_j,
take its products with C+/-Re Phi and C+/-Im Phi, where C exceeds
the uniform bound for |Phi|. Their differences reproduce the
complex weight, with only a fixed factor in the error. This does
not assert holomorphic dependence of the decomposition itself.

Fix eta as stated and choose source parameters

    vartheta=1/5+eta/4, epsilon=eta/4.

They obey 1/5<vartheta<1/4. Uniformly over the finite source windows,
N<=Y_j^vartheta eventually, since N/Y_j^vartheta
<=c_j^(-vartheta)T^(-eta/4) tends to zero. Pad q by zero beyond N.
Its coefficients are bounded by one, satisfying the source condition
with a constant independent of T,X. Keep the original N, q and L
on every piece. Bounded complex shifts divided by L are O(1/log Y_j).

The two source error exponents are

    1/2+2vartheta+epsilon=9/10+3eta/4,
    3/4+vartheta+epsilon=19/20+eta/2.

Both are below 19/20+eta. The fixed finite partition and bounded
height ratios therefore give the following uniform comparison:

    F(z):=integral w_XT |P_N(t)|^2 product_(i=1)^4 Z(t+zi/L) dt
         =H(z)+R(z),
    sup_(|zi|<=2)|R(z)|<=C_(w,eta) T^(19/20+eta).          (6)

Here L622's exact identity product Z=Phi times the four shifted zeta
factors is used. Summing the window main terms recovers (2) exactly.
The stronger BBLR theorem is applied to the whole prescribed
polynomial, not to individual twists outside Hughes--Young's range.

### 3. Collision-safe extraction and complex scalar pairs

F is holomorphic on a neighborhood of the closed shift polydisc:
the t support is compact and the zero-safe Hardy factors are
holomorphic there, with compact-local bounds allowing integration.
H is holomorphic there by the imported complete-sum statement.
L622 Section3 verifies the local-factor denominator conditions on
this same bounded-shift domain; they do not depend on the length of
the finite coefficient sum. Hence R=F-H is holomorphic. The source
remark extends the uniform remainder through shift collisions.

Hold z3=s,z4=r fixed and apply Q at z1=z2=0. Cauchy's formula on
the unit circles in z1,z2 costs at most 3 times the bound in (6):
one for the mixed derivative, and one for each second derivative
after its factorial 2! is multiplied by 1/2. The observer shifts
are strictly inside the holomorphy domain and are not differentiated.
The exact identity is

    L^2 [Q F]_(0,0,s,r)
      =integral w_XT |P_N|^2 (Z'^2-Z Z'') Z(t+s/L) Z(t+r/L) dt.

Denote this real symmetric matrix by B. Entrywise,
|B_sr-D_sr|<=3 C_(w,eta)L^2 T^(19/20+eta). Taking real parts
and averaging orientations preserves that upper bound. For any
unit complex pair,

    |a^*(B-G)a|
       <=max_(s,r)|B_sr-G_sr| (|a_-|+|a_+|)^2
       <=6 C_(w,eta)L^2 T^(19/20+eta).                   (7)

For real symmetric B, a^*Ba is precisely the integral with |V_a|^2:
the coefficient expansion a_s conjugate(a_r) agrees after swapping
s,r. No real-coefficient restriction is hidden here. The derivative
operator acts only on the first two Hardy factors, not on P_N or a.

### 4. Complete zero-safe curvature cost

L622 Section4 gives |(log A)''(t)|<=C T^(-2), including the
polynomial prefactor of A, throughout the real support. This is
a derivative of the nonvanishing gauge, never a logarithm of Z.
L619's audited H=T bounded-shift absolute fourth-moment estimate
gives, for s=-1,0,1,

    integral w_XT |Z(t+s/L)|^4 dt <= C_w T L^4.

Indeed its four-zeta absolute bound applies to the purely imaginary
shift i s/L; the real Hardy phase has modulus one. Cauchy--Schwarz
then bounds each integral of w_XT Z(t)^2 Z(t+s/L)^2 by C_w T L^4.
Also, using only |q|<=1,

    sup_t |P_N(t)|^2 <= (sum_(n<=N)n^(-1/2))^2<=4N,
    |V_a(t)|^2<=Z(t-1/L)^2+Z(t+1/L)^2.

Consequently

    |integral w_XT (log A)'' Z^2 |P_N|^2 |V_a|^2 dt|
                       <=C_w (N/T)L^4.                  (8)

The exact curvature identity in the hypotheses holds at every zero
of Xi, of any multiplicity. Combining (7),(8) and dividing by the
positive exact b_N^2 proves (1). There are no other discarded terms:
partitioning is exact, the phase stays in the weight, the full main
sum is retained, and the only differentiation cost is the fixed Q.

### 5. The bounded signed test and its unresolved inequality

Write d_-=G_--, d_+=G_++, r=G_-+. The exact smallest eigenvalue is

    lambda_-=(d_-+d_+)/2
                 -sqrt(((d_--d_+)/2)^2+r^2).             (9)

Real eigenvectors suffice even though the target permits complex
pairs: for a=x+i y, a^*Ga=x^T G x+y^T G y and
||x||^2+||y||^2=1. Thus no complex direction improves on (9).
The complete sufficient separation tests are

    inf_(T<=X<=2T) lambda_-(G(T,X))/e_eta(T) -> +infinity,
                                                        (10a)
or, for unit directions a=a(T,X) on all permitted windows,

    inf_(T<=X<=2T) [-a^*G(T,X)a/e_eta(T)] -> +infinity.   (10b)

Either test overcomes the unknown fixed error constant in (1)
eventually. At finite T the corresponding inequality must exceed
the actual constant, which has not been made effective. The factor
b_N^(-2) cancels from both comparisons; estimating b_N asymptotically
would not supply the missing eigenvalue information.

The prescribed Mobius weights give a useful exact account of what
remains to be estimated. A nonzero q(gh)q(gk) in (2) requires g,h,k
squarefree and pairwise coprime, and its sign is mu(h)mu(k), with
the positive taper factors retained. This follows directly from
squarefreeness and mu(gh)mu(gk)=mu(g)^2 mu(h)mu(k).
The inner arithmetic sum is therefore not a sum of positive weights.
Moreover the six individual shift terms are polar at collisions;
discarding the four mixed terms is not a lower-bound operation.

This attempt establishes no estimate of d_-, d_+, r strong enough
to verify (10a) or (10b). The source bounds the difference between
the actual form and (2), not the sign of (2) after Q. Separate
upper bounds for positive fourth moments do not lower-bound this
signed differentiated expression. This is the same logical warning
as the recorded November1 derivative-cost stops, not a new theorem
of impossibility. No conjectural limiting kernel, normalization
scale or numerical main-term sign is substituted for (10).

The precise retained obligation is (10) for (2)--(4), with the
fixed taper, length and shifts. Under the bounded-attempt rule the
profile is parked, not retuned or scheduled for another identical
transfer calculation. The useful partial result is (1) and the
removal of normalization asymptotics from the sign test. It does
not establish the requested signed decision.

### Separate conceptual application audit — 9 November 2026, step36

The audit covers (1)--(8), with the elementary normalization and the
logical implication of (9)--(10); it does not attempt either signed
inequality in (10). The ready SPECIALIZE assessment is
drafts/literature/2026-11-09-l935-prescribed-transfer-audit-34.md.
The BBLR version and theorem cited in the hypotheses were reopened:
printed pp2--3 give the weight, complex-shift, coefficient and full
six-term hypotheses; the remarks on pp3--4 give the holomorphic
extension and the coefficient-averaged character of the error.
L619 Section3 and its H=T audit, L622 Sections1--4 and its separate
audit, and L637's definitions were checked at their used scopes.

**Uniform application.** On each fixed window Y_j=c_j T, the
dimensionless weight has bounded derivatives of every fixed order,
independently of X/T and the bounded complex shifts. The constants
depend on the once-chosen partition and w; the partition can be fixed
universally. The theorem does not require a positive weight. Even
if one uses the four nonnegative real weights in Section2, all have
the same uniform seminorm bounds. Their recombination is linear.
For each fixed eta in (0,1/20), the chosen vartheta and epsilon give
the two exponents displayed in Section2. In particular their gaps
below 19/20+eta are 1/20+eta/4 and eta/2. The window constants are
absorbed at an onset depending on eta, since T^(-eta/4) tends to
zero. No constant or onset uniform as eta tends to zero is claimed
or needed. The shifts use log T throughout; log Y_j=log T+O(1)
preserves their source bound. The coefficient sequence on every
piece is exactly the same q, extended by zero, with bound one.

**Normalization and orientation.** Expanding |P_N|^2 gives
q(m)q(n)/sqrt(mn) times (m/n)^(-it). The unique substitution
m=gh,n=gk, (h,k)=1, gives the source coefficient q(gh)q(gk)/(ghk).
The h-prime factor increments the negative-height divisor function;
the k-prime factor increments the positive-height one, for each of
the six tuples. These match (2) and L622 (3). The entire polynomial
is the input to BBLR; attaching an additional absolute pair sum to
its remainder would use a different, weaker theorem application.
The normalization b_N is absent from H and is divided out once
after extraction and curvature, so its square has the same factor
in the main expression and both errors. Its positivity and stated
upper bound follow from q(1)=1 and |q(n)|<=1, respectively.

**Collisions with a parameter-dependent weight.** One may first fix
any shift vector z0 and regard f_(j,z0) as a fixed smooth weight.
The source's collision extension then applies while its zeta shifts
vary, with uniform constants from the seminorm bounds just checked.
Evaluating that extended theorem at the shifts of z0 proves (6)
there. Doing this for each z0 proves the pointwise uniform bound
on the whole closed polydisc; it does not differentiate Re Phi or
Im Phi. Independently, F and H with the varying analytic Phi are
holomorphic, so R=F-H is holomorphic. This separates the use of the
source extension from the later Cauchy differentiation.

For completeness, the local denominators checked in L622 (10) have
exponent real parts at least 1-4/L and 2-8/L on |zi|<=2, and the
global reciprocal zeta has real part of its argument greater than
one eventually. The same conditions hold for all six tuples and
on a slightly larger fixed polydisc after increasing the onset.
Thus no prime factor adds a pole there. The finite coefficient sum
preserves the imported complete-sum holomorphy; no estimate uniform
in the number of prime factors is required for this analytic fact.
Compact t support and the nonvanishing analytic gauge give the
corresponding holomorphy of F, including at zeros of Xi.

**Extraction and curvature.** The two observer shifts +/-1 lie
strictly inside this domain. Unit-circle Cauchy estimates cost
1 for partial_1 partial_2 and 1 each for the two half-weighted
second derivatives, hence 3 in every entry. Ordinary t derivatives
restore exactly L^2. The resulting actual matrix B is real and
symmetric. Replacing D by (Re D+Re D^T)/2 retains the same entry
error; for a unit complex pair the passage to its quadratic form
costs at most (|a_-|+|a_+|)^2<=2. Swapping the two real symmetric
indices makes a^*Ba equal the expansion with a_s conjugate(a_r)
from |V_a|^2. No conjugation is differentiated.

The used L619 input gives O_w(T L^4) fourth moments for each real
translated Hardy factor, uniformly on the original moving window.
Hölder against the positive measure w_XT dt bounds each cross
integral Z(t)^2 Z(t+s/L)^2 by the same order. Finite-dimensional
Cauchy--Schwarz gives |V_a|^2<=Z(t-1/L)^2+Z(t+1/L)^2, also for
complex a, and sum_(n<=N)n^(-1/2)<=2sqrt(N) gives |P_N|^2<=4N.
Multiplication by the audited gauge curvature bound O(T^(-2))
therefore gives exactly O_w((N/T)L^4). The product-rule identity
W=Z'^2-ZZ''-(log A)''Z^2 differentiates only the nonzero gauge A;
it remains valid at every real zero, without a simplicity premise.

The complete raw errors are thus O_(w,eta)(T^(19/20+eta)L^2)
and O_w((N/T)L^4). Dividing each by b_N^2 verifies (1) with no
changed hypothesis or exponent. The eigenvalue formula (9) and
real/complex quadratic-form decomposition justify the implications
in (10) only if their stated uniform separations are supplied; none
is supplied by the audit. This verifies a local known-theorem
application, not a new arithmetic theorem, a signed advance or an
RH candidate. Effective constants, pointwise transfer, realization
and higher signs remain unresolved. BBLR and its cited holomorphy
theorem remain named imports, not manuscript proofs audited here.

## Mathlib

Full matching coverage for BBLR's shifted mollified fourth moment,
the actual-Hardy analytic phase application and this signed
two-shift transfer has not been checked and is unknown. Standard
Cauchy estimates, finite Hermitian spectral theory and elementary
Mobius identities are supporting mathematics only; their possible
formalization would not supply (10) or actual-Xi mixed positivity.
