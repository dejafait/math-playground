# Opposite total defect — separate bound specialization

TARGET: Derive a fixed-parameter upper bound for the total normalization length of L120's opposite image using L121, L137 and Hoa's Hilbert-coefficient bounds.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed projective-degree discovery assessment and 2026-10-20-opposite-total-defect-hilbert-bridge.md; no new theorem-discovery search is needed for this specialization.
SOURCE_EVIDENCE: Hoa arXiv:math/0608118v1 Theorems 0.2/4.1, pp. 2/15–16, https://arxiv.org/pdf/math/0608118v1 ; Stacks 41.7.3 (04DG), 30.14.3 (0AG7), 30.14.1(4) (01YS), 33.35.14 (08AC), 33.33.2–3 (08AA/0AYT), 30.2.4 (089W), read in the bridge assessment: https://stacks.math.columbia.edu/tag/04DG , https://stacks.math.columbia.edu/tag/0AG7 , https://stacks.math.columbia.edu/tag/01YS , https://stacks.math.columbia.edu/tag/08AC , https://stacks.math.columbia.edu/tag/08AA , https://stacks.math.columbia.edu/tag/0AYT , https://stacks.math.columbia.edu/tag/089W .
COMPARISON: Known reduced-ring coefficient bounds and finite-morphism/Euler theorems cover the general tools; only their actual-image application and explicit bound in L137's fixed parameters remain. No general theorem needs reproving.
GAP: Establish finite support of the actual quotient and the exact constant-term/length identity, then combine the covered inequalities. No numerical ell,k,N, nonempty collision locus, useful lower comparison, F or transport is supplied.
REASON: One bounded known-tool specialization is justified by completed bridge coverage; this newly written ready continuation receives a separate approval next turn.
SCOPE: Exactly L071/L118/L120/L121/L137's conditional opposite family, full negative integral tensor, identical marked factors and common metric, original integral reduced image and unchanged fixed projective embedding. Allow empty collisions, arbitrary finite multiple fibres and linear degeneracy; assume neither normality nor CM nor coherent vanishing of Z.

Use essential inputs L071, L118, L120, L121 and audited L137.
First apply Stacks 04DG at closed singleton fibres, retaining the
normalization injection and coherent-support/Jacobson passage.
Then compare coordinate and Euler polynomials using 0AG7, 01YS and
08AC. Use the normalization exact sequence with 08AA, 0AYT and
089W. Evaluate Hoa's full binomial expression at zero rather than
identifying its last coefficient with that value. Retain n=N+1,
d=3, c=N-2 and e=adeg=delta from L137, including possible linear
forms in the image ideal. State the actual resulting length bound
in fixed parameters and every sign/constant; no script is needed.

Continue only if all parameters are independent of F and the unknown
defect and the stated sources cover every hypothesis. Stop and record
the exact missing hypothesis if they do not. A finite bound passes
this intermediate test, but is not a contradiction: a later exclusion
requires an independently justified geometric lower bound exceeding
it. F existence, collisions, transport and universal primitive Hodge
realization remain unresolved. Preserve ATTEMPTS/070,073,078 and the
parked order-five route. Matching Mathlib coverage is not checked.
