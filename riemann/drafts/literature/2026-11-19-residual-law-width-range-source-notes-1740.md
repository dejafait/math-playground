# Residual-law width-range source comparison1740

19 November 2026; literature only. Exact starting target is assessment1739's
review question. Main gap: L030-L032/C032a actual-Xi all-degree positivity.
Intermediate target: decide whether C033i's exact residual probability mu
belongs to C032q's finite real signed width-mixture range on [1,2]. A range
exclusion would delimit the arbitrary-output positivity-reflection stop;
full J_eta cancellation, tails, moments and Xi realization remain unpaid.

## Inspected sources and exact scope

1. Sra, *On some positivity properties of the Riemann Xi function*,
   [2610.00584v1](https://hexagonmath.org/pdf/2610.00584v1), 20 October 2026.
   Inspected Section2.1/(2.1)-(2.3), printed p3, Lemma2.1 and complete
   convergence proof p4, and PropositionB.1 with complete proof p17.
   The heat series and every fixed derivative converge locally absolutely
   on Re t>0. Gaussian decay absorbs the complex displacement and each
   fixed polynomial factor. B.1 treats counting error, displacement error
   and the large-time gap separately; its real-time j=0,1 bounds are
   available. They are not a theorem about a continuum signed width
   quotient, a density of its convolution exponential, or its uniform
   convergence. Retain the actual divisor, multiplicity, conjugation,
   strip/counting, through-height-100, first-zero and heat qualifications.
   No source-wide correctness or zero-data certification is claimed.

2. Sra, *Some positivity properties of Riemann Xi under smoothing*,
   [2611.00345v1](https://hexagonmath.org/pdf/2611.00345v1), 11 November 2026,
   Proposition3.1/(3.2)-(3.3), printed pp5-6, complete C.1 proof p21.
   Inspected the square-completion and absolute-summability justification.
   It gives the exact transformed heat function and Levy density for
   half-variance sigma. It does not identify this width operation as
   scaling a single probability law or characterize its signed-mixture
   image. Reuse C032j's probability construction and its fixed-v1 limits;
   no later version or unsmoothed endpoint is substituted.

3. Reuse source-notes1736, its finite-signed-measure case of Cekanavicius
   and Vellaisamy, *On closeness of two discrete weighted sums*, Modern
   Stochastics: Theory and Applications5(2) (2018), 207-224,
   [Section1 after (1), (23)-(24)](https://www.vmsta.org/journal/VMSTA/article/114/read),
   DOI10.15559/18-VMSTA103. The convolution exponential exists in total
   variation, has the exponential norm bound and signed inverse. The
   article URL was reopened; essential formula/proof coverage is reused,
   not newly claimed. This applies to arbitrary finite real signed
   measures on R; no lattice, positivity or density is required for that
   framework. It does not give continuity of a density from total-variation
   convergence. Reuse Mimica2015 Propositions1.4(iv)/1.8 via source-notes1552
   for positive half-line transforms and uniqueness; a signed application
   must explicitly reduce to finite positive measures, including zero.

4. Friedrich Haslinger, *Complex Analysis*, author lecture notes,
   [Section2.7, Theorem2.39, printed pp67-68](https://www.mat.univie.ac.at/~has/scriptneu.pdf),
   undated live PDF accessed 19 November 2026. Inspected full statement
   and proof. A positive measure, integrability at each parameter,
   holomorphy in the complex parameter and an integrable dominator on
   each parameter disk imply holomorphy of the integral and permit every
   derivative under it. The proof uses Cauchy's formula and dominated
   convergence on a smaller disk. Signed integration requires Jordan
   parts or total variation. Source search called this 2.38; the actual
   inspected PDF numbers it 2.39. Reuse Lebesgue's dominated convergence
   theorem and the Weierstrass uniform convergence theorem. Joint/local
   bounds for the actual family are obligations, not consequences of
   having an entire transform. Holomorphy is optional: the narrower
   proposed test needs only continuity near x=1.

5. NIST DLMF, [Euler beta integral (5.12.1)](https://dlmf.nist.gov/5.12.E1),
   accessed 19 November 2026. Inspected equation and its restrictions
   Re a>0, Re b>0: the integral of t^(a-1)(1-t)^(b-1) on (0,1) is
   Gamma(a)Gamma(b)/Gamma(a+b). This is a possible tool for bounding
   convolution powers with integrable endpoint singularities. No bound
   for the actual signed difference or series is derived here.

6. Barndorff-Nielsen and Hubalek, *Probability measures, Levy measures
   and analyticity in time*, Bernoulli14(3) (2008), 764-790,
   [arXiv:0811.0678v1](https://arxiv.org/pdf/0811.0678), Theorem8/(50)-(56),
   printed pp775-776. Inspected the full hypotheses and conclusion and
   opening proof case, not the entire contour proof. It assumes a Levy
   density analytic on a sector, leading a*z^(-1-alpha) with a>0 and
   0<alpha<1, an O(|z|^beta) remainder with beta>-1, and an exponential
   sector bound. Its stated entire variable is process time at fixed
   positive spatial x. This supplies neither positivity of a signed
   width difference nor the requested spatial/width-uniform regularity.
   No theorem from this paper is imported; do not silently swap variables.

7. Fantini and Fenyes, *Regular singular Volterra equations on complex
   domains*, [arXiv:2309.00603v2](https://arxiv.org/pdf/2309.00603v2),
   28 January 2025; SIAM J. Math. Anal.57(1) (2025), 336-363,
   DOI10.1137/23M1613876. Inspected Theorem1.6/Lemma1.8 hypotheses and
   conclusions pp9, and Proposition3.4's beta-integral estimate/proof p17.
   Their regular-singular operator assumptions and weighted holomorphic
   spaces have not been matched to this family. The full fixed-point
   theorem proof was not inspected or imported. This is a comparison
   lead, not an established deconvolution regularity result; item5
   suffices for the proposed elementary convolution estimate.

8. Bühler and Salamon, *Functional Analysis*, 11 May 2016,
   [Corollary2.3.4, p63; Example1.3.7, p28](https://math.jhu.edu/~js/Math637/eth.functionalanalysis.pdf).
   Inspected the norm-preserving real functional extension statement and
   signed C(M) duality. Reuse full signed Riesz coverage/qualifications
   from ledger1532 and C032q. These require a bounded functional on
   the actual image space for an exact range application; generic
   injectivity or dense span supplies no such bound. No new range
   equivalence is derived here. A generic dual reformulation was not
   selected because it supplies no discriminating test for this mu.

## Proposed necessary-condition test, not a result

Assess the weaker property: a signed remainder for every width sigma
in [1,2], after convolution factor nu_1 is removed, has the form
an atom at zero plus a density continuous on a neighborhood of x=1,
with bounds uniform in sigma that permit integration against any fixed
finite |eta|. No bound on |eta| across all inputs may be assumed.

Research must construct and identify these finite signed remainders;
prove uniform absolute integrability of ell_sigma-ell_1 on the full
half-line, including both endpoints; obtain a common integrable local
singularity bound at zero; and justify local uniform convergence of the
convolution-density series near x=1. Total-variation convergence alone
is insufficient. The unproved quotient must not be presumed positive.
The equality after cancelling nu_1 requires finite signed transform
uniqueness, not a positive-convolution inverse for nu_1 itself.

Then compare the resulting necessary regularity with C033i's exact
inverse series and its support intervals [n,3n/2]. The density behavior
on both sides of 1 and the passage from almost-everywhere density
equality to a continuous representative must be checked explicitly.
This paragraph is a specification of a future test, not a proof that
an invariant or a contradiction holds. No range exclusion is claimed.
A successful test would decide this mu's membership only; it would
not reflect positivity for arbitrary width remainders or settle C032r.

Continue if the uniform continuum and series estimates can be proved
and a mismatch with lambda established on a neighborhood, as measures.
Abandon this discriminator if a necessary uniform estimate fails or
lambda admits the required continuous representative; preserve any
partial result. Do not replace the test by larger grids, a positivity
assumption, a finite dictionary, or an analyticity assertion without bounds.

## Duplicate/failure check and bounded search

Inspected C032j in full; C032q hypotheses/conclusions/tools; C033i
hypotheses/conclusions/tools, finite-subfactor and residual-identification
proofs; C032s statement and zero-endpoint proof; C032u/v statement and
source scope. C032s's fixed widths 1,2 do not prove continuum uniformity.
C032u's positive two-width factor neither represents mu nor gives an
arbitrary-width range theorem. C032v concerns a one-jump scalar bound.
No duplicate regularity-at-1 test was located in the scoped 18/19 November
width/reflection/finite-Levy assessment paths. This is not a novelty claim.

Read stops1534/1536/1553/1571 completely. The proposed test requires
neither coefficient-span closure, a direct compact Fourier-Laplace
representation, reverse positive Levy ordering nor a coarse-box dual
fit. Their evidence remains unchanged. The completed C033i audit is
not reopened. No other notebook, API key or scheduler state was used.

Queries: signed mixture range characterization bounded linear functional
mixing measures Hahn Banach; mixture distributions range signed mixing
measures representation identifiability; compound Poisson density real
analytic convolution Levy density; holomorphic functions integrals measure
locally integrable dominating function theorem; analytic convolution
singularity alpha beta Volterra; Sra smoothing signed mixtures Xi; signed
mixtures subordinators range; convolution exponential continuous density
signed measures. No inspected exact family-range theorem was found.
Identifiability survey/search hits were not treated as theorem evidence.

Decision: EXPLORE for one bounded continuity discriminator. Sources cover
the basic operations; continuum estimates and the regularity obstruction
are the identified mathematical work. No essential unread theorem is
needed if the elementary dominated-convergence/beta route is taken.
Full matching Mathlib coverage remains unchecked and unknown. A new
assessment1740 nominates this proof attempt for separate gate approval.
The range answer remains open. This source step is EXPLORATION, not an
imported solution, mathematical discovery or exhaustion-counter reset.
