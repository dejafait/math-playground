# Gaussian growing-background cancellation test — 2026-10-04

The saved SPECIALIZE assessment in
[the first-spectrum review](literature/2026-10-03-gaussian-regulated-first-spectrum.md)
covers the exact unchanged large-frequency sign target. No further
literature search is needed for this invocation. Existing L358–L361,
their scripts, certificates and stopped implementations are preserved.

The main gap remains actual-theta mixed positivity and low-index signs
at unbounded heights. The current intermediate test concerns the
shrinking-value prerequisite in L359: can completely multiplicative
unit phases give an exact zero of the damped series for every
sufficiently small regulator? A regular zero would permit nearby
value adjustment. Nonzero weighted logarithmic derivative, the
gamma rotation, actual-frequency realization and higher signs would
remain unresolved.

Put R=ε^(−1/2), a_R(n)=n^(−1/2)exp(−π(n/R)²), and
N=ceil(R sqrt(8 log R)). Allow phases throughout the growing prime
range through N, with +1 above N. Select P={p prime:R<p≤16R}.
For large R, N>16R and N<R²; the truncation through N is affine
in the phases of P, because no retained integer has two factors
from P, counting multiplicity.

Randomize all remaining primes through N independently on the unit
circle. Unique factorization makes distinct integer monomials
orthogonal, so the part B with no P factor has
E|B|²≤1+log N. Each selected coefficient A_p differs from a_R(p)
by at most a_R(p)Σ_(m≥2)m^(−1/2)exp(−π(m²−1)), less than
a_R(p)/1000, uniformly in the background. An elementary binomial
argument should give #P≥cR/log R, hence total selected amplitude
L≥c′sqrt(R)/log R, whereas max_p|A_p|=O(R^(−1/2)).

Choose a background with |B|≤sqrt(1+log N), divide selected
amplitudes into three nearly equal groups, and align phases within
each group. Three group rotations then make a triangle cancelling
B. Its two-variable real Jacobian should have smallest singular
value comparable to L. The infinite tail and its first two group
derivatives should be O(R^(1/2−2π)), allowing a contraction to
preserve an exact regular zero of the full series.

Continue if these uniform estimates establish exact regular phase
zeros for all sufficiently large R; abandon this implementation if
the background or infinite tail has the same scale as the selected
amplitude, or if the triangle has no quantitative regularity. The
required sign still needs L359's derivative/rotation conditions at
actual frequencies; a zero template alone is not a negative sign.

Initial unfinished checkpoint: prove the elementary prime lower bound,
check random-background orthogonality and coefficient dominance,
and write the full-series contraction and its qualifications. No
zero existence or spectral sign is asserted at this checkpoint.

## Completed test

The full informal proof is
[L362](../lemmas/L362-gaussian-growing-prime-phases-have-regular-zeros.md).
The initial value-only outline was refined to three separated prime
windows so that their different logarithmic weights retain a nonzero
derivative at the cancelling triangle. Centering that derivative by
log(aR) removes the common growing weight. The elementary binomial
argument supplies enough primes in each fixed-ratio window without a
prime-number-theorem error term.

Random background phases give simultaneous bounds O(sqrt(log R))
for the value and O((log R)^(3/2)) for its centered derivative. Both
are o(M), where M≥c_a sqrt(R)/log R is a common selected group
amplitude. Each selected coefficient is its prime term plus an
arbitrarily small relative correction, by fixing a large enough.
The cancelling triangle has a Jacobian of order M and a nonzero
centered derivative of order M. The full infinite tail, with its
first two group derivatives, is O_a(R^(1/2−2π)); a contraction
retains an exact regular zero and the derivative margin.

This establishes exact zero templates with a nonzero weighted
logarithmic derivative for every sufficiently small regulator,
rather than a further finite-threshold scan. L335's qualitative
finite-phase visit argument, applied to finite value/derivative
truncations with absolute Gaussian tails, gives actual values as
small as desired at arbitrarily late frequencies, with derivative
bounded away from zero. Thus L358's bounded-away-from-zero premise
for a conditional positive tail is unavailable in this range.

The achieved rate is still below the actual required result: the
visits have no quantitative relation between value error and log ξ.
A zero template itself leaves the leading first sign nonnegative;
L359 instead needs the displaced cancellation ωS≈iS′ and a suitable
gamma rotation at the same actual frequency. No negative sign for
arbitrarily small ε, new actual-theta sign/exclusion range, or RH
candidate follows. Local regularity justifies continuing with those
occurrence conditions; the fixed-head and shell failures stay parked.

The outcome is ADVANCE as a relevant local mathematical input, with
classification REPRODUCTION of the elementary phase, prime-count,
Gaussian-tail and contraction tools. No originality beyond the
checked literature is claimed. Verification consists of the
displayed analytic estimates and the shared documentation checker;
no numerical prime-phase experiment or uncertified sign enters the
argument. The ready assessment still matches the exact saved
spectral target; the sole current Next action is in PROGRESS.md.
