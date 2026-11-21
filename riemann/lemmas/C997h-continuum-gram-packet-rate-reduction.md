# Corollary 997h: the continuum packet minimizer and its charged band norm

## Hypotheses

Use the COMPLETE response H_n^+(z;mu) from C997c(1),(4)-(6), with
integer n>=2 and the original

    K_(n+2)(t)=(L_(n+1)^(2)(t)-1)/(n+1),
    g_n(t)=K_(n+2)(t)*exp(-t/2)*cosh(3t/8).

Set a=15/8, b=17/8, J=[a,b], z_star=1+i/8, and use C997e's real
phase

    phi(c)=arccos(1-c/2)+sqrt(c*(4-c))/2, c in J.

Fix ONE A in C997e's sufficiently large admissible range, before n.
For any complex polynomial P of degree<=n, put

    w_n(c)=exp(-An(c-2)^2),
    dmu_P(c)=1_J(c)*w_n(c)*P(c)*exp(in(phi(c)-c))dc,
    H_P(z)=H_n^+(z;mu_P),
    E_n(P)=integral_J |H_P(gamma)|^2 dgamma,
    V_n(P)=integral_J w_n(c)*|P(c)|dc.                       (1)

The last expression is the ORIGINAL slope total variation, without a
coefficient-norm substitution. The optimization is over the exact
continuum E_n(P), subject to H_P(z_star)=1. These are hypothetical
slope packets, not actual zeta data. Both beta terms, both short
intervals, both slope endpoints and K's -1 are retained.

## Conclusion

For every n>=2, P -> H_P|J is injective. In the basis e_j(c)=(c-2)^j,
0<=j<=n, define the column vectors and matrix

    h_j(z)=H_(e_j)(z), v_j=h_j(z_star),
    G_(jk)=integral_J conjugate(h_j(gamma))*h_k(gamma)dgamma.

Then G is Hermitian positive definite. If v=0, the target-one constraint
is infeasible; if v!=0, it has a unique minimizer. C997e implies v!=0
for ALL sufficiently large n, with an onset depending on the fixed A.
There is no assertion about feasibility at the remaining finitely many
indices. At every feasible index define

    d=G^(-1)*conjugate(v),
    Kcal_n=v^T*G^(-1)*conjugate(v)>0,
    W_n(c)=sum_(j=0)^n d_j*(c-2)^j,
    M_n=integral_J w_n(c)*|W_n(c)|dc.

The minimizer P_n and its three relevant quantities are exactly

    P_n=W_n/Kcal_n, H_(P_n)(z_star)=1,
    E_n(P_n)=1/Kcal_n, V_n=V_n(P_n)=M_n/Kcal_n,
    D_n=sup_(gamma in J)|H_(P_n)(gamma)|.                  (2)

Kcal_n is a scalar evaluation-kernel value, not the Laguerre polynomial
K_(n+2). The transpose in Kcal_n is intentional: the response is
complex-linear in the coefficient vector.

Put

    T_n=17(n+2)/8, B=17/64,
    Q_n=(n+2)*(17*exp(51/32)*exp(17n/64)
                         +8*exp(3/4)*exp(-3n/32)).        (3)

For each fixed positive integer m there is a finite C_m, independent
of n, A and P, such that the minimizing response satisfies

    D_n <= C_m*[T_n^(1/2)*(Q_n*V_n)^(1/(2m))
                       *Kcal_n^(-1/2+1/(4m))
                       +Kcal_n^(-1/2)].                  (4)

Consequently the approved packet test is equivalent to the following
two simultaneous conditions on an unbounded integer subsequence S:

    log^+(M_n/Kcal_n)=o(n),
    Kcal_n>=exp(kappa*n) eventually on S,
                         for some fixed kappa>0.         (5)

Here log^+(x)=max{0,log(x)}, and o(n) is along S. If (5) holds, then
for every fixed 0<sigma<kappa/2, D_n<=exp(-sigma*n) eventually on S.
Conversely D_n<=exp(-sigma*n) implies Kcal_n>=4*exp(2sigma*n).
The TV condition in (5) is exactly the requested V_n<=exp(a_n),
a_n>=0, a_n/n->0. No favorable rate in (5) is established here.

Step336, completed 11 November 2026: RESEARCH / REPRODUCTION under the
unchanged pre-invocation EXPLORE review334, completed in step335. This
is local progress on feasibility, nullspaces and the charged band norm,
using known optimization and interpolation theorems. It is not a new
general theorem, a successful packet, a subclass obstruction or an RH
candidate. The step339 audit below accepts injectivity, feasibility and
(2) only; the higher-order interpolation and rate reduction remain unaudited.

## Proof

### Imported contracts and purpose of the specialization

Reuse C997c's audited exact Fourier measures and finite-complex-measure
Fubini justification. In particular its proof supplies
|g_n(t)|<=2(n+2)exp(3t/8) for t>=0, including the constant subtraction,
from the Laguerre bound based on [DLMF18.14.8](https://dlmf.nist.gov/18.14.E8).
Use the standard named identity theorem for holomorphic functions,
Fourier-Plancherel theorem on L2(R), and fundamental theorem of calculus.
Compact bounded densities below satisfy Plancherel's hypotheses;
no inversion of an unknown zeta signal is assumed.

Import D. Pappas, *Minimization of constrained quadratic forms in Hilbert
spaces*, Ann. Funct. Anal.2(2011), no.1, pp1-12, published
[primary PDF](https://ftp.gwdg.de/pub/misc/EMIS/journals/AFA/AFA-tex_v2_n1_a1.pdf),
Theorem3.4, pp5-6, in its positive invertible case. The complex
finite-dimensional constraint is consistent and has closed range when
v!=0. The unrestricted singular framework is also covered by
Gorokhov-Stoica, EUSIPCO1998, Theorem1, but is unnecessary after the
local injectivity argument. No projection away from an objective-null
direction is made. The specialization below verifies the conjugations,
original objective and TV; it does not reprove the general theorem.

Import C. Li and K. Zhang, *A note on the Gagliardo-Nirenberg inequality
in a bounded domain*, [arXiv2110.12967v1](https://arxiv.org/pdf/2110.12967v1),
25 October2021 version, Theorem1.3/(1.3)-(1.4), printed p2; its proof
and Lemmas2.1-2.2 are on p3. This is the general derivative-order theorem
already inspected in review334/step335. Its statement and short proof
were checked for the fixed-order application below. No new literature
assessment, sampling theorem, norm equivalence or uniform-in-order
constant is assumed. The response derivative charge is the local
specialization that the general interpolation theorem does not supply.

### The exact response has no polynomial nullspace

For a fixed n and P set

    f_P(c)=exp(-cn/4)*w_n(c)*P(c)*exp(in(phi(c)-c)).

C997c's Fubini representation gives H_P(z)=integral exp(izt)h_P(t)dt,
where

    h_U(t)=-2*g_n(t)*integral_(J intersect [t/(n+2),t/n]) f_P(c)dc,
    h_L(t)= 2*g_n(t)*1_{n<=t<=n+2}*integral_J f_P(c)dc,
    h_P=h_U+h_L.                                          (6)

The densities are bounded and compactly supported, hence in L1 and
L2. Formula (6) retains the lower interval's plus sign. Dominated
differentiation on any compact z set proves H_P is entire: each
fixed derivative contributes a bounded power of t on its finite
support. There is no interchange of limits in n.

Suppose E_n(P)=0. Continuity implies H_P=0 on the whole closed J,
and the identity theorem then gives H_P=0 throughout C. Plancherel
applied to h_P implies h_P=0 almost everywhere. With our convention
||integral exp(ixt)h_P(t)dt||_2=sqrt(2pi)||h_P||_2, so the
normalization does not affect this implication.

Let

    tau=max{bn,a(n+2),n+2}.

Each entry of this maximum is strictly below b(n+2), for every n>=2.
For tau<t<b(n+2), the lower density is absent and the upper integration
interval is exactly [t/(n+2),b]. Therefore on this nonempty open edge

    h_P(t)=-2*g_n(t)*F_P(t/(n+2)),
    F_P(x)=integral_x^b f_P(c)dc.                          (7)

K_(n+2) is a nonzero polynomial of degree n+1. The other real factors
of g_n never vanish, so g_n has only finitely many zeros in this edge.
Equations (7) and h_P=0 almost everywhere imply F_P=0 almost everywhere
on (tau/(n+2),b), hence everywhere there by continuity. The fundamental
theorem of calculus gives f_P=-F_P'=0 on that interval. Its weight
and phase factors are nonzero, so P vanishes on an interval and is
the zero polynomial. This proves injectivity. In particular E_n is a
genuine norm squared on the polynomial space and G is positive definite.
No claim about arbitrary, non-polynomial slope densities is needed.

### Eventual feasibility and the unique minimizer

For P=1, let Z_n=integral_J w_n(c)dc>0. The unnormalized measure in
(1) is Z_n times C997e's TV-one measure. Its audited target asymptotic
therefore gives

    h_0(z_star)=Z_n*n^(-3/2)*(B_star+o(1)), B_star!=0.       (8)

For the fixed admissible A, this is nonzero for all sufficiently large
n. The target functional is then nonzero, hence the constraint is
feasible. Its constant-polynomial feasible point is 1/h_0(z_star).
The original TV of that point is

    Z_n/|h_0(z_star)|<=2*n^(3/2)/|B_star|                  (9)

eventually. Equation (9) is a feasible-point TV bound only; minimizing
E_n does not minimize TV, so it is not assigned to P_n.

For a coefficient column p, the exact objective is p^*G p and the
constraint is v^T p=1. If v=0 there is no feasible p. Otherwise the
positive invertible specialization of the cited quadratic theorem gives
p=G^(-1)conjugate(v)/Kcal_n. To check its complex convention explicitly,
write u=conjugate(v). Then Kcal_n=u^*G^(-1)u is real positive and
v^T p=1. Moreover Gp=u/Kcal_n. For any other feasible p+r,
v^T r=0, whence p^*G r=(v^T r)/Kcal_n=0 and

    (p+r)^*G(p+r)=1/Kcal_n+r^*G r.

Strict positivity makes r=0 the unique minimum. This verifies the
claimed matrix specialization and (2). Since the phase in (1) is
real and Kcal_n>0, taking the absolute density gives V_n=M_n/Kcal_n
exactly. There is no Euclidean-minimum-norm or kernel-complement TV
substitution. All possible finite-n degeneracies are thus accounted for.

### Charge every fixed derivative to the original TV

Here retain any P from (1), writing V=V_n(P). For each c in J, the
upper measure in C997c(4) has variation at most

    8c(n+2)*exp(cn/8+3c/4).

Indeed its interval length is 2c and the bound on g_n gives a density
at most 4(n+2)exp(-cn/4+3t/8). Maximizing on that interval and then
over c<=b gives 17*exp(51/32)*(n+2)*exp(17n/64).
For the lower interval the corresponding bound is

    8*exp(3/4)*(n+2)*exp((3/8-c/4)n)
       <=8*exp(3/4)*(n+2)*exp(-3n/32),

using c>=a. Integrating these bounds against the ORIGINAL |mu_P|
proves

    ||nu_U||_TV+||nu_L||_TV<=Q_n*V,
    supp(nu_U+nu_L) subset [n,T_n].                       (10)

The stronger exponents here merely specialize C997c's same density
calculation from I to J. The subtraction, beta reflection and cutoffs
have not been dropped or replaced by bulk asymptotics.

For each fixed integer m>=1, differentiation of the compact Fourier
integral now yields

    sup_(x in R)|H_P^(m)(x)|<=T_n^m*Q_n*V,
    ||H_P^(m)||_L2(J)<=T_n^m*Q_n*V/2,                    (11)

since |J|=1/4. Also Q_n<=C_0(n+2)exp(Bn), with
C_0=17exp(51/32)+8exp(3/4). These are actual derivative estimates,
not consequences of an uncharged entire-function norm comparison.

### Fixed-order interpolation supplies the closed-band estimate

Apply the cited bounded-domain inequality on the fixed open interval
(a,b), with spatial dimension1, j=0, k=m, q=r=2, p=infinity and
theta=1/(2m). Its scaling condition is

    0=theta*(1/2-m)+(1-theta)/2.

We have 0=j/k<=theta<=1, and m-1/2 is not an integer, so the
exceptional case is absent. Entire H_P belongs to every required
Sobolev space. Apply the real theorem separately to its real and
imaginary parts; their norms are bounded by the corresponding complex
norms, and the triangle inequality only changes a fixed constant.
Continuity includes the closed endpoints in the essential supremum.
Thus, retaining the source's additive term,

    ||H_P||_sup(J)<=C_m*(||H_P^(m)||_2^(1/(2m))
                         *||H_P||_2^(1-1/(2m))+||H_P||_2).

Substitute (11), ||H_(P_n)||_2=Kcal_n^(-1/2), and absorb the
fixed factor 2^(-1/(2m)) into C_m. This proves (4).

Suppose (5) holds. Put a_n=log^+(V_n); then a_n=o(n). For each
FIXED m, the logarithmic upper rate of the first term in (4) is at most

    -kappa/2+(2B+kappa)/(4m),                             (12)

because log(T_n), log(n+2), log(C_m) and a_n are all o(n).
The second term has upper rate at most -kappa/2. Given any
0<sigma<kappa/2, choose a single integer m so large that

    (2B+kappa)/(4m)<kappa/2-sigma.

Only AFTER fixing m take n sufficiently large in S. The strict margin
absorbs both constants and the sum in (4), yielding D_n<=exp(-sigma*n).
No assertion about C_m as m grows with n is made or needed.

Conversely E_n(P_n)<=|J|*D_n^2=D_n^2/4, so (2) gives the stated
Kcal_n>=4exp(2sigma*n). The original TV condition is unchanged.
This proves the equivalence (5), including its subsequence quantifiers.

### What this attempt does and does not certify

The constant feasible point (9), together with (10), gives only

    E_n(P_n)<=C_A*n^5*exp(17n/32),
    Kcal_n>=C_A^(-1)*n^(-5)*exp(-17n/32)                 (13)

eventually, for some fixed C_A>0. To verify the first bound, use
E<=Q_n^2*V^2/4 for that feasible point, (9), and n+2<=2n; minimization
then transfers this upper bound to P_n. Equation (13) is much weaker
than the POSITIVE exponent required in (5). It neither rules out nor
establishes that exponent and says nothing about the minimizer's TV.
There is no informative negative result about the packet class here.

The useful completed input is that finite feasibility/nullspaces and
the continuum-to-closed-band conversion are now explicit. Even a
positive exponential Kcal_n estimate alone would remain insufficient
without subexponential M_n/Kcal_n. Small matrix eigenvalues, a finite
grid or the constant feasible point cannot replace these two costs.
The unmodulated, prescribed atomic, binomial and full-jet stops remain
on their stated scopes; this argument does not impose those designs.

The point bridge, selected/both-sign transfer, C997a(8), original assay,
actual reconstruction, signed recovery, complements, regulators, L993,
L984(H) and L030-L032/C032a remain unresolved. No RH claim or all-measure
obstruction follows. The general matrix/interpolation results are
imported known mathematics; the interpolation and rate reduction remain
unaudited. The minimizer input has the separate limited audit below.

### Independent conceptual audit of the minimizer input — step339

11 November 2026. RESEARCH / REPRODUCTION under the pre-invocation
SPECIALIZE review337, completed in step338. This audit accepts
injectivity, feasibility and (2), without changing their statements.
It does not audit (3)-(5) or their interpolation proof. C997i needs
only the accepted input. The general optimization theorem is known;
the response-specific checks below certify its local applicability.

**No hidden nullspace.** For each fixed n>=2, f_P in (6) is continuous
on the compact J. Its Fourier density is bounded and compactly
supported, including both interval contributions with their displayed
signs. C997c's audited complex-measure Fubini contract gives exactly
(6). Finite support permits differentiation on compact subsets of C
under every defining integral, so H_P is entire. If E_n(P)=0,
continuity gives H_P=0 on J, then holomorphic uniqueness gives H_P=0
on C. Plancherel for the L1-intersection-L2 density implies h_P=0
almost everywhere. No assertion about a limiting sequence in n is
used in any of these implications.

Write a=15/8, b=17/8 and tau=max{bn,a(n+2),n+2}. The three strict
inequalities needed for the edge argument are

    bn<b(n+2), a(n+2)<b(n+2), n+2<b(n+2).

They hold for every n>=2. On tau<t<b(n+2), we have t/n>b,
a<t/(n+2)<b and t>n+2. Thus the lower interval is absent and the
upper integral really is the whole interval [t/(n+2),b]. The
polynomial K_(n+2) has degree n+1 with nonzero leading coefficient;
subtracting 1 cannot remove it. Since the exponential and cosh factors
are positive on this real edge, g_n has only finitely many edge zeros.
Consequently (7) and h_P=0 almost everywhere give F_P=0 almost
everywhere on (tau/(n+2),b), hence everywhere by continuity.
F_P'=-f_P there. All the multiplying weights of P are nonzero, so P
vanishes on this nonempty interval and is identically zero. This also
covers degree strictly less than n and n=2. It establishes G>0 for
every n, without a uniform lower eigenvalue or condition-number claim.

**Feasibility uses exactly the audited normalization.** C997e(1)
has density w_n exp(in(phi-c))/Z_(n,A), with Z_(n,A)>0. Our e_0
has density Z_(n,A) times that measure. Complex linearity therefore
gives (8) with that factor, not its reciprocal. C997e(2) and its
step329 audit give B_star!=0 and an o(1) through all integers for
each fixed admissible A. For large n, |B_star+o(1)|>=|B_star|/2,
so h_0(z_star)!=0, v!=0, and the constant feasible point has the TV
in (9). This establishes neither its energy optimality nor the
minimizer's TV. At earlier indices v=0 means infeasible, while v!=0
is sufficient for feasibility by scaling any basis vector whose
target value is nonzero. No finite index is silently discarded.

**Exact theorem specialization and conjugations.** Rechecked D. Pappas,
*Minimization of constrained quadratic forms in Hilbert spaces*,
Ann. Funct. Anal.2(2011), no.1, 1-12,
[Theorem3.4 and proof, p6](https://ftp.gwdg.de/pub/misc/EMIS/journals/AFA/AFA-tex_v2_n1_a1.pdf),
with the positive square-root/closed-range case on pp5-6. This is
the already assessed source, not a new discovery search. To fit its
endomorphism hypothesis literally, take H=C^(n+1), T=G and
Bp=(v^T p)epsilon_0, with right side epsilon_0, where epsilon_0
is the first coordinate vector. When v!=0, B is rank one, singular
(n+1>=3), bounded with closed range, and the equation is consistent.
G is positive invertible by the argument above, so every source
hypothesis is paid. No singular-objective theorem is imported.

Put u=conjugate(v), R=G^(1/2), w=R^(-1)u and K=w^*w.
Then BR^(-1)=epsilon_0 w^*, whose Moore-Penrose inverse sends
epsilon_0 to w/(w^*w). The cited formula therefore gives
p=G^(-1)u/K, with K=u^*G^(-1)u=v^T G^(-1)conjugate(v)>0.
As a convention check, v^T p=1 and Gp=u/K. If v^T r=0 then
p^*G r=u^*r/K=0, so the exact objective is
(p+r)^*G(p+r)=1/K+r^*G r. This verifies uniqueness and energy
1/K without changing the coefficient convention. The phase is real
on J and K>0, hence the original density's variation is exactly
integral_J w_n|W_n/K|=M_n/K. These are all the identities in (2).
This short matrix computation verifies the source specialization;
it is not a new general constrained-minimization theorem.

The audit establishes a usable exact-minimizer input only. It asserts
no growth of Kcal_n, no bound on M_n/Kcal_n, no C997h(4)-(5) audit,
and no selected-response, actual-Xi or RH conclusion.

## Mathlib

Full matching coverage of this response-specific minimizer and charged
rate reduction has not been checked and is unknown. Supporting formal
coverage of Plancherel, holomorphic uniqueness, constrained positive
quadratic minimization and this bounded-domain interpolation theorem
has not been checked for these exact formulations. No absence claim
or Lean verification is made; the precise informal inputs are above.
