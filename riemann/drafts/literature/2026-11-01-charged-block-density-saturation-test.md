# Charged-block density saturation: bounded test nomination

TARGET: Calculate whether uniformly spaced conjugate blocks at displacement a/log T can obey the inspected density and unit-height count bounds while meas{t in [T,2T]: K_t>0}>=cT.
CHECKED: 2026-11-01
DECISION: EXPLORE
SEARCH_EVIDENCE: Exact zero-density/counterexample/interval, abstract Selberg density/spacing and horizontal-displacement/union searches; notebook-scoped density/multiset/saturation comparisons. No inspected matching model theorem was found; no originality is inferred. Full source comparison and queries are in 2026-11-01-charged-block-bad-height-measure.md.
SOURCE_EVIDENCE: Reuse that assessment's inspected Simonic arXiv:1910.08274v2 Theorem 1 and (74), including microscopic cases and Littlewood multiplicity convention; Dobner arXiv:2101.01747v2 Lemmas 5–8 and proofs. Reuse L464's Titchmarsh Theorem 9.2 unit-count input and the fixed-displacement assessment's closed-shell coverage; no new count theorem is proposed.
COMPARISON: Sources provide upper counts and a weighted exceptional-set result, not the exact charge-presence union estimate. Earlier C464c work changes a coefficient threshold; L486 concerns weighted energy. This test instead checks whether the inspected count constraints themselves exclude positive linear union measure in an abstract block family.
GAP: Construct a family or identify an incompatible quantitative constraint; verify every height/displacement count and clipped union measure. No such family, estimate or nonimplication is established in this nomination; Xi realization and all-height signs remain unresolved.
REASON: One concrete mathematical obstruction test is supported by the completed source review. A positive model would justify parking these count bounds as a sufficient mechanism, without disproving the actual-Xi target; failure must identify the exact missing compatibility. Separate supervisor approval is required next turn before the newly nominated calculation.
SCOPE: For each sufficiently large T, a finite multiset of blocks gamma+-id and their negatives, common positive integer multiplicities, gamma in [T,2T], 0<d<1/2. Start with d=a/log T for a fixed a>0 and equally spaced ordinates. Use C464c's strict charge rule only; these need not be zeros of Xi or satisfy its product normalization. Seek some fixed c>0 independent of T. Check the full dyadic density inequality and unit-height count condition below. No RH, simplicity of actual zeros, actual-Xi lower bound or complete analytic realization is asserted.

## Main gap, use and bounded test

Main gap: actual-Xi all-degree signs at unbounded heights. Intermediate
question: does the inspected count information already exclude a linear
set of charged centers? The downstream use is a rigorous sufficiency
check before spending further turns implementing a density-only saving.
A model with a positive fixed c would stop that count-only deduction;
it would not refute meas{K_t>0}=o(T) for Xi, nor any stronger approach.

The test uses only elementary finite counting and interval lengths.
Precisely state model hypotheses and every resulting bound in a canonical
lemma if a result is established. The sources are not citations for the
model's conclusion; they motivate the exact constraints being tested.
No non-elementary mathematical input is missing, and no result is derived
in this literature nomination. Full Mathlib coverage is not checked.

## Exact constraints for the later calculation

For the positive-ordinate blocks let N_mod(sigma,H) count one right-side
representative beta=1/2+d with its full multiplicity, for beta>sigma and
0<gamma<=H. Verify for every H>=H0=3.0610046*10^10 and every
1/2<=sigma<=0.831, with constants fixed independently of T,

    N_mod(sigma,2H)-N_mod(sigma,H)
      <=10395.2 H^(1-(sigma-1/2)/4) log H
        +1.104 log^2 H+0.173 log H log log H+0.51 log H.

These are the exact parameters of the inspected
[Simonic Theorem 1](https://arxiv.org/pdf/1910.08274v2#page=2).
Also require that the model's total positive-ordinate count of both
members of each block on every closed unit interval [v,v+1] is
O(log(v+2)), with an absolute implied constant independent of T and v>=0.
This matches the local-count type used in
[L464's cited Titchmarsh input](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf#page=110).
Do not assume that the two inequalities exhaust all known constraints
on zeta zeros. In particular, a finite model does not satisfy the full
Riemann–von Mangoldt asymptotic, Euler product or explicit formula.

Retain the strict displacement threshold, all H whose dyadic slab
partially overlaps [T,2T], both clipped endpoints of the charged-height
union, integer rounding of the number of centers and pair multiplicity
in local counts. Keep a and the sought union constant c distinct from
source constants. An asymptotic picture or fixed-sigma check is not a
uniform certificate. Source endpoint conventions do not authorize
dropping coincident ordinates or the boundary cases.

Continue only if all of those bounds and a fixed positive c are proved
uniformly for all sufficiently large T. If this equally spaced ansatz
fails, identify which constraint forces failure and stop the ansatz;
no automatic search over more families is approved. A successful test
requires materially new geometric or arithmetic input before reopening
count-only o(T) implementation. No proof-attempt/creative label is
justified: this is an ordinary analytic counting calculation, not a new
central positivity mechanism.
