# Square-variable transport — completed signed-interface comparison

TARGET: Assess whether Min–Kang's Lorentz–Laguerre transport equation gives a signed boundary-to-negative-axis estimate sufficient for L233's D_1 threshold, retaining the forcing term and the full all-height domain.
CHECKED: 2026-10-31
DECISION: EXPLORE
SEARCH_EVIDENCE: Exact transport-title, author/square-variable, boundary/forcing/negative-axis and chain-rule queries located primary transport and companion half-plane PDFs; narrow notebook searches checked earlier square-variable leads, first-sign differential and zero-compensation assessments, and Fourier-transfer/backward-energy failures. No inspected matching all-height signed estimate was found; no novelty claim.
SOURCE_EVIDENCE: Min–Kang, A Lorentz–Laguerre Transport Equation for the Square-Variable Riemann Xi Function, v1, 27 September 2026, Sections 1–7, Theorem 3.1, Corollaries 3.2/4.1–4.4/5.1, Remark 5.2 and Proposition 6.1 with complete proofs, printed pp.2–6; companion An Explicit Half-Plane of Complex Laguerre Positivity for the Square-Variable Riemann Xi Function, v1, 26 September 2026, Theorem 1.1, Lemma 3.1, Lemmas 5.1–5.2, Proposition 6.1, Theorem 7.1 and Sections 8–10, printed pp.2,4,6–12, inspected as qualified below.
COMPARISON: The exact transport fixes x=a^2-b^2. Its sign corollary imports positive forcing on x>=-0.1613 and starts from zero data at y=0. Neither this nor the companion parabolic region estimates forcing on the missing negative-axis segment. Actual-Xi normal curvature additionally needs the nonlinear-square derivative correction.
GAP: No independently bounded signed forcing or transverse derivative budget reaches L233's all-height D_1>=0 threshold; higher signs also remain open. No new coordinate-curvature lemma or estimate is derived here.
REASON: New negative source evidence parks citation-only fixed-x transport as a first-sign proof, without a no-go theorem for other mechanisms. EXPLORE records the bounded comparison, not permission to assume positive forcing or repeat the same integration.
SCOPE: Literature comparison only; no global sign calculation, lemma, mathematical script, source-manuscript audit or RH candidate is approved. A transverse mechanism has a separate REVIEW_REQUIRED nomination.
LITERATURE_REASON: Invocation-start essential transport hypotheses, boundary cases and forcing were unread; this turn fills that coverage rather than refreshing a ready target.

## Exact primary statement and proof cases

Use F_s for the source square-variable function, distinct from L233's
Fourier transform F=2Xi. The primary
[transport PDF](https://www.alphaxiv.org/abs/2609.lorentz-laguerre-transport-riemann-xi.pdf)
is dated 27 September 2026; its landing page labels it v1.
It defines xi(1/2+z)=F_s(z^2), H(x,y)=|F_s(x+iy)|^2,
M(z)=F_s(z^2)/F_s(0), P=-V|M|^2, and

    x=a^2-b^2, y=2ab, R=a^2+b^2, V=b partial_a+a partial_b,
    L_s(u)=|F_s'(u)|^2-Re(F_s''(u) conjugate(F_s(u))).

Sections 1–2, equations (4), (10)–(12), give H_yy=2L_s,
Vx=0, Vy=2R, VR=2y, and P/R=-2H_y/F_s(0)^2 for R>0.
Theorem 3.1, printed p.3, assumes real a,b, R>0 and this actual F_s,
with F_s(0)=xi(1/2) nonzero. It states

    V(P/R)=-8R L_s(x+iy)/F_s(0)^2.

Read its complete proof: apply V to H_y, use Vx=0, Vy=2R,
then H_yy=2L_s. No sign estimate enters. Corollary 3.2's monotonicity
is exactly equivalent to the forcing sign at the same point.
Corollary 4.1, printed p.4, retains the full equation

    VP-(2y/R)P=-8R^2 L_s(x+iy)/F_s(0)^2.

There is no division by F_s(u), hence no singularity at its zeros.
Corollary 4.2 multiplies through by R at the origin; Remark 4.3 extends
P/R as -2H_y/F_s(0)^2, with value zero by evenness. Neither supplies
a quantitative curvature bound at that point.

Section 5 equation (20), printed p.4, gives the characteristic form

    partial_y(P/R)=-4 L_s(x+iy)/F_s(0)^2, with x fixed.

Corollary 5.1, printed p.5, expressly assumes the companion theorem
L_s(u)>0 on Re u>=-1613/10000. Its entire proof fixes such an x,
uses H_y(x,0)=0, and obtains P<0 for y>0. It supplies no transverse
boundary data. Remark 5.2 includes x=-c<0 using
a=sqrt(c)sinh(tau), b=sqrt(c)cosh(tau), and handles x=0 separately.
Negative/null orbits are not excluded from the transport identity.
Proposition 6.1, printed p.6, is the x>0 rapidity version and assumes
L_s>0 for every 0<tau<=T; its complete proof includes P(0)=0.
It does not produce that sign from boundary data.

## Stronger companion region and mismatch

Read the primary
[half-plane PDF](https://www.alphaxiv.org/abs/2609.complex-laguerre-positivity-riemann-xi.pdf),
v1, dated 26 September 2026. Theorem 1.1, printed p.2, uses this F_s
and includes the boundary Re u=-0.1613. The stronger parabolic region
in Proposition 6.1, printed p.9, is

    x+y^2>=1/2 implies L_s(x+iy)>0.

Read the relevant geometric and product-limit cases in Sections 5–7,
printed pp.6–9. For an off-line zero 1/2+d+i gamma, 0<d<1/2,
gamma>0, its square-variable conjugate pair has
A=gamma^2-d^2, B=2 gamma d and block Q(u)=(u+A)^2+B^2.
Lemma 5.1 states L_Q(x+iy)=2((x+A)^2-B^2+3y^2).
Outside the disk (x+A)^2+y^2<=B^2 both the curvature sign and
logarithmic-derivative imaginary sign are controlled.
Lemma 5.2 places every obstruction disk strictly below x+y^2=1/2
using B^2-A<1/4. Section 6 uses Lemma 3.1's product identity,
common imaginary-part signs, a fixed positive block contribution and
locally uniform derivative convergence. It does not obtain strict
positivity merely by passing positive finite products to the limit.
The disk-plus-parabola proof of Theorem 7.1 was inspected;
Appendix A's coefficient intervals and underlying moment table were
not audited or installed as inputs.

L018 and the source definitions identify Xi(t)=F_s(-t^2): the target
locus is the unbounded negative real axis y=0. This identification is
a definition comparison, not a new differentiation lemma.
The half-plane leaves that axis uncovered when t^2>0.1613;
the parabolic region contains no negative real-axis point.
At fixed negative x the latter controls forcing only beyond an
intervening central segment; no signed budget across it is supplied.
Because Vx=0, the flow cannot change uncovered x into covered x.
Square-variable vertical curvature also differs from the second
normal derivative of |xi(1/2+a+it)|^2: the nonlinear square map
contributes a first-derivative correction. No correction estimate is
in the inspected proof; no formula for it is derived here.
Companion Sections 8–10, printed pp.10–12, expressly retain the
left-half-plane gap and make no RH conclusion. The earlier pairing
and orbit-tangency papers are references, not inspected theorem inputs.

## Relevance, local failures and decision

The main gap is actual-Xi all-degree positivity. The intermediate
target was a signed boundary/forcing estimate for its first sign;
success could support D_1 while higher signs remain independent.
L233 fixes the exact threshold and Fourier normalization.
The test required covered all-height data and an independent signed
remainder bound reaching that threshold. The domain, invariant and
correction mismatches fail that test. This NEGATIVE is source-routing
evidence, not new mathematics beyond the sources.

Narrow searches found no ready matching transport assessment; the
October 5 Gaussian-response assessment explicitly listed this source
family as unread. Reused the October 26 first-sign differential and
September 27 zero-compensation comparisons: an equation, coarse counts
or kernel signs do not bound a signed defect. The direct Fourier-
transfer failure remains separate. L487's backward-energy obstruction
concerns heat collisions, not this Lorentz equation; it gives no global
transport ban. L055's generic kernel conditions do not refute actual Xi.

Queries submitted included the exact title, Min/Kang square-variable
transport, Lorentz/Laguerre/Xi boundary forcing negative axis,
square-variable chain-rule Laguerre, and the referenced unique
positive-height tangency title. Both essential PDFs were accessible.
Snippets, abstracts and the tangency lead are not theorem evidence.
No source blocker, cross-notebook input, Mathlib matching claim,
new lemma/script or canonical argument change is reported.

Park direct fixed-x transfer. Reopening requires a new transverse
estimate or proved signed central-forcing budget. The next proposed
normal-curvature review is separately unapproved. A creative attempt
is not yet justified: its signed remainder/interface remains missing.
Narrow checks also rejected older L473/L528 audit continuations as
already completed in their canonical files, despite stale overview
shorthand; no repeat audit is scheduled.
