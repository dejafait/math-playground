# Self-duality test of the fixed-prime p^2 errors

This is a continuation of the exact COVERED_TARGET in
[the saved SPECIALIZE assessment](literature/2026-10-03-rank-zero-extra-relaxed-prime.md).
Its hypotheses and coefficient depth are unchanged. The already assessed
Sakamoto source is reread for its dual local conditions and finite-singular
relations; no new source search or literature assessment is performed.

## Gap, intermediate target and decision test

The main gap is the lower bound on rational rank, not Selmer dimension.
L015 supplies a conditional fixed-prime p^2 classical-lifting criterion.
Here the intermediate target is to determine whether actual global
self-duality and the two-prime finite-singular relations force its
remaining residual errors h_1,h_2 to vanish. Vanishing would settle this
depth and permit an additional lifting test; rational membership, higher
depths, analytic production of the minimal index and higher ranks remain
unresolved. A nonzero error compatible with precisely these constraints
stops the automatic-vanishing deduction from this package.

This test adds actual local Weil/Tate pairings to L015. It does not repeat
L001's unmarked finite-tower comparison or L013's cyclotomic determinant
model, and does not reopen the rational subtraction in ATTEMPTS/016.

## Reasoning saved before completion

Set R = Z/p^2 and choose finite and transverse bases u_i,t_i at ell_i.
Both lines are self-orthogonal. The local Tate form is symmetric: the
degree-one cup-product sign and the alternating Weil-pairing sign cancel.
Writing its value in R, it has the form
lambda_i (a b' + b a'), with lambda_i a unit.

Write loc_(ell_i)(c_i^(2)) = A_i u_i + D_j t_i, j != i;
the A_i are units and D_j = delta_2(ell_j). At the other prime,
c_i^(2) is transverse and its coefficient is divisible by p. Global
reciprocity applied to c_i^(2) with itself gives
2 lambda_i A_i D_j = 0 in R. Thus D_1 = D_2 = 0, since p is odd.
L015 now forces h_1 to lie on the residual c_2 line and h_2 on the
residual c_1 line. Reciprocity for c_1^(2),c_2^(2) gives one skew relation
between the two surviving transverse coefficients; it need not kill them.

If their common normalized scalar tau is nonzero, a linear combination
of the prescribed lifts is classical only when both residual coefficients
are zero. Any classical lift differs from this combination by iota(S_1),
which has no auxiliary singular component. The expected conclusion is
therefore rho(S_2) = 0 in this case, rather than a one-dimensional image.
The Kummer diagram would then give r = 0 and p Sha[p^2] = 0, hence all
p-primary Sha is killed by p and has order p^2. These implications need
careful verification; they do not evaluate tau for an actual curve.

For the surviving-error test use the graph of p J in the hyperbolic
module R^2_finite direct-sum R^2_transverse, where
J = [[0,-1],[1,0]]. This is a free maximal isotropic submodule with
residual finite space F_p^2, classical intersection p R^2 and zero
classical reduction. It should satisfy all two-prime finite-singular
equations in L015 with g_1 = p c_2 and g_2 = -p c_1. Only this truncated
localization package is modeled: no full Kato system, global Galois
cohomology realization or elliptic-curve counterexample is asserted.

## Mathlib

Full coverage of this specialization: **not checked**. Supporting local
Tate forms, Weil-pairing signs, reciprocity and coefficient maps: **not
checked**. Sakamoto's Theorem 2.1, Definitions 2.3/2.4/2.18 and Section 2.3
support the imported framework; they are not asserted to match this entire
calculation or to be Mathlib theorem names.

## Completion

[L016](../lemmas/L016-prime-deletion-alternating-p2-obstruction.md)
proves the saved claims. The doubly relaxed group is always free of rank
two at depth two, with the actual prescribed components as basis. Its
classical intersection is governed by the residual alternating form with
matrix [[0,tau],[-tau,0]]. It is the whole relaxed group when tau = 0 and
its p-socle when tau != 0. Thus classical reduction is respectively all
of S_1 or zero; a one-dimensional image is excluded. The nonzero case
forces rational rank zero and p-primary Sha isomorphic to F_p^2.

The surviving-error model satisfies maximal isotropy, coefficient
compatibility, all four tracked errors and the two-prime finite-singular
equations. It has tau = 1. The exact p = 5 enumeration in
`scripts/prime-deletion/check_p2_reciprocity.py` passes for both tau = 0
and tau = 1, checking the full ambient orthogonal complement and the
classical intersections. This is not an arithmetic realization or an
extension to the complete auxiliary-prime family.

The outcome is NEGATIVE for automatic promotion from the tested
self-duality package, with a useful actual-family dichotomy established
in the process. The step is REPRODUCTION of the assessed framework;
no progress beyond checked literature is claimed. The actual tau remains
uncomputed. The next mechanism within the unchanged covered target is
the explicit Section 2.5 Stark-system contraction, to test whether the
construction supplies a further global constraint on that coefficient.
No new assessment or extra mathematical target is attempted here.
