# Universal discrete-step repair: checked generic obstruction

The step111 audit reproduced the lambda=3/4 specialization of post49's
all-fixed-scalings obstruction. The canonical proof and exact replay are
in [L955](../lemmas/L955-fixed-pollaczek-step-even-sextic-obstruction.md)
and `scripts/pollaczek/fixed-step-audit-111.json`. This strengthens the
scaling scope of the generic route stop; it does not supersede L530's
different positive-moment-family evidence. No novelty claim is made.

WHY IT FAILS: For any proposed fixed 0<r_0<1, the audited construction
at rho=1/r_0 supplies a simple real-rooted even input with alternating
even basis signs and a nonreal-rooted output. Therefore a propagation
rule using just those hypotheses cannot establish actual-Xi mixed
positivity. A theta-specific restricted class could behave differently;
it still needs independent realization, initialization, signs and limits.
Do not repeat this generic scaling or degree route without a materially
different restricted hypothesis and a discriminating test.
