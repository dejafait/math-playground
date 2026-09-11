# Correction mass checkpoint — 2026-09-12

Existing L147 and prior changes are preserved. Current step: quantify the absolute mass of its correction using L139's integral-versus-sum argument.

Draft calculation: set a=π/4, y=log(x/N), Q(y)=5(−a+iy)−i((−a+iy)²+1/2). The mass profile is c₀ x^(−2)e^(−y²)|Q(y)|. Its integral is C₁/N, where C₁=c₀∫e^(−y²−y)|Q(y)|dy>0. Variation is bounded by V/N² with V=c₀∫e^(−y²−2y)|Q'(y)−(2y+2)Q(y)|dy. Use the complex profile and the modulus inequality to avoid assuming differentiability at zeros of Q.

Resume: prove this quadrature bound, convert to B t^(−3/2)+O(t^(−2)) after dividing by t, and compare with L147's remainder. Expected conditional threshold is δ<3/2; at δ=3/2 a coefficient larger than B suffices. These are sufficient conditions from absolute bounds, not necessary conditions for the actual center. No lower bound is proved.

Completed: L148 proves the mass asymptotic with the explicit variation error and the conditional threshold, including the endpoint constant. Analytic checks confirmed the derivative factor, Gaussian integrability, modulus quadrature argument and power conversion. No unfinished claim in this draft has been promoted to a lower bound.
