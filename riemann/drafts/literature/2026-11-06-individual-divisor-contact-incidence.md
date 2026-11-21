# Individual-divisor contact incidence — completed source comparison

TARGET: Test whether individual G-zero intersection counts and L860's conjugate tangent condition obstruct a nonempty finite set of simultaneous simple contacts on an exchange-symmetric nonnegative L847 radial torus.
CHECKED: 2026-11-06
DECISION: EXPLORE
SEARCH_EVIDENCE: Bounded exact-phrase, degree, signed-intersection and stronger-result searches located primary degree texts but no theorem settling this full radial-graph census. Read the scoped local contact records and three relevant stops; exact queries, inspected ranges and source limitations are below. No novelty inferred.
SOURCE_EVIDENCE: Milnor, Topology from the Differentiable Viewpoint (1965), Section5 pp27-29, definition, Theorems A/B and Lemmas1/2 with oriented boundary and exceptional-value proof cases; Teschl, Nonlinear Functional Analysis, 23 June 2004, Sections2.2-2.3 pp13-22, definitions(2.5)-(2.6), Theorems2.1/2.2/2.4/2.11 and local-sign/C2 proof cases. L847 and audited L860 supply the exact local graph and tangent input; links and qualifications below.
COMPARISON: Signed regular-value counts are standard imported mathematics, not new results. They neither prescribe individual contact pairs nor solve the coupled angular/tangent constraints. Milnor requires smooth maps; Teschl covers the C1/C2 finite-domain tools needed for cuts and fibers. No inspected source settles the exact census or upgrades it to existence of a nonnegative torus.
GAP: Specialize the cited degree tools to each individual coordinate value, checking cut boundaries and real orientation, then combine all necessary counts with exchange, angular location and L860's full conjugate-tangent condition. No count, incompatibility or compatible assignment has been derived in this literature turn.
REASON: Essential source coverage for this unchanged bounded test is now adequate. Approve one subsequent mathematical attempt using imported degree results, without reproof or further unchanged browsing; an obstruction or compatible census remains to be tested.
SCOPE: Exactly TARGET for the actual L847 G,R,C,F, real C2 periodic u with u1(theta2,theta1)=u2(theta1,theta2), original orientation and globally real q=F(Phi_u)det(I-iDu)>=0. Explicitly restrict the entire set where either pulled-back G vanishes to a finite nonempty set of distinct simultaneous nonzero simple-zero pairs, with J!=0 at each contact. No restrictions on J away from these contacts, no prescribed collar, no RH or existence of selected actual zeros are assumed.

## Completed review — 6 November 2026

The main gap is still L030-L032/C032a, actual-Xi all-degree mixed
positivity. The intermediate target is exactly TARGET: compatibility
of individual contacts on the restricted global torus. Its plausible
downstream use is to constrain global extension of L860's free germs.
It does not supply prescribed gluing, force a contact or transfer a
sign to Xi. This review supplies source coverage, not a new theorem.

### Primary results actually inspected

**Closed-manifold reference.** John W. Milnor, *Topology from the
Differentiable Viewpoint*, University Press of Virginia, 1965,
[Section5, printed pp27-29](https://www.maths.ed.ac.uk/~aar/papers/milnortop.pdf#page=38).
For smooth maps between oriented boundaryless n-manifolds, with compact
domain and connected target, degree is the sum of derivative-orientation
signs at a regular value. Theorems A/B give independence of that value
and smooth-homotopy invariance. Target compactness is not required.
Read Lemmas1/2: boundary-extension cancellation, oriented arc endpoints,
and the case where a value is regular only on the boundary. Our parameter
torus has the required topology; C2 regularity alone does not meet this
book's smoothness convention. Use the next source for finite-regularity
calculations rather than silently strengthening u to smooth.

**Finite-regularity reference.** Gerald Teschl, *Nonlinear Functional
Analysis*, version 23 June 2004,
[Sections2.2-2.3, printed pp13-22](https://www.math.chalmers.se/Math/Grundutb/GU/MMA120/A14/lecture%20notes/Teschl%20G.%20Nonlinear%20functional%20analysis%20%28lecture%20notes%2C%20web%20draft%2C%202004%29%2874s%29.pdf).
Here U is bounded open in R^n, f and its stated derivatives extend
continuously to its closure, and y is outside f(boundary U).
Theorem2.4 gives the finite signed-Jacobian sum for C1 f at a regular
value. Theorems2.1-2.2 give additivity, boundary dependence and admissible
homotopy invariance; Theorem2.11 establishes existence. Read the local
linearization and negative-determinant case (pp15-17), and Lemmas2.6-2.8's
inverse-neighborhood and compactly supported C2 divergence argument
(pp18-20). These are tools for one- and two-dimensional cut domains;
no C-infinity approximation is needed. Import these results, without
reproving general degree theory. Their hypotheses must be checked at
each subsequent application.

### Applicability and remaining comparison

L847's C2 periodic u gives C2 coordinate maps and C2 restrictions
to angular fibers. The finite simultaneous-contact hypothesis and
L860's rank-two conclusion are the available inputs for checking the
regular-value condition at each contacted coordinate value. Retain
all preimages of that value, rather than counting a selected subset.
For any cut interval or angular rectangle, first check that its entire
boundary misses that value and that derivatives extend to the closure.
Periodicity does not by itself supply admissibility of an arbitrary cut.
Use the real plane with its complex orientation and the original torus
orientation. Signed counts are not unsigned multiplicities. The complex
scalar J in L847 is not the real determinant of either coordinate map.

The future specialization must retain the exact coordinate arguments
and moduli of each zero label, possible coincident arguments, ordered
parameter locations, exchange symmetry and the complete condition
l2=c conjugate(l1), K0 c>0 from L860. It may not replace these by a
free intersection graph or treat q>=0 as positivity of each individual
intersection. Distinguish coordinate-value counts from the aggregate
zero count of G composed with a coordinate map. The cited general
theorems make no such coupled classification, and no inspected
stronger theorem supplies it. This is the remaining problem-specific
calculation, not a reason to reprove the standard inputs.

Reuse the completed Auroux/Pacini/linking comparison in
`2026-11-06-l858-forced-contact-linking-review.md` for its recorded scope.
Its relative-disc and totally-real-boundary formulas do not settle this
coordinate-value census. No new symplectic, holomorphic-curve or
divisor-complement hypothesis has been established. Search hits about
those subjects were not imported as intersection-positivity theorems.

### Search, duplicates and access evidence

Queries issued for this review:

- `Milnor Topology differentiable viewpoint degree regular value compact manifold mapping plane signed count zero`;
- `radial graph torus projection plane prescribed argument degree intersection signed zeros`;
- `Brouwer degree C1 regular value Teschl nonlinear functional analysis pdf`;
- `"signed intersection" "radial" "torus" holomorphic zeros`;
- `"torus" "conjugate" "positive" "holomorphic" "divisor" intersection`;
- `"nonnegative" "holomorphic volume form" "intersection"`;
- `"radial graph" "divisor" "torus"`;
- `"signed" "intersections" "torus" "fixed argument"`;
- `"simultaneous" "zeros" "conjugate" "totally real"`.

Milnor's primary text was accessible. Teschl's author-site PDF returned
403, but the Chalmers copy of the author's 2004 manuscript supplied the
actual definitions, theorem statements and relevant proof cases through
web text extraction. Its screenshot endpoint failed after a redirect;
the inspected text is the evidence, not a claimed PDF-image inspection.
No essential access blocker remains for this bounded attempt. The
different current author-site book was not used for theorem numbering.

Mark Groves's *Introduction to Nonlinear Applied Analysis*, 21 April
2016, [Section4.1, pp48-51](https://bathsymposium.ac.uk/wp-content/uploads/2021/07/scriptum.pdf#page=48),
was an inspected alternate lead. Its stability lemma prints uniform
closeness while asserting stability of regularity; do not import that
clause. It is unnecessary because Teschl supplies the load-bearing tools.
Other search hits on holomorphic curves, volume forms and unrelated
radial surfaces remained unread leads, not theorem evidence. A failed
exact search does not certify novelty.

Locally searched the individual-zero/incidence/intersection/degree
terms in the simultaneous-contact assessment, its source-review history,
the L860 audit history and the full-phase assessment. Read L847's full
graph/form section and L860's complete construction/converse/audit.
Read these specific failure records:
`ATTEMPTS/2026-11-06-full-phase-two-period-obstruction-stop.md`,
`ATTEMPTS/2026-11-06-forced-contact-linking-import-scope-limit.md`, and
`ATTEMPTS/2026-11-06-free-germ-boundary-scope-stop.md`.
No matching individual-label calculation was found in these scoped
records; no notebook-wide novelty claim is made. Preserve all three
stops. C858a's compatible full-phase periods are context, not a premise;
C858b is not used. No cross-notebook input is needed.

### Bounded mathematical continuation

Approve the unchanged TARGET with the unchanged SCOPE above. First
obtain the necessary individual-value counts using the cited degree
tools and then test their joint compatibility with all the retained
angular, exchange and L860 tangent data. Continue only if the test
gives a restrictive inconsistency or a substantive additional constraint.
Retire this count mechanism if a nonempty assignment satisfies every
condition actually established, or if it reduces to the stopped
full-phase periods. Report precisely which implication the assignment
tests. A formal assignment requiring unspecified zero configurations
is conditional evidence only; it is not a realized actual-G census.
Do not invent or certify actual zeros to obtain the discriminator.

The entire G-contact set is assumed finite and nonempty and consists
only of distinct nonzero simultaneous simple-zero pairs with J nonzero
at contacts. These restrictions are not forced by the sign condition.
No global restriction on J away from contacts, prescribed collar or
selected actual pair is added. Generic perturbation is not authorized
as a way to preserve q>=0 or to remove other contacts. If the exact
target requires an essential theorem outside this assessment, stop that
dependent derivation and mark the changed target REVIEW_REQUIRED.

This source gate is complete for the saved action; the mathematical
test has not begun. The next work is a bounded calculation importing
standard degree results and using audited L860, not a new general
topological theorem. Do not label routine specialization creative to
meet a scheduling preference. A justified creative central-gap mechanism
would require substantive new input beyond these necessary counts;
its availability is still unestablished. Full matching Mathlib coverage
has not been checked; no absence assertion is made.

## Original uncovered nomination — preserved

The paragraphs below record the nomination before this source review;
their requests for future review describe that earlier state. The
completed decision and unchanged scope above govern the continuation.

### Why this continuation, and what it does not assume

The main gap remains L030-L032/C032a, actual-Xi all-degree mixed
positivity. The intermediate question is whether locally admissible
contacts can satisfy a global radial torus's individual divisor
constraints. A valid obstruction could restrict a future extension;
a compatible nonempty census would retire this particular count-only
mechanism before investing in it. Neither outcome alone signs an Xi
minor or supplies a prescribed extension.

Use L847's full density throughout. Use L860's audited tangent
condition only at contacts meeting its precise simple, nonzero,
distinct-pair and nonzero-J hypotheses. The finite-contact and
all-contacts-simultaneous restrictions above are hypotheses of this
test, not conclusions inferred about arbitrary nonnegative tori.
In particular neither C858b nor an assumed simplicity theorem for G
is a premise. A selected actual zero census remains unresolved.
There is no need to read another notebook.

The source review should first retrieve primary statements and
essential cases for degree of smooth maps from a closed oriented
surface to the plane, signed regular-value counts, and their
applicability to each coordinate of this C2 radial graph. Check
the target-space, compactness and regularity hypotheses explicitly.
Then compare any known intersection or symmetry constraint with
the fact that a contact pair has prescribed arguments. These are
source leads, not imported results. Reuse existing contact and
Maslov assessments only for their recorded scopes. Mathlib coverage
for the complete proposed test is not checked.

After adequate coverage, one bounded test would ask whether the
resulting necessary counts, exchange symmetry, angular locations
and L860 tangent conditions exclude every nonempty finite census.
The alternative discriminator is an explicit nonempty signed
incidence assignment satisfying all the conditions actually
established by that test, including its conditional zero data.
Such an assignment would refute only the claimed implication from
those constraints; it would not construct an actual positive torus.
Do not manufacture, certify or assume actual G zeros to make it fit.
If the sources already settle that comparison, import their result
and give only the needed specialization. If the constraints reduce
to a previously exhausted total-phase argument, abandon this target
without reopening that calculation under new terminology.

Compared continuing free local germs, repeating full-phase periods,
and this individual-divisor census, nominate only the third. The
first has no boundary matching; the second has a recorded compatible
period calculation. Their stop evidence remains unchanged. The new
proposal is independently falsifiable but not yet a justified
creative proof attempt: source comparison must determine whether
the retained individual data can provide a substantive global
constraint. Missing coverage is the present blocker to that routing,
not a reason to repeat the completed audit. No derived balance,
incidence assignment, theorem approval or mathematical script is
part of this nomination.
