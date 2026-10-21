# One full-variable exact-cardinality attempt — step 364

The approved target is exactly the TARGET in
`literature/2026-10-20-free-cardinality-zero-block-feasibility.md`.
The main gap is arbitrary-center 68-agreement safety. Inputs L001,
L021,L023,L098 and foundations/04,12,13 supply necessity and the
normalizations; foundations/10 supplies general exact elimination.
No old pair or column assignment is imposed. ATTEMPTS/033,034,067,068,
080,081 retain their original scope.

Acceptance requires a complete rational feasible witness or an exact
original-coordinate contradiction. The former would park this relaxation;
the latter could support safety, subject to a separate critical audit.
A failed candidate or cap leaves feasibility open and parks this numerical
prescription. The 67-agreement question, omitted PSD blocks, representing
measures, RS realization and ABF comparison remain unresolved.

Implementation checkpoint, before construction: enumerate all ordered
orbits, quotient only the sorted distance triple together with t-s,
and lift Boolean repetitions to pair coordinates. Keep forbidden values
zero. Store complete integer factor recipes and the ordered map.
Independently check source factors against four-region counts and
the literal zero-label beta sums. All numerical scalings will be
invertible powers of two, fixed before the sole run, with every row
participating. The run is capped at 200 sweeps/600 numerical seconds;
the entire construction and verification at 1800 seconds, 20 million
source-orbit coefficient visits, 2 GiB live arrays and 512 MiB output.
One rounding to multiples of 2^-40 is permitted, with exact equality
elimination afterward. No convergence or rational-attainment assumption.

## Completed bounded attempt

The lossless model and sole proposal are
`scripts/finite-support/free-cardinality-zero-block-model.json`,
`free-cardinality-zero-block-model.npz`,
`free-cardinality-zero-block-numerical-contract.npz`, and
`free-cardinality-zero-block-proposal.npz` in that same directory.
The model stores every original ordered orbit, its exact class lift,
all integer D and beta factor arrays, all pair coefficients, every
scaling exponent, and the fixed update rule. Different t-s values are
never identified. The all-forbidden class is fixed zero; pair
coordinates 0 through 68 remain explicit.

There are 1,500,625 original coordinates, 269,779 coordinates after the
source lift, and 269,774 free coordinates before cardinality. The
4,501,875 ordinary scalar rows, 68 spectral pair rows, 69 pair signs,
all 69 contractions and both full 69-by-69 matrices participate.
All six presentations of every permitted distinct class were checked,
giving 1,618,260 presentation checks. There are 205 repeated orbits
in all; 12 also have a forbidden distance, leaving 193 permitted
repetitions. Forbidden-first evaluation accounts for this difference.

### Numerical contract and exact reconstruction

Use p_i=2^-37*x_i for nonzero pair indices and y=2^-74*x_q for
distinct permitted triples. Fix p0=1 and forbidden values zero.
Initialize permitted p_i=N/binomial(1024,68) and distinct y to the
square of that density; this is only a proposal, not a feasible point.
All other row and block scalings are stored integer powers of two.
The two PSD scalings are a positive diagonal congruence followed by
positive scalar multiplication; they are invertible. No pair moments
from L021–L098 are loaded or fixed.

Each sweep evaluates all scalar/pair negative parts, every contraction
residual, the objective residual, and the negative spectral parts of
both full matrices. Sum their adjoint residuals and subtract one half
of this gradient divided coordinatewise by the fixed row-l1 diagonal
majorizer saved before iteration. Restore only the prescribed fixed
coordinates. No convergence theorem or numerical proof is claimed.
The sole run completed 200 sweeps in 16.5542 seconds, reaching the
sweep cap before the 600-second cap. Its final pre-update diagnostics
still have nonzero residuals; the saved final proposal is the point
after the 200th update.

Round each scaled nonpivot coordinate once to a multiple of 2^-40,
ties to even. First solve the objective for p68. Then, for each
i=5,...,68, solve contraction i for the class (i,i,i,u=i).
Its only ordered presentation is (i,i,t=i,s=0), so it occurs only
in contraction i, with positive coefficient binomial(956-i,i).
The first pivot coefficient is g68>0. Thus this selected equality
minor is triangular with 65 nonzero pivots. Rows 1 through 4 are
zero identities; row 0 is the objective. This is exact elimination
of the saved equations, not a restriction on the free moment choices.
It leaves 269,709 independent nonpivot coordinates.

The full rounded vector and all 65 rational overrides are in
`scripts/finite-support/free-cardinality-zero-block-reconstruction.json`.
All 69 original contractions have exactly zero residual, but the
permitted original orbit (i,j,t,s)=(10,10,10,0), h=10, has value

    -98830325787762151105959048255149452902042647317403513358695570234161255291702140324301897199796951946612309277
    /40676987401566199872806611802174957804227523247071035392.

The denominator is positive. This violates the original scalar y>=0
and rejects this complete reconstructed point. It is not a dual
separator, an infeasibility proof, or a verdict on other assignments.
There is no reason to complete expensive PSD certification of a point
already failing a required scalar. Other signs and rational PSD
congruences are not claimed verified.

### Independent verification and caps

`scripts/finite-support/free-cardinality-zero-block-verify.py` imports
no constructor routine. It enumerates all original incidences again,
reconstructs each class and D by factorial counts of included points
in the four regions, and substitutes the entire saved assignment.
It checks the exact objective, all 69 contractions, every original
orbit lift, the nonzero triangular equality pivots, and the displayed
negative scalar. Full evidence is
`scripts/finite-support/free-cardinality-zero-block-verification.json`.
It completes in 6.2472 seconds with no verification failures.

Actual / allowed work:

- Original coordinates: 1,500,625 / 1,501,000.
- Scalar, spectral-pair and pair-sign rows: 4,502,012 / 4,600,000.
- Contractions: 69 / 69; full matrices: 2 / 2, each 69-by-69.
- Source-orbit coefficient visits, including verification:
  9,121,385 / 20,000,000.
- Conservative declared live-array bound: 746,538,504 / 2,147,483,648 bytes.
- Saved output at constructor completion: 39,027,059 / 536,870,912 bytes;
  the small independent verification and scripts also remain below cap.
- Largest saved reconstructed rational: 785 / 262,144 bits.
- Constructor: 24.5024 seconds; independent verifier: 6.2472 seconds,
  within the 1,800-second construction/verification cap.
- Numerical sweeps: 200 / 200; numerical seconds: 16.5542 / 600;
  rational reconstructions: exactly one.

No resource bound was exceeded. The first stopping bound was 200 sweeps;
the first exact acceptance failure was the negative scalar above.
The unchanged largest contraction residual in the floating diagnostics
is not evidence for equality: only the subsequent exact substitutions
establish the reconstructed equalities.

This is REPRODUCTION/EXPLORATION: a fully specified bounded attempt with
an independently verified failed candidate, not a mathematical advance
or a uniform negative result. Park this numerical prescription under
ATTEMPTS/082. No second solve, rounding, pair fixing, parameter scan or
old-control retuning is covered. The free-variable system and the
955–957 bracket remain unchanged. PROOF.md and DAG.md do not change.
Full matching Mathlib coverage remains not checked.

A different proposed continuation concerns a pole of order three
and 67 agreements. L019 and its old assessment cover only 66 agreements;
they do not approve this changed target. Its new assessment is
REVIEW_REQUIRED. No new dictionary, fiber count or source conclusion
for that family was derived here.
