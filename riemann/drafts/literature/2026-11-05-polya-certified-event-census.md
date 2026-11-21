# Exact Pólya pencil: proposed certified event census

TARGET: Assess source coverage for a certified census of L814's events on 0<x<=40 by isolating W=0 and testing F G<0 and W'!=0, retaining complete integral tails, the origin and upper edge, and unresolved multiple/common zeros.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step578 searched analytic root isolation, interval Newton and rigorous improper integration; inspected primary statements/proof cases below, reusing exact-reference/fold and failed-sign assessments. Exact-family searches found no matching inspected census; no novelty inference.
SOURCE_EVIDENCE: Hickey–Ju–van Emden2001, JACM48(5),1038–1068, DOI10.1145/502102.502106, author manuscript Section4.8 Theorems9–10/proofs PDF pp10–11 https://fab.cba.mit.edu/classes/S62.12/docs/Hickey_interval.pdf ; Johansson1802.07942v1 Sections2/2.1 pp2–4,3.2 p6 https://arxiv.org/pdf/1802.07942 ; Arb2.23 arb_calc/acb_calc contracts https://arblib.org/arb_calc.html and https://arblib.org/acb_calc.html ; DLMF8.2.2 https://dlmf.nist.gov/8.2#E2 ; reuse L814/step574 exact Q and scalar-fold citations.
COMPARISON: Primary interval inclusion and finite quadrature cover bounded analytic-function testing with complete exclusions outside an explicit unresolved set. They provide no automatic improper tails, multiple-root isolation, endpoint equality decision or actual signs. L016/L019/L020/L814 supply majorants and identities; explicit constants and certificates require specialization, not general-theorem reproof.
GAP: No evaluator, explicit tail constant, event or sign is certified. Source coverage is adequate for a bounded attempt retaining every unclassified cell; guaranteed resolution of multiple/common zeros is not covered. A new implementation continuation needs separate approval.
REASON: New primary coverage removes the polynomial-only method limitation and supports independently testable finite work. Missing numerical certificates are research obligations, not essential missing literature. No all-real-reference or signed-mechanism import is needed.
SCOPE: Completed literature-only step578; a bounded census with honest unresolved output is supported, not a guaranteed complete solver. No lemma, mathematical script, event calculation or global sign assertion was made.

Main gap: actual-Xi all-degree mixed positivity. The intermediate target
would be a certified presence/absence test for nondegenerate real events
in the stated finite box. A certified positive W' event would reject a
local no-loss rule; negative events or an absence certificate would give
only finite-box evidence for later deformation work. No outcome resolves
RH, all degrees, unbounded x, parameter-boundary events or zeros at infinity.

Essential local inputs are L019, L020, L021 and audited L814, including
its exact Q,S,c,B,F,G,D,W conventions. Do not substitute the non-even first
theta term or a finite Gaussian pencil. Common zeros and W'=0 are
unresolved cases, not absent by definition; an incomplete isolation must
report its uncertified intervals. Positive central values do not by
themselves provide an explicit zero-free origin interval. The included
edge x=40 and interval coverage between all isolated roots require care.

The source step should inspect primary hypotheses and relevant proof
cases for validated analytic root isolation and complete improper-integral
evaluation, and compare their assumptions with this exact pair. Reuse
adequate standard theorem coverage rather than reprove it. It may
approve a bounded census only if the proposed evaluation and full-domain
exclusion obligations are independently checkable; it must retain any
multiple-root nontermination limitation. No absent root follows from a
grid, floating point scan, or small absolute error alone.

Continue if one concrete certification method covers full tails and
all unresolved intervals, or yields a precisely bounded informative
partial test. Otherwise record the missing hypothesis and park dependent
computation; do not restart the blocked global-reference access loop.
This nomination does not approve a new mathematical mechanism. No
supported new signed mechanism currently warrants creative routing;
the census is a possible standard calculation, not relabeled creativity.
No cross-notebook input. Full matching Mathlib coverage is unchecked.


## Completed source comparison — step578, 5 November 2026

The preceding prospective instructions are retained as the original
nomination; this section resolves their source question. Read the full
L814 and needed L016/L019/L020 proofs after the supplied overview/DAG.
Reuse step574's exact-family/fold scope, step575's unsigned failure and
step577's sign-equivalence audit. No global real-zero reference is used.

### Known methods and inspected hypotheses

[Hickey–Ju–van Emden manuscript](https://fab.cba.mit.edu/classes/S62.12/docs/Hickey_interval.pdf),
Section4.8, Theorems9–10 and proofs, PDF pp10–11: let f be C1 on I,
with inclusion extensions A,A1 of f,f', a in I, and N=a-A(a)/A1(I).
When 0 is outside A1(I), every root in I lies in I intersect N. If N
is also bounded, nonempty and contained in I, existence and uniqueness
follow. The inspected proof uses the mean-value theorem, endpoint signs
and monotonicity. Its subdivision discussion preserves undecided cells;
multiple roots have no guaranteed resolution. Use closed bounded cells,
strict interior inclusion and no division by an interval containing zero.
Strict opposite endpoint signs and a nonzero derivative enclosure also
certify a unique simple root. These known results need no local reproof.

[Johansson1802.07942v1](https://arxiv.org/pdf/1802.07942), Sections2/2.1
pp2–4, specifies complex-ball evaluation and analytic-domain checks for
finite Gaussian quadrature, with direct-box subdivision fallback. Actual
returned radii determine accuracy, rather than requested tolerances.
Section3.2 p6 explicitly requires manual truncation and symbolic tail
bounds for improper integrals. It supplies no tail constants for this pair.
For this application integrate finite theta sums and Q; add independently
proved omitted-series/integral errors on the real path. Finite summands
are entire in the integration variable, so no unproved complex bound for
an infinite theta sum need be passed to a quadrature callback. Interval
x must be enclosed uniformly; midpoint-only integration is insufficient.
Ordinary interval boxes provide a slower alternative.

[Arb2.23 arb_calc](https://arblib.org/arb_calc.html), callback and
`arb_calc_isolate_roots`, documents coverage outside returned cells,
single-root flags and unresolved flags, with multiple/endpoint limits.
The callback requests Taylor coefficients, not unscaled higher derivatives.
[Arb2.23 acb_calc](https://arblib.org/acb_calc.html), callback and
`acb_calc_integrate`, requires finite bounded paths and holomorphicity
checks. These are versioned contracts, not an installed-backend audit.
The [author-hosted FLINT3.7.0-dev page](https://fredrikj.net/fdoc/html/arb_calc/isolate_roots.html)
corroborates root flags but carries an October2026 generated-text notice;
the primary theorem proof, rather than that prose, is the mathematical
basis. Detailed flintlib.org pages returned403/unavailable. This is not
an essential source blocker: record the actual backend/version and check
its API, or implement the cited explicit inclusion/sign tests.

[DLMF8.2.2](https://dlmf.nist.gov/8.2#E2) defines the upper incomplete
gamma integral. On positive real lower endpoints it has no branch
ambiguity. This supports exponential-power majorant integrals after an
explicit change of variables; it is not a numerical tail estimate.
Direct exponential/geometric majorization using L016/L814 is also allowed.
No new tail formula or constant was derived during this literature turn.

### Exact specialization still required

L020/L814 establish real analyticity, meeting the interval method's
regularity hypothesis. The missing work is an actual inclusion evaluator
for F,G and their first two x derivatives on whole cells, including a
normalization denominator bounded positively away from zero. Apply only
L814's existing W,W' and event formulas. No potentially zero F,G,D or
derivative interval may be divided out. Full matching Mathlib coverage
is unchecked; no formalization claim or absence claim is made.

L016/L019's finite existential constants are not numerical error bounds.
Research must exhibit explicit theta n-tails and u-tails for every order
used, including normalization; retain all omitted parts in each enclosure.
Publish those bounds/proofs canonically if used. This is SPECIALIZE, not
an assertion that an existing software call certifies this exact census.
It changes constants and implementation, not the general theorem.

Cover the whole requested x-domain. Certify positive F,G on a stated
[0,delta], delta>0, to exclude events near zero, or retain that interval
as unresolved. Center values alone do not close it. At40 certify exclusion,
a located event with domain membership, or an unresolved edge cell.
An open-interval isolator cannot determine the included edge by itself.

At a certified simple W root, enclose F G and W' over its isolating cell.
Strict F G<0 and W' excluding zero certify an event; evaluate tau and
orientation by L814. Strict F G>0 excludes an interior-parameter event
there. If a test contains zero, preserve the uncertainty. Common zeros,
W'=0 and parameter-endpoint equality cannot be silently discarded.
Direct strict same-sign F,G also excludes events without isolating W;
label that as event exclusion, not as absence of W roots.

Fix and report subdivision, precision and evaluation caps. Save a cover
by certified exclusions/events and explicitly unresolved cells, including
shared dyadic endpoints. Call it a complete census only after every
cell/boundary is settled for the event definition. A certified adverse
event rejects the local no-loss rule; favorable finite events or absence
leave RH and the mixed-positivity gap open. If relevant cells remain
undecided at the caps, stop and preserve them; do not repeat an indefinite
precision loop. No numerical inequality was certified today.

### Search extent and decision

Queries included `Johansson rigorous numerical integration arbitrary
precision Petras algorithm Arb 2018 tails`, `interval Newton real roots
isolation analytic function multiple roots interval arithmetic theorem`,
the exact Hickey–Ju–van Emden title, and `"Pólya" "xi" "Wronskian"
interpolation zeros` / `"Riemann" "Pólya" "collision" interpolation zeros`.
No matching census was identified in inspected material. Unrelated
Wronskian papers and unreviewed RH claims in results remain unread leads,
not inputs. The bounded search establishes neither novelty nor absence
of a stronger result. Polynomial-only tests are no longer the sole
method coverage, but the prior signed-comparison failures still stand.

Decision: source-supported bounded specialization with explicit failure
output. Outcome EXPLORATION, literature_comparison/REPRODUCTION; no actual
mathematics executed. The new implementation nomination in
`2026-11-05-polya-census-implementation.md` needs separate next-turn approval.
No further discovery browsing is needed for that gate. Creative routing
remains unjustified: no independent signed mechanism was discovered;
certifying this fixed family is ordinary implementation.
