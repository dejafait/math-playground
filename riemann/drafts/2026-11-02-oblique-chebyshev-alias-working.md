# Oblique negative-grid Chebyshev alias — bounded attempt

Prepared STEP_ID: 2026-11-02-oblique-chebyshev-alias-01.
Invocation-start coverage: the unchanged EXPLORE assessment
`drafts/literature/2026-11-02-rotation-averaged-anchor-line-hankel.md`.
Actual task: one proof attempt within its angular Fourier/residue scope.

Main gap: actual-Xi all-degree mixed positivity at unbounded heights.
Intermediate target: for odd m>=5, n=3m, r=27/50, unit-residue
Chebyshev nodes and |arg(u)-13*pi/16|<=10^(-6), bound the full signed
node average through b_0-2*b_(2m) and every higher alias. A strict
exponential margin below 1/32 would give an angular constant-input
lower bound on this subfamily and transfer through C645u. General
common-pole families, Xi layer isolation, other poles, census/clearance,
simultaneous realization, independent upper bounds and signs remain open.

Inputs read: C645g normalization; C645l's exact finite-node identity
(23) and its contour justification; C645n projection; C645t's
r=27/50 admissibility; C645u polynomial rate comparison. Reused the
assessed Fourier/residue sources. Scoped duplicate/failure checks read
the previous kernel and full-energy attempts and searched the oblique
records. Earlier pi/6 endpoint and outer-half-input stops do not decide
this signed finite-node question. No new source gate is asserted.

Write F_n(t,u)=B_u(x)/B_u(x+i*r*cos(t)) and
b_l=(2*pi)^(-1) integral F_n(t,u)*exp(-i*l*t) dt. The proposed test is

    |b_0-2*b_(2m)|-2*sum_(h>=2)|b_(2*m*h)|
        >= c*n^(-A)*exp(-gamma*n), gamma<1/32.

First justify the complete alias identity and a contour bound for its
entire higher tail; then examine the leading signed term. Continue only
with a rigorous margin, an informative obstruction, or a materially
refined bounded mechanism. An unenclosed finite coefficient evaluation
does not establish an asymptotic or an angular mean. Preserve any
unproved saddle/remainder claims explicitly. No conclusion yet.

## Completed bounded attempt

[C645v](../lemmas/C645v-oblique-chebyshev-higher-alias-tail.md) gives
the complete signed alias identity and the uniform estimate

    2*sum_(h>=2)|b_(2*m*h)| <=4*exp(-21*n/250).

The exact half-plane certificate controls every point of the contour,
every actual grid size, and the entire sector. Its product exponent
is at most 7722432503711/25600000000000 <31/100; its resulting tail
rate is 21/250=0.084 >1/32. The 512 rational cells, all discriminant
and slope inequalities, radical enclosures and logarithm remainders
were checked by `scripts/one-sided-hankel/oblique-alias-tail-certificate.py`.
The complete certificate is the adjacent JSON; the final failure list
is empty. The first certificate failed its tighter 3/10 envelope and
a nested-radical enclosure. It is preserved in
`scripts/one-sided-hankel/oblique-alias-tail-initial-failed.json`;
the canonical proof states the corrected intervals and 31/100 envelope.

This is a relevant local quantitative input, so the completed outcome
is ADVANCE, classified POTENTIALLY_NEW within the bounded source
comparison. The general alias identity is standard specialization;
only the evaluated uniform remainder is new local work. No certified
originality, full detector bound or actual-Xi positivity is claimed.
C645v has not received a separate conceptual audit.

The diagnostic `scripts/one-sided-hankel/oblique-alias-diagnostic.json`
retains all five finite n and three contour shifts. On the unshifted
contour the apparent leading rates for n=51,99,195,387,771 are about
0.02467, 0.01299, 0.00551, 0.00087 and -0.00193. These are unenclosed
finite diagnostics, not asymptotics or certificates. The shifted b_0
integrals suffer catastrophic cancellation: at n=387,h=.2 the reported
b_0 has modulus about 2.9*10^10 and absolute-mean/result ratio about
2.7*10^14, whereas the unshifted b_0 is at the numerical noise level.
The first-alias shift comparisons also fail 10^(-7) relative agreement
at n=387 and 771 (the h=.4 integrals are ill conditioned). Selected
high-alias values at the noise floor are equally unusable. None of
these values enters C645v, and no b_0 asymptotic is inferred.

## Preserved continuation

The genuinely unresolved test is now the leading signed term:

    |b_0(u)-2*b_(2m)(u)| >= c*n^(-A)*exp(-3*n/100)

for some c>0, finite A, one onset, all odd m with n=3m, and every u
in the same 10^(-6) sector. The numerical rate 3/100 is a proposed
threshold below 1/32, not an estimate. Use the exact coefficient
contour and retain both terms; any saddle deformation needs its
branches, all contributing saddles, endpoint terms, error and angular
uniformity proved. The new tail input removes the previously open
possibility of higher-alias cancellation at the required scale.
It does not remove cancellation within the leading signed term.

Essential inputs: C645g normalization, C645l (23), C645t admissibility,
C645v's whole-sector tail, and C645u only for downstream kernel
comparison. Continue with a rigorous leading-term margin or an
informative obstruction. If no such margin or materially refined
mechanism is obtained, preserve the analysis and reassess rather
than repeat a finite screen. General families, other poles, census,
clearance, simultaneous realization, an independent upper bound and
actual-Xi signs remain separate. Reuse the unchanged ready angular
assessment; no new assessment or source approval is asserted here.
