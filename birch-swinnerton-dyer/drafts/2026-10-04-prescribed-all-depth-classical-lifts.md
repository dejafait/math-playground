# Working calculation: prescribed compatible classical lifts

Date: 2026-10-04. Approved target: apply Kim's Theorem 1.8 and the
natural coefficient maps to C016a's prescribed depth-two Selmer basis,
retaining the divisible Sha radical. The saved SPECIALIZE assessment is
[the all-depth review](literature/2026-10-04-central-vanishing-all-depth-classical-lifting.md).

The main gap is rational rank equality for analytic order at least two.
Here the required conditional lower bound is r >= 2; the achieved bound
is r <= 2. Compatible classical lifts could eliminate finite descent
defects and identify the remaining obstruction to rational membership.
Continue the lifting implication if the paired structure rules out every
finite factor and the natural maps lift both fixed initial classes.
Abandon it if a permitted finite factor survives or compatibility needs
an additional hypothesis. No new auxiliary-prime eligibility is assumed.

The calculation to finish is:

1. Surjective E[p] gives E(Q)[p^infinity] = 0. The coefficient inclusion
   identifies S_m naturally with S_infinity[p^m], using the global long
   exact sequence and the local Kummer kernels. Downward maps become
   multiplication by p, not coefficient inclusions.
2. Kim's known decomposition has divisible corank d and paired finite
   factors. C016a gives infinitude and dim S_1 = 2. Thus
   2 = d + 2t with d > 0, forcing d = 2 and t = 0.
3. Fix ONE isomorphism S_infinity = (Q_p/Z_p)^2. Its torsion coordinates
   identify the full coefficient tower with (Z/p^m)^2 and reduction.
   The prescribed basis at depth two is a matrix in GL_2(Z/p^2).
   Lift that matrix to GL_2(Z_p) to obtain compatible bases at every depth.
4. The infinite Kummer sequence still has a divisible quotient. Show
   Sha[p^infinity] = (Q_p/Z_p)^(2-r); the Cassels pairing is zero on
   this subgroup because it lies entirely in its divisible radical.
   The inverse-limit quotient is T_p Sha, not a finite descent error.

This uses the assessed structure and Kummer inputs; it does not reprove
Kim's theorem or infer rationality from his finite-Sha clauses. L001's
finite-tower models and the stopped L016/L017 promotion packages remain
preserved. The new arithmetic input relative to those tests is C016a's
central-value consequence and the known infinite paired structure.

Proof details and the final continuation decision are being recorded in
L018. This checkpoint makes no claim of a complete BSD argument or of
progress beyond the checked literature.
