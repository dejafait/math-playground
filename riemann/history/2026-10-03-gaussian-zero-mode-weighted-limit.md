# Research history — 2026-10-03

## Exact subtraction repairs the regulated approximation

STEP_ID: 2026-10-03-gaussian-zero-mode-weighted-limit-01.
ADVANCE; RESEARCH; REPRODUCTION. Reused the prior ready SPECIALIZE
assessment without additional browsing and performed exactly its
saved weighted whole-line approximation test.

[L357](../lemmas/L357-gaussian-zero-mode-subtraction-repairs-weighted-convergence.md)
proves |k_ε−k|≤Cε exp(−5|u|/2), including the region e^(2u)
comparable to ε. Its weighted L¹ error is at most (132/125)Cε.
The two Fourier derivatives and their first Laguerre combination
converge uniformly in absolute error. This meets the requested
approximation threshold and repairs the Gaussian family's
whole-line mass problem; L235's different finite averages and
L356's separate-parity stop remain preserved.

The mechanism imports the known scalar Poisson identity, keeps
every derivative of the zero mode and prefactor, and uses the
dual small-parameter and original large-parameter derivative bounds.
This is a local reproduction using the covered theta tools, not a
claimed discovery beyond the checked literature. The recorded
sources did not state the full regulated weighted limit.

The main gap is unchanged: neither a nonnegative first spectrum
for these approximants nor the missing higher low-index signs is
established. Absolute O(ε) error gives no sign margin at unbounded
frequency. This is why the next direction tests the regulated
family's own first spectrum, rather than adding approximation
variants without a positivity mechanism. That changed target is
outside the old review's scope and has a fresh REVIEW_REQUIRED
[assessment](../drafts/literature/2026-10-03-gaussian-regulated-first-spectrum.md).
No mathematics for the new target is attempted in this step.

The DAG adds only L016 and L019 as direct mathematical inputs to
L357; L235 and L233 are comparisons and motivation in its proof,
not additional premises. PROOF.md records the repaired approximation
and its missing sign. The checkpoint reports the local advance,
unchanged actual-zeta sign/exclusion ranges, zero of three unresolved
mathematical exploration turns, and no RH candidate. STATUS remains
IN_PROGRESS. All prior unfinished artifacts are preserved.

Validation: exact Fraction arithmetic in
`python3 scripts/gaussian-zero-mode/check_derivatives.py` confirms
the operator, dual derivatives and normalization. The mathematical
proof uses analytic bounds; no numerical sign inference is involved.
`python3 ../scripts/docs/check_structure.py --problem riemann` passes
with 360 nodes and 817 edges. Metadata checks confirm one outcome,
the reused prior SPECIALIZE review, and exact matching of the new
Next action to its REVIEW_REQUIRED assessment. PROGRESS.md has 19
lines and PROOF.md remains within its 100-line limit. `git diff
--check -- .` passes. Hash comparison confirms that all 873 other
pre-existing Markdown/Python files, including the prior assessment
and unfinished parity work, are unchanged; only the three current
overviews were edited in addition to the five new artifacts.
