# Quartic branch field structure — assessed exact-instance continuation

TARGET: Identify the quartic branch field of L110 up to Q-isomorphism and test for an explicit quadratic tower usable in a certified two-descent.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Scoped pair-assessment/failure search found no prior quartic-field/tower calculation; exact coefficient queries found no inspected instance match; standard quartic resolvent/subfield searches led to Conrad's primary notes, whose theorem statements and essential proof cases were read.
SOURCE_EVIDENCE: Conrad, Galois Groups of Cubics and Quartics (Not in Characteristic 2), Definition 3.1, Theorem 3.6, Corollary 3.8 and Theorem 4.1 proof, pp.6–12; Galois Groups of Cubics and Quartics in All Characteristics, Theorem 4.1 and proof p.18 and subfield obstruction argument p.19; both author-hosted versions accessed 2026-10-25. Reuse the existing Stoll descent comparison.
COMPARISON: Standard resolvent theory and Galois correspondence cover the subfield decision and pair-coefficient construction; only the exact quartic's factorization, embedded generators, inverse maps and practical coefficient improvement remain to reproduce. No general new theorem or instance identification was located in the inspected sources.
GAP: No instance resolvent, quadratic subfield, relative equation or simpler defining polynomial has been calculated. Source theory alone supplies no class/unit completeness, Selmer bound, rank bound or rational-point classification.
REASON: The source gap is closed for a bounded exact rational-algebra specialization; this can test a concrete descent-arithmetic simplification without reopening the parked backend route. No general-theory reproof is needed.
SCOPE: The stated quartic over Q, using L110's exact coefficients and L132's irreducibility; complete cubic rational-root testing, pair-sum/product quadratic construction, coefficient comparison and inverse field-map certification, including zero discriminant and split-resolvent cases; no class/unit, Selmer or rank calculation.
LITERATURE_REASON: The saved REVIEW_REQUIRED continuation introduced quartic field-isomorphism and quadratic-subfield hypotheses outside the existing Stoll rank assessment; this turn supplies that missing primary comparison.

Use L110's exact model and L132's quartic irreducibility. The field is
Q[theta]/(7+52theta−6theta²−64theta³−25theta⁴). A proposed simpler field
must have explicit inverse Q-field maps, not merely matching numerical
roots or discriminants. A quadratic tower must identify its subfield
and relative equation exactly. Continue toward descent arithmetic only
if this produces a concrete simplification and a certifiable bounded
next computation; otherwise park the simplification without claiming
that two-descent itself fails. No backend-availability reprobe, generic
class-group implementation or rank calculation is approved here.

The old rank-bound assessment remains at
`2026-10-20-pair-jacobian-rank-bound.md`; its execution stop is preserved.
The bounded lower-detector failure ATTEMPTS/050 and cover-degree stops
ATTEMPTS/056–057 remain. All rank, point, marked-lift and integer-recovery
obligations are independent unresolved assumptions. Full matching Mathlib
coverage has not been checked; this is not evidence of absence.

## Primary comparison and hypotheses

[Keith Conrad, Galois Groups of Cubics and Quartics (Not in
Characteristic 2)](https://kconrad.math.uconn.edu/blurbs/galoistheory/cubicquartic.pdf),
author-hosted 18-page version (no revision date identified), Definition
3.1 and equation (3.7), p.6, give for an irreducible monic quartic
X^4+aX^3+bX^2+cX+d over a field of characteristic different from two
the resolvent R=X^3−bX^2+(ac−4d)X−(a^2 d+c^2−4bd).
Theorem 3.6, pp.7–8, separates irreducible-resolvent groups S4/A4
from reducible-resolvent groups D4/C4/V4. Corollary 3.8, p.9,
distinguishes one from three rational resolvent roots. Theorem 4.1's
proof, pp.10–12, constructs the unique quadratic subfield in the
D4/C4 cases using pair sums/products: their equations are
X^2+aX+(b−r) and X^2−rX+d. At least one generates that subfield;
the proof explicitly retains a rational pair sum or product with zero
discriminant. Do not substitute the splitting field's discriminant
quadratic field for the embedded quadratic field in the D4 case.

[Conrad, Galois Groups of Cubics and Quartics in All
Characteristics](https://kconrad.math.uconn.edu/blurbs/galoistheory/cubicquarticallchar.pdf),
author-hosted 21-page version (no revision date identified), Theorem
4.1 and both proof directions, p.18, characterize a quartic field
with a quadratic subfield by an even quartic primitive generator.
The p.19 subgroup argument distinguishes a quadratic subfield of the
quartic field from one merely in its normal closure: A4 has no index-two
subgroup; an S4 point stabilizer S3 is not contained in A4. These are
standard Galois-correspondence inputs. The V4 case is not subject to
the uniqueness assertion in the other notes' D4/C4 construction;
retain all three rational resolvent roots and certify each proposed map.

Applicability requires monic normalization of Q4, not a monic-input
assumption about its displayed integer coefficients. L132 supplies
irreducibility; characteristic zero supplies separability. All generic
theory is imported. Exact coefficient comparison and map verification
are needed because the sources do not identify this instance. The
existing `2026-10-20-pair-jacobian-rank-bound.md` supplies the Stoll
comparison and limitations: easier field coordinates alone are not
complete two-descent.

## Search and access evidence

External queries included `"7+52" "-64" "-25" quartic field`,
`"25*x^4" "64*x^3" "52*x" field`, `Keith Conrad quartic fields
cubic resolvent quadratic subfield`, and `quartic quadratic subfield
resolvent theorem pdf`. No inspected theorem identifies this exact
field; this is not a novelty claim. Local searches covered the pair
assessments, ATTEMPTS/050, /056–057 and the earlier narrow rank script
search. No sibling notebook was read.

PARI's indexed official entries suggest `polredbest(T,1)`, `modreverse`
and `nfsubfields`, but full HTML fetches and selected manual-page
retrieval failed repeatedly. The official 2.13.3 manual opening pages
were accessible, not its required function passages. Therefore those
entries remain leads, not essential approved implementation coverage.
Awtrey–Beuerle–Keenan, DOI 10.12732/ijpam.v112i4.5, is another unread
algorithm lead (author PDF failed); Kani's old PDF URL redirected to a
homepage. Neither supplies an imported theorem here. Stop access
retries: the inspected Conrad theory permits the elementary exact test
without these sources or software availability probes.

## Bounded next calculation and decision test

This is approval for the saved target next turn, not a calculation in
this literature turn. Use ordinary exact rational polynomial arithmetic.

1. Normalize Q4 to a monic rational polynomial, form the cited resolvent,
   and exhaust its rational roots using the rational-root theorem after
   primitive integer normalization. Handle a zero constant separately.
   Save full factorization/root-exhaustion evidence, not a numeric root
   preview. An irreducible cubic gives the standard no-subfield branch.
2. For rational resolvent roots, use both cited pair-coefficient equations
   and exact quartic coefficient comparison to construct candidate
   quadratic fields and relative quadratic factors. Retain zero
   discriminants and all roots in the V4 case; a degenerate formula is
   not a negative result. No unsupported uniqueness assertion is allowed.
3. For every claimed tower give its embedded quadratic generator in
   Q[theta]/(Q4), its irreducible quadratic equation, a relative quadratic
   equation for theta, and inverse Q-algebra maps. Verify substitutions,
   the full four-dimensional basis determinant and both map compositions
   exactly. A proposed simpler absolute polynomial also needs these
   certificates; equal discriminants or approximate roots do not suffice.
   A generator obtained by completing a square need not remain primitive,
   especially in the V4 case: verify degree four rather than assuming it.
   An elementary construction not completed is an unfinished case, not
   evidence that no tower exists.
4. Compare coefficient sizes with the original primitive integer
   quartic's height 64. A practical positive test is a strictly smaller
   primitive integral absolute defining height, or a certified quadratic
   tower whose squarefree subfield radicand and reduced relative-equation
   rational numerators/denominators all have absolute value below 64 in
   the basis (1,sqrt(d)). State the normalization and actual values.
   This is an operational simplification test, not a theorem that descent
   will succeed. Preserve any exact tower that misses it, but park its
   claimed practical advantage absent another concrete certified saving.

Bounds fixed before execution: at most three resolvent-root branches,
six relative-factor candidates, 250000 rational-root trials, 500000
charged exact scalar operations, degree at most eight and integer
numerator/denominator bit length at most 4096. Count divisor generation
and rejected candidates; a cap hit is incomplete evidence. Save full
certificate and ledger plus an independent exact replay of load-bearing
identities; print only results, actual/required bounds, failures and paths.
No external CAS, backend reprobe, generic class-group implementation,
class/unit completeness or rank calculation is required or approved.

Continue only if the explicit maps and relative equation yield the
stated practical simplification; otherwise park this simplification.
A certified no-quadratic-subfield result is informative negative
evidence. A bounded unsuccessful construction is only exploration.
Neither outcome excludes two-descent itself. Any later arithmetic target
outside this scope requires its own assessment.
