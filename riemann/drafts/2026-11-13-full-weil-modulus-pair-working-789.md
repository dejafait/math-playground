# Fixed-pair calculation, step789 — working record

Approved target: assessment `drafts/literature/2026-11-13-full-weil-modulus-pair-test-788.md`; full nonneutral Q, no semigroup theorem invoked.

Main gap: L030-L032/C032a. Test Delta<=0 only for the specified bumps.
Using L744(5)-(6) and L741(7),(13),(16)-(18), the candidate exact cross defect is
Delta=2 integral u(x)v(y)[4cosh((y-x)/2)-k(y-x)] dx dy,
k(d)=2exp(-d/2)/(1-exp(-2d)). Cross separations lie in (49/50,51/50).
All arithmetic correlations vanish: self differences have magnitude<1/50; cross differences have magnitude in (49/50,51/50); log2 lies in (1/50,49/50), and log3>51/50.
The gamma scalar and cutoff subtraction cancel by pointwise uv=0 before taking the cutoff limit. Pole difference is +8 integral uv cosh; gamma difference is -2 integral uv k. These factors need to be stated fully in the canonical proof.
Uniform bound: exp(49/25)>1+49/25+(49/25)^2/2>4, so k(d)<8/3, while 4cosh(d/2)>=4. This gives Delta>(8/3)(integral u)(integral v)>0, violating the requested threshold.

This is a provisional local calculation to preserve reasoning. No RH conclusion, negative Q value, ground-state conclusion, semigroup criterion or novelty claim follows. Final canonical proof and independent review remain to be recorded.

Completed: canonical derivation is C998z, including exact support/exponential bounds and all cross-term factors. The provisional result was retained; independent audit remains pending.
