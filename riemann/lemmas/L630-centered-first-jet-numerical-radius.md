# Lemma 630: a constant-2 bound for the centered compressed first jet

## Hypotheses

Let N>=2 be an integer and let a=(a_n)_(1<=n<=N) be arbitrary complex
coefficients, held fixed during shift differentiation. Use precisely
L623's full Gram matrix and L624's analytic arithmetic form:

    G_N(m,n)=product_p r_p(|v_p(m)-v_p(n)|),
    r_p(e)=p^(-e/2)(1+e(p-1)/(p+1)),
    Gamma=a^*G_N a,
    A_(u,v)(a;r)=sum_(n<=N,n|r) a_n sigma_(u,v)(r/n)/sqrt(r/n),
    sigma_(u,v)(k)=sum_(de=k) d^(-u)e^(-v),
    D_p(q)=sum_(j>=0) sigma_(alpha,beta)(p^j)
                         sigma_(gamma,delta)(p^j)/p^j,
    C_N(q)=product_(p<=N)D_p(q)^(-1),
    B_N(q;a)=C_N(q) sum_(r in S_N)
                 A_(alpha,beta)(a;r) A_(gamma,delta)(conjugate(a);r).

Here q=(alpha,beta,gamma,delta), |Re q_j|<1/4, and S_N is the set
of positive integers supported on primes <=N. There is no conjugation
of shifts. Every coordinate r in S_N is included, also when r>N.
The sum and its derivatives converge locally uniformly as in L624.

Use L627's orthonormal rational tensor basis and exact multiplier
identities (4)–(6), with the centering (9). The exact identities used
here are independently replayed in Section 5; this does not audit
the other conclusions of those lemmas. The only Hilbert
space identification involved is the finite-prime coefficient/torus
isometry cited there from H. Hedenmalm, P. Lindqvist and K. Seip,
*A Hilbert space of Dirichlet series and systems of dilated functions
in L2(0,1)*, Duke Math. J. 86 (1997), 1–37,
[arXiv:math/9512211v1, Section 2.2, (2-7), Lemma 2.3, pp. 7–9](https://arxiv.org/pdf/math/9512211v1#page=7).
The existing source comparison is reused. No nilpotency, real-axis
attainment of a numerical radius, real coefficient restriction,
zero-free region, zero simplicity or Xi sign is assumed.

For the downstream comparison only, use L629's finite signed
reduction with L=log T, N=floor(T^(1/100))>=2 and observer c=(0,1).
This retains that lemma's independent audit qualifications and the
Hughes–Young/phase/holomorphy inputs specified there. Those analytic
inputs are not needed for the first-jet inequality itself.

## Conclusion

There is one explicit absolute additive constant, namely 6, such that

    |partial_alpha B_N(0;a)| <= (2 log N+6) Gamma.          (1)

Equivalently, if Pi_N is projection onto L627's rational basis vectors
indexed by n<=N, H is its multiplier and mu_N its centering, then

    w(Pi_N(H-mu_N I)Pi_N |_(range Pi_N)) <= 2 log N+6.    (2)

The numerical radius is the supremum of the modulus of the scalar
quadratic form over complex unit vectors. No restriction to real
vectors or a selected numerical-range angle is made.

In L629 (3), the absolute relative cost of the complete arithmetic
degree-one term for c=(0,1) is consequently at most

    8/25+96/L.                                          (3)

This improves that single cost from 64/75+160/L. It does not bound
degrees two through eight, the total signed comparison, other observer
directions or pointwise Xi signs. In particular it is not a proof
of the required total half-budget or of RH. The result is a local
weighted quadratic-form specialization, critically replayed on 1 November 2026;
the bounded literature comparison did not certify originality.

## Proof

### 1. Exact scalar compression and the centered entries

Put M=log N. In L627's notation,

    f=sqrt(C_N(0)) product_(p<=N)(1-z_p/sqrt(p))^(-2)
                                             sum_(n<=N)a_n z^n
     =sum_(n<=N)y_n f_n,
    ||f||_2^2=sum_(n<=N)|y_n|^2=Gamma.

Here z^n denotes product_p z_p^(v_p(n)); it is not a one-variable
power. L627 (4)–(5) proves the basis expansion by a triangular
change of polynomials supported on divisors. Each f_n retains its
full infinite coefficient tail. Let the inner product be linear in
the first argument. L627 (9) and the subsequent derivative identity give

    partial_alpha B_N(0;a)=mu_N||f||_2^2-<Hf,f>
                          =-<Ky,y>,
    K=Pi_N(H-mu_N I)Pi_N |_(range Pi_N).                 (4)

Projection is valid because the second vector f lies in range Pi_N.
It deletes only orthogonal output from this one scalar product; it
does not truncate the original divisor-coordinate sum. We do not
apply a compression identity to a product of operators.

Write K=D+R+E for its centered diagonal, strictly raising part and
exceptional lowering part. At a prime p put x=1/p, t=p^(-1/2) and

    h0=x(2+x)/(1-x^2),   h1=x^2/(1-x^2),   h_k=0 (k>=2).

L627 (6)/(9) gives the exact centered diagonal

    D_nn=-sum_(p|n)(log p)[h0-h_(v_p(n))].

For v_p(n)=1 its bracket equals 2x/(1-x^2)<=4/3, since 0<x<=1/2.
For k=v_p(n)>=2 it is h0<=2/(p-1)<=2<=4k/3. Therefore

    |D_nn| <= (4/3)log n.                               (5)

The nonzero raising entries have m=n p^j<=N, j>=1, and

    R_mn=(log p)p^(-j/2) theta_(p,v_p(n),j),
    theta_(p,0,1)=1/(1-p^(-2)),
    theta_(p,0,j)=1/sqrt(1-p^(-2))             (j>=2),
    theta_(p,1,j)=1/sqrt(1-p^(-2))             (j>=1),
    theta_(p,k,j)=1                            (k>=2,j>=1).

In every case 0<theta<=4/3. All boundary coefficients in L627
are retained: the 0-to-1 coefficient is distinguished from the
other raising coefficients, and the sole lowering coefficient is

    E_(n/p,n)=-(log p)p^(-3/2)/(1-p^(-2))
                         when v_p(n)=1.                (6)

For a fixed p, the map from n with v_p(n)=1 to n/p is injective
on orthonormal basis vectors and stays within indices <=N. It is
a partial isometry of norm at most one. Consequently

    ||E|| <= sum_(p<=N)(log p)p^(-3/2)/(1-p^(-2)) <6.   (7)

For completeness the absolute constant requires no prime-distribution
theorem: its left side is at most

    (4/3)sum_(n>=2)(log n)n^(-3/2)
       <= (4/3)[4+(5/2)log 2]/sqrt(2)
       < 115/21 <6.

The sum is bounded by its n=2 term plus the integral from 2 to infinity;
log x/x^(3/2) decreases there because log 2>2/3. One elementary
verification is that log x-2(x-1)/(x+1) has derivative
(x-1)^2/[x(x+1)^2]>0 for x>1. The last displayed strict bound uses
log 2<7/10 and sqrt(2)>7/5; the former follows from the first four
terms of exp(7/10), whose sum exceeds 2. Thus (7) also verifies
the inherited constant directly without an uncontrolled tail.

### 2. A finite prime-power sum

For every real X>=1 set

    Q(X)=sum_(p^j<=X,j>=1)(log p)/p^j.

Then

    Q(X)<=2 log X.                                      (8)

If 1<=X<2 the sum is empty. Otherwise put K0=floor X>=2.
Every summation denominator p^j is an integer <=K0. For u>=1,
floor u>=u/2, so

    Q(X)<= (2/K0)sum_(p^j<=K0)(log p)floor(K0/p^j)
          =(2/K0)log(K0!)<=2 log K0<=2 log X.

The equality is unique factorization applied to the finite product
K0!: the exponent of p equals sum_(j>=1)floor(K0/p^j).
This is a finite sum, not an estimate for an omitted infinite tail.
The factorial argument is the finite part of L627 Section 5; here
there is no need to extend it to prime powers beyond X.

### 3. Weighted scalar estimate, including complex directions

For n<=N let v_n=n^(-1/2)>0. For each m=n p^j<=N, the elementary
inequality 2uv<=u^2+v^2 implies

    |y_m||y_n| <= (1/2)[(v_n/v_m)|y_m|^2
                                      +(v_m/v_n)|y_n|^2].

Since all R_mn are nonnegative, the complex triangle inequality gives

    |<Ry,y>| <= sum_(m>n)R_mn |y_n||y_m|
       <= (1/2)sum_(k<=N)|y_k|^2
             [sum_(n<k)R_kn v_n/v_k + sum_(m>k)R_mk v_m/v_k].

The incoming row at k is bounded by

    sum_(n<k)R_kn v_n/v_k
       <= (4/3)sum_(p^j|k,j>=1)log p
        = (4/3)log k.

Indeed v_(k/p^j)/v_k=p^(j/2), cancelling the reciprocal square-root
in R_kn. All proper-divisor indices are still <=N. The outgoing
row at k instead has v_(kp^j)/v_k=p^(-j/2), and therefore

    sum_(m>k)R_mk v_m/v_k
       <= (4/3)sum_(p^j<=N/k)(log p)/p^j
        <= (8/3)log(N/k),

by (8). Its cutoff is N/k, including when N/k<2 and the sum vanishes.
It follows that

    |<Ry,y>| <= sum_(k<=N)
         [(2/3)log k+(4/3)log(N/k)]|y_k|^2.              (9)

This weighted quadratic estimate is the elementary Schur argument
specialized to these exact entries. The proof above makes both row
orientations explicit. It does not require a theorem identifying
the numerical range with its real-axis section.

Combining (5), (7) and (9) now yields

    |<Ky,y>| <= sum_(k<=N)
           [2 log k+(4/3)log(N/k)]|y_k|^2 +6||y||^2
       = sum_(k<=N)[(4/3)M+(2/3)log k]|y_k|^2+6||y||^2
       <= (2M+6)||y||^2.

Every inequality is valid for arbitrary complex y. By (4) this proves
(1) and (2), including a=0 without division by Gamma. The constant
is independent of N, of the vector and of the numerical-range angle.

### 4. The exact downstream scope

For c=(0,1), L629 (3) identifies the degree-one contribution divided
by B(c)Gamma as 16 Re h/Gamma, where
h=partial_alpha B_N(0;a)/L. For Gamma>0, (1) therefore gives

    |16 Re h/Gamma| <= 16(2 log N+6)/L
                    <= 8/25+96/L.

L623's positive Gram identity, or the invertible triangular basis
change above, ensures Gamma>0 for a nonzero vector; the zero vector
is trivial. This proves (3). The reduction in L629 and its relative
O(1/L) analytic error remain as stated there. No estimate of the
other arithmetic degrees or of their signed sum is inserted here.

### 5. Independent audit of the exact inputs and constants

The 1 November 2026 replay verifies precisely (1)–(3), including the
following load-bearing parts of L623/L624/L627. It does not certify
their other conclusions or L629's finite-jet reduction.

For L623 (1), write x=1/p. The prime scalar product at exponent
difference e is

    p^(-e/2) sum_(j>=0)(j+1)(j+e+1)x^j
      =p^(-e/2)[(1+x)/(1-x)^3+e/(1-x)^2].

Dividing by (1+x)/(1-x)^3 gives exactly r_p(e). These
nonnegative series factor over the finite prime set. Every shifted
coefficient vector is square summable; the N-term complex expansion
of its norm is absolutely justified by Cauchy–Schwarz. This verifies
the full Gram identity, including all coordinates above N.

On compact shift domains |Re q_j|<=rho<1/4 the prime coefficients
are bounded by (j+1)p^(rho j); any fixed derivative adds only a
polynomial in j. Their squared coefficients after p^(-j) have a
convergent geometric majorant. Taking finitely many prime products
and finitely many input vectors justifies the bilinear products,
local uniform convergence and differentiation in L624. In its (5)
all denominator exponents have real part >1/2 and the numerator
exponent has real part >1. Thus C_N(q) is analytic and nonzero.
Direct logarithmic differentiation yields

    partial_alpha log D_p(0)
      =(log p)[x^2/(1-x^2)-2x/(1-x)]
      =-(log p)x(2+x)/(1-x^2).

This checks the sign and value of mu_N. Differentiating the first
shifted convolution vector multiplies f by -H; the second vector
at zero is conjugate(f). Consequently the inner product linear in
its first argument gives exactly (4), also for complex coefficients.

Here is a direct boundary-entry check independent of an output
cutoff. For one prime put x=t^2, u=1-x, v=1+x and c=sqrt(C),
so s=u/v, rho=2t/v and c sqrt(1-t^4)=u^2. The local rational
vectors in L627 (4) are orthonormal: the first two moments give
1-rho^2=s^2; the vectors of degree >=2 are powers of z times
the squared Blaschke factor. Their scalar products with the first
two vectors are integrals of

    c z^k/(1-tz)^2,
    (c/s) z^(k-1)(1-rho z)/(1-tz)^2,

respectively, which have zero constant coefficient for k>=2.
Their mutual scalar products reduce to those of distinct powers
of z. The finite divisor-supported triangular polynomial change
has a nonzero diagonal, so it is bijective on the input space.
In particular all complex y occur, as required by the claimed
equivalence with the numerical radius.

For H_p f_0, multiply the proposed identity by (1-tz)^3/c.
For H_p f_1, multiply it by s(1-tz)^3/c. The two identities to
check become the following polynomial equalities, with no square
roots left:

    tz = h0(1-tz)+(t/u^2)(z-rho)(1-tz)
                                      +(x/u^2)(z-t)^2,
    tz(z-rho) = -(t^3/v^2)(1-tz)
                    +(x^2/(uv))(z-rho)(1-tz)
                    +(t/(uv))(z-t)^2.

The constant, linear and quadratic coefficients on their right
sides are respectively (0,t,0) and (0,-t rho,t), equal to
the left sides. For the first equality the common denominator is
u^2 v; for the second it is uv^2, both positive. The tails used
here are the convergent geometric sums displayed in L627 (6).
For degrees >=2, H_p f_k=sum_(j>=1)t^j f_(k+j) directly by
the geometric series. Thus every raising coefficient and the
exceptional 1-to-0 lowering coefficient in (6) are checked, with
no completeness or finite-tail premise.

The scalar compression in (4) follows solely from f belonging to
the finite span. The centered diagonal subtracts the h0 contribution
at every prime, including primes not dividing n; those latter
terms cancel. The remaining diagonal is (5). For each fixed prime
the lowering map is injective on its domain of basis vectors and
has range still indexed by n<=N. Summing its operator norms gives
(7). The integral comparison there is legitimate since
1-(3/2)log x<0 for x>=2; the stated proof of log 2>2/3
verifies the endpoint. The explicit bound 115/21<6 follows from
log 2<7/10 and sqrt(2)>7/5, without a numerical prime cutoff.

Finally the weighted inequality has the coefficient of |y_m|^2
equal to v_n/v_m, and that of |y_n|^2 equal to v_m/v_n.
Hence the incoming row at k uses the full divisor sum log k,
while the outgoing row uses Q(N/k), including its empty case
N/k<2. The factorial identity in (8) is exact for floor X and
floor(floor X/p^j)>=floor X/(2p^j). Combining these two rows
with the diagonal yields (4/3)log N+(2/3)log k<=2 log N.
The complex triangle inequality, followed by the operator bound
for E, proves the full modulus estimate, rather than a selected
real numerical-range direction. This completes the universal
replay of (1) and (2). The normalization-only check of (3) uses
(6/pi^2)(1/315)/(1/(840pi^2))=16 and log N<=L/100;
it does not independently audit L629 (3).

## Mathlib

Full matching Mathlib coverage for this centered rational-tensor
compression estimate has not been checked and remains unknown. The
only named analytic import used is the finite-prime torus isometry
cited in the hypotheses; the specialized weighted quadratic estimate,
finite factorial bound and constants are justified above. No formal
certificate, new general numerical-radius theorem, audit of local
inputs beyond the exact identities in Section 5, or RH resolution is claimed.
