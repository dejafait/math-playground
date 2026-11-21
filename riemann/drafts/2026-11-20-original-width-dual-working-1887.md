# Original-width continuous dual attempt1887

20 November 2026. Saved working notes under the unchanged EXPLORE
assessment1885, approved at invocation. The completed proof is now
canonical in C034m; this preserves the reasoning before completion.
The auxiliary result is pending a separate conceptual audit.

Main gap: L030-L032/C032a actual-Xi all-degree positivity. Exact target:
the original-law observation-measure constancy question in PROGRESS at
turn start. A nonzero continuous separator would obstruct unrestricted
uniform residual-law approximation on [1,2]; excluding such separators
would remove only this obstruction, not solve realization or RH.

Source/duplicate check: notes1886/1740 and C033l give the exact family,
signed-measure scope and approved elementary tools. C033j exact range,
C034l fixed cap and C034k two observations are contrasts. Stops1571,
1576,1781,1782,1790,1792 are preserved and not retried. C032n's odd
scalar-span recursion is not used. Relevant input formulas are C032j's
all-positive-width heat transform and C032s's separate j=0 heat error.

Provisional route to check completely:

1. Continue B_sigma(s) on the connected width sector Re sigma>0,
   |Im sigma|<Re sigma. For each compact width set, the transformed
   heat sum should have an integrable time dominator uniform in
   s in [1,2], allowing Haslinger's cited integration theorem and
   integration against arbitrary finite |h|.
2. Put q=4*sigma, a(s)=sqrt(s)/4 and
   d=gamma_E+2*log(4*pi). The real j=0 heat estimate suggests
   B_sigma(s)=a(s)*(log q-d)+E(q,s), with
   sup_[1,2]|E|=O(q^(-1/2)*log q). Pay the full small/large-time
   integrals, including the exact log(1+1/(q*t)) correction.
3. If constancy extends to all positive widths, uniform decay first
   forces c=0. Then the weighted pushforward of h under a(s) would
   have ordinary Laplace transform O((1+y)*exp(-3*y/4)), y=log q.
   Its support is [1/4,sqrt(2)/4], strictly below 3/4. This is a
   potential signed-error discriminator, not yet a uniqueness proof.
4. Do not cite an unassessed signed support theorem. Test an elementary
   exact Cauchy-transform identity obtained by integrating the ordinary
   Laplace transform against exp(-z*y). The faster decay may continue
   that Cauchy transform through the entire support. Any inference
   back to the measure needs a complete signed argument, including
   singular parts and endpoint atoms.

Continue only with paid domination and exact signed-transform recovery.
If this leaves uncontrolled cancellation, park the mechanism. All
fixed-v1, divisor/conjugation/multiplicity, ordinate-zero exclusion,
strict strip/gamma>14, counting, through100/retained-real-zero,
reciprocal-square, heat positivity/separate fixed-j through2 and
Gaussian half-variance qualifications persist. No source-wide
verification, smoothness/sign restriction on h, or Xi transfer assumed.

## Saved discriminating step

The uniform remainder estimate is sufficient if paid: its absolute
action against finite |h| gives decay exp(-3*y/4), whereas the
weighted pushforward support is [1/4,sqrt(2)/4]. This need not rely
on the sign or first nonzero point of h.

For that pushforward nu, let F(y)=integral exp(-a*y) dnu(a).
The faster decay defines J(z)=integral_0^infinity exp(-z*y)F(y)dy
holomorphically on Re z>-3/4. For Re z>0, Fubini gives the exact
Cauchy transform J(z)=integral (z+a)^(-1)dnu(a). Identity on the
connected half-plane minus the negative support extends this equality.
The circle centered -1/3 with radius1/4 encloses the negative support
and lies within Re z>-3/4. Integrating exp(t*z)J(z) around it gives
zero by Cauchy's theorem and 2*pi*i*F(t) by the Cauchy formula and
finite signed Fubini. Thus F(t)=0 for every t>0; the already covered
Jordan-part Laplace uniqueness then gives nu=0. This is a proposed
complete exact recovery argument, to be checked and written canonically;
no support theorem or perturbative uniqueness import is assumed.

## Completion

[C034m](../lemmas/C034m-original-width-observation-dual-injectivity.md)
pays the complex-width domination, exact uniform remainder and signed
contour identity, and concludes h=c=0 under the retained inputs. The
decisive exponent3/4 exceeds the entire support endpoint sqrt(2)/4.
No script or numerical certificate was needed. This removes the
specified continuous dual witness, not the independent Xi gaps.
Critical review remains unpaid. The same exact target and unchanged
assessment1885 can be reused for that audit: its hypotheses and
analytic-width/exact-transform mechanism have not changed, and no
additional source theorem is introduced by the contour recovery.
