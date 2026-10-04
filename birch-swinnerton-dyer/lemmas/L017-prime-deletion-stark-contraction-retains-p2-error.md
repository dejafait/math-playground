# L017 — Stark contraction retains the transverse p^2 lifting error

## Hypotheses

Retain the hypotheses, eligible two-prime index N = ell_1 ell_2,
coefficient-compatible arithmetic systems and normalizations of L016.
Put R = Z/p^2 Z and write G = H^1_(F_cl^N)(Q,E[p^2]), with its
prescribed basis c_1,c_2. Use its coordinates A_i, B, C and tau; in
particular B,C belong to F_p, and their simultaneous vanishing is
equivalent to tau = 0. A product pB means the canonical injection into pR.

Let C_can = H^1_(F_can^N)(Q,E[p^2]). The canonical structure relaxes
the condition at p, so F_can = F_cl^p. Let phi be localization to the
singular quotient at p, identified with R by the normalization used in
Sakamoto, *p-Selmer group and modular symbols*, Documenta Math. 27
(2022), DOI 10.4171/DM/X21,
[Section 2.5, printed pp. 1905--1907](https://ems.press/content/serial-article-files/29299?nt=1#page=15).
The input is the already assessed construction, not a new transfer theorem.

Use the Stark modules X_d^r from that section's Definition 2.23. Thus
X_N^0 = exterior-bidual^2(G) tensor det(W_N), and X_N^1 uses
exterior-bidual^3(C_can); W_N is the sum of the dual singular lines at
ell_1,ell_2. Tensor generators are fixed throughout. Let epsilon^1 be
the canonical Stark family corresponding to the normalized Kato-derived
rank-one system under Theorem 2.24, and epsilon^0 its image by phi
contraction. Its scalar regulator is delta(kappa^(2)) by the commuting
diagrams (2)--(4) of Section 2.5 and Theorem 3.17. No rational Kummer
membership or positive analytic rank is assumed.

## Conclusion

The p-local sequence is split exact:

\[
0\longrightarrow G\longrightarrow C_{\rm can}
 \xrightarrow{\phi}R\longrightarrow0.
\tag{1}
\]

In particular C_can is free of rank three. At N the Stark transfer

\[
\phi:X_N^1\longrightarrow X_N^0
\tag{2}
\]

is an isomorphism of free rank-one R-modules. It imposes no vanishing
condition on B,C at this index.

After compatible choices of determinant orientations, there is a unit
U in R such that the rank-zero Stark components at divisors of N are

\[
\begin{aligned}
\epsilon_N^0&=U(c_1\wedge c_2),\\
\epsilon_{\ell_1}^0&=U pB c_2, &
\epsilon_{\ell_2}^0&=U pC c_1,\\
\epsilon_1^0&=U p^2BC=0\quad\hbox{in }R.
\end{aligned}
\tag{3}
\]

The suppressed determinant-line factors are the fixed generators.
Changing their orientations changes signs but none of these vanishing
tests. If tau != 0, both one-prime components in (3) are nonzero of
order p. Their finite scalar regulators nevertheless vanish. Thus
vanishing of all proper-divisor scalars modulo p^2 does not remove the
transverse error.

A coefficient-compatible, self-dual localization model with tau = 1
extends the earlier two-prime package to (1), the rank-one and rank-zero
Stark components on every divisor of N, and their commuting contraction
and scalar-regulator diagrams. This is a divisor subsystem, not a full
Stark/Kato family or an arithmetic realization. The actual tau remains
undetermined. The unconditional rational-rank bound remains r <= 2;
even tau = 0 supplies no rational rank-two lower bound.

## Proof

**The actual p-local extension splits.** The residual localization
isomorphism in L015 makes H^1_((F_cl)_N)(Q,E[p]) zero: a classical
class strict at both ell_i has both coordinates zero. Apply Sakamoto's
[Lemma 2.2, printed p. 1897](https://ems.press/content/serial-article-files/29299?nt=1#page=7)
to this strict structure, equivalently the dual of F_cl^N. Its level-two
group has zero p-socle and is zero. This uses the Cartesian propagation
and eligible primes already checked in L015, not an assumption that
classical coefficient reduction is onto.

Apply the imported Poitou--Tate exact sequence, Sakamoto's Theorem 2.1,
to F_cl^N contained in F_can^N. The only local quotient is the free
rank-one singular quotient at p. The following term is the dual of
H^1_((F_cl)_N)(Q,E[p^2]), just shown to vanish. This proves surjectivity
of phi and exactness of (1). Since R is free, choose w with phi(w) = 1;
then C_can = G direct-sum Rw. L016 makes G free of rank two.

On free modules exterior biduals agree with exterior powers. The
contraction convention is

\[
\iota_f(x_1\wedge\cdots\wedge x_t)
 =\sum_{j=1}^t(-1)^{j-1}f(x_j)
     x_1\wedge\cdots\widehat{x_j}\cdots\wedge x_t.
\tag{4}
\]

Consequently phi contracts c_1 wedge c_2 wedge w to c_1 wedge c_2.
It is an isomorphism on these determinant lines, and tensoring with
det(W_N) proves (2). Section 2.5 uses precisely this exterior-bidual
contraction for the exact sequence (1). This is an assertion at N;
it does not assert surjectivity between full modules of Stark families.

**The actual divisor transitions retain a vector invisible to scalars.**
Write f_i and s_i for the unramified and singular coordinates at ell_i.
L016 gives

\[
\begin{array}{c|cc}
 &c_1&c_2\\\hline
f_1&A_1&0\\
f_2&0&A_2\\
s_1&0&pC\\
s_2&pB&0.
\end{array}
\tag{5}
\]

In particular the finite coordinate map G -> R^2 is an isomorphism.
In Definition 2.23, the transition from N to ell_1 is induced by
the exact sequence with map s_2; the transition to ell_2 uses s_1.
The scalar regulator at N instead uses the finite projections f_1,f_2
to pass from relaxed conditions to transverse conditions, as in the
definition of Pi_d^0 on printed p. 1906. Its value on c_1 wedge c_2
is, up to the fixed determinant sign and finite-singular units,
A_1 A_2, a unit. Since delta_2(N) reduces to the assumed nonzero
delta_1(N), epsilon_N^0 = U(c_1 wedge c_2) for a unit U.

Choose transition orientations N -> ell_1 as iota_(s_2) and
N -> ell_2 as -iota_(s_1), with the subsequent transitions to 1
as iota_(s_1) and iota_(s_2), respectively. The two paths agree
because contractions anticommute. Applying (4) and (5) gives (3).

These formulas apply to the exterior biduals even if a one-prime group
is not free. For tau != 0 the groups at ell_1 and ell_2 are explicitly

\[
\ker(s_2)=pR c_1\oplus R c_2,\qquad
\ker(s_1)=R c_1\oplus pR c_2.
\tag{6}
\]

Their first exterior biduals are themselves. Indeed R and R/pR are
reflexive under Hom_R(-,R): the dual of R/pR is pR, and evaluation
identifies its double dual with R/pR. Direct sums preserve this fact.
The vectors pB c_2 and pC c_1 in (3) lie in the indicated free
summands, and contraction into these kernels is the source's natural
bidual map. If tau = 0 the kernels are simply G. At the empty index
the zeroth exterior bidual is R, irrespective of the classical group.

At a one-prime index the scalar regulator is the finite projection
at that prime, up to its fixed unit. Equation (5) gives
f_1(pB c_2) = f_2(pC c_1) = 0. The final singular contraction is
p^2BC = 0 in R. Thus the proper scalar vanishings hold for both
values of tau, whereas the one-prime Stark vectors vanish exactly
when tau = 0. The determinant transfer at N, followed by these
divisor transitions, does not add the desired vanishing condition.

**An extension of the nonzero-error model.** For any odd p and
t in F_p take a free module with basis x_1,x_2,w over R. Give it
local coordinates (f_1,s_1,f_2,s_2,f_p,s_p) by

\[
a x_1+b x_2+z w\longmapsto
 (a,-ptb,b,pta,0,z).
\tag{7}
\]

On the ambient six-coordinate module use the sum of the three
hyperbolic symmetric forms f_i s'_i+s_i f'_i. The image of (7)
is maximal isotropic: orthogonality to x_1,x_2,w imposes exactly
s_1 = -pt f_2, s_2 = pt f_1 and f_p = 0, which describe that image.
At p the classical line is the f_p line. Its intersection with (7)
is G = R x_1 direct-sum R x_2, and phi = s_p is projection onto z.
This gives the split p-local sequence with the required local lines.
Reduction and socle injection respect all lines and the coefficient
sequence; the residual auxiliary graph is the full finite F_p^2.

On the free top modules put eta^0_N = x_1 wedge x_2 and
eta^1_N = x_1 wedge x_2 wedge w. Use the rank-zero orientations
above and the opposite transition signs for rank one. Their components
on the four divisors are

\[
\begin{array}{c|cc}
d&\eta_d^0&\eta_d^1\\\hline
N&x_1\wedge x_2&x_1\wedge x_2\wedge w\\
\ell_1&pt x_2&-pt x_2\wedge w\\
\ell_2&-pt x_1&pt x_1\wedge w\\
1&-p^2t^2=0&-p^2t^2 w=0.
\end{array}
\tag{8}
\]

These are genuine elements of the required biduals. At a nonfree
one-prime module the displayed rank-one bivector uses its two free
summands, and the rank-zero vector uses its free summand. Formula
(4), or the defining dual evaluation, computes their transition maps.
Contraction with phi sends eta_d^1 to eta_d^0 for every d. Its
anticommutation with each s_i is canceled by the indicated rank-one
transition sign. Both divisor paths to 1 give the last row of (8).

Use the scalar orientation delta_N = -f_2 f_1(eta_N^0) = -1.
The rank-one regulator at N is -f_2 f_1(eta_N^1) = -w; its phi
value is also -1. At each proper divisor both scalar diagrams give
zero. The resulting rank-one vectors at the proper divisors are zero,
so their finite-singular equations on this divisor subsystem also hold.
The prime-deletion vectors -iota_(f_2)(eta_N^0) = x_1 and
iota_(f_1)(eta_N^0) = x_2, with
g_1 = pt x_2 and g_2 = -pt x_1, satisfy every two-prime equation
tracked in L015. Their transverse coefficients are pt and -pt.

For t = 1, the one-prime Stark vectors are nonzero, tau = 1,
and the classical auxiliary intersection is pG with zero reduction.
All of the determinant, coefficient, reciprocity and divisor-transition
data just tested allow this value. There are no components at further
auxiliary primes in this construction. In particular this is not a
counterexample to a theorem about the complete arithmetic Kato family,
and it does not determine the arithmetic value of tau.

`python3 scripts/prime-deletion/check_p2_stark_contraction.py` checks
these diagrams exactly over Z/25Z for all five residual values of t.
It checks signs, both divisor paths, the scalar maps, coefficient
reductions, the p-local kernel and the transverse-classical intersection.
The all-p argument is (4)--(8), not finite enumeration.

This supplies a new negative test of the proposed automatic promotion:
Section 2.5's top-index contraction and the four divisor transitions
retain the error without forcing it to vanish. The p^2 scalar reduction
loses its product p^2BC. The actual error, rational membership and
analytic comparison remain open. This is a reproduced specialization
of the assessed framework; no progress beyond checked literature or
originality claim is made.

## Mathlib

Full coverage of this fixed-index contraction and surviving-error model:
**not checked**. Supporting exterior biduals, Poitou--Tate duality,
Cartesian local conditions and coefficient maps: **not checked**.
Sakamoto's Theorem 2.1 and Lemma 2.2 support (1); Definition 2.23,
Theorem 2.24 and Section 2.5's diagrams support the transfer and
transition maps. Theorem 3.17 matches the arithmetic construction input.
They are not asserted to match this entire specialization or to be
Mathlib theorem names. No absence or certified novelty inference is made.
