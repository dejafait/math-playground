# Three-adic whole-fiber realization — source assessment

TARGET: Determine whether the 54a1 whole modular fiber has a primitive three-adic realization satisfying L032's three-adic residue conditions.
CHECKED: 2026-10-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Exact 54a1/local-three, square-coordinate and whole-fiber searches located FNS's explicit local pair (13,7,54a1); scoped checks of L032-L034, ATTEMPTS/008-014 and the even-C, primitive-eleven and two-adic assessments found no completed matching three-adic specialization. Failed searches do not establish novelty.
SOURCE_EVIDENCE: Read FNS final June 10, 2019 author manuscript Table 2 and Section 3's local-computation explanation, Section 5's explicit local pairs and verification criterion pp.17-18, Lemma 5.3 and its proof pp.19-20, Section 7.2's canonical entire-fiber identification p.25 and Table 5/equation (7.4) p.27; read Clark ANT II Corollary 1.77 with proof p.57 and Theorem 1.79 p.58; reuse foundations/17 and L033-L034's audited map interface.
COMPARISON: FNS already supplies primitive three-adic modular points for 54a1 and its explicit pair, and identifies K as the whole fiber at the canonical j(E). It does not state the additional square-coordinate/common-scalar specialization. Test that pair first; a full-fiber base-change identification can replace a fresh factorization if its precise applicability is proved.
GAP: Verify the square-coordinate and common eleventh-root witnesses for the source pair, L032's residues, and equality of the prescribed scalar with the canonical j(E), then justify the entire scheme-theoretic fiber identification. No realization, factorization or local emptiness is proved in this review.
REASON: Essential source coverage is ready for the unchanged target; the known explicit pair supplies a concrete bounded test, avoiding unsupported cube-root lifting and dependent global class arithmetic.
SCOPE: One REPRODUCTION attempt at the exact TARGET using the source pair and canonical complete fiber, with Hensel root checks and full-fiber base change; exact local factor certification is an optional fallback under the reused criteria, not an assumption. No global intersection or image classification.

This replaces the pending review with source coverage for a later
mathematical specialization. This literature turn establishes no new
lemma and performs no mathematical calculation. The supervisor may
separately approve the changed assessment before invoking research.

The precise proposed test asks for nonzero a,b,c in Z3, of minimum
valuation zero, with a^3+b^4=c^11, a congruent to 1 modulo 3,
b^2 congruent to 1 or 4 modulo 9, and c a unit, together with an
isomorphism B_s -> K tensor Q3 of the entire modular fiber for
s=1728 a^3/c^11. Here K and the complete modular map are exactly
L033–L034's; B_s has the meaning used in L041. All factors, multiplicities
and exceptional charts must be retained. Do not replace the complete
algebra by a single factor or replace the common c by separate witnesses.
There is no positivity or evenness condition on a three-adic witness.

Main gap: unconditional global emptiness in the 54a1 branch, the other
four twists and infinitely many signatures. A proved empty local set
could exclude only 54a1; one exact complete-fiber realization would retire
this local nonexistence test, without deciding any global image or
integer existence. These alternatives give the continuation/abandonment
test. Cube lifting at residue characteristic three and the full field
factorization need their own coverage; no analogue of the other-prime
lifting arguments is presumed.

Essential proposed inputs are L032 (branch residues), L033 (exact field
and transport) and L034 (complete modular map). L045's unevaluated
quotient classes remain unresolved and are not premises of this test.
No GRH, rank, Sha, class-table certification, Selmer/point equality or
cross-notebook input is assumed. ATTEMPTS/013's stopped witness search
and ATTEMPTS/014's two-adic equality remain in force for those mechanisms.
The change of prime does not reset mathematical exploration counters.
Mathlib matching coverage is not checked; unknown is not absence.

## Sources actually inspected and strongest relevant conclusions

Freitas, Naskręcki and Stoll, *The generalized Fermat equation with
exponents 2, 3, n*, Compositio Math. **156** (2020), 77-113,
[DOI](https://doi.org/10.1112/S0010437X19007693),
[final author manuscript](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf),
internally June 10, 2019. The following locators use printed footer pages,
not zero-based PDF indices. The earlier assessments' mixed page conventions
are not used to select passages here.

Section 3, pp.9-10, describes finite-precision local inertial computations
and Table 2. Its i3=7 cases have source square coordinate X congruent to
plus or minus 1 or 4 modulo 9, source cube coordinate Y congruent to 1
modulo 3, and labels 54a1 or 864a1. The two displayed j-disks are
-4*3^3+3^5 Z3 and -3^3+3^5 Z3. L032 retains the square-compatible
X residues 1 and 4. These statements concern necessary local cases,
not sufficient whole-fiber compatibility.

Section 5, pp.17-18, immediately after Theorem 5.1, explicitly lists
(X,Y,E)=(13,7,54a1) among locally primitive Frey realizations over Q3.
The accompanying verification checks the curve covariants against a
scaling d, local coprimality and that X^2+Y^3 is a unit. The source also
states that units over Q2 and Q3 admit pth roots for primes p>=5.
This is a much more specific input than existence of an unspecified
local modular point. It is not yet our fourth-power/common-witness claim.

Lemma 5.3, pp.19-20, assumes prime p>=5 and initially (3/p)=-1;
its final clause gives symplectic identifications instead when (3/p)=1.
Its proof extends the inertia comparison using the good-reduction
5-torsion field, and retains a possible unramified quadratic twist.
The paragraph following the proof explains primitive Q3-points and the
scope of optimality of the local modular list. At p=11 the applicable
case is the square-symbol clause, not the negative-symbol clause.
These conclusions alone would not supply the added square coordinate
or identify a single K-valued point with the entire algebra.
Corollary 5.5's three-adic case is 96a1, not the needed 54a1 case;
it is not used as a substitute for the displayed pair.

Section 7.2, printed p.25, identifies the geometric fiber with **all twelve**
cyclic order-eleven subgroups of E[11]. It expressly identifies its Galois
action with that at the canonical point's j(E), and states irreducibility
and degree twelve for the five curves. Table 5, p.27, gives the defining
polynomial used in L033. This canonical fiber identification precedes
the assumption of GRH for the two-Selmer computation. Read the paragraph
through that boundary; neither the Selmer dimensions nor global
classification is imported. The curve/map and equation (7.4), pp.26-27,
match L033-L034. A base change of the canonical entire fiber, if the
proposed scalar is proved equal to j(E), would retain every local factor
without deriving a new local factorization. This is an authorized
specialization plan, not a completed application.

Pete L. Clark, *Algebraic Number Theory II: Valuations, Local Fields and
Adeles*, [author notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf),
accessible 161-page version retrieved 2026-10-10, revision date unidentified:
Corollary 1.77, p.57, assumes a complete nonarchimedean field, an integral
polynomial and a simple residue root, and gives an exact integral root
with the prescribed residue. Its proof lifts the coprime linear factor
using Theorem 1.75. Theorem 1.79, p.58, requires the strict inequality
|f(r)|<|f'(r)|^2. Foundation 17's earlier inspection is reused as well.
Neither statement permits simple-root lifting of a unit cube equation
at three. The proposed source-pair test fixes the cube coordinate and
instead asks for square and eleventh roots, with every derivative and
residue check deferred to research. No general Hensel theorem needs
reproof. If a local algebra calculation is needed, reuse the exact
Hensel/Eisenstein/Krasner hypotheses recorded in the two-adic and
fixed-two assessments; matching degrees or sampled precision is insufficient.

## Search limits and duplicate/failure comparison

Queries on 2026-10-10 included: `"54a1" "3-adic" "Fermat"`,
`Freitas Naskrecki Stoll exponents 2 3 11 local 3 X0(11)`,
`"54a1" "13" "7" "square"`,
`"X0(11)" "9261" "3-adic"`, and
`"a^3" "b^4" "c^11" "3-adic"`.
The numerical term in a search query is a search lead, not a computed
or certified scalar. Exact searches supplied no inspected theorem
stating the full added-power target. The primary FNS PDF, not its
search snippets, supplies the explicit-pair and full-fiber inputs.

The search also returned *Revisiting the equation x^2+y^3=z^p*,
[arXiv:2512.10781](https://arxiv.org/abs/2512.10781).
Only its abstract/landing-page scope was inspected: the advertised
new exclusions concern conductor-864 curves, certain p=19 modulo 24,
and other local primes. Its theorem/proof is an unread lead, not an
input for this 54a1/p=11/Q3 target. The FK symplectic criteria referenced
by FNS were not independently reverified; import FNS's statements,
and prefer its direct displayed-pair check for the realization.

Scoped local comparison used L032's complete branch tables, L033's
field definition, L034's map and exceptional-chart proof, the even-C
global-descent review and the primitive-eleven/two-adic assessments.
ATTEMPTS/008-014 retain global arithmetic/source blockers, the constant
norm stop, the inappropriate unrestricted baseline, fixed j=1's failure,
the five-adic equality and the two-adic equality. No completed matching
three-adic fourth-power whole-fiber result appears in those records.
Their general source coverage is reused, while their conclusions at
other primes are not transferred. No sibling notebook was read.

## Bounded specialization and stopping test

First test the displayed source pair: propose a=Y=7, b^2=X=13 and
c^11=X^2+Y^3. Verify exact nonzero integral roots, primitivity, all
required residues and **one common c** before asserting scalar admissibility.
Verify that s=1728 Y^3/(X^2+Y^3) is the canonical j(E) for the source
curve and avoids 0,1728,infinity. Apply the cited canonical entire-fiber
identification and base change to Q3, explaining why it is an isomorphism
of the whole degree-twelve algebra. A rational point on one factor,
an unproved coordinate quotient, or twelve-dimensional degree counting
without a justified map is insufficient. If polynomial reconstruction
is used, retain L034's removable x=16 chart and every zero of its
y-reconstruction denominator. No descent class evaluation is needed
for this existence-only target.

One certified realization decides this local test and retires local
nonexistence at three; do not then enumerate more witnesses or claim a
global integer solution. Failure of the proposed pair rejects that pair
only. An empty-local-set conclusion would require exhaustive exclusion
of all allowed common witnesses and entire-fiber isomorphisms and would
exclude only 54a1. Record a precise missing interface if the bounded
pair test cannot be completed. Independent global gaps remain explicit.
This is REPRODUCTION scope, not a claim of progress beyond the sources
checked, and not approval to derive and certify the result in this
literature turn.
