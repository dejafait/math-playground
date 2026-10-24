# Marked octic — bounded global witness proposal

TARGET: Test the eight products theta^a(1-theta)^b(1+theta)^c, with a,b,c in {0,1}, for a global {2,3,5,11}-supported norm-square class rejected by L122's two-adic image.
CHECKED: 2026-10-24
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the scoped duplicate search recorded in this proposal; checked history/430–433, the two-adic audit note and ATTEMPTS/050–052; searched exact octic coefficients and explicit supported two-cover classes. No inspected source supplies this eight-product instance; failed searches establish no novelty.
SOURCE_EVIDENCE: Reused L114 support and ready two-adic coverage; directly inspected Bruin–Stoll arXiv:0803.2052v2 Section 2 p.3 and Section 6 pp.11–12; Milne Algebraic Number Theory v3.08 (19 July 2020), integrality definition and Propositions 2.4/2.6 pp.26–28, norm definition and Proposition 2.19/Corollary 2.20 pp.31–32, ideal-norm definition and Proposition 4.1 with full proof pp.68–69. Read L115 irreducibility argument and L122 exact transport and square/norm/scalar conventions.
COMPARISON: Known element/ideal norm theory and the existing full local square-class tables cover a bounded explicit-family test without a complete unit or class-group computation. The sources give no evaluated norms, support certificates, collision list or rejected product for this family.
GAP: Later certify invertibility, all maximal-place support conditions, exact rational norm square tests and localization/common-scalar collisions for all eight products; no product is asserted admissible or rejected in this review.
REASON: Essential method coverage for the unchanged global-witness target is now ready; specialize the cited standard methods and audited local tables, without a general reproof or backend retry.
SCOPE: Only the eight displayed products in L115's entire degree-eight field K, L114's global even-degree scalar quotient and L122's fixed two-adic transport; no complete global group, extra local place, backend probe or point-completeness computation.

## Proposed bounded test and unresolved assumptions

The main gap remains global supported arithmetic and rational/integer
point control, within the much larger unresolved Beal target. The
intermediate question is whether the certified proper two-adic filter
removes an explicit global class in this fixed family. Such a witness
would establish actual global pruning, without needing a complete class
basis. Its absence would stop this eight-product family only.

Essential local inputs are L113's unchanged G, L114's full map and
norm convention, L115's entire field, and audited L122's exact transport,
all square/norm/scalar labels and five-class point image. Read L115's
necessary proof before using it. Support must mean all maximal-ring
places outside {2,3,5,11}; it cannot be inferred from two-adic labels
or a chosen polynomial factor. Check the actual leading coefficient
in every global norm. Do not assume the three proposed generators are
independent, supported, norm-admissible, or nontrivial in the common
rational-scalar quotient. Certify these properties only as needed.

The approved later calculation should enumerate all eight exponent vectors,
retain norm/support failures and class collisions, and test each certified
norm-square supported product against the fixed five-element image.
A rejected product supplies the sought witness; if none is rejected,
preserve the complete negative evidence and park this exact family.
No bounded search is a complete supported-class enumeration. No new
norm, support or localization calculation was made in this proposal.

Global unit completeness, ordinary S-class two-torsion, simultaneous
local survival, surviving-cover points, degree-nine root recovery,
remaining factors, both L095 systems and minus-eleven remain open.
Preserve L108, ATTEMPTS/050–052 and the three-/eleven-adic equality stops.
This is not a backend retry or a larger point-search box. Full Mathlib
coverage is unchecked. The source comparison below approves this unchanged target for a later
research turn. No product calculation is performed here.


## Completed source comparison, 2026-10-24

LITERATURE_REASON: The invocation-start target was REVIEW_REQUIRED because global support and norm specialization were outside the local-image assessment; this review fills that scope and reuses ready local coverage.

The assessment is SPECIALIZE / subsequent REPRODUCTION: the general
method is known, and the missing work is this finite instance. This turn
is LITERATURE / NOVELTY_UNCHECKED / EXPLORATION, not a new mathematical
input or an evaluation of any product. No lemma or mathematical script
was written. The target text and fixed eight exponent vectors are unchanged.

Primary citations and inspected scope:

- Nils Bruin and Michael Stoll, *Two-cover descent on hyperelliptic
  curves*, Math. Comp. **78** (2009), 2347–2370,
  [DOI](https://doi.org/10.1090/S0025-5718-09-02255-8),
  [arXiv:0803.2052v2](https://arxiv.org/pdf/0803.2052v2),
  21 October 2008, manuscript Section 2 p.3 and Section 6 pp.11–12.
  These specify the even-degree norm fiber, localization, scalar
  projection and filtering. The class/unit warning remains applicable.
  Their algorithm permits testing explicit classes; it does not make a
  finite trial family complete. Reuse the detailed support extraction in
  `drafts/literature/2026-10-21-marked-octic-two-cover-support.md`
  and the ready two-adic assessment for the local algorithm cases.
- J.S. Milne, *Algebraic Number Theory*, v3.08, 19 July 2020,
  [author PDF](https://www.jmilne.org/math/CourseNotes/ANT.pdf).
  Norms are multiplication determinants and are multiplicative (p.31);
  Proposition 2.19 and Corollary 2.20 give conjugate products (pp.31–32).
  Integrality uses a monic equation; Propositions 2.4/2.6 cover finite
  stable modules and denominator clearing (pp.26–28). In the Dedekind
  setting, ideal norms send P to p raised to its residue degree (p.68).
  Proposition 4.1(c) identifies principal-ideal and element norms; its
  proof includes the non-Galois case via a Galois closure (p.69).
  These are imported standard inputs, not proposed reproofs.

The directly read norm proof includes both the generated-extension case
and the reduction by transitivity; the full ideal-norm proof includes
its torsion-free ideal-group step. PDF page indices exceed printed Milne
pages by one; Bruin–Stoll indices are one less than printed pages.
Shell PDF retrieval failed DNS, but browser text retrieval succeeded;
there is no essential source blocker. Screenshot responses did not expose
readable images and are not claimed as additional source evidence.

The exact-coefficient searches were `"275" "2860" "6930" hyperelliptic`
and `"275t" "2860" curve`; method searches included `Milne algebraic
number theory norm principal ideal norm element proposition S units`
and `"hyperelliptic" "supported" "explicit" "two-cover" Bruin Stoll`.
An irrelevant coefficient hit is not evidence. The Siksek–Stoll partial
 descent paper surfaced as a lead; its general introduction was visible,
but no theorem from it is needed or imported. No claim of novelty follows.

## Approved instance obligations, not completed calculations

Use L115's entire degree-eight field with its actual theta. L114's
squarefree degree-eight polynomial and leading coefficient fix the global
norm fiber; L122 fixes the entire localization and its single scalar
action. These meet the field/model hypotheses of the cited methods.
Their applicability does not establish support or norms of trial elements.

For every product retain exact rational coordinates, and prove it is
nonzero before using multiplicativity or square-class labels. Certify
support at **every** maximal-ring place outside the stated rational
primes. One acceptable route is a denominator-cleared integral element,
its exact norm factorization, and the principal-ideal norm theorem.
Every clearing denominator must be tracked. Integrality away from the
support is essential: rational norm support alone permits cancellations
between positive and negative valuations. Alternatively preserve exact
inverse identities in a finite ring integral away from support, with all
inverted rational primes accounted for. Either certificate must justify
maximal-ring valuations, without equating a polynomial order to O_K.
If a support check fails, preserve it and do not assume the element lies
in the supported ambient space. If the chosen sufficient certificate is
inconclusive, distinguish that from a proved support failure.

Compute exact rational norms by multiplication determinants in the full
field, retaining the polynomial leading coefficient and content. Check
sign and both numerator/denominator prime-exponent parities against
L114's norm fiber. Record all eight norm results even if some fail; no
new norm value or square test has been evaluated in this source turn.

Transport each eligible product through L122's exact theta=(alpha,-alpha)
identification and its complete square-label multiplication table.
Track error bounds if finite alpha approximants are used: the bounds
must apply to these products and their actual component valuations,
not be inferred from the previous point-evaluation bounds. An equally
valid implementation multiplies already certified individual field
square labels. Project by the **one** diagonal scalar image and compare
with L122's five classes. Independent scalars in the two factors are
forbidden. Local scalar equality need not prove global class equality;
label every reported collision accordingly. No independence of the three
trial generators is assumed. This needs neither a global square-class
basis nor a proof of completeness of supported units or class torsion.

A norm-square supported element with rejected localization proves the
requested properness witness only. A survivor need not be a curve point,
and passing this single place is not membership in the fake Selmer set.
Do not impose a subgroup structure on L122's five-element point image.
If all eight rows are inadmissible or survive, preserve the full table
and park this exact family. If some rows remain uncertified, report the
unfinished support/localization obligation rather than a negative result.
Known infinity classes prevent an empty-Selmer shortcut. No new theorem,
point completeness, integer exclusion or Beal conclusion is approved.
Full matching Mathlib coverage is not checked; no formal absence is claimed.
