# Total represented length — completed scope review

TARGET: Establish an explicit absolute upper bound on represented N for L031's actual closed two-postspell words using L038 and L035, retaining independent tails and repeated periods.
CHECKED: 2026-10-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Five focused exact-word and cycle-length queries completed; L031/L035/L038 hypotheses and conclusions, L035 count/repetition proof, L034 minimum count, ready balance/both-word/nonunit-run assessments, history 069/085 and Attempt 019 compared; queries and limits below.
SOURCE_EVIDENCE: Simons–de Weger, Acta Arith. 117 (2005), section 1.2 p. 52, Theorem 3 all cases p. 55, Lemma 8 and full proof p. 59, Lemmas 12/14 and full proofs p. 61, large-m proof case p. 62 inspected; Hercher, JIS 26 (2023), Article 23.3.5, Theorem 16 and full proof pp. 10–11 inspected; existing balance/both-word source assessments reused.
COMPARISON: Inspected general length ceilings depend on the full minimum count; no inspected theorem supplies the exact absolute two-postspell represented-N ceiling. L035 already supplies the represented counts and cycle inequality, and audited L038 controls both prefixes. Their remaining elementary combination is an unproved specialization, without a novelty claim.
GAP: Test whether the represented count identity and the two approved bounds yield a rigorously solvable effective inequality for N without an assumed tail cap or primitive period; no inequality or numerical ceiling has been derived here.
REASON: Essential count/period coverage and stronger-result comparison are sufficient for one later REPRODUCTION proof attempt at the unchanged target; no general cycle theorem needs reproof.
SCOPE: Actual positive closed W_1W_2 of L031 with integers J_i>=2,H_i>=3,a_i>=0 congruent to 2 modulo 18, positive odd residue-20 n,x,n>1, both tails exact, N the represented length, repetitions and x=n admitted.
LITERATURE_REASON: Absolute total length is outside the previously approved both-prefix logarithmic target; its full-minimum and represented-period comparison required separate review.

## Relevance and bounded test

The main gap remains universal eventual descent. The single intermediate
target is an explicit absolute ceiling for total represented length in
this conditional language. It could support a later integer-closure
analysis or comparison with cycle-length lower bounds; feasibility of
exhaustive testing is not assumed. Universal entry, closure exclusion,
other cycle languages and divergent orbits remain independent gaps.

Continue this combination only if a later proof obtains a solvable
inequality with explicit justified constants using the stated inputs.
Abandon it if an uncontrolled tail-dependent term remains or an extra
unproved height, repetition or minimum-identification hypothesis is
required. This assessment approves investigation, not the conclusion.

## Primary comparison and applicability

John Simons and Benne de Weger, *Theoretical and computational bounds
for m-cycles of the 3n+1 problem*,
[Acta Arithmetica 117 (2005), 51–70](https://www.impan.pl/shop/en/publication/transaction/download/product/82263),
section 1.2 allows nonminimal periods. Theorem 3(a),(d) gives finiteness
and effective bounds for fixed full local-minimum count m. All statement
cases, Lemma 14's proof and the large-m proof case were inspected.
These bounds depend on m; they do not state the present absolute target.
Lemma 8 and its complete proof provide a count-ratio estimate using the
published computational height input. Lemma 12 and its complete proof
supply the effective linear-form lower bound already imported in L036–L038.
The original Rhin proof remains unread; source computations remain imported.

Christian Hercher, *There are no Collatz m-Cycles with m <= 91*,
[JIS 26 (2023), Article 23.3.5](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf),
Theorem 16 and its full proof were inspected. Its cycle-product and
odd-run-sum argument supplies the upper estimate used by L035.
Reuse L035's documented primitive-to-represented scaling; do not apply
set cardinalities directly to repeated occurrences. No reproof is needed.

These are the precise primary inputs/comparators, not new imported
lemmas. The ready assessments
`2026-10-07-two-postspell-logarithmic-parameter-balance.md` and
`2026-10-07-two-postspell-both-word-joint-bound.md` in this directory
retain complete prior lower-bound, successive-minimum and transfer
coverage. Their scope limitations are preserved, rather than silently
expanded into a total-length theorem.

## Local inputs, duplicates and failures

L031 supplies actual integer closure with its exact independent tails.
L035's canonical count proof gives
K=3(J_1+J_2)+H_1+H_2, L=J_1+J_2+a_1+a_2, N=K+L,
and its conclusion gives the represented positive linear-form inequality.
L038's canonical conclusion bounds both 4J_i+H_i relative to log N;
its separate audit in history 085 found no defect. These are the essential
inputs to the next test, with inherited L037/L036 coverage reused.
The next proof must justify every comparison of these counts and every
explicit constant; none is established by this assessment.

L034 counts J_1+J_2+2 cyclic minimum occurrences, so two designated
junctions cannot replace the full count by two. History 069 preserves
the Brox exponent mismatch and unread later proof; no Brox result is
imported. Attempt 019 preserves that closure already enforces the
boundary guards. The proposed effective-bound combination is different
from another guard-only audit or a two-long-tail count-only exclusion.
The overview and canonical conclusions explicitly leave total N open;
no local duplicate total-length result was found in these scoped reads.

Retain all affine offsets, exact tails, n>1, positive odd residue-20
junctions, represented counts and x=n. Assume no tail cap, primitive
period, least root, relative growth or junction/global-minimum identity.
A bound here would concern this fixed two-word language; it would not
bound arbitrary multiples of an unrestricted cycle representation.
No positive closed integer example or complete candidate is asserted.

## Search and inspection limits

Queries: `Collatz cycles fixed number local minima upper bound length
Simons de Weger Theorem 1`; `Collatz cycle upper bound length two nonunit
even runs Hercher`; `Collatz "postspell" "cycle" length bound`;
`Collatz "OOEO" "cycle" bound`; `Collatz "two" "tails" upper bound cycle
length`. General fixed-m results led to the primary passages above.
Exact-word searches supplied no inspected matching theorem. Failure to
find a match does not certify novelty or source absence.

Search results also surfaced a Zenodo tail-structure preprint and public
research ledgers with broader claims. Only snippets were encountered;
these are unread leads, not theorem coverage or accepted inputs. They
are not needed for the elementary combination of the already audited
local inputs. No access blocker was encountered for essential coverage.
No cross-notebook input was used. Mathlib coverage of the full matching
combination and supporting count inequalities was not checked.

This LITERATURE/NOVELTY_UNCHECKED turn is EXPLORATION: a new bounded
comparison completes coverage but establishes no new mathematical bound,
repair or exclusion. It spends no mathematical exploration turn and
claims no counter reset. The exact TARGET above is ready for a later
RESEARCH/REPRODUCTION proof attempt under SPECIALIZE.
