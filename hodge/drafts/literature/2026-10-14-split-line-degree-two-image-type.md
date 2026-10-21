# Split-line degree-two ordinary image — source comparison

TARGET: Determine whether generic degree two in L103 forces its reduced analytic image germ Z to be the ordinary A1 surface singularity.
CHECKED: 2026-10-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched finite degree-two analytic extensions, nonnormal multiplicity-two images, holomorphic finite-group linearization, analytic invariant rings, the A1 quotient and analytic cotangent-generation criteria; narrowly compared L103, its saved finite-degree assessment and audit history 278. No inspected theorem states the complete actual-family conclusion.
SOURCE_EVIDENCE: Inspected Conrad's Galois Action on Integral Closures p. 1 before Proposition 1; Takamura (2019) holomorphic averaging construction and Lemma 3.6 pp. 381–382; Riemenschneider Chapter 8 Theorems 8.1/8.4/8.7 and Lemmas 8.3/8.5 pp. 233–235 with essential proof cases; Greuel–Lossen–Shustin (2007) Definition 1.1/Remark 1.1.1(4–5) p. 9, Theorem I.1.16 pp. 23–24 and Theorem I.1.20 p. 27 with proofs; Reid's Du Val notes Sections 1.1–1.2 pp. 2–3; Stacks Section 9.21 Lemma 9.21.2 and Theorem 9.21.7.
COMPARISON: Known inputs cover integral-closure action, analytic realization of ring automorphisms, finite holomorphic linearization, analytic invariant rings, the sign quotient model and surjectivity from a cotangent map. They do not identify the ordinary image A with the invariant ring without an additional argument. L103 retains the actual product functions and their full quadratic span, so a later specialization can test that missing equality without assuming normality.
GAP: Under conditional d=2, verify integral closure in Frac(B), the actual analytic involution and its tangent action, the convergent quotient model, and surjectivity of A into the analytic invariant ring using L103's actual quadratic generators. These are proof obligations, not conclusions of this review.
REASON: Essential primary coverage is now sufficient for one bounded mathematical test of the unchanged target; import the general results and derive only the actual extension/jet specialization. Multiplicity two and equality of fraction fields alone must not be substituted for ordinary-image equality.
SCOPE: Fixed audited L103/L094/L101/L102 setup at unchanged S,I,g,h,k,E; finite analytic A subset B=C{s,t}, m_A B=(s,t)^2, conditional degree two and the actual product first jets. Ordinary reduced analytic image only; no assumed image normality or parameter involution.

## Relevance and discriminating test

The main gap remains universal primitive rational Hodge realization. The
intermediate target is conditional ordinary-image classification, which
could clarify local double identifications before any comparison with a
compatible family or moduli image. Exact degree, quaternionic integration,
a common F, global mixed action, separation, reconstruction and transport
remain independent gaps. No complete candidate argument is present.

Continue the mathematical test only if all actual convergent-ring bridges
can be justified and the image-to-invariant-ring cotangent map is
surjective. If that last test fails, retain the ordinary-image gap and
record the failing generator or a precise nonnormal countertest. Merely
identifying a normalization is below the requested threshold.

## Primary inputs and qualifications

**Integral-closure action.** Brian Conrad, *Galois Action on Integral
Closures*, undated Math 210B author handout, inspected 2026-10-14,
[p. 1, paragraph preceding Proposition 1](https://math.stanford.edu/~conrad/210BPage/handouts/math210b-Galois-IntClosure.pdf).
For a domain A with fraction field K and a normal algebraic field
extension E/K, field automorphisms preserve the integral closure of A
in E, since they preserve integrality over A. That paragraph does not
require A normal. Proposition 1 adds normality of A for transitivity
on primes and is not needed here. A later proof must identify the
actual B as that integral closure; it cannot assume A normal.
The [Stacks Project, Section 9.21](https://stacks.math.columbia.edu/tag/09DU),
Lemma 9.21.2 and Theorem 9.21.7, supplies the finite Galois
automorphism/fixed-field facts. Characteristic zero and degree two
must be checked explicitly; the elementary quadratic-polynomial
specialization is permitted, without reproving general Galois theory.

**Analytic algebra tools.** G.-M. Greuel, C. Lossen and E. Shustin,
*Introduction to Singularities and Deformations*, Springer (2007),
ISBN 978-3-540-28380-5,
[Chapter I, primary textbook PDF](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/greuel.pdf).
Definition 1.1 and Remark 1.1.1(4–5), p. 9, treat C-algebra maps of
analytic algebras and show locality and substitution by convergent
coordinate images; Exercise 1.1.4 p. 19 gives the uniqueness/convergence
proof instructions. This is the analytic bridge for a ring involution.
Theorem I.1.16, pp. 23–24, proves factoriality of convergent power-series
rings using Weierstrass preparation/division; it supports normality of
B, not of A. Theorem I.1.20, p. 27, says an analytic algebra map is
surjective exactly when its cotangent map is surjective, equivalently
its extended maximal ideal is the target maximal ideal. Its proof uses
analytic finiteness and Nakayama. Apply this to the invariant analytic
ring, after verifying that ring and its cotangent generators. Ideal
equality in B is a different statement and is not a direct application.

**Holomorphic linearization.** Shigeru Takamura, *Linearization of
Quotient Families*, J. Math. Sci. Univ. Tokyo 26 (2019), 361–389,
[published PDF, pp. 381–382, Lemma 3.6](https://www.ms.u-tokyo.ac.jp/journal/26-3-3.pdf).
Read the preceding construction and its full equivariance proof: a
finite group of holomorphic transformations fixing zero is conjugated
to its derivative representation by averaging derivative-inverse
composites. The averaged coordinate map has derivative the identity,
so is locally biholomorphic. This local construction needs no proper
submersion. Lemma 3.8 and the larger quotient-family theorem have
additional family hypotheses; they are unnecessary here. A later
proof must first obtain an actual holomorphic finite-order germ and
then determine its derivative from the retained invariant jets. A
formal or meromorphic involution alone does not meet these hypotheses.

**Analytic invariant ring.** Oswald Riemenschneider, author lecture-book
Chapter 8, *Quotient singularities: General theory*, undated online
version inspected 2026-10-14,
[Chapter PDF](https://www.math.uni-hamburg.de/home/riemenschneider/bookchap08.pdf).
Theorem 8.1 p. 233 gives the quotient of a reduced complex analytic
space under a properly discontinuous group, with local ring the
stabilizer invariants. Finite groups satisfy the action hypothesis.
Theorem 8.4 p. 234 makes finite-group invariant rings analytic and the
inclusion finite. Read Lemma 8.5's adic-closedness proof, the monic
orbit-polynomial argument and Theorem 8.7's complete finiteness and
analytic-generation proof pp. 234–235. Lemma 8.3 p. 234 proves
normality of invariants of a normal analytic algebra. These results
concern the actual invariant ring; they do not identify a separately
given image subring A with it. No weak-normalization replacement is
licensed. General quotient construction is imported, not reproved.

**Standard A1 model.** Miles Reid, *The Du Val singularities A_n, D_n,
E_6, E_7, E_8*, undated author notes, online version inspected
2026-10-14,
[Sections 1.1–1.2, pp. 2–3](https://mreid.warwick.ac.uk/surf/more/DuVal.pdf).
Section 1.2 explicitly identifies the quotient of the plane by
(u,v) mapped to (-u,-v) with xz=y^2 via the quadratic invariant
coordinates u^2,uv,v^2; Section 1.1 names this the ordinary A1 point.
The displayed computation is algebraic. Its use for convergent germs
must retain analytic invariant-ring coverage above and justify the
convergent coordinate presentation, rather than treating polynomial
invariant generation as analytic surjectivity. Any short convergence
check is a necessary specialization, not a reproof of ADE classification.

## Exact remaining specialization and obstruction comparison

The audited L103 proof supplies more than numerical multiplicity two:
its actual products P_i Q_j, both coordinate-pair Jacobians, and the
stated first jets. A mathematical turn may use these established data
when testing the tangent action and the map on quotient cotangent
spaces. This review does not calculate either map or prove its rank.

The essential distinction is A versus the analytic invariant ring R.
A finite birational map from a normal space does not by itself prove
that the original image is normal. Even knowing an A1 normalization
would leave this equality unresolved. The inspected epimorphism theorem
provides an independent generator test for equality; its hypothesis
must be proved using the actual functions and all higher coefficients.
A finite-group quotient theorem whose target is already assumed normal,
or a multiplicity-two classification with missing normality hypotheses,
is therefore not a direct import for this target.

Prior global Hom and tangent-coincidence stops and the split quadratic
obstruction stop remain at their original scopes. History 278 and L103's
complete audit explicitly leave the involution and image structure open;
no duplicate completed image-classification theorem was found in the
scoped local comparison. A historical stop is not invoked as a ban.

Queries included `finite analytic map degree two smooth surface germ
nonnormal image multiplicity two quotient involution`, `finite group
action holomorphic germ linearization averaging proof pdf quotient
singularities`, `analytic algebras generators maximal ideal surjective`,
`normalization multiplicity two surface singularity nonnormal`, and
`M Reid Du Val singularities A1 quotient pdf warwick`. Search snippets
were discovery only. General multiplicity-two and global degree-two
surface leads did not supply an inspected exact statement. Cartan's
original paper/Manetti's formulation and Prill/Denneberg–Riemenschneider
quotient characterizations remain unread leads and are not dependencies.
The previously approved finite-germ/multiplicity assessment is reused;
a failed fresh Springer back-matter request does not block this target
because the newly needed analytic criterion is inspected in the textbook.
No novelty inference follows from the bounded search.

## Turn boundary and continuation inputs

This literature turn imports source coverage only. It derives no new
lemma, counterexample, involution, normality or A1-image conclusion, and
changes no lemma or mathematical script. The next mathematical attempt
should be REPRODUCTION under SPECIALIZE. The general statements above
are known; no exact matching theorem for the complete L103 specialization
was inspected. Full matching Mathlib coverage is **not checked**; unknown
coverage is not evidence of absence.

Essential inputs: audited L103 and its audited L094/L101/L102 setup.
Degree two is an additional conditional hypothesis, not an existence or
universality statement. No F, nonempty global reducible locus, W=r(TB),
smooth central unitary gauge, quaternionic family, prescribed global
mixed tensor, weakly normal/algebraic coarse identification, separation,
reconstruction or transport is assumed. All such gaps remain unresolved.
