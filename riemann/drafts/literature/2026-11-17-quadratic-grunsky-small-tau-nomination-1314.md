# Small-tau quadratic Grunsky branch: nomination1314, review1315

TARGET: Assess whether a small-tau implicit-function construction at b=(1,0,0,0,0) can produce a strict-positive-weight solution branch of C031a's full six quadratic-defect equations for the fixed1307 actual-Xi constants, checking theorem hypotheses, local duplicates and known obstructions before any rank calculation or univalence claim.
CHECKED: 2026-11-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1315 read C031a completely, reused1312, searched Grunsky-specific assessments/attempts for small-tau/implicit-function/Jacobian/Joukowski, and compared canonical C030y/C030z with1253/1307/1311 stops. External exact and terminology queries below found local-existence tools and ellipse examples, not a theorem realizing these actual six equations; no novelty inference.
SOURCE_EVIDENCE: de Oliveira arXiv1212.2066v1 Section3 Theorem2 and complete proof, https://arxiv.org/html/1212.2066v1 ; Beckermann-Stylianopoulos1606.00553v2 Section2.1(2.21)-(2.23), https://arxiv.org/html/1606.00553v2 ; reused1312 and reopened Ponnusamy-Wirths1704.08184v1 Theorem1/proof(2)-(4)/Remark1, https://arxiv.org/html/1704.08184v1 .
COMPARISON: The implicit-function theorem requires a verified zero and invertible dependent-variable derivative; it does not supply the needed rank, positive finite limiting weights or full-disk univalence. The ellipse example assumes r>1 and is not an endpoint deformation theorem. Linear stops do not decide these quadratic defects. Approve only a residual/Jacobian/first-order compatibility test under explicit branch assumptions.
GAP: No actual solution branch, rank or first-order feasibility result is established. Test a tau-parametrized C1 branch with finite strictly positive limiting weights; singular, non-C1, vanishing/diverging-weight branches and analytic realization remain unresolved.
REASON: Essential method-level coverage now permits one bounded necessary test, not branch existence or a new analytic construction. A separate newly ready calculation assessment1315 records the exact target for next-turn approval. No mathematical derivation was performed here.
SCOPE: Completed literature-only review of the unchanged nomination. Exactly C031a's five real coefficients, first three indices and fixed1307 constants. No parameter sweep, higher degree, new quadrature, coordinate blow-up, higher-order branch construction or univalence proof.

The following nomination text is preserved as the proposal at step1314;
its statements about missing review are historical. The completed review
and its narrower mathematical continuation appear below.

## Purpose and bounded continuation decision

The main gap remains L030-L032/C032a actual-Xi all-degree positivity.
C031a supplies complete finite equations but no solution. The proposed
base point is a candidate starting point for a local branch, not a claim
that a positive-tau branch exists. No linearization, Jacobian rank,
implicit-function specialization, analytic map or new lemma for this
proposal has been derived in step1314.

A later assessed local branch could produce an exact, actual-constant
formal solution, rather than a solution for some tuple in an outer box.
That could make a separate analytic-realization question concrete.
It would still leave pole exclusion, whole-unit-disk univalence, every
larger block, initialization and singular cases unpaid. A floating
branch, free dimension count or an assumed positive actual block would
not meet the purpose.

The source review should decide whether the local-existence tools give
a bounded rank/strict-sign test and whether known univalence constraints
already defeat the proposed use. If essential coverage is absent, retain
REVIEW_REQUIRED or SOURCE_BLOCKED honestly. If the local branch test
cannot discriminate or a persistent source blocker arises, park it and
choose a materially different target. No repetition of the completed
Cauchy relaxation is proposed. A historical linear stop is not a global
ban; its specific normalization obstruction must still be compared.

Reuse C031a and the unchanged assessment1312 for finite support only.
Essential actual-data context is L025,L027,L030,C030y,C030z,L019,L021,
L036,L037,L917; the fixed1307 numerical input retains its arithmetic
contracts. C031a's strict signs and three polynomial equalities remain
unresolved for actual b. No RH premise or cross-notebook input is allowed.
Full matching Mathlib coverage is unchecked.

This nomination is a source comparison followed, only if justified, by
finite established-method development. It is not a source-ready creative
analytic construction. The creative-route blocker is the lack of both
an actual compatible family and an independently specified analytic
construction that could certify unit-disk univalence; routine algebra
must not be relabeled creative to satisfy scheduling preferences.

## Completed source comparison1315 — 17 November 2026

Main gap: L030-L032/C032a require actual-Xi mixed-form positivity in
every degree. The intermediate target is the proposed small-tau branch
for one finite block. Its plausible use is an exact finite match to
which a later independent full-disk Grunsky argument might apply.
Neither this source review nor a feasible tangent supplies that match.

### Primary theorem and essential proof cases inspected

O. R. B. de Oliveira, *The Implicit and the Inverse Function Theorems:
Easy Proofs*, Real Anal. Exchange39(1),2013/2014,207-218;
[arXiv1212.2066v1,10 December2012](https://arxiv.org/html/1212.2066v1),
Section3, Theorem2 and complete proof. For C1 F on an open subset of
R^n x R^m, F(a,b)=0 and invertible D_y F(a,b) imply a unique local C1
graph y=f(x), with Df=-(D_y F)^(-1)D_x F. Its proof first secures local
injectivity of (x,F), normalizes the invertible matrix, then solves one
equation and the remaining system inductively. The scalar case uses a
nonzero derivative and the intermediate-value theorem. The final chain
rule supplies the derivative identity; injectivity gives uniqueness.
Import this theorem, without reproof. It grants neither existence at a
singular base nor analytic/Puiseux regularity. The newer differentiable
version1708.02065v1 was located but is unnecessary; its stronger
minor hypotheses are not a substitute for the classical rank check.

Applicability obligations for the later calculation: use C031a's full
finite polynomials as six residual equations, with actual constants
fixed, tau as the proposed branch parameter and both positive weights
explicit. First check the base residual rather than assuming it. State
the chosen dependent/free variables and test the required square minor;
a variable count alone is not the theorem's hypothesis. For an assumed
C1 branch the cited derivative identity gives a necessary tangent test.
Any strict-positive-weight conclusion needs positive limiting weights
and continuity, or a separately justified sign argument. This review
does not evaluate the residual, differentiate the equations, determine
rank, solve a tangent system or apply the existence conclusion.

B. Beckermann and N. Stylianopoulos, *Bergman orthogonal polynomials
and the Grunsky matrix*,
[arXiv1606.00553v2,6 July2016](https://arxiv.org/html/1606.00553v2),
Section2.1, equations(2.21)-(2.23). The explicit ellipse has semiaxes
(r+r^-1)/2 and (r-r^-1)/2 with r>1, exterior map
psi(w)=(r*w+(r*w)^-1)/2 and normalized Grunsky matrix
diag(r^-2,r^-4,...). It illustrates contraction and diagonal defect;
it does not prescribe a general defect block. The strict parameter
hypothesis excludes importing the degenerate r=1 case as a theorem
about a neighborhood of the proposed base. No endpoint specialization
or perturbation result is derived here. Reuse1312 for Lemma2.2's
domain and zero-area-boundary hypotheses and its Gram interpretation.

S. Ponnusamy and K.-J. Wirths,
[arXiv1704.08184v1,26 April2017](https://arxiv.org/html/1704.08184v1),
Theorem1, proof(2)-(4), Remark1, reopened to check1312's scope.
For normalized meromorphic f on the unit disk, the pointwise strict
bound |z/f-z*(z/f)'-1|<1 implies meromorphic univalence. The proof
factors the remainder as z^2*omega, bounds omega and integrates to
control divided differences. Remark1 permits a simple pole. Thus
holomorphic signing needs pole exclusion as well as the disk bound;
local coefficient closeness is not this theorem's hypothesis. No such
bound or pole exclusion is claimed for the proposed branch. Failure
of this sufficient condition alone would not stop the family.

### Duplicate and obstruction comparison

C031a's proof gives the complete columns and six full equations.
Assessment1312 remains adequate for their formal provenance; no repeat
Faber derivation is needed. Its Cauchy relaxation is compatible and
will not be rerun. C030y/stop1253 constrain linear c_mn with fixed
weights; C030z/stop1311 constrain linear c_mn with positive diagonal
weights and exclude their unit-disk realization. The former's mixed
coefficient contradiction and the latter's |c11|<=1 obstruction do
not automatically identify with a quadratic column defect. No escape
from either stop is claimed: this is a different system requiring its
own test. Stop1307 was only a four-point search before the later
linear audit; it is not an obstruction to all local branch mechanisms.
Assessment1302's near-disk inverse-spectral comparison is reused via
1312 and supplies no inverse-defect theorem for these actual constants.

Scoped local search: Grunsky-named assessments and stop files for
`small.?tau|implicit.function|Jacobian|Joukowski`, followed by the
specific canonical results above. Only the current nomination and
1302's different inverse-spectral comparison matched. This is not an
exhaustive novelty assessment. External queries: `implicit function
theorem surjective derivative parameter singular base point analytic
branch theorem`; `Grunsky coefficients rational functions Joukowski
slit mapping perturbation univalent coefficient b1 1 area theorem`;
`"Grunsky" "implicit function" Joukowski deformation`;
`inverse Grunsky "defect" matrix realization univalent`;
`"Grunsky" "prescribed" "defect"`; and the de Oliveira title query.
Irrelevant search results and general summaries were not theorem inputs.
The primary arXiv1212.2066v1 recovered the classical statement; an
attempted1708.02065v6 URL was nonexistent, not a persistent blocker.
Reade-Silverman-Todorov's rational-functions lead remains unread as
in1312; it is not essential to the present formal first-order test.

### Decision, bounded test and unresolved cases

SPECIALIZE only to the exact residual/Jacobian/finite-positive-weight
first-order test recorded in calculation assessment1315. A verified
incompatible necessary condition can exclude a tau-parametrized C1
branch with finite positive limiting weights. A compatible tangent
only retains it. Rank deficiency alone proves no nonexistence; a
singular, fractional-power or non-C1 branch, or weights tending to zero
or infinity, needs separate coverage and a different discriminating
test. No higher-order expansion or automatic blow-up is authorized.
Failure must be scoped to the branch class actually excluded. Keep
the broader formal feasibility and analytic questions unresolved.

Continuation inputs: C031a,L025,L027 and the unchanged fixed1307 boxes
in C030z, retaining L019,L021,L036,L037,L917 arithmetic/analytic
qualifications. L030-L032/C032a explain the intended use. Larger
blocks, initialization, singular cases, actual identification and
unit-disk univalence remain unpaid. No RH or cross-notebook premise.

Mathlib: inspected the current official
[Implicit](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/Implicit.html)
module documentation and followed its
[ImplicitContDiff](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/ImplicitContDiff.html)
link. `HasStrictFDerivAt.implicitFunction` supports finite-dimensional
surjective derivatives; `ContDiffAt.implicitFunction` is the documented
smooth invertible-partial-derivative version. These are supporting
tools, not matching Grunsky/actual-Xi branch results. Full matching
coverage and Lean verification are unchecked. No lemma or mathematical
script was written; this review settles coverage, not branch feasibility.
