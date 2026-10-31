# Actual negative-part harmonic majorant: completed source comparison

TARGET: Review whether a nonzero f in L504's H_a can have a nonnegative harmonic majorant of max(0,-Re f) on the upper half-plane outside its finite obstacle.
CHECKED: 2026-10-30
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched the exact linear-negative-part and exponential-type majorant question and the strict sector Phragmen--Lindelof terminology; checked the named parent assessments, L504 definitions, L506 stop and narrowly searched L502/L504 and the positive-class assessments for duplicates. Retrieved primary sector statements and proofs; no exact finite-obstacle theorem was identified and no originality is inferred.
SOURCE_EVIDENCE: Reuse ABR, Harmonic Function Theory, second edition corrected 17 July 2020, Theorem 7.26 pp. 158--159 from the parent assessment; additionally inspected Theorem 3.4 and its open-ball proof p. 47. Read Demkowicz, Lecture Notes on Non-Self Adjoint Operators and Related Topics, 4 December 2024 PDF, Theorem 3.9 and proof, printed pp. 42--43. Costin's current course PDF independently gives Theorem 205, printed pp. 107--108, rather than the indexed older Theorem 41.1.
COMPARISON: Positive harmonic representation and the strict sector theorem cover standard inputs for testing a restriction above the obstacle, without constructing an extension through it. They do not directly state nonexistence for L504's Fourier class. Logarithmic Cartwright/Nevanlinna majorants and the stopped exponential-envelope calculation do not decide the linear question.
GAP: The local specialization remains unwritten: test vertical growth of a putative majorant together with the harmonic real part, verify the role of evenness/reality, and apply a pole-free polynomial normalization in quadrants with strict order margin. No existence, nonexistence, H_a nonemptiness or truncation-cost result is established in this literature step.
REASON: Essential source coverage for this bounded application test is now available; a compact-obstacle extension theorem need not be assumed by the proposed restriction test. Mathematical applicability must be proved separately. This replaces an uncovered question with a source-supported specialization, without repeating L506's envelope mechanism.
SCOPE: Source comparison only in this completed turn; a subsequent separately approved research step may test the exact conditional majorant question by restriction above the compact obstacle and the cited classical growth principles. No source reproof or new general majorant theorem is needed.

## Exact question and essential inputs

Use L504's definitions and smooth Fourier class, with fixed R>0 and
fixed T>exp(1), a=log log T/pi, b=a/4, B=log T/(4pi), and
O=[-a,a] times [b,B]. Let

    Omega_infinity={(x,y): y>0} minus O,
    n_f(x,y)=max(0,-Re f(x+iy)).

For a fixed nonzero f in H_a, ask whether there exists a finite-valued
nonnegative harmonic function G on Omega_infinity such that G>=n_f
everywhere there. There is no imposed growth or boundary-continuity
condition on G. Keep the entire-function, evenness, reality, smooth
Fourier-support and continuum-rectangle hypotheses of H_a. Membership
is conditional: this question does not assume or prove that H_a is
nonempty. Do not silently replace the finite obstacle by a whole strip
or half-plane, or replace a linear negative part by log|f|.

L506 is contrasting evidence only: its positive top-envelope cost
diverges, but this is not an input proving anything about n_f. L504's
definitions and real Schwartz/Fourier representation identify the
function class. No conclusion of L503 or cross-notebook theorem is an
input. No dependency node is being proposed or added.

## Bounded review and decision test

Retrieve primary statements and essential proof cases about positive
harmonic majorants, differences of positive harmonic functions and
Hardy/Cartwright classes that genuinely address this *linear* negative
part. Reuse the inspected ABR representation instead of reopening its
general proof. Check whether any applicable theorem handles removal of
a compact obstacle; if not, identify precisely the missing extension or
growth hypothesis for a separately gated test. Hardy/Cartwright
terminology is a search lead, not an imported result or a proposed
logarithmic substitute. Inspect the exact theorem before assuming that
Fourier symmetry supplies an obstruction.

The discriminating result sought is applicable coverage proving or
excluding existence of G under these exact hypotheses, or one concrete
uncovered intermediate claim with an independently testable threshold.
If sources cover only log-modulus, whole-half-plane positivity or the
already stopped uniform envelope, park those leads and report the
missing condition; do not repeat qualitative Phragmen--Lindelof theory.
Do not infer actual finite-truncation cost divergence from nonexistence
of G without a separately justified comparison/compactness argument.

Downstream use is to decide whether a linear negative-part harmonic
majorization can support the positive-class Q estimate at all, before
trying to remove actual outer-boundary costs. A majorant obstruction
would concern that barrier method, not the Q inequality itself. A
majorant's existence would still leave quantitative weighted costs,
bottom kernels, T-uniformity, realization and actual-Xi signs open.
The RH gap remains all-degree positivity and initial signs at unbounded
heights. No justified creative central construction is yet available
from this nomination. Matching Mathlib coverage is unchecked.

## Completed bounded search and inspected coverage

Queries on 30 October 2026 included `harmonic function harmonic majorant
absolute value half plane Fourier transform positive frequencies Paley
Wiener`, `harmonic majorant real part entire function exponential type
half plane polynomial growth Fourier support theorem`, `"harmonic
majorant" "negative part" entire exponential type`, `"real part"
"harmonic majorant" "entire" "Phragmen"`, and `Phragmen Lindelof
quadrant theorem lecture notes exponential type bounded axes pdf`.
These found classical growth inputs, rather than an inspected theorem
stating the exact obstacle conclusion. The parent assessment remains
the record for Schmidt's finite-domain hypotheses; those were not
reopened. No sibling notebook was read.

1. Axler--Bourdon--Ramey, [Harmonic Function Theory](https://www.axler.net/HFT.pdf),
   second edition, corrected 17 July 2020. Reuse Theorem 7.26,
   pp. 158--159: positive harmonic functions on the upper half-plane
   have a positive Poisson-measure representation plus a nonnegative
   linear term in height. The representation includes infinity; it
   imposes no continuous boundary data. Theorem 3.4, p. 47, gives the
   sharp ball Harnack bounds, in dimension two with factors
   (1-r)/(1+r) and (1+r)/(1-r). Its proof compares Poisson kernels
   and passes from closed to open balls by dilation. Nonnegative
   functions require the usual added-positive-constant limit if
   using a strictly positive formulation. These are available
   growth tools, not an exterior-domain representation.

2. L. F. Demkowicz, [Lecture Notes on Non-Self Adjoint Operators and
   Related Topics](https://www.oden.utexas.edu/media/pending_reports/book.pdf),
   title-page version 4 December 2024, Section 3.4, Theorem 3.9,
   printed pp. 42--43 (PDF pages 50--51). An analytic function,
   continuous to the boundary of a sector of angle pi/lambda,
   bounded by M on its rays, and with log maximum of growth at
   most r^rho for rho<lambda, is bounded by M inside. The proof
   rotates the sector, chooses rho<rho_1<lambda, multiplies by
   exp(-delta z^rho_1), controls the circular boundary using the
   strictly positive cosine factor, applies the maximum principle,
   and lets delta decrease to zero. This is the strict sector
   theorem, not an endpoint assertion for a half-plane.

   A second primary check was the [Costin-hosted complex analysis notes](https://math.osu.edu/~costin.9/7651-2021/notes.pdf),
   current retrieved 202-page PDF, Theorem 205, Section 35, printed
   pp. 107--108. Its sector hypotheses are angle pi/beta, beta>1/2,
   growth C_1 exp(C_2 |z|^alpha) with 0<alpha<beta, and bounded
   continuous boundary values. The inspected proof uses a power
   map followed by exponential damping and truncated-domain maximum
   modulus. Search indexing still called this Theorem 41.1; that
   numbering is not the retrieved version. Screenshots timed out;
   the theorem and complete relevant proof were read as PDF text.
   Demkowicz is the stable citation selected for the continuation.

Search leads about Hardy/Cartwright classes, modified Poisson kernels,
and spectral-gap oscillation were not read at theorem level and are
not imports. In particular the spectral-gap snippet explicitly
concerned log-modulus majorants. No conclusion here rests on those
leads. Broad source discovery stops now: the two classical inputs
permit an independently testable local application without a new
Hardy theorem or a Fourier support/indicator theorem.

## Applicability still to prove in research

Keep fixed R,T and the complete L504 Fourier class. The proposed test
uses a horizontal half-plane strictly above height B, which lies in
the specified exterior domain. Restriction is the proposed mechanism;
no extension across the obstacle and no regularity at its boundary is
being presumed. The role of any two nonnegative harmonic functions,
the bound needed along the imaginary ray, and the conversion from
real-part to modulus control must all be checked in the later proof.

The decisive threshold proposed for that proof is polynomial control
of f along the imaginary axis, with constants allowed to depend on
f,G,R,T. The sector theorem has a strict margin for quadrant angle
pi/2 and exponential order one, provided a legitimate normalization
has bounded boundary values and no pole in the chosen sector. Local
compact bounds and all symmetry uses must be included. This paragraph
specifies proof obligations, not a derivation or a claimed obstruction.

Continue if these hypotheses can be verified from the assumed G;
abandon this particular test if it needs an additional bound on G,
unjustified deletion of the term at infinity, or control of Im f that
the stated symmetries do not supply. A failure is to be saved, rather
than repaired by assuming the desired conclusion. Even a successful
test would leave quantitative truncation compactness, weighted costs,
bottom kernels, Xi realization and RH signs unresolved.

The next mathematical specialization is recorded separately in
[its assessment](2026-10-30-actual-negative-part-majorant-specialization.md).
It requires the supervisor's separate next-turn approval; this turn
has neither derived nor audited its proposed conclusion.
