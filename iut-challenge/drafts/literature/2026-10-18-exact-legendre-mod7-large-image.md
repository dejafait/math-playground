# Exact auxiliary Legendre field — mod-seven image source comparison

TARGET: Determine whether the full mod-7 image of L078's unchanged E_L over G contains SL_2(F_7), using the auxiliary full image and the intermediate field F'=F_aux(s).
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step326 searched the local 2026-10-11/17/18 mod-7, SL_2 and quadratic-restriction assessments and histories 151–154; compared L047, L073, L077, L078 and ATTEMPTS/034. External searches for elliptic mod-l image containment under quadratic restriction and the cited Milne/Conrad theorem names found no exact combined instance used here; primary coverage below suffices and no novelty is inferred.
SOURCE_EVIDENCE: Reused the ready 2026-10-11 restriction/generation and 2026-10-18 pointed-coordinate assessments; freshly inspected Milne FT v5.10 (September 2022), Theorems 3.10, 3.17(b,d), Propositions 3.19, 3.21 and 7.4, pp.37–41,95; Conrad Simplicity of PSLn(F), undated nine-page version retrieved 2026-10-18, Theorem 3.3/proof p.4; Milne EC second edition (2021), II Proposition 1.5/proof and 1.6 p.49, II Theorem 2.4(b) pp.52–53.
COMPARISON: Known finite-Galois restriction and elementary generation cover two successive restriction stages, with pointed full-torsion transport over F' and subgroup inclusion from G into F'. L047 is method context only. Its original-curve conclusion cannot be imported for E_L/G; this exact application remains to be written. A global quadratic-twist formula or normality of F'/Q or G/Q is unnecessary for the proposed method.
GAP: Coverage is ready, but no SL_2 containment for the auxiliary restriction or E_L/G is established this turn. A separate mathematical application must verify each finite image, each normal quotient and its index, both-coordinate equivariance and the direction of the final field/subgroup inclusion.
REASON: The saved target's changed field/curve scope has now received its separate source comparison. Proceed to its known-method specialization, preserving all exact choices and independent gaps.
SCOPE: Exactly TARGET for unchanged L073, L077 D,s,t,iota,F' and L078 G in the same algebraic closure and embedding; full two-dimensional mod-7 representations with transported bases. No full GL_2 claim over G, global normality conclusion, normal-closure replacement, new curve or sufficient initial data.

LITERATURE_REASON: Invocation-start REVIEW_REQUIRED changes both the curve and the final base field from L047; its previous coverage did not explicitly assess the additional quadratic restriction and pointed transport. This comparison completes that missing scope rather than repeating an approved application.

## Inspected primary inputs and reuse — step326

[Milne, *Fields and Galois Theory*, v5.10 (September 2022)](https://www.jmilne.org/math/CourseNotes/FT.pdf),
Theorem 3.10, pp.37–38, equates finite Galois extensions with separable
splitting fields. Theorem 3.17(b,d), pp.39–40, gives index/degree and
normality/quotient correspondence. Proposition 3.19, pp.40–41, assumes
one Galois extension in a common field; compositum restriction is an
isomorphism onto the intersection-fixing group. Proposition 3.21,
pp.41–42, treats two Galois extensions over the same base. Proposition
7.4, p.95, extends embeddings inside a Galois extension to automorphisms.
Read the splitting-field equivalence, both normality directions,
restriction injectivity/surjectivity, intersection-normality proof and
embedding-extension/surjectivity argument. These cover finite images
obtained from the absolute group. Reuse the previously inspected
remaining compositum cases; no new general Galois theorem is needed.

[Conrad, *Simplicity of PSLn(F)*](https://kconrad.math.uconn.edu/blurbs/grouptheory/PSLnsimple.pdf),
Theorem 3.3, p.4, applies to every field and generates SL_2 by upper
and lower elementary unipotents. Rechecked the conjugation and all
three factorization cases: nonzero upper entry, nonzero lower entry,
and diagonal matrices. Import generation without reproof. The next
application must check generator orders and apply Lagrange in each
actual normal quotient. No perfectness, simplicity or classification
theorem is required. The previously assessed method is reusable at
each base separately; it is not restricted to a base named Q.

[Milne, *Elliptic Curves*, second edition (2021)](https://www.jmilne.org/math/Books/EC2.pdf),
II Theorem 2.4(b), pp.52–53, covers invertible pointed Weierstrass
changes over an arbitrary field. II Proposition 1.5 and 1.6, p.49,
give group-law compatibility for nonconstant origin-preserving maps,
including over extension fields. Read the Picard-group proof and
the resulting commuting group-law diagram. These supplement the
ready L077/L078 coordinate assessments. Their full pointed maps and
inverses are already canonical. Applying them on full seven-torsion
and checking equivariance over F' remain specialization obligations.
No twist classification is needed when using this actual isomorphism
over its field of definition.

## Exact scope and obligations for the later mathematical attempt

L073 supplies this same auxiliary curve's full Q-image, and explicitly
states that F_aux/Q is Galois with degree dividing 2^14*3^3*5.
Its retention proof and separate audit were read at the relevant
degree, full-image and same-witness passages. L047's hypotheses name
another curve, so use its known method, not its literal conclusion.
First apply the finite Galois inputs to the auxiliary full coordinate
field over Q and F_aux; check the intersection, actual image equality,
normality and degree divisibility before using elementary generation.

The second restriction has base F_aux, not Q. L077 gives the actual
nonzero D in F_aux and F'=F_aux(s), s^2=D. The later proof must check
the separable splitting-field hypothesis and degree at most two for
this extension. Apply the same restriction/index inputs over F_aux
to its full seven-division field and F', and verify the normal
image quotient and its order before invoking the generator test.
Both stages are applications left to that turn. This review does
not assert their image conclusions or assume that normality is
transitive in a tower.

Then retain L077's exact pointed map and inverse, with coefficients
in F'. Check their action on every geometric seven-torsion point,
including the origin, and G_(F')-equivariance on both coordinates.
Transport the torsion basis through this map. Finally use L078's
actual G subset F' for the same E_L; check the absolute-subgroup
inclusion in the correct direction and basis independence of the
determinant-one containment. Do not assert that the pointed map is
defined over G or that G=F'. No comparison of mere abstract image
orders or x-coordinate fields suffices.

The target is therefore SPECIALIZE, with a later research
classification of REPRODUCTION. The sources cover the necessary
general mechanisms; only their explicit exact-field application is
authorized, not a new general lemma proved during this review.
Full matching and supporting Mathlib coverage is not checked;
unknown coverage is not absence and is not a blocker here.

## Relevance, duplicate/failure screen and continuation test

The main gap remains original finite B>=A. Actual SL_2 containment
would supply one independent initial-data prerequisite for the
exactly generated auxiliary field. It would leave G/Q normality,
mixed radical/15-torsion information, other initial data, native
input/action, all-image factorization, pilot transport and essentiality
unresolved. Do not infer a complete IUT instance or an IUT flaw.

The scoped duplicate search finds L047's different-curve result,
not this combined application. The external image search returned
general image-computation, quadratic-twist and open-image leads;
their theorem texts were not inspected or imported. They are unused
leads, not evidence of novelty or of stronger applicable coverage.
Queries were `elliptic curve mod l Galois image contains SL2 quadratic
extension restriction`, `site.jmilne.org Fields Galois Theory "3.19"
"3.17"`, and `site.kconrad.math.uconn.edu PSLnsimple "Theorem 3.3"`.

ATTEMPTS/034 stops a separator made from powers of the recorded
89-Frobenius. This target uses the full auxiliary mod-seven image,
not that cyclic subgroup, and makes no normality verdict. The other
recorded packet, exact-curve and marked-pilot stops remain intact.
No cross-notebook input is used and no mathematical exploration
attempt is spent by this source comparison.

Continue with exactly TARGET if the later proof checks both
restriction stages and the full pointed transport. If a required
normal quotient, index divisibility or field-of-definition condition
fails, isolate the failed obligation and stop this mechanism rather
than silently passing to a normal closure or changing the witness.
No source blocker remains; no containment verdict is recorded here.

## Invocation-start proposal retained for provenance — step325

The following paragraphs record the original unapproved proposal.
Their future-tense routing describes step325's checkpoint; the
step326 SPECIALIZE assessment above supersedes that coverage status.

This is a proposed continuation only. Step325 performs the separate
L082 audit and does not derive or approve this target. The next turn
must be literature-only until its essential coverage is ready, reusing
adequate existing primary assessments before any new retrieval.

The main gap remains finite B>=A. The proposed intermediate containment
would test another initial-data prerequisite independently of the
normality and stable-reduction questions. Essential inputs for that
future application are L073 (the same auxiliary curve and full global
image), L077 (the actual F' and pointed comparison) and L078 (the exact
G and retained packet). L047 is method context for restriction of
representations, not a theorem about this E_L/G. Read only the needed
proof sections and prior source assessments when comparing coverage.

Three continuation choices were considered at the level of recorded
obligations: further pointed-model checks now duplicate the completed
L082 audit; the normality-ratio route still lacks mixed-kernel data and
additional powers of the recorded Frobenius remain stopped by
ATTEMPTS/034; the full mod-7 restriction question has an independently
testable threshold and existing global-image and coordinate inputs.
This selects the third without claiming a new normality mechanism or
spending a mathematical exploration attempt on it.

The discriminating test is actual SL_2(F_7) containment over the exact
G, with both coordinates and the same curve choices. Coverage must
justify any restriction through F_aux and F' and the pointed transport
to E_L, accounting for possible nonnormality of F'/Q and G/Q. Continue
only with a complete applicable theorem chain; if a needed image or
field hypothesis is unavailable, record it rather than replacing G
by a normal closure or changing the witness. No such chain is proved
in this proposal and no surjectivity over G is assumed.

G/Q normality, the mixed radical/15-torsion kernel, other initial data,
retained radical memberships/scalar occurrence, actual native input/
action, marked all-image factorization, pilot transport, essentiality
and finite B>=A remain unresolved even if this future target passes.
The two witnesses and ATTEMPTS/027,028,031,032,033,034 stay intact.
Full matching and supporting Mathlib coverage is not checked.
