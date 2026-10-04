# Fixed-prime prime-deletion test at p^2

Working record for the single target approved in
[the saved assessment](literature/2026-10-03-rank-zero-extra-relaxed-prime.md).
No new literature search is needed; exact formulas are reread from the
already inspected Sakamoto 2022 source for this application.

## Gap and continuation threshold

The needed rank-two lower bound concerns rational Kummer directions.
The intermediate test asks only whether the actual two prime-deletion
classes remain classical Selmer classes after coefficient reduction is
reversed from E[p] to E[p^2]. Passing permits a further-depth test;
failure of an auxiliary local condition stops automatic fixed-index
promotion. Rationality, analytic production of the two-prime premise,
the determinant comparison and higher ranks remain unresolved.

## Reasoning saved before completing the proof

Put N = ell_1 ell_2 and retain delta-minimality modulo p. First require
ell_i in Sakamoto's P_(2,0); membership in P_(1,0) alone is insufficient.
Use compatible generators and the coefficient-compatible systems from
Theorem 3.17/Proposition 3.19, not unrelated choices of finite systems.
Write c_i^(m) = kappa_(N/ell_i,ell_i)^(m) after trivializing the G factors.
Corollary 4.10 supplies the basis c_1^(1), c_2^(1).

Definition 2.18 gives, at level two, the singular localizations
v_(ell_i)(c_i^(2)) = delta^(2)_(ell_j) and
v_(ell_j)(c_i^(2)) = phi_(ell_j)^(fs)(kappa_(1,ell_i)^(2)), j != i.
The third relation also gives
delta^(2)_(ell_i) = -phi_(ell_i)^(fs)(kappa_(1,ell_i)^(2)).
Thus checking only delta_(ell_j) misses the other index prime.

At level one, delta-minimality and the two-prime localization
isomorphism force kappa_(1,ell_i)^(1) = 0. The coefficient exact
sequence therefore writes kappa_(1,ell_i)^(2) = iota(h_i), with h_i
in H^1(Q,E[p]). Cartesian local conditions and residual surjectivity
of localization at ell_i should place h_i in the classical Selmer
group. This gives an explicit first-order error vector for each
prime-deletion class.

To be proved carefully: both actual c_i^(2) are classical if and
only if the reduction Sel_(p^2) -> Sel_p is onto. The reverse
implication should use a classical lift of c_i^(1), subtract an
injected mod-p Selmer class to kill its finite localization at the
other prime, and compare two lifts in F_cl^(ell_i)(ell_j). Their
difference lies in its residual subgroup, which is classical.

The Kummer diagram identifies the cokernel of this reduction with
Sha[p]/p Sha[p^2]. This is not finite Sha, nor a rational-rank
certificate. An exact conditional criterion would connect the
arithmetic family to the existing higher-descent defect rather than
repeat L001's abstract countermodels.

## Mathlib

Full coverage of this proposed specialization: **not checked**.
Supporting coefficient exact sequences, Cartesian local conditions,
finite-singular maps and the Kummer diagram: **not checked**.
No claimed full-statement library match or novelty conclusion.

## Completion of this working record

[L015](../lemmas/L015-prime-deletion-p2-selmer-lifting-criterion.md)
proves the claims marked for checking above. In the eligible-prime
case, both prescribed family components are classical exactly when
the classical reduction is onto, equivalently Sha[p] = p Sha[p^2].
The two first-order error vectors h_i lie in the residual classical
Selmer group, and both components are classical exactly when both
vectors vanish. The proof tracks both auxiliary primes and uses
Cartesian propagation for the reverse implication. Conditional
success gives an R_2 Selmer basis, not a rational-point basis.

The actual h_i and the Sha-divisibility condition remain uncomputed;
no automatic lifting theorem or arithmetic counterexample is claimed.
This is a reproduced specialization of the assessed arithmetic
family and the standard Kummer diagram. No numerical experiment was
needed, and the former rational-correction obstruction is untouched.
The unfinished unconditional question stays within the same approved
fixed-prime p^2 target; no new source assessment is added in this turn.
