# L124 — A rational normalizer transformation of the complete norm moment

## Hypotheses

Retain all hypotheses, embeddings, coefficient modules, maps and branches
of L123. In particular, A/Q is modular; K is imaginary quadratic;
p>=5 is inert in K and split multiplicative for A; the conductor is
unramified in K with square-free inert part; the split-conductor
exponents are at most two; the residual image contains SL_2(F_p).
The source's incoherence condition holds for {p}, w=infinity, and the
character and conductor are trivial and one. The CM embedding is
integral at p and its fixed point tau reduces to the standard vertex.
No analytic-rank, rationality, finite-Sha or nonvanishing premise is added.

Write B for the source's indefinite quaternion algebra and G=B^*/Q^*.
Write z=tau_infinity, and use psi for the fixed embedding of K and its
torus into B and G. The fixed finite list {h_t} is exactly L123's list
from source equation (68); its p-components are 1. No representatives
are silently replaced or the list enlarged. Write Phi for the source's
measure-valued automorphic function and retain its maps j_m varphi_m.
The symbols X, M, r_tau, nu and J are those of L123. Put

\[
 q_\tau=\log_p N_\tau=\log_p r_\tau,\qquad
 J=\int_X q_\tau\,d\mu .                                      \tag{1}
\]

Let c_infinity be complex conjugation for the fixed complex embedding,
acting on coefficients by C_infinity. Keep L123's distinct p-decomposition
lift d and coefficient action C_d; neither lift is substituted for the
other on raw coefficients.

Source inputs (imported, not reproved):

- Blasius--Guerberoff, *Complex conjugation and Shimura varieties*,
  Algebra & Number Theory 11 (2017), 2289--2322,
  [doi:10.2140/ant.2017.11.2289](https://msp.org/ant/2017/11-10/ant-v11-n10-p02-s.pdf),
  Section 2.2, Lemmas 2.2.1 and 2.2.4 with Remark 2.2.3 and the
  real-reflex-field paragraph on p.2297. Apply its canonical-model
  action at small levels, then descend as justified below.
- Fornea, *Plectic Heegner classes*,
  [arXiv:2603.28327v2, 13 April 2026](https://arxiv.org/html/2603.28327v2),
  (5), (10), (14), Section 2.1.2, (20)--(23), Corollary 3.9,
  (34)--(35), (63)--(64), and (68)/Corollary 4.24. L123 supplies the
  already audited construction, projection domain and descent.
- The standard Skolem--Noether theorem: two embeddings of a separable
  field into a central simple algebra are conjugate by an invertible
  element. Only the embeddings psi and psi composed with conjugation
  are used here. The additional local and kernel assertions below
  are proved explicitly; they are not attributed to that theorem.

## Conclusion

Choose n in G(Q), represented by an invertible element of B, such that

\[
 n\psi(a)n^{-1}=\psi(\bar a)\quad(a\in K).
\]

Such an n exists. It interchanges z and bar(z), and tau and bar(tau).
Its p-component and inverse belong to K_{p^0}=PGL_2(Z_p). Define

\[
 k=n_p^{-1},\qquad
 w_p=1,\quad w_v=n_v^{-1}\ (v\ne p,\infty),\qquad
 \mu_n=\sum_t\Phi(h_t^{-1}w)(z),
\]
\[
 \nu_n=(r_\tau)_*\mu_n,\qquad J_n=\int_X q_\tau\,d\mu_n.       \tag{2}
\]

The inverse in h_t^{-1} is in G, and the sum retains the original
indexed representatives. These are genuine M-valued measures and
complete integrals at the original coefficient tower, not pointwise
elliptic projections. The exact formulas are

\[
 C_\infty\mu=(k^{-1})_*\mu_n,\qquad
 N_\tau(ks)=-N_\tau(s),\quad r_\tau(ks)=r_\tau(s),             \tag{3}
\]
\[
 \boxed{C_\infty\nu=\nu_n,\qquad C_\infty J=J_n.}             \tag{4}
\]

Thus the local normalizer contributes no logarithmic minus sign and no
surviving logarithmic constant. The remaining transformation is the
explicit tame translation w and inversion of the indexed CM torus
coordinates in (2).

Let h=d c_infinity^{-1} in G_K and H its coefficient action. Then

\[
 C_dJ=H J_n.                                                  \tag{5}
\]

All subsequent operations are on complete integrals. With B_0=pr_A(J
tensor 1) in H^1(L_1,V), b=desc(B_0), put

\[
 B_n=\operatorname{pr}_A(J_n\otimes1),\qquad b_n=\operatorname{desc}(B_n).
\]

These expressions are defined, B_n=c_infinity* B_0, and b_n=c b. In
particular, H acts trivially on B_n after its lift to H^1(L_1,V), and

\[
 \boxed{R=\operatorname{loc}_p(b+b_n),\qquad
 D^{++}=\tfrac14 u_1\otimes\operatorname{loc}_p(b+b_n).}        \tag{6}
\]

No scalar action of w, zero/nonzero value of R, or additional local
finite condition is asserted. For a single scalar epsilon, an eventual
proof b_n=epsilon b would give R=(1+epsilon)loc_p(b). The computation
here supplies neither epsilon nor that scalar premise.

## Proof

**Rational normalizer and CM orientation.** Skolem--Noether applied to
psi and psi composed with the nontrivial automorphism of K gives an
invertible representative of n. Its conjugation permutes the two
eigenspaces of the embedded K at both infinity and p; hence it
interchanges the two specified fixed points, rather than fixing their
orientation. This is a rational element constructed using the CM
embedding, not the real normalizer in the cited canonical-model theorem.

For completeness, n^2 centralizes K and hence lies in K^* before
passing to G. Conjugation by n on that field is its nontrivial
automorphism, while n commutes with n^2. Thus n^2 is rational, and n
is an involution in G. We will not infer any Galois involution from this.

At p identify B_p with End_{Q_p}(K_p), with the embedded K_p acting
by multiplication. The lattice Lambda=Z_p^2 in the chosen coordinates
is stable under O_{K_p} by the integral CM hypothesis. It is a
torsion-free rank-one O_{K_p}-module, so choose an O_{K_p}-basis.
An element conjugating K_p by its nontrivial automorphism then acts
as x -> a bar(x), for a in K_p^*. As K_p/Q_p is unramified, write
a=p^e u with u in O_{K_p}^*. Multiplication by p^{-e}, a central
Q_p-scalar, makes this a lattice automorphism. Thus n_p and k have
GL_2(Z_p) representatives. Their determinant valuations are even
before this rescaling and zero afterwards, so the twist in source
(5) is trivial. The standard vertex is preserved: no vertex change,
semigroup uniformizer or compensating noncompact operator is omitted.

**Canonical conjugation at the actual levels.** For the source's
indefinite quaternionic datum, the reflex field is Q and the connected
center of G is trivial. These satisfy the relevant hypotheses of
Blasius--Guerberoff. The datum coordinate may be identified with its
complex fixed point in P^1(C) minus P^1(R): composing its Deligne-torus
map with complex conjugation interchanges the two complex eigenlines.
Under this identification the conjugate coordinate is bar(z), not
minus bar(z) or an entrywise conjugate finite adele. At a sufficiently
small compact open U the cited theorem consequently gives

\[
 c_\infty[z,g]_U=[\bar z,g]_U.                               \tag{7}
\]

No neatness of K_m is assumed. Choose a sufficiently small U inside
K_m, use (7) on the lift [z,g]_U and push it down by the canonical
level map over Q. The result is [bar(z),g]_{K_m}. Any other lift
differs by a K_m-coordinate and gives the same image. This proves
(7) at K_m. The same argument applies to the intersected levels
below. Compatibility uses the canonical maps, not division by their
degrees or an assertion that all CM points avoid stabilizers.

For a cell xi X_m choose xi supported at p, which is possible because
K_m=K_0^{p} K_{p^m}. Equation (7), the left G(Q)-equivalence in the
double quotient, and the normalizer relation give

\[
 \begin{split}
 c_\infty[z,h_t\xi]_{K_m}
 &=[\bar z,h_t\xi]_{K_m}\\
 &=[z,n_f^{-1}h_t\xi]_{K_m}\\
 &=[z,h_t^{-1}w k\xi]_{K_m}.                                \tag{8}
 \end{split}
\]

Here conjugation on K^*/Q^* is inversion, since a bar(a) is central.
Both w and h_t have p-component 1. Thus (8) keeps the rightmost
level K_m unchanged and acts on its p-cell by *left* multiplication
by k. This is valid without k normalizing K_{p^m}; a left action on
K_{p^0}/K_{p^m} needs no such normalization.

Corollary 3.9, with the same target maps j_m varphi_m on both sides,
now shows

\[
 (C_\infty\mu)(\xi X_m)
 =\sum_t j_m\varphi_m([z,h_t^{-1}w k\xi]_{K_m})
 =\mu_n(k\xi X_m).                                          \tag{9}
\]

The source's varphi_m is the Hecke-normalized map in (22): it uses
T_l-l-1 divided by a_l(A)-l-1, a p-adic unit for the chosen auxiliary
prime. That exact map, its transition into the colimit, residual
localization and completion are retained. They commute with actual
Galois action because they are over Q. We have *not* commuted w
through this normalization or replaced varphi_m by a map to A.
The source provides trace compatibility for Phi evaluated at every
finite coordinate. Therefore (9) holds compatibly under refinements
and in M; it proves the first equality of (3) on all compact opens.

**The remaining level correspondence.** The w in (8) is fixed, has
trivial p-component, and need not normalize the tame level. Put

\[
 K'_m=w K_m w^{-1},\qquad C_m=K_m\cap K'_m.
\]

Right translation by w is an isomorphism X_{K'_m} -> X_{K_m}.
At the common level C_m the two maps are

\[
 a_m:[z,g]_{C_m}\longmapsto[z,g]_{K_m},\qquad
 b_m:[z,g]_{C_m}\longmapsto[z,gw]_{K_m}.                      \tag{10}
\]

Indeed w^{-1} C_m w is contained in K_m, which verifies the second
map's well-definedness. The maps are over Q and compatible with
increasing m. Their p-level remains K_{p^m} on both sides, because
w_p=1. In a cell of mu_n the actual lift is
[z,h_t^{-1}xi]_{C_m}; its b_m-image is
[z,h_t^{-1}w xi]_{K_m}, since w commutes with xi.

This specifies the correspondence branch at **every** deep level.
The Hecke operator [K_m w K_m] on a divisor is the pushforward
along b_m of its full pullback along a_m, hence sums the branches
described in source Section 2.1.2. Formula (9) does not take that
full pullback: it uses the displayed CM lifts. Replacing it by that
Hecke operator requires a further trace/multiplicity argument. Even
if w normalizes K_m, its action on the completed specialized CM
moment still needs evaluation. Good-prime Hecke eigenvalues alone
do not supply this missing branch or scalar identity. No replacement
of (10) by a shallow elliptic quotient is made.

**Local kernel and constants.** Choose a matrix representative K_0
of k in GL_2(Z_p). Source (35) identifies its left action as

\[
 [(v,z_0)]\longmapsto[(K_0v,\det(K_0)z_0)].
\]

This formula is unchanged by scaling the representative by a unit.
Let ell_tau=(1,-tau). Since k interchanges the column lines
(tau,1) and (bar(tau),1), there is alpha in K_p^* with

\[
 \ell_\tau K_0=\alpha\ell_{\bar\tau},\qquad
 \ell_{\bar\tau}K_0=\bar\alpha\ell_\tau.
\]

The two rows are independent. Taking the determinant of this action
on their two-dimensional space gives det(K_0)=-alpha bar(alpha).
For every primitive v, division by the transformed determinant
coordinate therefore gives

\[
 N_\tau(k[(v,z_0)])
 =\frac{\alpha\bar\alpha}{\det(K_0)}N_\tau([(v,z_0)])
 =-N_\tau([(v,z_0)]).                                       \tag{11}
\]

All numerator factors are nonzero, as in L123. Since p is odd,
-1 is a Teichmuller unit and log_p(-1)=0. Thus the potential additive
constant is exactly log_p(-1)=0; also r_tau(k s)=r_tau(s).
This retains and computes the constant rather than invoking a
mass-vanishing theorem to erase it. It concerns the *norm* kernel;
no individual f_tau constant has been separately discarded.

Combining (9) and (11) yields C_infinity nu=nu_n on every compact
open of 1+p Z_p. For the integral, first apply change of variables
to locally constant functions on X. Approximate q_tau uniformly by
such functions and use p-adic completeness and continuity of the
coefficient action, exactly in the raw module of L123. This gives
C_infinity J=J_n. No limit is moved through tensoring with I or
through pr_A; (4) is established before either operation.

**The intervening reciprocity action and descent.** The equality
d=h c_infinity is an equality of actual Galois elements. Hence its
coefficient action gives (5), with H retained. It cannot be removed
from raw cells merely because the final character is trivial.
More explicitly, at any fixed level take the finite compositum F_m
of the CM point fields of the points on the last line of (8).
For its restriction to F_m, choose a representative u_m in the
CM reciprocity quotient with geometric-Frobenius convention.
Shimura reciprocity (14) gives the finite-level formula

\[
 (C_d\mu)(\xi X_m)=\sum_t j_m\varphi_m
    ([z,\psi(u_m)h_t^{-1}w k\xi]_{K_m}).                     \tag{12}
\]

The finite quotient exists by CM class field theory; for the
compositum use the intersection of the finite open reciprocity
kernels. Representatives need not be asserted compatible as ideles:
their actions on overlapping fields are compatible because all
represent the same h. Formula (12) retains their p-components and
all finite coordinates. It makes no raw invariance or extra kernel
change. Equivalently their continuous limit on the actual coefficient
classes is H. This is the intervening action missing from an
unqualified identification of c_infinity and d.

By (4), J_n tensor 1 has the required invariant projection domain:
it is C_infinity applied to J tensor 1, whose domain was proved
in L123. The coefficient naturality argument there applies to
c_infinity as well as to d: it uses maps over Q and does not require
a p-decomposition lift until localization. Thus
B_n=c_infinity* B_0 in the cohomology over K^ab. The unique lift
to H^1(L_1,V), and its invariance under Gal(L_1/K), follow from
L123: L_1 is conjugation-stable and B_0 comes from b in H^1(K,V).
Conjugation preserves that invariant subspace. It follows that
H B_n=B_n there, since h is in G_K and its action factors through
Gal(L_1/K); elements of G_{L_1} act trivially on cohomology by the
inner-cocycle calculation of L123. Consequently

\[
 \operatorname{pr}_A((J+H J_n)\otimes1)=B_0+B_n.
\]

Apply equivariant finite descent (corestriction divided by [L_1:K]
on invariants), then localize using L123's p-decomposition lift.
This proves (6). There is no assumption that p avoids [L_1:K], and
no attempt to localize via the archimedean lift itself.

**Result and boundary.** Equations (2), (8)--(12) remove the unknown
outer conjugate points from the arithmetic specification and compute
the entire local kernel effect. The unevaluated object is now the
moment on the fixed tame correspondence (10), with the original
finite CM list inverted. This is more specific than naming C mu:
it isolates a correspondence independent of m at p, an exact
unchanged scalar weight, and the precise chosen branches whose
comparison would be necessary for a scalar argument.

The bounded specialization stops here. No comparison of b_n with b
other than its conjugation identity is proved, and no sign for that
comparison is imported. In particular (6) alone does not constrain
the value of R to zero or to nonzero. A continuation needs the actual
action of (10) on the traced, integrated specialization (or another
independent local test), not a repeated kernel-sign calculation.
Nonvanishing, rational Kummer membership, admissible auxiliary
choices, a multiplicative-prime rank criterion and general BSD
remain separate gaps. This is a known-source specialization
(REPRODUCTION), not a claim of progress beyond the checked sources.

**Separate critical audit, step 520 (2026-10-27).** PASS for the stated
transformation and descent, relative to the cited source construction
and L123. The audit checked (3)--(12), including the rational normalizer
versus the real canonical-model normalizer, descent through small levels,
the actual selected lifts at C_m, the complete-integral projection domain,
the unique cohomology lift and finite rational descent. No statement or
mathematical premise was changed. In particular, the equality of the
projected classes is first in H^1(K^ab,V); its equality over L_1 uses
L123's injective restriction, not a new descent of raw coefficients.
The intervening H is retained until that lift and its invariant character
are established. This audit accepts the correspondence specification,
not a full-branch trace identity, scalar eigenvalue, evaluation of R or
new BSD case. Mathlib coverage remains as stated below.

## Mathlib

The full CM normalizer/moment comparison, its canonical-model and
completed-cohomology inputs, and supporting matrix and measure
formalizations: **not checked**. This records no absence claim.
The cited source theorems and Skolem--Noether are mathematical
inputs, not assertions of matching Mathlib declarations.
