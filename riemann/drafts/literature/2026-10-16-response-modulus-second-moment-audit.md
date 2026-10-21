# Source and scope approval for the new second-moment diagnostic

TARGET: Critically audit L422's sharp full-response second moment and all-k fixed-g0 separation, including its complete rational certificate.
CHECKED: 2026-10-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused step 164's primary theorem inspection and exact-target search; inspected L422 in full, the certificate generator in full, relevant L381/L389/L419 input ranges, L421 component and audit passages, steps 163--165 and the fixed-g0 failure record. No additional external search was needed for unchanged source hypotheses.
SOURCE_EVIDENCE: Direct primary PDF https://www.math.ntnu.no/emner/MA3001/2020v/2022v_MA3004/Young.pdf ; Young, A short proof of Levinson's theorem, Arch. Math. 95 (2010), 539--548, DOI 10.1007/s00013-010-0199-9, (2.1)--(2.3), Lemmas 4--5/(4.1)--(4.5), pp. 540, 542--543; prior inspected theorem comparison is in drafts/literature/2026-10-16-response-modulus-weighted-second-moment.md. Reused L381 (7),(9) and its critical audit, L389 (3), L419 (3)--(4), L421 (4)--(9) and its step-163 audit.
COMPARISON: The imported fixed-twist moment covers the order-zero finite head, not the full response or the family separator. Those are written local specializations in L422; their independent audit requires no stronger source theorem and no essential unread source. This review identifies audit obligations without establishing them.
GAP: Critically verify the complete specialization and exact certificate, including all limits, determinant signs and fixed-k quantifiers; L422 remains unaudited. Other covariance weights, clipping, full-error regulator margin and global mixed positivity remain unresolved.
REASON: The new audit target is covered by unchanged primary inputs and a complete local proof/certificate specification. A bounded critical audit is approved; no new result, lemma edit, mathematical script execution or certificate verification occurred in this literature-only step.
SCOPE: Actual E=H^(-1) integral_[H,2H], x=F_0/A, W=|zeta(5/2+it)|^2; exactly L421's fixed-g0 family, every admissible fixed integer k and its prescribed theta. Constants/onset may depend on k. No growing-k uniformity or arbitrary-weight separation is covered.
COVERED_TARGET: Critically audit L422's sharp full-response second moment and all-k fixed-g0 separation, including its complete rational certificate.

## Relevance, use and decision test

The main target gap remains global mixed-form positivity. The intermediate
objective is an independent correctness decision for L422's added
response-weighted second-moment diagnostic. If validated, it constrains
future covariance-weight constructions by excluding the specified fixed-g0
family under this additional correlation. It does not reverse L421's
selected-information obstruction or establish actual clipping.

Continue using this separator only after its full sharp coefficient,
all-component law coefficient and every-fixed-k comparison survive the
audit. A false inequality, unbounded tail, missing component or unjustified
limit requires a precise repair or withdrawal of the affected separator
claim. A certificate preview or successful program exit alone is insufficient.
A repair outside this assessed scope requires separate source review.

## Source coverage and necessity of specialization

Reuse the primary inspection recorded in the step-164 assessment; this
step does not claim to have freshly read an external PDF. Young's weight
hypotheses are 0<=w<=1, support [T/4,2T], derivative scale T/log T,
fixed positive twists with product <=T^(2vartheta), vartheta<1/2, and
complex shifts O(1/log T). Both functional-equation diagonals and both
off-diagonal orderings are covered. At T=2H, L422's fixed-shape weights
supported in [H/2,3H] fit. For each fixed head the twist restriction holds
eventually. L381's combined holomorphic evaluation supplies zero shifts
without differentiating singular terms separately. No fast carrier or
size-two critical-line shift is being passed to this theorem.

L389 (3) supplies the exact Hardy-square identification, not a moment
independence assumption. L381 (9) supplies the sharp scalar norm. L419
(3) supplies full right-line fixed-power moments with their absolute
Dirichlet-series domain. L421's audited component bounds supply the law
comparison. The stronger finite-polynomial theorem of Bettin--Chandee--
Radziwill, Theorem 1, arXiv:1411.7764v1, is already compared in step 164
but is unnecessary as an additional input. No new literature reason or
reproof of either general moment theorem is needed here.

Neither source directly states this separator. Checking L422's elementary
specializations is necessary because the source does not determine the
specific Euler factors, component errors or all-k determinant comparison.
The determinant identity and geometric tails are fully written in L422;
the audit may verify them directly, without asserting a new general
moment theorem. Full matching Mathlib coverage remains not checked;
unknown coverage is not evidence of absence. No Lean verification is claimed.

## Approved independent audit obligations

1. Check L389's normalization including zeros, the fixed-twist gcd factor,
   both source diagonals, and the V_N expansion with every collision.
   Bracket the complete nonnegative integrand at both sharp endpoints.
   Keep smoothing width and head fixed for the height limit; remove
   smoothing and then the response head with a norm bound independent of N.
   Verify convergence of the full double sum and its Euler product.
2. Inspect all three L421 components as unnormalized component integrals.
   Retain high/intermediate second-moment contributions, bounded response
   factors, the complete O_k(sqrt(log H)) covariance correction, bounded
   bulk mean, rare-mass normalization, and L419's fixed-power mean error.
   Check the resulting B_k and prescribed theta without selecting a
   convenient admissible parameter or asserting a common onset for all k.
3. Verify the finite-prime moment representation and bounded Fubini
   determinant expansion, its factor 1/6, orientation, repeated-point
   cases and strict convexity for every pair of integers 1<=k<l. Check
   finite-prime passage, moment log-convexity, positive denominators and
   S>C_1 before division. Nonstrict monotonicity must suffice for all k,
   including algebraic comparisons outside the law's admissible range.
4. Independently verify L422 (8)--(12): exact local T factor, every local
   C_j truncation tail for j=1,2,13,14,15,16, omitted-prime bounds for
   C_j, zeta(3), zeta(5), zeta(6), and T, and the exponential-to-rational
   conversion. Verify the prime list through 200 and truncation order 40.
   Check outward rounding after every operation, positive denominators,
   all exact thresholds in (13), C_2>C_1^2 and S>C_1. Read the complete
   generator and relevant certificate evidence; floats are previews only.
5. Check that monotonicity and the two certified adjacent coefficients
   imply the strict 1/1000 gap for every admissible fixed integer k.
   Preserve L421's old selected-list result and all scope qualifications.
   Review direct mathematical inputs against the existing ID-only DAG;
   structural validation is not mathematical validation.

The approved audit should inspect the complete relevant certificate fields
using `python3 ../scripts/loop/inspect_json.py` with selected pointers,
including `/bounds`, `/checks`, `/failures`, `/log_tail_upper_bounds`,
`/primes`, `/prime_cutoff`, `/local_order`, `/denominator`, and all local
factor records needed for its verification. Use `--full` only for selected
load-bearing values. The certificate is
`scripts/discriminant/response-modulus-second-moment-certificate.json`;
its generator is `scripts/discriminant/check_response_modulus_second_moment.py`.
These are audit inputs, not newly verified evidence in this turn.

## Duplicate and failure comparison

The step-163 audit already validates L421 on its original selected list;
repeating that entire audit is unnecessary. Step 165 and the canonical
fixed-g0 attempt record already contain the new claimed separator; this
turn adds only separate coverage/scope approval. The radial-lift failure
concerns a different cubic obligation and is preserved. None of these
records rules out different covariance weights. No independent L422
audit was found in the inspected exact-target records, and no novelty
claim follows from this scoped check.

Completed work here is LITERATURE / NOVELTY_UNCHECKED: a new bounded audit
scope comparison, not mathematical validation or a new source import.
The next covered audit is RESEARCH / REPRODUCTION. Mathematical exploration
usage remains 0 of 3; this literature review spends no calculation budget.

## Step 167: direct-source metadata recovery

LITERATURE_REASON: The supervisor rejected ready coverage because this
assessment lacked a direct source URL; this bounded retrieval repairs
that omission without changing the mathematical target or approved scope.

On 2026-10-16 the direct primary PDF linked in SOURCE_EVIDENCE was
successfully opened. Rechecked (2.1)--(2.3), Lemmas 4--5, and the two
off-diagonal orderings in the proof on printed pp. 540, 542--543.
These agree with the prior theorem comparison. The auxiliary expression
in Lemma 4 is singular at zero total shift; the existing obligation to
use the combined holomorphic evaluation remains essential. No new source
theorem or stronger conclusion is imported. The stronger optional
Bettin--Chandee--Radziwill source is not needed and was not reopened.

The TARGET metadata now exactly repeats the already approved
COVERED_TARGET and checkpoint action. This is a process repair, honestly
STALLED as mathematical progress; it does not validate L422 or its
certificate, renew exploration, or change any historical stop. Reuse
this assessment for the same independent audit. Continue only if the
sharp limits, all components, determinant signs and complete exact tails
survive; otherwise identify and withdraw or repair the affected claim.
No lemma, mathematical script, DAG or proof assembly was edited.
