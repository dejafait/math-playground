# Lobe-dependent resource sharing — completed source comparison

TARGET: Assess primary coverage for nearest-neighbor allocations with lobe-dependent shares in L898's full marginal, including their exact feasibility criterion and infinite-lobe residual, and nominate one bounded noncircular test or retire this mechanism.
CHECKED: 2026-11-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step136 searched variable-lobe/Fourier allocation, weighted and countable Hall, Strassen prescribed marginals, and countable splitting terminology; inspected the three primary sources below and reused step133/134's shape/duplicate/failure comparisons. No inspected source determines the actual-theta resource inequalities; no originality claim.
SOURCE_EVIDENCE: Koperberg arXiv:2202.02092v1 Theorem1 pp2, Proposition4/proof pp5–6 and relevant Lemma3 cases pp3–4; Barthe et al. LMCS15(4:18)2019 Definitions2.1/3.2/3.8–3.10, Theorems3.7/3.11/3.12 and complete main cut/flow proof pp18:3,6–9, plus alternative limit cases pp18:10–11; Sokolova–Woracek CALCO2021 Theorem2 p23:3, Lemma11/Corollary12 p23:10, proof of Theorem2 p23:11 and Theorem15/proof pp23:12,14–15. Direct URLs and qualifications below.
COMPARISON: Weighted Hall/Strassen already supplies general resource feasibility; countable max-flow avoids inventing an infinite-path theorem or a dummy surplus of unknown sign. These theorems require all relevant cuts and do not estimate actual theta lobes. The constructive splitting theorem has no controlled total-norm convergence rate. Fixed-half-share, Planat remainder and actual-product cofactor stops remain scoped and intact.
GAP: Actual capacity inequalities and complete infinite-lobe signing remain unproved. A finite cut obstruction can be tested without assuming the total sign; a finite pass cannot pay the other negative lobes or certify infinite feasibility. No all-height or higher mixed-sign transfer is available.
REASON: Complete the changed-hypothesis literature gate and nominate only the finite necessary-cut discriminator in a separate assessment; no specialization, mathematical result, lemma or mathematical script is produced in this literature turn.
SCOPE: General finite and countable resource theorem coverage, with one proposed x=16,y=0 four-demand cut test. No approval to infer complete positivity from a finite flow or an uncontrolled infinite remainder.
LITERATURE_REASON: The supplied REVIEW_REQUIRED target changes equal shares to variable conserved shares; essential capacity and countable-residual source coverage was missing. Existing transform/shape assessments are reused rather than repeated.

The following original nomination is preserved; the completed comparison
below and current fields supersede its pending-source statements. It did not approve any
theorem application or mathematical target. The completed step135 remained
entirely within the old ready first-cell assessment. No sign claim about
variable shares, new source theorem or novelty finding is made here.

The proposed change is to permit different shares for different full
positive q lobes while retaining their two neighboring negative lobes
as the only recipients and conserving every positive resource. Ask for
the precise known feasibility conditions before attempting a calculation.
The first possible application would be a bounded test at x=16,y=0 with
an explicit retained infinite tail, rather than another equal-share cell
or parameter sweep. This is a question to assess, not an established
transport formulation or a ready test.

Essential local inputs for the review: L898's actual full marginal and
integrability, and L904's exact fixed-share failure and arithmetic
qualification. Reuse
`drafts/literature/2026-11-08-full-difference-marginal-signed-discovery.md`
for inspected transform/shape scope and the two recorded comparisons
`ATTEMPTS/2026-10-31-nonlocal-paired-tail-signed-remainder-stop.md` and
`ATTEMPTS/2026-11-04-actual-theta-product-compensation-source-limit.md`.
Those failures concern distinct transverse/cofactor mechanisms; they
do not establish or refute a variable q-lobe allocation theorem.
L313's known total sign is a comparison, not a feasibility premise.
No cross-notebook input is proposed. Supporting/full Mathlib coverage
is unchecked.

Continue only if inspected primary coverage yields a concrete test whose
resource and infinite-residual obligations can be stated independently
of assuming the desired sign. If it only restates complete positivity,
depends on an unproved actual-kernel shape bound, or cannot pay the
retained residual, retire this candidate and record the precise obstacle.
Do not reopen endpoint deletion or independent-sector domination.

The central gap remains all-degree actual-Xi mixed positivity. A local
resource test would still leave other frequencies/heights and higher
mixed signs open. The missing independent complete signed-compensation
estimate currently blocks a justified central creative escalation; this
source review must not label routine allocation feasibility creative.

## Completed comparison — step136, 8 November 2026

The main gap remains L030–L032/C032a actual-Xi all-degree mixed positivity.
The intermediate purpose is to determine whether variable conserved shares
can survive a finite necessary resource test after L904 rejects equal shares.
A viable local allocation could help develop signed section margins;
complete infinite compensation and the higher mixed forms remain separate.

### Inspected primary results

Twan Koperberg, *Couplings and Matchings: Combinatorial notes on Strassen's
theorem*, [arXiv:2202.02092v1](https://arxiv.org/pdf/2202.02092v1),
4 February 2022. Theorem1 (p2) concerns finite probability spaces and any
relation. Proposition4 (p5) concerns finite bipartite graphs with
nonnegative vertex weights and equal side totals: nonnegative edge weights
with those incident sums exist exactly when w(U)<=w(N(U)) for every subset
of one side. Read its necessity calculation and subforest/leaf proof through
p6, including Lemma3's tight-set and strict-slack cases, pp3–4.
This is exact feasibility, not a sign estimate. The version's Lemma3
prints w(B)=w(B); use Proposition4's explicit equal-side premise, not that
tautological display. No finite theorem is silently applied to infinitely
many lobes; no reproof of the general theorem is needed.

G. Barthe, T. Espitau, J. Hsu, T. Sato and P.-Y. Strub,
*Relational star-Liftings for Differential Privacy*, LMCS **15**(4:18)
(2019), [publisher PDF](https://lmcs.episciences.org/5989/pdf),
DOI 10.23638/LMCS-15(4:18)2019. Definition2.1 allows countable support.
Theorem3.7 (p18:7) gives the all-subset relation criterion for proper
distributions. Theorem3.11 (p18:8) gives attained countable max-flow/min-cut
when there are no infinite directed paths and source-outgoing and
sink-incoming total capacities are finite. Read Definitions3.8–3.10 and
Theorem3.12's complete main proof (pp18:7–9): infinite-capacity crossings,
auxiliary-node cases, remaining cuts and saturated flow. Its generalization
allows subdistributions and epsilon/delta error. The alternative proof's
finite restrictions and marginal-dominating limits were inspected
(pp18:10–11); parsed subscripts/complements there have typographical defects,
so no normalization-sensitive display from it is imported. General theorem
coverage is available without claiming the blocked 1965 original was read.

Ana Sokolova and Harald Woracek, *Nawrotzki's Algorithm for the Countable
Splitting Lemma, Constructively*, CALCO2021, LIPIcs **211**, 23:1–23:16,
[primary PDF](https://drops.dagstuhl.de/storage/00lipics/lipics-vol211-calco2021/LIPIcs.CALCO.2021.23/LIPIcs.CALCO.2021.23.pdf),
DOI 10.4230/LIPIcs.CALCO.2021.23. Theorem2 (p23:3) requires two nonnegative
unit-sum sequences on N, a partial order and every upward-closed-set
inequality; it yields a supported matrix with both marginals. Read Lemma11's
increasing/decreasing convergence cases and Corollary12 (p23:10), and
Theorem2's limiting proof (p23:11). Theorem15 (p23:12), with truncation
proof pp23:14–15, controls individual entries but expressly gives no rate
of total l1 convergence. It presupposes dominance. It cannot price a signed
infinite residual. A two-layer relation is not identified with a partial
order without a proved embedding. Prefer the arbitrary-relation/flow
source above; do not implement this algorithm for the present test.

### Applicability obligations and the infinite residual

For future specialization, assign each complete positive cosine lobe its
integrated nonnegative resource and each complete negative lobe its
integrated demand, using L898's complete marginal. Retain both real
directions and every theta index. Only nearest positive neighbors may
supply a given negative lobe. Source theorems neither prove these actual
inequalities nor require them to be assumed as a hidden sign lemma.

The planned flow application must orient source -> positive resources ->
negative demands -> sink; verify countability, no directed ray, finite
incident totals and conservation from L898. Unequal totals must be handled
as capacities. Do not normalize sides separately or insert a surplus sink
with mass equal to an unproved positive transform. That would conceal the
very sign being sought. No specialization is proved in this review.

An infinite application must verify *every* relevant cut, not just total
mass or a finite prefix. L898 supplies absolute integrability, which
legitimizes sums and limits; it supplies no signed residual estimate or
uniform finite cutoff. A small absolute remainder alone cannot satisfy
exact demands when margins may vanish. The constructive source does not
remove that obligation. A positive total first sign, including L313's
known sign at 16, is not an allocation certificate. Full positivity as a
premise, unpaid endpoint deletion and independent-sector domination stay
excluded. No full infinite allocation is approved.

There is nevertheless a bounded *necessary* test: select exactly the four
negative lobes centered at -3a,-a,a,3a, a=pi/16, and include every allowed
neighboring positive resource. Test all their nonempty demand subsets.
A negative capacity cut would reject the entire nearest-neighbor rule,
whatever happens in the other lobes. The proposed proof must establish
that no resource outside the selected neighbor set is allowed to enter
such a cut; this is locality bookkeeping, not a positive infinite-tail
assertion. Every included lobe must have its full theta/transverse tails
paid. Thus the obstruction test has no omitted resource that could rescue
a failed cut. A pass leaves the *global* infinite residual unpaid and
authorizes no later sweep or global claim. This distinction preserves the
useful finite discriminator without calling it a sufficient compensation
theorem. Its detailed scope is nominated separately, for approval next turn.

### Search, duplicates and decision

Queries: `Strassen 1965 existence probability measures prescribed marginals
theorem 7 closed relation pdf`; `weighted Hall theorem countable bipartite
graph finite measures fractional matching transport`; `cosine lobes Hall
positivity`; `Couplings and matchings Koperberg pdf Strassen`; `Strassen
1177700153 pdf`; `lobe allocation Fourier positivity nearest neighbor`;
`Barthe Espitau Hsu Sato Strub star liftings theorem countable approximate
Strassen Hall condition pdf`; `countable weighted Hall theorem`; and
`Strassen countable relation Hall coupling theorem`. Primary statements
and proof cases above, rather than search snippets or secondary summaries,
support the comparison. No comprehensive novelty search is claimed.

The original Strassen publisher PDF errored and its legacy page led to
a service notice; do not retry that route. The accessible arbitrary-relation
source resolves the essential coverage need. No persistent source blocker
remains for the proposed finite test. Published-version identity for the
Koperberg preprint was not checked or needed.

Read L898 and L904 fully; reused step133/134's saved Johansson/Csordas/Tuck
coverage and the named Planat and actual-product failure records. A scoped
search in the named November8 assessments/history found no variable-share
Hall test. The older conditional-order, separate-family, shape and cofactor
stops do not decide these changed conservation constraints. L904 is still
unaudited and its code need not be trusted for new integrals without
verification. Its numerical value is motivation, not a Hall-feasibility
premise. Supporting/full Mathlib coverage was not checked; it is unknown.

Decision SPECIALIZE: general resource theory is known; only actual-kernel
application and certified lobe values remain. This is local source progress,
not progress beyond the inspected theorems. No new feasibility lemma,
actual sign or theorem specialization was derived. Nominate
[the finite test](2026-11-08-variable-lobe-four-demand-cut-test.md), whose
new assessment requires separate approval next turn. Continue only for
this falsifiable obstruction test; if it survives, stop this bounded step
with the infinite remainder explicitly open. The lack of an independently
paid signed remainder still blocks a central creative escalation. Routine
capacitated allocation must not be relabeled creative. Mathematical
exploration usage is unchanged by this literature turn.
