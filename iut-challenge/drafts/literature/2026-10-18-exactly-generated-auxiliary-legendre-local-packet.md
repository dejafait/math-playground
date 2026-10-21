# Exactly generated auxiliary Legendre field — source scope approved

TARGET: Determine whether, for L077's same cross-residue model over T_0=Q(t), the exactly generated field G=T_0(iota,E_L[15]) and its full seven-division extension G(E_L[7]) have embedded completions H and N, respectively.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step304 searched the active quadratic-modification, global-adjunction and full-torsion assessments, L073/L074/L076/L077, foundations/05 step272 and ATTEMPTS/027,028,031,032,033; searched full rational torsion/Weil pairing, division-field completions and the exact Legendre 15-torsion completion terminology on 2026-10-18. General primary inputs below cover the mechanisms; no exact combined instance was identified and no novelty is inferred.
SOURCE_EVIDENCE: Reused the inspected coordinate/full-coordinate coverage of the step300/302 and 2026-10-11 global-adjunction assessments; freshly read Silverman AEC second edition (2009), III section 8 hypotheses p.92, Proposition 8.1(c,d) and proofs pp.94–96, Corollary 8.1.1 and proof p.96; Milne FT v5.10 (September 2022), Proposition 5.8(a,b) and proof pp.64–65; Milne ANT v3.08 (19 July 2020), section 8 introductory completion argument p.135 and Propositions 8.1–8.2 with proofs p.136.
COMPARISON: Known full-torsion, cyclotomic-generation, pointed-coordinate and induced-completion results cover this target's methods. L077 supplies an upper ambient field, not the required subfield lower bound or changed-curve seven-division identity; those are specific applications still to be written, without a new general theorem or classification.
GAP: Coverage is ready; neither G_u=H nor G(E_L[7])_w=N is proved here. A separate research turn must check the cyclotomic lower bound, both completion inclusions and full local seven-torsion transfer for this exact G and E_L.
REASON: The changed subfield's essential source comparison is now complete. Proceed to one known-method specialization of the unchanged target, preserving native-T and independent-initial-data qualifications.
SCOPE: Exactly TARGET for the same L073 witness, L074 ordering, L076 cross-residue choice and audited L077 root s in H, with both coordinates of all torsion points and places induced by the fixed embedding. No equality G=F_aux(s), native T=Q(t), global Galois/degree condition, or sufficient initial data is covered.

LITERATURE_REASON: The invocation-start REVIEW_REQUIRED target changes the ambient field to an exactly generated subfield; the earlier ready adjunction assessment did not cover its lower-bound obligation or the changed curve's local seven-division comparison.

## Primary coverage and applicability comparison — step 304

[Silverman, *The Arithmetic of Elliptic Curves*, second edition,
Springer GTM 106 (2009)](https://www.math.ens.psl.eu/~benoist/refs/Silverman.pdf#page=114),
III section 8 assumes an elliptic curve over a field, an integer m>=2,
and m prime to the characteristic when positive. Proposition 8.1(c,d)
gives nondegeneracy and Galois equivariance. Corollary 8.1.1 says that
full rational geometric m-torsion implies mu_m in the field. Read its
complete proof and the complete proofs of (c,d), including the
function-descent argument and the Galois conjugation computation.
The recorded pairing coverage in
`drafts/literature/2026-10-10-enlarged-field-full-torsion-critical-audit.md`
is reusable; fresh primary text now also succeeds. The intended
level is composite and the fields have characteristic zero. Residue
characteristic 3 is not a restriction on this theorem. Import it;
do not reprove the Weil pairing.

[Milne, *Fields and Galois Theory*, v5.10, September 2022](https://www.jmilne.org/math/CourseNotes/FT.pdf#page=64),
Proposition 5.8(a,b), pp.64–65, treats X^n-1 in characteristic not
dividing n: its roots form a cyclic group and a primitive root generates
the splitting field. Read the distinct-root/cyclic-group and
powers-of-a-generator proof cases. This is enough general coverage
for the proposed roots-of-unity test; the next turn must check the
particular root orders and coprime-order arithmetic with the specified
iota. No new cyclotomic degree calculation or disjointness assumption
is needed. No particular cyclotomic containment in G is established here.

[Milne, *Algebraic Number Theory*, v3.08, 19 July 2020](https://www.jmilne.org/math/CourseNotes/ANT.pdf#page=137),
section 8 pp.135–136, identifies the completion of a finite separable
extension A(alpha)/A at a specified extended place with A-hat(alpha)
using that root image. The absolute value is archimedean or discrete
nonarchimedean. Read the forward completeness argument, the converse
factor/place construction, and Proposition 8.2's canonical tensor-map
proof. There is no Galoisness, disjointness or integral-monogenic
assumption. Reuse the finite-coordinate-list specialization already
covered in
`drafts/literature/2026-10-11-global-torsion-adjunction-preserving-completion.md`.
The chosen embedding remains essential; neither a degree match nor
an arbitrary isomorphic completion suffices.

Reuse Milne, *Elliptic Curves*, second edition (2021),
[II Theorem 2.4(b), pp.52–53](https://www.jmilne.org/math/Books/EC2.pdf),
through the ready step300/302 coordinate assessments and audited L077.
The complete pointed map and inverse, including their group-law
compatibility and full torsion transport, have adequate coverage.
The general theorem is not restricted to global coefficient fields.
For the next local application, verify every coefficient in the same
H; a global isomorphism over a larger field alone is insufficient.
The existing full-coordinate torsion review covers compatibility of
the global and local geometric point sets; do not substitute x-only
fields or a cyclic subgroup.

## Specific obligations left to the research turn

Keep G exactly as in TARGET. Check first that it is a number field
with the stated nonsingular coefficient model and full geometric
15-torsion, and locate it in L077's ambient field using the actual
generators. Use the pairing and cyclotomic inputs to test the necessary
lower bound for its closure. Both directions are required; containment
of G in H by itself cannot establish the first completion equality.
These are unperformed applications, not a verdict on that equality.

Then apply the completion theorem to G with the complete E_L[7]
coordinate list at the same embedding. Compare its local full division
field with L073's H(E_aux[7]) by using both directions of the actual
pointed H-isomorphism. Do not assume that its coefficients belong to
G or that the two global division fields agree. Check all geometric
seven-torsion points in both directions before using the known N.
This is the specific difference from L077's original-curve adjunction;
no proof of the proposed seven-division completion is supplied here.

The strongest inspected general results supply all these mechanisms,
but do not mention this auxiliary witness or this exact coefficient
field. Hence SPECIALIZE, with a next research classification of
REPRODUCTION, rather than a direct citation claiming the two equalities.
No general theorem needs reproof; only the finite root-order check,
actual generator inclusions and local coordinate specialization need
to be written. Full matching and supporting Mathlib coverage for the
combined target remain unchecked, without an absence assertion.

## Discovery, duplicate and failure screen

Queries included `elliptic curve full rational n torsion Weil pairing
roots unity Corollary 8.1.1 Silverman`, `elliptic curve division field
completion local torsion field isomorphism coordinates`, `Milne Fields
Galois Theory roots unity primitive coprime orders cyclotomic`,
`"Legendre" "15-torsion" "completion"`, and `"division field"
"completion" "elliptic" local field`. Search results on CM-specific
division fields, entanglement and local-global divisibility are unused
leads; their theorem hypotheses/proofs were not read or imported.
The earlier general division-field assessment already warns against
assuming independence of torsion fields. No stronger classification
is essential for this same-embedding target. A failed exact search
does not certify originality. Screenshot requests returned locators
only; all fresh inspection claimed above used primary PDF text,
not visual inspection.

L073 supplies the same auxiliary packet; L077 proves the larger-field
result only. L074/L075 fix F_aux and therefore do not decide this
changed subfield. The inspected local records contain no proof of
TARGET. The step272 native field prescription remains a qualification,
not an identification of Q(t) with F_tpd. ATTEMPTS/027 stops exact
rational-q curve globalization, /028 concerns the broad universal-model
predicate, /031 and /032 retain marking/enclosure stops, and /033
parks classification retrieval. None is reopened or treated as a
global ban. The initial scoped status inspection found substantial
unfinished notebook work; it is preserved. Nonexistent exploratory
filename globs supplied no evidence and were replaced by exact paths.

The main gap remains original finite B>=A. The intermediate target
and both pass/fail thresholds remain exactly TARGET. Its plausible
downstream use is an auxiliary literal torsion-generation prescription
retaining the local packet before a native-T comparison. Continue only
if both embedded equalities are proved for the same model; an actual
failure stops this subfield choice, whereas an incomplete proof stays
unresolved. Native T/model, independent initial data, retained
memberships/scalar occurrence, marked all-image factorization, pilot
transport and essentiality remain open. This turn adds source coverage,
not a field theorem, a discovery beyond the checked literature or an
IUT flaw; no lemma or mathematical script is written.

## Original proposed scope retained

Keep the same L073 auxiliary witness, L074 ordered roots, L076
cross-residue choice and audited L077 root s in H and model E_L.
Here iota=zeta_60^15, t=(r_k-r_i)/(r_j-r_i), and both coordinates
of every geometric torsion point enter the field notation. All fields
and places use the same embedding. T_0 is the explicit coefficient
field Q(t); it is not asserted to be native T=F_tpd. No equality
G=F_aux(s) is part of this proposed target.

The main gap remains original finite B>=A. The plausible downstream
use is an auxiliary field defined by the literal torsion-generation
prescription while retaining the local packet, before any native-T
or independent-initial-data comparison. The continuation test is both
induced completion equalities for this exact G and same curve. An
actual failure stops this subfield choice; missing proof leaves it
unresolved, rather than giving a negative field verdict or an IUT flaw.

The separate source review should reuse the ready coordinate and
completion theorems and check precise full-torsion/roots-of-unity
statements needed for a subfield lower bound and the complete
seven-division field after local coordinate transfer. It must not
infer completion equality from inclusion in H,N, nor replace E_L[7]
by E_aux[7] without justification over the relevant local field.
No such comparison or new lemma is proved in this proposal.

Essential inputs are L073, L074, L076 and audited L077. Native T/model,
exact generation for the retained witness, independent initial data,
retained memberships/scalar occurrence, marked all-image factorization,
pilot transport, essentiality and finite B>=A remain unresolved.
Preserve foundations/05 step272 qualifications and ATTEMPTS/027,028,
031,032,033. This differs from the fixed-F_aux exclusion and parked
classification retrieval; no historical stop is reopened. Full matching
and supporting Mathlib coverage for this combined target is unchecked.
