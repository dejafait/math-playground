# Standard inputs and the limits of their scope

These are named starting results checked for route selection on 2026-09-24, with the Darmon–Merel and full-modularity statements audited on 2026-09-25. This is not a complete literature survey. The local-solubility argument uses none of their deep proofs.

## Fermat's Last Theorem

For every integer n > 2, a^n + b^n = c^n has no positive integer solution. This standard named theorem is the equal-exponent control case. See Andrew Wiles, *Modular elliptic curves and Fermat's Last Theorem*, Annals of Mathematics 141 (1995), 443–551, [publisher record](https://annals.math.princeton.edu/1995/141-3/p01), and the companion Taylor–Wiles paper in [the same issue](https://annals.math.princeton.edu/1995/141-3). The named theorem is being cited, not reproved from the publisher metadata. It makes no assertion that arbitrary unequal exponents can be replaced by a common exponent.

## Darmon–Granville finiteness

Henri Darmon and Andrew Granville, *On the equations z^m = F(x,y) and Ax^p + By^q = Cz^r*, Bulletin of the London Mathematical Society 27 (1995), 513–543, **Theorem 2**, printed p. 515: fixed positive exponents with 1/p + 1/q + 1/r < 1 and fixed nonzero integer coefficients give only finitely many primitive integer solutions. The statement was read in the [author-hosted paper](https://www.math.mcgill.ca/darmon/pub/Articles/Research/12.Granville/pub12.pdf#page=3).

For the present coefficient-one equation and exponents at least three, the reciprocal sum is below one except at (3,3,3), which Fermat's Last Theorem excludes. This supplies finiteness for each fixed remaining signature. It supplies neither zero solutions nor a uniform finite list as the signatures vary. No effective height bound is asserted here.

## Darmon–Merel signature results

Henri Darmon and Loïc Merel, *Winding quotients and some variants of Fermat's Last Theorem*, Journal für die reine und angewandte Mathematik 490 (1997), 81–100: the [author-hosted version](https://perso.imj-prg.fr/loic-merel/wp-content/uploads/merel-pub/winding.pdf#page=2), **Main Theorem, parts 2 and 3**, gives no nontrivial primitive integer solution to a^n + b^n = c^2 for n >= 4, and to a^n + b^n = c^3 for n >= 3 under the stated hypothesis that every elliptic curve over Q is modular. In this paper, trivial means abc is 0 or ±1, and primitive means gcd(a,b,c) = 1. Negative integer bases are permitted. The definitions on PDF page 1 and theorem on PDF page 2 were reread; this hosted version is dated January 5, 2001.

The historical hypothesis in part 3 is discharged by the separately cited theorem below. Neither clause is used in the local-solubility proof. Their direct scope requires repeated exponents and the stated square or cube; even powers cannot absorb a minus sign.

## Full modularity over the rationals

Christophe Breuil, Brian Conrad, Fred Diamond, and Richard Taylor, *On the modularity of elliptic curves over Q: Wild 3-adic exercises*, Journal of the American Mathematical Society 14 (2001), 843–939, **Theorem A**: every elliptic curve over Q is modular. The statement was read on PDF page 1 of [Breuil's author-hosted version](https://www.imo.universite-paris-saclay.fr/~christophe.breuil/PUBLICATIONS/STW.pdf#page=1); [publisher DOI](https://doi.org/10.1090/S0894-0347-01-00370-8).

This is precisely the hypothesis in Darmon–Merel's cube clause, so that clause is now unconditional. Modularity alone is a supporting input, not a theorem excluding every mixed Beal signature.

## Mathlib

Full coverage of the named results and relevant supporting theorem names: **not checked**. No absence claim or formal-verification claim is made.
