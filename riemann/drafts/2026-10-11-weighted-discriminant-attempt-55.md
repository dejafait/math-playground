# Fixed quadratic-weight discriminant attempt — step 55

Research / REPRODUCTION under the prior SPECIALIZE assessment
`drafts/literature/2026-10-11-positive-weighted-discriminant-mean.md`.
Exactly its TARGET is being tested; v stays fixed independently of H.

Main gap: actual-theta global mixed positivity. Intermediate target:
the signed Delta mean weighted by (v_0 x+v_1 y+v_2 z)^2. A positive
leading coefficient would force positive physical D in every sufficiently
high dyadic interval. Continue only if the complete quadratic form has a
positive direction with o(log^4 H) errors; otherwise stop this implementation.

Inputs read: audited L390 physical/norm reduction, L391 ordinary jets,
fixed-right-line primitive and connectors, L393 full four-jet formula (5)
and scaled-shift kernel (4), including its exact finite algebra. Prior
source comparison and step-53/54 history supply the duplicate/failure
screen. Preserve the old coarse O(H^2) contour failure.

Unfinished reasoning checkpoint: Cauchy--Schwarz should bound the weighted
physical error by O(log^3 H), since the quadratic weight is O_v(U).
For a fixed head the projected polynomial is K times this weight, a
homogeneous quartic. Conjugation followed by x,y,z=-R D leaves E, so
L391's signed-primitive proof can be specialized after checking the changed
polynomial. The balanced term is M times the weight times |Z_N|^2, using
L393 (5) and every gcd collision of its two head indices. Evaluate all six
matrix entries, then check signed endpoints with a smooth nonnegative U^2
majorant on fixed relative endpoint strips. Full-minus-head error is
O_v(eta_N log^4 H), independently of N. None of these tentative checks
is yet recorded as a proved conclusion.

Independent gaps remain: global mixed positivity, total L367 margin,
actual common-zero control, low indices, heights above forty, and the
endpoint arithmetic margin. No RH, simplicity, noncoincidence or
independent phases are assumed. No positive D witness is currently obtained.

## Completed bounded attempt

The canonical full proof, hypotheses, precise imports and qualifications
are in L394. All six exact matrix entries give a strictly negative-definite
form; the required positive direction does not exist. The proof includes
the changed carrier polynomial, signed sharp endpoints, every gcd collision,
the physical replacement and uniform complete-tail transfer. The exact
certificate is `scripts/discriminant/weighted-coefficient-certificate.json`.
Its full entry tables and division checks were inspected, not merely previewed.
This is an informative NEGATIVE / REPRODUCTION result for the implementation,
not new mathematics beyond the checked sources or an RH disproof. Stop this
fixed-weight sign witness. A separate critical audit remains pending; its
new target requires separate source approval before audit invocation.
