# Moving-interval eigenvector trace convergence — completed source comparison

TARGET: Prove convergence of both normalized endpoint traces for L516 eigenvectors on intervals (0,ell_j) with ell_j->ell_*>0, bounded eigenvalues tending to zero, and L2 convergence after unitary dilation to an assumed normalized nullvector on (0,ell_*).
CHECKED: 2026-10-30
DECISION: IMPORT
SEARCH_EVIDENCE: Searched exact-title/trace-continuity, logarithmic-Laplacian moving-domain eigenfunction, geometric-stable boundary/domain-perturbation and renewal/Weil queries. Paper 67 Section 7 explicitly covers the target. Narrow searches of Weil assessments, histories, stops and L512–L518 found fixed-interval inputs and a prior reading of (7.1)–(7.6), but no canonical moving-interval convergence result. Search failure is not a novelty claim.
SOURCE_EVIDENCE: Read bramble_trace, Boundary traces and support variation for localized Weil operators, paper 67 v1 (27 October 2026), (2.2), (2.8), (3.1)–(3.19), and Section 7 (7.1)–(7.6), especially the unnumbered continuity claim between (7.5) and the paragraph after (7.6); Section 9 (9.1)–(9.5) supplies its limitation. Reused the inspected GR renewal and bounded-data assessments and canonical L513–L516 rather than reopening unchanged primary inputs.
COMPARISON: Section 7 already asserts both trace limits under the proposed dilated L2 eigenvector convergence for the same common finite signed-measure model. Its bounded-spectrum scope includes the zero-eigenvalue limit and is not restricted to simple branches. This is a known manuscript result to import with its source qualification, not uncovered mathematics or a new continuity mechanism.
GAP: No missing source coverage for this exact convergence claim. The local canonical import and its coordinate/hypothesis check remain to be written in a research turn. The imported manuscript proof is not independently audited; nullvector existence, assumed eigenvector convergence, vanishing traces and the O(lambda) estimate remain separate.
REASON: The source comparison removes the REVIEW_REQUIRED coverage gap while preserving the original target. Import the precise Section 7 claim with only the necessary applicability check. No new lemma, proof, calculation or independent manuscript audit is performed in this literature turn.
LITERATURE_REASON: The supplied target changed from a fixed-interval raw-adjoint audit to moving-support trace continuity. Its essential theorem comparison was REVIEW_REQUIRED; the exact primary passage has now been located and read.
SCOPE: Common finite real even signed measure mu_A and c=log(2pi) from L516; 0<ell_j,ell_*<2A for fixed A and ell_j->ell_*>0; real normalized eigenvectors u_j with bounded real lambda_j->0; assumed real normalized u_* in Dom(A_(0,ell_*)) with A_(0,ell_*)u_*=0; D_j u_j->u_* in L2, where (D_j u_j)(x)=sqrt(ell_j/ell_*)u_j((ell_j/ell_*)x). Only convergence of the two L513-normalized traces is covered.

## Precise import and primary proof cases read

The citation is bramble_trace, [*Boundary traces and support variation
for localized Weil operators*, paper 67 v1, 27 October 2026](https://rstation.ai/problems/riemann_hypothesis/papers/67),
**Section 7, the unnumbered trace-continuity assertion following (7.5),
its two integral arguments through (7.6), and the paragraph immediately
after (7.6)**. It occurs inside the proof of Theorem 2.2; there is no
separate numbered trace-continuity theorem. Cite that passage rather
than attributing continuity to the fixed-domain boundary upper theorem.

The passage assumes convergent, bounded-spectrum eigenfunctions after
unitary dilation. Its common-measure class is (2.8). It uses (7.1)'s
bounded data and (3.19)'s signed formula: the first integral is split
near zero; the second uses (7.6)'s square-integrable logarithmic weight
on the entire exterior tail. The forcing-convergence assertion is
supported by (7.4)'s strong-continuity discussion, including activation
translations. The following simple-branch paragraph is a further
application, not a simplicity premise of the continuity assertion.

These are inspected source claims, not new local derivations. The
manuscript remains an external, independently unaudited input. The
existing assessments supply the older primary regularity/renewal inputs;
no new theorem about those papers is needed for this import.

## Exact applicability checklist for the later import

- Use L516's retained realization with one common mu_A and scalar c.
  The source class (2.8) matches it. Keep nu_rho, the signed pole,
  every prime power and equality cutoffs; never vary the cutoff measure
  separately with j. L512's full-Weil/source qualification stays explicit.
- Identify the source's centered radius a_j with ell_j/2 and translate
  to (0,ell_j). Use the displayed D_j, with its square-root normalization,
  and verify the correspondence of physical endpoint traces. No extra
  trace-topology convergence, sign choice or parity is an input.
- Check the eventual compact positive range of lengths required in
  Section 7. Bounded eigenvalues and the common finite measure are
  the source's uniform-data hypotheses; L515 supplies each fixed-vector
  application, L514 its domain split and L513 the exact signed trace
  normalization. Do not replace the eigen-equation by generic L2 data.
- The hypothesized limit is already an eigenvector at zero. No simplicity,
  uniform spectral gap, H1 regularity, nonzero trace or positive eigenvalue
  is assumed by this import. Existence or selection of such a limit is
  outside the target. Preserve the full exterior renewal integral.

These are applicability obligations, not a proof completed here. IMPORT
permits KNOWN_IMPORTED classification, with a precise citation and these
necessary checks. An independent reproof/audit of the manuscript is not
required to import its stated conclusion and is not silently certified.
A changed model or a discovered mismatch must reopen source comparison
rather than borrow this approval for a stronger claim.

## Duplicate and obstruction comparison

The local fixed-interval statements are L513–L515. L516's weak flux
identity alone gives no moving-interval limit. The averaged-prime
assessment previously lists Section 7 among inspected passages, but
approves a different arithmetic test; it is a reusable source lead,
not a duplicate canonical proof or approval of the present target.

The automatic-support stop concerns uniform propagation near a first
zero, and L518's raw-adjoint stop concerns coefficient cancellation.
Neither refutes continuity. Conversely continuity supplies no signed
arithmetic estimate and does not revive either stopped implementation.
The source's Section 9 explicitly leaves the eigenvalue-relative flux
estimate open; no local progress beyond the source is claimed.

Queries used: `"logarithmic Laplacian" "domain" "boundary trace"
convergence eigenfunctions`; `"geometric stable" "boundary" "domain
perturbation"`; `"renewal" "trace" "moving" "Weil"`;
`"logarithmic Laplacian" "trace" "convergence" eigenfunctions`;
`"Boundary traces and support variation" "continuity"`;
`"geometric stable" "boundary traces" convergence`.
Unrelated thin-domain and spectral-sum hits were not used as theorem
evidence. The source's fractional shape and small-order spectral
references remain unread leads, not asserted coverage for this target.
The exact source claim suffices; no broader source sweep is needed.

## Relevance and continuation test

The main gap is actual-Xi all-degree positivity. This intermediate
continuity input could transport a separately established relative-flux
bound to an assumed limiting nullvector. It would prove neither that
bound nor trace vanishing. The O(lambda) rate, branch/nullvector
existence, full-Weil identification, collars and Xi transfer remain open.
Full matching Mathlib coverage is unchecked; no absence claim or
cross-notebook input is made.

Continue with a citation-based canonical import only if the common
measure, unitary coordinates, trace normalization and full-tail scope
match exactly. Any failed applicability item must be recorded explicitly;
stop or sharpen the target rather than assume trace convergence. No
new convergence theorem is needed to meet this target. This newly
completed assessment receives separate next-turn approval; the current
literature result does not invoke its own research gate.
