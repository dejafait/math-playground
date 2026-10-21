# Exact-metric charge-four factor — boundary source comparison

TARGET: Determine whether L079's determinant-trivial rank-two charge-four block E_4 exists as an h-stable locally free bundle.
CHECKED: 2026-10-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the charge-five/six existence and audit assessments; searched the charge-four/nonprimitive boundary and O'Grady moduli terminology; inspected the primary equality hypothesis and rank-one proof case rather than relying on search snippets.
SOURCE_EVIDENCE: Yoshioka math/9907001v2, Introduction, Corollary 0.3, Sections 0.2 and 1.1, Lemma 1.5 and proof, pp. 1–5; alg-geom/9705027v2, Lemma 4.4 proof and Remark 4.1, pp. 10–11; O'Grady Algebraic Geometry 9 (2022), Definition 1.1, Definitions 3.1–3.3, Propositions 3.4, 3.8, 3.10 and proofs, pp. 2, 7–10; reused L052's stable Euler test and the saved freeness/chamber assessment.
COMPARISON: The inspected arbitrary-vector slope theorem includes its equality boundary and does not require primitivity; the earlier primitive-only freeness theorem is still inapplicable. Sources cover a bounded specialization, not a single theorem asserting locally free charge-four existence at this irrational h.
GAP: Verify the charge-four numerical/general-polarization hypotheses, use the stable-hull Euler test to settle possible point defects, and transfer strict stability to the exact real endpoint with L052's perpendicular lattice.
REASON: Essential boundary source coverage is now ready for this independent factor prerequisite; importing the covered theorem and justifying its local specialization is sufficient, without reproving the theorem or assuming a common kernel.
SCOPE: The identical marked projective K3 S and exact real h of L052/L079; rank two, determinant O_S, charge four and local freeness. No common product kernel, transform identification, transport or new Hodge algebraicity.

This completes one literature-only comparison. It approves the unchanged
target for a later mathematical specialization; it establishes no new
existence lemma. No lemmas or mathematical scripts were written.

## Primary statements and essential proof case

[Yoshioka, *Irreducibility of moduli spaces of vector bundles on K3
surfaces*, math/9907001v2, 7 February 2000](https://arxiv.org/pdf/math/9907001v2#page=5):
ell(v)=gcd(rank(v),c_1(v)). Corollary 0.3 covers positive-rank
semistable nonemptiness for multiples of vectors of square at least -2.
Section 0.2's condition (♮) requires equal slopes in a semistable sheaf
to imply equal normalized first classes; Section 1.1 retains this
generality. Lemma 1.5 is for arbitrary positive-rank vectors and assumes
v²/2 >= ell(v)², including equality. Its properly slope-semistable
codimension bound is v²/(2ell(v))-ell(v)+1, and it explicitly concludes
slope-stable nonemptiness from slope-semistable nonemptiness. Its proof
refers the all-rank-one filtration case to the earlier work. Theorem
0.1 and Proposition 0.5 retain primitive hypotheses and cannot replace
this arbitrary-vector input or establish nonprimitive freeness.

[Yoshioka, *An application of exceptional bundles to the moduli of stable
sheaves on a K3 surface*, alg-geom/9705027v2, 18 June 1997](https://arxiv.org/pdf/alg-geom/9705027v2#page=11):
read Lemma 4.4's complete filtration estimate through the r=1, ell=2
exception. The special filtration has trivial rank-two double dual;
its family bound is 3c_2-3. Remark 4.1 retains a non-strict slope-locus
threshold and distinguishes it from the strict inequality in the
primitive deformation theorem. This supports the equality case;
the later arbitrary-vector Lemma 1.5 is the existence input. Neither
the earlier primitive theorem nor its Picard-rank-one construction is
being applied directly to this rank-four Picard lattice. The earlier
preprint's numbering is not the extended journal article's numbering.

[O'Grady, *Modular sheaves on hyperkähler varieties*, Algebraic Geometry
9 (2022), 1–38](https://content.algebraicgeometry.nl/2022-1/2022-1-001.pdf#page=8):
Definition 1.1 and (1.2.1) fix the discriminant convention; Definitions
3.1–3.3 give locally finite rational a-walls in the real ample cone.
Proposition 3.4 preserves stability between ample divisor classes in
one open a-chamber. Proposition 3.8's bounded-subsheaf argument and
Proposition 3.10's discriminant/Hodge-index bound justify that statement.
Read their proofs. These numbered divisor-class assertions alone do
not identify stability at the irrational endpoint. Reuse L053's
separate continuity/equality-slope method only after checking the changed
Chern value; do not assert that h lies in an open chamber.

The saved [charge-five/six comparison](2026-10-05-minimal-survivor-stable-factor-existence.md)
and [audit coverage](2026-10-05-minimal-factor-existence-audit.md) remain
valid in their scopes. L053's hull-stability and stable Euler passages
are reusable tools, not a charge-four existence conclusion. Its general
point-defect dimension calculation need not be repeated if the Euler
lower bound already excludes all nonzero defects in this boundary case.

## Approved specialization and discriminating test

Essential inputs are L052's identical S,h, integral Picard lattice and
NS(S) intersect h-perp=Zk with k²=-14, and L079's exact E_4 block
requirement. L053 is a method comparison: its charges five and six
are not hypotheses supplying E_4. L082 supplies only the opposite J_5.

In the next research step, verify the charge-four Mukai vector,
divisibilities and square, checking the non-strict Lemma 1.5 threshold
explicitly. Choose an integral ample ray in a suitable adjacent bounded
chamber; prove the required generality (♮) using saturated rank-one
sequences rather than an assertion about avoiding countably many walls.
Retain persistent equal Hilbert polynomials for a divisible vector.
Apply Corollary 0.3 and Lemma 1.5 only after these checks.

Then justify stability of the double dual and apply the determinant-zero
stable Euler lower bound from L052 to every possible finite-length
defect. This is the required locally free test; torsion-free existence
is not the endpoint. Finally carry the chosen bundle along rational
rays in the chamber, take the slope inequality limit for each fixed
subsheaf, and exclude equality using the exact perpendicular line
lattice and the central Chern identity. Check determinant triviality
integrally. These local applicability checks are needed because no
inspected theorem states this entire exact-h conclusion; no general
nonemptiness, Quot or chamber theorem is to be reproved.

Continue with E_4 as an individual input only if slope nonemptiness,
absence of defects and strict exact-h stability all pass. If a theorem
hypothesis or endpoint passage fails, preserve that failure and park
this automatic-existence application; failure of an application does
not prove bundle nonexistence. No independent lemma was derived here.

The main gap is universal primitive rational Hodge algebraicity. The
intermediate target could supply E_4 for L079's image alternative
O_S plus E_4 tensor C^2. L082 supplies the separate opposite J_5 block;
it implies nothing about E_4 or whether the two arise from one F.

## Search, overlap and retained stops

Focused queries: `K3 rank two c1 0 c2 4 slope stable locally free
Yoshioka nonprimitive (2,0,-2)`; `"K3" "c2 = 4" "locally free"
O Grady`; `"Yoshioka" "2, 0, −2" slope stable`.
Primary passages above were readable through the web tool.
The O'Grady ten-dimensional-moduli and non-locally-free-locus hits
are uninspected leads, not theorem evidence or a substitute for slope
stability on this S. No novelty is inferred from the searches.
No download, access retry, authentication or purchase was needed.

L052 and L079 give necessary tests only, L050 is topological, and
L053's existing conclusion excludes charge four from its scope.
Thus none duplicates the requested actual E_4 conclusion. No
cross-notebook input is needed.

Preserve L079's necessary-test stop, ATTEMPTS/043,/045,/053, the t=2
branch and the parked flat (-10,-17) blocker. Common F with the
prescribed mixed tensor and transverse transport remain independent
unresolved assumptions. This is source readiness and local progress
toward a prerequisite, with no claim of mathematics beyond the checked
sources, new cycle algebraicity or a complete Hodge candidate.

## Mathlib

Full stable locally free charge-four existence and exact real-chamber
coverage: **not checked**. No matching declaration or absence is claimed.
