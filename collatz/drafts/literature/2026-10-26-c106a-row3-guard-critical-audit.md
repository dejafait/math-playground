# C106a separate critical audit — source coverage ready

TARGET: Critically audit C106a's fixed-tuple row3 J-guard failure, including its cyclic-prefix counts and exact bounds.
CHECKED: 2026-10-26
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step509 reused step507's exact-target discovery and stronger-cycle comparison; read C106a, L106 tuple(8)/identity(9), L055 table/guard conventions, L104 audited enclosure, Attempt034 and histories507/508; searched the specific working note and Attempt033 for duplicate guard/audit work. No independent C106a audit identified; no novelty inference.
SOURCE_EVIDENCE: Reopened Halbeisen–Hungerbuehler (1997), section2 definitions, equations(2)–(4), Lemmas1/2 and printed induction pp.228–229; NIST DLMF4.6.4 and4.2.19, displayed version1.2.8 released2026-09-15. Reused step507 and step485 finite-remainder/outward-rounding coverage and L104's recorded audited enclosure restrictions.
COMPARISON: The inspected sources cover finite-affine composition and positive-real enclosure methods, not C106a's cut3 indexing, changed operands, exact cap or guard verdict. L106 supplies the same tuple and all-cut identity; L104 supplies only the matching denominator enclosure. Separate arithmetic and hypothesis verification is still required.
GAP: No essential source gap remains for exactly TARGET; the critical audit itself remains undone. Full matching Mathlib and supporting coverage are unchecked; no integer-word realization is supplied.
REASON: Approve exactly TARGET for a separate RESEARCH/REPRODUCTION audit of existing machinery, preserving the fixed tuple and every closing term; no new guard/support investigation or general coding reproof is needed.
LITERATURE_REASON: Step508 introduced a new critical-audit continuation marked REVIEW_REQUIRED; this separate source comparison resolves that gate without repeating an unchanged ready assessment.
SCOPE: Only C106a on L106's unchanged tuple(8), literal25 table with H0=5,H24=32670656 and b0=b1=1,b2=12,b24=9250231,others0; L055 table/guard definitions, L106 identity(9), and L104 enclosure at K=397573379,N=630138897. No added minimum, seed, integrality, residue, realization or primitive-period premise.

## Gap and decision test

Universal eventual descent is still unresolved. This intermediate target
is to audit the reported failure of one necessary guard of one endpoint
tuple. Its downstream use is a reliable decision to park that fixed
full-guard witness, preserving L106's endpoint-only counterexample.
Continue to an audit verdict only if every load-bearing identity, count,
strict bound and own-input sign survives independent checking; a precise
defect requires correction or withdrawal of C106a's verdict. Inconclusive
evidence leaves it unaudited. Neither branch settles other allocations,
support/order exhaustion, entry, realization, cycles or divergence.

## Inspected primary coverage

Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational
Collatz cycles*, Acta Arithmetica78(1997),227–239,
DOI10.4064/aa-78-3-227-239,
[section2, Lemma2, pp.228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf),
gives the affine composition for finite binary words and the fixed-point
formula. Read the recursion and concatenation identity, length-one and
appended-zero induction cases; appended-one is printed as analogous.
Import only this composition machinery. Its rational-cycle interpretation
does not establish realization of these shifted real blocks. L106's
already audited coefficient matching and chronological tuple are local
inputs; the paper does not certify C106a's guard or cap. No general
coding theorem needs reproving.

[DLMF4.6.4](https://dlmf.nist.gov/4.6.E4) states the odd-power logarithm
series for Re(z)>=0,z!=0. L104's recorded audit uses positive arguments
2 and3, finite tails, outward bounds and full coefficient amplification;
an infinite-series citation alone would not certify its small difference.
Reuse that audited enclosure only after matching K,N exactly.
[DLMF4.2.19](https://dlmf.nist.gov/4.2.E19) states the entire exponential
series. Reuse step507's assessed positive-small-argument majorant, whose
geometric upper estimate requires x<1; C106a claims the stronger
0<Lambda<1/2 regime. The separate audit must check those hypotheses,
strictness and all rational comparisons. DLMF version1.2.8,
release2026-09-15, was displayed on the reopened logarithm page.
No new bound or certificate replay was performed here.

## Reuse, duplicates and audit boundary

Step507's recorded searches include the exact allocation and standard
rational-cycle/affine terminology; their scope still covers this narrower
audit. Reuse its stronger-cycle comparison: the inspected integer-cycle
results require hypotheses absent from this real relaxation. Knight's
full theorem remains an unread, nonessential lead. No broad rediscovery
or claim of literature originality is warranted. The already inspected
MathPrize universal target is unchanged.

Step508 and Attempt034 record construction and the pending audit, not
independent verification. L105's triangle omits the positive row2 budget;
L055's original-H witness has different data and its minimum/seed and
guard margins do not transfer. Attempt033 preserves the endpoint-only
cap refutation, which a failed extra guard does not undo. No such
failure proves anything about other supports. Preserve all these records.

The approved audit must check all25 cut3 terms as22+3; complementary
products c0*c1*c2,c1*c2,c2 against the full product; row24's actual
closing tail; the strict cap2300000000030429/14553; and row3's own
non-strict J3=52 requirement on the same original tuple. It must inspect
complete relevant certificate evidence if using it; passing flags or
previews are insufficient. The other49 guards remain untested and are
outside this audit. Repetitions remain allowed. No cross-notebook input,
new lemma, mathematical script, derivation or independent audit verdict
was produced in this literature-only step.
