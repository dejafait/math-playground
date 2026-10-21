# Incidence coordinate norm certificates — source comparison complete

TARGET: Construct and independently verify the full rank-seven B-relative multiplication operators for L074's two point coordinates and their determinant norms.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the adequate 2026-10-16 seven-incidence assessment and scoped searches of L066/L074, the quotient-fiber construction/audit assessments, history/269 and history/271, and ATTEMPTS/035/036/039; searched finite-free determinant norms, Schaefer--Stoll incidence norms, commutative-Q-algebra characteristic-polynomial algorithms and Mathlib norm coverage. Exact queries and inspected sources are recorded below.
SOURCE_EVIDENCE: Schaefer--Stoll author long version 2001-06-13, Section 2 p.3, Section 3 p.5 and Proposition 7.10 with preceding incidence proof and following matrix paragraph p.19; Stacks Lemma 31.18.6 tag 0BD2, complete statement/proof; Christian Bär, arXiv:2008.04247v3, manuscript dated 2021-08-06, Section 2.1 pp.3--4 equations (1)--(6), Section 2.2 p.5; Mathlib Algebra.norm_eq_matrix_det, Algebra.norm_algebraMap_of_basis and Matrix.det_succ_row_zero, current documentation inspected 2026-10-17.
COMPARISON: Known results cover the norm and two independent determinant methods over the entire commutative Q-algebra B without fieldness. Audited L074 supplies the actual global seven-element basis and specified projection pullbacks. A citation does not supply this fixed model's 98 B-valued matrix entries, two full norms or independent finite replay; those are the only remaining specialization tasks approved here.
GAP: The two coordinate multiplication matrices and exact determinant certificates remain uncomputed. Their full coefficient comparisons, independent replay, rejection tests and preservation must pass the fixed caps below. No global power-class, arithmetic descent or Selmer conclusion is approved.
REASON: This separate literature step closes the exact full-coefficient-ring and independent-determinant coverage missing at invocation start. The unchanged target is ready for one RESEARCH / REPRODUCTION implementation attempt, with no general norm reproof or renewed source search.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED explicitly requested comparison of this new norm target; the completed incidence-audit assessment excluded norm construction. Reuse the general incidence assessment and inspect only the missing exact specialization/verification sources.
SCOPE: Exact TARGET only; short coordinates X and Y on L067's conductor-389 curve at seven, L074's entire I/B, both V components and all direction embeddings, full rational transports, both 7-by-7 matrices and two norms. No arbitrary-power-class certificate, field-factor selection, L069 or stopped column computation.

The main gap is arbitrary-curve rank equality at complex analytic order at
least two. The intermediate target is the two full 7-by-7
multiplication operators over B and their determinant norms for the short
point-coordinate images X and Y in audited L074. These could provide an
initial verified norm implementation for the incidence condition used in
L066's conditional descent enclosure. No claim is made that testing these
two elements certifies norms on arbitrary power classes or supplies a
cohomology/descent condition.

Use L074 with complete incidence-269 and successful incidence-audit-271
evidence, and its accepted L067/L070/L071/L072/L073 inputs. Both source
coordinate transports, all 48 rational B coordinates, both V components
and all direction embeddings must remain. B fieldness is not available.
The source match below retains the correct projection and ordinary-dual
indexing. This assessment approves implementation, not its result.

## Primary results and precise applicability

Schaefer--Stoll, *How to do a p-descent on an elliptic curve*, Trans.
AMS 356 (2004), 1209--1231, DOI 10.1090/S0002-9947-03-03366-X;
numbering here is exclusively the
[author long version dated 13 June 2001](https://www.mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf#page=19).
Section 2 assumes an odd p over a number field; Section 3 permits products
of separable fields. Proposition 7.10 and its proof identify the map as
point pullback followed by norm along the line projection. The following
paragraph computes it by a multiplication matrix over the line algebra.
Thus K=Q,p=7 and L074's specified all-fiber identification apply without
a full residual Galois-image premise. The source's incidence algebra D
is our I; its B is our entire line algebra B, not L070's direction D.
L072's inverse ordinary-functional indexing and Cartier convention stay
in force. These statements and the relevant proof paragraph were inspected;
the ready general incidence assessment supplies unchanged earlier coverage.
The explicit p=3 slope example is not used for p=7.

[Stacks Lemma 31.18.6, tag 0BD2](https://stacks.math.columbia.edu/tag/0BD2)
assumes a finite locally free morphism of constant degree d>=1. Its
canonical norm is the determinant of multiplication on a local free
basis and commutes with arbitrary base change. The inspected proof checks
basis independence and the vanishing property over a residue field; it
does not assume the original base is a field or domain. L074 gives the
global B-basis (1,X,...,X^6) and finite etaleness, so Spec(I)->Spec(B)
meets these hypotheses with d=7. In particular the determinant makes
sense for any element, without proving that the element is a unit.
Power-class applications later require units separately.

For an independent determinant method use Christian Bär,
[*The Faddeev-LeVerrier algorithm and the Pfaffian*](https://arxiv.org/pdf/2008.04247v3#page=3),
arXiv:2008.04247v3 (revision 2021-08-05; PDF dated 2021-08-06), published
in Linear Algebra Appl. 630 (2021), 39--55. Section 2.1, printed pp.3--4,
explicitly assumes a commutative Q-algebra R and a matrix A of size n.
Equations (1)--(6) give N_1=Id, c_k=-tr(A N_k)/k,
N_(k+1)=A N_k+c_k Id, with c_0=1,
det(t Id-A)=sum_(k=0)^n c_k t^(n-k), c_n=(-1)^n det(A), and
N_(n+1)=0. The proof uses the adjugate identity and formal Jacobi formula,
then compares coefficients; singular matrices and zero divisors do not
require an inverse. Section 2.2's code is illustration only: use exact
rationals, not its NumPy machine arithmetic. Set R=B,n=7; the only
divisions are by 1,...,7, units in this Q-algebra. Import this algorithm,
without a new characteristic-polynomial or norm theorem.

The producer may use recursive Laplace expansion with memoized minors,
a different exact determinant algorithm. Its ring-general identity is
[Mathlib Matrix.det_succ_row_zero](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/Determinant/Basic.html#Matrix.det_succ_row_zero),
with Matrix.det_fin_zero for the empty minor. The inspected statements
require only a commutative ring. Use inherited row/column order for every
minor and its cofactor sign; caching identical ordered minors changes no
formula. This avoids division by a possibly nonunit matrix entry.

No closed coordinate-norm formula or new identity is derived in this
literature turn. The matrix-column specification below is the imported
definition of multiplication in L074's already proved basis.

## Duplicates, recorded stops and source search

Reuse `drafts/literature/2026-10-16-conductor389-seven-incidence-maps.md`
for the general source search, known norm construction and software
comparison. Its broader target included norms, but the subsequently
completed quotient-fiber construction and audit expressly did not.
L074 and history/269/271 confirm this; L066 still has only a conditional
power-class interface. No fixed coordinate-norm certificate appears in
these checked passages or the norm/incidence assessment filenames. This
is a scoped duplicate check, not a novelty or global absence claim.

ATTEMPTS/035 and /036 concern stopped uncompressed/compressed translation
columns. The present method operates on L074's already audited rank-seven
monic presentation and does not resume either route. ATTEMPTS/039's parser
failure and its preserved repair are retained. No repeated blocker is
being relabeled as a new mechanism; arithmetic cost of the new determinants
is genuinely untested.

Queries on 2026-10-17 included `site.stacks.math.columbia.edu finite
locally free algebra norm determinant multiplication resultant`,
`Schaefer Stoll how to do a p descent elliptic curve incidence norm lines
2001`, `site.math.mit.edu characteristic polynomial Newton identities
traces matrix Faddeev LeVerrier`, and `site.leanprover-community.github.io
mathlib4_docs Algebra norm determinant finite free Algebra.norm`.
The Faddeev--LeVerrier lead was followed to Bär's complete primary
Section 2 derivation, not accepted from a snippet. Gantmacher and other
search leads were not inspected and are not inputs. No broader
descent literature refresh is needed for this exact finite target.

## One bounded implementation and discriminating test

Use accepted L067/L070/L071/L072/L073/L074 and the complete
`scripts/seven-torsion/incidence-269/` and successful
`scripts/seven-torsion/incidence-audit-271/` evidence. Accept the existing
upstream audits; do not repeat all earlier constructions. Before costly
work, save the input paths/hashes, unfinished design and caps in a draft.
Create fresh artifacts under `scripts/seven-torsion/coordinate-norm-273/`
(or a fresh unoccupied directory if that name has been taken).

1. Reconstruct the entire B and I from the audited h,k,c',F and y-factor.
   Keep the full ordered bases Z^j T^i V^e and Z^j T^i V^e X^r of L074.
   Use both short point-coordinate images X and V*y_f. Column r of each
   operator is the full normal form of that coordinate times X^r for
   r=0,...,6. Save all 49 entries for each matrix, including every zero
   and all 48 rational coordinates of each B entry: 4704 rational slots
   across the two matrices. Save each determinant in all 48 coordinates.
   Check the corresponding short/original coordinate transports and both
   complete 48-column point bases against the accepted L074 evidence;
   do not substitute one chosen embedding or retain only the even part.
2. Produce both determinants by Laplace expansion. An independent
   verifier must reconstruct all columns with separately implemented
   rational tower arithmetic (for example sparse convolution versus
   fixed-length Horner reduction), importing no producer arithmetic.
   Compare every coefficient, with the existing full basis transports,
   then compute both determinants using Bär's recurrence over all B.
   Save every c_k and N_k, the terminal zero matrix and the two full
   determinant comparisons. Inspect their complete relevant evidence.
   The terminal zero matrix alone is not a determinant certificate.
3. As bounded convention controls, verify the scalar-multiplication
   case for 2 and the zero element using the imported rank-seven norm
   convention. Include three explicitly limited altered-evidence tests:
   change one B coefficient of a coordinate matrix; change one coefficient
   of a saved norm; omit the odd-V coefficient block. They must fail the
   full matrix comparison, full determinant comparison and full-basis
   shape check respectively. These are named-condition tests unless
   complete fresh malformed replays are actually performed; do not call
   a missing basis block a geometric sign selector.
4. Fix two stages before invocation: one construction stage <=180 seconds
   and one independent verification stage <=180 seconds, each with an
   external <=181-second watchdog. Verification includes reconstruction,
   the distinct determinant algorithm and the three limited rejections.
   The combined new directory is capped at 134217728 bytes, including
   reports/logs. No retry, cap extension or retrospective subdivision.
   Inventory accepted upstream/original files before execution, including
   every path in the successful 379-file audit inventory and the original
   incidence-268/269 evidence; preserve hashes. Print only actual/required
   bounds, failures and evidence paths. A timeout is an honest cost stop,
   not permission to approve a partial coordinate or selected fiber.

Continue only if both full operators and determinant norms pass, all
required evidence is complete and originals are preserved. Stop at the
first failed identity or cap, saving the partial evidence and reason.
Even success certifies only these two fixed coordinate norms. A later
arbitrary-input norm implementation and its application to a complete
global power-class basis need their own exact scope and review; norms of
two coordinates do not determine norms of sums or certify descent.

## Mathlib and remaining limits

[Algebra.norm_eq_matrix_det](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Norm/Defs.html#Algebra.norm_eq_matrix_det)
matches the generic multiplication-determinant statement with a finite
basis over a commutative base ring; the inspected signature does not
require a base field. Algebra.norm_algebraMap_of_basis supplies the
scalar convention. Matrix.det_succ_row_zero and Matrix.det_fin_zero
support the first algorithm. These are supporting/full generic theorems,
not a formalization of this fixed incidence certificate. Matching Mathlib
coverage for the explicit algebras, transports and independent replay
has not been checked; no absence claim is made.

Descent functions, complete global units/classes, local identifications
and upper bounds, Selmer containment, other L026 premises, a successful
localization, rational membership, divisible-Sha removal and arbitrary
complex-order comparison remain independent unresolved obligations.
No norm values, new lemma, mathematical script or change to the argument
overview/DAG was made in this literature-only step. The previous
REVIEW_REQUIRED proposal is now approved only in the bounded scope above.
This is local source-readiness progress using known methods, with no
claim of progress beyond the sources or of a BSD candidate.
