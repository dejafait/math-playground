# Step196 — independent moving-eta audit notes

Gate: reuse the supplied SPECIALIZE assessment
`drafts/literature/2026-11-10-moving-eta-critical-audit-review-194.md`.
Audit only L972; no new index inequality is being derived.

Independent replay so far: L026 gives |beta|<1/16 and
|Im beta|/Re beta<16/63, hence Re(beta^2)>0. On |z|<=1/4,
the finite odd-binomial sum bounds |P_n| by 2^(n-1); the normalized
analytic power has modulus |1+z/4|^(-n/2). Thus L964's 3^n bound
does not use its negative-margin hypothesis. Cauchy on radius 1/4
gives the complete Taylor remainder 8*9^n*|z| on radius 1/8.

For s=eta_n and t=s/9, the complete subtraction is (s-t) times
sum W(beta)*a_n(beta)^2, W=z^2/((z+s)(z+t)). The real-part
numerator is |z|^4+(s+t)|z|^2 Re z+st Re(z^2). Both signs of
the subtraction and all denominator factors agree with L972.
The separate majorants are sum |W|<=A/s and
sum |W*(a_n^2-n^2)|<=8*9^n*A. These license the separation;
no sum of bare constants is used. The exact final factor is 1/9.

Completed the canonical audit record in L972, retaining
multiplicity/conjugation and off-diagonal checks. No defect found.
The different next target is the fixed-parameter second-difference
sign test, a prospective independent component rather than a result;
its changed scope is recorded as REVIEW_REQUIRED. The retired
pointwise and reflected-prefix payment rules remain stopped.
