# Leading fourth tensor: bounded periodic carrier attempt

The invocation-start EXPLORE assessment is
`literature/2026-10-31-periodic-rare-fourth-tensor-cone.md`.
This working record is incomplete, not a feasibility certificate.

Main gap: actual-Xi all-degree signs at unbounded heights. The approved
intermediate test seeks all 126 coefficients of L473 (9) as limits of
positive occupation mixtures of unit paired-jet periodic C2 paths, with
uniform total weight and second cost and entrywise error O(1/ell).
A carrier could replace rare atoms without assuming their path extension.
Second completion, positive clipping and Xi transfer remain independent.

Read L473's leading formulas and rare/covariance construction, L582's
ordinary lagged-jet convention, the completed occupation comparison and
the recorded packet, exact-law and absolute-budget stops. The latter
are narrower obstructions, not premises excluding this tensor. Arithmetic
inputs retain L473's qualifications, especially Bui--Hall Proposition 3's
imported, unaudited proof. No cross-notebook result is used.

Initial alternatives within this one cone test: an explicit positive
frequency construction for q; a quartic occupation separator; or a
localized conversion of known paths. Any construction must control total
weight uniformly as accuracy improves. Normalizing a long sparse pulse
and paying its period is not sufficient. Finite-dictionary failure alone
would not be a global separator. No representation, compactness or
positive covariance repair is assumed.

Continue only with a certified all-entry carrier or a precise new
obstruction/refined test. Preserve failures and do not repeat the fixed
packet or absolute discarded-energy mechanisms.

## Saved partial reasoning

Changing variables in L473 (9), with a=1/2-u_1, b=1/2-u_2,
S=a+b, gives a symmetric frequency density
`(3/pi^2)(1-2 max_i |k_i|)` on `sum k_i=0, |k_i|<=1/2`.
Indeed integrate the endpoint separation d=|a-b| from
`max(|k_1-k_2|,|k_3-k_4|)` to `1-|S|`; the two orientations cancel
the factor 1/2 in the Jacobian. This suggests, with
`f_b(s)=integral_(-b)^b exp(iks) dk=2 sin(bs)/s`,
`q_m=(3/pi^3) integral_0^(1/2) integral_R J_(f_b)(s)^m ds db`.
The full change of variables, Fourier normalization, endpoint convergence
and every derivative allocation still need final verification.

Periodizing increasingly isolated pulses incurs a weight proportional
to the period and alone fails the uniform bound. The current refined
test is whether compactly supported perturbations of finitely many
sinc pulses span all nontrivial occupation coordinates. If so, a fixed
large period plus a small exact correction could suffice. No rank or
local surjectivity is yet claimed.

Candidate universal identities: the 35 total derivatives of homogeneous
quartics in (h,h',h(.+1),h'(.+1)), and the 15 differences of same-height
quartics at lags 0 and 1. Five overlaps suggest rank 45, leaving 81
coordinates. Check this algebra and the pulse first-variation rank
exactly, including both shifted Euler terms. This is a test inside the
approved tensor cone, not a claim that finite-Hardy sampling is stationary.

## Exact test result and pending analytic assembly

`scripts/periodic-tensor/pulse_rank.py` obtained relation rank 45 and
pulse-variation rank 81 over the rationals, certified by nonzero minors
modulo 1000003 (respectively 897600 and 700255). It used coefficients
through b^99 of the cubic Euler expression, evaluated at s=0,1,2.
All 50 candidate relations have identically zero symbolic Euler operator.
The full certificate is saved in that script's directory. Independent
regeneration and the analytic implication remain to be checked.

The proposed completion uses the convex cone of actual unit-jet periodic
occupation tensors, not an assumed compact path space. Sinc pulse tensors
and their compact perturbations lie in its closure by smooth cutoffs.
If a nonnegative cone functional vanishes at q, its nonnegative integral
over bandwidths vanishes at every interior bandwidth. Each such pulse
is therefore a minimizer against every compact perturbation, forcing its
Euler expression to vanish. Rank 81 then makes the functional an exact
occupation identity. Finite-dimensional separation would put q in the
relative interior of the closed cone. A finite-simplex approximation
then puts q in the original cone, yielding one finite representation
and hence uniform weight. These implications still require a complete
canonical proof; no closure-to-attainment shortcut is assumed.

## Completed attempt

The complete argument is now canonical in
`lemmas/L585-positive-periodic-carrier-leading-fourth-tensor.md`.
It supplies the cutoff estimates, positive-integral minimum argument,
finite-dimensional supporting plane and interior-simplex attainment.
The result is one fixed finite mixture, not a uniform bound asserted
for the raw periodization sequence. All 126 entries match exactly.

The independent checker reconstructed all 126 Euler columns, 50
universal identities and 10206 selected Taylor entries, then verified
the 45- and 81-dimensional matrix inverses entrywise modulo 1000003.
Its full certificate is saved in `scripts/periodic-tensor/`.
The mathematical result is not independently audited. Its continuation
assessment is REVIEW_REQUIRED; second completion, positive clipping,
the imported arithmetic proof and Xi transfer remain unresolved.
