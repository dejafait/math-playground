# Quartic slice population checkpoint — 2026-09-14

Existing L203 and its validation are complete; earlier changes are preserved.
The target is its count (2) with eta=1/32 on actual integer triples.

Candidate reasoning, not yet promoted to a lemma: differentiation gives
P4 third derivative = (3 x0 / (8 b0³))(1-5j/(2b0)).
Since j/b0=O_t(N^(-1/2)), this is uniformly comparable to 1/N.
For each fixed nonzero integer frequency the foundations third-derivative
test should bound its exponential sum by O_(t,k)(N^(5/12)),
which is o(sqrt(N)). A periodic triangular function centered at 3/4
with radius 3/32 is supported in the required interval [21/32,27/32].
Its positive mean and absolutely summable Fourier series should give
a uniform positive proportion on every slice, hence order N³ in aggregate.

Resume by checking the derivative-test hypotheses, deriving the triangle
Fourier coefficients and controlling the tail uniformly, then writing
and validating a canonical result. Coprimality and totient selection
are outside this candidate claim and remain unproved.

Completed as L204. The fixed-frequency third-derivative estimate is
O_(t,k)(N^(5/12)), uniformly in actual slices of length comparable to
sqrt(N). The triangular Fourier minorant yields a proportion at least
3/64, proving the requested aggregate N³ bound. Arithmetic selection
is not included. Current continuation belongs only in PROGRESS.md.
