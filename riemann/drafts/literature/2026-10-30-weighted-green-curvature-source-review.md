# Weighted Green-identity route: completed bounded source comparison

TARGET: Review coverage for a weighted Green identity that bounds W_delta at delta=log log T/log T using a smooth product test on log|xi(s)|, retaining both horizontal and vertical curvature terms.
CHECKED: 2026-10-30
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed bounded searches for Poincare--Lelong/Riesz zero measures, weighted Littlewood formulas and zeta-squared mixed log-modulus estimates; reused the exact-weight, selected-disk and Blaschke assessments. Queries and primary passages are recorded below. No matching quantitative theorem was identified; no novelty inference.
SOURCE_EVIDENCE: Krishnapur arXiv:math/0607504v1 (20 July 2006), Section 2.2 (2.2.1)--(2.2.2), printed p. 14/PDF p. 23, https://arxiv.org/pdf/math/0607504v1#page=23; Fazzari arXiv:1912.08127v2 Proposition 1.1 and following qualification, https://arxiv.org/html/1912.08127v2; reuse Bettin--Fazzari arXiv:2208.08421v1 Theorem 1.2/Section 2.1, Fazzari arXiv:2310.15918v2 Theorem 1, and Fazzari--Gerspach--Minelli arXiv:2507.04150v1 Theorem 1.1/Proposition 3.1, with direct links below.
COMPARISON: The deterministic distributional identity covers compact smooth tests and all multiplicities, but supplies no signed estimate. The nearest weighted prime-log approximation assumes RH precisely in its zero contribution. Unconditional analytic zero statistics and fixed polynomial log moments do not cover the real product cutoff with the exponential amplitude weight. Both curvature terms must remain.
GAP: Establish the proposed signed mixed log-modulus estimate at delta=log log T/log T, or isolate an explicit unclosed remainder in a bounded application. Smoothness, completion-factor cancellation, integrability and domination require local justification. No quantitative estimate, full-range uniformity or mass transfer follows from this review.
REASON: Essential identity coverage is accessible and the quantitative difference is explicit. EXPLORE supports a separately approved bounded cancellation test, not the W_delta inequality. Park an RH-based weighted prime-log substitution; other signed mechanisms remain testable. No new mathematics was derived during this literature-only comparison.
SCOPE: Actual completed xi and zeta; every sufficiently large real T; delta=log log T/log T; full zero multiplicities; no RH, simplicity, spacing, independence, external half-plane estimate or new weighted moment as an assumption.

## Exact proposed test to compare with sources

Preserve W_delta from
`drafts/literature/2026-10-30-zeta-squared-weighted-local-density.md`:
strict beta>1/2+delta/2, closed |gamma-t|<=2delta, and the continuous
weight |zeta(1/2+it)|^2 on [T,2T]. The desired bound is still
C T delta(log T)^2 exp(-c delta log T), with fixed C,c>0.

The proposed replacement uses the entire completion xi(s), as defined
in `foundations/notation-and-inputs.md`, and a smooth product test
Phi_delta(sigma) w_(T,delta)(v). Choose fixed smooth cutoff profiles:
0<=Phi_delta<=1, supported in (1/2,5/4), equal to 1 on
[1/2+delta/2,1], and a nonnegative Psi_delta supported in
[-3delta,3delta], at least 1 on [-2delta,2delta]. Set

    w_(T,delta)(v)=integral_T^(2T)
          |zeta(1/2+it)|^2 Psi_delta(v-t) dt.

The source review must compare the multiplicity-weighted zero statistic
with the proposed real two-dimensional integral of log|xi(sigma+iv)|
against the Laplacian of this product test. Both the horizontal
curvature Phi_delta'' w and the vertical curvature Phi_delta w''
must remain. No identity, domination, signed cancellation or bound for
this construction is derived or approved in this nomination.

The potential advantage to test is a continuous statistic that retains
the amplitude weight before summing zeros. The potential failure is
the cost of moving cutoffs and their signed curvature; taking separate
absolute values may simply lose the desired scale again. Review the
primary formula and relevant signed/mixed log-modulus estimates before
authorizing any application. A cited identity alone is not evidence for
the quantitative inequality. Do not insert an RH-dependent log-derivative
theorem or positivity of a complex-zero analytic statistic.

## Continuation and abandonment test

Complete one bounded primary-source comparison for this exact test,
including known stronger results and obstructions. Continue to a
separately approved mathematical test only if the sources justify the
identity and identify a quantitative signed-curvature target without
assuming the desired weighted count. If the available estimates only
give a renamed selected-amplitude premise or the old absolute-envelope
loss, park that implementation and record the precise obstruction.
No conclusion is drawn from a failed search alone.

Essential local inputs are the xi normalization in the foundations,
L471/L483/L486 for downstream mass relevance and the L485 count scope.
L500 is the new, separately unaudited diagnostic record, not an assumed
weighted estimate. The previous detector and Blaschke failures must be
compared without reopening them by renaming their unknown weights.
Even a successful bound would leave kernel transfer, other scales,
complementary mass and actual-Xi individual signs unresolved. Full
Mathlib coverage is unchecked.

Recommended next task: literature_comparison, standard/high. The
existing detector assessment remains unchanged and valid for its
original scope; this new target requires its own separate source gate.

## Completed source comparison, 30 October 2026

The preceding sections preserve the nomination and its stopping test, not
an established specialization. This section completes the missing review.
The newly written continuation needs separate approval before mathematics.

### Identity and its exact scope

M. Krishnapur, *Zeros of Random Analytic Functions*, Berkeley dissertation,
[arXiv:math/0607504v1](https://arxiv.org/pdf/math/0607504v1#page=23),
Section 2.2, printed p. 14, equations (2.2.1)--(2.2.2), states for a
deterministic analytic F on an open set Omega:

    dn_F=(1/(2pi)) Delta log|F|,
    integral phi dn_F=(1/(2pi)) integral log|F| Delta phi dm,
                            phi in C_c^infinity(Omega).

Here dn_F counts every zero multiplicity; m is planar Lebesgue measure.
Exclude an identically zero component. This standard one-variable
Poincare--Lelong identity requires no randomness. The full displayed
statement and multiplicity clause were inspected in the versioned PDF;
subsequent random-field expectation formulas are not inputs. Compact
support is essential: this is not a sharp-rectangle formula with omitted
boundary terms. Interior zeros are distributional masses, requiring no
zero-free branch of log F. The identity gives no uniform estimate for
changing tests. Smoothness of the proposed convolution, differentiation
through its finite t integral and quantitative derivative costs remain
application obligations. It does not permit deleting vertical curvature.
No reproof of the source identity is needed.

### Signed/mixed estimates and the conditional shortcut

A. Fazzari, *A weighted central limit theorem for log|zeta(1/2+it)|*,
[arXiv:1912.08127v2, 20 January 2021](https://arxiv.org/html/1912.08127v2),
Theorem 1.1 and Proposition 1.1, printed pp. 2--3. Proposition 1.1
approximates log|zeta| in zeta-squared weighted even moments by
Re sum_(p<=x) p^(-1/2-it), with x=T^(epsilon/k),
epsilon=1/log log log T. It assumes RH. The following paragraph
identifies the shifted discrete second moment over zeros as the
conditional input. Its unconditional short-polynomial Lemma 2.1 does
not remove that error. Thus a prime-log substitution is not an available
unconditional import here; its weighted error would need a new proof.
Park that substitution, without claiming all signed Green methods fail.

Reuse the completed exact-amplitude comparison in
[the weighted-density assessment](2026-10-30-zeta-squared-weighted-local-density.md).
The strongest inspected unconditional exact-amplitude theorem remains
Bettin--Fazzari, [arXiv:2208.08421v1](https://arxiv.org/pdf/2208.08421v1),
Theorem 1.2, printed pp. 1--3, Section 2.1 pp. 5--7. Its even test has
smooth compact Fourier support and is evaluated at potentially complex
zero coordinates; the height weight is smooth and macroscopic. It gives
neither a positive beta-selected count nor the real product-cutoff
estimate. No uniformity for this changing family is stated. Reopened
the primary theorem and complex-gamma footnote; reuse the earlier
explicit-formula proof comparison within its scope.

Fazzari, [arXiv:2310.15918v2](https://arxiv.org/html/2310.15918v2),
Theorem 1, assumes RH and treats a squared log derivative at displacement
a/log T with (log T)^(-1/4+epsilon)<<a<<1. Its proof outline identifies
RH in the positive zero-pair representation and the ratio bound. This
is not an unconditional two-variable log-modulus estimate.

Fazzari--Gerspach--Minelli,
[arXiv:2507.04150v1](https://arxiv.org/html/2507.04150v1), Theorem 1.1
and Proposition 3.1, use fixed nonnegative integer log-moment orders
and even fixed k, Fourier support inside (-2/(k+2),2/(k+2)). The proof
of Proposition 3.1, (3.3)--(3.6), uses Holder and fixed log moments;
it gives no exponential-amplitude or growing-order error theorem.
Theorem 1.2 assumes RH. The retrieved HTML labels v1 as 5 July 2025
and has internal date 24 August 2026; retain that version discrepancy,
with no assertion about an uninspected revision. These statements do
not supply the signed curvature bound.

### Local comparison, searches and disposition

Read L018's entire completion and multiplicity correspondence;
L471's normalization and finite windows; L485's count-only hypotheses;
L486's kernel and losing threshold; and L500's retained correlations.
These proofs were not re-audited. Compare the named selected-disk,
joint-Blaschke and positive-detector stops within their recorded scopes.
The new statistic retains signs before estimation, but no cancellation
has been established. Generic subharmonicity and unweighted moments
supply no new mixed weighted estimate. No cross-notebook theorem is used.

Queries included `Poincare Lelong formula one complex variable log absolute
holomorphic function distribution Laplacian zeros`, `zeta zero density
weighted by zeta squared log modulus Littlewood lemma weighted zeros`,
`weighted Littlewood lemma zeta`, `zeta log-modulus weighted`, `zeta log
modulus second moment` and `zeta logarithm twisted second moment`, plus
exact author/title searches. Irrelevant results and unsupported RH claims
were not imported. Demailly's agbook timed out and the IISc book URL was
restricted; Krishnapur's versioned dissertation provided the essential
identity, so these are not essential blockers. A shell download failed
at DNS resolution. No negative theorem follows from a failed search.

Decision EXPLORE permits a bounded attempt at the uncovered signed estimate,
not assuming it as a premise. The next assessment specifies the threshold
and forbids W_delta or conditional log approximations as inputs. Stop if
only a renamed weighted count survives. Main RH positivity, kernel transfer,
other scales, complementary mass and individual signs remain open.
Mathlib coverage is unchecked. No lemma, mathematical script, DAG or PROOF
change was made. This is source progress only, without a quantitative result
or a claim of progress beyond the inspected literature.
