# First associated theta kernel: complete parity-block assessment

TARGET: Test whether the complete parity blocks n+m even and n+m odd of the first-associated theta lattice sum are separately positive definite after exact modular resummation, retaining all polynomial weights and boundary terms.
CHECKED: 2026-10-03
DECISION: SPECIALIZE
SEARCH_EVIDENCE: A separate target-specific search on 2026-10-03 checked exact first-associated parity blocks, characteristic transformations and weighted coset resummation; no matching spectral-sign theorem was located. A recent blockwise-positivity lead was read at theorem level and concerns a different spatial partition. Queries and reading limits are recorded below; the 2026-09-27 parent screening remains preserved.
SOURCE_EVIDENCE: NIST DLMF v1.2.8, 20.2.2–4, 20.7.14 and 20.7.31–33, 21.1, 21.2.5–6 and 21.5.9, https://dlmf.nist.gov/21.5#E9; Roehrig (2021), Definition 4.3, Lemmas 4.4–4.6 and Proposition 4.7 with proof, pp. 20–24, https://doi.org/10.1007/s40993-021-00272-y; Planat, preprints202608.1692.v1, §5 (38)–(39), Theorems 4 and 6, https://www.preprints.org/manuscript/202608.1692. Earlier Borcherds and Csordas coverage is reused from the parent assessment.
COMPARISON: Characteristic inversion retains phases and changes characteristics; the weighted modular theorem uses corrected homogeneous weights and a dual-coset sum. Neither signs the two integrated reflected blocks. Planat's stated obstruction partitions a growth integral into frequency-dependent spatial intervals, not these index-parity blocks. The existing L233–L235 and L254 failures do not already decide this complete first-level test.
GAP: Determine the signs of the two complete block spectra with every modular boundary contribution retained; a negative block refutes only their separate positive-definiteness certificate, while the sign of their total remains the main missing first-level input.
REASON: This recovery supplies the saved parity target's own literature turn, rather than relying only on its simultaneous parent screening. Cite the standard identities and specialize their actual weights, reflected boundaries and infinite-series estimates. The unchanged target is ready for a later research invocation; no block identity, asymptotic or sign is derived here.
SCOPE: The exact complete reflected blocks defined below, including coset bookkeeping, polynomial-Gaussian corrections, convergence and boundary cancellation, and an analytic Fourier-sign or negative-tail test; no replacement by spatial phase intervals, finite sums or whole-line modular averages.

## Separate review and search record — 2026-10-03

The earlier screening is retained in the
[parent assessment](2026-09-27-first-associated-theta-lattice.md)
and the dated history. This review preserves the original TARGET and
the candidate objects below. It reads the sources for that target
without calculating either block. The whole overview, DAG, checkpoint,
existing changes, L019, L233–L234, L254 and the relevant failed attempts
were inspected. There were no existing local working-tree changes;
other notebooks' unfinished changes were left alone.

Queries actually used included:

- `"Riemann" "associated kernel" parity theta`
- `"theta" "parity" "positive definite" "Laguerre"`
- `theta polynomial weighted Poisson summation cosets characteristics modular transformation`
- `Riemann Xi first associated kernel even odd theta sums positive definite`
- `"first associated" "theta" "parity"`
- `"theta" "parity blocks" "positive definite"`
- `"sym18081283" "Theorem"`
- `"A Theta-Kernel Reformulation" "blockwise" "blocks"`
- `"Nonlocal Cancellation" "Theta-Kernel" "Planat" preprint`

The exact searches returned no usable matching sign statement. The
weighted search led to characteristic formulas and adjacent modular
results; the recent obstruction lead was followed to an accessible
author preprint. This bounded search does not establish originality.

## Newly inspected statements and hypothesis comparison

**Parity and characteristics.** Read the live NIST DLMF,
version 1.2.8 (released 2026-09-15):
[20.2.2–4](https://dlmf.nist.gov/20.2#E2) distinguish half-integer,
integer and alternating sums, including the constant term.
[21.2.5–6](https://dlmf.nist.gov/21.2#E5) define characteristics
and their translation factor. The Riemann-matrix condition is in
[21.1](https://dlmf.nist.gov/21.1).

Read the full [21.5.9](https://dlmf.nist.gov/21.5#E9): an integer
symplectic transformation changes the characteristics and retains
the multiplier, determinant and quadratic exponential. It is an
identity, not a positive-definiteness preservation statement.
[20.7.31–33](https://dlmf.nist.gov/20.7#E31) explicitly exchange
theta 2 and theta 4 under inversion, while theta 3 maps to itself;
the stated square-root convention must be retained.
[20.7.14](https://dlmf.nist.gov/20.7#E14) is a common-nome product
identity. The actual scales vary separately with s+t and s−t, so
its direct substitution still lacks the required hypotheses.

This source comparison does not assert that the reflected parity
half-sums are separately smooth at zero. Their boundary behavior is
part of the test, not a consequence assigned from the full kernel.

**Weighted coset theorem.** Reused the earlier arbitrary-polynomial
formula and read the additional corrected-weight modular statement:
Christina Roehrig, *Siegel theta series for indefinite quadratic
forms*, Research in Number Theory 7, 45 (2021),
[version-of-record PDF, pp. 20–24](https://link.springer.com/content/pdf/10.1007/s40993-021-00272-y.pdf#page=20).
Definition 4.3 fixes the Fourier normalization. Lemma 4.5 retains a
finite Laplacian correction for a polynomial times a Gaussian.
Lemmas 4.4–4.6 and Proposition 4.7 with proof were inspected.
The proposition assumes a positive-definite integral symmetric
matrix and a polynomial corrected from the specified homogeneous
class; inversion gives a finite dual-coset sum with phase and
determinant factors. It gives no Fourier sign in the subsequently
integrated variable. Applying that proposition directly to the
uncorrected actual weight would require an applicability argument;
Lemma 4.5 remains the covered algebraic starting point.
No harmonicity, missing correction cancellation or integral
domination is imported.

**Recent obstruction: distinct blocks.** Michel Planat,
*Nonlocal Cancellation in a Theta-Kernel Decomposition of the Riemann
Ξ-Growth Derivative: An Obstruction to Phase-Aligned Blockwise
Positivity*, [author preprint v1, posted 25 August 2026](https://www.preprints.org/manuscript/202608.1692),
DOI 10.20944/preprints202608.1692.v1. Read §1.3's scope, §5
(38)–(39), Theorem 4 and proof, and §7 Theorem 6 and proof.
Its blocks are J_m=[mπ/x,(m+1)π/x] in a longitudinal/transverse
decomposition of a growth derivative at y>0. Theorem 6 states a
negative-block conclusion under a strictly increasing envelope on
a compact interval, using Theorem 4's uniform asymptotics.
Those are spatial oscillation intervals, not restrictions on n+m.
No equivalence with the saved A_ε blocks is supplied, so this is
neither a sign theorem nor an imported obstruction for this target.
Its correctness is not independently certified here; no mathematical
input or broader research prohibition is taken from it.

**Access and reuse.** The publisher page, PDF route and DOI for
Planat's *A Theta-Kernel Reformulation of Riemann-Ξ Growth and the
Obstruction to Blockwise Positivity*, Symmetry 18 (2026), 1283,
[published link](https://doi.org/10.3390/sym18081283), returned access
errors. Its older [preprint v1, posted 1 June 2026](https://www.preprints.org/manuscript/202606.0062)
was read in §§3.3 and 6.2, Theorems 2 and 4; it formulates a global
growth-integral positivity problem. The revised published text is
an unread lead, and no theorem-level claim about that version is made.
Further retrieval is parked. The saved parity test depends on the
accessible transformation sources, not either Planat theorem.

The parent assessment's Borcherds Lemma 3.2/Corollary 3.4 proof and
Csordas associated-kernel criterion are reused with their recorded
qualifications. Freitag and the DLMF book references were not
separately read; no additional result from them is invoked. Mathlib
lookup was not needed. No essential source gap remains for this
bounded specialization, and no full-target positivity theorem has
been imported.

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

Within the unchanged target, the first diagnostic is to examine the
complete parity half-sums' right derivatives at zero and control the
corresponding Fourier boundary remainders. L234 supplies the method
for finite reflected sums; its conclusion must not be transferred
without estimates for the infinite parity sums. Exact resummation
must preserve these boundary terms. This is a proposed test only:
no derivative, block transform or sign has been computed here.
An analytic negative tail would end the separate-block certificate;
if that diagnostic is inconclusive, only a specified global
compensation bound would justify continuing the same implementation.

The review adds source-scope information, not a mathematical advance.
It leaves all-level positivity through |x|≤10, qualified nonreal-center
exclusion through |x|≤40, and the unbounded low-index and endpoint
gaps unchanged. No RH candidate is recorded. This literature-only
turn spends no calculation turn and resets no exploration count.

## Mathlib

Full-target and supporting coverage: **not checked**. The external
identities cited in the parent assessment are supporting statements;
no library theorem is claimed to sign the complete parity blocks.
