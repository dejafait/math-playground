# Signed kernels and positivity-sensitive separation: sources1542

18 November 2026. Literature only. No width-family theorem, signed law,
cone alternative, feasible measure or infeasibility certificate is proved
here. This completes the source comparison nominated in assessment1541.

## Primary sources actually inspected

1. Kyle Siegrist, *Probability, Mathematical Statistics, and Stochastic
   Processes*, Expected Value, Section 13, **Kernels and Operators**,
   [author text](https://www.randomservices.org/random/expect/Kernels.html),
   accessed 18 November 2026; no revision date displayed. Read Basic
   Theory, Definitions: kernel/probability-kernel definitions, the
   unnumbered positive-measure transformation statement
   `mu K(A)=integral K(x,A) dmu(x)` and its complete countable-additivity
   proof; the bounded-function estimate and its proof; Constructions,
   measure additivity and bounded-operator summary. Nonnegative summands
   justify the countable interchange. Finite positive input and a
   probability kernel give finite output. The text's blanket convention
   that integrals exist must be checked locally. A displayed equality
   for every f is a typo: the proof gives the inequality
   `||Kf||<=||K|| ||f||`, with equality for the operator norm. It also
   mislabels the codomain of Kf once. Neither typo is imported. This is
   positive-kernel coverage; signed input still requires both Jordan
   parts and a bounded-function integration argument in research.

2. Richard F. Bass, *Signed measures*, Chapter 12, version 4 November
   2011, [university-hosted extract](https://webspace.science.uu.nl/~kraai101/SignedMEasures),
   Theorem 12.8 and complete proof, printed p.97, and (12.1). A signed
   measure has unique mutually singular positive Jordan parts; their
   sum is its total variation. For finite variation both parts are
   finite. Definition of signed integration and its domination bound
   appear as Exercise 12.2/p98, not a supplied proof. Import the standard
   named Jordan decomposition theorem; do not count its exercise as
   a proved signed-kernel theorem. PDF extraction loses minus signs;
   the source statement is the difference of its positive parts.

3. Theo Bühler and Dietmar A. Salamon, *Functional Analysis*,
   11 May 2016, [PDF](https://math.jhu.edu/~js/Math637/eth.functionalanalysis.pdf),
   Corollary 2.3.19 and complete proof, printed p.68: in a real normed
   space, disjoint nonempty convex sets, one closed and one compact,
   admit a bounded linear functional with a strict uniform separation.
   Its proof first obtains positive distance using compactness, then
   applies Theorem 2.3.10 to an open convex enlargement. Read also
   Theorem 3.1.11 and complete proof, pp.90-91, for the topological
   version with one open set. These are not separation theorems for
   arbitrary disjoint nonclosed sets. Reuse ledger1532's inspected
   signed Riesz coverage and scalar subspace comparison; do not repeat
   that scalar approximation problem as a new mechanism.

4. Lewis Bowen, *Lecture Notes in Real Analysis*, 8 December 2014,
   [PDF](https://web.ma.utexas.edu/users/lpbowen/m381c/lecture-notes.pdf),
   Theorems 28.1/28.2, printed p.60, and Section 28.1, Exercises
   135-138 with supplied proofs, pp.61-62. The signed Riesz statement
   represents bounded functionals on C_0 by finite signed Borel
   measures. The regularity and continuous-test uniqueness arguments
   cover locally compact Polish spaces and measures finite on compact
   sets. The regularity proof exhausts by compact sets and uses open
   approximations. The uniqueness proof sandwiches compact indicators
   with continuous functions and invokes bounded convergence.
   Some E/E_i indices in Exercise137 are inconsistent; import its
   standard regularity conclusion, not those displayed indices.
   No complete Riesz existence proof is supplied in this PDF.

5. Reused Tao, *245B, Notes 12*, 2 March 2009,
   [author text](https://terrytao.wordpress.com/2009/03/02/245b-notes-12-continuous-functions-on-locally-compact-hausdorff-spaces/),
   Theorem24, Lemma29, Exercises31-32 and Remark33 from ledger1532.
   This turn additionally inspected Theorem24's uniqueness argument
   and its sigma-compact existence case, and Exercise22's regularity
   statement. Theorem24 gives positive Radon representation on
   sigma-compact locally compact Hausdorff spaces. Its noncompact
   proof uses a locally finite partition of unity and compact-case
   measures. Signed uniqueness can be checked using positive parts
   and the stated positive uniqueness, without assuming the signed
   mixture's positivity. Keep ledger1532's Lemma29 typo qualification.

## Proposed specialization, deliberately unproved

Keep W=[1,2], X=[0,infinity) and all C032j/k/m/p qualifications.
The dual width space is real C(W) with the supremum norm; its continuous
dual is finite signed Radon measures, also finite signed Borel measures
on this compact metric W. On X use bounded continuous real functions
C_b(X), with the supremum norm. For source comparison denote the
proposed test operator by

    Tf(sigma)=integral_X f(u) dnu_sigma(u).

C032p already states continuity of each Tf in sigma. No continuity of
Borel-set evaluations is needed or asserted. The local application
must verify boundedness/linearity and integration against signed eta.
The noncompact half-line is locally compact Polish and sigma-compact;
source4 covers regularity of the finite positive component measures.
Theorem24 and continuous-test uniqueness supply the general tools for
checking whether nonnegative continuous tests detect positivity of
the signed output. This is a pending applicability argument.

Let S denote the real linear span of real and imaginary parts of all
functions `sigma -> exp(-E_sigma(w))*sinh(O_sigma(w))`, w in C.
They belong to C(W) by C032m. This definition retains full complex
cancellation; it does not truncate Taylor coefficients. The proposed
cone to examine is

    Q=S+{Tf : f in C_b(X), f>=0}.

The bounded next target is to **test and prove or qualify** the proposed
alternative: mass-one eta with J_eta=0 and nonnegative mixed law exists
exactly when the constant -1 lies outside the supremum-norm closure
of Q. No direction of this alternative is established in this review.
The required research work is kernel construction, integral identity,
positivity detection, cone/sign orientation and mass normalization of
the separating Riesz functional. General separation, not a new source
theorem about this zeta family, is the intended input.

The closure here is part of the proposed statement, not an assertion
that Q is closed. No closure of the map eta -> (mass,J_eta,nu_eta),
no closed range, and no quotient-image topology is assumed. An
output-space Farkas alternative without a checked closure premise
is not approved. A finite approximation to -1 has an error paired
with the unknown total variation of eta; a numerical tolerance or
a single finite grid cannot become an unrestricted certificate.
Do not derive a bounded-variation variant or evaluate Q this turn.

## Scope comparison, duplicates and limits

The strongest inspected conclusions are general kernel composition,
Jordan decomposition, signed Riesz representation and separation of
closed convex sets from compact sets. They cover the construction
and general tools but state no feasible eta and decide no Q membership
for this family. A local proof is justified solely to match those tools
to simultaneous mass, cancellation and output positivity; do not reprove
the imported general theorems or advertise originality.

Finite stop1302 excludes finite signed positive-width repairs under its
moment condition. It does not extend to all finite signed Borel eta.
Ledger1532 treats scalar cancellation alone. Stops1534/1536/1538 concern
linear width recursion and direct compact-transform growth, not this
additional law cone. No prior proof of this joint criterion was found
in the named local ledgers. Nothing implies novelty from that search.
Moments and unsmoothed actual-Xi realization remain independent; even
a proved feasibility criterion would not supply RH or all-degree signs.

## Search and access record

Queries: `probability kernel measure composition theorem integral kernel
finite measure lecture notes proof`; `closed convex cone Hahn Banach
separation locally convex space theorem closed image duality signed
measures`; `signed measure Markov kernel total variation contraction
theorem Jordan decomposition`; `C(X) closed convex cone signed measure
separation`; `Riemann Xi signed width mixture`; `Sra smoothing signed
mixtures`; `Some positivity properties smoothing mixtures`; and
`signed regular C_c positive Riesz lecture notes`. Exact-family results
did not supply an inspected matching theorem. Search snippets, aggregator
Xi passages, unrelated density approximations and signed-kernel leads
are not imported. Existing fixed-v1 source qualifications are unchanged;
no new smoothing-preprint theorem was needed.

Cambridge functional-analysis PDF timed out. Nagy's AppendixE TheoremE.6
(p10009) was read as an alternative but is unnecessary given source3;
its unresolved internal reference is not a dependency. The large blocked
MIT volume was not retried. No essential source access blocker remains
for this proposed specialization. No other notebook was read.

## Mathlib

Inspected supporting official
[MeasureComp documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Probability/Kernel/Composition/MeasureComp.html):
`MeasureTheory.Measure.instIsFiniteMeasureBindCoeKernelOfIsFiniteKernel`
and `MeasureTheory.Measure.instIsProbabilityMeasureBindCoeKernelOfIsMarkovKernel`
cover positive composition infrastructure, not the full signed or cone
application. The guessed Separation/Basic documentation URL failed;
that is not evidence that a separation theorem is absent. Full matching
coverage of the proposed qualified result remains unknown.

## Direct-URL recovery1543

18 November 2026, separate literature-only recovery. All five primary
URLs above opened successfully. Rechecked the kernel source's integration
convention; Bass Theorem12.8 statement and initial proof; Bühler-Salamon
Corollary2.3.19 statement and distance argument; Bowen Theorems28.1/28.2;
and Tao Theorem24, uniqueness argument and signed Exercise31. These agree
with the existing coverage ledger. Prior complete-proof inspections and
typo qualifications are reused, not claimed as newly repeated audits.
The ready assessment now carries direct URLs in SOURCE_EVIDENCE itself.
No source theorem or target changed, no new search for novelty was needed,
and no local specialization was derived. This is a process repair, not
mathematical progress or a new source-coverage advance.
