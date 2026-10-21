# Changed split-Tate local packet — completed source comparison

TARGET: Assess the full torsion field N=H(E_q[7]) for the split Tate curve with H=Q_3(zeta_60) and q=3^30, including rational 30-torsion over H and the ramification/residue degrees of N/Q_3.
CHECKED: 2026-10-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the Tate-inertia, rational-torsion and cyclotomic assessments; checked ATTEMPTS/022,025,026 and exact local occurrences of zeta_60 and 3^30; searched full Tate torsion fields, all-characteristic-zero torsion, local cyclotomic extensions and the exact packet. Inspected theorem statements and relevant proof discussions; no novelty inference from unsuccessful exact searches.
SOURCE_EVIDENCE: Kedlaya, fall-2004 18.727 author handout Introduction: the Tate curve (notes index: amended 16 Sep), Theorem 1 and proof discussion pp.2–4, Theorem 2 p.4, https://kskedlaya.org/18.727/tate-curve.pdf; Milne EC2 (2021) III.3 pp.102–103 (24)–(26); Milne ANT v3.08 (2020-07-19), Proposition 7.50 with complete proof, Corollaries 7.51–7.52, Example 7.54, Proposition 7.55 with both proof directions, pp.127–130; reuse inspected ANT 7.38,7.42–7.43 and EC2 II.6.3, and Dupuy–Hilado arXiv:2004.13228v1 section 3.2, Definition 5.3.1/Remark 5.3.2, Lemma 5.4.1.
COMPARISON: Named Tate uniformization covers full torsion without requiring the torsion order to be prime to residue characteristic; local unramified correspondence, root lifting and valuation/degree bounds cover the cyclotomic and radical stages. No source directly tabulates this packet; its coordinate-field equality and exact degrees require a separate elementary specialization.
GAP: Compute the entire coordinate field and both local degrees, and test full rational 30-torsion, using the covered inputs; these are not established by this literature turn. Global realization, native input/action, marked pilot transport and essentiality remain independent gaps.
REASON: Essential source coverage is ready for the unchanged local target. Import Tate and local-field theory, then justify this finite packet; rebuilding uniformization or repeating stopped auxiliary radii is unnecessary.
SCOPE: Exactly TARGET as one later known-method calculation, with zeta_60 primitive in a fixed algebraic closure of Q_3, q=3^30 and E_q the standard split Tate curve. Permits full-torsion kernel comparison, cyclotomic residue degrees and radical valuation/degree tests only. No global F, field-of-moduli degree condition, selected native packet, logarithm/action calculation or tensor-component realization is assumed.

LITERATURE_REASON: The changed packet requires essential all-torsion coverage, including n=30 divisible by residue characteristic, and cyclotomic/radical compositum coverage outside the earlier necessary-inertia screen. Unchanged source assessments are reused.

## Preserved proposal (source-status claims superseded below)

Main gap remains original finite B>=A. A local packet constructed from
an elliptic curve, with full torsion tracked before logarithm or orbit
work, could provide a more relevant input for a later applicability
test. It would still leave global initial data, actual/native input
and action, marked pilot transport and essentiality unresolved.

Essential local input is audited L041, as a necessary-screen reference,
not as a theorem applicable without its global hypotheses. Retain its
distinction between normalized integer order and absolute valuation.
ATTEMPTS/022,025,026 exclude different exact fields; this proposal does
not reopen them or recompute their auxiliary radii.

The next review should reuse inspected Tate and local-field coverage
where it matches, and inspect primary statements for full torsion
coordinates, cyclotomic ramification/residue degree and any required
Kummer irreducibility or compositum step. Check duplicates and known
obstructions under this exact local target. Do not substitute a cyclic
subgroup field for N or assume coprime ramification gives linear
disjointness without an applicable theorem. No originality claim is
intended; import known results and justify only their specialization.

Continue to a separate mathematical turn only with adequate coverage
for computing the entire N and checking rational full 30-torsion over
H. A failure of a local prerequisite is informative and should stop
this packet; passing is local compatibility only. Essential inaccessible
coverage parks dependent work. Full matching Mathlib coverage is not
checked. No mathematics for this new target is derived here.

## Preserved interim source-review checkpoint (completed below)

The exact proposed target is unchanged. The earlier Tate-inertia
assessment and ATTEMPTS/022,025,026 have been checked for overlap:
they do not compute this curve-defined field. Reuse the Dupuy–Hilado
v1 field-role and full-30-torsion prerequisites and L041's necessary
screen; no global hypothesis is imported into the proposed local data.

Milne ANT v3.08 Proposition 7.50 with its full proof, Corollaries
7.51–7.52, Example 7.54, and Proposition 7.55 with both proof directions
have now been inspected in the author PDF, printed pp.127–130.
They cover unramified/residue-field correspondence and Eisenstein
total ramification over complete discretely valued perfect fields
with perfect residue field. Finite p-adic fields meet that scope.
Milne EC2 III.3 pp.102–103 also explicitly allows every finite
extension of Q_p for a parameter q in Q_p. Kedlaya's Theorem 1.1
explicitly states Galois equivariance; the remaining proof discussion
and original author-hosted version are being checked. No packet degree,
torsion-field equality or rational-torsion verdict has been derived.

## Completed comparison and bounded mathematical continuation

The main gap is original finite B>=A. The intermediate target is this
curve-defined local packet, with the entire torsion field determined
before any auxiliary shell or radius work. Its possible downstream
use is a local-prerequisite screen for a later global applicability
test. It supplies no global initial theta data or original-IUT verdict.

### Tate input and its scope

[Kedlaya's author handout](https://kskedlaya.org/18.727/tate-curve.pdf),
fall 2004, Theorem 1, printed p.3, states Galois-equivariant
uniformization with kernel q^Z over a finite extension K of Q_p,
also over every finite extension of K. Read its hypotheses on p.2
and proof discussion pp.3–4: convergence, group law, and the explicit
deferral of surjectivity to Silverman V.3.1/V.4. Import the named
Tate uniformization theorem; this is not a complete reproof in the
handout. Retain q nonzero as well as |q|<1. Theorem 2, p.4, specifies
split multiplicative reduction for the untwisted curve over K.
There is no restriction on torsion order in Theorem 1.

The standard curve coefficients are fixed by [Milne EC2](https://www.jmilne.org/math/Books/EC2.pdf#page=107),
III.3 (24)–(26), pp.102–103. Kedlaya's extracted a4 formula lacks
the factor 5 appearing in Milne; that displayed coefficient is not
imported. The imported named theorem concerns the standard Tate
curve. Its combined Warwick copy numbers the same result 1.1
(p.5); the author handout's numbering is canonical here. Silverman's
full chapter remains unread: an HTML mirror returned metadata, then
internal errors on targeted extraction. It is not represented as read.

Reuse [the full geometric torsion-count coverage](2026-10-10-selected-bad-place-ramification-critical-audit.md):
Milne EC2 II.6.3, pp.70–71, concerns order prime to the FIELD
characteristic. Thus characteristic zero is the relevant hypothesis
for both 30 and 7; reduction modulo 3 is not the theorem's setting.
The next calculation must account for every class in the torsion
kernel and compare its Galois kernel with the coordinate-field kernel.
Containment of two chosen points in a radical extension alone does
not prove equality of the full torsion field. No coordinate-field
identity or rational-30-torsion conclusion is derived here.

### Local field inputs and exact remaining specialization

[Milne ANT v3.08](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
7.50–7.54, pp.127–129, give the unramified/residue correspondence,
prime-to-residue-characteristic root generation, and cyclic finite
residue extensions with Frobenius. Read Proposition 7.50's complete
proof, including uniqueness and the Galois assertion. Proposition
7.55, pp.129–130, with both proof directions, identifies Eisenstein
extensions as totally ramified. Reuse 7.38 and 7.42–7.43 from the
audited assessment for completeness, degree=e f, and normalized
valuation/value-group scaling. The section assumes perfect base
and residue fields; finite p-adic fields satisfy these hypotheses.

Reuse [the cyclotomic assessment](2026-10-08-cyclotomic-base-change-logarithm.md)
for Clark's root-lifting/order-preservation and unramified
base-change proofs. The elementary specialization here must split
the sixtieth-root field into its prime-to-3 and 3-primary parts,
check the latter via a translated cyclotomic polynomial over each
relevant unramified base, and compute the prime-to-3 Frobenius orders.
Unramified composita must be justified by the residue correspondence.
For the radical stage, compare the denominator of its normalized
valuation with the polynomial degree upper bound, using 7.42–7.43.
This avoids requiring an uninspected general Kummer irreducibility
or compositum theorem. Do not call X^7-q Eisenstein over a ramified
base without checking its constant term, or assume coprime
ramification alone proves linear disjointness. No orders or degree
values for the proposed packet are computed in this review.

### Duplication, qualification and decision test

Exact local searches found this packet only in its proposal; exact
web queries included `"Tate curve" "zeta_60"`, `"Tate curve" "3^30"`,
`Tate curve full torsion field K zeta n q 1/n Galois equivariant
uniformization`, and `Milne Algebraic Number Theory local cyclotomic
extensions unramified Eisenstein`. Broader torsion-field searches
returned Kedlaya and prime-to-characteristic examples. Search
results about function fields are not imported for n=30 over Q_3;
uninspected formalization/research leads are not correctness evidence.
No originality is claimed for this standard-method specialization.

ATTEMPTS/022,025,026 stop other exact fields, not the new packet.
Reuse the [rational-torsion source assessment](2026-10-10-enlarged-field-rational-torsion-prerequisite.md)
and [Tate-inertia source assessment](2026-10-10-tate-division-field-ramification-prerequisite.md)
for Dupuy–Hilado v1's full 30-torsion and bad-place prerequisites.
L041 is a necessary-screen reference only: its global F/F_0 and
normalized valuation-transfer premises are not supplied by H and q.
Its divisibility conclusion cannot certify sufficient admissibility.

SPECIALIZE approves one separate mathematical assessment of exactly
TARGET. Continue only after a complete full-field proof and exact
ramification/residue degrees, together with the full rational
30-torsion check. A failed local prerequisite stops this packet;
passing permits only further applicability assessment. Global F/F_0,
prime-to-7 degree, selected-place realization, actual/native input
and action, marked pilot transport and essentiality stay unresolved.
No reproof of Tate theory, lemma or mathematical script is needed
for this source review. Full matching Mathlib coverage remains not
checked; unknown availability is not absence.
