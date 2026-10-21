# L023 — Fixed-depth two-prime scalar with the finite-defect valuation

## Hypotheses

Let E/Q be non-CM and p >= 5 be a prime of good ordinary reduction.
Assume that E[p] is surjective, p divides neither #E(F_p), the Manin
constant nor any Tamagawa factor, and E(Q_p)[p] = 0. Put
S = Sel(Q,E[p^infinity]) with classical Kummer local conditions. Grant
corank_Z_p S = 2 and a nonzero residual Kurihara number at some index
in Sakamoto's N_(1,0). These are L021's hypotheses. In particular,
finite p-primary Sha and rational rank two are not assumed.

Let F = S/S_div, h = length_Z_p F, and fix an integer m > h. Write
R_m = Z/p^m Z, T_m = E[p^m], and

\[
\mathcal P_{m,0}=
 \{\ell\text{ of good reduction}:\ell\equiv1\pmod{p^m},
 E(\mathbf F_\ell)[p^m]\simeq\mathbf Z/p^m\mathbf Z\}.
\]

Use the actual coefficient-compatible Kato-derived system
kappa_(xi,m,0) of Ryotaro Sakamoto, *p-Selmer group and modular symbols*,
Doc. Math. 27 (2022), 1891--1922, DOI 10.4171/DM/X21. For every eligible
ell fix a generator of G_ell = Gal(Q(ell)/Q), where Q(ell) is the maximal
p-subextension of Q(mu_ell), and the singular-quotient isomorphism in
Section 2.4. For a square-free index d, retain
G_d = tensor_(ell|d) G_ell. Define delta_m(d) to be the scalar of
v_q(kappa_(xi,m,0)_(d,q)) in R_m tensor_Z G_d, with q eligible and
coprime to d, using these trivializations. Sakamoto's definition makes
this independent of q. Valuation h in R_m means belonging to p^h R_m
but not p^(h+1) R_m; it is defined here because h < m.

The exact specialization is covered by
[the prior assessment](../drafts/literature/2026-10-05-positive-valuation-restricted-index.md).
L022 is a normalization comparison only, not a mathematical input.

## Conclusion

There are two distinct primes ell_1, ell_2 in P_(m,0) such that, for
N = ell_1 ell_2,

\[
R_m\delta_m(N)=(p^h),\qquad v_p(\delta_m(N))=h.
\tag{1}
\]

More precisely, the classical localization to the two rank-one finite
local groups is onto, on both the representation and its Cartier dual.
The Selmer group with transverse conditions at N equals the subgroup
of the classical depth-m Selmer group with zero localization at both
primes. As an R_m-module it is noncanonically isomorphic to F, so has
length h. These are existential choices at each m; no common pair for
all depths is asserted.

If h > 0 this scalar is nonzero at depth m but zero modulo p. It is
therefore not L015's residual-unit premise. The finite defect has not
been eliminated, and no rational Kummer membership, rational-rank lower
bound, complex-order comparison or BSD resolution follows here.

## Proof

**Finite-depth input and the source application.** L021 gives

\[
S\simeq(\mathbf Q_p/\mathbf Z_p)^2\oplus F,\qquad
F\simeq\bigoplus_{j=1}^t(\mathbf Z/p^{a_j}\mathbf Z)^2,
\quad h=2\sum_j a_j,
\tag{2}
\]

with a_j > 0. Every a_j is less than m. Import the natural classical
coefficient identification
Sel(Q,E[p^m]) = S[p^m] used in Chan-Ho Kim, *The structure of Selmer
groups and the Iwasawa main conjecture for elliptic curves*, author text
2025-05-12, [Section 5.3.1, printed p. 27](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=28).
That passage states the identification for an arbitrary coefficient
exponent, citing Mazur--Rubin Lemma 3.5.3. The hypotheses and classical
local conditions are unchanged from L021; global E(Q)[p] is zero by
surjectivity. This is not an assertion that coefficient reduction of
any Selmer group is onto, or that all local H^0 groups vanish. It gives

\[
M_0:=H^1_{\mathcal F_{\rm cl}}(\mathbf Q,T_m)
 \simeq R_m^2\oplus F.
\tag{3}
\]

For clarity about the induced local conditions in this import, put
A=E[p^infinity]. At each place v, the finite and infinite Kummer
conditions are the kernels of the maps to H^1(Q_v,E)[p^m] and
H^1(Q_v,E)[p^infinity], respectively. The coefficient map T_m -> A
commutes with these maps, and the map between the latter two groups
is inclusion. Thus the preimage of the infinite Kummer condition is
exactly the finite Kummer condition, even if the map on local H^1
is not injective. Globally A(Q)=0 by residual irreducibility, so the
coefficient sequence identifies H^1(Q,T_m) with H^1(Q,A)[p^m]. This
checks the local-condition applicability of the cited identification;
it does not assume local torsion vanishes away from p.

We specialize only the first-degree prime-selection case in Alberto
Angurel, *Kolyvagin systems of rank 0 and the structure of the Selmer
group of elliptic curves over abelian extensions*,
[arXiv:2504.20759v2, 2026-06-08, Theorem 3.27 proof, Section 3.5](https://arxiv.org/html/2504.20759v2#S3.SS5).
Its Corollary 2.30 chooses surjective primal and dual finite
localizations; Lemma 2.31 replaces the resulting dual transverse
condition by a strict one. To make its finite-coefficient application
explicit, use their underlying named inputs:
B. Mazur and K. Rubin, *Kolyvagin Systems*, Mem. AMS 168 (799) (2004),
[Proposition 3.6.1, pp. 30--31](https://webusers.imj-prg.fr/~christophe.cornut/ES/Ref/KolySys.pdf#page=36),
and [Lemma 4.1.7(ii), p. 37](https://webusers.imj-prg.fr/~christophe.cornut/ES/Ref/KolySys.pdf#page=43).
No general higher-Fitting equality, non-self-dual result or identification
with Angurel's scalar family is required.

Here are the hypothesis and prime-set checks for those imports.
T_m is free of rank two over R_m. Sakamoto, [p. 1896](https://ems.press/content/serial-article-files/29299?nt=1#page=6),
explicitly verifies Mazur--Rubin (H.0)--(H.3) for this representation:
absolute residual irreducibility, cyclotomic-trivial tau with rank-one
coinvariants, and the two residual Galois-cohomology vanishings.
p >= 5 supplies (H.4b), so residual non-self-duality is unnecessary.
Classical conditions are Cartesian by Sakamoto Corollary 2.15,
p. 1902, and self-dual under the Weil pairing by Definition 2.4,
p. 1898. Definition 2.3 also gives
(F_cl(n))* = F_cl(n) for transverse n. Thus these structures have
core rank zero, including after the first selection.

For (H.5) of Mazur--Rubin, take the full permitted depth-m eligible
prime set, omitting the finite set of bad primes and p. In the
Chebotarev construction of Proposition 3.6.1 at depth m, Frobenius is
conjugate to tau modulo T_m and acts trivially on mu_(p^m).
Lemma 3.5.6(i)--(ii), pp. 29--30, therefore gives the rank-one
Frobenius quotient and ell = 1 mod p^m. For good ell the invariants of
T_m are E(F_ell)[p^m]. A map Fr_ell-1 on the free rank-two R_m-module
has free rank-one cokernel exactly when its Smith form is diag(1,0),
which also gives free rank-one kernel. Hence the selected primes satisfy
precisely the cyclic condition of P_(m,0), not just Kim's weaker
congruences. Sakamoto Section 2.3, p. 1902, states the corresponding
finite/transverse local splitting and rank-one groups for this prime
set. All selections below use this full set at depth m and may exclude
any finite list of primes. No disjoint splitting extension is imposed.
This supplies the prime richness required for the imports.

More precisely, Mazur--Rubin Definitions 2.2.1 and 3.1.6, pp. 16
and 21, make their depth-m set equal to P_(m,0), outside the specified
finite exceptional set: I_ell=(ell-1,det(1-Fr_ell)) is zero in R_m,
and the Smith-form test above equates free rank-one invariants and
coinvariants. Hence (H.5) holds with t=m. For the second selection one
may use n=ell_1 in Lemma 4.1.7 without changing the original triple.
Its transverse modification is Cartesian by Mazur--Rubin
[Lemma 3.7.4, p. 34](https://webusers.imj-prg.fr/~christophe.cornut/ES/Ref/KolySys.pdf#page=40).
Thus the Chapter 4 hypotheses survive this modification as well as
self-duality. Positive density in Proposition 3.6.1 permits excluding
ell_1 without a new splitting condition.

Angurel's additional (H5), used for his relaxed-at-q system rather than
for this prime-selection argument, can also be met by q=p: Sakamoto
Corollary 2.14 at level zero gives the free rank-one classical local
quotient, while local Tate duality and E(Q_p)[p]=0 give
H^2(Q_p,T_m)=H^0(Q_p,T_m*)^vee=0. We do not instead assume this at an
eligible auxiliary prime. Angurel (H8) uses the full depth-m set with
trivial splitting extension; its other hypotheses correspond to the
checks above. The inconsistent strict/relaxed superscripts in his
Definition 2.18 are avoided below by specifying local conditions in
words. We import the selection and comparison inputs, and write only
the finite-module application needed to track h.

**A surjection removes one free direction.** Suppose a current
self-dual transverse Selmer group M is isomorphic to R_m^d direct sum F
with d > 0. Pick an element x generating a free summand, and its image
x* in the dual Selmer group under the Weil pairing. Both
p^(m-1)x and p^(m-1)x* are nonzero global cohomology classes. Apply
Proposition 3.6.1 to these classes (repeat each to fill its two primal
and two dual slots), at depth m. It supplies infinitely many eligible
primes ell for which both localizations are nonzero. At a new ell all
current Selmer classes have finite local condition. In its free
rank-one finite local group, p^(m-1)loc_ell(x) != 0 says precisely that
loc_ell(x) is a generator. The primal localization is therefore onto;
the same argument proves that the dual localization is onto. This is
the concrete use of Corollary 2.30, rather than an inference from
residual nonvanishing of the scalar family.

Apply Lemma 4.1.7(ii) to the primal surjection. It identifies the dual
Selmer group after imposing transverse condition at ell with the dual
group having zero condition at ell before that change. Since the
current and new transverse structures are self-dual, the same assertion
under the Weil identification gives

\[
M_{\rm new}=\ker\bigl(M\xrightarrow{\mathrm{loc}_\ell}
 H^1_{\rm f}(\mathbf Q_\ell,T_m)\bigr).
\tag{4}
\]

In particular, its classes have zero localization at ell, not merely a
possibly nonzero transverse localization.

Identify the target with R_m. Every element of F has order below p^m,
so its image lies in pR_m. A surjection R_m^d direct sum F -> R_m must
therefore have a unit coefficient on some free basis vector. Write
its formula as b_1 z_1 + ... + b_d z_d + u(f), with b_1 a unit after
reordering. The kernel is parameterized bijectively and R_m-linearly
by (z_2,...,z_d,f), setting
z_1 = -b_1^(-1)(b_2 z_2 + ... + b_d z_d + u(f)). Thus

\[
M_{\rm new}\simeq R_m^{d-1}\oplus F.
\tag{5}
\]

The copy of F in this kernel can be a graph inside the old free plus
finite decomposition; no canonical identification with the quotient
S/S_div or with rational points is being made.

**Exactly two selections.** Start with (3), d=2. Choose ell_1 by the
preceding argument and let M_1 be transverse at ell_1. Equations
(4)--(5) give M_1 contained in M_0, zero at ell_1, and
M_1 isomorphic to R_m direct sum F. Choose ell_2 distinct from ell_1
by the same argument applied to M_1 and its dual, now with d=1.
The final transverse group M_2 is

\[
M_2=\{c\in M_0:\mathrm{loc}_{\ell_1}(c)=
 \mathrm{loc}_{\ell_2}(c)=0\}\simeq F,
\quad \operatorname{length}_{R_m}M_2=h.
\tag{6}
\]

There is no third selection. The combined localization from M_0 to
the two finite local groups is onto: first lift the desired ell_1
component using M_0, then correct the ell_2 component using the
surjection from its kernel M_1. The correction does not change the
ell_1 component. The identical reasoning applies on the dual side.
The length check is also 2m+h - m - m = h. Strict and transverse
conditions coincide for these chosen global Selmer groups by (4),
not as local conditions on all cohomology classes.

**Use the scalar of the actual basis.** By Sakamoto
[Lemma 4.2, p. 1917, and Proposition 3.19, pp. 1915--1916](https://ems.press/content/serial-article-files/29299?nt=1#page=25),
the granted residual Kurihara nonvanishing makes kappa_(xi,m,0) a basis
of KS_0(T_m,F_cl) at every m. Apply his
[Theorem 2.20(2), p. 1904](https://ems.press/content/serial-article-files/29299?nt=1#page=14)
to this basis and N. It equates its scalar ideal with
Fitt^0_(R_m)(M_2^vee). A finite cyclic R_m/(p^a) has Pontryagin dual
of the same cyclic type. Using (2) and (6), a diagonal presentation of
M_2^vee has entries p^(a_j), p^(a_j) for each j, so the determinant
formula for the initial Fitting ideal gives

\[
\operatorname{Fitt}_{R_m}^0(M_2^\vee)
 =\Bigl(p^{2\sum_j a_j}\Bigr)=(p^h).
\tag{7}
\]

For F=0 the empty presentation gives R_m=(p^0). Because h<m, (p^h)
is nonzero; an element generating it has valuation exactly h, even
when m=h+1. There is no need to divide a scalar by p^h in R_m.

Finally, eligibility gives #G_ell = p^(b_ell) with b_ell >= m.
The tensor G_N is cyclic of order p^(min(b_ell_1,b_ell_2)), generated
by the tensor of the fixed generators. Hence a -> a tensor g_N is an
isomorphism R_m -> R_m tensor_Z G_N. This is the identification in
the scalar ideal computation. Changing generators or singular bases
only multiplies its generator by a unit. Theorem 2.20 is being applied
to Sakamoto's own constructed basis; no unknown comparison factor with
Angurel's system or an integral modular-symbol family is inserted.
We do not use residual nonvanishing to compare positive valuations.
Equations (6)--(7) prove (1).

Both depth-m surjections, the exact count two, and the length threshold
h have been checked. This is a conditional reproduction of the assessed
first-degree selection mechanism and scalar theorem. It does not claim
progress beyond those known inputs, and preserves ATTEMPTS/021's stop
on inferring F=0 from primitivity. The possible downstream construction
after inverting p has not been supplied here.

**Critical audit, 2026-10-05.** The later audit retained (1)--(7) under
the stated hypotheses. In particular, the nonzero classes used in
selection are p^(m-1)x in H^1(Q,T_m), not reductions of x whose
nonvanishing would need a separate argument. Repeating a class in
Proposition 3.6.1 is allowed; its p>4 proof does not require the primal
and dual representations to be nonisomorphic. Lemma 4.1.7(ii) is used
on the dual side before the self-dual identification. Its strict
condition is zero at the new prime; equality (4) is an equality of
global subgroups, not of the finite and transverse local lines.

When h=0, F=0 and the two kernels have free ranks one and zero,
including at m=1. When h>0 and m=h+1, every a_j<m; the same two
surjections apply, and (p^h) is a nonzero ideal of R_m even though
p times that ideal is zero. The scalar still has valuation h.
No cancellation of p^h is used. Residual nonvanishing is used only
to establish basis status; (7) comes directly from that basis's
Fitting identity. The added local-condition and Cartesianity details
make the applications explicit without changing the claim or its
mathematical inputs. The audit establishes no stronger arithmetic
conclusion or new result beyond the assessed sources.

## Mathlib

Full matching fixed-depth prime-selection/Kolyvagin scalar result: not
checked. Supporting Smith-form, finite-module kernel, cyclic tensor and
Fitting computations were written explicitly; their Mathlib coverage
was not checked. No matching formal theorem or absence claim is made.
