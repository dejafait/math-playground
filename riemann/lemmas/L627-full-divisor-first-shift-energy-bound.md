# Lemma 627: a first-shift energy bound in the full divisor Gram space

## Hypotheses

Let N>=2 be an integer, M=log N, P_N the primes at most N and S_N
the positive integers supported on P_N. Let a=(a_n)_(n<=N) be arbitrary
complex coefficients. Use L623's full Gram matrix G_N and constant C_N,
and L624's shifted convolution and analytic normalization:

    A_(u,v)(a;r)=sum_(n<=N,n|r) a_n sigma_(u,v)(r/n)/sqrt(r/n),
    sigma_(u,v)(k)=sum_(de=k) d^(-u)e^(-v),
    D_p(q)=sum_(j>=0) sigma_(alpha,beta)(p^j)
                         sigma_(gamma,delta)(p^j)/p^j,
    C_N(q)=product_(p<=N)D_p(q)^(-1),   C_N=C_N(0),
    B_N(q;a)=C_N(q) sum_(r in S_N)
                 A_(alpha,beta)(a;r) A_(gamma,delta)(conjugate(a);r).

The shifts are complex with |Re q_j|<1/4. There is no conjugation
of shift variables. Derivatives below are evaluated at zero shifts.
The coefficient vector is fixed during differentiation. The sum in
B_N is over all of S_N, including r>N.

For the comparison with the approved research target only, put L=log T
and N=floor(T^(1/100)). The signed six-term matrix and common observer
are those of L622/L624. No sign for that matrix is assumed or concluded.

The finite-prime coefficient/torus isometry used below is the finite
variable case of H. Hedenmalm, P. Lindqvist and K. Seip, *A Hilbert
space of Dirichlet series and systems of dilated functions in L2(0,1)*,
Duke Math. J. 86 (1997), 1–37, [arXiv:math/9512211v1, Section 2.2,
(2-7), Lemma 2.3, pp. 7–9](https://arxiv.org/pdf/math/9512211#page=7).
Here the coordinates are the exponents of the finitely many primes
in P_N, with normalized product Haar measure; square summability is
exactly that in L623/L624. Only this isometry is imported. The cited
multiplier theorem does not supply the restricted norm estimate below.
The rational basis calculations give explicit constants for this
particular weighted image; no general Hardy multiplier or Bernstein
theorem is reproved, and no originality claim is made.

## Conclusion

For either of the two shifts in A, there is a full-tail estimate

    C_N sum_(r in S_N) |partial_u A_(u,v)(a;r)|_(0,0)^2
        <= (8 log N+16)^2 a^*G_N a.                         (1)

For each j in {alpha,beta,gamma,delta}, the normalized arithmetic
form satisfies

    |partial_j B_N(0;a)|
        <= ((16/3)log N+10) a^*G_N a.                      (2)

Consequently the square-root bound in (1), divided by L, is at most
2/25+16/L, and the relative bound in (2), divided by L, is at most
4/75+10/L. These are bounds for the first derivatives at zero.
They apply also to the first microscopic b-derivatives, whose shift
coefficients are +/-i/L. The case N=1 has zero arithmetic derivatives
and can be included separately.

This is a local intermediate energy input, not the desired inequality

    |a^*(K_c-B(c)G_N)a| <= (B(c)/2) a^*G_N a.

In particular, (1) cannot be iterated on its output: multiplication
by the first-shift operator generally leaves the finite-input image.
No second, third or fourth mixed derivative bound, complex-neighborhood
bound, six-term signed estimate, phase budget, pointwise Xi sign or
RH conclusion follows here. The result has not received a separate
critical audit. The reused literature search did not establish an
exact matching result; that is not evidence of novelty.

## Proof

### 1. The full image and its first derivative

Write z^n=product_(p<=N) z_p^(v_p(n)), a monomial notation, and put

    P(z)=sum_(n<=N)a_n z^n,
    F(z)=product_(p<=N)(1-z_p/sqrt(p))^(-2),
    f(z)=sqrt(C_N) F(z)P(z).

The coefficient of z^r in FP is A_(0,0)(a;r). The torus isometry
and L623 (1) therefore give ||f||_2^2=a^*G_N a, with the entire
infinite coefficient sequence retained. The finite product F is
bounded and analytic on a neighborhood of the closed polydisc.

For shifted convolution replace each local factor of F by

    [(1-p^(-1/2-u)z_p)(1-p^(-1/2-v)z_p)]^(-1).

On compact subsets of the stated shift domain these products and
their derivatives are bounded on the torus. Equivalently, L624's
compact-shift square-summability argument applies. Differentiation
at zero in either shift thus multiplies FP by -H, where

    H(z)=sum_(p<=N)(log p) H_p(z_p),
    H_p(z)=t z/(1-tz),          t=p^(-1/2).                (3)

Thus the left side of (1) is ||Hf||_2^2. At fixed N the multiplier
is bounded; its unrestricted supremum grows with N and is not used
to obtain a uniform logarithmic-degree estimate.

### 2. An orthonormal basis adapted to the full image

Fix one prime, put x=t^2 and define

    C=(1-x)^3/(1+x),   rho=2t/(1+x),   s=(1-x)/(1+x).

For the probability measure C|1-tz|^(-4)dm(z) on the unit circle,
the following polynomials are orthonormal:

    phi_0=1,
    phi_1=(z-rho)/s,
    phi_k=z^(k-2)(z-t)^2/sqrt(C),              k>=2.

Here is a verification including the boundary degrees. The geometric
series gives integral |1-tz|^(-4)dm=(1+x)/(1-x)^3 and the normalized
first moment rho=2t/(1+x); the latter is L623's e=1 autocorrelation.
Thus ||phi_1||^2=(1-rho^2)/s^2=1 and phi_1 is orthogonal to phi_0.
After multiplication by sqrt(C)/(1-tz)^2, the corresponding unit
vectors in unweighted H2 are

    f_0=sqrt(C)/(1-tz)^2,
    f_1=sqrt(C)(z-rho)/[s(1-tz)^2],
    f_k=z^(k-2)[(z-t)/(1-tz)]^2,              k>=2.       (4)

The bracket has modulus one on the circle. Hence the vectors with
k>=2 are mutually orthonormal. Their products with conjugate(f_0)
and conjugate(f_1), respectively, are

    sqrt(C) z^k/(1-tz)^2,
    [sqrt(C)/s] z^(k-1)(1-rho z)/(1-tz)^2.

These are analytic functions with zero constant term for k>=2,
so their integrals vanish. This proves every claimed orthogonality.

Tensor the local vectors (4) over P_N, and denote the resulting
orthonormal vector indexed by n in S_N by f_n. Each tensor polynomial
product phi_(v_p(n)) has a nonzero leading monomial z^n and only
proper-divisor monomials below it. Divisors of n<=N are still <=N.
Triangular inversion, or induction on n, therefore gives an exact
expansion

    f=sum_(n<=N) y_n f_n,        ||f||_2^2=sum_(n<=N)|y_n|^2. (5)

The restriction n<=N in (5) is a restriction in this orthonormal
basis. Each f_n itself has its full infinite coefficient tail. It
does not truncate the original r-sum.

### 3. Exact multiplier matrix, including its boundary entries

In the local basis (4), multiplication by H_p has the following
convergent expansions:

    H_p f_0 = h0 f_0 + t/(1-t^4) f_1
                  + sum_(k>=2) t^k/sqrt(1-t^4) f_k,
    H_p f_1 = -t^3/(1-t^4) f_0 + h1 f_1
                  + sum_(k>=2) t^(k-1)/sqrt(1-t^4) f_k,
    H_p f_l = sum_(j>=1)t^j f_(l+j),             l>=2,    (6)
    h0=x(2+x)/(1-x^2),       h1=x^2/(1-x^2).

These identities can be checked as rational functions, without
discarding any coefficient. For example the tails in the first two
lines are respectively

    t^2 (z-t)^2/[sqrt(1-t^4)(1-tz)^3],
    t   (z-t)^2/[sqrt(1-t^4)(1-tz)^3].

Insert (4), use sqrt(C)sqrt(1-t^4)=(1-x)^2 and
s=(1-x)/(1+x), and multiply each line by (1-tz)^3. The constant,
linear and quadratic coefficients agree. The third line is the
geometric series times f_l. Their series converge in H2 since t<1
and the f_k are orthonormal.

Since t^4<=1/4, all raising entries in (6), from l to k>l, are
nonnegative and at most (4/3)t^(k-l). There is exactly one lowering
entry, from degree 1 to degree 0, equal to -t^3/(1-t^4).
The diagonal entries are h0,h1,0,0,..., all nonnegative, with
h1<=h0<=2/(p-1).

Write the global H as D+R+E according to these diagonal, raising
and lowering entries, including the log p factor in (3). Put

    S1=sum_(p<=N) log p/(p-1),
    S2=sum_(p<=N) (log p)^2 p/(p-1)^2,
    S3=sum_(p<=N) (log p)p^(-3/2)/(1-p^(-2)).

Then ||D||<=2S1. Each local lowering map has norm one before its
displayed scalar coefficient, so the triangle inequality gives
||E||<=S3, also on the full tensor space.

### 4. The raising estimate retains every output coordinate

Apply R to (5). Its coordinate at m in S_N is a sum over pairs
(p,j), j>=1, with n=m/p^j<=N an integer. Its summand has the form

    theta_(m,n) (log p) p^(-j/2) y_n,
    0<=theta_(m,n)<=4/3.

Weighted Cauchy--Schwarz, and the identity
sum_(p^j|m, j>=1)log p=log m, yield

    |(Ry)_m|^2 <= (16/9)(log m)
          sum_(p^j|m, m/p^j<=N) (log p)p^(-j)|y_(m/p^j)|^2.

For m=1 the sum is empty. Sum this inequality over all m in S_N.
Its nonnegative right side can be reordered by Tonelli. For each
input n<=N the resulting inner sum is

    sum_(p<=N,j>=1)(log p)p^(-j) log(np^j)
        = (log n)S1+S2.

All these sums are finite, by the geometric series and the finite
prime set. No cutoff m<=N was inserted. Hence

    ||Rf||_2 <= (4/3)sqrt(M S1+S2)||f||_2,
    ||Hf||_2 <= [2S1+(4/3)sqrt(M S1+S2)+S3]||f||_2.     (7)

### 5. Elementary constants, without a prime-distribution input

For p^j<=N, floor(N/p^j)>=N/(2p^j). Unique factorization gives

    sum_(p^j<=N)(log p)/p^j
      <= (2/N)sum_(p^j<=N)(log p)floor(N/p^j)
       = (2/N)log(N!) <= 2M.

Every remaining term in S1 has j>=2, so its total is at most

    sum_(n>=2) log n/[n(n-1)]
      <= 2sum_(n>=2)log n/n^2
      <= 1+(3/2)log 2 <3.

The last inequality uses the decreasing function log t/t^2 on
[2,infinity) and its integral. Thus S1<=2M+3. Also p/(p-1)<=2
and log p<=M give S2<=2M S1. Finally

    S3 <= (4/3)sum_(n>=2)log n/n^(3/2)
        <= (4/3)[4+(5/2)log 2]/sqrt(2) <6.              (8)

For the last integral comparison log t/t^(3/2) is decreasing on
[2,infinity). The numerical inequality follows, for example, from
log 2<7/10 and sqrt(2)>7/5; the former follows from
exp(7/10)>1+7/10+49/200+343/6000>2.

Since sqrt(6M^2+9M)<=3M+3, (7)–(8) imply

    ||Hf||_2 <= [4M+12+(4/3)sqrt(6M^2+9M)]||f||_2
              <= (8M+16)||f||_2.

Together with (3) and the isometry this proves (1).

### 6. The analytic normalization and all four first scalar jets

L624 (5), or direct differentiation of its convergent local sum,
gives for each j in {alpha,beta,gamma,delta}

    partial_j log C_N(0)=mu_N,
    mu_N=sum_(p<=N)(log p)h0(p).                          (9)

For example partial_alpha log D_p(0)
=(log p)[x^2/(1-x^2)-2x/(1-x)]=-(log p)h0. Thus (9) includes
the actual derivative of the normalization; it is not frozen.

Subtracting mu_N I from H changes only its diagonal in the basis
(5). Its diagonal at n is

    -sum_(p|n)(log p)[h0(p)-h_(v_p(n))(p)],
    h_k=0 for k>=2.

For k=1 the difference is 2x/(1-x^2)<=4/3. For k>=2 it is
h0<=2<=4k/3. Consequently this diagonal has absolute value at
most (4/3)log n, and on (5) its norm is at most (4/3)M.
The raising and lowering parts are unchanged. Therefore

    ||(H-mu_N)f||_2
      <= [(4/3)M+(4/3)sqrt(M S1+S2)+S3]||f||_2
      <= [(16/3)M+10]||f||_2.                            (10)

At zero, B_N(0;a)=||f||_2^2. Differentiating alpha or beta gives

    partial_j B_N(0;a)=mu_N||f||_2^2
                           - integral (Hf)conjugate(f) dm.

Differentiating gamma or delta gives its complex conjugate, because
the unshifted convolution and H have real coefficients. These are
holomorphic derivatives; the conjugation statement is only about
their zero-shift values. Apply Cauchy--Schwarz and (10) to obtain (2).
Since M<=L/100, the scaled bounds stated after (2) follow.

### 7. Scope of the attempt and the still missing signed estimate

The tensor coordinates in (5) and the unrestricted m-sum in Section 4
control an actual full-tail first derivative. They do not infer a
bound from an omitted boundary, or from log N/log T alone. The
normalization in (9) is also retained.

The six-term extraction D_c in L624 (8) uses derivatives through
order four at collisions, along with the pole cancellations, exact
Hardy phase and all permutations. Already Hf in (6) has arbitrarily
large basis indices. The hypothesis n<=N in (5), which is used in
(7) and (10), therefore does not hold for Hf. Applying (1) again
would be an invalid inference. Products of first derivatives and
the additional higher derivatives of the shifted multiplier likewise
need new estimates. Nothing here bounds them by powers of (8M+16).
The first-jet constants cannot be compared directly to the final
signed relative threshold 1/2. That target remains unresolved.

## Mathlib

Full matching coverage for the weighted divisor-image first-jet
estimate and its constants was not checked and is unknown. The
torus isometry is a named analytic input cited above; finite-prime
orthogonality, rational multiplier identities, full-tail summation
and explicit inequalities are proved here. No Lean proof, formal
certificate, complete signed estimate or new moment theorem is claimed.
