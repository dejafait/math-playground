# Expanded residual-discriminant coefficient test is inconclusive

This bounded calculation used C020q's exact two-double-input collision
domain under the unchanged ready assessment1468/review1469. The full
calculation and five passing algebra checks are in
`scripts/quartic-differential/sector-sextic-residual-invariants-1473.json`;
the method and qualifications are in
[working1473](../drafts/working/2026-11-18-sector-sextic-residual-count-1473.md).
No canonical count result was obtained and no lemma was added.

WHY IT FAILS: After factoring the cleared residual discriminant as
k^4*(l^2-4k)*F and substituting L=t*l,
S=t^2*(l^2-4k)>0, z=36*t-9 in [0,1], the coefficientwise Bernstein
positivity test for t^20*F fails. Seven coefficient polynomials are
negative at L=0; the S^17 endpoint coefficient at z=1 is exactly
-5036661/128. The complete transformation and this separately extracted
value are checked. Negative coefficients do not imply that F is
negative, and the test ignored additional admissibility inequalities.
Furthermore, a positive quartic discriminant alone would not distinguish
zero from four real roots. This is an unsuccessful sufficient
certificate, not a family exclusion or a count-increasing witness.

Retain all earlier stops, especially C020o's inverse-method failure and
C020p's restricted fourfold-family exclusion. After two exploratory
collision steps, the continuation changes to direct sign comparisons
at roots of T R for R=(1+l*x+k*x^2)^2, with shared and repeated zeros
retained. Do not repeat the expanded coefficient test without a new
representation or use this failure as evidence against RH.
