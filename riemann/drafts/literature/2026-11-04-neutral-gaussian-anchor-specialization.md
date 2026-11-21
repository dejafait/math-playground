# Fixed-test Gaussian starting sign: proposed standard specialization

TARGET: Prove the fixed-test positive-time anchor for L753 under a certified real-zero window H>1/2 and a real zero gamma_* with gamma_*^2<H^2-1/4 and F_f(gamma_*)!=0, controlling the complete complex-zero tail and leaving backward propagation separate.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed step-330 comparison in 2026-11-04-neutral-gaussian-positive-time-anchor.md, including exact Gaussian/Weil/eventual-sign and lowest-zero searches, local duplicate/failure checks and the explicitly unread Perisic overlap lead. No novelty claim or additional search is needed for this standard specialization.
SOURCE_EVIDENCE: Platt--Trudgian arXiv:2004.09765v1 Theorem 1 and Section 2 (https://arxiv.org/pdf/2004.09765v1), printed p.2; Platt 2017 Theorem 5.1 and preceding isolation/count report (https://research-information.bris.ac.uk/ws/portalfiles/portal/78836669/platt_zeta_submitted.pdf), printed p.8, with Sections 4.1-4.2; Carneiro--Milinovich arXiv:2403.17803v1 Lemma 4 (https://arxiv.org/pdf/2403.17803v1), printed p.5; L753's audited identity and strip bounds, L018/L024. Exact read scopes and qualifications are in the step-330 comparison.
COMPARISON: Import the explicit formula and computational theorems rather than reprove them. The difference is a fixed-test large-time absolute-tail specialization using the stipulated strict separation and nonzero coefficient. No inspected theorem directly states this exact weighted claim; this is REPRODUCTION with no claim of originality or new general sign principle.
GAP: Verify a strictly positive certified-window contribution against every complementary complex zero with a summable majorant suited to unbounded time. L753's bounded-interval estimate alone does not do this. Fourier nonvanishing remains assumed, not inferred from zero certification.
REASON: A restricted starting sign is an independently testable input to a later propagation question; it may be useful even though the backward comparison and all-test coverage are unresolved.
SCOPE: Fixed complex f in C_c^infinity(R), integral e^(x/2)f(x)dx=integral e^(-x/2)f(x)dx=0; F_f and E_f as in L753. Assume every Xi zero with |Re z|<=H is real, H>1/2, and assume a certified real zero gamma_* with gamma_*^2<H^2-1/4 and F_f(gamma_*)!=0. Seek E_f(tau)>0 for all sufficiently large tau, onset allowed to depend on f,H,gamma_*. Retain all multiplicities and unverified complex zeros. No uniformity over f, numerical onset, density extension, tau=0 sign or backward propagation.

## Later attempt and acceptance test

The essential local inputs are L753 (complete energy identity and Fourier
bounds), L018 (complex coordinates, strip and conjugation symmetry) and
L024 (zero summability and absence of a zero at the origin). The external
finite-window and low-zero inputs have primary coverage in the completed
comparison. If an actual numerical window is instantiated, cite those
theorems and justify the translation, including height zero; no decimal
first-zero approximation is necessary. Keep the test's nonvanishing and
the strict separation explicit. The conditional statement is meaningful
without claiming that every neutral test meets those assumptions.

Work only on the fixed-test anchor. Use the standard dominated convergence
theorem for series, absolute convergence, and elementary exponential
comparison as named inputs, verifying the needed hypotheses. Separate the
real certified window from its *whole* complementary zero multiset. At
complex zeros retain the holomorphic product F_f(z)F_f^#(z), not a modulus
square. Do not assume a positive spectral measure, real unverified zeros,
an ordering-dependent cancellation or a self-adjoint realization.

Continue if the full complementary contribution is eventually smaller
in absolute value than a strictly positive retained real contribution.
The proof must provide the complete summable bound and explain why
L753's identity may be used at each large time without asserting an
unproved global uniform derivative bound. If the proposed comparison
cannot be justified under exactly these assumptions, preserve the failed
step rather than omit zeros or strengthen hypotheses silently. No
mathematical script is needed for this analytic attempt.

This attempt would isolate only the starting-sign gap. Backward Weil-sign
propagation, tests vanishing at all suitable window zeros and unrestricted
neutral positivity remain unresolved. Preserve L751/L752's absorption
stop; the present target is not a reopening of that calculation. A
concrete creative propagation mechanism is still missing. Ordinary
spectral dominance is not creative research and is not presented as new
mathematics beyond the sources checked.

## Gate and coverage qualifications

Written during literature-only step 330, before any mathematical
invocation of this target. The source decision is ready for the
supervisor's separate next-turn approval; this is not a proved anchor
or authorization to derive and approve it in step 330.

The related Perisic v2 PDF remains unread; its accessible description
is recorded as an overlap warning, not an input. Its access is not
essential to the explicitly reproduction-only comparison above, which
uses already inspected theorems and standard absolute-sum arguments.
Do not claim that the exact target is absent from the literature.
Full matching Mathlib coverage is not checked. A successful proof must
state that qualification in its canonical lemma. No cross-notebook
input is proposed.
