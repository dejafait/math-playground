# Moment-distribution audit — 2026-09-13

Scoped step following completed L153: determine the information needed to improve
its large-value measure. Normalize dyadic Lebesgue measure to probability and set
X_T=T^(3/2)|S|². L149 gives E X_T→K>0; L153 gives E X_T²=O(log T).

Candidate reasoning, pending audit: Hölder gives P(X_T>θ) at least
((E X_T−θ)^q/E X_T^q)^(1/(q−1)). A spike of height K log T on
probability 1/log T saturates the logarithmic scale even with bounds on all
fixed higher moments of order (log T)^(q−1). This is a countermodel only to
moment information, not to the particular Dirichlet series.

A concrete sufficient distributional target is E[X_T;X_T>M]≤K/4 for a fixed M
and all sufficiently large T. Splitting at K/4 and M would then give positive
probability. Resume by checking constants, the distinction between diagonal
and full moments, and what is conditional before recording a proved lemma.

Completed as L154: the normalization, Hölder/interpolation exponents, exact
countermodel, and fixed-cutoff tail criterion have been checked. The abstract
obstruction is proved; the sufficient tail estimate for S remains unproved.
