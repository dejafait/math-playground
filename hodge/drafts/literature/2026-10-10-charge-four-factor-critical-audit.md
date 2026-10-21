# Charge-four factor — critical-audit source coverage

TARGET: Critically audit L083's nonprimitive charge-four existence, absence of point defects and strict stability at the exact real h.
CHECKED: 2026-10-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact-metric charge-four existence and L053 audit assessments; compared the full written L083 proof with primary arbitrary-vector equality, rank-one exception and bounded-chamber passages. No broad discovery search repeated.
SOURCE_EVIDENCE: Yoshioka math/9907001v2 (7 February 2000), Corollary 0.3 and Section 0.2 p. 2, Section 1.1 p. 4, Lemma 1.5 and entire proof p. 5; alg-geom/9705027v2 (18 June 1997), Lemma 4.4 and entire proof pp. 10–11, Remark 4.1 p. 11; O'Grady Algebraic Geometry 9 (2022), Definition 1.1 p. 2, Definitions 3.1–3.3 and Proposition 3.4 p. 8, Propositions 3.8 and 3.10 and chamber proof pp. 9–10. L052's stable Euler and exact integral perpendicular-lattice passages inspected.
COMPARISON: Primary Lemma 1.5 explicitly covers arbitrary positive rank and the non-strict square threshold, while chamber constancy concerns ample divisor classes of a modular sheaf; together with reused surface tools these cover an independently testable audit, not a theorem directly asserting L083's entire exact-real-h conclusion.
GAP: Mathematical critical review must still verify generality for the divisible vector, hull stability and every defect, K3 modular/chamber applicability, individual subsheaf limits and strict equality exclusion at h.
REASON: Source-scope comparison for the completed proof is now adequate; approve only the saved critical audit, without certifying the specialization or constructing a common kernel.
SCOPE: L083 at precisely L052's marked projective K3 S and real h, rank two, integral determinant zero and charge four; audit only, with no new existence mechanism or tensor realization.
LITERATURE_REASON: The newly completed L083 proof requires a separate audit-scope comparison; its point-defect argument differs from L053's dimension method and its nonprimitive equality application must retain the actual primary hypotheses.

## Primary coverage and qualifications

Reuse the [existence assessment](2026-10-10-exact-metric-charge-four-factor-existence.md)
and [L053 audit assessment](2026-10-05-minimal-factor-existence-audit.md)
within their scopes. Read L083 in full and L052's stable Euler and
integral perpendicular-lattice passages. This literature-only step
approves a later mathematical audit; it derives no new result and
leaves the lemma and argument overview unchanged.

[Yoshioka, *Irreducibility of moduli spaces of vector bundles on K3
surfaces*, math/9907001v2](https://arxiv.org/pdf/math/9907001v2#page=5):
Section 1.1 fixes a general H satisfying Section 0.2's condition (♮).
Lemma 1.5 explicitly says arbitrary positive-rank Mukai vector; its
hypothesis is v²/2 >= ell(v)² and its conclusion includes slope-stable
nonemptiness whenever the slope-semistable stack is nonempty. No
primitivity is imposed there. Corollary 0.3 concerns semistability at
general H, not local freeness. The full Lemma 1.5 proof includes the
stack dimension lower bound, filtration estimate and referral of the
all-rank-one case to the earlier work. Primitive Theorem 0.1 and
Proposition 0.5 cannot replace this input. L083's displayed equality
boundary is within the stated non-strict threshold; checking its
numerical and general-polarization specialization remains audit work.

[Yoshioka, *An application of exceptional bundles to the moduli of
stable sheaves on a K3 surface*, alg-geom/9705027v2](https://arxiv.org/pdf/alg-geom/9705027v2#page=11):
read the complete Lemma 4.4 proof, including its r=1, ell=2 exception
and trivial-double-dual family bound 3c_2-3. Remark 4.1 distinguishes
the non-strict slope-existence boundary from a strict primitive
moduli assertion. This supplies proof-case context only: the older
Picard-rank-one calculation is not an independent theorem applied to
this Picard lattice. Import the later arbitrary-vector Lemma 1.5;
no reproof of its dimension estimates is needed or approved.

[O'Grady, *Modular sheaves on hyperkähler varieties*, Algebraic Geometry
9 (2022), 1–38](https://content.algebraicgeometry.nl/2022-1/2022-1-001.pdf#page=8):
Definition 1.1 states the modularity hypothesis; Definitions 3.1–3.3
supply locally finite rational a-walls and the rank/discriminant wall
parameter. Proposition 3.4(ii) gives constancy for ample divisor classes
in the same open a(F)-chamber. Its proof uses Proposition 3.8's bounded
subsheaves and Proposition 3.10's discriminant/Hodge-index bound. The
source does not by this statement identify stability at an irrational
boundary class. The audit must explicitly check the K3 modularity and
parameter specialization and the integral multiples of rational rays;
then separately test the written limit and equality-exclusion argument.

L052 contains the determinant-zero stable Euler test, including its
charge-four boundary, and the integral lattice NS(S) intersect h-perp
= Zk with k²=-14. Reuse the surface RR, dual stability, Serre duality
and Picard-injection inputs precisely cited in L083 and the existence
assessment. L083 uses a stable double dual and Euler characteristic,
not a Quot-dimension proof. Thus the previously recorded Mukai-source
access issue for a different dimension audit is not essential here;
no new source access claim or theorem numbering is inferred.

## Approved audit and decision test

Audit the actual v=(2,0,-2), ell=2 boundary and chosen adjacent integral
ray. Test condition (♮) and generality from saturated rank-one sequences,
retaining equal Hilbert polynomials that persist for the divisible
vector. Check every stable hull and possible finite point defect before
claiming local freeness. Check modular/chamber hypotheses, the artificial
wall through h, limits for each fixed subsheaf, integral determinant,
strict endpoint stability and only then acyclicity and determinant wedge.
Retain E_4 as an audited input only if all passages pass. Otherwise isolate
the unsupported implication and preserve the completed proof for repair;
a failed application is not nonexistence.

Essential input IDs are L083 and its sole direct input L052. L053 is a
method comparison; L079 names the downstream repeated-block requirement,
and separately audited L082 supplies the other individual J_5. Neither
is an existence premise of L083. No cross-notebook input is needed.
The main gap is universal primitive rational Hodge algebraicity; this
prerequisite could support L079's image-block construction. Common F,
prescribed mixed action, actual image identification and transverse
transport remain unresolved. No complete candidate is claimed.

The earlier charge-five/six result and necessary/topological tests do
not duplicate this charge-four conclusion. Preserve L079's necessary-test
stop, ATTEMPTS/043,/045,/053, its t=2 alternatives and the flat (-10,-17)
blocker. The source comparison supplies no new exclusion or cycle.
Uninspected O'Grady moduli leads remain leads, not additional evidence.

## Mathlib

Full matching nonprimitive charge-four existence and exact-real-chamber
result: **not checked**. No matching declaration or absence is asserted.
