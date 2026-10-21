# Marked elliptic quotient — rank-zero source assessment

TARGET: Determine whether L111's elliptic quotient has Mordell–Weil rank zero over Q.
CHECKED: 2026-10-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched exact coefficient strings, quartic-to-Weierstrass/Jacobian identification, certified elliptic rank and torsion tests; compared L111, the prior pair-Jacobian rank assessment and ATTEMPTS/050. No exact-instance rank theorem was identified in the sources inspected; this is not a novelty claim.
SOURCE_EVIDENCE: Inspected Fisher (2022), Sections 1–2, equations (1)–(2); Milne (2006), Chapter I Proposition 4.10 and its rational-field descent passage, Chapter II Section 5 through Corollary 5.7; Cremona corrected online second edition, Chapter III Sections 3.1/3.3 and Section 3.6 equations (3.6.4)–(3.6.8); PARI stable manual ellfromeqn and complete ellrank technical explanation, accessed 2026-10-21.
COMPARISON: Standard binary-quartic theory identifies the exact Q-Jacobian, and the rational origin identifies its rank with L111's rank. Known torsion tests permit an exact positive-rank witness independently of a descent backend; complete algebraic descent can certify rank zero but is not supplied by a point search. No instance-specific rank is imported or computed.
GAP: Evaluate and verify the exact model and determine a rank certificate; if the bounded positive-witness test fails, rank remains unknown because executable complete descent is unavailable. Marked lifts, degree-nine recovery, remaining factors, both L095 integer systems and minus-eleven remain independent gaps.
REASON: Essential source coverage is now adequate for one bounded mathematical rank test using imported formulas and exact torsion bounds. Software-dependent full descent remains parked; absence of a backend does not block the independent positive-witness test.
LITERATURE_REASON: The saved rank target was REVIEW_REQUIRED and lay outside construction/audit coverage; this turn supplies its previously missing model and rank-certification comparison, rather than refreshing a ready assessment.
SCOPE: Exactly TARGET for audited L109/L110/L111 over Q: known Jacobian formulas, rational-origin rank identification, exact model scaling, covariant point images, bounded rational-point search and certified non-torsion tests. No new descent algorithm, larger genus-two search, rational-point completeness or integer elimination is approved.

## Gap, intermediate target and discriminating test

The main gap is positive primitive integer exclusion for residual Beal
signatures. The intermediate target is the rank of the smooth proper curve

    R²=825T⁴+2112T³+198T²−1716T−231,  O_E=(2,165).

Use audited L111 with L109/L110, preserving the exact minus-three
marking h²=3(4−T²). Rank zero could support a later complete torsion and
marked-lifting analysis. An exact positive-rank witness stops that finite
elliptic-point-list route. Neither alternative by itself settles root
recovery, complementary factors or either integer system. No rank value,
new invariant evaluation, Weierstrass coefficient or point is derived in
this literature-only turn.

## Inspected primary results and applicability

Tom Fisher, *On binary quartics and the Cassels–Tate pairing*, Research
in Number Theory **8** (2022), article 74,
[DOI 10.1007/s40993-022-00376-z](https://doi.org/10.1007/s40993-022-00376-z),
[author manuscript/publication PDF](https://api.repository.cam.ac.uk/server/api/core/bitstreams/f35e7d09-f88e-4058-959d-b8153d7708cf/content),
Section 2, p.2, equations (1)–(2): for the nonsingular binary quartic
ax⁴+bx³z+cx²z²+dxz³+ez⁴, use

    I=12ae−3bd+c²,
    J=72ace−27ad²−27b²e+9bcd−2c³.

Its Jacobian has model Y²=X³−27IX−27J. Section 1, p.1, states the
Selmer exact sequence and explains the unconditional rank upper bound;
nontrivial Sha can prevent sharpness. Apply over Q to the actual L111
coefficients, whose squarefreeness is already audited. Keep the full
constant −33: matching j-invariants alone does not identify a Q-twist.
No Selmer completeness or Sha vanishing is assumed here.

J.S. Milne, *Elliptic Curves*, BookSurge, 2006,
[author's text](https://www.jmilne.org/math/Books/ectext6.pdf), Chapter I,
Proposition 4.10, p.35, and the rational-field descent discussion p.38:
a genus-one smooth proper curve with rational O identifies with its
Picard group by P ↦ [P]−[O]. The proof uses Riemann–Roch and retains
Galois descent. L111 supplies O over Q, so the Jacobian rank is the
requested rank, with no twist ambiguity. Chapter II, Corollary 5.7,
p.66, supplies injectivity of rational torsion under reduction at a good
odd prime. Check nonsingularity of the chosen integral model modulo
each prime before applying it. Thus complete finite-field counts can
bound rational torsion; no finite-point search is a rank upper bound.

J.E. Cremona, *Algorithms for Modular Elliptic Curves*, second edition,
CUP 1997, corrected online edition,
[Chapter III](https://johncremona.github.io/book/fulltext/chapter3.pdf):
Section 3.1, pp.62–63, gives rational model changes with nonzero scaling.
Section 3.3, Proposition 3.3.1, p.69, gives integral coordinates for
torsion on a nonsingular integral monic cubic model, without requiring
minimality. Hence a nonintegral exact multiple certifies infinite order.
Section 3.6, pp.89–90, equations (3.6.4)–(3.6.8), gives both quartic
covariants, their syzygy and the degree-four map to the Jacobian. These
can supply exact images of known quartic points. That map is a
2-covering, not an inverse birational transformation. Any point used
must satisfy the exact cubic; verify any model scaling by substitution.
These standard results need no reproof; instance arithmetic and checks
are the necessary specialization.

[PARI stable manual, Elliptic curves](https://pari.math.u-bordeaux.fr/dochtml/html-stable/Elliptic_curves.html),
entries `ellfromeqn` and `ellrank`, accessed 2026-10-21: the former
returns Jacobian coefficients and can return a point image; it does not
promise inverse maps. The latter returns [r1,r2,s,L], with unconditional
rank interval and independent non-torsion points. Its technical passage
states the unconditional computation of Selmer dimension C, two-torsion
dimension T and pairing correction s, giving r2=C−T−s. Four-torsion in
Sha can leave the interval unresolved. The manual's subsequent analytic
example explicitly assumes BSD and is not an unconditional certificate.
Record the installed version, complete output and proof settings for
any eventual run. None is claimed here.

## Bounded next mathematical attempt

The approved immediate execution needs only exact rational arithmetic:

1. Evaluate Fisher's invariants on the exact quartic, verify a nonzero
   discriminant, and retain the original integral Jacobian model.
   Any simpler short model must have an explicit rational scaling
   verified in both directions. Minimality is unnecessary.
2. Use Cremona's covariant map on the two already known points
   (2,±165), verifying the syzygy and cubic equation. Test these images
   first. If needed, search a fixed finite box on a recorded integral
   short model: X=m/n² with |m|<=4096, 1<=n<=64, gcd(m,n)=1.
   Use integer square tests, retaining both Y signs and O. These caps
   are a diagnostic attempt, not a height bound or a point-completeness
   claim. Stop the search once a positive-rank certificate is obtained.
3. Certify any witness by exact nonintegrality of a nonzero multiple
   (test at most the first sixteen multiples), or by [d]P!=O where d is
   the gcd of complete point counts at two good odd primes <=101.
   Milne's injection makes every rational torsion order divide d.
   Exact group arithmetic, on-curve identities and all failures belong
   in a full certificate on disk, with concise printed results and paths.
4. A certified witness answers TARGET negatively and parks the finite
   elliptic-point-list route. If no witness is certified within these
   caps, report the rank question unresolved; do not infer rank zero or
   enlarge the caps automatically. Complete descent remains a distinct
   execution prerequisite, not permission to repeat backend probing.

This contract is a test specification, not a performed calculation or a
new lemma. A genuine rank-zero result still needs an unconditional
algebraic upper bound of zero with complete arithmetic certification.
No analytic estimate, conditional class computation or empty search
substitutes for it. A future exact-curve database lead would require
inspection and applicability checking before importing its rank claim.

## Duplicates, failures, access and coverage limits

The prior genus-two assessment already parked unavailable full descent.
ATTEMPTS/050 exhausted its particular point/divisor boxes; neither that
failure nor its numerical caps concern this exact elliptic witness test.
The different degree-twelve number-field descent obstruction L069 is
not a rank bound for this Q-elliptic curve. Preserve all these records
and unfinished L108. No cross-notebook theorem is used.

Queries included `"825" "2112" "1716" elliptic quartic rank`, standard
PARI/Magma certified-rank variants, quartic rational-point conversion,
Cremona torsion and Milne good-reduction torsion. Primary passages above
were read, rather than relying on search summaries. Fisher's 6/12-descent
paper, Proposition 5.1(i)–(iii), independently confirms the distinction
between a Jacobian model and a 2-covering; its higher-descent algorithms
are not proposed. Washington's Theorem 2.17 appeared in search results,
but the attempted PDF open returned 404, so its full theorem/inverse
formulas were not inspected and are not an input. The inspected Fisher
and Cremona alternatives make that access failure nonessential.

No gp/sage/magma/pari executable was found in PATH or the specifically
checked local/Homebrew locations; Python cypari2, sageall and sympy are
absent. No install or remote computation was performed. The approved
bounded witness test does not depend on these backends. Mathlib coverage
of the full target and supporting rank/conversion results is not checked.
