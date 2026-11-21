# Complete associated-kernel Gaussian-mixture source review753

TARGET: Assess whether L233's complete actual associated kernel admits A(t)/A(0)=integral_[0,infinity) exp(-a*t^2)dnu(a) with nu a positive probability measure, checking primary Schoenberg/Bernstein hypotheses and actual theta-tail constraints before nominating one bounded analytic test.
CHECKED: 2026-11-13
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Exact associated-kernel/Gaussian-mixture and completely-monotone decay searches, primary Bernstein theorem/proof retrieval and Schoenberg proof comparison completed753; precise queries, reading limits and local duplicate comparisons below. No novelty inferred from failed exact searches.
SOURCE_EVIDENCE: SSV, Bernstein Functions, 2nd ed.(2012), Definition1.3, Proposition1.2, Theorem1.4 with full proof, printed pp2-5; Khoshnevisan(2005), Schoenberg's Theorem and Section2 pp1-4; Csordas arXiv:1309.0055v2, Definition1.2, Theorem3.5 with both intervals, (4.2), Theorem4.5 and proof. Direct links and qualifications below.
COMPARISON: Bernstein covers the exact positive-measure class after the square-variable substitution; Schoenberg requires every Euclidean dimension, not line positivity. Csordas supplies complete associated-kernel admissibility with a super-Gaussian tail. These known inputs favor one tail-exclusion specialization rather than constructive mixture fitting; no actual-A exclusion is established here.
GAP: Verify finite nonzero A(0), exact theta-to-source rescaling and the inherited complete tail; compare that bound with the bounded-mass lower bound forced by any probability measure on finite nonnegative scales. These applicability and elementary measure steps remain for a mathematical turn; first-spectrum and higher/mixed signs remain unresolved.
REASON: Essential coverage is now available for a single ordinary specialization. Cite the known representation and admissibility theorems; prove only the exact applicability and elementary comparison, without redoing their general proofs or enlarging the sufficient class.
LITERATURE_REASON: The function is complete A as a function of t^2, rather than the direct kernel k, reciprocal Xi density, auxiliary Cauchy transform or S3 operator block. Existing assessments do not cover its positive Gaussian-scale-mixture hypothesis.
SCOPE: Completed source review of this exact sufficient class and actual-tail applicability; one later bounded specialization is nominated separately for approval. No general PD classification, parameter survey, approximate signed mixture, new lemma or mathematical script.

The invocation-start nomination paragraphs below are preserved as the
question reviewed; their imperatives do not report completed mathematics.

Main gap: L030-L032/C032a actual-Xi all-degree mixed positivity.
Intermediate target: the displayed positive representation for complete
A from L233, with k the even actual theta kernel of L019/L020.
Plausible downstream use: nonnegative first-associated spectrum through
L233, while higher signs, all-degree mixed transfer and global assembly
remain unresolved. A sufficient-class failure would not refute those
signs or RH.

Read the primary representation statement, exact measure hypotheses and
the essential necessity/sufficiency proof cases, then only the canonical
actual-theta tail evidence needed for applicability. Do not infer that
positive definite on the line means a Gaussian scale mixture. Retain
nu>=0, total mass one, finite nonzero A(0), a>=0 and every endpoint/atom.
Do not derive or approve a new tail estimate in this source turn.

Continuation test: known source coverage plus a specified complete actual
tail or derivative inequality giving one independently checkable pass/fail
test. If known tail restrictions already exclude the class, record the
precise applicability obligations for one later bounded specialization,
or import a fully matching theorem if it directly decides this object.
No failed approximate fit, finite derivative preview or sample spectrum
can decide the integral representation. Do not enlarge the class after
its first decisive obstruction.

Essential inputs: L019/L020/L233 for actual normalization and the complete
integral. L356 is parity-stop context only; L596 and its Cauchy-transform
source review distinguish a different variable and operation. No inherited
finite theta truncation, source certificate or numerical sign is assumed
verified. Mathlib matching/supporting coverage is unchecked. No cross-
notebook input. This is an unassessed lead, not a creative proof nomination;
missing essential source coverage must be paid before mathematics.

## Completed primary coverage753

René L. Schilling, Renming Song and Zoran Vondraček,
*Bernstein Functions: Theory and Applications*, 2nd revised and extended
edition, de Gruyter Studies in Mathematics37(2012),
[publisher preview](https://api.pageplace.de/preview/DT0400.9783110269338_A19166479/preview-9783110269338_A19166479.pdf),
Definition1.3/Proposition1.2, p2, and Theorem1.4/proof, pp3-5
(PDF pages16-19). The criterion is C-infinity on (0,infinity), with
(-1)^n f^(n)>=0 for every n>=0. It is equivalent to a unique positive
measure on [0,infinity) with finite Laplace integrals at every positive
argument. Finite f(0+) fixes its total mass. The proof handles normalized
vanishing data, finite mass, shifts for unbounded data, the constant term
as an atom at zero, and dominated differentiation in the converse.
All these cases were read, not only the theorem statement. Its measure
need not have a density or finite moments at zero. The
[author's 2012-edition errata](https://www.motapa.de/bernstein_functions/misprints-ssv-2nd.pdf)
were checked; the p6 integration-variable correction is outside these
passages. No bound for actual A follows without specialization.

Davar Khoshnevisan, *Schoenberg's Theorem via the Law of Large Numbers*,
author note dated29April2005, marked NOT FOR PUBLICATION,
[primary proof](https://www.math.utah.edu/~davar/PPT/SCHOENBERG/Schoenberg.pdf),
unnumbered Schoenberg's Theorem, p1, and Section2, pp2-4.
This author proof was read through its conclusion. For continuous radial
f, positivity on R^n is required for every n, as Section2 explicitly
states. Normalized data correspond to a probability mixture
exp(-t^2*s/2). The sufficiency case uses Gaussian characteristic functions;
necessity uses consistent radial measures, exchangeability, de Finetti,
the law of large numbers and dominated convergence. Continuity at zero
removes escaped mass at infinite scale. This supplies checked proof
coverage for the dimension qualification, not a local reproof or an
inference from positive definiteness on R alone.

The original is I.J.Schoenberg, *Metric Spaces and Completely Monotone
Functions*, Ann.Math.(2)39(1938),811-841, Theorem2, p817,
[DOI](https://doi.org/10.2307/1968466). Its original proof was not read.
The accessible Wisconsin scan instead contains *Metric Spaces and
Positive Definite Functions*, Trans.AMS44(1938),522-536. Its body was
not text-extracted; screenshot responses supplied placeholders, not
inspectable evidence. Neither scan nor a search snippet is used to claim
original-proof coverage. The inspected independent author proof and
SSV criterion suffice for this target; there is no essential blocker.

George Csordas, *Fourier transforms of positive definite kernels and
the Riemann xi-Function*, arXiv:1309.0055v2,21February2014,
[primary text](https://arxiv.org/html/1309.0055v2), Definition1.2, p2;
Theorem3.5/proof, pp6-7; (4.2), p9; Theorem4.5/proof, p11.
Admissibility includes strict positivity, evenness, smoothness and
O(exp(-|t|^(2+epsilon))) decay for some epsilon>0, including derivatives.
Theorem3.5 transfers admissibility from a strictly log-concave admissible
kernel to each complete associated kernel. Its monotonicity proof treats
0<s<t and s>t separately. Theorem4.5 applies this to the full theta
kernel. Read those cases and its use of Theorems4.1/4.2; reuse the earlier
recorded shape coverage rather than reopening concavity proofs. The
tail inheritance is asserted as immediate in Theorem3.5, not expanded
there. No Fourier-sign conclusion is contained in admissibility.
Positive scaling and a change of argument must still be checked against
L019/L233; this review does not perform the associated-integral rescaling.

## Local comparison, source limits and bounded nomination

L016/L019/L020/L233 were read in full. L019 supplies a bound of the form
C exp(9|u|/2-pi exp(2|u|)) for actual k; L233 supplies continuity and
weighted absolute integrability of complete A, and its exact Fourier
interface. No A-tail bound or normalization proof was derived here.
The relevant complete proofs of L234 and L239 were also read: finite-N
endpoint tails and frequency-sector bounds do not decide this real-axis
mixture class. Existing changes to L234 were preserved.

Reuse [September27's associated-lattice assessment](2026-09-27-first-associated-theta-lattice.md)
and [October31's Cauchy assessment](2026-10-31-associated-theta-cauchy-second-derivative-review.md)
for their recorded shape coverage and distinct operations. The parity
review concerns spatial cosets. L233's comparison mixture is for k,
whereas the present representation is for complete A. L232's normalized
theta Laplace test and the L022 generic positive-kernel counterexample
concern different objects; their failure records were checked. No
matching actual-A mixture theorem was found in the bounded search;
that does not establish originality. L356 is contrast only and was not
used as an input. No sibling notebook or external-input register was
needed: no zero-free-region or reciprocal-series claim is proposed.

Queries included `Schoenberg 1938 Metric spaces completely monotone
functions theorem 2 pdf`; `Schilling Song Vondracek Bernstein functions
theorem 1.4 completely monotone Laplace transform pdf`; `"Riemann"
"associated kernel" "Gaussian mixture"`; `"associated kernels"
"completely monotone" theta`; `"completely monotone" "decay"
"exponential" theorem`, followed by exact-title/author access searches.
The SSV2010 mirror timed out and shell downloads failed DNS. The
accessible publisher's SSV2012 preview resolved the needed coverage.
Mimica's *Exponential decay of measures and Tauberian theorems*,
introductory pp1-3, was inspected as a possible lead; it concerns the
tail of the representing measure under additional hypotheses, not the
tail of A. Its theorems are not imported. Unrelated search hits were
not promoted to evidence. Full matching/supporting Mathlib coverage
remains unchecked.

The one nominated mathematical test is source specialization followed
by a positive-measure tail comparison. Verify 0<A(0)<infinity and carry
Csordas's exact complete-kernel normalization through the integral.
Then test the sourced super-Gaussian upper bound against the lower
bound forced by positive mass on some bounded interval of scales.
The bounded-interval mass argument, endpoints/atoms and the actual
comparison must be written in a later mathematical turn, not inferred
from a failed numerical fit. If contradictory, abandon only this
positive Gaussian-scale-mixture certificate. Failure of this sufficient
class says nothing negative about A's Fourier transform or RH. If the
source's tail cannot be specialized, name the exact missing hypothesis;
do not silently change to signed mixtures or weaken the target.

Outcome753: EXPLORATION, essential coverage completed and an analytic
test isolated; no representation, obstruction theorem, first sign or
new mathematical bound established. This is local source preparation,
not progress beyond the inspected mathematics. The new ready proposal
is [specialization753](2026-11-13-complete-associated-gaussian-tail-test-753.md)
and receives a separate approval next turn. Mathematical exploration
usage is zero. No creative central mechanism is justified by this
routine sufficient-class diagnostic; an independent actual sign input
remains the blocker. No lemma/script, PROOF or DAG changes occurred.
