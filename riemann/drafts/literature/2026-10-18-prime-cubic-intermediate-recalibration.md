# Proposed coverage: one fixed-frequency intermediate recalibration

TARGET: Test whether a fixed nonnegative trigonometric recalibration of L421's intermediate component can match both L409's unweighted cubic and L430's cosine-weighted cubic while preserving every L429 constraint.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 217 searched Fejer--Riesz factorization, prescribed first trigonometric coefficient, extremal positive polynomials and Carlen--Lieb; inspected the author-hosted sources listed below. Repeated the narrow October-16--18 assessment/failure search for trigonometric, recalibration, Fejer and Caratheodory; only the proposal and phase-averaging context appeared. Reuse step 216 and steps 209/213 analytic discovery; no matching complete-law recalibration theorem was located, without a novelty inference.
SOURCE_EVIDENCE: Dritschel--Rovnyak, The Operator Fejer-Riesz Theorem, author-hosted 33-page version, p. 2 classical statement and Theorem 2.1 pp. 4--6; Patton--Putinar, On multivariable Fejer inequalities, September 20 2005 author manuscript, Theorem 1.1 p. 1, (2)--(4) p. 2 and Theorem 2.2/proof p. 4; Andreani--Dimitrov, Rocky Mountain J. Math. 33 (2003), pp. 760, 764--765, (1.1)--(1.4), Lemma 1/(2.12); Carlen--Lieb 0904.0734v2 pp. 1--2, Horn theorem following (1.1) and proof through (1.2). Audited L409/L430 supply exact actual coefficients; audited L421/L429 and L419/L423 supply the full correction interface.
COMPARISON: Known factorization, coefficient bounds and explicit positive kernels cover the fixed one-circle calibration tools; real Schur--Horn covers the finite covariance implementation. None compares the exact L409/L430 coefficient series or proves preservation of the complete L429 law after recalibration. Import those theorems, and test only this unprovided specialization; do not reprove a general moment theorem.
GAP: Determine whether the exact coefficient pair admits a fixed bounded nonnegative trigonometric calibration and prove or obstruct every induced mass, mean, full covariance, support and tolerance requirement. No coefficient-ratio bound, calibration or redesigned law has been established.
REASON: Essential source coverage is now sufficient for one bounded SPECIALIZE test after separate approval. This literature-only turn establishes coverage, not mathematical feasibility, and writes no lemma or mathematical script.
LITERATURE_REASON: Changed intermediate conditional cubic, hence changed remaining mass and full bulk corrections; the previous assessments explicitly covered only the unchanged law.
SCOPE: One fixed frequency log 2, a fixed bounded nonnegative trigonometric polynomial independent of H, complete actual response, uniform height marginal, all sufficiently large real H, original L429 tolerances and cap for each fixed lambda. No growing-frequency theorem or actual conditional law.

The main gap remains global mixed positivity. The independently testable
intermediate question is whether this one additional arithmetic constraint
survives a restricted redesign of the already feasible selected-moment law.
Success would show that this added test still does not force the favorable
joint signs in this relaxation; failure would stop this particular repair,
not establish an actual clipped statistic or exclude all counterlaws.

Review the exact two coefficient series and the applicable nonnegative
trigonometric moment results before calculation. Reuse the ready analytic
coverage for the actual coefficients; another cubic source search is not
needed unless a specific defect is found. Do not import a theorem from a
search snippet or infer the coefficient ratio from L430's separate coarse
bounds. A later approved test must either construct a calibration meeting
both sharp limits or prove an obstruction for this fixed class, and must
retain the high component, remaining mass w, N_H, m, all of A_H, strict
negative bulk support, fixed envelopes and cap bounds.

Continue only if the two coefficients and every induced error can meet the
original tolerances with one eventual real-H family. Abandon this restricted
repair if nonnegative calibration is impossible or a required correction
cannot be bounded. No new law is defined or feasibility result proved here.

Essential inputs: L409, L430, L421 and L429, with L419/L423 inherited
interfaces if needed. L427's fixed-mixture and L428's uniform-density stops
remain intact; C426c and the parked core/tail calculation are unused.
Actual critical-function and cross-H realization, clipping, capped
nondegeneracy, L413's full-error regulator margin and mixed positivity remain
unresolved. Matching Mathlib coverage is unchecked, without an absence
claim. No cross-notebook input is proposed.

## Completed comparison — 2026-10-18, step 217

The original proposal above is retained. Its mathematical obligations
remain unproved; only its source scope is ready, with separate supervisor
approval before mathematical invocation. No law or coefficient inequality
was derived in this turn. The main gap is global mixed positivity. The
intermediate target tests whether this one additional constraint survives
restricted redesign; success would extend the selected-information
obstruction, and failure would delimit this repair alone.

### Inspected sources and hypotheses

1. Michael A. Dritschel and James Rovnyak, *The Operator Fejer-Riesz
   Theorem*, [author-hosted 33-page version](https://uva.theopenscholar.com/files/james-rovnyak/files/p71.pdf),
   p. 2 and Theorem 2.1, pp. 4--6. A Laurent polynomial nonnegative
   everywhere on the unit circle factors as P*P with analytic polynomial
   P of at most the same degree. Take the Hilbert space to be C for
   scalar |P|^2. Non-strict positivity is permitted, including circle
   zeros. Read the scalar reciprocal-root explanation and the theorem's
   Toeplitz equivalence and shift-completion proof. This supplies a
   positivity parametrization, not prescribed coefficients or a law.
2. Linda J. Patton and Mihai Putinar, *On multivariable Fejer inequalities*,
   [author manuscript dated September 20, 2005](https://web.math.ucsb.edu/~mputinar/fejermultivarrev.pdf),
   Theorem 1.1 p. 1: if h(theta)=sum_(k=-d)^d h_k exp(ik theta)
   is nonnegative and h_0=1, then |h_1|<=cos(pi/(d+2)).
   The first-coefficient extremum is attained. Read (2)--(4), p. 2,
   and the coefficient-moment identity (5), compression/nilpotence
   argument (6)--(7), Theorem 2.2 and its proof, pp. 3--4; the n=1
   discussion returns to the classical inequality. Degree is fixed,
   normalization is essential, and Fourier h_1 differs by a factor two
   from a real cosine coefficient. This is an available obstruction
   test, not a bound on gamma_2/beta for the local arithmetic series.
3. Roberto Andreani and Dimitar K. Dimitrov, *An extremal nonnegative
   sine polynomial*, Rocky Mountain J. Math. 33 (2003), 759--774,
   [author PDF](https://www.ime.unicamp.br/~andreani/papers/andr.pdf).
   Inspected p. 760 (1.1)--(1.4), the explicit nonnegative Fejer cosine
   kernels and coefficient conventions; Lemma 1/(2.12), pp. 764--765,
   gives real-coefficient square factorization and exact coefficient
   autocorrelations for nonnegative cosine polynomials. These provide
   explicit fixed-degree candidates and coefficient bookkeeping. Its
   sine-polynomial extremum is not the notebook target and is unused.
4. Eric A. Carlen and Elliott H. Lieb, *Short proofs of theorems of Horn
   and Mirsky on diagonals and eigenvalues of matrices*,
   [arXiv:0904.0734v2, May 13, 2009](https://arxiv.org/pdf/0904.0734v2),
   pp. 1--2, Horn theorem after (1.1), proof through (1.2).
   A real eigenvalue list majorizing a proposed diagonal admits a real
   orthogonal realization. Read the two-dimensional rotation and
   induction. The theorem supplies existence; the Borel implementation,
   repeated-eigenvalue branches and trace-average applicability are
   reused from L419, not inferred anew from the source.

Dimitrov's *Extremal positive trigonometric polynomials*, pp. 6--7,
was a discovery lead for the coefficient theorem; the load-bearing
statement is checked in Patton--Putinar. The original Fejer article
DOI 10.1515/crll.1916.146.53 was located bibliographically but its
full original proof was not read; it is not an additional input.
No unread lead is needed for this fixed one-variable test. No source
claims the complete local counterlaw or an actual conditional jet law.

### Reused analytic scope and local comparison

Read L409's exact beta series, L430's hypotheses, exact gamma_2 series
and rational-character source interface. Their separate step-119/216
audits are reused. Read L421's intermediate kernel (5)--(6) and full
correction (7)--(9), and L429's all-real-height cutoff, (10)--(17),
translated support, remaining moments, envelopes and cap proof. Reuse
`2026-10-18-growing-prime-poisson-covariance.md`,
`2026-10-18-growing-prime-poisson-law-feasibility.md`,
`2026-10-18-growing-poisson-counterlaw-critical-audit.md`,
`2026-10-18-prime-twisted-cubic-coefficient-test.md` and
`2026-10-18-prime-twisted-cubic-separation-audit.md` in this directory.
Those assessments cover the fixed-product and actual coefficient tools;
there is no reason to repeat a cubic analytic-source search.

The unchanged intermediate component gives a constant conditional cubic.
The proposed modification is a fixed nonnegative polynomial in
 theta=t log 2, independent of H, multiplying that component's mass;
its degree may be chosen once, but cannot grow with height. The high
component, its orientation, the intermediate direction/radius, and
L429's Poisson covariance mechanism remain the reference construction.
Whether this proposed class meets the two coefficients is a research
question. Establish the exact period-moment requirements from the two
series, with the correct cosine normalization; do not infer a coefficient
ratio from their separately stated coarse bounds. Standard polynomial
factorization or kernels can be cited without reproof. Any needed
arithmetic series comparison and complete-law perturbation must be
proved locally in a later research turn.

Even a bounded nonnegative candidate does not certify the full family.
Retain p,k,w,W_H,N_H,Q,J_R,D_R,d_H,m and all symmetric entries of A_H,
including odd entries. Check nonnegative fiber mass and measurability,
normalization against the moving Poisson weight, and every fixed-test
limit on an eventual real-H ray. Compare the minimum covariance and
negative-trace margins with full subtraction and translated atoms.
Verify all six raw second tolerances and first B exactly where required,
first D at o(ell), W^2 x^2 at o(ell), every fixed-prime second correlation
at o(ell), both cubic limits at o(ell^2), all 23 quartics at o(ell^4),
absolute envelopes, fixed physical constants and the cap for every fixed
lambda with one lambda-independent family. The original L429 tolerances
are the targets; neither stronger conditional constraints nor sharper
incidental errors are silently imposed.

Continue only with a certified polynomial meeting both coefficient
requirements and all corrections, or an informative obstruction for this
fixed class. Abandon this repair if coefficient feasibility fails or an
essential correction violates its required tolerance; failure of one
chosen degree alone is not failure of the unrestricted fixed-degree
class. If a new theorem or a different law mechanism is essential, stop
and require separate assessment. L427's fixed-mixture stop, L428's
uniform-bound stop and L430's unchanged-law separation remain intact;
none forbids this changed intermediate mass. C426c remains unused.

Full matching Mathlib coverage is unchecked. No absence is claimed;
Mathlib is not needed to replace the inspected primary inputs. No
cross-notebook input is used. There is no advance beyond the sources
checked, no mathematical exploration expenditure and no RH conclusion.
