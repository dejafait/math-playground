# One bounded joint zero-plane attempt

Target: Determine whether L084's equality parametrization admits nonnegative eight/eight moments satisfying all 53 remaining original modes on L076's full domain with t78=s.

Pre-invocation gate: `literature/2026-10-17-zero-plane-remaining-mode-feasibility.md`, SPECIALIZE. Main gap: arbitrary-center 67/68-agreement safety, bracket 955–957. This intermediate target concerns only the fixed included-anchor family. A pass parks this diagnostic and may support a later scalar/other-anchor test; an exact whole-domain contradiction excludes only this family. Independent global consistency and RS realization remain open.

Prior evidence: L078/L080/L082 reject individual columns; L079/L081 stop extending older weights to the whole family; L083 forces t78=s; L084 proves equality compatibility everywhere on that plane. ATTEMPTS/053 and 060–066 preserve the distinct failures. No duplicate joint full-domain verdict was found in the ready assessment.

Local Python has NumPy but no installed conic optimization package in the checked Python 3 installations. The bounded numerical proposal will therefore use a direct product-PSD-cone alternating-direction iteration implemented with NumPy. This is numerical discovery only; no convergence theorem, solver status, rational-existence premise or new mathematical lemma is imported. The original affine blocks remain the mathematical model. One run, capped at **10000 iterations**, followed by **one** exact reconstruction pass. No point scan, parameter box, arbitrary upper cap or repeated solve.

Before iteration: save all exact original affine blocks, domain/sign rows and any checked rational congruence removing fixed zero directions. Keep all three column parameters and 45 original moments. The plane substitution is exact; all 81 modes are retained. Numerical scaling is invertible and does not bound variables. Accept only complete original-row rational verification or an exact whole-domain trace certificate. Otherwise preserve full data/residuals and report EXPLORATION.

Essential inputs: L021,L053,L073,L075,L076,L078,L079,L081,L082,L083,L084 and foundations/04,09,10,12 with their existing qualifications. L084 and ancestor pending critical reviews are not silently discharged. Full step-290/292/294 and equality certificates are read as data, not accepted from previews.

## Saved model and completed attempt

`scripts/finite-support/zero_plane_joint_feasibility.py` saves the full exact
model in `scripts/finite-support/zero-plane-joint-feasibility-results.json`.
For mode i, use the original source base B_i, cross c_i(t), positive
normalization n_i=p8*D8_i and forced-minus-anchor affine function F_i(t).
After the positive anchor Schur congruence already justified in L078,
the affine block is

    [ B_i/n_i          c_i(t)/n_i ]
    [ c_i(t)^T/n_i     F_i(t)-A_i*z ].

Substitute only t78=s. All three other parameters and all 45 original z
coordinates remain variables. In particular no quadratic P(q)+N*h
substitution is made in the numerical model. Keep the 85 original domain
rows and all z>=0 rows. Exact unit lower triangular base congruences
diagonalize B_i/n_i. Their identities, positive pivots, and identically
zero transformed cross rows at every discarded zero pivot are checked
and saved for every mode. This is the permitted removal of fixed zero
directions, preserving the entire plane system. It does not identify a
minimal feasible face or assert strict feasibility.

The 81 source blocks, full anchor, original beta rows, affine ranges,
all 90 weighted kernel equations and 500 full-key comparisons are checked
against the imported complete certificates. The 3000 presentation records
remain bound through their full verification input; ancestor coherent
normalization, PSD and whole-kernel exhaustion are qualified imports,
not fresh critical audits. The exact model checks pass, including all
17 new-only modes. General affine-LMI and trace methods are imported from
Vandenberghe–Boyd (1996), Sections 1.1 (1)–(6), 3.1 (27)–(32), printed
pp.49–51,63–64, DOI 10.1137/1038003, as assessed in foundations/10. L078
retains the precise Schrijver/Sano/Polak inputs and specialization limits.
No general algorithm convergence or certificate-existence theorem is used.

Invertible variable scalings and positive block congruences give a
440-by-48 numerical affine map. All 48 singular values are retained;
the observed extremes are approximately 6.41056 and 1.0. The numerical
iteration uses product-cone PSD projection, with relaxation 1.6, and
stops at the predeclared cap of 10000. Terminal primal residual is
0.993708, dual residual 2.37873, and distance from the affine point to
the product cone is 0.9714834579552192, against required exact distance
zero. These are floating diagnostics, not infeasibility evidence. The
full proposal, trace, dual iterate, affine map and residual vector are
saved. The dual iterate is not an exact separator.

Exactly one reconstruction rounds the three scaled parameters and the
18 nonpivot z coordinates to denominator at most 10^9. It sets the latter
to h and forms z=P(q)+N*h using L084's exact polynomial coefficients.
All 28 selected equalities then hold exactly, but domain row 26 is
negative, 22 moments are negative and 28 remaining modes are negative.
Every original and raw Schur residual, factor, moment and failed index
is saved in full. This does not test another parameter point by an LP or
constitute a second optimization run. Failure at the rounded point decides
neither feasibility nor infeasibility over the full plane.

`scripts/finite-support/verify_zero_plane_joint_feasibility.py` independently
recomputes the candidate's original bounds from forced entries, the full
anchor, original cross vectors and inverse actions, without assembled
quadratic substitution or an optimizer. It verifies all 85 factors,
45 raw moments, 81 scaled/raw mode residuals, the exact P+N*h relation
and all failed-index lists: 371 checks, zero verification failures.
The constructor has 1471 checks, zero model failures. Exact evidence:
`scripts/finite-support/zero-plane-joint-feasibility-verification.json`.
The normalized minimum domain factor lies in [-0.002485,-0.002484);
normalized minimum moment and mode slacks are approximately -9.68248e14
and -6.46460e14, respectively, against required minimum zero. These large
reconstruction defects prohibit interpreting the proposal as near an
exact completion. The saved exact rationals, rather than these decimal
descriptions, establish the failed candidate signs.

Two pre-solve implementation errors are preserved. The first queried
records in the constructor instead of its verifier (KeyError; no solve);
`zero-plane-joint-feasibility-initial.json` records it. The second compared
integer zero with encoded Fraction zero in the 17 empty modes; its full
failed report is `zero-plane-joint-feasibility-empty-mode-initial.json`.
Using Fraction(0) as the empty sum's identity repaired only the encoding.
No numerical run or reconstruction occurred before the model checks passed.

Reproduction, from the notebook (the first command reruns the single
declared numerical attempt; the second only verifies saved evidence):

    PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 scripts/finite-support/zero_plane_joint_feasibility.py
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/verify_zero_plane_joint_feasibility.py

Outcome: EXPLORATION / RESEARCH / REPRODUCTION. The joint feasibility
question is undecided; there is no new lemma, source-level discovery,
global bound, list realization or boundary improvement. This spends
one mathematical exploration attempt, now 1/3. The fixed conic run and
rounding prescription stop here. A possible fixed exact face reduction
using L082's positive-weight tight modes is proposed for separate source
assessment; no exposing matrix, face dimension or reduced feasibility
claim has been derived or approved in this turn. General exact SDP
Mathlib coverage remains not checked, not asserted absent.
