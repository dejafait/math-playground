# Proposed cutoff and degree-average recovery test — source contracts ready

TARGET: Test whether two-sided subexponential bounds for A_n(X_n) and P_n(X_n) are equivalent, quantifying common-cutoff tail and Cesàro inverse losses, and identify any independent estimate supplied by averaging.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step234's completed exact degree-average source comparison in 2026-11-10-prime-laguerre-degree-average-review-233.md, including the scoped duplicate/failure check. This target isolates its unpaid cutoff/recovery application; it does not request a fresh bibliography or a bound on the average.
SOURCE_EVIDENCE: Ross arXiv2210.08091v1 Prop3.4 p7 and its triangular-system proof, Prop4.2/Cor4.3 pp10-11 with complete proof and coefficient identification; DLMF1.15.4-7 for terminology. L981 and L982 are the audited local cutoff and normalization inputs, whose complete relevant proofs were read in step234.
COMPARISON: The algebraic inverse is standard and valid for arbitrary complex sequences; the actual moving-cutoff array is not directly the fixed sequence in that theorem. The remaining work is quantitative specialization, not a new summability theorem or creative cancellation mechanism.
GAP: Neither equivalence nor explicit inverse/cutoff losses has been derived for this array. An independent signed estimate for A_n remains unproved even if recovery succeeds. The implication from an upper bound alone is outside this target.
REASON: Coverage supports a bounded mathematical test after separate approval. Resolving exact losses can stop automatic-smoothing speculation without more lobe samples or inaccessible-source work. No result is proved or certified by this nomination.
SCOPE: Only actual Lambda and L981's P_k(X), k>=2, full prime-power endpoints, X_n=exp(10000*(n+1)^4), A_n(X)=(n-1)^(-1)*sum_(k=2)^n P_k(X), n>=2, and the every-epsilon two-sided threshold. No RH, simple zeros, head sign, fixed common X as n grows, or uniform exchange of limits is assumed.

## Exact bounded question

For each of the two sequences A_n(X_n) and P_n(X_n), the threshold
to compare is: for every epsilon>0 there exists a finite C_epsilon
independent of n such that the absolute value is at most
C_epsilon*exp(epsilon*n) for every integer n>=2.

The main gap remains actual-Xi positivity and the signed Li forcing
of L966/L968. A recoverable average could be useful only if it has
an independently payable estimate. This test establishes or rejects
the proposed recovery interface; it does not attempt that estimate.

The essential local mathematical inputs are L981 and L982, using
exactly their actual arithmetic function, compensator and cutoff
conventions. L980 and L968 provide downstream context only. L983's
positive pair is historical evidence against the preceding spatial
sign rule, not an input to an averaging identity. No cross-notebook
result is involved.

Use Ross, *The Cesaro Operator*,
[arXiv2210.08091v1, Prop3.4, p7](https://arxiv.org/pdf/2210.08091v1#page=7),
as the cited algebraic inverse rather than reproving general matrix
inversion. The source includes every complex sequence and no
convergence premise. Its initial row and the shift from index0 to
degree2 must be checked. The analytic inverse in Prop4.2/Cor4.3 is
available for comparison but is not needed if direct sequence
estimates settle this exact question. No new singularity theorem,
RH-equivalence criterion or saddle asymptotic is requested.

The application must account explicitly for the average with degree
n-1 evaluated at X_n versus at X_(n-1). Check that each invoked
L981 lower cutoff is met, including the smallest index2. Use L982
only with the degree fixed when taking its real-endpoint limit.
If introducing the averages of S_f(k) as a bridge, justify every
finite summation and every error bound; do not exchange growing n
with a cutoff limit. Polynomial inverse losses must be paid at the
every-epsilon scale, not suppressed by notation. Both directions
need proof; one-sided control is a distinct question.

## Continuation or abandonment test

Produce explicit valid losses or an actual failure of a proposed
implication. If equivalence holds with no independently supplied
arithmetic estimate, record that automatic first-order smoothing
has not weakened the unpaid threshold. That closes this precise
automatic-payment claim, while leaving independently proved bounds
for averages as a possible future mechanism. Do not manufacture a
new lemma solely to record an elementary source specialization.

If a concrete new signed inequality emerges, preserve it as an
uncovered nomination for later assessment rather than prove and
approve it in the same step. Additional source work needs a specific
changed hypothesis; the current sources are accessible and adequate.

This ready assessment was newly written in literature step234 and
receives separate supervisor approval next turn before mathematical
invocation. That approval need not repeat unchanged browsing.
Full matching Mathlib coverage is unknown; no claim of absence or
originality is made. The anticipated work is ordinary algebraic
calculation and tail bookkeeping, classified REPRODUCTION.
