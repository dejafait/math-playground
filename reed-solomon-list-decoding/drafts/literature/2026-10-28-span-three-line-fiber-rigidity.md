# Span-three line-fiber rigidity — bounded source comparison

TARGET: Test whether every auxiliary-line image in the pinned L030 full-sheet model with coefficient-difference span exactly three has affine dimension at most one over K.
CHECKED: 2026-10-28
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed bounded searches for restricted-direction line maps, line-to-plane planarizations, higher-dimensional net embeddings and finite-field variants; exact queries and reading limits appear below. Reused the cone/full-sheet assessments and checked ATTEMPTS/031–032,109 and the saved working reduction. No exact matching theorem or permitted counterassignment was found; this is not evidence of novelty.
SOURCE_EVIDENCE: Inspected Artstein-Avidan–Slomka arXiv:1604.01762v1 Theorems 1.3/1.4 and 2.7 with its complete two-case proof and Remark 2.8, printed pp. 6,11–14; Khare–Tikaradze arXiv:2212.02429v3 Theorems 1.3/1.8 and relevant proof passages, pp. 2–3,5–6; Petrushchenko–Timorin, On Maps Taking Lines to Plane Curves (2015), Section 1 definition, Main Theorem and degeneracy/duality descriptions. Reuse the cone assessment for Laguerre and planar-multinet comparisons; no theorem is imported as a span-three result.
COMPARISON: Restricted-direction collineation theorems assume injectivity and line images already lying on full lines over one field; affine concatenation assumes affine-linear restrictions. Smooth/analytic planarization classification requires all source lines over R or C and allows genuinely quadratic images. None upgrades these seven finite direction classes with repeated images and different characteristics to the required fiber bound; planar net exclusion remains conditional on the missing bridge.
GAP: Determine whether all seven complete evaluation classes force each auxiliary-line image to have affine dimension at most one under arbitrary permitted labels and repeated assignments, or whether an exact compatible counterassignment exists.
REASON: The inspected hypotheses expose the missing local incidence implication rather than providing a citation for it. A bounded all-label fiber test is justified under EXPLORE; no matching theorem, universal absence claim, reproof or mathematical result is asserted. The direct residual-rank route stays parked.
LITERATURE_REASON: The target changes from the audited span-two common-form implication to a span-three local affine-dimension assertion; neither the common-cubic assessment nor the prior cone comparison assesses this exact intermediate claim.
SCOPE: Pinned L030 parameters, every actual 61-core and bijection, all seven complete directions, K=E or F, quadratic assignments with repetitions, coefficient-difference span exactly three; no retention or RS-transfer assertion.

## Exact proposed assertion, not a result

Retain q=137, T={16,64,70,102,112,118,121}, E=F_65537,
F=F_(65537^28), H=<19139> of order 1024 and k=64. Let C be any
61-subset of H and sigma any bijection from (T times F_137) disjoint
union four dummy points to H minus C; put x_(t,y)=sigma(t,y).
Let K=E or F. For every P=(u,v) in F_137^2 let g_P in K[X] have
degree at most two and have a constant value at x_(t,y) on
A_(t,y)={P:u+tv=y}. Allow zero and repeated polynomials. Assume
dim_K span{g_P-g_(0,0)}=3.

The proposed bound is: for every (t,y) and any P_0 in A_(t,y),
dim_K span{g_P-g_(P_0):P in A_(t,y)}<=1. It has not been derived
or asserted to be new. This completed assessment covers a later bounded
attempt at this exact assertion, subject to the supervisor's separate
next-turn approval; no mathematical attempt occurs in this review.

## Relevance and bounded test

Investigate whether incidence between the other six complete direction
classes and a fixed fiber forces its coefficient images onto a line.
Do not assume that a projection of the cone preserves a planar net.
A proved bound could support a later degeneration-aware line-preserving
model and comparison with L137. The further implication to a global
plane or collapse is unresolved. Even full-sheet collapse would leave
partial retention and RS transfer open; no safety bound follows here.

A later mathematical attempt should seek an all-label proof or an
exact permitted compatible assignment with a rank-at-least-two line
fiber. Such an assignment refutes this diagnostic, not the main RS
target. If neither is obtained in one bounded attempt, preserve the
exact missing incidence implication; repetition needs materially new
evidence or a refined mechanism. Generic-label assumptions, sampled
ranks and the unchanged 74528-by-408 matrix do not pass this test.
ATTEMPTS/109 remains the stop evidence for that global-rank mechanism.

## Required comparison and input limits

Compare exact and stronger primary results on restricted-direction
line maps, degenerate grid embeddings and conic-normal plane
configurations. Reuse the cone/Laguerre comparison. Check assumptions
of injectivity, all auxiliary directions, equal characteristics and an
existing planar embedding before importing anything. A failed search
does not establish novelty.

L030 supplies the model. L135/L136/L137 are planar comparisons only;
their conclusions are not premises for span three. The full-sheet
assessment and ATTEMPTS/109 preserve the earlier reduction and stop.
No cross-notebook input is needed. Mathlib coverage is not checked.
The invocation completing this assessment is literature-only; no lemma
or mathematical script is changed. The exact target is now assessed as
EXPLORE, rather than left at REVIEW_REQUIRED.

## Primary statements and applicability

### Restricted-direction collineations

Shiri Artstein-Avidan and Boaz A. Slomka, *The Fundamental Theorems of
Affine and Projective Geometry Revisited*,
[arXiv:1604.01762v1](https://arxiv.org/pdf/1604.01762v1), 6 April 2016.
Theorems 1.3/1.4 (printed p. 6) classify injective maps R^n -> R^m
mapping every line in n, respectively n+1 generic directions **onto**
lines. Theorem 2.7 (pp. 11–13) gives the two-direction form
f(s)u_1+g(t)u_2+f(s)g(t)u_3, after translation, with u_1,u_2
independent and f,g normalized bijections. Remark 2.8 (p. 14) extends
this theorem to a common field other than F_2. The complete proof's
parallel-image case uses Lemma 2.6; its skew-image case uses three
complete image lines and their transversals. Both cases were read.
These hypotheses already demand one-dimensional fiber images and
injectivity. Our assignment permits repetitions, has only plane
containment initially, and has different source/target characteristics.
No cross-field or line-into-plane extension is stated or imported.
Even proving our proposed fiber bound would not by itself establish
the source theorem's onto or common-field assumptions. This is a
comparison, not an application or a reason to assume the desired bound.

### Concatenation and non-bijective line maps

Apoorva Khare and Akaki Tikaradze, *Recovering affine-linearity of
functions from their restrictions to affine lines*,
[arXiv:2212.02429v3](https://arxiv.org/pdf/2212.02429v3), 24 March 2023;
published *Journal of Algebraic Combinatorics* 58 (2023), 761–773,
[DOI](https://doi.org/10.1007/s10801-023-01233-7).
Theorem 1.3 (p. 2) treats f:M->R for a free module with basis indexed
by I over a unital commutative ring. Integers 1 through |I| must be
nonzerodivisors (or use its integral-domain alternative). Restrictions
on every basis-parallel line and a specified line with nonzerodivisor
coordinates for each finite subset of the basis must be affine-linear.
It concludes global affine-linearity. Theorem 1.8 (p. 3) uses vector
spaces over one field other than F_2, source dimension at least two,
all affine lines mapped onto lines, and the nonincidence condition
v outside ell => f(v) outside f(ell); it concludes injectivity and
semiaffine linearity with a field automorphism. Inspected proof passages
are the Vandermonde elimination (p. 5) and injectivity/plane preservation
(p. 6). They require the stated restrictions, not mere plane containment.
Our repeated, cross-characteristic assignments meet neither set of
premises. No additive identification or scalar-coordinate
affine-linearity is supplied by the pinned model.

### Line-to-plane planarizations

Vsevolod Petrushchenko and Vladlen Timorin, *On Maps Taking Lines to
Plane Curves*, accepted 16 October 2015, published article
[Section 1 and Main Theorem](https://amj.math.stonybrook.edu/html-articles/Files-2015-2024/15-27/).
A planarization is a sufficiently smooth map on an open subset of
RP^2, or an analytic map on an open subset of CP^2, taking the portion
of **every** line into a hyperplane. For target P^3, the Main Theorem
classifies it on a nonempty open subset as trivial, co-trivial,
quadratic or dual quadratic. Section 1's definitions and discussion
were read; later classification proofs were not imported or audited.
Trivial means image contained in a plane; co-trivial means the
containing planes may all be chosen through a fixed point. The source
explicitly includes quadratic maps taking lines to conics, not only
to lines. This does not assert fiber dimension at most one, even in
its own setting. Here there is no smooth/analytic domain, all-line
hypothesis, or same-characteristic geometric extension. The seven
direction families and their conic evaluation normals do not provide
such an extension by citation. This broader comparison therefore
supplies no usable import; it is not a counterexample to our
additionally constrained finite model.

## Search record and limits

Searches on 2026-10-28 included:

- `"quadratic polynomials" "affine plane" "constant" evaluations rigidity`
- `"seven directions" "planes" map rigidity`
- `"coefficient" "span" "fiber" "quadratic" "nets"`
- `finite grid maps seven directions planes affine dimension line rigidity projective space`
- `nets embeddings projective space hyperplanes dual multinet dimension three`
- `finite field direction preserving maps restricted directions fundamental theorem affine geometry degenerate`
- `"nets" "embedded" "projective space" hyperplanes`
- `"maps" "lines into planes" finite field`
- `"conic" "dual" "multinet" space`
- `"planarizations" "lines" "planes" Timorin`
- `"Recovering affine linearity" Khare Tikaradze arxiv`
- `"net" "embedding" "planes" "PG(3"`
- `"planarization" "finite field"`
- `"net" "quadratic cone" "rigidity"`
- `"restricted directions" "maps" "finite fields" line preserving`
- `"line" "plane" "maps" "different characteristics" geometry`

Exact-description searches above returned no matching statement;
generic curve texts and unrelated uses of seven directions were not
read as theorem inputs. Broader `"planar maps" "finite fields" geometry` results concerned
cryptographic planar functions, not this incidence assertion. Net
embedding searches also returned derivable/subplane-covered nets and
flocks; their complete classification theorems remain unread leads,
not inputs. In particular, no embedding theorem from those snippets is
assumed to apply to our repeated point-plane configuration. The prior
cone assessment remains the source of the inspected finite Laguerre
comparison; it is reused without another EKR/stability search. Planar
light-multinet/ordinary-net exclusion is still a comparison requiring
a planar incidence bridge. L135–L137's accepted span-two arguments
are not silently extended or treated as span-three premises.

The DOI fetch initially failed; the journal page and pinned arXiv v3
were subsequently accessible. A web PDF screenshot failed; the PDF
theorem/proof text was accessible. Neither is an essential source
blocker. This bounded review neither proves that no matching theorem
exists nor certifies originality. Mathlib full/supporting coverage for
the target remains not checked; there is no Mathlib absence claim.

## Decision and continuation boundary

The main gap is still arbitrary-center 67/68 safety. The intermediate
target is exactly the displayed affine-dimension bound, under the
original full-sheet hypotheses. Its plausible downstream use is a
degeneration-aware line model for span three; global collapse,
partial retention, compatible laws and RS transfer remain unresolved.
There is no mathematical gain toward the 955–957 bracket in this turn.

Continue with one bounded proof attempt that fixes a potentially
rank-two fiber and uses the other six complete direction classes
without presuming injectivity or planar projection. Decisive evidence
is either a proof uniform in C,sigma and K, or a fully specified
permitted compatible assignment of global difference span exactly
three with a fiber of rank at least two. A relaxed conic-normal model,
generic labeling, sampled rank or repeated residual-matrix reformulation
does not decide this target. If neither certificate emerges, save the
precise missing incidence implication; another attempt needs a new
input or refined mechanism. ATTEMPTS/109 stays stopped, and the two
omission failures recorded with L135 stay preserved. This is source
readiness for an independently testable local mechanism, not approval
of any uncovered mathematical conclusion.
