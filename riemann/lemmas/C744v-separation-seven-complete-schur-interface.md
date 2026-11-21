# C744v: Separation-seven complete pairing and a paid complementary diagonal

## Hypotheses

Put ell=log(3)/2, M=7ell, and let N be the complex functions in
C_c^infinity(0,ell) with integral exp(x/2)f(x)dx and integral
exp(-x/2)f(x)dx both zero. Extensions are by zero. Use C744r's
unconditional definitions d(f)=H(f,f) and q_7(f)=H(f,tau_M f),
with inner product linear in its first slot. Use only L742(8)-(12)
and L744(6),(8), not a conditional positivity conclusion of L742.

The analytic response input is Hongmin Li, *Cutoff-free positivity
of localized Weil forms through the (log 11)/2 threshold*,
[paper45, displayed v2, 9 November 2026](https://rstation.ai/problems/riemann_hypothesis/papers/45),
Lemma3.1, (2.1)-(3.4), for arbitrary radius a>0. Its complete form
comparison in (4.7)-(4.9) and weighted covariance method (5.1)-(5.5)
are the Schur precedent. Its endpoint sign and numerical supplement
are not inputs. The bounded-response method is also in bramble_trace,
[paper60, displayed v1, 26 October 2026](https://rstation.ai/problems/riemann_hypothesis/papers/60),
Section2, (2.1)-(2.7), and Sections5-9. No radius-two constants,
inverse, prime list or positivity certificate is transferred here.
These sources were assessed and separately approved in steps529/530.

Below, a=ell/2 and the response identity is applied only to the
single-cell archimedean form. The cross-cell form is calculated
directly from L742. This avoids applying a whole-window sign theorem
at the enclosing length 8ell>4.

The scalar computation uses the [Python Decimal arithmetic contract](https://docs.python.org/3/library/decimal.html):
directed basic operations and correctly rounded logarithm and square
root, widened by one neighboring Decimal. This is the same arithmetic
contract already used in the assessed local response calculations.
The digamma estimate is precisely L744(8)'s specialization of
[DLMF5.11.2](https://dlmf.nist.gov/5.11.E2) and
[5.11(ii)](https://dlmf.nist.gov/5.11#ii).

## Conclusion

There is an explicit bounded operator T on L2(0,ell), defined in (1),
such that on N

    q_7(f)=-<Tf,f>,           ||T||<4.71.                 (A)

It includes all sixteen active prime powers and the entire remaining
archimedean response. In the complete single-cell cosine representation,
write d(f)=<Df,f>+<Sf,f> as in (4), with S bounded positive. Define
the bounded moment map Cf=(integral e^(x/2)f, integral e^(-x/2)f), and

    V_theta=(e^(i theta)T+e^(-i theta)T*)/2,
    A_theta=D+S+256 C*C+V_theta.

This is a closed semibounded form; it agrees exactly with
d(f)-Re(e^(i theta)q_7(f)) on N. The moment penalty changes no
energy value on N and is not a positive shift of the target metric.

Let P retain the cosine modes n=0,...,511 and Q=I-P. For every real
theta the entire complementary form satisfies

    Q A_theta Q >= 1.43 Q.                               (B)

The complete sufficient Schur test is the finite matrix condition

    M_theta - (1/1.43) F_theta* F_theta >=0 for all theta,
    M_theta=P A_theta P,
    F_theta=Q(S+256 C*C+V_theta)P.                        (C)

**Condition (C) was unpaid at step531.** C744w subsequently supplies
a complete certificate; the step534 audit below upholds both under
the stated computational contract. The
step531 result (A)-(B), by itself, does not prove
|q_7(f)|<=d(f). They neither give an exactly neutral smooth violation
nor prove nonnegativity on any larger window. All other separations,
the strict C744q margin, non-neutral directions and global assembly
remain independent gaps. No H2 cutoff was imposed in this sufficient
larger-class comparison; no out-of-budget witness was obtained.

This is a local REPRODUCTION/specialization under the prior EXPLORE
assessment `drafts/literature/2026-11-12-separation-seven-joint-schur-test-529.md`.
The new contribution to the notebook is the explicit complete operator,
certified complementary floor and fixed residual, not a new general
Schur theorem or a sign result beyond the sources checked. This
derivation received the separate critical audit recorded below.

## Proof

### 1. Complete cross-cell operator

For c_j=2j+1/2 and delta_n=M-log(n), set

    (Tf)(x)=(Kf)(x)+sum_(n in P7) a_n f(x+delta_n),
    K(x,y)=sum_(j>=1) exp[-c_j(M+x-y)],
    a_n=Lambda(n)/sqrt(n),
    P7={29,31,32,37,41,43,47,49,53,59,61,64,67,71,73,79}.
                                                               (1)

Each translation in (1) includes its zero-extension indicator. In
L742's polarization the local scalar has zero cross pairing on the
two disjoint supports. Both pole terms factor into the two exponential
moments, hence vanish. Its continuous cross kernel is -k(M+x-y)/2,
where k(t)/2=sum_(j>=0)exp(-c_j t). The j=0 term likewise factors
into those moments and is exactly zero. Since M+x-y>=6ell>0,
the remaining series is absolutely uniformly convergent on the
closed square. Integrals and sums can be interchanged, even for
complex profiles, by this uniform bound and finite-support L1 bounds.

For an arithmetic delay b=log(n), causality gives the cross integral
-a_n integral f(M+x-b) conjugate(f(x))dx. The reverse causal
pairing has no contribution. Thus the coefficient is a_n, not 2a_n.
The term can contribute precisely when |M-log(n)|<ell, that is
27<n<81. Enumerating prime powers gives exactly P7. The endpoint
powers 27 and 81 have zero overlap; all other delays have none.
This proves (A)'s identity, with all nonzero cross terms retained.

### 2. Full operator norm bound

Write J=T-K. For a.e. x put

    r(x)=sum_(n in P7) a_n 1_(0,ell)(x+delta_n),
    R=ess sup r(x).

Weighted Cauchy--Schwarz followed by a change of variables gives

    ||Jf||^2 <= R integral sum_n a_n |f(x+delta_n)|^2 dx
             <= R R_col ||f||^2.

The column sum is sum_n a_n 1_(0,ell)(y-delta_n)=r(ell-y),
up to irrelevant endpoints. Hence R_col=R and ||J||<=R. This
bound is for the complete sum, not a sum of individual operator norms.

Each row integral of K, and each column integral, is at most

    sum_(j>=1) e^(-6ell c_j)(1-e^(-ell c_j))/c_j
    <= e^(-15ell)/[(5/2)(1-e^(-12ell))]
    =1/[2187 sqrt(3) (5/2)(1-1/729)] =: kappa.            (2)

The integral form of the same Cauchy--Schwarz argument proves
||K||<=kappa. It applies because the kernel is nonnegative with
finite row and column integrals. It bounds the entire infinite
response tail, rather than truncating it.

The scalar certificate specified below encloses all event points
-delta_n and ell-delta_n inside the cell, in strictly disjoint
ordered intervals. On each of the resulting seventeen open
subintervals r is constant. Their exact active sets and all sums are
saved and checked. The maximizing set is

    {41,43,47,49,53,59,61,64,67,71},
    log(71)-7ell < x < log(41)-6ell.

The resulting certified bounds are

    R<4.701900<4.702,
    kappa<0.000106,
    ||T||<=R+kappa<4.702006<4.71.                         (3)

In particular ||V_theta||<4.71 for every theta. No real-profile,
parity, phase-grid or self-adjointness assumption about T is used.

### 3. Complete single-cell response representation

Use the orthonormal cosine basis on (0,ell)

    e_0=1/sqrt(ell),  e_n=sqrt(2/ell)cos(n*pi*x/ell), n>=1,
    k_n=n*pi/ell,
    D e_n=h(k_n)e_n,
    h(t)=Re psi(1/4+it/2)-log(pi).

To specialize the imported identity, center the cell at a=ell/2.
For g(y)=f(y+a), split g=g_++g_- by reflection, and identify each
parity with v_epsilon(y)=sqrt(2)g_epsilon(y), 0<y<a. Li's identity
gives the archimedean energy as its diagonal plus the full squares
of the response coefficients, with

    r_j^epsilon(y)=e^(-c_j a)(e^(c_j y)+epsilon e^(-c_j y))
                     /sqrt(1-epsilon e^(-2c_j a)).

The even frequencies q*pi/a and odd frequencies (q+1/2)*pi/a
combine into k_n=n*pi/ell. The signs from centering cancel within
each response square. The diagonal and response terms have no
cross parity contribution, including for complex functions. The
single-cell arithmetic part is empty since exp(ell)=sqrt(3)<2.
The pole is zero on N. Subtracting the pole in the general smooth
identity gives, for the archimedean form itself,

    integral h(t)|F_f(t)|^2 dt/(2pi)=<Df,f>+<Sf,f>,
    <Sf,f>=sum_(epsilon=+,-) sum_(j>=0)
                             |<v_epsilon,r_j^epsilon>|^2. (4)

Here the j=0 SINGLE-CELL response is retained: neutrality does
not license removing it from (4). Its cancellation in (1) concerned
a different, separated cross response.

For completeness the bounded-response specialization is as follows.
Let d_a=1-e^(-a)>0 and t=a-y. Both response absolute values are
at most 2e^(-c_j t)/sqrt(d_a). Thus every finite-prefix absolute
kernel is bounded by

    (4/d_a) e^(-(t+s)/2)/(1-e^(-2(t+s)))
    <=4/d_a+2/[d_a(t+s)].

The constant kernel has norm a. For the second kernel, the Schur
weight t^(-1/2) gives
integral_0^a s^(-1/2)/(t+s)ds <= pi t^(-1/2), by s=t u^2.
It follows that ||S_epsilon||<=(4a+2pi)/d_a. Monotone convergence
of the nonnegative squared projections defines a bounded positive
S on L2 of the full cell. This is the cited source's boundedness
method with the actual a and both boundary cases; its Green identity
is imported, not reproved. No numerical bound for S is used in (B).

D is semibounded and grows logarithmically in this basis by L744(8).
Its form domain consists of coefficients with
sum_n(1+log(2+n))|f_n|^2 finite. Thus D plus any of the bounded
forms S, C*C, V_theta is a well-defined closed semibounded form.
Original compact smooth functions lie in this domain and satisfy (4).
Finite projections lie in the diagonal form domain; no membership
in the original causal generator domain is claimed for those
noncompact cosine vectors. The argument only needs equality on
the original smooth class and positivity of the stated extended form.

### 4. Entire complementary diagonal, uniform in phase

For n>=512, L744(8) gives

    h(k_n)>=log(n/(2ell))-2ell^2/(n^2*pi^2)
           >=log(512/(2ell))-2ell^2/(512^2*9),            (5)

using pi>3. The right side is a uniform bound without needing a
monotonicity assertion about the exact digamma values. S and 256C*C
are positive. Combining (3),(5) therefore gives for every form-domain
y=Qy and every real theta

    <A_theta y,y>
    >=[log(512/(2ell))-2ell^2/(512^2*9)-4.71]||y||^2
    >1.43427654 ||y||^2 >1.43||y||^2.                    (6)

The bracket, not a finite-section eigenvalue, is enclosed in the
scalar certificate. This proves (B) on the infinite complement.

### 5. Exact residual and why the target remains open

For f=x+y with x=Pf and y=Qf, D has no off-diagonal contribution.
Put W_theta=S+256C*C+V_theta. Its boundedness makes F_theta=QW_theta P
a genuine bounded map from the retained finite space to the ENTIRE
complement. Completing the square using (B) gives

    <A_theta f,f>
    >=<M_theta x,x>+2Re<F_theta x,y>+1.43||y||^2
    =< [M_theta-F_theta*F_theta/1.43]x,x>
                      +1.43||y+F_theta x/1.43||^2.       (7)

Consequently (C) would imply the target for every complex smooth
neutral f. All phases imply d(f)>=|q_7(f)|, including the case
q_7(f)=0; no division by a possibly unproved positive d is used.

More explicitly put

    F_0=Q(S+256C*C)P,
    F_c=Q(T+T*)P/2,
    F_s=Qi(T-T*)P/2.

Then F_theta=F_0+cos(theta)F_c+sin(theta)F_s, and its covariance
contains all of

    F_0*F_0, cos(theta)^2 F_c*F_c, sin(theta)^2 F_s*F_s,
    cos(theta)(F_0*F_c+F_c*F_0),
    sin(theta)(F_0*F_s+F_s*F_0),
    cos(theta)sin(theta)(F_c*F_s+F_s*F_c).                (8)

Each matrix entry is the convergent full sum over modes n>=512.
Cauchy--Schwarz and boundedness of W_theta justify the convergence.
The complement floor alone pays none of these products. No matrix
in (C), nor a uniform lower enclosure for it, is computed here.
Failure of this sufficient scalar-floor certificate, if later proved,
would not by itself refute the original neutral inequality.

### 6. Reproduction evidence and diagnostic boundary

Run from the notebook:

    OPENBLAS_NUM_THREADS=1 python3 scripts/separation-seven/complete-schur-531.py

`scripts/separation-seven/scalar-certificate-531.json` contains all
prime powers, weight/delay intervals, sorted event intervals, all
seventeen row sums, the continuous norm bound, and the complementary
floor. Directed arithmetic uses 60 digits; no floating special
function or approximate eigenvalue enters (3) or (6). The checked
upper bound for R+kappa is below 4.702005361; the checked lower
bound in (6) exceeds 1.4342765416. Complete relevant event and row
data were inspected, including the short maximizing interval between
enter:71 and exit:41. Reproduction checks assert every event order,
every active-set decision and both claimed rational thresholds.

The separate `scripts/separation-seven/finite-locator-531.json`
is NOT a certificate. It saves all 64-mode matrices, the numerical
moment projection and all 65 sampled phases. It reports maximum
sampled relative support about0.865163 and minimum sampled finite
margin about0.264171. These numbers do not bound the infinite-space
numerical radius from above or prove uniformity between sample phases.
The fixed 512-mode residual (C) is not that 64-mode compression.

For reproducibility, the response matrix used by the locator has
zero entries between different parities. For the same parity epsilon,
put nu_0=ell^(-1/2), nu_n=sqrt(2/ell) for n>=1, and alpha_n=sqrt(2)nu_n.
Direct integration of the imported responses gives

    S_nm=alpha_n alpha_m sum_(j>=0)
       c_j^2(1-epsilon e^(-ell c_j))
       /[(c_j^2+k_n^2)(c_j^2+k_m^2)].                    (9)

The locator sums j<65536 and adds the leading tail
alpha_n alpha_m/(2c_65536) within each parity. Its omitted-tail
operator error is bounded symbolically by sum alpha_n^2 times

    1/c_J^2+2k_max^2[1/(6c_J^3)+1/c_J^4]
                   +e^(-ell c_J)[1/(2c_J)+1/c_J^2].     (10)

Indeed a decreasing c^-2 sum differs from its integral by at most
c_J^-2; replacing the rational integrand in (9) by c^-2 costs at
most (k_n^2+k_m^2)c^-4, and the exponential factor has the last
bound. Integral comparison gives the c^-4 bound in (10). Entrywise
domination by alpha_n alpha_m times this scalar gives the displayed
operator bound. Its floating evaluation is about3.59e-8. The tiny
cross-response tail after j=7 is bounded by (2)'s geometric argument
starting at j=8. These analytic tail estimates do not certify the
locator's remaining floating arithmetic, digamma evaluation, exact
neutrality, smooth transfer, phase coverage or missing covariance.
No locator vector is promoted to an exactly neutral smooth witness.

The step531 fixed-inequality attempt was inconclusive. That bounded attempt
stops with (C),(8) unpaid, without changing separation, target ratio,
head size, penalty or complementary floor in response to a failure.

### 7. Separate conceptual audit — 12 November 2026, step534

The prior SPECIALIZE assessment532/approval533 authorized this audit.
It reuses the source comparison, not any source numerical sign.
Li's displayed v2 Lemma3.1, (2.1)-(3.4), was reopened solely to check
the exact half-interval normalization, both Green boundary cases and
the smooth-core hypothesis. This is a necessary source-input check
within the approved audit, not a new literature assessment.

Here is the normalization check explicitly. For n=2q, translation
to the centered cell sends e_n to (-1)^q nu_n cos(k_n y);
for n=2q+1 it sends e_n to (-1)^(q+1) nu_n sin(k_n y).
The parity identification multiplies both by sqrt(2). Direct
integration against the imported r_j gives respectively

    +sqrt(2) nu_n c_j sqrt(1-exp(-ell c_j))/(c_j^2+k_n^2),
    -sqrt(2) nu_n c_j sqrt(1+exp(-ell c_j))/(c_j^2+k_n^2).

The minus sign is common to every odd mode. Products therefore give
exactly (9), with alpha_n=sqrt(2)nu_n and zero opposite-parity
entries. The n=0 normalization is nu_0=ell^(-1/2), not sqrt(2/ell).
This verifies both the factor of two and the retained single-cell
j=0 response. The boundedness argument in Section3 is valid on
both parity spaces: 1/(1-exp(-2u))<=1+1/(2u) for u>0, and the
weighted Carleman integral is at most pi. The resulting bounded
positive S suffices for the diagonal closed-form extension. Equality
is needed only on original compact smooth profiles; no claim that
the finite cosine vectors lie in the causal generator domain is used.

For the complex cross pairing, polarize the unconditional L742(9)
or (10), with the first slot linear. On the separated supports its
continuous part is -sum_(j>=0) integral integral
f(y)conjugate(f(x)) exp[-c_j(M+x-y)]dy dx. The j=0 summand and
the pole terms factor into the two exact moments and vanish.
The surviving operator is exactly (1), with neither a conjugation
nor an extra factor of two. Its finite-delay contribution has
coefficient -a_n, as Section1 states. This uses no RH-conditional
conclusion of L742 or positive-zero representation.

The scalar replay independently re-enumerated every prime power,
checked all event orders and active sets on all seventeen intervals,
and reproduced the complete stored certificate exactly. In particular
R+kappa<4.702005361 and the entire complementary floor exceeds
1.4342765416>1.43. The bound uses L744(8) at k_n>1 and the increasing
lower comparison log(n/(2ell))-2ell^2/(9n^2); it does not require
monotonicity of h. All scalar ln and sqrt calls use ROUND_HALF_EVEN
followed by neighboring-value widening; directed basic operations
use their own explicit 60-digit contexts. No context-rounding
assumption is made about Decimal ln itself.

For the Schur step, D has no P-Q block, W_theta is bounded, and
the positive lower floor applies on the full complementary form
domain. The square completion (7) is therefore legitimate there.
All six terms in (8) are necessary. Their complete payment and
the all-phase conclusion are audited in C744w Section7. Audit
artifacts and reproduction commands are specified there. This
establishes the interface under its stated analytic and arithmetic
inputs; it creates no all-separation or RH implication.

## Mathlib

Full matching coverage for the localized Weil response identity,
the separation-seven comparison and this complete Schur interface
has not been checked. No Mathlib theorem is asserted to cover them.
Plancherel, elementary integration, bounded-operator Cauchy--Schwarz
and the finite Schur completion are supporting mathematics, not a
formalized proof of the desired positivity or RH.
