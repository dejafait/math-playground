# Actual heat multiple-zero potential diagnostic — separate continuation

TARGET: Test whether every finite real multiple zero of the actual theta heat family forces a strictly positive first-order symmetric time difference of its localized unregularized spatial logarithmic potential.
CHECKED: 2026-11-01
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed semiconcavity source review and its exact scoped heat/potential searches; checked L059/L060 against L616 and the prior positive-transition source assessment. Splitting is already known; no exact all-multiplicity integrated-potential statement was located in the records and sources inspected. No novelty claim.
SOURCE_EVIDENCE: Polymath, arXiv:1904.12438v2, Proposition 3.1(ii), (29)–(30) and complete repeated-zero proof, https://arxiv.org/html/1904.12438v2 ; El Amrani–Jeddi, Proyecciones 32(1) (2013), unnumbered theorem p. 2 and local preparation/integrability proof pp. 4–5, https://www.scielo.cl/pdf/proy/v32n1/art01.pdf . The local splitting proofs are already canonical in L059/L060; the Cauchy/divisor normalization is canonical in L616.
COMPARISON: Sources cover finite-multiplicity heat-zero splitting, local preparation and linear divisor calculus. They do not state the target's full compact-test time asymptotic. Only that integrated-potential specialization and its limiting-order justification are proposed; do not reprove splitting or generic current theory.
GAP: Transfer the finite-root information to the full actual local potential, control its analytic nonzero factor and smooth cutoff contributions, and decide a positive first-order symmetric lower threshold without assuming simplicity, RH or a sign inequality.
REASON: This independently testable conditional diagnostic replaces the parked upper-curvature bound. It would test whether that bound would already need collision exclusion; it is not itself a new collision-exclusion mechanism. Newly written source coverage requires separate next-turn approval before mathematics.
SCOPE: One hypothetical finite real multiple zero, m>=2, of L058 at a positive time, on a sufficiently small fixed spatial disk and two-sided time interval. Standard local analytic specialization only; no all-height uniformity, global product, nonlinear current product, event-atom law or numerical search.

## Precise proposed test, not a conclusion

Use L058 with the exact theta kernel of L019 and zero-time
identification L020. Suppose F(lambda_*,x_*) has exact finite spatial
multiplicity m>=2, lambda_*>0 and x_* real. Existence is a hypothesis,
not a result. Choose a sufficiently small disk D about x_* isolating
that zero at lambda_*, and a real nonnegative smooth phi compactly
supported in D, equal to one on a neighborhood of x_*. Keep D and phi
fixed as time varies. Define

    U_0(lambda)=(1/2) integral_D phi(z) log|F(lambda,z)| dA(z).

The proposed threshold is

    liminf_(h down to 0)
       [U_0(lambda_*+h)+U_0(lambda_*-h)-2U_0(lambda_*)]/h > 0.

Determine whether this holds for every such finite m. No value for the
coefficient, asymptotic remainder, or epsilon-uniform implication is
asserted here. The later attempt may establish a more precise local
expansion if needed, but must prove every error estimate it uses.

L059 covers m=2 and L060 covers m>=3 in precisely this normalization.
They provide conditional local branches and exhaust nearby zeros.
Their source comparison with Polymath is available in
`2026-10-30-positive-transition-finite-collision-reduction.md`.
Use those results as known inputs, not as discoveries. L616's Cauchy
normalization and spatial potential methods give a finite calibration,
not this actual-family conclusion. Weierstrass preparation, the
distributional fundamental solution for the planar Laplacian and
ordinary smooth convolution are standard named/local tools; verify
their hypotheses and constants when specializing them.

In particular root location errors alone do not control the complete
time-difference error. The nonvanishing analytic factor and the smooth
test away from the isolated zero must be retained. Holomorphic
symmetric combinations and real modulus expressions are different.
Do not transfer real-time traces from a complex-parameter almost-
everywhere assertion. No global zero labeling or infinite interchange
is needed or authorized for this local target.

If the proposed threshold is obtained, justify separately any consequence
for U_epsilon=(1/4) integral phi log(|F|^2+epsilon^2): passage to U_0 at
fixed times requires local logarithmic integrability and convergence,
not commuting epsilon with time differentiation. This would show a
conditional incompatibility with the old upper O(h^2) bound, not that
the actual family possesses a collision or that RH is false or true.

Continue only if the first-order threshold and every remainder survive
all m, including the odd central branch, or identify a precise
counterexample/failing hypothesis. Park if the work supplies only the
already proved quartic cusp or an unproved theta positivity premise.
Its downstream use is route discrimination at the collision bridge;
actual-Xi signs, collision exclusion, tails, zero time and C489a's
source qualifications remain unresolved. No cross-notebook input.

The appropriate completed classification would be REPRODUCTION under
SPECIALIZE. This is development of known local analytic tools, not
creative work: an independent theta-specific coercive condition remains
missing. Full matching Mathlib coverage and supporting local-potential
theorems have not been checked; unknown availability is not absence.

This assessment was prepared during a literature-only turn. It is ready
for the supervisor's separate approval; no proposed implication above
has been derived or approved as a mathematical result.
