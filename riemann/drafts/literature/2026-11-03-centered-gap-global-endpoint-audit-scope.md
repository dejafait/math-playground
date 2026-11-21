# Source scope for the signed global-endpoint obstruction audit

TARGET: Critically audit L702's admissible fixed-profile selection, signed limit at u=-1 and endpoint-remainder obstruction, including its complete rational certificate.
CHECKED: 2026-11-03
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 139 reused the step-128 exact-target search/comparison and the step-112/118/136 audit-tool records; read L702 and its complete 82-line certificate generator, the necessary L666/L690/L694/L696 interfaces, and the step-129/133/137 failure records. No broad repeated search or novelty inference.
SOURCE_EVIDENCE: Directly read Lev arXiv:2007.09930v3 (27 September 2021), Lemmas 4.2--4.7 with proofs and Sections 4.9--4.10 through Theorem 4.8's proof; collated published Lemma 4.3, p.1984 (4.6), against the publisher PDF. Reuse the checked DLMF 4.6.4 and Python Fraction coverage in the step-136 assessment. Exact reading limits and local input scope appear below.
COMPARISON: Lev's coefficient constant is independent of the shift parameters and the later prescription width; its fixed-point framework supports the local L694/L696 interface. It does not supply L702's width-uniform Wiener bound, signed finite-product limit, alias estimate or endpoint remainder. L690 (1) covers the finite unshifted family; no informal infinite comb substitutes for it.
GAP: Audit L702 Sections 2--5 and the complete rational certificate, particularly the order of constant/radius/width selection, uniform scaled-cutoff norm, full-spatial coefficient extraction, dominated l1 difference, aliased signs and strict endpoint comparisons. Tool coverage does not validate these claims or an angular logarithmic mean.
REASON: The separate source comparison now covers the unchanged bounded audit, with no essential source blocker. EXPLORE permits scrutiny of the existing family-specific argument; it neither imports nor critically verifies its conclusion. The supervisor may approve this newly completed assessment next turn.
LITERATURE_REASON: The invocation-start audit was REVIEW_REQUIRED after the new L702 argument; earlier ready coverage concerned the scalar attempt and different residue/bulk audits. Reuse that coverage and resolve only this constant/width, finite signed-limit and certificate interface.
SCOPE: Exactly TARGET, with L666 (6), L690 (1) at common shift zero, L694 (2)--(9) and L696 Section 2. Retain fixed real l1 shifts, r<=1/8, a fixed positive centered gap, n=12q+3, both actual endpoints, unit masses, anchor, all n factors including j=0, inverse angle and all M moments. No cross-notebook input.

## Original nomination

The nomination below is preserved. Its pending-source wording is
superseded by the completed source comparison; the mathematical audit
remains pending.

The main gap remains actual-Xi mixed positivity. This audit would decide
whether the new signed remainder is reliable evidence against the
direct full-circle extension of the local endpoint method. It cannot
establish scalar charge payment, full-spatial compensation, H/support
or Xi transfer. L702's conclusion is restricted to profiles meeting its
attainable smallness condition; it is not universal over Picard choices.

Reuse ready source assessments rather than repeating broad searches.
The exact input IDs are L666, L690, L694 and L696. L699/L700/L701 and
L695 are comparisons and route history, not premises of L702. The
complete scalar root formula need not be reimported for this audit:
the proposed conclusion stops at a pointwise signed remainder.

The separate source comparison should determine whether the already
inspected Lev coefficient estimate and Picard scope permit increasing
the valid constant before choosing the fixed radius and width. Check
L690's common-shift-zero applicability and coefficient extraction from
the full spatial polynomial; do not silently replace it by an infinite
oscillatory sum. The elementary integrations by parts, Taylor bounds
and l1 dominated-series passage are fully stated in L702 and require
hypothesis-level review, not an unrelated new theorem search.

After source approval, the bounded audit test is to accept all these
steps and the complete exact certificate, repair a real mathematical
error, or identify the precise unsupported assertion and withdraw it.
Pay both actual endpoints, all n product factors, the anchor, unit
masses, inverse angle, fixed positive gap, real l1 cap and all downstream
M moments. Inspect the entire relevant exact certificate, not a preview.
The script verifies constants only and is not an independent proof of
the analytic profile selection or limit. Full matching Mathlib coverage
is not checked; no formal result or absence claim is nominated.

## Completed source comparison — 3 November 2026, step 139

### Purpose, overlap and limits of this turn

The main gap is actual-Xi all-degree mixed positivity and unbounded-height
signs. The intermediate target is a reliable decision on L702's claimed
signed interior remainder. Its downstream use is to decide whether the
direct full-circle endpoint-only extension can be retired on sound
evidence. Even acceptance would leave the existential scalar charge
target, angular logarithmic control, spatial comparison, H/support and
Xi realization unresolved.

Read L702 in full to identify its proof obligations. Read L694's kernel,
two-norm construction and relevant completed-audit qualifications;
L696's prescribed-center construction; L690's hypotheses and (1); and
L666's exact product (6). These are local inputs, not newly imported
general results. Reused the search and theorem comparison in
[step 128](2026-11-03-centered-gap-scalar-complete-log-lower.md),
the coefficient/Picard coverage in
[step 112](2026-11-03-summable-anchored-gap-audit-scope.md),
the centered-profile scope in
[step 118](2026-11-03-centered-gap-scalar-audit-scope.md), and
the elementary-series/Fraction coverage in
[step 136](2026-11-03-centered-gap-bulk-pole-audit-scope.md).
No unchanged broad search was repeated. No matching theorem for the
signed finite-family conclusion was identified in those checked records;
this is not a novelty claim.

Checked the recorded failures in
`ATTEMPTS/2026-11-03-centered-gap-scalar-charge-unpaid.md`,
`ATTEMPTS/2026-11-03-centered-gap-common-sign-residue-stop.md` and
`ATTEMPTS/2026-11-03-centered-gap-bulk-pole-pairing-stop.md`.
L699's unpaid sufficient signs, L700's mixed-residue obstruction and
L701's microscopic zero-free subsequence neither prove L702 nor ban its
independently testable remainder claim. L695 remains an absolute-tail
comparison, not a premise. This audit does not reopen those mechanisms.

### Primary coefficient and fixed-point scope

Directly retrieved Nir Lev,
[*An example concerning Fourier analytic criteria for translational tiling*,
arXiv:2007.09930v3](https://arxiv.org/html/2007.09930v3#S4.SS3),
dated 27 September 2021. Read Lemmas 4.2--4.7 with their proofs and
Sections 4.9--4.10, including the complete proof of Theorem 4.8.
Also checked the [published PDF](https://ems.press/content/serial-article-files/39104):
*Rev. Mat. Iberoam.* 38 (2022), no.6, 1975--1991,
DOI [10.4171/RMI/1318](https://doi.org/10.4171/RMI/1318),
Lemma 4.3, p.1984, (4.6). This matches arXiv (4.10).

Lemma 4.3 assumes smooth varphi with varphi'(0)=0, a fixed smooth
cutoff Phi, real u,v in [-1,1] and integer k. Its coefficient constant
depends on Phi,varphi,m, not u,v,k. The proof includes zero/nonzero
Fourier modes and boundary-free integration by parts. Sections 4.5--4.8
give the supported real-coefficient spaces, distributional summation,
nonlinear operator, small-radius contraction and unique fixed point in
its specified ball. Theorem 4.8 assumes Hermitian data supported in two
annuli and small coefficient supremum; its conclusion gives bounded
real shifts and a distributional counting-measure identity. Its proof
uses the Wiener multiplier norm for general data.

These inspected hypotheses impose no distinguished numerical value of
the coefficient constant and no later prescription width in it. Thus
there is no source-level restriction forbidding the selection order
proposed in L702. This is source-scope clearance, not verification that
L702's quantitative selection succeeds. Absolute summability, the
smooth-data integral bound and the centered anchored prescription are
the local L694/L696 additions. Do not attribute their conclusions, or
L702's new quantitative norm estimate, to Theorem 4.8. No reproof of
Lev's imported coefficient estimate or contraction theorem is needed.

### Exact local interfaces and the remaining audit

1. L702 Section 2 must retain one fixed Phi, eta and Psi independently
   of the enlarged valid C. Check every dependence in A_0,A_2,B and
   the bound claimed uniform in w, including both bumps, the periodic
   boundary terms, k=0, N=ceil(1/w) and both frequency tails. Check
   Q_w against L696's actual reflected Q, L694's coefficient-smallness
   condition and its same-limit l1 bound. Only after these checks may
   one accept the claimed attainable r*E<=1/(16*pi^2), with C,r,w and
   a positive gap fixed before n. No second fixed point or n-dependent
   sequence of profiles may replace the selected profile.
2. L690 (1) applies to its common-displacement subfamily, uniformly on
   both circles, with all spatial moments. The required interface is
   its alpha=0 case, followed by constant-coefficient extraction in
   the spatial variable. Check that this yields L702 (6) with the
   same normalization. Its finite contour estimate is the baseline;
   neither a bare infinite half-lattice sum nor L701's bulk asymptotic
   supplies it. No contour theorem is newly invoked in L702.
3. Sections 3--4 require checks of the exact u=-1 substitution,
   including j=0 and inverse angle, the uniform real derivative bound,
   fixed-index Riemann/Taylor limit and domination of the displaced
   difference by a summable majorant. The undisplaced series must
   remain handled by L690. Check both moving finite endpoints and
   every fixed index's eventual inclusion; a compact-index limit
   cannot be asserted at indices of order n.
4. For the alias step, verify the strict frequency enclosure,
   tau=Omega/(2*pi)-1 in (-1/8,0), Q_w(tau)=0 and Phi(tau)=1.
   Pointwise evaluation needs L694's continuous Wiener limit, not
   just an equality of distributions. Check the exponential phase
   convention and division by the nonzero v, then the signed identity
   and its quadratic remainder. The existing local proof states
   these elementary estimates; this turn has not derived or verified
   them. No complex-frequency continuation is supplied by Lev.
5. Section 5 must check the strict positive envelope and both actual
   outermost nodes at the claimed onset, the all-n upper bound, every
   product factor, the node count, and the eventual triangle-inequality
   margin. Distinguish the existence of one selectable small profile
   from the conditional claim for every profile meeting (1). Neither
   claim is universal over other Picard choices.

The basic integration-by-parts, Taylor and dominated-series arguments
are already written in L702; they remain mathematical audit obligations,
not missing general-theorem citations. Reuse
[DLMF 4.6.4](https://dlmf.nist.gov/4.6#E4) for the logarithm series and
the [Python Fraction documentation](https://docs.python.org/3/library/fractions.html)
as read in step 136. The actual positive arguments, finite tails,
operand types and exact comparisons still require checking. No new
series bound or analytic lemma is established in this source turn.

Read the entire 82-line generator
`scripts/one-sided-hankel/centered-gap-global-endpoint-138.py` only to
identify its asserted checks and rational backend. Inspected the complete
JSON `/scope` value with `inspect_json.py --pointer /scope --full`.
It explicitly limits the certificate to constants. This is not a replay
or certificate verification. The later audit must inspect the complete
two logarithm records, both Omega bounds, all twelve actual/required
comparisons, failures and aggregate result; check the generator against
each value. Float conversions occur in displayed summaries and must
not enter any proof comparison. A passing certificate cannot validate
the profile selection, signed limit or fixed-point identity.

### Decision and bounded continuation test

EXPLORE now covers the unchanged TARGET. There is no essential source
blocker; no further literature turn is needed unless an actual changed
hypothesis or missing essential theorem is identified. The supervisor's
separate next-turn assessment approval remains distinct from this
completed source comparison and from the mathematical audit.

Accept L702 only if its fixed-profile selection, signed limit, strict
endpoint inequalities and complete certificate survive. Otherwise
identify and repair or withdraw the exact unsupported assertion while
preserving the original argument and stop evidence. A lower modulus at
one angular point must not become a logarithmic-mean or charge bound.
This test does not require an effective or profile-uniform onset.

Route the same target to proof_audit/conceptual_audit,
deep_research/xhigh: the order of parameter selection and the signed
alias/limit interface need analytic judgment beyond arithmetic replay.
Full matching Mathlib coverage is not checked; no formal verification or
absence claim is made. This literature-only turn changes no lemma,
mathematical script, dependency or mathematical overview, and establishes
no new mathematical result.
