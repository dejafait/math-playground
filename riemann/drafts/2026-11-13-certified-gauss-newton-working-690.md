# Certified Gauss setup working checkpoint690

The supplied overview/DAG and ready SPECIALIZE assessment687 were read
before this REPRODUCTION calculation. Source-notes688 and C998k were
read in full; C998g Section1 fixes the scalar convention. Existing
notebook changes and the stopped bisection implementation are preserved.

Main gap: actual-Xi positivity and signed remote-plus-induced S3 coupling.
Target: all Gauss nodes AND weights for degrees63,81,117, separate
radii<=2^-512, setup<=5000000 scalar operations. Possible use: the
unchanged shared endpoint-bank square service. No sign transfer follows.
Continue this prescription only on BOTH thresholds; fail it at the first
unpaid case, excess work or exhausted finite schedule. No bank or complete
square error is inferred. Assessment687/source-notes688 suffice; no new
literature assessment or general convergence theorem is sought.

## Fixed prescription, saved before execution

1. Generate the rational positive mesh 1-j^2/16384, j=0,...,127.
   Evaluate exact signs by Bonnet recurrence, and require exactly
   (N-1)/2 disjoint sign-change brackets. Use imported simple-root count,
   parity and the exact zero root for completeness; no seed asymptotics.
2. Bisect every bracket exactly16 times, checking signs. Then permit at
   most12 interval-Newton updates per bracket. All polynomial point
   values are exact rationals, using the integer-scaled Bonnet recurrence
   with common D=2^640. No approximate table or unchecked point evaluator.
3. Enclose derivatives by the exact midpoint derivative plus/minus Mr,
   with M the smaller of the endpoint-valid bound in Proposition3(7)
   and the rational upper bound 4N^2/(1-hi^2)^2 for its interior bound.
   The latter uses 2^(5/2)/sqrt(pi)<4, N^(3/2)<=N^2 and
   0<1-hi^2<=1. Only already-inspected Proposition3 is specialized.
   Exclude zero before division; intersect the Newton image with the
   old interval. Failure of strict contraction is a failure case.
4. Round the intersected image outward without a unit-cost floor oracle:
   binary-search its center within the old dyadic interval until the
   cell width is<=the image width, then expand the cell by its width
   on both sides and intersect with the old interval. The last cell
   width is greater than half the image width, so this covers the image.
   Charge every comparison, halving, update and loop operation. All
   dyadic endpoints must remain on the D grid; exhaustion stops.
5. Once node width<=2^-550, recompute the derivative enclosure on that
   node interval and form exact rational weight endpoints from
   2/[(1-x^2)P'_N(x)^2]. Check weight and node radii separately against
   2^-512. Weight outputs remain exact rational intervals, so no
   floating conversion is assumed. Evaluate the zero-node weight and
   explicitly construct reflected nodes and copied weights.
6. Count real arithmetic, assignments, comparisons, loop control,
   constants, all interval endpoints, safeguards and conversion. Charge
   the integer-scaled recurrence as a scalar rational algorithm, with
   no claim about bit complexity. Certificate serialization and checking
   are proof-record overhead, not service operations; no timing is used.

Exact source inputs: Johansson--Mezzarobba, arXiv:1802.03948v1,
Section1(1),(3), Section2(5), Proposition3(7), pp1,4-5;
Alefeld--Claudio1998 Section5 Theorem2, scalar case, p6; DLMF18.2(vi).
Source URLs and inspected proof qualifications are canonical in
assessment687/source-notes688. Reopening the already-covered Proposition3
statement supplied its interior bound for implementation, not a changed
target or an additional literature turn. Full Mathlib match unchecked.

The script/certificate will retain every mesh sign and bisection choice,
exact point recurrence outputs and derivative/Newton endpoints for every
accepted step, all final rational weights, guards and the scalar ledger.
No witness, bank, signed S3 comparison or source-to-Xi contract is used.
Completion, failure and continuation are to be recorded after the run.

## First execution checkpoint

The fixed prescription stopped, without retuning, at the640-bit binary
conversion safeguard on the second positive root for N=63. The first
positive root and its weight passed both radii, but this is not all-root
success. First-run evidence is preserved separately. The next operation
is an exact failure replay with additional proof serialization only;
the numerical prescription and scalar ledger are unchanged. Do not
silently impose a different conversion stopping test during this step.

## Completed step

C998l now holds the canonical full proof, precise imported inputs and
qualifications. The stopped trace was reproduced with failure-only
serialization and checked by an unscaled rational recurrence replay:
3051 exact checks passed, with no change to the numerical prescription.
No further construction was attempted. This is a prescription-specific
precision negative; all-node accuracy and the full setup bound remain
unestablished. The current continuation is recorded only in PROGRESS.md.
