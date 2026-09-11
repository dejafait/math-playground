# Exterior window estimate checkpoint — 2026-09-11

Draft, not yet promoted. Fix a strip |Im ρ|≤H, target w=a+ib with |a|≤A and 0<b≤H, and exterior cutoff R>A. Define the full-multiset tail T(R)=Σ_{|Re ρ|>R}|ρ|^(-2). For u=Re ρ and v=Im ρ,

|ρ|²/|w−ρ|² ≤ (u²+H²)/(|u|−A)² ≤ (R²+H²)/(R−A)².

The last function is decreasing in |u|>A. Thus the exterior upward sum is at most 2(H−b)(R²+H²)/(R−A)² T(R). For R≥2A and R≥H the comparison factor is ≤8. No bound controls targets right up to the same cutoff without a buffer. For fixed additive buffer d the displayed coefficient grows quadratically in A.

Resume audit: prove the comparison without differentiating, check full-zero versus paired-tail factors, and state the multiple-zero local rate with the quartet removed. Store only the static estimate and its local rate consequence; time-uniform control remains unproved.

Audit completed: the two ratios x/(x−A) and H/(x−A) give the comparison directly. The tail counts all zeros, so no extra pair factor belongs in (1). Absolute imaginary summability permits the multiplicity-m quartet extraction. The final result is stored in L129. The proportional-buffer annulus remains outside the scope of the bound.
