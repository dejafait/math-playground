# Adjacent triangle and upper-pair matching — nomination1056 / review1057

TARGET: Test whether C467r's lambda=1 trace can be matched by bounded adjoints on C467k's adjacent j=1 triangle and its actual upper-pair face, with the original bump data, four complex L1 products per piece and complete cutoff identities.
CHECKED: 2026-11-16
DECISION: EXPLORE
SEARCH_EVIDENCE: Review1057 searched prescribed inflow/outflow compatibility and network/interface transport; compared reviews1042/1046/1050/1054, canonical C467k/l/m/p/r and stops1043/1051 with their audits. No inspected theorem settles the exact added trace problem; this bounded search makes no novelty claim. Queries and inspected ranges below.
SOURCE_EVIDENCE: Reuse the recorded primary ODE, transport and normal-trace comparisons in reviews1042/1046/1050/1052/1054. Narrow primary rereads: Iyer's 2026 Method of Characteristics, Proposition7/Remark8/Lemma9/Theorem10 proof/Remark11; Roggensack arXiv HTML labelled1506.07966v1, section2 assumptions, Theorem14 and full proof, section6 coupling setup. Exact URLs and scope qualifications below.
COMPARISON: C467l/m already cover both signs of h for geometry, coefficient bounds and fixed smooth tests, with the forced slot orientations; this is usable coverage without a reflection argument. C467p's constructed adjoint remains positive-h only, and C467r leaves angular sides free. Known transport and trace results do not establish the additional prescribed radial value, an upper-pair adjoint and their joint matching in the requested class.
GAP: Construct the unchanged nominated pair and triangle adjoints with both prescribed matches, all eight separate complex L1 products and both complete independent-cutoff identities, or exclude precisely that class. Actual characteristic compatibility and upper-pair unknown-test estimates remain mathematical obligations; no essential source is blocked.
REASON: Separate literature-only review1057 completes the changed-scope comparison for the original TARGET. EXPLORE approves one bounded mathematical attempt without deriving a matching result, an upper-pair specialization or a symmetry reduction in this approval turn.
LITERATURE_REASON: The target adds the h<0 upper-pair piece and a prescribed shared radial-face value outside the unchanged positive-h/j=0 assessments. Reuse their adequate sources and compare only these essential new hypotheses before dependent mathematical work.
SCOPE: Actual n=3, original B/beta/H/H0/F, raw time, fixed bump, common minus sign, R=1/4, a=1/16, T0=1/1920, b=1/4096, X=1/256 and H_*=1/128; one upper-pair face and its adjacent j=1 triangle with C467r fixed on the shared side.

## Proposed test; no new mathematical result

Use exactly C467k's j=1 map and orientation. Its lambda=0 radial
face is the same physical map as C467r's j=0, lambda=1 face.
Seek one common positive time, no larger than C467r's interval,
and a real bounded test psi_1 with 0<=psi_1<=1, continuous on its
closed parameter box, smooth at positive t and 0<r<1, with fixed
x/lambda endpoint neighborhood extensions, satisfying

    psi_1(0,x,r,lambda)=f(x)^3,
    psi_1(t,x,r,0)=psi_r(t,x,r,1).

The value at r=0 may depend continuously on lambda, as in C467r;
no single physical-vertex value is imposed. The prescribed side value
is the actual selected function of C467r, not an adjustable solution
of a different construction.

For the incident upper pair, use initial (x,x,x+h), -H_*<=h<=0,
with the actual upper two ranks paired and the lower rank singleton.
Use the slot order sigma=(1,3,2), h<0, specified for j=1 by
C467k's orientation table. Let phi_- denote the sought test in that
pair's (t,x,s,h) coordinates. Require 0<=phi_-<=1, continuity on
the closed box, positive-time negative-h smoothness with the original
endpoint neighborhood extensions, and

    phi_-(0,x,s,h)=f(x)^2 f(x+h),
    psi_1(t,x,1,lambda)=phi_-(t,x,1-2lambda,0).

The upper-pair test is an unknown in this proposed test. No assertion
that it is obtained by reflecting C467p, or that the actual beta is
invariant under such a reflection, is permitted without justification.
Retain the actual map and conjugation-normalized background.

On each piece impose d(test) wedge Re(-pullback Omega)=0 in the
interior with the original divisor. Require absolute integrability
of each of the four original complex coefficient times coordinate
derivative products on that piece's whole box. Require its complete
complex Stokes identity in the limit of arbitrary independent positive
time/radial or time/separation cutoffs, with every original face
retained and no added corner distribution. In particular retain the
pair's full h=0 trace, the triangle's full r=1 trace and the common
radial-face terms. Require zero original inner radial flux for psi_1.
The equal test values on shared faces are the proposed compatibility;
the already known opposite orientations alone do not establish it.
Do not impose zero exterior flux or favorable signs on other faces.

The decisive positive result would be functions satisfying this entire
local matching problem on one common interval. A decisive negative
result would exclude this precise class. Failure of a particular
backward construction or a sufficient bound would be inconclusive.
This nomination does not attempt either result.

## Relevance, input qualifications and separate gate

The main gap remains L030–L032/C032a actual-Xi all-degree algebraic-square
positivity. C467r supplies one local matched outer edge but leaves its
angular side terms unpaid. The proposed test addresses one neighboring
interface. Even success would leave the remaining triangles, chamber
matches, exterior payment, global signed assembly, realization and other
degrees open. It would not be an RH candidate.

Carry C467r/audit1056, C467p/o/audit1049, C467k/audit1033,
C467e/audit1017 and C467q/audit1053's graph formulas; retain
C467l/m audits1037/1041 through the positive-pair construction.
C467l/m's applicability to an upper pair is not assumed. Preserve
stops1000/1009/1023/1043 and the single-physical-vertex stop1051.
The L018/C466a external first-zero qualification remains unreplayed;
no density realization or RH is assumed. Full matching Mathlib coverage
is unchecked.

At nomination1056 the next turn was a separate literature comparison for exactly TARGET.
Compare transport with adjacent boundary traces, the actual upper-pair
hypotheses and existing matching/normal-trace results, reusing already
read primary statements and retrieving only essential missing cases.
Choose IMPORT, SPECIALIZE or EXPLORE only after that comparison, or
record an actual source blocker. Do not derive the new matching theorem
in its own approval turn. Future proof routing depends on the comparison;
no creative or development attempt was preapproved by the nomination alone.

## Separate source comparison1057 — 16 November 2026

This is one LITERATURE step, with the proposed test above unchanged.
The source gate is now EXPLORE. No adjoint is constructed, no necessary
compatibility equation is derived, and no original-form cutoff limit
or upper-pair reflection is proved in this source review.

### Local overlap, applicability and recorded failures

Read C467k's hypotheses/conclusion, complete orientation table, (17)–(20)
and audit1033's six-edge/radial-face check. Read C467p's hypotheses and
conclusion, (33)–(36) and their boundary-continuity argument; read
C467r's hypotheses/conclusion, selected-edge section (10)–(12), backward
hit section (13)–(15) and audit1056's common-domain/hit-variation cases.
These readings compare the actual selected functions, not merely their
initial data. C467r explicitly allows a characteristic to cross an
angular side in its auxiliary domain: that side was free there. Its
construction is therefore not already a matching theorem for the fixed
side in this nomination. No conclusion about compatibility follows
from that freedom alone.

Read C467l/m's hypotheses/conclusions and their negative-h proof cases:
C467l audit1037's ordered singleton and both-sign secant/orientation
arguments; C467m audit1041's both-sign gap limit and six full oriented
edges, together with (18)–(19)'s complete tested limit. They already
include the upper pair, without assuming beta is reflection invariant.
Their unknown-test scope remains important: C467m's full limit is for
fixed smooth tests with bounded first derivatives. The new adjoints
have only the nominated weighted integrability, so those statements
cannot simply be applied to them on the closed corner. The canonical
geometry and coefficient bounds may be reused within their proved
hypotheses; their reproduction is unnecessary. C467p's actual
characteristic construction is explicitly positive-h and supplies no
upper-pair adjoint by citation.

Scoped searches were confined to November16 reverse assessments and
attempts, the named canonical results and their relevant histories.
The selected nearby records are review1042's smooth matched-chain
comparison, reviews1046/1050/1054's weakened pair/triangle comparisons,
and audit1056. No existing solution of this exact adjacent-side
problem was identified. This is a duplicate check, not a novelty claim.
The stop1043 record/audit1045 excludes joint smooth time-zero pair
jets; stop1051/audit1053 excludes a lambda-independent physical-vertex
value. Neither hypothesis is imposed here. Reuse review1042's scoped
comparison of stops1000/1009/1023: their forward-payment, forward-cap
and unaugmented reverse-current obstructions retain those scopes.
A historical stop does not exclude the current retained-piece,
angular-parameter class. No stopped route is silently reopened.

### Primary theorem comparison and sources reused

Fresh search queries were `transport equation prescribed inflow outflow
boundary data compatibility characteristics continuous solutions
interface` and `transport equations networks continuity transmission
trace boundary compatibility multidimensional characteristic`.
The exact local target was also compared against the already recorded
sources below. Search snippets on numerical/advection-diffusion
boundary conditions and an Euler-system paper were uninspected leads,
not theorem evidence. No larger passage from those leads was needed.

**Iyer, local classical characteristics.** Gautam Iyer, *Method of
Characteristics*, 2026 course notes,
[Proposition7, Remark8, Lemma9, Theorem10/proof and Remark11](https://www.math.cmu.edu/~gautam/c/2026-632/notes/moc.html).
Reread the smooth-equation setup, admissible boundary jet and nonzero
normal characteristic derivative, the inverse characteristic chart,
and the proof's zero tangential-jet error and gradient identification.
The conclusion is local classical solvability; Remark11 separately
requires compatible data at multiple boundary hits. This does not
verify a common chart through the present degenerations or establish
compatibility of the selected trace. No source-stated incompatibility
is specialized to the weaker nominated boundary regularity.

**Roggensack, coupled transport.** Arne Roggensack, *Well-posedness of
space and time dependent transport equations on a network*,
[arXiv HTML labelled1506.07966v1, section2, Theorem14/full proof, section6 setup](https://arxiv.org/html/1506.07966v1).
Reread (2): u in L1_t W1,1_x, c in L1, (u_x+c)^- and (u_x)^+
in L1_t Linfinity_x; bounded nonnegative initial data and nonnegative
source in L1_t Linfinity_x. The affine inflow operator requires
positivity, causality, weak-star continuity, weighted L1 contraction
and invariant bound (5). Theorem14 gives bounded weak solutions.
Its proof uses monotone outflow-to-inflow iteration, the invariant
bound, convergence and the weak-limit boundary equation. Section6
specifies a mixing operator and conservation hypotheses. No such
normalized velocity or transmission operator has been verified here;
the conclusion also does not supply the required pointwise continuity,
interior smoothness and four separate complex products. The HTML's
v1 label says26June2015 while its displayed manuscript date is
24August2026; this assessment identifies the inspected rendering,
without asserting an independently checked publisher version.

Reuse review1042's already-inspected Ambrosio–Crippa flow/superposition,
Egger–Philippi classical network and Camilli–DeMaio–Tosin measure-network
comparisons. Reuse review1046's Boyer trace/renormalized-solution,
Arlotti–Banasiak–Lods regular invariant-flow and Chen–Comi–Torres
product/normal-trace comparisons; reviews1050/1054 supply the recorded
Imagawa–Kawagoe, Calvo–Hingant–Yvinec and BV/normal-Lebesgue-trace
comparisons. Their exact versions, theorem numbers, proof cases and
URLs remain in those assessments. None may be invoked here without
its recorded velocity, inflow, Sobolev/BV, invariant-measure or
trace-approximation assumptions. Directional or flux-weighted weak
traces do not provide the full nominated test class by citation.

Ordinary smooth ODE dependence on verified open charts, Stokes on
smooth cutoff boxes and dominated convergence remain supporting known
tools, with precise references already in C467r's source-import
paragraph and reviews1052/1054. They do not construct compatible
unknown boundary data or justify arbitrary independent cutoffs before
the actual estimates are supplied. No standard theorem is reproved.
Full matching Mathlib coverage was not checked; supporting coverage
must not be reported as the full theorem's presence or absence.
The essential primary comparison is accessible; no source blocker
requires another literature turn.

### Gate, bounded test and continuation decision

Decision EXPLORE for exactly TARGET, retaining every condition above.
The strongest inspected results give conditional local classical or
coupled weak solvability and conditional trace identities; none settles
this actual-data matching problem. The remaining difference is
mathematical, so further generic browsing is not the default.

One later proof attempt may test whether the selected radial value
and an actual negative-h pair can be transported consistently through
the adjacent triangle. Verify the upper-pair charts and forced slot
orientation directly; no invariance of the actual beta under reflection
or equality of differently selected characteristic solutions is granted.
Retain the original divisor, undivided real equation, raw time, fixed
bump, and common minus normalization. Any local chart or division must
be justified on its actual domain. Save partial reasoning before
lengthy development.

Positive evidence is a pair of functions meeting the entire stated
class on one common time, including both exact face equalities, each
piece's four complex L1 products, all independent-cutoff faces and zero
inner radial flux. Negative evidence must exclude that class. A failed
reflection, auxiliary extension, sufficient estimate or selected
characteristic ansatz alone is inconclusive. Preserve the residual and
require a refined mechanism or materially new input before repeating
an unsuccessful attempt. No two-prescribed-face compatibility test is
performed in this literature turn.

Use the continuation inputs and unresolved assumptions recorded above,
with C467l/m now explicitly available for their both-sign geometry and
fixed-smooth-test conclusions only. A successful match supplies one
neighboring component for signed assembly; remaining triangles,
chambers, exterior payment, realization, all degrees and Xi transfer
still separate it from L030–L032/C032a. No RH candidate is claimed.
Next routing is proof_attempt/development, deep_research/xhigh:
difficult compatibility development along the established characteristic
route, with the selected C467r trace fixed rather than redesigned.
