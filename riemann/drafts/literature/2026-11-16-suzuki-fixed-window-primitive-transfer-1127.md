# Fixed-window primitive transfer — proposed coverage1127

TARGET: Transfer Li paper45/v2 Theorem1.1 to C618b at a=log(3) for every complex L2 test, retaining the primitive jump and proving the closed-form identification.
CHECKED: 2026-11-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1127 compared the exact fixed-window full-form and coupling scope; reused869/874 and the November1 screw screen, checked primary theorem/domain/proof cases, and screened the distinct scalar/localization/residue stops. See the completed assessment1126 for queries and source distinctions; no novelty claim.
SOURCE_EVIDENCE: Hongmin Li paper45/v2, 9November2026, Theorem1.1/(2.1), Sections4-5 and7; Suzuki2606.09096v3, 23September2026, Theorem1.1, (2.9), Sections3.1-3.2/(3.2)-(3.4); C618a primitive/Fourier identities and audited C618b complete decomposition. Primary passages inspected during review1127; source numerical supplement not replayed.
COMPARISON: Strict positivity of the complete closed geometric Weil form on a window containing log3 is known. Its application to a possibly discontinuous q_phi requires a local domain/normalization argument; a new Schur certificate or reproof of source positivity would duplicate known mathematics.
GAP: Establish q_phi in the source closed form domain and equality with C618b's anchored form for all complex L2 phi, without imposing mean zero, H_0^1 regularity or parity. Track the Fourier normalization and every prime, pole and gamma term. No such specialization has been proved in review1127.
REASON: This bounded applicability question is the remaining local difference identified by the completed coupling review. It can import a reliable fixed-window input while leaving all-support positivity and actual-Xi realization unresolved. Separate next-turn approval is required for this newly saved coverage.
SCOPE: One proof_attempt/development, REPRODUCTION specialization at the single fixed half-width log3; no numerical spectral-gap claim, larger-window extension, projection split, source-certificate replay, paper144 application or RH claim.

Main gap: L030-L032/C032a actual-Xi all-degree positivity. Proposed
intermediate conclusion: a strictly positive, possibly nonexplicit
constant multiplying E0 in the full C618b form at this fixed window.
Its use would be a known supported-positivity input in later signed
comparisons; no uniform-in-window or degree conclusion is intended.

The controlling positive-form source is Hongmin Li,
[*Cutoff-free positivity of localized Weil forms through the (log11)/2
threshold*, paper45/v2](https://rstation.ai/problems/riemann_hypothesis/papers/45),
Theorem1.1 and normalization(2.1). It covers the complete closed
form, both complex parity sectors. The support comparison is
log3<(log11)/2. Import the theorem; do not redo its certificate.
No effective constant is provided by that theorem.

For the closure framework use Masatoshi Suzuki,
[*Weil's quadratic form via the screw function*,2606.09096v3](https://arxiv.org/html/2606.09096v3),
Theorem1.1, distributional formula(2.9) on the smooth core, and
Sections3.1-3.2, especially(3.2)-(3.4). The source identifies the
Friedrichs extension initially defined using H_0^1 and verifies a
smooth form core using logarithmically weighted Fourier estimates.
It does not state that every piecewise primitive is in H_0^1.
Use that framework only after proving the exact local membership
and limiting identity; a support enlargement inside the cited
positive window may be an approximation device, not a new theorem.

Essential local inputs are C618a's actual q_phi and transform
identities, with zero outer traces and its potentially nonzero jump
at zero, and C618b's full complex-test definition/decomposition.
The later proof must justify approximation or distributional
pairings, absolute convergence and passage to the closed form.
An L2 limit alone is insufficient for an unbounded logarithmic form.
No positivity of an assumed tail block or inverse is an input.

Continuation test: establish the domain and identity for arbitrary
complex phi with nonzero integral as well as mean-zero phi, with
all terms and factors matching; only then import the strict sign.
Abandon the claimed full-space transfer if a genuine domain or
normalization obstruction survives, and preserve any restricted
conclusion with its exact hypotheses. Do not treat the already
known fixed-window sign as a new discovery or extrapolate it to RH.

No matching Mathlib coverage checked; no cross-notebook input.
The special-case proof remains undone. This assessment is newly
written and is subject to the supervisor's separate approval turn.
