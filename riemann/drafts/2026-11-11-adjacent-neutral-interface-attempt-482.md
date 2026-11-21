# Adjacent neutral interface: working record, step482

This is the one mathematical attempt approved by the unchanged EXPLORE
assessment `drafts/literature/2026-11-11-adjacent-neutral-interface-attempt-480.md`.
The fixed question is beta_1<1/2 on complex, exactly two-moment-neutral
C_c^infinity(0,ell), ell=log(3)/2, using the full unshifted energy.
No threshold, separation, denominator or test-class change is permitted.

Main gap: actual-Xi positivity (L030-L032/C032a). A strict adjacent
neutral-cell margin could pay nearest-neighbor terms; remote coupling,
moment complements, their mixed terms, odd signs and global propagation
remain independent gaps. Decisive tests: a uniform beta_1<=b<1/2, or a
certified nonzero exactly neutral smooth pair with ratio>=1/2. Otherwise
retain the exact unpaid comparison, without claiming either result.

Inputs read: L740 hypotheses/conclusion; L741 hypotheses/conclusion and
Sections2-4; L743(2); L744 Section1/(6). The completed step480 source
comparison and its failure distinctions are reused. Zhu's sign theorem
and the available constant1 are imported, with its unreplayed computation
qualification. No RH or cross-notebook theorem is assumed.

Working reduction (to be fully justified before any result is asserted):
write F(v)=f(ell-v), lambda_n=2n+1/2, d=log(2), a=d/sqrt(2).
L741(21)-(24) gives a continuous Hankel interface plus the retained
partial reflection J_d F(s)=1_(d-ell,ell)(s)F(d-s).
The two completion moments vanish. The n=0 exponential response of
k(u)/2=sum_(n>=0)exp(-lambda_n u) also vanishes exactly.
Thus the candidate remaining pairing is minus the sum of response
products for n>=1, minus a<J_d F,g>. Finite-support smooth tests allow
the response sum; a uniform estimate must also cover approach to the
interface. Carleman boundedness alone does not give the required
relative constant. The single-cell denominator has no prime delay
and has zero pole product, but retains the full digamma symbol.

Current unpaid step: compare this neutral-compressed response operator
and the exact arithmetic reflection with the unshifted logarithmic
single-cell energy. No numerical certificate or strict margin is yet
established. This file preserves unfinished reasoning before longer work.

## Completed attempt

The full analytic reduction, sharp neutral L2 tail norm, and its limits
are now canonical in C744i. The slow response cancels, but every fixed
remaining response tail still has neutral L2 norm pi/2. Its sharpness
sequence has diverging energy and complete relative ratio tending to zero.
The fixed beta_1 test is therefore inconclusive, not refuted. Full proofs
are not duplicated here.

The locator `scripts/adjacent-neutral/interface-diagnostic-482.py` saves
all six runs in its adjacent JSON. Degree128/order1024 gives about0.467919
and a finite half-test L2 margin about0.065717, without enclosures. The
prime pairing contributes about0.465988 and the continuous pairing
about0.001930 to the energy-one maximizing vector. Exact moment enforcement,
smooth transfer, quadrature errors and an all-space tail are uncertified.

The precise unpaid certificate is C744i(6): one uniform mu>0 for both
E+/-2X on N. Pure L2 response-tail shrinkage cannot pay it. A finite
Legendre section with a rigorous logarithmic-energy complementary bound
is the refined continuation, subject to separate source coverage in
`drafts/literature/2026-11-11-adjacent-neutral-weighted-section-certificate-482.md`.
