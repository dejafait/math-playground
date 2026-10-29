# Positive row0/row1 full-support row2 test — source scope approved

TARGET: Test whether every closed endpoint tuple in the literal d35 real system with s_i>=540/11, nonnegative integer budgets summing to 9250245 and b0,b1>=1 satisfies s2<(4/11)*2^112 when b2,...,b24 are unrestricted.
CHECKED: 2026-10-26
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step503 ran the five focused queries below and scoped duplicate/failure searches in L10*/C10*,L055,L065,L076,L084,L098,the cited assessments and Attempt032; no inspected matching full-support endpoint-only cap identified. No novelty inference.
SOURCE_EVIDENCE: Reopened Halbeisen–Hungerbuehler (1997), section2 definitions/equations(2)–(4), Lemmas1/2 and printed induction pp.228–229, section3 Lemma4 with complete exchange proof and Lemma5 statement p.230; rechecked MathPrize. Read L055 table/root,L105 proof/audit,L104 enclosure/audit passages,L103 guard-conditioned cap,L065 witness scope and Attempt032; reused step495/487/467 analytic and stronger-cycle coverage. Knight publisher preview inspected only for scope; full theorem unread and not imported.
COMPARISON: Finite-affine/enclosure methods cover an exact-root test with arbitrary tails, not an inspected matching verdict. L105 fixes rows2–23 to tail2; L103's arbitrary-tail cap assumes omitted J guards; C103a assumes b0=0; C104a fixes b1=...=b23=0. Minimum/integer-cycle results do not supply this designated-input endpoint-only cap.
GAP: No essential method-source gap remains for exactly TARGET; matching shifted blocks/totals/denominator and controlling every arbitrary-tail prefix, or certifying a complete endpoint/lower-domain counterexample at the threshold, remain mathematical obligations.
REASON: Approve exactly TARGET for one separate RESEARCH/REPRODUCTION attempt specializing assessed finite-affine/enclosure machinery; no enlarged cap, monotonicity or counterexample established in this literature turn.

LITERATURE_REASON: The saved REVIEW_REQUIRED target removes L105's tail2 restriction on rows2–23 and omits all J/H guards; essential changed-domain comparison required this separate literature-only step.
SCOPE: Exactly TARGET in L055's chronological25-row table except H0=5,H24=32670656; B=9250245,kappa=23/11,a_i=2+18b_i,all25 endpoints,closure,s_i>=540/11,nonnegative integer b_i,sum b_i=B,b0,b1>=1. No J/H guards,minimum,seed,integer-junction,residue,actual-word or primitive-period premise; closing tail2,coincident values and repetitions retained.

## Proposed scope and discriminating test

This preserves step502's proposal. Its pending-review wording is
superseded by step503 below; TARGET is unchanged.

Main gap: universal descent. The intermediate target asks whether the
row2 necessary-guard mechanism extends beyond the audited triangle.
A positive result could exclude all positive-row0/positive-row1 supports
in this literal order. A counterexample would reject that uniform cap
and direct work toward different guards or support subdivisions. Neither
outcome alone settles the remaining row1-zero supports, other orders,
entry, unrestricted cycles or divergence.

Essential proposed inputs are L055's complete literal table only,
L105's shifted endpoint and cut2 machinery and audited L104's enclosure
only after checking unchanged totals. C105a supplies the actual-word
boundary case, not a premise for a stronger real-system claim. L041
would be needed for a later actual-word application, which is outside
this test. Keep the precise primary citations/qualifications already
recorded in L105 and the triangle assessments; inspect any newly
essential source case separately. Full matching Mathlib is unchecked.

Fix r=25,H0=5,H24=32670656 and all other literal J,H unchanged.
Let all b_i be nonnegative integers with sum b_i=9250245,b0,b1>=1,
a_i=2+18b_i. Retain every equation
s_(i+1)=2^(-a_i)*(G_i*s_i-Q_i)+23/11, with
G_i=(27/16)^J_i*(3/2)^H_i,Q_i=(12/11)*(3/2)^H_i+1,
closure s25=s0 and all lower domains s_i>=540/11.
Do not assume the J/H guards in the proposed endpoint-only bound;
its threshold is precisely row2's necessary J28 guard. No minimum,
seed, integrality, residue, actuality or primitive-period premise is
allowed. Closing tail2 and coincident values remain in scope.

The changed support removes the fixed-tail2 hypothesis on rows2 through23
used in L105's geometric-prefix estimate. The next review must compare
this exact difference with known finite-affine results and recorded
failures, including Attempt032; it must not silently reuse that estimate.
Continue only with source-ready coverage and a concrete uniform-bound
proof test or exact counterexample search. A counterexample must satisfy
all25 endpoints, closure and lower domains and have s2>=(4/11)*2^112;
it would refute this bound, not establish any actual Collatz word or
feasibility of all guards. Preserve both d0 witnesses and unfinished work.
No new mathematics has been derived or approved for this target.

## Separate source comparison — step503, 2026-10-26

Universal descent remains the main gap. The proposed cap could support
a later exclusion of positive-row0/row1 supports in this literal order;
a counterexample would reject this cap and motivate another guard or
support subdivision. Neither settles row1-zero supports, other orders,
entry, unrestricted cycles or divergence. No estimate, allocation test,
mathematical script or certificate replay was performed in this review.

### Discovery and primary coverage

Queries actually run:

- `Collatz rational cycles affine fixed point prescribed parity vector upper bound all permutations`
- `Collatz "9250245" "row2"`
- `Collatz cyclic affine recurrence tail allocation prefix bound`
- `"Collatz high cycles do not exist" theorem pdf`
- `Collatz prescribed parity word fixed coordinate upper bound positive real cycle affine prefix`

The bounded search returned finite-affine, general parity-word material
and the high-cycle lead below; no matching literal-domain cap was
inspected. Other repositories, 2-adic, stochastic-tail and claimed-proof
discussions were not imported. Search absence is not novelty evidence.

Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational
Collatz cycles*, Acta Arithmetica78 (1997),227–239,
DOI10.4064/aa-78-3-227-239,
[section2 equations(2)–(4), Lemmas1/2 pp.228–229; Lemmas4/5 p.230](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf):
Lemma2 gives finite real affine composition and its fixed point for a
nonempty binary word, with denominator 2^length-3^ones. Inspected the
recursion, concatenation identity, length-one and appended-zero proof;
appended-one is printed as analogous. Import finite composition only;
shifted-block applicability and denominator sign need local checks.
Lemma1 supplies no integer-junction premise. Lemma4 requires distinct
equal-length/equal-one-count words and prefix-one-count domination at
every position; its finite exchange proof orders scalar numerators.
No such binary-word comparison is established here. Lemma5 controls
the greatest cycle minimum over those words, not a prescribed row2
input. Neither supplies TARGET by citation. No coding reproof is needed.

Reuse primary analytic inspection in
`2026-10-25-d35-row0-row1-row24-feasibility.md`,
`2026-10-25-d35-row0-row24-edge-family.md` and
`2026-10-25-d35-last-three-tail-feasibility.md`:
[NIST DLMF4.6.4](https://dlmf.nist.gov/4.6.E4),
[4.5.8–4.5.11](https://dlmf.nist.gov/4.5) and
[4.2.19](https://dlmf.nist.gov/4.2.E19), recorded version1.2.8.
The log series requires Re(z)>=0,z!=0; exponential inequalities require
real nonzero x, with x<1 for the geometric upper majorant. Establish
the positive arguments and small positive Lambda before use. Reuse
L104's audited enclosure only after exact K,N matching; it does not
bound arbitrary prefixes. Retain finite remainders, outward rounding
and full coefficient amplification. No new enclosure, analytic reproof
or fresh DLMF version check is claimed.

Reuse step467/495's inspected Simons–de Weger, *Theoretical and
computational bounds for m-cycles of the 3n+1-problem*, Acta
Arithmetica117 (2005),51–70,
[sections1.2,2.1–2.2, Lemmas4/6/7 pp.52,56–59](https://www.impan.pl/shop/en/publication/transaction/download/product/82263).
Its integer-orbit minima partition and global-height hypotheses are
unavailable; its number of minima is not automatically25 or an allocation
budget. No conclusion is imported or computational hypothesis strengthened.

New nonessential lead: Kevin Knight, *Collatz high cycles do not exist*,
Discrete Mathematics349(3) (2026),114812,
[publisher abstract and section previews](https://www.sciencedirect.com/science/article/pii/S0012365X25004200),
DOI10.1016/j.disc.2025.114812. The inspected scope concerns a designated
extremal rational cycle and an exclusion of integer high cycles;
section4's preview restricts its definition to coprime counts and positive
cycles. This is not an arbitrary designated real coordinate bound.
Direct retrieval returned403; the indexed primary preview was readable,
while HAL manuscript hal-04261183 was access denied. Full theorem/proof
remain unread and no theorem or formalization claim is imported. This
lead is not needed for the finite-affine test; no essential source blocker
or further dependent source review is recorded.

The [MathPrize statement](https://mathprize.net/posts/collatz-conjecture/),
page dated2021-07-07, was reopened: every positive integer reaches1
under even halving and odd3n+1. This agrees with the target; adjudication
supplies no premise. Full matching Mathlib coverage is unchecked,
not known absent. No cross-notebook input was read.

### Duplicate and failure boundaries

L105's statement, cut2 proof and audit fix b2=...=b23=0. Its first23
reciprocal-prefix estimate uses this restriction; the last-two-prefix
identities alone supply no enlarged cap. No replacement growth or
monotonicity claim is derived here. C105a's audited actual-word transfer
does not enlarge this domain. C104a fixes b1=...=b23=0; C103a assumes
b0=0; L104 fixes one edge allocation; L098 changes H0/H24. None is TARGET.

L103's complete “Cyclic cap with arbitrary later allocations” passage
uses own-input J guards at rows1–24 to bound its logarithmic summands.
Those guards are omitted here; neither its cap nor its consequent prefix
comparison may be imported. The lower domain does not replace them.

L055/L065's hypotheses, conclusions and relevant root/witness passages
retain original H0=40,H24=32670621 and different supports. They are real
witnesses in their own scope, not counterexamples at d35 with b0,b1>=1.
Attempt032's complete WHY IT FAILS rejects a sufficient fixed support
package for d>=5; this supplies neither feasibility nor failure of TARGET.
An exact-root/lower-domain test is independently testable and does not
retune that package. Preserve both d0 witnesses and all unfinished work.

### Approved bounded continuation

SPECIALIZE covers one separate RESEARCH/REPRODUCTION attempt on exactly
TARGET using assessed finite-affine/enclosure methods. Proposed inputs
are L055's literal table, L105's shifted endpoint/cut2 machinery and
L104's audited enclosure after total matching. C105a is boundary evidence,
not a premise for a stronger cap. No enlarged theorem is approved here.

Match shifted blocks and denominator, retain every original endpoint and
closure, and account for every arbitrary-tail prefix. Do not extend
L105's fixed-tail2 estimate or use L103's omitted-guard cap. Cover the
entire integer simplex, including zero later budgets and b24=0, with no
minimum, seed, actuality or primitive-period premise.

Continue with either a uniform proof of s2<(4/11)*2^112 or an exact
allowed allocation and closed endpoint tuple certifying all25 lower
domains and s2>=(4/11)*2^112. Positivity alone is insufficient for the
lower domain. A witness need not satisfy the omitted guards: it refutes
this cap only, not Collatz or full-guard infeasibility. Samples and failed
sufficient estimates establish neither verdict. If inconclusive, save
the precise unproved comparison and reassess within the exploration rules.

Completed LITERATURE/EXPLORATION/NOVELTY_UNCHECKED: source coverage is
ready, with no new cap/counterexample or result beyond inspected sources.
Mathematical exploration usage remains0; the independent gaps persist.
