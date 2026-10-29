# L118 — Derived-height accounting for the augmentation defect

## Hypotheses

Let E/Q be an elliptic curve and p an odd prime of good ordinary
reduction. Use the classical cyclotomic tower, discrete Selmer group,
Pontryagin dual X, and generator T = gamma - 1 of
[the cyclotomic control conventions](../foundations/03-cyclotomic-control.md).
Write

\[
\Lambda=\mathbf Z_p[[T]],\quad A=\Lambda_{(T)},\quad
M=X\otimes_\Lambda A,\quad h=\operatorname{ord}_T f_X,
\quad\delta=\operatorname{length}_A(TM).
\]

Thus L002 applies, in particular X is finitely generated and torsion
over Lambda. Put r = rank E(Q) and
s = corank_Zp Sha(E/Q)[p^infinity]. Neither finite Sha nor
height nondegeneracy is assumed.

Let

\[
\mathcal S=\varprojlim_a\operatorname{Sel}_{p^a}(E/\mathbf Q),
\qquad V=\mathcal S\otimes_{\mathbf Z_p}\mathbf Q_p.
\]

The inverse transition maps are induced by multiplication by p on
torsion coefficients, not the inclusions used for the discrete
p-primary Selmer group. Let V_j, j >= 1, be Howard's derived-height
filtration on V, normalized with V_1 = V. These are full compact
Selmer spaces, not a filtration assumed to lie in E(Q) tensor Q_p.

## Conclusion

The filtration is eventually zero, and the following are finite sums:

\[
\boxed{\quad
\delta=\sum_{j\ge2}\dim_{\mathbf Q_p}V_j,
\qquad
h=r+s+\sum_{j\ge2}\dim_{\mathbf Q_p}V_j.
\quad}                                                    \tag{1}
\]

More explicitly, take the finite decomposition of L002,
M = direct-sum_i A/(T^{e_i}), with e_i >= 1. If there are no summands,
put B = 0; otherwise put B = max_i e_i. Then

\[
\dim V_j=\#\{i:e_i\ge j\},\qquad
V_j=0\quad(j>B),\qquad \dim V_1=r+s.                       \tag{2}
\]

Equivalently, with c_j = dim(V_j/V_{j+1}),

\[
c_j=\#\{i:e_i=j\},\qquad
\delta=\sum_{j\ge2}(j-1)c_j.                              \tag{3}
\]

The identities measure the augmentation defect and do not show that
any term vanishes. They neither remove s nor compare h with the
complex analytic order. This is a specialization of known results,
not a new general nondegeneracy theorem or a BSD resolution.

## Proof

**The imported arithmetic theorem.** The primary source is Benjamin
Howard, *Derived p-adic heights and p-adic L-functions*,
[arXiv:1202.6343v1, submitted 2012-02-28](https://arxiv.org/pdf/1202.6343v1),
Section 3 setup (printed p.12), Propositions 3.4--3.5 (pp.13--15),
and Section 4, equation (9), Lemma 4.1, Theorem 4.2 and Corollary 4.3
(pp.15--17). The relevant statements and their comparison proofs
are the source for the following input; no height construction is
reproved here.

In that notation, specialize the base field F to Q, the abelian
variety to E, and its Z_p-extension to the cyclotomic one. The
Section 4 group Y is explicitly the classical infinite-level
Selmer group, and X is its Z_p-dual with values in Q_p/Z_p.
Lemma 4.1 identifies the rationalized auxiliary inverse limit with
the rationalized compact classical Selmer group. Theorem 4.2 gives

\[
V_1=V,\qquad
\dim_{\mathbf Q_p}V_j
=\operatorname{rank}_{\mathbf Z_p}
       (J^{j-1}X/J^jX),\quad J=(T).                       \tag{4}
\]

It also gives pairings from the j-th spaces for E and its dual to
(J^j/J^{j+1}) tensor Q_p, whose left and right kernels are the next
filtered spaces. We use (4), without assuming these kernels zero.

**Applicability and matching.** Howard assumes p > 2, good ordinary
reduction above p, p unramified in the base, ramification of primes
above p in the tower, and finite decomposition of bad primes. The
first two are hypotheses; Q is unramified over itself, and p is
totally ramified in the cyclotomic tower by the cyclotomic
ramification theorem. Every bad prime ell is different from p.
Cyclotomic reciprocity sends its arithmetic Frobenius to the
projection of ell in
Z_p^times/mu_{p-1} = 1+p Z_p. This projection is nonidentity:
otherwise ell would be in mu_{p-1}, implying ell^(p-1) = 1 in Q_p,
contradicting injectivity of Q into Q_p and ell > 1. The group
1+p Z_p is torsion free by the p-adic logarithm. Its nonzero closed
subgroups are open, as follows under logarithm from the closed
subgroups p^b Z_p of Z_p. Consequently the closed subgroup generated
by Frobenius has finite index, which is finite decomposition.
This verifies the tower hypotheses, including at every bad prime.

Howard's Section 3 local conditions are compared to the classical
ones in Propositions 3.4--3.5; finite-coefficient groups are not
silently identified integrally. The bounded-error comparison and
inverse-limit passage needed for (4) are precisely equation (9)
and Lemma 4.1. The latter's proof compares coefficient Selmer groups
with p-power torsion in the discrete group and uses finite control
errors before rationalization. Thus this invocation does not assume
an unstated exactness of arbitrary inverse limits. In particular,
neither finite Sha nor a Mordell--Weil basis is a source hypothesis.

For clarity about the limit argument, fix the filtration index j and
the base layer n = 0. The comparison systems in equation (9) have
finite terms: the auxiliary j-th terms lie in the first auxiliary
Selmer group at the base, which has bounded finite error relative to
the finite classical coefficient Selmer group. The target terms are
p^a-torsion in a cofinitely generated Z_p-module. The comparison
kernels and cokernels are killed by some p^{C_j}, uniformly in a.
For a compatible system of maps U_a -> W_a of finite groups with
this property, put K_a = ker(U_a -> W_a) and I_a = image(U_a -> W_a).
The inverse system K_a satisfies the Mittag--Leffler condition:
at each fixed level its descending images stabilize in a finite
group. Consequently lim U_a -> lim I_a is surjective, and its
kernel lim K_a is killed by p^{C_j}. Left exactness applied to
0 -> I_a -> W_a -> coker(U_a -> W_a) shows that the cokernel
of lim U_a -> lim W_a embeds in lim coker(U_a -> W_a), so it too
is killed by p^{C_j}. Rationalization therefore gives an isomorphism.
The same argument applies to the two finite-system comparisons in
Lemma 4.1 at n = 0, including the map from classical coefficient
Selmer groups, whose kernels are bounded by the finite E(Q)[p^infinity].
This explains the bounded-error passage used here; it asserts neither
integral equality nor exactness for arbitrary inverse systems.

Since the infinite Selmer group is discrete, all its homomorphisms
to Q_p/Z_p are continuous. We use the usual contragredient dual
action, matching the control conventions. If dual action is instead
written using the inverse generator, T becomes -T/(1+T); this
preserves every ideal (T^j) and all dimensions and lengths below.
There is no change of augmentation prime or lost normalization
factor. E's canonical principal polarization identifies the two
compact Selmer filtrations for E and its dual; it imposes no
nondegeneracy or finiteness hypothesis. In fact the dimension input
(4) itself does not require making this identification.

**Reduction of each layer to L002's localized module.** The module
N_j = T^{j-1}X/T^j X is finitely generated over Z_p and killed by T.
Every g outside (T) acts on it through its nonzero constant term
g(0). Hence localization of N_j at (T) is exactly rationalization
over Z_p. Exactness of localization, applied to the image and
quotient of multiplication by powers of T, gives

\[
N_j\otimes_{\mathbf Z_p}\mathbf Q_p
\simeq N_j\otimes_\Lambda A
\simeq T^{j-1}M/T^jM.                                    \tag{5}
\]

The residue field of A is Q_p by L002, so (4)--(5) imply

\[
\dim V_j=\dim_{\mathbf Q_p}(T^{j-1}M/T^jM).                \tag{6}
\]

This is only an equality of dimensions with a localized layer;
we do not assert a canonical isomorphism of V_j with that layer.

**Finite accounting.** On the summand A/(T^{e_i}) of L002, the j-th
layer in (6) is one-dimensional for 1 <= j <= e_i and zero for
j > e_i. Summing over the finitely many summands proves (2), except
for its last equality, and proves termination at B. L002 identifies
the first-layer dimension with d = r+s, proving that last equality.
It also gives delta = sum_i(e_i-1). All relevant sums are now finite,
so counting the pairs (i,j) with 2 <= j <= e_i gives

\[
\sum_{j\ge2}\dim V_j
=\sum_i\sum_{j=2}^{e_i}1
=\sum_i(e_i-1)=\delta.
\]

Combining this with L002's h = r+s+delta proves (1). The filtration
is decreasing, so dim(V_j/V_{j+1}) = dim V_j - dim V_{j+1}.
The count in (2) then yields c_j = #{i:e_i=j}; grouping the last
finite sum by e_i gives (3). When M = 0, (6) makes every V_j zero
and L002 gives h = d = delta = r+s = 0. All formulas therefore
include the empty case.

Only a fixed-index assertion is needed in (4)--(6). For each integer
j those equalities hold after killing that index's bounded errors.
The single exponent B comes instead from the finite-length module M;
for every j > B its j-th layer is zero. Thus all V_j with j > B
vanish, without an error bound uniform in j and without exchanging
an infinite sum or intersection with rationalization.

**Errors and scope.** Torsion of X, supplied by L002's hypotheses
and arithmetic inputs, is essential. A free Lambda summand would
give a nonzero dimension in every layer and no finite sum. This is
the free contribution explicitly retained in Howard's Corollary
4.3; it is zero here by cotorsion, not by a conjectural height
assertion. Contributions supported away from (T) vanish on
localization: a finite set of generators of any such module has
annihilators outside (T), whose product is inverted. In particular
finite/pseudo-null errors in a Lambda pseudo-isomorphism vanish
there. Here Lambda is the two-dimensional regular local ring
Z_p[[T]]; finitely generated pseudo-null modules have finite length
over Lambda and are killed by a power of p, a unit in A. The proof
of (5)--(6) uses X itself, so it does not even require choosing that
pseudo-isomorphism. These observations explain why neither
nonaugmentation factors nor finite errors alter the answer.

L003's finite-Sha/nonzero-regulator implication is a different,
conditional way to remove delta. The present formula handles
degenerate full-Selmer heights without removing the defect. The
formal obstruction in L019 to sending a first-height radical onto
a rational/Sha quotient is untouched. Future arithmetic upper
bounds on the higher V_j could bound delta through (1); producing
such bounds, removing s, and the comparison with complex analytic
order remain unresolved. The source assessment predating this
attempt is [the approved specialization review](../drafts/literature/2026-10-25-derived-height-defect-accounting.md).

**Critical audit (2026-10-25, step 490).** The stated identity passes
the separate approved audit. The complete local comparison cases in
Propositions 3.4--3.5 were checked: away from p at good primes the
relevant kernel vanishes; at bad primes finite decomposition bounds
the error; above p the reduction groups and ramification give the
required bounds. Equation (9), Lemma 4.1 and Theorem 4.2 match the
compact coefficient transitions and classical discrete dual used here.
The algebraic checks cover every layer, zero M, absence of a free
part, and disappearance of finite and nonaugmentation contributions.
The explicit bounded-error and fixed-index explanations above clarify
the existing proof; no hypothesis or conclusion is changed. This is
verification of a known-theorem specialization, not new arithmetic
bounds or a resolution of BSD. The only direct local lemma input
remains L002; the canonical DAG requires no change.

## Mathlib

Full matching arithmetic derived-height filtration theorem: **not
checked**. Supporting results on localization, DVR module
classification, finite-dimensional filtered spaces and finite sums:
**not checked**. No absence claim or full library theorem match is
made. Howard supplies the arithmetic input; L002 supplies the
finite-length algebra, with the specialization proved above.
