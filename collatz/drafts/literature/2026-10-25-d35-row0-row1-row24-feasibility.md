# d35 row0/row1/row24 support — source scope approved

TARGET: Determine feasibility of the literal d35 real system on b0=m,b1=u,b24=B-m-u, all other budgets zero, for integers m,u>=1 and m+u<=B=9250245.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step495 searched active lemmas, assessments, histories488/490/494 and ATTEMPTS for row0/row1,b0=m,b1=u and {0,1,24}; web queries Collatz "9250245" "row1" and Collatz rational cycles prescribed parity word prefix domination affine fixed point Halbeisen Hungerbuhler supplied no inspected matching verdict. Reused step487/483/467 discovery; no originality inference.
SOURCE_EVIDENCE: Reopened Halbeisen–Hungerbuehler (1997), section2 equations(2)–(4), Lemmas1/2 pp.228–229 and section3 Lemma4 with complete exchange proof p.230; rechecked MathPrize. Read L055 table/root/enclosure,L104 shift/root/enclosure,C104a parameter/root proof and audit evidence,L098/C103a hypotheses,L065 witness scope/enclosure and Attempt032. Reused ready step487/467 DLMF and stronger-cycle comparisons.
COMPARISON: Finite-affine and positive-real enclosure methods cover this support specialization; the cited prefix-order theorem compares scalar numerators under additional prefix hypotheses, not all guards. C104a fixes u=0,C103a assumes b0=0,L104 fixes m=1,u=0,and L098 changes H0/H24; none supplies the interior verdict.
GAP: No essential source gap remains for exactly TARGET. Changed shifted-block applicability, denominator matching, all parameter-dependent reciprocal prefixes and a uniform violated necessary guard or fully certified feasible tuple remain mathematical obligations.
REASON: Approve exactly TARGET for one separate RESEARCH/REPRODUCTION attempt using assessed finite-affine/enclosure machinery; derive only changed-support applicability and comparisons, without reproof of general coding or assuming C104a monotonicity.

LITERATURE_REASON: The saved REVIEW_REQUIRED continuation introduces positive row1 budget outside C104a's approved edge; this separate source comparison is required before dependent calculation.
SCOPE: Exactly TARGET in the original chronological 25-row L055 table except H0=5,H24=32670656, with kappa=23/11,a_i=2+18b_i,all25 C104a endpoint equations and closure,s_i>=540/11,own-input non-strict J/strict H guards,including m+u=B and repeated periods; no minimum,seed,integer junction,realization or primitive-period premise.

## Original proposal: exact scope

Use the original chronological 25-row L055 table, replacing only
H0=5 and H24=32670656. Use precisely C104a's real-system domains,
all25 endpoint equations, closure and own-input non-strict J/strict H
guards, with kappa=23/11 and a_i=2+18b_i. Replace only its budgets
by b0=m,b1=u,b24=B-m-u, all other budgets zero, for integers
m,u>=1,m+u<=B. The closing-tail2 boundary m+u=B is included.
No minimum, seed, integer-junction realization or primitive-period
premise is allowed. Coincident values and repeated periods are allowed.

The main gap is universal descent. The proposed intermediate target
tests the first three-recipient support adjacent to the audited
row0/row24 edge. A uniform exclusion would supply one additional
positive-row0 support input; a rigorously feasible real tuple would
instead limit that exclusion mechanism. Neither would supply an
actual Collatz cycle or an order/entry reduction. No result for this
support is asserted here.

Essential proposed inputs are L055's table, C104a's exact system and
finite-affine machinery, and L104's audited enclosure only after
checking its applicability to the new totals. C104b is motivation,
not a real-system feasibility input. L041 would be needed only for a
later separately scoped actual-word transfer. Preserve Attempt032's
failed sufficient mechanism, both d0 witnesses and unfinished work.

The separate review must inspect relevant prior support results,
including the different H-data qualifications noted for L098, and
reuse primary coverage where its hypotheses match. It must identify
whether the changed reciprocal-prefix dependence is already covered;
do not presume the one-parameter monotonicity of C104a persists.
No new estimate, analytic proof or script has been attempted here.

Continuation test: after source approval, seek either a proved
uniform violated own-input guard on the full integer triangle or an
exact certified real tuple satisfying every equation and guard. A
failed sufficient estimate is not a feasibility result; if the chosen
bound fails, record its failed premise and reassess rather than
claiming an exclusion. Other supports, ordering, entry, divergence
and universal descent remain independent gaps. Full matching Mathlib
coverage is unchecked. No cross-notebook input is proposed.

## Separate source comparison — step495, 2026-10-25

This review supersedes the proposal's pending-coverage wording above.
The exact target is unchanged. No new estimate, parameter identity,
monotonicity statement, feasibility verdict or mathematical script was
produced. Universal eventual descent remains the main gap. This support
test could supply a further restricted exclusion, or a real witness
limiting this relaxation; neither would give integer realization,
support/order exhaustion, entry or exclusion of divergent trajectories.

### Primary statements and applicability

Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational
Collatz cycles*, Acta Arithmetica78 (1997),227–239,
DOI10.4064/aa-78-3-227-239,
[section2 equations(2)–(4), Lemmas1/2 pp.228–229; Lemma4 p.230](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf)
was reopened at those passages. For a nonempty finite binary word,
Lemma2 gives its real affine composition and fixed point with denominator
2^length-3^ones. Read the numerator recursion, concatenation identity,
length-one and appended-zero induction; appended-one is printed as
analogous. Import formal composition only; the shifted blocks, cyclic
cut and denominator sign require local matching. Lemma1's odd-denominator
parity argument supplies no positive-integer junction premise here.

Lemma4 assumes distinct binary words of the same length and one-count,
and prefix one-count domination at every position. It strictly orders
their scalar numerators. Its complete proof exchanges the first differing
0/1 pair and iterates finitely, using the concatenation identity. Neither
its hypotheses nor its conclusion certify all designated own-input
guards. No such word comparison is assumed for the changed support.
This is reusable machinery, not a published verdict for this triangle;
there is no reason to reprove a general coding theorem.

Reuse the inspected positive-real analytic coverage in
`2026-10-25-d35-row0-row24-edge-family.md` and
`2026-10-25-d35-last-three-tail-feasibility.md`:
[NIST DLMF4.6.4](https://dlmf.nist.gov/4.6.E4),
[4.5.1](https://dlmf.nist.gov/4.5.E1),
[4.5.8–4.5.11](https://dlmf.nist.gov/4.5) and
[4.2.19](https://dlmf.nist.gov/4.2.E19), recorded version1.2.8.
The logarithm series requires Re(z)>=0,z!=0; log(1+x)<x uses x>0.
The exponential inequalities assume real x!=0, and the geometric upper
majorant needs x<1. Positivity and the relevant small-argument interval
must therefore precede any application. L055/L065/L104 already retain
finite logarithm remainder, outward rounding and full large-coefficient
error amplification methods. Their changed operands must be enclosed;
their numerical root/guard caps are not automatically reusable. No
fresh DLMF retrieval, version verification or analytic reproof is claimed.

Reuse step467's inspected stronger-result comparison with
Simons–de Weger, *Theoretical and computational bounds for m-cycles
of the 3n+1-problem*, Acta Arithmetica117 (2005),51–70,
[sections1.2,2.1–2.2 and Lemmas4/6/7, pp.52,56–59](https://www.impan.pl/shop/en/publication/transaction/download/product/82263).
Its integer-orbit minimum partition and global-height hypotheses are
unavailable in this real system. Its number of minima is neither the
budget m nor automatically25. It is a scope contrast, not an input;
inherited computational/Rhin/Crandall qualifications are not strengthened.

The [MathPrize page](https://mathprize.net/posts/collatz-conjecture/),
dated2021-07-07 and rechecked today, still states arrival at1 for every
positive integer under even halving and odd3n+1. This agrees with
foundations/01-target-and-scope.md. Adjudication supplies no premise.
Full matching Mathlib coverage remains unchecked; supporting affine or
logarithm facts are not a matching feasibility theorem.

### Duplicate and failure boundaries

The scoped local search identified the proposed target and its immediate
edge/fixed precedents, but no completed interior result. C104a's proof
uses a cut1 prefix pattern specific to b1=0; the later attempt must
replace, not silently extend, that comparison. L104's root cap concerns
only m=1,u=0. Its audited Lambda enclosure may be reused only after
matching the exact full exponent totals. C103a requires b0=0 and cannot
remove that hypothesis. L098 has H0=6,H24=32670655, so neither its signed
bound nor its guard margin transfers to H0=5,H24=32670656 by citation.
L055 and L065 are the two original-H d0 witnesses; they are neither
feasible tuples nor counterexamples at this target's changed table.

Attempt032's complete WHY IT FAILS records the failed sufficient row0
tail20 support datum for d>=5 and additional fixed-cap/order failures.
Those failures do not establish feasibility. This test asks for the
exact cyclic root on a specified support, rather than renewed invocation
or tuning of that failed package. Preserve its evidence, both d0
witnesses and all unfinished work. C104b and L041 concern a possible
later actual-word interpretation, not the present real-system verdict.

The two external queries returned general rational-cycle material and
the primary affine paper, with no matching verdict identified in the
bounded inspected scope. Other returned repositories, newer purported
formalizations and preprints were not inspected or imported; they are
unread leads, not essential inputs to the already covered method. No
claim of exhaustive search or novelty follows. No cross-notebook input
was read, and no essential source blocker was identified.

### Approved bounded mathematical continuation

SPECIALIZE now covers one RESEARCH/REPRODUCTION attempt on exactly
TARGET. Essential local inputs are L055's literal table and finite-root
method, C104a's exact real-system specification and audited edge as a
comparison, and L104's audited denominator enclosure subject to matching
totals. L065 supplies an enclosure-method precedent only. The new
support comparisons themselves are unproved; no edge exclusion is
being assumed to extend to the interior.

First match the shifted block coordinates and all25 original endpoints,
including closure, to the cited affine construction; justify the
denominator before division. Retain both subtractions inside tail
division and kappa outside. Track every changed reciprocal prefix at
the chosen cut, rather than assuming the fixed-prefix pattern or a
parameter endpoint extremum. Any reduction must cover the entire
integer triangle m,u>=1,m+u<=B, including m=u=1 and the full closing-tail2
edge m+u=B. Coincident coordinates and repeated periods remain allowed.

Continue this exclusion mechanism only with a rigorous uniformly
violated necessary own-input guard on the entire domain, or record an
honest partial region. For example row1's existing J1=15 threshold is
(4/11)2^60, but C104a's upper cap is not established here; another
original guard may instead discriminate. A feasible verdict requires an
exact root with all25 endpoints/closure, all25 lower-domain conditions,
all non-strict J and all strict H guards certified. Samples and failed
sufficient bounds decide neither. If the proposed uniform bound fails,
record that precise obstruction and reassess the test; a rigorous
feasible tuple would abandon exclusion by this unchanged relaxation for
this support without asserting a Collatz cycle. Other supports, order,
entry, integer realization and universal descent remain independent gaps.

Completed LITERATURE/EXPLORATION/NOVELTY_UNCHECKED: source coverage is
ready; no mathematical advance or result beyond inspected sources is
claimed. Literature work spends no mathematical exploration turn.
