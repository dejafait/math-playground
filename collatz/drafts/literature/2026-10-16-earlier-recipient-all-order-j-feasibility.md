# Earlier-recipient all-order J feasibility — source assessment

TARGET: Test all-order endpoint/domain/J infeasibility for a_j=20 with 0<=j<=21, a_23=2+18t, a_24=166504394-18t, other tails 2, and 1<=t<=9250244.
CHECKED: 2026-10-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Focused cyclic parity/affine intermediate-constraint, exact-constant and scalar-ordering web queries; narrow local checks of L055/L064/L070/L071, ready assessments and Attempts 026/031 found no inspected theorem deciding this earlier-recipient family.
SOURCE_EVIDENCE: Reused inspected Halbeisen–Hungerbuehler (1997) section 2 equations (2)–(4), Lemma 2 and induction pp. 228–229, Lemma 4 p. 230; ready ISAAC 2024 scalar-ordering and DLMF scope records; newly read Fernandez–Ibanez arXiv:2607.24844v1 definitions and Theorem 7.3 with proof, and Theorems 8.1/8.2 statements and proofs as a nonimported scope comparison.
COMPARISON: Known finite affine/logarithm machinery covers the proposed techniques, but L071 fixes recipient 22, L070 fixes that recipient in literal order, and L064 covers only the t=0 literal boundary; scalar extrema do not supply the simultaneous guard verdict.
GAP: Changed-support uniform cyclic control, complete first-displacement comparisons and literal rejection or a verified feasible tuple remain mathematical obligations; this review derives none of them.
REASON: Essential source scope is now assessed; permit one separate SPECIALIZE/REPRODUCTION attempt for exactly TARGET without redoing general affine coding or transferring old-allocation conclusions.
SCOPE: L055 indexed pairs, arbitrary intact cyclic orders, real s>=540/11, exact shifted endpoints including closure and own-input non-strict J guards; no H/seed, minimum-location, integrality, actual-word or primitive/count-ray premise.
LITERATURE_REASON: The saved REVIEW_REQUIRED target moves the fixed recipient outside prior ready support; this essential changed-hypothesis comparison is the reason for the literature-only step despite the balance target.

The initial REVIEW_REQUIRED proposal is preserved below in scope. The separate
source comparison recorded later in this file now authorizes one later
mathematical attempt, not an exclusion verdict. No new mathematics was
derived during this literature-only step.

The proposed system uses exactly L055's 25 indexed J_i,H_i pairs.
Choose integers j in {0,...,21} and 1<=t<=9250244. Keep every outgoing
triple intact under any permutation pi. Require real s_0,...,s_25
with s_25=s_0 and s_k>=540/11, and exactly L071's shifted endpoint
equation and own-input non-strict J guard, with the newly attached tails.
In particular row 22 now has tail 2. Repetitions and coincident junctions
remain allowed. There is no H/seed, minimum-location, integrality,
actual-word or primitive/count-ray premise.

Potential local inputs are L055's complete table and logarithm bounds,
L071's product/first-displacement method and L070's literal comparison
method. Their old-allocation conclusions are not inputs for the new
support. L041 would supply an eventual actual-word necessity bridge only
after an independently justified subsystem result. No change to a prefix,
minimum argument, literal rejection or certificate is justified here.
Full matching Mathlib coverage is unchecked.

Main gap: universal eventual descent. Plausible downstream use: identify
whether the restricted exclusion withstands an earlier location of the
fixed transfer, or obtain a concrete limitation of the current guard
method. A later approved mathematical attempt should continue only with
a uniform justified exclusion over the stated j,t,pi domain or a rigorously
verified admissible tuple. A failed sufficient comparison alone is only
a method stop, not feasibility. If that comparison fails, record its exact
failed premise or margin and reassess before enlarging the family. This
target cannot by itself address all allocations, entry, unrestricted
cycles, divergence or universal descent.


## Separate source comparison — step 246, 2026-10-16

### Primary machinery and applicability

Reused the ready records in
[the row-22 all-order assessment](2026-10-15-permuted-two-recipient-j-test.md),
[its literal assessment](2026-10-15-two-recipient-tail-j-feasibility.md),
and [the last-pair primary comparison](2026-10-14-last-pair-permuted-j-feasibility.md).
These record actual primary readings, including the essential induction
and exchange cases; their primary PDFs were not reopened this turn.

Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational Collatz
cycles*, Acta Arithmetica 78 (1997), 227–239, DOI
10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf),
provides finite chronological binary-word affine composition and the fixed
point when its denominator is nonzero. The recorded proof reads the
length-one case, appended-zero induction and stated analogous appended-one
case. Only this formal identity is eligible for import; rational parity
or integer realization is not inferred. L055 supplies the complete fixed
indexed table and count-dependent positive Lambda enclosure. Recipient
redistribution and permutation must be checked to preserve those totals
before applying the denominator assertion. The changed-coordinate match,
root bounds, signs and every endpoint remain the later attempt's work.
There is no reason to reprove general coding.

Lemma 4, p. 230, requires equal length/one count and every-prefix count
domination to compare numerators. Equal totals alone do not suffice.
Kubo–Makino–Sakamoto, *Composition Orderings for Linear Functions and Matrix
Multiplication Orderings*, ISAAC 2024, DOI 10.4230/LIPIcs.ISAAC.2024.44,
[Theorems 1/3, pp. 44:3–44:4](https://drops.dagstuhl.de/storage/00lipics/lipics-vol322-isaac2024/LIPIcs.ISAAC.2024.44/LIPIcs.ISAAC.2024.44.pdf),
concerns a scalar composition at a prescribed real input. Reuse its
recorded increasing-affine definitions and proof cases (i)/(ii),
pp. 44:8–44:9. It does not characterize simultaneous intermediate guards
at a cyclic root. The omitted case-(iii) proof/full version and the
previously recorded Kawase–Makino–Seimi ordering lead are not imported;
no optimizer algorithm is needed for this target.

Reuse [DLMF 4.5.1](https://dlmf.nist.gov/4.5.E1) at positive eta/n,
[4.2.19](https://dlmf.nist.gov/4.2.E19) at positive real arguments, and
[4.6.4](https://dlmf.nist.gov/4.6.E4) on positive reals, with L055's
outward rational remainder method. Positivity, remainder sizes and
rounding directions still need verification in any new calculation.
Full matching Mathlib coverage is unchecked, not asserted absent.

### Discovery and stronger-result comparison

Queries actually run this turn:

- `Collatz rational cycles prescribed parity vector cyclic permutation intermediate inequalities affine composition`
- `Collatz "166504394" "recipient"`
- `"Composition Orderings for Linear Functions" cyclic constraints`

The exact-constant query supplied no matching theorem. Other results
included the already assessed ISAAC paper, informal repositories/forums
and unreviewed claimed resolutions; none of the latter is used as evidence.
A failed search establishes no novelty.

A new primary lead was Fernandez–Ibanez, *Christoffel Words as Extremal
Structures in Collatz Dynamics*,
[arXiv:2607.24844v1, 24 July 2026](https://arxiv.org/html/2607.24844v1).
Read sections 2–3 definitions, Theorem 7.3 and its proof, and Theorems
8.1/8.2 with their proofs. Theorem 7.3 states a scalar rotation-minimum
numerator maximization over binary words of fixed length and one count.
Theorem 8.2 assumes an actual periodic parity word with N/r>log_2(3)
and bounds some orbit element. Neither statement gives every designated
own-input guard for intact prescribed blocks. Their full supporting
combinatorial proof is not audited; no theorem is imported or specialized
numerically here. This lead is nonessential for the proposed direct
finite-affine test, not a source blocker.

Rechecked [MathPrize's page](https://mathprize.net/posts/collatz-conjecture/),
dated 7 July 2021: it still asks that the ordinary even/odd map reach 1
from every positive integer. The exact local target remains unchanged;
prize conditions are not a correctness premise.

### Duplicates, failures and bounded continuation

Directly read L055's full indexed table, L071's hypotheses and product,
rotation, prefix and first-displacement proof, L070's changed-root,
parameter and boundary passages, and L064's scope and canonical boundary
classification. The narrow earlier-recipient search found L064 and this
proposal, not a completed all-order result for the proposed interval.
L064 treats t=0 in literal order, outside TARGET. L070/L071 require the
fixed recipient at 22; their verdicts cannot be applied with j<=21.
L069 is a method precedent with different tails. In particular, the
prefix containing the moved recipient and the literal comparison must
be justified afresh; no signs, margins or monotonicity are approved as
already true for the new support.

Attempts 026 and 031 were read directly. Their old-allocation real
witness and one rejected permuted tuple neither settle this target nor
ban this different test. The recorded prime-diagnostic stops remain
preserved; this is not a restart of those routes. No cross-notebook input.

One later RESEARCH/REPRODUCTION attempt may address exactly TARGET.
Essential inputs: L051 endpoint/J conventions through L055/L070/L071;
L055 full table and count/log bounds; L071 product/rotation/displacement
method; L070 literal-root comparison method; L064 boundary contrast.
Their old-allocation conclusions are not new-support premises. L041 is
only a possible later actual-word bridge requiring separate assessment.
Continue with a uniform exclusion only after controlling every admitted
j,t and cyclic order and all own-input pairings, including closure and
the final tail-2 endpoint. Alternatively verify one admissible exact tuple.
Failure of a sufficient bound is a method stop, not feasibility. Do not
enlarge the support in the same attempt. Other allocations, entry,
unrestricted cycles, divergence and universal descent remain unresolved.

Outcome EXPLORATION: source coverage and an actionable bounded test are
ready; there is no new mathematical input or claim beyond the checked
literature. No lemma, DAG, PROOF or mathematical script was changed.
