# Upper-face heat-moment tail — working record

STEP_ID: YM-20261005-046-upper-face-heat-moment-tail

The unchanged SPECIALIZE assessment
`drafts/literature/2026-09-26-current-target.md` is reused inside its exact
combined-response target. Essential inputs are L008 and L030–L032.
Main gap: the full interacting response and ultraviolet-uniform reflected
comparison remain unknown. Intermediate target: quantify all omitted modes
in both pure sectors, using the finite weak differential expansion rather
than the stopped lattice global-norm bound. Downstream use: a complete
spectral-tail bound would make a sufficiently accurate finite evaluation
of the selected power coefficient possible, before testing compensation
in the full coefficient. Independent gaps include quadrature, all other
vertices/pairings, L019 compensation, finite matching, reflected error
<= c_box/2, continuum fields, reflection positivity and infrared mass.

Unfinished reasoning saved before computation: the coupled weights have
exact representations lambda_k^-2 = integral_0^infinity s exp(-s lambda_k)
ds and lambda_ell^-1 = integral_0^infinity exp(-r lambda_ell) dr. These
identities permit future tensor contraction, but do not themselves provide
a certified quadrature. For a bounded test now, use the positive spectral
gap only in the tail estimate, retain all seven free indices, and transfer
coefficient derivatives by compact-support integration by parts. The
weak Q monomials have total derivative degree four and the N2 monomials
degree six. With R^2 the sum of the seven squared indices, the product is
bounded by a computable constant times R^10 exp(-9 R^2/1024). Quantify
the omitted cube via one-coordinate heat moments and exact rational
upper bounds on exponentials. This does not approximate the signed sum.

Continuation test: establish a rigorous analytic bound for the entire
omitted sum and compare it with the retained cutoff-12 values, with no
sign claim until quadrature and finite-sum rounding are also enclosed.
A bound requiring a larger cutoff than the dense implementation can
handle motivates the exact Laplace/tensor factorization; it does not
revive the failed low-mode/global-norm certificate in ATTEMPTS/014.

## Completed bounded proof and exact-arithmetic test

Outcome: ADVANCE / RESEARCH / POTENTIALLY_NEW; actual task proof_attempt.
[L033](../lemmas/L033-upper-face-separable-heat-moment-tail.md) is the
canonical proof. It verifies both an exact double-Laplace representation
and a complete omitted-mode bound from the actual weak monomials.
Compact-support integration by parts avoids bump derivatives. Explicit
conservative coefficient counts prove the constants independently of the
existing numerical implementation; its finite rational expansion also
passes the coefficient-sum and derivative-degree consistency checks.
No general flow renormalization or stress-matching theorem is reproved,
and no originality beyond the inspected sources is certified.

The full exact-rational test is saved in
`scripts/combined-ward-response/continuum-heat-tail-certificate.json`.
Reproduce with `python3 scripts/combined-ward-response/check_continuum_heat_tail.py`.
Selected complete evidence was inspected with the supervisor JSON inspector:
`/expansion_checks`, `/full_moments`, `/rows/3` and `/failures` with `--full`.
At cutoff 112 the rigorous outward bounds are
(1.37381915696e-11,5.49527662781e-11); at cutoff 96 they are
(21.2323460649,84.9293842596). At cutoff 64 they exceed 1e19, and
at cutoff 80 they exceed 1e11. The direct p=10 geometric bound at
cutoff 12 fails: its ratio bound is 1.65495701228, against required <1.
This failure is retained. The initial implementation also exceeded
Python's integer-string size limit when adding large rational denominators;
rounding each positive term outward before addition corrected this without
weakening exactness of the upper estimates. No mathematical failure was
converted into a sign certificate.

The new bound is local mathematical progress toward evaluating a selected
upper-face power coefficient. It does not evaluate that coefficient or
its complete cancellation. The dense seven-index implementation cannot
be used at 112 with its present allocation: one 112^6 binary64 array
alone requires 15,790,581,481,472 bytes. Thus the next concrete subtask
inside the unchanged approved response target is implementation of the
exact tensor/Laplace contraction with all components and coefficients,
first reproducing the existing small-cutoff sums. The integral and
coefficient quadratures require separate enclosures; no accuracy follows
from the algebraic separation itself. A sign test must compare the
certified retained value at the SAME cutoff against its full tail,
quadrature and rounding bounds. This continuation does not reopen
ATTEMPTS/014's failed lattice norm mechanism.

Essential inputs for continuation: L008, L030–L033, and the existing
continuum finite-sum program. Unresolved assumptions are not inputs:
no sign for either pure sum, no compensation by L019, no other
plaquette/pairing or action/measure/insertion/flow-jet control, no
finite matching, no prescribed-trajectory reflected error <= c_box/2,
and no continuum/infrared construction. Exploration usage is 0 of 3
after this explicit tail-bound advance; old stopped branches retain
their recorded evidence. The current checkpoint keeps the exact
combined-response Next action and reuses its unchanged prior assessment.
