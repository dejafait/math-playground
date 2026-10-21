# Union-six twelve-incidence attempt

Date: 2026-10-07. STEP_ID: 2026-10-07-mca-074-six-coordinate-equality-descent.

Approved target: Prove or refute that every L033 union-six pencil over F_(97^20) with no weight-three parameter has at most twelve valid additional finite incidences.

The main gap is arbitrary-family sixteen-count equality. This attempt
uses the unchanged EXPLORE assessment in
[the twelve-incidence review](literature/2026-10-07-six-coordinate-twelve-incidence-bound.md).
Intermediate target: a necessary arithmetic constraint on a hypothetical
thirteen-incidence completion, potentially reducing extension-field
weights to a finite projective configuration. Continue if the actual
overlap formulas force two rational points of the pencil; abandon this
mechanism if it only uses the false implication that meeting rational
lines forces rational descent. The twelve bound, universal cluster
extraction and challenge identification may remain unresolved.

Inputs inspected: the complete relevant L010 proof, L032's union-six
lift and rank proof, and L033's support split, converses, uniqueness and
finite accounting. The existing source assessment is reused. A targeted
local duplicate search found no paired-ratio equality descent result.
ATTEMPTS/017, /019 and /020 stop different mechanisms and are preserved;
neither L015's enumeration nor positive-only sampling is an input.

Working checkpoint before completing the argument: under equality every
coordinate of U occurs twice in the selected three errors and four times
in total. L033 therefore forces twelve overlapping external errors,
two at each x in U, and one disjoint external error. An overlap at x
gives rational ratios on both coordinate pairs not containing x. This
appears to force all three paired ratios into F_97. With those ratios
fixed, the coordinate paired with x determines the coefficient of
delta_x relative to the rational g_K vector. Two distinct overlapping
errors should then give distinct rational points of the pencil. The
original point [v] must remain excluded; no rationality of that point
or of the original parameter values is being inferred.

Completed result: [L034](../lemmas/L034-six-coordinate-equality-projective-descent.md)
proves the overlap distribution, rationality of all paired ratios, and
projective descent by two explicit distinct rational overlap points.
It also proves rationality of the three selected directions and the
disjoint additional direction, and of all normalized actual error
weights. The complete proof and qualifications are canonical there.
The original parameters and point [v] remain unrestricted over F.

Outcome: ADVANCE / RESEARCH / POTENTIALLY_NEW. This is a local necessary
condition beyond the inspected reduction, not certified novelty, the
twelve bound, or a complete solution. The mechanism passes its test
because it constructs rational points using additional paired-root
constraints. It does not make the previously rejected generic descent
inference. No mathematical script or finite sample was used. L034 has
not yet received an independent critical audit. Continue the unchanged
approved twelve-incidence target using this restriction, checking the
new proof before relying on it and retaining the original finite chart;
do not use L015's numerical maximum or assume rational input words.
