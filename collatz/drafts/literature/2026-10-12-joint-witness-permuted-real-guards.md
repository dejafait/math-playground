# Fixed joint witness: approved real-system guard comparison

TARGET: Test whether L060's fixed two-transposition rational root satisfies L055's complete 25-word real-system guards, allowing cyclic relabeling at its minimum junction.
CHECKED: 2026-10-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Three focused searches on prescribed-word/block permutations, exact K,N and rotation minima; scoped comparison of fixed-count/permutation assessments, relevant histories 169–173 and Attempts 027–030; no inspected result supplies this fixed order's guard verdict.
SOURCE_EVIDENCE: Reopened Halbeisen–Hungerbuehler (1997), section 2 equations (2)–(4), Lemmas 1/2 and relevant proof cases pp. 228–229; reused previously inspected rotation and Simons–de Weger coverage; inspected NIST DLMF 4.6.4 and L055's complete rational-log/remainder proof and audit.
COMPARISON: Known affine coding supplies the fixed point and chronological composition; the local specialization must match shifted coordinates and certify this order's own-index guards and minimum/seed. Literal-order margins and modular checks do not decide that verdict.
GAP: The fixed order has no certified real-system verdict; source coverage permits its finite guard comparisons, but order-dependent bounds and cyclic relabeling remain obligations of the next research step.
REASON: This separate literature-only comparison approves one RESEARCH/REPRODUCTION calculation on the unchanged TARGET, without a new mathematical derivation or feasibility claim.
SCOPE: Only L060's intact swaps (0,8),(7,12), row 24 and tail 166504412 fixed, K=397573379 and N=630138897; no new orders, factors, powers or actual integer realization.
LITERATURE_REASON: The permuted real-guard verdict was outside the literal-witness and modular assessments; resolve this changed scope once, reusing their adequate affine coverage.

Essential inputs for the proposed continuation: L055's literal allocation
and exact statement of the simultaneous real system, L056's positive
integral unshifted offsets, L057's chronological composition, and L060's
fixed order. L061 establishes why the two tested denominator primes no
longer decide this order. Inspect L055's precise system and its referenced
L051 hypotheses narrowly before selecting the guard implementation; do not
infer those guards from the modular audit or silently transplant their
literal-order verification. The present turn derived no permuted heights.

Main gap: universal eventual descent. The intermediate target is TARGET.
Its plausible downstream use is to decide whether the order surviving both
prime tests also survives the necessary real constraints already retained
in the restricted 25-word analysis. A failed necessary guard could remove
this order from that simultaneous system; a full verified pass would show
that this independent filter also fails for the order. Neither outcome
alone establishes integer realization, excludes every order or resolves
universal descent.

Continuation test after separate source approval: fix the unique positive
affine cyclic root, retain every intact triple and all 25 endpoints, and
either certify one violated necessary guard or verify every guard with
rigorous enclosures. Identify the smallest designated junction for the
seed without assuming that position zero stays minimal after permutation.
Preserve each own-index parameter/height match under any cyclic relabeling.
If bounds straddle a threshold, record the exact unresolved comparison;
rounded values or nominal pass flags do not decide it. Do not broaden the
order or modify parameters to repair failure within this target.

Unresolved assumptions: the permutation has no certified real-system
feasibility, integrality, actual parity/exact-tail or primitive realization.
Other orders/allocations, entry, unrestricted cycles, divergence and eventual
descent remain open. Inherited source qualifications persist; full matching
Mathlib coverage/build remain unchecked. Attempts 027–030 remain evidence
for their own stops, not bans on this different test. This assessment was
initially REVIEW_REQUIRED. The separate source comparison below now
approves its unchanged target; no permuted heights or margins were derived.

## Separate source comparison — 2026-10-12

The [MathPrize page](https://mathprize.net/posts/collatz-conjecture/),
dated 2021-07-07, was rechecked today. Its statement remains universal
eventual arrival at 1 for positive integers under n/2 when even and
3n+1 when odd. This agrees with GOAL.md and the conventions in
`foundations/01-target-and-scope.md`; prize adjudication is separate.

Read L055's full statement, allocation, rational construction, guards,
logarithm proof and separate audit; L051's hypotheses (1)–(4); and the
relevant L056/L057/L060 affine/chronological-coordinate passages.
The order is exactly
`8 1 2 3 4 5 6 12 0 9 10 11 7 13 14 15 16 17 18 19 20 21 22 23 24`.
Every triple stays intact. Reuse the canonical counts and positive Delta,
not their order-dependent literal-root brackets or guard margins.

### Primary sources and scope

Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational
Collatz cycles*, Acta Arithmetica 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemmas 1/2, pp. 228–229](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf),
is the primary affine input. Read the odd-denominator argument,
length-one case, last-bit-zero induction and stated analogous
last-bit-one case. For a nonempty binary word of length l with k ones,
Lemma 2 gives (3^k x+phi)/2^l and its fixed point phi/(2^l-3^k);
equation (4) gives chronological concatenation. Here l=N, k=K,
0 denotes E, 1 denotes O and Delta>0 is already certified. Use the
affine formula only, with the shifted match in L055/L056; no coding
reproof is needed. The source does not give these finite guard margins.

Reuse `drafts/literature/2026-10-11-twenty-five-fixed-count-tail-budget.md`
and `drafts/literature/2026-10-11-fixed-count-real-witness-audit.md`.
The former already inspected Lemma 5/Corollary 1, pp. 230–231:
their extremum concerns parity words and all parity-phase rotations,
not the designated-junction guard verdict for this prescribed order.
It also inspected Simons–de Weger, *Theoretical and computational bounds
for m-cycles of the 3n+1-problem*, Acta Arith. 117 (2005), 51–70,
[sections 1.2/2.1/2.2, Lemmas 4/6/7, pp. 52, 56–59](https://www.impan.pl/shop/en/publication/transaction/download/product/82263).
Their chain/matrix construction does not decide these guards; their m
counts every local minimum and cannot be set equal to our 25 words.
Integer-cycle height assumptions cannot be imposed on arbitrary reals.
L051 defines the tested system. Its published computational,
continued-fraction/Rhin/Crandall qualifications remain unchanged.

NIST DLMF, version 1.2.8, release 2026-09-15,
[equation 4.6.4](https://dlmf.nist.gov/4.6.E4), was inspected with its
domain Re(z)>=0, z!=0: log z has the odd-power expansion in
(z-1)/(z+1). Positive real arguments here meet that domain. L055's
canonical proof and audit already provide rational partial sums,
integrated remainder bounds, binary reduction and rounding budgets.
Reuse those proofs, rather than an unproved truncation estimate.
The existing script's base_log/log_bounds definitions were read only.
Separate E3 TeX/image retrieval failed; the HTML exposed E4 and its
domain completely, so no essential source is blocked.

### Exact approved calculation

Retain all of L051 (1)–(4), specialized as L055 states them: integer
J>=2, H>=3, a>=0 with a=2 modulo 18; all count identities and positive
integer primitive scaling with K_0>225640000; Lambda>0 and
N<(8/5)K+1725/1034; all 25 exact endpoint equations and closure;
s_i>=540/11 and h_i=log s_i; a smallest designated s_0; the strict
seed 0<h_0<(133/10)log N+8+log25; and both own-index guards with
their original non-strict J and strict H signs. This restates existing
hypotheses, not a new necessary condition. Primitive scaling is a
system constraint, not a certified primitive integer orbit.

Use the already recorded exact factored rational construction in this
chronology, with s_i=n_i+23/11. Recompute any order-dependent bounds.
Cyclic relabeling must move each triple with its input junction and
preserve the closing edge; it may select a smallest designated junction
only. L055's literal 18–20 billion root bracket and v_i table cannot be
transplanted without justification in the subsequent research step.
No new parameters, order search or global-orbit-minimum premise is covered.

Bounds must retain all affine corrections. A pass needs the appropriate
lower bound; a failure needs a sufficient upper bound or exact comparison
in the correct direction. Certify one violated required guard or every
required guard; if intervals straddle a threshold, save that exact
unresolved comparison and stop this bounded attempt. Full load-bearing
evidence must be inspected, not just saved flags or a preview. A different
essential theorem/technique beyond this affine/logarithm coverage requires
separate review. No root, prefix or guard was calculated in this turn.

### Discovery, duplicates and decision

Queries actually run today:

- `Collatz rational cycle permuting blocks prescribed parity word logarithmic guards Halbeisen Hungerbuehler`
- `"Collatz" "397573379" "630138897"`
- `rational Collatz cycles minimum cyclic permutations prescribed word`

Hits included the primary affine paper, the already compared Christoffel
preprint, exact-count tables, repositories and speculative forum/preprint
claims. Such snippets are not theorem coverage. The publisher lead
*Collatz high cycles do not exist* could not be opened; the ready
`drafts/literature/2026-10-10-fixed-pair-cyclic-product-range.md` already
parks that extremal high-cycle lead. It is not an input to this guard
test. Neither it nor the exact-count snippets supply an imported result.
No novelty inference or essential source blocker is claimed.

The narrow local comparison found only L055's literal-order witness
and the order-sensitive arithmetic results. The relevant permutation
assessments and histories 169–173 explicitly leave permuted guards open.
Attempts 027–030 stop their prime diagnostics without testing these
guards; preserve those stops. No duplicate completed verdict was found
in the checked paths. No global or exhaustive literature claim is made.

SPECIALIZE approves one separate RESEARCH/REPRODUCTION calculation of
TARGET. Full matching Mathlib coverage and external Lean builds remain
unchecked. Integer/parity/exact-tail/primitive realization, other orders
and counts, entry, unrestricted cycles, divergence and descent remain open.

Completed LITERATURE/NOVELTY_UNCHECKED, outcome EXPLORATION: this bounded
source comparison newly approves an actionable fixed-order test, with
no mathematical advance or claim beyond checked literature. No lemma or
mathematical script was modified or executed. Mathematical exploration
usage stays zero. This is the separate approval of the supplied proposal;
the following invocation defaults to the exact mathematical calculation.
