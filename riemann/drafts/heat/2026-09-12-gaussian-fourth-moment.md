# Gaussian fourth-moment checkpoint — 2026-09-12

L151 was complete on entry. Preserve all earlier work. Scoped target: improve
L150 to O(T^-2 log(T)^2), leaving the requested one-log bound unresolved.
Draft route: dominate moving b_n by C n^-2 exp(-beta log(n/N)^2), beta=1/2.
For every fixed beta>0 the coprime parametrization of L151 gives envelope
energy D_beta(N)=O(N^-6 log(2N)); prove its H_beta bound at all scales.
Absorb k log(2k)/(N² log(2N)) into half the four Gaussian exponents to
bound sum k A_k² log(2k) by O(N^-4 log(2N)^2). Then L150's elementary
integration-by-parts and harmonic argument applies without the divisor envelope.
These claims are unproved at this checkpoint. Resume by checking Gaussian
absorption, small-X bounds, and all infinite tails before creating a lemma.

Completed as L152 after analytic verification. Gaussian energy holds for every
fixed beta>0; absorbing the weighted k log(2k) factor at half width closes the
two-logarithm estimate. The one-logarithm full bound remains unproved. No draft
claim beyond the stated L152 result is promoted to a graph input.
