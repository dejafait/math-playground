# Corollary 997j: scalar damping cannot reduce the exact Gram dual cost

## Hypotheses

Use C997h(1) and its audited injectivity, feasibility and (2), with the
COMPLETE C997c(1),(4)-(6) response. Thus

    J=[15/8,17/8], z_star=1+i/8, n>=2,
    w_n(c)=exp(-An(c-2)^2), deg(P)<=n,
    dmu_P(c)=1_J(c)*w_n(c)*P(c)*exp(in(phi(c)-c))dc,
    H_P(z)=H_n^+(z;mu_P), V(P)=integral_J w_n(c)*|P(c)|dc,
    ell_n(P)=H_P(z_star), phi(c)=arccos(1-c/2)+sqrt(c*(4-c))/2.

Fix ONE A in C997e's admissible range with A<6553600, if this remaining
range is nonempty. Its nonemptiness and a numerical value of C997e's
threshold A_0 are not assumed. All limits below keep A fixed. Retain
both beta terms, both short intervals, slope endpoints and K's -1.

Let S_n={H_P|J: deg(P)<=n}, a subspace of complex L2(J). Use the inner
product <f,g>=integral_J conjugate(f)*g, linear in its second variable.
At a feasible index retain C997h's W_n and Kcal_n, and set R_n=H_(W_n)|J.
This R_n is a band dual vector, not C997a's full quartet response.

For q in L2(J), define its ORIGINAL-TV residual norm by

    eps_n(q)=sup_(P!=0) |ell_n(P)-<q,H_P>|/V(P).

The candidate dual class tested here is

    q=conjugate(alpha)*R_n+r, alpha in C, r perpendicular to S_n. (1)

This allows scalar damping of the exact response representer and any
component invisible to the polynomial response space. It does not
include general changes of individual response directions.

## Conclusion

There are c_*>0 and an onset N_A such that the target's original-TV
operator norm satisfies, for all n>=N_A,

    t_n:=sup_(P!=0) |ell_n(P)|/V(P),
    c_* n^(-3/2) <= t_n <= C_* (n+2),
    c_*=|B_star|/2, C_*=17 exp(17/16)+8 exp(1/2).          (2)

Here B_star!=0 is the audited C997e target constant. In particular
log(t_n)/n tends to zero. The constants bound the original slope norm;
no coefficient norm replaces it.

For every q in (1), at every feasible index,

    eps_n(q)=|1-alpha| t_n,
    ||q||_2^2=|alpha|^2 Kcal_n+||r||_2^2.                 (3)

Consequently, along any unbounded integer subsequence S, existence of
members of (1) satisfying eventually

    ||q_n||_2<=exp(b_n), b_n>=0, b_n/n -> 0,
    eps_n(q_n)<=C_0 exp(-delta n), 0<C_0<infinity, delta>0, (4)

is equivalent to log^+(Kcal_n)=o(n) on S. Indeed (4) forces

    |1-alpha_n| <= (C_0/c_*) n^(3/2) exp(-delta n),
    ||q_n||_2 >= (1-(C_0/c_*) n^(3/2) exp(-delta n))
                                                 *sqrt(Kcal_n) (5)

eventually. Thus scalar damping offers no exponential saving over the
exact dual when an exponentially small original-TV residual is required.

This is a limitation of a specified certificate, not a lower or upper
bound on the ACTUAL Kcal_n, not an obstruction to the whole packet class,
and not a claim that no band dual can work. The continuum minimizer's
TV and band rates remain unestimated. A successful packet with
D_n<=exp(-sigma n) would have Kcal_n>=4 exp(2 sigma n); hence (1) could
not supply the proposed certificate on that subsequence. This last
conditional observation does not prove that such a packet exists.

Step340, 11 November 2026: RESEARCH / REPRODUCTION, outcome EXPLORATION
under unchanged pre-invocation EXPLORE review334. The bounded scalar
dual test yields an exact cost tradeoff but no new packet rate. It is
not reported as a mathematical advance, a new general theorem, or an RH
candidate. The specialization has not received an independent audit.

## Proof

### Existing contracts and the scope of the calculation

Use C997c's audited complex-measure Fubini representation and its bound
|g_n(t)|<=2(n+2)exp(3t/8), t>=0, for the ORIGINAL kernel. That bound
includes the constant subtraction and imports the Laguerre estimate
from NIST [DLMF18.14.8](https://dlmf.nist.gov/18.14.E8).
No asymptotic expansion of g_n is used in the upper estimate below.

C997e(2), audited in step329, supplies the nonzero constant B_star for
the fixed admissible A. Its primary bulk input is M. Vanlessen,
*Strong asymptotics of Laguerre-type orthogonal polynomials and
applications in random matrix theory*,
[math/0504604v2](https://arxiv.org/pdf/math/0504604v2), Theorem2.4(b)
and Proposition5.1; the exact local specialization and all complete
errors are already paid in C997e. We import that local result, rather
than redo its saddle calculation or infer a numerical admissible A.

C997h(2), audited in step339, is the positive definite specialization of
D. Pappas, *Minimization of constrained quadratic forms in Hilbert
spaces*, Ann. Funct. Anal.2(2011), no.1, pp1-12,
[Theorem3.4, pp5-6](https://ftp.gwdg.de/pub/misc/EMIS/journals/AFA/AFA-tex_v2_n1_a1.pdf).
Use also the standard named orthogonal projection theorem for a closed
Hilbert subspace. S_n is finite dimensional, hence closed. These known
contracts were covered by review334. The calculation here checks the
original-TV residual, complex scalar convention and growing-n costs;
it does not reprove the general minimization or projection theorem.
C997h(4)-(5) is not an input.

### The target functional is not exponentially small in original TV

For z_star=1+i/8, |exp(i z_star t)|=exp(-t/8). In the upper interval
of C997c(1), for a single c in J, the absolute density is at most

    4(n+2) exp((t-cn)/4), cn<=t<=c(n+2).

Its integral is at most 8c(n+2)exp(c/2), because the interval has
length 2c and t-cn<=2c. Thus the entire upper contribution obeys

    |H_U(z_star;mu_P)|<=17 exp(17/16)(n+2)V(P).            (6)

For the lower interval use n<=t<=n+2 and c>=15/8 in the SAME density
bound. Its length is 2, so

    |H_L(z_star;mu_P)|
        <=8 exp(1/2)(n+2)exp(-7n/32)V(P).                 (7)

Equations (6)-(7) use absolute integration against the actual |mu_P|;
they keep the lower interval's sign in the defining identity, and
bound it only after splitting that exact identity. Both beta terms
and K's subtraction are included through the g_n bound. No slope
endpoint, branch or lower response has been removed. Finite support
and C997c's Fubini contract justify all integrals. The upper bound in
(2) follows; in fact (7) retains an unnecessary additional decay.

For the lower bound choose P=1. Put Z_n=integral_J w_n(c)dc>0.
Then V(1)=Z_n, and mu_1 is exactly Z_n times C997e's TV-one measure.
Its audited target asymptotic gives

    ell_n(1)/Z_n=n^(-3/2)(B_star+o(1)).                   (8)

For this fixed A there is an N_A after which the last factor has
modulus at least |B_star|/2. This proves the lower bound in (2), and
also ensures the feasible indices needed below. Since log(n)/n tends
to zero, the two bounds in (2) imply log(t_n)/n -> 0. The bounds
are polynomial, not exponentially weak lower bounds on t_n.

### The exact dual and its scalar residual

Use C997h's basis e_j=(c-2)^j, response vector h_j, target column v
and positive definite Gram matrix G. For a coefficient column p,

    ell_n(P)=v^T p, E_n(P)=p^*G p,
    d=G^(-1)conjugate(v), W_n=sum_j d_j e_j.

The audited matrix convention gives

    <R_n,H_P>=d^*G p=v^T p=ell_n(P),
    ||R_n||_2^2=d^*G d=Kcal_n.                           (9)

In particular R_n is the exact representer in S_n. If another q has
the same functional on S_n, then q-R_n is perpendicular to S_n; this
is precisely the orthogonal projection theorem's finite-dimensional
application. Its norm cannot be smaller than sqrt(Kcal_n).

For (1), the inner product is conjugate-linear in its first variable,
so <conjugate(alpha)R_n,H_P>=alpha*ell_n(P). The perpendicular term
vanishes. Therefore

    ell_n(P)-<q,H_P>=(1-alpha)ell_n(P).

Taking the supremum divided by the unchanged V(P) proves the first
identity in (3). Pythagoras proves the second. A complex alpha, a
nonzero invisible component and all degenerate choices alpha=0 or 1
are included. No auxiliary polynomial norm or sampled Gram matrix
is being used.

### Compare actual and required rates

Suppose (4) holds. Divide the residual identity in (3) by the lower
bound in (2); this gives the first inequality in (5). The reverse
triangle inequality |alpha|>=1-|1-alpha| and the norm identity give
the second. Its parenthesis tends to 1, so eventually

    sqrt(Kcal_n)<=2 exp(b_n).

This implies log^+(Kcal_n)=o(n) along S. Conversely, if that rate
holds, take alpha_n=1 and r_n=0. Equation (9) gives zero residual and
norm sqrt(Kcal_n); b_n=(1/2)log^+(Kcal_n) satisfies (4), with any
fixed positive delta and C_0. This proves the stated equivalence.

For the final conditional comparison, C997h(2) alone gives
1/Kcal_n=||H_(P_n)||_2^2. Since |J|=1/4, a closed-band bound
D_n<=exp(-sigma n) implies 1/Kcal_n<=exp(-2sigma n)/4.
This proves the claimed lower bound on Kcal_n without invoking
C997h's unaudited interpolation. Neither D_n's hypothesis nor a
growth bound for the actual Kcal_n has been proved here.

The result stops scalar damping as a way to trade exact-dual norm for
an exponentially small original-TV residual. It leaves open proving
Kcal_n subexponential directly, or constructing a nonscalar dual that
discards costly directions with exponentially small target action in
the original-TV norm. The latter is a proposed continuation, with no
discarded-direction estimate established here. Point bridge, selected
and both-sign transfer, C997a(8), original assay/reconstruction, signed
recovery/complements/regulators, L993, L984(H) and actual-Xi positivity
remain open. No cross-notebook input or numerical certificate is used.

## Mathlib

Full matching coverage of this original-TV response-dual statement has
not been checked and is unknown. Hilbert projection, finite-dimensional
Riesz representation and integral inequalities are supporting general
tools, not a verified matching Mathlib theorem for this packet operator.
No theorem identifier or formal verification is claimed.
