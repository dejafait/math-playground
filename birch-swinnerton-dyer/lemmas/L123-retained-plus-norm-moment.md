# L123 — The retained-plus component as a complete norm moment

## Hypotheses

Let A/Q be a modular elliptic curve, K/Q imaginary quadratic, and p>=5
inert in K and split multiplicative for A. Write L=K_p and V=V_p(A).
Retain Fornea's conductor and residual hypotheses: the conductor is
unramified in K, its inert part is square-free, the residual image
contains SL_2(F_p), and every split-conductor exponent is at most two.
The set cal S={p} is incoherent in Definition 1.2. Use w=infinity,
conductor one, trivial character, and the integral CM embedding and
level choices of the source. In particular, its CM fixed point tau at
p has the standard reduction vertex, and the lift g_v can be 1.

The primary input throughout is Michele Fornea, *Plectic Heegner
classes*, [arXiv:2603.28327v2, 13 April 2026](https://arxiv.org/html/2603.28327v2),
Definitions 4.3, 4.5, 4.8, 4.17 and 4.23, equations (54), (63) and
(68), Corollaries 4.15 and 4.24, and Remark 4.20. Import the construction
with these hypotheses; it is not reproved here. Supporting source
locations used below are equations (20)–(23), Lemma 2.16, Proposition 2.18,
Corollary 2.21 with its
proof, Corollary 3.9, equation (35), Lemma 4.12 and Theorem 4.13.

Put U=H_f^1(L,V). Let lambda:L -> U be the source's split Tate
exponential followed by local Kummer, and set u_1=lambda(1). Let
kappa_0 in U tensor H^1(K,V) be the trivial-character class descended
from L_1/K; L_1 is the conductor-one class field, not identified with K.
Define e_l^+=(1+sigma_p)/2 on U, e_g^+=(1+c)/2 on H^1(K,V), and

\[
D^{++}=(1\otimes\operatorname{loc}_p)
              (e_l^+\otimes e_g^+)\kappa_0.                 \tag{1}
\]

Here c is the outer Gal(K/Q)-action. Fix an algebraic embedding into
Qp-bar and a lift d in the resulting p-decomposition group whose
restriction to K is nontrivial. It induces sigma_p on L. Its action C
on raw global coefficients below need not satisfy C^2=1.

For the actual complete integral use the following notation. Let M be
the p-adically completed, residual-localized coefficient module
(J_{cal S}^{glo})^wedge_{bar rho} of the source, **before** its further
Hecke localization by tensoring with I. Write D^diamond for its diamond
group. Let T be exactly the finite CM index set in equation (68), with
representatives h_t=psi(t), and tau_infinity the fixed CM point at w.
On the compact source domain

\[
 X=\mathbf Z_p^\times\backslash
       [((\mathbf Z_p^2)\setminus p\mathbf Z_p^2)
          \times\mathbf Z_p^\times]
\]

put mu_t=Phi_{cal S}^{glo}(h_t)(tau_infinity) and mu=sum_{t in T} mu_t,
viewed as M-valued measures. A scalar a in Z_p^times replaces
((x,y),z) by ((ax,ay),a^2 z) in this description of X. Set

\[
 f_\tau([(x,y),z])=\tfrac12\log_p((x-\tau y)^2/z),\qquad
 I_\tau=\int_X f_\tau\,d\mu .                              \tag{2}
\]

The branch is log_p(p)=0 on L, agreeing with its usual power series on
principal units. The operation producing kappa is integration in (2),
then tensoring with I, then the diamond-invariant pr_A of (63), Tate
exponential/Kummer, and the source's descent. No pr_A on measure values
or on arbitrary finite integral approximations is assumed.

No analytic-rank, Selmer-dimension, rational-rank or finite-Sha hypothesis
is used in the conclusion. The intended rank-two application additionally
assumes ord L(A/Q,s)=2 and L(A^K/Q,1) nonzero, but this result produces
neither of those hypotheses nor admissible K,p for every A.

## Conclusion

Define continuous functions and coefficient measures by

\[
 N_\tau([(x,y),z])=\frac{(x-\tau y)(x-\bar\tau y)}{z}
       \in\mathbf Q_p^\times,\qquad
 r_\tau=\langle N_\tau\rangle\in1+p\mathbf Z_p,
\]
\[
 \nu=(r_\tau)_*\mu,\qquad
 \nu^\dagger=\nu+C\nu,
 \qquad (C\nu)(B)=C(\nu(B)).                                \tag{3}
\]

The brackets remove the p-power and Teichmuller factors of a nonzero
Q_p scalar. C acts on coefficients only; (3) does not reindex CM points
or posit an involution on M. The complete first logarithmic moment is

\[
 J^\dagger=\int_{1+p\mathbf Z_p}\log_p(u)\,d\nu^\dagger(u).
                                                               \tag{4}
\]

After integration, J^dagger tensor 1 belongs to the domain of pr_A.
Its projected class is regarded in H^1(L_1,V) using the source's
descent, and has trivial character there. With desc denoting the
subsequent cohomological descent to K, define

\[
 R=\operatorname{loc}_p\operatorname{desc}_{L_1/K}
          \big(\operatorname{pr}_A(J^\dagger\otimes1)\big).
                                                               \tag{5}
\]

The precise retained-component identity is

\[
 \boxed{D^{++}=\tfrac14\,u_1\otimes R.}                       \tag{6}
\]

In particular, u_1 is nonzero, R lies in H^1(L,V)^{sigma_p=+1}, and
D^{++}=0 if and only if R=0. No assertion R=0 is made. The second
factor is not asserted to lie in H_f^1(L,V).

The residual is specified by genuine coefficient data, independently
of any rational-determinant conjecture. In a sufficiently fine cell
decomposition of X, the values of mu+Cmu are

\[
 (\mu+C\mu)(\xi X_m)
   =\sum_{t\in T}\left(j_m\varphi_m(P_{t,\xi,m})
               +j_m\varphi_m(dP_{t,\xi,m})\right),\qquad
 P_{t,\xi,m}=[\tau_\infty,h_t\xi]_{K_m}.                    \tag{7}
\]

The maps to M include the source's residual localization and completion.
For every compact open B in 1+p Z_p, nu^dagger(B) is obtained by summing
(7) over the cells in r_tau^{-1}(B). Only the actual Galois-conjugate
points occur; no formula identifying them with another CM representative
is asserted.

For an exact convergent form, let

\[
 a_n=\int_{1+p\mathbf Z_p}((u-1)/p)^n\,d\nu^\dagger(u)\in M.
\]
\[
 J^\dagger=\sum_{n\ge1}(-1)^{n+1}\frac{p^n}{n}a_n,
 \quad
 J^\dagger-\sum_{n=1}^{N}(-1)^{n+1}\frac{p^n}{n}a_n
       \in p^{b_N}M,\quad
 b_N=N+1-\lfloor\log_p(N+1)\rfloor.                         \tag{8}
\]

The bound in (8) is in the **raw** coefficient module. It is not a
certified error bound after Hecke localization, pr_A, descent and
localization; no bounded lattice for that composite is supplied.
Formula (7) is a specification of arithmetic inputs, not their evaluation.

## Proof

**Local/global conjugation on cocycles.** Let a:G_K -> V be a
continuous 1-cocycle, with a(gh)=a(g)+g a(h). Use the action

\[
 (d*a)(g)=d\,a(d^{-1}gd).                                   \tag{9}
\]

Since d normalizes both G_K and its chosen p-decomposition subgroup,
restriction of (9) to the latter is exactly the same formula for the
restricted cocycle. Consequently loc_p(c[a])=sigma_p loc_p([a]).
For h in G_K the cocycle identity gives

\[
 h\,a(h^{-1}gh)=a(g)+(g-1)a(h).
\]

Thus inner conjugation changes a by a coboundary. It follows both that
the global action is independent of the chosen lift and that its square
is the identity on H^1(K,V). The identical argument in the local group
gives the local involution. There is no inference that d^2=1 in G_Q or
that C^2=1 on M. In particular loc_p e_g^+=e_loc^+ loc_p, with the local
projector acting on the entire local H^1.

**Coefficient action and the domain of projection.** K^ab is stable
under G_Q: conjugation sends a finite abelian extension of K to another
such extension. The Jacobians, transition maps, Hecke correspondences
and maps varphi_m in the source's (20)–(23) are over Q. They therefore
commute with d. The residual summand is preserved, because the Hecke
operators commute with G_Q. This defines a continuous Z_p-linear C on
M commuting with its Hecke and diamond actions. It acts trivially on
the scalar field in a tensor and on I, unless a separate scalar action
is explicitly specified. Integration commutes with C: this holds for
locally constant integrands by finite additivity and then for continuous
integrands by p-adic completion.

The naturality needed for pr_A is also coefficient naturality, not a
pointwise extension of its domain. In Corollary 2.21 the construction
starts with Kummer, uses restriction/inflation isomorphisms and diamond
invariants, and then uses the Galois-equivariant ordinary transition
isomorphisms displayed in its proof. Kummer is natural: if [p^n]Q=P,
the cocycle g -> gQ-Q for P transforms under d into the cocycle for dP
by (9). Restriction, invariants and transition maps commute with this
action; the inverses of bijective equivariant maps also commute. The
Hecke A-specialization and the map on Tate modules used in (63) are
maps of G_Q-representations. Hence pr_A(CB)=d*pr_A(B) **for B in its
stated invariant domain**, where d* is the chosen lift action on the
cohomology of the field of definition. Only after descent to K is this
the involution c. This does not define pr_A(mu(B)) for a cell B.

**Scalar projection.** The branch log_p commutes with the nontrivial
sigma of L/Q_p: the p-power is fixed, roots of unity are killed, and
the power series has Q_p coefficients. Therefore

\[
 f_\tau+\sigma(f_\tau)
   =\log_p\!\left(\frac{(x-\tau y)(x-\bar\tau y)}z\right)
   =\log_p(r_\tau).                                        \tag{10}
\]

All arguments of the logarithm are nonzero, since tau is not rational
over Q_p and (x,y) is nonzero. The norm ratio is unchanged under
((x,y),z) -> ((ax,ay),a^2z), so (3) is well defined on X. It is continuous
there. Passage to principal units is continuous on Q_p^times.

Let J=integral log_p(u) dnu. Equation (10) gives
1 tensor J=(1+sigma tensor 1)I_tau in L tensor M. This calculation
uses g_v=1, so the coefficient twist in Definition 4.8 is trivial. The
same representative is used in every summand of (68); no coordinate
change and no discarded constant are involved.

For split multiplicative A, its Tate parameter q is in Q_p and its
Tate uniformization is over Q_p. The logarithm on the Tate quotient is

\[
 \log_q(a)=\log_p(a)-\frac{v_p(a)}{v_p(q)}\log_p(q).
\]

It commutes with sigma, as do uniformization and Kummer. Thus lambda
intertwines sigma with sigma_p. The source's Tate isomorphism implies
that lambda is a Q_p-linear isomorphism onto U. Consequently U^+ is
the line Q_p u_1 and u_1 is nonzero. No Tate-parameter correction has
been omitted: log_p is the branch in (2), and lambda retains the full
log_q inverse used by the source.

**Full integral, invariance and descent.** Corollary 4.15 makes
I_tau tensor 1 diamond invariant after integration and tensoring with I.
The scalar action sigma commutes with diamonds. Therefore (10) places
J tensor 1 in the invariant subspace as well: the inclusion Q_p -> L is split
by half the trace, so invariance of 1 tensor J implies invariance of J.
The coefficient action C preserves that subspace. To identify it with
the actual domain of (63), use Lemma 4.12, not an unstated commutation
of invariants and tensor products. The map T_{bar rho} -> I is a flat
localization, so the lemma gives the natural isomorphism

\[
 M^{D^\diamond}\otimes_{\mathbb T_{\bar\rho}}\mathbb I
       \ \simeq\
 (M\otimes_{\mathbb T_{\bar\rho}}\mathbb I)^{D^\diamond}.
\]

Its naturality makes it commute with the T-linear C. Thus J^dagger
tensor 1=(J+CJ) tensor 1 can indeed be projected by (63). No corresponding
domain statement is made for a raw cell value or partial moment sum.

By the source's equation (68) and Corollary 4.24, applying pr_A and
lambda to I_tau tensor 1 gives the trivial-character class over L_1.
The scalar operation (1+sigma) does not change its field of definition
or character. More explicitly, let ell:U -> Q_p be
Tr_{L/Q_p} composed with lambda^{-1}, and let kappa_{L_1} be the
source class before the final descent to K. Then

\[
 B=\operatorname{pr}_A(J\otimes1)
   =(\ell\otimes1)\kappa_{L_1},
\]

where on the left the initial value in H^1(K^ab,V) is understood by
restriction. The equality first holds there by (10) and Definition
4.17; its right side supplies a lift to H^1(L_1,V), fixed by
Gal(L_1/K). This lift is unique. Indeed Lemma 2.16 gives
A[p]^{G_{K^ab}}=0 over the solvable extension K^ab/Q, with
the residual hypothesis retained. A nonzero fixed vector in V could
be scaled to a primitive vector of T_p(A), giving a nonzero fixed
class modulo p, a contradiction. Thus V^{G_{K^ab}}=0, and
inflation-restriction makes restriction from
H^1(L_1,V) injective. Thus no descent of a raw coefficient or moment
is being inferred. This
conductor-one ring class field is stable under conjugation, since its
defining class-field subgroup is stable, so L_1/Q is Galois. C on the
projected class is conjugation by d. In this paragraph write d* for
that action over L_1 (it need not be an involution there). Naturality
gives pr_A(J^dagger tensor 1)=B+d*B.

Over Q_p, restriction gives
H^1(K,V) isomorphic to H^1(L_1,V)^{Gal(L_1/K)}: the higher cohomology
of the finite group with Q_p coefficients is zero by averaging, and
inflation-restriction applies. Its inverse is equivariant under d
because restriction is. Equivalently, it is corestriction divided by
[L_1:K] on the invariant subspace. This division is permitted even if
p divides that degree. This justifies precisely the desc in (5),
without a descent of the raw measure to K.

The first plus projector applied to kappa_0 now gives
one half of u_1 tensor desc(B), by (10). The second plus projector
adds its c-conjugate, namely u_1 tensor desc(d*B) with the same first
factor 1/2, and divides by two once more. Localizing gives
(6) with the factor 1/4. Equation (9) shows that R is locally plus.
Tensoring with a nonzero vector over Q_p is injective, proving the
stated equivalence with R=0. It adds no vanishing information.

**An arithmetic description of what remains.** Corollary 3.9 gives
mu_t(xi X_m)=j_m varphi_m(P_{t,xi,m}). As these maps are over Q, acting
by d gives j_m varphi_m(dP_{t,xi,m}), proving (7). The coset partitions
refine to the profinite topology of X. A compact open inverse image
r_tau^{-1}(B) is therefore a finite union of cells at a sufficiently
large level. This proves the assertion about nu^dagger(B), with the
full CM sum and the coefficient action retained.

For u in 1+p Z_p write u=1+pv. Uniformly for v in Z_p,
log_p(1+pv)=sum_{n>=1}(-1)^{n+1}p^n v^n/n. Every term has valuation
at least n-v_p(n), which tends to infinity. For n>N,

\[
 n-v_p(n)\ge n-\lfloor\log_p n\rfloor
       \ge N+1-\lfloor\log_p(N+1)\rfloor=b_N.
\]

The second inequality holds because the integer-valued function
n-floor(log_p n) is nondecreasing. The remainder divided by p^{b_N}
is a continuous Z_p-valued function. Integrating it into the complete
Z_p-module M proves (8). This justifies the one interchange of a limit
and integration used here by uniform convergence before tensoring with
I. It does not interchange an infinite sum with Hecke localization.

**What this rules out, and what it does not.** The kernel log_p N_tau
is fixed by tau <-> bar(tau), rather than changing sign. At the valid
points [(1,0),1] and [(1,0),1+p] of X it is respectively 0 and
-log_p(1+p). The latter is nonzero: the leading term has valuation one
and every remaining logarithmic-series term has valuation at least two.
Thus total mass zero cannot by itself annihilate this kernel. For
example, the formal scalar measure delta_{[(1,0),1+p]} minus
delta_{[(1,0),1]} has mass zero but a nonzero log-norm moment. This is
only a test of the mass-only inference. It is **not** the arithmetic
CM measure, need not satisfy its diamond/Hecke constraints, and is
not a counterexample to D^{++}=0 or to BSD.

For cal S={p}, Theorem 4.13 kills the complete constant integral after
Hecke localization. Its omitted-coordinate hypothesis does not kill
the nonconstant function (10). Theorem B controls (1-sigma_p)kappa
in the split case, not the plus component. Likewise the conjugation
statement in [Fornea–Gehrmann, arXiv:2311.03100v2, Corollary 2.9 and
Section 2.2.5](https://arxiv.org/html/2311.03100v2) concerns the mock
invariant; it supplies no sign for the coefficient moment (4).

An exact proof nu^dagger=0 from the actual point relations (7) would
be a sufficient arithmetic cancellation, independently of conjectural
plectic rationality. A nonzero finite coefficient of nu^dagger would
only refute that stronger measure identity. Neither a nonzero raw
moment nor a finite raw truncation proves R nonzero; the projection,
descent and localization can kill it. Conversely a zero finite
truncation proves no exact vanishing. These distinctions are necessary
before any computational continuation; none is carried out here.

This is a REPRODUCTION of the source definitions with an elementary
explicit residual calculation, not a novelty claim, a nonvanishing
result or a new BSD case. No rational determinant, tensor alternation,
finite Sha or global Selmer membership is imported. L005 and L122 motivate
the hoped-for strict-Kummer application but are not inputs to this
proof; their good-reduction hypotheses are not silently changed.
The independent rationality and multiplicative-prime rank gaps remain.

**Separate audit (step 515, 2026-10-26).** The conceptual audit accepts
(6)–(10) as a formal reduction under the stated source inputs. The
explicit extraction by ell above clarifies the initial descent; the
finite descent still uses Q_p coefficients, with no assumption that
p is prime to [L_1:K]. Coefficient C is never an involution before
descent, and neither finite cells nor truncated moments are passed
through an undefined pr_A. Both projector factors and the raw tail
bound pass. No arithmetic moment, vanishing, nonvanishing or stronger
error bound is certified by this audit. The audited reduction is still
an unevaluated diagnostic, not a new arithmetic input closing the gap.

## Mathlib

The full source construction and this norm-moment diagnostic: **not
checked**. Supporting cohomological naturality, p-adic integration,
Tate uniformization and uniform-series coverage: **not checked**.
The cited primary theorems are mathematical inputs, not claims of
matching Mathlib theorems. The separate step-515 audit accepts the
formal reduction only; no arithmetic vanishing is asserted.
