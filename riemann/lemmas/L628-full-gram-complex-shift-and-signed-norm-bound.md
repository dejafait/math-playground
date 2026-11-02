# Lemma 628: full-Gram complex-shift and signed norm bounds

## Hypotheses

Let N>=2, M=log N, P_N={p prime: p<=N}, and S_N be the positive
integers supported on P_N. Let a=(a_n)_(n<=N) be any complex vector.
Use the full Gram matrix G_N of L623 and write Gamma=a^*G_N a.
Use the exact shifted convolution and normalization of L624:

    A_(u,v)(a;r)=sum_(n<=N,n|r) a_n sigma_(u,v)(r/n)/sqrt(r/n),
    sigma_(u,v)(k)=sum_(de=k) d^(-u)e^(-v),
    C_N(q)=product_(p<=N) D_p(q)^(-1),
    D_p(q)=(1-p^(-2-alpha-beta-gamma-delta))
       /product_(v in {alpha+gamma,alpha+delta,beta+gamma,beta+delta})
                                                     (1-p^(-1-v)),
    B_N(q;a)=C_N(q) sum_(r in S_N)
                     A_(alpha,beta)(a;r) A_(gamma,delta)(conjugate(a);r).

Here q=(alpha,beta,gamma,delta) is complex, with no conjugation of
shift variables. The coefficient vector is fixed during differentiation.
All r in S_N, including r>N, occur. Put S=sum_(j=1)^4 |q_j|.

For the signed application only, retain exactly L622's fixed w>=0 in
C_c^infinity((0,1)) with integral 1, L=log T, N=floor(T^(1/100)),
T<=X<=2T, common real unit observer c, exact phase Phi, six permutations
q_v and exponent factors lambda_v, and Hermitian matrix K_c(T,X).
There is no RH, simplicity, spacing, zero-free or sign assumption.

The torus isometry is the finite-prime case of H. Hedenmalm,
P. Lindqvist and K. Seip, *A Hilbert space of Dirichlet series and
systems of dilated functions in L2(0,1)*, Duke Math. J. 86 (1997),
1–37, [arXiv:math/9512211v1, Section 2.2/(2-7)/Lemma 2.3,
pp. 7–9](https://arxiv.org/pdf/math/9512211#page=7), as specialized
in L627. The source for the arithmetic factors and complete-sum
holomorphy is C. P. Hughes and M. P. Young, *The twisted fourth
moment of the Riemann zeta function*, J. reine angew. Math. 641
(2010), 203–236, [arXiv:0709.2345v2, Theorem 1.1/(12)–(17),
printed pp. 4–5 and the subsequent holomorphy remark](https://arxiv.org/pdf/0709.2345v2#page=4).
The audited H=T application of L619 supplies the phase asymptotic
and the untwisted normalization B(c)=(28c0^2+c1^2)/(840 pi^2),
specializing bramble_trace, *Signs and uniform filtered positivity
in fourth moments of Hardy's function*, [paper 36 v4, 21 October
2026, Theorem 6/(21)](https://rstation.ai/problems/riemann_hypothesis/papers/36).
These are reused imports; their manuscript proofs are not audited here.
The new estimates below concern the exact full divisor image and its
constants, rather than a reproof of any of those theorems.

## Conclusion

For s=|u|+|v| with sM<=1/16,

    [C_N(0) sum_(r in S_N)|A_(u,v)(a;r)|^2]^(1/2)
          <= exp((108M+150)s) sqrt(Gamma).                 (1)

For SM<=1/16 the normalized holomorphic arithmetic form satisfies

    |B_N(q;a)| <= exp((120M+168)S) Gamma.                  (2)

In particular, for every multi-index nu in N_0^4,

    |partial^nu B_N(0;a)|
       <= nu! exp(21/2) [64(M+1)]^|nu| Gamma.             (3)

Here nu! is the product of the four factorials. These are full-tail
bounds, including arbitrarily high mixed jets. They do not iterate
L627's restricted first-derivative estimate on its infinite output.
After microscopic scaling q_j=+/-i b_j/L, the corresponding bound
is nu! exp(21/2)(16/25+64/L)^|nu| Gamma.

For the exact signed application there is one existential onset,
depending on the fixed w, beyond which, uniformly in X,a,c,

    |a^*(K_c(T,X)-B(c)G_N)a| < 10^14 B(c) Gamma          (4)

for a nonzero vector; for a=0 both sides vanish. The intended threshold
is B(c)Gamma/2. Thus (4) supplies a coefficient-uniform relative bound
but misses the requested constant by a factor of 2*10^14. It neither
proves nor disproves the half-budget, any negative eigenvalue, a positive
averaged detector margin, pointwise Xi signs or RH. No effective onset
is claimed. Section 6 records the later used-scope audit of (1) and
(2); the other conclusions retain their separate audit qualifications.
The reused source search does not establish originality.

## Proof

### 1. Full rational basis and the local two-block estimate

For a single prime put t=p^(-1/2), x=t^2,

    C=(1-x)^3/(1+x),  rho=2t/(1+x),  h=(1-x)/(1+x),
    f_0=sqrt(C)/(1-tz)^2,
    f_1=sqrt(C)(z-rho)/[h(1-tz)^2],
    f_k=z^(k-2)[(z-t)/(1-tz)]^2,  k>=2.

These are the orthonormal vectors of L627 (4). To check the relevant
boundary cases, the weighted circle measure C|1-tz|^(-4)dm has mass 1
and first moment rho, with 1-rho^2=h^2. The last vectors are mutually
orthonormal because |(z-t)/(1-tz)|=1 on the circle; their inner products
with f_0 and f_1 are integrals of analytic functions with zero constant
term. Completeness follows as well: the corresponding polynomials are
triangular with nonzero leading coefficients, hence span all polynomials;
multiplication by sqrt(C)/(1-tz)^2 is bounded and invertible on H2.
The finite-variable tensor products therefore form a complete basis.

Let R be multiplication on this H2 space by

    R_(u,v)(z)=(1-tz)^2/
                 [(1-t exp(-u log p)z)(1-t exp(-v log p)z)].

Write s=|u|+|v|, d=s log p<=1/16, and define the positive diagonal
operator E_s f_k=exp(-8dk)f_k. The parameter d=0 is trivial, so assume
d>0. The logarithmic power series on |z|<=1 gives

    |log R(z)| <= d t exp(d)/(1-t exp(d)) <= 5dt.          (5)

Indeed |exp(-j u log p)-1|<=j|u|log p exp(j|u|log p), and similarly
for v. Also exp(d)<=16/15, t<=5/7, and
exp(d)/(1-t exp(d))<=112/25<5. The series converge absolutely;
in particular ||R||<=exp(5dt).

There is a sharper estimate on f_0. The coefficient of z^j in
R f_0 is sqrt(C) t^j sum_(k=0)^j exp(-log p(ku+(j-k)v)).
Its modulus is at most sqrt(C)(j+1)t^j exp(jd). With
D(y)=(1+y)/(1-y)^3, Parseval gives

    ||R f_0||^2 <= D(x exp(2d))/D(x) <= exp(20d/p).       (6)

For the second inequality, for 0<=v<=d and y=x exp(2v),

    d/dv log D(x exp(2v))=2y/(1+y)+6y/(1-y).

Since exp(2v)<=8/7 and x<=1/2, this is at most
(16/7)x+16x=(128/7)x<20x. Integrating proves (6).

Let Q be orthogonal projection onto the span of f_k, k>=1, and set
A=E_s R^*R E_s. Its block on Q has norm at most

    exp(-16d) exp(10dt) <= exp(-8d) <= 1-5d.              (7)

The last inequality uses
1-exp(-8d)>=8d/(1+8d)>=16d/3. Its 00 entry is at most
a_0=exp(20d/p). Its off-diagonal block has norm at most b_0=20dt:
the off-diagonal block of the identity vanishes, and the quadratic
form of R^*R-I is integration against |R(z)|^2-1, whose absolute
value is at most exp(10dt)-1<=20dt. Here 10dt<=25/56<1/2,
and exp(y)-1<=2y on 0<=y<=1/2. The further factor E_s on Q is
a contraction. These bounds apply to every vector in the full space.

For z_0 f_0+y with y in Q, Cauchy--Schwarz and (7) give

    <A(z_0 f_0+y),z_0 f_0+y>
       <= a_0|z_0|^2+2b_0|z_0| ||y||+(1-5d)||y||^2
       <= (a_0+b_0^2/(5d))|z_0|^2+||y||^2.

Since b_0^2/(5d)=80d/p and exp(20d/p)+80d/p<=exp(100d/p),
we have proved the local estimate

    ||R_(u,v) E_s|| <= exp(50s log p/p).                 (8)

No coordinate of the output has been omitted.

### 2. Tensoring and undoing the input damping

Use the finite-prime torus isometry with normalized product Haar measure.
L623 (1) and L627 (5) identify the full zero-shift vector as

    f=sqrt(C_N(0)) product_(p<=N)(1-z_p/sqrt(p))^(-2)
                                      sum_(n<=N)a_n z^n
      =sum_(n<=N)y_n f_n,       ||f||^2=sum|y_n|^2=Gamma.

The tensor basis restriction n<=N follows from divisor-triangular
inversion of the local polynomials. It is a restriction on these basis
indices, not on the original infinite coefficient sequence.
Tensor E_s over P_N; its eigenvalue at f_n is n^(-8s). Hence its
inverse on this finite input subspace satisfies

    ||E_s^(-1) f|| <= exp(8sM)||f||.

Tensoring (8) over the finite prime set gives

    ||R_(u,v) E_s|| <= exp(50s sum_(p<=N)log p/p).

The elementary factorial estimate in L627 (8) gives
sum_(p<=N)log p/p<=sum_(p<=N)log p/(p-1)<=2M+3.
It uses unique factorization of N! and convergent prime-power tails,
not a new prime-distribution input. Composing on the specified finite
input gives exp((108M+150)s)||f||. The coefficient vector of R_(u,v)f
is sqrt(C_N(0))A_(u,v)(a;r) for every r in S_N. This proves (1).

### 3. Analytic normalization and all mixed jets

The condition SM<=1/16 puts every shift strictly inside the convergence
domain |Re q_j|<1/4. For v complex with |v|log p<=1/16, the power-series
logarithms satisfy, for k=1,2,

    |log(1-p^(-k-v))-log(1-p^(-k))|
       <= |v|log p * p^(-k)exp(|v|log p)
                                      /(1-p^(-k)exp(|v|log p)).

The multiplier of |v|log p is at most (5/2)/p for k=1 and
(3/2)/p^2 for k=2. The four cross-shift absolute values total at most
2S, while the total shift has absolute value at most S. Thus

    |log(C_N(q)/C_N(0))|
       <= S sum_(p<=N)log p [5/p+(3/2)/p^2]
       <= 6S(2M+3)=(12M+18)S.                           (9)

The logarithms here are the analytic branches from their absolutely
convergent power series; there is no modulus normalization or frozen C_N.
Apply (1) separately to both convolution vectors in B_N and use
Cauchy--Schwarz on their full absolutely convergent bilinear sum.
Conjugating a leaves its G_N norm unchanged because G_N is real
symmetric. Combining the two vector bounds with (9) proves (2).

L624's compact-shift convergence proves holomorphy, including termwise
derivatives for each fixed N. Alternatively the finite products above
give the same holomorphy. On the closed polydisc
|q_j|<=r=1/[64(M+1)], we have SM<1/16 and

    (120M+168)S <= (120M+168)/(16(M+1)) <=21/2.

Successive Cauchy formulas give (3), for every multi-index, with a
neighborhood of the closed polydisc still in the convergence domain.
For the microscopic derivatives, M<=L/100 gives 64(M+1)/L<=16/25+64/L.
This settles convergence and finite constants for higher jets; their
smallness at the signed threshold is a separate matter.

### 4. The complete signed form and the actual Cauchy budget

Let H_a(b) be L624 (8)'s holomorphic expression before taking Re D_c,
using a in place of V_N xi, so that

    H_a(b)=1/(T L^4) integral w_XT(t) Phi(t,b)
       sum_(v=1)^6 exp(-ell lambda_v(q(b)))
                           J(q_v(b)) B_N(q_v(b);a) dt,
    Re D_c H_a(0)=a^*K_c a.

The equality holds for every a by L624 (1), or because V_N is
invertible. Both twist orientations and all original coefficient
multiplicities are retained. Put

    E_a(b)=H_a(b)-Gamma H_11(b),

where H_11 is L622's untwisted germ and its arithmetic factor is 1.
The complete-sum holomorphy import makes this difference holomorphic
through every collision. Individual singular summands are used only
on the following separated boundary torus:

    |b_1|=1/4,  |b_2|=1/2,  |b_3|=3/4,  |b_4|=1.

Every zeta polar linear form in every permutation is +/-i(b_j-b_k)/L.
The difference has modulus at least 1/4 and at most 7/4. The standard
Laurent expansion of zeta at its simple pole of residue 1 gives
|zeta(1+v)|<=5L on these annuli beyond one onset. The reciprocal
zeta factor is near 2, where the absolutely convergent Euler product
is nonzero; hence it is at most 2 in modulus beyond one onset. Thus
|J(q_v)|/L^4<=1250, uniformly on the whole torus and all six terms.

All permutations preserve S=sum|q_j|=5/(2L). Hence SM<=1/40<1/16,
and (2), for L>=420, gives

    |B_N(q_v;a)-Gamma| <= [exp(3+420/L)+1]Gamma
                                  <= (exp(4)+1)Gamma.   (10)

This is a deliberately crude difference bound; no smallness follows
from it. Since ell/L<=6/5 eventually, the six exponential factors
have modulus at most exp(3). L619 Section 3's complex-neighborhood
phase estimate gives |theta'(z)|<=3L/5 eventually on the required
segments, uniformly for T<=t<=3T. Therefore the exact Phi, without
replacing it by an asymptotic germ, has modulus at most exp(3/2).
Nonnegativity and integral 1 of w give integral w_XT=T, and thus

    sup_torus |E_a(b)|
       <= 7500 exp(9/2)(exp(4)+1) Gamma.                (11)

Apply Cauchy's formula to the complete holomorphic E_a on this
polydisc. The Q=partial_1 partial_2-(partial_1^2+partial_2^2)/2
cost is 8+16+4=28, including the second-derivative factorials.
The observer cost is

    (|c0|+(4/3)|c1|)(|c0|+|c1|)
       <= (5/3)sqrt(2) <=5/2,

because c0^2+c1^2=1. The total cost is at most 70. With
beta_c=Re D_c H_11(0), (11) yields

    |a^*(K_c-beta_c G_N)a|
       <=525000 exp(9/2)(exp(4)+1) Gamma.                (12)

For completeness, beta_c=B(c)+o(1) uniformly in X,c follows by applying
the audited L622 transfer to a=e_1 and the audited H=T case of L619
to the same untwisted integral. No growing-vector error is used here.
Increase the onset so that |beta_c-B(c)|<=1/(1680 pi^2)<=B(c)/2.
Since B(c)>=1/(840 pi^2), the relative coefficient in (4) is at most

    840 pi^2 *525000 exp(9/2)(exp(4)+1)+1/2
       <8400*525000*243*82+1/2
        =87873660000000+1/2 <10^14.

Here pi^2<10 and exp(1)<3 suffice. This proves (4), retaining every
tail coordinate, analytic normalization, phase factor, signed derivative
and source term. It is uniform but far larger than 1/2.

### 5. What remains unresolved

Equations (1)–(3) remove the earlier domain obstruction to controlling
higher mixed derivatives in the full growing-prime space. Equation (12)
also bounds the complete signed extraction relative to Gamma. These are
local intermediate advances, not the missing positivity comparison.
The large absolute Cauchy majorant (10) discards cancellations; repeating
it does not justify a half-budget, even if the constants are renamed.

The pole order matters in any later direct germ computation. The product
of four zeta factors can have homogeneous degree -4 before summing the
six terms. Consequently extracting a degree-four coefficient of the
complete germ can require arithmetic Taylor coefficients through degree
eight, unless an explicit cancellation identity lowers that requirement.
Only after cancellation may one speak of four derivatives of a regular
germ. Bound (3) covers every required order but supplies no cancellation
or sharp signed constant. No individual pole term is evaluated at zero.

A further attempt must preserve the complete signed cancellations, or
otherwise supply a substantially sharper quantitative comparison. A
bound above 1/2 is inconclusive and implies no negative eigenvalue.
The reference lower bound, L622 transfer, pointwise signs and all-degree
positivity must continue to be distinguished.

### 6. Used-scope conceptual audit for L629, 1 November 2026

Equations (1) and (2) pass this audit under the named torus input.
This checks the full-tail norm actually used by L629, not (4), all
of L627, or the external manuscripts. No constant has been improved.

The fixed rational basis is orthonormal, including degrees zero and
one: the circle products displayed in L627 have zero constant term
against the higher vectors, and 1-rho^2=h^2 checks the remaining
norm. Its triangular polynomials span the finite divisor ideal n<=N.
Multiplication by the bounded invertible factor sqrt(C)/(1-tz)^2
also proves completeness in H2. Thus the block Q in Section 1 and
the finite-prime tensor operator act on the entire output space.

For d=s log p<=1/16, the logarithmic series in (5) converges since
t exp(d)<1. The elementary bounds exp(d)<=16/15, t<=5/7 give
exp(d)/(1-t exp(d))<=112/25<5. For the vacuum estimate, put
y=x exp(2v), 0<=v<=d. Then exp(2v)<=8/7 and
2y/(1+y)+6y/(1-y)<=128x/7<20x; integration gives (6).
On Q, E_s has norm exp(-8d), so the compressed positive operator
E_s R^*R E_s has norm at most exp(-16d+10dt)<=exp(-8d).
Moreover 1-exp(-8d)>=8d/(1+8d)>=16d/3>=5d.
The cross block is bounded by ||R^*R-I||<=exp(10dt)-1<=20dt:
the logarithm bound controls both upper and lower moduli of R,
and 10dt<=25/56<1/2. These are full-operator bounds, without
invariance of the finite input space being assumed.

Completing the square in the two blocks costs
(20dt)^2/(5d)=80d/p. For u=d/p>=0,
exp(20u)+80u<=exp(100u), since
exp(20u)(exp(80u)-1)>=80u. Taking the square root proves (8).
At d=0 the operator is the identity, so the division by d causes
no missing boundary case. Tensor norms multiply over the finite
prime set, and E_s^(-1) on the input n<=N costs at most exp(8sM).
The factorial bound and its convergent prime-power tail give
sum log p/p<=2M+3. The resulting exponent is exactly
8sM+50s(2M+3)=(108M+150)s, proving (1).

For normalization, SM<=1/16 puts each shift inside |Re q_j|<1/4
because M>=log 2. Each cross-shift satisfies |v|log p<=1/16.
The power-series logarithms of the local factors obey the stated
(5/2)/p and (3/2)/p^2 bounds. The cross-shifts total at most 2S,
and 5/p+(3/2)/p^2<=6/p for p>=2. Consequently (9) costs
(12M+18)S. Applying (1) to both full convolution vectors and using
Cauchy--Schwarz on their bilinear sum adds (108M+150)S, proving
(2) with exponent (120M+168)S. G_N is real symmetric, so replacing
a by its conjugate preserves Gamma. No shift was conjugated, no
C_N derivative was suppressed, and no infinite output was removed.

This closes the previously unaudited norm input at L629's actual
torus, where S=5/(2L), SM<=1/40 and the exponent is at most
3+420/L. The proof is an audit of the existing estimate, not a
new shift theorem or a stronger source conclusion.

## Mathlib

Full matching coverage of these weighted rational-basis estimates,
complex-shift constants and the complete signed relative bound was not
checked and is unknown. The finite-prime isometry and source holomorphy
are the named imports above. Orthogonality, the damped two-block bound,
finite tensor composition, normalization estimate and Cauchy costs are
proved here. No Lean proof or formal certificate is claimed.
