# Amplitude-level cancellation — completed source comparison

TARGET: Assess whether an amplitude-level coarea decomposition of L471's Hardy-function defect can retain the signed cancellation needed for N(T)=o(T(log T)^3), without estimating the full positive pair majorant.
CHECKED: 2026-10-30
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed bounded exact/stronger-result searches for deterministic coarea, Hardy-amplitude crossings, stationary points and weighted Kac--Rice formulas; inspected primary statements and relevant proof cases below. Reused negative-mass, sign-adapted-leakage and moment assessments; no matching clipped saving found and no novelty inferred.
SOURCE_EVIDENCE: Simon, Introduction to Geometric Measure Theory (2017/2018 author text), Chapter 2 (4.19)--(4.20), Theorem 7.3/Remark 7.4 and Theorem 7.5; Armentano--Azais--Leon arXiv:2304.07424v2, Theorem 2.1, Proposition 3.2/proof, Section 5 and Theorem 7.1/proof; Hall, Acta Arith. 111 (2004), Theorem 2 and (66)--(73); reused Bui--Hall v1 (1), Theorems 1--3 and Sections 5--7. Precise links and qualifications below.
COMPARISON: Deterministic coarea supplies a weighted equality, not a clipped cancellation bound. Weighted Rice formulas retain density/conditional-law hypotheses and an unknown weighted conditional expectation. Hall's stronger stationary-point conclusion assumes RH; Bui--Hall's unconditional moments and fixed-positive-density signs do not supply the full clipped saving.
GAP: No inspected result estimates the amplitude-conditioned joint curvature/slope contribution needed for N(T)=o(T(log T)^3). A raw level identity can retain clipping, but no independently controlled signed correlation or error estimate emerged; neither the saving nor its impossibility is proved.
REASON: Park direct coarea-to-saving and random-level-law implementations after these theorem-level mismatches. EXPLORE records bounded discovery, not approval to assume a missing joint law or derive a cosmetic identity. Reuse ready weighted-cubic coverage for a coefficient-uniform test rather than repeat discovery or a completed audit.
SCOPE: Actual real-analytic Hardy Z and the completion A of L471 on [T,2T], full N(T), all zeros and endpoint levels; no RH, simplicity, spacing, selected-zero moment or unproved level-crossing asymptotic may be assumed.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED target needed primary coarea/level-crossing hypotheses outside the ready reciprocal-zero and residual-moment assessments.

## Original nomination (source status superseded below)

This is a newly nominated continuation, not ready mathematical coverage.
The completed moving-cutoff audit is unaffected by its REVIEW_REQUIRED
status. Next turn is literature-only, with primary hypotheses and relevant
proof cases required before deciding IMPORT, SPECIALIZE or EXPLORE.

The prospective intermediate target is an exact amplitude-level expression
or inequality for the ordinary-derivative defect in L471 (7) that retains
the interaction of Z Z'' and Z'^2. The downstream purpose would be a
test of the full N(T) scale, including the sector omitted by C483a.
No such expression or saving is asserted here. Even full integrated
negative-mass saving would leave individual-height signs and all-degree
mixed positivity unresolved.

Review coarea/level-crossing identities for smooth real functions and
actual-zeta amplitude/derivative results, distinguishing unconditional
inputs from RH-dependent inputs. Search exact statements and stronger
results, then compare with the recorded sign-adapted leakage,
selected-energy, residual interpolation and global-envelope failures.
The narrow local terminology check found scalar level-set references;
those are leads, not coverage of the joint derivative observable.

The bounded eventual test would identify every endpoint/critical-level
term and a specific remaining correlation at the T(log T)^3 scale.
Continue toward a creative proof attempt only if this gives a materially
different, independently testable mechanism. Abandon the proposed
implementation if it merely repackages the full unknown N(T), needs an
unproved selected amplitude law, or reproduces the existing norm losses.
The later proof attempt's escalation must name that precise term and
test; no creative approval is inferred from this nomination.

No mathematical derivation, new source import, Mathlib coverage claim
or source novelty assessment was performed for this continuation.

## Completed review, 30 October 2026

NEGATIVE / LITERATURE / NOVELTY_UNCHECKED; actual task
literature_comparison. New evidence changes the implementation decision;
it is a source-to-observable mismatch, not an obstruction theorem or an
improved bound. No lemma, mathematical script, DAG or PROOF edit.

### Relevance and decisive test

The main gap is actual-Xi all-degree mixed positivity. The intermediate
question was whether amplitude-level analysis supplies both a zero-safe
representation of L471 (7) and an independently testable signed estimate
below the full T(log T)^3 scale. The downstream purpose is full mean
first-sign control, including C483a's complementary sector. Individual
heights, higher signs and mixed positivity would remain unresolved.

The source test fails for the direct implementations reviewed: the
deterministic identity retains the unknown clipped weight, while the
probabilistic replacement requires an unsupplied law. A representation
of the same unknown integral is insufficient. This does not prove
that a future level-set method or the desired saving must fail.

### Primary statements and relevant proof cases

**Deterministic coarea.** Leon Simon, *Introduction to Geometric
Measure Theory*, author text, copyright 2017/2018,
[Chapter 2 (4.19)--(4.20), PDF pp. 36--37](https://math.stanford.edu/~lms/ntu-gmt-text.pdf#page=36),
and [Section 7, PDF pp. 42--44](https://math.stanford.edu/~lms/ntu-gmt-text.pdf#page=42).
Theorem 7.3 applies to a locally Lipschitz map on an n-dimensional C1
submanifold into R^m, m<=n; fibers carry H^(n-m) and the time integral
has the normal Jacobian. Remark 7.4(1) permits nonnegative measurable
weights. The n=m proof invokes (4.19); read that chart-reduction proof
and (4.20)'s simple-function extension. Read also Theorem 7.5 and its
preceding zero-Jacobian argument: exceptional levels and exceptional
times are different matters. These are citation inputs, not results
requiring reproof here.

A later Hardy specialization must check regularity, critical-time
contributions when dividing by |Z'|, integrability and endpoints. H^0
counts preimages, not algebraic zero multiplicities. The theorem gives
no simplicity assertion. Clipping may stay inside the measurable weight;
it cannot be moved outside a signed fiber sum by citing this theorem.
No specialized identity or integration by parts is derived here.

**Weighted random crossings.** Armentano--Azais--Leon,
*On a general Kac-Rice formula for the measure of a level set*,
[arXiv:2304.07424v2, 20 July 2023, Theorem 2.1](https://arxiv.org/html/2304.07424v2#S2).
The hypotheses are a.s. C1 paths, continuous marginal densities uniformly
bounded on compact parameter sets, and conditional path laws continuous
in the level in the C1 topology. Proposition 3.2 gives an almost-every-level
version with weaker density/integrability hypotheses; read its full
coarea/conditioning/Fubini proof. Section 5's D=d argument tapers boundary
and small-Jacobian points before continuity and limits.
[Theorem 7.1 and proof](https://arxiv.org/html/2304.07424v2#S7) permit
nonnegative weights lower semicontinuous in location and the extra path,
with a continuous conditional law for that extra field. Its right-hand
side still contains a weighted conditional Jacobian expectation. These
results provide neither a Hardy conditional law nor a quantitative
bound for the curvature-selected weight. No such law, density control
or weighted estimate is a retained actual-zeta input. The Gaussian
alternative is not an actual-Z theorem. An almost-every-level assertion
also cannot be assigned to a prescribed zero/critical level without
its stronger hypotheses. No stochastic result is imported locally.

Randomizing height would not by itself identify a Gaussian or independent
jet law. Establishing the applicable law and its weighted estimate is
additional mathematics, not a consequence of naming Kac--Rice.

**Actual Hardy geometry.** R. R. Hall, *On the stationary points of
Hardy's function Z(t)*, Acta Arithmetica 111(2) (2004), 125--140,
DOI 10.4064/aa111-2-2,
[Theorem 2, p. 127](https://www.impan.pl/shop/en/publication/transaction/download/product/82433#page=3).
Read the multiplicity convention, Rolle comparison (3), the theorem's
RH and endpoint exclusions, and
[(66)--(73), pp. 136--137](https://www.impan.pl/shop/en/publication/transaction/download/product/82433#page=12).
The positive reciprocal kernel (69)--(70) is used under RH. The resulting
real-stationary-point conclusion and single-between-zeros argument cannot
be imported unconditionally. The elementary Rolle comparison supplies
no amplitude-weighted clipped estimate. No unconditional simplicity or
extremum-amplitude assertion is imported.

**Reused derivative moments.** Reuse
[Bui--Hall, arXiv:2304.05178v1, 11 April 2023](https://arxiv.org/html/2304.05178v1),
as assessed in `2026-10-27-actual-xi-negative-part-mean-coverage.md`.
Rechecked (1), Theorems 1--3 and relevant Sections 5--7 passages.
Theorem 1 gives measure at least (3/25+o(1))T for ZZ''<0, not a
level-conditioned upper bound for the complementary clipped mass.
Section 6 uses mollified signed and square means for that fixed
proportion. Section 7 differentiates a shifted fourth moment; its input
Proposition 3's proof is omitted by the authors. These existing
fixed-order inputs do not supply the joint level-conditioned estimate.
Their arithmetic proofs are not independently audited here.

### Duplicates, failures and searches

Read L471's definitions and (6)--(10): the zero-safe completion identity
and ordinary-moment O(T(log T)^3) bound already exist. Retain C483a's
audited sector limitation from the supplied overview. Read L475's
statement/envelope, L482's stated obstruction and L481's relevant
moment-certificate conclusion. Their positive-envelope, formal-length
and interpolation failures have their original narrower scope. Reuse
the sign-adapted leakage assessment: multiplier variation and
sign-boundary costs remain uncontrolled by the coarea identity.

Narrow local searches found no completed duplicate of this exact target;
older amplitude-cutoff references concern different weights. No sibling
notebook was read. Existing unfinished work is preserved.

Queries actually included `one dimensional area formula level sets
derivative absolutely continuous function coarea theorem weighted`,
`Hardy Z function level crossings nonzero values derivatives moments
Z Z second derivative`, `Hardy Z Z second derivative Z prime squared
sign Laguerre negative mean`, `"Hardy" "level crossings"`,
`"Hardy" "a-points" Z(t)`, `"Z(t)" "coarea" zeta`,
`"Z(t)" "level" "Kac-Rice"`, the Hall stationary-points title,
and weighted Kac-Rice theorem searches. Zeta a-points were not presumed
to be real Hardy-amplitude crossings. No novelty follows from a failed
search.

Ivic's value-distribution and large-value articles remain unread theorem
leads. An Azais--Wschebor 2007 author PDF opened at its introduction but
theorem retrieval timed out; the accessible 2023 primary paper above
supplies the comparison used. A local Simon download failed at DNS;
its relevant theorem/proof text was accessible in the web reader. No
essential source remains blocked for this decision. Mathlib matching
is not checked; a search hit is not coverage evidence.

### Route decision

Park direct coarea-to-saving. The missing actual-height joint
curvature/slope estimate after clipping blocks a justified creative
sign attempt. Reopening requires a quantitative new input or a
specified pairing with an independently provable error test; merely
writing the coarea identity does not pass the original test.

Reuse the unchanged ready EXPLORE assessment
`2026-10-29-saturation-weighted-cubic-feasibility.md` for a different
mathematical test. Its p=1 attempt failed but did not decide the infimum
over all T-dependent cubics. The specific refinement is coefficient-uniform
separation using its cited L1 annihilator criterion, retaining the exact
actual-height residual measure and both phases. That lower-bound option
is explicitly in its existing scope. No annihilator or mass bound is
constructed here; this is established-method development, not a creative
sign-saving claim. Exact action and routing are solely in PROGRESS.md.
