# Vaughan bulk phase-and-loss test — approved source scope

TARGET: Test whether first- and second-derivative Vaughan Type I/II bounds can pay B_n on exp(n)<m<=exp(2*n), retaining exact degree averaging, compensation and fixed-order remainder costs.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step241's completed bounded Vaughan/nonlinear/logarithmic-phase and exact Laguerre-von-Mangoldt search in 2026-11-10-prime-laguerre-bilinear-bulk-review-240.md. No inspected theorem pays this compensated block; this tests applicability and losses of named tools, with no novelty claim.
SOURCE_EVIDENCE: Reused review240 step241 contracts and rechecked direct primary sources on 2026-11-10: Tao arXiv1201.6656v4 Lemma4.11/(4.18)-(4.19), pp23-24, https://arxiv.org/pdf/1201.6656v4 ; Tao Notes5 Proposition6/proof and Proposition7, https://terrytao.wordpress.com/2015/02/07/254a-notes-5-bounding-exponential-sums-and-the-zeta-function/ ; Robert2015 Theorem1/Sections3.1-3.2, pp5-6, https://perso.univ-st-etienne.fr/rool6510/robert-2015-indag.pdf ; DLMF https://dlmf.nist.gov/18.18.E18 , https://dlmf.nist.gov/18.15.E19 , https://dlmf.nist.gov/10.17 .
COMPARISON: Standard arbitrary-weight decomposition and derivative tools cover ingredients; missing are the n-dependent phase and amplitude on multiplicative factor ranges, differenced Type II phases, and complete centered loss comparison. No existing block bound or obstruction is asserted.
GAP: Determine whether these specific tools give sufficient cancellation with all costs, or identify a precise hypothesis failure or surviving positive exponential loss. A leading-phase estimate alone cannot bound B_n; the complement in L984(H) remains independent.
REASON: Step242 completes the separate source approval and repairs missing direct source URLs; SPECIALIZE and the exact target are unchanged. The sources license a bounded applicability/loss test, not a block bound. No new mathematics or novelty claim; next turn executes the saved calculation using this approved scope.
SCOPE: Actual Lambda, integers n>=2, K_n and B_n below; finite degree-sum specialization; real scaled Laguerre/Bessel formulas at fixed truncation order; dyadic Type I/II factors; first/second derivative tests and one standard Cauchy/differencing reduction. No new zero-free region, RH, simplicity, growing-order asymptotics or complex contour shift.

## Exact observable and relevance

    K_n(u)=(n-1)^(-1)*sum_(k=2)^n L_(k-1)^(1)(u),
    B_n=sum_(exp(n)<m<=exp(2*n)) Lambda(m)*K_n(log m)/m
                              -integral_n^(2*n) K_n(u)du.

The payment threshold remains: for every epsilon>0 there is a finite
C_epsilon>=0, independent of n, with B_n<=C_epsilon*exp(epsilon*n)
for all n>=2. A two-sided estimate suffices but is not presumed.
Eventual estimates must retain a finite-prefix argument. All prime
powers and the full right endpoint are mandatory.

L984's unpaid (H) concerns the entire common-cutoff degree average.
Paying B_n would control one interior logarithmic range only.
L981 pays a remote tail; L982 fixes fixed-index normalization.
Neither bounds B_n. The ranges log m<=n and
2*n<log m<=log X_n and matching integrals remain unresolved.
The main L030-L032/C032a positivity and L966/L968 signed-forcing
gap is unchanged. No cross-notebook input is needed.

## One bounded test

Import the cited tools without reproof. The mathematical task is
their exact specialization and loss check:

1. Specialize DLMF18.18.18 to the finite degree sum, retaining the
   missing degree-zero term and 1/(n-1). Establish the compact scaled
   argument range before using18.15.19. Keep exp(u/2), correction
   terms and additive remainder. Use10.17.3 only with fixed Bessel
   order and positive argument conditions.
2. On dyadic m near X within the block, and products r*s near X with
   r near R,s near S,R*S near X, compute the first two derivatives of
   the explicit leading phase from nu*xi(u/nu). Compare with the full
   hypotheses and bounds of Tao Proposition6 and Robert Theorem1.
   For Type II retain both factor coefficients and compute the
   differenced phase after Cauchy, including diagonal/near-diagonal
   pairs. Never apply an unweighted test directly to arbitrary
   coefficients. Fix Vaughan support parameters with strict upper
   inclusion before using Lemma4.11.
3. State actual versus required gain after restoring amplitudes,
   all Type I/II terms, endpoints, degree-zero correction and the
   compensating integral. Retain the full fixed-order remainder cost;
   an absolute envelope can fail without proving the remainder large.
   No derivative of an O remainder is licensed.

This is one mechanism test. A rigorous phase-range obstruction or
demonstrable insufficiency of these particular upper bounds is an
informative negative, with exact scope stated. Failure of an estimate
does not establish positive B_n or rule out arithmetic cancellation.

Continue only with a concrete applicable bound reaching the full
every-epsilon threshold, or a materially refined mechanism addressing
the exact loss found. Stop this derivative-bound mechanism for a
decisive hypothesis failure on the relevant factor regime or fixed
positive exponential loss without an identified removal. Do not try
successively higher derivative orders or extra source hunts inside
this attempt. If a necessary comparison remains unresolved, save the
exact formulas and assumption rather than report a theorem.

No differentiation, decomposition, remainder integration or rate
comparison was performed in the nomination or its source approval.
Step242 completes the separate approval before execution. This is
ordinary specialization and obstruction testing, not a justified
creative proof attempt. Full matching Mathlib coverage is unchecked
and unknown.


## Source approval and recovery repair — step242

10 November 2026. This is the separate literature approval requested
by step241 and the supervisor's direct-URL recovery gate. The direct
links in SOURCE_EVIDENCE are now in this assessment itself. Reused
the completed search and theorem comparison in review240; no changed
hypothesis or new theorem search was needed. Reopened the primary
statements, the relevant first-derivative proof and Robert's trivial
curvature/sign cases, and DLMF's fixed-order error conditions. These
agree with the recorded contracts; no stronger conclusion is added.
The prior complete proof-case readings remain in review240.

For traceability: [Tao Lemma4.11, pp23-24](https://arxiv.org/pdf/1201.6656v4)
is the arbitrary-weight decomposition, with strict support and both
coefficient families retained. The [Notes5 Proposition6 and7](https://terrytao.wordpress.com/2015/02/07/254a-notes-5-bounding-exponential-sums-and-the-zeta-function/)
are unweighted derivative/differencing tools, not arbitrary-coefficient
prime estimates. [Robert Theorem1, pp5-6](https://perso.univ-st-etienne.fr/rool6510/robert-2015-indag.pdf)
requires a two-sided nonzero curvature comparison with a fixed ratio;
its uniform constant does not remove the inverse-curvature term.
[DLMF18.18.18](https://dlmf.nist.gov/18.18.E18),
[18.15.17-20](https://dlmf.nist.gov/18.15.E19) and
[10.17.2-3/(iii)](https://dlmf.nist.gov/10.17)
remain finite-connection and fixed-order asymptotic inputs only.
For the Bessel real-argument error theorem, retain the stated order
conditions on each truncated sum, not only positivity of its argument.
No derivative of an O remainder or growing truncation order is approved.

Checked the recorded step235 automatic-average and step240
criterion-only stops and step241 comparison. The present test asks
for arithmetic cancellation in a fixed bulk block, not automatic
payment by averaging or an equivalent RH criterion. Those stops
remain intact. No direct block theorem was found by the reused search;
this is not an assertion of novelty or an absence theorem.

Decision: SPECIALIZE approved for exactly TARGET and SCOPE. All
phase derivatives, weighted Cauchy reduction, endpoint terms,
compensation and exponential-rate comparisons remain work for the
research step. An insufficient upper bound would stop only these
specified tools, not disprove the desired one-sided bound. This
repair supplies no new mathematical evidence: outcome STALLED,
classification NOVELTY_UNCHECKED, actual task literature_comparison.
