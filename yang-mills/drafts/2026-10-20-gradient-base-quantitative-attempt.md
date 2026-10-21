# Gradient-base quantitative attempt — working record

STEP_ID: YM-20261020-363-gradient-base-explicit-localization

The approved target is the complete R_gx remainder against exactly
L104(6), with threshold O(N^(5/2) log(eN)^2). The main construction
and interacting reflection gaps remain unchanged. Inputs being used
are L102, L103, L104, L028 and L248's supporting raw-mode/heat
estimates, matched to the four traversals in L104(4), rather than any
reverse-trace conclusion. Existing ATTEMPTS/028,029,032 remain intact.

Unfinished test: quantify L104's positive geometric inverse polynomial
in absolute walk sums. A degree proportional to epsilon^-1 log(eN)
has explicit uniform inverse error and sublinear range for
epsilon >= N^-1/2. Compact W should anchor all polynomial walks away
from transverse faces; the cumulative X coefficient itself need not
be compact. Freezing all coefficients along such walks appears to
cost O(N^2 epsilon^-3 log(eN)) in the unnormalized response. This is
not yet a proved bound. Combine only after checking every coefficient,
the half-weight/upper endpoint, both inverse positions and full heat
sum. L103's separate inverse error remains O(N^3 epsilon^(1/4)).

A fully explicit weaker subcubic rate would be useful partial evidence
and a baseline for a sharper joint energy comparison. It would not
meet the requested threshold. Stop this absolute-walk mechanism if
its mass losses cannot reach that threshold; do not claim signed
growth or use fixed-mass convergence at a varying mass.

Completed: the uniform comparison and the full coefficient/heat checks
are now written in canonical L249. Its explicit weaker remainder is
O(N^(38/13) log(eN)^(1/13)); the requested threshold remains unproved.
The estimate's mass loss is exposed rather than hidden in fixed-mass
constants. No script was needed. Separate critical audit is the next
step; the initial unfinished record above is retained as work history.
