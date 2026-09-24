# Functional-equation lower-bound attempt — 2026-09-12

Apply the zeta functional equation to the Mellin remainder in hopes that the absolutely convergent zeta series on Re(s)=2 supplies a center lower bound. The exact interchange and its leading approximation are proved in [Lemma 146](../lemmas/L146-functional-equation-returns-the-original-series.md).

WHY IT FAILS: the gamma multiplier varies in phase across the Gaussian integral. Its leading expansion returns exactly the earlier weighted series S/C, retaining the phases n^(iτ), with an additive O(sqrt(τ)) error before rescaling. The reciprocal-zeta lower bound cannot be passed through this complex integral. This calculation supplies no new lower estimate; it does not prove that every possible analysis of the exact representation must fail.
