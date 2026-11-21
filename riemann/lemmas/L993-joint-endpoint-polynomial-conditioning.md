# Lemma 993: polynomial conditioning of the exact joint endpoint observations

## Hypotheses

For integers n>=2 use precisely L990's corrected real kernels and rows:

    K_m(u)=[L_(m-1)^(2)(u)-1]/(m-1),
    a_n=(K_n(n),K_(n+1)(n),K_(n+2)(n)),
    b_n=(K_n(2n),K_(n+1)(2n),K_(n+2)(2n)),
    d_n=a_n cross b_n, c_n=d_n/||d_n||_1.

For all sufficiently large n, L990 and C990a make these rows and

    U_n=a_n/||a_n||_2, V_n=b_n/||b_n||_2,
    J_n=[U_n; V_n; c_n]

well defined. Brackets denote matrix rows. Use the standard Laguerre
normalization p_n(u)=L_n^(2)(u). No RH, arithmetic bound, actual
off-line zero, effective onset, or Diophantine estimate on a full
frequency vector is assumed.

## Conclusion

There are C>0 and an integer N such that, for every integer n>=N
and every x in R^3,

    ||J_n x||_2 >= (C/n)*||x||_2.                         (1)

In particular the approved polynomial target holds with exponent A=1,
and ||J_n^(-1)||_2<=n/C. The constants and onset are existential.
No optimality of the exponent or bound for all n>=2 is claimed.

Step276, 10 November2026: REPRODUCTION, a quantitative specialization
of the previously assessed recurrence and phase argument. This is a
local advance; no originality beyond the checked sources is claimed.
Step278 independently critically audits the proof under review276,
approved in step277, and accepts (1) on its stated existential tail.
No mathematical correction or stronger bound is needed. This validates
the local specialization, not a result beyond the sources checked.

This recovers three coordinates only from all three observations.
It does not bound any actual arithmetic output, repair scalar recovery,
or pay actual-Xi positivity L030-L032/C032a, L966/L968 signed forcing,
common/shifted interval identification, prime powers, other zeros,
either complement, or L984(H). It is not an RH candidate.

## Proof

### Established inputs and purpose of the specialization

Use L990(5),(13) for individual-row scales and the exact corrected
recurrence, and C990a(1),(10)-(11) for additive second-order endpoint
phases. Those statements were separately audited in steps265/267.
Their external analytic inputs are A. Gil, J. Segura and N. M. Temme,
*Asymptotic approximations to the nodes and weights of Gauss-Hermite
and Gauss-Laguerre quadratures*,
[arXiv1709.09656v1, section3.3, equations81-87](https://arxiv.org/html/1709.09656v1#S3.SS3),
and *Efficient computation of Laguerre polynomials*,
[arXiv1609.00829v1, section2.1.3, equations20-25](https://arxiv.org/html/1609.00829v1#S2.SS1.SSS3),
with [DLMF10.17(iii)](https://dlmf.nist.gov/10.17#iii).
The fixed parameter is alpha=2, and all scaled arguments lie in the
positive compact interval [1/9,1/2], within the GST domain with
delta=1/2. No individual-zero expansion, differentiated remainder,
or numerical asymptotic-error claim is used. These source contracts
and their normalization are reused, not reproved.

Review275, using the completed comparison in review274, found no
inspected theorem supplying (1). The missing specialization is the
quantitative effect of a residual in C990a's exact-collinearity
argument. It is proved below before applying standard SVD facts.
Single-polynomial root spacing and generic algebraic approximation
are not inputs to this proof.

Write a=a_n, b=b_n, alpha_n=||a||_2, beta_n=||b||_2. The individual
row estimates from L990 give fixed positive lower and upper constants
in each of

    alpha_n asymp exp(n/2)*n^(-3/2),
    beta_n  asymp exp(n)*n^(-3/2).                       (2)

Here asymp denotes two-sided inequalities holding for every n beyond
one onset. They hold even at near-collisions of row directions: the
leading row norms squared are 3/2 and 1+cos(psi_n)^2 in [1,2], and
the additive row errors after scaling are O(1/n).

Let M_(r,n)>0 be C990a's amplitudes, explicitly

    N_n=4n+6, t_(r,n)=rn/N_n,
    D_0(t)=4*t^(5/4)*(1-t)^(1/4),
    M_(r,n)=exp(rn/2)*sqrt(2/(pi*N_n))/D_0(t_(r,n)).

Uniform compact bounds on D_0 give

    M_(r,n) asymp exp(rn/2)*n^(-1/2), r=1,2.           (3)

Every constant used below is independent of n and of its phases.

### Near parallel or antiparallel rows force two small values

Set rho=U_n dot V_n. Choose s in {+1,-1} with s*rho=|rho|
(take s=1 if rho=0), and put

    epsilon=||V_n-s*U_n||_2=sqrt(2*(1-|rho|)),
    lambda=s*beta_n/alpha_n, r=b-lambda*a.

Thus 0<=epsilon<=sqrt(2), ||r||_2=beta_n*epsilon, and lambda is
nonzero. Its magnitude is comparable to exp(n/2) by (2). This choice
treats both orientations without dividing by a small angle or pivot.

L990's exact finite identity, retaining the constant subtraction, is

    R(u) dot (K_n(u),K_(n+1)(u),K_(n+2)(u))=-u,
    R(u)=((n-1)*(n+2),-n*(2n+3-u),(n+1)^2).          (4)

In particular R(2n)-R(n)=(0,n^2,0). Number vector coordinates
0,1,2. Substituting b=lambda*a+r into R(2n) dot b=-2n gives

    lambda*(-n+n^2*a_1)+R(2n) dot r=-2n.

Since n*a_1=p_n(n)-1 and n*b_1=p_n(2n)-1, this yields exactly

    p_n(n)=2-2/lambda-[R(2n) dot r]/(lambda*n),
    p_n(2n)=lambda-1-[R(2n) dot r]/n+n*r_1.           (5)

The second identity follows by substituting the first into
p_n(2n)-1=lambda*(p_n(n)-1)+n*r_1. In particular both constant
corrections remain present; no homogeneous recurrence is substituted.

For n>=2,

    ||R(2n)||_2 <= ||R(2n)||_1
                 =2*n^2+6*n-1 <=5*n^2.

The Cauchy-Schwarz inequality and (5) therefore imply

    |p_n(n)|/M_(1,n)
      <=(2+2*alpha_n/beta_n)/M_(1,n)
                             +5*n*alpha_n*epsilon/M_(1,n),
    |p_n(2n)|/M_(2,n)
      <=(beta_n/alpha_n+1)/M_(2,n)
                             +6*n*beta_n*epsilon/M_(2,n).

Equations (2)-(3) bound the coefficients of epsilon by fixed
constants, and the other terms by a fixed multiple of
sqrt(n)*exp(-n/2). Hence for one H>0 and every sufficiently large n,

    |p_n(rn)|/M_(r,n)
            <=H*(epsilon+sqrt(n)*exp(-n/2)), r=1,2.  (6)

This is uniform on all indices, with no fixed-neighborhood exclusion.

### Uniform phase errors and the integer obstruction

Use C990a's additive bound

    |p_n(rn)/M_(r,n)-cos(theta_(r,n))|<=C_*/n^2,
    theta_(1,n)=n*(sqrt(3)/2+pi/3)-3*pi/4+gamma_1/n,
    theta_(2,n)=n*(1+pi/2)-pi/2+gamma_2/n,
    gamma_1=13*sqrt(3)/108, gamma_2=-13/24.            (7)

The exponential term in (6) is at most n^-2 beyond a fixed onset:
n^(5/2)*exp(-n/2) tends to zero. Thus (6)-(7) give a constant H_1
such that |cos(theta_(r,n))|<=H_1*(epsilon+n^-2).

For any real t choose a nearest member of pi/2+pi*Z, with distance
d<=pi/2. Then |cos(t)|=sin(d)>=2*d/pi. Consequently integers k,l
can be chosen, separately for each n, with

    theta_(1,n)=pi/2+pi*k+eta_1,
    theta_(2,n)=pi/2+pi*l+eta_2,
    |eta_1|, |eta_2| <=(pi*H_1/2)*(epsilon+n^-2).     (8)

This inequality is valid even when its right side is large; no local
inverse-function hypothesis or assumed small epsilon is needed.

Define the integers P=12*k+15-4*n and Q=2*l+2-n. Retaining the
rational offsets and the 1/n corrections in (8), rearrangement gives

    P=a_0*n+c_0/n+e,
    Q=b_0*n+d_0/n+f,
    a_0=6*sqrt(3)/pi, b_0=2/pi,
    c_0=12*gamma_1/pi, d_0=2*gamma_2/pi,
    e=-12*eta_1/pi, f=-2*eta_2/pi.                   (9)

Choose L>=1 so that |e|,|f|<=L*h, where h=epsilon+n^-2.
For n>=2, h<=sqrt(2)+1/4<2. Direct expansion of (9), with
a_0^2=27*b_0^2, gives

    P^2-27*Q^2
      =2*a_0*c_0-54*b_0*d_0+(c_0^2-27*d_0^2)/n^2
       +2*(a_0*n+c_0/n)*e-54*(b_0*n+d_0/n)*f
       +e^2-27*f^2,
    2*a_0*c_0-54*b_0*d_0
      =(144*sqrt(3)*gamma_1-216*gamma_2)/pi^2
      =(52+117)/pi^2=169/pi^2.                       (10)

All error products are controlled. The two linear error terms are
at most 2*L*(|a_0|+|c_0|+27*|b_0|+27*|d_0|)*n*h.
The quadratic errors are at most 28*L^2*h^2<=56*L^2*h.
Also n*h=n*epsilon+1/n, h<=n*h and n^-2<=1/n. For example, the
finite positive constant

    K=1+|c_0^2-27*d_0^2|
       +2*L*(|a_0|+|c_0|+27*|b_0|+27*|d_0|)+56*L^2

satisfies the uniform bound

    |P^2-27*Q^2-169/pi^2| <=K*(n*epsilon+1/n).       (11)

This tracks the amplification by the O(n) integer expressions;
the additive O(n^-2) phase remainder becomes O(n^-1), not O(1).

By C990a's established transcendence input,

    delta=dist(169/pi^2,Z)>0.

For precision that input is the Lindemann-Weierstrass theorem in
L. Fukshansky, *Geometric Number Theory*,
[Theorem6.2.1, printed p138](https://www1.cmc.edu/pages/faculty/lenny/papers/GNT_lecture_notes.pdf#page=142),
and its explicit [Corollary6.3.2, printed p144](https://www1.cmc.edu/pages/faculty/lenny/papers/GNT_lecture_notes.pdf#page=148).
The author-hosted source and the corollary's complete proof were
inspected in step277. As justified in C990a, pi is transcendental, so 169/pi^2
cannot be an integer. The distance is positive since Z is discrete.
No quantitative transcendence measure is required: this is one fixed
constant, not an approximation to a varying algebraic number.

Since P^2-27*Q^2 is an integer, (11) implies
delta<=K*(n*epsilon+1/n). At every n>=2*K/delta beyond all preceding
onsets it follows that

    epsilon >= delta/(2*K*n)=:c_epsilon/n>0.          (12)

Thus the near-collision argument gives a bound at every sufficiently
large integer, not just on a subsequence. All constants in its
contradiction are uniform. The proof does not rely merely on C990a's
qualitative nonvanishing; it establishes the needed quantitative gap.

### The exact Gram matrix

The row c_n is exactly orthogonal to U_n and V_n. Its l2 norm q_n
satisfies 1/sqrt(3)<=q_n<=1, since
||d_n||_2<=||d_n||_1<=sqrt(3)*||d_n||_2. Therefore

    J_n*J_n^T = [[1,rho,0],[rho,1,0],[0,0,q_n^2]],

whose eigenvalues are 1+rho, 1-rho and q_n^2. The singular values
are the square roots of these eigenvalues. The standard SVD and
inverse-norm facts are covered by D. Bindel, *CS6210: Matrix
Computations*,
[25August2025 lecture, The SVD and the 2-norm](https://www.cs.cornell.edu/courses/cs6210/2025fa/lec/2025-08-25.html#the-svd-and-the-2-norm),
as inspected in review274. Here the displayed exact Gram calculation
justifies the specialization to our rows. Hence

    sigma_min(J_n)=min{sqrt(1-|rho|),q_n}
                 =min{epsilon/sqrt(2),q_n}
                 >=min{c_epsilon/sqrt(2),1/sqrt(3)}/n.

Taking C to be this positive minimum proves (1) and the stated
inverse norm. No lower bound for an individual coefficient of c_n,
infinite matrix product, scalar filtered observable or signed
arithmetic sequence has been used or proved.

### Critical audit — step278, 10 November 2026

The entire proof passes the separately approved conceptual audit.
Its exact inputs are L990(5),(13) and C990a(1),(10)-(11),(16).
The previously audited GST compact-bulk and additive phase contracts
are reused at unchanged hypotheses; their general proofs are not
reproved. L991/L992 and the scalar route stops are contrasts only.
The following checks record the load-bearing uniformity issues.

The scaled row norms have phase-independent lower bounds because
||v||_2^2=3/2 and ||w||_2^2=1+cos(psi)^2>=1. Thus the two-sided
constants in (2), and the amplitude constants in (3), can be chosen
before n or its phases. Choosing s by the sign of rho gives exactly
||r||_2=beta_n*epsilon and |lambda|=beta_n/alpha_n for either
orientation, including rho=0. Applying the affine recurrence gives
lambda*n*(p_n(n)-2)+R(2n).r=-2*n, and its middle component gives
p_n(2n)-1=lambda*(p_n(n)-1)+n*r_1. These verify both signs and both
constant corrections in (5). The coefficient-sum bound used for (6)
is valid at n=2 as well as on the tail: 5*n^2 minus that sum
is 3*n^2-6*n+1=3*(n-1)^2-2>0. The products n*alpha_n/M_(1,n)
and n*beta_n/M_(2,n) are bounded uniformly. All remaining constant
terms are bounded by a fixed multiple of sqrt(n)*exp(-n/2).

The nearest-zero argument in (8) holds for every real phase, with
distance in [0,pi/2]. It does not require a preliminary smallness
assumption. Multiplying its first equation by 12/pi and its second
by 2/pi verifies the integer offsets 15-4*n and 2-n and both
negative error signs in (9). In (10), the n^2 terms cancel exactly,
the two cross terms are 52/pi^2 and 117/pi^2, and the remaining
pure coefficient term has order n^-2. Every phase error product is
displayed in (10): linear terms cost at most a constant times n*h;
quadratic terms cost at most 28*L^2*h^2<=56*L^2*h, since h<2.
Because h<=n*h and n*h=n*epsilon+1/n, the stated K bounds them
all. In particular no O(n^-2) error is silently treated as remaining
O(n^-2) after multiplication by an O(n) expression.

The number 169/pi^2 is fixed and nonintegral; no varying-frequency
Diophantine estimate is assumed. Let N_rows and N_phase be onsets
for (2)-(3) and (7), N_exp an onset for sqrt(n)*exp(-n/2)<=n^-2,
and N_def the cofinite-definition onset of C990a. A single integer

    N >= max{2,N_rows,N_phase,N_exp,N_def,ceil(2*K/delta)}

works in (6)-(12). Thus delta<=K*(n*epsilon+1/n) implies
epsilon>=delta/(2*K*n) at every integer n>=N, not merely on a
subsequence depending on epsilon. Constants H,H_1,L,K are chosen
in that order independently of n, before this final N.

Finally exact cross-product orthogonality gives the displayed Gram
matrix, without an asymptotic normalization error. Its least
eigenvalue is min{1-|rho|,q_n^2}; the l1 normalization ensures
q_n>=1/sqrt(3) regardless of the size of d_n. This proves the stated
C/n bound with Euclidean norms and the inverse-norm consequence.
Only the standard SVD theorem is imported from Bindel; the mistyped
weighted-average norm display noted in review276 is not used.

No numerical sample or mathematical script is needed for these exact
checks. The two DAG inputs remain sufficient and unchanged. The
onset and constants remain existential; all three arithmetic output
estimates, interval transport, prime powers, other zeros, both
complements and L984(H) remain unresolved. This is not an RH candidate.

## Mathlib

Full matching Mathlib coverage of this moving corrected joint matrix
and its quantitative conditioning is unchecked. Standard SVD facts,
norm inequalities and the cited GST/Bessel/transcendence inputs are
mathematical references, not claims of a matching formal theorem.
No absence claim or Lean verification is made.
