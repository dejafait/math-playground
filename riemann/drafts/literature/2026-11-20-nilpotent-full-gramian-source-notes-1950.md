# Nilpotent full-cost diagnostic: source notes1950

Literature-only step, 20 November 2026. No asymptotic, new lemma or
mathematical program is established. The exact target and definitions
remain in assessment1949. Main gap: actual-Xi positivity and C028b's
H_d=o(d). This model can test a limitation of one metric schedule;
neither possible model outcome settles that gap.

## Inspected primary results and qualifications

**Finite Gramian and nilpotent example.** Tony Stillfjord and Filip
Tronarp, *Computing the matrix exponential and the Cholesky factor of
a related finite horizon Gramian*, BIT Numerical Mathematics66(2026),
article65, published2November2026,
[Sections1 and7, Experiment0](https://doi.org/10.1007/s10543-026-01160-6).
Read (2a-b), (4b), (5), and the complete Experiment0 setup and discussion.
The example has A_ij=1 for i=j+1, zero otherwise, and B=e_1.
Its propagated input is (1,t,t^2/2!,...,t^(n-1)/(n-1)!)^T;
the authors describe a closed-form Gramian/Cholesky calculation using
Legendre polynomials. The displayed experiment supplies neither that
factor formula nor our full-cost asymptotic. Its single-input
controllability metric differs from the prescribed identity-observation
realification. A switch of transpose, phase, observation rank or
principal block needs justification before transferring any formula.
The identity integral/positivity input remains the versioned v2 source
already assessed in source-notes1947; no numerical algorithm is imported.
The journal HTML's prose change-of-variables display for G_o omits the
adjoint on its generator; use the defining (2b) integral and C029b's
already justified substitution, not that display as a new theorem.

**Scalar differentiation comparison.** A. Shadrin, G. Nikolov and
D. Aleksov, *On the Markov inequality in the L2-norm with Gegenbauer
weight*, [arXiv:1510.03265v1](https://arxiv.org/pdf/1510.03265v1),
12October2015. Read the weight/norm definitions, Theorem1.1 p2,
(2.1)-(2.3) p3 and the concluding even/odd cases p7 (PDF pages).
For weight (1-t^2)^(lambda-1/2) on [-1,1], lambda>-1/2, its
degree-n derivative bound is

    c_(n,lambda) < (n+1)(n+2lambda+1)/(2 sqrt(2lambda+1)).

The proof splits even/odd Gegenbauer coefficient vectors and bounds
the largest eigenvalue of each derivative Gram matrix by its trace.
Thus both parities are covered; lambda=1/2 is in scope for ordinary
unweighted L2. This concerns a scalar differentiation operator norm,
not our Hermitian-imaginary trace norm in a changing energy metric.
No affine rescaling, vector observation reduction or Schatten estimate
for our model is derived here. The Schmidt asymptotic mentioned in the
introduction is a cited lead, not an independently inspected theorem
input; it is unnecessary to approve an attempt using the finite inputs.

**Sobolev differentiation comparison.** Parisa Alvandi and Stephen M.
Watt, *Handwriting Feature Extraction via Legendre-Sobolev Matrix
Representation*, 2019 author-hosted
[PDF](https://cs.uwaterloo.ca/~smwatt/pub/reprints/2019-synasc-ls-matrix-rep.pdf).
Read SectionII (1), p2, and SectionIII.A, Lemma1, Proposition1,
Theorem2 and its complete proof, pp3-4. Its inner product is the sum
of unweighted scalar L2 and mu times first-derivative L2 on [-1,1],
mu>=0. Theorem2 gives a coefficient differentiation matrix in that
Legendre-Sobolev basis; the proof uses triangular change of basis and
parity. It gives no singular-value/full-cost estimate for our metric.
In particular, the name Sobolev does not authorize discarding other
observation coordinates or identifying their norm with (1). No formula
from this paper is needed as a new premise; the mismatch is recorded.

## Local duplicate and failure comparison

Read C029b fully, including both attempts; read C028h's full proof and
C028b's hypotheses, conclusion and cited convergence/scale argument.
Reuse source-notes1947's completed comparison of C028i/o/p, C029a and
stops1525/1588/1695/1713. They concern actual coefficients or specified
diagonal, shear, theta-moment or branch families, not this nilpotent
realified integral. They do not stop general metrics or prove a floor
for this model. The two unpaid actual endpoint attempts stay parked:
their coercivity and signed decomposition do not answer the full norm.

Searched C028/C029 and companion/metric/Gramian assessment/attempt paths
for nilpotent, Jordan, unit/weighted/subdiagonal shift and Hilbert terms;
then searched the active notebook's lemmas, literature and ATTEMPTS
for nilpotent/Jordan-block/integrator/Hilbert-matrix occurrences.
Relevant matches reduce to the present proposal/C029b and old distinct
metric evidence. Narrow contexts show C020o is a finite differential
preserver inverse, L571 a disk-Hardy interpolation budget, C744j/L741
multiplicative-Hilbert/Carleman bounds, and nomination914 a
resolvent/adjugate discussion. These are not duplicates or theorem
inputs for the diagnostic. No sibling notebook was read.

## Search record and decision

Queries included `nilpotent Jordan block finite horizon observability
Gramian polynomial Hilbert matrix`, `integrator Gramian Hilbert matrix`,
`finite horizon Gramian nilpotent`, `nilpotent Gramian commutator`,
`finite horizon Gramian trace norm nilpotent`, `nilpotent Gramian
Schatten`, `time averaged Gramian Jordan symmetrizer`, and Legendre/
Sobolev differentiation singular-value and L2 Markov queries.
No exact full-cost asymptotic at T=d^2 was located. This is bounded
coverage, not a claim of novelty or exhaustive absence.

Discrete-time learning/Jordan results, wave-system observability,
infinite-horizon stable Gramians, and Sobolev zero-location search
hits were not imported. No essential source access blocker remains:
the finite integral and exact polynomial source cases are accessible.
The precise remaining research difference is the prescribed real
principal-block norm, its inverse normalization and all d singular
values jointly at T=d^2. Sources do not justify a scalar-channel or
fixed-d asymptotic replacement. EXPLORE approves one bounded attempt
on that unchanged difference; it proves neither alternative.

Reuse the matrix norm inputs under assessment1947; reproof is not
justified. Any later moment representation or source specialization
must verify the changed hypotheses and normalization in its canonical
proof. Full matching Mathlib coverage is not checked. No RH candidate,
model-to-actual transfer, conditioning bound or real-spectrum
sufficiency theorem is asserted. Literature uses no mathematical
exploration allowance; supervisor counters and routing remain external.
