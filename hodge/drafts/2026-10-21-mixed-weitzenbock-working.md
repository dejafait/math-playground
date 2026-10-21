# Mixed product Weitzenböck calculation — working checkpoint

Approved target: derive the product projection of Oliveira–Waldron v2
(4.6) and test its full mixed energy coupling on the simultaneous
quaternionic su(2) module. Pre-existing SPECIALIZE coverage is
`drafts/literature/2026-10-21-equality-mixed-curvature-weitzenbock.md`,
including its exact COVERED_TARGET. No changed source scope is needed.

Main gap: universal primitive Hodge realization. Intermediate target:
a vanishing-forcing mixed Bochner identity could obstruct the hypothetical
L071 equality F. Independent gaps remain F existence, reconstruction,
transport, other representatives and the universal conjecture.

Inputs read: L071 connection passage; L095 coefficient harmonicity;
L131 SU(2) passage; the supplied general formula; reused Fowdar invariant
module assessment; ATTEMPTS/082 and the distinct product-splitting and
normal-curvature source comparisons. No completed duplicate was found.

Working calculation, not yet a verified result: write R=P+K+Q with
indices a,b on the first factor and mu,nu on the second. Substitution
omega=R in (4.6) suggests the mixed bundle term
-2 sum_b[P_ab,K_bmu]-2 sum_nu[K_anu,Q_numu]. Product Riemann mixed
terms vanish; Ricci terms vanish by Ricci flatness; the parallel
form-leg projection commutes with the rough Laplacian. HYM supplies
Delta_A R=0, not Delta_A K=0.

Test: verify this projection, its multiplicities and exact coefficient
sign with explicit invariant matrices. The energy coupling is cubic and
odd under R -> -R. An exact nonzero value therefore rules out a universal
favorable sign. Retain both pure blocks and describe the full zero
equation; do not promote a pointwise tuple to global curvature.

Continue only for a verified sign/zero-locus statement. A wrong-sign
tuple parks this universal sign mechanism; even a semidefinite result
forcing parallelness would require a separately assessed argument.

Completed: the canonical derivation, exhaustive zero-fibre description
and both-sign witnesses are in L143. The original working calculation
above was confirmed with both pure blocks retained. Exact negative
energy -32 occurs with |K_m|^2=8 and both pure blocks nonzero; no
universal favorable sign exists. The script and full certificate are
under `scripts/mixed-weitzenbock/`. No global F was excluded. Current
status and the sole next action are recorded in PROGRESS.md.
