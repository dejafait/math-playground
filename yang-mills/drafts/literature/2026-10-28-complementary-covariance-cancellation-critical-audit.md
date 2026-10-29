# Complementary-covariance cancellation — completed audit coverage

TARGET: Critically audit L297's complete complementary-covariance infrared cancellation, including source-energy bounds, weighted spectral residues and every mixed heat-line term.
CHECKED: 2026-10-28
DECISION: EXPLORE
SEARCH_EVIDENCE: Read all of L297, searched its exact mechanism in the prior infrared assessment, attempt record and histories 531--532, and compared ATTEMPTS/047--050; reused the bounded primary searches recorded in the infrared and bare-tail audit assessments. No duplicate completed L297 audit was found in these selected records; no new external search or novelty inference.
SOURCE_EVIDENCE: Reuse BBS arXiv:1907.05474v2 Propositions 2.1.6/2.1.9 and Corollary 2.1.11, Higham--Lin MIMS 2013.73 Definition 3.3, Schweitzer arXiv:2203.03930v1 Lemma 1/Theorem 2, Watrous 2018 draft (1.165)--(1.175), and Ponge Summer 2025 chapter 4 slide 56 as previously read; newly compare the local L282(18), L283(9)--(11),(17), L287(12)--(13), L289(11)--(13),(16) and L296 sections 3/6 with L297's claimed applications.
COMPARISON: The versioned finite Gaussian, analytic derivative and trace-ideal statements cover the unchanged standard tools. L296 supplies audited unweighted residues, full high-spectrum trace control and bounded-weight cubic estimates; L282/L283/L289 explicitly cover sampled smooth fields on all relative edge grids. L297's energy-weighted residues, source-energy estimates and signed mixed contraction are additional written specializations to audit, not imported uniform theorems.
GAP: Independently verify L297(9)--(14),(17)--(24),(26)--(28), including all source placements, counting/physical normalization and complete errors. No separate audit conclusion or stronger rate is established by this comparison.
REASON: Admit one later RESEARCH / REPRODUCTION conceptual audit of exactly TARGET; the written proof and standard-input coverage are available without an essential unread theorem. Acceptance remains conditional on the complete uniform specialization surviving that audit; any stronger target requires separate coverage.
LITERATURE_REASON: L297's newly written energy-weighted low-residue and signed mixed-heat contraction estimates are now load-bearing; compare their precise hypotheses with the ready sources before the separate conceptual audit, reusing unchanged primary readings.
SCOPE: Exact SU(2) relative cube, even N>=2, a=8/N, counting measure, all-face pins/fixed gauges and all normal endpoints, exact reflected bump, fixed transverse space, own-slice all-link jets/full density, both source orders and source-independent r_N. Essential local inputs L003 L279 L280 L282 L283 L287 L289 L296, with L297 as the object audited. No L291 or one-face substitute.
COVERED_TARGET: Critically audit L297's complete complementary-covariance infrared cancellation, including source-energy bounds, weighted spectral residues and every mixed heat-line term.

## Original registration and discriminating test (step 532, retained)

The completed result is
[L297](../../lemmas/L297-complementary-covariance-infrared-cancellation.md),
tau_N(r_N)=o(N^(1/2)(log N)^2), conditional on its stated inputs.
The new source comparison should reuse
`2026-10-28-complementary-covariance-infrared-test.md` and its precise
primary citations. No repeat general browsing is justified unless
an essential unread source or changed hypothesis is identified.
Registration is not a source obstruction and does not spend a new
mathematical exploration attempt.

The later audit must check the positive complementary split on the
open source domain; all factors in the exact polynomial difference;
both inverse and heat-source orders; the form bounds for zero/first/
mixed derivatives of the full one-line operator; the application of
the three canonical strong limits to counting-normalized ground
modes; and the external-curl error when replacing the full cubic
operator by its internal-curl part.

For the remainder, check all low-pole placements with energy weights
at both ends, the entire high-spectrum trace estimate, all four terms
of the differentiated one-line trace, and every derivative placement
in the mixed H,H,G term. Verify the factor three for colors, the
half-residue per source order, the exponents -17/20 and -1/20 for
the multiple-heat terms, and the normalization against the required
N^(1/2)(log N)^2 scale. A formal ground cancellation alone is
insufficient. Preserve ATTEMPTS/047--050 and do not infer a bounded
tail, uncut rate, higher remainder or continuum construction.

Continue if the complete proof survives those checks under the exact
input hypotheses. A failed weighted residue estimate, uncontrolled
mixed term or normalization error requires a concrete correction or
downgrade of L297, with the earlier work preserved. No audit result
or new mathematical target is derived here. Full matching/supporting
Mathlib coverage remains not checked.

## Completed source comparison (step 533, 2026-10-28)

The main gap is still construction of the interacting continuum theory
and positive infinite-volume mass. The intermediate target is independent
scrutiny of L297's necessary leading infrared test. Its plausible use is
deciding whether mixed contractions genuinely escape L296's specific
bare-tail obstruction before stronger quantitative estimates are attempted.
This literature step performs no proof audit or new derivation.

### Reused primary statements and exact limits

The completed assessment `2026-10-28-complementary-covariance-infrared-test.md`
records the inspected statements and proof cases of Bauerschmidt--Brydges--Slade,
*Introduction to a Renormalisation Group Method*, LNM 2242 (2019),
[arXiv:1907.05474v2](https://arxiv.org/pdf/1907.05474v2), printed pp. 31--33,
Propositions 2.1.6/2.1.9 and Corollary 2.1.11. Finite real symmetric
positive semidefinite covariances, including singular support, are allowed.
Thus the fixed transverse extension is within the source scope; the later
audit must still check the claimed positivity of both source-dependent
pieces and the actual polynomial multiplicities. Gaussian convolution
does not identify the scalar difference with a complete effective action.

The completed `2026-10-27-bare-heat-tail-obstruction-critical-audit.md`
records the primary statements and proof readings of Higham--Lin,
*Matrix Functions: A Short Course*,
[MIMS 2013.73](https://eprints.maths.manchester.ac.uk/2067/1/paper.pdf),
Definition 3.3, section 3.1.3, p. 6; and Schweitzer,
[arXiv:2203.03930v1](https://arxiv.org/pdf/2203.03930v1), section 2.1,
Lemma 1 and Theorem 2, pp. 2--3. Their finite-matrix analytic calculus
requires enclosing spectral contours inside the analytic domain and
retains both second-derivative orders. The inverse/heat function excludes
zero. Neither theorem supplies a mesh-uniform weighted residue bound.

The same assessment records Watrous, *The Theory of Quantum Information*,
[2018 draft](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf), section 1.1,
pp. 32--33, (1.165)--(1.175), for finite complex trace duality and ideal
bounds, and Ponge, *Introduction to Noncommutative Geometry*,
[Summer 2025 chapter 4](https://raphaelponge.org/wp-content/uploads/2025/07/summer-chap4-1.pdf),
slides 53--57, especially slide 56, for standard Schatten Holder with
1/p+1/q=1/r in the cases p,q,r>=1 used here. The latter is a statement
of the named inequality, not a proof reading. These dimension-independent
inequalities allow signed and nonnormal matrices; they do not give the
local spectral count or Wilson tensor estimates. Cite these tools;
no general theorem reproof or additional primary reading is needed.

### Local scope comparison and remaining audit obligations

The following comparison identifies what is available, not whether
L297's deductions are correct.

- L282(18), L283(17), and L289(12) are explicitly strong physical-norm
  limits on samples of smooth fields on the actual relative edge grids.
  Their surrounding proofs include all boundary layers and normal links,
  using fixed polynomial approximants before the mesh limit. They are
  broader than a source-sandwich-only limit. The audit must verify L297's
  ground-vector sampling, transverse membership, counting normalization
  and color convention; a full-lattice operator-norm limit is not given.
- L283(9)--(11) supplies the local quartic row bound and whole-box
  approximation. L287(12)--(13) supplies the complete external/internal
  curl energy and the Gaussian factor relating it to the cubic tensor.
  L296 section 6 explicitly checks bounded real weights, signed relative
  covariance contractions and fixed multiplicities. These cover the
  premises of L297's proposed Cauchy--Schwarz specialization; the full
  source partition in (13), its signed two-slot use and the J_N form
  bounds in (9)--(14) still require independent verification.
- L289(16) is the recorded convergent Brillouin integral identity, with
  its excised small-sphere flux justified in the canonical proof.
  It can be cited directly. L297's assembly of density, quartic and
  cubic constants, external-curl error and color factors remains the
  audit's responsibility; L291 is neither needed nor an allowed shortcut.
- L296 sections 3/6 provide the audited fixed complex polydisc, relative
  spectral count, low-pole cases and complete high-spectrum trace bound.
  L297 retains that family, but adds outside energy weights to every
  low coefficient and pairs them with a source-dependent operator.
  The audit must check all pole placements and analytic-coefficient
  derivatives, both source orders, the four product-rule trace terms,
  and that no extra logarithm reaches the leading scale.
- The all-tail multi-heat terms are recorded L296 inputs. The H,H,G
  term is a changed contraction. L297 writes a signed tensor/form-norm
  argument for every derivative placement; its trace-ideal pairing and
  absence of a volume loss must be checked directly. General Holder
  or positivity of the undifferentiated covariance does not prove it.

No essential source blocker remains for this finite written audit.
The unresolved parts above are its mathematical checks, not reasons to
import a stronger unstated theorem. The bare-tail stop and the distinct
failures in ATTEMPTS/047--050 remain applicable as contrasts: neither
integration by parts, absolute norms nor generic orbit identities alone
settles the Wilson-specific cancellation. Selected histories 531--532
record source approval and a new attempt, not a completed independent audit.
No sibling notebook or cross-notebook theorem was consulted.

Continue only if the complete response, under every retained hypothesis,
has the claimed zero normalized limit. A failed weighted residue,
source placement or mixed-line bound requires correction or downgrade,
with the previous evidence preserved. Even acceptance yields no bounded
tail, uncut rate, uniform higher remainder or continuum construction.
Full and supporting Mathlib coverage remains not checked, not absent.

Outcome: EXPLORATION / LITERATURE / NOVELTY_UNCHECKED. This is new
target-specific coverage for the audit, not mathematical validation or
progress beyond the checked sources. It spends zero mathematical
exploration attempts. The exact TARGET is ready for a separate
proof_audit/conceptual_audit, deep_research/xhigh, classified REPRODUCTION.
