# Twenty-five-word fixed-count total-tail budget — source comparison

TARGET: Test the r=25 branch K=397573379, N=630138897 using the exact total-tail budget in L051 (1)–(4).
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Six focused searches on prescribed-parity/even-step allocation, rational-cycle exponent sums, tail budgets and the exact K; scoped duplicate search in drafts/literature, ATTEMPTS and history; read L051 hypotheses and L054 count/product/envelope passages plus Attempt 025/history 145. No inspected theorem decides the fixed-count coupled-tail system.
SOURCE_EVIDENCE: Reopened Halbeisen–Hungerbuehler author and published PDFs, Lemmas 1/2 and 3/4/5/Corollary 1 with relevant complete proof cases; reopened Simons–de Weger section 1.2, sections 2.1/2.2 and Lemmas 4/6/7 with complete proofs. Precise versions/pages below; unchanged general coverage reused from the ready 25-word and fixed-range assessments.
COMPARISON: Known rational coding and global-rotation/full-minimum bounds do not supply the requested allocation verdict. L054 loses tail distribution in its forward envelope; its aggregate realization already shows that testing the sum alone is insufficient. Coupling the retained total and congruences with guards/endpoints is the identified specialization gap.
GAP: No allocation inequality, all-allocation contradiction or fully checked simultaneous witness for the fixed branch is established; one separate mathematical attempt must retain the exact budget inside the cyclic constraints.
REASON: Essential source coverage supports one separate RESEARCH/REPRODUCTION specialization of existing endpoint/count machinery; no coding reproof or stronger integer-cycle import is needed. This newly ready assessment requires separate approval next turn, without rejecting L054.
SCOPE: Exactly L051 (1)–(4) at r=25 and K=397573379, N=630138897, L=232565518, with log25 seed, 1725/1034 remainder, all integer/primitive guards, real minimum/lower-height and own-index guards, all cyclic endpoints, independent tails, repeats and ties; enforce the existing total-tail identity and congruences, without a new pair or source threshold.
LITERATURE_REASON: The fixed-count coupled-tail allocation mechanism was outside the completed L054 envelope assessment; compare relevant primary allocation/rotation results once and reuse unchanged general inputs.

The main gap is universal eventual descent. The narrow intermediate
target concerns only one necessary count branch of the 25-word real
system; excluding it would still leave other count branches, entry,
unrestricted cycles and divergence unresolved. Establishing a full real
witness would locate a limitation of this system, not an integer cycle.

Essential local inputs are L051, L052 and L054. Keep r=25, the log25
seed, 1725/1034 remainder, all integer J,H,a guards, primitive scaling,
K_0>225640000, real minimum/lower-height guards, and all 25 exact cyclic
endpoints. Fix K=397573379, N=630138897, L=232565518; the unchanged
pair gives z=1. L054's height bounds are conditional necessities, not a
witness. Independent tails, repeated periods and ties remain admitted.

The aggregate identity sum a_i=N-K-sum J_i is already part of the
system's definitions. The proposed mechanism is to retain this total
and the congruences a_i=2 modulo 18 in the cyclic height constraints,
instead of substituting a_i>=2 independently at every forward step.
No feasibility, allocation theorem, optimal envelope or new arithmetic
bound is asserted here. No stronger source threshold or pair is proposed.

The later mathematical test, only after source approval, must produce
either a contradiction for all parameter allocations in this fixed
branch or a fully checked simultaneous witness; otherwise preserve the
precise failed coupled constraint and stop that comparison. Repeating
L054's envelope or changing only the count does not qualify. Review
general primary coverage for reuse before any new browsing; unread leads
are not evidence. Published computational/Rhin/Crandall qualifications
and unchecked external Lean/Mathlib coverage persist.

## Inspected primary sources

Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational
Collatz cycles*, Acta Arithmetica 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239:
[published PDF](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf)
and [author version](https://people.math.ethz.ch/~halorenz/publications/pdf/collatz.pdf).
Read Lemmas 1/2 pp. 228–229, Lemma 3 statement p. 229/proof p. 230,
Lemma 4 p. 230 and Lemma 5/Corollary 1 pp. 230–231 in the published
version (author PDF pp. 2–6). Proof cases inspected: odd-denominator
parity, length-one/last-bit-zero induction (last-bit-one stated analogous),
prefix-sum induction, finite bit exchanges, maximal-deficit rotation
and every rotation of the balanced word. Lemma 2 gives a nonempty
word's unique odd-denominator rational fixed point phi/(2^l-3^n);
positive denominator and n>0 give positivity. Lemma 5 optimizes the
minimum rotation numerator over all words of length l with n ones.
The existing coding uses l=N,n=K. This does not supply the constrained
tail-allocation verdict or integer realization, and the minimum is over
all parity phases, not merely designated junctions. No reproof is needed.

Simons–de Weger, *Theoretical and computational bounds for m-cycles
of the 3n+1-problem*, Acta Arithmetica 117 (2005), 51–70,
[published PDF](https://www.impan.pl/shop/en/publication/transaction/download/product/82263).
Read section 1.2 p. 52, chain/matrix sections 2.1/2.2 pp. 56–57,
and Lemmas 4/6/7 with complete proofs pp. 57–59. Their m counts
every local minimum; k_i,l_i are consecutive run lengths, and their
auxiliary a_i in x_i=2^{k_i}a_i-1 is not our tail. Fixed positive
run lengths give a unique rational cyclic solution, with integrality
an additional condition. Inspected cases: product cancellation and
strict logarithm estimate, chaining with l_i>=1,a_i>=1,x_i>=X_0,
cyclic product comparison and choice of the global minimum. Those
bounds do not optimize our tail distribution. Their full partition
and computational lower height cannot be imposed on L051's real
system by setting m=25. No stronger integer-cycle result is imported.

Reuse the ready
`drafts/literature/2026-10-11-twenty-five-simultaneous-feasibility.md`
and `drafts/literature/2026-10-10-fixed-pair-cyclic-product-range.md`:
Hercher, JIS 26 (2023), Article 23.3.5,
[Theorem 16 and full proof pp. 10–11](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf);
Simons–de Weger Corollary 2 p. 53/Lemma 12 p. 61; the previously
compared general global-minimum criteria and unimported Fernandez–Ibanez
arXiv:2607.24844v1 Theorems 7.3/8.1/8.2. L051's actual-word bridge,
primitive scaling and seed remain covered without changed hypotheses.
The exact target page was inspected on the same date in the ready
assessment; universal eventual arrival at 1 and map conventions are
unchanged. Published computation/continued-fraction/Rhin/Crandall
qualifications and the inspected correction's scope persist. External
Lean builds and full matching Mathlib coverage remain unchecked;
unknown availability is not absence. No new source theorem is imported.

## Discovery, duplicates and continuation

Queries actually run on 2026-10-11:

- `Collatz cycles prescribed parity blocks total even steps allocation bounds cycle`
- `Collatz cycle "sum" "exponents" "Halbeisen" rational`
- `Collatz "cycle" "tail" "budget"`
- `"Collatz" "397573379" cycle`
- `"Collatz" "prescribed" "parity" "bounds" rational cycles`
- `"Collatz" "even" "allocation" cycles bounds`

Results included the primary rational-cycle paper, the already compared
Christoffel preprint, repositories, forums and speculative cycle papers.
Exact-count hits included a bit-position preprint and a forum claiming
a stronger integer-cycle cutoff. These are unread snippet-only leads,
unused and nonessential to this real-system test; no such cutoff is
asserted or imported. No essential source remains blocked. The bounded
search does not establish novelty or exhaustive coverage.

The scoped duplicate search found only this assessment, Attempt 025
and history 145 proposing the coupled-tail test. The total-tail identity
is already a definition in L051, not a new lemma. L054 supplies an
aggregate allocation expressly without guards or endpoints. Repeating
that allocation check, the tail-free envelope or its scalar failed bound
would supply no new test. The attempt must couple tail placement with
the own-index guards and all endpoints. Earlier stopped scalar/fixed-test
routes remain stopped; they do not ban this different constraint.

SPECIALIZE covers existing source machinery, not a new allocation
theorem. A later RESEARCH/REPRODUCTION attempt may assemble its coupled
consequences at this fixed branch. Continue for an all-allocation
contradiction, a fully checked simultaneous witness, or an informative
rigorous obstruction to the chosen comparison. Otherwise save the precise
unresolved coupled constraint and stop that comparison. A relaxed numerical
survivor is not a full witness. Any essential new source hypothesis or
different target requires separate review. Other count branches, entry,
unrestricted cycles, divergence and universal descent remain unresolved.

Completed LITERATURE/NOVELTY_UNCHECKED, outcome EXPLORATION: the new
mechanism has actionable source comparison, without a mathematical result
or advance beyond inspected sources. No lemma or mathematical script was
modified or executed. Mathematical exploration usage stays zero after
L054's NEGATIVE. The unchanged TARGET remains the sole Next action;
the newly ready assessment receives separate approval next turn.
