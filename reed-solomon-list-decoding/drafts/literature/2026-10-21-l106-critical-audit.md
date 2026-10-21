# L106 restricted shared-scalar obstruction — audit coverage

TARGET: Critically audit L106's restricted shared-scalar obstruction, including support exhaustion, uniqueness and the complete original-coordinate verification.
CHECKED: 2026-10-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 395 reused the exact-target discovery and inspected-source comparison in the step-393 fixed-pair-cardinality-scalar-feasibility assessment; read L106 in full, L098's homogeneous conversion and audit qualifications, foundations/04,12,13, ATTEMPTS/081–082,088–089 and history/394; inspected the existing verifier's input recovery, elimination and output scope. No fresh web search or certificate verification was performed.
SOURCE_EVIDENCE: Reuse Schrijver III.B (62)–(67), author manuscript p.7; Kim–Toan arXiv:1212.3467v1 (31)–(35), pp.8–9; Raghavendra–Tan arXiv:1110.1064v1 Section 3 Definitions 3.1,3.3 p.7 and cardinality display/qualification pp.8–9; Polak arXiv:1703.05171v1 Proposition 1.1 and full indicator proof p.2, Section 1.2 p.3, as inspected and qualified in foundations/04,12,13. Step 393's finite rational elimination coverage is reused without a new solver theorem.
COMPARISON: The sources cover ordinary actual-orbit constraints and cardinality-marginal methods, not L106's finite restricted-support verdict. L098 audits a different fixed control, L105 tests uncoupled rows and ATTEMPTS/082 stops one numerical prescription. None is an independent critical audit of L106's 64-class support, uniqueness or complete scalar certificate.
GAP: Independently audit the local support exhaustion, all 69 contraction equations, rank/closed solution, strict sign and lossless original-coordinate evidence; these have an existing proof and verifier but no separate critical audit.
REASON: Essential source coverage is ready and unchanged. One finite proof audit can validate or correct a recorded obstruction without new support choices, new optimization, a general infeasibility claim or reproof of the cited hierarchy.
SCOPE: Only the exact TARGET is approved; fixed L098 pairs, prescribed L106 support, all actual orbits, all source scalar rows and contractions. No new solve, support enlargement, parameter scan, PSD test or unrestricted feasibility inference.
LITERATURE_REASON: The supervisor required separate approval of this newly proposed critical-audit scope after step 394; this turn compares it to existing source coverage rather than refreshing a ready mathematical target's bibliography.

## Source applicability and retained qualifications

The primary results are precisely cited in the canonical foundations and
L106; this assessment reuses their inspected passages, not fresh source
retrieval. Schrijver, *New code upper bounds from the Terwilliger algebra
and semidefinite programming*, IEEE TIT 51 (2005), 2859–2866,
DOI 10.1109/TIT.2005.851748,
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
III.B (62)–(67), p.7, and Kim–Toan,
[arXiv:1212.3467v1](https://arxiv.org/pdf/1212.3467v1), (31)–(35),
pp.8–9, apply to nonempty binary constant-weight codes with
0<10<136<=1024. Their actual-orbit normalization and equalities preserve
t-s as well as permuted distances. Impossible indices are absent;
forbidden actual orbits and Boolean repetitions are retained.
Schrijver (61)'s qualified complement prefactor is unused. PSD and
block decomposition are outside this audit.

Raghavendra–Tan,
[arXiv:1110.1064v1](https://arxiv.org/pdf/1110.1064v1), Section 3,
Definitions 3.1,3.3 and pp.8–9, concerns consistent local distributions
with an additional global-cardinality condition; consistency alone does
not imply it, and a global representing distribution is not promised.
The Boolean universe here is the set of 68-subsets, not the 1024 code
positions. L098 supplies the local homogeneous specialization and
positive-singleton normalization, including null pairs and both repeated
third words. This is a previously proved specialization to check against
L106's use, not new mathematics approved and derived in this review.
Polak, [arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1),
Proposition 1.1 and its indicator proof p.2, Section 1.2 p.3, supplies
constant-weight indicator necessity and constraint-preserving averaging.
Retain the printed A(n,d) versus proved constant-weight qualification.
No actual-label RS averaging is licensed.

The step-393 assessment's inspected MIT 6.854 linear-equality passages
cover exact rational elimination and substitution. No Phase I,
full-row-rank simplex assumption or runtime guarantee is needed for an
audit of saved finite operations. The restriction itself is not a theorem
import: only its stated infeasibility is to be audited. No source found
in the reused discovery establishes that finite verdict directly.
Unread Trinker, split-algebra and bounded-variable algorithm leads remain
unread and are not essential for this audit. No novelty is inferred.
Full matching Mathlib coverage remains not checked.

## Duplicate and failure comparison

L098's frozen-control rejection is already critically audited despite
stale pending language in PROOF.md. Its moment assignment is different
from L106's free-triple prescription. L105's all-row interval pass uses
independent copies of entries and supplies no shared-variable assignment.
ATTEMPTS/082 rejected one numerical reconstruction with free pairs and
PSD; it is neither a separator nor a proof of full infeasibility.
ATTEMPTS/089 parks L106's prescribed support and must remain parked.
The new audit tests the correctness and scope of that recorded negative
result; it does not reopen any stopped construction. Existing verifier
checks are evidence to inspect, not independent audit approval.

## One approved future audit

Essential inputs: L021–L023,L098,L106; foundations/04,12,13; the complete
fixed-pair-shared-scalar-results.json and
fixed-pair-shared-scalar-verification.json certificates and both matching
constructor/verifier scripts under scripts/finite-support/. L105 and
ATTEMPTS/081–082,088 are contrasts, not added mathematical premises.
No cross-notebook input is required.

Read the canonical proof against the complete load-bearing evidence:

1. Recover the exact N and pair prescription from L021–L023/L098 data;
   verify certificate and endpoint hashes without loading unrelated
   large evidence. An unchanged claimed hash alone is not a mathematical
   check of the new support.
2. Check actual-orbit admissibility, t-s invariance, every presentation,
   forbidden distances, both repetitions and null pairs. Audit the
   claimed exhaustion of 64 free classes and 190 original entries;
   equating distance-only variables would invalidate the conclusion.
3. Independently check all 69 equations, coefficients and fixed terms,
   including row zero and rows 1–4, the rank/uniqueness argument, all
   closed formulas and the exact negative coordinate. Inspect complete
   relevant rational values, not truncated previews or solver flags.
4. Check the lossless scalar codebook and lift over every original
   orbit, all six eight-atom reanchorings and every scalar slack, plus
   all 69 contraction residuals. Independently reconstruct rather than
   merely copying constructor or verifier verdicts. Separate the claimed
   single mathematical sign failure from implementation failures.
5. Check that no conclusion extends to unrestricted triples, other
   pairs, PSD, actual support-code realizability, RS lists or safety.

Use a fresh audit artifact prefix; preserve both original certificates
and scripts. One independent complete reconstruction and replay suffice;
no optimizer or alternate candidate is covered. Reuse the original work
bounds (20 million presentation visits, 5 million elimination updates,
1 GiB live memory, 256 MiB fresh certificates, 262144 bits per rational
component and 900 seconds), recording any incomplete evidence explicitly.
Save partial audit reasoning before lengthy work. Script outputs must
identify actual/required bounds, failures and evidence paths.

## Relevance, continuation and abandonment test

Main gap: arbitrary-center safety at 68/67 agreements in the 955–957
bracket. Intermediate target: critical validation of exactly L106's
restricted-support obstruction. Downstream use: a retained negative
result prevents later coupling work from relying on this failed support;
a correction prevents an invalid obstruction from guiding route choice.
Independent unrestricted scalar/cardinality and PSD gaps remain open.

Retain L106's verdict only if source conventions, support exhaustion,
uniqueness, exact sign and complete evidence agree. Any discrepancy is
a correction task or explicitly incomplete audit, never a reason to
silently change the support or restart a solve. This literature turn
does not execute the audit, verify the certificates or establish a new
lemma. It approves this scope for the next research turn, subject to the
supervisor's separate gate; all prior stops and budgets remain intact.
