# Simultaneous recovery — shared outside pair attempt

Work in progress on the unchanged EXPLORE-ready target in
`drafts/literature/2026-10-08-nine-union-simultaneous-recovery-count.md`.
Main gap: arbitrary sixteen-error equality. Intermediate test: couple
actual overlapping candidates whose outside triples share two labels,
using all common recovery equations. A new uniform restriction may help
exclude L045's twelve profiles; it need not settle the no-repeated-pair
branch. Continue on a justified simultaneous restriction, and abandon
the relaxed eleven threshold only with a verified twelve-candidate pencil.

Inputs checked: L010's kernel/distance and locator bound; L041 local
converse; audited L042–L043; L045's six-coordinate lift (still unaudited).
The earlier draft's five-row equation is rederived before use. No rational
original chart, universal finite lift, equality or pair existence is assumed.
Known-result comparison and failures reuse the supplied assessment and
ATTEMPTS/022; isolated per-tag degree summation remains parked.

Unfinished calculation saved before further work: for supports tagged b,b'
with outside triples S,S', write a_x(mu)f_S(x)=uW(x) off b and
its counterpart at nu. If S,S' share a pair, cancel that pair. Two untouched
z-labels force S=S'; then one untouched y-label forces mu=nu. The same
argument with two untouched y-labels rules out distinct candidates. Thus
the putative tags must be opposite singleton types. For tags y_i,z_j,
let y,z be the other singleton labels. Write S=R union {c},
S'=R union {e}, kappa=u/u', and
U(X)=(X-c)-kappa(X-e), V(X)=mu(X-c)-kappa*nu(X-e).
The common equations give U(z)=V(y)=0 and
qU(h)=pV(h), (1-r)U(d)=rV(d).
Subject to checking U,V nonzero and all denominators, this suggests
rq/((1-r)p)=(h-y)(d-z)/((h-z)(d-y)), which is not one.
The no-repeated-pair branch remains unresolved. No result is yet inserted
in the canonical argument; no mathematical script was run.

## Completion and decision

The calculation is now canonical in
[L046](../lemmas/L046-shared-outside-pair-recovery-obstruction.md), with
hypotheses, complete proof, qualifications and Mathlib status. The initial
shorthand above omitted the S=S' cases in which both y- or both z-labels
are tags; the canonical proof handles both using the common d equation.
It checks every slope and denominator and needs no full-weight or
near-twelve premise. Direct mathematical inputs are L010 and L043;
L045 remains application context, not a dependency of this result.

Outcome: ADVANCE, classification POTENTIALLY_NEW under the unchanged
saved EXPLORE assessment. This means a new local restriction relative to
the saved inputs, not certified novelty beyond all literature. No new
source review, mathematical script, finite witness or eleven bound was
produced. The constraint rules out the repeated-pair branch whenever
rq=(1-r)p, including an eligible universal lift and the E_*=0 case. In
general, repeated pairs can occur only across at most two disjoint tag
pair types; it does not bound the number of repetitions of each type.

The no-repeated-pair branch and candidates avoiding B remain open.
Continue on the same approved target by testing compatibility between
an overlap's cubic recovery and a B-disjoint support's recovery; retain
both j=11 and j=12 and do not assume that a disjoint candidate exists.
A useful discriminating result would exclude a remaining twelve profile
or impose a uniform simultaneous constraint not implied by the degree
budgets. Retain L010, L041, audited L042–L043, and unaudited L045–L046;
L044 is optional and unaudited. Universal extraction, other triple
patterns, independent audits and ABF26 identification stay unresolved.
The mathematical exploration count resets to zero on this ADVANCE.
