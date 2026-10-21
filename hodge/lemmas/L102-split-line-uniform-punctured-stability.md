# L102 — Uniform punctured stability of the split-line complex family

## Hypotheses

Retain audited L094's marked projective K3 surface S, complex structure I,
hyperkähler metric g and its real Kähler class h. In particular L has
integral class k, k^2=-14 and k.h=0. The reference bundle E=L direct sum
L^{-1} has its fixed direct-sum Hermite--Einstein connection A of slope
zero. Use L094's harmonic operators I,J,K, its orthonormal positive-weight
vectors e_1,e_2, and v=e_1+Je_2, Jv=Je_1-e_2.

Fix any one actual determinant-trivial holomorphic slice family from
audited L101. Its harmonic parameter is a convergent map alpha(s,t),
alpha(0)=0, satisfying the complete integrability equations Psi(alpha)=0
and

\[
 alpha(s,t)=ell(s,t)+R(s,t),\qquad
 ell(s,t)=sB(v)+tB(Jv),\qquad R=O((s,t)^2),                 \tag{1}
\]

where B(w)=w^{0,1} and B(Iw)=iB(w). Its actual fibre is the slice bundle
with Dolbeault operator d+a(alpha), where d=bar-partial_A and
a(alpha)=alpha+d^*beta(alpha), exactly as constructed in L101.
No product kernel F or quaternionic parameter family is assumed.

## Conclusion

There is a single radius rho>0, depending on this fixed analytic family
and the reference connection, such that every fibre E_(s,t) with
0<sqrt(|s|^2+|t|^2)<rho is strictly slope-stable at the unchanged real h.
The central fibre remains the polystable split bundle E. The radius is
uniform over parameter directions, including both coordinate axes; no
radius uniform over all possible Artin approximations is asserted.

This is an ADVANCE / REPRODUCTION specializing known local stability
theorems. The separate critical audit below preserves it. It supplies a
local stable holomorphic prerequisite. Quaternionic integration, a common F, prescribed
global mixed action, separation, reconstruction, transport and universal
primitive rational Hodge realization remain unresolved.

## Proof

**Imported stability criterion.** Use Nicholas Buchdahl and Georg
Schumacher, *Polystable bundles and representations of their
automorphisms*, Complex Manifolds **9** (2022), 78--113,
DOI 10.1515/coma-2021-0131,
[published text](https://d-nb.info/1262812674/34), Theorem 8.1, p. 103,
and Theorem 5.4, pp. 93--94, with the scalar convention on p. 79.
Theorem 8.1 supplies a Hermite--Einstein connection for sufficiently small
GIT-polystable harmonic slice parameters; its radius depends only on the
reference connection. Actual integrability then gives bundle
polystability. Theorem 5.4 identifies parameter stability with vector
bundle stability once bundle polystability is established. The acting
group is the full vector automorphism group modulo common nonzero
scalars. These theorems are imported, not reproved. Their hypotheses use
a fixed compact Kähler metric, so no integral polarization is required.
The saved assessment covers this specialization; the following proof
checks the actual parameters and orbit, rather than repeating the
elliptic or uniformity arguments in the source.

**Two projections of the exact first jet.** The complex harmonic space
H=H^1(S,End E) has no diagonal sector, because H^1(S,O_S)=0. L094 and
L101 identify it with H_+ direct sum H_-, where
H_+=H^1(S,L^2) and H_-=H^1(S,L^{-2}); each has dimension 26. Write P_+
and P_- for the projections. Equip H with the Hermitian norm induced by
L094's real harmonic metric G through B: ||B(w)||^2=G(w,w).
This is a Hermitian norm because B is complex-linear for I and I is
orthogonal. The sectors are orthogonal, so these projections have norm
one. In this norm B(e_1),B(e_2) are orthonormal in H_+, and
B(Je_1),B(Je_2) are orthonormal in H_-: J exchanges sectors, is
anti-complex-linear, and preserves G. In particular these are actual
harmonic representatives, not arbitrary cohomology coordinates.

Since v=e_1+Je_2 and Jv=Je_1-e_2, complex-linearity of the projections
gives

\[
 P_+ell=sB(e_1)-tB(e_2),\qquad
 P_-ell=sB(Je_2)+tB(Je_1).                              \tag{2}
\]

Consequently, with r=sqrt(|s|^2+|t|^2),

\[
 ||P_+ell||=||P_-ell||=r,\qquad ||ell||=sqrt(2)r.        \tag{3}
\]

The anti-linearity of J does not conjugate the displayed coefficients:
ell is the prescribed I-complex-linear map sB(v)+tB(Jv), with Jv fixed.
Thus both separate projections are injective, including on both axes.

**Uniform estimate for the actual analytic remainder.** Choose r_0>0
such that the closed parameter ball of radius r_0 lies inside the domain
of this fixed convergent map and the L101 slice construction. Since
R(0)=0 and DR(0)=0, its real second derivative has a finite operator-norm
bound M on this compact ball. Taylor's integral formula along the segment
u(s,t), 0<=u<=1, is

\[
 R(s,t)=\int_0^1(1-u)D^2R(u(s,t))[(s,t),(s,t)]\,du.
\]

Hence ||R(s,t)||<=Cr^2 throughout the ball, for
C=max(1,M/2). Orthogonal projection and (3) imply

\[
 ||P_+alpha||>=r-Cr^2,\qquad ||P_-alpha||>=r-Cr^2.        \tag{4}
\]

For 0<r<min(r_0,1/(2C)), both are at least r/2>0, and
||alpha||<=sqrt(2)r+Cr^2<2r. The achieved lower bound is r/2
in each sector, against the required strict positivity. This is one
ball estimate; it does not choose a radius separately for each line.

**Full vector action on every actual parameter.** Audited L101 gives
Aut(E)=(C*)^2: vanishing of H^0(L^2) and H^0(L^{-2}) excludes
off-diagonal automorphisms, including exchanges. For diag(a,b) its
conjugation action on H sends (p,q) to (z p,z^{-1}q), where z=a/b.
The map (a,b) to z is onto C*, with kernel exactly the common scalars.
There is no diagonal harmonic coordinate or further component of H to
discard. Thus this is the full source action modulo common scalars,
not merely its determinant-one subgroup.

Fix any actual nonzero parameter in the ball in (4), and set
p=P_+alpha, q=P_-alpha. Both are nonzero. Its orbit is

\[
 \{(z p,z^{-1}q):z\in C^*\}.
\]

The subspace Cp direct sum Cq is closed in H. Identifying that subspace
with C^2 by (u,v) to (up,vq), the orbit is precisely the algebraic
closed subset uv=1. Thus the orbit is closed in the whole H; in
particular its closure cannot contain zero. A group element fixes
(p,q) only if z=1, since p is nonzero. Its full stabilizer in Aut(E)
is therefore exactly the common scalars, and its stabilizer in the
effective quotient is trivial. These statements apply to the complete
actual parameter alpha, including every higher-order coefficient.
They prove its GIT stability under the source convention.

**Fixed-radius theorem on the actual slice bundle.** The reference A is
integrable Hermite--Einstein at g, with i Lambda F_A=0, because both
line summands have h-degree zero. Let epsilon>0 be the radius from
Theorem 8.1, diminished if necessary to stay within the source's slice
and Theorem 5.4 neighborhoods. The harmonic norm in the source and the
one used in (3) are norms on the same finite-dimensional H; choose
K>=1 with ||x||_source<=K||x|| for all x in H. Choose

\[
 0<rho<min(r_0,1/(2C),epsilon/(2K)).                     \tag{5}
\]

For every 0<r<rho, alpha is GIT-stable and
||alpha||_source<2Kr<epsilon. The beta(alpha) used in L101 is exactly
the Proposition 2.6 solution: trace-free restriction preserved it by
uniqueness in the full vector slice. Its complete equations
Psi(alpha)=0 ensure that d+a(alpha) is the actual integrable
Dolbeault operator of E_(s,t). Thus Theorem 8.1 yields a
Hermite--Einstein connection in the complex gauge orbit of this very
holomorphic bundle and gives h-polystability. Theorem 5.4 then gives
strict h-stability from the GIT stability proved above. Every hypothesis
is satisfied at the original metric, and (5) is independent of the
nonzero parameter direction.

The central bundle has its proper equal-slope summand L, so is not
stable. Nothing in this argument constructs a unitary gauge varying
smoothly through zero, a quaternionic base family, or a product kernel.
In particular the fibrewise stability conclusion must not be promoted
to any of those stronger claims.

**Separate critical audit, 2026-10-14 (step 274).** The stated
uniform punctured stability survives. This audit is EXPLORATION /
REPRODUCTION: no substantive error, stronger theorem or additional
existence result was found. The approved source coverage is reused;
Proposition 2.6/(2.4), Theorems 5.4/8.1 and the relevant stability/splitting
proof cases were checked again in the published text cited above.
The following checks concern this actual family and do not reprove the
imported analytic theorems.

First, the norm in (3) is an auxiliary transported norm, so no unstated
normalization of the real-to-Dolbeault map is needed. More explicitly,
for real harmonic w,z define

\[
 H_G(Bw,Bz)=G(w,z)-iG(Iw,z).
\]

Orthogonality and I^2=-1 show that this is a Hermitian inner product,
linear in its first argument, with H_G(Bw,Bw)=G(w,w). L094's real
harmonic/Dolbeault bijection makes it defined on the entire H. The
circle preserves G and I; its distinct complex characters therefore
give orthogonal H_+ and H_-. Hermitian orthonormality of e_1,e_2
includes G(Ie_i,e_j)=0. Since J is an isometry and IJ=-JI, the same
orthonormality holds for Je_1,Je_2 in H_-. Thus both norms in (3)
are exactly r in this chosen convention. In (2), J is applied only
to the fixed vector v before multiplying by t. In particular
sB(Je_2)+tB(Je_1) must not be replaced by an expression involving
conjugates of s,t. Both axes give one nonzero vector in each sector;
no direction has been omitted.

Second, choose the closed ball strictly inside the analytic domain.
Convergence makes the real second derivative continuous on that compact
ball, so its operator norm has a finite bound. The segment from zero
to each point remains inside the ball; Taylor's integral formula
therefore proves the same Cr^2 estimate for all directions. The bound
r-Cr^2 is at least r/2 for r<1/(2C). The upper estimate used in (5)
is also valid: sqrt(2)r+Cr^2<(sqrt(2)+1/2)r<2r. In particular alpha
cannot be zero anywhere in the punctured ball. These constants belong
to the one chosen analytic family, including all its higher coefficients.
Neither first-jet injectivity alone nor a collection of linewise
estimates would establish this conclusion.

Third, the relevant holomorphic automorphism group is exactly the
one asserted. L094's no-section argument for L^2 and L^{-2} excludes
both off-diagonal entries in every endomorphism. Its diagonal entries
are constants because S is connected and compact. An automorphism
therefore has two nonzero diagonal constants; these are also parallel
for A, as required by the source's reference group. Quotienting by
common scalars gives the surjective ratio character a/b, with weights
+1,-1. The determinant-one group's ineffective order-two centre is
not mistaken for a nontrivial stabilizer in this effective group.
For the actual p,q in (4), Cp plus Cq is a two-dimensional complex
linear subspace. The equation uv=1 proves algebraic closedness of
the entire orbit there and hence in all of H, not only in the local
slice domain. It avoids zero and has trivial effective isotropy.
Thus it meets the source's affine stability convention. No choice
of a special higher-order term or of a minimal-norm representative
is required for this orbit test.

Fourth, check the corrected operator rather than only its formal
or quadratic approximation. In the notation of L101, set

\[
 a^{0,1}=alpha+d^*beta(alpha),\qquad
 T=d d^*beta(alpha)+a^{0,1}\wedge a^{0,1}.
\]

On the complex surface, d is zero in degree two; hence ker d* there
is exactly the harmonic space H^2. L101's equation (6) gives
(1-H_2)T=0, while H_2(dd^*beta)=0 by orthogonality. Its complete
equation (7) gives H_2 T=0. Consequently T=0. The trace-free solution
of (6) is a solution in the full endomorphism slice with beta orthogonal
to ker d*. Uniqueness in Proposition 2.6 identifies it with the
correction required by Theorem 8.1. This remains true after the
convergent substitution alpha(s,t). The unitary connection to which
that theorem applies is A+a^{0,1}-(a^{0,1})^*, whose (0,1) part
is precisely the family operator. Its integrability has just been
checked, independently of any stability assertion.

Finally, finite dimensionality gives the norm-conversion constant K.
The slice map alpha to a^{0,1} is continuous in the required Sobolev
norm and vanishes at zero; more explicitly its linear term is alpha
and its correction is O(||alpha||^2) by Proposition 2.6. Thus epsilon
can be decreased once so that its entire harmonic ball lies in all
of the slice and Theorem 5.4 connection neighborhoods as well as the
Theorem 8.1 ball. This checks a potential difference between harmonic
smallness and smallness of the corrected connection. Reference A has
scalar contracted curvature zero at the fixed metric. Theorem 8.1
then supplies a complex-gauge-equivalent connection with that property;
integrability is preserved by this gauge action. The resulting
holomorphic bundle is h-polystable. Only at this point is the
strict-stability equivalence of Theorem 5.4 applied. Formula (5)
puts every punctured parameter in these same neighborhoods.

This completes the audit without changing the argument or its direct
inputs L094 and L101. The central equal-slope splitting remains.
Fibrewise existence of Hermite--Einstein gauges is not smooth dependence
through the centre, and strict stability does not make the parameter
map quaternionic or identify different parameter points. No global
kernel, mixed action, separation, reconstruction or transport follows.

## Mathlib

Full matching coverage of the local analytic fixed-metric stability
theorems and this punctured C^2 family: **not checked**. Unknown coverage
is not evidence of absence. The general analytic theorems are imported
with precise citations; the two-projection estimate and full orbit
specialization are proved above. No numerical or Lean verification is
claimed.
