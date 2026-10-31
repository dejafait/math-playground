# Saturation in the actual residual-weighted norm: completed source review

TARGET: Assess whether E_3(T)=inf_{p in R[x],deg p<=3} integral_T^(2T)|R_T(t)| |p(|F_T(t)|^6)-|F_T(t)|^6/(1+|F_T(t)|^6)|dt is o(T(log T)^3) along an unbounded sequence, for the exact R_T and F_T of L477/L481.
CHECKED: 2026-10-29
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed bounded exact/stronger-result searches for weighted L1 fixed-degree reciprocal approximation, best-approximation duality and short-Dirichlet-polynomial distributions; inspected the primary statements and relevant proof cases below and reused the ready bounded-correlation comparison. No matching E_3 estimate was located; this does not establish novelty or either asymptotic alternative.
SOURCE_EVIDENCE: Houston--Roggendorf--van der Zee, ESAIM M2AN 56 (2022), Section 2.1, Theorem 2.1 and Corollary 2.4, pp. 185--186; Heap 1703.08842v1, norm definition, Theorem 1, Propositions 1--2 and Section 2 opening, pp. 1--5; retained approximation and finite-mean-square inputs in 2026-10-29-bounded-short-resonator-dual-correlation.md. Additional screened statements and exact URLs are below.
COMPARISON: General L1 optimality supplies an annihilating bounded functional, including freedom on the zero-error set; it supplies no error rate for this varying weighted statistic. Heap's small-q bound uses infinite-time means with length fixed, not growing N=floor(T^(1/24)) on [T,2T] with the full residual weight. Uniform reciprocal approximation and the ready absolute-moment results likewise do not decide E_3.
GAP: Decide the normalized E_3 asymptotic for degree at most three and A=0 without assuming weighted amplitude concentration, negligible exceptional mass, coefficient bounds, Haar transfer or phase independence. Both residual phases and all endpoints remain. Feasibility would still leave positive signed correlation and all-degree positivity unresolved.
REASON: The bounded source comparison is complete and no essential inspected source remains inaccessible. Approve one exploratory mathematical attempt on this unchanged exact target using elementary weighted inequalities, the retained finite-polynomial interface or the cited general optimality criterion; do not import an unproved distribution estimate or reprove the general approximation theorem. This is not approval of a direct signed-correlation or RH argument.
LITERATURE_REASON: The actual residual-weighted norm differs from the ready global-uniform norm, and its general L1 optimality and finite-height distribution coverage were essential unread inputs at invocation start.
SCOPE: Actual finite-height R_T=U+Re(exp(2i theta)V) and F_T of L477/L481; arbitrary real T tending to infinity along a sequence; real coefficients allowed to depend on T; degree at most three includes zero and constant polynomials; A=0 only. No RH, phase independence, Haar replacement, discarded exceptional set or source theorem for the complete signed statistic is assumed.

## Original nomination, preserved

The following nomination records the invocation-start review requirement.
Its unreviewed-source status is superseded by the completed comparison below.

### Relevance and bounded review

The main gap remains actual-Xi all-degree mixed positivity. The
intermediate target is feasibility of one actual-height approximation
implementation for the bounded dual certificate, not positivity itself.
The degree cap is motivated by the now established formal-length
obstruction, with its exact scope retained. Fixing A=0 specifies one
weight; it neither optimizes over A nor settles other saturation scales.

Compare three routes only for selection. The unchanged interpolation
certificate is stopped by L481. Global-envelope uniform polynomials
with the stipulated length budget are stopped by L482. Approximation
in the actual |R_T| measure has a different, explicit failure test and
is selected for source assessment. No mathematical test of it is done
or approved here. These comparisons do not reset any exploration
counter by renaming an exhausted mechanism.

If such approximation were available, a separate evaluation of the
complete signed polynomial correlation might support a bounded dual
test of L477's L1 defect. Approximation alone is insufficient: even a
constant approximant might have no useful signed correlation. Both
phases, coefficient errors and a positive T(log T)^3 margin would
still have to be established. The negative mass and all higher signs
would remain unresolved even after a successful defect obstruction.

The review should first reuse the exact statements and proof cases
already inspected in the bounded-correlation assessment, then examine
only essential results about approximation in this weighted actual-time
norm. Absolute moments, Haar polynomial approximation and small
exceptional-set measure are not matching theorems without a bound
for their full |R_T|-weighted error. Unread new leads must be labeled.

Continue only with source coverage supporting a concrete decision at
E_3(T)=o(T(log T)^3) on an unbounded sequence, or a positive lower
bound on that normalized infimum. If essential coverage remains
blocked, park this dependent implementation and nominate an
independently testable target. Do not repeat a search solely to meet
a schedule or infer novelty from failure to find a source.

Mathlib matching has not been checked; no absence claim. No new
lemma, computation or approval for this target is supplied here.

## Completed comparison — 29 October 2026

The exact TARGET and scope are unchanged. This is one literature-only
step: no E_3 estimate, new specialization, lemma or mathematical script
has been derived. The main gap remains actual-Xi all-degree positivity.
The intermediate obligation is feasibility of a degree-at-most-three
bounded-weight implementation; its possible downstream signed test
would still need its own positive margin and coefficient-error control.

### Primary results actually inspected

**Houston--Roggendorf--van der Zee, _Gibbs phenomena for Lq-best
approximation in finite element spaces_, ESAIM M2AN 56 (2022),
177--211, DOI 10.1051/m2an/2021086.**
[Published primary text, pp. 185--186](https://www.numdam.org/item/10.1051/m2an/2021086.pdf#page=9).
Read Section 1.1's bounded Lipschitz-domain convention, Theorem 2.1
(Banach space, closed linear subspace), and the complete L1 argument
leading to Corollary 2.4. A best approximant is characterized by a
bounded annihilator agreeing with the error's sign where it is nonzero;
on the zero-error set its values may lie anywhere in [-1,1]. The
proof retains that set and uses the L1/L-infinity pairing. Theorem 2.1
quotes Singer (1970), Theorem 1.1; Singer itself was not separately read.
Do not reprove this standard characterization. Its finite-time weighted
application, closed-subspace justification and any quantitative estimate
remain work for the mathematical turn. No approximation rate is stated
for our residual or growing-length amplitude law. The displayed zero
branch of (2.1) prints norm equality 1; do not import that branch as a
description of the entire subdifferential. Corollary 2.4 explicitly
retains the bounded freedom needed on zero-error sets. Use its L1 case,
not a differentiable q>1 formula or an assumption of a null error set.

**Heap, _Upper bounds for Lq norms of Dirichlet polynomials with small
q_, arXiv:1703.08842v1, 26 March 2017.**
[Primary version, pp. 1--5](https://arxiv.org/pdf/1703.08842v1#page=1).
The norm is the limiting height average with N fixed. For
f(s)=sum_(n<=N)n^(-1/2-s), Theorem 1 gives, for fixed 0<q<=1,
||f||_q <= (1+o(1)) C_q (log N)^alpha_q
(log log N)^(1/2-alpha_q), alpha_q=1/(4(2-q)). In particular
||f||_1 << (log N)^(1/4)(log log N)^(1/4). Read Propositions
1--2, their limiting-mean definitions, the Holder step proving
Theorem 1 and Section 2's Carlson/mean-value reduction to equal
products. Proposition 2 restricts its Euler-product cutoff to
exp((log log N)^2)<=Y<=exp(log N/(5 log log N)).
Neither the statement nor these proof passages provides a uniform
finite-height transfer with N growing as prescribed, or a joint
|R_T|-weighted error. These are mathematical scope mismatches, not
an access blocker or a proof that E_3 is large. The v2 URL returned
404; v1 was accessible, with its version verified on the title page.

**Other inspected statements, not imported.**
[Kohlenbach--Oliva, _Proof mining in L1-approximation_, author
preprint dated 23 August 2002, pp. 2--3, main-result statement of
Theorem 4.1](https://www2.mathematik.tu-darmstadt.de/~kohlenbach/l1final.pdf#page=2)
concerns uniqueness moduli for best polynomial approximation in the
fixed unweighted norm on [0,1]. Its theorem statement and norm
definition were inspected; its full proof was not. It gives no
estimate for our varying weighted best error.
[Wang--Xu, _Representer Theorems in Banach Spaces_, JMLR 22
(2021), Sections 2--3, pp. 6--9](https://www.jmlr.org/papers/volume22/20-751/20-751.pdf#page=6)
defines a minimum-norm interpolation problem with finitely many
independent continuous constraints. Propositions 2--3 characterize
that problem; their hypotheses are not an E_3 theorem. No
representation result or proof from that paper is used here.

### Reused coverage, duplicates and failures

Reuse the inspected primary approximation, exceptional-set and
finite-polynomial statements in
[the bounded-correlation comparison](2026-10-29-bounded-short-resonator-dual-correlation.md).
Kraus--Vassilevski--Zikatanov v3 Theorem 2.1 addresses best uniform
reciprocal approximation on a prescribed interval; it does not replace
the actual weighted measure by that interval. Heap--Soundararajan
Section 5/(14), retained in L481 (3)--(4), controls finite mean
squares with a length-dependent error, not a nonlinear weighted
distribution. The already inspected good/bad prime-block arguments
of Heap--Radziwill--Soundararajan cannot discard a set merely from
its Lebesgue measure. No fresh browsing of those unchanged sources
was required.

Narrow local checks covered L477 (1)--(5), L481's definitions and
finite-polynomial interface/Section 2, L482's exact hypotheses and
conclusion, the ready Hardy-space comparison, and the two residual
interpolation/global-envelope attempt records. Searches for E_3,
weighted cubic, saturation and annihilator terminology found no
completed duplicate of this exact implementation. Older prime-twisted
jet cubics concern different observables. No sibling notebook was read.
L481 stops a specific interpolation certificate; L482 stops a
global-uniform approximation under its formal budget. Preserve both
stops without extending them to this norm. The Haar/finite-height and
chirped-cancellation qualifications in the Hardy-space review remain.

Searches included `weighted L1 polynomial approximation fixed degree
rational function varying measures duality best approximation`,
`best L1 approximation measure duality polynomial`, `Dirichlet
polynomial distribution weighted small values short partial sum zeta
critical line`, `weighted L1 best approximation Cheney characterization
measure`, `best L1 approximation characterization Pinkus pdf`, and
`best L1 approximation 1/(x polynomial weight`, plus exact theorem-name,
reciprocal and nonlinear weighted-distribution variants. Hits for
coefficient l1 norms, fixed Jacobi weights, fixed Lebesgue-measure
interpolation and generic large-value bounds were not treated as
matching theorems. Snippets are discovery leads only. In particular,
_Canonical Sets of Best L1-Approximation_, Theorem 2.7, appeared as
an unread fixed-Lebesgue interpolation lead; no result from it is used.
No novelty claim follows from this bounded search.

### Decision, bounded mathematical test and remaining obligations

EXPLORE approves exactly the existing TARGET for one mathematical
attempt. General optimality conditions and elementary weighted norm
inequalities are available; an actual-height concentration theorem is
not an established input. Begin with the included constant candidate
p=1 and test its complete weighted error against T(log T)^3. A
failure of an upper-bound method for that candidate does not prove a
lower bound on the infimum. If a lower-bound approach is used instead,
it must be uniform over every real cubic with T-dependent coefficients,
including constants and zero; any required weighted mass or coefficient
control must be proved rather than supplied by a hypothetical law.
This specifies a future test and asserts no result of that test.

Continue this implementation only on a proved little-o bound along an
unbounded sequence, a positive normalized lower bound, or an explicit
new intermediate estimate with a discriminating continuation test.
If the bounded attempt only returns the already recorded ordinary
moment/Haar mismatch without new evidence, park this implementation
and choose an independently testable target; do not repeat source
searches or rename an exhausted route. Do not silently replace the
saved E_3 target by a single-candidate or unweighted conclusion.

Even successful approximation supplies no positive complete signed
correlation. L477's full residual, L481's exact F_T, endpoints,
coefficient-dependent errors, negative mass and higher signs remain
essential obligations. A central creative sign attempt is currently
unjustified by the missing actual-height joint signed input; this
finite-degree feasibility test is established-method exploration,
not a creative proof of the main positivity gap. Mathlib matching
was not checked; no absence claim is made.
