# L068 — Conditional retained pilot-scaled tensor-shell enclosure

## Hypotheses

Retain L066's field N=Q_3(zeta_420,3^(1/7)), with e=14,f=12,
O=O_N, m=m_N, ord_N(3)=14 and the genuine J=log(O^times).
Retain its complete-unit bounds, including the infinite tails and all
unit torsion before logarithm. The retained presentation, reciprocity,
group and global data are unchanged, but no group action theorem is
needed below. Retain L048's changed Tate parameter q_0 with
v_3(q_0)=30. Conditionally assume the native identification K_w=N
and a distinguished pilot representative rho in N with rho^14=q_0.
Neither assumption, nor full initial Theta-data or IUT IV Theorem 1.10's
additional global hypotheses, is established here.

In the repeated-place j=1 packet put

    T=N tensor_(Q_3) N,  P=J tensor_(Z_3) J subset T,
    S=(J/3) tensor_(Z_3) (J/3)=3^(-2)P.

The factors remain labeled 0 and 1, with factor 1 distinguished. Use
the source versions and hypotheses in foundations/04 and foundations/05:
IUT III, May 2020, Definition 1.1(i), pp.23–24, and Remark 1.2.2(i),
p.36, for S; IUT IV, April 2020, Proposition 1.4(iii), pp.13–14,
and Theorem 1.10(v), pp.27–28, for the enclosing modules. Direct
reproductions: [IUT III](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%203.pdf),
[IUT IV](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%204.pdf).
Author-PDF byte identity remains unverified.

Let d_N be the absolute different valuation used there, and set

    k=floor(1/7-2d_N),  E_out=3^k P.

Let Phi range over Q_3-linear automorphisms of T satisfying Phi(P)=P.
This algebraic family is not identified with the native permitted family.

## Conclusion

For every zeta in mu_14(N), including zeta=1, and every such Phi,

    (zeta rho)J subset J,
    Phi((1 tensor zeta rho)S) subset S subset E_out.

Thus the union of these algebraic images is enclosed in the same
module E_out used by the conditional j=1 application of Proposition
1.4(iii). This supplies the scalar stage of the approved step-259 audit.
It does not assert that the native image family is a subset of this
algebraic family, or that all points of S are actual unit/pilot images.
It is a known-method specialization, not an IUT counterexample or a
claim of progress beyond the checked literature. The separate critical
audit of 2026-10-17 passes under exactly these conditional hypotheses.

## Proof

L066, proof parts 1–2 and its separate critical audit, give the complete
bounds m^8 subset J subset m^(-19). The inner bound uses log/exp
at depth 8>14/(3-1); the outer bound covers every unit and the whole
convergent logarithm series, not finitely sampled logarithms.

From rho^14=q_0 and v_3(q_0)=30 one obtains v_3(rho)=15/7,
hence ord_N(rho)=30. Every zeta under consideration has valuation
zero. Therefore

    (zeta rho)J subset (zeta rho)m^(-19)
                 = m^11 subset m^8 subset J.

This uses multiplication of fractional ideals in N. It does not
assume that J is an O-module, or that multiplication by a general
unit preserves J. In particular, rho is an integral field element;
its valuation is nonintegral in the Q_3 normalization, and it is not
a rational scalar.

On pure tensors the map 1 tensor multiplication_by_(zeta rho)
takes (j_0/3) tensor (j_1/3) to
(j_0/3) tensor ((zeta rho)j_1/3), which lies in S by the preceding
inclusion. Finite sums give (1 tensor zeta rho)S subset S.
The identity S=3^(-2)P follows by moving the rational scalar 1/3
from each factor to the tensor product. Since Phi is Q_3-linear and
Phi(P)=P, Phi(S)=S. This proves the first image containment without
commuting Phi with multiplication by rho.

It remains to check the exact target module. Here lambda=15/7,
|I|=2, a_I=2 and d_I=2d_N, so Proposition 1.4(iii)'s integer
exponent is floor(lambda-d_I-a_I)=k. Theorem 1.10(v)'s intermediate
module is

    M_lambda=3^(floor(15/7)-2) 2^(-2)P=(1/4)P=P,

since 4 is a Z_3-unit. The different bound d_N>=(14-1)/14 is
the bound cited from Proposition 1.3(i) and used explicitly in the
proof of Proposition 1.4(iii), printed p.14. Consequently

    1/7-2d_N <= -12/7,  k<=-2,
    S=3^(-2)P subset 3^kP=E_out=3^k M_lambda.

No exact different computation is needed. The enlargement exponent
is nonpositive, as required; more precisely it is at most -2 in this
packet. Taking the union over Phi and zeta preserves the proved
containment. Nothing in this argument supplies a labeled native
factorization of a general image, or extends a partial log-link to a
pilot multiple outside its domain. No log-volume inequality, reverse
membership, global initial-data sufficiency, essentiality or finite
B>=A conclusion is inferred.

### Separate critical audit — 2026-10-17, step 262

**Verdict and scope.** The conditional conclusion passes without repair
or strengthening. The pre-existing SPECIALIZE assessment is
`drafts/literature/2026-10-16-retained-scaled-shell-independent-audit.md`.
Only L066's complete-logarithm estimates and L048's changed-parameter
valuation are mathematical inputs; neither the paired action nor its
container orbit is needed. The following independently checks their
use, rather than importing the native all-image assertion as a premise.

**Complete logarithm bounds.** The cited deep log/exp theorem applies
strictly at depth 8>14/2, giving every element of m^8 as a logarithm.
For each n>=1, put r=v_3(n). The bounds 3^r-14r have values
1,-11,-19,-15 for r=0,1,2,3 and increase strictly for r>=2.
Since n>=3^r, every term of every log(1+x), x in m, has order
at least -19. Moreover n-14 log_3(n) tends to infinity, so the
whole convergent series lies in the closed ideal m^(-19).
L066's audited identity J=log(U_1) covers all units: residue-unit
torsion contributes zero, and primary torsion is retained before
taking log, not removed by an injectivity assumption. Thus both
inclusions m^8 subset J subset m^(-19) concern the complete J.
No sampled lattice or lowest-layer attainment claim is needed here.

**Scalar and labeled tensors.** L048 supplies v_3(q_0)=30 for the
same changed curve. The assumed equation rho^14=q_0 gives
ord_N(rho)=14*(30/14)=30. Any zeta in mu_14(N) has order zero
because 14*ord_N(zeta)=ord_N(1)=0. Multiplication by zeta*rho
therefore takes m^(-19) exactly to m^11. Since 11>=8, this lies
in m^8 and hence J. This proves the required scalar inclusion for
every representative, independently of any unit-stability of J.

The full J is a finite free Z_3-lattice spanning N: the two ideal
bounds ensure fullness and boundedness, and submodules of finite free
Z_3-modules are finite free. A Z_3-basis of J is a Q_3-basis of N;
its pairwise tensors form a Q_3-basis of T. Consequently the abstract
tensor P embeds as the asserted lattice in T, without identifying T
with N or a single field component. Every element of S is a finite
sum of tensors (u/3) tensor (v/3), u,v in J. Acting on the labeled
second factor preserves each such summand's membership in S by the
scalar inclusion. Q_3-linearity and Phi(P)=P then give Phi(S)=S.
The order of these operations is retained; no commutation with rho
or partial log-link is used. Taking arbitrary unions introduces no
closure or infinite-sum assertion.

**Exact source module.** The April 2020 IUT IV reproduction linked
above was reopened at Proposition 1.3(i), statement pp.11–12 and
complete part-(i) proof p.12; Proposition 1.4(iii), statement p.13
and complete part-(iii) proof p.14; and Theorem 1.10(v)'s module
comparison pp.27–28. The tensor-automorphism hypothesis was also
checked in Proposition 1.2, pp.10–11. Byte identity with the author
PDF remains unverified. These checks reuse the assessed source cases,
not a new literature-discovery claim.

Take k_0=Q_3 in Proposition 1.3(i): d_0=0,e_0=1,e_i=14,
so d_N>=13/14. No Galois hypothesis or tame-equality assertion
is needed. For Proposition 1.4(iii), the two labeled finite fields
are N,N in the retained algebraic closure, lambda=15/7=30/14
is admissible, and I*={0,1} contains both exceptional indices.
The definitions give a_i=ceil(14/(3-2))/14=1 and d_I=2d_N.
Thus its precise P-module exponent is k=floor(1/7-2d_N),
not floor(lambda)-d_I-a_I. The bound on d_N gives k<=-2.
For any s in S, writing s=3^(-2)p with p in P yields
s=3^k(3^(-2-k)p); since -2-k>=0 the parenthesis is in P.
This verifies the direction S subset E_out at the exact prescribed
exponent, without enlarging the source module at will.

In the source intermediate module, floor(15/7)-2=0 and 1/4
is a Z_3-unit. Hence M_lambda=P and E_out=3^k M_lambda,
with nonpositive enlargement exponent k. The scalar-shell proof
does not show containment in M_lambda itself; only containment in
S and then E_out is claimed. Theorem 1.10(v)'s native all-image
assertion is not used to prove this algebraic inclusion. A compatible
native factorization, native K_w=N and representative applicability,
full initial data, the extra global hypotheses and essentiality all
remain independent obligations. The original finite B>=A question
is unchanged; no candidate flaw is obtained.

## Mathlib

Full matching conditional enclosure and supporting tensor/lattice,
local different and p-adic logarithm coverage: **not checked**.
No formal verification or absence claim is made. The complete local
logarithm estimates are reused from audited L066, not rederived.
