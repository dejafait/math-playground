# Sixth-power amplification — source coverage for conditional audit

TARGET: Audit family 003 lem:inverse-amplification at commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a using L539, checking sixth-power multiplier fibres, row-dependent test majorization and the exponent max{1,(1+5r)/6}, with primitive arithmetic estimates retained as explicit contracts.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched family003 assessments, notes, histories and relevant L53x files for inverse-amplification, raw-moment, sixth-power and row-dependent tests; searched ATTEMPTS for amplification/sixth/family003. Earlier application assessments retain amplification as a contract; no completed matching local audit was located. Web queries included "inverse-amplification" "sixth" and sextic character large sieve sixth power amplification Mobius inverse moment; inspected the pinned source, Xu–Sang v1 Theorem 1.1/Corollary 1.2 and the qualifications of the teal-sea amplification note. This bounded comparison does not establish novelty.
SOURCE_EVIDENCE: OpenAI September 30, 2026, pinned build/paper.tex: arithmetic conventions/count 520–588, marked hypotheses/statement 8681–8730, complete raw-moment/amplification argument and post-proof qualification 11664–11788; smooth-calculus definitions/parameter-Sobolev statement 1019–1066 and relevant proof 1123–1154. L539 hypotheses/conclusion were read. Stable labels and applicability are recorded below.
COMPARISON: The exact amplified maximum and rowwise norm-twist clause are already claimed by lem:inverse-amplification. The task is conditional verification using L539 without assuming lem:marked or amplification itself. Generic sextic operator norms concern arbitrary coefficients and do not replace this structured Möbius argument; inspected lower bounds do not refute its specified vector.
GAP: Primary coverage is adequate for the stated conditional audit. The L539-to-raw specialization, zero-retaining column identity, injectivity, small-scale Sobolev envelope and loss/height bookkeeping have not been independently proved in this review. L539's primitive arithmetic/support/uniformity contracts and actual-Xi signs remain unresolved.
REASON: SPECIALIZE permits checking this known argument under the notebook's conditional input, not claiming a new estimate. Reproduction is justified by interface verification of the qualified external manuscript: citing its conclusion alone would assume the interface under review. This literature-only step supplies proof coverage, not an application proof.
SCOPE: Exactly the unmarked sixth-power-free-row interface, either common orientation, fixed excluded primes/ray presentation, smooth compact annular tests, bounded nonnegative r, compact real norm twists and polynomial height cost. Retain L539 and primitive ideal/divisor-count contracts. Exclude arbitrary column coefficients, moving excluded-prime sets, row-dependent prime coefficients, other moments, complete external import closure and Xi positivity. No cross-notebook input.

## Primary source and complete proof coverage

OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free
Half-Plane Re(s)>7/8*, September 30, 2026, commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`,
[pinned build/paper.tex](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex),
`lem:inverse-amplification`, `eq:raw-moment`,
`eq:inverse-scale-supremum`, `eq:sixth-power-column-identity`,
`eq:amplified-note`, and `lem:smooth-calculus`/
`eq:parameter-sobolev`. Retrieval lines identify this pinned version.
The whole amplification proof, rather than a preview, was read.
The repository supplies an [Apache-2.0 license](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/LICENSE).

The following are **source assertions and future audit obligations**,
not newly established local results.

| Interface | Inspected source cases and qualifications |
| --- | --- |
| Presentation, 520–588 and 8682–8696 | Norms are ideal norms. Ideal sums use primary representatives outside a fixed finite S; element rows retain units. The full fixed ray modulus is supported on S. Both common signs retain the original zeros, including for six-divisible exponents. The coefficient is the ideal Möbius function times nu(n) chi_n(u)^sign, normalized by D^(-1/2). |
| Raw bound, 11664–11680 | The source uses no slots, Z=H, m=1, r=log_H D, H>=D^(1+c), c>0 fixed. It separates very short columns and bounded scales before applying fixed marked margins. The audit must use L539 instead of assuming the source marked theorem and retain uniform derivative/seminorm control. |
| Statement, 11681–11708 | U,D>=1, q_u comparable to U and every valuation of (u)<=5. H=max(2U,D^(1+c)), P=(H/U)^(1/6); the claimed bound is (H/P)(UD)^epsilon, hence max{U,U^(1/6)D^(5(1+c)/6)}(UD)^epsilon. Bounded nonnegative r in D=U^r gives max{1,(1+5r)/6}+epsilon by a positive c depending on the loss/range; no raw endpoint c=0 is asserted. |
| Scale supremum, 11709–11726 | All 0<D'<=D are included. Empty annular supports terminate the small scales. Differentiation in log D' gives -W/2-yW'. Enlarged-interval Sobolev, logarithmically many intervals, endpoint enlargement and direct initial-scale bounds are explicitly used. |
| Supply, 11727–11731 | Multipliers are ALL good ideals a with q_a<=P, not primes or only squarefree a. The asserted lower count is c_S P; bounded P uses the unit ideal and large P uses positive-density ideal counting after fixed exclusions. The nomination's prime-supply concern is superseded by this ideal-count obligation. No prime-in-ray-class input is needed here. |
| Zeros, 11732–11751 | Separate the part of squarefree n supported on rad(a). The source identity has divisor coefficient mu(d) psi_u(d) q_d^(-1/2), scale D/q_d and row u a^6; the remaining column is coprime to a. Shared primes of u and a are explicitly covered. The divisor mass and its power loss must be checked without deleting a zero or adding (u,a)=1. |
| Fibres, 11752–11759 | The source claims injectivity of (u,a) to u a^6: valuations modulo six recover the row ideal; quotients recover a; its primary representative then determines the row element/unit. It encloses image rows in one fixed multiple of the H-ball. |
| Closing losses, 11760–11770 | Average over multiplier ideals, use the all-row scale supremum and choose preliminary divisor/power losses before the final epsilon. This is the claimed H/P mechanism, not a separately assumed estimate. |
| Row tests, 11771–11788 | Tests are W(y)y^(-sigma_u+i t_u), sigma_u in one fixed compact interval and |t_u|<=T_1. Parameter Sobolev uses enlarged boxes, sums nonnegative row moments before parameter integration and costs a fixed polynomial (1+T_1)^A. The later height-scale exponent is chosen after A. Arbitrary row-dependent prime coefficients remain forbidden. |

The common majorant for the last clause is specified by
`eq:parameter-sobolev` (1056–1066); its proof (1141–1154) uses first
derivatives in each parameter, enlarged unit boxes, nonnegative row sums
and a height cover. This is sufficient source coverage to test a common
bound, not permission to apply Minkowski to separately chosen row measures.
Fixed support and finite seminorm/polynomial-height uniformity must survive
scale and parameter derivatives. Primitive fixed-S ideal/divisor counting
remains an explicit contract, alongside L539's inherited contracts.

## Known overlap and limits

Earlier selection-measure assessments and L534 use amplification as a
contract; L539 explicitly excludes its audit. No matching local proof or
recorded failure was located. These are scoped searches, not novelty evidence.

Yuanda Xu and Hejian Sang, *A sharp lower bound for the sextic large sieve*,
[arXiv:2610.17675v1](https://arxiv.org/html/2610.17675v1), definition (1.1),
Theorem 1.1 and Corollary 1.2 were inspected. For fixed exclusions containing
the primes above 6, their squared operator norm has squarefree ideal rows
and columns with arbitrary column coefficients. For 0<delta<3/11 and
B^(16/11+delta)<=A<=B^(2-delta), they claim the lower bound
(AB)^(-epsilon) A^(5/6) B^(1/3). The balanced corollary is full-cutoff
X^(17/16-epsilon), not a balanced dyadic assertion. This is theorem-level
comparison, not an audited proof or local theorem import. It warns against
generic coefficient substitution; an operator-norm lower bound neither
supplies nor refutes the fixed Möbius-vector upper bound. Their citation to
de Faveri's generic upper bound was seen; its primary theorem/proof was not
inspected and is not used.

The [teal-sea amplification note](https://zeta.teal-sea.com/read/hunts/below_seven_eighths/amplification/LOSS_MAP.html),
compiled October 30, revision 40800649, was screened at its introduction,
source/version qualifications and summary. It declares unreviewed lane
output and uses a different 16,677-line manuscript snapshot. It is only an
overlap lead: no enumeration, LP certificate, optimality or conditional
zero assertion from it is used. Coefficient-transfer and Kubota-mean search
hits remain unread leads. Full matching Mathlib coverage was not checked;
generic calculus support would not certify the arithmetic/import closure.

## Gate and bounded continuation

The unchanged TARGET now has adequate coverage for one separate conditional
reproduction audit with essential input L539. Retain its inherited L538
arithmetic/support/witness/fibre-count/principal-tail/adjustable-uniformity
contracts and the primitive fixed-S ideal/divisor counts above. Do not assume
raw-moment, the scale supremum, amplification or rowwise-test conclusions.
Continue if every source branch checks and the claimed maximum/exponent
follows with a common Sobolev bound and fixed polynomial height order.
Narrow or stop on unsupported ideal supply, extra collisions, a lost zero,
invalid small-scale enclosure or a row-dependent measure substitution.
This could close a conditional input behind L533/L534; primitive arithmetic,
other moments, complete import closure and actual-Xi positivity remain open.

The earlier REVIEW_REQUIRED nomination is preserved by its prior history:
only an adjacent statement had been encountered during initialization.
This review newly covers the proof and corrects the prime-supply concern.
No lemma or mathematical script was written and no application was proved.
