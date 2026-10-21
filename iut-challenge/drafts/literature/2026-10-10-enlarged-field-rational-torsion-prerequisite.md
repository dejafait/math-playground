# Enlarged field and the rational torsion prerequisite — completed review

TARGET: Assess whether the rational 30-torsion prerequisite in Dupuy–Hilado arXiv:2004.13228v1 Definition 5.3.1 permits L=Q_3(zeta_20,pi), pi^27=3, as an individual selected division-field completion.
CHECKED: 2026-10-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused ready pairing/field-role coverage; narrowly read L029, L032's torsion paragraph, ATTEMPTS/022–024 and the cyclotomic-enlargement review; exact rational-torsion searches and versioned primary HTML resolve the PDF's lost overbar. Queries and access qualifications are recorded below.
SOURCE_EVIDENCE: Dupuy–Hilado arXiv:2004.13228v1 (28 April 2020), Definitions 3.6.1/3.6.3 pp. 11–13, 5.3.1/Remark 5.3.2 p. 26, section 5.4 pp. 28–29, 5.5.1 p. 30 and section 5.7.4 p. 33, https://arxiv.org/html/2004.13228v1 and https://arxiv.org/pdf/2004.13228v1; reused inspected Silverman (2009), III.8.1(c,d)/III.8.1.1 pp. 94–96, https://www.math.ens.psl.eu/~benoist/refs/Silverman.pdf#page=114; freshly read Clark's 161-page Algebraic Number Theory II, Corollary 2.33(b) p. 77 and preceding cyclotomic Eisenstein proof, https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf#page=77.
COMPARISON: The condition is full geometric 30-torsion rationality over F, rather than a cyclic subgroup; the selected completion contains the base completion. The known pairing theorem covers composite m in characteristic zero, and L032 already excludes third roots in the enlarged field. Prior fifth/fourth-root checks did not cover this condition.
GAP: A separate mathematical application must combine exact full-torsion/completion hypotheses with the pairing theorem and L031/L032's field facts; no enlarged-field exclusion is derived here.
REASON: Essential source scope is now resolved for one bounded necessary-condition application; no pairing or local torsion reproof is needed.
SCOPE: Completes exactly TARGET as a source review; the separately recorded continuation tests only individual selected division-field completions in this versioned exposition. Native hypotheses, tensor components, global construction, radii and actions are not covered.

LITERATURE_REASON: The enlarged field and rational 30-torsion prerequisite are outside the earlier prime-to-3 unchanged-packet assessment; the exact meaning and applicability of that source condition are essential unread coverage for this new target.

## Completed source comparison, 2026-10-10

The [versioned primary HTML](https://arxiv.org/html/2004.13228v1#S5.SS3)
resolves an essential extraction ambiguity: Definition 5.3.1(3) reads
`sqrt(-1) in F and E(F) superset E(overline F)[30]`. The PDF reader drops
the overbar. The preceding declaration fixes an algebraic closure;
section 5.7.4 adjoins coordinates of that same full geometric group.
All five conditions and Remark 5.3.2 were inspected. The condition is
full rational torsion, not one order-30 point or the ell-cyclic M.
The remark distinguishes the exposition's 30-torsion from native
6-torsion; no native equivalence is imported. Printed pages are one
above the zero-based PDF indices returned by the tool.

Reuse Definitions 3.6.1/3.6.3 and rechecked Definition 5.5.1: write
D=F(E[ell]), with D_w an individual selected completion. Section 5.4
explicitly includes F_v in D_w and E(D) in E(D_w). These are inheritance
inputs for a later application. Remark 5.4.4 warns about the G(w/v)
action on M_w, rather than removing rational points. The test requires
no identification of M with E[30] or of a tensor component with D_w.

The [ready field-role review](2026-10-07-packet-initial-data-field-roles.md)
and [direct-source repair](2026-10-07-packet-field-exclusion-critical-audit.md)
already inspected Silverman, *The Arithmetic of Elliptic Curves*, second
edition, Springer GTM 106 (2009), Proposition III.8.1(c,d), pp. 94–95,
and Corollary III.8.1.1, p. 96. For an elliptic curve over a field and
m>=2 prime to its characteristic when positive, rationality of all
geometric m-torsion implies containment of mu_m. The inspected proof
uses nondegeneracy for a primitive pairing value and equivariance for
rationality. Composite m and characteristic zero are covered; residue
characteristic is not field characteristic. No pairing reproof is needed.
Fresh book-URL requests failed today; adequate recorded primary inspection
remains reusable, without claiming fresh access.

[Clark's notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf#page=77),
undated 161-page author-hosted version accessed 2026-10-10, Corollary
2.33(b), printed p. 77, state that for a finite extension H/Q_p,
if p-1 does not divide e(H/Q_p), then mu_(p-infinity)(H) is trivial.
The preceding shifted cyclotomic Eisenstein proof was read completely.
The corollary itself is left as Exercise 2.19, rather than given a
standalone proof. L032 already supplies the needed local proof in its
“Torsion and the genuine all-unit logarithm” paragraph, using the
Eisenstein valuation and L031's value group. That paragraph and field
hypotheses were read. It excludes third roots in L, not elliptic torsion
directly; the pairing is the required connection. L031 supplies e=27,
f=4 and the normalized value group; total degree 108 must not replace e.
No new torsion argument or field-specific exclusion is derived here.

The narrow duplicate screen preserves L029/ATTEMPTS/022's old-factor
stop and ATTEMPTS/023–024's scalar-transport/whole-kernel stops. The
cyclotomic review checked fifth/fourth roots only, not full 30-torsion.
Queries included `"Dupuy" "Hilado" "E(F)" "30"`,
`"2004.13228" "torsion"`, `"Silverman" "Corollary 8.1.1" "roots"`
and `"initial theta data" "30" "torsion" Dupuy full`; broader standard
terminology and stronger-result screening reuse the ready review.
No required stronger field-specific theorem was found; this implies no
novelty. Secondary results and newer journal versions are unread leads,
not mathematical inputs. Screenshot calls returned locators only, and
a shell download failed DNS; neither counts as visual inspection.
Successful versioned HTML resolves the essential formula, so these
failures do not block the bounded exposition-only application.

Coverage is sufficient for the [separate application](2026-10-10-enlarged-field-full-torsion-test.md),
whose newly written assessment receives separate supervisor approval.
A failed necessary condition would stop only the individual-factor
realization; a scope mismatch would narrow or abandon this test.
No admissibility verdict or IUT flaw is established today. Actual/native
input/action, tensor components, global realization, pilot transport,
essentiality and finite B>=A remain open. Full matching and supporting
Mathlib coverage: not checked.

## Original relevance and source plan (completed above)

The main gap is original finite B>=A with the actual source hypotheses.
L038's audited radius 729 is auxiliary and supplies no field admissibility.
This intermediate review can determine whether a proposed use of the
enlarged field as an individual selected division-field factor is viable
before further numerical work. Passing a local necessary condition would
not construct global initial theta data.

Read the exact torsion condition in Definition 5.3.1 and the statements
fixing base field, full division field and selected completions. Reuse
the earlier inspected field-role evidence where unchanged, but retrieve
the load-bearing torsion wording and its qualifications. Distinguish
full rational torsion from one cyclic subgroup. The prior assessment
records a difference between the exposition's 30-torsion and the native
6-torsion condition; do not identify them. Native definitions and the
old missing log-Kummer theorem are outside this test.

Essential local inputs for any later specialization are L031's field
model and L032's already established torsion/ramification statement;
L029 supplies the precise earlier role restriction, not a theorem about
this enlarged field. L038 motivates the application only. Inspect only
the relevant L032 hypotheses and proof range after the source comparison
identifies the needed local fact. Its no-3-primary-unit-torsion statement
must not be confused with elliptic-curve torsion; any connection requires
the precise pairing theorem and its hypotheses. L030's scalar-transport
failure and ATTEMPTS/020,022–024 remain in force for their own mechanisms.

Continue to a separate mathematical turn only if the primary condition,
completion inheritance and local theorem give a concrete admissibility
test with all hypotheses stated. Import an exact matching result if
available. If the condition has different scope, record that distinction
and abandon this proposed obstruction; absence of a matching argument is
not a contradiction. If an essential source is inaccessible, park the
dependent test and choose an independently testable target. No conclusion
about this field's admissibility is derived or approved in this proposal.

Actual/native actions and inputs, tensor versus individual-factor roles,
packet/global realization, pilot transport, essentiality and finite B>=A
remain unresolved. Full matching Mathlib coverage: not checked.
