# Thirteen-adic same-class witness — audit coverage ready

TARGET: Critically audit L064's thirteen-adic same-class witness, including both complete field identifications, residue fifth-root lifts and common primitive scalar witnesses.
CHECKED: 2026-10-13
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the unchanged membership assessment's exact/stronger-result searches; targeted checks of L033, L034, audited L062, L064, history/192–193 and ATTEMPTS/029 distinguish this pending independent audit from the completed scalar search and retired removal mechanism.
SOURCE_EVIDENCE: Inspected Milne ANT v3.08 Theorem 7.38, Corollary 7.42 with proof, Proposition 7.50 with construction/uniqueness proof and Example 7.54; Clark Theorem 1.79 and Corollary 1.77; Schaefer–Stoll Section 5 evaluation/restriction diagram; FNS Section 7.2 map, full canonical fiber, Table 5's 54a1 row and (7.4); Stacks tags 01JQ, 0CCL, 0CCK and 02K9 statements and relevant proofs.
COMPARISON: These imported general results cover the audit's local-field, lifting, entire-fiber and fixed-class interfaces; none certifies L064's particular arithmetic. L064 remains an unaudited positive local witness, with no claimed new general theorem or Beal exclusion.
GAP: No essential source gap remains for this bounded audit; complete independent replay of the defining/residue polynomials, whole-fiber reconstruction, fifth roots and common power witnesses remains required. Exact source-page references also require the qualification below.
REASON: Approve one REPRODUCTION proof audit of the unchanged target using known general inputs and existing exact evidence; passing confirms the local survivor-removal failure, while a defect requires precise repair or a saved unresolved obligation.
SCOPE: Exactly TARGET, retaining L033's K and normalized delta, L034's complete j-map, audited L062's fixed sigma/class and L064's entire thirteen-adic fields and witness; no new prime, class search, full image computation or global lifting claim.
LITERATURE_REASON: The saved REVIEW_REQUIRED continuation requires separate comparison of the new critical-audit interfaces; reuse the ready membership search and general coverage while checking the exact theorem hypotheses and primary locators.

## Relevance and bounded audit scope

The main gap is positive primitive integer emptiness in the 54a1 branch
and the other residual signatures. The intermediate target is independent
verification of the existing thirteen-adic same-class witness. Its
downstream use is a reliable decision to retire removal of this fixed
survivor at thirteen; it supplies no all-place or integer conclusion.

Inputs: L033's exact K and normalized delta, L034's entire j-map and
source coefficients, audited L062's fixed sigma, and L064's new proof
and `scripts/thirteen-adic-membership/membership-certificate.json`.
No cross-notebook input is proposed. The general source coverage in
`2026-10-13-thirteen-adic-canonical-class-membership.md` remains reusable.

Check mbar and M irreducibility and full degree twelve; distinguish
the canonical branch polynomial G² from a maximal-prime factorization.
Check integrality and unit reconstruction for the fixed canonical point,
the exact residue fifth roots, and unit-derivative lifting in the whole
unramified field. Check B_3 exhausts the entire projective fiber and that
its identity class matches localization of the fixed global class under
every permissible isomorphism. Independently recompute both strict
Hensel bounds and the common primitive power identities at scalar 3.

A passing audit confirms a local negative decision for survivor removal,
not Beal or the all-place intersection. A defect requires a precise
correction or saved unresolved obligation. The threshold is complete
load-bearing evidence, rather than a successful rerun of the original
program or a bounded preview. No new mathematical claim is established
in this literature turn.

## Primary theorem coverage and applicability obligations

J. S. Milne, *Algebraic Number Theory*,
[v3.08, July 19, 2020](https://www.jmilne.org/math/CourseNotes/ANT.pdf):
reuse Theorem 7.33/Remark 7.36, printed pp.121–123. Rechecked Theorem
7.38, p.123 (complete discretely valued base, finite separable extension),
Corollary 7.42 and its proof, p.124 (degree equals ef), and Proposition
7.50 with its construction and uniqueness proof, pp.127–128. The latter
assumes perfect base and residue fields. Example 7.54, p.129, explicitly
states uniqueness up to base-field isomorphism of the unramified extension
of each degree for characteristic-zero local fields. These hypotheses
fit Q13 and finite residue fields. The audit must establish irreducible
degree-twelve reductions for the two actual defining polynomials before
using these results. The canonical G² reduction is not that evidence.
Matching e,f for ramified fields is outside this comparison.

Pete L. Clark, *Algebraic Number Theory II: Valuations, Local Fields
and Adeles*, [161-page author notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf),
revision date unidentified: rechecked Section 5's complete nonarchimedean
field/valuation-ring conventions, Corollary 1.77 and its proof, printed
p.57, and Theorem 1.79, p.58 (PDF indices 56 and 57). The latter requires
an integral polynomial and approximation with |H(r)|<|H'(r)|²; its root
and closeness conclusions apply over both Q13 and its finite complete
extensions. The audit must check actual residue roots, nonzero unit
derivatives and the strict inequalities for both ordinary f-values and
the cube/eleventh roots. The theorem is imported, with no reproof or
claim that a derivative alone supplies a residue root.

Edward F. Schaefer and Michael Stoll, *How to do a p-descent on an
elliptic curve*, Trans. AMS **356** (2004), 1209–1231,
[DOI](https://doi.org/10.1090/S0002-9947-03-03366-X),
[June 13, 2001 long manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf),
Section 5, printed pp.8–9: rechecked the two cohomology requirements,
good-divisor function evaluation and the commuting restriction diagram.
Its evaluation identification cites Schaefer [25, Theorem 2.3], imported
through the inspected stated result rather than independently reverified.
L033's audited dual direction, mu_5 kernel and normalized f supply this
interface. L062 fixes sigma before base change. The audit must verify
that the particular evaluations are ordinary, finite and nonzero, and
that the same sigma is tensored; separately choosing a local conjugate
would not be this input. No unrestricted-image theorem is necessary to
validate the positive witness, and no good-reduction or image-size
calculation is substituted for its explicit fifth roots.

Freitas–Naskręcki–Stoll, *The generalized Fermat equation with exponents
2, 3, n*, Compositio Math. **156** (2020), 77–113,
[June 10, 2019 final author manuscript](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf),
Section 7.2: inspected the twelve-subgroup whole-fiber paragraph, the
complete modular numerator a and both factors of b, Table 5's 54a1
defining polynomial and (7.4). The extracted printed headings put the
map on p.25 and Table 5/(7.4) on p.26 (PDF indices 25 and 26); the
earlier local p.27 locator for Table 5 is imprecise. Keep the exact
formula/table identifiers and resolve that citation during the audit.
The field statement precedes the GRH-dependent Selmer computation;
the table's dimension and two-adic domain theorems are not inputs here.
L034's audited elimination and exceptional-map analysis remain reusable.

The Stacks Project, retrieved 2026-10-13:
[Lemma 26.17.2, tag 01JQ](https://stacks.math.columbia.edu/tag/01JQ)
gives the affine tensor-product fiber construction.
[Lemma 53.2.4, tag 0CCL](https://stacks.math.columbia.edu/tag/0CCL)
requires a proper source of dimension at most one, separated target and
nonconstant image on each one-dimensional component for finiteness.
[Lemma 53.2.3, tag 0CCK](https://stacks.math.columbia.edu/tag/0CCK)
gives flatness for a nonconstant curve map to a normal curve; its proof
uses torsion freedom over the target field/DVR.
[Lemma 29.49.2, tag 02K9](https://stacks.math.columbia.edu/tag/02K9)
identifies finite flat and finite locally free over a locally Noetherian
base. L034 has the smooth projective curves, nonconstant degree-twelve
map and normal Noetherian target. The audit must retain this whole
degree before checking that reconstructed distinct points exhaust B_3;
elimination alone is only a necessary polynomial relation.

## What remains for the research turn

Independently verify all load-bearing arithmetic in L064's existing
certificate, including the complete Frobenius remainders and gcd tests
for mbar, G and M, coefficient provenance, curve reconstruction and
nonzero fifth-root identities. Inspect complete relevant certificate
values with the shared JSON inspector; previews cannot establish them.
The elementary irreducibility argument already written in L064 also
needs critical review. Do not repeat or enlarge the scalar search.

Review the integrality/unit arguments and the direction of whole-fiber
maps before using the source theorems. Confirm that the positive witness
uses one common a,b,c and that equality of the two identity classes
survives every permissible whole-field isomorphism. The canonical
scalar's primitive obstruction is a comparison claim to check, not the
class-exclusion mechanism. No global class/unit basis, v value, all-place
compatibility, Selmer/point equality, GRH or integer lift is assumed.
No cross-notebook input is used.

Prior exact membership searches and their recorded queries are retained
in `2026-10-13-thirteen-adic-canonical-class-membership.md`; unchanged
claims require no repeated web discovery. History/192–193 and
ATTEMPTS/029 record the positive witness and removal stop, while L062's
independent audit covers the existing fixed-class interface. This turn
does not reopen earlier quotient, generator or local-exclusion routes.

Full matching Mathlib coverage and supporting declarations remain not
checked; unknown coverage is not absence. Existing canonical lemma
citations remain the mathematical inputs. Completed kind/classification:
LITERATURE / NOVELTY_UNCHECKED. Outcome EXPLORATION records new audit-scope
comparison and approval, with no mathematical certificate replay,
verified application or advance beyond the sources checked.
