# Fixed-witness Cassels–Tate entry-gate attempt

Completed bounded attempt. The prior SPECIALIZE gate is
`drafts/literature/2026-10-28-pair-cassels-tate-test.md`; its exact target
is the current invocation's sole target. Main gap: the accepted genus-two
rank bound is at most seven, versus the sufficient bound one; point
control, marked/integer recovery and other Beal signatures also remain.

Intermediate target: authenticate membership at 3 and 5 for the fixed
39-column subspace after the real/11/2 conditions. Downstream use:
choose at most one certified Selmer pair for the published Fisher–Yan
calculation, conditionally sharpening the rank bound. No global basis
or independence of formal coefficient vectors is assumed.

Continue only after complete local-image saturation and exact witness
maps at both places. Stop at an unresolved membership, compatible-model,
or rational-Kummer-point gate; use the approved caps (200000 divisor/disk
tests per place, depth 64, rational coefficients 8192 bits). No backend
probe, remote execution or enlarged witness pool is authorized here.
L138/L139/L140/L141/L145 are the essential inputs; L144's scalar-quotient
norm condition is a contrast and does not certify odd-model membership.
Existing uncommitted work and unfinished L108 are preserved.

## Membership result and rank use

The canonical proof, exact local coordinates, sources and limitations are
in L147. The complete images at 3 and 5 have dimensions 2 and 3, reached
by actual divisors after 134 and 924 tests. Independent full arithmetic
replay passes. The new conditions have rank three on the previous
34-dimensional formal coefficient kernel; the joint kernel has dimension
31. Since these three quotient images are independent in the actual
ambient group, the rank bound improves to 2+c<=4 without assuming a
global basis. This is local progress by known methods, not a new general
descent theorem. The separate critical proof audit remains pending.

The sole selected pair has coefficient masks 165 and 132102. L147 gives
the full representatives and all-place membership argument. Their full
localization tuples certify independence. No other pair is selected.

## Unfinished covering construction and its bounded stop

The existing approved Fisher–Yan assessment covers this application.
For construction, retrieved the same author manuscript's Proposition
2.6 and equations (30)–(31), pp.11–14, including the determinant choice;
this was formula lookup within ready coverage, not a new literature turn.
Source: T. Fisher and J. Yan, *Computing the Cassels–Tate pairing on the
2-Selmer group of a genus 2 Jacobian*, author manuscript dated
14 September 2023, https://www.dpmms.cam.ac.uk/~taf1000/papers/genus2ctp.pdf.

Preserved candidate transport: order the sextic branches as (2,−2,theta),
theta=alpha/25, and normalize the T=2 component to one. For a moved
degree-zero divisor, the exact coordinate identity

    X−eta = −c*(T−theta)/((T−2)*(theta−2)), c=−36300,

gives each odd evaluation as the ratio of its sextic evaluation to the
T=2 evaluation. The same identity holds for the T=−2 component. Thus the
proposed representatives are xi=(1,q,b), with product norm one and m=1.
The rational Weierstrass point makes the canonical class zero. The two
norm-root signs are equivalent via nu=(−1,1,1), whose square is one and
norm is −1. This normalization still needs a separate critical check
before any claimed standard covering or pairing evaluation; none is used
in L147's rank argument.

For each of epsilon, eta_class and their product, constructed all six
quadratic coefficient forms by multiplying xi*u² in the sextic algebra.
In the product basis (two rational idempotents followed by O), all 216
coefficient identities are checked per class. The raw matrices are
G=Q5 and H=Q4−(f5/f6)Q5 in the source's half-matrix convention. Their
determinants equal −1/det(M)² for the full power-to-product matrix M.
These are raw forms, not determinant-compatible standard covering models.

Searched every primitive projective vector with coordinates in [−2,2]
in this product basis: 7448 per form, 22344 total. Every value is represented
in a deterministic full-grid hash; independent replay recomputes every
value and every coefficient identity. There are no isotropic vectors in
these boxes, versus the required dimension-three isotropic subspace for
each standard model. Coefficient sizes are at most 114/8192 bits.

WHY IT STOPS: no rational isotropic plane or determinant-compatible
standard change of basis was certified. Failure in these particular tiny
coordinate boxes does not refute the source's existence theorem or exclude
larger rational vectors. No Magma installation was assumed or probed.
The Kummer-point search and pairing are not reached; there is no omitted-
place certificate or nonzero value. Park this dependent computation;
do not merely enlarge this box or retry a backend. The useful completed
local theorem has its own independent critical-audit target.

Full construction and replay evidence:
`scripts/pair-genus-two/pair-cover-gate-certificate.json` and
`scripts/pair-genus-two/pair-cover-gate-verification.json` (139 replay
checks, no failures). Reproduce with `pair_cover_gate.py` and then
`verify_pair_cover_gate.py` in that directory. No full-model or point
certificate is implied by the raw determinant identities.
