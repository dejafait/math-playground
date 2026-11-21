# Three-particle collision volume — nomination974 and source review975

TARGET: Assess source coverage for a class-uniform stopped weighted three-volume bound for the three-particle Vandermonde raw flow, allowing simultaneous collisions and arbitrarily small initial separations.
CHECKED: 2026-11-14
DECISION: EXPLORE
SEARCH_EVIDENCE: Review975 reused local reviews948/958 and C466s, searched exact Vandermonde/weighted-volume/holomorphic-gradient-Jacobian phrases and Calogero/Dyson alternatives, and inspected the statements and proof cases below. No matching class-uniform three-particle theorem or admissible counterexample was located in this bounded review; this establishes neither novelty nor absence from the literature.
SOURCE_EVIDENCE: TNV arXiv1706.03822v2 AppendixB(B.1)-(B.5), p22, and Sections2.2/3.1-3.2; WKM arXiv2008.10321v2 Sections2.2/2.4-2.5, (17), Section3.1 Theorem4/Proposition5/full proofs, pp4-9; Hall-Ho, Lett.Math.Phys.115:60(2025), Proposition3.1/Remark3.2/full proof (3.1)-(3.7); Voit-Woerner arXiv1910.07888v1 (2.1), Lemma2.1, Theorem2.8/full proof, pp3/6-7. Direct links and source-access qualifications are below.
COMPARISON: The arbitrary-k real compound estimate covers three-volume on compact survivor intervals but supplies no uniform singular cancellation. Heat-root evolution is holomorphic rather than conjugated and lacks general coupled H. The repulsive real Weyl-chamber boundary theorem does not cover this complex stopped class. C466s remains a one-divisor comparison.
GAP: The precise inequality below remains unproved and unrefuted: control collective tangent three-volume with the Vandermonde weight uniformly near intersecting divisors for bounded coupled H, or prove an admissible fixed-data counterfamily. No source supplies that estimate, a sign or Xi transfer.
REASON: Essential flow and arbitrary-degree volume tools are accessible; new many-particle leads have precise scope mismatches rather than essential access blockers. Prepare the bounded mathematical test in continuation975 without deriving or approving its estimate in this literature-only turn.
LITERATURE_REASON: The invocation-start assessment was REVIEW_REQUIRED: intersecting divisors, three-volume and many-particle applicability were outside ready single-divisor coverage. This review fills that missing comparison rather than repeating ready-target browsing.
SCOPE: Only the finite-time three-particle weighted spatial determinant specified below, with standard Hermitian norms and unit flat raw physical time; no phase theorem, current identity, endpoint trace, changed metric, or actual-Xi specialization is included.

The nomination below is retained verbatim as the original proposal. Its
unread-lead and next-task statements describe nomination974; the completed
source verdict and continuation are in review975 at the end.

## Exact proposed mathematical test, not an established inequality

Fix real 0<a<R<infinity, T_0>0, finite nonnegative M_1,M_2 and
H_0 in C. On B={z in C^3: |z_j|<R for j=1,2,3}, let H be
holomorphic, H(0)=H_0, ||grad H||_2<=M_1 and
||D^2 H||_op<=M_2 throughout B. Set

\[
 \Delta(z)=\prod_{1\le i<j\le3}(z_j-z_i),\quad
 U=B\setminus\{\Delta=0\},\quad
 S=-2\log\Delta+H,\quad F=\Delta^2e^{-H}.
\]

Only derivatives of a local logarithm enter the raw flow
dot X=conjugate(grad S(X)). Start at X(0,u)=iu for real
u in (-a,a)^3 with pairwise distinct coordinates. Let [0,tau(u))
be the first maximal lifetime in U and J_t=D_uX(t,u) the complete
complex 3-by-3 Jacobian at fixed physical time, initially i Id.
Use the signed density

\[
 W_t(u)=(-1)^3 F(X(t,u))\det_{\mathbb C}J_t/i^3
 \quad(t<\tau(u)),
\]

and define W_t=0 at stopped points and at initial collisions.
The sign convention is that of the three-variable squared
Vandermonde form in C466k; the proposed estimate is for its modulus.

The question is whether there is a finite
C=C(R,a,M_1,M_2,T_0,Re H_0), common to the whole stated class, with

\[
 |W_t(u)|\le C\,|\Delta(u)|^2
 \quad(0\le t\le T_0,\ t<\tau(u)).
\]

C must not depend on initial pair spacings, relative collision rates,
the surviving distance to a divisor, or the particular H beyond the
fixed data. Do not add a separation cutoff or assume a smooth first-hit
surface. The definition stops at the first event, including outer
exit; it does not restart trajectories. A fixed-compact-survivor
estimate alone does not meet the requested uniformity. No quantitative
formula for C, validity of this inequality, or counterexample is
derived or approved in this nomination.

## Relevance, comparison and bounded decision test

The main gap remains L030-L032/C032a actual-Xi all-degree
algebraic-square positivity. Three particles are the first case with
intersecting pair-collision divisors. A uniform weighted determinant
bound would be an input for later multi-collision integration and
cutoff work; an admissible failure would stop this envelope before
extending the current construction. Neither outcome supplies a sign,
a complete-form current estimate, actual-H bounds, global homology,
all orders, or transfer to Xi. The constant-background case alone
would not settle the quantified bounded-H class.

Three continuations were compared without attempting new mathematics:

1. More coefficients in the affine/mixed sign search: stops971/972
   record exclusions of those families, and audit974 makes the mixed
   stop reliable; the affine proof remains unaudited. A general-H
   extension would reuse the same single-divisor
   mechanism and still leave collisions between several particles open.
2. Restart the buffered current through arbitrary time: C466t/stop961
   exhibits an earlier-outer-grazing defect; changed initial surfaces
   and cutoff terms would need new control. C466u and stop968 do not
   provide global signed invariance. No new repair mechanism is proposed.
3. Test collective weighted three-volume at intersecting collisions:
   select this separate mass question. It asks for a quantitative
   uniform bound or a counterexample, without assuming pointwise sign
   or the discarded global current identity.

Reuse the accessible variational/compound sources rather than repeat
their discovery. The essential new search is for exact or stronger
Vandermonde/logarithmic-force weighted-volume estimates, including
complex coupled perturbations, attractive versus repulsive Dyson or
Calogero dynamics, simultaneous collisions and finite first lifetimes.
These names are unread leads, not theorem inputs. Inspect the primary
hypotheses and relevant proof cases before claiming applicability.
Also compare any general k-compound statement with the full real
three-volume and complex determinant, including its norm convention.

Continue to a separately covered mathematical test only if sources
justify a concrete comparison or obstruction mechanism with the stated
uniformity. Import an exact known theorem with its hypotheses; do not
reprove it as a discovery. If a primary theorem excludes the proposed
class, record the precise hypothesis mismatch. If the exact inequality
is refuted in the literature, preserve that obstruction. If essential
coverage remains inaccessible, park the dependent target rather than
repeat retrievals. A finite simulation, missing estimate, or failure
of a triangle-inequality envelope is not a counterexample.

C466s is the single-divisor comparison and source-convention record;
C466u/t are current/survival contrasts, and C466k supplies the relevant
three-variable form and the generic local-phase limitation. None is
silently promoted to the proposed theorem. No cross-notebook input is
used. Matching Mathlib coverage is unchecked, not asserted absent.

The exact next task is literature_comparison, standard/high. A central
creative attempt is not yet justified: multi-collision source scope
and a concrete discriminating estimate remain unpaid. This nomination
prepares that gap instead of relabeling an audit or ordinary theorem
specialization creative. After coverage, choose the mathematical
purpose from the actual remaining work; no result is approved here.

## Completed bounded source comparison975

The exact TARGET and quantified mathematical test above are preserved.
No lemma or mathematical script was written or modified in this review.

### Search, duplicates and failures

Reused reviews948/958. Read C466s through its weighted cancellation and
the relevant local-scope/signed-form ranges of C466k. C466s uses one
normal divisor; C466k's arbitrary-map construction does not prescribe
this raw flow. C466t/u, stops971/972 and route-closure974 remain contrasts,
not premises. A targeted local search in the 14 November flow reviews,
ATTEMPTS and histories for three-particle, intersecting-divisor,
simultaneous-collision, Calogero/Dyson and class-uniform three-volume
phrases located only this nomination and explicitly deferred gaps.

External queries included `"Vandermonde" "holomorphic gradient flow"
Jacobian`, `"Vandermonde" "weighted volume" flow`, `"logarithmic"
"gradient flow" "simultaneous collisions"`, `"Vandermonde" "gradient
flow" "collision" "Jacobian determinant"`, `"Vandermonde" "third"
"compound" flow`, complex Calogero polynomial/heat-root dynamics and
deterministic Dyson/freezing limits. No inspected result matched the full
bound or supplied a counterexample. No novelty or exhaustive-absence
claim follows. Search snippets and random-matrix density formulas were
not used as theorem evidence.

### Available source inputs

TNV: Tanizaki, Nishimura and Verbaarschot, *Gradient flows without
blow-up for Lefschetz thimbles*, JHEP10(2017)100,
[v2, 27 September 2017](https://arxiv.org/pdf/1706.03822v2).
Reopened [Appendix B](https://arxiv.org/html/1706.03822v2#A2),
(B.1)-(B.5), printed p22 (HTML (69)-(73)): real initial variations
give dot J=conjugate((D^2S)J) for unit flat flow, locally on a
nonsingular branch. Both factors are conjugated. Sections2.2/3.1-3.2,
printed pp4-9, distinguish finite-time raw singularities and
weight-times-Jacobian qualifications from a decelerating metric with
polynomial S_B,D. Reused review948 and reopened the scalar zero case,
both footnotes, and the modified-flow proof cases. Taking D=Delta^2
does not remove the changed metric or polynomial-H restriction.
Neither scalar boundedness nor modified completeness supplies our
multidivisor raw bound. No homology theorem is imported.

WKM: Wu, Kanevskiy and Margaliot, *k-Contraction: Theory and
Applications*, [v2, 27 September 2021](https://arxiv.org/pdf/2008.10321v2),
Sections2.2/2.4-2.5 and Section3.1, printed pp4-9. Continuous real
A(t), any 1<=k<=n, Euclidean exterior norms and (17)/Proposition5 give
||Phi^(k)(t)||<=exp integral_0^t mu_2((A(s))^[k])ds; mu_2 is the sum
of the k largest eigenvalues of (A+A^T)/2. Read the complete
Proposition5 proof (compound equation and Coppel inequality) and
Theorem4 proof. Uniform negativity belongs to the contraction
conclusion, not this growth inequality. The stated range includes
n=6,k=3 and rectangular tangent columns via their initial wedge.
Compact survivor intervals have the required continuous coefficients.
The source does not bound the singular exponent uniformly.

### Many-particle comparisons

Hall and Ho, *The heat flow conjecture for polynomials and random
matrices*, Lett.Math.Phys.115:60 (26 May 2025),
[Section3.1, Proposition3.1, Remark3.2 and complete proof](https://link.springer.com/article/10.1007/s11005-025-01946-9),
(3.1)-(3.7): degree-N polynomials satisfy
partial_tau p=(1/(2N))partial_z^2 p. Distinct roots at complex sigma
admit local holomorphic labels satisfying
dz_j/dtau=-(1/N)sum_(k!=j)1/(z_j-z_k). The polynomial persists
through repeated roots; this asserts neither smooth root labels there
nor our fixed-initial-data determinant bound. Inspected the implicit
function step and the complete second-derivative cancellation. Our
target conjugates the force and permits arbitrary coupled H. No
complex-time identification or preservation of the initial imaginary
plane is justified for that class. Large-N transport conjectures are
not used as theorems. The cited Csordas-Smith-Varga (1994), Lemma2.4,
and Choodnovsky-Choodnovsky (1977), Corollary7, are unread originals,
not imported inputs.

Voit and Woerner, *The differential equations associated with
Calogero-Moser-Sutherland particle models in the freezing regime*,
[arXiv:1910.07888v1, 17 October 2019](https://arxiv.org/pdf/1910.07888v1),
(2.1), Lemma2.1, printed p3, and Theorem2.8/proof, pp6-7, concern
dx_i/dt=sum_(j!=i)1/(x_i-x_j) in the real ordered Weyl chamber.
Theorem2.8 gives a unique continuous solution from every closed
chamber point, interior for all positive times. Inspected its complete
boundary proof: symmetric polynomials, the real-rooted coefficient
region, discriminant, scaling and coincident-start case. These are
essential to that repulsive real evolution. This covers simultaneous
initial coincidences for its equation, not complex coupled H,
attraction toward a terminal divisor or our spatial determinant.
Time reversal alone imports no weighted boundary estimate. No
stochastic limiting statement replaces pathwise control.

### Real/complex volume convention and access qualification

The prospective real three-volume is the Euclidean norm of the
decomposable wedge of three real tangent columns in R^6, not ambient
six-volume or a product of column lengths. The complex determinant
comparison needs its standard finite-dimensional justification in the
mathematical attempt. For terminology checked Joyce, *Lectures on
special Lagrangian geometry*,
[arXiv:math/0111111v3, 29 September 2003](https://arxiv.org/pdf/math/0111111v3),
Section2, Definitions2.1-2.2 and phase paragraph, p2: the metric is
sum |dz_j|^2 and the phase-rotated real complex-volume forms have
the calibration bound on real m-planes. This is an inspected
exposition, not newly verified original theorem coverage. No
Lagrangian condition on the flowed plane is assumed.

The cited original Harvey-Lawson, *Calibrated geometries*, Acta
Math.148(1982), pp47-157, SectionIII.1, was not retrieved in full:
the YMSC mirror timed out, Euclid returned a security page and
Springer subscription content. No original theorem number or proof
is claimed inspected. This optional lead is parked, not an essential
blocker: continuation975 includes a short direct Gram/Hadamard norm
verification instead of importing the unread calibration theorem.
Reproving this supporting elementary inequality is justified to fix
the three-column norm convention, not as a new mathematical result.

### Decision and bounded test

EXPLORE records adequate bounded comparison for a mathematical attempt,
not proof of the inequality. The accessible primary variational and
arbitrary-k compound tools leave collective singular cancellation and
stopped class-uniformity unpaid. A failed separate bound on Jacobian
and weight, or an unbounded ambient-volume exponent, only rejects that
sufficient envelope unless actual admissible trajectories and the full
determinant are also controlled. The specified initial plane matters.

The single continuation is
[attempt975](2026-11-14-three-particle-weighted-volume-attempt-975.md).
It retains the full class and tests collective third-volume growth
against weight decay; no new estimate, constant or counterexample has
been derived here. Separated-pair control alone fails its threshold.
New hypotheses require review; further optional calibration retrieval
is not nominated. Full matching Mathlib coverage is unchecked.

This is development of the existing volume mechanism. No justified
central creative mechanism is supplied: a concrete source-assessed
link from local modulus to signed/global all-degree positivity is
still missing. Do not relabel this extension creative to fill a quota.
No cross-notebook input or change to the mathematical argument.
