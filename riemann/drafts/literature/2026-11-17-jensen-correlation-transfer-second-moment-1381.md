# Actual-Jensen correlation transfer — source review1382

TARGET: Test transfer of C019l's negative shifted correlation to C019j's normalized actual Jensen values using a uniform O(X*log X) band second moment for C019k's S_d and an o(B*log X) product error.
CHECKED: 2026-11-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1382 searched ordinary and variable-coefficient Dirichlet-polynomial mean values, moving-heat mean squares and actual-Jensen heat correlations; reused comparisons1372/1376/1377 and checked exact local second-moment/product-error mentions plus stops1345/1355/559. No inspected theorem states the complete saved target; no novelty claim follows.
SOURCE_EVIDENCE: https://arxiv.org/html/0803.1141v2#A Appendix A.1-A.3 and Section2/(2.4)-(2.6) were inspected for theorem hypotheses and both proof channels; Polymath1904.12438v2 Theorem1.3/Corollary6.5 coverage is reused through C019k/audit1376. Montgomery-Vaughan1974 pp74-75,82 were inspected in accessible OCR only, with formula-access limits below; it is not an imported input.
COMPARISON: The known real-product method and its classical integral/sum bounds cover the necessary tools, not the moving-heat square or Jensen product conclusion. Reuse C019l (6)-(21) for the already paid phase, coefficient-variation and entry analysis; the unshifted square and normalized-error application require a separate specialization, rather than a new general moving-heat moment theorem.
GAP: Prove the proposed full-band O(X*log X) real-square bound with actual entries and weights, then bound the actual-Jensen product difference below the existing negative margin at one common onset. Neither estimate is established by this source review.
REASON: The changed square/transfer scope now has essential tool coverage: classical oscillatory estimates, the checked local moving-weight reduction and integral Cauchy-Schwarz. Direct import of an ordinary zeta or fixed-coefficient moment would omit hypotheses; a separate, explicitly qualified specialization is justified.
SCOPE: Exact C019j/C019k/C019l data; integer d tending to infinity; X=Y_-, B=(sqrt(2)-1)*X, h=3*pi/log(X); actual floor and time at every argument; no RH, nonvanishing, simplicity, heat real-zero hypothesis or effective onset.

## Preserved target, still unproved

Use C019j's positive normalization, denoted here by N_d^norm to
distinguish it from C019k's source floor. For Y in [X,sqrt(2)*X], set

\[
 r(Y)=T^2/Y^2,\qquad
 P_d^{\rm act}(Y)=
 \frac{(-1)^d A_d(-r(Y))}{N_d^{\rm norm}(r(Y))}.
\]

The proposed intermediate input is an absolute C such that, eventually,

\[
 \int_X^{\sqrt2X}|S_d(Y)|^2\,dY\leq C X\log X.
\]

The transfer test is whether the existing uniform errors can then pay

\[
 \left|\int_X^{\sqrt2X-h}
 \big(P_d^{\rm act}(Y)P_d^{\rm act}(Y+h)
              -S_d(Y)S_d(Y+h)\big)\,dY\right|
           =o(B\log X).
\]

These remain proposed tests, not conclusions or derivations of this turn.
The prospective mechanism is mean-square control of the factors in the
product error; the previous crude pointwise envelope is not a substitute
for proving the displayed bound. Review1382 below identifies known tools
for a separate moving-weight specialization; it does not assert the
second moment or transfer conclusion.
Preserve this exact target while assessing it; do not perform it during
the source gate or reopen the parked mollified deficit (A).

## Input scope, acceptance test and limitations

Essential local inputs are C019j, C019k and C019l, inheriting L018/L021
conventions. C019j (1) has error O(1/log d), and C019k (3) has error
O(X^(-1/4)); their canonical audits already exist. C019l supplies only
the reference signed mean and its coefficient. Review those results at
their exact hypotheses and use the old assessments for unchanged sources.
There is no need to repeat the completed C019l audit.

Search exact and standard real shifted/second-moment formulations and
local duplicate/failure records before approving the target. Keep both
channels of a squared real sum, floor endpoints and the exact heat time
in the comparison. Existing Kösters and Polymath records are leads for
reuse, not a claimed theorem covering the proposed bound. Full matching
Mathlib coverage remains unchecked.

Continue only if the full product error is smaller than a fixed positive
portion of C019l's B*log X negative margin at one onset. An unpaid
second-moment or error term rejects this proposed transfer proof, not
the correlation theorem or RH. Even a successful transfer would leave
quantitative amplitude margins, disjoint ordered samples, c*sqrt(d)
additional roots and bulk separation unresolved. Actual-Xi all-degree
positivity remains the main gap. Stops1345/1355/559 are preserved.

The nomination was REVIEW_REQUIRED at the start of review1382. This
literature-only review completes that gate for the same exact TARGET;
it neither changes the target nor executes it. SPECIALIZE permits a
subsequent mathematical attempt classified REPRODUCTION, with all
remaining verification obligations below retained.

## Review1382: searches and source comparison

Exact queries included `Montgomery Vaughan mean value theorem Dirichlet
polynomials variable coefficients bounded variation second moment`,
`"heat" "Riemann" "second moment" moving time`,
`"Jensen" "heat" "correlation" polynomial zeta`,
`"de Bruijn" "heat" "mean square" zeta`,
`"Riemann" "heat flow" "mean square" Dirichlet polynomial`, and
`"Riemann-Siegel" "variable coefficients" "mean square"`.
Many exact heat/Jensen hits were irrelevant. Search summaries, unofficial
courses, public notebook mirrors and claimed heat-flow results were not
used as theorem evidence. A fractional Riemann-Siegel remainder lead,
arXiv2610.03728v2, was not inspected and is not needed here. A failed
search is not evidence of novelty or absence of stronger results.

The local search was limited to the named Jensen literature/working/history
files and the exact stop records. No completed full-band square or
actual-Jensen product-transfer proof was located in those paths. C019l's
fixed nonzero shift conclusion does not state an unshifted mean square.
Stop1345 concerns an unpaid exterior Airy contribution, stop1355 concerns
the signs of two fixed Airy endpoints, and history559 records an unpaid
automatic unshifted bulk import. These do not prohibit this particular
moment calculation; their original evidence and parked direct (A) remain.

### Inspected classical input and proof cases

H. Kösters, *On the Occurrence of the Sine Kernel in Connection with the
Shifted Moments of the Riemann zeta function*, arXiv0803.1141v2,
5 September2008, [Appendix A](https://arxiv.org/html/0803.1141v2#A):
A.1 requires monotone F' separated from zero and bounds the integral by
4/epsilon; A.2 requires twice differentiable real F with F'' of one sign
and modulus at least epsilon, giving 8/sqrt(epsilon). A.3 bounds the
sum of 1/(sqrt(m*n)*log(n/m)), 1<=m<n<=M, by O(M*log M).
These reproduce Titchmarsh, second edition, Lemmas4.2,4.4,7.2.
Section2/(2.4)-(2.6) retains conjugated and unconjugated real-product
channels, pair entry endpoints, unequal-index terms and the diagonal.
Its theorem has divisor coefficients and microscopic ordinate shifts;
it does not state the present heat-family square or Jensen transfer.
Those are proof methods and classical inputs, not a matching theorem.
The direct elementary inputs can be cited without reproving them.

The earlier Bettin/Hardy-Z/mollifier comparisons in assessment1376 are
reused, including their printed hypotheses and limitations. No fresh
reading of their full proofs was necessary for this unchanged source
comparison. Polymath's effective approximation and gamma conversion are
already specialized and audited in C019k; no new heat or gamma formula
is imported by this review.

### Nonessential fixed-coefficient lead and access qualification

H.L. Montgomery and R.C. Vaughan, *Hilbert's Inequality*, J.London
Math.Soc.(2)8(1974),73-82,
[author-hosted PDF](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf),
[DOI](https://doi.org/10.1112/jlms/s2-8.1.73).
Read the accessible OCR of Theorem2 and Corollaries2-3, pp74-75,
and the concluding proofs, p82. The proof expands a fixed exponential
polynomial, isolates the diagonal and applies the separated-frequency
bilinear inequality to endpoint terms. This is a useful comparison with
fixed coefficients, not authority for arbitrary moving coefficients.
OCR drops essential displayed formulas; web screenshot requests returned
references without usable page images, and local curl failed DNS.
Accordingly no exact numerical formula from these corollaries is
imported or marked fully verified. This optional lead is parked. Essential
coverage comes from the fully readable Kösters inputs and checked local
reduction, so this access limitation does not block the saved target.

## Approved scope of the separate specialization

The mathematical attempt may use C019l's elementary a_n,f_n,V reduction
and its already checked uniform variation estimates, but must verify
the square on the complete closed band. In particular it must account
for both channels of a squared real sum, equal and unequal indices,
and the actual unshifted entry intervals. It may not simply substitute
h=0 into a conclusion proved only for h=3*pi/log X. An upper bound is
sufficient; a new exact diagonal asymptotic is unnecessary. If an
analytic-half modulus majorant is used instead, its moving coefficients
and entries still need explicit control.

For transfer, C019j(1) and C019k(3) supply uniform normalized additive
errors. Integral Cauchy-Schwarz is the standard named theorem for
controlling their cross terms after the proposed square estimate is
proved. Its hypotheses require square-integrable factors on the actual
integration domain. Both translated arguments must remain inside the
original band, every cross term and the error-error product must be
paid, and all estimates must hold at one onset. No product bound or
new error rate has been derived in this literature step.

Full matching Mathlib coverage remains unchecked. Supporting finite-sum,
integral Cauchy-Schwarz or oscillatory estimates would not alone formalize
the target. A later canonical proof must retain Hypotheses, Conclusion,
Proof and Mathlib sections and precise citations. The plausible benefit
is checked transfer of a signed mean to actual polynomial values;
quantitative margins, ordered separated samples, root counts, bulk
separation and actual-Xi all-degree positivity remain independent gaps.
