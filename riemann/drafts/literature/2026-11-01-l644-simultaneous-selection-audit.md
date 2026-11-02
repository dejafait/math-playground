# L644 simultaneous selection — approved audit coverage

TARGET: Critically audit L644's positive-measure simultaneous dimension and full-trace estimate, including the count fraction, U_X-inside-E_N domination, all endpoints and the uniform O(N^(-1/160)) normalization.
CHECKED: 2026-11-01
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse drafts/literature/2026-11-01-vertical-pick-simultaneous-height-selection.md and its exact joint-target comparison, scoped duplicate/failure searches and primary theorem reads; no new search or novelty claim. The proposed audit has unchanged hypotheses and operations.
SOURCE_EVIDENCE: Previously inspected MIT Lecture 17 Section 1 p.1 https://ocw.mit.edu/courses/6-436j-fundamentals-of-probability-fall-2018/f44fa78f05ac31a4ba2bd82f599dcf60_MIT6_436JF18_lec17.pdf ; Lototsky RKHS note p.1 theorem/(1.2)/Corollaries (3)--(4) https://dornsife.usc.edu/sergey-lototsky/wp-content/uploads/sites/211/2023/06/RepKernHilbSp.pdf ; Bellotti--Wong 2412.15470v2 Thm 1.1 https://arxiv.org/pdf/2412.15470v2 ; Baluyot 2017 Thm 1.2.1 p.16 https://urresearch.rochester.edu/fileDownloadForInstitutionalItem.action?itemFileId=183460&itemId=33320 ; Penrose 1955 Thm 1 pp.406--407 and lemma p.408 https://www.cambridge.org/core/services/aop-cambridge-core/content/view/5F4516D6B9989BB6563A4B267CC7D615/S0305004100030401a.pdf/div-class-title-a-generalized-inverse-for-matrices-div.pdf . Other unchanged finite-model and zero-expansion coverage is recorded in the reused assessment.
COMPARISON: L644 specializes the same Markov, rank, finite projection and complete-tail operations approved for the joint target. The primary sources do not state its combined actual-Xi conclusion; the new proof needs a separate critical audit. No new source scope, density exponent, constraint type or spectral assertion is proposed.
GAP: Check the new same-height assembly and its local input verification, especially the fixed positive count fraction versus the vanishing bad-annulus fraction, and the entire mixed sum after projection. The proof has not received its later independent critical audit.
REASON: Separate literature approval completed 2026-11-01: the saved primary reads cover the exact audit scope without changed hypotheses. Proceed to one bounded mathematical audit; this approval does not certify L644. Further browsing requires an essential changed premise.
SCOPE: Exactly L644 with L018, L467, relevant finite-space/count/zero-pair portions of L641, the full projection/tail proof of L642 and audited L643; N=floor(log T), fixed E_N, all actual-Xi value constraints, all orders and both displacement signs. No new pole grid, derivative constraints, source-manuscript audit, RH, positivity or sign mechanism.

The [invocation-start joint assessment](2026-11-01-vertical-pick-simultaneous-height-selection.md)
is unchanged and retains the exact queries, inspected theorem/proof
ranges, source versions and source limitations. Its finite-dimensional
and measure tools cover the new application. This nomination does not
claim that a later audit has passed. Newly written coverage receives
the supervisor's separate approval before that audit invocation.

The canonical new proof is
[L644](../../lemmas/L644-vertical-pick-simultaneous-height-selection.md).
Its asserted constants are q_0=(arctan(1/3)+pi/4)/pi,
kappa=q_0-1/pi, b_0=(q_0+1/pi)/2,
c_*=kappa/4 and delta_*=kappa/(4b_0). Verify that the averaged
closed-window count <=N/pi+C leaves measure >=delta_*T at
M_T<=b_0 N, and that the spectral error sqrt(N)V_N leaves
r_X>=c_*N there. The count and majorant are finite sums of
measurable functions; no measurable choice of basis or regular
projection rank is needed by the claimed selection.

Verify the Markov exponent from mean O(N^(159/80)) to threshold
N^(2-1/160), and the intersection measure >=delta_*T/2 for all
sufficiently large T. This is an existential-onset claim. Verify
|k_U(z,conjugate(z))|<=F_N(Re z,Im z) inside the fixed E_N;
do not silently replace E_N by H_N or insert a dimension factor.
Retain the complete distant O(N^(3/2)) tail and ell_X>=N/2.
Equality at the inner annulus endpoint belongs to the local constraints,
and equality at sqrt(N) belongs to the distant tail. Repeated rows
are value constraints; source zeros are counted with all orders.

The local input checks in L644 belong to this audit's scope. They
do not certify L641's unrelated exterior countervectors or reprove
the density/count manuscripts. Preserve the two recorded
boundary-transfer and deterministic-annulus failures; the selected
height mean mechanism does not contradict them. Small signed trace
does not imply a small absolute eigenvalue or any spectral sign.

Continue only if the stated uniform simultaneous conclusion survives
the check; repair an actual error with its quantitative effect or
record a precise failing premise. Full matching Mathlib coverage
remains unchecked, not absent. This is an ordinary application audit
(proof_audit/routine_audit, standard/high); if it exposes a delicate
analytic premise beyond the saved input proof, record and reroute
that premise rather than reducing its required rigor. No new central
sign mechanism is nominated just to meet a creative scheduling aim.


## Separate coverage approval — 1 November 2026

The invocation-start nomination has now received its separate literature
comparison. DECISION remains SPECIALIZE and TARGET is unchanged. This
is approval of source scope only; the correctness audit has not occurred.

Read the completed joint assessment's primary-source statements and
proof-range records, and the operative parts of its count/concentration,
constrained-trace, weighted-density and L643-audit assessments. Compared
these with L644's hypotheses and conclusion, without checking or deriving
its new proof inequalities. All operations proposed for the audit are
covered: normalized Lebesgue Markov selection; finite closed-subspace
projection and complex evaluation; dependent value rows via Penrose;
all-zero cumulative counts with closed-endpoint specialization; and
the unchanged fixed-space weighted density input. No new density
exponent, pole array, derivative constraint or spectral assertion occurs.
The primary citations and essential proof cases recorded in those ready
assessments are reused, not newly browsed or independently reverified.

The RKHS note is used only for finite closed spaces, not its unqualified
incomplete-subspace wording or garbled extracted norm line. Penrose
covers singular matrices, not uniform conditioning. Bellotti--Wong v2
counts all positive ordinates with orders; it does not give selected
heights. Baluyot's fixed theta=11/20 and uniform sigma>=1/2 statement
has existential onset and a strict horizontal threshold; its arithmetic
proof remains imported. These qualifications already match the nominated
local inputs. L641's finite-space/count specialization and the full
L642 tail proof still require the saved mathematical audit, as does
L644's assembly. The audited L643 mean is reused within its exact scope.

Read both named ATTEMPTS records. Boundary-only paired transfer is
obstructed by unconstrained test vectors, not actual constrained Xi
zeros; the deterministic annulus envelope fails to prove an upper bound,
not a trace lower bound. Neither is a duplicate of the selected-height
mean mechanism. L644 is the existing simultaneous-selection proof, so
the next action is its audit rather than a second derivation. A small
signed trace remains insufficient for absolute eigenvalue control or
spectral signs. The main initial-sign/all-degree positivity gap is open.

The continuation test and input list above remain binding. Retain the
simultaneous conclusion only after checking all quantitative premises
uniformly, or record a precise failing premise and its effect. Full
matching Mathlib coverage remains unchecked. No theorem was imported
into a lemma, no mathematical result was established, and no lemma,
mathematical script, DAG or PROOF was changed in this approval step.

LITERATURE_REASON: The supervisor requires a separate approval of the newly nominated L644 audit assessment; this step compares that exact scope with ready primary coverage rather than repeating external discovery.

Outcome: STALLED / LITERATURE / NOVELTY_UNCHECKED as mathematical evidence.
This necessary gate approval repeats no claimed mathematical advance
and spends or resets no mathematical exploration budget. The exact
saved audit is ready; no further literature step is nominated. A new
central signed mechanism is not justified by this source comparison,
so the concrete pending audit takes precedence over creative routing.
