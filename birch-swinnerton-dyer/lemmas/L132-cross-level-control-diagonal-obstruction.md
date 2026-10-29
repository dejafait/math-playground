# L132 — The literal cross-level control diagonal has excess multiplicity

## Hypotheses

Retain L123's original hypotheses: A/Q is modular, K/Q is imaginary
quadratic, p>=5 is inert in K and split multiplicative for A; the
conductor is unramified in K, its inert part is square-free and its
split exponents are at most two; the residual image contains SL_2(F_p).
Keep the incoherent set {p}, w=infinity, conductor-one trivial-character
CM data, and the original integral embedding and levels. This calculation
uses only the original geometric curves at levels 1,2 and their finite
correspondences; it changes none of those arithmetic hypotheses.

Use the integral lattices and comparison of audited L131. Thus
L_n=H_1(X_n(C),Z_p), with sums over proper components,
V_n=T_p(J_n), D_n=Hom_Zp(V_n,Z_p(1)), and iota_n:D_n -> L_n is
integral evaluation. At p,

\[
 K_n=\left\{\begin{pmatrix}a&b\\c&d\end{pmatrix}\in
 \mathrm{GL}_2(\mathbf Z_p):c\in p^n\mathbf Z_p,
          a/d\in1+p^n\mathbf Z_p\right\}/\mathbf Z_p^\times.
\]

All tame components are unchanged. Put g=diag(1,p) at p, identity
elsewhere, and pi:X_2 -> X_1 for forgetting. Write U_n^cov for
the covariant cycle [K_n g K_n]. Write A_n=(U_n^cov)^t for its
transpose, the action of the physical U_n label transported from D_n
by iota_n. Let P_n be the integral projector onto the adjoint-ordinary,
trivial-finite-diamond summand S_n=iota_n(D_n^0). In particular,
A_n is an integral automorphism of S_n, and L131 gives

\[
 \pi_*P_2=P_1\pi_*,\qquad \pi_*A_2=A_1\pi_*.
                                                        \tag{1}
\]

Let Gamma_n=(1+p Z_p)/(1+p^n Z_p), acting on S_n with the
transported, inverse diamond labels. Gamma_1 is trivial. Put

\[
 B=S_2\otimes_{\mathbf Z_p[\Gamma_2]}\mathbf Z_p
   =S_2/\langle(\gamma-1)x\rangle,\qquad q:S_2\longrightarrow B.
\]

The ring map is augmentation, not a normalized averaging operator.
Diamond compatibility makes pi_* descend to
bar-pi:B -> S_1. No freeness of B over Z_p, control isomorphism,
auxiliary neat level, residual localization or completion is assumed.

The source convention being tested is the literal geometric
correspondence T=[K_1 g K_2]:X_1 --> X_2 of Fornea,
[*Plectic Heegner classes*, arXiv:2603.28327v2, 13 April 2026](https://arxiv.org/html/2603.28327v2),
Section 2.1.2, Definition 2.3/(15), and Definition 2.8. Its two legs
give T^cov=b_*a^! on homology. Fornea Section 2.4, Lemma 2.22,
[printed pp.17--18](https://arxiv.org/pdf/2603.28327v2), uses a
diagonal with this label from level one to level-two coinvariants.
One necessary triangle is forgetting after the diagonal equals U at
level one. This lemma tests that triangle on S_n; it does not identify
S_n with the source's M_n^bullet by assumption.

The integral transfer, evaluation and projector facts are imported
through L131, using Fornea Proposition 2.9 (both p-level cases),
Remark 2.12/(21), Milne, *Jacobian Varieties*, corrected 12 June 2021,
[Theorem 2.5 and Proposition 6.1/Corollary 6.3](https://www.jmilne.org/math/xnotes/JVs.pdf),
pp.7--8,19--20, and Sertoz--Ouaknine--Worrell,
[*Computing transcendence and linear relations of 1-periods*, arXiv:2505.20397v1](https://arxiv.org/html/2505.20397v1),
(4.5.54)--(4.5.55), (7.3.29)--(7.3.35), (7.4.37)--(7.4.42).
All markings and punctures are empty; smooth proper characteristic-zero
components meet these comparison hypotheses. Their general results
are not reproved. The additional calculation is the exact cross-level
index and its specialization to the proposed diagram.

## Conclusion

The literal cross-level cycle has source-leg degree p^3 and target-leg
degree p, counting all components and ramification multiplicities, and

\[
             \pi_*T^{cov}=p^2U_1^{cov}:L_1\longrightarrow L_1.
                                                        \tag{2}
\]

Even allowing integral ordinary projection, its candidate diagonal

\[
 Q=qP_2T^{cov}|_{S_1}:S_1\longrightarrow B
\]

satisfies

\[
 \bar\pi Q=p^2P_1U_1^{cov}|_{S_1},\qquad
             (\bar\pi Q)(S_1)\subseteq p^2S_1.             \tag{3}
\]

If S_1 is nonzero, this cannot equal A_1|_{S_1}, which is invertible
modulo p. Thus this diagonal does not satisfy the required triangle
on the proposed integral modules. If T^cov already preserves S_n,
the projector in Q is redundant and the same failure holds.

Dualizing the physical Jacobian map of this very same cross-level
cycle instead gives a map D_2 -> D_1, hence L_2 -> L_1 under iota.
It does not supply the printed arrow S_1 -> B. Consequently neither
literal covariance nor simply invoking L131's duality establishes the
proposed full labeled identification. A different convention for that
arrow would require justification; none is inferred here.

This is an informative negative for this finite specialization,
REPRODUCTION of a known-method multiplicity calculation. Separate
critical review is pending. It does not disprove the source's control
theorem in another justified convention, exclude every controlled
comparison, prove L128's scalar false, or supply a BSD counterexample.
If S_1 is zero, the mod-p contradiction is inapplicable; identification
with any nonzero intended target would already fail at level one.

## Proof

**Both legs and every generic branch.** Use local matrix
representatives modulo unit scalars and set

\[
 H=K_1\cap gK_2g^{-1},\qquad H_0=K_1\cap gK_1g^{-1}.
\]

For k=[[a,b],[c,d]],

\[
 g^{-1}kg=\begin{pmatrix}a&pb\\c/p&d\end{pmatrix}.
\]

It follows, with a,d units, that H has exactly the extra conditions
c in p^3 Z_p and a/d in 1+p^2 Z_p, whereas H_0 has c in p^2 Z_p
and a/d in 1+p Z_p. In particular

\[
       H\subset K_2\subset H_0\subset K_1.
\]

Each successive index is p. For K_1/H_0 take representatives
[[1,0],[p t,1]], t modulo p. For any k in K_1, there is a unique
t such that c-pt a is divisible by p^2; left multiplication by
the inverse representative preserves the diagonal condition modulo p.
For H_0/K_2 the ratio a^{-1}d modulo p^2 is a homomorphism to
(1+p Z_p)/(1+p^2 Z_p), since the off-diagonal product in a matrix
product is divisible by p^2. Its kernel is K_2 and representatives
are diag(1,1+pj), j modulo p. For K_2/H use
[[1,0],[p^2 t,1]]; the same elimination of c now preserves the
diagonal condition modulo p^2. These verifications prove

\[
        [K_1:H]=p^3,\qquad [H_0:H]=p^2.                 \tag{4}
\]

Also g^{-1}Hg is precisely the subgroup of K_2 with upper-right
entry divisible by p. It has index p: representatives are the
upper unipotents [[1,t],[0,1]], and elimination of the upper-right
entry preserves a/d modulo p^2 because c is divisible by p^2.
Thus the two maps

\[
 a:X_H\longrightarrow X_1,\quad [z,h]\longmapsto[z,h],
 \qquad b:X_H\longrightarrow X_2,\quad[z,h]\longmapsto[z,hg]
\]

have the stated respective degrees p^3 and p. The original projective
arithmetic action has trivial generic stabilizer, as in L131. Degrees
are total degrees above each target component. Elliptic points and
cusps may ramify; they do not remove branches from these degrees.

**Composition as proper correspondences.** Let j:X_H -> X_H0
be forgetting. Let a_0:X_H0 -> X_1 be forgetting and
b_0:X_H0 -> X_1 right translation by g. Their cycle is U_1^cov,
and their proper-map identities are

\[
                    a=a_0j,\qquad \pi b=b_0j.
\]

They hold on the open Shimura curves by their adelic formulas and
therefore on the smooth proper extensions. The degree of j above
each component is p^2 by (4). The integral transfer identity is
j_*j^!=p^2 id. It follows either from divisor norm/pullback and
the imported integral Jacobian comparison, or directly from the
transfer comparison cited above; it retains ramification multiplicities.
With composition rightmost first,

\[
 \pi_*b_*a^!
   =(b_0)_*j_*j^!a_0^!
   =p^2(b_0)_*a_0^!
   =p^2U_1^{cov}.
\]

This proves (2) on the whole integral lattice. It counts p^3 source
branches collapsing to p branches with multiplicity p^2. It is a
different composite from L129's pi_*U_2=p r_*; that older obstruction
is a comparison warning, not a premise for (2).

**Coinvariants and ordinary projection cannot remove the factor.**
For every gamma in Gamma_2, the transported diamond compatibility
gives pi_* gamma=pi_*: its image at level one is the identity.
This remains true for the inverse diamond convention, since inversion
preserves the augmentation ideal. Thus bar-pi q=pi_*|S_2.
Equation (1), already obtained by dualizing coefficient pullback,
implies

\[
 \bar\pi qP_2T^{cov}|S_1
       =\pi_*P_2T^{cov}|S_1
       =P_1\pi_*T^{cov}|S_1
       =p^2P_1U_1^{cov}|S_1.
\]

Every map here is integral. In particular q is a quotient; even if B
has torsion, this computation in S_1 is unchanged. No replacement of
coinvariants by invariants or averaging over the order-p group is used.
Nor is it assumed that U_1^cov preserves S_1: P_1 suffices.

L131 makes S_1 a finite free direct summand of L_1. If it is nonzero,
S_1/pS_1 is nonzero. A_1 is invertible on that reduction, whereas
bar-pi Q is zero there by (3). Hence bar-pi Q != A_1. The outer
square with A_2, A_1 and bar-pi does commute by (1), but the two
triangles demanded by a control diagonal include this failed equality.
The other triangle need not be tested after this first failure.
The achieved image bound p^2S_1 falls short of the required
automorphism of S_1; no rational rescaling is permitted by this test.

**Why precomposition duality does not fix that arrow.** The physical
cross-level map is a_{12}=b_*a^*:J_1 -> J_2. On V_1 -> V_2 it
corresponds to Tr_b a^* on cohomology. Its precomposition dual is
a_{12}^vee:D_2 -> D_1. For v in V_1 and ell in D_2, put
x=iota_2(ell). L131's integral evaluation gives

\[
 (a_{12}^\vee\ell)(v)
   =\langle\operatorname{Tr}_b a^*q_1(v),x\rangle
   =\langle q_1(v),a_*b^!x\rangle.
\]

Here q_1 is the Kummer/cohomology comparison of L131, distinct from
the coinvariant quotient q. Thus iota_1 a_{12}^vee=a_*b^!iota_2.
Its source is level two and its target level one. For endomorphisms
the reversal of endpoints is invisible; for this diagonal it is
essential. Keeping the same geometric cycle while dualizing is not
a construction of a level-one-to-level-two map. Choosing another
cycle, normalizing a trace, or postulating a separate homology
convention is outside the conclusion and was not done.

The bounded attempt therefore stops before the remaining uniformizer,
tame T and tame bad-U comparisons. It neither certifies nor refutes
those later labels. L128 stays on HOLD; residual relation transfer,
the scalar, rational Kummer membership, nonzero localization and
strictness remain unestablished. No control theorem was used to prove
the finite obstruction, and no assertion about the source's unspecified
cross-level homology convention is substituted for a proof.

## Mathlib

Full matching coverage of this cross-level Shimura correspondence,
its integral transfer and the proposed control comparison: **not
checked**. No absence or formal-verification claim is made. Supporting
matrix identities and finite-free-module facts are not a full matching
theorem. The proof is the exact subgroup-index, proper-map and integral
image calculation above; no numerical script or preview is evidence.
