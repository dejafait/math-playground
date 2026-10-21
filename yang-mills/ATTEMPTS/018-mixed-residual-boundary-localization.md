# Uniform boundary localization of the mixed residual cross covariance

WHY IT FAILS: [L060](../lemmas/L060-mixed-cubic-residual-cross-covariance.md)
computes the actual upper-noise/conditional-link cross block as
K_s=-(s/N)P-g_s(Delta_T)(I-P). Its concatenated squared operator norm
is (N-1)(2N-1)/(6N), asymptotic to N/3, rather than uniformly bounded.
The gradient sector persists at macroscopic depth even though residual
link variances are bounded within a fixed number of upper-face layers.
Taking a transverse curvature removes this sector, but a transverse
cubic derivative need not vanish on a gradient variation. This stops
only estimates that discard the gradient block or assume uniform
boundary localization before contraction. It does not prove a leading
power, a nonzero correction, or failure of cancellation in the complete
signed response. A joint gradient-sector contraction with the actual
observables is a distinct test; conditional centering alone is not one.
