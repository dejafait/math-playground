# Attempt: combine log-concavity with superexponential kernel decay

Date: 2026-09-09

Outcome: failed generic real-zero sufficiency claim.

For a=1/100, the mixture h_a(u)=(9/10)exp(-cosh(2u))+(exp(-cosh(2(u-a)))+exp(-cosh(2(u+a))))/20 is smooth, positive, even, and has theta-scale superexponential tails. Lemma 50 proves globally that (log h_a)''<-cosh(2u)/4. Its Fourier transform is (9+cos(az))G(z)/10 and has a nonreal zero at (π+i log(9+√80))/a.

**WHY IT FAILS.** Even strict global log-concavity together with superexponential decay does not prevent a positive small-shift mixture from introducing an explicit factor with nonreal zeros. The log-concavity proof controls both the central region and all tails, so this is not an unproved stability assertion. The displayed nonreal zero lies outside the actual Ξ horizontal strip; this construction has not yet duplicated that extra zero-confinement property. An argument using confinement as well would require a further test, not a claim that this counterexample already settles every combination of properties.

Next lemma: prove the Fourier growth bound for the superexponential mixture and examine whether modifying the positive mixture weights can place its nonreal zeros within the same strip while retaining log-concavity.
