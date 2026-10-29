# Fixed-half-plane negative-witness cutoff: source comparison

TARGET: Test whether L320's negative-witness cutoff can be sharpened to ceil(c log(2+|a|)+B_c) for every c>3/16 under L452's retained strict Re(s)>7/8 premise.
CHECKED: 2026-10-24
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Read L320 and L266 in full, L452's quantitative proof, L018's normalization, the required October 21 overlap/register and the existing endpoint derivative assessment; checked scoped witness/anchor duplicates and L322's complete obstruction. Searched exact witness/cutoff and Littlewood reciprocal terminology; primary passages and limits are recorded below.
SOURCE_EVIDENCE: Titchmarsh, second edition (1986), Theorem 14.2 and proof, printed pp. 336–337, especially (14.2.5)–(14.2.6); pinned September 30 manuscript Theorem 1.1 and complete Logarithmic control lemma (label lem:logarithmic-control, equation eq:disk-control); DLMF 5.11.1/5.11.3 sector and remainder statements. Reused prior analytic-logarithm coverage, without repeating its audit.
COMPARISON: The inspected sources cover the two-sided subpower logarithm mechanism and complex Stirling, while L266 supplies the central-zero-safe witness interface. L320 covers only c>1/4; L452's stated derivative strip does not cover all proposed anchors. No inspected theorem states this exact cutoff; a changed-domain specialization and application are needed, with no originality claim.
GAP: Prove uniform reciprocal and upper bounds at fixed real parts strictly above 7/8, propagate a completed-zeta bound across the whole circle strip, and apply L266 with an anchor above the externally narrowed zero strip. Check all real heights, parameter order, complete power losses and independence from displacement and central multiplicity.
REASON: Essential quantitative coverage is now inspected; a research attempt may specialize known mechanisms rather than infer bounds from nonvanishing or reprove the external zero-free theorem. This literature-only review establishes no new anchor estimate or cutoff.
SCOPE: The exact TARGET, with fixed 3/8<eta<R<1/2 when useful, arbitrary fixed c>3/16, existential B_c independent of height and zero displacement/multiplicity, and the retained external-input qualifications. No boundary anchor, sign theorem or all-index conclusion is covered.

## Main gap, intermediate target and discriminating test

Initial low-index Laguerre signs at unbounded heights and global mixed
positivity remain unproved. The exact TARGET is an intermediate witness
bound: if established, it would reduce the initial sign segment sufficient
to exclude an off-line zero. It would not prove any sign in that segment.
The conditional partial bands motivating the nomination do not fill it.

Continue to one bounded specialization attempt if the inspected logarithm
mechanism can provide upper and reciprocal subpower control on the fixed
anchor/boundary lines and hence a circle-to-anchor ratio with sufficiently
small power loss for the stated c. Stop this implementation if a loss
cannot be made small with parameters fixed before height varies, if a
central denominator reappears, or if it needs a boundary nonvanishing
claim. Record the actual failed threshold; do not assert the cutoff from
source coverage alone. No such bound has been derived in this review.

## Primary theorem and essential proof cases actually read

E. C. Titchmarsh, *The Theory of the Riemann Zeta-function*, second edition
revised by D. R. Heath-Brown (1986), [Theorem 14.2 and its proof,
pp. 336–337](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf#page=173):
Chapter XIV assumes RH. The printed logarithm estimate is uniform on a
fixed closed substrip to the right of 1/2; equations (14.2.5)–(14.2.6)
state subpower upper and reciprocal bounds. Read the Borel–Caratheodory
step and the three-circles step, including their analytic-logarithm and
Euler-convergence inputs. The printed theorem cannot be imported with
7/8 substituted into its hypothesis. Its proof mechanism, with a different
zero-free domain and fixed margins, is the relevant specialization.
This reproof is justified by that changed hypothesis and the exact uniform
domains needed here, rather than by novelty. The earlier endpoint review
already assessed the same mechanism; its fixed numerical derivative
exponent and narrower strip are not a theorem about the present anchors.

OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re s > 7/8*,
September 30, 2026, [pinned primary source](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex),
commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a`: inspected Theorem 1.1
and the full lemma titled **Logarithmic control**, label
`lem:logarithmic-control`, including `eq:disk-control` and its proof.
That lemma concerns Hecke functions and a regularized Dedekind zeta,
not literally the present Riemann-zeta witness. It uses a zero-free disk,
a bounded Euler-normalized logarithm at its center, polynomial growth,
Borel–Caratheodory and three-circles; both exponential signs give
subpower upper and reciprocal estimates. It is corroborating mechanism
coverage, not a direct import for zeta or permission to divide a
Dedekind-zeta estimate by an uncontrolled factor. No additional audit of
its antecedent growth lemma or full manuscript is claimed or needed for
this use of the classical mechanism.

The load-bearing external premise remains precisely Theorem 1.1 as
registered locally: strict Re(s)>7/8, principal pole allowed, boundary
not excluded, manuscript and formal import closure locally unaudited.
Neither a new proof of that premise nor Liu's stronger boundary is part
of this target. Retain these qualifications in any later lemma.

[NIST DLMF 5.11.1 and 5.11.3](https://dlmf.nist.gov/5.11), including the
closed-sector condition |arg z|<=pi-delta and the complex remainder
paragraph, were inspected. They cover the gamma factors on fixed
positive-real-part vertical strips. Their use still requires the later
application to retain the common exponential decay at both shifted
heights. Direct TeX endpoints returned an unsupported-content-type
error; the HTML equations and sector text were accessible and read.
There is no essential source blocker.

## Local comparison, failure scope and necessary application work

L266's full proof requires 0<b<eta<R, a positive H_a(eta) lower bound,
and a supremum on the **complex** circle |y|=R. It allows Xi(a)=0 of
arbitrary multiplicity; its constant coefficient is nonnegative and the
proof never divides by the central value. Thus no center-deflation
lemma is needed. L018 fixes Xi(z)=xi(1/2+iz), the functional equation,
reality, and the exact zero correspondence. The register already states
the conditional narrowed zero width |Im z|<=3/8. Any application must
invoke this width explicitly to put every putative nonreal zero below
the new anchor; L266's old classical width alone would not suffice.

L320's full strip proof and gamma cancellation can be reused as methods,
but its inequalities were proved with R>eta>1/2. Neither its reciprocal
Dirichlet-series bound nor its stated conclusion can simply be applied
at eta<1/2. L452 proves a derivative bound only for Re(s)>=63/64;
this does not cover anchors arbitrarily close to Re(s)=7/8. Its inspected
Euler-normalized logarithm argument and the existing derivative-source
assessment supply reusable technique, rather than the missing estimate
on the enlarged domain.

The later attempt should establish two-sided subpower zeta control on
fixed compact real strips strictly above 7/8 at large absolute heights.
Reserve an actual disk neighborhood, avoid the pole at one, and bound
the normalized logarithm, not merely its real part. Use only absolute
Euler convergence to the right of one. For the circle, a boundary bound
must be propagated through the full completed-zeta strip using its
entirety, reflection and a valid growth/damping argument. Keep the two
heights a plus or minus Im(y), not just the diameter y real. For the
anchor, establish nonvanishing and positivity on the bounded height
range as well as the large-height asymptotic; account for the completed
polynomial and gamma factors. Transfer all power losses to L266's
ceiling formula before optimizing fixed eta,R and loss parameters for
the given c. No uniform constant at eta=3/8, c=3/16, or under shrinking
margins is sought. B_c may depend on fixed c and the retained input,
not on the zero's displacement, multiplicity or height.

Read the full L322 obstruction and the recorded local-circle/elliptical
attempts. Its signed-tail obstruction fixes eta>1/2, and its exterior-arc
argument stays in absolute convergence. It remains valid there and
prevents merely reshaping that exterior-anchor remainder to beat 1/4.
The new test changes the anchor domain using the fixed-half-plane input;
it neither contradicts nor reproves L322. The earlier central-denominator
failure and L266's repair are preserved. No historical stop is treated
as a global ban.

## Search scope, classification and continuation

Queries included `zeta zero-free half-plane reciprocal Littlewood`,
`Xi negative coefficient logarithmic witness zeta`, `Laguerre inequalities
witness zeta cutoff`, `zeta negative-witness cutoff`, and
`zeta 3/16 cutoff`. An initial broad Laguerre search returned a manuscript
about pointwise large-order and mean Laguerre inequalities; only its
returned preview was seen, and it is not a source for this witness target.
Other returned research-project pages and a rendered copy of the
quasi-Riemann manuscript were leads only. The logarithmic-control lead
was followed to the pinned primary source above. No search result is
used as a theorem, and no failed search establishes novelty.

Scoped local searches covered anchor/witness attempts, the applicable
literature assessments, and L3xx/L45x/L46x lemma text. L320 and L322 are
the relevant prior cutoff and obstruction. The October 21 broad overlap
screen was reused rather than repeated. No exact matching cutoff was
found in these checks; this is a bounded comparison, not an exhaustive
bibliography. The appropriate later classification is REPRODUCTION for
a known-mechanism specialization, with no progress beyond the checked
sources claimed. Full matching Mathlib coverage and supporting API names
remain unchecked; absence is not asserted.

Essential continuation input IDs are L018, L266, L320 and L452, with
L005 for Euler-log normalization and the foundations' standard growth
and Stirling inputs. L322 is a scope obstruction, not a premise of the
proposed cutoff. C460b is motivation only. Unresolved obligations are
the new uniform analytic bounds and their whole-strip/witness
application; initial signs, bounded-height sign coverage, mixed
positivity and selected-law/regulator realization remain independent.

This is approval of source coverage for the exact saved TARGET only.
The mathematical attempt is future work, subject to the supervisor's
separate approval of a newly changed ready assessment. No lemma,
mathematical script, DAG edge or PROOF.md argument was changed here.
