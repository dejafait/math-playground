# Step 537 — actual adjoint factor-cup working record

Approved target: test the two actual harmonic trace forms for L117's
K=J^{-1}Phi_1, retaining W_0 and unknown t. Prior SPECIALIZE assessment:
`literature/2026-10-25-adjoint-factor-cup-sign.md` (covered target).

Main gap: universal primitive Hodge realization; F existence is itself
unproved. A spectral restriction on the actual K could constrain later
section/deformation arguments, but an independent contrary condition
would still be needed. Stop if either positivity or the comparison with
the actual j needs an extra premise. No change to stopped sign routes.

Inputs read: L116 in full; L117's construction/audit; L071's actual
connection and factor restrictions; L159's ordinary operator and frame
calculation as a convention comparison, not an imported trace sign;
ATTEMPTS/069 and /091; the ready source assessment and its earlier
coefficient-Lefschetz coverage. Existing unfinished changes preserved.

Working calculation, to be completed canonically: with coefficient
involution rho(A)=-A*, ordinary j_form(a)=J_quat(bar(a)), put
R(A tensor a)=rho(A) tensor j_form(a). Then R^2=-1. In the common
unitary quaternionic coframe, tr(alpha_i wedge R beta_i) equals
(1/2)<alpha_i,beta_i> bar(sigma_i), with Hilbert-Schmidt coefficient
metric. Thus with common normalization 1/8 the two integrated forms
are respectively the L2 norms of the second and first components.
The base form Q_2 is nondegenerate by L117's actual J isomorphism,
R's invertibility and coefficient Serre duality. For Q_1, a vanishing
second component makes the first component holomorphic along every
second-factor fibre. L071 gives charge 21 there, hence stability
(21 is not 14r^2) and no trace-free endomorphisms. This would force
the first component to vanish too. Check this at the smooth-form level,
without assuming restricted representatives harmonic.

Actual-map comparison to finish: j_3 Phi_1=theta_1 cup j_1 and
j_3 J=theta_2 cup j_1 imply Q_1(u,v)=Q_2(Ku,v) by the same global
Serre pairing. W_0 is retained in those identities; no multiplicative
splitting or local vanishing of Ext^2 is used. If all checks hold,
K is positive self-adjoint for Q_2 when t>0, vacuous for t=0.
This would be local conditional progress only, with no exclusion.

Completed in L163: the polarized norm formulas, both radical tests and
the actual-map comparison establish the conditional positive operator.
The full proof/citations are canonical there; this preliminary record
is preserved, not a second proof. A separate critical audit is pending.
