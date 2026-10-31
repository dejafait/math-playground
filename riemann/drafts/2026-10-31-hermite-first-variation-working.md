# Coupled Hermite first variation: bounded attempt

Approved target and source scope: the unchanged EXPLORE assessment
`drafts/literature/2026-10-31-hermite-coupled-first-variation-test.md`.
Main gap: actual-Xi all-degree positivity. Test the proposed sign
B_N=2P_N'R_N'-P_NR_N''-R_NP_N'' on the actual moving intervals.
Downstream use would be to replace the linear loss by a quadratic tail;
D(P_N) margins, that quadratic term, multiplicities and higher forms
would still need independent control.

Continuation/stop test: start T=1, N=64, and permit only the specified
probes 1,5/4,3/2,7/4,2. A complete enclosure with upper endpoint below
zero stops this sufficient mechanism; positive samples prove no interval
sign. No division by a real jet, assumption of simplicity or arbitrary
grid enlargement is allowed.

Read L564 completely, C567a's full proof and completed analytic/arithmetic
audit, the conclusions of L565/L566 and the parent comparison's relevant
source and failure passages. Prior work remains intact. C567a's negative
evaluations lie outside the target intervals and are not inputs to the
new sign. Its certified actual coefficient intervals are reusable data;
their applicability and precision for this different expression must
be checked. Romik's expansion and derivative bounds are imported through
L564, not rederived or independently source-audited.

First bounded calculation planned: write R_64 as the sum of indices
65 through 256 plus R_256, use the audited coefficient enclosures for
the finite part, and apply L564 (4) through derivative order two to the
remainder. This retains actual coefficients without subtracting two
nearly equal approximate values. It is an exact decomposition, not a
sign argument. The computation and a justified coupled-integral formula
are pending; no sign is established at this checkpoint.

Completed bounded test: the first probe t=1 gives a strictly negative
complete rational enclosure, including R_256 and its two derivatives.
The proof, all hypotheses, exact bounds and qualifications are now
canonical in L568; the full calculation is
`scripts/hermite-gram/first-variation-certificate.json`.
All three contributions to B_64(1) are individually negative. The
stopping test has fired, so no further probes or putative positive
symmetrization are pursued. This is an informative local obstruction,
not a sign conclusion for D(Xi), a new source theorem or an audited
resolution. The fresh certificate awaits a separate verification turn.
