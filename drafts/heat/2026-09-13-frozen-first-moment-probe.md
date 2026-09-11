# Actual frozen first-moment probe — 2026-09-13

Scope: a finite-scale computational part of the first-moment question after
L172, preserving the completed earlier work. No asymptotic claim is proved.
Use exactly L170's amplitudes and L171's variance normalization, with
T=2πN², H=T^(3/4), and the first, middle and last equal blocks.

For a midpoint mesh of width d on a block, the exact-arithmetic error in
its average of |Z| is at most d Σ_n |z_n λ_n|/4. Indeed |Z| is Lipschitz
with that sum as constant, and the integral of distance to the midpoint
of a cell is d²/4. This handles zeros of Z without differentiating |Z|.
The variance integral will be evaluated by high-order Gauss quadrature;
floating-point output is exploratory, not an outward-rounded certificate.
Compare two time meshes and two variance quadratures, and independently
compare the sampled second moment to its exact finite sinc expansion.

Checkpoint: implement scripts/heat/probe_frozen_first_moment.py, run it,
and record the observations and remaining asymptotic question here.

## Completed finite-scale calculation

Reproduce from the repository root:
`python3 scripts/heat/probe_frozen_first_moment.py > scripts/heat/frozen-first-moment-probe.json`.
Requires Python 3 and NumPy (run with NumPy 2.5.3). The JSON retains all
12 observations, mesh differences, and exact-formula second moments.

| N | First block | Middle block | Last block |
| --- | --- | --- | --- |
| 16 | 0.928927 | 0.950172 | 0.885456 |
| 32 | 0.924988 | 0.897758 | 0.888648 |
| 64 | 0.884561 | 0.857482 | 0.845380 |
| 128 | 0.870695 | 0.850737 | 0.830298 |

These are estimates of E_j|Z_j|, using V(u_j), not the sampled second
moment, for normalization. Block indices are zero-based in the script.
Both endpoints n=N and n=2N are included, as required by the definition.
The mesh widths are at most 0.1 and 0.05. All first-moment changes under
refinement are below 6.1e-7. The exact-arithmetic Lipschitz error bounds
for the fine mesh range from 0.0129 to 0.0406; these deliberately coarse
bounds must not be replaced by the much smaller refinement differences.
The 64- and 128-point variance quadratures agree to relative 1e-11.
Neither their errors nor floating-point roundoff are certified.

For independent normalization/phase verification, the script uses

E_j|Z_j|² = Σ_(m,n) z_m z_n cos((c_j−π/2)(λ_m−λ_n))
                    sinc(h(λ_m−λ_n)/2),

where sinc(x)=sin(x)/x, with value one at zero. NumPy uses sinc(x/π)
for this convention. This formula follows by integrating each exponential
on the centered block, including the diagonal. The largest discrepancy
from the fine time mesh is below 3.3e-7. The script also checks it against
the midpoint bound with Lipschitz constant 2(Σz_n)(Σz_nλ_n).
All coefficients and frequencies here are nonnegative, so these constants
are valid without absolute-value cancellations. The script's assertions
are consistency tests in floating point, not certified inequalities.

The sampled first moments are of order one at these scales, with some
modest decline. This neither proves a positive asymptotic lower bound nor
excludes decay to zero. Only three blocks per scale were sampled; no claim
about a minimum over all blocks is made. In particular, the L172 obstruction
has not been established. This completes a precisely scoped numerical
part of the requested estimate; the asymptotic analysis remains unfinished.
No new proved lemma, DAG input, or change to the overall proof is warranted.
