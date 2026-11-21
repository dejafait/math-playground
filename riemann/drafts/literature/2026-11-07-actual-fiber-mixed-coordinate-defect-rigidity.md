# Actual-fiber mixed-coordinate defect rigidity — source assessment

TARGET: Test whether mixed-coordinate distributional compatibility forces h=0 near a simple actual-G fiber for every locally Lipschitz one-sided form satisfying L893's domination and full graph saturation, or give a counterexample to that local vanishing claim under the same actual-G hypotheses.
CHECKED: 2026-11-07
DECISION: EXPLORE
SEARCH_EVIDENCE: Step85 bounded searches for the exact coupled weak system, nonnegative-defect rigidity, elliptic unique continuation, differential-form continuation, degenerate maximum principles and holomorphic calibrations found no adequate theorem or actual-G counterexample; queries and inspected sources below, with no novelty inference.
SOURCE_EVIDENCE: Aronszajn (1957), pp235–236,245–248; Bony (1969), doi:10.5802/aif.319, Section1 pp278–279, Proposition3.1/Theorem3.1/Corollary3.1 and Remark3.2 pp285–287, Theorem4.1/Corollary4.1 pp288–289; Gerner arXiv:2207.02029v1, Section2 Theorems2.1–2.2 pp3–4 and Section3 proof pp5–7; reuse step82 weak-Stokes/calibration coverage only within its unchanged scope.
COMPARISON: Inspected scalar and differential-form continuation theorems require differential inequalities and stronger vanishing data not supplied by L893; Bony requires a suitable scalar operator and propagation hypotheses. They decide neither actual-G defect rigidity nor its failure. L868 and the frozen L894 example retain their restricted scopes.
GAP: Establish or refute local h=0 for all L893 coefficients under the exact varying actual-G bound and full graph traces; no scalar elliptic reduction, codifferential estimate, infinite-order vanishing or actual counterexample is established by this review.
REASON: Separate step85 source review fills the nominated comparison gap and approves one bounded mathematical attempt on the unchanged TARGET. This is source assessment only; no new lemma, compatibility identity, vanishing claim or counterexample is derived or approved.
LITERATURE_REASON: At invocation start the new full-class mixed-coordinate rigidity target lacked essential PDE coverage; this review supplies it using primary theorem hypotheses and relevant proof cases rather than repeating weak-Stokes browsing.
SCOPE: Exactly L847 actual G,R,C,F,omega; L879 smooth real stationary graph with original J!=0; an interior segment of the conditional clean simple G(z1)-zero fiber with G(z2) and z1-z2 nonzero; all L893 locally Lipschitz coefficient constraints, both weak closure directions, continuous representatives and complete local graph saturation. Includes distributional compatibility and an exact local counterexample test; excludes frozen substitutions and ansatz-only stops.

## Original nomination — step84, retained as history

At nomination, the exact target above was proposed for separate source review. No
mixed-derivative condition, unique-continuation theorem, vanishing
claim or counterexample is derived or approved in this file.

The main gap is L030–L032/C032a actual-Xi all-degree mixed positivity.
If actual-G dependence forced the defect to vanish, the remaining
holomorphic coefficient problem could obstruct the local certificate
through its opposite graph phases. That downstream implication must
be justified in a later approved attempt; it is not a theorem imported
here. A counterexample under the exact local actual-G conditions would
retire the proposed vanishing mechanism. A frozen substitute does not
settle either alternative.

Retain L847's full F and logarithmic coframe, L879's smooth real
stationary graph with J!=0, and an interior segment of the nominated
clean simple G(z1)-zero fiber, with G(z2) and z1-z2 nonzero. L893's
locally Lipschitz q,r,h, continuous representatives, nonnegative h,
exact bound |q-ir|<=|F|, both weak closure directions, and complete
local graph saturation must all remain. L893 and L894 have not had
independent audits. The local question does not assume minimization,
dual attainment, a smooth coefficient, a derivative bound, or an
actual realization of the conditional graph configuration.

The bounded test, if separately approved, is compatibility in an open
neighborhood using both coordinate directions and the varying actual
holomorphic factor. It must not evaluate ambient a.e. identities on
the graph or replace F by a frozen coefficient. Decide by a proof of
the local vanishing claim with all hypotheses, or a counterexample
meeting them; an ansatz-specific failure alone is insufficient.
The L894 multiplication ansatz is retired and cannot be relabeled
as this new test. L887–L892 and attempt65/69 remain at their stated
scopes. Graph existence, full-strip assembly, unrestricted competitors,
global sharp bounds, higher signs and Xi transfer remain open.

This was a proposed new compatibility mechanism at the dual-certificate
gap, not a routine respecialization of weak Stokes. Essential coverage
must be prepared before a creative proof attempt can be scheduled.
The calibration route has used 2/3 mathematical exploration attempts;
this nomination does not reset that budget. Mathlib coverage is unchecked.

## Separate source review — 7 November 2026, step85

### Exact statement under comparison

Retain the full density of L847, without discarding the squared
diagonal or freezing the second variable:

\[
F=-C G(z_1)G(z_2)(z_1-z_2)^2/(z_1^2z_2^2),\qquad
C=R^2/G(R)^2>0.
\]

The graph and simple fiber are conditional configurations of L879
and L893, not constructed here. In logarithmic coordinates w_j=x_j+i y_j,
the objects being tested are L893's real locally Lipschitz q,r,h on
an open ambient neighborhood, with continuous representatives and

\[
h\geq0,\quad |q-ir|\leq|F|,\qquad
r_{x_j}=q_{y_j},\quad(q+h)_{x_j}=-r_{y_j}\quad(j=1,2)
\]

in distributions, and the complete local graph traces

\[
h\circ\Phi_u=0,\qquad
(q-ir)\circ\Phi_u=-|F\circ\Phi_u|\overline J/|J|.
\]

These are quotations of the saved local problem, not newly derived
compatibility conditions. All matrices, including J=0, and F=0 remain
in its one-sided domination condition. There is no assumed scalar
PDE for h, ellipticity, harmonicity, differentiability on the graph,
dual attainment or minimizer. L893/L894 remain unaudited inputs;
any later proof using their reductions must verify the needed parts.

### Primary theorem comparisons

Nachman Aronszajn, *A unique continuation theorem for solutions of
elliptic partial differential equations or inequalities of second
order*, J. Math. Pures Appl. (9) **36** (1957), 235–249,
[Section1 pp235–236, Section5 pp245–247, Remark3 p248](https://sites.math.washington.edu/~blwilson/Nodal/Aronszajn.pdf).
Read the statement, local strong-second-derivative assumption,
C^{2,1} positive-definite principal part, bounded lower coefficients,
infinite-order 1-mean vanishing hypothesis, cutoff/convolution passage
and common-principal-operator systems remark. The scan's OCR loses
superscripts; no singular-coefficient refinement or ambiguous formula
is imported. The theorem gives identically zero from those hypotheses.
Its systems extension retains one common elliptic principal operator.
The target supplies neither such an inequality for h or the triple,
nor infinite-order vanishing. A graph trace is not the source's
vanishing hypothesis. Thus this theorem cannot presently be applied;
this comparison does not prove that an appropriate reduction is
impossible. No Carleman estimate is reproved here.

Jean-Michel Bony, *Principe du maximum, inégalité de Harnack et unicité
du problème de Cauchy pour les opérateurs elliptiques dégénérés*,
Ann. Inst. Fourier **19**(1) (1969), 277–304,
[Section1 pp278–279; Proposition3.1, Theorem3.1, Corollary3.1,
Remark3.2 pp285–287; Theorem4.1/Corollary4.1 pp288–289](https://www.numdam.org/article/AIF_1969__19_1_277_0.pdf).
Read the operator assumptions, barrier proof of Proposition3.1,
Theorem2.2 propagation argument and the named statements/proof cases.
The operator is L=sum X_k^2+Y+a with smooth real fields and a<=0.
For C2 u with Lu>=0, a positive attained maximum propagates along
the Lie algebra generated by the X_k; full rank everywhere gives
constancy on the connected component. Remark3.2 supplies a qualified
rank-deficient failure. Section4's distributional support propagation
additionally uses analytic coefficients and one-sided open vanishing.
Neither a scalar inequality for h, the required regularity, nor
appropriate fields/rank or open-side vanishing are supplied here.
The rank-deficient example is not an actual-G counterexample.
Nonnegativity alone licenses no application of these results.

Wadim Gerner, *A unique continuation theorem for exterior differential
forms on Riemannian manifolds with boundary*,
[arXiv:2207.02029v1, 5 July 2022, Theorems2.1–2.2 pp3–4,
Section3 proof pp5–7](https://arxiv.org/pdf/2207.02029v1).
Theorem2.1 explicitly restates AKS: on an oriented connected C^{1,1}
manifold without boundary with C^{0,1} Riemannian metric, an H1_loc
k-form satisfying |d alpha|^2+|delta alpha|^2<=C_K|alpha|^2 a.e.
on every compact K, and having an infinite-order 1-mean zero, vanishes.
Gerner's Theorem2.2 adds boundary points with C^{2,1} manifold,
C^{1,1} metric and vanishing full tangential or normal trace.
Read both trace cases via Hodge star and the even/odd reflection,
matching H1 traces, reflected metric and differential inequalities
in (3.1)–(3.4). L893 gives closedness but no codifferential estimate
or infinite-order zero. Its graph is a real two-dimensional set in
the four-dimensional ambient space, not the boundary hypersurface
in this theorem. Reflection cannot be presumed to repair those gaps.
No theorem from this paper is specialized into a new local result.

The original AKS paper, *Ark. Mat.* **4** (1962), 417–453,
[doi:10.1007/BF02591624](https://doi.org/10.1007/BF02591624),
was read only through its introduction pp417–418 at the Tsinghua
mirror: both d and delta control and infinite-order vanishing are
explicit there. Later detailed-page retrievals timed out; the publisher
offered metadata only. Full original proof coverage is not claimed.
Gerner's inspected precise restatement and primary boundary theorem
suffice for this nonapplication comparison; no hidden AKS proof case
is used as a mathematical input. The 2026 published Gerner version
was a bibliographic lead; the version actually inspected is v1.

### Local overlap, reused coverage and bounded search

Read L893's weak system and trace argument; L847/L879 hypotheses and
conclusions; L868's pointwise/closure and radial-independent comparison;
L894's diagnostic and actual-factor obstruction, with its conclusion
and lift argument. Read step84's history and attempt65/69 records.
L868's global C1 h-radially-independent stop does not establish
independence on the new neighborhood. L894's frozen feasible form
does not refute actual-G rigidity; failure of its constant-phase lift
does not establish it. Attempt65/69 concern unsigned kernels and
unpaid chord compensation, not this full-system local test.

Reuse `2026-11-07-weak-local-paired-strip-calibration.md` for exactly
its inspected Kangasniemi–Prywes weak-Stokes theorem and
Lawrence–Yamauchi, Harvey–Lawson, Helein, Lotay–Pacini comparisons.
Their prior scopes and qualifications remain; none supplies a
certificate or h-vanishing theorem. No repeat integration search was
needed and no cross-notebook input was read.

The bounded searches used these queries and theorem-title refinements:

- `overdetermined Cauchy Riemann system nonnegative defect unique continuation differential forms Lipschitz calibration`
- `unique continuation degenerate elliptic system Lipschitz counterexample Cauchy data codimension two`
- `"r_{x_j}" "q" "h" calibration`
- `"nonnegative" "defect" "calibration" "rigidity" holomorphic`
- `"mixed" "Cauchy-Riemann" "nonnegative" rigidity defect`
- `"closed differential forms" "unique continuation" "codifferential"`
- `Bony 1969 principe maximum propagation support operateurs elliptiques degeneres pdf theorem`
- `Aronszajn 1957 unique continuation theorem solutions elliptic partial differential equations inequalities pdf numdam`
- `"A unique continuation theorem for exterior differential forms" pdf`
- `"calibration" "holomorphic" "Lipschitz" "zeros"`

Search-only leads on pluriharmonic functions, nonsmooth scalar
elliptic continuation, CR embeddings and Smith immersions are not
theorem coverage or imported counterexamples. No adequate match for
the exact actual-G constraints was found. This neither establishes
novelty nor predicts the answer. Bony's item URLs failed, but the
article URL above supplied the primary text; the initial retrieval
failure is resolved. Shell downloads failed DNS and supplied no
evidence. No essential theorem is left blocked for this bounded test.
Mathlib coverage of the target and comparison theorems was not checked;
no absence claim or formalization gate is asserted.

### Gate decision and discriminating test

EXPLORE approves one later mathematical attempt on the unchanged
TARGET, not its answer. The proposed new mechanism must use both
coordinate directions on an open neighborhood and retain the varying
actual density. Check all necessary distributional operations and
input reductions there; never restrict ambient a.e. derivative
equations to the graph or assume h differentiable on its zero set.
The comparison sources do not approve a new scalar PDE, maximum
principle, unique continuation conclusion or division through F=0.

Decisive evidence is a proof of local h=0 for every coefficient triple
in the nominated class, or one fully specified actual-G counterexample
satisfying all local domination, closure and graph-trace hypotheses
and having nonzero h arbitrarily near the nominated fiber point.
A frozen model, isolated jet, ansatz failure, smooth-only argument
or satisfaction on just one side is insufficient. A conditional
counterexample must retain the original stationary-graph hypotheses;
existence of that configuration is still unresolved, not assumed away.

The plausible downstream use is to decide whether this defect can
support a weak local saturating certificate, before a separate
coefficient-phase obstruction or paired-strip construction. Even
successful rigidity alone would establish neither finite descent nor
the sharp global period bound, higher signs or Xi transfer. Failure
to prove rigidity does not itself produce a certificate.

The route remains at 2/3 mathematical EXPLORATION attempts. This
literature step spends and resets none of that budget. The next test
is its last inconclusive allowance before mandatory reassessment;
another change of name is not renewal. Corner-only and constant-phase
multiplicative routes remain retired. This source approval prepares
a creative test of a different full-system mechanism and does not
derive previously uncovered mathematics during its approval turn.
