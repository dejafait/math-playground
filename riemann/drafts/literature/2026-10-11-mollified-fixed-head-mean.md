# Complete fixed-response-head mollified mean: source comparison

TARGET: Assess source coverage for a constant-scale asymptotic of the complete fixed-response-head mean H^(-1) integral_[H,2H] d_N(t)|P_H(t)|^2 dt.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused step 58, audited L395, L390, L381 Section 4, L391 jet/connector passages and the L394 stop; bounded exact-statistic, fixed-twist and same-sign/unbalanced mollifier queries found no inspected theorem for the complete mean. The cross-mollifier lead was followed to its primary statement and relevant proof cases.
SOURCE_EVIDENCE: Reused Bui–Hall arXiv:2304.05178v1 Proposition 1 and (6)–(8); directly read Young, Arch. Math. 95 (2010), 539–548, (2.1)–(2.3), Lemma 5 with both off-diagonal cases, Lemmas 6–7 and (6.1)–(6.4), Section 7; Bui–Conrey–Young, Acta Arith. 150 (2011), 35–64, (2.3), Theorem 3.2, Lemma 4.1 with full proof, and Lemma 5.1 through (5.7); Bourgain arXiv:1408.5794v2 Theorem 5 (0.5).
COMPARISON: Young covers balanced growing twists but its evaluated mollifier has no extra response head; Bui–Conrey–Young supplies a uniform same-height product approximation, while its evaluated cross moment has different coefficients, cutoff and polynomial vanishing. These tools support a narrower carrier diagonal-reduction attempt, not an imported complete coefficient or a negligible carrier.
GAP: Balanced finite-prime arithmetic, the complete carrier's sharp growing-weight diagonal reduction and limiting coefficient, and a signed constant-scale asymptotic remain unproved; only the independently testable carrier reduction is selected for specialization.
REASON: Essential primary tools are accessible for a bounded carrier attempt; select its explicit diagonal with o(1) error before asking for either limiting coefficient or a positive complete mean. Do not reprove the source theorems or invoke the changed cross-mollifier theorem.
LITERATURE_REASON: The new target inserts fixed response twists and the complete carrier into a growing-mollifier signed mean; these essential hypotheses and constant-scale errors were expressly excluded from the prior ready scalar target.

SCOPE: Fixed N, L395's exponent 1/100 and polynomial u^2; source comparison of both terms of d_N. SPECIALIZE authorizes only the separately recorded sharp carrier diagonal-reduction continuation, not the complete limiting mean.

## Scope reviewed

Use exactly L395's P_H, exponent 1/100, polynomial u^2 and normalized
ordinary jets, with N a fixed positive integer as H tends to infinity.
The target includes both terms of d_N from L390. The review must allow
a nonzero carrier contribution: o(1) negligibility is not a premise.
Do not take N growing with H or replace signed endpoint errors by
nonnegative bracketing. Seek an explicit complete fixed-N coefficient
with an o(1) normalized error, or identify precisely what coverage fails.
No coefficient, asymptotic or sign is asserted in this assessment.

Essential local inputs: audited L395 and L390 for definitions and transfer;
L391's signed-carrier tools and L381's same-height contour argument are
potential tools, not automatic theorems about this changed growing weight.
Their needed ranges were read after reusing the step 58 comparison.
The primary leads and exact source sections are recorded there, including
[Young's paper](https://www.math.ntnu.no/emner/MA3001/2020v/2022v_MA3004/Young.pdf)
and [Bui–Hall Proposition 1](https://arxiv.org/html/2304.05178v1#S3).
No essential unread theorem is silently imported from those leads.

Main gap: global actual-theta mixed positivity. A complete coefficient
could test an arithmetic weight for positive physical discriminant values;
it would not establish RH or global mixed positivity. L395 already supplies
the absolute comparisons needed for a subsequent controlled response-head
limit, but neither the signed limit nor a positive margin is known.
Continue only if primary hypotheses cover a concrete fixed-N calculation
of the complete mean and its required error. If only the balanced term is
covered, record the carrier as an independent missing obligation; do not
discard it using a bound that is merely O(1) at this scale. A persistent
source blocker calls for a different independently testable target.

Keep the fixed-weight negative result L394 and L390's stopped coarse
absolute contour certificate. Neither gives the signed value here.
No RH, simplicity, disjointness, phase independence or eventual D sign is
available. Total L367 margin, actual common-zero upper counts, low-index
and above-forty signs, and endpoint arithmetic margins remain unresolved.
Matching Mathlib coverage is not checked. The proposed continuation below
receives separate approval next turn; no mathematical work is performed here.

## Completed source review — 2026-10-11, step 62

This is LITERATURE / KNOWN_IMPORTED / EXPLORATION. The new evidence is
the inspected same-height approximation and the cross-mollifier hypothesis
mismatch. No new lemma, diagonal identity, asymptotic, sign or claim beyond
the checked literature is established. The entire original mean remains a
target; narrowing the next attempt does not replace it by its balanced part.

### Balanced coverage

Young's [paper](https://www.math.ntnu.no/emner/MA3001/2020v/2022v_MA3004/Young.pdf),
pp. 540–547, permits complex shifts O(1/log T), positive integer twists
with hk<=T^(2 theta), theta<1/2, and smooth weights satisfying
(2.1)–(2.3): values between zero and one, support [T/4,2T], derivatives
O_j((T/log T)^(-j)). Lemma 5 retains both functional-equation diagonals
and an arbitrarily small power error, uniformly in its twist range.
Its proof treats both unequal orderings and uses product decay plus
integration by parts. The Cauchy argument after (3.4) handles normalized
fixed-order shift derivatives. Section 6 cancels the shifted s-pole;
Lemma 7 uses the standard zero-free region and reciprocal-zeta bound,
not RH. Section 7 evaluates its unmodified arithmetic factor.

For the proposed application one must check every combined response and
mollifier twist against that range, sum the uniform errors, and evaluate
the changed collision arithmetic. The fixed response indices introduce
prime conditions absent from Young's evaluated scalar formula. Both
diagonals and the removable shift singularity must be retained. These are
future specialization obligations, not completed deductions. A fast gamma
carrier is not an admissible weight. Signed sharp endpoint removal needs
absolute control; scalar nonnegative bracketing alone is insufficient.

### Same-height coverage and cross-mollifier mismatch

Bui–Conrey–Young, [*More than 41% of the zeros of the zeta function are
on the critical line*](https://aimath.org/~kaur/publications/69.pdf),
Acta Arith. 150 (2011), 35–64, Lemma 4.1, pp. 42–43, states, for
log^2 T<=|t|<=2T and complex alpha,beta=O(1/log T),

    zeta(1/2+alpha+it) zeta(1/2-beta+it)
      = sum_(l>=1) sigma_(alpha,-beta)(l) l^(-1/2-it)
                      exp(-l/T^3) + O(T^(-1+epsilon)),
    sigma_(alpha,-beta)(l)=sum_(ab=l) a^(-alpha)b^beta.

The proof retains both moving zeta poles when shifting the gamma-Mellin
line; their residues have exponential decay, and the remaining line is
bounded before choosing the cutoff. Coincident shifts are included in
the stated uniform formula. Theorem 3.2 and Lemma 5.1, pp. 40, 46–47,
evaluate a different cross moment: (2.3) uses mu_2, product support and
P_2 vanishing through its second derivative. Its proof exposes a genuine
same-height diagonal. Neither that theorem nor its coefficient is imported
for the present mu-times-mu square cutoff and u^2 polynomial.

This pointwise product formula is a usable known tool without the
cross-mollifier restrictions. Its use with the present finite weight still
requires a complete ordinary-jet conversion, justified differentiation on
small complex-shift contours, summed approximation errors, and signed
off-diagonal and endpoint estimates. The long cutoff is not permission
to sum its absolute off-diagonal coefficients on the critical line.
Only a future calculation can establish the actual collision sum or its
limiting value. In particular no o(1) carrier premise is supplied.

For a possible holomorphic height-contour treatment, reuse L381's
Section 4 and L391's exact ordinary-jet/connector tools. Directly checked
[Bourgain v2 Theorem 5 (0.5), p. 2](https://arxiv.org/pdf/1408.5794v2#page=2):
unconditionally |zeta(1/2+it)|<<_epsilon |t|^(13/84+epsilon).
Fixed-strip interpolation, Cauchy and absolute right-line series are
already supporting tools in L391. Inserting the growing mollifier changes
their bounds; its holomorphic extension must be written explicitly and
both connectors estimated again. The modified-Gonek theorem in L391 has
fixed series/q constants and does not by itself authorize growing twists.

### Search record, duplicate check and next test

New queries: `zeta mollified second moment same sign zeta squared mollifier
twisted moment`; `mollified twisted second moment fixed rational twist
asymptotic Mobius polynomial`; `"Hardy" "discriminant" "mollifier"`;
`"zeta" "same sign" "mollifier"`; `"zeta" "unbalanced" "second moment"`;
`Bui Conrey Young more than 41 percent zeros lemma 2.3 I12 mollifier zeta`.
The Robles–Roy–Zaharescu author PDF's Proposition 2.1 points to the
cross-mollifier result; the originating statement and essential averaging
cases were then inspected as above. The 2025 *Short mollifiers* paper is
an unread optimization lead, not a theorem about this statistic; no input
is assumed from it. BCR's longer balanced moment scope is reused from
step 58 and does not settle the carrier. No novelty is inferred from
the bounded search. The specific local records checked contain no ready
complete mollified-mean evaluation or carrier diagonal reduction.

The chosen intermediate target is an explicit H-dependent finite diagonal
for the entire fixed-N carrier with normalized error o(1), including both
sharp endpoints. It may leave its own limiting coefficient and the balanced
coefficient unresolved. See the separate proposed
[specialization assessment](2026-10-11-mollified-carrier-diagonal.md).
Continue if the actual growing-weight ordinary jets and all summed errors
meet that threshold; abandon this certificate if a retained connector or
off-diagonal bound stays order one or larger after normalization. Preserve
the full carrier in either outcome. Audited L395 then supplies the physical
and head-tail transfer for a later complete coefficient test. No positive
witness, eventual discriminant sign or RH consequence follows now.
