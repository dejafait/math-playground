# Principal-power construction — source comparison

TARGET: Assess constructing an L058 witness from an exact principal-power relation for J with exponent coprime to five.
CHECKED: 2026-10-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched order invertibility/conductor, principal-power generators, PARI bnfisprincipal and ideal-lattice LLL; inspected primary order theory and official software statements below, comparing L058 and ATTEMPTS/013,025.
SOURCE_EVIDENCE: Kopp–Lagarias, Class Field Theory for Orders of Number Fields, author-hosted 50-page manuscript, Definition 2.15/Proposition 2.16 pp.14–15 and Lemma 2.12 pp.13–14; Conrad, The Conductor Ideal of an Order, Theorem 3.6 and proof p.6 and Section 4 pp.10–11; official PARI bnfisprincipal flags 1,2,4; Sage order_ideal class/method scope; SymPy 1.14.0 DomainMatrix lll/lll_transform hypotheses and transformation example.
COMPARISON: Known invertible-ideal group algebra and exact lattice verification cover a conditional construction, but supply neither a coprime principal power nor its generator. Complete principal-ideal routines require missing arithmetic or have quadratic scope; a bounded positive-only power-order test avoids these dependencies.
GAP: Check an actual principal-power equality, justify any inverse in R, specialize Bezout group algebra and verify the final L058 identity; no relation, inverse certificate, generator, class value or execution is known.
REASON: Approve only bounded candidate generation and exact verification, with no completeness or guaranteed-success claim; cite general known results rather than reprove them.
LITERATURE_REASON: Principal-power construction and its order hypotheses were outside the prior interface/audit coverage.
SCOPE: Fixed L033 field, R=Z[k], J=11R+(k-8)R; positive h coprime to five and literal J^h=beta R. Conditional construction and the companion bounded test only; no maximal-order enumeration, assumed inversion, class-group computation or absence proof.

## Primary coverage inspected

Gene S. Kopp and Jeffrey C. Lagarias, [Class Field Theory for Orders of
Number Fields](https://gskopp.com/wp-content/uploads/2022/12/cftfororders_kopplagarias.pdf),
50-page author-hosted manuscript accessed 2026-10-12; p.1 identifies
December 17, 2022 (preliminary draft), confirmed during source-URL recovery. Definition 2.15, printed p.14, defines invertibility by
ab=O and states that invertible fractional ideals form a group. Read
quotient definition (2.13), Proposition 2.16 and its reference on p.15:
its identity order is ord(a), which may exceed O. Do not infer an inverse
in R without checking that identity. Lemma 2.12, pp.13–14, characterizes
noninvertible nonzero prime ideals by conductor containment; its proof
reduces to localization and DVR properties. This does not certify J.
The follow-up must verify JI=R for any inverse it uses; standard Bezout's
identity supplies the group algebra to specialize. No class-field theorem
is needed, and the field-specific specialization has not been performed.

Keith Conrad, [The Conductor Ideal of an Order](https://kconrad.math.uconn.edu/blurbs/gradnumthy/conductor.pdf),
20-page live author notes, accessed 2026-10-12, revision unspecified.
Theorem 3.6, printed p.6, gives invertibility for ideals comaximal with
the conductor. Read the prime case and full induction on index, and
Section 4, pp.10–11: equality of the multiplier ring with the order is
generally insufficient. Conductor coprimality has not been checked here.
An explicit product certificate is an alternative input; arbitrary
R-ideal invertibility is not an available premise.

[PARI official general-number-field manual](https://pari.math.u-bordeaux.fr/dochtml/html/General_number_fields.html#bnfisprincipal),
live entry accessed 2026-10-12, release unspecified: read the
bnfisprincipal class-generator relation and flags 1,2,4, including
missing-generator, precision and large-output cases. It requires bnf
data from bnfinit. This stronger complete principality test supplies
neither missing data nor an R-ideal identity. Returning to that backend
would repeat ATTEMPTS/025's dependent route and is not selected.

[Sage official order-ideal documentation](https://doc.sagemath.org/html/en/reference/number_fields/sage/rings/number_field/order_ideal.html),
live version accessed 2026-10-12, release unspecified: inspected generic
versus quadratic classes, gens_reduced's quadratic-form algorithm and
is_principal's placement in NumberFieldOrderIdeal_quadratic. The examples
do not document a degree-twelve order-principality solver. Generic
lattice representation is relevant; quadratic principal-power examples
cannot be specialized to K.

[SymPy 1.14.0 DomainMatrix documentation](https://docs.sympy.org/latest/modules/polys/domainmatrix.html#sympy.polys.matrices.domainmatrix.DomainMatrix.lll_transform),
accessed 2026-10-12: read lll/lll_transform. Rows must be independent
over ZZ, shape m<=n, delta in (1/4,1); the example verifies T X=B.
Use a square rank-twelve integer basis, transposed from column convention,
delta=3/4; check integral T, determinant +/-1 and T X=B explicitly.
LLL supplies candidates only. Its approximation guarantee is unnecessary
for accepting a positive identity. Installed availability is unverified.

Reuse the inspected HNF/product-extension coverage in
[the interface assessment](2026-10-11-global-eleven-order-extension-certificate.md)
and L058's audited two-inclusion procedure. A fixed candidate list needs
no exhaustive enumeration theorem or Fincke–Pohst import.

## Relevance, comparison and continuation test

The main gap remains positive primitive integer emptiness in surviving
ordered (3,4,11) branches and other residual signatures. The intermediate
target is one principal power of J with exponent prime to five, followed
by an exact L058 witness. Its downstream use would be u=0 and survival
of both L044 vectors through audited L045. It would retire this
valuation exclusion mechanism; it would not prove integer existence or
branch emptiness. Inversion and the conditional construction remain
mathematical proof obligations, not results of this literature turn.

The bounded test is h in {1,2,3,4,6,7,8,9,11,12}. For each exact reduced
basis b1,...,b12 of J^h, test only bi and bi+bj, bi-bj for i<j: at most
144 candidates per exponent, 1,440 total. Coefficient Euclidean length
is a heuristic, not field norm or a generator bound modulo units.
Accept beta R=J^h only by entire lattice equality. After success,
verify a literal inverse before negative ideal powers, justify the
coprime-exponent group specialization, and verify the final L058
identity with rank, stability and two inclusions. No such work ran today.

This is distinct from ATTEMPTS/013's low-degree element boxes and
ATTEMPTS/025's maximal-order enumeration: all twelve coordinates and
J-products are retained, no maximal basis or five-prime data are needed,
and there is no exhaustive short-vector claim. Stop at the fixed list,
or an implementation/verification blocker. Finite failure cannot prove
nonprincipality, nonzero u or a class-order bound; do not enlarge this
search without a new idea. A relation alone is not a completed L058
certificate.

Queries included `number field orders invertible ideals prime ideals
conductor simple root polynomial principal ideal algorithm`,
`PARI bnfisprincipal ideal power principal generator non maximal order`,
`number field ideal lattice principal ideal short vector norm ideal
Minkowski LLL principal ideal problem`, and
`site:docs.sympy.org DomainMatrix lll_transform ZZ delta`.
Subfield norm-relation PIP and cyclotomic short-vector papers are unread
search leads, not theorem inputs. No novelty follows from this search.

Essential inputs: audited L058, L033 exact field/power basis, L041 all
ordered eleven places, audited L045; L044 retained downstream.
Unresolved: principal-power existence, coprime h, beta and any inverse
in R; arbitrary five-prime freedom, units, other places, global points
and integer lifting remain independent. No cross-notebook input or GRH.
Reuse the primary Beal formulation recorded in
foundations/01-target-and-scope.md. Full matching and supporting Mathlib
coverage are not checked; no absence assertion is made.

The companion ready continuation is newly written and awaits the
supervisor's separate approval next turn. This review establishes source
coverage, not a mathematical advance or witness.
