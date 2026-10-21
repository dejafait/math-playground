# Upper-face pure-sector evaluation — working record

STEP_ID: YM-20261005-045-upper-face-pure-sector-evaluation

The unchanged SPECIALIZE assessment
`drafts/literature/2026-09-26-current-target.md` is reused for its exact
combined-response target. This is one bounded mathematical calculation
inside that target, with inputs L008 and L030–L032. Existing unfinished
work and ATTEMPTS/011–015 are preserved.

Main gap: the complete interacting response and a cutoff-uniform
comparison remain unknown. Intermediate target: evaluate the two pure
13/24 sectors of L032 for both original probes, keeping transitions,
both heat weights, inverse powers and every second-index component.
Downstream use: a certified nonzero I_i would identify a power term in
L030's selected class requiring compensation before interpreting a
full logarithm. Zero would leave slower powers and logarithms open.
Continuation test: use a separable continuum matrix-element calculation
of the full formal residual, validate symmetry/compression identities,
and test spectral and integration stability. A sign claim additionally
needs a rigorous omitted-mode and quadrature bound smaller than the
computed absolute value. Abandon a sign claim if that bound is missing
or exceeds the value; finite partial sums remain diagnostic.

Unfinished reasoning saved before implementation: expand the formal
operators in L030(5)–(8) into sums of tensor products of one-dimensional
differential operators. Products of rho and x rho and their derivatives
remain separable. Integrate derivatives on coefficient factors by parts
onto the sine/cosine factors where possible. Compute the N matrix via
the weak symmetric-action formula, including both adjoint contributions,
and subtract both order-t Q coefficients. This preserves the actual
average-of-squares triplet and clover-product shear. Compare against
L031's axial-zero core calculation and L032's mixed-sector cancellation.

Independent unresolved steps: full spectral/integration certificates,
other plaquettes/pairings, all remaining action/measure/insertion/flow
jets, L019 compensation, finite matching, error <= c_box/2 along a
prescribed trajectory, continuum fields, full reflection positivity,
infrared control and finite positive mass. None is used as a premise.

## Completed bounded calculation

Outcome: EXPLORATION / RESEARCH / POTENTIALLY_NEW; actual task calculation.
No new lemma, sign certificate or full coefficient is claimed.
`scripts/combined-ward-response/check_continuum_pure_sectors.py` implements
finite continuum spectral sums using the full L030 formal operators.
It expands the bilinear Q operators and the symmetric action variation,
including both transposed terms and every order-t correction. For each
separable coefficient it moves coefficient derivatives onto products
of trigonometric basis factors. The Fourier integrals of rho and x rho
are evaluated with composite Gauss–Legendre rules on the four intervals
split at -5/2, 0 and 5/2. This is a binary64 implementation, not a proof
of a certified infinite-sum evaluation. Canonical mathematical inputs
remain L008 and L030–L032; no source theorem is newly imported or reproved.
Their Mathlib coverage is unchanged and the computation is not formalized.

The partial sums retain all four second-index components and all allowed
indices up to the named cutoff. Only the proved axial parity restriction
is imposed in the sum; the tensor integrals also enforce their exact
one-dimensional parity. The potentials are kept separate, so both mixed
sums are independently inspected for each probe. At cutoff 12 and
quadrature degree 96 the largest zeroth-order residual/mixed-sector/
13-axial-zero check error is 2.05e-14, below the implementation tolerance
1e-8. These checks confirm internal consistency numerically; they do not
prove the order-t implementation or certify its truncation error.

At cutoff 12 the 13 sector contributes (158.126173712,1180.284557279)
to probes (3,6). The 24 sector contributes
(132.545843014,674.435582555), split into axial-zero
(87.250864317,445.891539584) and positive-axial
(45.294978697,228.544042971). The totals are
(290.672016726,1854.720139835). At cutoff 10 they were
(189.232838189,1162.696976014), and at cutoff 8
(109.641114692,351.016826413). Thus the spectral sequence is unresolved.
Refining degree 64 to 96 at cutoff 12 changes these totals by about
(3.13e-11,1.30e-10); this observed agreement supplies no rigorous
quadrature bound and no control of the omitted modes.

An independent implementation check uses the pre-existing lattice
`RelativeBox.residual`, whose matrix divided by a^4 should approach the
continuum N2 entry for normalized discrete modes. Three selected entries
(including a second-index component 3) are compared at N=24,32,48.
All three absolute differences decrease: from
(7.94e-4,3.09e-4,3.77e-4) at N=24 to
(6.77e-5,4.67e-5,1.79e-5) at N=48. These are mesh diagnostics rather
than a convergence proof or a full-spectrum implementation certificate.
The complete selected mode labels, limits, values and differences are in
`scripts/combined-ward-response/continuum-pure-sectors-stencil-certificate.json`.

Full finite-sum evidence is saved in
`scripts/combined-ward-response/continuum-pure-sectors-certificate.json`
(cutoffs 2,4,6,8; degrees 32,64) and
`scripts/combined-ward-response/continuum-pure-sectors-higher-certificate.json`
(cutoffs 10,12; degrees 64,96). Selected complete load-bearing values
were inspected with the supervisor JSON inspector, including both pure
and mixed sectors and every selected lattice comparison. Reproduction:

```sh
OPENBLAS_NUM_THREADS=1 python3 scripts/combined-ward-response/check_continuum_pure_sectors.py --cutoffs 2 4 6 8 --degrees 32 64
OPENBLAS_NUM_THREADS=1 python3 scripts/combined-ward-response/check_continuum_pure_sectors.py --cutoffs 10 12 --degrees 64 96 --output scripts/combined-ward-response/continuum-pure-sectors-higher-certificate.json
OPENBLAS_NUM_THREADS=1 python3 scripts/combined-ward-response/check_continuum_pure_sectors.py --lattice-check 24 32 48
```

The continuation test is not met for a sign claim: the required bound
on quadrature plus all omitted modes is unavailable. This stops the
current finite-cutoff attempt short of evaluating I_i; it does not
exhaust the separable continuum mechanism or revive ATTEMPTS/014's
global-norm certificate. A concrete continuation within the unchanged
ready target is to use separability also for the coupled inverse
Laplacian weights, avoiding the current seven-index contraction cost,
then test a quantified spectral tail. Inputs L008 and L030–L032 are
essential; L019 compensation and every other jet remain unresolved,
not premises. Exploration usage is 1 of 3 after L032. The full response,
its logarithm and reflected-error threshold <= c_box/2 are unchanged.
