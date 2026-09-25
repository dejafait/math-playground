# Target and conventions

## Official scope

Checked on 2026-09-24 and rechecked on 2026-09-25: the [current Clay problem page](https://www.claymath.org/millennium/birch-and-swinnerton-dyer-conjecture/)
links [Andrew Wiles, *The Birch and Swinnerton-Dyer Conjecture*](https://www.claymath.org/wp-content/uploads/2022/05/birchswin.pdf).
The displayed conjecture on printed page 2 is the rank assertion for every
elliptic curve over Q. Remark 1 states a stronger refinement separately.

Let E/Q be an elliptic curve, and write E(Q) = Z^r direct-sum T with T finite.
Following the official description, choose an integral model
y^2 = x^3 + ax + b with nonzero cubic discriminant Delta. Put
S = {primes dividing 2 Delta}. For q outside S let
a_q = q + 1 - #E(F_q), including the point at infinity in #E(F_q), and set

\[
L^S(E,s)=\prod_{q\notin S}(1-a_q q^{-s}+q^{1-2s})^{-1}
\qquad (\operatorname{Re}s>3/2).
\]

Use its holomorphic continuation to define
m(E) = ord_{s=1} L^S(E,s). The exact target of this notebook is

\[
\boxed{m(E)=\operatorname{rank}E(\mathbf Q)\quad\text{for every }E/\mathbf Q.}
\]

This concerns the precise multiplicity, not only whether the central value
vanishes. No restriction to a family, a density-one subset, or ranks at most
one would meet this target.

## Stronger refinement

Wiles's Remark 1 restores the missing finite Euler factors and predicts the
leading coefficient in terms of the order of Sha, a height regulator, a real
period factor, local factors, and the square of the rational torsion order.
In his notation the coefficient is

\[
c^*=|\Sha(E/\mathbf Q)|R_\infty w_\infty
       \prod_{q\mid2\Delta}w_q/|T|^2.
\]

Here R_infinity is the regulator and w_infinity, w_q are the period and
local factors of that statement. This is a separate stronger claim, including
finiteness of Sha; it is not a consequence established here of rank equality.
The restored L-series in that remark does not include an archimedean Gamma
factor. The current step neither proves this formula nor uses it as an input.

## Mathlib

Coverage of the complete rank assertion, the refinement, and the analytic
conventions above: **not checked**. No formalization claim is made.
