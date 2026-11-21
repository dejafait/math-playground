# Source assessment for the fixed-forcing zero-fiber obstruction audit

TARGET: Audit C869a's full-class zero-fiber obstruction, including C1 tangential trace differentiation and the exact -3H/2 residual for every phase.
CHECKED: 2026-11-06
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the ready fixed-h lift assessment and its bounded exact-system/prescribed-trace searches; inspected C869a, L869(7)-(9), the C868a/C868b hypotheses and relevant fiber passage, and the named preceding stop/history. One targeted primary-source search checked the elementary derivative input; details below. No novelty inference.
SOURCE_EVIDENCE: Jiří Lebl, Basic Analysis II, author-maintained HTML section8.3, Definition8.3.8, https://jirilebl.github.io/ra/html/sec_svtheder.html (accessed 2026-11-06), explicitly defines partial derivatives on an open subset of R^n by coordinate difference quotients. Reuse drafts/literature/2026-11-06-green-countermodel-zero-fiber-lift.md for the exact closure/trace scope and its inspected ODE/Fourier/SCV comparisons; none supplies the fixed-h obstruction.
COMPARISON: The submitted proof uses coordinate difference quotients along a full pointwise C1 trace, rather than a mean trace, distributional trace or normal derivative. Elementary derivative definitions cover the proposed operation; the exact cutoff specialization and residual remain for the mathematical audit. The existing general ODE/Fourier/extension results do not replace that check.
GAP: Independently audit C869a(1)-(9), including exact agreement with L869's h, tangent directions, all cutoff terms, H>0 and phase independence. This review approves scope and source adequacy only; it does not accept the obstruction or a changed-forcing construction.
REASON: The unchanged full-class lift assessment covers this narrower local-contradiction audit, and the elementary derivative source has been inspected. No essential source blocker remains. EXPLORE permits the saved audit without asserting a known matching obstruction theorem or originality.
LITERATURE_REASON: Mandatory separate approval of the newly nominated audit; resolve the elementary pointwise trace-differentiation source scope while reusing the ready lift assessment, without repeating its broad searches.
SCOPE: Exactly C869a's prescribed L869 h with arbitrary real ell, phase phi and H>0; real global C1 periodic q,r obeying both closure equations and the entire q=r=0 trace with both second coordinates free. Arbitrary homogeneous and zero modes remain allowed. No domination, extra zeros, growth, bandwidth or graph assumptions are added.

## Completed source review

The main gap remains L030-L032/C032a actual-Xi all-degree mixed
positivity. The one intermediate target is the submitted fixed-h
nonexistence audit. Its downstream use is to decide whether this
forcing is genuinely excluded by full actual-zero compatibility,
beyond the abstract Green package. It will not establish positivity
for the admissible class or the period inequality.

Read the complete submitted C869a proof, L869 through its cutoff and
h definitions and support discussion, C868a's hypotheses, C868b's
hypotheses and relevant zero-fiber context, and the preceding
`ATTEMPTS/2026-11-06-fixed-green-zero-fiber-lift-stop.md` and
`history/2026-11-06-fixed-green-zero-fiber-lift-01.md`.
The prior ready lift assessment explicitly authorizes a local
obstruction valid for every lift and includes precisely the full
pointwise trace. Its recorded searches and theorem comparisons are
reused; no new global solvability theorem is needed for the audit.
The preceding stop is the same submitted result, pending audit,
not independent corroboration. The angular-mean and Green stops
remain at their own scopes; neither is a duplicate proof of C869a.

The sole additional query was
`site.jirka.org ra partial derivative definition chain rule several variables`.
Read the author-hosted HTML of Jiří Lebl, *Basic Analysis II*,
section8.3, **Definition8.3.8** (live HTML accessed 2026-11-06;
no fixed edition number asserted):
[The derivative](https://jirilebl.github.io/ra/html/sec_svtheder.html).
The definition assumes a real-valued function on an open subset of
R^n and an existing coordinate difference quotient. It requires
neither analyticity nor second derivatives. This is a definition,
so there is no additional theorem proof case to import. A local
angular lift gives the relevant real-coordinate domain; the audit
must still verify that its varying coordinates remain on the stated
trace. No source grants zero derivatives in fixed normal directions.
No broader chain-rule, PDE existence or manifold trace theorem is
being imported or reproved. Other search hits were not used.

This source covers the elementary operation, not the numerical
value or sign of the submitted residual. The audit must check all
terms of L869(7)-(9), including the mean's pair products, on the
stated open transition interval and at the selected interior point.
It must verify that the contradiction quantifies over the original
functions, so it includes all homogeneous and zero modes without a
Fourier reconstruction. Those are mathematical checks deferred to
the next turn; no new calculation or proof has been performed here.

Pass only if the full trace and closure equations force the claimed
zero derivative and the exact fixed h contradicts it for every phase
with H>0. Otherwise identify the first failing statement and retain
the unfinished lift question. Stop the unchanged fixed-h realization
route only on a passed audit. Actual-F domination, other zeros and
diagonal conditions, K>=-|M|, graph realization and Xi signs remain
independent unresolved assumptions or goals. Mathlib matching
coverage remains unchecked; this is not an absence claim.

The existing audit is the justified next action. A creative changed-
forcing mechanism is not nominated: it needs a concrete independent
test and separate coverage, and the essential pending audit has not
yet settled the stop it would need to address. No lemma, mathematical
script, PROOF.md or DAG.md is changed by this literature-only step.

## Preserved nomination scope (before approval)

The exact next action is the TARGET line. Reuse the ready lift
assessment where adequate; no repeated broad search is requested.
The essential mathematical input is L869's exact prescribed h;
C869a is the submitted proof. L868 and C868a/C868b explain the
closure/fiber setting but their stronger actual-F assumptions are
not needed for the proposed local contradiction. Inspect the local
equations and trace, the interval 2<s-ell<3, all cutoff terms and
the strict H>0 condition. Check that arbitrary homogeneous and zero
modes cannot alter the derivative identity. No global Fourier
summation, PDE existence or additional zero theorem should be needed.

Pass only if the pointwise equations really require a zero residual
where the fixed h gives -3H/2 for every phase. Otherwise identify
the failing hypothesis or calculation and preserve the unfinished
lift question. L869's abstract countermodel remains at its original
scope in either case. Actual-F domination, all other zeros/diagonal,
K>=-|M|, graph realization and Xi signs remain independent gaps.
Mathlib coverage is not checked. This nomination does not approve
or perform a changed-forcing construction.
