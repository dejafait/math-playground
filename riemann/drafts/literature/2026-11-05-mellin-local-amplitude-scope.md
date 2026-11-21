# Finite Mellin local amplitude: completed source comparison

TARGET: Assess paper23 v1's local amplitude budget 1.24eta on the finite descent diameter using L019, L797 and L798, and specify the normalized integral test before calculation.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step515 searched exact theta/amplitude/1.24 and continuum-certificate/amplitude/bramble_trace phrases, inspected paper23 and the relevant author post20 cases, and searched notebook-local Mellin assessments/stops; reused step511's primary saddle comparison. No novelty inference from search results.
SOURCE_EVIDENCE: bramble_trace paper23 v1 (18 October 2026), Section2 (1), Section3 Lemma2 (10)–(14); author post20 original local-amplitude paragraph and 12:27:38 UTC revision (d=3/(16u)); DLMF2.4(iv), (2.4.14)–(2.4.16), plus step511's O'Sullivan statement/proof-case assessment; exact links and qualifications below.
COMPARISON: The source gives P and the leading factor and asserts the amplitude allowance; L019 fixes P=K/2, while L797/L798 supply geometry and phase only. An operational finite-integral audit is now specified. Fixed-data asymptotics and scalar source checks do not certify its uniform numerical constant.
GAP: Prove or rigorously fail the nominated finite amplitude inequality, including normal convergence, the rotated-path complex theta tail and all boundary cases; none of these amplitude estimates is imported as established.
REASON: Accessible formulas suffice to define an independent local audit without supplementary premises. SPECIALIZE describes known-method partial coverage and a source reproduction requiring verification, not a proof of the allowance or global (11).
LITERATURE_REASON: Changed hypothesis and conclusion: the ready assessment covered only the explicit phase, whereas this proposed target includes the actual theta amplitude and its uniform complex remainder; essential source formulas and proof cases remain unread for that target.
SCOPE: Completed literature-only comparison in step515. DECISION below supersedes nomination status; no amplitude inequality was derived. The newly specified research continuation is nominated separately and needs supervisor approval in a separate turn. Global assembly and supplement searches remain parked.

## Step515 decision

DECISION at nomination was REVIEW_REQUIRED. The current SPECIALIZE
decision records this completed source comparison, rather than treating
the old nomination as prior authorization for mathematical work.

Primary sources inspected on 5 November 2026:

- bramble_trace, *A continuum certificate for the decreasing Levy factor
  associated with Riemann xi*, [paper23 v1](https://rstation.ai/problems/riemann_hypothesis/papers/23),
  18 October 2026, Section2 (1) and Section3 Lemma2 (10)–(14).
  Formula (1) specifies the full kernel; (11) specifies the leading
  normalization; (14) assigns an amplitude allowance. Its detailed
  supplementary derivations remain unread and are not premises here.
- The same author's [post20](https://rstation.ai/r/riemann_hypothesis/posts/20),
  original post at 06:52:47 UTC and comment at 12:27:38 UTC on
  18 October 2026. The original local-amplitude paragraph uses
  d=1/(16u), whereas the later comment explicitly uses d=3/(16u)
  and the eta in paper23 (14). These are distinct scopes. The later
  comment asserts a local theta parameter exceeding Q/(5u), but
  does not print a full complex-series proof of the amplitude allowance.
  The 12:43:22 UTC reader comment checks clearance and scalar totals;
  those checks are not a uniform theta-tail theorem. No supplementary
  access search was repeated.
- [DLMF2.4(iv)](https://dlmf.nist.gov/2.4#iv), version1.2.8,
  (2.4.14)–(2.4.16): analytic amplitude enters a fixed-phase interior
  saddle expansion. Reused step511's inspected O'Sullivan
  Assumptions1.1/Theorem1.2, localization proof and Corollary5.1/proof
  comparison, recorded in
  `2026-11-05-actual-mellin-remainder-source-scope.md`.
  Neither reference supplies this parameter-uniform numerical budget.

The queries were `"Riemann" "theta" "amplitude" "1.24"` and
`"continuum certificate" "amplitude" "bramble_trace"`. The inspected
author discussion is a relevant primary lead, not independent validation.
Unrelated search hits were not used. The local searches covered
Mellin-named assessments and attempt records for amplitude and 1.24;
L798 treats only phase, and the global-import stop concerns a different
automatic-import mechanism. No duplicate verified amplitude bound was
identified in that scope. This is not a claim of novelty or exhaustive
search of the notebook.

## Operational normalization and research obligations

Use exactly L798's D, x, u, Q, d, S_s, A, a, J and branches. Define

    P(z) = K(z)/2 using the series in L019 (complex extension to verify),
    H(z) = 4pi^2 exp((9/2)z-pi exp(2z)),
    rho(z) = P(z)/H(z)-1,
    eta(u) = (1/2)exp(-2u+3/(8u))+20exp(-3Q/(5u)),
    T_amp(s) = a integral[-d,d]
                 exp(S_s(x+av)-S_s(x)) rho(x+av) dv.

The nominated test is, for every s in D,

    |T_amp(s)| / |sqrt(2pi/A)| <= (31/25)eta(u).

These are test definitions, not a derived result. H is the nonzero
leading factor specified in the source's normalization. L019's real
series matches P=K/2 term by term; its real positivity conclusion is
not a theorem about complex amplitudes. No extra moment factorial,
Fourier factor or change-of-variable Jacobian belongs in this test.
The factor a is the diameter Jacobian. A future proof must explicitly
check the local integrand factorization against that normalization.

L798 already supplies a nonzero denominator, strip clearance for the
phase disc, |A|<(2801/600)Q, and real-phase decrement at least
(85/48)Qv^2. Cite these audited statements instead of reproving them.
The additional obligations are normal convergence of the complex
theta series on each required compact subset, a uniform bound on rho
along the rotated diameter, and the normalized integral estimate.
One proposed sufficient pair of tests is sup|rho(x+av)|<=eta(u) and
the corresponding phase-weight integral divided by |sqrt(2pi/A)|
<=31/25. Neither test nor their proposed use is verified in this turn.
The source's lower bound on Re(pi exp(2z)) along the rotated path must
be proved if used; L797's saddle strip clearance alone is not quoted
as that stronger numerical assertion. Both signs of Im(s), h=0, the
closed boundary of D, and unbounded u must be included.

Success would pay only the finite local amplitude replacement in the
source normalization. It would not settle the missing Gaussian,
horizontal/far-left tails, endpoint continuation, (11), quotient,
inversion, certificates or sufficient Xi signs. A failure of the
proposed supremum bound alone need not refute the integral test;
record which assertion fails and retain that distinction.

Continue with the exact finite test only after separate approval of
`2026-11-05-mellin-finite-amplitude-audit.md`. Abandon the proposed
majorant mechanism if a rigorous violating case is found, or park it
if an essential non-explicit premise is needed. No such premise is
needed merely to state the local test. Full matching Mathlib coverage
is unchecked; no absence claim or formal verification is asserted.

## Preserved nomination (before step515)

## Purpose and bounded decision

Main gap: actual-Xi all-degree mixed positivity. The intermediate
target is source coverage for the local amplitude component of a
possible uniform actual Mellin estimate. Its plausible downstream use
is a paid local integral error, followed by separately assessed global
assembly, quotient/inversion control and a sufficient sign mechanism.
No such sign mechanism follows from the local estimate alone.

The existing comparison records, without verifying it,

    eta=(1/2)exp(-2u+3/(8u))+20exp(-3Q/(5u)),

and the term 1.24eta in paper23's (14). It records
L(s)=4pi^2 exp(S_s(x)) sqrt(2pi/A(s)), and P=K/2 for the
source's kernel convention. These are source data awaiting the exact
amplitude comparison, not premises establishing its bound. The finite
diameter, branches, D and normalization of L798 must be retained.
Do not silently replace its finite Gaussian or absorb the omitted
Gaussian, global tails or endpoint into an amplitude term.

Read the exact local amplitude statement and required proof cases in
[paper23 v1](https://rstation.ai/problems/riemann_hypothesis/papers/23),
18 October 2026, Section3 Lemma2, before larger passages. Read only the
needed kernel formula and convergence qualifications from L019, and
reuse L797/L798 and the step511 comparison. Search specific local
amplitude records for overlap and failures; do not infer novelty from
an unsuccessful search. No additional literature was searched during
step514's completed phase audit.

Continue only if the exact normalization and accessible primary data
permit an independently stated finite-integral test on all of D with
explicit inputs and a justified relation to 1.24eta. State every
uniform analytic or series bound still requiring proof in that test.
If an essential formula or premise remains inaccessible, identify it
and park this dependent component; do not repeat supplement searches
or nominate an unqualified global estimate. No amplitude inequality
is derived in this nomination, and the source-review turn may not
derive one either.

Essential local inputs for the proposed review are L019, L797 and
L798; none is a sufficient Xi sign theorem. Full Mathlib coverage is
unchecked. The global-import stop in
`ATTEMPTS/2026-11-05-mellin-global-remainder-import-unpaid.md`
remains in force for its stated automatic-import mechanism, without
being a ban on this separate local target. No cross-notebook input.
