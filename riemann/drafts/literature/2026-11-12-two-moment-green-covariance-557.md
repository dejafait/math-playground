# Source comparison: exact two-moment primitives and the induced metric

TARGET: Assess the clamped two-moment primitive map f=(d²/dx²-1/4)u for C744z's full separation7/14 block, and determine whether it supplies a computable signed relative-covariance test below1 without losing the induced energy metric.
CHECKED: 2026-11-12
DECISION: EXPLORE
SEARCH_EVIDENCE: Step558 searched compact-support exponential-moment differential ranges, minimal/maximal regular operators, clamped Green covariance and Weil derivative factorization; checked scoped separation/shared-middle assessments and stops544/545/546/557, plus the differently scoped two-moment stops323/324 and periodic-Jacobian stop. No quantitative matching estimate was located; no novelty inference follows.
SOURCE_EVIDENCE: Directly inspected Teschl GSM99,12February2009, Section9.1/(9.1)-(9.13), Theorem9.1 and Lemmas9.2/9.4 including proofs and regular-endpoint example pp181-185; Fasshauer-Ye1109.5755v1 Definitions3.2/3.4/3.5, Lemma3.2, Theorems3.1/4.1 with proofs, Example5.2 pp8-13/16-17/23; Dritschel-Rovnyak0903.3639v1 AppendixA.1 both proof directions pp28-29. Reuse assessments541/548/553/555 for closed forms, Suzuki's metric warning and non-dense inverse order.
COMPARISON: Teschl's compact-support proof already uses annihilation of two homogeneous-solution moments; ordinary Green/RKHS positivity concerns its specified differential energy, not C744z's logarithmic D+S or its two defect metrics. Contraction factorization supplies an equivalence with the unknown signed block, not a bound below1. No inspected source supplies an independently computable covariance gain for this map.
GAP: No paid relative-covariance estimate, weighted-domain inverse theorem or analytic remainder establishing threshold1 for the actual V14+R^2 was found. The map's complete specialization has not been proved here. Park the stand-alone coordinate mechanism; an additional signed estimate in the induced metric is required to reopen it.
REASON: This completed literature-only comparison finds standard representation overlap but no quantitative sign mechanism. It changes the route without deriving a new primitive identity, proving impossibility of derivative methods, or modifying lemmas/scripts. A separate bounded original-form covariance nomination reuses ready inverse-order coverage.
LITERATURE_REASON: The invocation-start target was REVIEW_REQUIRED because the clamped second-order map, two exponential constraints and induced weighted metric were outside assessment548's first-derivative scope; this turn supplies that missing comparison.
SCOPE: ell=log(3)/2, offsets0,7ell,14ell, complex profiles, u=u'=0 at both cell endpoints, original complete D,S,T,U and both exponential moments; no constant-centered density envelope, response truncation, guessed scalar floor or fixed546 retuning.

The nomination below is preserved; its pending-review wording is superseded
by the completed comparison at the end. It is not a derived primitive identity,
kernel estimate or approval to calculate. The main gap remains
L030-L032/C032a actual-Xi positivity. The intermediate purpose is an
independently testable bound on the full three-cell signed covariance;
it could address compatibility of local signs while leaving other
separations, C744q margin, strict H2 slack/existence, non-neutral coverage
and global assembly unresolved.

Review the proposed differential map with both endpoint values and
derivatives zero. Determine its exact image and inverse on the two-moment
subspace, first for smooth profiles and then in the actual weighted form
domains. Neither surjectivity nor a domain-preserving bounded inverse
is asserted here. Preserve the complete transformed single-cell metric:
ordinary unweighted derivative estimates or smoothing of the cross kernel
alone cannot replace that metric.

The desired test concerns C744z(4)'s two defects I-R*R and I-RR* and
the actual V14+R², including the neutral middle inverse. Seek a computable
strict contraction bound below1 in their defect metrics. Nullspaces,
range conditions and any use of generalized inverse square roots need
explicit treatment. An equivalent contraction criterion alone is not
progress; the literature review must identify an independently checkable
kernel/covariance estimate or a precise obstruction. No such bound is
claimed in this nomination, and no source theorem may assume the unknown
three-cell positivity in order to supply it.

The materially new element to assess is a second-order map enforcing both
exponential moments, with complete signed covariance retained. Stop544
instead integrated a subtracted prime density once and paid its absolute
L1 primitive by a derivative envelope; its coefficient>.03200576 missed
the required<.01072864 and cannot be repaired by an integration constant.
Stop545 removed the middle response; stop546 kept only32 response squares.
Neither removal is proposed. C999k pays one fixed endpoint pair only;
repeating its reference or enlarging its trial is not the present target.

Compare the exact statement, standard Green/closed-form terminology,
stronger results and known metric obstructions in primary sources.
Reuse [Suzuki v3](https://arxiv.org/pdf/2606.09096v3) only within the scope
actually inspected in assessment548: its first-derivative, mean-zero
inverse-Neumann metric is a warning, not coverage of this map. Reuse
C744v/w's entry/response contracts and assessment541's representation
theorems without reopening unchanged source approvals. Essential new
source cases must be read before approving any mathematical test.

Continue only if the review identifies a complete finite test and
analytic remainder with the stated relative threshold, or a concrete
obstruction test in the induced metric. If it is only an invertible
coordinate congruence with no independently estimable gain, park this
mechanism and record that reason. A failed sufficient estimate is not a
negative Weil witness. No automatic creative classification is assigned:
a source-supported new central mechanism may merit proof_attempt/creative,
but merely changing coordinates is routine specialization.

Essential local inputs are C744z Sections1-3/6-9, C744v/w's complete
forms and entries, C999j's residual identity and C999k's audit557 for
contrast, and assessments541/548. Preserve all analytic/runtime and
whole-core/unreplayed c_* qualifications when an input uses them.
L742/L744 are the original full-form normalizations; no RH or H2 premise
is licensed. Full matching Mathlib coverage has not been checked.

## Completed comparison — 12 November2026, step558

The main gap is L030-L032/C032a actual-Xi positivity. This review asks
only whether second-order neutral coordinates expose a quantitative
way to pay the complete three-cell signed covariance. Success would
give one local compatibility input; all other separations, C744q margin,
strict H2 slack/existence, non-neutral coverage and assembly remain open.

### Primary range and kernel sources

[Teschl, *Mathematical Methods in Quantum Mechanics*, GSM99,
12 February2009 author PDF](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf),
Section9.1, pp181-185: the expression has positive p,r and locally
integrable p^-1,q,r, with q real. Theorem9.1 and Lemma9.2 give
inhomogeneous existence/uniqueness and variation of constants.
Lemma9.4 identifies the compact-support closure and maximal adjoint
using boundary Wronskians. Its full proof explicitly constructs a
compactly supported inverse for sources annihilating both homogeneous
solutions; the regular-endpoint example identifies zero value and
flux. Read both endpoint cases and the complete adjoint/closure proof.
The proposed expression is the negative of the regular p=r=1,q=1/4
case; sign conventions and the notebook's first-slot convention must
be respected. This is standard representation coverage, not a new
mechanism. Extension to the notebook's logarithmically weighted V0,
a bounded inverse in its induced norm, and quantitative covariance
control remain applicability obligations; none is asserted here.

[Fasshauer and Ye, *Reproducing Kernels of Sobolev Spaces via a Green
Kernel Approach with Differential Operators & Boundary Operators*,
1109.5755v1,27 September2011](https://arxiv.org/pdf/1109.5755v1),
Definitions3.2/3.4/3.5 and Theorems3.1/4.1, pp8-13/16-17:
the setting is a regular bounded domain, m>d/2, a differential vector
in the specified elliptic class and boundary operators characterizing
all traces through order m-1. The Hilbert inner product is the sum
of L2 products of those differential outputs. Theorem4.1 assumes an
existing Green kernel for L=P*P and identifies its reproducing space;
its proof uses smooth density, duality and Sobolev embedding. Read
the full proof and Lemma3.2's trace criterion. Example5.2, p23, uses
P=(d/dx,sigma I) and value-only Dirichlet data. It is not a clamped
inverse of the proposed second-order map. No application of its
positive kernel to the notebook's D+S or defect metric is justified.

[Dritschel and Rovnyak, *The Operator Fejer-Riesz Theorem*,
0903.3639v1,21 March2009](https://arxiv.org/pdf/0903.3639v1),
AppendixA, LemmaA.1, pp28-29: for bounded blocks, positivity is
equivalent to nonnegative diagonals and off-diagonal factorization
through their square roots by a contraction. Both proof directions
and the partial-isometry construction were checked. It handles
singular diagonals through closures of ranges; it does not license
everywhere-defined inverse square roots. A bound strictly below1
is extra quantitative information. LemmaA.2 assumes positivity of
the whole block and cannot provide the presently missing sign.

These standard results are cited rather than reproved. No clamped
range identity or weighted covariance lemma is established in this
literature turn. Full matching Mathlib coverage is unchecked.

### Comparison with the actual target and recorded failures

C744z(2)-(4) fixes the required objects: A0 is the neutral restricted
operator, R=A0^-1/2 K A0^-1/2, V14=A0^-1/2 J A0^-1/2, the two
diagonals are I-R*R and I-RR*, and the cross block is V14+R^2.
Its Section1 states V0's logarithmic cosine weight. C744v's full
single-cell response includes its j=0 term; cancellation of a
separated j=0 product does not remove that local response. These
are existing canonical inputs, not newly derived formulas.

Neither the ordinary Sobolev Green metric nor the source's positive
reproducing kernel supplies those three operator comparisons. In
particular the 334 actual remote prime-power translations, including
the identity delay, and the entire induced middle covariance cannot
be replaced by the continuous Green part. A new kernel representation
would need a quantitative estimate for these terms together, with
the original energy and both defect ranges. No such estimate or
complete finite test plus analytic remainder was found. This is a
source-scope conclusion, not a proved lower bound on the desired
contraction norm or a proof that every possible primitive method fails.

Reuse Suzuki2606.09096v3 Sections8.4-8.5/(8.6)-(8.7), p32, exactly
as inspected in assessment548. Its first-derivative mean-zero
inverse-Neumann metric warning is consistent with this mismatch;
it is not a theorem about this clamped two-exponential map. Do not
repeat that source approval or infer a metric-preserving signed gain.

Stop544 rejects a particular absolute L1 primitive coefficient;
stops545/546 omit respectively the middle response or its unpaid
suffix. None proves the current map impossible. Stop557 correctly
limits the successful C999k audit to fixed endpoints. The older
two-moment Hardy-Poincare assessment323/324 concerns L751's different
weighted remainder, and the periodic-Jacobian stop concerns L847's
unweighted moments; neither is a matching duplicate. No local ready
clamped covariance theorem was found in the scoped paths searched.

Queries included `differential operator compact support exponential
moments range D2 a2 Green function Sobolev clamped boundary`,
`minimal maximal regular ordinary differential operator range
orthogonal kernel adjoint H0 Sobolev theorem`, `exponential splines
vanishing exponential moments differential operator`, `Weil quadratic
form second derivative exponential moments`, and `clamped Green
covariance operator relative norm`. The Berkeley Oh/Tang ODE notes
Theorems2.24/2.27 were inspected as a parallel range lead; Teschl's
primary proof suffices. EPFL's khalidov0501p.pdf could not be opened;
it is an optional exponential-spline lead, not essential coverage.
Other search hits were not theorem inputs. No source blockage is
used to postpone a ready mathematical attempt.

### Decision and bounded continuation

Park the clamped primitive representation as a stand-alone sign
mechanism: the inspected sources give representation machinery and
an equivalent factorization, with no independent metric-relative
gain. Reopening requires a concrete new signed estimate, its exact
domain and a discriminating bound below1; another coordinate identity
or derivative-envelope retuning does not meet that condition.

The separate nomination in
[assessment558](2026-11-12-neutral-head-uniform-covariance-558.md)
tests a different quantifier in the original form: all endpoints in
one fixed finite exact-neutral head, while retaining the infinite
middle response. It uses the audited reference unchanged, not a new
scalar floor, a response prefix or a fixed546 rerun. No family sign,
predictor, covariance matrix or remainder is derived in this turn.
This is a standard-method specialization; no justified creative sign
mechanism emerged from the current source review. The new ready
nomination requires separate approval next turn.
