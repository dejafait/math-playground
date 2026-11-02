# L585 periodic carrier: separate critical-audit coverage

TARGET: Critically audit L585's exact periodic carrier, checking the sinc-density identity, modular rank certificate, and finite-weight cone argument.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the approved periodic-cone/occupation assessments and recorded packet, exact-law and absolute-budget stops; searched Tao 245C Plancherel/convolution, Boyd supporting hyperplanes and Rockafellar relative-interior closure, then read the primary statements and relevant proof cases below.
SOURCE_EVIDENCE: Tao, 245C Notes 2 (6 April 2009), (5),(8),(10)--(11), Theorem 43 and Exercise 44, https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/; Boyd--Vandenberghe, Convex Optimization (2004), section 2.5.2, pp.50--51, https://www.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf#page=64; Rockafellar--Wets, Variational Analysis, author PDF third printing 2009, Theorem 2.33 pp.58--59 and Proposition 2.40 p.64, https://sites.math.washington.edu/~rtr/papers/rtr169-VarAnalysis-RockWets.pdf#page=72; Bui--Hall v1 section 4.2 Proposition 3, https://arxiv.org/html/2304.05178v1.
COMPARISON: Plancherel covers L2 products after checking convention and integrability; finite-dimensional supporting hyperplanes cover the boundary argument; Proposition 2.40 directly covers interior-to-membership even for a nonclosed convex cone. These standard results do not verify the proposed sinc density, rank, or strict interiority. Earlier cubature/occupation sources still supply no prescribed-tensor feasibility.
GAP: Independently audit all 126 entries, Fourier constants/reflection, cutoff limits, both shifted Euler terms, exact rational rank and the strict supporting-functional argument; conditional standard-source coverage is ready, but L585 remains an unaudited intermediate candidate.
REASON: Separate coverage approval now permits the saved conceptual audit under standard finite-dimensional and L2 theorems; no new carrier result or independent verification is claimed by this literature-only step.
LITERATURE_REASON: The invocation-start continuation was REVIEW_REQUIRED for Fourier and finite-cone hypotheses; this review fills that specific missing coverage rather than repeating the ready construction assessment.
SCOPE: Critical audit of L585 as stated, with L473 (9) as explicit tensor input, ordinary derivatives through order two, lag one, unrestricted finite periods and nonnegative finite weights; no positive second completion, numerical W, full stationary law or Xi realization is covered.

The main RH gap remains actual-Xi all-degree signs at unbounded heights.
The intermediate result to audit is L585's claim that L473's complete
126-entry leading fourth tensor admits one fixed finite nonnegative
mixture of smooth periodic occupation tensors with unit paired-jet
support. Fixed finite weight would then give the requested uniform
weight and second-cost bounds. Second-moment completion, positive
clipping and actual-Xi transfer remain independent unresolved steps.

The construction turn's invocation-start EXPLORE assessment covers its completed tensor
attempt; this file does not retroactively approve uncovered work or
claim that an independent audit has already occurred. Use the canonical
L585 proof and its two exact scripts/certificates. In particular, its
successful modular tests are not a substitute for the analytic proof.

The separate review should compare the standard named Plancherel theorem
and finite-dimensional supporting-hyperplane theorem with their exact
uses, retaining the source qualifications on L473 (9). The proof uses
only finite-dimensional separation and supplies a nearest-point boundary
argument plus the nonclosed-cone simplex step. It invokes neither an
infinite-dimensional strong alternative nor a compact path-space
attainment theorem. Confirm that this is sufficient audit coverage
before undertaking the conceptual proof audit.

The subsequent mathematical audit should test all occurrence allocations
in the frequency change of variables, the factor 3/pi^3, both shifted
Euler terms, all 45 universal identities and all 81 quotient directions,
the exact modular-to-rational implication, and the passage from a
nonnegative functional to a strict interior point. Verify that interiority
really yields one fixed finite mixture and does not leave a diverging
period/weight sequence. The unit support bound must be phasewise.

Essential mathematical input: L473 (9). L582's convention is restated in
L585 and is not an additional theorem premise. L578/L579/L581/L584 remain
scope contrasts, not inputs to the carrier. The arithmetic proof of
Bui--Hall Proposition 3 remains imported and unaudited. No cross-notebook
result, positive covariance repair or Xi realization is assumed.

Continue if the full tensor, analytic limits, exact rank and interior
argument survive independent scrutiny. Repair a specific local defect
if possible; reject the carrier claim if those steps require an unproved
closure/attainment premise or lose uniform weight. A later failure of
second completion would not by itself refute this isolated fourth result.
Matching Mathlib coverage is unchecked. Coverage is now approved for
proof_audit/conceptual_audit, deep_research/xhigh; the retained nomination
above describes the separate work still to be done, not a completed audit.

## Completed source comparison, 31 October 2026

This step read L585 to identify its actual theorem uses, L473's full
formula (9) and source qualifications, the prior approved cone assessment,
and the narrow recorded failures. It performed no new tensor calculation,
certificate replay or proof audit, and changed no lemma or mathematical
script. The audit target is unchanged.

### Fourier input

Tao's [245C Notes 2](https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/),
dated 6 April 2009, was read at (5), (8), (10)--(11), the Parseval
argument preceding Theorem 43, and Exercise 44. Theorem 43 extends
the Schwartz transform unitarily to L2(R^d); Exercise 44 identifies
it with the integral transform on L1 intersect L2. Equation (5)
states the L1 convolution rule. The convention uses exp(-2pi i x xi).
L585 uses exp(i k s); its frequency rescaling, reflected bilinear
pairing and product hypotheses must be audited explicitly. The
L1-integrability of the individual physical pulses is not a premise
one may add silently. These sources cover the standard L2 input,
not the density change of variables or its 3/pi^3 coefficient.
No Plancherel reproof is needed.

### Supporting planes

Boyd--Vandenberghe, [section 2.5.2, pp.50--51](https://www.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf#page=64),
states existence of a nonzero supporting normal at each boundary
point of a nonempty finite-dimensional convex set. Read both proof
cases: separate the point from the nonempty interior, or use the
proper affine hull when the interior is empty. L585 proposes to
apply this inside V to closure(K), not in path space. Its claims
that this set spans V and q is not on its boundary require its
rank and strictness proof. The nearest-point paragraph is an
optional closed-set specialization, not a new separation theorem;
the audit should check its hypotheses without requiring a reproof
of the general result.

### Nonclosed-cone attainment

Rockafellar--Wets, *Variational Analysis*, author-hosted version
marked third printing 2009, [Theorem 2.33, pp.58--59 and Proposition
2.40, p.64](https://sites.math.washington.edu/~rtr/papers/rtr169-VarAnalysis-RockWets.pdf#page=66),
were read with their relevant proofs. For a nonempty convex subset
of R^n, Proposition 2.40 states rint(cl C)=rint C and nonempty
relative interior. Its proof reduces to the affine hull and invokes
2.33; that proof's final case uses approximating simplices and
continuity of positive barycentric coordinates. Thus the precise
closure-to-interior implication in L585 is already standard, with
no closedness or compact generator requirement. Conditional on
the earlier interiority proof, this source is a direct alternative
to L585's simplex paragraph; it supplies no numerical weight bound.
Its source comparison does not establish q's interiority.

The first Rockafellar book mirror returned HTTP 403; the inspected
author-hosted theorem above resolves the needed coverage. The first
Stanford URL timed out, while the www.stanford.edu book succeeded.
These were resolved retrieval failures, not persistent source blockers.
Rockafellar's *Convex Analysis* Theorem 6.3 appeared in search results
but its full primary passage was not retrieved and is not an input.

### Arithmetic qualification, duplicates and audit boundary

Read Bui--Hall v1 [section 4.2, Proposition 3](https://arxiv.org/html/2304.05178v1):
the shifted fourth moment is uniform for four complex shifts of
size O(1/log T), has coefficient T(log T)^4/(2 zeta(2)) and error
O(T(log T)^3). The subsection explicitly omits its derivation.
L473 supplies the local Hardy conversion and full derivative tensor;
its identification with arithmetic moments retains that unaudited
source proof. The proposed audit can verify L585 from the stated
integral (9) without claiming an independent arithmetic proof.

Reuse the preceding Bayer--Teichmann and Bernard comparisons; neither
is a theorem premise for L585. L579's finite packet stop, L581's
exact-law obstruction and L584's specified absolute-budget failure
remain intact. They do not decide this full leading-tensor carrier.
The new source comparison identifies standard convex attainment,
not novelty of L585's combined construction. Matching Mathlib coverage
remains unchecked; no formalization or broader novelty conclusion follows.

The complete audit still has to connect both scripts and their complete
selected evidence to the stated Euler expression and Taylor coefficients,
including all 45 identities and 81 quotient directions. Modular success
does not replace this linkage or the analytic strictness argument.
No further essential source gap was found for this bounded audit.
