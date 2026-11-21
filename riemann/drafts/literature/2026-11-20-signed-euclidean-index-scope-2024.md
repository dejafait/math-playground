# Signed Euclidean index mechanism — completed source comparison2025

TARGET: Review primary-source coverage for a coefficient-explicit signed Euclidean or subresultant condition that could bound the full Kuznetsov U_N family's eventual negative index by one, checking degree drops and singular cases before proposing one bounded actual-family test.
CHECKED: 2026-11-20
DECISION: EXPLORE
SEARCH_EVIDENCE: Located Lascoux–Pragacz's precise paper and read its primary decomposition hypotheses/proofs; inspected Heinig–Rost's stronger arbitrary-degree-drop factorization and complete inertia argument; checked the integer-input Sturm–Habicht scope. Exact Kuznetsov/Pollaczek plus Euclidean, subresultant, signed-remainder and Sturm searches supplied no matched family-specific sign theorem. This bounded search establishes no novelty or nonexistence claim.
SOURCE_EVIDENCE: Lascoux–Pragacz, Ann.Comb.9(2005),301–319, DOI10.1007/s00026-005-0259-1, author bez7.pdf Section2/Definition2 pp3–4, Lemma9/Theorem11/Proposition13 with proofs pp6–7; Heinig–Rost, Chemnitz2008-09 Section5.1–5.5, Theorem5.1/(5.1)–(5.5), Corollary5.2 and full reduction/homotopy argument, printed pp31–33; Emiris–Mourrain–Tsigaridas, Real Algebraic Numbers: Complexity Analysis and Experimentation, author emt-lncs-2006.pdf Section2, Definitions2.1–2.2/Theorems2.4–2.5/Corollary2.1, author pp4–6. Primary URLs and scope below; prior derivative-inertia coverage reused.
COMPARISON: The generic scalar remainder formula requires unit degree drops. The stronger block theorem handles arbitrary drops and gcd nullity, but still needs actual quotient degrees and signs. Neither inspected algebraic result provides those for Kuznetsov's coefficients; an integer-input root-count implementation is not a sign oracle for the actual pi-dependent coefficients. No bounded family-specific sufficient-condition test emerged.
GAP: C029m's eventual uniform negative index<=1 remains unpaid; no coefficient structure forces the generic or block signs. Actual-degree, exact-zero decisions, initialization and qualified weighted convergence/upstream[9] are separate. No derivative root count, nullity deletion, or finite signature supplies these missing quantifiers.
REASON: The primary-source comparison changes routing: the previously unread decomposition lead is now inspected, so its generic algorithm alone no longer justifies another finite computation. Park this unstructured signed-chain route; retain the formulas as reusable coverage if a concrete new coefficient constraint appears.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED lacked essential primary decomposition and singular-case coverage. This one literature-only step fills that scope; ready representation/inertia assessments were reused rather than browsed again.
SCOPE: Completed source review only. EXPLORE records the bounded absence of an adequate match, not approval of an unspecified sign calculation. No lemma, mathematical script, actual-family remainder or new mathematical result was derived. The earlier nomination below is preserved as historical context and is superseded by this completed comparison.

## Completed source comparison

The main gap remains L030–L032/C032a actual-Xi all-degree mixed
positivity. This review's intermediate target was a coefficient-explicit
signed-chain sufficient condition for C029m's full family. Such a
condition could support its eventual index premise; a root-count
algorithm with unspecified signs could not. The continuation test was
an explicit actual-family condition and a bounded discriminating test.
That threshold was not met. This is an informative source-scope negative,
not a counterexample to any possible signed-chain approach or to RH.

### Inspected primary decomposition

A. Lascoux and P. Pragacz, *Bezoutians, Euclidean Algorithm, and
Orthogonal Polynomials*, Annals of Combinatorics9(2005),301–319,
[DOI](https://doi.org/10.1007/s00026-005-0259-1),
[author manuscript,22pp](https://www.impan.pl/~pragacz/download/bez7.pdf).
Read Section2's signed recurrence, Definition2, and Lemma9/Theorem11/
Proposition13 with their complete displayed proofs, author pp3–7.
Their convention is R_(-1)=f, R_0=phi and
R_(i-1)=Q_i R_i-R_(i+1), with the same Bezoutian numerator order as
C029o. Theorem11 telescopes kernels weighted by divided differences
of Q_i. Proposition13 makes those weights scalar slopes for a
**general pair** of degrees(n+1,n): all subsequent drops are one.
That premise must be verified; it is not automatic for a derivative
pair. Higher-degree quotients give nonconstant divided differences,
not scalar positive weights. The stated scalar formula supplies no
sign law for the actual family. No extension through vanished pivots
or early common-factor termination is imported from this proposition.
The manuscript page numbering is used here, not journal pagination.

G. Heinig and K. Rost, *Bezoutians*, Chemnitz preprint2008-09,
[primary PDF](https://www.tu-chemnitz.de/mathematik/preprint/2008/PREPRINT_09.pdf),
Section5.1–5.5, printed pp31–33: read division step(5.1)/(5.2), signed
recurrence(5.3), Theorem5.1/(5.4)–(5.5) and Corollary5.2's full inertia
argument. For real polynomials u of actual degree n and v of degree at
most n, the nonsingular triangular congruence has a zero block of size
deg gcd(u,v) and quotient blocks B(q_i). Arbitrary quotient degrees
m_i are allowed. For leading quotient coefficient rho_i, the source's
nonsingular homotopy to rho_i J_(m_i) gives signature zero for even
m_i and sign(rho_i) for odd m_i; rank and signature determine inertia.
Thus degree loss and common factors do not require pretending all
scalar pivots exist. Quotient signs and degrees still require proof.
Taking u=U_N,v=U_N' is within this algebraic scope at its actual degree;
the theorem supplies no uniform signs for these inputs. The existing
comparison2013 covers basis congruence and derivative-Hermite inertia,
including distinct-pair versus algebraic-multiplicity qualifications.

### Subresultant algorithm scope

I. Z. Emiris, B. Mourrain and E. P. Tsigaridas, *Real Algebraic Numbers:
Complexity Analysis and Experimentation*,
[author manuscript emt-lncs-2006.pdf,26pp](https://who.paris.inria.fr/Elias.Tsigaridas/files/emt-lncs-2006.pdf),
Section2, author pp4–6. Read the signed-PRS/Sturm–Habicht definitions,
defective-sequence discussion, Theorems2.4–2.5 and Corollary2.1.
Theorem2.5 assumes coprime integer polynomials, squarefree f, positive
leading coefficient and endpoints not roots of f. It uses modified
variation, with consecutive-zero handling explicitly distinguished
from ordinary variation. Theorem2.4 states squarefree-part extraction;
it does not license counting multiplicities as distinct roots.
These cited algorithm statements are not proved anew here. Their
integer bit-complexity scope cannot be transferred without argument
to C029n's coefficients involving pi and sqrt(2); replacing them by
rational approximations changes the polynomial. No exact-zero test
or uniform sign bound for that coefficient family is provided.
This is an additional scope check, not an essential blocked source.

### Local comparison, search limits and route decision

Reused comparison2013's Heinig–Rost derivative-inertia assessment and
comparison2020's transformation scope; read C029m in full, C029o's
kernel convention, C029p's finite statement and the closed finite-audit
and affine-quotient stop records. C029q's independently audited stop
was supplied at startup. C029n's coefficient/enclosure inputs are
retained through those already assessed uses; no enclosure arithmetic
was rerun. The local search for Pragacz, subresultant and signed
Euclidean found the unread lead and the squarefree sextic nomination;
that is no novelty claim. No cross-notebook input was read.

Queries included `Pragacz Bezoutian Euclidean algorithm decomposition
signature`, exact `Pragacz Bezoutians` / `Pragacz Euclidean Bezout`,
`signed subresultant signature defective zero principal minors Sturm
Habicht theorem polynomial real roots`, and Kuznetsov/Pollaczek with
`subresultant`, `signed remainder`, `Sturm`, and the named authors.
Primary theorem hypotheses and relevant proofs were inspected before
larger passages. Generic search results and unrelated orthogonal-
polynomial abstracts were not theorem evidence. Further subresultant
papers and references inside the algorithm survey remain unread;
none was silently promoted to an actual-family sign theorem. PDF
screenshots returned references without image payloads; the inspection
uses legible indexed primary formulas, with no visual-verification claim.
All three primary PDFs were accessed20November2026 in the versions
identified above. Full matching Mathlib coverage remains unchecked.

The actual input retains all odd coefficients and U_N=T_N/S with
S=sin(pi/8)/sqrt(2)>0. A coefficient sign constraint controlling the
entire chain is still absent. Replacing the unpaid Hermite index by
its algorithmic expression, computing another isolated degree, assuming
squarefreeness, or dropping a singular part would fail the stated test.
Park this generic mechanism without degree/precision escalation; it
can reopen on a materially new actual-coefficient constraint with a
bounded test. The source obstruction does not prohibit other methods.

For routing only, a narrow search of C034p's existing audit assessment
and stop record found that audit1902 already completed despite the
compact overview's pending label. Do not nominate a duplicate audit.
No C034p proof or new mathematics was inspected. No ready new central
coefficient mechanism was established; a separate bounded source
discovery is nominated, not performed here. It must reuse this coverage
and the earlier stopped mechanisms, rather than repeat their approvals.

## Original nomination (preserved; superseded)

## Scope and mechanism comparison

The main target remains L030-L032/C032a actual-Xi mixed positivity.
C029m's eventual negative-index-at-most-one premise is an alternative
sufficient bridge, not an established estimate. Keep its full odd/even
coefficients and U_N=T_N/S, S=sin(pi/8)/sqrt(2)>0. A future source-based
coefficient condition could help only if its signs or structural
relations can be checked using these actual coefficients without
assuming the desired root count. No such condition is derived here.

Three mechanisms compared for routing, without new mathematics:

1. The prescribed affine quotient between U_6 and U_7: C029q's audited
   negative direction rejects its PSD residual. Park this fixed route;
   neither a higher degree nor a new precision is a different mechanism.
2. An unspecified unrestricted comrade metric of index at most one:
   C029n stops the boundary-supported ansatz, while C029o/p supply a
   full finite metric. Merely demanding a uniform suitable metric
   repeats the unpaid index gap and gives no new concrete test.
3. A signed Euclidean/subresultant decomposition internal to
   (U_N,U_N'): selected for primary-source comparison. Its prospective
   input is a family-specific coefficient relation, rather than a
   positive inter-degree residual or an unspecified low-index metric.
   The earlier comparison leaves the relevant decomposition lead unread.

The local sextic nomination1490 mentions classical Sturm endpoint
variation for a squarefree polynomial and requires its terminal
nonzero remainder to be checked. Only that matching paragraph was
read; no sextic theorem/proof or mathematical input is imported.
It does not assess this full tilted family or license ignoring degree
drops, repeated roots, identically vanishing pivots or common factors.
No duplicate audit of the present source target was found; this does
not establish novelty.

## One bounded review and its stopping test

Start from comparison2020's precise unread decomposition lead; verify
its bibliographic identity and retrieve the primary theorem hypotheses
and relevant proof cases before reading larger passages. Compare with
the already inspected Heinig-Rost derivative-Bezoutian interpretation
recorded in comparison2013/C029p. Read those narrow source notes as
needed; neither their exact statements nor a new theorem is asserted
from memory here. Check whether the decomposition counts negative
squares with explicit coefficient/pivot signs, including how it treats
degree loss and singularity. Do not silently replace singular cases by
a squarefree assumption or compare algebraic multiplicity with a
distinct-root count without justification.

Continue only if the review yields an explicit checkable sufficient
condition and one bounded test using C029m's actual coefficients, or
an informative source obstruction identifying why this mechanism
cannot supply it. A generic inertia/Sturm algorithm, a reformulation
of index<=1, or another isolated finite root count is insufficient.
If this lead is inaccessible or supplies only that equivalence, record
the limitation and park dependent mathematics without repeated access
attempts. Do not revive the stopped quotient pair or degree24 runtime.

Essential continuation inputs: C029m exact full family and qualified
analytic bridge; C029n normalization/enclosures; C029o kernel convention;
C029p baseline solely for comparison; C029q independently audited stop;
comparison2020's transformation scope and unread leads. Uniform signs,
actual-degree/singular control, initialization and C029m's qualified
weighted convergence/upstream[9] remain unresolved. No cross-notebook
input is proposed. Full matching Mathlib coverage is unchecked.

This is a newly nominated target and needs a separate literature-only
turn. No source is represented as newly inspected, no lemma is derived,
and no mathematical script for this mechanism has been written or run.
