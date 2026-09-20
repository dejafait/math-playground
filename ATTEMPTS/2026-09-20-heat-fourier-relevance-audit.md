# Heat/Fourier relevance audit — 2026-09-20

This is a strategic review of existing results, not a new lemma or a
counterexample to RH. The working tree was clean at entry. The whole
proof overview and canonical DAG were inspected before selecting this step.

## Final target and the proposed local target

The shortest recorded assembly is Corollary 32a: for the actual reciprocal
zero power sums, H_d=(S_{m+n+2}) for 0<=m,n<=d must be positive semidefinite
for **every** d. L030 and L032 then force real reciprocal nodes; L026 and
L018 convert this into RH. The requirement is every real coefficient
vector having nonnegative quadratic form, not just positive diagonal
entries or any fixed finite collection of matrices. No such all-degree
estimate is supplied by the later Fourier branch.

The local target in [L230](../lemmas/L230-finite-fourier-reduction-with-endpoint-control.md)
is F_H=o(B_0), H=ceil(N^6). Together with L227–L229 this would give
C-B_0=o(B_0) and the interior comparison E_full=o(T). Here h is comparable
to N^(3/2), and c N²h/log N<=B_0<=C N²h. Thus
F_H=o(N²h/log N) is a sufficient absolute target; it is not claimed necessary.
[L231](../lemmas/L231-second-derivative-budget-for-the-paired-fourier-sum.md)
only supplies O(N²h log N) via bounded sawtooths, a relative bound
O((log N)^2), rather than o(1). Its summed derivative bound is weaker.

The proposed k<=N^(1/4) calculation treats only part of a sum extending
to N^6. Even granting little-o for that entire low-frequency part leaves
an unbounded-in-the-required-sense high-frequency remainder. Cancellation
between the two parts could also matter; separate smallness is sufficient,
not necessary. No claim of failure of the actual discrepancy is warranted.

There is a further sign warning: [L221](../lemmas/L221-real-main-term-exceeds-the-target-scale.md)
proves M_tot/N³ tends to infinity and says the proposed Q_N=O(N³) would
require E_tot/M_tot=-1+O((log N)^2/sqrt(N)). A negligible discrepancy for
that *total* sum would contradict that proposed bound. L230 concerns an
interior restricted comparison, not E_tot; neither its hypothetical
smallness nor its negation settles the total signed comparison. A claim
that all progression errors should simply be small would lose this distinction.

## Where a heat-route completion would still be needed

The center-estimate motivation already has a precise audit in L135:
a common strip on a heat interval and a uniform logarithmic
maximum-to-center ratio would give logarithmic local zero counts.
Both are additional hypotheses there. L148 gives a sufficient lower-bound
threshold at just the fixed slice lambda=-1 and center t+3i/2:
|S(t)|>=d t^(-delta) for all sufficiently large t, with delta<3/2
(or delta=3/2 and d>B), dominates its correction envelope.
This is not a common-parameter estimate or the full ratio estimate.

[L154](../lemmas/L154-moment-information-and-a-truncated-tail-criterion.md)
explicitly limits its tail criterion to a positive-proportion conclusion.
Even proving that criterion leaves an exceptional set uncontrolled; it
cannot be substituted for the above all-t lower bound. The quartic,
profile and arithmetic reductions have not supplied an alternative
argument handling that exceptional set or excluding all off-line zeros.

Even granting the local counts would not complete the heat route.
L133 controls exterior interactions under a common strip, but leaves the
buffer annulus, location of height maxima and uniform time remainders
uncontrolled. [L126](../lemmas/L126-fixed-slice-motion-selection-and-supremum-obstruction.md)
and L128 already isolate the decisive missing passage: static or
bounded-domain velocities do not prove an upper Dini derivative bound
for the whole-plane moving height supremum. A proof would need a valid
uniform global evolution estimate, applicable initial bounds and a
comparison reaching zero height at lambda=0. None is established by
F_H=o(B_0). This is a list of missing implications, not a conditional
RH theorem with silently assumed hypotheses.

## WHY IT FAILS and route decision

Continuing with a low-frequency lemma fails the relevance test: its
success would neither meet the full Fourier threshold nor repair the
independent average-to-uniform and local-to-global gaps. These gaps are
already documented, including the canonical L126 counterexample to the
abstract supremum inference. No new mechanism connecting this calculation
to a final proof was identified. Park this technical extension; retain
all its results and the canonical graph. Reopening it requires an explicit
completion mechanism addressing these gaps, not another special estimate.
The all-degree positivity gap remains unchanged; no candidate or disproof
has emerged. Reviewing the essential polynomial-detection proof is a
better justified use of the next step than extending this detached branch.
