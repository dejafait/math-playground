# Corollary 997k: the response spectral cutoff pays its norm but leaves a target spectral tail

## Hypotheses

Use C997h(1)'s COMPLETE C997c(1),(4)-(6) response, and the audited
injectivity in C997h's step339 section. Put

    J=[15/8,17/8], |J|=1/4, z_star=1+i/8, n>=2,
    w_n(c)=exp(-An(c-2)^2),
    phi(c)=arccos(1-c/2)+sqrt(c*(4-c))/2,
    X_n={w_n P: P complex, deg(P)<=n} subset L2(J),
    V(f)=integral_J |f(c)|dc,
    dmu_f(c)=1_J(c)*f(c)*exp(in(phi(c)-c))dc,
    T_n f=H_n^+(.;mu_f)|J, ell_n(f)=H_n^+(z_star;mu_f).

Fix ONE A in C997e's admissible range with A<6553600, if this range
is nonempty. Its nonemptiness is not assumed. All constants and limits
keep A fixed. Since phi is real, V(f) is exactly the original slope TV.
Use inner products <f,g>=integral conjugate(f)*g, linear in the second
variable, in both slope and band spaces. No coefficient norm is used.

Let b_n in X_n be the Riesz vector of ell_n. The positive operator
T_n^*T_n has an orthonormal basis u_j, 0<=j<=n, with positive
eigenvalues s_j^2. Put v_j=T_n u_j/s_j and a_j=ell_n(u_j). Thus
the v_j are orthonormal in the band space and

    b_n=sum_j conjugate(a_j)*u_j.

For tau_n=exp(-sqrt(n)), retain s_j>=tau_n and discard s_j<tau_n.
Define

    q_n=sum_(s_j>=tau_n) conjugate(a_j)/s_j * v_j,
    Pi_-=1_{[0,tau_n^2)}(T_n^*T_n),
    beta_n=||Pi_- b_n||_2=(sum_(s_j<tau_n)|a_j|^2)^(1/2),
    eps_n=sup_(0!=f in X_n) |ell_n(f)-<q_n,T_n f>|/V(f).    (1)

Here q_n is a band dual, not the quartet kernel with a similar symbol.
Both beta terms, both short intervals, slope endpoints and K's -1
are retained in every response. These are hypothetical slope measures.

## Conclusion

Set C_star=17 exp(17/16)+8 exp(1/2). For every n>=2,

    ||q_n||_2 <= (C_star/2)*(n+2)*exp(sqrt(n)).              (2)

Define the actual slope-norm comparison constant

    B_n=sup_(0!=f in X_n) ||f||_2/V(f).

For each epsilon>0 there is D_(epsilon,A)<infinity, independent of n,
such that

    2<=B_n<=D_(epsilon,A)*exp(epsilon*n),
    2*beta_n<=eps_n<=B_n*beta_n.                           (3)

In particular log(B_n)/n tends to zero. Along any unbounded integer
subsequence, an exponential upper bound with some positive rate for
eps_n exists if and only if one exists for beta_n; the rates need not
be identical. The explicit implications are

    eps_n<=C exp(-delta*n) => beta_n<=(C/2)exp(-delta*n),
    beta_n<=C exp(-delta*n)
       => eps_n<=C D_(delta/2,A) exp(-delta*n/2).           (4)

IF the second hypothesis in (4) holds, every sequence with
ell_n(f_n)=1 and V(f_n)<=exp(o(n)) on that same subsequence obeys

    sup_J |T_n f_n|
       >= [4*(1-o(1))/(C_star*(n+2))]*exp(-sqrt(n)).       (5)

It therefore cannot have uniform suppression exp(-sigma*n) for any
fixed sigma>0. This implication is conditional: no exponential bound
for the ACTUAL beta_n is established. The only unconditional bound
obtained for it here is beta_n<=(C_star/2)*(n+2), which does not
decide either required exponential rate or a conflicting lower rate.

Step341, 11 November 2026: RESEARCH / REPRODUCTION, outcome EXPLORATION
under unchanged ready EXPLORE review334. The retained dual cost is
paid and the original-TV residual is reduced to an exact target spectral
tail. This is a known-tool specialization, not a packet construction,
packet obstruction, new general theorem, or RH advance. No independent
audit of this specialization has been performed.

## Proof

### Existing contracts and the required norm specialization

C997h's step339 audit gives injectivity of the complete response on
polynomials at each n, hence also on X_n because w_n never vanishes.
It gives no singular-value rate. Finite-dimensional spectral and Riesz
representation theorems therefore apply with s_j>0. They are used in
their standard named forms, not reproved. Eventual nonvanishing of the
target is also audited in C997h, but (1)-(4) do not require it: if the
target is zero, b_n=q_n=0. A target-one sequence is then infeasible.
Eigenvalue multiplicities cause no ambiguity: the spectral projection
and q_n are independent of orthonormal choices within each eigenspace.
An eigenvalue exactly at the threshold is retained.

The norm input is T. Bloom, N. Levenberg, V. Totik and F. Wielonsky,
*Modified logarithmic potential theory and applications*,
[arXiv:1502.06925v2](https://arxiv.org/pdf/1502.06925v2),
Definition4.10, Theorem4.13, especially (4.15), and Example4.14,
printed pp16-18,21-23. Its complete proof and applicability were
inspected in review329 and reused by review334. Specialize K=J,
mu=Lebesgue measure on J, f=g=identity in the source's function class,
q_k=1 and k=n. The source's f and q_k are unrelated to our slope
function and dual. The interval is strongly regular and has the
required uniform lower mass in small disks, including at its endpoints.
An enclosing disk verifies its holomorphic-domain requirement.
The fixed field is Q(c)=A(c-2)^2, continuous and real on J.
Every complex polynomial of degree at most n is allowed. Thus for
every eta>0 the cited weighted L1 Bernstein-Markov theorem gives

    ||w_n P||_infinity
       <=C_(eta,A)*exp(eta*n)*integral_J w_n|P|.           (6)

This is an import with its original integral norm; it is not a
response-norm equivalence. No A_n or uniform constant in A is claimed.
The following L2 conversion, cutoff convention and residual calculation
are the needed specialization. C997h(4)-(5) and unaudited C997j are
not premises. Rechecking the short target bound below keeps this
calculation independent of C997j; no general theorem is reproved.

### Pay the target vector in the actual slope Hilbert space

C997c's audited bound for the original kernel is

    |g_n(t)|<=2*(n+2)*exp(3t/8), t>=0.

It includes K's constant subtraction and imports the Laguerre estimate
from [NIST DLMF18.14.8](https://dlmf.nist.gov/18.14.E8). At z_star,
|exp(i*z_star*t)|=exp(-t/8). For a single c in J, the absolute
integrand in either short interval of C997c(1) is consequently at most

    4*(n+2)*exp((t-cn)/4).

On the upper interval its length is 2c and t-cn<=2c, so its integral
is at most 8c*(n+2)*exp(c/2)<=17 exp(17/16)*(n+2).
On the lower interval its length is 2 and
t-cn<=2-(7/8)n, giving 8 exp(1/2)*(n+2)*exp(-7n/32).
Absolute integration against |mu_f| therefore proves

    |ell_n(f)|<=C_star*(n+2)*V(f)
              <=(C_star/2)*(n+2)*||f||_2.                (7)

The last step is Cauchy-Schwarz on an interval of length 1/4.
All integrals are on compact rectangles and use C997c's audited
finite-complex-measure Fubini contract. No asymptotic branch, reflected
beta contribution, endpoint or lower response is omitted. Riesz
representation now gives ||b_n||_2<=(C_star/2)*(n+2).

### The cutoff and original-TV residual are exact

Write f=sum_j f_j u_j, so T_n f=sum_j s_j f_j v_j and
ell_n(f)=sum_j a_j f_j. With the stated complex convention,

    <q_n,T_n f>=sum_(s_j>=tau_n) a_j f_j,
    ell_n(f)-<q_n,T_n f>=<Pi_- b_n,f>,
    ||q_n||_2^2=sum_(s_j>=tau_n)|a_j|^2/s_j^2
                         <=tau_n^(-2)*||b_n||_2^2.       (8)

Together with (7) this proves (2). In particular the norm allowance
is actually subexponential: sqrt(n)+log(n+2)+O(1)=o(n).

For each f in X_n, Cauchy-Schwarz gives V(f)<=||f||_2/2.
Also (6) with eta=2epsilon gives

    ||f||_2^2<=||f||_infinity*V(f)
       <=C_(2epsilon,A)*exp(2epsilon*n)*V(f)^2.

Thus (3)'s assertion for B_n holds with
D_(epsilon,A)=sqrt(C_(2epsilon,A)), enlarged if necessary.
The upper residual estimate follows from (8) and
|<Pi_- b_n,f>|<=beta_n*||f||_2<=beta_n*B_n*V(f).
For the lower estimate, if beta_n>0 take f=Pi_- b_n. The numerator
is beta_n^2 and V(f)<=beta_n/2, so eps_n>=2beta_n.
If beta_n=0 both sides are zero. This proof does not assume that the
spectral projection is contractive in L1. Such an assumption would be
unjustified; the actual comparison constant B_n is explicitly paid.
Equations (3)-(4) follow, including common zero cases without taking
the logarithm of zero.

### Actual bounds versus the required rate

Under the conditional exponential bound for beta_n, (4) gives an
exponential residual bound. For any sequence as in (5),
eps_n*V(f_n) tends to zero. Consequently (8) and Cauchy-Schwarz give

    1<=||q_n||_2*||T_n f_n||_2+eps_n*V(f_n)
      <=(C_star/2)*(n+2)*exp(sqrt(n))*||T_n f_n||_2+o(1).

Since ||T_n f_n||_2<=sup_J|T_n f_n|/2, this proves (5).
The response is continuous, so the supremum includes both closed
endpoints. No derivative interpolation or unaudited C997h rate
reduction is needed for this LOWER bound. Its comparison with
exp(-sigma*n) is strict eventually for every fixed sigma>0.

This calculation does not evaluate beta_n for the complete operator.
Injectivity supplies s_j>0 at each fixed n, not a lower bound by
exp(-sqrt(n)); the target bound (7) supplies no small projection onto
the discarded eigenspaces. The unmodulated target asymptotic likewise
does not specify this projection. Thus (7)'s polynomial upper bound
for beta_n is an insufficient estimate, not a conflicting lower rate
and not a proof that this cutoff fails. No finite sampled spectrum,
coefficient norm or auxiliary L2 residual is substituted for (1).

The original point bridge, selected/both-sign transfer, C997a(8),
original assay/reconstruction, signed recovery/complements/regulators,
L993, L984(H) and L030-L032/C032a remain open. No cross-notebook input,
mathematical script or numerical certificate is used.

## Mathlib

Full matching coverage of this exact-response cutoff and original-TV
residual has not been checked and is unknown. Finite-dimensional
spectral decomposition, Riesz representation and Cauchy-Schwarz are
supporting tools, not a verified matching Mathlib theorem. No theorem
identifier or formal verification is claimed for the weighted norm
import or the packet specialization.
