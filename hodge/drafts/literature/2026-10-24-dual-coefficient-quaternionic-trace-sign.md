# Dual-coefficient quaternionic trace sign — source comparison

TARGET: Test whether a natural quaternionic map between opposite coefficient cohomologies forces a common trace-sign constraint excluding L158's two z=0 extremal branches.
CHECKED: 2026-10-24
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 521 checked L158's actual edges/witness/audit, L157's rotation-IT/cross-power duality, L090's counit/trace method and ATTEMPTS/069,/089,/090; targeted hyperholomorphic/dual-coefficient/quaternionic-Hodge searches located Verbitsky's doubled-dual proof and coefficient Kodaira identities, but no inspected theorem states this two-projection sign constraint.
SOURCE_EVIDENCE: Read Verbitsky alg-geom/9307008v1 (29 July 1993), Section 3 Proposition 3.2 pp. 11–12, Section 4 setup/Propositions 4.1–4.3/Theorem 4.1/Corollary 4.3 pp. 12–16 and Theorem 4.2.A proof p. 17, https://arxiv.org/pdf/alg-geom/9307008v1; Verbitsky math/0604303v2 Sections 3.2–3.4 pp. 14–16, https://arxiv.org/pdf/math/0604303v2; BBHR (1998) Definition 2/Section 3.3 pp. 244–246 and Demailly alg-geom/9410022v3 Section 4.A (4.3)–(4.4') pp. 27–28; reuse step-516/518 precise counit/trace coverage below.
COMPARISON: Known results cover harmonic operators after doubling a hyperholomorphic coefficient with its dual, general coefficient Kodaira identities, natural Hermitian transforms and the coefficient Serre integral. They do not state the opposite-twist operator's determinant convention, its two actual restriction comparisons or a common strict sign; L158's formal witness remains valid for its assessed relaxation.
GAP: Extract and check the proposed opposite-coefficient operator in ordinary (0,1) convention, including its square and determinant identification; then compute both actual restricted trace values with one fixed normalization and test the four-distinct-input identity. This review establishes none of those specialized conclusions.
REASON: Primary hypotheses and essential operator proof cases now support one bounded specialization attempt, including a possible failed compatibility verdict; no source-access blocker remains and no new mathematical result is derived or approved as established in this literature turn.
LITERATURE_REASON: The proposed anti-linear actual-connection constraint is outside the ready complex-linear cup assessment; essential harmonic/dual-coefficient source scope had not been inspected for this target.
SCOPE: Exactly the fixed L158 data, z=0, four preferred signed line twists and branches (12,2),(6,8); one actual harmonic-map/restriction/trace-sign test. No assumption that either twist has a parallel real structure, no independent factorwise Lefschetz action, positive-z extension, higher product, F-existence theorem or transport.

The supplied entry state was REVIEW_REQUIRED. Step 521 completes its
separate literature-only comparison and makes the exact target ready for
one subsequent mathematical attempt, subject to supervisor approval of
this changed assessment. This is LITERATURE / EXPLORATION /
NOVELTY_UNCHECKED: actionable source coverage, with no theorem-level sign
verdict, new exclusion or claimed mathematical originality. It does not
alter L158, its audit, PROOF.md or DAG.md. No lemma or script was changed.

The intermediate target is a naturally defined anti-linear comparison
J_s:V_s -> V_{-s}, or a precise obstruction to such a comparison, for
s=-- and -+. It must come from the actual kernel connection and the
preferred dual HE lines, not from choosing a Hermitian structure on
abstract vector spaces. If such maps exist, the requested discriminant
is whether the two trace components on (v,J_s v) have fixed common
phases and strict signs across both pairs. This is a question to assess,
not a claim that the maps, their harmonicity or these signs hold.
L158's four-distinct-input identity is the intended downstream test.

## Inspected primary inputs and limits

**Harmonic operator.** Verbitsky, *Hyperholomorphic bundles over a
hyperkähler manifold*, [alg-geom/9307008v1](https://arxiv.org/pdf/alg-geom/9307008v1),
29 July 1993; numbering here is the 43-page preprint, not an assertion
about the published J. Algebraic Geom. **5** (1996), 633–669 version.
Section 3, Proposition 3.2 (PDF pp. 11–12) distinguishes a parallel
anti-linear involution from an alternating self-duality. Section 4's
setup, Propositions 4.1–4.3, Theorem 4.1 and Corollary 4.3 (pp. 12–16)
give the real-coefficient harmonic action, using rotated Kodaira
commutators and equality of Laplacians. Theorem 4.2.A's proof (p. 17)
uses the explicit Hermitian exchange real structure on E direct sum
E-dual to treat general hyperholomorphic E. These proof cases were read.

The proposed specialization starts with the actual coefficient
Q_s=F tensor T_s and its dual, rather than calling Q_s real. On the
compact product the inherited compatible unitary kernel and preferred
HE line connections are the candidate theorem inputs. The next attempt
must match their dual connections and the same determinant trivialization
before extracting a map to the opposite sign coefficient. The alternating
wedge and the real doubled-coefficient structure must be kept distinct;
even the square of the extracted operator is a check, not a quoted
quaternionicity conclusion for V_s. The diagonal product triple is used.
No theorem about independently rotating one factor is imported. Retain
the earlier assessment's qualifications on the printed 4.2.A endpoint
injection and scalar polynomial-ring display; neither is needed here.

**Coefficient curvature control.** Verbitsky, *Quaternionic Dolbeault
complex and vanishing theorems on hyperkähler manifolds*,
[math/0604303v2](https://arxiv.org/pdf/math/0604303v2), 16 September 2006,
Sections 3.2–3.4, Proposition 3.3 and Theorems 3.5–3.6 (PDF pp. 14–16).
For a holomorphic Hermitian coefficient on a hyperkähler manifold these
give coefficient differentials, Kodaira commutators and the Laplacian
difference [Theta_+,Lambda_Omega]. Read the curvature-component proof
and graded-Jacobi proof of Theorem 3.6; 3.5 refers to the 1993 Proposition
4.2, whose proof was inspected above. This supplies a way to check an
operator argument without silently discarding coefficient curvature.
The irreducibility assumptions in the later scalar cone/vanishing
sections are not imported to this product. This theorem is not a
restriction-harmonicity theorem or a two-trace positivity assertion.

**Metric and trace.** Bartocci–Bruzzo–Hernández Ruipérez, *A hyperkähler
Fourier transform*, Differential Geom. Appl. **8** (1998), 239–249,
[published scan](https://mat.usal.es/ruiperez/Site/Papers_files/Hyperkahler-Fourier-Mukai.pdf),
Definition 2 and Section 3.3, Lemmas 1–2 and Theorem 3 (pp. 244–246),
with the natural base-change/Dirac-metric proof cases read. Compact
source, compatible hyperkähler spheres, Hermitian quaternionic kernel
and IT source coefficient are its hypotheses. L157/L158 already check
the applicable concentration cases. The theorem identifies natural
Hermitian transforms, allowing reducibility; it does not identify a
global harmonic representative restricted to a fibre with that fibre's
harmonic representative. Its positive real twistor form in Section 2.3
is not a real structure on each individual signed coefficient over X.

Demailly, *L2 vanishing theorems for positive line bundles and adjunction
theory*, [alg-geom/9410022v3](https://arxiv.org/pdf/alg-geom/9410022v3),
28 February 1995, Section 4.A (4.3)–(4.4'), printed pp. 27–28, was read
for the compact Hermitian coefficient harmonic realization and the
generalized-star integral defining Serre duality. In complex dimension
four this star alone does not give a degree-one to degree-one map.
On a K3 fibre its canonical-form identification must still be compared
with the proposed operator and the actual determinant wedge. Reuse the
step-516/518 inspected coefficient Dolbeault resolution from Section 1.A
and the actual cup/counit/trace comparison, rather than reprove them.

Specifically the
[four-twist assessment](2026-10-24-four-twist-determinant-cup-comparison.md)
and [audit assessment](2026-10-24-four-twist-cup-critical-audit.md)
record Stacks 20.31.3 (0FP3), 20.31.7 (0FP6), 20.31.8 (0H99),
48.12.4 (0AAB), 48.7.1 (0B6J) and 48.15.7 (0BRT), with direct links,
proof-read qualifications and smooth-proper/Tor-independent scope.
L158's audit already proves that both cohomological edges restrict the
same global coefficient class and compute its actual trace components.
This complex-linear naturality is reused unchanged. It gives no
anti-linear commutation theorem. Smooth pullback of the proposed form
operator, its coefficient identification, and any harmonic-projection
or exact-representative correction are the specific specialization to
check next, not missing general source assertions to assume.

## Exact bounded mathematical test

Keep one determinant wedge and the original metric two-forms on both
factors. First extract the doubled-dual operator and test its source,
target, anti-linearity and harmonicity in the usual Dolbeault convention.
If it gives the required opposite-coefficient comparison, use those same
global representatives in each L158 edge. Compute both fibre Serre
integrals on (v,J_s v) for s=-- and -+, retaining line evaluation,
coefficient duality, exterior order and complex orientation. Determine
whether the resulting phases agree across both pairs and whether the
relevant values are strictly controlled for nonzero v. A positive total
L2 norm, a sum of the two components or abstract perfection alone does
not answer this question. Do not assume restriction preserves harmonic
representatives: check pullback at form level, or retain and justify the
correction before using a fibre harmonic norm. No such calculation is
performed in this review.

Only then compare with L158's four-distinct-input relation. Continue the
mechanism if the actual comparisons exclude its opposite-ratio witness;
park it if a required compatibility fails or the established signs still
permit that witness. A failed square convention may require renaming
the operator rather than discarding a usable anti-linear comparison.
No reproof of general Hodge, Serre, Fourier or Lefschetz theorems is
warranted. Any subsequent result should be classified REPRODUCTION as a
known-tool specialization, without claiming novelty from these searches.

## Discovery, duplicates and verification limits

Queries included `Verbitsky hyperholomorphic bundles cohomology quaternionic
Serre duality antilinear J`, `hyperholomorphic bundles cohomology dual bundle
harmonic forms quaternionic Hodge star`, `"hyperholomorphic" "dual" "real
structure" cohomology`, `"quaternionic" "cohomology" "restriction"
"Hermitian" bundles Serre`, and `"hyperholomorphic" "Hodge-Riemann" bundles`.
The inspected results above cover the machinery; none was read as a
theorem of the proposed two-projection sign constraint. No inference of
novelty follows. Broader quaternionic torsion and Real-bundle search hits
were not inspected as matching theorems and are not inputs.

Local comparisons included the earlier coefficient-Lefschetz assessment
`2026-10-17-equality-coefficient-lefschetz-constraints.md` and preferred
central-metric assessment `2026-10-23-preferred-twisted-central-critical-audit.md`.
Their End_0 real-structure results do not directly cover these signed
rank-two coefficients. Preserve ATTEMPTS/069's uncontrolled actual entry
and /089,/090's compatible formal models. This proposed use of the actual
connection is distinct from assigning another pair of perfect matrices.
Full matching Mathlib coverage is **not checked**; no absence is asserted.

Continue only if primary hypotheses and proof cases cover the required
dual coefficient maps and permit a bounded test of their actual trace
comparison. Abandon this specific sign mechanism if a necessary map
or compatibility fails, or if the established sign relation still
permits the L158 witness. Persistent essential source blockage requires
parking dependent work and choosing an independently testable target.

Essential inputs: L158 and its step-520 audit, L157's H_r and cross-power
duality, L147's actual M,W, and L090's actual coefficient/counit/trace
method; retain L071/L093/L153/L156 through those hypotheses. The factors
are identically marked with common g,h; F is hypothetical locally free
Omega-polystable rank two, integral c_1=0, with full character
2-14e_1-21e_2-tau_D+62P. Retain k=(-4,-2,1,2), k.h=0,
k^2=-14 eta and integral eta=1. Both branches assume z=0.
Actual cup values, F, nonempty Z in the wider problem, independent lower
control, transport and universal primitive Hodge realization remain
unproved. No cross-notebook input is proposed.
