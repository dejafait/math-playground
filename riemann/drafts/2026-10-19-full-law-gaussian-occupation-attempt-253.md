# Exact L438 occupation attempt — step 253, completed

Approved target: Determine whether L438's law has a nonzero limsup Gaussian occupation defect for L424's fixed test, retaining its moving Poisson bulk and all rare components.

Coverage: `drafts/literature/2026-10-19-full-three-prime-law-occupation-defect.md` (pre-existing EXPLORE). Main gap: global mixed positivity. Downstream use: discriminate this particular counterlaw from C^2 trajectory occupation; no realization or RH implication.

Result: NEGATIVE / RESEARCH / POTENTIALLY_NEW / proof_attempt. The
complete absolute statistic tends to zero, so the specified nonzero
limsup test fails. Full hypotheses, proof, source qualifications and
Mathlib status are in
[L439](../lemmas/L439-full-poisson-law-gaussian-occupation-vanishes.md).
The early candidate estimates saved here before lengthy work are now
proved there, with the direct logarithmic mean-square argument replacing
the proposed finite-head concavity comparison. No additional literature
or mathematical script was needed. No originality claim is made.

The result uses exactly the existing cutoff and full law. Its
basis-independent linear envelope includes translations and all
covariance entries; rare components use second integrals. No fixed-mixture
sign, moving Haar limit, phase independence or uniform integrability
is assumed. The continuation is separate critical-audit coverage and
review, not a stronger-rate demand. Actual/global realization, clipping,
capped nondegeneracy, L413's full-error regulator margin and global mixed
positivity remain unresolved.
