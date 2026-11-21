# Approved angular-box test — working checkpoint, step420

Main gap: actual-Xi all-degree mixed positivity. Work is restricted to the
exact target approved in `literature/2026-11-04-exceptional-angular-box-mass-test.md`.
L018/L021 supply actual G, its entire positive-coefficient expansion and
the normalization G(z)=xi_1(z/4)/8. Reuse the saved Katkova source assessment;
the exact angular identity is known, not a new result.

Provisional proof plan, not yet a verified bound: coefficient positivity
gives |G(R exp(i theta))|/G(R)<=1, hence inside mass at most
(2 k^(-2/5))^(r^2). Use the positive-axis sector asymptotic and convexity
of log G(exp(t)) to relate sqrt(R) log R to the scalar mean k, without
differentiating an asymptotic error. Then seek a uniform exp(-Ck) lower
bound on a fixed arc inside |theta|<pi/2. Place r disjoint intervals on
that arc and retain pairwise distances proportional to (j-i)/r. The full
distance product, rather than its minimum spacing, is needed to avoid
an artificial r^2 log r loss. All interval volumes must be included.

Still to verify: radius existence/uniqueness, dilation, exact uniform
sector statement, nonvanishing on the arc, C_in>0, every volume and
Vandermonde estimate, and comparison with exp(r^2 log(r)/10).
No signed phase or minor sign follows. Success stops only this shrinking
core against the full absolute complement. Failure is inconclusive.
The earlier L765/L766/L774 mechanisms are contrasts, not premises.

Completed step420: the provisional checks are now supplied in canonical
L775. The bound exceeds the requested threshold; it stops only the
full-absolute-complement certificate. Independent review remains pending.
This working checkpoint preserves the initial plan, not a second proof.
