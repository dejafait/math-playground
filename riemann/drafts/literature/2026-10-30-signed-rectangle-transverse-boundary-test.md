# Signed rectangle: bounded transverse boundary test

TARGET: Test the first-transverse-mode Green identity for signed rectangle detectors, seeking a nonvanishing K-weighted absolute-cost lower bound for each fixed Fourier radius R, or a quantified boundary-leakage obstruction to that bound.
CHECKED: 2026-10-30
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse the completed exact-class and stronger-result comparison in drafts/literature/2026-10-30-signed-rectangle-absolute-cost-review.md. The proposed boundary test stays within that signed family and uses the elementary identities inspected there; no matching quantitative theorem was found and no novelty is inferred.
SOURCE_EVIDENCE: Direct primary URLs verified 2026-10-30: Kovrijkine https://arxiv.org/pdf/math/0012186v1 Theorem 1, pp. 1--7; Brevig et al. https://arxiv.org/pdf/2210.13922v2 Theorem 3.6, pp. 12--13; ABR https://axler.net/HFT.pdf#page=12 second edition, 17 July 2020, (1.1)/(1.2), printed p. 4. Reuse the parent review for proof coverage; this approval rechecked theorem hypotheses and ABR divergence proof.
COMPARISON: Signed norm control and Green's identity are known. Turning positivity on a tall off-axis rectangle into a nonvanishing weighted boundary norm is not supplied by those results. The first-mode test is an uncovered quantitative combination, not an ordinary Harnack specialization or an already proved obstruction.
GAP: Control the complete boundary expression using only rectangle positivity and fixed Fourier radius, with an explicit conversion from the K-cost to any unweighted norm used. All signs, constants, height dependence and possible cancellation remain to be established.
REASON: Removing full-strip positivity materially changes the feasibility problem; a boundary balance can test whether that change avoids its audited obstruction. The separate literature-only approval on 2026-10-30 repairs the missing direct-URL field; coverage is ready for its unchanged bounded mathematical invocation.
SCOPE: One first-transverse-mode boundary test for exactly the family below. No general construction search, other scales, arithmetic application or further target is approved here.

## Family and proposed discriminating threshold

For real T tending to infinity let L=log T, delta=log L/L,
a=log L/pi, b=log L/(4pi), B=L/(4pi), and
K(x)=1-(sin(pi x)/(pi x))^2 with K(0)=0.
For each sufficiently large T, f_T is even entire and real on R, with

    f_T(z)=integral phi_T(v) exp(2pi i v z) dv,
    phi_T in C_c^infinity(R), supp phi_T subset [-R,R],
    Re f_T(x+iy)>=1 for |x|<=a and b<|y|<B.

Here R>0 is fixed independently of T; phi_T and its derivative bounds
may vary without a uniform bound. There is no sign restriction elsewhere.
Put M_T=integral |f_T(x)|K(x)dx. The desired family has
M_T<=C log L L^(-c) for some fixed positive R,C,c.

For each fixed R, the proposed necessary-bound target is
M_T>=kappa_R>0 beyond an onset T_R, uniformly over this class.
This would exclude every fixed C,c>0 for that R. It is a target only.
Any weaker bound must be compared honestly with the desired cost;
L^(-A_R) alone cannot exclude all positive c.

## One mechanism and stopping test

Use u=Re f_T and the first positive transverse Dirichlet mode
cos(pi x/(2a)) on [-a,a]. Attempt the corresponding Green/boundary
identity in a finite rectangle with horizontal levels strictly between
b and B. Account for both vertical faces, both horizontal faces and
every normal derivative; boundary values at b or B require justified
limits. Green's smooth-boundary formulation needs direct iterated
integration by parts or a controlled treatment of corners. Do not delete
a boundary term merely because u is positive inside the rectangle.
No identity or differential inequality for the projection is asserted
by this assessment.

Fourier support may be used for signed real-axis norm estimates.
If Kovrijkine is applied, verify its thickness condition, Fourier units
and constants independent of T. The zero of K at the origin must be
handled explicitly. Point-evaluation duality is a comparison, not a
ready formula for this weighted continuum problem. No reproof of the
cited general theorems is intended; the justification for local work
is precisely the missing quantitative boundary combination.

Continue only if the complete expression yields the discriminating
bound or a sharper, independently testable residual estimate. Otherwise
save the actual residual with its justified scale and stop this mode
before another attempt; failure of this test is not nonexistence of the
signed family. An unbounded or unsigned boundary term with no estimate
is an unresolved gap, not an informative negative result by itself.

## Relevance and remaining obligations

Main gap: actual-Xi positivity and initial signs at unbounded heights.
A feasible signed detector could support a weighted off-line statistic;
a necessary-cost obstruction would eliminate one sufficient geometric
class. Negative contributions at actual zeros, uniform moving-test
errors, kernel and height transfers and initial signs remain separate.
No RH, simplicity, spacing or external half-plane estimate is assumed.
No local lemma is a premise: L502 is contrast only, L018 future
coordinate interpretation only. Mathlib coverage is unchecked.

The separate source-gate approval is complete. The mathematical test has
not been completed, and no novelty is asserted.

## Direct-source approval: 2026-10-30

All three primary URLs above were accessible through the web tool.
Kovrijkine Theorem 1 retains the Lp, interval-support and every-interval
thickness hypotheses; any weighted specialization remains future work.
ABR printed p. 4 states a bounded smooth domain and C^2 functions near
its closure, with outward normals; its divergence proof was rechecked.
No rectangular boundary formula or sign estimate is imported. Brevig
et al. Theorem 3.6 retains 1<=p<infinity and the unweighted PWp
extremizer context; its two proof directions and p=1 duality qualification
are available on printed pp. 12--13. It remains comparison only.

The parent review supplies the prior exact-class search, stronger-result
comparison and full-strip failure comparison; these remain unchanged.
No additional search or new theorem is needed for this narrow repair.
Outcome STALLED: this removes a process blocker but adds no mathematical
evidence and does not renew exploration counters. EXPLORE approves only
the stated boundary test, with all unresolved estimates retained above.
