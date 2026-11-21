# Six-node crossing working checkpoint — step 336

Approved target: the exact six-node test in
`literature/2026-11-04-neutral-gaussian-six-node-crossing.md`.
One RESEARCH/proof_attempt using ready EXPLORE coverage; expected
classification REPRODUCTION. This draft is unfinished reasoning, not
an independently audited result.

Completion: the argument below was written in full in
`lemmas/L754-realizable-six-node-gaussian-upward-crossing.md` (path
relative to the notebook). The exact test succeeds, giving an
informative negative result for abstract backward comparison. This
working checkpoint is preserved; the canonical proof has not yet
received a separate audit.

Candidate parameters: H=3/4, r=1/2, a=1, b=1/4; all six
multiplicities one. Prescribe F(+/-r)=1, F(+/-1+i/4)=1,
F(+/-1-i/4)=-1, and F(+/-i/2)=0. Thus the real coefficients
are 1 each and all four reflected products are -1. Burnol's finite
Mellin interpolation applies at s=1/2-iz, with
f(x)=exp(x/2)g(exp(x)); the added nodes s=0,1 impose neutrality.
No support or norm bound is requested; no symmetry of f is assumed.

The complete candidate sum is
S(tau)=2 exp(-tau/2)-4 exp(-15tau/8) cos(tau).
It starts at -2. On (0,pi/2), q(tau)=2 exp(-11tau/8) cos(tau)
strictly decreases from 2 to 0, so the unique q=1 crossing has
S'>0. All-time positivity follows eventually from
S>=2 exp(-tau/2)[1-2 exp(-11tau/8)].

Before canonicalizing: verify all eight Mellin nodes are distinct,
write each reflected product, pay complete symmetry/multiplicity,
strip/window/separation/visibility and absolute-summability analogues,
and distinguish the synthetic sum from L753's actual arithmetic form.
Main gap: actual-Xi mixed/neutral positivity. Success parks only an
abstract backward comparison; actual arithmetic and all-test coverage
remain open. No expansion of the spectrum is authorized this turn.
