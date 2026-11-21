# Exact sparse PSD representation: source comparison629

TARGET: Assess source coverage for an exact sparse positive-semidefinite decomposition of C999w(12) that preserves its full-output .000999 implication.
CHECKED: 2026-11-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step629 searched Kakimura's direct chordal decomposition proof, Agler--Helton--McCullough--Rodman's sparse PSD theorem and rational exact sparse certificates; inspected the primary report below. Narrow common-residual/joint-structured/tail-Galerkin/shared-middle records had no earlier assessment of this decomposition. Read598/600/603 stops and reused599/601/625 coverage; no novelty inference.
SOURCE_EVIDENCE: N. Kakimura, METR2009-13 (April2009), Theorem1 and complete proof, printed pp2-3 (PDF pp4-5), and Corollary2/definitions printed p3, https://www.math.keio.ac.jp/~kakimura/papers/METR09-13.pdf ; published successor DOI10.1016/j.laa.2010.04.012, LAA433(2010),819-823, identified on the author's publication list, but journal text not inspected. C999w Sections4-5/7 and599/625 provide existing exact-witness and conditional-implication coverage.
COMPARISON: The theorem gives exact clique-supported PSD sums for a fully specified real symmetric PSD matrix with chordal zero pattern, including singular cases. Its separate completion corollary does not certify the fixed coefficient matrix. No small C999w graph, feasible rational multipliers or .000999 floor follows.
GAP: A later mathematical step must determine the support of the entire C999w(12), including every multiplier entry, and test exact reconstruction with controlled clique sizes and fill; no local graph, cancellation, factor or size reduction is established here.
REASON: Essential theorem coverage for a single symbolic structural test is available. This completes a source comparison, not a sparse implementation or existence proof. A newly nominated continuation receives separate approval next turn.
LITERATURE_REASON: The changed sparse method was outside626's scope; decomposition, its singular proof case and its distinction from completion were unread at invocation start.
SCOPE: Literature only; unchanged C999w joint2044 full free2:1023 independent complex endpoints, exact Galerkin Y, R/head512/K65536/penalty256/fraction1/2, every finite/infinite output and original .000999 Euclidean metric. No lemma, local reduction, mathematical script, optimization, numerical run or tuning.

## Exact primary input and qualifications

Kakimura's **Theorem1**, in the inspected April2009 technical report,
assumes a finite undirected chordal graph containing all diagonal edges,
its maximal cliques C_k, and real symmetric A zero outside that graph.
It equates A>=0 with A=sum_k Y_k, where Y_k>=0 is supported on
C_k times C_k; the stated representation also preserves the sum of ranks.
Read the full induction: a zero pivot forces a zero row; a positive pivot
uses invertible elimination and a PSD Schur remainder. **Corollary2**
instead concerns existence of a PSD completion from PSD principal clique
blocks. Neither statement asserts small cliques or rational feasibility.

Cite this precise report, not a guessed theorem number in the unread
published successor. Its early attribution differs from the final
publication's Agler et al. attribution. The report's opening chordal
definition says "at least three", a wording error; use the standard
meaning, cycles of length greater than three have a chord. No local
argument relies on the erroneous phrase.

## Application obligations, not results of this turn

The later object is the **constant coefficient matrix** C_cert of
C999w(12), after coefficients and multipliers are fixed, not P(theta)
pointwise or a partial matrix. The imported representation format is

    C_cert = sum_k E_k^t B_k E_k,    B_k >= 0,

where E_k selects the clique coordinates. No such identity has been
established for C999w here. Its future applicability check must address:

- Scalar indices (noise-symbol index, endpoint coordinate), including
  all m=2044 endpoint coordinates. Zero coefficients need exact identities;
  intervals containing zero or centers equal to zero are not structural zeros.
- C, every N_i tensor Lambda_i and every L_a tensor Gamma_a, retaining
  each Lambda_i>=0 obligation. Sparse multiplier restrictions are extra
  sufficient ansatz restrictions unless losslessness is justified.
- A chordal support supergraph containing all diagonals, with explicit
  ordering/cliques. Added edges never release fixed coefficients: exact
  reconstruction must hold there too, at zero when prescribed. Overlap
  contributions must sum to the fixed entry; a factor is not presumed to
  equal a principal submatrix of C_cert. Nonchordal support alone is not
  an obstruction if a controlled chordal extension is available.
- Exact rational coefficient/reconstruction identities and exact rational
  LDL^t witnesses with nonnegative diagonals for every B_k and Lambda_i,
  using C999w's existing witness option. Do not assume a real feasible SDP
  has a rational feasible point. Singular factors require zero-pivot-compatible
  exact identities; ordinary Cholesky success or approximate agreement is
  insufficient.

A floating replacement would require the already assessed complete Rump
error ledger and separate local admission. The nomination uses exact
symbolic structure only. No reproof of the source theorem is needed.
Application to the full lift, sparsity, fill, rational witness feasibility
and size remain untested. No AA losslessness or certificate feasibility
is inferred.

## Search, reuse and decision

Queries: "Kakimura simple proof matrix decomposition theorem semidefinite
programming chordal 2010 pdf"; "Agler Helton McCullough Rodman positive
semidefinite matrices chordal decomposition theorem singular pdf";
"Kakimura Theorem1 decomposition pdf 2010 819 823"; "sparse positive
semidefinite rational chordal certificate exact". The author-hosted report
supplied the complete essential statement and proof cases. The journal
request returned403; no result is taken from its abstract. The report
itself is the cited primary proof, so this is not an essential source blocker.
The author publication list was read to identify the published successor.

A Vandenberghe--Andersen survey was opened for orientation; later theorem
searches timed out and no extra theorem is imported. A Zheng--Fantuzzi
polynomial-matrix paper appeared as an unread lead; no polynomial-matrix
or rationality claim is imported. This target concerns a constant matrix.
Reused599's Rump scope,601's witness limitations and625's AA/S-lemma reads;
C999w's audited implication is unchanged. No matching local finite
certificate was located, and no novelty follows from the bounded search.

The598 scalar losses,600 box-radius stop and603 implementation-allowance
stop reject particular sufficient tests, not actual F or all representations.
Preserve603 and all saved arrays. A historical stop does not ban this
independently testable structural question.

The downstream use is a potentially smaller verifiable sufficient finite
joining-block certificate. Continue only to the separately approved symbolic
support/reconstruction test. Require explicit reconstruction obligations
and a proved largest PSD order at most half the uncompressed (p+1)m;
otherwise park without numerical optimization, generic searches or tuning.
Even structural success supplies no feasible factors or .000999 floor.

The main gap is L030-L032/C032a actual-Xi positivity. Essential inputs:
C744v/w/z, C999k, C999q Sections1-2/5/8 and C999w Sections1-7, with599/601/625
source scope.600's inclusion/pins and analytic/IEEE754/Decimal/core/c_*
contracts remain conditional. Higher endpoints, actual remote-plus-induced
coupling, C744q, H2, non-neutral coverage and global assembly remain open.
Full matching Mathlib coverage is unchecked; no cross-notebook input.
This is local known-method source progress only, not progress beyond the
inspected theorem or a mathematical exploration budget reset.
