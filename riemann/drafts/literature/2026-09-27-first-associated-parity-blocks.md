# First associated theta kernel: complete parity-block assessment

TARGET: Test whether the complete parity blocks n+m even and n+m odd of the first-associated theta lattice sum are separately positive definite after exact modular resummation, retaining all polynomial weights and boundary terms.
CHECKED: 2026-09-27
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Screened as the concrete specialization of the saved full-lattice review; searches for associated theta kernels, parity, Poisson summation and polynomial Gaussian transforms found no theorem signing these two actual blocks. The full query and source record is in 2026-09-27-first-associated-theta-lattice.md.
SOURCE_EVIDENCE: DLMF 21.6.8 and 21.5.8; Roehrig (2021), Definition 4.3 and Lemmas 4.4–4.5, pp. 20–22, https://doi.org/10.1007/s40993-021-00272-y; Borcherds, author-hosted manuscript, Lemma 3.2, pp. 11–12, https://math.berkeley.edu/~reb/papers/aut/aut.pdf. Statements, parameter conventions and the polynomial-transform proofs were inspected in this literature-only turn.
COMPARISON: The sources cover coset bookkeeping and the full polynomial-Gaussian transform, not nonnegative Fourier spectra of these integrated parity blocks. L233 treats a generic first kernel, L234 finite truncations, L235 finite modular averages, and L254 second-level fixed-pair swaps; none states the complete first-level parity-block test.
GAP: Determine the signs of the two complete block spectra with every modular boundary contribution retained; a negative block refutes only their separate positive-definiteness certificate, while the sign of their total remains the main missing first-level input.
REASON: This bounded specialization tests a full arithmetic regrouping with accessible standard inputs. It was screened within the parent representation review and is ready for a later research invocation; no block identity, asymptotic or sign has been derived in this assessment.

## Fixed target and source boundary

Use exactly q_n(u) and k_n(u)=q_n(|u|) from L254; these are the
positive half-line summands of L019 and their even reflections.
The two candidate blocks to be tested, for ε=0,1, are defined by

\[
 A_\varepsilon(t)=\int_{\mathbb R}s^2
   \sum_{\substack{n,m\ge1\\n+m\equiv\varepsilon\pmod2}}
       k_n(s+t)k_m(s-t)\,ds.
\]

This fixes proposed objects, not a newly proved representation or sign.
Before using their spectra, justify convergence, the decomposition
of A, Fourier interchanges and all differentiation in the intended
normalization. The target is the complete infinite grouping, not a
finite numerical lattice section. A modular rewrite must represent
these same reflected blocks; replacing them by an unreflected summand
or another averaging prescription would change the target.

The [parent assessment](2026-09-27-first-associated-theta-lattice.md)
records the theorem-level reading and applicability limits. A general
matrix Gaussian allows the unequal scales; the common-parameter
addition formula cannot be substituted directly. Keep the polynomial
correction, determinant, zero-frequency contributions and characteristic
phases in a resummation. Pointwise-in-parameter Poisson summation does
not supply domination over the subsequent unbounded integrals.
No essential source gap remains for this algebraic specialization.

## Relevance, redundancy and decision test

The main gap is global actual-theta Laguerre positivity, with first
level given exactly by L233. Separate positive definiteness of both
blocks would be a sufficient route to that first level; it is not
asserted to be necessary. The other low Laguerre signs required by
L320 would remain unresolved even if this test succeeds.

This grouping retains infinitely many cross terms within each parity
class, beyond the fixed-pair grouping previously stopped in L254.
It does not make L234's boundary-jump issue disappear automatically:
verify the modular boundary terms of each block, instead of assigning
the cancellation for the total kernel to every part. L235 also prevents
using compact convergence alone to justify a whole-line transform.
L355's generic positive-kernel model supplies no sign for these actual
arithmetic blocks.

Continue this implementation only with a proof that both spectra are
nonnegative for every real frequency, or a concrete residual estimate
E(x)≥−P(x) for a specified nonnegative main spectrum P(x). If a block
has a rigorously negative spectrum, stop the separate-block certificate
and retain the result's limited scope. If the transformation only
reproduces the original unsigned spectrum, stop without presenting the
identity as an advance. No extension of any sign or zero-exclusion
range follows from this review alone.

The standard transformation algebra is covered literature and should
be imported. Verifying its actual weights, convergence and block signs
is the remaining specialization; this assessment establishes no
originality. It belongs to the same exploration streak as the parent
review. The sole current action and count are kept in PROGRESS.md.

## Mathlib

Full-target and supporting coverage: **not checked**. The external
identities cited in the parent assessment are supporting statements;
no library theorem is claimed to sign the complete parity blocks.
