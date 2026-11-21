# Three-interval head-margin source review: completed step2161

TARGET: Review source coverage for certifying C919c's uniform head margin above 1/2000000000 from three real zero pairs confined to disjoint fixed intervals on 0<=lambda<=1/20, using C919d and interval Vandermonde bounds.
CHECKED: 2026-11-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step2161 inspected Gautschi1975 Sections3-4, Boyd-Vandenberghe AppendixA and Polymath Proposition3.1; searched exact Vandermonde/confinement terms and targeted local head failures. No matching actual-family three-interval certificate was found in this bounded search; this is not evidence of novelty or impossibility.
SOURCE_EVIDENCE: Gautschi, Numer.Math.23(1975),337-347, Section3(3.1)-(3.4), Section4(4.1)-(4.1'); Boyd-Vandenberghe, Convex Optimization(2004), A.1.1/A.1.5/A.5.4, pp633-636,648-649; Polymath1904.12438v2 Proposition3.1(i)-(ii); reused step2159/C919d compact-propagation coverage, with Theorem7.2 statement/proof reopened.
COMPARISON: Known inversion and singular-value inputs cover a conditional fixed-box Gram calculation. Neither compact propagation nor local motion supplies the three fixed boxes for actual zeros. Actual confinement remains unpaid; the separately scoped algebraic feasibility test needs no confinement theorem.
GAP: No quantitative head margin or actual zero brackets have been computed. Park the full confinement-and-margin target; test only the frozen hypothetical box in the separate step2161 assessment before considering a new actual-zero certificate.
REASON: The comparison separates source-covered finite linear algebra from missing actual-family placement. Explicit weights and a numerical threshold require a later specialization, not a reproof of general inversion or propagation. No new mathematical result is derived in this literature turn.
LITERATURE_REASON: Changed available hypothesis: C919d now supplies closed-band interior reality and positive-time simplicity. The remaining interval confinement and explicit uniform head-eigenvalue comparison were not covered by the exact propagation IMPORT assessment.
SCOPE: Completed source comparison only. No confinement implementation is approved. The conditional fixed-box calculation is nominated separately in 2026-11-21-h2-fixed-box-gram-test-2161.md and requires the supervisor's separate approval before invocation.

## Original nomination, retained as historical scope

The proposed downstream purpose is C919c's conditional H2 comparison,
not the all-degree/global conclusion. The existing w(x)=
(x^(-2),200*x^(-4),40000*x^(-6)) convention and epsilon=1/2000000000
must be retained. No numerical interval endpoints, head bound or
zero census are asserted by this nomination.

Essential local inputs are L018,L019,L058,C919c,C919d, with C919c's
inherited C919a/C919b/L919 normalization and Decimal contracts.
The review must identify what certifies the presence of distinct
nonzero opposite classes throughout the closed band and what known
bound controls the resulting three-vector Gram matrix uniformly.
Reality alone cannot be substituted for either obligation. Initial
multiplicities must not be silently replaced by distinct zero classes.

Continue only if the comparison yields an independently testable
confinement-and-margin target with all essential source coverage;
if the known bound is inadequate or confinement needs an unpaid
uniform separator, name that obstruction and refine or park the
dependent target. Do not rerun outer-only residue reconstruction,
the fixed inner-contour sup-norm budget, or the L917/L920/L922
moment-box mechanisms. Their stop evidence remains unchanged.

This proposal introduces different head observables (real-node
intervals), not a new evaluator or a precision/mesh refinement of
those stopped mechanisms. Its adequacy remains to be reviewed.
It is not labeled a central creative mechanism: no supplied estimate
connects this finite three-node problem to uniform degree or global
positivity. No cross-notebook input is proposed. Full matching
Mathlib coverage is unchecked. The next turn is literature-only;
this file is not a ready research authorization.

## Completed comparison, 21 November 2026 (step2161)

The main gap is still L030-L032/C032a all-degree actual-Xi mixed
positivity. The intermediate purpose remains a finite H2 head margin,
not a uniform-degree or global implication. C919c and C919d were read
completely; the relevant L919 matrix/audit passages were checked.
No lemma, mathematical script, zero enclosure or numerical bound was
created. The original nomination above does not remain a pending task.

### Known finite-matrix input

Walter Gautschi, *Norm Estimates for Inverses of Vandermonde Matrices*,
Numerische Mathematik 23 (1975), 337-347,
[author's scan](https://www.cs.purdue.edu/homes/wxg/selected_works/section_01/051.pdf).
Read Section3, printed p339, including (3.1)-(3.4) and its complete
Lagrange-interpolation argument; Section4, p340, (4.1)-(4.1').
For distinct complex nodes and order n>1 the source uses columns
(1,x_j,...,x_j^(n-1)) and obtains inverse rows from Lagrange
coefficients. Its maximum-row-sum bound is

    ||V^(-1)||_infinity <= max_j product_(k!=j)
                               (1+|x_k|)/|x_j-x_k|.

Equality holds for positive nodes. This is not a spectral-norm
identity or a bound for unseparated nodes. The explicit inverse,
rather than an unnecessary reproof, is the useful input for weights.

Stephen Boyd and Lieven Vandenberghe, *Convex Optimization*, Cambridge
University Press, 2004 (author PDF, corrected seventh printing 2009),
[Appendix A](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf),
A.1.1 pp633-634 (A.1)-(A.2), A.1.5 p636, A.5.4 pp648-649 (A.12).
Read the Frobenius definition, induced-norm definitions, full-rank SVD
and the displayed Gram-eigenvalue/condition-number discussion.
These cover real finite matrices, Euclidean operator norms and the
relation of Gram eigenvalues to singular values. They give no
numerical bound for the notebook's weights. A later proof must track
the diagonal factors, orientation, inverse norm and exact box extrema;
positive determinant alone is not the required eigenvalue margin.

### What the zero sources do and do not supply

Reuse the ready step2159 propagation assessment and C919d's exact
normalization and hypotheses. Reopened Planat-Raymond
[2611.06245v1 Section7](https://arxiv.org/html/2611.06245v1#S7),
Theorem7.2 and its complete proof: boundary nonvanishing preserves
the multiplicity count in that rectangle; local cluster continuation
and the backward multiple-root case give the stated reality and
positive-time simplicity. The proof supplies no effective radii or
brackets. Its Section7.1 separator has a different X; it cannot pay
the smaller interior interval endpoints. The finite-height initial
location theorem is reused only in C919d's already checked scope.

Reused the 9November finite-zero assessment, and inspected
[Polymath1904.12438v2 Section3](https://arxiv.org/html/1904.12438v2#S3),
Proposition3.1(i)-(ii), (28)-(33) and the simple-case product argument.
The simple branch is local and its velocity includes the paired sum
over all other zeros; complex zeros are allowed. The repeated case
has a zero-dependent local remainder, not a uniform numerical radius.
The earlier assessment inspected its full repeated-case proof; that
coverage is reused. C919d does not assert initial simplicity.
Discarding the exterior sum, integrating an unpaid velocity bound,
or substituting positive-time simplicity at zero is not justified.

Consequently no inspected input certifies three distinct nonzero
opposite classes in disjoint fixed intervals throughout the closed
band. A proposed actual-family application still needs certified
placement at zero and either closed-band endpoint signs/separators
or a complete validated motion argument. None is supplied here.
This is a missing certificate, not an impossibility result or an
inaccessible essential source. The dependent confinement task is
parked without retrying the source search.

### Search, overlap and decision

External queries included `Gautschi norm estimates inverse Vandermonde
matrices 1975 real nodes`, `de Bruijn Newman heat flow zeros rigorous
interval enclosure first zeros 0.05`, `Planat Raymond 2611.06245
Theorem 7.2`, `"de Bruijn" "zeros" "interval" "first" "certified"`,
`"H_t" "zeros" "14" "0.2"`, and an author-site singular-value query.
Search snippets and a collective-contraction preprint lead
(2609.37164), other recent heat-flow claims and software repositories
were not inspected as theorem inputs. No comprehensive-search or
originality claim is made.

Local scope: the exact 21November H2 literature/attempt/history paths,
the 9November finite-zero and endpoint assessments, C919a/c/d and L919.
Read the step204 approval-loop and step206 endpoint-inconclusive stops.
The old 5.691e-6 threshold is not the present 5e-10 threshold, but their
logical lesson remains: a tail bound does not pay a head margin.
L917/L920/L922 and both contour stops are preserved. No matching
three-box Gram certificate was located in these checked paths.
The initial status/search call printed excessive untracked-file names;
subsequent reads were narrowed to the paths above. No unfinished work
was reset, discarded or edited outside this literature step.

The independently testable refinement is the conditional frozen-box
calculation in the separate step2161 assessment. Those boxes are
hypotheses for a finite algebraic test, not claims about actual zeros.
Continue only if a certified lower bound exceeds 1/2000000000; an
inadequate bound stops that fixed test without subdivision, a box sweep
or an inferred negative eigenvalue. Success would justify considering
separately reviewed actual confinement, not license it automatically.
All-degree signs and global coverage remain independent gaps.

Full matching Mathlib coverage of the quantitative weighted interval
bound has not been checked; unknown coverage is not evidence of absence.
Outcome: EXPLORATION, completed literature comparison, NOVELTY_UNCHECKED.
The new source coverage is useful preparation, not a mathematical
advance beyond the checked sources or a certified head sign.
