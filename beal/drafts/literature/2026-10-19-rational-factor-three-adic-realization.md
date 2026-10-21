# Both rational-factor systems at three — source comparison complete

TARGET: Test for a primitive 3-adic realization of each complete L095 system with C a unit, using a finite residue obstruction or a certified Hensel lift.
CHECKED: 2026-10-19
DECISION: EXPLORE
SEARCH_EVIDENCE: Searched the exact signature with local/rational and three-adic terms, the cover polynomial, and distinctive H coefficients; reused the rational-factor and eleven-adic assessments and searched their associated histories/attempts. No inspected result decides this exact target; no novelty inference follows.
SOURCE_EVIDENCE: Reused foundations/17-local-power-hensel-inputs.md and the ready eleven-adic assessment for Clark Theorem 1.79 and Zabradi Theorem 2.4; inspected Putz (2024), Proposition 5.14 and every left-column condition of Table 5.17, printed pp.167–168 (PDF indices 173–174), including its computational proof attribution.
COMPARISON: General Hensel–Newton covers non-simple lifting under its strict error/derivative inequality but supplies no system-specific verdict. Putz's special three-adic covering rows do not apply to coefficient triple (1,1,1); unrestricted local solvability and L096's eleven-adic points do not supply either required tuple.
GAP: Obtain exact nonzero common primitive tuples in both systems, or an exhaustive finite residue obstruction for a system; no three-adic mathematical result was obtained in this review.
REASON: Essential method coverage is ready for one bounded local attempt, independent of parked class arithmetic; no essential source is blocked within this scope.
LITERATURE_REASON: This target changes the local prime from eleven to three, where simple cube lifting cannot be assumed, and requires checking the previously unread coefficient conditions of Putz's three-adic table.
SCOPE: Both complete L095 systems over Z_3, with m,u,a,A,B,C nonzero, min(v_3(m),v_3(u))=0 and C a unit; elementary residue/valuation tests and the cited Hensel criteria only. Integer positivity and conditions at five and eleven are outside this local scope.

## Gap, intermediate target and use

The main gap is integer elimination in ordered (3,5,11), within Beal's
remaining signatures. This intermediate target asks whether three alone
excludes either rational-direct-factor system. An exact local witness
retires standalone local nonexistence for its system; a complete
obstruction removes that integer branch. Neither resolves surviving
integer systems, other algebra factors, or other signatures.

## Existing inputs, duplicates and failures

Use audited L095's full forms, without dropping any coefficient:

    Q(m,n)=3m²+mn+n²,
    H(m,n)=55n^8+165mn^7+594m²n^6+1100m³n^5
           +2145m^4n^4+2475m^5n³+2970m^6n²+1782m^7n+1215m^8.

I: C=5m+u^5, H(m,C)=a^3, A=ma, B=Q(m,C)u.
II: C=m+5^10u^5, H(m,5C)=5^11a^3, A=ma, B=Q(m,5C)u.
The existing identity is
n^11−Q(m,n)^5(n−5m)=m³H(m,n).
Use it to verify one common tuple gives A^3+B^5=C^11.

The relevant L095 statement, complementary identity, reconstruction and
converse ranges were read. Reuse its completed independent audit.
L096's local conclusion and ATTEMPTS/043 retire eleven-adic exclusion
only; its m=u=1 choices must not be imported at three. The earlier
rational-factor assessment, its audit, histories 316–323 and targeted
rational-factor drafts contain no completed three-adic test. L001's
unrestricted local-solubility conclusion, already compared in the ready
eleven-adic assessment, is insufficient for a rational factor. No detailed
reread of that unrelated construction is needed. ATTEMPTS/044's rational
factor-descent stop and ATTEMPTS/045's backend park remain intact; the
present target needs neither class data nor factorization of H.

## Primary source comparison

P. H. C. Putz, *Enumeration of local and global étale algebras applied to
generalized Fermat equations*, VU Amsterdam (2024), version of record,
DOI [10.5463/thesis.832](https://doi.org/10.5463/thesis.832),
[primary PDF](https://research.vu.nl/ws/portalfiles/portal/367784086/Thesis_CasperPutz.pdf),
Proposition 5.14 and Table 5.17, printed pp.167–168, inspected 2026-10-19.
The proposition assumes nonzero pairwise coprime coefficient integers
and a solution in its defined solution set; each covering assertion
also requires its row condition. All three-adic row conditions are
v3(a)=4,6,7,8,9,10; v3(b)=3; or v3(c)=6. Here a,b,c denote equation
coefficients, not L095's cube-root parameter a or reconstructed bases.
At coefficient triple (1,1,1), none holds. Coordinate divisibility cannot
replace coefficient divisibility. The proof cites Algorithm 2.74 and
Magma script local_algebras.m; no computation was replayed. These rows
therefore supply neither an obstruction nor a realization for this target.
No row's algebra list is imported. General discriminant data already
used in L094 do not decide the simultaneous systems.

Reuse the earlier comparison of Putz's terminal exclusions and
Pacetti–Villagra Torcomian Theorems A–C from
`2026-10-18-ordered-three-five-eleven-rational-factor.md`: special
coefficients and the explicit prime-eleven exception respectively
prevent an applicable global exclusion. Dahmen's inaccessible provenance
page remains an unread nonessential lead; no theorem there is assumed.

The needed lifting inputs are already precisely cited and inspected in
`foundations/17-local-power-hensel-inputs.md` and
`2026-10-18-rational-factor-eleven-adic-solvability.md`:
Pete L. Clark, *Algebraic Number Theory II: Valuations, Local Fields and
Adeles*, [author notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf),
Theorem 1.79, printed p.58; and Gergely Zábrádi,
*Notes for the course p-adic methods in arithmetic*, 29 June 2022,
[author notes](https://zabradi.web.elte.hu/Jegyzetek/p-adic-meth-arith.pdf),
Lemma 2.3 and Theorem 2.4, printed p.4. Reuse unchanged theorem coverage:
for an integral polynomial over a complete discretely valued field,
v(F(alpha))>2v(F'(alpha)) suffices for the stated nearby exact root.
The multivariable version requires an error zero modulo p^n and a
partial derivative of valuation k with 0<=2k<n; it fixes other
coordinates and preserves congruence modulo p^(n-k). No unit derivative
is required by this version. Actual errors and derivatives still need
verification; a cube derivative at three must not be declared a unit.
No reproof or new specialization is performed this turn.

## Discovery scope and bounded continuation

Queries included `"Putz" "Table 5.17"`,
`"3-adic" "(3,5,11)" rational`,
`"generalized Fermat" "3,5,11" "local" rational`,
`"3t^2+t+1" "3-adic"`, and
`"55" "165" "594" "1215" cube Fermat`.
Relevant hits were the already assessed thesis and author's package;
unrelated arithmetic hits and snippets supply no theorem evidence.
This is bounded discovery, not a claim of exhaustive coverage or novelty.

Approve one bounded residue/valuation attempt on both systems. Begin
with residues modulo 27, retaining all m,u cases with C a unit. A finite
obstruction must cover the full allowed domain, not only fixed sample
coordinates. For existence, seek a seed satisfying the cited strict
Hensel inequality while preserving the defining C relation; use one
variable only after substitution, or an equivalent formulation that
retains both equations. If initial seeds are inconclusive, permit a
single bounded refinement through modulus 3^5, with a stated lifting
test; stop rather than repeatedly increasing precision. Nonzero exact
coordinates, C a unit, local pair primitivity, and both reconstructed
bases must be checked after lifting. Residue survivors alone are
inconclusive, and existence needs only one admissible exact tuple per
system, not a classification of all valuations. A complete residue
obstruction or an exact lift is the continuation/abandonment test.

This review approves methods and scope only. It produces no residue
calculation, local witness, obstruction, lemma or mathematical script.
Mathlib coverage of the full systems and supporting declarations is
not checked; unknown coverage is not evidence of absence.
