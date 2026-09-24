# Gaussian-window tail audit — 2026-09-13

Checkpoint: use L149's exact coefficients and off-diagonal majorant to truncate
at aN≤n≤bN, N=sqrt(T/(2π)), with a,b fixed. The normalized squared L2 error
should converge to the corresponding Gaussian diagonal integral, tending to
zero as a→0 and b→∞. This reduces the actual fixed-cutoff tail question to a
moving polynomial of order sqrt(T) terms, not a fixed finite polynomial.

Pending proof audit: for F=G+R, show
E[|F|²;|F|²>M]≤2E[|G|²;|G|²>M/4]+4E|R|².
A fixed number of original terms has vanishing normalized L2 mass and cannot
supply an approximation. No fixed-cutoff estimate for the moving core is
claimed. Resume with the diagonal limit, truncation boundary errors, and
constants in the event split before promoting any assertion.

Completed as L155. The diagonal complement integral and its mesh errors,
tail-transfer inequality, and failure of fixed-index approximation are proved.
The moving-core tail bound is explicitly unproved; the next task is recorded
only in PROGRESS.md.
