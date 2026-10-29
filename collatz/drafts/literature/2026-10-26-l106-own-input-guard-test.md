# L106 fixed tuple — own-input guard test source assessment

TARGET: Test whether L106's fixed endpoint tuple satisfies all25 own-input J and H guards, by certifying one violated guard or all50 inequalities.
CHECKED: 2026-10-26
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step507 searched Collatz rational cycles affine fixed point inequalities Halbeisen Hungerbuhler and Collatz "9250231" guards; scoped duplicate checks read L106 construction, L105 hypotheses, L055 table, Attempt032/033 and searched the step504/506 histories and working notes. Reused step503/505 discovery and stronger-cycle comparisons; no matching guard verdict inspected and no novelty inference.
SOURCE_EVIDENCE: Reopened Halbeisen–Hungerbuehler (1997), section2 equations(2)–(4), Lemmas1/2 and printed induction pp.228–229; NIST DLMF4.6.4 and4.2.19, version1.2.8. Reused step503/505 and step485 finite-remainder, outward-rounding and exponential-majorant coverage with its stated restrictions.
COMPARISON: Known finite-affine and positive-real enclosure methods cover this finite test, but no inspected source supplies its verdict. L106 supplies the audited tuple and lower domains, not the guards; L105's triangle omits this positive row2 budget, and L055's full-guard witness has different H data and tails.
GAP: No essential source gap remains for exactly TARGET; original-index guard operands and rigorous bounds remain to be calculated in a separate research turn. Full matching Mathlib coverage is unchecked.
REASON: Approve exactly TARGET as a bounded RESEARCH/REPRODUCTION calculation using existing affine and enclosure machinery; this review supplies source readiness only and no guard verdict.
LITERATURE_REASON: Step506's saved continuation added previously unassessed own-input guards to the endpoint-only scope, requiring this separate comparison; no repeated review of an unchanged ready target.
SCOPE: Only L106 tuple(8) at its fixed allocation, with all original chronological inputs, all endpoints and closure, and exactly the J/H inequalities below; no support extension, minimum, seed, realization or primitive-period premise.

## Gap, target and decision test

Universal descent remains the main gap. This intermediate test asks if
one endpoint-only witness survives the omitted necessary real-system
guards. A failed guard parks this particular stronger-witness route;
all50 passes strengthen the real-system obstruction to exclusion methods.
Neither outcome gives integer realization, support/order exhaustion,
entry, unrestricted cycle exclusion or control of divergent trajectories.
An inconclusive interval gives no verdict. This is an independently
testable target, not a revival of the false endpoint-only cap.

## Primary coverage and applicability

Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational
Collatz cycles*, Acta Arithmetica78 (1997),227–239,
DOI10.4064/aa-78-3-227-239,
[Lemma2, pp.228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf):
read section2 definitions, recursion and concatenation identity, plus
length-one and appended-zero induction cases; appended-one is printed
as analogous. For a nonempty binary word it gives real affine
composition and its rational fixed point. Import the composition method
only. L106's shifted blocks need their local coefficient matching;
its audited construction already supplies that matching. Lemma1's
rational-cycle interpretation is not imported into this real relaxation.
A fixed point alone does not certify these extra inequalities. No general
coding reproof is needed and no new coding claim is proposed.

[NIST DLMF4.6.4](https://dlmf.nist.gov/4.6.E4), version1.2.8,
requires Re(z)>=0,z!=0. Its positive-real instances support logarithmic
enclosures after positive arguments are checked. The series alone is
not a finite numerical certificate: reuse the previously assessed
finite remainder and outward rounding, retaining coefficient amplification.
[DLMF4.2.19](https://dlmf.nist.gov/4.2.E19) gives the entire exponential
series; reuse the prior positive-small-argument majorant assessment,
including x<1 where a geometric upper bound is used. L104's audited
Lambda enclosure may be reused only for exactly its K,N operands;
it does not enclose arbitrary prefixes or any guard margin by itself.

The step503 stronger-cycle comparison is unchanged: its inspected
Simons–de Weger inputs require integer-orbit/minimum hypotheses absent
here. Knight's full high-cycle theorem remains an unread, nonessential
lead, not an input. The exact-integer search found unrelated and
unverified material, none imported. No essential source blocker remains.
The already checked MathPrize universal target is unchanged. No
cross-notebook input is used; full matching Mathlib coverage is unchecked.

## Duplicates and recorded failures

L106 establishes endpoints, closure and lower domains, with a row2
lower bound only. It explicitly omits the guards. The searched step504
and step506 records supply no completed guard verdict. L105 assumes
b2=...=b23=0, so its exclusion and fixed-prefix cap cannot decide this
tuple. L055's original-H full-guard witness uses H0=40,H24=32670621
and different tails; its margins cannot transfer. Reuse its method only.
Attempt033 refutes the endpoint-only cap, without claiming feasibility
of the full real system. Attempt032 fails a sufficient support package;
that failure is not a necessary-guard violation or feasibility proof.
Preserve both attempts, original-H witnesses and unfinished work.

## Approved bounded continuation

Inputs: audited L106 tuple(8), L055 literal25-row table, L104 audited
enclosure at K=397573379,N=630138897, and L105 guard definitions only.
Fix r25,d35,H0=5,H24=32670656,kappa=23/11,B=9250245,
b0=b1=1,b2=12,b24=9250231,other budgets0,a_i=2+18b_i.
Retain the same original tuple throughout. At each original input test
4J_i log2 <= log s_i + log(11/4) and
H_i log2 < log s_i + J_i log(27/16).
The first is non-strict, the second strict. A certified strict failure
of the first, or certified failure including equality of the second,
suffices to reject this witness. Success requires all50 rigorous
inequalities with their proper strictness. Inconclusive bounds settle
neither branch; do not report rounded equality as exact equality.

All25 endpoints, closure and lower domains are established inputs;
no minimum, seed, integer/residue junctions, valuation realization or
primitive period is assumed. Repetitions remain allowed. Keep full
load-bearing bounds in a canonical result if the test produces one,
with a complete certificate if using scripts; a preview is not proof.
No guard calculation, certificate replay, new lemma or mathematical
script was produced in this literature-only step. It approves one
separate calculation; no further literature is essential for this scope.
