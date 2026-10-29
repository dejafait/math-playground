# Numerical shell specialization — ready source scope

TARGET: Specialize Bellotti–Wong v2 Theorem 1.1 to a numerical A with N(u+1)-N(u)<=A log(u+2) for every real u>=1, and justify an explicit closed-shell bound for all v>=0 as required by L464.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the primary-source comparison and scoped duplicate review in drafts/literature/2026-10-25-explicit-unit-shell-count-coverage.md; no new source discovery is required for this coarse numerical specialization.
SOURCE_EVIDENCE: Bellotti–Wong, arXiv:2412.15470v2 (7 July 2025), https://arxiv.org/pdf/2412.15470v2, Theorem 1.1, p. 1 (reopened 2026-10-25), and Section 5, pp. 23–24, as inspected and qualified in the companion assessment.
COMPARISON: The unconditional explicit global error covers the analytic count; elementary inequalities, compact-height monotonicity and endpoint handling remain to obtain the stated shell bounds.
GAP: Numerical constants and full all-height inequalities have not yet been proved locally; this assessment approves that bounded specialization only.
REASON: Replaces one qualitative input of L464 without claiming effective saddle constants or overlap with finite-height signs.
SCOPE: Actual-zeta positive-ordinate counts with multiplicity, natural logarithms, half-open and closed unit shells, including compact heights; no simplicity, RH or fixed-half-plane premise.
LITERATURE_REASON: Supervisor recovery requires a direct source URL in this ready assessment; repair that field and verify its theorem/version without repeating discovery or deriving the specialization.

The exact global inequality, version corrections, primary links, proof
cases and source-computation qualifications are recorded in the companion
assessment. Import that theorem by citation; do not reprove its analytic
or computational ingredients. Essential local context is L018 and L464
Section 3, especially equation (6). No cross-notebook input is used.

Continue if one conservative numerical constant for each stated shell
convention is proved for every height, with complete endpoint and
multiplicity checks. An optimized constant is unnecessary. Stop the
certificate if it requires an unproved numerical zero table, an
uncontrolled endpoint limit, or a height-dependent constant.

Downstream use is L464's near-factor degree and far reciprocal-square
shell estimates. Its full effective threshold and the L465/C465a saddle,
amplitude and common-onset constants remain unresolved. The full
numerical-onset route stays parked. Mathlib coverage is unchecked.
## Source URL recovery — 2026-10-25

The direct versioned primary URL is now in SOURCE_EVIDENCE. Reopening
that PDF confirmed the v2 date, the definition using 0<gamma<=T and
Theorem 1.1's first bound for every T>=e:

    |N(T)-(T/(2pi)) log(T/(2pi e))|
       <=0.10076 log T+0.24460 log log T+8.08344.

The companion review's Section 5 coverage, computational qualifications,
duplicate comparison and recorded effective-onset stop are reused.
L464 Section 3, equation (6), was checked for the closed-shell convention
and multiplicity requirements. No new theorem comparison or mathematical
result is claimed. This is a metadata repair, not another source advance;
the same SPECIALIZE target and its continuation/abandonment test remain.
No numerical specialization was performed. The next research attempt
must cite the source and justify only the stated elementary difference.
