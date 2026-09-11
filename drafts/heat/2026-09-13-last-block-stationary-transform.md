# Last-block stationary transform — 2026-09-13

Checkpoint: earlier L173–L174 steps are complete. Put a=(t−π/2)/(2π).
The stationary point for a log(x/N)−kx is x=a/k; the dual range is
(a/(2N),a/N), amplitude sqrt(a)/k and phase a log(a/(kN))−a−1/8.
The expected error is O(log N), since curvature stays comparable to one,
including endpoint slopes arbitrarily close to integers. This error bound
is not yet established here. Resume by checking a precise B-process
statement and its endpoint conventions before promoting this formula.
The dual range still has length comparable to N; retaining the phase is
necessary. No first-moment improvement is yet proved.

## Completed

L175 proves the formula with O(log(2N)) error using the C^4 transform
in Vandehey Theorem 1.1. The older C^3 bound in Robert Theorem 4 would
only give O(N^(4/5)) here and was not used. Conjugation fixes the
negative-curvature phase; all changed endpoint terms are O(1).
The first-moment question is equivalent for this moving dual sum;
the transferred second moment remains N+o(N). No decay is proved.
