# Fixed nonzero-pole attempt — checkpoint before computation

2026-10-20, approved target from the unchanged fixed-nonzero-pole
SPECIALIZE assessment. Main gap: arbitrary-center 67/68 safety. Work
only on the displayed pole-3 family, not a pole sweep or new character
theorem. C012a, L001 and foundations/02 are mathematical inputs;
L099–L101 and ATTEMPTS/083–084 are comparisons and preserved stops.

Planned dictionary: write Z=X-3. The entire list is indexed by
67-subsets S with product_(x in S)(Z+3-x) congruent to c+bZ+aZ²
modulo Z³. Monic cancellation and divisibility should give strict
degree<64; the ambient-field converse and zero remaining rows must
be written out. Generator 3 has order 65536, so 3 is outside H.

Use G=(E[Z]/Z³)^*, of size (Q-1)Q², without claiming a smaller
container. Logarithmic unit coordinates give E^* times E². A nonzero
additive character stays nonzero for all powers 1,...,67. Filter H
in X via its index-64 indicator and apply the inspected Li–Wan
Lemma 4.1 to the CRT joint modulus X(X-3)³: nonprincipal sums have
absolute value at most 3 sqrt(Q)<769. Both excluded evaluations
0 and 3 have zero weight under extension by zero. Constant-only
characters have orders d=2,4,...,65536, multiplicities phi(d)=d/2;
their powers divisible by d have exact cycle sum 1024. Other powers
retain the bound 769. Do not import their old vanishing subset sum.

Proposed one upper certificate: principal binomial(1024,67)/|G|,
nonconstant contribution (1-Q^-2)*binomial(835,67), and all
constant-only contributions divided by |G|, using the full unsigned
cycle coefficients with weights 1024 at multiples of d and 769
otherwise. These coefficients and the final cap remain to be checked.
Preliminary arithmetic finds binomial(835,67)/T between 4780 and
4781, so this conservative estimate is unlikely to pass. No inference
about actual fiber sizes follows. Finish this one certificate; park it
if its exact allowance exceeds T. No retuning in this step.

Unresolved: complete rigorous dictionary, every CRT/power case, full
certificate and exact ratio. Afterwards a separate critical audit can
check the resulting proof and arithmetic; no main-boundary conclusion
is anticipated. Mathlib coverage has not been checked.

## Completed result

The checkpoint above is preserved as the pre-computation state. The
complete proof and exact certificate are now canonical in L102 and
scripts/coefficient-fibers/fixed-nonzero-pole-results.json. All 5853
checks pass; 4780<U/T<4781, so the single estimate is parked in
ATTEMPTS/085. No retuning, family exclusion or large-fiber conclusion.
A separate critical audit awaits its own source-coverage approval.
