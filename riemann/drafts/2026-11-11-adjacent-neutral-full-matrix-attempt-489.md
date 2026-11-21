# Full finite-matrix attempt, step489

The unchanged ready step483 EXPLORE assessment approves the current
target. Main gap: L030-L032/C032a actual-Xi positivity. Intermediate
target: both entire C744l(2) matrices above I/25, using columns2,...,256,
all257 projection rows and every covariance/cross term. Together with
the retained C744j/k/l analytic payments this would imply a common
neutral margin >1/30 and could pay adjacent neutral interactions via
C744i(6); remote, non-neutral, odd and all-window signs remain open.

Reuse the step488 coefficient section and exact-integration procedure.
The bounded implementation will batch the very same power-log moment
functional, using exact integer convolution for the moment sequences
and GMP integer dot products for Gram entries. No new analytic
estimate, changed form, threshold or source theorem is proposed.
Compare all saved step488 entries, not a sampled eigenvalue, and
enclose both complete matrices before claiming a full finite bound.
Positive shifted LDL pivots establish the I/25 matrix bound; their
minimum is not an eigenvalue bound. Preserve all operands and errors.

Continuation test: complete all255 columns and both full shifted
factorizations with arithmetic widths <1e-30, or retain the exact
unpaid computation/error. A failed sufficient Schur budget alone does
not refute the original target. Only a certified exactly neutral smooth
ratio>=1/2 does so. C744i/j/k/l remain independently unaudited; a full
arithmetic certificate would still require a later analytic audit.
No RH, collar, shifted energy, H2 cap or cross-notebook input is used.

This draft preserves unfinished reasoning before the potentially
lengthy implementation. No full finite or all-space sign is yet claimed.

## Intermediate implementation checkpoint

All255 coefficient maps and all257 projected moments per action
column have completed. The per-column coefficient intervals, exact
batched power-log moment operands and L2 error operands are saved
under `scripts/adjacent-neutral/full-matrix-489/`. The complete Gram
assembly, covariance subtraction and full shifted LDL tests remain
pending at this checkpoint. The compilation first required correcting
the standard-header order before any arithmetic was run; that initial
failure and the corrected execution are preserved in
`scripts/adjacent-neutral/full-matrix-enclosure-489.log`.

The batched operation uses D=lcm(1,...,2049)^3. For midpoint integer
coefficient arrays p,q with denominator2^2048, it evaluates all
U_k=sum_i[p_i D/(i+k+1)-q_i D/(i+k+1)^2], k<=1024, and
V_k=sum_i[-p_i D/(i+k+1)^2+2q_i D/(i+k+1)^3], k<=256,
by exact signed integer convolution. Native GMP then evaluates
sum_k[p_(i,k)U_(j,k)+q_(i,k)V_(j,k)], with exact zero padding.
This is the same C744l(9) functional, with every mixed term retained.
All midpoint operands and native inputs are retained in compressed
files. Coefficient errors are charged before outward coarsening to
the512-bit matrix grid. A later full saved-operation replay is still
required; none of these checkpoints certifies a complete sign.

The complete minus-sign factorization has now passed all255 shifted
pivots, certifying S_T,-1>=I/25. Its largest head/Gram/covariance/Schur
interval width is <=4.325837624097e-153 versus1e-30 required. All
operands and factors are saved in
`scripts/adjacent-neutral/full-matrix-489/full-sign--1.json.gz`.
The minimum positive pivot lower endpoint exceeds0.2947956; this is
not an eigenvalue bound. The plus sign and complete saved-operation
replay remain pending at this checkpoint. No common full neutral
margin or independent analytic audit is yet established.

## Completed bounded attempt

Both full255-dimensional matrices are now certified >=I/25. All12
computation checks and all54 complete saved-operation replay checks
pass, with255 positive shifted pivots per sign. Maximum matrix widths
are <=4.325837624097e-153 and<=4.400421031409e-153, versus1e-30
required. Full coefficient, native input/output, error, projection,
matrix and factorization evidence is retained under the saved-data
directory. The summaries are `scripts/adjacent-neutral/full-matrix-enclosure-489.json`
and `scripts/adjacent-neutral/full-matrix-replay-489.json`.

C744l Section8 is the canonical proof and qualification record. Its
new(11) explains batched exact moments; (12) is the full finite bound.
There are no unpaid finite columns or couplings. The replay independently
implements the complete projected interval products in native integer
arithmetic, while retaining the same LDL routine. It does not independently
regenerate all coefficients or midpoint Gram products, or audit the
analytic input lemmas. Thus the proposed original-form mu>1/30 remains
conditional on those reductions. This is local exact implementation
progress using known tools, without a mathematical novelty claim or RH
conclusion. Earlier pending checkpoints above preserve the computation's
unfinished states; their pending finite tasks are now complete.

Continue the unchanged ready target by a fresh conceptual audit of the
energy/form normalization, exact neutral form domain, entire-complement
and mixed-term payments, and whole-map approximation transfer. These
are essential unreviewed inputs before claiming the full neutral margin;
they take priority over nominating an uncovered creative mechanism.
Preserve the degree128 and fixed-response stops, and all independent
remote/non-neutral/odd/all-window gaps. No assessment refresh or new
mathematical target was introduced in this step.
