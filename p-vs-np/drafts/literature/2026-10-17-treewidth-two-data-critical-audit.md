# Treewidth-two data — approved critical-audit scope

TARGET: Critically audit L071's all-root selector reduction, affine-ABP suffix realization and aggregate full-bit bound under the full signed treewidth-two promise.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact structural-target searches in 2026-10-16-treewidth-two-extension-data.md; compared completed L071 with L026/L037 receiving hypotheses and targeted history/271–272 and Attempts 019–021; no new general discovery search or originality claim.
SOURCE_EVIDENCE: Reused the prior Jha–Suciu Corollary 2.14/section 4 and Raz–Shpilka Lemma 2 Step 1 coverage; freshly read Amarilli–Bourhis–Senellart arXiv:1604.02761v1 Definitions 6.2/6.4, Lemma 6.6 and its complete Appendix A proof (PDF pp.15–16,28–29), and de Colnet–Ordyniak–Szeider AI 351 (2026) Definition 1, Proposition 2 and section 3.1 correction (PDF pp.3–4).
COMPARISON: Fixed-treewidth single-output Boolean compilation and same-order completion are covered; L026 supplies exact ordered value/K/P/W identities and L037 receives explicit affine ABPs. L071 supplies the additional selector and graph realizations to audit; neither a source theorem nor this review certifies those local constructions.
GAP: Independently check L071's selector decomposition/restriction, exact suffix graphs, signs/terminals and aggregate encoding against the covered inputs; unrestricted ER data existence and SAT transfer remain outside the target.
REASON: This separate source comparison finds no missing essential coverage for the exact saved audit target; authorize one bounded proof audit under SPECIALIZE, with no mathematical audit or new theorem established here.

Essential local inputs are L071 and its actual mathematical inputs L025,
L026 and L037. Reuse the preceding structural assessment, including its
all-root/common-order and explicit-ABP scope; it has not been changed.
The original main gap is unrestricted SAT decision/separation. This audit
concerns a restricted data-existence result, not a P-versus-NP candidate.

The approved concrete audit should check the degree-two elimination/decomposition,
the ownership and connectedness of all 17-vertex selector bags, the fixed
width compilation hypotheses, all selector restrictions and complete common
orders, the exact free-ring polynomials of the two-region K and paired W
graphs, exact signed wrappers, terminal/constants/repeated-input cases,
and separately written roots and dictionaries in R and E_ABP. Do not replace
the formal identities by Boolean equivalence outside L026's increasing
multilinear subspace. No implementation evidence is claimed by L071.

Continue on a complete valid restricted construction or a repair preserving
its bounds; otherwise identify the exact broken claim and narrow it.
Unrestricted ER representation, formula-only bounds, W/V/U and SAT
transfer remain unresolved assumptions/obligations outside this audit.
No cross-notebook input is needed. Mathlib matching coverage is not checked.


## Separate source-scope comparison — step 273

LITERATURE_REASON: The completed L071 construction is new relative to the
prior structural assessment; this mandatory separate review compares its
actual imported hypotheses and representation interfaces before the audit.
The exact TARGET is unchanged. The prior assessment remains the canonical
record of discovery queries, Jha–Suciu proof cases and Raz–Shpilka composition
coverage; no repeated broad search was necessary.

Freshly inspected primary sources:

- Amarilli–Bourhis–Senellart, *Tractable Lineages on Treelike Instances:
  Limits and Extensions*, arXiv:1604.02761v1 (10 April 2016),
  [author long version](https://pierre.senellart.com/publications/amarilli2016tractable_long.pdf),
  Definitions 6.2/6.4, Lemma 6.6 and complete Appendix A proof,
  PDF pp.15–16,28–29. The model permits AND/OR/NOT circuits with graph
  treewidth. The theorem gives polynomial-time single-output compilation
  for fixed width; it does not assert simultaneous outputs or arithmetic
  witnesses. The proof constructs a decomposition-induced order, merges
  residual-equivalent prefixes and tests equivalence using two restricted
  circuit copies sharing remaining inputs and a disagreement gadget.
  Its initial constant-width shorthand must be read with its later explicit
  polynomial pair bound, as already noted in the prior assessment.
- de Colnet–Ordyniak–Szeider, *OBDDs, SDDs, and circuits of bounded width:
  Completeness matters*, Artificial Intelligence 351 (2026), 104458,
  [published PDF](https://eprints.whiterose.ac.uk/id/eprint/234745/9/1-s2.0-S0004370225001778-main.pdf),
  Definition 1, Proposition 2 and section 3.1, PDF pp.3–4.
  Completion preserves order with O(n|B|) time and factor-n width cost.
  The paper explicitly allows dummy tests with equal successors in its
  completion discussion, despite the distinct-successor wording in its
  initial BDD definition. Constant functions and variables omitted from a
  root's support require explicit completion conventions. The correction
  concerns the OBDD-to-pathwidth converse; L071 does not invoke it.

This comparison leaves the existing construction unverified. In particular,
polynomial Boolean compilation alone does not imply that a selector circuit
has width 16, nor that a restriction supplies every required root, nor that
any arithmetic circuit admits a small ABP. Those are exactly local claims
for the next audit. L026's formal recurrences (6) and (8), its signed-root
identification and increasing-multilinear injectivity, and L037's complete
receiving hypotheses are available locally and match the proposed audit
interfaces. Their reuse avoids a new proof of their identities here.

The audit must distinguish the primary sources' incomplete-width definitions
from L026's dense levels: use size-controlled completion, explicitly charge
omitted original-variable tests and constant roots, and retain parallel
edges/equal successors in the arithmetic graphs. This is a source-interface
checklist, not a finding that L071 is correct or defective. No new bound,
lemma, computation or certificate is established in this literature turn.

Targeted comparisons with history/271–272 and Attempts 019–021 find no
completed duplicate audit. The HWB stop concerns the unrestricted promise;
the degree-only and prescribed-pair-table stops concern different receiving
polynomials. They remain intact and do not decide the present restricted
audit. No unread lead is essential within this scope. Mathlib full matching
coverage remains not checked; no absence or novelty is inferred.

SCOPE: Exactly TARGET under L071's full signed graph promise, with inputs L025, L026 and L037; source applicability checks, explicit graph identities, degenerate cases and full-bit accounting, allowing a bounded repair within the same hypotheses but no stronger structural theorem or unrestricted conversion.

Continue only if all stated interfaces survive or admit a bounded repair
preserving the claimed polynomial bounds. Otherwise record the exact failed
claim and narrow or abandon that construction. A changed mathematical target
outside this scope requires a separate REVIEW_REQUIRED assessment. Restricted
L037 certificate assembly is the downstream use; arbitrary ER representation,
formula-only bounds, W/V/U and unrestricted SAT decision/separation remain
unresolved. No cross-notebook input is used.
