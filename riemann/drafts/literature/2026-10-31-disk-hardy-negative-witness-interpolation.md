# Disk Hardy interpolation for a first negative witness: source comparison

TARGET: Assess sharp disk-Hardy interpolation bounds for a negative D_1 witness at the center of an off-line conjugate pair, using a normalized boundary L2 norm and retaining full multiplicity and other zeros.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched minimum-H2-norm interpolation, confluent/derivative kernels, prescribed zeros, quadratic functionals and logarithmic-derivative/Laguerre signs; checked named local Hardy-moment and Blaschke comparisons. No inspected theorem states the exact nonlinear sign threshold. Queries and search limits: drafts/2026-10-31-disk-hardy-interpolation-source-working.md.
SOURCE_EVIDENCE: Read Groenewald--ter Horst--Woerdeman arXiv:2412.11473v1, Problem 2.14, Lemma 2.15, Theorem 2.16 and its full proof sketch (PDF pp.9--10), Section 4.1 (p.13), and (5.5) (p.27); Le arXiv:1912.05715v1, norm definitions (pp.1--2), Section 3.1 and derivative kernels (p.11), Proposition 3.6 and its polynomial-separation proof (p.12).
COMPARISON: Known projection and confluent-kernel results supply the linear minimum-norm tools. The distinct-point representer theorem alone does not cover derivative observations. Nonlinear D_1 optimization, exact multiplicity, nonvacuity and endpoint attainment remain specialization work; no new theorem or Xi application is approved by this literature step.
GAP: No sign threshold, nonempty sign-forcing interval or actual-Xi normalized norm bound is established. Compare the admissible norm infimum with the infimum permitting D_1>=0, retaining exact order, neighborhood analyticity and attainment questions, in a later mathematical test.
REASON: Essential linear source coverage is now available for one bounded classical extremal specialization. Citation alone does not decide the nonlinear sign. The original nonvacuity test remains pending; newly ready continuation receives separate supervisor approval before execution.
LITERATURE_REASON: The mechanism changed from asymptotic coefficient remainders to exact boundary-norm-constrained jets; essential primary coverage and the full duplicate comparison were missing at invocation and were completed here for the stated later test.
SCOPE: Completed literature comparison covers the listed later classical extremal test for real-symmetric functions analytic near the closed unit disk, f(0)=1, exact order m>=1 at +/-i r, 0<r<1; other zeros allowed. Xi interpretation requires Xi(gamma)!=0 and R>d, r=d/R. No zero-free quotient, simplicity, separation, actual-Xi norm estimate or global witness claim is assumed.
COVERED_TARGET: Solve the sharp normalized disk-Hardy norm-budget test for D_1(f;0)<0 with f(0)=1, exact multiplicity m>=1 at +/-i r, 0<r<1, and other zeros allowed, including minimum-norm feasibility and endpoint attainment.

The main gap remains actual-Xi low-index signs at unbounded heights and
eventually all-degree positivity. The proposed intermediate problem
uses the boundary norm

    ||f||_H2^2 = (1/(2 pi)) integral_0^(2 pi) |f(exp(i theta))|^2 dtheta

and the existing convention D_1(f;0)=f'(0)^2-f(0)f''(0).
These specify the target, not an asserted estimate. Seek source coverage
for an exact threshold, or an exact feasibility test, deciding whether
the allowed norm range forces this defect to be negative, while all
specified zero multiplicities are retained. The source review must
first check the minimum admissible norm: a certificate whose norm
range contains no admissible function is vacuous. No threshold value,
attainment, sign or finite-dimensional reduction is derived here.
Use exact order m at each designated root; if a source instead imposes
only vanishing through order m-1, distinguish that relaxed class and
justify any passage to the exact-multiplicity class rather than assuming
the extremizer has the required order.

If usable, this could locate a conditional first-order negative witness
from a selected off-line pair and quantitative local analytic data,
without identifying a saddle coefficient. It does not supply the
actual-Xi normalized norm, positivity of D_1 or higher signs. Central
real zeros, disks/heights not satisfying a norm criterion, effective
overlap and the other initial indices remain independent gaps. In the
Xi interpretation normalization is only for the explicitly nonzero
center case; an additional zero at gamma must not be silently excluded
from a later global assertion.

Bounded continuation test: inspect primary minimum-Hardy-norm and
confluent-interpolation theorems, then compare their precise hypotheses
with the nonlinear real two-jet sign condition. Continue to a separately
approved mathematical test only if they supply an explicit finite or
otherwise checkable extremal problem with a nonvacuous attainable norm
range and a clear actual-Xi input obligation. Import a matching known
criterion instead of reproving it. If boundary norm data leave the sign
unrestricted at the relevant norm, or only a vacuous threshold is
available, record that exact limitation and park this mechanism. No
generic countermodel would be a counterexample to Xi or RH.

Essential input IDs: L018 and L463 for eventual interpretation; L474
and L570 are contrasts, not norm or sign inputs. Start the overlap check
with the parent review, L474's proof and the named prior Hardy-jet and
Hardy-space comparisons in the working record. No cross-notebook input.
Matching Mathlib coverage is unchecked. The original nomination treated
the extremal sign test as a possible creative mechanism. The comparison
below now identifies its next stage as classical specialization, not a
creative central proof attempt. No source search certifies originality.

## Primary coverage completed in this literature turn

G. J. Groenewald, S. ter Horst and H. J. Woerdeman, *Optimal interpolation
in Hardy and Bergman spaces: a reproducing kernel Banach space approach*,
[arXiv:2412.11473v1, 16 December 2024](https://arxiv.org/pdf/2412.11473v1).
Problem 2.14 uses distinct points. Lemma 2.15 requires independence of
evaluation functionals; Theorem 2.16 gives a unique minimum-norm
interpolant and its dual representer in a uniformly convex, uniformly
Frechet differentiable RKBS. Its proof uses the closed affine constraint
set and annihilator orthogonality. Equation (5.5) states the inverse-kernel
matrix formula in the Hilbert case. Section 4.1 supplies the normalized
boundary norm and Szego kernel when n=1; p=2 is within its hypotheses.
Import these known statements without reproving general interpolation
theory. They address linear values, not the quadratic jet inequality.

Trieu Le, *Inner functions in weighted Hardy spaces*,
[arXiv:1912.05715v1, 12 December 2019](https://arxiv.org/pdf/1912.05715v1),
[DOI 10.1007/s13324-020-00373-4](https://doi.org/10.1007/s13324-020-00373-4).
Use the inspected v1. Section 3.1 gives the Gram-determinant orthogonal
projection onto the complement of finitely many independent vectors.
Section 3.2 defines kernel derivatives representing derivative
evaluations; Proposition 3.6 proves independence across distinct nodes
by polynomial separation. The norm definitions specialize to usual H2
with all weights one. These supply confluent linear tools without a
limit of coalescing nodes. The weighted-space classification in Theorem
3.7 is unnecessary and is not imported as an exact-order or sign theorem.

Page references count PDF pages from one. These primary passages and
the relevant proof arguments were inspected beyond snippets. Later
revisions, complete paper audits and all cited antecedents are unchecked.
The DOI endpoint was inaccessible; the complete relevant primary v1
passages were accessible, so this is not an essential source blocker.

## What the later specialization must establish

Use the standard Hilbert projection theorem and cited kernel results.
Check independence and real symmetry for the actual derivative list;
do not cite a distinct-point statement as a confluent theorem. Exact
order m requires nonzero m-th derivatives in addition to vanishing
orders 0 through m-1. This is an open condition: a relaxed optimizer
may have excess multiplicity. A sharp exact-class infimum or endpoint
claim therefore needs its own justification.

The ambient source space is H2, whereas this target requires extension
across the closed disk. Check proposed extremizers/approximating
families in that smaller class. Keep the normalized boundary norm,
derivative factorials and conjugation conventions. Symmetry averaging
does not automatically preserve a nonlinear sign.

No finite matrix, extremal value or sign range is calculated here.
The sources provide linear interpolation and a finite projection
procedure, not a passed nonvacuity test. First determine the minimum
admissible norm with an exact-order example, then the infimum permitting
D_1>=0 and its attainment. Distinguish strict from non-strict budget
endpoints. Continue only on a certified nonempty sign-forcing interval;
park this norm-only certificate if competing signs reach every attainable
budget. Retain any restrictions on r and m in a partial answer.

Eventual Xi transfer also needs the derivative rescaling and a proved
normalized boundary norm bound, including any height/parameter
uniformity used. Neither L474 nor these sources supplies that bound.
The nonzero-center restriction does not dispose of central real zeros
in a global argument. Higher indices/heights and effective overlap
remain independent gaps. The next extremal calculation is classical
specialization; a creative Xi attempt still lacks concrete actual-Xi
norm information or another new central input.

## Duplicate comparison and search limits

The paired Hardy-jet assessments of 27--28 October and the L472/L473
feasibility stop concern abstract moment laws for Hardy's real Z
function. They do not constrain one disk function by prescribed zeros.
The 10 October sharp-Hardy source stop concerns a blocked weighted zeta
moment theorem. The 29 October Hardy-L1 comparison concerns coefficient
bounds and finite-height transfer. L474 uses bounded-holomorphic
Blaschke factors and a positive aggregate; none decides this nonlinear
center jet. Their stops remain recorded and are not reopened here.

The bounded search located the cited linear results, not an inspected
exact sign criterion. General Hp extremal papers, model-space surveys
and control-theoretic interpolation remain unread leads, not coverage;
they are not essential to this finite Hilbert-space test. No claim of
novelty or absence follows. No cross-notebook theorem is used.
