# Quartic radial test — saved working state, step418

Gate: unchanged SPECIALIZE review417, supplied at invocation start and
approved for the exact test in this invocation. No new source assessment
or mathematical script is needed. This is a known-tool reproduction.

Main gap: actual-Xi positivity and L984(H), not resolved by this model.
Target: the one specified Q in review417; require both a rigorous bounded
weighted real-radius continuation and failure of the every-epsilon lower
coefficient envelope. If both hold, park inference from the retained
properties alone; otherwise stop this model without enlarging the family.

Working exact algebra (pending completed canonical write-up):
Q(1)=425/256;
H_Q(z)=(17-26z+25z^2)(25-26z+17z^2)/(425(1-z)^4);
ell_1=608/425. The mapped zeros are (13+-16i)/25 and
(13+-16i)/17; all are simple and the inner radius is sqrt(17)/5.
The log-derivative cumulative quotient has residue w/(1-w) at each
mapped zero, hence the inner poles survive the degree-one subtraction.

For s=1/(1-r)>=1, a in {1/4,3/4}, t=s-a>0,
2s(s-a)/((s-a)^2+1)<=2+a by 2t<=t^2+1.
Thus A=r*s*Q'(s)/Q(s) is between 0 and 5, and
B=ell_1*r*(1-r) is between 0 and 152/425. Consequently
|(1-r)^2 F_Q(r)|=|A-B|<=5 for every 0<=r<1.

Pending proof completion: check the local logarithm, coefficients at
degrees0/1, Taylor radius and regularity at positive R; fix
epsilon_0=-(log R)/2 and add D*(z/exp(-epsilon_0))^2 /
(1-z/exp(-epsilon_0)). Pringsheim then forbids nonnegative
coefficients because the correction preserves the inner pole while the
positive point R is regular. This will refute even the envelope at that
one epsilon, with all finite degrees retained.

No actual xi order-one growth, Euler product, zero census or arithmetic
identity is supplied. Existing direct-import scope stop417 remains valid.
Matching full Mathlib coverage is unknown, not asserted absent.

Completion: the full proof, including the fixed-epsilon contradiction
and all finite-degree checks, is now canonical in
`lemmas/C984a-symmetric-quartic-real-radius-coefficient-obstruction.md`.
Both thresholds hold; the earlier pending notes above preserve the
saved intermediate state and do not replace that completed proof.
