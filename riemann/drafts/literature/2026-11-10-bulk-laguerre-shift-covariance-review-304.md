# Bulk Laguerre shift covariance — completed source comparison

TARGET: Assess arXiv:1707.01315's shift-averaged von Mangoldt correlation results for the signed quadratic form of the exact compensated bulk Laguerre sum B_n, retaining exceptional shifts, weights, endpoints and the compensator.
CHECKED: 2026-11-10
DECISION: EXPLORE
SEARCH_EVIDENCE: Step305 inspected the named primary lead after reusing reviews231/241/243, L981/L982/L984 definitions and stops233/235/243/302; searched exact Laguerre/correlation and weighted partial-summation combinations. No inspected theorem matches the complete weighted centered square; other hits remain unread leads, not evidence of absence or novelty.
SOURCE_EVIDENCE: Matomäki–Radziwiłł–Tao, arXiv1707.01315v3 (18 February2019), https://arxiv.org/pdf/1707.01315v3 : Theorem1.3(i), p8; Proposition3.1/Corollary3.2 with proofs, pp32–34; Propositions3.3(i)/3.4, theorem reduction/Remark3.5, pp35–37; Proposition4.1 and the Lambda major-arc proof through(66)–(67), pp37,39–40; Section1/(7), pp2–3, and footnotes4/6, pp4–5. HTML cross-check https://arxiv.org/html/1707.01315v3 . Reused review231 variance and review241 Laguerre contracts without new browsing.
COMPARISON: The source genuinely controls Lambda-Lambda correlations, but for most shifts with fixed logarithmic savings and singular-series main term. Its arbitrary-sequence corollary still assumes major/minor-arc estimates. Neither statement imports the growing weighted, fully centered B_n square; exceptional shifts, long/cross-block pairs, weight uniformity and continuum compensation remain unpaid.
GAP: No inspected estimate controls the complete signed weighted covariance with all residuals at B_n^2<=D_epsilon*exp(epsilon*n) for every epsilon>0. This is a scope limit of direct import, not a lower bound or an impossibility theorem for covariance methods.
REASON: Park direct Theorem1.3(i)-to-B_n^2 payment on the newly inspected hypotheses and proof cases. EXPLORE records the bounded assessment; it does not approve a weighted specialization or repeat the old absolute-envelope tests. A separate deterministic reconstruction question is nominated for review, without deriving it.
LITERATURE_REASON: The startup REVIEW_REQUIRED target named this essential unread primary correlation source; its actual shift, exceptional-set and centering hypotheses were absent from the ready coefficient, variance and Vaughan assessments.
SCOPE: Completed literature-only comparison of this lead with the exact B_n. No new square identity, weighted specialization, lemma or mathematical script. The source's deeper Dirichlet-polynomial proofs are not independently audited or imported as new weighted estimates.

The nomination below is preserved as historical scope. Step305's completed
comparison at the end supersedes its unread/missing-coverage language.

The main gap remains L030-L032/C032a actual-Xi positivity and
L966/L968 signed forcing, with L984(H) unpaid. For this nomination
use exactly review241's real kernel and bulk statistic:

    K_n(u)=(n-1)^(-1)*sum_(k=2)^n L_(k-1)^(1)(u), n>=2,
    B_n=sum_(exp(n)<m<=exp(2n)) Lambda(m)*K_n(log m)/m
                               -integral_n^(2n) K_n(u)du.

All prime powers and the full upper endpoint are retained. This
definition, not a new representation or lemma, fixes the target.
The proposed mechanism is to keep the two-point correlations in
a prospective expansion of the real square B_n^2, rather than
replace each prime error or formal factor by its absolute norm.
No such expansion, source specialization or estimate is derived
in step304.

A sufficient downstream threshold is, for every epsilon>0, a
finite D_epsilon with B_n^2<=D_epsilon*exp(epsilon*n) for every
n>=2. This two-sided bulk control would suffice for the one-sided
bulk requirement in review241. It would not settle the full
average a_n of L984(H): log m<=n, 2n<log m<=log X_n and their
compensators remain independent gaps. L981 controls only its
remote tail, and L982 only fixed-index identification. No RH
assumption, zero simplicity or prime-only replacement is allowed.

The next source review must first identify the actual statements
of arXiv1707.01315, checking whether they concern Lambda against
Lambda, their main term, permitted shift and summation ranges,
exceptional sets, uniformity and weight restrictions. Do not
infer these from this nomination's descriptive target or the old
search hit. Inspect only the proof cases essential to those
features before larger extracts. Then compare the source with
the proposed exact square, which would require a diagonal,
off-diagonal, prime-integral and integral-integral accounting.
A theorem for most shifts alone is insufficient without its
quantitative exceptional contribution; a logarithmic saving
alone is not the stated exponential-in-n threshold. Do not
derive the weighted specialization during the source turn.

Continue only if coverage supports a precise, independently
testable signed-covariance specialization with every residual
cost stated. If the theorem concerns a different correlation,
requires RH, has inadequate ranges or retains an unremovable
loss under its stated contract, record that exact scope limit
and park this import. An upper-bound loss is not a lower bound
for B_n. An unanswered source search is EXPLORATION, not
automatic negative evidence. New mathematical work requires a
separately saved and approved assessment.

The local duplicate screen is bounded, not an originality claim.
Review231 covers increment variance, review243 centered Vaughan
and an explicitly unread correlation lead, review241 derivative
phase tools, stop233 a false universal lobe sign, and stop235
automatic first-degree averaging. Stop302 concerns unit formal
coefficients versus arithmetic norms in the Diamond-Steinig
interface. None is being erased or presented as a blanket ban.
The next review should verify whether the correlation lead is
materially distinct at theorem level before nominating research.

Essential continuation inputs are L984(H)'s exact target,
review241's B_n, L981/L982's normalization and endpoint
conventions, and the named source/failure comparisons. C999a is
now audited but is not a premise for a covariance bound. Actual
signed correlations, all growing-order uniformity, complete
centering, both omitted ranges and regulator/infinite-zero
control remain unproved. No cross-notebook input. Full matching
Mathlib coverage is unchecked and unknown.

This nominates literature_comparison, standard/high. A genuinely
new covariance mechanism at the central arithmetic gap could
later justify proof_attempt/creative with a bounded test, but
only after source coverage and a concrete residual expression
exist. Missing coverage is the present blocker; no creative
classification or ready mathematical continuation is claimed.

## Completed comparison — step305, 10 November2026

Primary source: Kaisa Matomäki, Maksym Radziwiłł and Terence Tao,
*Correlations of the von Mangoldt and higher divisor functions I.
Long shift ranges*, arXiv:1707.01315v3, 18 February2019,
Proc. London Math. Soc.118 (2019), 284–350,
https://arxiv.org/pdf/1707.01315v3 . Page numbers here are the printed
preprint pages, not journal pagination. No source-access blocker remains.

### Primary contract and essential cases

Theorem1.3(i): fix A>0 and 0<delta<1/2; X>=2,
X^(8/33+delta)<=H<=X^(1-delta), 0<=h0<=X^(1-delta). Then

    sum_(X<r<=2X) Lambda(r)Lambda(r+h)
        = S(h)X+O_(A,delta)(X*log(X)^(-A))

outside O_(A,delta)(H*log(X)^(-A)) shifts |h-h0|<=H.
For nonzero h, (7) defines S(h): zero for odd h, and
2*Pi_2*product_(p|h,p>2)(p-1)/(p-2) for even h,
Pi_2=product_(p>2)(1-1/(p-1)^2).

Corollary3.2 assumes finite complex sequences, H>=1,
eta,F,G,X>0, measurable arcs and integer h0: squared norms
O(F^2 X), O(G^2 X), major-arc error O(eta FGX) outside
O(eta H) shifts, and every minor-arc local energy
O(eta^6 F^2 X). Its conclusion retains O(eta H) exceptions.

Read the Poisson-localization/Cauchy/Chebyshev proof,
both rational-offset cases in Proposition3.4 and their theorem
reduction. Read the overlap and Ramanujan-series major-arc case
(66)–(67). Remark3.5 only sketches exceptional-shift sieve disposal.
Proposition4.1 notes ineffective constants. Footnote6 points to
extensions at H comparable to X; those references remain unread.

These are cited contracts, not reproofs. No RH, simplicity or
effective constant is added. The diagonal is not an established
nonzero-shift asymptotic. The source's arbitrary fixed A must not
be promoted to A depending on the Laguerre degree with uniform constants.

### Comparison with the exact target

The main gap is still L030–L032/C032a actual-Xi positivity and
L966/L968 signed forcing. L984(H) is unpaid. The intermediate
target remains the exact B_n above and the sufficient two-sided
threshold B_n^2<=D_epsilon*exp(epsilon*n), for every epsilon>0
with D_epsilon independent of n. Its plausible use is payment of
only the bulk part of L984(H); both logarithmic complements remain.

The following are application obligations, not newly derived
identities or bounds:

| Piece of the proposed square | Unresolved obligation |
| --- | --- |
| Diagonal | Retain the actual squared Lambda weights; h=0 may be exceptional and S(0) is not defined by the nonzero-shift product. |
| Nonzero pairs in admissible shift ranges | Supply a theorem for K_n(log r)K_n(log(r+h))/(r(r+h)), with degree-uniform costs. A dyadic unweighted asymptotic does not itself provide weighted partial sums. |
| Exceptional shifts | Bound their weighted contribution, including how exceptional sets change under truncation. A count of exceptions is not a signed error estimate. Remark3.5 is not a proof for this new weight. |
| Other pairs | Account for all long shifts and cross-block pairs throughout (exp(n),exp(2n)], including sharp terminal pieces. The stated sublinear shift contract alone does not do this; footnote6 prevents interpreting that contract as a universal barrier. |
| Arithmetic main term | Retain S(h); it is not the constant1 centering in B_n. No signed weighted singular-series cancellation has been proved here. |
| Prime-integral and integral-integral terms | Retain the original integral_n^(2n) K_n(u)du and every endpoint term. Pair correlations do not supply the separate single-prime centering estimates. |

All prime powers and the full upper endpoint remain mandatory.
No smoothing, exceptional-set averaging in n, weight-norm estimate,
square expansion or summation-by-parts specialization is performed
in this literature turn. In particular, no residual is silently set
to zero. The fixed logarithmic source errors, without an additional
signed reconstruction and rate comparison, establish none of the
stated every-epsilon exponential threshold. This is not a proof
that those upper errors are attained by B_n, or that every possible
adaptation of the source fails. L985's recorded positive-rate loss
is comparison evidence only; it is not newly rederived here.

Corollary3.2 is useful as a conditional architecture, but inserting
the weighted prime sequence would require proving its arithmetic
arc hypotheses anew. Such insertion is not a licensed known-result
import. Likewise, the positivity of a real square does not sign
its off-diagonal terms or pay compensation. No independence of
prime phases or positive-measure model for actual Xi is assumed.

### Search, decision and continuation

Queries: `"1707.01315" weighted correlations exceptional shifts
Theorem 1.3 Laguerre`, `"Laguerre" "Correlations of the von
Mangoldt"`, `"1707.01315" weighted "partial summation"`, and
`site:arxiv.org "von Mangoldt" "correlations" "weights" "Laguerre"`.
Only the named primary paper supports the source comparison.
Search hits suggesting later correlation papers and divisor-sum
Laguerre occurrences were not read and supply no theorem here.
No search failure certifies originality or nonexistence.

Reused review231's variance scope, review241's exact observable,
review243's centered-Vaughan comparison and stops233/235/243/302.
The finite-quartet mechanism in review245 is a separate existing
route, not being renamed. A narrow check of review200 distinguishes
its complex-zero Fejer obstruction from the real finite arithmetic
reconstruction question below. C999a remains an audited formal
coefficient result, with no arithmetic norm premise imported.

Decision: park direct payment by Theorem1.3(i); the continuation test
requires an applicable signed weighted estimate and complete residual
accounting, and this source does not meet it. This is new NEGATIVE
source evidence changing the import decision, not new mathematics
beyond the source. No lemma, script, DAG or PROOF.md change is needed.
Full matching Mathlib coverage is unchecked and unknown.

The [separate nomination](2026-11-10-bulk-laguerre-short-shift-reconstruction-review-305.md)
asks whether the deterministic kernel can be reconstructed from
short shifts with a controllable remainder before any prime theorem
is applied. This is a different, independently testable target;
neither a reconstruction nor a remainder estimate is asserted.
It is REVIEW_REQUIRED, not approval to calculate. Missing kernel
coverage and a precise signed residual block creative routing now;
the next review must justify a bounded central mechanism or abandon
that reconstruction, without repeating this source comparison.

Essential continuation inputs: L984(H), review241's exact B_n,
L981/L982 endpoint conventions and this completed source scope;
review200 and stops233/235/243/302 for contrasts. Signed arithmetic
covariance, exceptional shifts, growing degree, both complements,
full compensation and regulator/infinite-zero control remain open.
No cross-notebook input or mathematical exploration budget reset.

