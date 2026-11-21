# Fixed-line signed core: proposed mathematical continuation

TARGET: Attempt one signed-core comparison for G_w on 1<=w<=3/2 and 40<=t<=45 using the normalized Lagarias–Rains (4.8) line y=pi/8, the centered parameter derivative of its finite integral over -2<=x<=2, and its full differentiated complement; seek a uniform positive margin or one certified nonpositive rational point, with no scripts, saddle assumption or collision hypothesis.
CHECKED: 2026-11-11
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse the completed searches and failure comparisons in 2026-11-11-theta-power-contour-sign-review-427.md, completed in step428; the original derivative-sign searches in assessments425/426 remain within scope. No matching effective signed conclusion found; no novelty inferred.
SOURCE_EVIDENCE: Lagarias–Rains math/0104176v5 Theorem4.4 proof (4.8)-(4.9), Lemmas4.5-4.7 pp21-24, Proposition3.2/(3.7) p12, https://arxiv.org/pdf/math/0104176v5 and https://arxiv.org/html/math/0104176v5 ; DLMF20.5.3 https://dlmf.nist.gov/20.5.E3 . Complete relevant proof cases and normalization distinction inspected in step428; no general saddle expansion applied.
COMPARISON: Known results provide a normalized horizontal-line identity and compact strip decay, not its signed derivative on the finite box. This retains a signed finite contribution rather than repeating C999f's endpoint expansion and zero-centered absolute remainder. It is independent of the parked flint/Krawczyk backend and the older two-copy theta saddle proposal.
GAP: Justify centered differentiation on the complex line with effective bounds and certify the real signed core against all complex tails and approximation errors. C999f's real-axis tail bound is insufficient on this line. No sign margin, nonpositive value or event is known.
REASON: One precise finite signed integral and its entire complement give an independently estimable threshold without assuming a dominant saddle. This is a bounded refinement of the same derivative diagnostic, not a new creative solution mechanism or a source theorem reproof.
SCOPE: Newly written ready nomination; separate next-turn approval is required. One analytic attempt; no scripts, package installation, evaluator implementation, root location, parameter sweep, smaller box, arbitrary contour optimization, saddle asymptotics or global transport theorem.

Use the original G(w,t)=xi_Q(w,w/2+i*t), theta convention and
completion from C999f and L018/L019. C999f is still unaudited: the
attempt must justify its used representation, not silently promote
it to an audited result. Import the entire-family theorem and source
equation (4.8) by precise citation. Do not reprove them.

The main gap is actual-Xi all-degree positivity L030-L032/C032a;
L966/L968 forcing, L984(H) and C997s's capped E_n bridge stay open.
A uniform positive G_w would pay only one prospective collision
factor. G_tt, existence/nondegeneracy, higher multiplicities, all
heights, initialization and global transport would still be missing.
A nonpositive point rejects only this stronger uniform-factor claim.

Define the proposed signed core as the real part of the total w
derivative, at fixed real t, of one half of the integral in source
(4.8) restricted to x in [-2,2], y=pi/8, s=w/2+i*t. Keep its
exp(s*(x+i*y)) factor. This is a target definition, not an evaluated
derivative or a new integral identity. All logarithms are continued
from the positive real theta branch described in review427.

First justify differentiating the full source formula on a compact
complex parameter neighborhood and establish effective bounds on
the omitted |x|>2 part. Retain the moving center and completion
factors. Work directly from the full shifted-line formula; if a
truncated real contour is used instead, account for every finite
vertical connector. Do not import C999f's real-axis numerical tail
constant on this complex line.

The acceptance threshold is a signed lower bound m on the core,
uniform over the entire original rectangle, with m>E where E bounds
all omitted contributions and approximation errors, so m-E>0.
The alternative is an upper bound core+E<=0 at one documented
rational (w,t) in the rectangle. Merely deriving a shifted formula,
an exponential decay rate or a bound straddling zero does not pass.
No favorable point or smaller rectangle may replace the uniform
claim unless it certifies the stated nonpositive alternative.

Preserve the unpaid signed term if the single bounded attempt fails.
Do not follow it with another absolute-bound or contour-parameter
repetition without materially new input and separate assessment.
Mathematical exploration usage continues from step427; literature
step428 does not reset it. The old backend/source stops retain their
scopes. No cross-notebook result is needed. Full matching Mathlib
coverage is unchecked and unknown. Route as proof_attempt/development;
routine contour specialization is not a creative mechanism.
