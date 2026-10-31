# Fixed PF256 model — global comparison continuation

The startup EXPLORE assessment for the frozen P_* is reused unchanged.
This attempt concerns only its global H_k signs, 2<=k<=256. L561's
density, negative first polynomial sign and origin/tail proofs are
retained as inputs, not recomputed. They remain unaudited.

Main gap: actual-Xi all-degree positivity. Downstream use: a complete
fixed-model certificate would obstruct a generic finite-order transfer;
actual-Xi realization and its signed remainder would still be missing.

Bounded test: seek a determinant comparison that is uniform in x and
k<=256, using the exact reciprocal factorization or L561 (6). A bound
must preserve determinant cancellation, not just control individual
derivatives. Samples and existential positive ends do not join the gap.
If the comparison cannot provide an overlap, preserve the precise
uncontrolled term and park this mechanism rather than repeat it.

Prior evidence checked: L561 in full and the preceding working/history
records; the approved assessment already compares the finite-order
criterion and known transform results. No additional source is needed
for this attempt, and no new source theorem will be presumed.

Unfinished starting idea: factor the bilateral density into a causal
gamma270 kernel convolved with a fast conjugate exponential pair, and
its reflection. Test whether the slow repeated poles give a positive
determinant comparison strong enough to absorb the oscillatory pair.
This is a proposed calculation, not an established PF statement.

The comparison now has a concrete candidate proof. For d=A-1 and
epsilon=b/d, Schur expansion in the last two letters +/-i epsilon
gives a relative error at most

    beta=2*256^2*epsilon/(1-2*256^2*epsilon)
        =32768/1015807 < .033.

The bound is uniform over all partitions of length at most 256:
removing one box changes s_lambda(1^270) by a factor at most 256;
there are at most binomial(l+255,255) ways to remove l boxes, and
each two-letter skew tableau contributes at most (2 epsilon)^l.
An infinite Cauchy--Binet expansion of the causal density's derivative
determinant involves only these straight Schur minors and positive
factorial Vandermonde minors. The proposed transfer to p_* is an
Andreief integral of two ordered derivative-evaluation determinants
of the causal factor, using the already assessed Sra C.1. It avoids
needing C^510 regularity of the causal factor across its support edge:
only derivatives through 255 are distributed between the two factors.

Still to check before claiming the certificate: index shift N-k+1
with N=271; absolute convergence of the infinite expansion; the
zero-extension and convolution derivatives; every sign in Andreief;
and the fixed rational margin. Full details will be canonical in L562
if these checks succeed. This saved sketch alone is not verification.

Completed: the full argument is now in
[L562](../lemmas/L562-fixed-reciprocal-model-global-pf256-certificate.md).
It supplies global H_k positivity and invokes C.6 for strict PF256;
L561 supplies the retained negative polynomial sign. The rational
comparison is theta=983039/1015807, and all nine exact scalar checks
passed in `scripts/reciprocal-pf256/global-comparison-certificate.json`.
The proof remains unaudited. No effective tail-overlap computation is
needed by this argument, since it integrates positive ordered
determinants directly at every real center. No Xi transfer is supplied.

Continuation is a separately gated source review preparing independent
scrutiny of L561-L562; no new target is approved in this mathematical
turn. The new assessment records the exact standard-algebra passages
still to inspect and the analytical audit obligations.
