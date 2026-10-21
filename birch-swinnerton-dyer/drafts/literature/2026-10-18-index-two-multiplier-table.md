# Index-two multiplier order — proposed bounded construction

TARGET: Construct and independently verify the complete multiplication table of L080's index-two multiplier order in the original H coordinates, within one 180-second production stage and one 180-second verification stage.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 320 searched exact phrases number field multiplication table change of basis order and Stevenhagen multiplier basis order; compared L077/L078/L080, the prior prime-local quotient and changed-prime assessments, history/305 and 306--319, ATTEMPTS/041/042, and the scoped table verifier. No completed multiplier-table duplicate was found in that scope; no novelty is inferred.
SOURCE_EVIDENCE: Reused and reopened Peter Stevenhagen, The arithmetic of number rings, Algorithmic Number Theory, MSRI Publications 44 (2008), pp.209--266, Lemma 6.4 p.221 and Section 9 pp.233--235, equation (9-2), Proposition 9.3 with proof and following full action/kernel/lifting paragraph; https://library.slmath.org/books/Book44/files/08psh.pdf . The inspected passages cover nonsimple orders, both radical cases, multiplier integrality and complete kernel lifting.
COMPARISON: Published multiplier theory and audited L080 already identify the entire order and its basis; L078 supplies a full-table/original-H verification precedent. The missing task is exact construction for the changed lattice, with independent complete field verification, not a new multiplier theorem or another strictness audit. The citation supplies no fixed runtime guarantee or instance table.
GAP: No essential theorem coverage is missing for this fixed implementation. All new table coefficients, actual identity, full two-way transports and inclusion/index witnesses must still be constructed and verified within the two caps; feasibility is unproved.
REASON: Approve only the stated known-method implementation after this separate exact-scope comparison. No new mathematical result, table, maximality verdict or executable evidence is produced in this literature turn.
SCOPE: Full L067 field with original H=343h; L077 original basis/transports; L078 entire changed-order table/transports; audited L080 multiplier basis m_0,...,m_46,m_47/2 and index two. No new prime, iteration, maximality test, trace/discriminant calculation, units/classes or descent assertion.
LITERATURE_REASON: The proposed target changes from L080's strictness verdict to the new multiplier's multiplication table, explicitly outside the prior audit scope; reuse ready general source coverage but compare this exact implementation obligation before research.

## Proposed scope and decision test

The main gap remains arbitrary-curve rank equality at analytic order at
least two. The nearer arithmetic gap on the retained explicit-descent
route is complete global arithmetic, including units/classes; no claim
is made that a single local correction closes it. A fully certified
table would permit a subsequent local maximality test on the actual
changed order. No maximality test is performed or approved here.

Essential retained inputs are L067's exact full degree-48 field,
L077's original-H order identification, L078's changed-order transports
and full table, and L080's audited multiplier basis and index two.
History/305 confirms that no new table or further correction was supplied.
Step 320 checked subsequent histories and targeted local claims; no
completed new multiplier table was found in that checked scope. Existing strictness
proofs are imported, not rederived. L079's 31-maximality is background,
not an assumption that supplies a table or a verdict at two.

The intended finite test requires every product of the 48 basis elements
to have certified integral coordinates and independent equality in the
original H field, together with complete two-way rational transports,
identity and index-two agreement. Stop on any missing input, failed
identity or either stage cap, preserving evidence without retries or
iteration. The exact production/verification schedule and coverage are
approved in the separate step-320 comparison below. No new mathematical derivation or script is
part of this proposed assessment.

Keep ATTEMPTS/041's stopped ideal-power evidence and ATTEMPTS/042's
repeat-audit stop. This proposal uses the already certified multiplier
lattice, not the stopped power expansion or a repeated source approval
for L080 itself. Global maximality, all other index primes, complete
units/classes, full descent and any general rank comparison remain
unresolved. Full matching Mathlib coverage is not checked.


## Separate exact-scope comparison — step 320

The source applies to a full order in a number field and a nonunit prime;
it does not require a monogenic order or an odd prime. Lemma 6.4 uses a
nonzero finite module preserved by the candidate multiplier. Section 9
handles both zero and nonzero radical and computes the multiplier through
the full I/pI action, with integral kernel lifts. Proposition 9.3's proof
covers strictness and its equality criterion. These results are imported;
L080 already supplies their fixed application. This review neither
rederives that mathematics nor extends the stopping criterion.

L078 and L080's relevant full proofs were compared, including the original
scale 31 and actual identity, and L077's complete-product verification
range was read. The existing `changed-order-two-303/verify.py` input-table
check reads `radical-overorder-295/product-ii.json`: it verifies R, not R⁺.
Its `decision.json` contains the multiplier basis, inverse, identity and
index but no new products. Thus rerunning that verifier would not close
the proposed obligation. No supplied certificate was mathematically
replayed in this literature review. The scoped code read establishes the
interface distinction, not the correctness of a future program.

Approve one production stage of at most 180 seconds followed by one
independent verification stage of at most 180 seconds. Include input
validation and report writing within each stage. Retain the existing
134217728-byte combined artifact limit, including code, logs and reports.
Save unfinished notes before execution, write full certificates to a new
notebook-local directory, and preserve original inputs. No retry,
continuation after a cap, representation change during the run, or
additional correction is approved.

Production must retain all 48 basis representatives, both complete
rational transport matrices to the original H power basis and L067's
coordinate algebra, their inverses, the actual identity, and all 48³
integer product slots including zeros. Use exact arithmetic and retain
all denominator factors; the original scale 31 is not replaced by the
new enlargement denominator two. The entire L080 lattice must match,
with integral old-order inclusion and exact index two. Do not assume
that the first coordinate vector represents one.

Independent verification must reconstruct the input basis from canonical
L067/L077/L078/L080 data, check every transport entry and both inverse
products, every integer coefficient and every ordered product equality
in Q[T]/(H), and identity multiplication on both sides of every basis
element. Polynomial remainder checks must cover all coefficients with
exact rational arithmetic or justified denominator clearing; no unproved
exact divisibility shortcut is licensed. All 110592 product slots are
required. Verify inclusion/index and agreement with L080's actual lattice,
not merely closure of some index-two lattice. An independent polynomial
remainder verifier may check a table produced by transported arithmetic;
shared unchecked producer routines do not provide independent evidence.
These are verification obligations, not computations performed here.

Success supplies this one explicit order table for a possible later local
maximality test. Any missing input, nonintegral product, failed identity,
missing slot or cap stops this attempt with full failure evidence, without
iteration. Such failure concerns this certificate schedule; it does not
refute the imported theorem. ATTEMPTS/041's ideal-power expansion and
ATTEMPTS/042's repeated-approval stop stay preserved. The new table target
uses the already audited lattice after the independent local-data route;
it does not resume either stopped execution.

The external searches also returned Voight's *Orders* chapter (Springer,
2021) and an older Stevenhagen author preprint. These are unread leads,
not additional theorem evidence; no essential reliance on them is needed.
Full matching Mathlib coverage remains unchecked. The next work is
RESEARCH / REPRODUCTION / implementation using this SPECIALIZE coverage.
This source comparison makes no progress beyond the checked mathematics
and leaves global maximality, complete units/classes, descent completeness
and arbitrary-curve analytic-order/rank equality unresolved.
