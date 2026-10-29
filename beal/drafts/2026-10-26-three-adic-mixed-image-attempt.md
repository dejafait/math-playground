# Bounded 3-adic mixed-image attempt

2026-10-26, step 517, in progress. The gate-approved target is to determine
whether the norm-trivial part of lambda_B(Jac(B)(Q_3)) is contained in
lambda_E(E(Q_3)), or certify a class outside that image. The prior
SPECIALIZE assessment is `literature/2026-10-26-three-adic-mixed-image-nonredundancy.md`.

The main gap is residual primitive Beal point control, with the current
rank bound still eight above the sufficient bound one. A local mismatch
could justify later global supported-class testing; certified containment
stops this extra filter at 3. No global exclusion follows in either case.

Inputs inspected: L110/L111 actual equations and origins, L138 odd-model
and quartic coordinate transport, L142 embedded kernels, L143 evaluation
interface and audit, and ATTEMPTS/062's exact-same-T redundancy. Preserve
all existing work, including unfinished L108. No duplicate complete
mixed-image comparison appears in those relevant current inputs.

First bounded test: factor the actual quartic algebra using alpha=25theta.
A candidate Newton polygon at alpha=1 has root-valuation multiplicities
3 and 1. If this certifies a linear plus odd cubic decomposition, check
whether the square-norm kernel of the entire scalar quotient is already
zero. This is within the approved factorization/square-class/interface
stage; no image exclusion or new target is assumed. If this fails,
retain the original elliptic-cell and B-witness caps. Full local images,
not sampled nonmembership, remain necessary whenever the ambient argument
does not decide containment.

Global realization, mixed global nonredundancy, full descent, Abel
membership, point control, integer recovery and other signatures remain
unresolved. Source theory is reused; no new general local descent theorem
is proposed. Exact calculations and their complete evidence will be saved
under `scripts/pair-genus-two/` before a conclusion is recorded.

## Completed attempt

The canonical proof and its precise sources/qualifications are in
[L144](../lemmas/L144-three-adic-mixed-norm-kernel-trivial.md).
The entire quartic coefficient quotient has dimension two and norm
is an isomorphism. Its norm-trivial kernel is zero, so the requested
B slice is exactly the identity and the actual elliptic origin covers
it. This is certified containment, rather than a deficient point span.
Full B and E images are not asserted or required for this ambient
upper bound. The preapproved square-class/factorization stage decides
the unchanged target before either bounded point search is needed.

Outcome: NEGATIVE, classified REPRODUCTION of known local-field and
descent theory at this instance. It stops this extra norm-restricted
filter at 3. It does not produce a Beal counterexample, a rank gain,
global pruning or progress beyond the inspected general methods.
The producer's 59 checks and independent replay's 74 checks pass;
the complete certificates and commands are recorded in L144. The
replay checks arithmetic, not the pending conceptual critical audit.
The stop and reopening condition are in ATTEMPTS/063. PROOF.md now
records this local stop and the already completed L143 audit; the
DAG adds only L144's actual direct inputs.

Before further mathematical use, assess the distinct critical-audit
coverage in `literature/2026-10-26-three-adic-mixed-norm-kernel-audit.md`.
It is REVIEW_REQUIRED; no new mathematics is approved by that proposal.
No global creative exclusion is yet a concrete source-covered target.
