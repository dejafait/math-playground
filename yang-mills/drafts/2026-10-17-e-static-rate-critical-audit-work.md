# E static trace rate — critical audit working record

2026-10-17. Approved target and unchanged EXPLORE assessment:
`literature/2026-10-17-e-static-trace-rate-critical-audit.md`.
Inputs: L008 L028 L097 L101 L222 L223; inherited relative-cell domain
checked narrowly in L003, actual path symbols in L088 and mode
normalization in L080/L026. These are supporting checks, not an
upstream re-audit. No cross-notebook input is used.

The main construction gap is interacting cutoff removal with reflected
error <=c_box/2, continuum axioms and finite positive mass. The one
intermediate target is acceptance or rejection of L224's O(N^2)
static-continuum error. Its downstream use is the E-component
O(N^(5/2)) remainder with L223. Accept only if the signed stencil,
relative projection cutoffs, actual modes and entire heat sum close;
withhold acceptance on an essential unbounded sector. The weaker
requested static threshold is O(N^(5/2)log(eN)^2).

Checks completed before writing the final canonical audit:

- L101(13)/(15): compact coefficients and exact commutators give zero
  row sums and bounded normalized coefficients; the quarter layer and
  moving-cut endpoint survive in their stated places.
- Zero extension intertwines differentials on relative cells, including
  normal end rows, but not adjoints. Only the former is used. Finite
  gradient/curl ranges are subspaces of the respective full-grid ranges.
- Both dipole potential cutoffs have squared error O(N^-3). The finite
  second spatial l2 moment, rather than an absolute first moment, is
  what permits exterior freezing. The curl-projection bilinear error
  uses the difference of nested orthogonal projections.
- Actual normal transverse end edges use the same prefix formula:
  the prefix on a boundary vertex is exactly zero because A_1 is
  tangential there. No value at axial level N is substituted.
- L097's c coefficients agree with the whitened L008 forms and
  L080's physical normalization. L222 supplies polynomial modal errors
  before the full heat sum. No color or assembly factor is added.

At the initial save the canonical verification and final normalization
were pending. Completed: L224 proof section 7 records acceptance of the
existing rate relative to its imported inputs, with the complete
cell/heat comparison. History 294 records the decision and the one
REVIEW_REQUIRED L220 audit continuation. No script or numerical
experiment was needed for these analytic checks.
