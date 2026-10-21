# Bounded principal-power test — coverage for separate approval

TARGET: Test J^h for h in {1,2,3,4,6,7,8,9,11,12} using exact power-order lattice reduction and verify any resulting L058 certificate.
CHECKED: 2026-10-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the searches, duplicate/failure comparisons and inspected primary statements in 2026-10-12-power-order-principal-power-construction.md; this is its specified bounded test.
SOURCE_EVIDENCE: Direct primary sources rechecked: https://gskopp.com/wp-content/uploads/2022/12/cftfororders_kopplagarias.pdf Definition 2.15/Proposition 2.16 pp.14–15 (December 17, 2022 preliminary draft); https://kconrad.math.uconn.edu/blurbs/gradnumthy/conductor.pdf Theorem 3.6 p.6; https://docs.sympy.org/latest/modules/polys/domainmatrix.html#sympy.polys.matrices.domainmatrix.DomainMatrix.lll_transform (1.14.0); reused HNF coverage at https://pari.math.u-bordeaux.fr/dochtml/html/Vectors__matrices__linear_algebra_and_sets.html#mathnf.
COMPARISON: Standard ideal-group algebra and lattice operations cover a conditional positive certificate; LLL supplies candidates only, with no guarantee of a coprime principal power or finding its generator in the fixed list.
GAP: Generate and verify exact J-powers, test the specified candidates and, if successful, justify inversion and the coprime-exponent specialization before checking the final L058 identity.
REASON: Direct-source recovery confirms the previously proposed bounded positive-certificate scope unchanged; finite failure permits no class inference and no mathematical test runs in this literature turn.
LITERATURE_REASON: Supervisor recovery requires direct source URLs in this ready assessment; reuse theorem comparison and repair locators without expanding the target.
SCOPE: Ten listed exponents, twelve reduced basis vectors and pairwise sums/differences; at most 144 candidates per exponent. No expansion, exhaustive generator bound, maximal-order computation or negative class conclusion.

The [completed source comparison](2026-10-12-power-order-principal-power-construction.md)
contains inspected hypotheses, proof cases, versions, links, applicability
qualifications and the stopping test. Reuse it without a fresh search
if this exact target is approved unchanged. No mathematical result or
implementation is present here.

Inputs: L033, L041, audited L045 and audited L058; L044 retained through
L045. Check full rank, k-stability, all product generators and every
lattice compression. Verify reduction transformations exactly; accept
only literal beta R=J^h. A relation is not yet an L058 witness: verify
any inverse in R, write the conditional Bezout specialization with all
signs and integer powers, then check the final identity by L058.
Cite known general algebra in any canonical result and justify only
the necessary specialization. No new general theorem is claimed.

Save full certificates under scripts/power-order-principal-power/ during
research. Print candidate counts against 1,440, actual/required ranks
and equalities, failures and paths. Stop at the fixed list or a blocking
implementation defect. A failed heuristic search is at most EXPLORATION
unless a new justified obstruction is found; it cannot prove u!=0.
A verified witness would settle projected valuation survival only.
Principal-power existence and construction remain unproved; units,
other images, global points and integer lifting remain unresolved.
Installed backend availability and Mathlib coverage are not checked.

## Direct-source recovery, 2026-10-12

Opened the three primary URLs in SOURCE_EVIDENCE, then read the exact
order statements and Conrad's prime and index-induction proof cases,
and the SymPy lll/lll_transform hypotheses and transformation example.
Kopp–Lagarias p.1 identifies the preliminary draft as December 17, 2022;
the companion's previous unidentified-date note is corrected.
Definition 2.15 uses the original order as group identity; Proposition
2.16 instead concerns the associated order, which can be larger.
Consequently a verified product with identity R remains required.
Conrad's conductor hypothesis remains unchecked for J; his theorem
is a conditional input, not a certificate of invertibility here.

SymPy requires independent integer rows, m<=n and 1/4<delta<1.
The planned rank-twelve basis fits these documented requirements only
after its rank and integrality are verified. Check the transformation
and its unimodularity independently; no shortest-generator guarantee
is used. HNF/product coverage is reused from the existing interface
assessment, not refreshed or extended. No new theorem search was needed.

ATTEMPTS/013 and ATTEMPTS/025 were read narrowly: the parked element
boxes lack completeness, and maximal-order enumeration lacks certified
data and coverage. The saved power-order test avoids those dependencies
but still has no success guarantee. No duplicate witness or class value
is established by the existing interface. The main gap, downstream use,
input IDs, unresolved assumptions and fixed stopping test above remain
unchanged. Full matching and supporting Mathlib coverage are not checked.

DECISION remains SPECIALIZE for this exact TARGET. This is a source
metadata repair, reported STALLED rather than a mathematical advance
or a new informative negative result. No lemmas or scripts were edited.
