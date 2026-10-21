# Source coverage: bounded covariance and finite-prime tests

TARGET: Assess source coverage for testing whether a uniformly bounded bulk covariance density, with L421's lower-order rare second integrals, can match all fixed finite-prime Fourier correlations of the actual critical second moment.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 204 searched weighted prime phases, fixed-twist second moments, bounded densities, Riesz products and Bessel tests; inspected primary Young hypotheses and both off-diagonal cases, BCR Theorem 1, Fazzari's conditional Theorem 1/Corollary 1, and author notes for Bessel and Euler prime-reciprocal divergence. Scoped local covariance/finite-prime/Bessel searches found no completed matching obstruction; L422/L427 test narrower weights. Search failure does not establish novelty.
SOURCE_EVIDENCE: Young, Arch. Math. 95 (2010), 539--548, DOI 10.1007/s00013-010-0199-9, (2.1)--(2.3), Lemmas 4--5, pp. 540, 542--543, https://www.math.ntnu.no/emner/MA3001/2020v/2022v_MA3004/Young.pdf ; Garrett, Hilbert spaces (29 October 2016), claim 5.2, p. 9, https://www-users.cse.umn.edu/~garrett/m/fun/notes_2016-17/01_hsp.pdf ; Narcowich, Math 641-600 Orthonormal Sets (Fall 2014), finite projection identities and Bessel paragraph, https://people.tamu.edu/~f-narcowich/m641/m641_notes/orthonormal_sets2014.html ; Rusin, UT Austin 328K Spring 2017 zeta note, unnamed theorem and proof, pp. 1--2, https://web.ma.utexas.edu/users/rusin/328K-17a/zeta.pdf ; audited L381 (7),(9), L389 (3), L421 (4),(6), L423 (9)--(10).
COMPARISON: Known fixed rational-twist moments supply the actual order-zero coefficients; finite Hilbert-space projection bounds and Euler's divergent prime-reciprocal sum supply an adequate test framework. No inspected source states the exact H-dependent covariance-law obstruction. The finite-height specialization, sharp complex-twist passage and complete-law error comparison remain to be proved; neither a conditional moment formula nor infinite-product measure is needed for this narrower necessary test.
GAP: Test whether the fixed single-prime coefficients are compatible with one H-independent bound on the normalized bulk raw second density after retaining the rare components. Prove the finite-height Gram/projection comparison and sharp limits before concluding obstruction or compatibility. No such conclusion is established in this literature turn.
REASON: Essential sources cover a bounded RESEARCH / REPRODUCTION attempt within the original covariance-domination question. Reuse L381's moment theorem rather than reprove it; the changed Hilbert-space application and law bookkeeping need a local proof. No new mathematics or scripts are produced here.
SCOPE: Actual sharp dt/H averages on [H,2H], f from L389, fixed finite sets of primes and fixed Fourier polynomials before H tends to infinity; one H-independent bound on the bulk covariance density, with the lower-order rare second integrals retained. No growing prime head, independence of critical jets and phases, global critical-function realization or conditional actual covariance formula is assumed.
COVERED_TARGET: Test whether an H-dependent uniformly bounded bulk raw second-moment density, with L421's lower-order rare second integrals retained, can match every fixed single-prime Fourier correlation of the actual critical second moment.
LITERATURE_REASON: The broader covariance-domination target was REVIEW_REQUIRED and lies outside the ready W^3 assessment; essential coverage of H-dependent densities and finite-test quantifiers was missing. This step supplies that comparison, without repeating the W^3 audit or spending a mathematical exploration turn.

The main gap is global mixed positivity. The proposed intermediate
target is a necessary correlation test of the bounded covariance
mechanism, rather than one more W-power fit. A usable criterion or
obstruction could determine whether subsequent designs must change the
bulk scale or rare second-moment contribution. Even a successful
obstruction would not decide actual clipping, capped nondegeneracy,
L413's full-error regulator margin or RH.

Essential starting IDs are L381, L389, L421, L423 and the audited L427.
L419 supplies the fixed response context. The unresolved issues are
the exact scope of known joint prime/critical moments, the quantifiers
for bounded H-dependent covariance densities, and the limit passage
from fixed Fourier tests to any measure comparison. A density need not
be a fixed function of prime phases; that stronger premise must not be
silently imposed. No uniform bound over growing twist sets is available.

The original proposal above is preserved as motivation. The completed
comparison below approves only the stated single-prime necessary test;
no domination obstruction is proved by this document.

## Completed source comparison — step 204

### Primary moment coverage and its limits

Young's published PDF was directly read at (2.1)--(2.3), Lemma 4's
kernel/gamma formulas and Lemma 5's statement and full proof. The weight
is smooth, between zero and one, supported in [T/4,2T], with derivative
scale T/log T. Twists h,k are positive integers with hk<=T^(2 theta),
theta<1/2; complex shifts are O(1/log T). Both functional-equation
diagonals remain. The off-diagonal proof treats hm>kn and kn>hm
separately by the same separation bound and repeated integration by
parts. At scale T=2H, each fixed twist and fixed-shape smoothing fits.

Import the already audited combined-diagonal zero-shift specialization
L381 (7), whose leading coefficient is gcd(h,k)/sqrt(hk), and scalar
bound (9). L389 (3) identifies f squared with the critical zeta modulus
squared everywhere, including zeros. No new derivative moment, critical
Euler product, carrier weight, or assumption about RH is required.
L381's cited audit also explicitly warns that its sharp bracketing is
for a nonnegative complete square, not an individual complex twist.

The next attempt must therefore establish the sharp complex-twist
consequence by polarization of fixed finite nonnegative modulus squares,
or by a fully controlled scalar endpoint estimate. It must preserve
both endpoints and take H to infinity at fixed smoothing width and
fixed twist before removing smoothing. The source does not directly
license inequalities between a complex twist and smooth minorants.
This is a local specialization obligation, not missing theorem coverage.

For comparison, directly inspected Bettin--Chandee--Radziwill,
*The mean square of the product of the Riemann zeta-function with
Dirichlet polynomials*, arXiv:1411.7764v1 (28 November 2014),
[(1.1), Theorem 1, pp. 1--2](https://arxiv.org/pdf/1411.7764v1).
It assumes smooth phi supported in [1,2], coefficients a_n=O_epsilon
(n^epsilon), and length N=T^theta with theta<17/33. Its error is
O(T^(3/20+epsilon)N^(33/20)+T^(1/3+epsilon)); the complete main sum
uses a_d conjugate(a_e)/lcm(d,e) and the logarithm containing
gcd(d,e)^2/(de). This stronger length range is unnecessary here.
Fixed coefficients may have constants depending on the fixed test.
The Young/L381 route already suffices; no BCR reproof is authorized.

### The finite-dimensional test framework

Directly inspected Garrett's claim 5.2 and its projection proof, and
Narcowich's finite projection identities and Bessel paragraph. For an
orthonormal family in a complex Hilbert space, Bessel bounds the sum of
squared inner products by the squared norm. Completeness of the family
is unnecessary. The finite identity follows by expanding a nonnegative
residual square. Import this named inequality; reproducing general
Hilbert-space theory would add nothing.

Directly inspected the unnamed theorem and complete two-page proof in
Rusin's note: Euler's sum of reciprocal primes diverges. It uses finite
Euler products, unique factorization, the harmonic series and a summable
quadratic logarithm error, without the prime number theorem or RH.
Only divergence, with no rate or explicit cutoff, is needed for the test.

The proposed comparison is between the sourced fixed-prime coefficients
and finite Bessel energy under a uniform density bound. This document
does not specialize those coefficients, calculate their energy, or
derive a contradiction. At finite H the characters p^(-it) are not
orthogonal. The mathematical attempt must evaluate their finite Gram
entries and justify the limiting projection inequality with the number
of tests fixed. Direct finite Cauchy--Schwarz or a finite Gram inverse
is an acceptable implementation of the imported projection principle.
No infinite-family inequality on a finite height interval is licensed.

Allow the candidate normalized bulk *raw* x-second density b_H(t) to be
any measurable function with 0<=b_H<=C, with C fixed on an eventual
real-H ray. It need not be a fixed phase function, response function,
scalar multiple of K, or consistent between different H. A bound on
centered covariance alone must be supplemented by a bound for the mean
contribution before it implies this raw-density hypothesis. L423 has
a bounded mean and the full O(sqrt(log H)) covariance correction; those
terms must be retained in any application to that particular law.

The rare second integrals are nonnegative and L421 (4),(6) bound their
total by O(sqrt(log H)) (the high component is smaller). The attempt
must explain their error against each fixed bounded Fourier test at
the leading-log scale, using their *unnormalized* second integrals.
Small probability alone does not prove that error. No retuning of
L423, reconstruction of its negative cone, or preservation of further
moments is part of this necessary test.

All quantifiers must remain explicit: first fix a proposed C; select
only finitely many fixed tests when needed; then take H to infinity
for that finite list. A finite list may depend on C, but may not grow
with H. The potential obstruction concerns matching *all* fixed tests
with one bound. It need not reject each prescribed finite list, and
cannot invalidate L421/L423 on their original selected constraints.

### Adjacent literature and duplicate/failure checks

Exact search strings included `"zeta" "second moment" "prime phases"
distribution`, `"zeta" "twisted second moment" "gcd" fixed`,
`zeta weighted measure prime phases twisted second moment limiting
distribution`, `"zeta" "bounded density" "second moment"`,
`"zeta" "prime" "Bessel" "twisted"`, and searches for Poisson-kernel
Riesz products, Bessel's inequality and Euler prime-reciprocal divergence.
Uninspected search snippets and informal research-site hits are not
theorem inputs. No exact matching H-dependent covariance obstruction
was located in the inspected sources; this is not a novelty claim.

One substantive adjacent result was read at theorem level:
A. Fazzari, *Weighted value distributions of the Riemann zeta function
on the critical line*, [arXiv:2101.08036v1 (20 January 2021),
Theorem 1 and Corollary 1](https://arxiv.org/html/2101.08036v1).
Theorem 1 assumes RH and the stated twisted/shifted moment conjecture;
Corollary 1 still assumes RH for k=1,2. They concern a weighted central
limit theorem for log|zeta|, not the finite-prime bounded-density test.
Neither is imported. They supply no unconditional conditional covariance
law, and are unnecessary for the approved finite test.

Also inspected the Poisson-kernel expansion in section 2.4, p. 24, of
[L. Silvestre's PDE notes](https://www.math.uchicago.edu/~luis/pdenotes.pdf),
and Theorem 4.54, p. 103, of
[A. Seeger's Analysis II notes (12 May 2023)](https://people.math.wisc.edu/~aseeger/Math522-notes-May12-2023.pdf).
These cover respectively the disk Poisson Fourier expansion and uniform
approximation by a self-adjoint point-separating algebra on a compact
metric space. They do not identify the zeta-weighted prime-phase measure.
Their possible product-measure route is not required or approved for
this one attempt. Kakutani singularity and infinite Riesz products were
search terminology only; no such theorem was inspected or imported.

Local searches covered the active notebook's literature/history/failure
records for covariance densities, finite-prime Fourier tests, Riesz
products and Poisson kernels, followed by Bessel/prime-reciprocal/Gram
terms in the October-15--17 records and L414--L427. Read relevant
L381/L389/L419/L421/L423/L427 proof ranges and the previous W^3
assessment and stop record. The only direct proposal was step 203.
An older Poisson-kernel lead in the endpoint Sobolev failure record
concerns an unrelated periodic comparison model, not this covariance
test. No matching completed proof was found in this bounded local scope.

L422's single-power stop and audited L427's fixed-mixture W^3 mismatch
do not decide the current all-fixed-tests question. The C426b/C426c
core/tail stops remain preserved and parked at their existing cap;
neither they nor the unevaluated I supply an input here.

### One approved test and decision threshold

The covered next target is the single-prime necessary test stated in
COVERED_TARGET. Write a rigorous sharp moment specialization, then
one finite projection/Cauchy comparison for arbitrary H-dependent b_H,
retaining the rare second integrals and any mean/covariance corrections.
Compare the resulting finite coefficient-energy requirement with the
sourced divergence theorem. No numerical script, cutoff sweep, new
source theorem, or infinite-measure construction is needed.

Continue this mechanism only if the proof gives, for each proposed fixed
bound C, a finite fixed test list with a strict contradiction after the
height limit, while keeping every error o(1) at normalized second scale.
If the argument needs growing twists, a fixed phase-only density,
unproved conditional moments, or drops a leading rare contribution,
stop and record that exact limitation. If no contradiction follows from
the valid finite inequality, record an inconclusive test rather than
compatibility of all correlations. No downstream clipping or RH claim
is licensed even if the bounded-density mechanism is excluded.

Essential continuation IDs: L381, L389, L419, L421, L423 and audited
L427 as the narrower historical separator. The remaining obligations
are the sharp complex-twist limits, finite Gram limit, raw-density
hypothesis and complete-law comparison. Actual clipping, global
realization, capped nondegeneracy and L413's full-error margin remain
independent unresolved gaps. Full matching Mathlib coverage and its
supporting finite-projection names were not checked; no absence claim
is made. This source-only EXPLORATION establishes coverage, not a new
lemma, obstruction, solution candidate or mathematical certificate.
