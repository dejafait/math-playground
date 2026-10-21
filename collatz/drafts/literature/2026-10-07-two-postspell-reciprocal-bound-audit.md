# Uniform two-postspell reciprocal bound — approved audit coverage

TARGET: Critically audit L035's uniform two-postspell reciprocal bound, complete odd-occurrence accounting, and repeated-period specialization of Hercher's Theorem 16.
CHECKED: 2026-10-07
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused exact-statement and stronger-result discovery in 2026-10-07-two-postspell-reciprocal-sum.md; read full L035, relevant L020/L034 proof ranges, Attempt 019 and histories 069–071; narrowly retrieved Hercher's primary definitions, run proof, cycle proof and comparator proofs, without repeating discovery searches.
SOURCE_EVIDENCE: Hercher, JIS 26 (2023), Article 23.3.5, Definitions 1/5/6 pp. 2–4, Remark 7 and full proof pp. 4–5, Theorem 16 and full proof pp. 10–11, Corollary 17 and full proof p. 11, Theorem 27 and full proof pp. 19–20, Remark 31 p. 21; live journal PDF retrieved 2026-10-07. Other ready source coverage is reused, not newly retrieved.
COMPARISON: Source coverage suffices for the exact finite-word and repeated-period audit; a concrete comparator attribution mismatch needs attention: Corollary 17 uses 97M/(54X_0), not the loose 3M/X_0 envelope from Remark 7, and its proof's reciprocal-mass conclusion is non-strict.
GAP: L035 remains unaudited; its local accounting, constant, period scaling and source-comparison qualifications require a separate mathematical review. Integer closure and a sufficient Diophantine lower bound remain unresolved.
REASON: Approve one bounded audit with unchanged hypotheses, importing the published estimates and auditing only their local specialization; new source-comparison evidence changes an audit obligation without establishing or refuting the core bound.
SCOPE: Audit complete L035 for actual positive W_1 W_2, J_i>=2,H_i>=3,a_i>=0 congruent to 2 modulo 18, n>1 and positive odd residue-20 n,x,y, exact tails; no closure for the finite-word estimate, y=n only for the cycle application; retain repetitions, and review the existing comparison section under the source's verification-height qualifications.
LITERATURE_REASON: The saved critical-audit target was REVIEW_REQUIRED; separate scope approval is mandatory. Narrow primary rereads resolve the terminal-subrun and set-versus-occurrence questions and check exact comparator constants/signs; no enlarged target or repeated general discovery is undertaken.

## Scope approved for a later audit

Read the complete canonical proof in
`lemmas/L035-two-postspell-uniform-reciprocal-bound.md`, retaining its
actual positive W_1 W_2, J_i>=2,H_i>=3, a_i>=0 congruent to 2 modulo 18,
positive odd residue-20 n,x,y, n>1 and exact-tail hypotheses. Use the
unchanged prior assessment
`drafts/literature/2026-10-07-two-postspell-reciprocal-sum.md` for covered
primary statements, subject to the comparator clarification below.
Full matching and supporting Mathlib coverage remains
not checked, without an absence claim.

Essential input IDs are L020 and L034. L021's composition and L031's
closure criterion are contextual comparisons, not proof premises.
The proposed audit checks all internal input times of OOEO, the terminal
subrun's applicability despite a preceding O, the positive-offset growth
bound, the geometric constant and strict signs. Under y=n it checks
nontriviality, primitive return-time divisibility and simultaneous scaling
of K,L,S; compare generic envelopes with the exact source qualifications.
The bound does not assume distinct junctions, minimal representations,
least-root minimality, or existence of a closed word.

Continuation test: the cited coverage suffices to approve one bounded
critical audit of exactly these claims; that later audit must identify
any genuine proof defect or report its concrete checks without claiming
a complete Collatz resolution. A defect requires correction within its
covered scope or a new review if the hypotheses change. Missing essential
coverage permits source review only. Integer closure, Diophantine lower
bounds, other cycles, divergent orbits and eventual descent remain open.

This approval covers a later audit only. It does not perform that audit,
certify L035, derive another estimate or approve any changed research target.

## Primary comparison and precise source qualification

Christian Hercher, [*There are no Collatz m-Cycles with m <= 91*](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf),
JIS 26 (2023), Article 23.3.5, uses the same shortcut map (Definition 1).
Definition 6 partitions a nontrivial cycle into maximal odd/even runs.
Remark 7's first bound is T(n_i)<3/n_i; its proof uses only positive
odd-step growth. Its second bound requires n_i>X_0. This supplies
coverage for auditing the terminal-subrun specialization, not an audit verdict.

Theorem 16 states
delta<(K+L)/K<delta+sum_i T(n_i)/(3K log(2)).
Its proof uses sets of cycle states; L034's primitive-period argument
is therefore essential to reviewing represented time occurrences.
The full product, AM–GM, strict logarithm and odd-run partition proof
was inspected. Reproving the cycle theorem is unnecessary.

Corollary 17 uses 97m/(54X_0) in the ratio bound; its proof establishes
sum_i T(n_i)<=97m/(54X_0). Theorem 27's proof gives
sum_i T(n_i)<=3K/(4X_0). Both ratio bounds are strict.
Remark 31 retains X_0>765 for supporting estimates; X_0 denotes a
verified convergence height. Lemma 26's case proof is not newly audited.

The source has **not** changed from the version in the reusable
assessment. The narrow reread clarifies an omitted sharper comparator
and the signs, rather than refreshing source coverage by age.
In L035's existing comparison section, the phrase associating Corollary 17
with 3M/X_0 conflates that corollary with the weaker run-by-run envelope.
The prior assessment also reports only that the corollary retains M/X_0,
without its exact coefficient. The later audit must distinguish the
published comparator from the loose Remark 7 envelope, check which
claimed ratios refer to which bound, and repair attribution or narrow
the comparison if necessary. This source comparison supplies no revised
local ratio, new constant, or verdict on inequalities (1)–(3).
The mathematical lemma is preserved unchanged during this literature turn.

## Reuse, duplicates and unresolved inputs

The prior reciprocal-sum assessment records targeted searches for the
exact statement, stronger odd-run/geometric estimates and known
obstructions, including Simons–de Weger v1.44 (2010-08-31), section 1.2
and Lemma 4/Corollary 5, and Rozier–Terracol v2 (2025-02-13), Theorem 4.1.
Those inspected results remain ready comparisons; neither is newly
retrieved or an additional premise for this audit. The qualified infinite
orbit-set summability leads remain nonessential and are not imported.
No search failure is evidence of originality. The exact public target
statement checked in history 069 and the prior assessment is reused.

Read L035 completely to delimit the audit, L020 through its affine,
positive-offset and membership passages, and L034 through its occurrence,
nontriviality and primitive-period arguments. Essential input IDs are
L020 and L034 as in the supplied DAG. The finite-prefix identity must
be justified for each actual initial group, without silently extending
L020's whole-word parameter hypotheses. L021 is notation/context and
L031's closure criterion remains an unresolved contrast, not an input.

Histories 070/071 record the completed source approval and specialization;
there is no prior completed L035 audit. Attempt 019 stops adding boundary
guards to integer closure, not this mass estimate. History 069 parks the
two-long-even-run count parameter and inaccessible Brox proof route;
neither is needed here. The source discrepancy changes the audit's
comparison obligation, without reopening either exhausted route.

The main gap remains universal eventual descent. The intermediate
target is a reliable critical review of the already written uniform
reciprocal bound. Its plausible downstream use is a justified input to
a later Diophantine cycle-language test. Continue only if the exact
accounting, applicability and strict inequalities survive the covered
audit; a concrete defect requires repair or a narrowed claim, and a
changed essential hypothesis requires new coverage. No distinct
junctions, least-root assumption or cycle existence is admitted.
Unbounded integer closure, adequate lower bounds, other cycles,
divergent orbits, entry and universal descent stay open.

Completed step: NEGATIVE, LITERATURE / NOVELTY_UNCHECKED, actual task
literature_comparison. The new evidence is the sharper published
comparator and non-strict mass conclusion missing from the local
attribution; it changes what the later audit must accept or repair.
This is source clarification, not a new mathematical discovery or a
core-proof disproof. SPECIALIZE is ready for the unchanged TARGET.
No lemma, mathematical script, new derivation or numerical test was made.
