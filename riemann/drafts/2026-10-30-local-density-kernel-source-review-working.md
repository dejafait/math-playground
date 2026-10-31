# Local-density aggregate kernel: source-review checkpoint

Literature-only step, 30 October 2026. The target is the supplied
variable-cutoff review. No kernel norm, new bound, counterexample,
lemma or mathematical script has been produced. Existing unfinished
work is preserved.

The main gap is actual-Xi all-degree mixed positivity. The intermediate
target tests whether L485 can enlarge C483a's controlled sector of
L471's sufficient negative-mass majorant. Even a successful sector
estimate leaves the complementary displacements, full negative mass,
individual-height signs and higher mixed forms unresolved.

## Evidence read and reused

Read L485 in full, including its restricted proof and qualifications;
L483 in full; C483a through its complete cutoff comparison and the start
of its audit; and L471's hypotheses/conclusion. The shared kernel was
already audited; no new identity or replay is needed in this review.
Reuse the prior restricted-source assessment and the joint-Blaschke
source notes and failure record. L485 proves only its stated indicator
estimate. Its proof repairs do not license general-weight (19).

Primary sources inspected online:

- Maples--Rodgers, *Bootstrapped zero density estimates and a central
  limit theorem for the zeros of the zeta function*, IJNT 11 (2015),
  2087--2107, arXiv:1404.3080v2 (4 June 2016),
  https://arxiv.org/html/1404.3080v2 and
  https://arxiv.org/pdf/1404.3080v2. Read Theorem 2.4 and Proposition
  2.5, printed p. 5; definition (8), p. 6; Corollary 4.2 with its
  step-majorant/tail definitions and proof setup, pp. 9--10; and
  (18)--(23), Lemma 4.3 and the final indicator/proof remarks, pp. 10--12.
  The earlier assessment already read the complete relevant proofs;
  reuse that coverage and L485's complete restricted replay rather than
  claim a new manuscript audit. All zeros are counted with multiplicity.
  The source has strict beta>sigma and 0<gamma_0<U. Proposition 2.5
  is a one-sided local count integrated on [0,T], with
  1<=H<=T^(1/4), fixed integer k and fixed 0<c<1/2. This step uses
  only L485's audited k=2,c=1/4 specialization. Neither the larger-c
  remark nor arbitrary-weight Lemma 4.3 is an input.
- Bui--Hall, *On the derivatives of Hardy's function Z(t)*,
  arXiv:2304.05178v1 (11 April 2023),
  https://arxiv.org/html/2304.05178v1, definition of Z in Section 1,
  definition of HARDY immediately before Theorem 3, Theorem 3, and
  Section 7's reduction. Reuse the complete ordinary-fourth-moment
  application already recorded in L471/L483/C483a, at orders
  (0,0,0,0). The source integrates on [0,T]; the existing dyadic
  application is retained. This is continuous, not zero-selected,
  short-window or correlated with a zero count. The versioned PDF
  fetch timed out; the HTML and existing assessment suffice, so this
  does not block the input.

The arithmetic proofs behind the cited count and fourth-moment
statements remain imports. Full matching Mathlib coverage is unchecked.
No cross-notebook result or fixed-half-plane premise is used.

## Bounded searches and overlap comparison

New queries (in addition to the explicitly reused joint-Blaschke
searches) were:

- `"Maples" "Rodgers" "zero density" local moments weighted zeta`
- `zeta zeros local density second moment weighted |zeta| squared near critical line`
- `"zeta" "zero density" "weighted" "local" "second moment" Maples Rodgers`
- `"zeta" "zeros" "(d^2" kernel density`
- `"Maples" "Rodgers" "Proposition 2.5"`
- `"zeta" "local zero density" "|zeta|"`
- `"zeta" "displacement" "kernel" "zero density" "second moment"`
- `"Maples" "Rodgers" "density" "weighted" site:arxiv.org`

These did not identify an inspected theorem for this B sum, or a
weighted strengthening covering its moving displacement and |Z|^2
factor. Search snippets, secondary RH claims and unrelated weighted
polynomial moments were not treated as theorem evidence. The exact
Proposition 2.5 search returned the primary paper's known count estimate.
No absence or novelty conclusion follows from the bounded searches.

Narrow local comparisons also checked the earlier fixed-displacement,
moving-cutoff and moving-cutoff-audit assessments and the aggregate
recovery stop. L483/C483a use a cumulative density count and a shell
supremum; they do not already use L485's integrated local second moment.
The joint-Blaschke failure requires weighted sparse control for a
different tool. L475's exponential envelope is preserved as an
obstruction to that tool. Neither stop rules out testing this new
count input; neither provides the proposed estimate.

## Application scope approved for a later calculation

The following is a proof plan and a list of obligations, not a derived
bound. Freeze T and delta, keep the original finite B sum, and group
displacements into dyadic bands with a truncated final band below 1/2.
Use the existing nonnegative kernel identity and attempt a local-count
majorant for each band. Apply only L485, the continuous fourth moment,
Cauchy--Schwarz and the finite L2 triangle inequality. The mathematical
turn must actually prove the band domination, all parameter bounds and
the final estimate.

Its local count must include the band's equality displacement. Compare
this to the source by lowering a strict beta cutoff within the allowed
1/2<=sigma<=1 domain; any decrease of the exponential saving is a cost
to retain, not an endpoint theorem to assume. Similarly, a closed
ordinate window can be compared by a strict enlargement, or by an
explicit almost-everywhere endpoint argument for the finite selected
set. Multiplicities and coincident ordinates must remain intact.

The source permits changing its base parameter to a fixed multiple of
T. The proposed calculation must place every shifted window start in
that base interval, set H from the required physical window length and
the logarithm of that same base, and verify 1<=H<=base^(1/4)
uniformly over the bands. No negative start, translation-invariant
moment theorem or fixed-H-only assertion may be assumed. If the
smallest proposed window falls below the H lower bound, enlarge it
and keep the cost. Clipping and singleton windows must preserve the
original B sum; padding is only an upper-bound operation.

Finite band summation and all Cauchy--Schwarz/width/height losses must
appear before comparison with T(log T)^3. It is permissible for the
estimate to fail the all-mesoscopic threshold. Demonstrating a
surviving bound-loss for a concrete admissible cutoff with
delta(T)log T tending to infinity would stop this particular
certificate, not refute the mass assertion or prove a sharp necessity.
No such calculation, saving or obstruction is established today.

Decision: SPECIALIZE for this bounded application. The cited results
cover the required count and continuous-moment inputs; the precise
geometry and scale comparison remain research obligations. No reproof
of their arithmetic content is justified. This is a known-tool
specialization, not a source-ready creative mechanism. A genuinely new
central mechanism still lacks a concrete weighted-correlation input.
