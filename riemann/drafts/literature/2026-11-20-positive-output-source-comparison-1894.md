# Positive-output residual approximation: source comparison1894

20 November2026. Literature only. No new theorem, limit calculation,
positive approximant or separator is established.

## Target and local evidence

Assessment1893's TARGET is unchanged. The main gap is actual-Xi
all-degree positivity in L030-L032/C032a. The intermediate question is
whether C033l's exact residual can be approximated uniformly on [1,2]
by finite mass-one signed width mixtures on [1,2] with output positive
on every Borel set. A construction or full-class separator would test
whether affine approximation can survive this independent positivity
requirement. Cancellation, moments, signed height and realization remain.

Read C032q's signed-law/positivity interface, C033l's exact residual,
C034l's capped threshold, C034n's qualified affine conclusion, and the
complete construction proof of C032u. Reused notes1551/1552/1562/1565
and stop1551; checked completed affine route1893. C033i's arbitrary
signed remainder is not a width representation; C033j's exact-range
exclusion is not an uncapped closure theorem. C034l's positive cap-two
distance cannot be transferred by omitting its variation cap.

## New primary source inspected

Christian P. Robert and Julien Stoehr, *Simulating signed mixtures*,
[arXiv:2401.16828v1, 30 January2024](https://arxiv.org/html/2401.16828v1),
Sections1-3 equations(1),(4)-(10), including the positivity condition
and the decomposition into pairs and a residual. The source works
with Lebesgue densities; the general signed mixture is assumed
nonnegative. For two distinct densities it requires compatible supports
and finite a*=sup(g/f), using (a*f-g)/(a-1) for a>=a*. Pairing needs
componentwise domination constants and compatible allocations of the
given weights. Its decomposition retains a signed residual; the later
rejection step still uses the original nonnegative target density.

This supplies no construction of positive approximants from arbitrary
affine approximants. C032q supplies Borel laws without assumed Lebesgue
densities or computable global ratios. Even with densities, domination
constants and the residual sign remain unpaid. Only the explicit
hypotheses and decomposition were inspected for this comparison.
Simulation correctness, efficiency lemmas, Appendix6 and the assertion
that acceptable pairs always exist are not imported or certified.
No local mathematical specialization of this source is performed.

## Reused theorem coverage

Reuse notes1562's complete statement/proof coverage of Ante Mimica,
*Laplace transform*, Dresden course, 27 April-1 May2015,
[Proposition1.4(i)-(ii), pp6-7; Definition2.3/Theorem2.4, pp14-16](https://web.math.pmf.unizg.hr/~amimica/lt.pdf).
Positive half-line measures with transforms finite for every s>0 have
alternating derivative signs there; Bernstein--Hausdorff--Widder gives
the converse representation from complete monotonicity. Recorded proof
coverage includes the atom at zero and exponential shifts for the
unbounded case. This is a characterization, not a finite sign
certificate or density inside the prescribed width span. The residual
is already a probability; this characterization does not establish its
constrained approximation.

Reuse notes1552's inspected Bertoin2000 Theorem1.2 pp7-8/finite-activity
case p9, Lalley's Definition5.1/(5.2)-(5.4) p12, and Mimica
Proposition1.4(iv)/1.8 pp6-7/9-10, with the direct URLs and proof
qualifications there. C032u supplies an all-Borel positive two-width
family and its exact comparison factor; its range is explicitly
sufficient, not claimed optimal. Notes1562's Blanchard--Lee--Scott2010
Proposition5/AppendixA.2 supplies a sharp measure-domination criterion,
not its actual value. The old automatic optimal-domination stop remains.

Reuse notes1889's signed Riesz and affine norm-closure coverage;
neither imposes output positivity. Notes1551's localization and
certificate hypotheses remain missing. Do not repeat those imports.

## Search, access and duplicate record

Queries: signed mixtures approximation probability density positive;
negative weights mixtures nonnegative density approximation theorem;
positive approximation linear span cone densities signed mixtures;
Simulating signed mixtures arxiv; Bernstein Widder theorem Laplace
transform completely monotone probability measure theorem;
Kruijer Rousseau van der Vaart2010 adaptive Bayesian density estimation
location scale mixtures pdf theorem1.

Kruijer--Rousseau--van der Vaart, *Adaptive Bayesian density estimation
with location-scale mixtures*, EJS4(2010),1225-1257,
doi:10.1214/10-EJS584: the author URL returned404, VU repository403,
and Project Euclid required a security check. Abstract/search excerpts
were seen; no primary theorem or proof was retrieved. No hypothesis
comparison or approximation import from this paper is claimed.
Park this optional lead; do not repeat those accesses without a
materially different source. It is not evidence of an exact matching
result or of mathematical infeasibility.

Bonaccorsi--Hanzon--Lombardi, *A generalized Budan-Fourier approach to
generalized Gaussian and exponential mixtures*, AIMS Math9(2024),
26499-26537, doi:10.3934/math.20241290: publisher abstract/references
only. The full-text link returned the landing page. Its theorem/proof
was not read; it remains an unread certification lead, not an import.

A shell fetch of Mimica failed DNS; the web tool retrieved the PDF,
and notes1562 already cover the relevant proof. No retry is needed.
Duplicate checks covered C032/C033 canonical files and the named
positive-output, first-odd, reverse-domination, finite-Levy and affine
assessments/ATTEMPTS. No completed sharpness classification of C032u's
oriented family was located there. This is not archive-wide absence
or a novelty claim. The initial notebook-scoped git status produced
an oversized pre-existing change list; no unrelated contents were read
and no such work was edited or discarded.

## Decision and bounded continuation

The inspected sampler cannot be used as an automatic approximation
theorem: its hypotheses already spend the missing sign control.
Park that import and optional inaccessible sources. The full d_pos
question remains REVIEW_REQUIRED, without a construction or separator.
This is a source-scope negative that changes routing, not a theorem
that positive approximation fails.

Nominate a distinct test: determine whether C032u's sufficient range
is sharp for eta_a=(1+a)delta_2-a*delta_1, a>=0. Compare the known
sufficient construction with necessary nonnegativity of bounded positive
Laplace integrals at large s. The comparison-factor zero atom and
standard dominated convergence are ready inputs. The actual ratio
limit and necessity calculation are deferred; no new mathematical
claim is established here. Continue to an exact coefficient range or
an informative obstruction; otherwise stop this pair without adding
widths or deciding d_pos. Assessment1894 specifies the test.

This is routine specialization, not a protected creative mechanism.
A justified creative approximation attempt still lacks a concrete
positivity-preserving construction or full-class separator. Full matching
Mathlib coverage is unchecked/unknown. No cross-notebook input, lemma,
mathematical script, PROOF/DAG or scheduler change occurred.
