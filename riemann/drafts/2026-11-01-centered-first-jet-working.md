# Centered compressed first jet: bounded attempt

1 November 2026. The unchanged approved target and source comparison are
in `literature/2026-11-01-centered-first-jet-numerical-radius.md` (EXPLORE
before invocation). One proof attempt; no fresh source assessment is
needed for the same hypotheses. Main gap: actual-Xi initial signs at
unbounded heights and all-degree mixed positivity. The target could
reduce L629's first-degree cost; higher degrees and transfer stay open.

## Saved reasoning before verification

Use L627's exact rational basis, full-tail scalar identity, and centered
matrix K=Pi_N(H-mu_N)Pi_N. Write K=D+R+E for its centered diagonal,
raising part and exceptional lowering part. The earlier estimates give
|D_nn|<=(4/3)log n and ||E||<=6. For raising m=n p^j<=N,
0<=R_mn<=(4/3)(log p)p^(-j/2).

Candidate weighted quadratic estimate: choose v_n=n^(-1/2). Incoming
raising row at m has weighted sum <=(4/3)log m. The outgoing weighted
sum at m is <=(4/3) sum_(p^j<=N/m)(log p)/p^j
<= (8/3)log(N/m), using the finite factorial estimate, with floor(N/m)
and an empty sum if N/m<2. Applying 2uv<=u^2+v^2 with the weight ratios
would give

    |<Ry,y>| <= sum_(n<=N)
        [(2/3)log n+(4/3)log(N/n)] |y_n|^2.

Combining the diagonal gives at most 2log N times ||y||^2, and E adds
at most 6. This would prove the precise approved threshold with C=6,
including complex y by taking coordinate moduli. It is only a scalar
compression argument; it does not assert a compressed-product identity.

Verification pending: check both weighted row orientations and endpoints,
the boundary coefficients in L627 (6), centering in (9), full-tail basis
change, and the elementary constant for E. No numerical matrix is a
certificate. Continue only if these give a uniform proof; otherwise
retain the failure and do not infer the target from a leading constant.

## Completed bounded attempt

The pending checks give the bound with C=6. Full hypotheses, exact
boundary coefficients, the finite floor-factorial estimate, both
weighted row orientations and the all-complex-vector argument are
canonical in L630. The lowering-tail constant is checked by an integral
bound. No finite matrix calculation or asymptotic evidence is used.
The result meets this intermediate target for every N>=2, without
solving the independent signed higher-degree or pointwise gaps.

The scalar projection removes orthogonal output only from <Hf,f>;
it does not remove a divisor tail from f, change C_N(q), or justify
iteration of a compressed operator. This is why it avoids the precise
full-output loss in L627 without contradicting its warning. Reused
source scope is unchanged; no nilpotent or one-variable restricted-shift
theorem is applied. The local result and its inputs remain subject
to a separate critical audit. No source refresh, mathematical script,
cross-notebook import or infrastructure edit was needed.
