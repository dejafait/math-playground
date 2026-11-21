# Finite local theta-amplitude audit: nominated continuation

TARGET: Audit paper23 v1's finite local amplitude cost <=1.24eta throughout D using L019, L797 and L798 and the normalized T_amp test.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step515's completed exact-amplitude source comparison and notebook-scoped duplicate/failure search in 2026-11-05-mellin-local-amplitude-scope.md; queries and inspected primary cases are recorded there. No novelty inference.
SOURCE_EVIDENCE: paper23 v1, 18 October 2026, Section2 (1), Section3 Lemma2 (10)–(14), https://rstation.ai/problems/riemann_hypothesis/papers/23; author's 18 October 2026 12:27:38 UTC revision in https://rstation.ai/r/riemann_hypothesis/posts/20; DLMF2.4(iv) and step511's primary O'Sullivan comparison, as qualified in the completed step515 assessment.
COMPARISON: The source already asserts an amplitude allowance; this test specifies its finite local operational meaning. L019 fixes the real kernel normalization and L797/L798 verify geometry/phase. Neither scalar source checks nor fixed-data saddle expansions pay the remaining uniform complex-series bound.
GAP: Verify complex normal convergence and the full theta amplitude correction along the finite rotated diameter, and prove or rigorously fail its normalized integral cost without assuming a source amplitude inequality.
REASON: Accessible formulas specify a bounded independent source-reproduction audit without supplementary premises. No new theorem or originality claim follows from this comparison.
SCOPE: Newly nominated in step515, requiring separate supervisor approval before research. SPECIALIZE permits REPRODUCTION only for this finite amplitude audit and necessary uniform series/geometry estimates; no global assembly, inversion, certificates or sufficient Xi sign claim is approved.

## Exact test and purpose

Main gap: actual-Xi all-degree mixed positivity. The target pays one
finite local amplitude component of a possible Mellin estimate;
other local/global errors, quotient/inversion and a sufficient sign
theorem remain independent gaps. Ordinary B_J membership is insufficient.

Use exactly L798's D, x, u, Q, d, S_s, A, a and principal branches:

    D={s: |s|>=6000, Re(s)>=-|s|/(8 log|s|)},
    d=3/(16u), Q=pi exp(2u), a=exp(-i Arg(A)/2),
    P(z)=(1/2) times the kernel series displayed in L019,
    H(z)=4pi^2 exp((9/2)z-pi exp(2z)), rho(z)=P(z)/H(z)-1,
    eta(u)=(1/2)exp(-2u+3/(8u))+20exp(-3Q/(5u)),
    T_amp(s)=a integral[-d,d]
                exp(S_s(x+av)-S_s(x))rho(x+av) dv.

The proposed conclusion, still unproved, is

    |T_amp(s)|/|sqrt(2pi/A)| <= (31/25)eta(u),  s in D.

The completed step515 comparison specifies the normalization and
source qualifications. P is the full complex series; verify normal
convergence and the local factorization. Do not extend real positivity
to complex arguments, insert factorials or alter the diameter Jacobian.
Use L798's audited denominator, curvature and phase decrement bounds.
The source's rotated-path theta-parameter lower bound and sup|rho|<=eta
are proposed obligations, not inputs from L797/L798. A phase-weight
integral bound <=31/25 together with that supremum bound is a permitted
sufficient route, not a result proved by this assessment.

Include the full n>=2 sum, both signs of Im(s), h=0, both closed
boundaries of D and unbounded u. Continue if a uniform proof pays the
cost. A violating integral refutes this operational reading, not RH;
failure only of the pointwise majorant need not refute the integral.
Park newly essential inaccessible premises without supplement searches
or an assumption of global (11). Preserve failed estimates.

Full matching Mathlib coverage remains unchecked. Reproof is justified
by the unverified effective source bound and unavailable detailed proof,
not by claiming saddle analysis is new. This nomination neither performs
the audit nor approves itself for immediate research in step515.
