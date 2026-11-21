# First-zero log-concavity preservation: completed review2257

TARGET: Prove or refute logarithmic-concavity preservation under removal of the first positive real Fourier-zero factor for even positive smooth kernels with strictly negative logarithmic second derivative and faster-than-exponential decay of every derivative.
CHECKED: 2026-11-21
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed2257 exact first-zero/division/log-concavity and stronger-obstruction searches; compared C919m/p/q, L049/L050 and stops667/1117. Actual queries and inspected ranges are in drafts/literature/2026-11-21-first-zero-preservation-source-notes-2257.md; no matching preservation theorem or counterexample identified, no novelty inference.
SOURCE_EVIDENCE: Tuck2006 pp133-135 equations(1)-(4), https://doi.org/10.1017/S0004972700047511 ; Csordas1309.0055v2 p9 Remark3.11/Example3.12, https://arxiv.org/pdf/1309.0055v2 ; DLMF1.13.8-10 analytic-forcing scope, https://dlmf.nist.gov/1.13.iii ; Tao2009 Section3 Exercise30/inversion(11), https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/ ; reused2254's inspected Csordas1998/2014 and Prekopa1973 statements and2249's finite-integration tools. Full hypotheses, proof-case read limits and direct URLs are recorded in notes2257/2254.
COMPARISON: Tuck supplies a positivity tool, not curvature preservation or a first-zero theorem. Csordas Example3.12 has no positive real transform zero, and C919p/q do not assert strict log-concavity. Nonnegative correlation/convolution results concern different operations. The generic invariant remains unresolved; a fixed analytic kernel test is within the covered ordinary tools.
GAP: For the single nominated K_*(u)=exp(-u^4-u^2), all admissibility checks, first-zero existence/exclusion and enclosure in(0,8), generic-origin/quotient specialization and the curvature determinant at u=1 remain unpaid. No zero enclosure or sign was computed; no theorem about all quartic-transform zeros is imported.
REASON: Completed essential new source comparison for the changed invariant. A strict positive output curvature in one certified admissible member would reject the generic bridge; a nonpositive value at one point cannot prove preservation. The earlier actual-kernel enclosure route remains closed in its recorded scope.
SCOPE: Ready EXPLORE nomination for only K_*(u)=exp(-u^4-u^2), first-zero certification within(0,8), and Delta_*(x)=G_x(1)G_x''(1)-G_x'(1)^2, with all origin/quotient and tail checks. No parameter retuning, generic preservation proof, other spatial points, Xi zero census or all-degree conclusion is approved. Updated coverage needs separate approval next turn before mathematics.

## Exact statement to compare, not an established assertion

Let K:R->(0,infinity) be even and C-infinity, with
(log K)''(u)<0 for every real u. For every integer m>=0 and B>0
assume exp(B|u|)|K^(m)(u)| tends to0 at both infinities. These
quantifiers also give the required weighted derivative integrability
by using a larger B; no merely polynomial Schwartz decay is intended.
Suppose F_K(z)=integral_0^infinity K(u)cos(zu)du has a positive real
zero and let x be its least positive real zero, with multiplicity
unrestricted. Ask whether the even inverse after removing that factor,
whose half-line candidate is

    G_x(u)=x integral_0^infinity K(u+t)sin(xt)dt, u>=0,

satisfies (log G_x)''<=0 on the real line. An answer must justify
positivity, the even-origin interface and the transform identity
under these general hypotheses, rather than citing C919m as already
proving a generic extension. Its actual-K proof is a comparison input,
not automatic authorization to generalize it. The strict input
condition and nonstrict output condition are intentional; a zero
curvature value alone does not refute the proposed preservation.

## Bounded future test and downstream limitations

Review2257 completed the primary comparison and selected the single
fixed test K_*(u)=exp(-u^4-u^2), x its first positive real Fourier
zero to be certified within(0,8), at u=1. The full source evidence,
unresolved hypotheses, finite cap, exact sign threshold and stopping
conditions are in [source notes2257](2026-11-21-first-zero-preservation-source-notes-2257.md).
Selection is not proof of admissibility, root existence or a sign.
The original uncovered nomination2256 performed none of these checks;
completion2257 remains literature-only.

A bounded later test seeks one certified point with (log G_x)''>0
in that fixed admissible member. A nonpositive upper bound is evidence
only for this point; an enclosure meeting zero is inconclusive. Failed
admissibility or root certification is not a counterexample. Do not
automatically change parameters, spatial point or the root-search cap.
No protected creative attempt is authorized: the missing comparison
principle between the first-zero condition and curvature is still a
blocker. The fixed source-supported calculation is a separate future
attempt after approval. A counterexample would stop only this generic
invariant; it would not refute actual-Xi curvature or RH. A future
preservation theorem would still need actual-K hypothesis verification,
iteration and an all-degree mixed-positivity interface. No first-zero
census for Xi, bound on its first zero or RH-equivalent positivity is
assumed. Full matching Mathlib coverage is unchecked.
