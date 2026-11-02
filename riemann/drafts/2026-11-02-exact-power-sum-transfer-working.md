# Exact full-sequence power-sum transfer — working record

Approved target: test the full Newton-Girard/pure-power representation
under the unchanged EXPLORE scope in
`literature/2026-11-02-positive-mass-angular-propagation.md`.
No external theorem beyond that assessment is needed for this attempt.

Main gap: actual-Xi mixed positivity and unbounded-height signs. The
intermediate target is E_n >= c exp(-n/16) D_single,n for the exact
common-pole angular family. Such a bound would give the synthetic
detector, with Xi realization and signs still unresolved.

After reading C645g/o and the C645y prefix failure, set
alpha_a=a/R, b_u(z)=B_u(Rz)=sum_(ell>=0) beta_ell(u) z^ell,
c_k(u)=R^(-1) sum_a r_a W_a(u) alpha_a^k, and
p_j=sum_a r_a (a/x)^j. All n grid factors and all spatial modes remain.

Candidate exact identity, to be checked before promotion:

    p_j = R (R/x)^j / B_u(x)
                  * sum_(ell>=0) beta_ell(u) c_(j+ell)(u).

Multiplication by b_u followed by negative Fourier projection should
give this identity. Because b_u is inner, sum |beta_ell|^2=1.
Thus the coefficient functional has exact ambient l2 norm
R (R/|x|)^j / |B_u(x)|. This may collapse to C645n's full-inner
response rather than repair its loss. Biro applies to p_1,...,p_M
by repeating a/x according to the integer residues; p_0=M is already
known. The key test is whether his conclusion yields anything stronger
than the existing p_0 estimate, not merely whether the identity exists.

Continuation test: a uniform complete-sum transfer with squared loss
at most 1/16, or a precise remaining cost with a discriminating test.
Stop this particular deweighting argument if its sharp norm and the
available pure-power bound only reproduce the stopped inner response.
No conclusion about every nonlinear or family-restricted transfer,
the full energy ratio, or RH is licensed by an ambient norm calculation.

This is saved unfinished reasoning. C645n/L646 are possible overlap
inputs, not yet an excuse to claim a new lower bound. C645y/z and
L647/L648 remain contrasts; no change to their audit status is made.

## Completed bounded attempt

The full proof and precise source applicability are canonical in
[L649](../lemmas/L649-exact-power-sum-deweighting-limitation.md).
The proposed identity is exact, and its normalized operator is a
coisometry. The norm-one rows give the sharp ambient recovery cost;
the complete recovered sequence is exactly C645n's stopped inner-input
response. Biro's imported lower bound is weaker here than p_0=M.
Even the full recovered energy divided by D_single,n, after multiplying
by exp(n/16), tends uniformly to zero, with exponent gap >63/2000.
The discarded kernel component is uncontrolled and may be large.

This is an informative mechanism overlap, not a countersequence for
the admissible family and not a new theorem beyond the checked sources.
The original target survives. Repeating unweighted Newton-Girard
relations or this ambient contraction estimate is not justified.
A different prospective mechanism would have to use the full pole
support to force the discarded component; multipoint Padé/Markov
remainder coverage has not been read or approved. The current action
and routing live only in PROGRESS.md.
