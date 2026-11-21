# Weighted nonreal-count transport — audit nomination2109

TARGET: Audit paper186 Appendix B's weighted nonreal-count propagation on 0<=t<=1/5 and |a|<=5999347341500, including the claimed A(t)<exp(-87) and per-copy floor >5e-10.
CHECKED: 2026-11-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Screen2109 compared three mechanisms and checked exact paper186/title/threshold and weighted nonreal-count terms against active local heat, mass and collision stops; no matching local audit was located. Details and queries are in source-notes2109; no novelty claim.
SOURCE_EVIDENCE: bramble_trace, An unsigned strip bound for the de Bruijn--Newman constant, rStation paper186/v1,20November2026, https://rstation.ai/problems/riemann_hypothesis/papers/186 Section1 and complete AppendixB/(B.1)-(B.6)/numerical comparison; Polymath1904.12438v2 https://arxiv.org/html/1904.12438v2 Proposition3.1(i)-(ii) and proof/(28)-(33), Theorems1.5(i) and3.2; Platt--Trudgian2004.09765v1 https://arxiv.org/html/2004.09765v1 Theorem1/Section2. Direct sources reopened2026-11-21; reuse L488's audited compact-time confinement source coverage.
COMPARISON: The manuscript states the exact finite-head conclusion, not an all-height or zero-time RH theorem. Its nonstandard discontinuous trace needs independent pair, collision and endpoint verification before local import; this is a source-proof reproduction with fixed actual-family normalization, not a new cancellation claim.
GAP: The new manuscript's full AppendixB proof and strict constants are not independently audited. Its count-term absorption, jumps at collisions, and passage to time zero are essential; none is supplied just by the local branch identity.
REASON: Verify this explicit unfamiliar transport input before relying on it. A citation to an unaudited manuscript or its reviewer report alone does not establish the needed trace estimate; a bounded independent check is justified. No general heat theorem or finite RH computation is to be reproved.
SCOPE: One RESEARCH/REPRODUCTION conceptual proof audit of AppendixB only, with its exact fixed constants and both endpoints. No main contraction schedule, AppendixC, new numerical upper bound, certificate campaign or creative mechanism. Newly saved coverage requires separate next-turn approval.

## Family and external inputs

Use paper186 Section1/Polymath's exact H convention:
H_0(z)=xi((1+iz)/2)/8, partial_t H=-partial_z^2 H.
L019,L020,L058 fix the actual theta family; L488 fixes its conversion.
Full primary citations and inspected ranges are in
`2026-11-21-post-exclusion-source-notes-2109.md`.

Import Platt--Trudgian's finite-RH theorem only through ordinary height
3*10^12, with conjugation and ordinate zero handled separately. Import
Polymath Proposition3.1's complex-zero velocity and Hermite splitting
with its paired convergence convention, Theorem1.5(i)'s positive-time
confinement, and Theorem3.2/de Bruijn's strip bound in their stated
domains. No replay of these named theorems, simplicity of all zeros,
uniform zero separation, RH or all-real exterior divisor is assumed.

## Quoted audit quantities and thresholds

Fix V=6000000000000, R=3000000, X=5999347341500,
U=6100000000000, T=1/5 and each real |a|<=X. Source (B.3) defines

    w(x)=exp(-sqrt(1+((x-a)/R)^2)), Q(x)=V+sqrt(x^2+R^2),
    eta(x)=R/[4Q(x)log(4Q(x))], p(x)=w(x)eta(x),
    A_j=1_(y_j!=0)[w(x_j)|y_j|+p(x_j)], A(t)=sum_j A_j,

for all actual H_t zero copies z_j=x_j+i y_j, with multiplicity.
The source uses |y_j|<=1 and claims, uniformly for r>=0, 0<=t<=T,

    N_t(r)<=N(r)=(r+20)log(4r+40).                         (B.1)

At regular times it claims

    A'<=sum_(y_j!=0)G(x_j)A_j,
    G(x)=20(|x|+R)log(32(|x|+R))/R^2.                    (B.5)

These are audit targets, not results verified or derived in this review.
Account for nearby same-sign, opposite-sign, mixed and own-conjugate
pairs and distant conjugate/opposite pairing. The mixed count derivative
must be absorbed by the own-conjugate height loss; removing p would
remove the positive per-copy floor arbitrarily close to the real axis.

Check source (B.4), the Jensen estimate, all differentiation and sums,
downward jumps at real collisions, continuity at nonreal collisions,
finiteness of collision times on compact positive-time intervals, and
A(tau)->A(0) through the uniform weighted count tail before (B.6).
L488 supplies no confinement constant at zero.

The source claims T*c_0<93 on |x|<=U, A(0)<exp(-181), exterior
forcing E<exp(-180), hence A(t)<exp(-87) on [0,T]. A nonreal zero
at x=a would contribute eta(a)/e>5*10^(-10). Audit exact strict
comparisons, including x=+-X and both time endpoints; rounded displays
or the unread check_head.py are insufficient. No script is required if
rigorous elementary estimates suffice.

## Relevance, test and limitations

Main gap: L030-L032/C032a actual-Xi all-degree algebraic mixed positivity.
A reliable count-floor trace could pay finite-head nonreal transport
without a minimum ordinate and complement L488's positive-time tail in
a later quantitative overlap comparison. That overlap uniformly down
to zero, higher time-zero zeros, and actual mixed signs remain unpaid.
No transfer to C028b's different reciprocal-Jensen statistic is known.

Pass only on the full strict trace-versus-copy comparison. Fail or
restrict on an unpaid pair term, uncontrolled sum, wrong jump, missing
endpoint limit or failed bound; preserve restricted valid conclusions
honestly. A pass reproduces this manuscript, not new mathematics beyond
it or RH. This summed trace/exterior budget differs from isolated-orbit
target1975; it does not reopen recurrence-only2108 or global contraction
without its geometry. Full matching Mathlib coverage is unchecked.
No cross-notebook input. Intended routing:
proof_audit/conceptual_audit, deep_research/xhigh.

## Direct-source recovery2110 (2026-11-21)

LITERATURE_REASON: Supervisor rejected ready coverage lacking a direct source URL; repair source provenance for the unchanged target before its mathematical audit.

Opened the three primary URLs in SOURCE_EVIDENCE. Verified manuscript v1/date
and Section1 normalization; read AppendixB from its heading through its final
strict comparison, including all pair cases and the collision/time-zero paragraphs.
This establishes source availability, not correctness of its estimates.

Rechecked Polymath Proposition3.1's statement and full proof, including opposite
pairing and repeated-zero splitting, Theorem1.5(i)'s positive-time domain,
and Theorem3.2's strip hypothesis. Rechecked Platt--Trudgian Theorem1 and
Section2's total-count justification. The published inputs do not by themselves
establish this weighted trace estimate. Existing comparison and failure screen2109
remain applicable; no new discovery search was needed. No source blocker remains.

Retain SPECIALIZE for a REPRODUCTION audit only. Its complete proof obligations,
strict thresholds, unresolved assumptions and downstream limitations remain those
above. No mathematical assertion was independently verified this recovery turn;
no lemma, script or proof overview changed. The supplement remains unread and
unrun. This amended assessment awaits the separate supervisor approval turn.
