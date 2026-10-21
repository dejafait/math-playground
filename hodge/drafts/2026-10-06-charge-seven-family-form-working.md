# Charge-seven family-form attempt — working checkpoint

Approved target: compute the charge-seven family Mukai two-form and
test Kodaira--Spencer injectivity for L060's conditional F at L044's
exact h. The saved SPECIALIZE assessment covers this target.

Inputs read: L044 (exact chamber and full mixed operator), L048
(character convention), L052 (connection and all-fibre polystability),
L060 (conditional F and stable charge-seven fibres), ATTEMPTS/044--045.
Existing notebook changes are preserved. No F existence is assumed.

Main gap: universal primitive Hodge algebraicity. Intermediate target:
evaluate the actual family trace/Yoneda form. Downstream use: a local
injectivity constraint on any prospective bundle. Continue if the full
mixed tensor gives a justified nonzero form; abandon this differential
test as uninformative if it vanishes or its normalization cannot be
justified. Global F and transverse transport remain independent gaps.

Reasoning in progress: the raw mixed character acts by D, with
D(sigma)=2lambda sigma. Pure point terms cannot contribute to the
parameter-holomorphic-two-form/target H^2(O) component. The exact
conversion from the relative Atiyah square to the ordered Yoneda
pairing still needs checking, including exterior and cohomological
signs and the Chern comparison convention. No pullback coefficient
or injectivity conclusion is asserted in this checkpoint.

Completion: the direct Dolbeault calculation is saved in canonical L062.
It gives C_F(sigma)=2lambda sigma and, with its explicit ordered
integral normalization, beta_F=-2lambda sigma. Nondegeneracy forces
kappa_x injective for every x. The local source retrieval reused
approved coverage; it was not approval of a changed target. An
independent convention audit is proposed with REVIEW_REQUIRED
coverage; global existence and transport remain unresolved.
