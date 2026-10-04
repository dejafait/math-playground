# L046 — Bogomolov excludes the fixed lower Chern data in every rank

## Hypotheses

Fix the very general cubic RM K3 surface S, X=S x S and the exact
final ample chamber of L044 (9)--(12). Use its cup-product pairing q,
point class eta with integral_S eta=1, ample real class h=omega_c,
self-adjoint operator A_c and correction tensor B_c. Write
N=NS(S)_Q, W=im(A_c), K=ker(A_c) and T=N^perp. Thus

\[
A_c h=\lambda h,\qquad h\in W,\qquad
1<\lambda<3/2,\qquad \lambda^3+\lambda^2-2\lambda-1=0.
\]

Let Omega=p_1^*h+p_2^*h be the actual product Kahler class.
The proposed bundle F is holomorphic and locally free of arbitrary
positive rank r, slope-polystable with respect to Omega, with

\[
c_1(F)=0,\qquad \operatorname{ch}_2(F)=\beta=2[C]+B_c
\]

in rational cohomology. No presentation, K-class, third or fourth
character, or rank-two hypothesis is imposed.

## Conclusion

Put s=q(h,h)>0. The full second character has the intersection

\[
\int_X\beta\,\Omega^2=(8+4\lambda)s>0.                 \tag{1}
\]

Consequently no such polystable locally free bundle exists in any
positive rank. In fact the same exclusion applies to slope-semistable
locally free bundles with these data. Arbitrary higher Chern classes
cannot repair the necessary inequality.

This is an informative NEGATIVE specialization of the cited
Bogomolov inequality, classified as REPRODUCTION. It closes the
fixed lower-data recipe independently of L045's particular K-class
exclusion. It does not exclude different point coefficients, other
divisor corrections, nonzero first Chern class or other cycle
representatives. No new cycle or transverse surface is supplied;
the span remains 21, with three RM directions attained against four
required. The universal rational Hodge conjecture remains unresolved.

## Proof

**Import the inequality with its actual sign and polarization.**
Use Arvid Perego, *Kobayashi-Hitchin correspondence for twisted
vector bundles*,
[arXiv:1910.01867v1, Corollary 6.42, p. 118](https://arxiv.org/pdf/1910.01867v1#page=118).
For a slope-semistable bundle of rank r on a compact Kahler
n-fold with metric form sigma_g, it gives

\[
\int_X\bigl((r-1)c_1(F)^2-2r c_2(F)\bigr)
                         \sigma_g^{n-2}\leq0.           \tag{2}
\]

Take the trivial twisting cocycle and zero auxiliary B-field, so
the Chern classes are ordinary ones. That auxiliary B-field is
unrelated to B_c. Definition 4.20, p. 65, includes semistability
in polystability. Definition 4.7, p. 59, uses slope against the
metric's real form, and sections 3.1--3.2, pp. 41--44, specify
the Chern-class conventions. These statements were inspected in
the prior assessment. They apply directly to Omega; neither an
integral polarization nor a rational approximation preserving
stability is needed. Import (2) without reproving curvature or
the Kobayashi-Hitchin correspondence.

The character identity
ch_2=(c_1^2-2c_2)/2 from
[Stacks Section 42.45, Tag 02UM](https://stacks.math.columbia.edu/tag/02UM)
gives c_2(F)=-beta here. Since n=4, the left side of (2) is
therefore 2r integral_X beta Omega^2. Its required sign is
nonpositive, not nonnegative.

**Contract the full prescribed class.** Put e_1=eta tensor 1 and
e_2=1 tensor eta. L044 supplies the full Kunneth decomposition

\[
\beta=4e_1+4e_2+\tau_D,\qquad
D|_N=2A_c+4\pi_K,\qquad D|_T=2U.                       \tag{3}
\]

Here tau_D is the mixed H^2 tensor H^2 class, with correspondence
action D under the cup-product pairing. Both point coefficients
are four: the projections of C have degree two, and B_c is purely
mixed. The operator is q-self-adjoint. Since h is in W and is the
lambda eigenvector, (3) gives D h=2lambda h.

For a tensor tau=sum_i a_i tensor b_i define its action by
D_tau(x)=sum_i q(x,a_i)b_i. Then directly

\[
\int_X\tau\,(h\otimes h)=q(h,D_\tau h).               \tag{4}
\]

All degrees are even, so this formula has no Koszul minus sign.
It includes every mixed component. The T tensor T part in (3)
contributes zero because h belongs to N and q(N,T)=0; no full
second-character component is otherwise dropped.

On S, h^2=s eta. Hence

\[
\Omega^2=s(e_1+e_2)+2h\otimes h.
\]

The relations e_1^2=e_2^2=0, integral_X e_1e_2=1 and the
vanishing of the pure/mixed products in top degree now give

\[
\begin{aligned}
\int_X\beta\Omega^2
 &=4s+4s+2q(h,Dh)\\
 &=8s+4\lambda s=(8+4\lambda)s.
\end{aligned}
\]

Ample-cone membership in L044 ensures s>0, and lambda>1.
This proves (1). Substitution in (2) gives
2r(8+4lambda)s>0 for every r>0, contradicting its required sign.
Equivalently, the usual discriminant
2r c_2-(r-1)c_1^2 has strictly negative integral against Omega^2.
No higher character appears in this contradiction.

**Exact arithmetic check.** In L044's basis (f_ell,O,E_exc,P),
the scaled vector v=lambda h has coordinates
(2lambda^2+3lambda+1,lambda+1,-1,0). Its square under G is
4lambda^3+8lambda^2+4lambda-2. Reducing by the cubic relation
gives

\[
\lambda^2s=4\lambda^2+12\lambda+2,\qquad
\lambda^2\int_X\beta\Omega^2
             =64\lambda^2+136\lambda+32.               \tag{5}
\]

Both are positive without decimal root approximations. A direct
exact calculation in Q[t]/(t^3+t^2-2t-1), using L044's integral
g and B_0 and the mixed tensor matrix 4G^{-1}+gB_0g^t, agrees
with (5) and verifies Dv=2lambda v. The arithmetic checkpoint is
recorded in `drafts/2026-10-04-fixed-lower-chern-bogomolov-calculation.md`.
The proof uses the cited inequality and the cohomological
contraction above, rather than numerical evidence or virtual-bundle
existence. Invariance of the lower classes alone does not imply
polystability or supply the missing compatible representative.

## Mathlib

Coverage of the full fixed-data exclusion: **not checked**. No
matching Mathlib declaration or absence from checked Mathlib sources
is asserted. Perego's linked corollary supplies the inequality;
the linked Stacks section supplies the character conversion.
These are supporting results, rather than a match for this entire
evaluated statement. Kunneth and the cup-product tensor contraction
are standard supporting tools. This numerical specialization is a
reproduction with no originality or general Hodge resolution claim.
