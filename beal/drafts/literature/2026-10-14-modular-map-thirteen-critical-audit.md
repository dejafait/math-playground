# Entire-map thirteen-adic certificate — approved audit coverage

TARGET: Critically audit L066's entire-map good-reduction certificate at thirteen, including chart coverage, reduced pole orders and unramified base change.
CHECKED: 2026-10-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the completed fixed-class elliptic-Chabauty and map-specialization searches; compared the exact audit target with L066, L034's prior coefficient/chart audit, L064's full-field audit, history/200–201 and ATTEMPTS/029–030. No fresh external search or mathematical replay was performed.
SOURCE_EVIDENCE: Reusable primary assessment inspected Bruin 2003 Section 4.2 pp.42–45 including both Lemma 4.1 proof cases, FNS June 10 2019 Section 7.2 pp.25–28 including (7.4), and official Magma handbook text/1568; relevant L033/L034/L064 proofs and prior audits were read for applicability and input scope.
COMPARISON: Existing sources cover the general reduction prerequisite and exact source map, but do not independently verify L066's integral-chart specialization; approve only independent verification of that existing specialization, without reproving Chabauty or deriving downstream point bounds.
GAP: Independent verification of integral open coverage, origin cancellation, complete reduced polar divisor, separability and full-field base change remains pending; coverage approval is not certificate approval.
REASON: The audit is within the unchanged source hypotheses and explicit chart method already assessed; independent scrutiny is needed before using this local prerequisite in a global rational-j method.
LITERATURE_REASON: The supervisor requires separate approval of this newly proposed audit target; reuse adequate primary coverage rather than repeat browsing or perform mathematics during the literature-only turn.
SCOPE: Only L066's original modular map over Z13 and its base change to L064's entire unramified degree-twelve field; no translated covering, rank/index, zero bound, class enumeration or power lifting.

## Coverage and source reuse

The main gap is positive primitive integer emptiness, both in the 54a1
branch and across the remaining signatures. The intermediate target is
an independently verified original-map reduction certificate at thirteen.
It could provide a reduction input to later rational-j Chabauty work;
that work still needs global rank/index information, coset-wise zero
bounds, other-class coverage and global primitive power lifting.

Reuse the actual primary readings recorded in
[the fixed-class comparison](2026-10-14-fixed-class-elliptic-chabauty-scope.md)
and [the map-specialization assessment](2026-10-14-modular-map-thirteen-good-reduction.md).
Nils Bruin, *Chabauty methods using elliptic curves*, J. reine angew.
Math. **562** (2003), 27–49,
[author-hosted published copy](https://www.cecm.sfu.ca/~nbruin/bruin_crelle.pdf),
Section 4.2 pp.42–45, supplies the arbitrary-cover rationality method
and its reduction prerequisite. Lemma 4.1's linear and quadratic
zero tests are not performed or assumed here. The degree-two formulas
of Section 4.1 are outside the scope. The
[official Magma handbook](https://magma.maths.usyd.edu.au/magma/handbook/text/1568),
“Elliptic Curve Chabauty,” requires curve and map good reduction at all
places above the chosen rational prime; its output may be infinite and
requires the documented index qualifications for completeness.
Neither source certifies this map at thirteen or implies point finiteness
from this certificate alone.

Freitas–Naskręcki–Stoll, *The generalized Fermat equation with exponents
2, 3, n*, Compositio Math. **156** (2020), 77–113,
[June 10, 2019 final author manuscript](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf),
Section 7.2: printed p.25 supplies entire-fiber transport, p.26 the
map coefficients a,b, p.27 (7.4) and Table 5, and p.28 the
reconstruction qualification in Lemma 7.6. L034's independent audit
already compared all source coefficients and exceptional characteristic-zero
charts. The source's same-field generator failure and GRH-dependent
Selmer replacement remain limitations, not inputs to L066. No source
is newly downloaded, and no unseen passage or unread lead is imported.

Local input scope is precise: L033 supplies the integral E0 model,
discriminant and torsion coordinates; L034 supplies the complete source
map and its existing coefficient/norm audit; L064 supplies the audited
entire unramified degree-twelve thirteen-adic field. Its local-field
inputs are Milne, *Algebraic Number Theory*, v3.08 (2020), Theorem 7.33,
Corollary 7.42, Proposition 7.50 and Example 7.54, with the qualifications
recorded in L064. This audit need not reconstruct the already audited
field factorization. It must verify that the claimed map certificate
base-changes to that whole integer ring, rather than a selected factor.
No fixed sigma, global class basis or cross-notebook input is required.

## Independent evidence plan, not an executed audit

Read L066 and its full load-bearing certificate values in
`scripts/modular-map-thirteen/reduction-certificate.json`. Candidate
coefficient lists may be reused only with their L034 source provenance.
A replay must not import or execute construction code as its verification.
Independently verify the NN' polynomial identity and exact unit values;
check coverage as scheme opens, including generic points and geometric
residue extensions, rather than listing only rational residue points.
Verify the entire x=16 locus and both removable/polar charts. Check the
projective origin equation, the unit definition V=1/U, both complete
factorizations and unit leading terms without dividing by a nonunit.
Check agreement on overlaps with the integrality and separatedness
hypotheses actually used. Determine all reduced poles and their exact
orders, the degree comparison and separability, then justify persistence
under the entire unramified base change. Full polynomial residuals and
relevant certificate values are essential; success flags and previews
are not proof. General degree/gluing facts must have their stated
hypotheses checked in the audit, not be inferred from sampled fibers.
This paragraph sets a verification plan and establishes no new result.

L034's characteristic-zero audit and L064's field audit are partial
prior coverage, not duplicates of the integral-map audit. History/201
records construction only; no completed independent L066 audit was
found in the targeted history and proof reads. ATTEMPTS/029–030 stop
removal of the fixed class by the assessed finite-prime image tests.
This target does not reopen those tests or remove their survivor.

Continue upon complete independent verification, or repair a named
concrete defect within this certificate. Park thirteen only for a genuine
unrepairable reduction defect; a bad quotient chart alone is not enough.
Translated-isogeny reduction, rank below twelve, adequate generators or
index control, rationality zero bounds, other classes and one common
global primitive rational/integer power triple remain unresolved.
No GRH or Selmer/point equality is assumed. Full matching and supporting
Mathlib coverage remains not checked; unknown availability is not absence.
The next turn may execute this exact audit as RESEARCH / REPRODUCTION.
