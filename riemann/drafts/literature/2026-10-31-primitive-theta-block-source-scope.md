# Direct primitive theta-mode blocks: completed source comparison

TARGET: Assess a primitive-index block decomposition of L233's first associated spectrum using the half-axis summands of L019, with absolute convergence and the diagonal (1,1) block as the first sign test.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed the scoped primitive/gcd/coprime/diagonal-pair screen and exact/stronger-result web queries below. Read the complete L019/L233-L239 and L356 proofs and the parity stop; reused the September 27 lattice and October 31 factor/heat assessments. No inspected result states the full diagonal-family sign. This bounded finding does not certify novelty.
SOURCE_EVIDENCE: Durrett, Probability: Theory and Examples, author version 5 (11 January 2019), Theorem 1.7.2 and proof cases 1-4, printed pp.38-40, counting-measure corollary p.41; Csordas arXiv:1309.0055v2, Definition 1.2, Theorems 4.5-4.6 and Open Problem 4.7, printed pp.2/11-12. Reuse the previously inspected lattice statements; L356 supplies the directly relevant half-axis derivative envelope and infinite-block Fourier method.
COMPARISON: Ordinary positive-series/Fubini regrouping and the existing cusp calculation supply the tools, but not the diagonal infinite-family conclusion. L356 already rejects separate parity positivity; L234 rejects finite reflected sums. Neither permits taking an uncontrolled infinite sum of asymptotic remainders. No new positive representation or first sign follows from source review.
GAP: For the precisely nominated primitive-pair partition, justify the associated-kernel/Fourier interchanges and summable boundary remainders, then determine the full n=m family's eventual spectrum. Its sign, off-diagonal compensation, all-frequency total sign and higher signs remain unproved.
REASON: Coverage is sufficient for one bounded specialization of the established boundary-tail method. The diagonal family is independently testable without a regulator or an RH premise. No block identity, coefficient or sign is derived in this literature-only turn; the newly written mathematical continuation requires separate approval next turn.
SCOPE: Reflected half-axis k_n(u)=K_n(|u|), with K_n from L019; unordered primitive positive pairs a<=b, gcd(a,b)=1, common multiplier d>=1, retaining both ordered orientations when a<b and one when a=b=1. The full diagonal is n=m=d for every d>=1. No unreflected whole-line theta-mode interchange or assertion that this partition has nonnegative spectra.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED coverage lacked the grouping/convergence and complete-family boundary comparison. This turn supplies that essential assessment; it does not repeat literature on an already ready calculation.

## Completed review — 31 October 2026

The main gap is actual-Xi all-degree positivity at unbounded heights.
The intermediate target is a legitimate primitive-pair decomposition
of the first associated spectrum and its full diagonal-family sign.
Separate nonnegative block spectra would be a sufficient route to the
first sign only. The present review approves a test of that stronger
mechanism, not its mathematical premise.

### Local duplicates and failures

Read L019/L233/L234 in full, then the complete L235-L239 proofs.
L234's finite reflected sums have nonzero boundary derivatives and
negative first-associated tails. L235's smooth modular averages fail
L1 convergence. L236's smoothing changes the spectrum, while L237-L239
retain missing global threshold and zero-geometry hypotheses. None
supplies a sign for the proposed infinite diagonal family.

The heat and normalized-factor assessments point to the complete-parity
stop, which was read, followed by the full L356 proof. Its equation (1)
controls the sum of absolute half-axis derivatives of any fixed order,
including their polynomial-weighted integrals; (6)-(8) retain the
reflected boundaries, Fourier constants and infinite-block remainders.
Its conclusion is an eventually negative complete same-parity spectrum
with cancellation from the opposite-parity spectrum. It is the closest
existing method, not a theorem about primitive pairs. In particular,
nonnegativity of spatial summands does not imply a spectral sign.
The existing proof has been read for reuse; no new independent audit
of every L356 source is claimed here.

Exact term searches for gcd, coprime, primitive-index/primitive pair,
diagonal family and diagonal block in theta/associated/parity lemma,
attempt and assessment paths located this nomination, not a completed
diagonal-family test. The broader mode-pair search was bounded to the
relevant records. An initial overly broad local output was truncated;
no conclusion uses omitted output. Later exact files/ranges supplied
the load-bearing evidence. All pre-existing edits were preserved;
no cross-notebook mathematical input was read.

### Primary statements and applicability

Rick Durrett, *Probability: Theory and Examples*, author version 5,
11 January 2019, [primary PDF](https://math.duke.edu/~rtd/PTE/PTE5_011119.pdf),
Theorem 1.7.2, printed pp.38-40, and counting-measure corollary p.41.
Read the sigma-finite product-measure setup, theorem and proof cases
1-4: indicator sets, simple functions, nonnegative monotone limits,
and positive/negative parts under absolute integrability. Counting
and Lebesgue measures meet the space hypotheses. For an oscillatory
factor, apply the absolutely integrable case to real and imaginary
parts; the nonnegative case alone is insufficient. These are known
tools to cite, without reproof. The needed integrable majorants must
still be verified for the proposed partition in a research turn.

George Csordas, *Fourier transforms of positive definite kernels and
the Riemann xi-Function*, [arXiv:1309.0055v2](https://arxiv.org/pdf/1309.0055v2),
21 February 2014. Rechecked Definition 1.2 and Theorems 4.5-4.6/Open
Problem 4.7; reuse the prior lattice assessment's normalization and
proof coverage. Admissibility includes smooth even positivity,
strict decrease on the positive half-line and rapid derivative decay.
The first sign is posed as a problem; all associated-kernel positive
definiteness is the real-zero criterion. An individual reflected mode
must not be assumed admissible. Use L233's exact constants instead
of transplanting the source's differently scaled theta convention.
The dated open problem does not establish its status in 2026.

Reuse `2026-09-27-first-associated-theta-lattice.md` and the completed
parity assessment for addition and polynomial-Gaussian transformations.
They require common theta parameters or retain signed corrections;
neither is a primitive-pair spectral-sign theorem. No new Poisson,
Bessel or Mellin identity is needed for the proposed first diagnostic.

A specific search lead was inspected at its defining hypotheses:
bramble_trace, [rStation post23](https://rstation.ai/r/riemann_hypothesis/posts/23),
18 October 2026, updated 21 October, opening definitions and scope.
Its Bessel modes use a reciprocal cutoff and unequal scales. Reported
negative single-mode and full-cutoff examples concern that family,
not the reflected half-axis primitive family here. No certificate was
replayed or imported, and its more elaborate signed-Gram/trace claims
are not inputs. It supplies a relevant warning against diagonal or
all-cutoff positivity, not a citation deciding this target.

### Search record and next-step bounds

New web queries included:

- `"Riemann" "associated kernels" Csordas theta positivity`;
- `"theta" "kernel" "coprime" "Laguerre"`;
- `"Riemann" "diagonal" "theta" "Laguerre inequalities"`;
- `"Riemann" "theta" "primitive pairs" kernel`;
- `"theta kernel" "diagonal" "positive definite"`;
- `"Riemann xi" "gcd" "kernel"`;
- `"Laguerre" "theta" "coprime"`;
- `"theta" "associated kernel" "diagonal"`;
- `"Riemann" "primitive" "associated kernel"`.

These returned standard associated-kernel work, unrelated uses of
primitive pairs, and the cutoff lead above. Other snippets, proof
claims and repository indexes are not theorem evidence. No inaccessible
source is essential to the fixed boundary-tail test. No novelty or
absence of stronger literature is inferred from this bounded search.

The partition and diagonal restriction in SCOPE are a proposed object,
not a derived identity. The continuation must prove its convergence
with the reflected original summands, then control the infinite
diagonal's Fourier remainders before asserting a sign. It must not
identify a sum of self-pair spectra with the spectrum of a summed
kernel: the latter also contains cross terms.

A strictly negative full diagonal Fourier value or eventual tail
abandons separate positivity for every primitive family, without
refuting the full spectrum or RH. A nonnegative tail only passes this
test; all finite frequencies, off-diagonal families and higher degrees
remain. An unsummable remainder is inconclusive and must be saved,
not replaced by a finite-mode preview. The method is an established
boundary-tail specialization, so it is not labeled creative. A new
central sign mechanism still lacks independent inter-family
compensation data; the creative-routing preference does not justify
inventing such a premise.

Outcome: EXPLORATION, a completed actionable comparison, with no new
mathematical sign, representation or advance beyond checked sources.
No lemma, mathematical script, DAG or PROOF change. Mathlib coverage
for the full primitive-family result and supporting interchange/tail
specialization is not checked; no absence claim.

## Original nomination (completed status supersedes its gate)

## Mathematical purpose and bounded next review

The main gap is actual-Xi all-degree signs at unbounded heights. A
nonnegative block representation of the first associated spectrum would
be a useful intermediate input, while the higher-degree gap would remain
independent. Even the exact block decomposition needs checking before
its sign can be a legitimate mathematical target.

Begin with narrowly targeted duplicate/failure searches for theta-mode
pairing, index ratios, diagonal families, common-divisor regrouping and
even-reflection boundary terms. Compare the relevant L234-L239
truncation/cusp evidence and the actual-theta Fourier-determinant stop
before reading further proof ranges. Use L019/L233's exact normalization;
do not infer a full matching result from the generic product theorem.
Retrieve primary theorem hypotheses and relevant proof cases for any
suggested Mellin/Fourier grouping or positivity result. No cross-notebook
input or inaccessible optional letter is needed for this review.

The proposed later discriminating test is the sign of the diagonal
primitive (1,1) family's Fourier contribution, after its precise
definition and all exchanges have been justified. A rigorously negative
value or tail stops this blockwise sufficient mechanism only, without
refuting the full spectrum. A nonnegative answer for one block leaves
all off-diagonal families and their uniform summability unresolved. If
the existing cusp/truncation evidence already decides this target,
import that conclusion rather than reproduce it. If the grouping is
not legitimate, record that obstruction rather than calculate a preview.

No new block formula, lemma, estimate or mathematical script was derived
while nominating this target. A future creative mathematical attempt
would require ready source coverage and a precise bounded block test;
this nomination alone does not authorize it. Mathlib coverage for this
grouping is unchecked; no absence is asserted.
