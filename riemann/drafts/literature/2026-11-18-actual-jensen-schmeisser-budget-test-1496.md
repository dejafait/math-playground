# Actual reciprocal Jensen coefficient-height budget nomination1496

TARGET: Test whether Schmeisser's coefficient bound I(P_d) in the mean- and variance-matched Hermite basis of P_d=R_d/gamma_0 can be o(d), first checking the third coefficient below the leading term and stopping if it forces a non-sublinear bound.
CHECKED: 2026-11-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the exact coefficient-height source search and full Schmeisser proof coverage in source-notes1493; review1496 checked actual Appell normalization and compared L763/L764, L827 and the primitive stop379. The actual-series specialization differs from the generic sector-operator hinge target; no novelty inference.
SOURCE_EVIDENCE: Schmeisser, Mathematica Balkanica16(2002)203-217, https://www.math.bas.bg/infres/MathBalk/MB-16/MB-16-203-217.pdf , definitions pp203-204, Theorem1/(2.1)-(2.2) pp205-206 and complete relevant proof pp211-214 already inspected in1493; theorem and definitions retrieved again in1496. O'Sullivan2007.13582v2 (1.2)-(1.3)/(3.1) supplies exact actual normalization; L021/L027 provide actual coefficient positivity and the strict second-coefficient inequality. No general theorem is to be reproved.
COMPARISON: Schmeisser supplies an upper height bound from orthogonal-expansion coefficients without real-rooted input. It does not estimate the actual expansion norm. The new work is a necessary-budget test on the unchanged actual reciprocal family, not the stopped fixed-Gaussian product Turan budget or a reverse derivative inequality.
GAP: Establish the matching Hermite basis and its positive variance, compute the first unmatched coefficient with all factorials and norm ratios, and determine whether its contribution alone rules out I(P_d)=o(d). No actual coefficient mismatch, height asymptotic, vanishing or RH consequence is assumed.
REASON: This is a bounded known-method specialization using ready source coverage. A retained nonnegative term may stop the majorant before any large calculation; otherwise preserve the exact remaining norm question. This newly written continuation awaits separate approval next turn.
SCOPE: d>=3 tends through integers; R_d=x^d sum_(j=0)^d binom(d,j)gamma_j x^(-j), gamma_j=j!M_(2j)/(2j)!, P_d=R_d/gamma_0. Translate/scale a monic Hermite orthogonal basis to match its first two coefficients below the leading term; verify existence using L027 before applying the source. No fitted root model, LP premise, input real-rootedness, coefficient multiplier or degree sweep.

Main gap: actual-Xi all-degree positivity and the unbounded exceptional-root
deficit. A direct sublinear upper bound for reciprocal root heights would
be a prospective replacement for unpaid inverse propagation. Transfer to
the normalized ordinary Jensen plane, the reciprocal denominator, and
all-degree signs remain separate obligations; this nomination asserts no
automatic RH implication.

For the source statistic, if p=sum a_nu H_nu has degree d in a monic
orthogonal system of positive measure with all moments, write
h_nu=||H_nu||^2 and kappa=Im(a_(d-1)/a_d). Schmeisser's definition is

    I(p)^2=kappa^2+sum_(nu=0)^(d-2)
                   (h_nu/h_(d-1)) |a_nu/a_d|^2.

The paper calls the norm squares gamma_nu; h avoids confusing them with
the actual xi coefficients. This is the cited statistic, not a newly
derived identity for P_d. Theorem1 assumes a nondecreasing convex function
on [0,infinity) vanishing at zero, and c=-t*kappa, 0<=t<=1/2. Its height
upper bound remains conditional on the computed I; no root signs follow
merely from orthogonality of the reference basis. Source-notes1493 contain
the complete theorem interface and essential matrix proof cases.

Use L018/L021/L027 as essential actual inputs; L028 and O'Sullivan fix
conventions. L763/L764 and L827 are contrasts, not premises. Prefer an
analytic nonvanishing argument for the retained mismatch; if certified
coefficient data are essential, retain the exact inherited error/software
contracts and inspect their full relevant evidence. No model coefficients
may replace the actual moments. A vanishing third mismatch is inconclusive
for this test, not permission for an unbounded higher-order sweep.

Continue only if this first retained contribution is o(d) at the level of
I and the full majorant still has a concrete justified route; record the
remaining terms explicitly. Stop this majorant if that term has positive
liminf after division by d, or diverges. If neither is proved in one
attempt, save the exact unresolved coefficient inequality. A large bound
is a failure of the bound, never a nonreal actual root certificate.

This is calculation/standard/high, a reproduction/specialization of a
known bound. It is not a creative mechanism. No justified creative theta
payment estimate is ready; source coverage alone cannot invent one.
Mathlib coverage is unchecked. No mathematical calculation was performed
when preparing this assessment.
