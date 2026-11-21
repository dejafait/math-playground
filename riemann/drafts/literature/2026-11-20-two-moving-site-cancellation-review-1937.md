# Two moving negative sites: bounded realization attempt assessed1938

TARGET: Establish a uniform C^1 limit for the three centered root-power sums at two negative sites of size sqrt(T_d), sufficient to realize C028y's strict moment solution with exact three-residual cancellation.
CHECKED: 2026-11-20
DECISION: EXPLORE
SEARCH_EVIDENCE: Source-notes1938 records a new bounded search for joint varying-site/degree Uvarov limits and derivatives, reusing1931/1934 and the exact1933/1937 stops; no adequately inspected matching theorem was located.
SOURCE_EVIDENCE: Delgado et al., SIGMA12(2016),090,Theorem3.1,(3.1)-(3.14),pp8-10, https://www.emis.de/journals/SIGMA/2016/090/sigma16-090.pdf ; Castillo--Rafaeli2015,Theorem2.2/Section3.1,pp272-277, https://etna.ricam.oeaw.ac.at/vol.44.2015/pp271-280.dir/pp271-280.pdf ; Rudin1976,Theorem9.24/full proof,pp221-223, https://djvu.online/file/cNW6EtZ7m9PIB ; direct access and statements rechecked in recovery1939; reuse audited C028x and source-notes1938 for scope and earlier proof reads.
COMPARISON: Fixed-degree exterior-support zero escape and increasing-mass attraction do not cover two unit masses on the full-support theta law as degree grows; finite Uvarov identities and the inverse-function theorem supply interfaces, not the required uniform estimates or a common finite-degree image neighborhood.
GAP: Establish the exact proposed local C^1 map, including bulk second moment and joint two-site inverse conditioning, then verify nondegeneracy and stable inversion against C028w's exact finite targets. No such estimate is imported or derived in this source review.
REASON: Separate literature review1938 completes the essential comparison for one bounded finite-system attempt, preserving the exact1937 target; no novelty or general mass-point asymptotic theorem is asserted, and the1993 blocker stays parked.
SCOPE: One bounded research attempt using C028w's finite shared system, C028y's compression, C028x's audited bounds and the named local inverse theorem. The full theta law and two fixed unit masses remain; no exterior-full-support, leading recurrence constant, automatic zero sticking or derivative-limit interchange is assumed.

## Exact proposed statement for comparison, not an established result

Use C028x's base T_d=sum_(j=1)^(d-1)beta_j. Let x_1>x_2>0 be
the strict solution constructed in C028y under C028c's coefficient
contracts, and set c_0=sqrt((v-x_1^2-x_2^2)/2)>0.

For variable (c,y_1,y_2) near (c_0,x_1,x_2), with c>0 and
y_1>y_2>0, prescribe

    a_d=-y_1*sqrt(T_d)/c, b_d=-y_2*sqrt(T_d)/c,
    s_d=d*c/sqrt(T_d).

Let lambda_i be all degree-d zeros for mu_0+delta_(a_d)+delta_(b_d),
and m_d their mean. Define the proposed observable

    F_d(c,y_1,y_2)=(
      (s_d/d)^2*sum_i(lambda_i-m_d)^2,
      -(s_d/d)^3*sum_i(lambda_i-m_d)^3,
      (s_d/d)^4*sum_i(lambda_i-m_d)^4).

The specific target to assess is uniform C^1 convergence on some closed
neighborhood contained in c>0,y_1>y_2>0 to

    F_infinity(c,y_1,y_2)=(2*c^2+y_1^2+y_2^2,
                          y_1^3+y_2^3,y_1^4+y_2^4).

This formula is a proposed mechanism, not a derived moving-site theorem.
It must retain the full theta law and the two fixed unit masses jointly.
No assumption that modified zeros stick to their sites, that the other
zeros have unchanged second moment, or that parameter derivatives
commute with a degree limit is allowed. C028y's necessary envelope
does not establish any of those assertions.

The intended downstream use is a verified local finite-degree inverse
argument against the exact centered coefficient targets in C028w
(8)-(9), with the finite nondegeneracy and onset justified. Translation
must be exactly t=-b_1-s_d*m_d; then A=t+s_d*a_d<B=t+s_d*b_d.
Exact equality of the three retained coefficients would make B_d=0
without needing upper bounds on its weights. A limiting match alone
would not suffice. This is only a proposed countersequence to the
retained floor; all omitted full Schmeisser costs remain unpaid.

## Source scope, decision test and remaining obligations

The nomination required comparison of this varying-site, infinite-support, fixed-mass
statement with primary mass-point/Christoffel/Uvarov results and known
obstructions. Reuse the existing finite formulas; do not repeat their
literature assessment or infer a moving-site theorem from a fixed-site
abstract. The persistent1993 access blocker stays parked. If available
theorems do not cover this statement, a bounded finite-system derivation
may be nominated EXPLORE only after the separate source comparison.
Review1938 now permits the bounded finite-system route detailed in
[source-notes1938](2026-11-20-two-moving-site-source-notes-1938.md).
Any need for stronger base input must be explicit; do not assume an
actual leading recurrence constant or a weighted-tail limit.

Continue if the uniform local limit and derivative control are supported
by adequate sources or a separately assessed concrete finite estimate.
Reject or refine this scaling if a verified missing contribution changes
the proposed map or its local solvability. A source-only stall is not
evidence against the mathematics; persistent blocking requires another
independently testable target under the shared recovery rules.

Essential local inputs: C028w/x/y and C028c, with C028a/b's actual
coefficient and height conventions. C028y and C028w's finite reductions
await independent conceptual audit; C028x is audited. C028c's accepted
numerical result retains L778/Decimal contracts. Primary finite formulas
and their positivity applicability are in source-notes1931, while
source-notes1934 covers the base import. No cross-notebook result,
actual-root reality, free atomic masses, existing positive realization,
small full cost or RH premise is supplied. Full matching Mathlib
coverage remains unchecked. The source comparison is now ready for one
bounded attempt, subject to the supervisor's separate approval of this
changed continuation. No mathematical conclusion is established here.
