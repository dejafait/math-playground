# Ordered static comparison — deterministic matching work record

Approved target: Test the ordered static bound |U_i^0(F^0)-a^(-3)K_(i,Vmix)|<=C_i N^(5/2)log(eN)^2 against exactly L179(7), for both actual probes.

Reuse the unchanged EXPLORE assessment in
literature/2026-10-20-smooth-action-ordered-static-rate.md. The main
gap remains interacting reflected-error control and the independent
continuum/infrared requirements. One intermediate test within this
target is to replace all deterministic coefficients of L257's
triangular trace by their continuum samples, leaving both finite
massless Green inverses and the action's separate level unchanged.

Working calculation: L257(8) bounds the ordered Green/multiplier/JG
contraction by C sqrt(N) times the multiplier supremum. The full
triangular axial weight has sum O(N^3); there are O(N^3) transverse
closing vertices and boundedly many local closing stencil entries.
With the original coefficient factor a^3, the absolute envelope is
O(N^(7/2)). Thus an O(a) normalized deterministic discrepancy would
give O(N^(5/2)), with no transverse commutation. This is a proposed
error count until every coefficient and the heat tail are checked.

Essential inputs: L156 L175 L178 L179 L248 L257. L248(3),(8),(11)
give the raw exterior and heat estimates on the same modes; L179(10)
gives the complete two-order local generator comparison. The action
extension must be checked globally at the original (t,Y), rather than
only on compact generator rows. Keep normal end rows, constant axial
indices, the sole -6 and both Q subtractions through L175 only.

Continue if the complete coefficient replacement costs at most
N^(5/2) with a summable polynomial heat envelope. Abandon a factorization
requiring coefficient/Green commutation, an upper forest extension,
or a varying-mass use of L179. Boundary transfer and transverse action
freezing remain independent obligations even if this test succeeds.
ATTEMPTS/030/038/045 and unfinished prior work remain preserved.

The intended downstream use is a precisely defined smooth-coefficient
finite Green trace whose quantitative continuum comparison, combined
with L257 and L256, would finish this component. No new literature
assessment, audit approval or full static rate is inferred.

Completed: [L258](../lemmas/L258-massless-static-complete-coefficient-matching.md)
proves the complete deterministic replacement with O(N^(5/2)) error.
Its canonical proof includes the full action-extension estimate,
original-order telescoping, both heat matrices and omitted labels.
The exact sampled comparison remains on the finite massless Green
space and has L179(7)'s qualitative coefficient by L257's controlled
comparison. No quantitative boundary/freezing/quadrature rate is proved.
The new result awaits separate critical audit; its classification is
REPRODUCTION, without a claim of progress beyond the checked sources.
Continue the unchanged approved static target on this reduced trace.
