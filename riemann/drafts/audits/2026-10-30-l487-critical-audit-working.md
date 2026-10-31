# L487 finite collision-energy audit

2026-10-30. Completed: the finite certificate passes. The initial
in-progress reasoning below is retained as the interruption checkpoint.
Gate: `drafts/literature/2026-10-30-l487-critical-audit-coverage.md`,
SPECIALIZE, exact TARGET supplied at invocation. The supplied target
and assessment agree verbatim; no changed scope or additional source
is required. Existing unfinished notebook work is preserved.

Main gap: actual-Xi all-degree mixed positivity and signed mass control.
Intermediate target: independently replay the entire L487 quartic
certificate on 0<=t<=1/100. Downstream use: decide whether the generic
bounded backward negative-energy comparison can remain parked on a
verified obstruction. This is not actual-Xi realization or a new lemma.

Continuation/abandonment test: verify all parameter inequalities, complete
root signs, collar flux, internal interfaces, absolute continuity and the
exact analytic energy derivative. Repair any failed claim; a load-bearing
failure requires reassessing the obstruction. No general source theorem
is being reproved. Reuse the approved Alber/Brezis--Ponce coverage and
named analytic implicit-function, Leibniz and integral Gronwall tools.

Initial replay: the finite heat jets, the quadratic roots in z^2, the
cubic Q(t,v), and its four evaluation signs agree with direct expansion.
The three disjoint real-root intervals exhaust the cubic degree. The
interface term in (4) has the correct minus sign and counts all four
endpoints. Collision regularity and derivative scaling are still being
replayed before the final verdict.

## Completed replay

The full proof and the audit's exact algebraic additions are canonical
in `lemmas/L487-quartic-heat-collision-negative-energy-obstruction.md`.
All checks below are for the full closed parameter interval, with
one-sided derivatives at its endpoints where appropriate.

- Heat jets, beta/gamma bounds, imaginary-axis positivity and all four
  z zeros pass. The quadratic discriminant is strictly negative for
  t>0; the modulus identity and gamma<=1 prove the closed strip bound.
- All four Q evaluations pass, including the exact rational lower
  bounds added to the proof. Three distinct real v roots exhaust the
  cubic degree, so no positive root or negative-defect interval is
  omitted. The t=0 factorization treats the colliding roots separately.
- The squared collar coordinates exceed the larger positive v root; the
  negative part vanishes on neighborhoods of both external endpoints.
  Smoothness of q supplies the cited trace hypotheses. No trace theorem
  is needed to delete an internal interface, and none is so used.
- Spatial primitives, time primitives and all three defect jets pass
  expansion. The heat identity and integration by parts give exactly
  minus the four absolute internal slopes plus the retained bulk term.
  In contrast, Leibniz time endpoint terms vanish because q itself is
  zero there. The uniform bound on partial_t Q makes e' strictly positive.
- The positive-part Lipschitz inequality and the explicit M<620 prove
  absolute continuity through t=0 without relying on an exceptional-time
  Sobolev statement. All moving roots are simple for t>0. At t=0 the
  implicit-function theorem is applied to the two simple scaled roots,
  never to either colliding root in the original variable.
- The full scaled polynomial R is now displayed. Its two limiting
  roots and the complete earlier root count identify the analytic
  endpoints. The analytic primitive gives the exact r^3 A(r) identity;
  differentiating that identity proves both derivative asymptotics and
  the ratio limit. It also proves the endpoint derivative directly.
- A locally essentially bounded C gives one finite upper bound after
  the time change. Absolute continuity, nonnegativity and e(0)=0 supply
  every Gronwall hypothesis; e(t)>0 contradicts its conclusion. The
  one-sided time orientation agrees with the proposed inequality.

No load-bearing repair was needed. The additions expose hand-checkable
algebra and explicit constants rather than changing the argument.
This audit verifies the existing generic negative result; it is not a
new obstruction, original discovery or actual-Xi theorem. Source coverage
was reused, with no new browsing, source theorem reproof, numerical
preview or mathematical script. Full Mathlib coverage remains unchecked.

Next-direction screen: the recorded positive-Fourier-kernel/count/gap
countermodel in `ATTEMPTS/2026-09-27-count-gap-positive-kernel-test.md`
and the finite-sign masking stops do not supply an extra actual-Xi
hypothesis. Merely adding another generic polynomial/kernel example
would not justify a creative continuation. An additional arithmetic or
theta-specific discriminator is missing. Instead nominate the separate
ready conceptual audit in
`drafts/literature/2026-10-26-l468-critical-audit-coverage.md`, for its
exact existing TARGET; no L468 proof is audited in this step. It tests
the independent moving-anchor witness-range gap and reuses prior
coverage without a new literature turn. The actual-Xi sign, realization,
mass and effective-onset gaps remain unresolved.
