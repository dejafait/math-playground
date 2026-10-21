# Literal d=5 survivor H test — source comparison

TARGET: Test whether both literal d=5 endpoint roots at t=0,1 violate their own-input row18 H guard using L084's independent H data.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused step 330's five-query affine/prefix/own-input search and step 334's four-query fixed-table/stronger-result comparison; scoped searches of L080–L087, H/d5 assessments and histories 330–353 found the d=1 root results and d=5 proposals/reductions, not a completed independent d=5 fixed-root H application; read Attempt 032.
SOURCE_EVIDENCE: Inspected L077 hypotheses and proof (7)–(12), L083 statement/proof (6)–(9) and its critical audit, L084 independent H data and complete all-member audit, L055 table and L081/L082 exact scopes; reused assessed Halbeisen–Hungerbuehler (1997), section 2 equations (2)–(4), Lemma 2 pp. 228–229 and DLMF 4.5.1/4.6.4/4.2.19.
COMPARISON: L083 as stated requires every C077a O/S/C test and cannot be invoked at d=5; its fixed-root cap/margin proof precedes the separate all-order reduction, while audited L084 already supplies independent d=5 H data. Specializing that proof case requires an explicit premise check, not a new certificate search or the failed conjunction.
GAP: A later mathematical step must justify the restricted use of L083 (6)–(9) from L077's independent endpoint formulas and L084's H data, then match both fixed roots to the existing row18 upper expression; no root verdict is derived in this review.
REASON: Coverage is ready for one separate RESEARCH/REPRODUCTION specialization at exactly TARGET; reuse existing affine formulas, analytic bounds and audited finite data, proving only the omitted-reduction applicability difference.
SCOPE: Only the literal d=5 table r=25,B=9250245,H_0=35,H_24=32670626, other L055 pairs unchanged, early b_i=0,b_23=t,b_24=B-t,a_i=2+18b_i, separately t=0,1, with every cyclic endpoint retained; no order/support/cutoff assembly or actual-word conclusion.
LITERATURE_REASON: The saved REVIEW_REQUIRED target omits the full C077a conjunction assumed by L083 and asks about two already specified roots; that changed hypothesis needs this separate proof-case comparison before mathematics.

## Original proposal retained from step 353

The proposal below records the earlier pending scope. Its instructions
for a future literature review and pending-readiness language are
superseded by the separate step-354 comparison below.

The main gap remains universal eventual descent. The intermediate target
is confined to the two fixed literal endpoint roots for r=25,B=9250245,
H_0=35,H_24=32670626 and every other L055 pair unchanged. Set early
b_0=...=b_22=0,b_23=t,b_24=B-t,a_i=2+18b_i, separately at
t=0 and t=1. Retain all endpoints including closure and test the strict
own-input guard
H_18 log2 < log s_18 + J_18 log(27/16).
No minimum, seed, integer/parity/valuation realization, order reduction,
or successful full C077a conjunction may be assumed.

Essential prospective inputs are L055,L077,L083,L084. L086 and audited
L087 motivate a possible later literal-allocation reduction only; they
are not assembled here and do not establish feasibility of either root.
A negative H margin could supply a survivor obstruction for that later
reduction. Cyclic-order reduction, actual-word transfer and universal
eventual descent would still require separate work.

The next invocation is literature-only: compare the exact target with
ready source assessments and canonical proof cases, check relevant
duplicates and Attempt 032, and classify the application before any
calculation or new lemma. Do not repeat primary browsing if existing
coverage suffices. In particular determine which parts of L083's cap
argument require the full reduction and which can be applied to a
specified root. The H cap uses its actual L_*, and its incoming-prefix
and denominator-exponent bounds use different parameter endpoints;
neither may be replaced silently by the C package.

Continuation test: after separate approval, require a rigorously matched
nonpositive upper bound for the row18 H margin at both specified roots,
with every cap and sign hypothesis justified independently. A missing
premise or inconclusive/positive bound stops that fixed test without a
feasibility inference or automatic tuning. Attempt 032 and both original
d=0 witnesses must remain intact. Full matching Mathlib coverage is
unchecked. No cross-notebook input is proposed.

## Separate source comparison — step 354, 2026-10-20

The main gap remains universal eventual descent. The intermediate target
is exactly TARGET. A negative own-input H verdict for both specified roots
could later complement L086's literal early-support reduction and L087's
last-pair cutoff. No assembly, cyclic-order reduction, actual-word transfer
or universal-descent argument is attempted here. This is a literature-only
EXPLORATION, not a new mathematical exclusion.

### Reused primary coverage

Reuse the adequate discovery and primary inspections in
`2026-10-18-variable-table-uniform-h-survivor-test.md`, its critical-audit
assessment, and `2026-10-19-h-transfer-family-sufficient-tests.md`.
The target changes the local reduction hypothesis, not the finite-word
or analytic machinery, so no repeat external browsing is needed.

The published input is Halbeisen–Hungerbuehler, *Optimal bounds for the
length of rational Collatz cycles*, Acta Arithmetica 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239, [section 2, equations (2)–(4), Lemma 2,
pp. 228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
The reused inspections include the nonempty binary word hypotheses,
numerator recursion, length-one and appended-zero proof cases; appended
one is printed as analogous. Import only the formal affine map and
nonzero-denominator fixed-point identity. L077 provides the existing
coordinate specialization; positive Lambda must still be matched.
No general coding reproof or parity-realization converse is justified.

Reuse NIST [DLMF 4.5.1](https://dlmf.nist.gov/4.5.E1) on real
x>-1,x!=0, [4.6.4](https://dlmf.nist.gov/4.6.E4) on Re(z)>=0,z!=0,
and [4.2.19](https://dlmf.nist.gov/4.2.E19), with the assessed positive-real
log/exp facts and rational remainder method. The actual positive arguments
and Lambda in L077/L084 are within scope. The reused assessment records
version 1.2.8; no current release was independently checked here. Import
audited enclosures with amplified errors, without rerunning their scripts.

The ready comparisons of the paper's Lemmas 4–5/Corollary 1 and the
inspected Christoffel preprint distinguish scalar prefix ordering and a
minimum over rotations from a bound at a prescribed outgoing row. They
do not supply the missing own-input statement; no preprint claim is
imported. Unread references remain nonessential. Reuse the unchanged
ordinary-map target and shortcut equivalence from the recorded primary
MathPrize inspection. Full matching Mathlib coverage is unchecked, not
absent; no Lean verification is claimed.

### Exact local comparison and remaining proof obligation

Read L077's hypotheses and endpoint proof (7)–(10), L083's hypotheses,
cap/margin proof (6)–(9) and corresponding audit cases, and L084's
independent C/H construction, failure list and complete all-member audit.
L055 supplies unchanged indexed pairs. L081/L082 explicitly concern
H_0=39,H_24=32670622: their verdicts are d=1 benchmarks, not a d=5
theorem. Scoped searches found no completed d=5 H application; this
limited search is not evidence of novelty.

L083's theorem explicitly assumes every independent O/S/C test. L084
records the actual d=5 row0 S failure, so citation of that theorem's full
conclusion would be invalid. Its proof separates incoming data and cap
(6)–(8), own-input margin (9), and a later all-order/full-allocation
reduction using C077a. The later mathematical step may specialize the
first two proof cases only after explicitly checking their premises
independently. Thus SPECIALIZE, rather than IMPORT of L083's theorem,
is appropriate. No restricted implication is proved by this review.

The existing data are L084 (1), (2), (5), (6), (9) and its audit sections
“Separate C/H packages and closure” and “Uniform H and application
matching.” They record the complete H package at m=1, actual L_*=1,
complete finite reciprocal sum, and H cap failures confined to
d=34,...,37. The d=5 H cap is therefore covered by the audited all-member
data, not displayed (7)'s d<=4 estimate. The audit separately verifies
all incoming factors, both changing tails, positive Lambda, exponential
threshold and all 925 rational H values. This review relies on canonical
audited evidence, not a certificate preview or stored success flag;
it performs no independent re-audit.

For the later specialization use L077's independent endpoint formulas
and positive-eta bounds, with its (3) data from L084. Use L084's H
constants and incoming data at m=1, not C's t=2 package. L083's proof
cases identify two different parameter choices: incoming lower bounds
use the largest tested parameter; the H upper expression uses the
smallest denominator exponent at t=0. The remaining proof obligations
are to check these comparisons for the specified roots, justify the cap
and margin without O/S or C077a, and match row18 to L084 (9).
No new root construction, certificate tuning or analytic reproof is
needed. The closing C_25 stays in the fixed-point denominator; only
C_0,...,C_24 receive incoming bounds. No closing-row growth or minimum/
seed at row0 is available.

Attempt 032 remains a stop for the failed full conjunction. This target
fixes literal order and both allocations in advance; it does not infer
that arbitrary feasible allocations reduce to them. Both d=0 witnesses
and recorded arithmetic stops remain intact. L086/L087 motivate later
use only, not premises of this H test. No cross-notebook input or
integer-cycle/realization premise is proposed.

### One bounded continuation after separate approval

Retain exactly TARGET, essential inputs L055,L077,L083,L084. A later
RESEARCH/REPRODUCTION attempt should import identities and audited data
and justify only the restricted applicability. Require a rigorously
matched nonpositive rational upper row18 H margin at both roots, keeping
the strict margin comparison and every cyclic endpoint. No verdict on
either root follows from this review. A missing premise or inconclusive/
positive bound stops this fixed test without feasibility inference or
tuning. No other table, order/support assembly, integer test or actual-
word application is covered. Newly ready coverage receives separate
supervisor approval next turn. No lemma, mathematical script, DAG or
PROOF argument is changed by this literature step.
