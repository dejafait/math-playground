# First theta summand as a signed reference: finite-truncation obstruction

TARGET: Assess primary coverage and recorded obstructions for using the n=1 theta summand as an actual-coefficient reference, seeking a signed minor comparison with a remainder threshold uniform in the minor order.
CHECKED: 2026-11-05
DECISION: IMPORT
SEARCH_EVIDENCE: Step571 checked the full-first-summand/cumulant assessments, L234's complete proof, the step551 stop, and exact Pólya/finite-theta/perturbation terminology; recovered Pólya's original 1926 paper and read its finite-truncation statement, rather than relying on a search snippet or a modified-kernel real-zero theorem.
SOURCE_EVIDENCE: Pólya, Acta Math.48 (1926),305–317, DOI10.1007/BF02565336, (3) p.305 and Section4/HilfssatzI with its proof and following finite-truncation paragraph pp.315–316; Hladík arXiv:1709.07629v1 PDF, Sections1–2/Theorem2 pp.2–4 and Section7/Theorem22 pp.15–16. Exact source scopes and read limits are below.
COMPARISON: Pólya explicitly assigns infinitely many zeros but only finitely many real zeros to finite sums of the full theta summands, including a single term. This defeats an all-real-reference premise, subject to the local scalar match; it does not determine any specified coefficient minor. Finite-matrix perturbation radii retain reference-sign and conditioning hypotheses and provide no order-uniform theta margin.
GAP: A local citation/normalization closure remains; individual reference-minor signs, a sufficient signed actual-minus-reference comparison, useful order dependence and mixed/edge transfer remain unresolved. No inspected theorem supplies those missing estimates.
REASON: Park the proposed all-real first-summand reference and close its exact known obstruction by citation in existing L234, without duplicating its endpoint proof. A different signed mechanism must explicitly accommodate the reference's nonreal zeros; no general ban on finite-order comparisons is inferred.
LITERATURE_REASON: At invocation the target changed from a covered finite-order import to a first-summand reference and an order-uniform signed comparison without essential primary coverage. This review resolved the reference-obstruction scope and checked finite perturbation hypotheses; no ready-target search was repeated to fill a quota.
SCOPE: Completed literature-only source comparison; no reference-sign derivation, determinant experiment, lemma or mathematical script. IMPORT concerns the known obstruction, not the desired positive comparison. The separate narrow import nomination needs next-turn approval.

## Original nomination, retained as scope history

The pending-gate wording below describes the invocation-start nomination;
the completed source decision above and comparison below supersede it.

Main gap: actual-Xi all-degree mixed positivity. The proposed intermediate
object is the n=1 summand already displayed in L019,

\[
 K_1(u)=(8\pi^2 e^{9u/2}-12\pi e^{5u/2})e^{-\pi e^{2u}},
 \qquad u\ge0.
\]

The proposed reference uses its moments with the same ordinary
coefficient normalization as L776. No real-zero or minor-sign theorem
for this reference is assumed. A successful independently sufficient
signed comparison might give an actual input beyond fixed-order sector
positivity; the other indices, mixed regimes and full bridge would
still require explicit justification. No claim that such a comparison
exists is made.

Continuation test: locate inspected primary hypotheses for the reference
sign and a relative minor perturbation mechanism, and identify a bound
whose required margin is independent of the minor order or has a stated
usable order dependence. A scalar moment error, positive kernel tail,
unqualified real-zero assertion or mere restatement of the actual
determinant sign fails this test. Park this reference if known failures
already cover it or no independently testable sufficient threshold can
be specified. Do not use the existing absolute-tail stops as a global
ban, or reopen them without a materially changed signed estimate.

Start with narrowly targeted duplicate searches for the single-summand
reference in local literature/ATTEMPTS. Reuse the theta signed-integral
assessment, `2026-11-05-theta-signed-mechanism-bounded-discovery.md`,
L811's accepted envelope qualifications and the step551 reference stop.
Load full canonical proofs only for a load-bearing overlap. Primary
reference-sign and perturbation theorems must be read before any later
mathematical nomination. No broader source passage or sibling notebook
is needed for orientation.

Essential input IDs: L019/L021/L776 definitions. L811, L808 and L813 are
comparison evidence, not sign premises for the new reference. Unresolved
assumptions are its real-zero/minor-sign property, a signed relative
comparison and usable degree uniformity. Full matching Mathlib coverage
is unchecked. No cross-notebook input is proposed. A creative attempt
cannot yet be nominated responsibly; these essential hypotheses must
first have an independently checkable formulation and source assessment.

## Preserved working source checkpoint — step571

Literature-only review in progress. Narrow duplicate checks found the exact
full first-summand base in the completed step393 Nuttall assessment, but
its observable is a cumulant Wronskian, not L776 coefficient minors.
Pólya-type real-zero approximations read so far replace the exponentials
by cosh terms and are different kernels. The geometric gamma approximants
in bramble_trace paper96 are also different; their zero theorem is not
an input for this reference. No local reference sign, boundary derivative,
minor perturbation inequality or new mathematical result has been derived.
A possible next diagnostic is the half-line Fourier endpoint contribution;
its exact applicability and source scope are still being checked.

## Completed comparison — step571, 5 November 2026

Main gap: actual-Xi all-degree mixed positivity. The reviewed intermediate
target was a first-summand signed reference plus an order-uniform relative
minor margin. Such a comparison could pay one actual-coefficient regime;
other indices and mixed/edge transfer would remain. The continuation test
required independently supported reference signs and a usable relative
threshold. The all-real-reference branch fails the source test below.
This is an informative known-result overlap, not new mathematics or an
impossibility theorem for every comparison using this summand.

### Exact primary obstruction

G. Pólya, *Bemerkung über die Integraldarstellung der Riemannschen
ξ-Funktion*, Acta Mathematica **48** (1926),305–317,
[DOI10.1007/BF02565336](https://doi.org/10.1007/BF02565336),
[original primary PDF](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/5376-11511_2007_Article_BF02565336.pdf),
Section4, HilfssatzI and the immediately following paragraph, pp.315–316.
Read (3), p.305, for the full summand, and all of HilfssatzI's proof and
the finite-sum application. The original PDF text was legible for these
hypotheses and the finite-sum statement; its equation OCR is imperfect.
[Tim Hosgood's translation](https://translations.thosgood.net/AM-48-1926-305.html),
Section4, was used to cross-check the displayed formulas. Screenshot
requests produced no inspectable images; no visual verification is claimed.

HilfssatzI assumes F analytic and real-valued along the nonnegative real
axis, u^2 F^(j)(u) tending to zero for every fixed j>=0, and F not even.
It states that its half-line cosine transform is nonzero for sufficiently
large real arguments. The complete proof selects the first nonzero odd
origin derivative and uses repeated integration by parts with an integrable
derivative remainder. The next paragraph explicitly applies this to any
finite sum of the full summands in (3): the transform is entire with
infinitely many zeros, but only finitely many real zeros. The assertion
of infinitely many zeros invokes Hadamard theory briefly; it is an imported
source statement, not an independently completed proof audit here.

This is stronger and more directly applicable than a statement just about
the leading positive exponential. The full polynomial factor in (3) is
retained. A single summand is within the source's explicit finite-sum
scope. The remaining local operation is to match its scalar convention
with L019 and the half-line/even-Fourier conventions of L234. That operation
is reserved for the next import turn. No boundary derivative or new
reference zero theorem was calculated in this literature step.

The source's older word “imaginär” must be understood here as nonreal,
not as a certificate of zeros on the imaginary axis. Only “infinitely
many zeros, finitely many real” is needed. This determines no actual-Xi
zero and no particular D_(r,k) of either kernel. In particular, this
review does not infer that every edge minor of the reference is negative,
nor use an unassessed coefficient-minor/zero equivalence.

Pólya's (5)–(6), pp.305–306, replace the exponentials by a reciprocal
even expression; the final note on p.317 retains both polynomial terms
but also changes the exponential to exp[-pi(e^(2u)+e^(-2u))]. Those
real-zero statements concern different kernels. Replacing the proposed
K_1 by either of them would change the target and require a new review.

### Perturbation scope and usable thresholds

Milan Hladík, *Tolerances, robustness and parametrization of matrix
properties related to optimization problems*,
[arXiv:1709.07629v1 PDF](https://arxiv.org/pdf/1709.07629v1),
PDF internal date19 October2018 (arXiv label22 September2017),
Section1 regularity radius pp.2–3; Section2 Theorem2 and its complete
proof p.4; Section7/Theorem22 pp.15–16. The HTML mirror carries a different
generated date, so this citation binds to the identified PDF.

Theorem2 starts with a finite real matrix A with det A>0. The radius
preserving that sign under every strict norm-bounded perturbation is
the distance r(A) to singularity; the proof includes the crossing along
the real line segment. For induced norms Section1 records
r(A)=1/||A^(-1)||; for spectral or Frobenius norm it is sigma_min(A).
Section7 assumes strictly positive minors of a finite square matrix,
not merely a nonnegative or potentially singular reference. Theorem22
reduces its total-positivity radius to the minimum regularity radius
of the initial submatrices. Read its initial-submatrix definition,
the reduction to positive determinants and the spectral/Frobenius case.
The underlying initial-minor characterization is cited there to Fallat–
Johnson, not independently reaudited here. No theorem is imported for
the actual coefficient matrices.

Thus there is a concrete finite threshold, but it depends on each
reference matrix and its submatrices. The source supplies no positive
lower bound uniform in the minor order, no actual theta remainder
estimate and no conversion of scalar moment closeness into such a
bound. Even one-matrix use retains an independently positive determinant
and a bound below its regularity radius. These are the missing inputs,
not an automatic sign consequence of a small positive kernel tail.
The structured signed comparison originally sought remains unpaid.

### Duplicates and recorded failures

Read L234's full canonical proof. It already establishes a positive
origin derivative for every raw finite truncation, an eventual negative
Fourier tail and a negative first-associated spectrum. Its infinite
theta cancellation and N-dependent onsets explicitly preclude passing
that obstruction to the full K. Do not calculate that endpoint again
or create a duplicate lemma merely to record this review. The Pólya
finite-sum zero statement supplies an exact primary precedent for the
proposed reference's global zero premise; its citation can be added to
the existing canonical discussion after the normalization check.

Reuse step393's full-first-summand cumulant assessment and step402's
all-order comparison qualifications. Nuttall's cumulant/Wronskian
observable is different from the factorial-normalized coefficient
minor; no new review of its already assessed proofs is needed. L811's
complete proof confirms an envelope denominator only. L808's complete
finite reference proof and step551 ATTEMPTS record concern a distinct
two-node Gaussian law; that negative pair is not used as a premise for
K_1. L813 remains a finite-order actual-coefficient comparison only.
All these scopes and unfinished work are preserved.

The geometric reciprocal gamma approximants of bramble_trace,
*Nonreal zeros of geometric gamma approximations to the Riemann xi
function*, [paper96](https://rstation.ai/problems/riemann_hypothesis/papers/96),
v1,2 November2026, were checked only through Section1/(1)–(4) and
Theorem1 to identify their object. Their geometric completion of finite
gamma convolutions differs from a raw finite theta sum. Their theorem,
proof and numerical supplement are not imported or audited. Shi,
[arXiv:1502.06844](https://arxiv.org/html/1502.06844), Section3/(3.1)–(3.2),
was likewise used only to identify the changed cosh kernel before following
Pólya's original source. Neither is evidence for a sign of K_1 minors.

### Decision and continuation

Outcome NEGATIVE: primary coverage changes the route decision from seeking
an unqualified all-real first-summand reference to parking that premise.
No progress beyond the checked sources is claimed. Do not spend a
mathematical turn reproving its already recorded endpoint failure.
The remaining useful closure is a narrow known-theorem applicability
check and canonical citation, nominated separately in
`2026-11-05-polya-first-theta-obstruction-import.md`. No new lemma is
needed for that task. A different finite-order reference comparison is
not excluded, but would need an independent signed margin and explicit
order scope. A creative central mechanism is not yet justified: no
sufficient signed functional accommodating the nonreal reference zeros
has been specified. Scheduling preference supplies no such hypothesis.

Essential continuation inputs: L019/L021/L776 definitions and L234's
existing proof. L808/L811/L813 are comparison evidence only. Actual-Xi
signs, all coefficient-minor signs of the reference, order-uniform
compensation and mixed/edge transfer remain unresolved. Full matching
Mathlib coverage is unchecked. No cross-notebook input is used.

Queries included `Polya Riemann xi first term theta kernel Fourier transform
real zeros incomplete gamma 1926`; `"theta" "first term" "Pólya"`;
`Toeplitz minors perturbation relative error total positivity uniform order
theorem`; `"Pólya" "first term" "nonreal" kernel`; `"Riemann" "first
summand" zeros`; `"Bemerkung" "Integraldarstellung" "doi"`; and the
exact German title with `pdf`. Search results were leads only. DLMF2.3(i),
(2.3.4)–(2.3.6), including the infinite-endpoint hypotheses, was inspected
as a possible endpoint diagnostic before the exact Pólya statement was
found; no specialization was performed. Hadamard lecture-note results
were located but are unnecessary for this citation import; no independent
Hadamard proof audit is claimed. Failed Euclid/download requests did not
block access to the recovered original PDF.

Local searches were confined to active-notebook literature/ATTEMPTS,
then exact matches in lemmas for the finite-truncation precedent. Initial
status/search outputs were oversized and were not treated as exhaustive
evidence; subsequent reads used identified paths. No mathematical script,
lemma, DAG or PROOF argument changed. This step spends zero mathematical
EXPLORATION turns and resets no historical budget or supervisor state.
