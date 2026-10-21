# Selected-model condition at the retained 3-adic place — completed source comparison

TARGET: Determine whether L048's retained 3-adic place satisfies the selected-model multiplicative-reduction condition in Dupuy–Hilado v1 Definition 5.3.1(4), with its exact model quantifier.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Scoped search of the October 11 reduction/adjunction assessments, relevant histories and ATTEMPTS/022,025,026,027 found no completed selected-model test; external searches for the exact every-model wording, ramified quadratic twists and characteristic-3 reduction located the primary passages below.
SOURCE_EVIDENCE: Dupuy–Hilado arXiv:2004.13228v1 (28 April 2020), section 5.3 and Definition 5.3.1/Remark 5.3.2 p.26, section 3.3 p.9 and section 5.7.1 p.32; Milne EC2 (2021) IV.7 Example 7.12/Corollary 7.16 pp.140–141; Barrios et al. arXiv:2501.03209v2 (2 July 2025), Definition 3.4/Proposition 3.5/Table 1 pp.5–7, odd-characteristic proof pp.8–9, Theorem 4.1/Table 4 and type-determination proof pp.13–15; Cremona (1997) III.1–2 pp.62–67. Direct links and retrieval qualifications below.
COMPARISON: The primary definition retains a universal model quantifier; known twist and odd-residue reduction theorems supply a discriminating test using a valuation-one quadratic twist. L048/L049 alone do not decide the universal condition; no twist of the retained curve is constructed or adjudicated in this review.
GAP: A research turn must justify the field of moduli and membership of a proposed Q-model in the quantified class, check its F-isomorphism without enlarging F, and apply the cited reduction theorem at 3; a change of equation of the chosen Q-isomorphism class must not be confused with a different descent.
REASON: Essential model/twist source coverage is now ready for exactly TARGET; specialize the cited results next, with the literal exposition verdict separated from native IUT and essentiality.
SCOPE: Exactly TARGET with L048's same E_0 and L045's same F; permits a proposed quadratic twist by d=3, an explicit cyclotomic square-root/isomorphism check inside Q(zeta_60), the known strongly-minimal-model replacement and odd-residue twist theorem, or the isomorphic-equation interpretation if the model class is explicitly restricted. No curve reselection, field enlargement or new general twist theorem.
LITERATURE_REASON: The startup REVIEW_REQUIRED gate covers a new universal-model applicability obligation, outside the ready semistability assessment; prior torsion, Tate and field-role coverage is reused.

## Preserved proposal (pending source-status statements superseded below)

Read the primary definition and its immediate model qualifications
before selecting reduction or twisting results. Reuse the local
packet-field-role assessment and the semistability assessment where
their scope suffices. Inspect relevant primary theorem hypotheses
and proof cases, including any nonsplit or additive cases that the
exact model quantifier permits. Do not infer the meaning of that
quantifier from these notes. No new mathematical result is established
by this proposed assessment.

Essential local inputs are L048 and L049, retaining L045 and
L044–L047 and L042 through their statements: one E_0, the fixed
precision M>=max(M_tors,31), F=Q(zeta_60,E_0[30]), Omega,H,N and
absolute v_3(q_0)=30, without q_0=3^30. Do not reselect the curve or
enlarge the fields. The narrow downstream use is deciding whether
the retained place can meet this particular prerequisite in the
inspected exposition. It is not sufficient initial data or native
definition equivalence.

Continue to mathematics only when the exact model class and applicable
reduction theorems have ready coverage. The subsequent test must either
verify the quantified condition or identify a permitted model that
fails it; a statement about the one chosen model is insufficient if
the source quantifies more broadly. If the literal reading is
ambiguous or inconsistent, record that source issue without calling
it an essential IUT flaw. Other-place parameter orders, the remaining
selected data, native/input/action/pilot/essentiality bridges and
finite B>=A stay unresolved. Preserve ATTEMPTS/022,025,026,027.
Full matching Mathlib coverage is unchecked.

## Completed comparison — 2026-10-11

### Exact primary quantifier and its limits

[Dupuy–Hilado, arXiv:2004.13228v1](https://arxiv.org/pdf/2004.13228v1#page=26),
Definition 5.3.1(4), p.26, says:

> every model E_Q(j_E) of E over Q(j_E) has multiplicative reduction at v.

The preceding setup fixes E/F; neither it nor Remark 5.3.2 restricts
these models to one Q(j_E)-isomorphism class or to semistable descents.
Section 3.3, p.9, repeats the any-model phrasing. Section 5.7.1,
p.32, checks one named curve at 11, without an additional definition
of the quantified class. Thus the word “model” is not formally
disambiguated in these passages. Do not silently replace the
universal quantifier by existence or by potential multiplicativity.
The geometric reading and the more restrictive F-descent reading
must both be distinguished from coordinate changes of one Q-model.

The versioned PDF, including the complete definition, its preceding
setup, both footnotes and following remark, was inspected. The HTML
endpoint also agrees on the quantifier, but displays an anomalous
August 24, 2026 date; the cited source is the versioned PDF.

### Known results available for the discriminating test

[Milne, *Elliptic Curves*, second edition (2021)](https://www.jmilne.org/math/Books/EC2.pdf#page=144),
IV.7, Example 7.12, p.140, gives the quadratic-twist construction
and its pointed isomorphism over any field in which the twist
parameter is a square. Proposition 7.13 and Corollary 7.16,
pp.140–141, classify twists when j is neither 0 nor 1728; the
characteristic assumption is on the field, not its residue field.
These statements and the explicit isomorphism discussion were read.
No reproof of descent or twist classification is needed.

[Barrios, Roy, Sahajpal, Tallana, Tobin and Wiersema,
*Local data of elliptic curves under quadratic twist*,
arXiv:2501.03209v2, 2 July 2025](https://arxiv.org/pdf/2501.03209v2#page=13),
Theorem 4.1 and Table 4, pp.13–14, cover perfect odd-characteristic
residue fields: type I_n, n>0, stays I_n for v(d)=0 and becomes
I_n^* for v(d)=1. Splitness/Tamagawa subcases do not change these
types. Definition 3.4, Proposition 3.5 and Table 1, pp.5–7, provide
a strongly-minimal representative. Read its odd-characteristic
I_n proof, pp.8–9, and the theorem's complete type-determination
argument, pp.14–15: it compares coefficient valuation patterns
using that representative. This includes residue characteristic 3;
the separate Q_2 theorem is unnecessary. The Cambridge PDF timed
out on follow-up; the versioned arXiv PDF supplied these passages.
Its Comalada reference is a lead, not an independently inspected
input. No companion computation is required for the cited import.

[Cremona, *Algorithms for Modular Elliptic Curves*, second edition
(1997)](https://johncremona.github.io/book/fulltext/chapter3.pdf),
III.1–2, pp.62–67, was inspected for coordinate changes, invariant
scaling, minimal models and Tate's algorithm. The type list on p.65
identifies I_n^* as additive, distinguishing it from multiplicative
I_n. Reuse the prior characteristic-3 reduction assessment for L048;
do not apply a short-form residue criterion requiring p>3.

### Application obligations reserved for the research turn

The intermediate target remains exactly TARGET. The main gap is
original finite B>=A; the downstream use is deciding whether this
retained place supplies one selected-place prerequisite in the
inspected exposition. It will not establish sufficient initial data.

Test the proposed twist d=3 of the same retained E_0. Before assigning
any verdict, justify Q(j_E)=Q, check that this is a Q-model of the
given E_F even under an F-isomorphism requirement, and verify square
membership in the already fixed cyclotomic subfield of F by an
explicit roots-of-unity identity. State the pointed isomorphism and
the local twist valuation. Import Proposition 3.5 and Theorem 4.1
for the local type, rather than assume the original cubic is already
strongly minimal or derive a new general twisting theorem. Coordinate
changes needed for a local representative do not reselect E_0.

Continuation test: continue if a permitted model and the theorem's
hypotheses can be checked with the unchanged fields; a single
nonmultiplicative permitted model settles the literal universal
condition negatively. If an explicit source restriction excludes
that model, audit that restriction and the isomorphic-equation
interpretation instead. If the text remains ambiguous, state a
qualified literal-reading verdict and leave intended/native meaning
open. Do not call an exposition issue an essential IUT flaw.

Essential inputs remain L048,L049, with L045 and L044–L047,L042
retained through them; same E_0,F,Omega,H,N and fixed M, absolute
v_3(3)=1 and v_3(q_0)=30, without q_0=3^30. No actual twist,
field-membership calculation or reduction specialization was proved
in this literature-only turn. The scoped duplicate/failure check
found no earlier universal-model test; it is not evidence of novelty.
ATTEMPTS/022,025,026,027 remain in force for their own targets.
Other-place orders, selected data, native/input/action/pilot/essentiality
and finite B>=A are unresolved. Full matching Mathlib coverage is
not checked. Save the eventual application and its precise citations
in a canonical lemma only in the subsequent research turn.
