# Fixed global line and selected places — completed source comparison

TARGET: Test whether L105's SL_2(F_ell) image permits a full place section over F_mod=Q whose members above S minus {ell} identify L107's fixed U with the local Tate toric line, without changing C_o or K_C.
CHECKED: 2026-10-24
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Exact global multiplicative subspace/place-section and Tate torsion/nonsplit/SL_2 transitivity searches locate Dupuy–Hilado arXiv:2004.13228v1 Lemma 5.6.2; compared its entire proof and footnote with sections 5.4–5.5, the old singleton records, L105/L107 and ATTEMPTS/029,030,031,034,035. No novelty inference from searching.
SOURCE_EVIDENCE: Dupuy–Hilado v1 (28 April 2020), Lemma 5.4.1 and Definitions 5.4.3–5.4.5, pp.27–29, Lemma 5.6.2 with full proof/footnote 19 p.31; Kedlaya fall 2004 Theorems 1–2 pp.3–4 and Proposition 3/proof p.5; Milne EC2 (2021) IV.7.13 and nonexceptional proof case p.140; Conrad Transitive Group Actions Theorem 4.21/full proof p.10; Milne ANT v3.08 (2020) Proposition 8.10/full proof p.139; qualified IUT I May 2020 reproduction Definition 3.1(b)–(f) pp.61–63; EtTh PRIMS 45 (2009) Definition 2.5(i) p.265. Direct links, scope and source defects below.
COMPARISON: The fixed-line/variable-place mechanism is already explicit in the literature. Its exact same-member application and nonsplit covariance require qualified specialization; the printed untwisted local-module and all-place assertions are not imported literally. No new general transitivity or global existence theorem is needed.
GAP: Establish the unchanged object's toric-line definition and covariance under actual completion transport, then apply the known place-selection mechanism and extend to a full section; no such mathematical application is performed in this literature turn.
REASON: Essential source coverage is now adequate for the saved target, using explicit Tate parametrization and pointed-automorphism classification to handle the local qualification. This approves a later known-method attempt, not its conclusion or full native data.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED target adds simultaneous fixed-line compatibility and nonsplit local scope beyond the old singleton assessment; this review completes that missing comparison rather than refreshing ready global-core coverage.
SCOPE: Exactly L105/L107's same member, ordering, E_o, G_o, C_o, selected ell>=7, full K_C=C_o(E_o[ell]) and fixed U; one selected lift per rational place, toric-line alignment only at S minus {ell}. No graph, sign, theta-splitting, full-data or repair assertion.

## Primary theorem comparison

The precise primary version of the matching mechanism is
[Dupuy–Hilado, arXiv:2004.13228v1, 28 April 2020](https://arxiv.org/pdf/2004.13228v1),
Lemma 5.6.2, printed p.31 (PDF page index 30). Its complete proof
chooses conjugating elements separately at the different places, then
composes with a section from the moduli field. Sections 5.4–5.5,
pp.27–30, including the split computation, quadratic reduction,
module warning and definitions, were read to compare its scope.
Qualifications: the lemma ranges over places lacking a multiplicative
subspace; its proof reverses the needed image containment; and its
local untwisted cyclotomic description suppresses nonsplit twisting.
Definition 5.4.5's global-submodule wording must not impose descent
of the prescribed line. Footnote 19 acknowledges a character caveat.
The source therefore supplies the known selection method, not a
literal unrestricted theorem to invoke without these qualifications.

Use [Kedlaya, Introduction: the Tate curve, fall 2004](https://kskedlaya.org/18.727/tate-curve.pdf),
Theorem 1, p.3: for a finite extension L/Q_p and q in L with
0<|q|<1, the explicit parametrization is a Galois-equivariant
surjection from the geometric multiplicative group with kernel q^Z.
Theorem 2, p.4, gives the unique small parameter for negative
j-valuation, geometric pointed Tate comparison, and the extra splitness
condition for comparison over L itself. Proposition 3 and its proof,
p.5, give the torsion basis after a prime-to-ell extension; this
covers the old transvection input but is not needed as a new global
hypothesis. Its valuation-scaling prose calls the multiplier a residue
degree; use the correct ramification convention already checked in
L100, rather than importing that sentence.

For the choice of geometric pointed comparison, import
[Milne, Elliptic Curves, second edition (2021)](https://www.jmilne.org/math/Books/EC2.pdf),
IV Proposition 7.13, printed p.140 (PDF index 144), with its complete
nonexceptional proof case and the adjoining conjugate-isomorphism
construction pp.140–141. In characteristic different from 2,3,
nonexceptional j gives precisely the pointed automorphisms ±1.
Here the fields have characteristic zero even at residue characteristic
3. L090 retains the same rational j different from 0,1728. This input
and the explicit Tate formulas cover the proposed check that the
image of geometric mu_ell is independent of pointed comparison and
respects completion isomorphisms, including a nonsplit downstairs
curve. That applicability check remains for the mathematical attempt.
No untwisted nonsplit Galois-module identity is assumed.

[Keith Conrad, Transitive Group Actions](https://kconrad.math.uconn.edu/blurbs/grouptheory/transitive.pdf),
Theorem 4.21 and full proof, p.10, state double transitivity of
SL_2(F) on the lines in F^2 for every field F. Only transitivity
is needed, with F=F_ell. Example 2.3, pp.1–2, supplies its elementary
matrix input; no real-field restriction is imposed in Theorem 4.21.
A general group-theoretic reproof would add nothing here.

[Milne, Algebraic Number Theory, v3.08, 19 July 2020](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
section 8, Proposition 8.10 and full proof, p.139, fix the action
(sigma w)(x)=w(sigma^(-1)x), identify the decomposition subgroup
with the completed Galois group and prove transitivity on extending
places. The preceding action definition and conjugation computation
were read. Apply only to the finite Galois extension K_C/C_o.
The future proof must write the actual induced maps of completions
and their effect on torsion; replacing place transport by an unrelated
change of basis is not covered. The extension K_C/Q need not be
Galois for this method.

## Native boundary and version qualification

Reused the completed October 14 quantifier record and reinspected
[IUT I, May 2020 reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%201.pdf),
Definition 3.1(b)–(f), pp.61–63. A full place section and the local
requirements at its selected bad members are separate. No condition
asks that every lift over a rational prime be selected. The later
proof must retain the one global covering object. Identity with
current author/journal bytes remains unverified; this review does
not retry authentication or remove L091's def= qualification.

[EtTh, PRIMS 45 (2009)](https://ems.press/content/serial-article-files/41069?nt=1),
Definition 2.5(i), p.265, was read at the publisher endpoint. It
requires a graph-quotient factorization and a splitting compatible
with the stated sign structure, under odd residue/level and its local
field condition. Identifying a toric line alone is not that assertion.
No new application of these native predicates is made here.

## Local evidence, duplicates and exact continuation

The supplied full PROOF.md and DAG were used before detailed reads.
The narrow input screen inspected L105's same-prime hypotheses,
conclusion and imports; L107's fixed U and algebraic/global clauses;
L090's field-of-moduli and nonexceptional-j conclusions; L092's actual
normal-closure setup; L098's reduction classification; and L103's
support conclusion. The L098 reduction conclusion is used separately
from its extra ell-integrality premise; L100/L103 already make the
unconditional support separation precise. L053's local Tate method
and L060's singleton statement are old-object methods, not conclusions
about this object. The October 14 source assessment and full source
review leave simultaneous alignment uncovered locally. The inspected
external matching lemma now identifies this as known-method work.

Preserve ATTEMPTS/029's redundant-core stop, /030's full-rank-cover
stop, /031's unverified-coordinate stop, /034's cyclic-normality stop
and /035's repeated-authentication stop. None establishes an obstruction
to the present bounded place/line target, and none is reopened.
The Silverman PDF endpoint timed out on this new scope; the inspected
Tate and automorphism sources suffice, so no dependent source blocker
or repeat access attempt is needed. Screenshot calls returned no
visible page image; only the complete relevant extracted text is
claimed as read. No cross-notebook input was used. Full matching
Mathlib coverage remains unchecked.

Write Sigma=S minus {ell} for the rational support, reserving U for
L107's fixed torsion line. Essential existing IDs are
L089,L090,L092,L098 (reduction only),L100,L101,L103,L105,L107.
Retain the same member/order/closure and all actual full-coordinate
fields. The approved next attempt has these application obligations:

1. Define the local toric line geometrically via the unique small Tate
   parameter and a pointed comparison. Check independence and transport
   using the cited formulas and automorphisms; do not assume split
   reduction over C_o or uniqueness from a local character alone.
2. Identify the actual finite Galois representation group over C_o,
   apply the imported line-transitivity result, and check the direction
   of the place action on the unchanged fixed U. Do not replace U
   separately at different primes or require U to descend to C_o.
3. Check the choice at every prime of Sigma and the extension to one
   full section over Q, using the same-member F_mod=Q dictionary.
   All unselected lifts remain outside the alignment assertion.

These are proof obligations, not completed derivations. Continue if
all three pass without changing the objects or adding splitness or
ell-integrality. Narrow or abandon this application if covariance,
the full linear action or the native section quantifiers fail. An
essential theorem outside this assessed scope needs a separate review.

The main gap remains original finite B>=A. A passing application would
support a later local graph test. Graph/label/splitting/section data
beyond line alignment, full native data/III/P7, exact generation and
complete repair, relative factor-four excess, actual native
input/action/factorization/pilot, source qualifications and essentiality
remain independent unresolved obligations. No complete candidate or
result beyond the checked sources is claimed. The next work is the
known-method specialization, classified REPRODUCTION; this assessment
approves coverage and does not certify that specialization's result.
