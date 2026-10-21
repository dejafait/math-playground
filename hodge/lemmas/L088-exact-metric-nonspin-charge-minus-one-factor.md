# L088 — Exact-metric ordinary charge-minus-one factor

## Hypotheses

Let S and the real ample class h be the marked projective K3 surface
and unchanged metric class of L052. In its integral Picard lattice,
NS(S) intersect h-perp = Zk, where k=(-4,-2,1,2) is primitive and
k^2=-14. Write eta for the integral point class. Stability means
strict slope stability, including for real ample classes.

## Conclusion

There exists an algebraic locally free rank-two bundle B on S with

det(B) isomorphic to O_S(k), c_2(B)=-eta,

strictly slope-stable at the exact h. This supplies only the individual
ordinary second factor proposed in L087's t=1 witness. Tensor stability,
acyclicity, actual image identification, common F and transverse
transport remain unresolved. This is a REPRODUCTION specialization
of known existence and chamber results. The separate critical audit
below preserves this individual-factor conclusion.

## Proof

**Standard inputs and reason for specialization.** Import Yoshioka,
*Irreducibility of moduli spaces of vector bundles on K3 surfaces*,
[math/9907001v2, 7 February 2000](https://arxiv.org/pdf/math/9907001v2),
Theorem 0.1(1), Section 0.2 (generality convention), Proposition 0.5
and Section 3.3(2), pp. 2–4,16. These give primitive nonemptiness at a
general integral polarization and the complete non-locally-free
exception list. They do not directly identify the real h. Import
O'Grady, *Modular sheaves on hyperkähler varieties*, Algebraic Geometry
9 (2022), [Definitions 1.1,3.1–3.3 and Propositions 3.4,3.8,3.10,
pp. 2,8–10](https://content.algebraicgeometry.nl/2022-1/2022-1-001.pdf),
for locally finite numerical surface walls. Import Greb–Toma,
*Compact moduli spaces for slope-semistable sheaves*, Algebraic
Geometry 4 (2017), [Theorem 6.6 and Section 6.3.3, pp. 74–75](https://content.algebraicgeometry.nl/2017-1/2017-1-003.pdf#page=35),
for uniform slope stability on rational real chamber strata at fixed
full Chern data, including lower-dimensional strata. The following
checks are the required changed-charge specialization, not reproofs
of these general theorems.

**Numerical vector and genuine walls.** Surface Chern identities give
ch_2(B)=k^2/2-c_2=-6 eta, so the required Mukai vector is
v=(2,k,-4). It is primitive, v^2=-14+16=2, and its discriminant
Delta=4(-1)-(-14)=10. Its rank/first-class divisibility ell(v) is one.

For any slope-semistable torsion-free sheaf of this vector at alpha,
a rank-one equality-slope subsheaf may be saturated without changing
its slope: a positive divisorial increase would violate semistability.
The saturation and torsion-free quotient have the forms L tensor I_Z
and L' tensor I_W. Put l=c_1(L) and z=length(Z), w=length(W).
Their Chern identity is -1=z+w+l(k-l). Consequently xi=2l-k obeys
xi.alpha=0 and xi^2=4(z+w)-10. Primitivity of k makes xi nonzero.
Hodge index therefore gives -10<=xi^2<0. Every genuine equality
wall is thus among the numerical 10-walls. None contains h: a nonzero
integral perpendicular class is nk and has square -14n^2<-10.
Local finiteness and closedness of these walls provide an open ball
U about h, contained in the ample cone and disjoint from all 10-walls.
At any integral polarization ray in U, slope semistability for v
implies strict stability. Equality of reduced Hilbert polynomials
would imply equality of slopes; normalized first-class equality is
impossible in rank two because k/2 is not integral. These rays are
therefore general for v and satisfy Yoshioka's condition (♮).

**Choose the correct integral ray.** Take a compact convex neighborhood
of h inside U and apply Greb–Toma to (rank,c_1,c_2)=(2,k,-eta),
which are the full topological data on this surface. Intersect the
kernels of its finite rational wall equations that vanish at h.
This rational linear subspace contains h and has dense rational
points. Choose a rational alpha there sufficiently close to h that
all other wall equations retain their strict signs. The segment
from h to alpha lies in the same relative stratum and in U. A positive
integral multiple of alpha is the first class of an ample line bundle
H. Multiplication by a positive scalar multiplies every slope
inequality by that scalar. Apply the compact-set comparison only
to alpha and h, both inside the chosen neighborhood; H itself need
not lie in that compact set. Thus H has the same stability condition
as alpha and is general for Yoshioka. Artificial walls through h
are retained, rather than treating h as an open-chamber point.

**A locally free stable point.** Theorem 0.1 gives nonempty M_H(v).
Use the explicit exception list in Section 3.3(2): rank one;
v=(rank v_0)v_0-eta; or rank v_0=1 and
v=ell v_0-(ell+1)eta, with v_0 spherical. Rank one is excluded.
The second case has rank (rank v_0)^2, which cannot equal two.
In the third case rank two forces ell=2, so its first class is
2c_1(v_0), contradicting primitive k. These exclusions retain all
line-bundle twists: a rank-two twist changes c_1 by twice an integral
class and cannot change its nondivisibility by two. Hence M_H(v)
has a locally free point B. Every Gieseker-stable point is slope
semistable, and the wall calculation above makes this same B strictly
H-slope-stable. There is no need to intersect separately asserted
nonempty loci or to invoke an unproved defect estimate. Greb–Toma
then preserves this B's strict stability at the identical h.

Finally c_1(det B)=k integrally. On a K3, H^1(O_S)=0, so the
exponential sequence makes c_1:Pic(S)→H^2(S,Z) injective.
Thus det B is the specified O_S(k). Negative c_2 causes no
Bogomolov conflict since Delta=10>0. L080's spherical hull argument
would allow a length-one defect at this changed square; it is not
used. No assertion concerning a tensor or common kernel follows.

**Separate critical audit, 2026-10-11.** The numerical calculation,
saturated rank-one equality test, primitive freeness exceptions and
same-real-stratum passage survive the independent check. In the
saturation step any nonzero effective divisorial increase has positive
alpha-degree since alpha is ample; a zero-dimensional increase does
not change the slope. Both rank-one terms are therefore torsion-free,
and their point lengths are nonnegative, as required by the displayed
wall bound. No vanishing of all possible point defects is inferred.

For the real passage, let W be the intersection of the kernels of
all Greb–Toma wall equations vanishing at h. Their rationality makes
W a rational vector space. Rational points of W are dense in W, and
all remaining finitely many strict inequalities persist near h.
Their intersection with the compact convex neighborhood is convex,
so the chosen alpha and h lie in one connected relative stratum.
Section 6.3.3 explicitly includes these smaller strata; the
higher-dimensional Proposition 6.7 is not used. Theorem 6.6 retains
strict stability as well as semistability. Freeness and stability
concern the same point of M_H(v): every such Gieseker-stable point
is slope-semistable, and the independent wall test removes every
rank-one equality at H. No intersection-of-loci assumption is needed.

The freeness comparison uses Proposition 0.5 with Section 3.3(2)
and Proposition 3.4's line-twist normalization, rather than reading
its abbreviated final exception literally. Neither normalization
nor an arbitrary line twist changes rank or first-class parity.
No substantive mathematical correction or stronger conclusion was
found. This audit is EXPLORATION / REPRODUCTION, not a new existence
result beyond the cited theorems. Tensor realization and the common
kernel remain outside the claim.

## Mathlib

Full matching existence and real-chamber specialization: not checked.
Supporting Mathlib coverage is not checked; unknown availability is
not absence. The precise mathematical inputs above are imported
from primary sources. No formal verification or novelty is claimed.
