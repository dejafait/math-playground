# One-sided full-density graph relation — completed source comparison

TARGET: Assess whether convex integration for open ample first-order relations applies to Re(F(Phi_u)det(I-iDu))>0 off the full F divisor, with periodic graph and exchange constraints.
CHECKED: 2026-11-06
DECISION: EXPLORE
SEARCH_EVIDENCE: Searched exact one-sided holomorphic-form, graph, ample-relation and equivariant terms; read Gromov's primary theorem and relevant proof cases, the Eliashberg-Mishachev definitions and cube/global proofs, and the sphere-eversion project's smooth theorem proof. Checked the named local moment, phase and contour-import failures. No inspected theorem decides the actual relation; no novelty inference.
SOURCE_EVIDENCE: Gromov (1973), definitions1.1.1-1.2.6, Theorem1.3.1/Corollary1.3.2, pp329-331, Lemma3.1.3 and Section3.2, pp339-340; Eliashberg-Mishachev (2002), Sections18.1-18.4, pp163-168, especially18.2.1-2/18.4.1 and following Remark2; sphere-eversion blueprint Definition3.23/Theorem3.26 and its proof. Reuse L847(1)-(3) and the inspected Katkova scope in the joint-contour assessment. Exact access and qualifications below.
COMPARISON: The primary result requires ampleness in local coordinate principal directions, not merely an open underdetermined inequality; its general corollary tests every principal direction. It is conditional on a formal solution. The smooth implementation does not remove these hypotheses. Neither inspected construction gives the requested exchange-symmetric graph across the moving full F divisor without additional work.
GAP: The actual principal slices have not been computed, so no ampleness or nonampleness conclusion is established. Formal-solution existence, an applicable global open relation including divisor contacts, exchange-preserving construction and C2 extension remain unproved. A separate bounded slice calculation is now specified; no graph or Xi sign follows from this review.
REASON: The primary theorem supplies a concrete discriminating local test and rules out treating openness alone as an existence input. Complete that routine prerequisite before proposing a creative global construction. This is new source coverage, not a new mathematical theorem or a proof that the contour route is impossible.
LITERATURE_REASON: The changed one-sided off-divisor relation was REVIEW_REQUIRED at invocation; its essential primary ample-relation and regularity hypotheses were outside the ready two-moment/full-phase coverage.
SCOPE: Actual L847 G,R,C,F and angular graph; prospective real periodic exchange-symmetric C2 u. The strict relation is considered only where F(Phi_u)!=0; the full F divisor including the exchange diagonal is retained. It would restrict to J!=0 off that divisor and does not exclude other graphs with J zeros there. No actual quadruple, prescribed collar, global graph, bound on u, RH or all-degree transfer is assumed.

## Original nomination — preserved, superseded by the completed review below

The main gap remains L030-L032/C032a actual-Xi all-degree mixed
positivity. A less restrictive phase condition is a prospective way
to seek an actual contour sign rather than impose an unproved estimate
on variable weights. At best a construction here concerns L847's fixed
r=2,k=1 form; higher dimensions, shifts and the full positivity target
would remain independent. No new implication for a minor is proved
in this nomination; reuse the exact integral input before asserting one.

The next step is source comparison only. Retrieve the exact primary
definition and theorem for open ample first-order relations, including
the principal affine-slice convex-hull condition. Determine whether its
graph, global formal-solution and regularity hypotheses even fit the
proposed coefficient-dependent relation. Check duplicates and source
obstructions before proposing an algebraic slice test. Do not infer
ampleness from underdetermination or openness, or infer C2 solutions
from a C1 h-principle. Exchange and extension across a moving vanishing
divisor require explicit coverage; allowing the density to have an
imaginary part does not remove those obligations.

Continue only if exact source scope identifies a concrete local test
with a plausible graph-preserving construction downstream. If an
essential hypothesis fails or no such construction route is justified,
record that restriction and select independent work; do not repeat an
automatic contour-existence import. This review may instead delimit
a bounded obstruction test, but may not perform and approve it in the
same turn. Full matching Mathlib coverage has not been checked.

Compared three possibilities when closing the prior test: repeat
unweighted moments (now stopped), seek an actual-F range bound without
any bound on u (no justified estimate available), and examine this
changed open relation. Only the third is nominated for assessment.
The count-only, full-phase, linking-import, prescribed annular
and fixed-cutoff stops remain evidence at their stated scopes.
In particular the source stop in
`ATTEMPTS/2026-11-06-joint-contour-automatic-sign-transfer-source-stop.md`
already rejects invariance or a conjectural flow as an existence proof.

Creative priority is considered: the changed relation is a candidate
construction mechanism, but no applicable primary theorem or concrete
formal solution has been identified. These missing inputs prevent an
honest creative proof-attempt nomination now. If source comparison
prepares a genuinely new central construction, nominate its exact
bounded test and escalation separately. This file derives no
mathematics and approves no continuation calculation.

## Completed review, 6 November 2026

The main gap remains L030–L032/C032a actual-Xi all-degree mixed
positivity. The intermediate target is applicability of open-ample
convex integration to the nominated one-sided graph condition. A
successful construction could supply a sign contour for the fixed
r=2,k=1 integral; higher orders, other shifts and all-degree transfer
remain independent. The present review constructs no such contour.

### Primary theorem and the exact test it requires

M. L. Gromov, *Convex integration of differential relations. I*,
Math. USSR-Izv. **7** (1973), 329–343,
[primary English text, DOI10.1070/IM1973v007n02ABEH001940](https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=2250&what=fullteng).
Read definitions1.1.1–1.2.6, pp329–331, Theorem1.3.1 and
Corollary1.3.2, p331, the complete cube Lemma3.1.3 and proof,
p339–340, and Section3.2, p340. The theorem assumes a smooth
bundle and an open first-jet relation, ample in suitable local base
coordinate directions over neighborhoods of zero-jets. The corollary
uses all principal directions. A formal section into the relation is
an essential input; weak homotopy equivalence does not produce one.
The cube construction gives C1 sections and preserves the specified
boundary jets, then the global argument uses local cubes and skeleta.

In source terminology a principal slice fixes a zero-jet and the
derivative on a base hyperplane. Each nonempty path component of its
intersection with the relation must have the whole slice as convex
hull. The empty intersection is ample by convention. This component
condition, rather than the convex hull of the entire derivative
fiber or a count of free variables, is the required discriminator.
These definitions are cited inputs, not new results reproved here.

Y. Eliashberg and N. Mishachev, *Introduction to the h-Principle*,
Graduate Studies in Mathematics **48**, AMS, 2002,
[book transcription, Sections18.1–18.4, pp163–168](https://fliphtml5.com/ksndd/kdwz/(Graduate_Studies_in_Math.)_Eliashberg_Y.,_Mishachev_N._-_Introduction_to_the_h-Principle._Volume_48-AMS_(2002)/).
Read the principal-space definitions, cube theorem18.2.1 and its
complete coordinate-by-coordinate proof, relative corollary18.2.2,
Theorem18.4.1, its proof and following Remark2. Principal coordinate
slices vary one column with the others fixed. The cube theorem
starts with a formal solution genuine near the preserved boundary;
successive derivative corrections stay in the open relation. The
global theorem follows by induction over a triangulation. Remark2
permits ampleness in a covering's chosen coordinate directions.
Section18.1's half-space example is a warning that open derivative
conditions need not be ample. Its submersion example is not a
classification of our coefficient-dependent relation. The transcription
contains apparent dimension-inequality errors in examples; none is
used as a theorem input or silently repaired. The definitions and
theorem were compared with Gromov's primary text.

### Smooth version and qualifications at the actual target

The authors' formalization project supplies a further inspected
implementation: *The sphere eversion project*,
[global chapter, Definition3.23, Theorem3.26 and its proof](https://leanprover-community.github.io/sphere-eversion/blueprint/chap-global.html).
Its smooth formal sections and smooth homotopies are explicit in
Definitions3.16–3.20 and the proof's predicates. The theorem is
relative, parametric and C0-dense for open ample relations on smooth
manifolds. Its proof localizes and applies the local h-principle
successively. Thus C1 output is not an intrinsic restriction of every
implementation. This still supplies no smooth actual solution here:
openness, ampleness and an applicable formal solution must first be
established for the required global relation. No smoothing theorem is
invoked across a divisor where the strict margin vanishes.

Use exactly L847(1)–(3), with independent derivative variable A when
testing a first jet. The prospective strict relation is considered
over zero-jets (theta,y) with F(Phi_y(theta)) nonzero. Working on that
open domain retains the one-sided inequality; it does not solve the
global problem in which a graph may meet the full F divisor. Adding
unrestricted jets at F=0 is not justified by the cited open-relation
theorem. No openness proof or disproof for that enlarged relation is
claimed here. Nor may one remove the exchange diagonal and infer a
C2 extension there. The divisor depends on the zero-jet y, so it
cannot be treated as a prescribed closed subset of the base without
specifying and checking the construction.

Periodicity can be posed intrinsically over T2 in the trivial
R2 bundle. That identifies the correct ambient setting but supplies
no formal solution. Keep the angular projection fixed by solving for
u; a theorem for arbitrary immersions in X need not preserve this
graph condition. Exchange means u(t,s) is the coordinate swap of
u(s,t). The inspected relative/parametric theorems do not assert an
equivariant version with this fixed-point diagonal. Averaging a
solution, quotienting the diagonal or preserving an unconstructed
collar is not authorized by them. An independent equivariant or
relative extension argument would be necessary after the local test.

No branch of log F, global bound on u, actual zero quadruple, collar,
nonvanishing Jacobian at F=0, minor sign or RH is assumed. The
nonvanishing Jacobian requirement off F=0 is already part of the
nominated strict relation; this review does not exclude graphs
allowing Jacobian zeros elsewhere. Reuse the joint-contour assessment's
Katkova real-part integral scope before asserting any minor conclusion.

### Searches, overlap and bounded next discriminator

Queries actually issued included:

- `convex integration open ample first order differential relation principal subspace theorem Eliashberg Mishachev`;
- `site.math.ias.edu Gromov convex integration ample differential relation half space`;
- `"Eliashberg" "18.4.1" ample pdf`;
- `"18.4. Convex integration" "167"`;
- `"Gromov" "convex integration" "1973" pdf ihes`;
- `"Re" "holomorphic volume form" "ample" graph`;
- `"positive" "complex volume form" "convex integration"`;
- `"convex integration" "exchange" "fixed points" equivariant differential relations`.

The bounded search found the primary and book statements above,
not a matching graph/exchange/divisor theorem. Generic symplectic,
Calabi-Yau and unrelated exchange hits were discarded. Martinez-Aguinaga
and del Pino's *Convex integration with avoidance and hyperbolic (4,6)
distributions*, arXiv2112.14632, is an unread lead, not an applicable
theorem or a ready replacement if ordinary ampleness fails. No novelty
claim follows from the searches. The nzdr book PDF timed out twice;
the full relevant book passages and primary English paper were accessible
elsewhere, so no essential source blocker remains for a slice test.
PDF screenshot calls returned no readable image; only the retrieved
text passages count as inspected evidence.

Local comparison used L847's exact graph/pullback and moment section,
the actual-G full-phase assessment, and the recorded two-moment,
two-period and automatic-contour-import stops. A narrow search of
6 November assessments/attempts and foundations found only generic
h-principle leads in the annular review, not this principal-slice test.
No exhausted mechanism is reopened by the source comparison.

The concrete next discriminator is recorded in
`drafts/literature/2026-11-06-real-part-principal-slice-test.md`.
Compute the actual derivative-slice intersections and component convex
hulls before attempting a formal solution or global construction.
Check arbitrary principal directions if a failure in the displayed
coordinates could be remedied by another coordinate frame; failure
in one displayed direction alone does not reject Gromov1.3.1's weaker
hypothesis. Continue this import mechanism only if the required local
coordinate ampleness survives. If a zero-jet rules out every local
frame, retire the direct open-ample import; that would not exclude
all convex-integration techniques or all contours. No slice result
is derived or approved as true in this source turn.

Creative priority is considered. A new central contour construction
would require the still-unverified local flexibility hypothesis and
an actual formal solution. The bounded next step is an ordinary
hypothesis calculation, not a creative proof attempt. Complete that
discriminator before nominating more expensive construction work.
The newly written ready continuation receives a separate approval
next turn. No lemma, mathematical script, DAG edge or PROOF argument
was modified. General supporting Lean declarations include
`RelMfld.Ample` and `RelMfld.Ample.satisfiesHPrincipleWith` in the
external sphere-eversion project; current Mathlib coverage of the
full target has not been checked. No cross-notebook theorem is used.
