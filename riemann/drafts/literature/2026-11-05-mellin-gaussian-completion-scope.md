# Omitted finite Gaussian: completed source comparison

TARGET: Assess paper23 v1's omitted Gaussian budget (2.35u/sqrt(Q))exp(-1.65Qd^2) on D using L797/L798 and specify the normalized completion test.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step518 searched complex Gaussian tail erfc bound Re z positive DLMF 7.7 and exact bramble_trace/2.35/Gaussian; searched only Mellin-named local assessments and the recorded global-import stop. No duplicate completed Gaussian-component proof was found in this scope; no novelty inference.
SOURCE_EVIDENCE: paper23 v1 (18 October 2026), Section3 Lemma2 (10)–(14); NIST DLMF7.7.6 (Re a>0), DLMF7.8.1–7.8.2 (real x>=0), inspected 2026-11-05. Exact formulas, applicability and unread references are recorded below.
COMPARISON: The finite Gaussian uses B=|A|>0, not Re A; L798 already fixes its branch normalization. Exact Gaussian integration and the real Mills-ratio upper bound cover the tail mechanism, but neither source states paper23's parameter-specific 2.35/1.65 budget.
GAP: Verify the normalized finite-to-complete identity and compare the imported real tail bound uniformly with the source allowance using L797/L798; this numerical specialization remains unproved.
REASON: Accessible exact tail formulas and existing uniform curvature bounds permit an independent local test without supplementary sources. SPECIALIZE approves known-method source reproduction only, not a new theorem or the claimed allowance.
LITERATURE_REASON: The changed target is Gaussian completion rather than amplitude replacement; essential exact tail hypotheses had not been inspected before this turn.
SCOPE: Literature-only step518; no inequality for the nominated observable was derived. The separate research continuation is newly written and requires the supervisor's next-turn approval. Global assembly stays parked.

## Inspected statements and source comparison

The main gap is actual-Xi all-degree mixed positivity. Completing a paid
finite local Mellin approximation is a possible downstream use of this
component; it supplies no sufficient sign theorem.

[paper23 v1](https://rstation.ai/problems/riemann_hypothesis/papers/23),
Section3 Lemma2, (10)–(14), inspected 5 November 2026, assigns the third
term of (14) to the omitted Gaussian. The printed leading factor uses
principal sqrt(2pi/A), and the local path is the rotated diameter with
d=3/(16u). The budget is (2.35u/sqrt(Q))exp(-1.65Qd^2).
It is asserted within a conditional analytic enclosure argument;
the text's scalar check at u=3 does not establish uniformity.
Supplementary Derivations42/43/65 remain unread and are not premises.
This reinspection confirms the earlier six-term extraction; it does not
reopen supplement access or the parked full-contour import.

[NIST DLMF7.7.6](https://dlmf.nist.gov/7.7.E6), inspected 5 November 2026,
prints, for real x and Re alpha>0,

    integral_x^infinity exp(-(alpha t^2+2 beta t+gamma)) dt
      = (1/2)sqrt(pi/alpha) exp((beta^2-alpha gamma)/alpha)
        erfc(sqrt(alpha)x+beta/sqrt(alpha)).

The prospective substitution is alpha=B/2, beta=gamma=0, x=d.
L798 supplies real B>0 and real d>0, so these premises are accessible.
The two-sided completion and its normalization must still be written
out next turn using L798 (7); no moving complex contour theorem is
needed for this real-variable tail. DLMF's notes describe verification
of (7.7.6) by differentiation after an exponential factor; its Gaussian
case suffices here. No asymptotic expansion is used.

[NIST DLMF7.8.1–7.8.2](https://dlmf.nist.gov/7.8.E2), inspected the same
day, defines M(t)=exp(t^2) integral_t^infinity exp(-v^2)dv and states

    1/(t+sqrt(t^2+2)) < M(t)
      <= 1/(t+sqrt(t^2+4/pi)),  t>=0.

The prospective real argument is t=d sqrt(B/2)>0. The upper bound
is an exact inequality, stronger than the elementary Mills upper bound;
there is no sector or large-argument exception. Re A alone must not
replace B in the chosen finite G. This is the strongest inspected
bound used for the comparison, not a claim that it is optimal.
DLMF attributes (7.8.2) to Mills (1926), Mitrinovic (1970), p177,
and Gautschi (1959b). The bibliography identifies the latter as
*Some elementary inequalities relating to the gamma and incomplete
gamma function*, J. Math. Phys.38(1),77–81. Those original works were
not inspected; no additional theorem from them is assumed. The exact
reference used for the ready continuation is the inspected NIST formula.

## Exact continuation and limits of approval

Retain L797/L798's entire D, x=u+ih, Q=pi exp(2u), d=3/(16u),
A, B=|A|, a=exp(-i Arg(A)/2), and finite G with principal branches.
The proposed test is exactly

    T_G(s)=|G(s)-sqrt(2pi/A(s))|/|sqrt(2pi/A(s))|
      <= (47u/(20sqrt(Q)))exp(-(33/20)Qd^2),  s in D.

A next mathematical step should verify the completion identity against
DLMF7.7.6, apply DLMF7.8.2 at the specified real argument and attempt
only the scalar comparison needed for this test. Available existing
inputs include L798 (5)–(7), in particular B>(15/4)Q and the exact
principal-square-root normalization. No new bound or scalar comparison
is established here. This is an effective specialization requiring a
written applicability proof; a citation alone does not pay the constants.

Continue if a rigorous uniform comparison covers both signs of Im s,
h=0, both closed boundaries of D and unbounded u. If that majorant
fails, distinguish failure of the sufficient bound from a counterexample
to T_G; preserve the precise failed inequality and retire that test
unless a materially different estimate is justified. No numerical sample
or scalar endpoint preview verifies the domain.

Local overlap/failure evidence reused: L798's hypotheses and normalization
proof, the exact extraction in
`2026-11-05-actual-mellin-remainder-source-scope.md`, the phase/amplitude
assessments, and `ATTEMPTS/2026-11-05-mellin-global-remainder-import-unpaid.md`.
They address other error components or whole-contour hypotheses; none
imports this allowance. L799 provides amplitude context only. Mathlib
full matching coverage is unchecked. Global tails, endpoint continuation,
quotient/inversion, certificates and signs remain unresolved; no
cross-notebook input is used. No justified creative central sign
mechanism follows from these elementary tail sources.

## Preserved nomination (superseded by this comparison)

## Purpose and bounded decision

The main gap remains actual-Xi all-degree mixed positivity. The
intermediate target is precise source coverage for the omitted Gaussian
component of a possible Mellin estimate. Its downstream use would be
completion of the finite local comparison after L798's phase and
L799's amplitude costs; the remaining global and sign gaps are
independent and unresolved.

Retain exactly L797/L798's D, x=u+ih, Q, d, A, B and a, principal
branches, and their definition

    G(s)=a integral_{-d}^{d} exp(-Bv^2/2) dv.

The source extraction records the separate term

    (2.35u/sqrt(Q))exp(-1.65Qd^2).

The proposed observable for source comparison is

    |G(s)-sqrt(2pi/A)| / |sqrt(2pi/A)|.

These are definitions and recorded source data, not a derivation or
claim that the observable satisfies the budget. In the literature
turn, first inspect the source's relevant statement and exact primary
Gaussian-tail hypotheses. Reuse unchanged inspected source evidence;
search the exact missing-Gaussian target for duplicates and failures.
Compare its strongest applicable conclusion to the displayed budget
before deciding IMPORT or SPECIALIZE. A generic saddle expansion or
a scalar check at u=3 is not a uniform effective bound on D.

Continue only if an independently specified normalized test with
accessible premises covers both signs of Im(s), h=0, both closed
boundaries of D and unbounded u. Otherwise identify the essential
missing premise and park this component without supplement searches.
Do not treat a failed sufficient bound as a counterexample to the
observable. Global assembly remains parked under
`ATTEMPTS/2026-11-05-mellin-global-remainder-import-unpaid.md`.

Essential local inputs for the comparison are L797 and L798; L019
and audited L799 explain normalization and the paid amplitude context,
but no result is a sufficient Xi sign theorem. Full matching Mathlib
coverage is unchecked. No cross-notebook input is proposed. No new
central sign mechanism is justified by the finite amplitude result;
source coverage must precede work on this distinct local component.
