# Lemma 634: a uniform full-arithmetic margin from normalized prime rows

## Hypotheses

Let L tend to infinity, N=floor(exp(L/100)), M=log N, and let a be
an arbitrary vector in C^N, fixed during all shift differentiations.
Use L623's full Gram form Gamma=a^*G_N a, L624's full analytic
arithmetic form B_N(q;a), and precisely L633's finite spectral
extraction Q_(N,L), polynomial H, signed derivatives d_j, point y_*,
and divisor-triangular orthonormal change of basis V. In particular,
V^*G_N V=I and every arithmetic tail and derivative of C_N(q) is
retained. No product of finite compressed operators is substituted
for a compressed product.

The local rational orthonormal vectors and torus identification are
those of L627. Its underlying finite-prime isometry is the already
assessed input from H. Hedenmalm, P. Lindqvist and K. Seip, *A Hilbert
space of Dirichlet series and systems of dilated functions in L2(0,1)*,
Duke Math. J. 86 (1997), 1–37,
[arXiv:math/9512211v1, Section 2.2, (2-7), Lemma 2.3, pp. 7–9](https://arxiv.org/pdf/math/9512211v1#page=7).
The arithmetic specialization is of C. P. Hughes and M. P. Young,
*The twisted fourth moment of the Riemann zeta function*, J. reine
angew. Math. 641 (2010), 203–236,
[arXiv:0709.2345v2, (12)–(17), pp. 4–5](https://arxiv.org/pdf/0709.2345v2#page=4).
L633 reuses the scalar HCIZ identity of C. McSwiggen,
[arXiv:1712.03995v3, (2), Theorem 1, Section 3.4/(24)](https://arxiv.org/html/1712.03995v3).
None of those named results is reproved here or asserted to contain
the uniform signed estimate below. The existing assessment of this
exact target is reused. Section 7 records an independent conceptual
audit of this row argument, its needed basis identities and finite
spectral contraction. It does not constitute a blanket audit of
L633, the other local inputs or the external source manuscripts.

## Conclusion

Write mathsf Q for the real symmetric matrix representing Q_(N,L),
E=V^*mathsf Q V-I, and v_n=n^(-1/2). Then

    limsup_(L->infinity) max_(n<=N) sum_(m<=N)|E_nm|v_m/v_n
      <= 5590124687024429/20000000000000000
       = 0.27950623435122145 < 3/10.                       (1)

Consequently, for every sufficiently large L, uniformly over all
complex a,

    Q_(N,L)(a) >= (7/10) Gamma.                           (2)

Thus the specified averaged c=(0,1) arithmetic target has epsilon=1/5
and one existential, coefficient-independent onset. The proof gives
no numerical onset. Its relevance to L629 is that a fixed reserve
above Gamma/2 leaves room for that lemma's qualified O(Gamma/L)
transfer error. Other observers, pointwise Xi signs and the remaining
input audits are not settled. This is a proposed local advance beyond
the conclusions found in the bounded source comparison, with no
certified novelty claim and no RH resolution candidate.

## Proof

### 1. Coefficient norms and the cancellation to preserve

All series below are Taylor series at zero. For a series F in four
variables v=(v1,v2,v3,v4), write

    b_k(F)=sum_(|nu|=k) |[v^nu]F|.

This is a coefficient norm, not a value of F on a real ray.
It satisfies the triangle and convolution product inequalities.
We use coefficientwise majorization only through degree eight.
Constants denoted C_k can change between inequalities; they depend
only on the fixed integer k<=8, never on p,N,e,f or the vector.

For A=exp(-v1), B=exp(-v2), put

    S_j(A,B)=sum_(r=0)^j A^r B^(j-r),
    U_0=1,
    U_d=S_d-2S_(d-1)+S_(d-2),             d>=1,           (3)

where S_(-1)=S_(-2)=0. Their generating functions are

    sum_(d>=0) U_d z^d = (1-z)^2/((1-Az)(1-Bz))
      = (1+(A-1)z/(1-Az))(1+(B-1)z/(1-Bz)).             (4)

For d>=1 the second expression shows that all nonzero Taylor
coefficients of total degree k have sign (-1)^k. Indeed each factor
(A-1)A^r has coefficient (-1)^k((r+1)^k-r^k)/k! at v1^k,
nonnegative after that sign, and likewise for B. Products have the
same total-degree sign. Thus their exact absolute generating series is

    u_d(t):=sum_k b_k(U_d)t^k
      =(d+1)exp(dt)-2d exp((d-1)t)
                         +(d-1)exp((d-2)t),             (5)

with the last term absent at d=1. It has constant coefficient zero.
For every fixed k>=1,

    b_k(U_d)<=C_k(d+1)^(k-1),
    b_k(S_j)=(j+1)j^k/k!.                               (6)

For the first assertion, the numerator of [t^k] in (5) is the
second finite difference of (d+1)d^k, a polynomial of degree at
most k-1; d=1 is included separately. Nonnegativity was proved
by (4). These bounds retain the cancellation at zero shifts.

### 2. Exact local entries, including degrees zero and one

Fix p, x=1/p, t=sqrt(x), and v_j=(log p)q_j. In this section t
is the fixed prime parameter; the formal variable in (5) will be
renamed when used below. Put

    C=(1-x)^3/(1+x), s=(1-x)/(1+x), rho=2t/(1+x),
    f_0=sqrt(C)/(1-tz)^2,
    f_1=sqrt(C)(z-rho)/(s(1-tz)^2),
    f_e=z^(e-2)((z-t)/(1-tz))^2,             e>=2.

These are L627's full-tail orthonormal vectors. Let A=exp(-v1),
B=exp(-v2), C'=exp(-v3), D=exp(-v4), and set

    R_L(z)=(1-tz)^2/((1-tAz)(1-tBz)),
    R_R(z^-1)=(1-tz^-1)^2/((1-tC'z^-1)(1-tDz^-1)),
    kappa=D_p(0)/D_p(q)
      =[(1+x)/(1-x)^3]
        (1-xAC')(1-xAD)(1-xBC')(1-xBD)/(1-x^2ABC'D).

The normalized local entry is

    T_ef(v)=kappa integral f_e(z) conjugate(f_f(z))
                                      R_L(z)R_R(z^-1) dm(z).       (7)

This convention gives B as sum y_e conjugate(y_f)T_ef. Its extracted
real symmetric matrix is the same Hermitian quadratic form as in
L633. The conjugation in (7) concerns the fixed basis only; it never
conjugates shifts. Superscripts L,R on U or S below specify their
argument pair. All Fourier expansions converge absolutely near zero.

If e,f>=2 and e=f+d with d>=0, the Blaschke factors cancel exactly,
leaving f_e conjugate(f_f)=z^d. Hence

    T_(f+d,f)/t^d = kappa sum_(j>=0) x^j U_j^L U_(d+j)^R. (8)

The boundary formulas are different. For e>=2,

    T_e0/t^e = kappa sqrt(C) sum_(j>=0)x^j S_j^L U_(e+j)^R,
    T_e1/t^(e-1) = kappa sqrt(C)/s
         sum_(j>=0)x^j S_j^L
                        (U_(e-1+j)^R-rho t U_(e+j)^R).   (9)

To verify them directly on the circle, the corresponding unweighted
products are sqrt(C)z^e/(1-tz)^2 and
sqrt(C)z^(e-1)(1-rho z)/(s(1-tz)^2). Multiplying by R_L replaces
the denominator by (1-tAz)(1-tBz); matching opposite Fourier
exponents with R_R gives (9), including its factor rho t.

For the remaining entries put

    R1_R=(C'+D-xC'D(A+B))/(1-x^2ABC'D),
    R1_L=(A+B-xAB(C'+D))/(1-x^2ABC'D).

L633's closed exponent-one factor, or summing the geometric series,
gives

    T_00=1,
    T_10=(t R1_R-rho)/s,
    T_11=(1+rho^2-rho t(R1_R+R1_L))/s^2.                (10)

The reverse orientation follows by exchanging the L and R pairs;
this exchange preserves b_k. In particular every boundary case is
included. Formulas (8)–(10) give T_ef(0)=delta_ef and retain the
normalization kappa, including its derivatives.

### 3. Local remainder estimates with a degree loss

The following estimates hold uniformly for 0<x<=1/2. For e,f>=2,
d=|e-f|>=1, let U_d be in the orientation of (8). Then

    b_1(T_ef/t^d-U_d)=0,
    b_k(T_ef/t^d-U_d)<=C_k x(d+1)^(k-2),   2<=k<=8.     (11)

If min(e,f)<=1 and d>=1, the boundary estimate is instead

    b_k(T_ef/t^d-U_d)<=C_k x(d+1)^(k-1),   1<=k<=8.     (12)

On the diagonal, T_00=1 exactly, and

    b_k(T_ee-1)<=C_k x,                    e>=1,k>=1.    (13)

Here are uniform justifications, including the constants' dependence.
The rational formula for kappa gives kappa(0)=1 and
b_k(kappa-1)<=C_k x for every k>=1. Expand its denominator as
sum_(j>=0)x^(2j)exp(-j(v1+v2+v3+v4)); its degree-k coefficient
norm is bounded by a constant times sum j^k x^(2j). The finite
numerator has coefficients O_k(x), and (1-x)^(-3) is bounded on
0<=x<=1/2. This proves the asserted bound, including the continuous
endpoint x=0. All other scalar prefactors in (9)–(10) are bounded
on this interval; their differences from their values at x=0 are
O(x), and rho t=2x/(1+x)=O(x).

For (11), subtract U_d from (8). The term (kappa-1)U_d starts at
degree two. At degree k its bound from (6) is at most
C_k x(d+1)^(k-2). Every j>=1 summand U_j^L U_(d+j)^R also starts
at degree two. At total degree k its coefficient norm is bounded
by C_k(d+1)^(k-2)(j+1)^(k-2), using
d+j+1<=(d+1)(j+1) and the convolution inequality. The geometric
sum sum_(j>=1)x^j(j+1)^r<=C_r x is uniform for x<=1/2. Multiplying
by kappa preserves this estimate. These observations also prove the
exact vanishing at degree one, rather than merely a small bound.

For (12) with e>=2, separate j=0 in (9). The part multiplying U_d
differs from 1 by a scalar O(x) at degree zero and coefficients
O_k(x) at positive degree. Its other j=0 term has the additional
factor rho t=O(x). For j>=1 use (6): at each fixed total degree,
S_j contributes a polynomial in j, while U_(d+j) contributes at
most C_k(d+1)^(k-1) times another polynomial in j. Summing with
x^j gives C_k x(d+1)^(k-1). The case {e,f}={1,0} follows directly
from (10): after division by t, its value at x=0 is
C'+D-2=U_1^R, and the difference has coefficient bounds O_k(x)
from the displayed rational denominator. This also covers the
reverse boundary orientations.

For (13) with e>=2, (8) at d=0 is
kappa(1+sum_(j>=1)x^j U_j^L U_j^R); the same estimates give O_k(x).
For e=1, formula (10) has nonconstant coefficients multiplied by
rho t=O(x), with s>=1/3. Its zero-shift value is one. This proves
all the local estimates. They use whole convergent geometric series,
not a cutoff or an iteration of a restricted operator bound.

### 4. Full weighted rows and uniform control of the remainders

Define the local absolute row series in a formal variable h by

    S_e(h)=sum_(f>=0) t^(f-e) sum_(k>=0)b_k(T_ef)h^k.

Only its coefficients through degree eight are needed. The factor
t^(f-e) is precisely the local factor of v_m/v_n. In (11)–(12),
the additional t^d makes the weight 1 for incoming f<e and x^d
for outgoing f>e. Put

    I_e(h)=sum_(d=1)^e u_d(h),
    O_x(h)=sum_(d>=1)x^d u_d(h)
          =((1-x)/(1-x exp(h)))^2-1.

Equations (11)–(13) imply the coefficientwise bound

    S_e(h) <= 1+I_e(h)+O_x(h)+E_e(h),
    [h^k]E_e(h)=C_k(1_(e>=1)x(e+1)^(k-1)+x^2),
                                                    1<=k<=8.     (14)

Take the C_k large enough for all previous estimates and E_e(0)=0.
For incoming bulk entries, sum (d+1)^(k-2) over d<=e; this is
O_k((e+1)^(k-1)), and at degree one their remainder vanishes.
There are at most two incoming boundary entries, of the same final
order by (12). The non-vacuum diagonal is covered by (13). Outgoing
remainders have an additional x^d, so their sum is O_k(x^2), also
when e=0 or 1. The exact equality T_00=1 is essential: no O_k(x)
diagonal cost is charged at primes absent from n.

The incoming sum telescopes:

    1+I_e(h)=(e+1)exp(eh)-e exp((e-1)h) <= exp(2eh)      (15)

coefficientwise. For e=0 it is 1. For e>=1 and k>=1 its numerator
coefficient is (e+1)e^k-e(e-1)^k, bounded by (k+1)e^k<=2^k e^k;
the first inequality uses e^k-(e-1)^k<=k e^(k-1). All coefficients
of I_e and O_x are nonnegative. Therefore (14) gives

    S_e(h) <= exp(2eh)((1-x)/(1-x exp(h)))^2(1+E_e(h)).   (16)

For a row n<=N write e_p=v_p(n), and tensor (16) over p<=N with
h=(log p)z. The finite-prime torus identity gives the exact product
formula for each full shifted matrix entry. The coefficient norm
product inequality, followed by summing over all m in S_N, bounds
every absolute row coefficient by product_p S_(e_p)((log p)z).
This sum includes m>N and thus majorizes the finite row actually
needed; it never deletes an arithmetic divisor tail. Each local
weighted row coefficient is summable by the preceding geometric
bounds, so these finite-prime products and nonnegative sums are
legitimate. No product-of-compressions identity is used.

The first factor on the right of (16) tensors to exp(2z log n).
The logarithm of the second factor has coefficient at z^k equal to

    (2/k!) sum_(p<=N,j>=1) j^(k-1)(log p)^k/p^j.         (17)

For k>=1 the part j>=2 is bounded by an absolute constant depending
only on k: sum_(j>=2)j^(k-1)p^(-j)<=C_k/p^2 and
sum_(r>=2)(log r)^k/r^2<infinity. For j=1 use

    sum_(p<=N) log p/p <= 2 log N=2M.                   (18)

Indeed floor(N/p)>=N/(2p) and unique factorization of N! imply
sum_(p<=N)(log p)/p <= (2/N)log(N!)<=2 log N. Thus (17)
is at most 4M^k/k!+O_k(1). This needs no prime-distribution theorem.

The third factor in (16) is at most exp(sum_p E_(e_p)((log p)z))
coefficientwise. Its exponent, after substituting z=u/M, tends
coefficientwise to zero uniformly over n<=N. In detail, its degree-k
coefficient is bounded by

    C_k/M^k [sum_(p|n) (log p)^k(e_p+1)^(k-1)/p
                           +sum_(p<=N)(log p)^k/p^2].    (19)

For p|n, (e_p+1)log p<=2M. The first sum is bounded by
(2M)^(k-1) sum_(p|n)log p/p. Uniformly over n<=N,

    sum_(p|n)log p/p=o(M):

for any fixed R>=2 it is at most sum_(p<=R)log p/p+M/R.
First let M tend to infinity and then R to infinity. The second
sum in (19) is bounded independently of N by the convergent integer
sum just used. This proves the claimed uniform little-o estimate.

Combining (16)–(19), using log n<=M and exponentiating series with
nonnegative coefficients, yields, for 0<=k<=8,

    M^(-k) sum_(m<=N) (v_m/v_n)
       sum_(|nu|=k)|[q^nu] T_nm(q)| <= a_k+o(1),
    a_k=[u^k] exp(2u+4(exp(u)-1)),                      (20)

uniformly in the row n. The o(1) can depend on k, and there are only
eight positive degrees. This is a coefficientwise asymptotic bound,
not an asserted uniform approximation of an analytic function or a
limit interchange on a growing polydisc. At degree zero the row is
exactly the identity. All infinite sums used for its positive-degree
coefficients were bounded before taking this limit.

### 5. Contract the complete signed spectral polynomial

For a multi-index nu, let c_nu be the average of

    (-1)^(nu3+nu4) partial^nu H(y_*)

over the distinct swaps within the first pair and within the second
pair of nu. Every T_nm is symmetric within those pairs. Consequently
replacing the individual derivative values by c_nu leaves L633's
exact contraction unchanged. This symmetrization is done before
taking absolute values. The exact maxima C'_k=max_(|nu|=k)|c_nu|
and the coefficients in (20) are

    k       0  1   2    3    4     5       6          7          8
    C'_k    1  4  35/2  84  420   840     2520       2520       5040
    a_k     1  6   20  146/3 577/6 979/6  44261/180  47127/140 4287229/10080.

These are finite rational computations from the explicit four
alternants defining H in L633. The reproduction command is

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/full_gram/normalized_row_margin.py

The full certificate is
`scripts/full_gram/normalized_row_margin_certificate.json`.
It records all 495 derivatives and their distinct pair orbits,
compares all 175 orbit sums to the independent six-subset polynomial
prescription of L629, and stores every rational coefficient and cost.
For the a_k one may also use a_0=1 and
k a_k=sum_(j=1)^k j b_j a_(k-j), where b_1=6 and b_j=4/j! for j>=2.
No floating value is used in the inequalities. The finite U_d
diagnostics in that certificate supplement (3)–(6); their finite
range is not the proof of the universal identities.

By (20), L633's finite spectral extraction and M/L<=1/100,

    sum_(m<=N)|E_nm|v_m/v_n
      <= sum_(k=1)^8 C'_k (M/L)^k(a_k+o(1))
      <= sum_(k=1)^8 C'_k a_k/100^k+o(1)
       = 5590124687024429/20000000000000000+o(1),         (21)

uniformly in n. All arithmetic degrees one through eight occur in
this bound. Higher degrees contribute exactly zero by L633; no
higher-order arithmetic remainder is discarded. The rational number
in (21) is strictly less than 3/10, proving (1). Hence eventually
the weighted absolute row bound is at most 3/10. L633's weighted
Hermitian quadratic estimate gives y^*V^*mathsf Q V y>=7||y||^2/10.
Set a=Vy and use V^*G_N V=I. This proves (2) for every complex
vector, including the zero vector, with a common existential onset.

### 6. Qualifications and what this step does not resolve

The critical analytic content is the loss of one power in (11),
the separate boundary treatment (12), and the exact vacuum entry in
(10). Without these, (19) need not be o(1); a large absolute Cauchy
bound or a finite eigenvalue screen cannot replace them. This proof
uses full normalized matrix entries and their scalar Taylor
coefficients, not iterated finite first-jet operators. No positivity
of a complex shifted measure or of an HCIZ differential lift is
assumed. The uniform row bound is new local work under the ready
EXPLORE assessment, rather than an imported theorem or a rebranding
of L633's finite screen. Its independent conceptual audit remains
the next mathematical check. L629's transfer and all other unresolved
Xi sign and audit qualifications remain unchanged. The subsequent
audit in Section 7 supersedes the preceding next-check statement;
the original development and its finite certificate are preserved.

### 7. Independent conceptual audit, 1 November 2026

**Scope and outcome.** The local normalized-row proof and its finite
signed contraction pass the audit below. There is no change to (1)
or (2), no additional observer conclusion and no new inequality
claimed by this audit. Its evidence is an independent reconstruction
of the boundary and uniformity argument, together with a full
polynomial verification of the extraction. The relevant identities
from L623, L624, L627 and L633 were checked at the scope actually
used here; their unrelated estimates and external manuscript proofs
were not audited. L629's transfer is not a premise of (1) or (2).

**Normalization and local boundary cases.** For the fixed local
basis, multiplication by sqrt(C)/(1-tz)^2 sends phi_e to f_e.
The normalized torus measure in L633 is therefore exactly (7),
since its scalar relative normalization is
D_p(0)/D_p(q), not its reciprocal. At zero shifts the vectors f_e
are orthonormal: the bulk Blaschke factor has modulus one, the
products against f_0 and f_1 have zero Fourier constant term, and
1-rho^2=s^2 verifies the remaining unit norm. Divisor triangularity
then gives V^*G_N V=I on n<=N, without restricting the Fourier output.

For all e>=2, direct circle algebra gives

    f_e conjugate(f_0)=sqrt(C)z^e/(1-tz)^2,
    f_e conjugate(f_1)=sqrt(C)z^(e-1)(1-rho z)/(s(1-tz)^2).

After inserting R_L R_R, matching Fourier powers gives exactly (9):
the second numerator term requires exponent e+j on the right,
which explains the factor rho t, rather than rho or rho/t. For
e=f+d>=2 with f>=2 the corresponding product is z^d, giving (8).
The normalized zeroth moment is one for every small complex shift.
The first moments are t R1_R and t R1_L, so integrating
|z-rho|^2/s^2 gives (10). Thus neither T_00 nor its derivatives
incur an error. Swapping the two shift pairs transposes every entry;
this proves that the reverse boundary orientation has the identical
coefficient-norm bound. It does not conjugate any shift variable.

**Universal degree loss and uniformity.** Formula (4) makes every
positive-degree coefficient of U_d have its common total-degree
sign. Hence (5) is its coefficient norm, including d=1. For k>=1
the second difference of (d+1)d^k has degree at most k-1. In the
bulk, (kappa-1)U_d and each j>=1 product in (8) have at least two
positive-degree factors. For 1<=i<=k-1 their product is bounded by
a constant times

    (j+1)^(i-1)(d+j+1)^(k-i-1)
      <= (d+1)^(k-2)(j+1)^(k-2).

Summing its full geometric j-series proves (11), with identically
zero first-degree remainder. No bound is iterated on a compressed
operator. Each incoming bulk row has sum O_k(x(e+1)^(k-1)); its
first-degree contribution is zero. There are at most two incoming
boundary entries, for which (12) supplies exactly that same final
order. For outgoing entries the weight is x^d, so their O_k(x)
remainders sum to O_k(x^2), uniformly in the input degree e.
The non-vacuum diagonal is O_k(x); the vacuum diagonal is exact.
These observations verify every case of (14), including e=0,1.

All products may be taken in the cone of nonnegative series modulo
terms of degree nine. For fixed N each coefficient of the full row
sum is summable, by the geometric bounds just established. Tensoring
over the finite prime set and extending m<=N to m in S_N are
therefore justified coefficientwise by nonnegative summation.
This does not require convergence of a uniformly growing analytic
disc. The input restriction is used only in sum_p e_p log p=log n<=M.

For clarity, the actual uniform limiting estimate in (19) is, for
each fixed k>=1 and R>=2,

    sup_(n<=N) M^(-k)
      sum_(p|n)(log p)^k(e_p+1)^(k-1)/p
      <= 2^(k-1)[A_R/M+1/R],
    A_R=sum_(p<=R)log p/p.

The remaining p^(-2) contribution is O_k(M^(-k)). First let
M tend to infinity with R fixed, and then let R tend to infinity.
This proves uniform o(1); an n-dependent cutoff or onset is not
being used. The j>=2 part of (17) also has bounded coefficients.
For j=1, the factorial estimate (18) and log p<=M give the stated
4M^k/k!. Exponentiation in the finite coefficient cone is continuous,
so the product has the majorant (20), uniformly in every row. This
checks the limiting step independently of the finite diagnostic.

**Independent finite extraction and Hermitian bound.** The audit
script `scripts/full_gram/normalized_row_margin_audit.py` imports no
notebook calculation module. For each of the 175 pair-symmetric
monomials of degree at most eight, it constructs the entire
degree-ten numerator of L629 (5) with d_out=4, using the six exact
polynomials Delta/D_I. It divides that numerator by the full
Vandermonde and multiplies the quotient back to verify zero
remainder. Applying 5040(-2[2011]+[1111]) agrees with the sum of
the signed H derivatives over that monomial's pair orbit in every
case. These monomials span every admissible truncated amplitude,
so this verifies the needed finite extraction, including factorials
and the zero-degree normalization. It is a normalization audit,
not a reproof of HCIZ or the Hughes--Young moment theorem.

The same independent implementation reproduces all 495 signed
derivative entries, all degree maxima, and the majorant coefficients
by truncated exponentiation instead of the original recurrence.
It checks H(-pi y)=H(y). Together with the local pair-swap identity,
this makes the extracted real matrix symmetric; its extension to
arbitrary complex vectors is therefore Hermitian. Pair-orbit
averaging is valid before absolute values because the arithmetic
Taylor coefficient is constant on each orbit. The coefficient is
[q^nu]T, already divided by nu!; no extra factorial enters (21).

The resulting exact cost is unchanged, with positive slack

    3/10 - 5590124687024429/20000000000000000
      = 409875312975571/20000000000000000 > 0.

The uniform o(1) is eventually less than this fixed slack. The
weighted Hermitian quadratic estimate then applies simultaneously
to every vector, giving (2) with an existential common onset.
There is no passage from finite eigenvalues to an asymptotic sign.

Reproduce the finite portion from the active notebook with

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/full_gram/normalized_row_margin_audit.py

The complete evidence, including all homogeneous quotients, all
derivative comparisons, the original certificate's SHA-256 and the
exact contraction, is in
`scripts/full_gram/normalized_row_margin_audit_certificate.json`.
All 14 aggregate checks pass, with no failures. The written audit
above, rather than that finite certificate, establishes uniformity.
No effective onset, pointwise sign, other observer estimate or
external-source proof audit is added.

## Mathlib

Full matching coverage for this normalized arithmetic-row estimate,
its uniform asymptotic remainder and signed margin has not been
checked and remains unknown. The named inputs above are reused with
their local hypotheses. Geometric series, finite Fourier products,
coefficientwise inequalities and the elementary factorial bound are
proved here at the needed scope. The rational certificate checks the
finite contraction, not the infinite-row argument, external sources,
a Lean formalization or RH. The separate conceptual audit and its
independent finite algebra certificate have the limited scope stated
in Section 7; Mathlib coverage remains unchecked.
