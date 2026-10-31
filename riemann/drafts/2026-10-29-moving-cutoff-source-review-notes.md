# Moving-cutoff aggregate source review — completed evidence

Literature-only review of the exact target in
`drafts/literature/2026-10-29-moving-cutoff-aggregate-coverage.md`.
No moving-cutoff estimate has been derived. L483's full proof and
L471's definitions and moment-loss argument have been inspected.

## Uniform density source and essential proof cases

Chourasiya–Simonič, *An explicit form of Ingham's zero density
estimate*, [arXiv:2507.15184v1, 21 July 2025](https://arxiv.org/html/2507.15184v1),
Introduction p. 1, Corollary 1/(3), Table 1 p. 2, its proof in
Section 2.1 pp. 4–5, and Section 4's closing proof were inspected.
The full inequality is already quoted in L483's Hypotheses. Constants
8.604, 9.461, 167.8 apply simultaneously for 0.500<=sigma<=0.625,
U>=3*10^12, with inclusive cutoffs and multiplicities. Theorem 1
requires sigma>1/2+d/log U; the corollary explicitly fills the omitted
strip using (11) and the total count. Its first row uses d=0.28.
The closing perturbation removes boundary nonvanishing restrictions.
Use the corollary, not an extension of Theorem 1. The opening reference
to Theorem 2 in the corollary proof is the recorded cross-reference
typo; subsequent text uses Theorem 1. Parameter computations, the
verified-height input and full manuscript remain cited, not
independently audited. This resolves source uniformity, without
evaluating the weighted bound or its proposed coefficient 100.

## Reused moment, shell and kernel coverage

Reuse `drafts/2026-10-29-fixed-displacement-source-review-notes.md`
for Bui–Hall, *On the derivatives of Hardy's function Z(t)*,
[arXiv:2304.05178v1, 11 April 2023](https://arxiv.org/html/2304.05178v1),
Theorem 3, its defining asymptotic and Section 7. These primary
passages were also retrieved here. Fixed ordinary orders (0,0,0,0)
give the already imported continuous fourth moment. Its order and
interval do not change with the cutoff; no shifted, selected-zero
or discrete moment is needed. No independent manuscript audit or
new reproof is claimed.

Read L467's shell specialization and reuse its completed audit and
Bellotti–Wong v2 Theorem 1.1 coverage. Every closed unit shell has
multiplicity-counted bound 18 log(v+2). This theorem has no
displacement parameter; changing the cutoff does not enlarge the
enclosing shell. No new shell result is needed.

L483 Sections 1–3 display k_d<=delta^(-2), full-window mass 1/d
and the delta^(-3) factor in (7), before inserting the fixed value.
These are existing statements, not a new moving-cutoff inequality.
The later attempt must justify the height-dependent restriction,
retain both additive density terms, handle padding 3T and prove
one common sufficiently-large-height domain. Its final fixed-sector
exponent alone cannot be extrapolated. No numerical cutoff threshold
is certified here.

## Bounded search and comparison with failures

New queries: `zeta zero density uniform sigma approaches 1/2 log log T
log T Ingham Chourasiya Simonic 2025`; `"zeta" "negative mass"
"kernel" zeros fourth moment`; `"Xi" "Laguerre" "zero density"`.
The useful primary hit was the cited density paper; no inspected
theorem directly states this amplitude-weighted moving-sector sum.
General expositions and unrelated claimed RH proofs were not used.
Rediscovered rStation paper 41 is an already assessed growing-order
positivity lead, not a newly inspected theorem for this B sum.

Reuse the fixed-sector review's Guth–Maynard comparison and the
near-line Simonič Theorem 1 coverage in
`drafts/literature/2026-10-28-zero-selected-disk-energy-coverage.md`.
That alternative has a strict real-part cutoff and dyadic endpoints;
it is unnecessary when the chosen corollary supplies inclusive uniform
cumulative coverage. No novelty claim follows from bounded searches.

Read L475's hypotheses/conclusion and
`ATTEMPTS/2026-10-29-scale-adapted-band-cost-test.md`: the exponential
global-disk cost stops that implementation. The proposed real-axis
aggregation uses no such envelope. The selected-energy assessment
still lacks amplitude-selection correlation at microscopic scales;
no estimate of that energy is imported. L471's separate-pair loss
is preserved; L483 already distinguishes aggregation. The stop in
`ATTEMPTS/2026-10-29-aggregate-route-recovery-stop.md` was procedural,
not a mathematical refutation. Preserve L483's later result.

## Disposition and continuation test

Source coverage is SPECIALIZE for the listed calculation, not IMPORT
of its weighted conclusion. The later attempt must retain full m_j,
one-copy F_j, coincident ordinates, clipped windows and endpoints;
use the inclusive cumulative count at 3T; and compare its complete
bound with T(log T)^3. Continue only if the ratio tends to zero;
otherwise record the loss or missing hypothesis and park this
implementation. No smaller-cutoff variant or fresh cancellation
mechanism is approved. L483 still awaits separate critical audit.

Even success leaves d_j<delta(T), full negative-mass saving,
individual-height signs and higher mixed positivity unresolved.
No RH, spacing, simplicity, selected-amplitude or external half-plane
premise enters. Mathlib matching is unchecked. Source readiness alone
has changed; no lemma, mathematical script, DAG or overview changed.
