# Quartic endpoint stationary phase — 2026-09-13

Draft checkpoint, not yet a proved input. Preserve L181 unchanged.
Put s=t−π/2 and s0=2π sqrt(k). The exact phase is
φ(s)=s log(k/N⁴)−2[s log(s/(2πN²))−s−π/4].
At its saddle φ(s0)=2s0+π/2. Set
z=sign(s−s0)sqrt(2[s log(s/s0)−s+s0]); then φ=φ(s0)−z².
Planned uniform formula: kernel equals exp(iφ(s0))*sqrt(s0)/h
 times the finite Fresnel integral from z− to z+, with O(1/h) error.
To prove: write dt/dz=sqrt(s0)+z*g(z/sqrt(s0)), g uniformly C¹,
and integrate z*g*exp(−iz²) by parts. L181's strip count would
make the normalized summed remainder O(1). Endpoint transitions must
remain inside the finite Fresnel factor. Signed arithmetic cancellation
is still unproved. Resume by checking this Jacobian estimate, summing its
error, and recording a qualified lemma only if both checks succeed.

Completed: L182 proves the formula with O(1/h) kernel error and O(1)
absolute accumulated error. The finite Fresnel limits retain both endpoint
transitions. The signed product sum remains unestimated beyond L181.
