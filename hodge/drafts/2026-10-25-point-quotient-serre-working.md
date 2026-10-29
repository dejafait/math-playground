# Point-quotient Serre comparison — step 557 working record

Gate: the invocation-start SPECIALIZE assessment is
`literature/2026-10-25-point-supported-quotient-serre-form.md`.
Work only on its unchanged target, with L109/L111/L116/L164/L165
and L167's intended use. Existing uncommitted work is preserved.

Main gap: primitive algebraic realization and existence of the hypothetical
F remain open. Intermediate target: identify L165's actual quotient form
in L164's fixed point coordinates. Downstream use: access the actual point
quartic, without asserting values of section quadrics or square length.
Continue if the actual adjoint gives a local finite-duality expression;
stop any dependent calculation requiring an unassessed theorem or new
trace normalization. ATTEMPTS/092–094 remain parked with their scopes.

Tentative comparison to check (not yet a canonical result): with
D=RHom(-,O_B), alpha:C[2] -> DC, put
Lambda=(alpha^{-1} Da)[-2]:W^dagger[-2] -> C.
Then r Lambda=0 follows from aj=0, and a Lambda=gamma[-2].
The candidate actual lift is Lambda gamma^{-1}[-2]; its adjoint should
be Da[-2] gamma^{-1}[-2]. Test the global trace against the finite-point
evaluation pairing and retain the base-form normalization. In particular,
do not replace gamma by itself, identify W^dagger with W, or replace a
derived fibre by its ordinary middle fibre.

The actual-arrow calculation succeeds: a Lambda=gamma[-2] and
r Lambda=b^{-1}[-1]D(aj)[-2]=0. Thus phi=Lambda gamma^{-1}[-2]
has a phi=id, r phi=0, and induces L165's unique orthogonal lift T.
Pullback of alpha[-2] through phi has adjoint gamma^{-1}[-2], since
Dphi[-2] Da[-2]=D(a phi)[-2]=id. Global evaluation is therefore
Tr_B((gamma^{-1}u) composed with v), with both shifts even.
Finite-support evaluation splits over Z, giving no cross-point terms.

Local coefficient calculation to record canonically: use L111's actual
Koszul summand, d=c_0/s_0, with d^0=(x,y) and d^1=d(y,-x).
The top generator w maps under the quotient adjoint to the dual bottom
generator times s_0. Relative to the standard resolution with arrows
(-y,x)^t and (x,y), the comparison matrices in degrees -2,-1,0
are d^{-1}, [[0,d^{-1}],[-d^{-1},0]], 1. Both chain equations hold.
Thus the evaluated Ext class on (w,w) is (s_0^2/c_0) epsilon_{x,y}.
If the relative trace is kappa times L164's integral normalization,
ell_z(w)=bar(s_0)/(2 kappa). The coefficient in ell_z coordinates
is consequently 4 kappa^2/bar(c_0) times the canonical base-trace
evaluation of epsilon_{x,y}. No numerical residue value is used.
The full statement and proof are now canonical in L168, with separate
audit pending. Step 557 is ADVANCE / REPRODUCTION, actual task
proof_attempt; no source result is claimed as a new discovery. The
scoped documentation checker passes (169 nodes, 480 edges). No actual
quartic, numerical residue, lower square length or exclusion was computed.
