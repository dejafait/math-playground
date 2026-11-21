# Periodic Jacobian moments — source comparison

TARGET: Test whether periodic trace/determinant integral identities obstruct a global nonnegative L847 graph realizing L861's conditional four-cycle, retaining the full F and J zero sets.
CHECKED: 2026-11-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Bounded searches for periodic gradient minors, null Lagrangians, trace/determinant positivity and holomorphic-volume positivity located Ball–Currie–Olver (1981) and Olver–Sivaloganathan (1988); primary theorem statements and relevant proof cases were read. Compared L847's full pullback/homology proof, L861's restricted conclusions and the named contact/full-phase/annular stops; queries and limits below.
SOURCE_EVIDENCE: Ball–Currie–Olver, JFA41 (1981) 135–174, Section3 mean definition p140, Theorem3.4(iii) p143, Theorem4.1 p149 and divergence case (4.2) p150; Olver–Sivaloganathan, Nonlinearity1 (1988) 389–398, assumptions/Proposition2 pp391–392, Theorems7–8/proofs and local-only remark pp394–395; Lebl SCV v4.4, TheoremB.2 p206 and TheoremC.6/regularity remark p224. Links and qualifications below.
COMPARISON: Sources cover unweighted periodic derivative moments and local inhomogeneous null-Lagrangian structure, not a sign estimate for L847's varying complex coefficient or a global graph with the prescribed contacts. L847 already supplies the full-form homology equality; L856–L857 concern specified local collars rather than this whole-torus test. No additional actual-G restriction has yet been established.
GAP: Apply only the two known unweighted moment identities to the exact L847 density and decide whether an extra sign/range restriction follows under the unchanged hypotheses; no quotient at zeros, unproved image estimate, global primitive, prescribed collar or formal-field realization may be assumed.
REASON: Essential source coverage is now adequate for one bounded specialization, not for an automatic obstruction or extension theorem. This literature-only step neither calculates that specialization nor approves new mathematics; the completed assessment is available for separate supervisor approval before the mathematical test.
LITERATURE_REASON: The whole-torus derivative-moment target was REVIEW_REQUIRED at invocation start; the ready contact-degree/germ assessments did not cover these identities or the inhomogeneous/global-period qualification.
SCOPE: Actual L847 G,R,C,F; real C2 periodic exchange-symmetric u; full real q=F(Phi_u)det(I-iDu)>=0; conditional four-zero data of L861(1), with exactly the prescribed eight G contacts if a global realization is hypothesized. Keep J zeros away from contacts and the full F zero divisor, including the exchange diagonal. No actual quadruple, global realization, bound on u, prescribed collar, RH or zero-free region is assumed.

The nomination below is preserved verbatim as the pre-review problem
specification. Its pending-source language is superseded by the completed
comparison at the end of this file, not by a mathematical test.

## Original nomination: purpose and bounded discriminator

The main gap is L030-L032/C032a actual-Xi all-degree mixed positivity.
L861's accepted conditional census has exhausted a zero-data-independent
contradiction from its established counts and jets. The proposed
intermediate target concerns integral compatibility of the derivatives
over a whole periodic graph. A substantive constraint could rule out
or narrow future global completions; it would still leave contour
existence in the unrestricted class and transfer to all degrees open.
The scope does not certify the conditional zero data.

The first task is source comparison only. Retrieve exact primary
hypotheses for periodic Jacobian/null-Lagrangian integral identities
and relevant signed-density applications at C2 regularity. Compare
with the complete pullback in L847 and the audited local constraints
in L861. Do not reprove a standard divergence or determinant identity.
Assess whether the proposed use supplies a restriction beyond those
identities and the already recorded full-form homology equality.
No formula, inequality or mathematical script is derived in this
nomination, and no Mathlib coverage has been checked for the target.

If source coverage supports a distinct test, bound it to the two
integrals associated with tr Du and det Du and their relation to the
complete pointwise density. Continue only if they impose an additional
sign/range condition under the stated hypotheses. Abandon this mechanism
if they are automatic bookkeeping for any periodic graph, if the sign
test becomes merely the original q>=0 assertion, or if a contradiction
requires an unproved bound on F(Phi_u) or an unjustified quotient at its
zeros. Do not treat formal fields satisfying selected moments as an
actual graph. Any further analytic estimate is a changed target.

## Scope comparison and route choice

Compared three continuations: repeating individual contact balances,
seeking a certified actual quadruple, and this global derivative-moment
test. The first is stopped by the conditional assignment; the second
has no justified zero-data input and would not resolve global extension.
Nominate only the third for source assessment. It interrogates the
whole graph rather than contact counts or free local germs, but whether
that distinction survives mathematical comparison is unresolved.

Preserve these exact records:
`ATTEMPTS/2026-11-06-individual-divisor-count-only-scope-limit.md`,
`ATTEMPTS/2026-11-06-full-phase-two-period-obstruction-stop.md`,
`ATTEMPTS/2026-11-06-forced-contact-linking-import-scope-limit.md`, and
`ATTEMPTS/2026-11-06-free-germ-boundary-scope-stop.md`.
Before approving a calculation, compare also the previously recorded
annular boundary-moment stop; an integrated identity alone does not
supply a prescribed extension. No historical stop is made a global ban.

Essential local inputs for continuation are L847 and L861, with L860
only if its exact germ construction must be inspected. No cross-notebook
theorem is needed. Actual zero data, global completion/avoidance, and
Xi signs remain unresolved. Creative priority is considered: no new
central proof mechanism is justified yet by a pair of standard integral
identities. Missing comparison and an unestablished quantitative link
to the actual F are the blockers; do not label a routine specialization
creative or repeat the completed audit to fill the gap. Source review
must determine whether a substantive mechanism warrants development.

## Completed source comparison — 6 November 2026

Completed task: LITERATURE / NOVELTY_UNCHECKED, actual task
literature_comparison, outcome EXPLORATION. New source coverage is
recorded; no mathematical discriminator was evaluated. In particular,
neither global existence nor a new obstruction is established.

### Primary periodic-minor input

J. M. Ball, J. C. Currie and P. J. Olver, *Null Lagrangians, Weak
Continuity, and Variational Problems of Arbitrary Order*, Journal of
Functional Analysis **41** (1981), 135–174,
[author-hosted published paper](https://people.maths.ox.ac.uk/~ball/Papers/Ball%2C%20Currie%20%26%20Olver%201981.pdf).
Read Section3's mean definition p140, Theorem3.4 p143, Theorem4.1
p149 and its divergence proof case (4.2) p150. For continuous L
depending only on kth derivatives, Theorem3.4(iii) characterizes
null Lagrangians by

    M[L(D^k v)] = L(M[D^k v])

for v in C^k(R^p) with almost-periodic D^k v. M is the large-domain
mean. Theorem4.1 characterizes these L as affine combinations of
kth-order Jacobian determinants. Its opening proof writes each
Jacobian as a divergence. For k=1 the eligible functions include
individual gradient entries and determinant. Continuous periodic
gradients fall within the almost-periodic case. This supplies the
standard mean identity, not a sign assertion about variable weights.

Applicability obligations for the future test are narrow: use the
periodic lift of the stated real C2 u, the source's p=q=2,k=1 case,
and the normalized fundamental-cell mean. State the cell normalization
and check the mean of the derivative entries before specializing.
Do not reprove the null-Lagrangian classification or divergence formula.
The source's matrix variable is Du, not L847's complex J. Its theorem
does not prescribe any contact set. No trace/determinant specialization
or new consequence for actual F is derived in this review.

### Inhomogeneous weights and the global qualification

P. J. Olver and J. Sivaloganathan, *The structure of null Lagrangians*,
Nonlinearity **1** (1988), 389–398,
[author-hosted published paper](https://www-users.cse.umn.edu/~olver/e_/null.pdf).
The author's publications index calls it *The classification of null
Lagrangians*; the PDF title above is used here. Read pp389–392,
Theorems7–8 and their proofs pp394–395, including the remark following
Theorem8. The standing assumptions are bounded open Omega in R^m,
closure contained in an open V, and C1 L on V x R^n x R^(mn).
Theorem7 requires star-shaped Omega and characterizes null Lagrangians
as total divergences of suitable C1 potentials. Theorem8 represents
them by finite sums of homogeneous null Lagrangians applied to
derivatives of potentials. For non-star-shaped domains the stated
representation is local on star-shaped subdomains. The proof uses
the Poincare lemma. The introductory field-theory discussion p390
requires a comparison functional bounded by the functional being
minimized, with equality at the proposed minimizer; invariance alone
is not that inequality.

For this notebook, angular coordinate charts may be used locally.
There is no source warrant to assert a globally periodic potential
on T2 or cancel boundary flux of a potential that is not periodic.
L847 already proves its own full-form integral invariance without
such a potential. A lower bound for the variable complex coefficient
is an additional obligation, not supplied by the source's abstract
field-theory framework. No potential or comparison inequality is
constructed here. This is a hypothesis comparison, not an application
of Theorem7 to the full torus.

### Finite regularity and signed integration

Jiří Lebl, *Tasty Bits of Several Complex Variables*, version4.4,
31 May 2026, [TheoremB.2 p206](https://www.jirka.org/scv/scv.pdf#page=206)
and [TheoremC.6 p224](https://www.jirka.org/scv/scv.pdf#page=224).
Reinspected both statements. B.2 covers bounded planar domains with
positively oriented piecewise-C1 boundary and continuous coefficients
with bounded continuous first partials. C.6 states Stokes for smooth
forms on compact smooth oriented manifolds with boundary, with a
following less-regularity remark. Do not turn that remark into a
precise unstated C1 theorem; B.2 suffices for a fundamental rectangle
with C1 coefficients. Here C2 u supplies the needed regularity for
coefficients built from u and first derivatives. Check paired sides
and their orientations if using that rectangle. Reuse L847 for the
already established full-form homology equality.

### Overlap, searches and unread leads

Read L847's hypotheses, complete pullback (3)–(4), and full
homotopy/Stokes argument; L861's hypotheses, restricted conclusion
and source inventory; and the four exact ATTEMPTS records named in
the nomination. Also read
`ATTEMPTS/2026-11-06-positive-total-flux-annular-gluing-stop.md` and
`ATTEMPTS/2026-11-06-nongraph-fixed-chart-annular-stop.md`, together
with the setup and source summary of
`2026-11-06-positive-annular-gluing-boundary-moment.md`.
No further contact-germ proof or sibling notebook was needed.

L847's invariance is already known locally; relabeling it a new moment
obstruction would be duplication. L861's conditional contacts do not
supply a bound on F away from their neighborhoods. L856–L857 use
boundary-forced nonconstant observables on specified small collars
in one chart. The current target prescribes no such collar or image
range; their obstruction cannot be imported into the whole torus.
The stopped full-phase mechanism concerns winding, not an integral
estimate; it supplies no missing inequality. These comparisons do
not assert that all derivative-moment approaches are impossible.

Queries actually submitted included:

- `null Lagrangians periodic gradient determinant integral minors Ball Currie Olver 1981`
- `holomorphic volume form totally real torus positive real pullback prescribed phase integral obstruction`
- `"positive" "holomorphic volume form" "totally real" integral Pacini`
- `"Jacobian" "periodic" "null Lagrangian" positive determinant gradient`
- `"Riemann xi" "radial" "contour" positivity`
- `"holomorphic" "null Lagrangian" "positive"`
- `"trace" "determinant" "periodic" "null Lagrangian"`

The initial Ball lecture slides were opened and searched but did not
serve as theorem evidence; the published paper supplied that evidence.
Search results on real conductivity Jacobians, special Lagrangians,
and modern constant-rank null Lagrangians were leads only, not imported
theorems. A result titled *Contour Hankel dynamics and indicator fields
for the Riemann Xi-function* (arXiv:2608.11520v1) appeared in a secondary
index; its primary text was not inspected and it is not coverage for
this graph problem. No conclusion about any such paper is relied on.
No inspected source settles the exact full-density/four-cycle target;
this bounded search does not certify novelty. Full matching Mathlib
coverage is not checked; supporting calculus is not a matching theorem.

### Gate and continuation

SPECIALIZE covers exactly TARGET with its existing SCOPE. The next
mathematical step may cite the periodic-minor theorem, specialize only
the two nominated moments, and compare with the unchanged full L847
system (4). It must keep actual F(Phi_u), exchange symmetry, all
F-divisor zeros and all permitted J zeros. A formal collection of
matrix values or moment measures is not an actual derivative field
or a torus. A separate ready-assessment approval may be imposed by
the supervisor; this turn performs no dependent mathematics.

Continue only for an explicitly justified additional sign/range
condition useful for restricting global completion. Stop this test if
the result is only periodic bookkeeping or L847's existing homology
identity, restates q>=0, or needs an unproved image bound or division
at zeros. A stop would apply to this two-moment mechanism alone.
The four actual zero data, global completion/avoidance, other degrees
and actual-Xi mixed positivity remain unresolved independently.

Recommend one calculation with standard/high settings, classed
REPRODUCTION when invoked under SPECIALIZE; no script is required.
Creative priority was considered. The present sources supply standard
identities and no new coercive relation between actual F and Du;
that missing mechanism blocks an honest central creative nomination.
Do not replace this bounded test by another unchanged contact audit
or by unassessed higher moments. Literature-only work spends no
mathematical exploration turn and supplies no budget-reset claim.
