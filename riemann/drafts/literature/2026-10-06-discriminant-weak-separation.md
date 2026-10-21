# Direct weak separation — bounded assessment

TARGET: Determine whether Δ≤0 and G′²−GG″>0 on an eventual ray force a bounded deficit of distinct real zeros of F_0 relative to G, including common and multiple F_0 zeros.
CHECKED: 2026-10-06
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse the completed Sturm/Obreschkoff/differential-pencil search in 2026-10-06-discriminant-zero-interlacing.md; no matching weak analytic-pair theorem was found in the inspected statements.
SOURCE_EVIDENCE: MIT 18.034 Spring 2009 Lecture 9 Theorem 9.1, printed pp. 1–2 and full proof https://ocw.mit.edu/courses/18-034-honors-differential-equations-spring-2009/0cdeb657491010f0f8c60aa49f2d5248_MIT18_034s09_lec09.pdf; Borcea–Brändén–Shapiro Master4 §3.1 printed p. 9 Theorems 9–10 https://staff.math.su.se/shapiro/Articles/Master4.pdf; DLMF 1.13.1–1.13.6 https://dlmf.nist.gov/1.13#i; L018, L366 (1), L367 (1)–(3), L368 (1)–(8) and L370 (1)–(6)/common-zero case inspected before proposing this target.
COMPARISON: Sources cover common-ODE or hyperbolic-polynomial separation, but not weak physical discriminant control for this real analytic pair; a direct real-variable proof or counterexample is needed, without importing their stronger premises.
GAP: Establish or refute a zero-count deficit bounded independently of the interval endpoint under the exact weak inequality, including all degeneracies; actual arithmetic contradiction and G counting asymptotic are excluded from this target.
REASON: Independently test the missing geometric implication before spending further literature work on blocked signed-count sources; this is bounded exploration, not approval of an implication or novelty claim.
SCOPE: Real analytic pair F=F_0,G on t≥H with L368 positivity and conditional Δ≤0 there; physical ordinary derivatives, distinct-zero counting, no common ODE, no all-real complex-zero premise and no simplicity assumption on F_0.

This is a narrower continuation of the reviewed obstruction, not a
solution of it. The source details, queries, limitations and duplicate
comparison are in [the original assessment](2026-10-06-discriminant-zero-interlacing.md).
The only new item here is the target and its scope; no mathematical
result has been derived. The separate literature recovery on 2026-10-06 rechecked the primary
hypotheses and repaired direct source URLs; the EXPLORE scope is unchanged.
This assessment permits a subsequent bounded research attempt, not a
mathematical conclusion.

Main gap: actual-theta global mixed positivity and the total L367 margin.
The intermediate threshold sought is a constant C, independent of X,
such that for all large X the count of distinct F_0 zeros in [H,X]
is at least the count of G zeros there minus C, assuming the displayed
weak discriminant condition. Endpoint conventions must be fixed, and
H may be increased finitely. This is a proposed threshold, not a theorem.
A concrete real analytic counterexample satisfying all abstract
hypotheses would refute that generic implication; it would not refute RH
or establish a counterexample for the actual functions.

Use L370's physical polynomial identity at zeros. A quotient argument,
if attempted, must justify every extension through zeros and cannot
assume W never vanishes. Common zeros and local proportionality must be
handled explicitly; finite endpoint errors must not accumulate into an
unbounded count loss. G′²−GG″>0 is supplied only after L368's unevaluated
onset. F_0 and G have the analytic representations in L018/L366/L368;
any needed real-analytic continuation qualification must be justified.
Retain the full q correction if using normalized functions, or use the
physical pair throughout. No regulator curve differentiation is allowed.

The plausible downstream use is a necessary zero-count condition for
the eventual discriminant route. It would make a later arithmetic count
comparison well posed. Such a comparison still needs a locally justified
G phase count and primary unconditional signed S(t) information; neither
is approved or assumed here. The sharp-mean source blocker and L365 stop
remain independent, as do higher signs, heights above forty and the
endpoint arithmetic margin.

Continue only after either a proof covering the weak/common-zero cases
or an exact counterexample with verified hypotheses. Abandon the generic
count implication if those hypotheses admit unbounded deficit; do not
replace it with strict separation or a no-common-zero conditional result.
If a proof succeeds, its actual-family applicability and the separate
arithmetic source target require explicit follow-up review. Full matching
Mathlib coverage is not checked. Classification for an eventual attempt
may be REPRODUCTION or POTENTIALLY_NEW; failed searches do not certify
originality. No lemma or mathematical script is created in this turn.

## Direct-source recovery, 2026-10-06

LITERATURE_REASON: Supervisor recovery requires direct source URLs in the ready assessment; repair traceability and confirm the previously inspected hypotheses without broadening the target.

Reopened the three primary URLs listed in SOURCE_EVIDENCE. MIT Lecture 9,
Theorem 9.1 and its complete proof on printed pp. 1–2 require independent
solutions of one second-order homogeneous equation with continuous
coefficients; the proof uses a nowhere-vanishing Wronskian. The author
Master4 PDF, §3.1 printed p. 9, Theorems 9–10 and the preceding definition
of proper position, concern real polynomials and stability/hyperbolicity;
the strict versions exclude common zeros. DLMF §1.13(i), equations
1.13.1–1.13.6, treats solutions of the same equation on a domain with
analytic coefficients; Abel's identity is not an arbitrary-pair identity.
The author manuscript revision date and current DLMF release number remain
unverified. These references identify adjacent results, not an import for
the weak discriminant condition. The earlier search and local-input review
are reused; no new theorem, novelty conclusion or source blocker for this
independent test is reported. The unconditional arithmetic source blocker
belongs to the parked downstream contradiction.

The comparison and stopping test above remain unchanged. No lemma,
mathematical script, DAG edge or argument overview was modified. Full
matching Mathlib coverage remains not checked.
