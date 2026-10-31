# Fixed-symbol test-shape variational discriminator

TARGET: Test L527's fixed-symbol variational threshold on real even normalized C_c^infinity(-1,1) by one certified Fourier-multiplier bound, seeking either a smooth witness c(h)>pi/4 or a uniform upper bound sup c(h)<pi/4.
CHECKED: 2026-10-30
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse the completed exact-symbol, finite-interval Wiener-Hopf and variational comparison in 2026-10-30-common-pole-test-shape-variational-coverage.md. No inspected matching threshold theorem or duplicate was found; no novelty claim.
SOURCE_EVIDENCE: Direct primary PDFs rechecked 2026-10-30: Teschl, GSM 99, 12 February 2009, Theorem 2.19, p.77, Theorems 4.10/4.13, pp.118--120, https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf ; Carlsson, GMIG (2010), (1.1)--(1.4), Theorem 2.5 and proof, pp.9,15, https://gmig.science.purdue.edu/pdfs/2010/10-02.pdf . Companion assessment supplies the prior exact-symbol searches and nonmatching comparisons; L526/L527 supply conventions and motivation only.
COMPARISON: Standard variational and compressed-convolution tools are covered; the exact-symbol bound is not. Existing L527 quadrature concerns one bump and cannot bound the enlarged supremum. No trace extension, compactness or finite-section spectral convergence is imported.
GAP: Prove a strict discriminator with normalization and infinite-dimensional error control, or record the precise unresolved remainder after one bounded attempt. A finite trial value below pi/4 is not an upper bound on the supremum.
REASON: Shape variation tests a different independently falsifiable quantity after the prescribed bump's insufficient coefficient. Known tools cover the proposed test but do not decide it. This ready nomination requires separate next-invocation approval before mathematics.
SCOPE: Exactly the TARGET, fixed K, interval, real-even smooth class and Fourier convention below. No generalized trace proof, moving pole/support optimization or Sonin-asymptotic extension is covered.

Use K(t)=(e exp(2it)-1)/(1+2it),
H(t)=integral h(x)exp(-itx)dx, dm=dt/(2pi), and
c(h)=integral |H(t)|^2 Re(K(t)/|K(t)|) dm(t).
The norm is ||h||_2=1. No positivity condition is imposed on h.

First justify the operator/sector representation actually used. A
uniform upper certificate needs control of the entire discarded
sector and coupling, or another proved uniform bound. A proposed
L2 witness needs a justified smooth compact approximation with a
retained strict margin; an approximate matrix eigenpair or a supremum
endpoint alone is not a smooth witness. Finite-dimensional calculations
may guide the test, but all load-bearing estimates require proof or
complete certified evidence. Do not repeat L527's fixed-bump quadrature.

Continue the shape mechanism only with a strict witness or a refined
independently testable unresolved estimate. Abandon this variation
if a uniform strict upper bound is proved. If one bounded attempt
cannot decide the threshold, save its exact error/remainder and
report it honestly rather than manufacturing a lemma or global stop.

The main gap is actual-Xi all-degree positivity. A strict witness
could motivate separately reviewing a trace specialization for that
one h; the trace asymptotic is not assumed for this class. Essential
local input IDs are L526/L527 for conventions and motivation. Source
proofs, omitted terms, missing primes, full-Weil identification,
nullvector/trace/nonresonance, family bounds and Xi transfer remain
unresolved. Full Mathlib coverage is unchecked; no cross-notebook
input is used. This file records source scope, not new mathematics.

## Direct-source recovery review, 30 October 2026

The supervisor reported missing direct source URLs in this ready
assessment. Both URLs above now resolve to primary PDFs. Reused the
companion assessment's searches and comparisons; no new discovery
search or changed mathematical target was needed. Relevant generic
and Sonin stop records still concern the prescribed bump.

[Teschl's author-hosted PDF](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf):
rechecked Theorem 2.19 (PDF p.89), Theorem 4.10 (PDF p.131),
and Theorem 4.13 with proof (PDF p.132). The spectral-edge formula
requires self-adjointness. Min-max includes the essential-spectrum
endpoint after discrete eigenvalues are exhausted. Temple requires
a unit domain vector and exactly one isolated spectral value in the
chosen open interval; its proof uses spectral positivity on the
complementary intervals. Thus a finite matrix supplies no automatic
isolation certificate. These general tools do not evaluate c(h).

[Carlsson's primary report](https://gmig.science.purdue.edu/pdfs/2010/10-02.pdf):
rechecked (1.1)--(1.4), Theorem 2.5 and its proof (PDF p.7, printed
p.15), including regularization on interior intervals and passage to
distributions. For a>0 and a distribution on (-a,a), boundedness of
the truncated convolution is equivalent to a bounded-Fourier-transform
extension; its least extension norm is attained and is between the
operator norm and three times that norm. No evaluated extension for
this K is supplied. Fourier sign, interval translation and sector
restriction remain application obligations.

Decision remains EXPLORE for exactly TARGET. This is a valid source
URL/process repair, not new mathematical evidence or a renewed
exploration budget. Essential coverage is ready for the saved bounded
calculation. No compactness, spectral isolation, trace extension or
threshold conclusion is imported. Full Mathlib coverage remains
unchecked. No lemma or mathematical script was changed.
