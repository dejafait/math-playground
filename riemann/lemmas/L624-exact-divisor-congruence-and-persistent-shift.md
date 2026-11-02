# Lemma 624: exact shifted divisor congruence and a persistent prefix deformation

## Hypotheses

Use the arithmetic factors B_hk(q), J(q), the six shift permutations,
the exact Hardy phase Phi, and the signed matrix K_c(T,X) of L622.
For the algebra below N is any positive integer. Let P_N be the primes
at most N and S_N the positive integers supported on P_N, including 1.
Let d=1*1 be the divisor function, mu the Mobius function, eta=mu*mu,
and V_N the finite inverse in L623. Dirichlet convolution is denoted
by *. Coefficients may be complex. Write

    sigma_(u,v)(n)=sum_(ab=n) a^(-u)b^(-v),
    D_p(q)=sum_(j>=0) sigma_(alpha,beta)(p^j)
                       sigma_(gamma,delta)(p^j)/p^j,
    C_N(q)=product_(p<=N) D_p(q)^(-1),
    C_N=C_N(0).

Initially assume |Re q_j|<1/4. This is more than enough for all local
series below; the application has q_j=O(1/log T). No conjugation of
the shift variables is implicit. The source for the arithmetic factors
and the complete moment is C. P. Hughes and M. P. Young, *The twisted
fourth moment of the Riemann zeta function*, J. reine angew. Math. 641
(2010), 203–236, [arXiv:0709.2345v2, (12)–(17), printed p. 4, and the
complete-sum holomorphy remark, p. 5](https://arxiv.org/pdf/0709.2345v2#page=4).
These are the previously assessed imports. The identities below are
elementary specializations of their factors, not a reproof of the
moment theorem or its holomorphy input.

In the asymptotic application put theta=1/100, L=log T,
N=floor(T^theta), and retain the fixed nonnegative smooth w, T<=X<=2T,
and the single real unit observer c of L622. Its transfer and L623 have
not received separate critical audits. No RH, zero-free region, zero
simplicity, sign of a shifted kernel or uniform spectral estimate is
assumed.

## Conclusion

For a vector xi in C^N put a=V_N xi and, for r in S_N, define

    A_(u,v)(a;r)=sum_(n<=N,n|r) a_n sigma_(u,v)(r/n)/sqrt(r/n).

There is an exact identity, with absolutely convergent right side,

    sum_(m,n<=N) a_m conjugate(a_n)
           B_(m/g,n/g)(q)/sqrt((m/g)(n/g))
      = C_N(q) sum_(r in S_N)
           A_(alpha,beta)(a;r) A_(gamma,delta)(conjugate(a);r),
    g=gcd(m,n).                                             (1)

For the first N coordinates this is a finite shifted inverse map:

    A_(u,v)(V_N xi;r)=(T_N(u,v)xi)_r,
    (T_N(u,v)xi)_r
      =sum_(j|r) xi_j (sigma_(u,v)*eta)(r/j)/sqrt(r/j),
    1<=r<=N,             T_N(0,0)=I.                       (2)

The exact formula for the remaining coordinates is (6) below. Inserting
(1) into **all six** terms gives the full congruence (8), with the
Hardy phase and all gcd multiplicities unchanged. It supplies no sign
by itself: it is generally a bilinear, rather than positive, expression,
and the signed extraction must be applied to the complete analytic sum.

In particular the finite inverse does **not** turn the shifted prefix
into I+o(1), uniformly on the permitted complex shift domain. Put

    h_N=sum_(n<=N)1/n,       xi_n=1/sqrt(n h_N),
    s=tau/L,                0<tau<=1 fixed.

Then ||xi||_2=1, a_n=mu(n)/sqrt(n h_N), and exactly

    (T_N(s,0)xi)_n=n^(-s)xi_n.                             (3)

Consequently

    ||(T_N(tau/L,0)-I)xi||_2 --> d_(theta,tau)>0,
    d_(theta,tau)^2=(1/theta) integral_0^theta
                                      (1-exp(-tau u))^2 du,
    exp(-tau theta) tau theta/sqrt(3)
          <=d_(theta,tau)<=tau theta/sqrt(3).               (4)

At tau=1 the limit is at least 99/(10000 sqrt(3)), while the
conditional transformed transfer error/C_N tends to zero as a power
of T. The two quantities are different: (4) is a lower bound for a
prefix-map deformation, **not** for a signed matrix error. It refutes
an o(1) prefix-map argument only. It does not refute
C_N^(-1)V_N^*K_c V_N >= B(c)I/2, prove a negative direction, or
control the signed infinite tail. The exact collective spectrum and
actual-Xi first-sign gap remain unresolved. This lemma is unaudited.

The later bounded Mobius specialization in Section 5 extracts the exact
real 2-by-2 common-observer matrix. A mixed arithmetic boundary jet,
even at a coordinate whose zero-shift value is zero, exceeds the L622
transfer-error scale along an unbounded sequence. This rules out a
jetwise negligible-boundary shortcut only. The signed matrix comparison
is inconclusive, and Section 5 does not assign a sign to that matrix.

## Proof

### 1. Convergence, normalization and both twist orientations

On any compact subdomain with |Re u|,|Re v|<=rho<1/4,
|sigma_(u,v)(p^j)|<=(j+1)p^(rho j). Therefore its squared modulus
times p^(-j) is summable. Products over the finite set P_N show that
each vector A_(u,v)(e_n;r), r in S_N, is square summable. Their finite
linear combinations are square summable too. Products of two such
vectors are absolutely summable by Cauchy--Schwarz, uniformly on each
compact shift set. Inserting any fixed number of shift derivatives
only adds polynomial factors in the prime exponents, leaving this
argument valid. No uniform-in-N bound is inferred from this convergence.

As in L622 (10), summing the local geometric series gives

    D_p(q)=(1-p^(-2-alpha-beta-gamma-delta))
      /[(1-p^(-1-alpha-gamma))(1-p^(-1-alpha-delta))
        (1-p^(-1-beta-gamma))(1-p^(-1-beta-delta))].         (5)

Every exponent here has positive real part on our domain, so all
factors and C_N(q) are analytic and nonzero. At q=0 this is exactly
the positive C_N in L623.

To expand the right side of (1), fix m,n and write g=gcd(m,n),
h=m/g, k=n/g. The common multiples are r=lcm(m,n)d with d in S_N.
Then r/m=kd and r/n=hd, and the reciprocal square-root factor is
1/(sqrt(hk)d). At a prime dividing h, the second divisor function
has its exponent incremented; at a prime dividing k, the first does.
At the other primes the local sum is D_p(q). Multiplying the local
sums and then C_N(q) gives exactly B_hk(q)/sqrt(hk), with the source
orientation in each case. Absolute convergence justifies the finite
coefficient expansion and the product of local series. This proves
(1), including pairs sharing a gcd and every diagonal pair.

### 2. What the finite inverse actually cancels

The explicit inverse from L623 says

    a_n=sum_(k|n) eta(k)xi_(n/k)/sqrt(k),  n<=N.

Substitute this finite sum into A_(u,v), set n=jk, and collect terms.
For every r in S_N, without a restriction r<=N, the exact result is

    A_(u,v)(V_N xi;r)
      =sum_(j<=N,j|r) xi_j/sqrt(r/j)
          sum_(k|(r/j), k<=N/j) eta(k)sigma_(u,v)(r/(jk)). (6)

When r<=N the inner bound k<=N/j is automatic, giving (2).
For r>N it is not automatic. More explicitly, extend xi by zero
outside [1,N], put t_(u,v)=sigma_(u,v)*eta, and write

    A_(u,v)(V_N xi;r)
      =sum_(j<=N,j|r) xi_j t_(u,v)(r/j)/sqrt(r/j)
       -sum_(j<=N,j|r) xi_j/sqrt(r/j)
          sum_(k|(r/j), k>N/j) eta(k)sigma_(u,v)(r/(jk)).  (7)

This is a finite identity at each r, not an assertion that either
term may be discarded in the infinite signed sum. At u=v=0,
t_(0,0)=d*eta is the convolution identity, so the first term in (7)
vanishes for r>N. The missing-divisor term is precisely the tail
left by the truncated inverse. L623 could discard its squared norm
for a positive lower bound at zero shifts; that argument supplies no
sign after the present bilinear combination and signed derivatives.

### 3. The full shifted congruence and its remaining threshold

To state the whole expression without an implicit freezing, let
q=(alpha,beta,gamma,delta) and list the six pairs (q_v,lambda_v):

    ((alpha,beta,gamma,delta),       0),
    ((-gamma,-delta,-alpha,-beta),  alpha+beta+gamma+delta),
    ((-gamma,beta,-alpha,delta),    alpha+gamma),
    ((-delta,beta,gamma,-alpha),    alpha+delta),
    ((alpha,-gamma,-beta,delta),   beta+gamma),
    ((alpha,-delta,gamma,-beta),   beta+delta).

Define

    F(q;xi)=sum_(r in S_N)
       A_(q1,q2)(V_N xi;r) A_(q3,q4)(conjugate(V_N xi);r).

For microscopic variables b=(b1,b2,b3,b4), use exactly

    q(b)=(i b1,i b2,-i b3,-i b4)/L,
    D_c=[partial_1 partial_2-(partial_1^2+partial_2^2)/2]
                             (c0+c1 partial_3)(c0+c1 partial_4).

With ell=log(t/(2pi)) and Phi(t,b) as defined in L622, equations
(1) and L622 (3)–(6) imply

    xi^*V_N^*K_c(T,X)V_N xi
      = Re D_c {1/(T L^4) integral w_XT(t) Phi(t,b)
          sum_(v=1)^6 exp(-ell lambda_v(q(b)))
               J(q_v(b)) C_N(q_v(b)) F(q_v(b);xi) dt}_(b=0).
                                                               (8)

First prove (8) at noncolliding shifts, where all six terms exist
separately. Equation (1) then identifies it with the original finite
coefficient sum exactly. The imported complete-sum holomorphy extends
that equality to collisions, where D_c is taken. No isolated pole
term has been assigned a value or differentiated at a collision.
The coefficient vector and V_N are fixed during this differentiation.
The convergence in Section 1 justifies the arithmetic bilinear sums;
it does not assert termwise positivity or replace the exact phase.

The L623 reference argument gives V_N^*G_N V_N>=C_N I. If epsilon_T
denotes the complete normalized error in L622, its error in (8) is
at most epsilon_T ||V_N xi||^2. In particular L623 gives, uniformly,

    epsilon_T ||V_N||^2/C_N
       =O_w(T^(-13/80)/L^2+T^(-97/50))=o(1).

This statement is conditional on the unaudited L622 transfer, with
its existential constants. The sought signed margin is B(c)/2,
B(c)=(28c0^2+c1^2)/(840pi^2). No bound on the signed expression
(8) minus its reference is obtained. Prefix and tail terms in (6)
are both retained and neither has been shown harmless.

### 4. A full coefficient vector with nonvanishing prefix deformation

The elementary divisor identity 1*mu=delta follows from
sum_(d|n)mu(d)=product_(p|n)(1-1) for n>1, with value 1 at n=1.
Therefore eta*1=mu, and applying V_N to the unit vector xi stated
above gives a_n=mu(n)/sqrt(n h_N). The coefficients a are nonzero
and can be normalized in the original coefficient norm if desired;
they are not being claimed as a signed witness.

Write 1_s(n)=n^(-s). Since sigma_(s,0)=1_s*1, one has
sigma_(s,0)*mu=1_s. For r<=N all divisors of r occur in A_(s,0),
so this proves (3) directly, without any asymptotic or discarded tail.
The shift is within the authorized complex domain: q=(tau/L,0,0,0)
is q(b) for b=(-i tau,0,0,0). This diagnostic evaluates only the
analytic arithmetic map, not an individual singular main term.

For completeness, put f(u)=(1-exp(-tau u))^2 and theta_N=log N/L.
The squared norm in (4) is

    (1/h_N) sum_(n<=N) f(log n/L)/n.                       (9)

We have h_N=log N+O(1), theta_N->theta, and

    sum_(n<=N) f(log n/L)/n
       = L integral_0^theta_N f(u)du + O(1).

Indeed, for F(x)=f(log x/L)/x the derivative is
[f'(log x/L)/L-f(log x/L)]/x^2. Its absolute integral on [1,N]
is bounded independently of T, since f and f' are bounded on a
fixed compact interval containing [0,theta_N]. Comparing each
unit interval with its left endpoint proves the displayed sum–integral
error, including the bounded last endpoint. Dividing by h_N proves
the limit in (4). For 0<=u<=theta,

    exp(-tau theta) tau u <=1-exp(-tau u)<=tau u.

Integrating their squares proves both stated bounds. At theta=1/100,
tau=1, exp(-1/100)>=99/100 gives the explicit positive lower bound.

The first scaled derivative also persists: differentiating the exact
finite identity (3) at s=0 gives

    ||L^(-1) (partial_s T_N)(0,0)xi||^2
        =sum_(n<=N)(log n/L)^2/(n h_N) --> theta^2/3.

Thus even the normalized first-jet map is not uniformly vanishing.
This is a coefficient-correlated statement after the finite inverse,
distinct from L623's single-factor long-prime-power example. It stops
the attempted estimate sup ||T_N(u,v)-I||=o(1) on the fixed microscopic
shift domain. A fixed small deformation could still be compatible with
a positive signed margin, and other terms could cancel it. Formula (9)
proves no lower bound on ||K_c-B(c)G_N|| and no negative eigenvalue.
No enlargement of the allowed observer family is used.

### 5. Bounded Mobius specialization: exact matrix and unresolved boundary

Retain all application hypotheses above and set

    m_N^2=sum_(n<=N) mu(n)^2/n,
    a_n=mu(n)/(sqrt(n) m_N).

The n=1 term gives m_N>=1, and sum |a_n|^2=1 exactly. The
coefficients are real and held fixed during shift differentiation.
Define the unnormalized finite convolution

    b_N(u,v;r)=sum_(d|r,d<=N) mu(d) sigma_(u,v)(r/d),
    b(u,v;r)=(mu*sigma_(u,v))(r),
    e_N(u,v;r)=sum_(d|r,d>N) mu(d) sigma_(u,v)(r/d).

For every r in S_N, b_N=b-e_N exactly, and

    A_(u,v)(a;r)=b_N(u,v;r)/(m_N sqrt(r)).                 (10)

For r<=N one has e_N=0. For r>N it is kept. Each divisor sum is
finite. The square-summability and locally uniform differentiated
convergence in Section 1 apply to (10); no uniform bound in N follows.
In particular the analytic arithmetic factor is

    F_N(q)=1/m_N^2 sum_(r in S_N)
                b_N(q1,q2;r) b_N(q3,q4;r)/r.             (11)

Split it as F_N=F_N^pre+F_N^tail by r<=N and r>N. This is an
exact identity of locally holomorphic functions near q=0. Neither
piece is evaluated as a single singular main term.

For any of these three functions F define the six-term transform

    H_F(b)=1/(T L^4) integral w_XT(t) Phi(t,b)
        sum_(v=1)^6 exp(-ell lambda_v(q(b)))
                         J(q_v(b)) C_N(q_v(b)) F(q_v(b)) dt. (12)

All six permutations, the original ell=log(t/(2pi)), and the exact
Phi are those in Section 3. In particular (12) includes the cutoff
correction in every permuted term, rather than only the first term.

Here each split in (12) also has removable shift collisions. The
imported full-sum statement alone does not identify removable values
for this truncated arithmetic split, so the following residue check
justifies its separate differentiation. Set z=(alpha,beta,-gamma,-delta).
The six terms are indexed by subsets I of {1,2,3,4} of size 2, with
q_I=(z_i,z_j,-z_k,-z_l), where I={i,j} and I^c={k,l}. Their exponential
is exp(ell(sum_(i in I)z_i-z_1-z_2)). Each summand's only possible
poles in a sufficiently small fixed neighborhood of zero come from

    product_(i in I,j in I^c) zeta(1+z_i-z_j).

Indeed 1/zeta(2+sum q_I) is analytic there, C_N is analytic, and
F is analytic by (11). The neighborhood can be chosen so that zeta
has no zero near 2 and its only pole near 1 is its simple pole at 1.
Multiplying each zeta factor by its argument difference removes that
pole. C_N F and the remaining factors are symmetric under reordering
the two entries in each of I and I^c.

At a generic collision z_i=z_j, a term with i in I and j outside I
pairs with I'=(I\{i}) union {j}. The other variables are distinct.
The analytic numerators coincide on this hyperplane, including the
exponential, while the factors z_i-z_j and z_j-z_i have opposite
residues. The residues cancel. Terms with i,j on the same side have
no such pole. Multiply the whole sum by the Vandermonde product
Delta(z)=product_(i<j)(z_i-z_j). Every summand is then analytic, and
the resulting numerator vanishes on every collision hyperplane by
the generic-residue calculation and analytic continuation. Successive
division by these distinct linear factors shows divisibility by
Delta, including at intersections: after dividing by one factor,
vanishing on any other persists off their intersection, hence on the
whole other hyperplane by continuity. Thus the quotient is analytic
also at multiple collisions. This proves removability for the prefix,
tail and full sum. It proves no quantitative bound on them.

Write H_mu=H_(F_N), and retain Q from Section 3. The exact real
symmetric observer matrix is

    R00=Re (Q H_mu)(0),
    R01=R10=(1/2) Re (Q (partial_3+partial_4) H_mu)(0),
    R11=Re (Q partial_3 partial_4 H_mu)(0).                (13)

Expanding (c0+c1 partial_3)(c0+c1 partial_4) gives
c^t R c=a^*K_c a for every real c, by L622 (6) and (1) above.
Linearity and the proved removability also give exactly
R=R^pre+R^tail, with both matrices extracted by (13) from (12).
No sign for either matrix has been inferred from the arithmetic
Gram representation. In particular the prefix is not substituted
for R in this identity.

Let B_mu denote the actual real symmetric matrix whose quadratic
form is integral w_XT W |M|^2 U_c^2/(T L^6). Then L622 (1),
uniformly over the unit real observer, implies

    ||B_mu-R||_op <= epsilon_T,
    epsilon_T=C_w[T^(-17/80)/L^4+T^(-199/100)/L^2].       (14)

For a real symmetric 2-by-2 matrix, its operator norm is the maximum
absolute quadratic form over real unit vectors, which justifies (14).
Thus the required test is lambda_min(R)<-epsilon_T for a negative
direction, or lambda_min(R)>epsilon_T uniformly in X for a positive
conclusion for this fixed coefficient vector. Neither is proved.
The constants and onset in (14) remain existential, and its analytic
inputs retain L622's unaudited qualifications.

One explicit boundary calculation explains why the zero-shift prefix
cannot close this extraction by a negligible-jet claim. Take any odd
prime p, T=p^100 and N=p; such T are unbounded by Euclid's theorem.
Then r=2p is in S_N, lies above N, and all its proper divisors
1,2,p lie at most N. Its only omitted divisor is 2p, with mu(2p)=1.
The identity mu*sigma_(u,0)=1_u gives exactly

    b_N(u,0;2p)=(2p)^(-u)-1,
    b_N(0,0;2p)=0,
    partial_u b_N(0,0;2p)=-log(2p).                     (15)

In particular this coordinate contributes nothing to the zero-shift
tail Gram norm, but it contributes to the mixed derivative of (11):

    (partial_alpha partial_gamma F_N^tail)(0)
       =1/m_N^2 sum_(r in S_N,r>N)
                       [partial_u b_N(0,0;r)]^2/r
       >= [log(2p)]^2/(2p m_N^2).                       (16)

All summands in this particular derivative are real and nonnegative.
Differentiation through the sum is justified by Section 1's local
square-summability with logarithmic factors, or its resulting locally
uniform holomorphic convergence. This is an arithmetic derivative,
not a derivative of an isolated J term at a pole.

For comparison with the known transfer scale, define the nonnegative
raw jet benchmark E_N=C_N L^(-2)
(partial_alpha partial_gamma F_N^tail)(0). The C_N here is held at
zero shifts; E_N is not the derivative of C_N(q)F_N^tail(q).
L623 (9) gives C_N>=2/[p^3(p+1)]. Also
m_N^2<=sum_(n<=p)1/n<=1+log p and log(2p)/L>=1/100. Hence

    E_N >= 1/[10000 p^4(p+1)(1+log p)].                 (17)

At the same T, (14)'s bound is

    epsilon_(p^100)=C_w[p^(-85/4)/(100 log p)^4
                              +p^(-199)/(100 log p)^2]. (18)

For any fixed positive C_w the lower bound in (17) divided by
(18) tends to infinity; for example its ratio to the first term
has growth comparable to p^(65/4)(log p)^3. The second term is
smaller eventually. Therefore a proposed term-by-term arithmetic
boundary-jet budget E_N<=epsilon_T is false even on this subsequence.
No prime-distribution estimate is required. The inequalities are
elementary specializations, not new estimates for Mobius cancellation.

This obstruction is deliberately narrower than the missing sign.
E_N omits the differentiated C_N, the four zeta pole factors, their
six-term collision cancellations, the exponential, the Hardy phase,
and the other derivatives in Q and the observer. It is neither an
entry nor a lower bound for ||R^tail||. Those omitted operations
are all retained in (12)-(13); their cancellations may change size
and sign. Thus (17) does not lower-bound the final signed boundary,
give a negative eigenvalue, or contradict a positive matrix margin.
The bounded Mobius attempt ends without a signed estimate for
R^tail or R. The first unresolved cost is precisely that complete
boundary extraction, and the specialization is stopped as inconclusive.

## Mathlib

Full matching coverage for this shifted arithmetic congruence, its
boundary formula, persistent normalized-log deformation and Section 5's
observer extraction and raw boundary-jet obstruction has
not been checked and is unknown. The finite convolution identities,
absolute convergence and integral comparison are proved above as
informal mathematics. Hughes–Young and its complete-sum holomorphy
remain named imports; their manuscript proofs are not audited here.
There is no numerical matrix certificate or claimed RH candidate.
