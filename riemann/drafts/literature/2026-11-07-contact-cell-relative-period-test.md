# Contact-cell relative integrals — completed source comparison

TARGET: Test whether the four relative full-form cell integrals cut out by L882's fibers impose a phase constraint beyond its divisor counts, retaining both label branches and all arc windings.
CHECKED: 2026-11-07
DECISION: EXPLORE
SEARCH_EVIDENCE: Scoped local comparison of L847/L879-L882, L846/C858a, the named phase/fiber/count assessments and three relevant failure records; external searches for relative periods with divisor boundary, constant-phase contours and cubical Stokes. Read the primary statements and essential proof cases documented below. No matching four-cell constraint was found; this bounded search does not establish novelty.
SOURCE_EVIDENCE: Will J. Merry, Differential Geometry (2020-2021), Lectures25-26, Definition25.1, Definition25.20, Theorem26.2 and its restatement/proof Theorem26.17, PDF pp208,211,213,218-220; Jiri Lebl, Guide to Cultivating Complex Analysis v1.10 (5 November 2026), Definition4.1.1/Proposition4.1.2 pp94-95, Theorem4.3.3/Corollary4.3.4 pp100-101, Theorem4.4.2/Proposition4.4.3 pp104-108. Exact URLs and reading limits below; reuse the accepted stationary-phase and fiber inputs rather than reprove them.
COMPARISON: Smooth cubical Stokes and one-variable primitives with recorded logarithm changes provide tools for a bounded cell test. They supply neither the boundary-preserving comparison chain nor an actual-G phase restriction. L846's finite-box obstruction and C858a's compatible global windings do not decide this new relative-cell question.
GAP: Prove an evaluation of the actual four integrals, with every boundary face and logarithm change justified, then determine whether their common phase imposes anything beyond L879/L881/L882 and the total period. Cell invariance, determination by labels/windings and nonredundancy are unproved.
REASON: Essential source comparison is now adequate for one bounded attempt under unchanged hypotheses; no essential source blocker remains. General theorems must be cited, with only their necessary applicability checks. This review proves no cell formula or restriction. The newly ready assessment receives separate source-scope approval next turn before mathematical use.
LITERATURE_REASON: Changed target from L882's audited contact/count argument to relative full-form integrals; boundary preservation, corners and winding-dependent primitives were essential uncovered inputs. This turn fills that coverage rather than repeating the ready count audit.
SCOPE: Exactly L847 actual G/R/C/full form and dy1 wedge dy2 orientation; L879 smooth real periodic stationary u with J nowhere zero and its global phase line; L880-L882 complete fibers and both label branches. Smooth finite parameter cubes and homotopies in X=(C*)^2, with explicit side boundaries and lifted arc data. Retain all other zeros, diagonal vertices and multiplicities; no positivity, symmetry, analytic-u, collar, product graph, finite contact census or existence assumption.

## Completed review — 7 November 2026

This is a literature-only EXPLORATION, classified NOVELTY_UNCHECKED.
New source coverage is local preparation, not a mathematical advance
beyond the inspected literature. No cell integral, deformation theorem,
phase constraint, new lemma or mathematical script was derived. The
invocation-start REVIEW_REQUIRED decision is superseded by EXPLORE;
its original proposed test is preserved below. The exact TARGET has
not changed. A separate source-scope approval must precede the attempt.

### Local overlap and failures checked

Use the supplied full PROOF/DAG for the overview. Read L847's full-form,
orientation and smooth compact-homotopy argument, L879's hypotheses and
phase-line conclusion, L881's full hypotheses/count alternatives and
source interface, and L882's hypotheses, two branches and proof through
the completed count argument. Reuse the accepted audits of L879-L882;
this is not a fresh audit of their proofs. The existing assessment
`2026-11-06-odd-contact-boundary-fiber-compatibility.md` covers their
factorization, exact contact continuation and boundary-count tools.
The proposed calculation needs no fresh boundary principal-value
residue theorem unless it introduces a logarithmic derivative at G
zeros; that would require checking its new contour hypotheses.

Reuse `2026-11-06-real-zero-box-relative-cycle-test.md` for the distinction
between ordinary relative chains and a proved equality of their classes.
Read the finite-box and retired full-phase two-period stop records and
`ATTEMPTS/2026-11-07-boundary-fiber-count-only-limit-55.md`. They exclude
neither a new relative invariant nor these cell integrals. Their
conclusions cannot supply the missing cell evaluation. Also read
`ATTEMPTS/2026-11-06-divisor-real-flux-homotopy-incomplete.md`: a source
primitive did not solve a real radial correction problem. The present
test is integration on a fixed conditional stationary graph, not a
claim to repair that parked local existence mechanism.

The four parameter cells are the two arcs between a,c times the two
arcs between a,b. These are parameter domains only. L882 fixes one
coordinate on each of their four types of edge, but does not prescribe
the other coordinate's entire arc. Both eta=theta and eta!=theta
remain in scope. No sign is assumed throughout a cell, and the
additional zeros allowed in the unmatched branch cannot be discarded.
No cross-notebook result is used.

### Primary inputs actually inspected

**Smooth parameter-chain Stokes.** Will J. Merry, *Differential
Geometry*, ETH Zurich, academic year 2020-2021, Lectures25-26, last
modified 17 July 2021: [Definition25.1, PDF p208](https://www2.math.ethz.ch/will-merry/files/Merry%20-%20Differential%20Geometry%20%282021%29.pdf#page=208),
[Definition25.20, PDF p211](https://www2.math.ethz.ch/will-merry/files/Merry%20-%20Differential%20Geometry%20%282021%29.pdf#page=211),
[Theorem26.2, PDF p213; restatement26.17 and full proof, PDF pp218-220](https://www2.math.ethz.ch/will-merry/files/Merry%20-%20Differential%20Geometry%20%282021%29.pdf#page=218).
A smooth cube extends smoothly to a neighborhood of the closed cube;
it need not be embedded or immersed. Stokes pairs its signed cubical
boundary with a smooth form on the ambient smooth manifold. Read the
face convention, matching-face determinant calculation, Fubini/FTC
case and pullback reduction in all three proof steps. This covers
corners directly. Use real and imaginary parts separately. L847's
smooth form on X and L879's smooth periodic parameter map meet the
ambient regularity requirements for the proposed fixed cells. Every
proposed homotopy must also meet those requirements and retain all
side faces. This theorem supplies no homotopy or boundary cancellation.

Compared the narrower lead already cited in L847: Jiří Lebl, *Tasty
Bits of Several Complex Variables*, v4.4, 31 May 2026,
[Appendix C, Theorem C.6 and following regularity remark, p224](https://www.jirka.org/scv/scv.pdf#page=224).
Its stated theorem concerns an embedded compact oriented smooth
manifold with boundary; the following remark mentions corners but
supplies no proof. Merry's cubical theorem is the precise statement
used for the proposed parameter boxes. No stratified-space or
semialgebraic comparison theorem is needed for an explicit smooth
cubical homotopy. An arbitrary continuous relative-class replacement
would exceed this narrower approved implementation.

**One-variable primitives and logarithm changes.** Jiří Lebl, *Guide
to Cultivating Complex Analysis*, v1.10, 5 November 2026:
[Definition4.1.1/Proposition4.1.2 and complete proof, pp94-95](https://www.jirka.org/ca/ca.pdf#page=94),
[Theorem4.3.3/Corollary4.3.4 and proofs, pp100-101](https://www.jirka.org/ca/ca.pdf#page=100),
[Theorem4.4.2 pp104-107 and Proposition4.4.3 pp107-108](https://www.jirka.org/ca/ca.pdf#page=104).
The first proof tracks local logarithms along a piecewise-C1 cycle
avoiding the reference point. The primitive theorem requires a
holomorphic function on a simply connected planar domain; the log
corollary also requires a nowhere-zero function. Laurent expansions
converge on compact subannuli; the primitive formula excludes the
coefficient of z^(-1). Read that complete proposition: its proof is
explicitly left as Exercise4.4.1, not a supplied proof. Import the
stated standard result rather than reprove Laurent theory. The
primitive and logarithm proofs were inspected for path independence
and their nonvanishing requirements. For this test, any denominator
singularity at zero must stay outside the paths and comparison
chains; G zeros and the squared diagonal are numerator zeros in
L847, not poles of its full form. No log of G or division by G is
approved at a contact. Actual residues and primitive increments for
the chosen one-variable factors are still to be computed.

**Stationarity comparison.** Reuse the completed
`2026-11-06-stationary-graph-phase-components.md` and the boundary-fiber
assessment for Scott Lawrence and Yukari Yamauchi, *Convex optimization
and contour deformations*, arXiv:2311.13002v2, 14 August 2024,
[Section II B, equations(11)-(16), pp3-4](https://arxiv.org/html/2311.13002v2#S2.SS2).
The primary phase-variation passage and the following zero-separation
paragraph were reopened. They concern local phase constancy away
from zeros with an invertible complex Jacobian. They supply no
four-cell integral or cross-cell phase exclusion. L879 is the accepted
constrained specialization; neither unrestricted contour existence
nor its sufficiency language through zeros is imported.

### Discovery searches and result

Actual external queries for this review were:

- `"relative periods" "divisor" "boundary" integrals holomorphic`;
- `"constant phase" "contour" "relative" zeros integral`;
- `Lebl Tasty Bits Several Complex Variables Theorem C.6 Stokes`;
- `complex analysis primitive annulus residue logarithm path winding number theorem`;
- `"relative periods" "divisor" "chain integrals"`;
- `"Stokes theorem" "cube" differential forms university`;
- `"constant phase" "contour" "boundary" zeros "integral"`;
- `"radial graph" "relative periods" holomorphic`;
- `"constant phase" "divisor" "cell" contour integrals`;
- `"contour deformation" "relative homology" "zeros" phase`.

The relevant direct inputs were the author-hosted notes and
Lawrence-Yamauchi. Relative-period Calabi-Yau/string and rapid-decay
thimble hits, general generating-function contour material, numerical
pages and secondary mirrors were not inspected as theorem inputs.
They establish neither coverage nor novelty for this exact target.
There is no essential inaccessible source remaining for the stated
smooth finite-cell implementation. Broader relative de Rham,
Picard-Lefschetz and stratified-integration theories are not imported.
Full matching Mathlib coverage and supporting formal coverage remain
unchecked; that is not evidence of absence.

### Approved attempt scope and discriminating test

After separate approval, perform one bounded creative test of the
unchanged TARGET. First justify whichever explicit chain comparison
or primitive method is used; then evaluate all four actual full-form
integrals, retaining lifted arc endpoints and any windings. Apply
Stokes only to a displayed smooth comparison and account for every
side face. If boundary preservation in the zero divisor is claimed,
verify it throughout the deformation; endpoint membership alone does
not discharge that premise. A formal ambient primitive or a replacement
by product arcs does not by itself prove the desired equality. State
any additional zero or homotopy assumption explicitly and distinguish
a conditional formula from the original target.

Check equality with the total period only as a consistency check.
The decisive positive evidence is an actual-label phase restriction
not already implied by L879's global line, L881/L882's counts and the
known period identities. If the only justified consequences are those
identities, stop this mechanism with that scoped negative. Failure to
justify an evaluation is an unresolved step, not an exclusion. A
compatible phase restriction is not a stationary-graph realization.
This test could narrow the boundary odd-contact branch toward L868's
sharp threshold; exterior alternatives, existence, compactness, sharp
period control, higher signs and Xi transfer remain independent gaps.

For the mathematical attempt after source-scope approval, nominate
proof_attempt/creative, deep_research/max. The precise obstruction is
that both audited L882 branches remain compatible with divisor counts;
the bounded new test is whether the four full relative cell periods
force an independent actual-label phase relation. Preserve partial
reasoning and require a refined mechanism or new evidence before
repeating an unsuccessful attempt. This is not routine specialization
of Stokes, which is only an imported tool.

## Invocation-start nomination — preserved historical text

The following nomination is retained as evidence of what was uncovered
at invocation start. Its requests for missing source comparison have
been discharged above; it records no mathematical evaluation.

## Purpose and bounded test

The main gap is L030-L032/C032a actual-Xi all-degree mixed positivity.
L882 leaves both boundary branches of the stationary odd-contact mass
gap open. A new phase restriction from relative full-form integrals
could narrow this branch toward L868's sharp threshold. Exterior
alternatives, existence, compactness, sharp period and Xi transfer
remain independent gaps.

The proposed domains use the two angular intervals between a,c in the
first coordinate and those between a,b in the second. This specifies
cells to investigate, not a product graph or a homology calculation.
Retain eta=theta and eta!=theta, additional zeros inside cells or on
edges, original dy1 wedge dy2 orientation and lifted arc windings.
Do not assume constant sign throughout a cell. Do not replace these
cells by finite real-zero boxes whose class equality L846 excludes.

After adequate coverage, seek a justified evaluation giving a new,
nonautomatic common-phase restriction on actual G labels and allowed
windings. Merely restating Q=lambda*s, the sum of the cell integrals,
or compatible integer counts is insufficient. Stop this mechanism
if all justified restrictions reduce to the known phase/period
identities. Any unproved graph deformation or required zero data must
be exposed; formal primitives and numerical alignment are not exclusion.
No evaluation or verdict on this new mechanism is made today.

## Essential review still required

Reuse the named local assessments, then compare the exact target with
literature on relative periods with divisor boundary and stationary
contours. Inspect primary hypotheses and essential proof cases for
each load-bearing Stokes/homotopy or primitive/monodromy claim.
Smooth parameter-chain Stokes may suffice; do not import stratified
or semialgebraic results merely because L846 used them. Check boundary
faces and corners, the pole at zero, retained arc windings and any
homotopy's ambient and boundary conditions.

The narrow local statement checks above are not complete discovery or
evidence of novelty. No cross-notebook input is proposed. Mathlib
coverage is unchecked. No new lemma or mathematical script accompanies
this nomination, and no ready assessment is approved during this audit.

After coverage, the proposed route is proof_attempt/creative. The
precise obstruction is that L882's necessary counts leave both
stationary boundary branches open; the full relative cell integrals
have not been tested for phase compatibility. The bounded test is a
justified four-cell evaluation and a nonredundancy check against those
counts, with a new actual-label constraint as the decisive positive
evidence. This targets the odd-contact mass-gap branch, not a full RH
solution. Until coverage is ready, use
literature_comparison/standard/high.
