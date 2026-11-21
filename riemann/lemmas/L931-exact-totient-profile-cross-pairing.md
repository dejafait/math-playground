# Lemma 931: uniform exact cross pairing for the totient profile

## Hypotheses

Use precisely L930's finite matrices G,K,A=D+K,M,Q,H_-,H_+,V,
its fixed nonnegative w in C_c^infinity((0,1)) with integral one,
its probability average <.>, and its exact Hardy phase epsilon_t.
Thus L=log T, N=floor(T^(1/5)), T<=X<=2T, h=2i/L,
r=log N, and

    v_d=1/sqrt(phi(d)), 1<=d<=N,
    W_+=M(h)^T Q(h) M(h), W_-=Q(-h),
    I_±=<exp(i epsilon_t)exp(±i ell_t/L)>,
    V=zeta(1+h)I_+W_++zeta(1-h)I_-W_-,
    rho(T,X)=|v^*Vv|/sqrt((v^*H_-v)(v^*H_+v)).

The denominator is positive at L930's common onset. All powers use
real logarithms of positive numbers; T denotes transpose in matrix
superscripts, and * denotes adjoint. The vector v is real. It is a
test vector in divisor coordinates, not a Schur weight chosen to bound
the cross operator. The associated original coefficient pair is
c_s=D_s^(-1)G^(-1)v in L930's notation.

Two previously assessed scalar arithmetic inputs are imported:

1. Terence Tao, *254A, Notes 1: Elementary multiplicative number
   theory*, 23 November 2014, [Section 2, Theorem
   13](https://terrytao.wordpress.com/2014/11/23/254a-notes-1-elementary-multiplicative-number-theory/):
   sum_(n<=x) Lambda(n)/n=log x+O(1), for every real x>=1,
   with an absolute constant. The full first-Mertens proof and its
   Chebyshev input were inspected in the row-sum assessment.
2. Pieter Moree, Sumaia Saad Eddin, Alisa Sedunova and Yuta Suzuki,
   *Jordan totient quotients*, [MPIM preprint 18-66 (2018),
   Section 2, Condition Theta1 p. 4, Lemma 2 and its proof
   pp. 5–6](https://archive.mpim-bonn.mpg.de/3557/1/preprint_2018_66.pdf).
   For squarefree-supported multiplicative theta, set
   f(n)=product_(p|n)(1+theta_p). If 0<=sigma<1, kappa,A>=0,
   and sum_(p<=x)|theta_p|/p^sigma<=kappa log log x+A for x>=2,
   its beta=-1 case gives

       sum_(n<=x) f(n)/n
          =S_theta log x+C(theta,-1)
             +O_(sigma,kappa,A)(x^(sigma-1)(log x)^kappa),
       S_theta=product_p(1+theta_p/p).

The harmonic-case proof was inspected in step16. This is a real
exponent theorem; the moving imaginary powers below are handled by
explicit partial summation, not an unproved complex extension.

The invocation-start EXPLORE assessment is
drafts/literature/2026-11-09-exact-totient-profile-cross-test-15.md.
The first-Mertens coverage reused there is in
drafts/literature/2026-11-09-logarithmic-gcd-row-sum-review.md.
No scalar mean-value theorem is reproved. The finite profile propagation
and paired endpoint evaluation are supplied because those sources do
not state the present normalized correlated limit. L737 is used only
for its all-N finite identities; L928 supplies the exact moment/phase
interface through L930. No L925/L929 theorem, new moment estimate,
zero-free region, RH, or cross-notebook result is assumed.

## Conclusion

Let

    C_phi=product_p(1+1/(p(p-1)))>0, alpha=r/L.

Uniformly for T<=X<=2T as T tends to infinity,

    v^*H_s v=C_phi L^2 alpha(1-alpha)+O(L), s=-1,+1,       (1)
    v^*Vv=C_phi L^2 exp(-2i alpha)
                   sin(alpha)sin(1-alpha)+O(L),           (2)
    rho(T,X)=sin(1/5)/(1/5) * sin(4/5)/(4/5)+O(1/L).      (3)

In particular, there is a common sufficiently-large-T onset for which
rho(T,X)<=9/10 for every admissible X. The onset is not made effective.
This excludes this one prescribed profile as a witness tending to one.
It does not establish any upper bound for the operator on all vectors,
or exclude a different saturation witness. The fixed/sufficient
shrinking joint contraction gap, joint projection, signed realization
and transfer, and L030–L032/C032a actual-Xi mixed positivity remain open.

Written 9 November 2026, step17; the separate step19 conceptual audit
below validates (1)–(3) and the scoped exclusion without correction.
The outcome is a local negative test of this saturation proposal.
The arithmetic inputs are known imports; the assessment did not find
this exact profile limit, which is not a claim of certified originality.
There is no RH candidate or newly claimed arithmetic moment theorem.

## Proof

### 1. Reciprocal-totient mass and the mean kappa correction

In the cited general-totient lemma take theta_p=1/(p-1), extending
theta multiplicatively with support on squarefree integers. Then
f(n)=n/phi(n). Take sigma=1/2 and kappa=0: for all x>=2,

    sum_(p<=x) 1/((p-1)sqrt(p))
       <=sum_(n>=2) 1/((n-1)sqrt(n))=:A_0<infinity.

The convergence follows by comparison with n^(-3/2). These are fixed
parameters satisfying every hypothesis. The theorem therefore gives

    S(x):=sum_(d<=x)1/phi(d)
       =C_phi log x+C_0+O(x^(-1/2)), x>=2.                 (4)

The Euler product defining C_phi converges to a positive finite value,
since sum_p 1/(p(p-1)) converges. Enlarging an absolute bound on the
error over 1<=x<2 yields S(x)=C_phi log x+O(1) for every x>=1.
In particular ||v||^2=S(N)=O(1+r).

Put

    B_0=sum_p log(p)/(p-1)^2<infinity.

Convergence follows by comparison with sum_(n>=2)log(n)/(n-1)^2;
no prime asymptotic is used for this comparison. The finite Euler
product gives phi(pm)>=phi(p)phi(m), including when p divides m.
For kappa(d)=sum_(p|d)log(p)/(p-1), as in L737/L930, finite
reordering and positivity now give

    sum_(d<=N) kappa(d)/phi(d)
      =sum_(p<=N) log(p)/(p-1)
                         *sum_(m<=N/p)1/phi(pm)
      <=sum_(p<=N) log(p)/(p-1)^2 S(N/p)
      <=B_0 S(N)=O(1+r).                                  (5)

Thus the kappa contribution to this vector's full metric is retained
and controlled, rather than discarded or bounded by its pointwise
maximum r.

### 2. Uniform approximate eigenvector, including cutoff rows

For each d<=N the exact finite definition of K gives

    (Kv)_d/v_d
       =sum_(p^a<=N/d, a>=1) log(p)*phi(d)/phi(dp^a).       (6)

If p divides d, the totient ratio in (6) is p^(-a). If p does
not divide d, it is 1/(p^(a-1)(p-1)), which exceeds p^(-a)
by 1/(p^a(p-1)). Consequently, for every real cutoff x=N/d>=1,

    0<= (Kv)_d/v_d-sum_(n<=x)Lambda(n)/n
       <=sum_p sum_(a>=1)log(p)/(p^a(p-1))=B_0.            (7)

The equality on the right uses a convergent geometric series. By the
cited first-Mertens theorem, (6) is log(N/d)+O(1) with one constant
independent of both N and d. This also handles 1<=N/d<2, where the
prime-power sums are empty and log(N/d) is bounded. Since A=D+K,

    e:=(A-rI)v satisfies |e_d|<=C v_d,
    ||e||<=C||v||.                                        (8)

No right eigenvector identity is being asserted. The error bound is
uniform in the growing dimension and will be propagated quantitatively.
For u=2/L and 0<=s<=u, differentiating the finite matrix exponential
(or integrating that derivative) gives exactly

    M(iu)v-exp(-iur)v
      =-i integral_0^u exp(-i(u-s)A) exp(-isr)e ds.         (9)

L930(10) supplies ||exp(-i q A)||<=exp(2rq) for q>=0.
Since r<=L/5, (8)–(9) imply

    M(h)v=exp(-hr)v+eta,
    ||eta||<=C u exp(2ru)||v||=O(||v||/L).                (10)

Only a finite matrix integral is used. No truncation limit, eigenbasis
condition number, or normality of A has been assumed.

### 3. Both Jordan sums and the transpose endpoint

For z=+h or -h, the finite Euler product is

    j(z,d)=d^z product_(p|d)(1+(1-p^(-z))/(p-1)).

Because z is imaginary, |1-p^(-z)|<=|z|log p. The elementary
product estimate |product(1+b_p)-1|<=exp(sum|b_p|)-1 yields

    |j(z,d)-d^z|
       <=|z|kappa(d)exp(|z|kappa(d))
       <=|z|kappa(d)exp(2r/L).                            (11)

Here |d^z|=1 and 0<=kappa(d)<=r, including d=1. Summing (11)
against 1/phi(d) and using (5) gives, with no termwise positivity
claim for j,

    q_z:=v^TQ(z)v
       =sum_(d<=N)d^z/phi(d)+O(S(N)/L).                   (12)

For completeness the needed uniform complex summation is finite Abel
summation. Write S(t)=C_phi log t+E(t), with |E(t)|<=C for t>=1
by (4). Then

    sum_(d<=N)d^z/phi(d)
       =N^z S(N)-z integral_1^N t^(z-1)S(t)dt
       =C_phi integral_1^N t^(z-1)dt
          +N^z E(N)-z integral_1^N t^(z-1)E(t)dt.          (13)

This formula includes the atom at d=1; no lower endpoint mass is
dropped. For imaginary z the last two terms are bounded by
C(1+|z|r). At z=±h, |z|r<=2/5. Equations (12)–(13), together
with S(N)=O(L), therefore give

    q_h=C_phi L exp(i alpha)sin(alpha)+O(1),
    q_(-h)=C_phi L exp(-i alpha)sin(alpha)+O(1).            (14)

These equalities follow by evaluating integral_0^r exp(±2iu/L)du;
they do not import a mean-value theorem with moving complex parameters.

As v is real, v^*W_+v=(M(h)v)^T Q(h)(M(h)v), with transpose,
not adjoint. L930's bound ||Q(h)||<=exp(2r/L), and (10), give

    |v^*W_+v-exp(-2hr)q_h|
       <=||Q(h)||(2||v||||eta||+||eta||^2)
       =O(S(N)/L)=O(1).                                  (15)

The inequality for complex bilinear products follows from the usual
absolute Cauchy–Schwarz inequality; it does not turn Q into a positive
matrix. Thus both complete endpoint pairings are

    v^*W_+v=C_phi L exp(-3i alpha)sin(alpha)+O(1),
    v^*W_-v=C_phi L exp(-i alpha)sin(alpha)+O(1).           (16)

### 4. Both full energies

L737's exact column identity is

    (v^T K)_n=log(n)v_n,
    v^T K v=sum_(n<=N)log(n)/phi(n).                       (17)

Indeed v_d K_(d,n)=Lambda(n/d)/sqrt(phi(n)), and summing over
proper divisors d of n gives log n by the finite Mangoldt identity.
For n=1 both sides vanish. Finite partial summation using (4) gives

    sum_(n<=N)log(n)/phi(n)
       =r S(N)-integral_1^N S(t)/t dt
       =C_phi r^2/2+O(1+r).                              (18)

The scalar v^T K^T v equals v^T K v, since v is real. Substituting
(4),(5),(17),(18) into L930's exact formula
H_s=a_s I+2diag(kappa)-K-K^T yields

    v^*H_s v
       =a_s S(N)+2sum_(d<=N)kappa(d)/phi(d)
                           -2sum_(n<=N)log(n)/phi(n)
       =C_phi(Lr-r^2)+O(L).                              (19)

Here a_s=L+O(1) uniformly in X for each s=-1,+1, as already
established in L930 from the exact translated time average. No
diagonal-only replacement of either metric was made. This proves (1).

### 5. Coupled poles, exact time factors, and the threshold

The scalar time factors remain their exact definitions. On the whole
support of the fixed probability weight, ell_t=L+O(1) uniformly in X,
and L928/L930 give epsilon_t=O(1/(TL)). The elementary bound
|exp(ix)-exp(iy)|<=|x-y| for real x,y therefore gives

    I_+=exp(i)+O(1/L), I_-=exp(-i)+O(1/L).                 (20)

The averaging is justified by its nonnegative normalized weight; this
estimate bounds the error of replacing the exact phase, rather than
silently freezing it. L930's residue-one Laurent decomposition gives

    zeta(1+h)=L/(2i)+O(1),
    zeta(1-h)=-L/(2i)+O(1),                               (21)

with uniform regular-part constants for L>=4. Insert both terms of
(16), (20), (21) into the exact V. Every regular-part contribution
is O(L), every endpoint O(1) error is multiplied by O(L), and every
I error contributes O(1/L)*O(L)*O(L)=O(L). Hence

    v^*Vv
      =C_phi L^2 sin(alpha)/(2i)
          *[exp(i-3i alpha)-exp(-i-i alpha)]+O(L)
      =C_phi L^2 exp(-2i alpha)
                     sin(alpha)sin(1-alpha)+O(L).         (22)

This proves (2), preserving cancellation between the endpoints before
taking modulus. All errors are uniform for X/T in [1,2]. In particular
the regular zeta terms and the exact Hardy phase have been paid for.

Since N=floor(T^(1/5)), r=L/5+O(T^(-1/5)), and consequently
alpha=1/5+O(T^(-1/5)/L). It stays in a compact subinterval of
(0,1) eventually. The main energy in (19) is therefore bounded below
by a positive constant times L^2, and

    sqrt((v^*H_-v)(v^*H_+v))
       =C_phi L^2 alpha(1-alpha)+O(L).                    (23)

The error in taking the numerator's modulus is at most the O(L)
error in (22). Dividing by (23) proves

    rho(T,X)=sin(alpha)sin(1-alpha)/(alpha(1-alpha))+O(1/L).

The smoothness of this elementary quotient near alpha=1/5 justifies
substitution of its limit and proves (3). No infinite coefficient or
time integral has been interchanged with a limit without its uniform
error estimate.

Finally 0<sin(x)/x<=1 for 0<x<=1. The alternating sine expansion
with its decreasing-term remainder gives

    sin(4/5)/(4/5)
       <=1-(4/5)^2/6+(4/5)^4/120
       =8407/9375<9/10.

Thus the limit in (3) is strictly below 9/10. Its fixed positive
distance from 9/10 absorbs the uniform O(1/L) error at one common
onset, proving the asserted eventual bound. This is a scalar test;
the operator norm is a supremum over all coefficient pairs, so this
bound supplies no operator contraction. In particular it proves no
margin that could be used to absorb L928's charged arithmetic error
O(T^(-9/80)/L) for all vectors. The earlier termwise-Schur and
parameter-norm stops retain their scopes; no stopped estimate was
reopened here.

### Separate conceptual audit — 9 November 2026, step19

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-11-09-exact-totient-profile-audit-17.md`.
This is an independent REPRODUCTION check of the existing proof,
using the previously inspected primary scalar statements and the
audited L737 finite interface and L930 exact coordinates and bounds.
It establishes no new mean-value theorem or operator upper bound.

**Arithmetic constants and every cutoff.** In the general-totient
Lemma 2, beta=-1, sigma=1/2, kappa=0 and the fixed finite A_0 meet
Condition Theta1 for every real x>=2. The harmonic branch requires
sigma<1 and no additional prime-asymptotic condition. The function is
exactly f(n)=n/phi(n), including n=1, and its Euler product constant
is exactly C_phi. Thus one may fix C_S such that

    |S(x)-C_phi log x|<=C_S for every real x>=1.

Here and below constants are independent of N,d,X and T. They may
depend on the already fixed weight or named scalar estimates. The
totient inequality in (5) holds both when p divides m (ratio p/(p-1))
and when it does not (ratio one). Consequently the entire averaged
kappa term is at most B_0 S(N); it has not been replaced by r S(N).
In (7) the correction is zero for p|d and log(p)/(p^a(p-1))
otherwise. Summing over all primes and exponents gives exactly B_0.
The first-Mertens estimate therefore supplies a single C_e with
|((A-rI)v)_d|<=C_e v_d for every row. Empty rows at N/d<2
are included. These checks validate (4)–(8) from the cited imports.

**Finite propagation and transpose.** For u=2/L, differentiating
exp(-i(u-s)A)exp(-isr)v with respect to s gives i times the
integrand containing e in (9). Its endpoint difference is
exp(-iur)v-M(iu)v, verifying the minus-i sign. L930(10) gives

    ||eta|| <= (2 C_e exp(4/5)/L) ||v||.

The bound uses r<=L/5, and no diagonalization, dimension factor or
condition number. Since v is real, v^*M(h)^T=(M(h)v)^T;
using an adjoint here would remove the essential exp(-2hr) phase.
With ||Q(h)||<=exp(2/5), the error in this bilinear pairing is
at most exp(2/5)(2||v||||eta||+||eta||^2)=O(S(N)/L).
Thus the propagation remains sufficient after both occurrences of M.

**Jordan average and lower atom.** From (11) and (5), the absolute
error in replacing q_z by sum d^z/phi(d) is at most
(2/L)exp(2/5)B_0 S(N). For z=±h the last two terms of (13)
have absolute value at most C_S(1+|z|r)<=7 C_S/5. The lower
endpoint has S(1)=1: in the displayed Abel formula its atom is
retained in E, with no subtracted S(1) term. Evaluation of
(exp(zr)-1)/z gives the two phases exp(±i alpha) in (14).
The preceding propagation contributes exp(-2hr)=exp(-4i alpha)
at W_+, proving precisely the two endpoint phases in (16), with
uniform O(1) errors. No moving-complex-parameter source is assumed.

**Complete metrics.** The exact column calculation includes every
proper divisor, not merely prime divisors: sum_(q|n) Lambda(q)=log n.
It gives v^T K v=sum log(n)/phi(n), and its transpose has the
same real scalar value. Abel summation and the bound C_S give an
error at most 2 C_S r in (18). Also |a_s-L|<=C_a for both signs,
uniformly over X, because the translated support lies at height
comparable with T and the averaging weight has integral one.
The errors in a_s S(N), the averaged kappa term, and twice (18)
are respectively O(L), O(1+r), and O(r). It follows that

    v^*H_s v=C_phi(Lr-r^2)+O(L), s=-1,+1,

with one constant and one onset for both full metrics. The logarithmic
cross terms are responsible for -C_phi r^2; omitting them would change
the leading denominator, rather than merely its error.

**Coupling, normalization and a common strict threshold.** On the
complete weighted support, |ell_t-L| is bounded and L928's exact
phase has |epsilon_t|<=C/(TL). Hence each I_± differs from
exp(±i) by O(1/L). Each zeta value differs from its signed pole by
at most the fixed C_g of L930. The endpoint main terms are O(L)
with O(1) errors, so expanding the two exact products in V leaves
O(L) total error; products involving several errors are smaller.
The leading difference is

    exp(i-3i alpha)-exp(-i-i alpha)
       =2i exp(-2i alpha)sin(1-alpha),

which verifies the sign and factor in (22). Cancellation is performed
before taking modulus. All these constants are independent of X.
The floor gives |alpha-1/5|=O(T^(-1/5)/L), so eventually alpha
is in a fixed compact subinterval of (0,1). Write
b=C_phi L^2 alpha(1-alpha)>=c L^2. Each energy is b+O(L),
positive after a common onset. Rationalizing the square root of their
product gives b+O(L); the modulus of the numerator changes by at most
its O(L) error. Division is therefore valid uniformly and gives (3).

The alternating sine remainder at x=4/5 has the stated upper sign.
The exact rational margin is

    9/10-8407/9375=61/18750>0.

Since 0<sinc(1/5)<=1, the limiting product has at least this
distance from 9/10. Once the uniform normalized error is less than
61/37500, every X has rho<9/10. The common onset is existential,
as claimed; the proof does not supply a numerical onset.

**Audit result and boundary.** All of (1)–(23) pass without correction.
The formerly unaudited scalar exclusion is now a checked informal
input. This justifies parking this prescribed saturation witness.
The coefficient pair is still the admissible moving pair
c_s=D_s^(-1)G^(-1)v; no uniform inverse bound is needed for this
finite scalar test. Taking one pairing below one gives no bound on
the supremum over other pairs and pays no general joint margin.
L928's arithmetic charge, signed realization/transfer and the main
Xi positivity gap remain. Direct inputs are unchanged; L925 and L929
are not used as theorems. No mathematical script or numerical evidence
is needed for this audit.

## Mathlib

Full matching coverage for this normalized growing-profile limit has
not been checked and is unknown. The cited first-Mertens and
general-totient theorems are informal named imports. Finite divisor
identities, partial summation, matrix exponentials, Cauchy–Schwarz,
Euler products and elementary trigonometric bounds are supporting
topics, not checked full matching Mathlib theorems. The step19 review
is an informal critical audit, not a formal verification. Full matching
Mathlib coverage remains unknown; no absence claim is made.
