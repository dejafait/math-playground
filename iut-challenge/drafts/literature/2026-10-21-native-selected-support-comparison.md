# Native selected support — completed source comparison

TARGET: Compare IV Theorem 1.10's selected bad-place and good-reduction hypotheses with L097's full j-pole support for L089-L090, determining whether the support identification is automatic or requires an additional assumption.
CHECKED: 2026-10-21
DECISION: IMPORT
SEARCH_EVIDENCE: Step389 reused steps382/385, the completed native Definition 3.1 comparison, L089/L090/L096/L097 and ATTEMPTS/035; searched the exact Theorem 1.10 good-reduction/2ell clause and native selected-support terminology, then read the relevant reproduced primary statements and proof cases. No matching normal-closure support theorem was located or claimed.
SOURCE_EVIDENCE: Fresh IUT I May 2020 reproduction Definition 3.1(b),(c),(e), printed pp.61-63; IV April 2020 reproduction Definition 1.9 pp.21-22, Theorem 1.10 opening/definitions/proof(ii)-(iii) pp.22-25 and Proposition 1.8(v)-(vii) with proof pp.19-21; reused Silverman AEC second edition VII.5.5 pp.197-199 through the step368/382 assessments. Source links and exact scope below.
COMPARISON: Native bad is selected, good is its complement rather than a reduction verdict, and ell is excluded from selected residue characteristics; IV imposes good reduction on that complement only away from 2ell. L097 uses every rational j-pole. L089 supplies dyadic j-integrality, but the reviewed hypotheses supply no j-integrality at the as-yet-unselected ell or native initial data for C_o.
GAP: An unconditional support identification is not an imported theorem. A conditional same-member reduction/support application with v_ell(j(E))>=0 has adequate standard-source coverage for a later turn; occurrence of that assumption for the height-selected prime, all other initial data and exact generation remain independent.
REASON: The exact complement and exceptional-prime clauses isolate the missing ell condition and prevent both a tautological support identification and an unnecessary repeat of the weighted audit.
LITERATURE_REASON: The next target changes from an explicitly defined rational support to the native selected-place and good-reduction hypotheses, outside the approved L097 audit scope.

SCOPE: IMPORT covers the source requirements and their hypothesis comparison only. No support theorem, changed-field native application, stronger estimate or complete repair is proved here.

## Completed review — 2026-10-21, step389

The main gap remains original finite B>=A. This review's intermediate
target is TARGET. Its downstream use is deciding when the audited
explicit-support estimate can be read with the native reduced divisor.
The discriminating test was an exact hypothesis ledger, including the
exceptional primes. It supplies the following source information; it
does not execute the proposed mathematical specialization.

### Primary text, quantifiers and exceptions

The inspected texts are [IUT I, May 2020 reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%201.pdf)
(186 pages) and [IUT IV, April 2020 reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%204.pdf)
(87 pages). All references below use printed pages. Neither retrieval
authenticates current author/journal bytes; ATTEMPTS/035 stays parked.

| Source | Exact requirement relevant here |
| --- | --- |
| I Definition 3.1(b), pp.61-62 | Nonempty selected moduli places have odd residue characteristic; the fixed curve is multiplicative at every F-place above them. The good set is the complement and may include bad reduction. Stable reduction everywhere and Galoisness are separate clauses. |
| I Definition 3.1(c), p.62 | ell>=5 is prime to selected residue characteristics and selected integer q-orders; the mod-ell image requirement is separate. |
| I Definition 3.1(e), pp.62-63 | The K-place section does not replace the complete inverse images in (b). |
| IV Theorem 1.10 opening, p.22 | Good reduction is required at every finite F-place in the complementary set away from 2ell. |
| IV definitions, p.23 | The reduced divisor has coefficient one on the full inverse image of the selected q-support; the absolute different is separate. |
| IV proof(ii)-(iii), pp.24-25 | The pre-ell increment is log(2^11*3^3*5^2); (D0) concerns K/T and excludes 2,3,5,ell. |

This ledger imports source hypotheses. In particular, the word good
does not make the support equality a definition. The selected-support
predicate is on the actual fixed curve, not every field-of-moduli
descent and not one chosen completion. IV's exact-generation equality,
III Corollary 3.12 situation and other initial-data requirements remain
in force for the original theorem. They are not supplied for C_o.

### Comparison with the unchanged local records

Here L090 identifies F_mod=Q and T=Q(E[2])=Q(t_o). Therefore the
objects to compare are a selected set U of rational primes and
L097's S={p:v_p(j(E))<0}, each with its complete inverse images in
T and C_o. L089 already requires v_2(j(E))>=0; this review does not
prove any new dyadic fact. L089 also retains the split height-30
place at three on the original same member. Transferring its
reduction classification to the literal models over C_o is a later
application, not a transfer from a different named curve.

The ledger leaves the following precise application questions:

| Places/obligation | Available coverage | What is not yet certified |
| --- | --- | --- |
| Selected U | Native clause requires multiplicative reduction at all extending places, odd characteristic and p!=ell. | L097 does not choose U or check q-order coprimality. |
| Complement away from 2ell | Actual good reduction is required, even if a place is called good. | No ready hypothesis permits omitting an arbitrary pole from U. |
| Prime two | Never selected; L089 supplies integral j there. | Integral j alone is potential good reduction, not actual good reduction of an arbitrary twist; IV permits an exception here. |
| Prime ell | Never selected by I(c); IV permits bad reduction there. | No retained choice of the height-selected ell, or assertion v_ell(j(E))>=0, is available. If ell is a j-pole, it belongs to S but cannot belong to U. This conditional mismatch does not assert that such an ell actually occurs. |
| C_o reduction | Full 15-torsion of the actual E_o is rational since G_o is contained in C_o. | The reduction/support application has not been executed for all places. Normality alone supplies neither selected data nor exact generation. |

Thus the existing hypotheses do not license writing U=S. A sufficient
conditional route to test is to add explicit j-integrality at ell,
then check actual reduction and support uniqueness. This is a proposed
test, not an assertion that the extra assumption is necessary for
every possible estimate or that the conditional route already passes.
Without it the ell-place requires separate treatment. The source's
(D0) cannot settle that case, and subset inclusion alone would not
justify subtracting reduced divisors on both sides of L097.

### Standard coverage for the separate mathematical test

IV Proposition 1.8(v), p.19, with full proof p.20, covers complete
discretely valued fields and full rational prime-level torsion at a
level >=3 invertible in the valuation ring. It supplies semistability,
not splitness. Its proof uses the proper compactified level-moduli
scheme and the valuative criterion. This is the same general input
previously applied in L081, but no other curve's conclusion is used.
At residue characteristic five, use level three; otherwise use level
five. The later application must verify actual full-coordinate
rationality after each completion, including residue characteristics
two and three. This case assignment specifies applicability, rather
than deriving its reduction conclusion here.

Reuse the inspected [Silverman, AEC, second edition (2009)](https://studylib.net/doc/28155304/the-arithmetic-of-elliptic-curves),
VII.5.5, pp.197-199, including the residue-characteristic-two case
recorded in `2026-10-20-normal-closure-local-two-degree-scope.md`:
integral j characterizes potential good reduction over complete
discrete valuation fields with perfect residue field. Together with
the semistability input this covers the proposed good-versus-
multiplicative classification, to be justified in the mathematical
turn. Good reduction is preserved under finite local extension;
the distinction from potential good reduction must be retained.
There is no reason to reprove these general theorems.

L096's ramification result and L097's complete weighted estimate are
already audited. Their conclusions do not perform this reduction or
support test. The step382 and step385 assessments explicitly reserved
it; the completed October 12 native-model comparison handles the
different all-F-place/descent quantifier. No duplicate same-member
support application was found in these scoped records. No sibling
notebook or cross-notebook mathematical input was read.

Fresh queries were `Mochizuki "Theorem 1.10" "good" "2l"` and
`Mochizuki "Vbad" "good reduction" "Legendre"`. Their results led
back to the native text and expositions. Only the specified primary
statements/proof cases and reused inspected book theorem are inputs;
expositions, indexed author snippets, unrelated hits and a repository
formalization lead were not used as mathematical evidence. A failed
search does not establish originality.

### Decision and bounded continuation

This completes the requested source comparison, KNOWN_IMPORTED,
without a new lemma, script, mathematical proof or dependency change.
The exact ell exception is additional source evidence, rather than
a repetition of the old unspecified support distinction. Full and
supporting Mathlib coverage remain unchecked. No new result beyond
the sources, essential IUT flaw or complete candidate is claimed.

The separate conditional application is assessed in
`2026-10-21-conditional-native-support-bridge.md`. Continue only by
checking its stated actual-place reduction predicates and support
identity under the explicit extra ell-integrality assumption; isolate
any failure. Do not infer that the actual height-selected prime meets
that assumption. This newly written ready continuation receives
separate supervisor approval next turn. L092's factor-four relative
degree excess, exact generation/repairs, source-version/def= boundary,
independent initial data, native input/action/factorization/pilot and
essentiality all remain open. Mathematical exploration usage stays
zero; STATUS remains IN_PROGRESS.

## Invocation-start proposal — historical; completed above

## Continuation and discriminating test

Retain the same arbitrary E/Q, c,h,d_*,e_*, both fixed domains and
closure from L089, all six full-coordinate Legendre models of L090,
T=Q(E[2])=Q(t_o), G_o=T(iota,E_o[15]), and C_o=G_o^nor over Q.
L097 is the audited explicit-support conclusion; L094-L096 supply
its local inputs. Do not assume initial theta-data for C_o or silently
replace G_o in an exact-generation prescription.

Reuse step382's source-definition extraction before retrieving any
missing primary clause. Compare the exact quantifiers for selected
moduli places, their inverse images and good reduction away from
them. Record which implications are actually source-covered and
which would require a subsequent mathematical application. The test
is a precise hypothesis ledger: either source definitions make the
supports match under stated assumptions, or identify the missing
assumption and the affected places. A mere repeat of the known
support distinction is not new evidence. Do not prove an uncovered
support theorem during this literature step.

Downstream use is deciding whether L097's numerical allowance can
be considered for the native pre-ell estimate. This would leave
L092's relative degree excess, exact generation and complete repair
independent. Preserve the April reproduction/current-version and
def= qualifications, height-selected prime, independent initial data,
native input/action/factorization/pilot, essentiality and original
finite B>=A gaps. Do not import a selected singleton from an older
curve or substitute seven for the height-selected prime. ATTEMPTS/035
remains parked. Mathlib is unchecked; no candidate resolution is
asserted. Separate next-turn review is required.
