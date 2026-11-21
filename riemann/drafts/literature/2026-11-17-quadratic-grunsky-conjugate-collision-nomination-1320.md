# A distinct-point collision nomination1320 — source review1321

TARGET: Test whether C031c's fixed-u=400 branch has distinct conjugate points in |z|<1 with equal f_tau-values for every sufficiently small positive tau, by first-order continuation of the single candidate pair exp(±i*pi/3) at tau=0, using only C031c's tangent and the fixed1307 boxes.
CHECKED: 2026-11-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1321 searched Grunsky-named local assessments/attempts/histories and C031a-d for collision/conjugate/two-point/divided-difference/Joukowski terminology; read C031a,c and relevant C031d/stop1307/1311/1320 ranges. External exact, stronger-result and typically-real queries below; primary passages inspected, ready IFT coverage reused. No novelty inference or branch calculation.
SOURCE_EVIDENCE: Leeman, Pacific J. Math.52(2)(1974),481–484, p481 Definition1 and following observation, https://msp.org/pjm/1974/52-2/pjm-v52-n2-p16-p.pdf ; Stanford Math270 course extract Chapter1 The Holomorphic Functions, dated31 March2003, printed p32 (3.23)-(3.25), https://math.stanford.edu/~ryzhik/MATH270-06/shabat-chapter1.pdf ; Ponnusamy-Wirths arXiv1704.08184v1 Theorems1-2/proofs/Remark1, https://arxiv.org/html/1704.08184v1 ; reuse de Oliveira arXiv1212.2066v1 Section3 Theorem2, https://arxiv.org/html/1212.2066v1 , as inspected in1315/1319.
COMPARISON: Classical typically-real necessity identifies an interior nonreal real-valued point as an obstruction for a real-coefficient holomorphic univalent map; the Joukowski example covers the base boundary pairing after normalization. Real C1 IFT covers a scalar radial continuation only after its dependent derivative is verified. No inspected theorem determines this branch's radial sign. Sufficient disk bounds, outward critical roots and failure of sufficient criteria do not decide the collision.
GAP: In a later mathematical turn, verify the nominated pair's exact denominator/base guards, scalar radial Jacobian, derivative and strict inward sign from C031c's tangent/fixed1307 boxes, then prove equality and distinctness persist. Source coverage is adequate; these instance-specific calculations, any effective tau interval and whole-disk univalence remain unpaid.
REASON: The changed target now has inspected classical obstruction/base coverage and reusable IFT coverage. Import the general results rather than reprove them; only the stated finite specialization remains. Preserve the single-pair target for separate supervisor approval before calculation; no essential source blocker remains.
SCOPE: Exactly the saved TARGET: fixed u=400, C031c's real C1 branch/tangent, one pair exp(±i*pi/3), fixed angle with a common real radial variable near1, unchanged fixed1307 actual boxes, and first order only. No angle/weight sweep, higher-order branch calculation, uniform effective radius, whole-disk sufficiency or all-degree positivity.
LITERATURE_REASON: This target was REVIEW_REQUIRED at invocation: distinct-point conjugation and the boundary-pair normalization were outside the ready four-root assessment. Reuse the existing IFT extraction; inspect only the missing collision/base coverage and the relevant sufficient-criterion boundary case.

## Original nomination1320 (historical, before review1321)

The main gap remains actual-Xi all-degree positivity in L030–L032/C032a.
A proved collision inside the open disk would park this particular
realization even though its four continued pole/critical roots move
outward. Failure of this new test would leave whole-disk univalence
undecided. This is a bounded independently testable obstruction lead,
not a new sufficient realization construction or an approved theorem.

The source-review task is to search the exact statement and stronger
results, inspect primary hypotheses/proof cases for the required
specialization, and compare the recorded local divided-difference and
meromorphic-univalence evidence. The base pair and relevant real root
formulation are to be checked in that assessment without deriving a
new collision lemma. Ready real IFT coverage may be reused only when
its applicability is actually established. If essential comparison
fails, record it rather than approving a calculation by analogy.

Continuation inputs are C031a,C031c,C031d and C030z's inherited fixed1307
boxes, with L025,L027 and L019,L021,L036,L037,L917/1307 inclusion and
Decimal contracts. C031d is new and has not received a separate
critical audit; it motivates the route choice, rather than serving as
a premise for any collision theorem. Independent initialization,
larger blocks, actual identification and analytic realization remain
open. Other regular/singular/non-C1/fractional-power/zero/diverging-weight
branches are unclassified. No RH or cross-notebook premise is used.

No new formula, lemma or script is part of this nomination. A strict
inward collision continuation would justify stopping this fixed branch;
an absent or uncertified strict sign stops this single-pair test, with
no higher-order or angle search. A genuinely new sufficient mechanism
at the central all-degree gap is still unspecified; do not relabel this
classical-tool obstruction specialization as proof_attempt/creative.
Mathlib coverage for this changed target remains unchecked.

## Completed literature-only review1321 — 17 November2026

The main gap is actual-Xi all-degree positivity in L030–L032/C032a.
The intermediate target is the exact single-pair test above. A verified
interior collision would park this fixed realization despite successful
finite matching. Its absence would not supply the analytic hypothesis
needed for a Grunsky sign transfer. No new lemma, expanded collision
polynomial, Jacobian value, branch derivative or interval calculation is
part of this review.

### Inspected inputs and their limits

G. B. Leeman, Jr., *A local estimate for typically real functions*,
Pacific J. Math.52(2)(1974),481–484,
[p481, Definition1 and following observation](https://msp.org/pjm/1974/52-2/pjm-v52-n2-p16-p.pdf).
Read the definition and the full short conjugation argument: normalized
analytic univalent functions with real coefficients are typically real,
so a nonreal interior point cannot have real image. This supplies the
standard name and necessity relevant to the nominated obstruction.
It is not a sufficient univalence condition or a perturbation theorem.
No coefficient estimate from the remainder of the paper is imported.

The university-hosted Stanford Math270 course extract, *Chapter1.
The Holomorphic Functions*, dated31 March2003,
[printed p32, (3.23)–(3.25)](https://math.stanford.edu/~ryzhik/MATH270-06/shabat-chapter1.pdf)
(PDF index31), gives J(z)=(z+1/z)/2, its equal-value factorization,
the reciprocal-pair condition z1*z2=1, and its radial real/imaginary
coordinates. Read that whole example through the ellipse discussion.
C031c's stated base rational map
is 1/(2J) away from exceptional values. Thus the named conjugate
unit-circle pair is in the classical boundary-pairing example, rather
than an asserted interior collision. Reciprocal postcomposition needs
a finite nonzero J-value; z=0, J=0 and the real coincident endpoints
cannot be silently included. This normalization comparison identifies
the source scope only; the future proof must record exact candidate
values and guards. The extract itself has no visible author/title-page
attribution, so no book edition or author is inferred from its filename.

Reuse de Oliveira, *The Implicit and the Inverse Function Theorems:
Easy Proofs*, Real Anal. Exchange39(1)(2013/2014),207–218,
[arXiv1212.2066v1, Section3 Theorem2](https://arxiv.org/html/1212.2066v1),
with the full theorem/proof extraction already inspected in1315/1319.
The hypotheses are a C1 real map on an open neighborhood, a base zero
and an invertible dependent derivative. Its local graph and derivative
formula are all that is needed. C031c supplies real C1 coefficients on
both sides of zero; rational evaluation is usable only on a neighborhood
where its denominator does not vanish. The scalar dependent variable
can be a common real radius near1 with angle fixed at pi/3. The relevant
real equation asks that the evaluated image have zero imaginary part.
No two-dimensional holomorphic-parameter theorem or analytic dependence
on tau is assumed. In particular the general theorem does not certify
the scalar Jacobian, and a nonzero spatial derivative of f alone does
not replace that specific radial check.

Reopened Ponnusamy–Wirths, *Elementary considerations for classes of
meromorphic univalent functions*,
[arXiv1704.08184v1, Theorems1–2/proofs/Remark1](https://arxiv.org/html/1704.08184v1).
Theorem1 assumes normalized meromorphic f and the strict disk bound
|z/f-z*(z/f)'-1|<1. Its proof obtains an integral representation and
bounds a divided difference; Remark1 permits a simple pole. Theorem2(b)
requires the stronger bound with a fixed lambda<1 for closed-disk
univalence; read its proof's lower bound 1-lambda*|z1*z2|>0.
Neither theorem is automatic from coefficient continuity. The strict
lambda<1 condition cannot be replaced by lambda=1 at boundary points.
Failure of either sufficient hypothesis proves no collision. We do not
test these inequalities here or use the representation for an arbitrary
rational branch. This reuses1312/1314 and checks the additional boundary
case relevant to the new target.

### Bounded specialization and decision test

After separate approval, keep the one nominated angle and introduce
only the common real radius. Verify the base equation and both
denominators, real C1 regularity on an open neighborhood and the scalar
dependent derivative before invoking IFT. Derive the radial tangent
using only C031c's existing tangent. Clearing denominators requires
proof that it preserves the equation near the pair; no numerator root
at a pole counts as a collision. The real-coefficient conjugation
identity must be justified for this rational map, so a real image gives
equal finite values at the conjugate points. Radius near1 must remain
positive and the pair nonreal/distinct. These are future proof
obligations, not completed checks in this assessment.

The continuation threshold is strictly negative first derivative of
the squared radius at zero. If certified with the unchanged fixed1307
boxes, use the differentiability remainder to prove that both points
lie in the open disk for every sufficiently small positive tau.
Continuity must preserve all guards on the same sufficiently small
interval. The interval may depend on the fixed actual tuple; no
effective or box-uniform radius follows from the sources.
If the base or scalar IFT hypotheses fail, or the required strict inward
sign is absent or uncertified, stop this single-pair test. Outward
motion excludes only this continued pair as an inward obstruction;
zero/tangential motion is inconclusive. Do not search other angles,
vary weights, expand to higher order or infer global univalence.

### Duplicate, search and coverage record

Scoped local searches used collision, conjugate, two-point,
self-intersection, distinct-point, divided-difference and Joukowski
within Grunsky-named assessments/attempts/histories and C031a-d.
Read C031a and C031c, C031d's hypothesis/conclusion, and recorded
stops1307/1311/1320. C031d's outward evidence is motivation only; no
separate audit is smuggled into this test. The older linear-prescription
stop is not a theorem about these quadratic-defect equations.
No completed single-pair collision test was found in this bounded
comparison; that is not a novelty claim.

External queries included `Joukowski map unit circle conjugate points
z/(1+z^2) univalent reciprocal rational function`; `Ponnusamy Wirths
1704.08184 univalence rational functions divided difference theorem 1`;
`rational function univalence conjugate points real coefficients
perturbation Joukowski map`; `"Grunsky" "quadratic defect" collision`;
`"Joukowski" "perturbation" "univalence" rational`;
`"z/(1+z^2)" univalent`; `"rational functions" "univalence"
"real coefficients" typically real`; `"typically real" "univalent"
"real coefficients" theorem`; `"implicit function" "Joukowski"
collision`; and `"Grunsky" "conjugate" "collision"`.
Only the inspected primary passages above are theorem inputs. Search
results did not establish a theorem deciding this actual branch's sign.

A targeted Reade–Silverman–Todorov query located the AMS contents entry
for *Classes of rational functions*, Contemporary Mathematics38(1985),
91–97, and an Academia lead titled *Univalent Rational Functions on the
Unit Disc*. Neither theorem text was inspected or imported. They remain
unread leads, not evidence for a collision or a source-access blocker:
this target needs one explicit necessary obstruction rather than a
classification or a sufficient rational-univalence criterion. Harmonic
and logharmonic typically-real search hits have different hypotheses
and are not imported. No broader inverse-realization theorem is claimed.

Mathlib: reuse the supporting IFT tools documented in1315/1316 and
C031c. Full matching typically-real, conjugate-collision, rational-map
and actual-Xi specialization coverage has not been checked; no absence
or Lean-verification claim. The later canonical proof should carry the
precise imported citations and verify its instance-specific hypotheses.

Continuation inputs are C031a,C031c and the fixed1307 boxes in C030z,
with L025,L027 and inherited L019,L021,L036,L037,L917/1307 inclusion
and Decimal contracts. C031d is contextual, not a mathematical premise.
Larger blocks, singular/non-C1/fractional-power/zero/diverging-weight
branches, actual identification and initialization remain unresolved.
No RH or cross-notebook input. Local progress is source coverage only,
not progress beyond the cited classical results. The next calculation
is REPRODUCTION specialization. A sufficient central-gap construction
is still unspecified, so no creative target is justified by this review.
