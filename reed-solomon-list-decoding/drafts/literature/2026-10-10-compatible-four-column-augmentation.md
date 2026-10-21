# Compatible four-column augmentation — finite source comparison

TARGET: Assess a finite constructive lower bound for pairwise-compatible nine-set additions on at most four F_107 graph columns to exceed total packing size 19800269675.
CHECKED: 2026-10-10
DECISION: EXPLORE
SEARCH_EVIDENCE: Searched constant-weight augmentation, finite generalized Gilbert bounds and multiply constant-weight constructions; inspected primary PDFs 1512.08220v1 and 1411.2513v1 and the relevant definitions in 1107.4120v2; no matching threshold-crossing finite construction was located.
SOURCE_EVIDENCE: Wang–Wei–Shangguan–Ge v1 Section IV, printed p. 8, finite ball formula and first inequality in Theorem 4.4 proof; Chee–Kiah–Zhang–Zhang v1 Section IV.A product construction pp. 8–9 and Theorems V.1–V.2/proof pp. 9–11; Bailey–Burgess v2 Definition 2.1.1 p. 3. Reuse Xu–Chen v4 Proposition 2.2 coverage from the finite-nine-set assessment.
COMPARISON: A finite Gilbert method is available for fixed equal part weights, but the requested universe varies both column support and profile; known product/asymptotic results inspected do not supply its finite compatible augmentation.
GAP: Derive and evaluate a finite closed-neighborhood certificate for the actual restricted universe, retaining all cross-profile conflicts; no packing above 19800269675 or such certificate value is established here.
REASON: Actual compatibility differs from L043 resource feasibility; a bounded exact greedy test can quantify a guaranteed augmentation without assuming integrality or finite applicability of asymptotic matching results.
SCOPE: Source comparison only for nine-subsets of Omega={0,...,8} times F_107 meeting at most four columns; the two embedding points remain unused.

## Source statements and qualifications

Wang, Wei, Shangguan and Ge, *New bounds and constructions for
multiply constant-weight codes*, [arXiv:1512.08220v1, 27 December
2015](https://arxiv.org/pdf/1512.08220v1), printed p. 8, Section IV:
for MCWC(m,n,2d,w), the finite forbidden-ball size is
sum over i_1+...+i_m<=d-1 of product_j binomial(w,i_j)
binomial(n-w,i_j). The first inequality in Theorem 4.4's proof
bounds code size below by binomial(n,w)^m divided by this volume.
Here m,n,w are positive integers, w<=n, with even prescribed distance.
The displayed asymptotic theorem additionally assumes omega<=1/2
and delta<=max(1/2,2omega). Read its complete proof, including the
finite inequality before the entropy estimate. Do not substitute an
entropy approximation for a finite certificate. Equal weights on fixed
parts do not describe the mixed-profile universe. Extending the
finite greedy argument and counting its neighborhoods is future work,
not a result of this review.

Chee, Kiah, Zhang and Zhang, *Constructions of Optimal and Near-Optimal
Multiply Constant-Weight Codes*, [arXiv:1411.2513v1, 10 November
2014](https://arxiv.org/pdf/1411.2513v1), Section IV.A, printed p. 8:
inner CWC(n,d1,w) families C_i have union distance d2<=d1; an outer
MCWC(m,s,d3,1) yields distance at least min(d3*d2/2,d1). Equal inner
sizes M give outer-size times M^m words. The complete distance proof
was inspected. It needs these inner families and outer code; it does
not supply the present mixed weights or their cross-support compatibility.
Section V, Theorem V.1, pp. 9–10, gives an asymptotic generalized
packing limit for fixed weights and n_i=c_i*v. The inspected proof
uses Theorem V.2 (Kahn): for each bounded edge size and error tolerance
there exists a codegree cutoff. No effective cutoff at v=107 is given.
The proof's o(1) codegree step cannot certify this finite instance.
The distance-four optimal constructions are outside distance ten.

Bailey–Burgess, [arXiv:1107.4120v2](https://arxiv.org/pdf/1107.4120v2),
Definition 2.1.1, printed p. 3, allows unequal positive block part
sizes and all admissible t-subsets, but fixes that profile. This
terminology identifies relevant families; it does not justify taking
a union of independently constructed profile packings.

Reuse Xu–Chen's graph input exactly as cited in L043 and
`2026-10-10-finite-nine-set-packing-lower-bound.md`: baseline
107^5=14025517307. Its stated small augmentation bound is
14025517325, below the benchmark. No graph reproof is needed.

## Relevance, duplicates and bounded continuation

The main gap is arbitrary-center safety at 67/68 agreements. L041/L042
motivate testing whether a large ordinary local packing obstructs the
sufficient labeled-cap certificate; even success supplies no RS list.
L043 and ATTEMPTS/027 stop only resource exclusion, and L044 and
ATTEMPTS/028 stop only the quoted Derksen prescription. Targeted
searches of the October 10 assessments and histories 120–129 found
no completed mixed-profile greedy compatibility calculation.

Search terms included `constant weight codes generalized Gilbert bound
multiply constant weight codes finite construction packing` and
`Xu Chen 1505.06524 constant weight codes augmentation`. Search hits
were discovery aids; conclusions above use inspected primary passages.
No novelty follows from the bounded search. The product construction
is a read lead, not a ready numerical input without its constituent
codes. No essential source blocker remains for a greedy-method test.

Propose one bounded test: exact finite Gilbert closed-neighborhood
counts for the entire restricted universe and, separately, each
single decreasing-profile class across all column assignments. Use
actual mutual conflicts, not only used five-subsets. A threshold-crossing
certificate would justify a later packing/deletion application; a
shortfall parks this greedy prescription only. The proposed test
requires its separate approval assessment before mathematics.
Essential inputs are L043's universe and cited graph baseline;
L041/L042 are downstream only and L044 is a contrast. Unresolved
assumptions remain actual-label transfer, cross-core consistency,
common-center RS realization, 67/68 safety and ABF comparison.
Full matching Mathlib coverage is not checked. No lemma, numerical
bound or construction was derived during this literature-only step.
