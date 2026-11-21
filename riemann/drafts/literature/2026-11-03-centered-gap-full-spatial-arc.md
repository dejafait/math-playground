# Source review: centered gap and the complete spatial polynomial on an arc

TARGET: Assess whether L697's fixed centered-gap profile yields sup_(|theta|<=delta,|zeta|=1)|G_(n,e)(exp(i*theta),zeta)|<=C*exp(-c*n) with fixed delta,c>0 in L666, retaining all M=n/3 spatial moments and both finite endpoints.
CHECKED: 2026-11-03
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 123 compared the exact target with L666/L697, L683--L686, L695, the recorded L682 stop and C645p's statement; reused the scalar-arc and inner-spatial assessments, then searched spectral-gap rational tests, Cauchy-transform decay, Fourier pole half-planes and Plemelj boundary values. The stronger finite-measure Cauchy-decay criterion was inspected, not merely its search snippet. No matching complete finite-polynomial estimate was found; this is no novelty conclusion.
SOURCE_EVIDENCE: Reuse the scalar assessment's complex-measure, Bernstein and Schwartz-Poisson inputs and L683's exact finite geometric remainder (7). New inspection: NIST DLMF 1.14(iii), (1.14.17)--(1.14.20), (1.14.30)--(1.14.31) and standing convergence hypotheses; Howell--Mathews Section 8.1, Theorems 8.1.5/8.1.7 and complete proofs; Haber, Physics 215 Winter 2018, The Sokhotski-Plemelj Formula, pp.1,3--5, (1)--(5),(12)--(21); Mitkovski--Poltoratski arXiv:0903.4499v2 (26 May 2009), Lemma 3 and full proof pp.7--8. Reading limits and applicability below.
COMPARISON: The Cauchy-decay criterion assumes finite total variation and concerns one fixed measure on an imaginary ray; it does not control L697's infinite unit-mass comb or the growing finite spatial polynomial. Laplace convergence, residues and Plemelj supply interfaces, not uniform exponential costs. L683--L686 are small-spatial-circle lower bounds near the opposite angular arc with different support restrictions; L695, L682 and C645p stop specified substitutes, not this signed complete upper bound.
GAP: Establish or obstruct a signed frequency-side estimate for the complete M=n/3 spatial polynomial, uniformly in the spatial boundary variable, with all resolvent pole/boundary contributions, finite geometric remainder, comb samples and both finite endpoints paid within one positive exponential margin. This family-specific quantitative difference is unproved; no inspected source settles it.
REASON: Essential source comparison is complete for one bounded exact-target attempt after separate approval of this changed assessment. EXPLORE licenses investigation, not the claimed estimate; no essential source blocker remains. The target was neither derived nor mathematically approved during this literature-only step.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED identifies the essential change from a scalar to all growing spatial moments, including resolvent pole and boundary cases outside the ready scalar assessment.
SCOPE: Exactly TARGET for every fixed real l1 profile satisfying L697, cap 1/8, prescribed omega_* and fixed gap g>0, n=12q+3, unit masses, anchor, j=0, denominator 1/u, exact -2q<=m<2q and M=n/3. Constants delta,c,C,N may depend on that fixed profile/gap, never on n. A signed resolvent or retained finite-polynomial treatment may be tested; no pole omission, uniform derivative bound, finite-measure replacement of the comb, or small-remainder claim is assumed. No complete logarithmic, whole-angular-circle, H/support or Xi assertion is covered.

The nomination below is retained as the motivation and bounded test. Its
future-tense review requests are resolved by the completed comparison at the
end of this file, not assertions that its mathematical estimate is proved.

## Purpose and proposed bounded mechanism

The main gap remains actual-Xi all-degree mixed positivity and realization.
The audited scalar arc controls only G(u,0), whereas the later spatial
logarithmic tests involve the complete G(u,zeta). A uniform exponentially
small full spatial polynomial on one fixed angular arc would test whether
the cancellation survives that change of observable. Even success would
leave the rest of the angular circle, logarithmic integrability estimates,
the angular maximum H, support and actual-Xi realization unresolved.

The proposed new mechanism is a signed frequency-side treatment of the
complete finite spatial resolvent: retain T_M and account for the
spatial-resolvent pole contributions and the finite geometric remainder.
It must use the same profile fixed before n, not retune the shifts at
each degree or angle. It must not replace the sum by the absolute tail
cost stopped in L695, select a single highest coefficient, or propagate
the continued origin value by the already stopped normalization.
No representation, contour deformation, residue estimate or rate for
this mechanism has been proved in the nomination turn.

The exact threshold is the TARGET for all allowed n>=N, with fixed
delta,c>0. A source-reviewed attempt should either establish that bound
or exhibit a specific unavoidable cost or counterexample for this
mechanism. A shrinking arc, discarded geometric remainder, uncontrolled
spatial pole, truncated moment list, or missing finite endpoint fails
the test. Failure of this mechanism alone would not refute its target
or RH. Any source-indicated change of target needs its own approval.

## Essential comparison before approval

Reuse the scalar-arc sources and audited L697 only in their actual
scope. Check primary statements for multiplying the frequency kernel
by a complex spatial resolvent, with the signs, convergence domains,
pole cases and all required contour contributions explicit. A generic
convolution or concentration statement does not by itself cover these
cases. Check stronger known results and duplicates before deriving
anything, and record unread leads separately from inspected theorems.

Read the relevant portions of the local L683--L686 full-spatial response
route and its assessments only as needed to compare the proposed
mechanism; those proofs have not been inspected in step 122. Reuse the
recorded L682 and C645p stops as comparisons, checking their full proofs
only if a claimed overlap needs them. L695's absolute-tail obstruction
remains preserved. Step 105's numerical screen stays parked; it is not
evidence for the proposed uniform theorem. No cross-notebook input is
requested. Full matching Mathlib coverage has not been checked.

If this comparison yields ready coverage, the later mathematical step
can test the proposed spatial-resolvent mechanism. Its proof-purpose
would be creative if the source comparison confirms that it is a new
mechanism for this gap, rather than a routine application or a renamed
stopped route. The precise escalation is simultaneous control of the
full growing spatial polynomial and its pole/remainder costs while
preserving L697's positive decay margin. This is an intermediate test;
no route from a single small arc to RH is asserted.

## Completed comparison — 3 November 2026, step 123

### Exact local overlap and retained failures

Read L666's definitions and rational continuation, L697's hypotheses,
conclusion, factor-law interface and complete endpoint estimate (24),
and L695's hypotheses/conclusion, source scope and final qualification.
The fixed profile, cap, gap center and one positive gap width in L697
are retained. Its five scalar error terms are audited local inputs;
their constants do not assert estimates for a spatial multiplier.

Read L683's hypotheses/conclusion and exact finite remainder (7), L684's
hypotheses/conclusion and Section 2 contour argument, L685's hypotheses,
conclusion and source interface, and L686's hypotheses/conclusion and
Sections 1--3. L683 retains all moments through G=F-T, but its useful
tail charge is on the inner spatial circle r=1/32. L684's explicit
resolvent contour is on an angular arc around -1, and its lower bound
uses fixed central support. L685 allows logarithmically growing central
support; L686 pays exact clearing for a small support fraction. None
asserts the present upper bound near +1 for a fixed summable gap profile
on the spatial unit circle. Their qualifications and audit status are
unchanged; this comparison is not a new audit of their proofs.

The recorded L682 countersequence controls only the highest moment,
with zero shifts, against a specified lower threshold. It does not
upper-bound every coefficient for the present gap profile. Read C645p's
full hypotheses/conclusion and the step-87 origin-overlap record: the
continued-origin argument pays its ambient evaluation factor, but it
supplies no upper bound for the actual complete response. Neither
certificate is being reopened. L695's absolute tail cost is on the full
angular circle and its explicit profile is not asserted to have a gap;
its signed difference remains uncontrolled. This is not a source of a
counterexample to TARGET. The step-105 numerical screen stays parked.

### Reused standard inputs

Reuse the complete reading records in
[the scalar-arc assessment](2026-11-03-centered-gap-fixed-angular-arc.md)
and [the scalar-convolution assessment](2026-11-03-fourier-gap-positive-convolution-transfer.md).
Kallsen--Kruehner Lemma A.1(6),(9)--(11),(14), Maiale Proposition 1.7,
Vershynin Theorem 2.8.1, and Miller Theorems 4.1--4.2/Section 6 retain
exactly their recorded hypotheses. Complex convolution needs variation
integrability; Bernstein concerns normalized positive independent laws;
Schwartz Poisson and distributional duality require a justified limiting
test. These results do not permit testing a non-Schwartz infinite comb
against an arbitrary growing polynomial by formal interchange. No
standard measure, concentration or Poisson theorem needs reproving.

Reuse the inner-spatial assessment for the already inspected rational
quadrature and polynomial-root formulas. They concern norms or root
accounting, not a signed exponential upper bound. L683 (7) is the local
canonical finite geometric identity. Any later use must retain its T
term and verify the domain of each representation; its paid r=1/32
estimate is not an estimate of that term at spatial radius one.

### Newly inspected primary interfaces

**Laplace convergence.** [NIST DLMF 1.14(iii)](https://dlmf.nist.gov/1.14.iii),
accessed 3 November 2026: read (1.14.17)--(1.14.20), the standing
convergence paragraph and (1.14.30)--(1.14.31). The functions may be
complex, piecewise continuous and bounded by an exponential; convergence
requires Re(s) strictly above the growth exponent. Inversion adds
continuity/piecewise derivative hypotheses. Convolution retains those
standing conditions. These are function statements, not a finite-comb
or pole-boundary theorem. A one-sided exponential formula cannot be used
outside its convergence domain solely by retaining the rational expression.
No family-specific spatial factorization or boundary estimate is derived here.

**Finite residues.** J. H. Mathews and R. W. Howell,
[*Complex Analysis*, online Section 8.1](https://complexanalysis.org/web/sec_residue-thm.html),
Theorems 8.1.5 and 8.1.7; read both statements and full proofs. The
contour is simple, closed and positively oriented in a simply connected
domain; finitely many isolated singularities lie inside, with none on
the contour. The residue theorem counts every enclosed singularity.
The pole formulas include simple and higher orders. These cover a
later finite deformation only after its actual pole census and boundary
conditions are checked. They supply no estimate uniform in n or the
spatial parameter, and do not license omitting a crossed pole.

**Boundary prescription.** Howard E. Haber,
[*The Sokhotski-Plemelj Formula*, Physics 215, Winter 2018](https://scipp-legacy.pbsci.ucsc.edu/~haber/ph215/Plemelj18.pdf),
pp.1,3--5, (1)--(5),(12)--(21). Read the standing test-function/decay
hypotheses, both contour-side signs and the full distributional
logarithm-derivative argument. The limit of 1/(x-x_0 +/- i epsilon)
is PV(1/(x-x_0)) minus/plus i*pi*delta_(x_0). Tests are smooth and
nonsingular near x_0; the real-line integrals and integrations by parts
require decay and vanishing surface terms. The contour derivation also
requires local analyticity. This supplies the boundary terms a split
resolvent must retain, not a uniform estimate for the present growing
kernel. Appendix A was viewed for context but its separately cited
Fourier-integral evaluation is not imported; Appendix B was not inspected
in full and is not needed here. No L666 boundary value is calculated here.

**Stronger Cauchy-decay lead.** Mishko Mitkovski and Alexei Poltoratski,
[*Polya sequences, Toeplitz kernels and gap theorems*, arXiv:0903.4499v2](https://arxiv.org/pdf/0903.4499v2),
26 May 2009, Lemma 3 and complete proof, pp.7--8. For a measure of
finite total variation, vanishing Fourier transform on [-a,a] is
equivalent to exp(x*y) times its Cauchy integral at i*y tending to zero
as y tends to either infinity, for every x in [-a,a]. The proof uses
finite-measure Fubini/dominated convergence and a Cartwright-class
uniqueness argument. It provides no uniform growing-product estimate.
L697's comb has infinite variation; modulation does not repair that
hypothesis. Weighting/truncation would need its own gap and error control.
The criterion does not import TARGET or its finite-M/endpoint bounds.

### Search record, access and limits

External queries included `Fourier transform rational function pole upper
lower half plane Cauchy kernel Sokhotski Plemelj formula lecture notes`,
`spectral gap measure rational test functions finite geometric sum
exponential decay Fourier gap`, `"spectral gap" "rational" "measure"
"Cauchy transform"`, `"Fourier" "finite geometric" "spectral gap"
measures`, `"rational functions" "Fourier transform" poles upper half
plane theorem`, `Poltoratski spectral gaps measures Cauchy transform
exponential decay iy gap lemma`, and `"spectral gap" "Cauchy transform"
"exponential"`. The final Haber query located an accessible author copy.
No exact matching theorem was identified; that search result is not a
claim of originality or an impossibility theorem.

Makarov--Poltoratski, *Two-spectra theorem with uncertainty*,
[author manuscript](https://people.math.wisc.edu/~poltoratski/Uncertainty.pdf),
Remark 3 p.20 and reference [30] p.32, was used only to locate the
Cauchy-decay criterion. The journal reference says Lemma 4.5; the
inspected v2 criterion is Lemma 3. Journal numbering was not verified.
Poltoratski arXiv:0908.2079v2 was screened at its finite-measure setup
and model-space Lemma 7 statement; its broader gap theorem and proofs
were not imported or assessed for this target.

The CMI Krishnaswami notes were accessible initially at the metadata
and search-excerpt level, but subsequent passage fetches timed out;
the shell could not resolve the host. They are not an inspected proof.
The inaccessible alternate Haber URL was replaced by the author copy
read above. These access failures leave no essential source blocker:
the elementary pole, convergence and boundary interfaces were obtained
elsewhere. No claim depends on the failed fetches or snippets. More
general Wiener--Hopf, frame and gap-characteristic hits were not read
as target theorems and supply no evidence here.

### Bounded mathematical continuation and decision

EXPLORE is appropriate: the sources supply standard interfaces but no
matching finite estimate, and the relevant local stops do not already
settle this particular signed mechanism. After separate approval, make
one attempt at the unchanged TARGET. Its essential local inputs are
L666, audited L697 and its L696/L694/L693 hypotheses; L683 (7) is an
available exact finite identity. L683--L686 and L695 remain scope
comparisons, not coercivity or small-tail premises for the target.

The proposed mechanism is a signed frequency-side spatial-resolvent
treatment. Its bounded test is whether the complete finite polynomial
can retain a positive exponential margin uniformly for |zeta|=1 on
one fixed angular arc. Account for both resolvent sides and any boundary
case, every crossed-pole or principal-value term if a split is used,
the exact M=n/3 remainder, every required comb sample and both finite
endpoints. Alternatively keeping the finite polynomial intact avoids
assuming that its pieces are separately legitimate infinite tests;
it does not remove the obligation to estimate the whole expression.
No new representation, residue, growth bound or cancellation estimate
has been derived in this review.

Continue only with fixed delta,c>0 and finite C,N for the original
profile, or an independently checkable obstruction that changes the
research decision. Shrinking arcs, retuned n-dependent profiles, omitted
moments/poles/endpoints, and unquantified distributional limits do not
meet the threshold. If the signed resolvent attempt fails, preserve the
specific failure and require a materially different input or refined
mechanism before repeating it. A failed proof does not itself refute
TARGET. Even success leaves the angular complement, logarithmic
integration, H/support, actual-Xi realization and mixed signs open.

Matching Mathlib coverage for the complete estimate has not been checked.
Supporting convolution, Fourier and residue results are not being
represented as a full matching theorem. No lemma, mathematical script,
numerical certificate, DAG edge or PROOF assembly was changed in step 123.
