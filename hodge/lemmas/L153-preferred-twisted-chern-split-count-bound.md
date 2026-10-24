# L153 — Preferred twisted Chern split-count bound

## Hypotheses

Retain L147's identical marked projective K3 factors S_1 and B, original
common hyperkähler metric g and real Kähler class h. Suppose F on S_1 x B
is locally free of rank two, slope-polystable for
Omega=p_1^*h+p_2^*h, with integral c_1(F)=0 and
ch_2(F)=-14e_1-21e_2-tau_D, with the full tensor and fixed chamber of L147.
Let k=(-4,-2,1,2), k.h=0, k^2=-14, and use exactly L152's preferred
dual HE metric on the twisting line L^{-1}. Let
M=R^1p_{2*}(F tensor p_1^*L^{-1}) and let Z be the finite, possibly
empty, split-parameter set. Use audited L147 and L152 for this same M.
Normalize the integral point class by integral_B eta=1.
Neither F nor a nonempty Z is known to exist.

## Conclusion

The actual M is slope-polystable of slope zero at the original real h,
allowing reducibility, and its full Chern inequality gives

\[
 \int_B\bigl(23c_1(M)^2-48c_2(M)\bigr)
      =48|Z|-7792\leq0.
\]

Consequently

\[
                         \boxed{0\leq |Z|\leq162.}
\]

This is a conditional ADVANCE / REPRODUCTION of known tools. The separate
critical audit below preserves it without repair or strengthening.
It supplies a necessary upper restriction only,
not F existence, nonempty Z, a contradictory lower count, an algebraic
cycle, transverse transport or universal primitive Hodge realization.

## Proof

Reuse the invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-23-preferred-twisted-chern-bound.md`.
Import Arvid Perego, *Kobayashi-Hitchin corrispondence for twisted vector
bundles*, [arXiv:1910.01867v1](https://arxiv.org/pdf/1910.01867v1)
(4 October 2019), Definition 3.7, printed p. 47, Definition 4.20 and
Theorem 4.21, printed p. 65, and Corollary 6.42, printed p. 118.
Theorem 4.21 makes a Hermite–Einstein bundle on a compact Kähler manifold
polystable; Corollary 6.42 gives for a semistable rank-r bundle on a
compact Kähler n-fold

\[
 \int ((r-1)c_1^2-2r c_2)\wedge\sigma_g^{n-2}\leq0.
                                                        \tag{1}
\]

Use the ordinary-bundle case, with trivial twisting cocycle and zero
auxiliary B-field. These statements allow nonzero c_1, a real Kähler
metric and reducibility. Import the general theorems without reproof;
only their surface specialization and arithmetic are needed here.

**Metric hypothesis on the actual bundle.** L152 gives a smooth positive
Hermitian metric on L147's specific M over the entire compact surface B.
Its Chern connection is ASD for the original g with complex orientation.
On a Kähler surface, coefficientwise complexification of the Hodge-star
decomposition gives

\[
 \Lambda^2_{\mathbb C}
   =\bigl(\mathbb C\omega_I\oplus\Lambda^{2,0}
                         \oplus\Lambda^{0,2}\bigr)
      \oplus\Lambda^{1,1}_0,
\]

where the first parenthesis is self-dual and the last summand is
anti-self-dual. Thus the full unitary curvature of this connection
satisfies Lambda_{omega_I} F_M=0. In Perego's Definition 3.7 this is
Hermite–Einstein with constant scalar factor zero. It is the same metric
and holomorphic M as in L147, not merely another extension of an abstract
punctured bundle. Theorem 4.21 therefore supplies slope-polystability
at h and, in particular, semistability. Also
c_1(M).h=-4k.h=0 directly checks its zero slope. No irreducibility or
determinant-triviality hypothesis is used.

**Entire signed discriminant.** L147 supplies rank r=24,
c_1(M)=-4k and c_2(M)=(55-z)eta, where z=|Z|. In particular

\[
                   c_1(M)^2=16k^2=-224\eta.
\]

The surface has n=2, so the metric factor in (1) has exponent zero.
With the normalized eta the entire left side is

\[
 23(-224)-48(55-z)
       =-5152-2640+48z=48z-7792.                         \tag{2}
\]

Equation (1) gives z<=7792/48=487/3=162+1/3. Since Z is a finite set,
z is a nonnegative integer, giving z<=162. As a direct boundary check,
the signed value in (2) is -16 at z=162 and +32 at z=163. Thus 162
is precisely the largest integer allowed by this inequality, without
an equality-case argument. Equivalently, the usual opposite-sign
discriminant 2r c_2-(r-1)c_1^2 is 7792-48z and is nonnegative.

Every split-point correction remains in c_2(M) with the sign proved
in L147; no hull correction or ordinary split base change is inserted.
Although c_1(M) has degree zero, its square is nonzero and its full
contribution -5152 was retained. L115's determinant-trivial rank-48
normal bundle is different and its numerical conclusion is not an
input. Empty Z satisfies (2). The permitted integers are not claimed
realizable. ATTEMPTS/066's reflexivity-only inference, ATTEMPTS/067's
duality-only limitation and ATTEMPTS/086's arbitrary-metric obstacle
remain within their recorded scopes: the added input here is audited
smooth ASD curvature for the preferred metric.

The continuation test therefore passes for a necessary bound. An
independent lower comparison would still be needed to exclude F; no
such lower comparison is assumed or established in this step. The
universal primitive Hodge gap remains open.

**Separate critical audit, 2026-10-23 (step 497).** Reuse the unchanged
invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-23-preferred-twisted-chern-bound-critical-audit.md`.
The verdict is EXPLORATION / REPRODUCTION: the conditional bound and
polystability conclusion survive; no substantive error or stronger
conclusion is found. This is an audit of the known-tool specialization,
not a new mathematical input or progress beyond the inspected sources.
Perego's versioned Definition 3.7, Definition 4.20, Theorem 4.21 and
Corollary 6.42 were rechecked at the precise pages cited above; reuse
the assessment's prior proof coverage without reproving those theorems.

First, compare actual objects before applying the curvature theorem.
Both inputs use G=F tensor p_1^*L^{-1}, with the dual of the fixed HE
metric on L, the identical marked factors and original common g.
L147's M is the ordinary R^1 image on all of B, not its derived central
fibre or a virtual index. L152's audited conclusion transports the
smooth positive metric to that very holomorphic M by two inverse
holomorphic comparison maps. Its connection agrees with the preferred
harmonic Chern connection on U and is ASD on all B for the same g.
Consequently there is no further metric choice, punctured semistability
inference or unknown point correction between these inputs and (1).
The use of L148–L151 remains through audited L152; their proofs are not
reaudited here.

The orientation and central curvature matter. In an oriented unitary
orthonormal real coframe on B, omega_I=e^1 wedge e^2+e^3 wedge e^4
is self-dual for the complex orientation. Together with the real and
imaginary parts of a (2,0) form it spans the self-dual subspace; its
orthogonal complement is the real primitive (1,1) subspace. Apply this
identity to every real u(24)-coefficient of the actual curvature,
including the scalar coefficient. Thus i Lambda_g F_M=0 as an
endomorphism, not just after taking its trace or removing its centre.
Definition 3.7 gives the constant HE factor zero. Theorem 4.21 applies
to the ordinary holomorphic bundle on compact Kähler B with trivial
cocycle and zero B-field. Definition 4.20 supplies semistability as
well as a same-slope stable decomposition; it imposes neither
irreducibility nor an integral Kähler class. The slope computed from
c_1(M).h=-4k.h is also zero. This checks the entire theorem hypothesis.

Next retain every signed Chern term. L147 gives the actual character
24-4k+(z-167)eta and no hull quotient. Since k^2=-14eta, the character
identity recovers c_2=(-112-z+167)eta=(55-z)eta. In particular degree
zero has not erased c_1^2=-224eta. Corollary 6.42, with n=2 and r=24,
has no remaining Kähler power; integrating against integral_B eta=1
gives 23(-224)-48(55-z)=48z-7792. Independently its signed expression
equals 2r ch_2-c_1^2, which here is 48(z-167)+224 and gives the same
answer. This second evaluation checks both the point contribution
and the first-class term without redoing L147's GRR theorem application.

The real threshold is 487/3, so nonnegative integer z must be at most
162. The full signed values -16 at 162 and +32 at 163 verify the cutoff
and the inequality direction. No integer attains equality, but this
audit draws no equality-case or stability enhancement. Empty Z passes;
none of the permitted integers is asserted realized. The rank-48
normal-bundle bound is not a mathematical input. The earlier failures
in ATTEMPTS/066/067/086 remain unchanged in their stated scopes.

Direct mathematical inputs remain L147 and L152, with no changed DAG
edge or argument assembly. F existence, nonempty Z and an independent
lower comparison remain unresolved. The audit validates only the
conditional upper restriction and supplies no cycle or transport.

## Mathlib

Full matching coverage of the real-Kähler HE/Chern theorem and this
conditional higher-image specialization is **not checked**. Unknown
availability is not evidence of absence. The cited general theorems
are imported, and the surface applicability and exact arithmetic above
are their local REPRODUCTION, without a novelty or Lean-verification claim.
