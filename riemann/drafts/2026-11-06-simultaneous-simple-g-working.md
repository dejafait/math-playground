# Simultaneous simple-G contact — working checkpoint

Completed later in the same bounded step: the full proof is now canonical
in `lemmas/L860-simultaneous-simple-g-nonzero-j-positive-germ.md`.
The unfinished sketch below is preserved as the interruption checkpoint;
it is superseded by that proof and is not independent evidence.

Invocation-start coverage: `drafts/literature/2026-11-06-simultaneous-simple-g-contact-scope.md` (EXPLORE), exact saved target. One mathematical attempt; conditional on two distinct nonzero simple zeros of the actual G. No selected actual pair or global conclusion.

Unfinished calculation, 6 November 2026: with w=z1-zeta and t=z2-eta, write the full form as w t H(w,t) dw wedge dt, H(0,0)!=0. The candidate divisor-preserving coordinate is v=t B(w,t), B^2=2 integral_0^1 s H(w,s t) ds. Then v v_t=t H and omega=w v dw wedge dv, including both divisors. The inverse t=h(w,v) should satisfy h(w,0)=0 and h_v(0)=1/B(0), h_w(0)=0.

Test the real surface w=x+i y, v=k(x-i y). Its exact parameter density is -2i k^2 (x^2+y^2). At the center the angular determinant is -Im(k/(zeta eta B(0))). Choose k from the signed pair of directions exp(i pi/4), exp(3i pi/4) so that this determinant is nonzero and has the same sign as -2i k^2. Need a common inverse neighborhood, the original angular graph, and an everywhere nonzero full J; no sign may be inferred from the parameter density alone.

First-order discriminator to finish: q(p+epsilon v)/epsilon^2 tends to K0 l1(v) l2(v), K0!=0. If one real-linear coordinate differential has rank one, reality forces the other into a real line and nonnegativity forces proportional kernels, contradicting their nonzero complex determinant. If both have rank two, the allowable tangent should be l2=c conjugate(l1) with K0 c>0. This is only a planned argument until written completely.

Preserve the free-germ boundary and full-phase two-period stops. No automatic gluing, contact forcing, global torus, all-degree transfer or RH claim. Final canonical proof and independent later audit remain to be supplied; this note is not a result certificate.
