# Local heat-zero counts — source comparison2112

TARGET: Assess a uniform bound N_t(x,r)<=100 r log(2+|x|) for actual H_t zero copies with |Re z-x|<=r, 0<=t<=1/5 and |x|>=2r>=400, as a local replacement for C488a's global count.
CHECKED: 2026-11-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step2112 searched local H_t zero counts, uniform heat counts and explicit constant100; checked L135, C488a, L488, the September20 heat-route audit, the October30 selected-circle assessment and the November20 isolated-orbit assessment. Exact local assessment/attempt searches found no ready numerical match. No novelty inference.
SOURCE_EVIDENCE: Polymath1904.12438v2 Theorem1.5(iv), Proposition9.1(ii)-(iii) and their proof cases, Section9/(99)-(105), https://arxiv.org/html/1904.12438v2 ; Caceres hexagon2610.00207v2 Lemmas3.1-3.2, pp.3-5, https://hexagonmath.org/pdf/2610.00207v2 and its versioned TeX; Rodgers--Tao1801.05914 current HTML Theorem3.12 hypothesis and Section3 context inspected as a scope contrast.
COMPARISON: Polymath1.5(iv) already supplies a positive-time unit-window O(log(2+X)) count with an absolute constant independent of t, without x>=exp(C/t). Its proof supplies the off-axis mechanism missing from L135. The constant100 and entire closed numerical domain are not stated. Caceres gives explicit counts including t=0 only for t<=1/(100 log((X+1)/(4pi))), not the full time band.
GAP: Quantify the known off-axis method sufficiently to prove or fail constant100 for the exact target, including finite heights, t=0, closed spatial endpoints and arbitrary r. Neither an unspecified O constant nor small-time count pays this numerical threshold. No new bound is established here.
REASON: Approve a bounded quantitative specialization of a known local-count mechanism, not a new local-count theorem in order of magnitude. Spatial counts may reduce C488a transport costs; all-height reality, overlap and mixed signs remain independent. A citation alone does not fix the requested numerical constant/domain.
SCOPE: Exact TARGET retained. Later mathematical work may track constants in the inspected off-axis/Jensen or logarithmic-derivative method, use L019/L020/L058 and the strip/global-count conventions of L488/C488a, and test endpoint/window specialization. This turn is literature-only; no lemma or mathematical script was written. The proposed bound is unproved.
LITERATURE_REASON: The start assessment was REVIEW_REQUIRED for a changed spatial target; essential local-count theorem coverage was missing. This comparison resolves that gate and does not repeat the ready AppendixB audit.

## Original nomination2111 (historical; decision above supersedes its gate)

Main gap: L030-L032/C032a actual-Xi all-degree mixed positivity.
The intermediate target is the stated count in a horizontal interval,
with all zero copies in the known global strip included. The proposed
constant is a test threshold, not a value derived or approved here.
The count is independent of any prescribed lower nonreal ordinate.

Its possible use is a later re-estimate of C488a's collective transport:
the current proof pays a global count even for nearby partners and the
middle horizontal range. A local count would supply different spatial
information. Such a re-estimate, an improved quantitative overlap with
L488, passage to all heights, and mixed signs remain independent unpaid
steps. No claim that a local count itself implies RH is intended.

Search precise local zero-count terminology for the actual heat family,
stronger uniform asymptotic counts, and local stops before deriving
anything. Read the primary hypotheses and proof cases for any proposed
import, especially the domain x>=exp(C/t) and t=0. Match normalizations
using L019/L020/L058/L488 and retain C488a's multiplicity convention.
Do not import a generic entire-function count with an unpaid lower
bound at its Jensen center. Unknown Mathlib coverage is not absence.

Continue only if primary coverage supplies this threshold, or exposes
a specific independently testable difference under the stated hypotheses.
If the bound is known, import it with its exact constant/domain and
classify the later use honestly. If only a positive-time asymptotic
regime is covered, record that restriction rather than extrapolating it.
Persistent source obstruction requires a different target. No source
failure or global ban is asserted by this nomination.

This assessment is newly written and REVIEW_REQUIRED. The next turn
must conduct the literature comparison; it is not an authorized new
mathematical attempt. No creative purpose is assigned before that
comparison determines whether a new mechanism is actually needed.

## Completed source comparison — 21 November2026, step2112

The main gap and downstream use remain those in the nomination. The
new evidence changes the intermediate task: a uniform positive-time
local-count mechanism is already published. The remaining specialization
is quantitative and includes a zero-time endpoint, not an invention of
a local-count method. No estimate is derived in this source turn.

### Primary theorem and load-bearing proof cases

D. H. J. Polymath, *Effective approximation of heat flow evolution of
the Riemann xi function, and a new upper bound for the de Bruijn--Newman
constant*, Research in the Mathematical Sciences 6 (2019), article31,
[arXiv1904.12438v2, 4August2019, Theorem1.5(iv), pp.9-10;
Section9, pp.56-60](https://arxiv.org/html/1904.12438v2).
For 0<t<=1/2 and X>=0 its multiplicity count satisfies
N_t(X+1)-N_t(X)=O(log(2+X)); its constant is absolute, independent
of t. This part has no exp(C/t) condition. Parts(i)-(iii) have that
condition and must not be substituted for part(iv).

Read the proof of (iv), including (105): its paired Hadamard sum at
X+4i has positive imaginary-part kernel contributions because every
zero is in |Im z|<=1. It obtains the logarithmic-derivative bound from
Proposition9.1(ii)-(iii) and Cauchy's formula. Read those hypotheses
and proof cases: (ii) uses 3<=y<=4 and x>=C with unspecified C;
(iii) controls bounded neighborhoods for x_0>=200. Unlike (i), neither
requires x>=exp(C/t). The proof of (ii) bounds the Dirichlet remainder
by pi^2/6-1 plus O(x^(-1/2)), reaching the stated 0.7 only for a
sufficiently large unspecified x. These are cited proof inputs, not
numerical estimates certified here.

This source supplies an off-axis nonvanishing comparison; it does not
authorize assigning numerical values to its hidden constants or to its
compactness step. Its theorem states t>0. Passing to t=0 with closed
window endpoints must be justified separately using local uniform
convergence, padded contours/windows and multiplicity conservation;
no such passage is proved in this literature-only step. Evenness and
the normalization F(lambda,z)=8H_(4lambda)(2z) must remain explicit
if local F coordinates are used. C488a and L488 already verify this
normalization from L019/L020/L058; the present target stays in H units.

### Explicit small-time comparison, with its restriction retained

Pedro Caceres, *Cross-Energy of Dirichlet Partial Sums. Part35: How
long can an off-line zero survive the de Bruijn--Newman heat flow?*,
[Hexagon2610.00207v2, Lemma3.2, pp.3-5](https://hexagonmath.org/pdf/2610.00207v2).
The versioned resource served on this date has a November2026 title
date and subsequent-revision notes, despite its v2 URL; no stronger
version identity is inferred. Read the statement, Lemma3.1, Gaussian
representation(P4), and both upper-circle and lower-center cases of
Lemma3.2's proof through its concluding estimate. The exact statement
was also checked in the [served TeX, label lem:C](https://hexagonmath.org/api/v1/works/2610.00207v2/source?path=Caceres_CE35_DBN_OfflineZero.tex).
For X>=200, ell_X=log((X+1)/(4pi)), and 0<=tau<=1/(100ell_X),
it states that the CLOSED window [X,X+1], and its negative reflection,
contains at most 2.07ell_X+2.5 zero copies. It includes tau=0.

Its center is X+1/2-2i. The lower bound uses a Gaussian-shift
comparison with xi at real part3/2; the small-time restriction controls
the shift and its error. Thus extending its bound to all tau<=1/5
cannot be inferred by dropping that restriction. The proof invokes
AppendixA numerical certificates; those certificates were not inspected
or replayed and this lemma is not adopted as a verified numerical
premise. Its narrower statement already rules out direct import for
the full target. The November20 assessment1975 had recorded this as
an unread survival lead after a wrong-domain arXiv URL failed; the
correct Hexagon PDF/source are now accessible. No persistent source
block is claimed.

### Other sources, duplicates and failures

Rodgers--Tao, *The de Bruijn--Newman constant is non-negative*,
[arXiv1801.05914, Section3, Theorem3.12](https://arxiv.org/html/1801.05914),
was inspected at its exact hypothesis: Lambda<t<=0, in the standing
contradiction setting Lambda<0. It is a count for real zeros in that
regime, not an unconditional count for the present mixed divisor over
0<=t<=1/5. No estimate is imported from it.

L135's full proof and its missing-estimate audit were read. It supplies
a conditional Jensen reduction, and warns that subtracting global
upper counts is invalid. Its symmetric heat-time/strip hypothesis is
broader than this target; the old unpaid anchor is not a ban on using
Polymath's positive-time off-axis analysis. The September20 relevance
audit preserves the separate global moving-supremum obstruction.
The October30 selected-circle assessment covers one real/simple zero
at exponentially high phase centers on a positive time band, not an
all-zero window count. C488a's global count and the audited AppendixB
transport are reused with their qualifications; neither is replaced
or modified by this review.

Queries: `"H_t" "local" "zeros" "count" Polymath`,
`Rodgers Tao heat flow zeros local counting uniform t positive zero`,
`"H_t" "local" "100" zeros count`, and
`"heat" "zero" "count" "Polymath" "uniform"`.
Search snippets were only leads. The conclusions above use inspected
primary statements/proof cases. No absence or novelty claim follows
from the bounded search. Full matching Mathlib coverage is unchecked;
no Mathlib declaration is used as evidence for the numerical bound.

### Approved continuation and discriminating test

SPECIALIZE applies to the unchanged TARGET line. A subsequent attempt
should extract actual uniform constants from the published off-axis
method, then test the requested 100r log(2+|x|) on every stated
parameter, including |x|=2r and r=200. It must pay finite heights,
the t=0 limit, closed interval boundaries and the conversion from
unit windows to arbitrary radii. These are obligations, not results
of this review. Keep multiplicity and complex partners throughout;
neither simplicity nor a lower nonreal ordinate may be assumed.

Continue only with a complete numerical comparison meeting100, or
an informative explicit failed inequality. If a source constant
cannot be made effective, retain that obstruction and restrict or
park this quantitative specialization rather than repeat its
qualitative theorem. A bound with an unspecified constant is known
scope, not completion of the saved numerical target. No new creative
mechanism is justified by this review: the actual all-height input
needed for transport and the central mixed signs remain unpaid.
