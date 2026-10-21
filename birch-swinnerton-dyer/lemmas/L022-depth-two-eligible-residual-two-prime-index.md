# L022 — Depth-two eligible residual two-prime index

## Hypotheses

Let E/Q be non-CM and p >= 5 be good ordinary. Assume that E[p] is
surjective, p divides neither #E(F_p), the Manin constant nor any
Tamagawa factor, and E(Q_p)[p] = 0. Put
S = Sel(Q,E[p^infinity]) with classical Kummer local conditions.
Grant corank_Z_p S = 2 and S/S_div = 0, where S_div is the maximal
divisible subgroup. Grant also a nonzero residual Kurihara number
somewhere in Sakamoto's N_(1,0). These are precisely L021's assumptions
with the additional zero finite quotient; neither rational rank two nor
finite p-primary Sha is assumed.

Use the Neron-period normalization and the coefficient-compatible
Kato-derived systems of Sakamoto, *p-Selmer group and modular symbols*,
Doc. Math. 27 (2022), 1891--1922, DOI 10.4171/DM/X21, received
2022-05-13, revised 2022-07-20. Fix the same generators of G_ell and
compatible singular-quotient trivializations at common indices.
The application is covered by the saved
[SPECIALIZE assessment](../drafts/literature/2026-10-05-depth-two-prime-restriction.md).

Write R_m = Z/p^m Z and T_m = E[p^m]. At cyclotomic level zero,

\[
\mathcal P_{2,0}=\{\ell\text{ of good reduction}:\quad
  E(\mathbf F_\ell)[p^2]\simeq\mathbf Z/p^2\mathbf Z,
  \quad\ell\equiv1\pmod{p^2}\},
\]

and N_(2,0) is its set of square-free products. Write kappa^(m) for
Sakamoto's kappa_(xi,m,0), delta_m(d) for its scalarized system
evaluation, and tilde-delta(d) for the mod-p Kurihara number.
Divisor-minimal means nonzero tilde-delta at the index and zero at every
proper positive divisor. No depth-two eligible witness is assumed.

## Conclusion

There are distinct primes ell_1,ell_2 in P_(2,0) such that
N = ell_1 ell_2 is divisor-minimal for the residual Kurihara collection.
With the coefficient-compatible normalizations,

\[
\widetilde\delta(N)\ne0,\qquad
\widetilde\delta(e)=0\ (e\mid N,\ e<N),\qquad
\delta_2(N)\in R_2^\times.
\tag{1}
\]

Thus the eligible-index premise of L015 can be supplied conditionally
under the present assumptions. The primes are produced existentially;
they are not arbitrary prescribed primes. The index is minimal for
residual nonvanishing, not necessarily for nonzero depth-two scalars:
proper divisors may have nonzero depth-two scalars in pR_2.
No elimination of the finite quotient from weaker assumptions, rational
membership, rational-rank lower bound, complex-order comparison or
higher-depth eligibility of these same primes is concluded.

## Proof

**Import the systems and the depth-two detector.** The arithmetic
hypotheses meet Section 1.1 of Sakamoto, p. 1892: p > 3, ordinary
reduction, surjective residual representation, and p prime to #E(F_p)
and all Tamagawa factors. The additional Manin and local-torsion
conditions are retained for L021. At (m,n)=(2,0), Section 2.3, p. 1902,
has R=R_2 and T=T_2, and its prime set is exactly the set above.
The classical structure is Cartesian by Corollary 2.15 and self-dual
by Definition 2.4; its residual core rank is consequently zero.

Import [Theorem 3.17 and Proposition 3.19, pp. 1915--1916](https://ems.press/content/serial-article-files/29299?nt=1#page=25).
By [Lemma 4.2, p. 1917](https://ems.press/content/serial-article-files/29299?nt=1#page=27),
the granted residual Kurihara nonvanishing is residual system-scalar
nonvanishing. Proposition 3.19 therefore makes kappa^(2) a basis of
KS_0(T_2,F_cl). We use its explicitly constructed inverse-limit family
and canonical projections, not separately chosen bases at each level.

By [Remark 2.21, p. 1904](https://ems.press/content/serial-article-files/29299?nt=1#page=14),
applied to the self-dual residual classical structure, choose
d in N_(2,0) with H^1_(F_cl(d))(Q,E[p])=0. More precisely, the
remark gives vanishing for F_cl^*(d); this equals F_cl(d) because
F_cl is self-dual. At depth two, Definition 2.3 gives
(F_cl(d))^* = F_cl^*(d) = F_cl(d). Apply Lemma 2.2, p. 1897,
to this dual structure, with its propagated residual conditions:
the inclusion E[p] -> T_2 identifies the residual Selmer group
with H^1_(F_cl(d))(Q,T_2)[p]. Hence that p-torsion group is zero,
and the depth-two group is zero (a nonzero group killed by p^2
has nonzero p-torsion). These are the transverse conditions at d,
not strict conditions at d or an assertion that arbitrary global
Selmer reduction is surjective. Definition 2.3 and Section 2.3
use the same transverse extension at both depths; classical
conditions are Cartesian by Corollary 2.15.
[Theorem 2.20(2), p. 1904](https://ems.press/content/serial-article-files/29299?nt=1#page=14)
now gives

\[
R_2\delta_2(d)=\operatorname{Fitt}_{R_2}^0(0)=R_2,
\tag{2}
\]

so delta_2(d) is a unit. This is precisely the unit-detection use in
the proof of Corollary 2.22. Injectivity of the scalar evaluation map
alone would not justify (2). We import this source's depth-dependent
existence theorem, without a new Chebotarev or connectivity argument.

**Check the common-index scalar map.** For every ell in P_(2,0),
taking p-torsion of E(F_ell)[p^2] gives E(F_ell)[p] cyclic of order p,
and the congruence modulo p^2 implies the congruence modulo p. Hence
P_(2,0) is contained in P_(1,0). Every depth-two index and each of its
divisors is a common index for both systems.

Section 2.3 defines G_d as the tensor over Z of the groups
G_ell = Gal(Q(ell)/Q), where Q(ell) is the maximal p-subextension of
Q(mu_ell). Fix generators g_ell and put g_d = tensor_(ell|d) g_ell,
with g_1=1. Write #G_ell=p^(a_ell); eligibility gives a_ell>=2.
The tensor of cyclic groups Z/p^(a_ell) is cyclic of order
p^(min a_ell), generated by g_d. Thus, for m=1,2,

\[
R_m\longrightarrow R_m\otimes_{\mathbf Z}G_d,\qquad
a\longmapsto a\otimes g_d
\tag{3}
\]

is an isomorphism, also when d=1. The canonical scalar-coefficient
map sends a tensor g_d to (a mod p) tensor g_d. It is ordinary
reduction R_2 -> R_1 under (3); it does not send g_d to p g_d.

The proof of Proposition 3.19, p. 1916, places the constructed family
in the inverse limit of the system modules under their canonical
projections. On a common pair (d,q), these use the coefficient map
[p]:E[p^2]->E[p] and the unchanged G_d. The singular-quotient maps
and their compatible trivializations commute with this projection;
these are the Section 2.3 local modules and Section 2.4 scalar maps.
To check the normalization concretely, the unramified module is
T_m/(Fr_q-1)T_m. Reduction of this presentation gives a surjection
from its free rank-one R_2 module to its rank-one R_1 module.
The coefficient-natural finite-singular comparison of Section 2.3,
with the same generator of G_q at both depths, gives the corresponding
surjection on singular quotients. The reduction of an R_2 basis
therefore supplies the R_1 basis. In these bases the singular map is
reduction, with no p factor. This verifies the trivializations used
in the scalar computation, rather than identifying maps by dimension
alone.
In particular, evaluate using any q in P_(2,0) coprime to d. Such
auxiliary primes are available: Remark 2.21 provides infinitely many
indices in N_(2,0), so their prime supports cannot all lie in a fixed
finite set. The definition delta_m(d)=v_q(kappa^(m)_(d,q))
on p. 1904 and the inverse-limit compatibility give

\[
\delta_1(d)=\delta_2(d)\bmod p.
\tag{4}
\]

The scalar is independent of the evaluating q by that definition.
The same formula holds for every divisor of d. Compatible changes
of the generators or quotient bases multiply scalars by units; the
unit assertion and residual vanishing are invariant. Equation (4)
is downward coefficient reduction, not coefficient inclusion
E[p]->E[p^2]. That inclusion must not be substituted here.

There is also a direct check of (4) for the actual constructed
family, independent of any inference from ranks of local modules.
Use [Theorem 3.17, Lemma 3.13 and Definition 3.15, pp. 1913--1915](https://ems.press/content/serial-article-files/29299?nt=1#page=23).
At level n=0 let H_d = Gal(Q(d)/Q), put
N_d = sum_(sigma in H_d) sigma in Z_p[H_d], and let c_d be
the common specialization to Z_p[H_d] of the rank-zero Euler
system (tilde-xi_(K_infinity)) in Theorem 3.17. Fix the derivative
operator D_d with the same g_ell at both depths. The source's
scalar construction and invariant-derivative assertion give unique
A_m(d) in R_m with

\[
D_d c_d\bmod p^m=A_m(d)N_d\quad\hbox{in }R_m[H_d],
\qquad \delta(\kappa^{(m)})_d=A_m(d)\otimes g_d.
\tag{5}
\]

Uniqueness here does not require the order of H_d to be invertible:
the coefficient of each group element in a N_d is a, so
a -> a N_d is injective over either R_m. Reduce (5) at m=2
coefficient by coefficient and compare it with (5) at m=1.
The group, derivative operator and integral specialization have
not changed. Injectivity gives A_2(d) mod p = A_1(d); under (3)
these are precisely delta_2(d) and delta_1(d). This proves (4)
again, including d=1, and rules out a hidden factor from the norm
element. We never apply augmentation and divide by #H_d. This
check uses the constructed family and its invariant derivative,
not an arbitrary group-ring element. It is only the coefficient
specialization of the cited scalar construction, not a reproof
of its invariance or of system rigidity.

No equality of delta_1 with a differently normalized Kurihara number
is needed: Lemma 4.2 supplies their exact nonvanishing equivalence.
Together, (2) and (4) give tilde-delta(d) != 0.

**Minimize without changing the support.** Among the finitely many
positive divisors e of d with tilde-delta(e) != 0, choose N having
the fewest prime factors. If a proper divisor of N had nonzero
Kurihara number, it would have fewer factors, contradicting this
choice. Thus N is divisor-minimal in the residual collection on
N_(1,0), since all its proper divisors are divisors of d. No prime
replacement is involved, so N remains in N_(2,0).

Apply L021 with S/S_div=0. Its paired finite factors are absent,
and it gives dim_F_p Sel(Q,E[p])=2 and nu(N)=2 for this
divisor-minimal residual index. This is the imported residual-count
theorem, not a deduction of rational rank two. Hence
N=ell_1 ell_2 with distinct eligible primes. Lemma 4.2 gives
delta_1(N) != 0; (4) at N then makes delta_2(N) a unit in R_2,
proving (1). Its proper divisors' residual scalars vanish, so their
depth-two scalars belong to pR_2, which need not be zero.

Both discriminating tests succeed: a depth-two unit survives reduction,
and divisor selection preserves the stronger support. The finite-defect
stop in ATTEMPTS/021 is unchanged because zero finite quotient was
granted explicitly. L015 and L018 describe downstream uses only and
are not proof inputs. In particular, nothing above identifies the
remaining divisible Selmer directions with rational points. This is
local progress by a conditional specialization of known theorems,
with no claim of a result beyond the assessed sources.

## Mathlib

Full matching Sakamoto/Kim system and residual-count results: not
checked. Coverage of the supporting cyclic tensor, coefficient-of-norm
and reduction calculations was not checked; their elementary proofs
are given above.
No formal matching theorem or absence from Mathlib is asserted.
