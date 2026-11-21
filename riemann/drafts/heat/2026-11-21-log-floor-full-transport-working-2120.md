# Full logarithmic-floor transport working2120

Approved target and assessment: exact rate40 regular-time inequality in
`drafts/literature/2026-11-21-log-floor-full-transport-review-2118.md`
(SPECIALIZE saved before invocation). Main gap remains L030-L032/C032a
actual-Xi all-degree mixed positivity. Test one quantitative specialization
of C488a, using audited C488d for the nearby real-partner cost. No
collision, integrated finite-head, time-zero or global conclusion is part
of this attempt. Continue if all full-domain coefficients fit40; failure
of this sufficient majorant would not refute the actual-family inequality.

Assembly completed in canonical C488e; the proposed constants below
close the exact target. This preserved working note is not an independent
audit. Consult `lemmas/C488e-logarithmic-floor-regular-time-transport.md`
for the full hypotheses, proof, qualifications and Mathlib status.

Partial reasoning saved before final assembly: with s=sqrt(x^2+R^2),
L=log(2+s)>5, |L'|<=1/R and |L''|<=1/R^2 (the latter is the
difference of two nonnegative terms each <=1/R^2). Thus
|eta'|/eta<=1/(5R), |eta''|/eta<=7/(25R^2), and
|p''|/p<=42/(25R^2)<2/R^2. Also |p'|/p<=6/(5R), so on a
segment of length<=R, p is <=exp(6/5)<4 times either endpoint;
w has factor<3. The count part of a nearby nonreal unordered pair
is <=8(p_j+p_k)/R^2; the height part is <=(9/2)(h_j+h_k)/R^2.
The combined endpoint coefficient8 is sufficient. Own-conjugate loss
is reserved for C488d and must not be double counted.

Provisional assembly, to be checked in the canonical proof: distant
horizontal multiplier <=(12/5)A_j/R; C488a's paired reciprocal bound
is N(2m)/R+5log(32m), m=|x_j|+R. Hence total <=
[8N(m)+(12/5)N(2m)+12Rlog(32m)]A_j/R^2.
Using N(u)=(u+20)log(4u+40), this is <=
[(64/5)m+208+12R]log(32m) A_j/R^2,
which is <=(646/25)m log(32m) A_j/R^2<26m log(32m) A_j/R^2
for m>=R>=200. Required threshold40. No sampled-domain or
actual-zero computation is involved. Remaining check: exact regular-time
finite-sum differentiation, conjugation-invariant distant split and
opposite-paired tail factors. This working note is not a verified result.
