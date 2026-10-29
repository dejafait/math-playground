# Ratio spectral calculation — working record

Approved target: Certify a one-sided cyclic spectral upper bound for L123's pair-intersection sum on every 61-point core and compare its Bonferroni survivor bound with 1600876449624.

Main gap: arbitrary-center 67/68 agreement safety. Intermediate target:
a uniform ratio-sensitive upper bound on the unordered pair sum for any
61-element K in H. Possible downstream use: local-link diagnostics;
selected-family transfer and threshold saving remain independent gaps.
Continue only for a certified strict improvement over 1600876449624;
otherwise park this scalar certificate (a precision straddle is inconclusive).

Inputs read: full L123, L122, C122a; parent source comparison and supplied
ready SPECIALIZE assessment; ATTEMPTS/010 and /019. Preserve their stops
and unfinished L121 work. No cross-notebook inputs. Classification:
REPRODUCTION of the cited finite Fourier/Rayleigh/Bonferroni method.

Planned specialization: index H by h^i (h=19139), w_0=0,
w_j=d(1,h^j), A_ij=w_(j-i mod 1024). Inverse symmetry makes A real
symmetric. Gray's Fourier diagonalization supplies all modes. With row
sum R and x=1_K-(61/1024)1, the quadratic form is
R*61^2/1024 + x^T A x, with norm squared 61-61^2/1024.
Use the largest algebraic nonconstant eigenvalue, then divide by two
for unordered pairs and apply L123's event model and Bonferroni direction.

Certification plan: exact dyadic enclosing arithmetic at 128 fractional
bits; positive half-angle roots from cos(pi/2)=0 to cos(pi/512), then
cos(2a theta)=2 cos(a theta)^2-1 and
cos((2a+1)theta)=2 cos((a+1)theta)cos(a theta)-cos(theta).
All cosine arguments for this construction are in [0,pi/2]; reflection
extends the table to every residue. Save exact square-root inequalities,
all recurrence operations, all modes, hashes and rational comparisons.
Allow one 256-bit retry only on a threshold straddle. No numerical FFT.

Completed at 128 bits; no retry used. Canonical proof: L124. The full
certificate is `scripts/finite-support/ratio-spectral-bound.json`; its
complete verifier writes `scripts/finite-support/ratio-spectral-verification.json`.
All 2386 production and 2355 verification checks pass, including all
1023 nonconstant modes. Uniform pair energy <=120815550367; survivor
upper <=1597620964591, improving the comparison by 3255485033. This is
a local reproduction of known methods, not a new general theorem.
No selected-family or RS inference is made.

The strict continuation test passes. Separate critical audit remains
pending; its uncovered scope is recorded REVIEW_REQUIRED for next turn.
