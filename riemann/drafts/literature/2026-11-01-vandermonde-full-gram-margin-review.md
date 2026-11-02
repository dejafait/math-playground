# Growing-N signed spectral margin: completed bounded source comparison

TARGET: Test a full-arithmetic Vandermonde spectral-lift bound Q_{N,L}(a)>=(1/2+epsilon)Gamma for some fixed epsilon>0, all complex a, N=floor(exp(L/100)), and all sufficiently large L.
CHECKED: 2026-11-01
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused ready scalar/differential HCIZ, collective arithmetic and full-Gram energy assessments; completed the bounded signed-margin searches below. No matching coefficient-uniform full-B_N lower bound was identified; failed searches establish neither novelty nor absence.
SOURCE_EVIDENCE: Reused McSwiggen arXiv:1712.03995v3 (2)/Theorem 1/Section 3.4 and assessed Hughes--Young arithmetic cases; retrieved Hughes--Young arXiv:0709.2345v2 Theorem 1.1/(16)--(17) and holomorphy remark; inspected Durkan--Page arXiv:2606.27323v2 Section 1.2/(1.6), Theorem 15 and Section 5.1's arithmetic replacement; inspected Bui--Hall arXiv:2304.05178v1 Proposition 2 and initial proof/Section 5 Cauchy passage.
COMPARISON: Moment and differential representations have the coefficient restrictions detailed below; no inspected theorem provides this signed half-margin. L632's fixed-N identity and L630's first-jet bound do not supply full growing-N domination. Earlier stops remain mechanism-specific.
GAP: Prove or obstruct the exact signed lower bound with full tails, differentiated C_N, arbitrary complex vectors and an L-independent reserve above Gamma/2; justify the all-N differential construction and any uniform interchange actually used.
REASON: Essential representation and arithmetic coverage is available; the signed comparison is missing mathematics, not an essential unread theorem. Admit one bounded test of the unchanged target without assuming a positive lift. This literature turn neither invokes that test nor establishes its inequality.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED target changes a fixed-N identity into a uniform growing-N inequality; compare this changed scope while reusing adequate scalar HCIZ coverage.
SCOPE: Proposed c=(0,1) leading functional Q_{N,L}(a)=5040 Re S F_{N,L}(0;a), with L629's complete six-term F and full L623 Gamma; arbitrary fixed complex coefficients, N=floor(exp(L/100)), all sufficiently large L, and one absolute epsilon>0. Neither other observers nor pointwise Xi signs are included.
COVERED_TARGET: Test a full-arithmetic Vandermonde spectral-lift bound Q_{N,L}(a)>=(1/2+epsilon)Gamma for some fixed epsilon>0, all complex a, N=floor(exp(L/100)), and all sufficiently large L.

## Reuse and precise relevance

Reuse the completed
[fixed-N differential assessment](2026-11-01-vandermonde-spectral-derivative-hciz-review.md)
and its primary-source evidence. The full N=2 construction is canonical
in L632; its exact test is at
`scripts/full_gram/spectral_lift_n2_certificate.json`. L631's
multiplicative obstruction is preserved. Scalar HCIZ should not be
searched or proved again merely because N changes in the arithmetic
amplitude; the unitary group in this proposed mechanism remains U(4).

The main gap is still actual-Xi initial signs at unbounded heights
and all-degree mixed positivity. The narrower prospective estimate
would give an averaged c=(0,1) margin, with epsilon leaving room for
L629's qualified O(Gamma/L) error. It would not settle pointwise
signs, other observers, independent input audits, or RH.

## Mathematical continuation and discriminating test

Essential local inputs are L623's full Gram form, L624's full B_N
and fixed-N compact convergence, L629's complete signed prescription,
L631's fixed-N diagnostic and L632's explicit differential construction.
The source comparison must address the signed full arithmetic estimate,
not merely whether an analytic symbol can be inserted into a determinant.
Full tails, all C_N derivatives and arbitrary coefficient vectors must
remain present. No positive extraction, uniform all-N operator bound,
coefficient-independent onset or acceptable loss is assumed.

After separate approval of this newly completed assessment, the required
test is an actual signed quadratic-form
inequality with one epsilon>0 independent of L and a. A formal lift
alone does not pass. Any loss must be compared with Gamma/2 and the
transfer error. An obstruction to the selected estimate must identify
its exact hypothesis or a genuine coefficient direction; a large
absolute upper bound is not a negative direction. Persistently obtaining
only the known unsigned costs would require a materially different
estimate or target. This review neither computes the bound nor
establishes new mathematics. No cross-notebook input is proposed.

## Primary source comparison for the changed scope

### Arithmetic theorem and differentiation

C. P. Hughes and M. P. Young, *The twisted fourth moment of the
Riemann zeta function*, J. reine angew. Math. 641 (2010), 203--236,
[arXiv:0709.2345v2, Theorem 1.1/(16)--(17), pp. 4--5](https://arxiv.org/pdf/0709.2345v2#page=4).
Retrieved the complete statement and holomorphy remark. Conditions:
coprime h,k, hk<=T^(2/11-eta), complex shifts O(1/log T), smooth
nonnegative weight supported in [T/2,4T], derivatives O_j(T0^(-j)),
and T^(1/2+eta)<<T0<<T. The six-term main integral has 1/sqrt(hk);
the raw error is O(T^(3/4+eta)(hk)^(7/8)(T/T0)^(9/4)).
Holomorphy concerns the complete sum. Reuse the inspected prime-power
cases, both orientations and application comparison in
[collective arithmetic coverage](2026-11-01-collective-arithmetic-signed-spectrum.md).
The proposed length lies inside the twist range. No sign of the
extracted sum or improved error is supplied; no reproof is needed.

### Amplified moment with polynomial coefficients

B. Durkan and T. Page, *Amplified moments of the Riemann zeta
function*, [arXiv:2606.27323v2, 5 August 2026, Section 1.2/(1.6),
Theorem 15 and Section 5.1](https://arxiv.org/html/2606.27323v2#S5.SS1).
Read the full theorem, shift-continuation qualification and relevant
arithmetic replacement in its proof. The amplifier uses a fixed real
profile P(log(y/n)/log y), power |A|^(2k), and y=T^vartheta_k,
vartheta_k<1/(4k). Shifts are O(1/log T), continued holomorphically
at collisions; weight conditions are in Lemma 4. The error is
O(T(log T)^((k+2)^2-1)). Section 5.1 replaces its aggregated
analytic factor by its value at zero after Mellin substitution.
That is not a uniform replacement of individual L624 factors or a
Gamma-relative signed estimate. General coefficients are proposed
as a possible extension. Interpolating arbitrary vectors by polynomials
would require unprovided degree/coefficient uniformity. No extension
or complete proof audit is imported.

### Mollified derivative formula

H. M. Bui and R. R. Hall, *On the derivatives of Hardy's function Z(t)*,
[arXiv:2304.05178v1, 11 April 2023, Proposition 2, pp. 9--10;
Section 5, pp. 14--15](https://arxiv.org/pdf/2304.05178#page=9).
Read the full proposition, initial six-term/annulus proof passage and
Cauchy differentiation. Its Mobius-polynomial mollifier occurs as
|M|^4, with P(0)=P'(0)=0 and length T^vartheta, vartheta<1/8;
the shift-uniform error is O_eta(T(log T)^(-1+eta)). Its holomorphic
error control permits the stated fixed derivatives. These are not
arbitrary coefficients in the present quadratic amplifier. The integral
and differentiated-error method assert no such signed coercivity.
Reuse the earlier BBLR comparison; no universal sign, norm-relative
error or mollifier theorem is newly imported.

### Unchanged differential and norm coverage

Reuse the [spectral-derivative assessment](2026-11-01-vandermonde-spectral-derivative-hciz-review.md)
for exact McSwiggen/Miglioli/Eynard hypotheses and inspected proof cases,
and the [Gram/simplex assessment](2026-11-01-signed-functional-gram-simplex-review.md)
for HG/Andreief and filtered positivity. Pair symmetry alone does not
make Miglioli's polynomial symbol conjugation-invariant. L632 instead
uses the multiplied scalar HCIZ identity. Neither its successful N=2
specialization nor these identities supplies a positivity-preserving
all-N arithmetic operator. Arithmetic N grows while the orbit remains
U(4); large-matrix HCIZ asymptotics do not by themselves address this
limit. No reproof of known identities is warranted.

Reuse [full-Gram energy coverage](2026-11-01-full-gram-log-degree-energy.md)
for weighted Bernstein/Dirichlet-series multiplier scope mismatches.
The actual measure, norm and uniform constants must be checked in any
application. No source examined there supplies the signed reserve.
Full matching Mathlib coverage is not checked and remains unknown;
supporting kernel identities are not a formalization of TARGET.

## Searches, duplicates and recorded failures

New queries actually submitted:

- `"twisted fourth moment" "derivatives" positivity Dirichlet polynomial`
- `"Harish-Chandra" "differential" "positivity" orbital integral`
- `"Durkan" "Page" "twisted fourth moment"`
- `"twisted fourth moment" "positive definite"`
- `"twisted fourth moment" "lower bound" arbitrary coefficients`
- `"Hardy" "Laguerre" "Dirichlet polynomial" positivity fourth moment`
- `"Vandermonde" "twisted fourth moment"`
- `"Hughes" "Young" "Gram" positivity`
- `"HCIZ" "arithmetic" "positivity"`

Filtered-positivity papers 36/41 were rediscovered; reuse their inspected
untwisted/fixed-positive-order-ratio limitations from collective
arithmetic coverage. No new applicability claim follows. Random-matrix
Schur-twist and unbounded-shift moment hits remain uninspected leads,
not premises or essential sources for this test. Search snippets and
secondary summaries were not accepted as theorem evidence. Shell
retrieval failed DNS, but the primary passages were accessible through
the web tool; no persistent essential source blocker remains.

Read L623/L624's stated full-space identities and convergence,
L629's full prescription, L631/L632's constructions and diagnostic,
and the relevant ready assessments. Preserved the
[multiplicative stop](../../ATTEMPTS/2026-11-01-scaled-multiplicative-grassmannian-insertion-stop.md),
[absolute-Cauchy stop](../../ATTEMPTS/2026-11-01-full-gram-absolute-cauchy-budget-inconclusive.md),
[termwise stop](../../ATTEMPTS/2026-11-01-full-gram-signed-jet-budget-inconclusive.md),
and L623/L624's freezing/prefix obstructions. None supplies a negative
direction for TARGET. L630's scalar first-jet result leaves the joint
functional open. The differential lift is a specific new input relative
to the stopped multiplicative/absolute mechanisms, not a reason to
repeat their majorants. Local input audits remain separate obligations.

This is a completed source comparison with EXPLORE coverage for one
bounded mathematical test. No bound, new lemma, mathematical script,
proof audit or RH candidate was produced. PROOF.md and DAG.md retain
their invocation-start content. Later mathematical work may use this
assessment once its separate approval has occurred; no further broad
search is needed with unchanged assumptions.
