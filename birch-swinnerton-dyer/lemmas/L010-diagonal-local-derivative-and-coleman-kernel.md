# L010 — The diagonal local derivative and the Coleman kernel

## Hypotheses

Retain all hypotheses and notation of L009, including the nonzero
diagonal class kappa, F = Q_p, V = V_p E, xi_T = 1 + Td + O(T^2),
and x = res_K(kappa). Thus x is strict, S = Sel(K,V) = S^+ has
dimension two, and Delta_d is defined using the unique invariant
ordinary first-order lift. Strict always means zero localization.

Let Z be the anticyclotomic component of the diagonal family with
the test vectors of Castella--Hsieh's Corollary 3.7. Use its fiber
normalization Z(0) = x, as in their Section 5.1 and Lemma 5.1.
These data and exact source statements are recorded in
[the CM diagonal foundation](../foundations/09-cm-diagonal-deformation.md).
No existence of these auxiliary data for arbitrary E is assumed.

Put R = F[[T]], A = R/(T^2), and epsilon = T mod T^2. All series
below are taken in the formal neighborhood of augmentation. Let

\[
M_v=\varprojlim_n H^1(K_v,V\otimes_F R/(T^n)(\xi_T)),\quad
U=\operatorname{Loc}_{\mathfrak p}Z\in M_{\mathfrak p},\quad
D_v=H^1_f(K_v,V).
\]

Shapiro and coefficient specialization send the Iwasawa class Z
to these modules and to its global first-order reduction z_A.
The scalar Coleman map, denoted C_eta, is extended to this formal
neighborhood. Its values may require the coefficient extension B
in the source; assertions of vanishing descend to F. Superscripts
on D = D_mathfrak_p direct-sum D_overline_mathfrak_p are tau signs,
not ordinary filtration signs.

## Conclusion

The local module M_mathfrak_p is free of rank two over R, and
reduction induces M_mathfrak_p/T^n M_mathfrak_p = H^1(K_mathfrak_p,V_(R/T^n)).
There is a unique U_1 with U = T U_1. Its reduction

\[
u=U_1(0)\in D_{\mathfrak p}
\tag{1}
\]

is ordinary. The actual first-order family z_A is therefore an
ordinary Selmer lift of x with localizations (epsilon u,0), and

\[
\boxed{\Delta_d(x)=\tfrac12(u,-\tau u).}
\tag{2}
\]

Consequently,

\[
x\text{ has a strict first-order lift}
\quad\Longleftrightarrow\quad u=0
\quad\Longleftrightarrow\quad U\in T^2M_{\mathfrak p}.
\tag{3}
\]

The checked scalar reciprocity law gives only

\[
C_\eta(U)\in T^2B[[T]],\qquad
\ker C_{\eta,0}=D_{\mathfrak p}\otimes_F B.
\tag{4}
\]

Even a prescribed full scalar series C_eta(U) in T^2 leaves the
ordinary derivative u arbitrary in the local module after extending
coefficients. Thus the scalar law and the zero localization at the
other prime do not, by themselves, imply (3). This is an insufficiency
of specified local data, not a counterexample involving the actual
global diagonal class. Its u and q(kappa) are not computed here.
There is no new rational-rank bound or Kummer-membership criterion.

## Proof

**Local specialization has no hidden torsion.** At v | p, H^0(K_v,V)
is zero: the p-primary torsion in E(K_v) is finite. The Weil pairing
and local Tate duality give H^2(K_v,V) = 0. Local Euler characteristic
then gives dim_F H^1(K_v,V) = 2, since K_v = Q_p. These are the local
vanishings used in L009.

Write V_n = V tensor R/(T^n)(xi_T). Induction in the exact coefficient
sequences shows H^0(K_v,V_n) = H^2(K_v,V_n) = 0. In particular the
sequence with kernel T^(n-1)V_n is exact on H^1 and yields

\[
0\longrightarrow H^1(K_v,V)\longrightarrow H^1(K_v,V_n)
\longrightarrow H^1(K_v,V_{n-1})\longrightarrow0.
\tag{5}
\]

The other coefficient sequence, with kernel TV_n isomorphic to
V_(n-1), shows that the kernel of reduction to H^1(K_v,V) is exactly
T H^1(K_v,V_n): the map to H^1(K_v,V_(n-1)) is surjective and its
composition with the injection induced by multiplication by T is
multiplication by T on H^1(K_v,V_n). Lift a basis of H^1(K_v,V).
Nakayama gives a surjection (R/T^n)^2 onto H^1(K_v,V_n), and (5)
gives equal F-dimensions 2n, so this is an isomorphism. Compatible
basis lifts exist by (5). Taking their inverse limit proves the
freeness and reduction assertions. In particular multiplication by
T is injective. This argument does not assume a global control
isomorphism for the ordinary or strict Selmer group.

**The scalar has at least a double zero.** Put m_ac = ord_T Theta_(f/K).
Castella--Hsieh, Section 5.5, (5.9)--(5.11) and the characteristic
divisibility in that proof give integers r_i >= 1 and d_i >= 2 with

\[
\sum_i r_i d_i\le m_{\rm ac}\le2r_t.
\tag{6}
\]

Since the sum is at least 2r_t + 2 sum_(i<t) r_i, (6) forces t = 1.
Then r_1 d_1 <= m_ac <= 2r_1 gives d_1 = 2 and m_ac = 2r_1 >= 2.
Here r_1 is a derived-height filtration index,
not rank E(Q). The source's nonzero theta element makes the order
finite. Corollary 3.7 gives Loc_overline_mathfrak_p Z = 0 and
C_eta(U) = C(T)Theta_(f/K). The prefactor C is a unit at augmentation:
w is a unit, the auxiliary L-value is nonzero, and its remaining
algebraic factors are nonzero. In particular alpha_p cannot equal
the finite-order value chi(overline_mathfrak_p): its complex
conjugates have absolute value sqrt(p), not one. This checks the
displayed Euler denominator. Hence C_eta(U) belongs to (T^2).

**What its augmentation detects.** Theorem 3.4 at the trivial
character gives C_(eta,0) as a nonzero multiple of the dual
exponential paired with eta. One can check nonvanishing without
choosing a dual-exponential convention as follows. Proposition 4.3
expresses the Coleman map as the local Tate pairing with the
finite local family w_eta, up to a factor whose augmentation is
nonzero: the sum there reduces to [F_loc:Q_p]/[F_infinity:Khat_infinity]
because h_e(0) = 1. Here F_loc is the auxiliary local field in the
source, distinct from this lemma's coefficient field F.

Lemma 4.4 and the proof of Theorem 4.5 compute the logarithm of
the corestricted fiber w_0 as

\[
\log_{\omega_E}(w_0)
 =[F_{\rm loc}:\mathbf Q_p]\,
   \frac{1-\alpha_p^{-1}}{1-p^{-1}\alpha_p}\ne0.
\tag{7}
\]

Indeed alpha_p != 1 by the Hasse bound, and alpha_p != p since
alpha_p is a p-adic unit. Thus w_0 spans the one-dimensional finite
local line D_mathfrak_p. Local Tate duality is perfect on the
two-dimensional H^1(K_mathfrak_p,V), and the finite line is its
own annihilator. Pairing with w_0 therefore has exactly that
line as kernel. This proves the kernel assertion in (4), including
after scalar extension. The same conclusion follows directly from
the dual-exponential formula. The Coleman output is regular at
augmentation (the slope -1 vector with h = 1 gives a bounded
distribution in (3.9)), so it extends to the formal modules used here.

**The first-order class and the sign.** Since x is strict, U(0) = 0.
Local specialization now gives U = T U_1 uniquely. Scalar linearity
and (4) imply

\[
0=(C_\eta(U)/T)(0)=C_{\eta,0}(U_1(0)).
\]

The kernel just proved gives u = U_1(0) in D_mathfrak_p. The family
z_A has localizations (epsilon u,0); the injection from the fiber
local cohomology into the epsilon part is the one in L009. These
localizations lie in the ordinary local conditions. Away from p
the rational local H^1 for V and its first-order deformation vanish,
as checked in L009, so there is no further local condition to verify.
Thus z_A belongs to S_A.

Conjugation exchanges the two primes and sends epsilon to -epsilon.
Consequently loc(tau z_A) = (0,-epsilon tau u). Since x is invariant,
(z_A + tau z_A)/2 is the unique invariant ordinary lift y_x of L009.
Taking its localization gives (2). The definition of Delta_d and
L009's strict-lifting equivalence give the first equivalence in (3).
The second is the local specialization isomorphism applied to U_1.
Multiplying Z by a scalar unit with value 1 at T = 0 does not change
u, since U(0) = 0. An inverse parameter convention changes d and u
by the same nonzero tangent factor and does not change the criterion.

**The loss of information persists for the full scalar series.**
In M_mathfrak_p tensor_R B[[T]], choose s with C_eta(s) = 1;
this is possible because C_(eta,0) is nonzero, so a suitable lift
has unit Coleman image. Choose a lift f_0 of a nonzero vector in
D_mathfrak_p and set f = f_0 - C_eta(f_0)s. Its reduction is still
f_0(0), because C_eta(f_0)(0) = 0, and C_eta(f) = 0. The reductions
of f and s form a basis; hence f,s form a B[[T]]-basis.

For any fixed b(T) in T^2 B[[T]] and c in B the local classes

\[
U_c=b(T)s+cTf
\tag{8}
\]

all reduce to zero and have precisely the same full Coleman image
b(T), while (U_c/T)(0) = c f(0). With zero localization at the
other prime, their first-order local data consequently give both
possibilities in (3). This ambiguity also respects the first-order
ordinary and conjugation diagrams: on A e_1 + A e_2 with invariant
basis, take local bases f_p,f_bar exchanged by tau and define

\[
\operatorname{loc}_A(e_1)=(f_p,f_{\bar p}),\qquad
\operatorname{loc}_A(e_2)=\tfrac{\epsilon c}{2}(f_p,-f_{\bar p}).
\]

This map is equivariant. The lift z_c = e_2 + epsilon c e_1/2 has
localizations (epsilon c f_p,0); its invariant average is e_2.
For c = 0 its strict derivative vanishes, and for c = 1 it does not,
with identical fiber map and scalar Coleman data modulo T^2.

Equation (8) concerns actual local module freedom; the last diagram
is abstract linear algebra. Neither asserts that all these local
choices arise from global diagonal cycles or satisfy additional
arithmetic constraints. Their point is that the specified scalar
reciprocity data do not determine the missing ordinary coefficient.
No implication in either direction between (3) and Kummer membership
has been established. The bound rank E(Q) <= 2 from L009 is unchanged;
the required lower bound remains rank E(Q) >= 2.

## Mathlib

Coverage of the full arithmetic derivative statement: **not checked**.
Supporting local cohomology, Tate duality, formal-module, and
semilinear averaging results: **not checked**. The named source
theorems and direct links are retained in the CM diagonal foundation.
They supply the diagonal class, its one zero localization, and the
scalar reciprocity and interpolation formulas; they are not a match
for (2), (3), or a rational Kummer-membership criterion. The deductions
and the limitations of the local and abstract models are proved above.
