# Mixed first/second-power actual cups — coverage review

TARGET: Test whether the actual mixed-power determinant cups for Q_(-1,-1) and Q_(-1,-2), paired with their harmonic opposites, force m_1*m_2=0 under L161's hypotheses with W and delta retained.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 532 compared L157-L161 and the step-521/523/525/527/529 read registers against ATTEMPTS/069,/089,/090; mixed-line/cup-product/quaternionic-Hodge-Riemann searches found general machinery but no inspected theorem giving the exact mixed multiplicity exclusion; queries and unread leads are distinguished below.
SOURCE_EVIDENCE: Fresh primary reads: Verbitsky alg-geom/9307008v1 (29 July 1993), Section 4 setup, Propositions 4.2-4.3, Theorem 4.1, Corollary 4.3, doubled-dual proof of 4.2.A and Theorem 4.3 proof, PDF pp. 13-18; Demailly alg-geom/9410022v3 (28 February 1995), Section 4.A (4.3)-(4.4'), pp. 27-28; Stacks 36.23.1 (0FLN), 20.31.3 (0FP3) and 15.59 (0GWN), statements and relevant displayed proofs; direct links and qualifications below, accessed 2026-10-25.
COMPARISON: General coefficient harmonicity, Serre integration, line-valued Kunneth and graded cup comparison cover a bounded calculation; L160/L161 give only separate opposite-power exclusions. None of the inspected statements supplies the mixed determinant-product sign or excludes simultaneous m_1,m_2>0.
GAP: Determine the actual degree-two cup/opposite-cup comparison, including harmonic-representative corrections and all exterior signs, and test its sign in the full polarized identity; the comparison may permit cancellation rather than yield an exclusion.
REASON: Essential general source coverage is sufficient for one separate specialization attempt, including an informative failed-sign verdict; no mixed sign, multiplicativity of harmonic representatives or new exclusion is derived in this literature-only review.
LITERATURE_REASON: The changed coefficient pair introduces a degree-two product pairing outside the ready equal-magnitude trace assessments; this review checks that essential scope once and reuses unchanged edge/transform coverage.
SCOPE: Exactly TARGET with L161's conditional data, actual preferred connections, ordinary W and unevaluated delta; one mixed-cup sign and quartic-identity test, without other powers, optimization, new F existence, lower z comparison or transport.

The following invocation-start proposal was REVIEW_REQUIRED; its source
coverage is superseded by the completed comparison below. It is not a
derived result. Preserve the exact target while assessing it. Reuse the existing
harmonic, derived-edge and line-valued product sources where their
hypotheses apply; inspect the primary hypotheses and relevant proof
cases for the new degree-two comparison. Check stronger results,
duplicates and known failures before approving a calculation. No new
Mathlib coverage is asserted.

The main gap remains universal primitive rational Hodge realization.
The intermediate target would restrict coexistence of two remaining
line types in the hypothetical kernel's ordinary middle image M.
Its possible downstream use is a restriction beyond the separately
excluded opposite-sign pairs. It supplies neither an independent lower
comparison on z nor a plan to construct F or to treat all stable types.

Write Q_(e,d)=F tensor p_1^*L^e tensor p_2^*L_B^d as in L161.
Essential inputs to check are L071's actual connection, L147's ordinary
M,W, L157's full first- and second-power multiplicities and opposite
transforms, L158's actual determinant products and polarized identity,
L159's actual harmonic operator, L160's W-retaining edges, and audited
L161's bounded second-power restriction. Retain L093,L153,L156 through
L157. The new target is not preapproved by their individual scopes.

Retain identical marked K3 factors/common g,h and ordered triple;
the hypothetical locally free Omega-polystable rank-two F with integral
c_1=0 and ch=2-14e_1-21e_2-tau_D+62P; preferred dual HE lines with
k=(-4,-2,1,2), k.h=0, k^2=-14 eta and integral eta=1; 0<=z<=119;
W the ordinary residue-field sum on finite Z, and unevaluated delta.
Kernel existence, other stable types, lower control on z, transport
and global realization remain unresolved. No cross-notebook input
is proposed.

Discriminating test: determine whether inspected source machinery
controls the needed actual mixed cup pairing with the sign required
by the polarized identity. Approve only a bounded specialization if
essential coverage is adequate; import a matching theorem if found.
If a sign is uncontrolled or compatible with the identity, record that
specific failure and park the proposed exclusion. Do not transfer the
degree-one strict sign to degree two without justification or replace
the mixed cup by a free matrix. ATTEMPTS/069,/089,/090 remain valid
limits; their finite relaxations are not to be rerun.

The invocation-start proposal spent no mathematical exploration turn and
contained no derivation for the new target. Its literature-only gate is
handled by the comparison below, not by a mathematical attempt.

## Completed source comparison — step 532

LITERATURE / EXPLORATION / REPRODUCTION; actual task literature_comparison.
This is new coverage for the exact TARGET, not a mathematical advance or
a claim of progress beyond the sources checked. No lemma or mathematical
script is written. PROOF.md and DAG.md are unchanged because the argument
and its mathematical inputs have not changed. Mathematical exploration
usage stays at one since step 530.

**Local comparison and failures.** Read L157's all-power statement,
L158's product/trace and target checks, L159's actual operator and raw
restriction calculation, and L161's coefficient/trace/target proof and
recorded separate audit. Reused the ready
[second-power assessment](2026-10-25-second-power-opposite-line-trace.md)
and the harmonic, operator-audit and positive-z read registers it names.
The all-power scope and W-retaining edge method can be reused; the
mixed-pair conclusion cannot be imported from the equal-power cases.
No local matching proof was found in these specific records. This is
not a claim that no other proof exists.

ATTEMPTS/069 forbids replacing an unevaluated actual cup by an assigned
matrix. ATTEMPTS/089 stops the selected additive spectrum filter;
ATTEMPTS/090 stops its finite cup relaxation, even with every recorded
quartic identity. Those stops survive. The present target adds an actual
harmonic comparison; it authorizes no rerun of either finite relaxation.

**Primary harmonic source.** Verbitsky, *Hyperholomorphic bundles over a
hyperkähler manifold*, [alg-geom/9307008v1](https://arxiv.org/pdf/alg-geom/9307008v1),
29 July 1993: Section 4, setup (PDF p. 13), Propositions 4.2-4.3 and
Theorem 4.1 (pp. 14-15), Corollary 4.3 (p. 16), doubled-dual proof
of Theorem 4.2.A (p. 17), and Theorem 4.3 with proof (p. 18), using
one-based PDF pages. Read the commutator, anticommutation, Laplacian,
harmonic-preservation, exchange-real-structure and Green-operator cases.
These support harmonic comparison for hyperholomorphic coefficients,
using a parallel real structure after doubling with the dual. They do
not state a sign for this determinant cup. Use only those operator
facts, not the printed scalar-ring or endpoint-injection assertions,
nor an unchecked group-action formula in every degree. The broader
Hodge-Riemann sentence in Theorem 4.2 is not a substitute for matching
the actual coefficient pairing and degree. No general reproof is needed.

For applicability, L071 and L157 already supply the actual compatible
connections and preferred tensor/dual lines; L159 matches their Hermitian
exchange and determinant identification. The base here is the compact
hyperkähler product with its diagonal triple. No irreducible-base cone
theorem or independent rotation of one factor is an input. The extraction
on the changed degree-two line target, and its compatibility with the
two determinant cups, are still mathematical obligations.

**Metric, cup and product sources.** Demailly, *L2 vanishing theorems for
positive line bundles and adjunction theory*,
[alg-geom/9410022v3](https://arxiv.org/pdf/alg-geom/9410022v3), 28 February 1995,
Section 4.A, (4.3)-(4.4'), printed pp. 27-28 (PDF pp. 27-28), was
freshly read with the preceding elliptic decomposition and generalized
star construction. It provides harmonic realization and the dual-coefficient
Serre integral on compact Hermitian manifolds. The actual locally free
coefficients on X and the factors meet this scope; flatness of their full
Chern connection is not required. It does not identify this harmonic
opposite with the generalized star or assert that a wedge of harmonic
forms is harmonic. Reuse its Section 1.A Dolbeault product coverage
through the existing assessment; do not reprove Hodge or Serre theory.

[Stacks Lemma 36.23.1, 0FLN](https://stacks.math.columbia.edu/tag/0FLN)
covers quasi-coherent derived inputs for quasi-compact quasi-separated
factor maps, Tor-independent over the base, with affine base for the
global formula. Projective K3 factors over Spec(C) and their line bundles
satisfy these assumptions. Read both proofs, including the affine K-flat
case and the two open-cover inductions; the first proof's compatibility
verification is explicitly omitted. This controls cup-defined product
cohomology, not a metric sign.

Freshly read [20.31.3, 0FP3](https://stacks.math.columbia.edu/tag/0FP3),
its adjunction/naive-cup diagram proof, and
[15.59, 0GWN](https://stacks.math.columbia.edu/tag/0GWN), its signed
interchange and differential calculation. They support computing the
actual products in resolutions and retaining the graded tensor order.
The surrounding setup of 0FP3 and its use with coefficient resolutions
are reused from the ready four-twist assessment. They do not prove the
new coefficient duality sign. Keep the existing qualifications for
20.31.8 (0H99), whose omitted proof is not claimed as read.

**Unchanged derived coverage.** Reuse the positive-z and second-power
assessments for Stacks 01E6, 01F2, 0A1H, 0BDK, 0AAB, 0B6J and 0BRT:
projection formula, Leray, perfect proper pushforward/base change and
smooth-proper duality of relative dimension two. The same projective
projections and locally free tensors retain their hypotheses. BBHR,
*A hyperkähler Fourier transform*, DGA 8 (1998), 239-249, Definition 2
and Section 3.3 Lemmas 1-2/Theorem 3, pp. 244-246, is used only through
L157's established opposite concentration/preservation, with its prior
IT and metric qualifications. No new forward IT or ordinary base change
at Z is asserted. L160/L161 retain W and delta; their ready edges are
inputs to test applicability, not permission to remove the top sheaf.

**Discovery register.** Queries were `hyperholomorphic bundle cup product
quaternionic Hodge Riemann bilinear relations degree two Verbitsky`,
`hyperholomorphic line bundle mixed tensor powers cup product positivity K3`,
`"hyperholomorphic" "cup product" positivity`, `Verbitsky Hodge Riemann
bilinear relations hyperholomorphic bundle coefficients degree 2`,
`"hyperholomorphic" "cup product" "line"`,
`"hyperholomorphic" "Hodge-Riemann" "pairing"`, and
`"K3" "mixed" "line bundles" "cup product" positivity`.
The inspected primary machinery is listed above. Search leads concerning
quaternionic line-bundle vanishing, moduli symplectic forms, motives and
ample-bundle Hodge-Riemann inequalities were not read as matching theorem
statements and are not inputs. No absence or novelty inference follows.

**Approved bounded test and stopping criterion.** After separate approval
of this changed assessment, attempt exactly TARGET. Use L157's full
multiplicities and L160/L161's retained edges to check the chosen classes.
Keep L159's single determinant and common ordered triple. Identify all
line targets and surviving pair partitions of L158's polarized identity
for these four actual inputs. Compare the mixed cup's cohomology class
with the cup of the two harmonic opposites. Justify any passage between
raw closed products and target harmonic representatives; neither generic
harmonic-wedge closure nor cochain commutation with bar-partial is an
assumption. Compute the normalized degree-two pairing with explicit
coefficient evaluation, exterior order and factor orientations before
using its sign. These are finite specialization checks, not missing
general theorems being silently assumed.

Continue only if the complete identity and justified signs give the exact
exclusion, or if an identifiable failed comparison/cancellation explains
why this test cannot give it. In the latter case preserve the evidence
and park this exclusion mechanism rather than assign the unknown mixed
cup or infer positivity from degree one. No such sign or failure has
been derived in this review. F existence, other stable types, lower
control on z, transport and the universal primitive gap remain open.
Full matching Mathlib coverage is not checked, not absent. No
cross-notebook theorem is used. This new ready continuation awaits the
supervisor's separate approval before mathematical invocation.
