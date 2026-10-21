# Step 306 — one fixed-face, equality-eliminated joint proposal

Gate: `literature/2026-10-18-fixed-face-reduced-joint-feasibility.md`,
SPECIALIZE before invocation; completed work will be RESEARCH / REPRODUCTION.
The main gap is arbitrary-center safety at 67/68 agreements, bracket 955–957.
The sole intermediate target is the approved full zero-plane joint system.
A complete original-coordinate feasible certificate would park this fixed
diagnostic; an exact whole-domain lifted separator would exclude this family.
Neither settles global moments, other anchors or RS realization.

Inputs: L076,L078,L082,L083 and separately reviewed L084,L085, with
L021,L053,L073,L075,L079,L081 and foundations/04,09,10,12 retaining their
ancestral contracts. The complete step-290/292/294, equality/face and
critical-audit certificates supply the finite data. ATTEMPTS/052–053,
060–067 remain intact. No duplicate reduced full-domain verdict is recorded.

Before numerical work save a rational affine model and both directions
of its elimination/lift. On this plane the selected right sides have no
quadratic coefficients, so use the first four coefficients of L084's
particular solution, checking all six others vanish. Keep all three plane
parameters and 18 homogeneous coordinates. Recover every original moment
and all mixed/removed equations coefficientwise. Retain all 85 domain
rows, 45 signs and 81 modes; L085 reduces their retained sizes 140 to 112.

Predeclared numerical method: one NumPy product-cone ADMM proposal,
relaxation 1.6, at most 10000 iterations, tolerance 1e-9 for primal and
dual residuals. Use only invertible variable/positive block/scalar row
scalings saved before iteration; no variable box. Selected compressed
blocks stay in the model, including empty blocks and every zero equation.
All nonzero singular values of the numerical affine map are retained;
if numerical rank is lost or the exact model fails, stop before a solve.
No convergence, attainment, Slater or rational-existence claim is made.

One reconstruction rule: round the 21 scaled proposal coordinates once
to denominator at most 10^9, then apply the exact affine lift. Check all
original and raw rows and every original block exactly, with singular
and empty cases. No second rounding, point/active-set/weight search or
solve. Failure means save full residuals and stop this prescription,
without a feasibility or infeasibility claim. The unverified numerical
dual is retained as evidence only; a separate separator search is excluded.

Mathlib: full matching finite-system and combined exact certification
coverage not checked; unknown availability is not absence. General
methods are imported by the precise citations in the approved assessment
and L084/L085, without a new general-method proof.

## Exact model saved before iteration

`scripts/finite-support/reduced_zero_plane_joint.py` specializes the
reviewed L084/L085 identities. Its complete certificate is
`scripts/finite-support/reduced-zero-plane-joint-results.json`.
The first four columns of L084's particular matrix are used only after
checking every remaining quadratic coefficient is zero. In augmented
coordinates w=(1,u,z) and v=(1,u,h), the saved lift L satisfies w=L*v.
The reverse R selects (1,u,z_nonpivot); all 18 nonpivot rows of N form
the identity. Write G*w=0 for the 28 original selected equalities,
including their affine right sides. The saved exact checks are

    G*L=0, R*L=I_22, L*R-I_49=K*G.

K uses minus the corresponding rows of L084's invertible row transform
at pivot coordinates, and zero rows elsewhere. These are checked in
every entry before iteration. Thus the parametrization loses no point
of the original equality locus, rather than merely providing a subset.
The constant coordinates of both augmented spaces stay equal to one.
All 85 domain rows and 45 original signs are pulled back by this same
map. All 28 mixed/removed face equation groups vanish coefficientwise
after the lift, including empty compressed blocks. Every original
49-coefficient mode pencil and its old-kernel extraction/inverse lift
are saved and checked. All 81 modes and both face pullback directions
remain present; the retained size sums are exactly 140 and 112.

The construction consumes the complete relevant step-290/292/294,
equality, face and audit arrays. Original beta rows, 90 whole-kernel
equations, full 500-key comparisons and the 3000-presentation contract
are retained. The canonical weights, source decomposition, old PSD,
dictionary uniqueness and whole-kernel exhaustion remain imports under
their recorded ancestral qualifications, not newly completed audits.
No scalar upper rows or other-anchor condition is added.

The method citations remain Permenter–Parrilo,
[arXiv:1408.4685v3](https://arxiv.org/pdf/1408.4685v3), Lemma 1 (1)–(4)
pp.4–5, Lemma 3 and proof p.8 and Section 4.1 p.18;
Vandenberghe–Boyd (1996), DOI 10.1137/1038003,
[published paper](https://web.stanford.edu/~boyd/papers/pdf/semidef_prog.pdf),
Sections 1.1 (1)–(6) pp.49–51 and 3.1 (27)–(32) pp.63–64;
and Ye, *Conic Linear Programming*, October 2017,
[monograph](https://web.stanford.edu/class/msande310/sdpmain.pdf),
Theorem 1.11 p.13 and Section 1.5.1 pp.23–24. These general methods
are imported by the ready assessment and canonical L084/L085, with
the exact finite maps checked rather than asserted from a citation.
No fresh external retrieval or new general theorem is used.

## Single proposal and failed exact reconstruction

All 21 variables remain free over the full domain. Initial nonzero
coordinate scales are 10^(-11) on the three plane parameters and the
old model's positive z scales on the 18 nonpivot coordinates. Each
scalar row is divided by the largest absolute scaled coefficient or
constant (one for an identically zero row). Unselected mode blocks use
positive diagonal congruences; selected compressed constant blocks use
the saved rational congruence to their positive diagonal and then a
positive diagonal normalization. Empty blocks are retained as empty.
One invertible diagonal column equilibration is saved. None imposes
variable bounds or deletes equations. The full unscaled rational model
and all scalings precede the run in the certificate.

The numerical affine map has size 392-by-21. All 21 singular values are
retained, with observed extremes approximately 0.9427075 and 1.0541834.
This numerical rank diagnostic is not an exact feasibility argument.
The single ADMM run reaches 10000 iterations. Terminal primal and dual
residuals are approximately 6.24498265 and 0.02769438; the affine point's
distance to the product cone is 6.244974010438509, against required
exact violation zero. The full trace, terminal affine/cone/dual iterates
and projection residual vector are saved. Scaling differs from step 298,
so these distances are not comparable as measures of progress.

Exactly one reconstruction rounds all 21 numerical coordinates once
to denominator at most 10^9, then applies the saved exact coordinate
scales and affine lift. It satisfies every selected original equality
and all 85 domain rows. It fails 11 moment signs (indices
2,4,9,10,12,16,18,21,23,29,36) and 28 remaining original modes
(4,5,6,8,15,17,22,25,31,34,40,41,42,44,52,58,59,60,62,64,66,70,
73,75,76,77,78,80). Every scaled and raw residual is saved exactly.
All 81 original normalized source blocks are reconstructed, including
singular cases; 75 of their 693 principal minors are negative, in
exactly those 28 modes. This candidate is far from passing and supplies
no feasibility or infeasibility verdict for the full domain. The saved
numerical dual is not claimed to be a separator.

The constructor passes 6784 model/identity checks with zero failures;
the inequality failures are recorded separately as failed candidate
evidence. `scripts/finite-support/verify_reduced_zero_plane_joint.py`
independently rebuilds every original bound from forced terms, full
anchor, cross vectors and inverse actions, checks all raw/scaled rows,
both affine-lift identities, every compressed coefficient and every
mixed/removed group, and reconstructs all 693 original principal minors
with a different determinant calculation. Its 830 checks pass with
zero verification failures. Complete evidence:
`scripts/finite-support/reduced-zero-plane-joint-verification.json`.
These are arithmetic checks for a failed candidate, not a new critical
review of all ancestral claims.

Using the old model's positive scales only to describe the exact failed
residual magnitudes, the domain minimum is in [14,15)/10^6; the moment
minimum is about -9.68257e14 and the mode minimum about -6.46470e14,
against required minima zero. Exact rational intervals and full values
are in the verification certificate. A small numerical residual would
not have sufficed either. No failed sign is hidden by tolerance.

Reproduction from this notebook (the first command reproduces the one
declared run; the second only checks saved evidence):

    PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 scripts/finite-support/reduced_zero_plane_joint.py
    PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 scripts/finite-support/verify_reduced_zero_plane_joint.py

The initial bounded audit-inspector calls hit Python's integer-string
limit; PYTHONINTMAXSTRDIGITS=0 fixed access without changing any data.
There was no failed model build, second numerical run or second
reconstruction. No lemma, DAG node or PROOF.md argument changed.

Outcome: EXPLORATION / RESEARCH / REPRODUCTION / calculation. This is
the second mathematical exploration attempt (2/3) on joint feasibility,
not mathematical progress beyond the sources checked. Stop this reduced
conic prescription; preserve ATTEMPTS/067 and all earlier stops. A
materially different proposed continuation is an exact polyhedral test
of the selected affine equalities plus domain and moment signs, leaving
the 53 remaining PSD modes aside. It has no conic convergence premise
and could identify whether signs alone obstruct this plane. Its changed
scope is REVIEW_REQUIRED in a separate assessment; no such test or new
source approval was performed here. A feasible sign-only witness would
leave all remaining-mode, global and RS gaps open. The main bracket
remains 955–957 and STATUS remains IN_PROGRESS.
