# Height-localized Weil-form rank-trace: completed source comparison

TARGET: Assess Alpöge–Furman's finite Weil-form rank-trace inequality for detecting a single off-line zero pair in a height-localized compression without assuming Weil positivity.
CHECKED: 2026-10-30
DECISION: EXPLORE
SEARCH_EVIDENCE: Searched the paper ID with rank/trace and error/Poisson terms, and Alpöge/Furman with single/zero; inspected the primary v2 HTML rather than search summaries. Narrow local rank-trace/ID searches found only the prior nomination and geometry/count screen; the exact source cases and comparison are recorded below.
SOURCE_EVIDENCE: Read Alpöge–Furman arXiv:2608.13637v2, Theorem A, sections 1.2/1.4, 2.1–2.3, Lemmas 3.1–3.4 and their proofs, Propositions 4.1–4.3 and Corollary 4.5 with proofs, Proposition 5.4 and its prime off-diagonal cases, Theorem 5.7, section 6 and section 7.2(a)–(f). These are inspected source statements, not an independent manuscript or Lean audit.
COMPARISON: Lemma 3.2 is a finite rank lower bound with no RH premise; Proposition 4.1 bounds positive inertia from above under pull-back, not negative inertia from below. The stated trace, second-moment and boundary errors and the resulting proportion conclusion supply no single-pair negative margin or comparison with localization error.
GAP: A displacement-sensitive negative direction surviving other zeros and compression, plus an independently proved arithmetic bound excluding it, remain missing. Neither the positive off-line index bound nor an asymptotic proportion supplies these inputs or actual-Xi signs.
REASON: Complete the source test negatively and park this two-moment rank-trace implementation for single-pair exclusion. EXPLORE records no adequate match, not approval to construct a localized detector. Reopening requires a new quantitative spectral/localization input; no lemma or script is warranted.
LITERATURE_REASON: At invocation the arithmetic-form theorem and inertia/localization cases were essential unread coverage; this turn completed that source comparison, without repeating the covered strip/count work.

## Completed comparison, 30 October 2026

The original nomination below is retained as the pre-review record.
The completed review changes the route, not the mathematical argument.
No source conclusion is installed as a canonical input or reproved.

### Exact finite statement and off-line case

Primary source: [Alpöge–Furman, v2](https://arxiv.org/html/2608.13637v2),
version record 19 August 2026; displayed manuscript date 24 August 2026.
Lemma 3.2 assumes Hermitian d-by-d P,Q, P positive semidefinite,
rank P<=r and n_+(Q)<=b. It states

    r >= 2 tr P + 4 tr Q - 4b - ||P+Q||_HS^2.             (3.1)

Its proof uses the positive/negative spectral decomposition and von
Neumann's trace inequality. No positivity of P+Q is assumed.
Proposition 4.1 writes an off-line pair, of equal multiplicity m,
with sampling vector v=u+iw as 2m(uu^T-ww^T). Lemma 3.1 bounds the
positive index of its pull-back by one, including degenerate sampling;
it does not assert retention of a negative eigenvalue.

### Localization and arithmetic scope actually inspected

Sections 2–5 fix large T, L=log(T/(2pi)), X=exp L, grid
alpha_k=T+2pi k/L, 0<=k<floor(LT/(2pi)), and a fixed smooth taper
of sqrt(psi(u/L)) supported in [-L/2,L/2], where psi is even,
C^2 on [-1/2,1/2] and strictly positive there. With
a=||phi||_2^2/L and z_rho=(rho-1/2)/i, (2.10) uses
sum m_rho v_rho v_rho^T/(aL^2), v_rho,k=hat(phi)(z_rho-alpha_k),
over I'=[T-sqrt(T),2T+sqrt(T)); the Fourier convention is
hat(phi)(z)=integral phi(u)exp(-iuz)du. It includes all zeros and
multiplicities in I', not a selected isolated pair.

Propositions 4.2/4.3, Corollary 4.5 and Theorem 5.7 state respectively

    tr G = N(I') + O(sqrt(T)L^2),
    ||E||_1 = O(T^(-1/2)),
    boundary-count error = O(sqrt(T)log T),
    ||G||_HS^2 = (R(psi)+O(1/L)) N(T,2T).

The implied constants depend on the fixed taper/window. Proposition
5.4's prime off-diagonal estimate is O(L^2 X); section 7.2(a) identifies
X<=T as its usable range. Theorem A yields asymptotic proportions
2/3 (simple and on-line), 5/6 (distinct), improved by its stated window;
section 1.4 explicitly excludes sensitivity to o(N) off-line exceptions.

These reported estimates are not claimed independently audited. In
particular, the small tail norm is only one error: it does not certify
that a negative direction persists after adding all retained zeros.
The trace and second-moment estimates give no displacement-dependent
one-pair lower bound with which to compare any error. A proportion
bound tolerates exceptional pairs. This fails the nomination's test
even granting the source's analytic claims; no repaired localization
or new impossibility theorem has been derived here. The numerical
bandwidth ceiling and its formal certificates are not needed or imported.

### Relation to local work and continuation

L471 equation (6), read with its convergence and zero-safe
qualifications, already isolates signed pair kernels. The present
source supplies no missing pointwise collective lower bound for that
identity. L511 is a finite allocation contrast, not an actual-Weil
matrix model; neither direction of transfer is asserted. Thus the
new evidence is a source-scope obstruction, not a new theorem beyond
the checked literature. First signs, higher signs and RH remain open.

Full matching Mathlib coverage was not checked. The paper's companion
Lean claim does not certify a local single-pair theorem, and no
uninspected formal artifact is imported. arXiv:2610.08965 remains
an abstract-only lead outside this bounded comparison.

A different, independently testable lead is support enlargement of
the actual Weil quadratic form, using coercivity and controlled prime
terms rather than its first two trace moments. Section 7.1 cites
Yoshida (1992) for small-support positivity. A narrowly targeted search
also located arXiv:2608.24827 on compact-window positivity; its theorem
and certificate were not inspected. Narrow Yoshida/compact-window/
support-enlargement/2608.24827 searches in local literature and
ATTEMPTS found no ready assessment. The separate REVIEW_REQUIRED
nomination records exact source coverage still needed. No support
continuation inequality, global positivity premise or creative proof
target is approved here.

## Initial nomination (historical; coverage superseded above)

Main gap: actual-Xi all-degree mixed positivity. The proposed
intermediate target is a finite, height-localized arithmetic-form test
that is sensitive to one off-line conjugate pair, with an explicit
comparison between its negative direction and all localization errors.
This is a source-review question, not a claimed inequality. Such a test
could offer a different route to zero exclusion; transfer to Laguerre
signs, higher signs and all-height coverage would remain unproved.

Initial exact local inputs are L511 as the finite allocation contrast
and L471 equation (6) as the existing actual-Xi signed identity and its
convergence/zero-safe qualifications. The completed comparison is
`2026-10-30-actual-xi-collective-kernel-coverage.md` in this directory.
Do not read unrelated proofs for orientation. Identify any additional
exact local result before its narrow read. No cross-notebook input is
nominated. Full matching Mathlib coverage is unchecked; abstract claims
of Lean verification are not a substitute for checking source hypotheses.

Primary lead: Levent Alpöge and Ralph Furman,
[*More than two thirds of the zeta zeros are simple and on the critical
line*, arXiv:2608.13637v2](https://arxiv.org/html/2608.13637v2).
Start with its exact theorem and finite rank-trace statement, then the
off-line inertia case and the cited arithmetic estimate actually needed.
Record whether any positivity premise is itself RH-equivalent. Do not
assume a positive zero-side sum, RH, simplicity, an all-height proportion
upgrade or an effective uniform limit absent a theorem.

Bound the review to that mechanism. Continue only if the inspected
statement yields an independently testable finite inequality with its
signs, test-function support, height localization, multiplicities and
error threshold specified. Otherwise record the exact scope obstruction
or access failure and park this lead. Do not rederive rank-trace, invent
a local theorem from an asymptotic, or approve a creative proof attempt
in the same turn that discovers uncovered mathematics. No lemma or
mathematical script is authorized by this nomination.
