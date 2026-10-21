# Count-dependent cycle exclusion — completed scope review

TARGET: Determine the maximal word-count cutoff obtainable by combining L041's r-dependent represented-length inequality with Simons–de Weger Corollary 2, using rigorous bounds and retaining primitive-to-represented counts.
CHECKED: 2026-10-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Four focused exact-word, coefficient and general-cycle queries; reused multiword/three-word/odd-count assessments; inspected L041 statement/count passages, complete L042, its audit record, Attempt 019 and history 069; queries and limits below.
SOURCE_EVIDENCE: Published Simons–de Weger Acta Arith. 117 (2005), sections 1.1–1.3 pp. 51–53, Corollary 2 and complete proof reopened; inherited Lemma 12, Hercher Theorem 16 and general full-minimum comparisons reused from ready assessments.
COMPARISON: L041 covers all integer r>=3 and L042 checks the count bridge; Corollary 2 supplies the chosen threshold but no maximal cutoff for this word language. No inspected source or scoped local result supplies the requested optimization.
GAP: Certify the maximal initial range of word counts excluded by the fixed L041 inequality and chosen Corollary 2 comparison; delimit failure at the next count without asserting a cycle exists.
REASON: Essential coverage is complete for one separate REPRODUCTION calculation/application; import the general bounds and prove only the elementary optimization and its precise limitation.
SCOPE: All L041 hypotheses for integer r>=3, actual closed positive words with J_i>=2,H_i>=3,a_i>=0 congruent to 2 modulo 18, n_0>1, positive odd residue-20 junction occurrences and independent exact tails; retain repeated periods and coincident values.
LITERATURE_REASON: The saved maximal-cutoff target was REVIEW_REQUIRED and lies beyond the prior r=3 application; this turn resolves its optimization scope using ready source coverage.

The main gap remains universal eventual descent. The intermediate target
would quantify how much of the finite word-count range the existing
length mechanism can exclude at once, avoiding a sequence of isolated
one-count lemmas. Its plausible downstream use is a rigorously delimited
restriction on possible closed postspell itineraries. It supplies no
entry theorem, unrestricted count bound or divergence control.

Essential proposed inputs are L041's full r-dependent inequality and
count definitions, L042's audited primitive-to-represented comparison,
and published Corollary 2 with its imported computational qualifications.
Maintain r>=3 and all L041 actual-word hypotheses: J_i>=2, H_i>=3,
a_i>=0 congruent to 2 modulo 18, n_0>1, positive odd residue-20
junctions, closure and independent exact tails. Repetitions and coincident
states remain allowed. Reuse the existing multiword and three-word
assessments; a new discovery search is needed only for missing coverage.

Continuation test for later approved mathematics: identify a certified
cutoff and a precise failure of this inequality-only contradiction at
the next count, retaining integer counts and all source qualifications.
If no extension is justified, record that limit and choose a different
mechanism; failure of the bound is not existence of a cycle. The startup
proposal supplied no cutoff or approval. The separate review below now
approves the calculation scope, without performing it.

## Completed comparison — 2026-10-08

The primary input is John Simons and Benne de Weger, *Theoretical and
computational bounds for m-cycles of the 3n+1-problem*,
[Acta Arithmetica 117 (2005), Corollary 2 and proof p. 53;
conventions pp. 51–53](https://www.impan.pl/shop/en/publication/transaction/download/product/82263).
The published version uses the shortcut map, odd count K and even count
L, allows nonminimal periods and can start at any cyclic local minimum.
Corollary 2 gives K>225640000 with no fixed-m restriction. Its complete
proof uses Lemma 1, the published height input x_min>301*2^50 and
continued-fraction denominators 225644606 and 397573379. These remain
imports; original computation certificates and Crandall's proof are
not independently certified. No stronger modern threshold is imported.

Reuse `2026-10-08-multi-postspell-represented-length-bound.md`,
`2026-10-08-three-postspell-cycle-exclusion.md`,
`2026-10-08-three-postspell-exclusion-audit.md`, and
`2026-10-08-two-postspell-cycle-length-comparison.md` in this directory.
They cover L041's inherited estimates, general fixed-minimum ceilings
and the Hercher correction qualifications. No general theorem is to
be reproved. The source's full minimum count is a different parameter
from r; those general ceilings cannot be specialized by setting m=r.
This comparison retains the strongest relevant conclusions actually
inspected in the reused coverage, rather than certifying every newer
cycle-bound claim returned by search.

L041's Hypotheses, Conclusion and occurrence/period passages were read.
Its exact A(r),B(r) and all-r inequality are established local inputs,
with N=K+L, K=sum_i(3J_i+H_i), L=sum_i(J_i+a_i), and N>=13r.
The complete L042 and its separate audit were inspected. They check
nontriviality, rotation and K=dK_0,L=dL_0 for a positive integer d;
the all-r scaling passage is already in L041. L042's three-word
exclusion is a comparator, not an all-r exclusion to import unchanged.
The remaining work is the optimization, not another wordwise proof.

"Maximal" must be qualified by the fixed L041 inequality and the
Corollary 2 threshold. The later proof must specify its retained integer
count restrictions and show exclusion throughout the claimed initial
r-range, then certify why the same comparison ceases to exclude at the
next r. If it uses only K_0<=K<N, say so; if the exact K,L restrictions
sharpen that comparison, justify them explicitly. A scalar feasible
length or count tuple is evidence of the inequality's limitation only,
not an actual parity word, affine closed root or positive cycle.
Any claim of optimality among other bounds is outside this approval.
Certified logarithm enclosures and an analytical monotonicity argument
are within scope; floating-point previews alone cannot establish a
cutoff or its maximality. No such enclosure, count test or derivative
calculation was performed this turn.

The focused queries were `Collatz "postspell" "cycle" "word"`,
`Collatz "Simons" "de Weger" cycle lower bound 225640000 length minima`,
`Collatz "postspell" "word count" cycle cutoff`, and
`Collatz "399/5" "23/8" cycle`. No matching optimization theorem was
identified. Results included the published paper, its distinct 2010
revision, the already assessed Hercher paper, public Collatz ledgers
and newer claimed minimum-count exclusions. Apart from the published
paper reopened above, these new search leads were not read and supply
no theorem input. Exact coefficient searches returned unrelated items.
Failed searches are not evidence of originality. There is no essential
source blocker for this fixed-input target; the known exact target page
and map comparison are reused from the same-day multiword assessment.

Attempt 019 and history 069 were read and preserved: boundary guards
alone and omission of intervening minima do not furnish exclusions.
The proposed length optimization uses neither failed mechanism. Scoped
local comparison found the all-r bound and r=3 exclusion, but no completed
maximal-cutoff calculation. No sibling notebook was read. Full matching
Mathlib coverage and external Lean build remain unchecked; inherited
Rhin/source-computation qualifications remain in L041.

Decision: SPECIALIZE for the exact unchanged TARGET, permitting a later
RESEARCH/REPRODUCTION calculation and theorem application. Completed
EXPLORATION, LITERATURE/NOVELTY_UNCHECKED: coverage is ready but no cutoff,
new mathematical result or advance beyond the checked sources is claimed.
No lemma or mathematical script was written, no mathematical exploration
turn was spent, and no counter reset is claimed. Universal entry, arbitrary
word counts, other cycles, divergence and eventual descent remain open.
