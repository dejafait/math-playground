# Proposed shell test without the entire-incidence trial zero

TARGET: Test full anchored distance-five shell feasibility at L053's fixed pairs with nonnegative invariant triple coefficients, Boolean repetitions and only forbidden-distance zeros.
CHECKED: 2026-10-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 181 compared the changed shell-only scope with primary Polak and Schrijver statements, reusable spectral coverage, L053/L054/L055 and ATTEMPTS/035,036,037; exact-parameter and prescribed-distance searches found no inspected verdict for this slice. Queries and limits below.
SOURCE_EVIDENCE: Freshly read Polak arXiv:1703.05171v1 Section 1.1 (1)–(3), Proposition 1.1 and complete indicator proof, p. 2, and Section 1.2 averaging, p. 3; Schrijver author manuscript III.B (65) and its symmetric-difference justification, p. 7. Reuse foundations/04,09,12 and step 176 for the remaining inspected primary cases and full Johnson-product/Schur coverage.
COMPARISON: Known union matrices, orbit consistency and complete product spectra cover the shell-only specialization after releasing the incidence zero. L055 excludes only the restricted slice; the stronger source programs require conditions intentionally absent here. No inspected theorem supplies a verdict at these fixed pairs.
GAP: Verify the shell coefficient dictionary, represented unordered-orbit consistency and all spectral/Schur inequalities for one exact feasible shell certificate or exact dual contradiction; no global triple extension or new feasibility result is established in this review.
REASON: Essential coverage for the changed zero hypothesis and deliberately weaker shell-only scope is adequate; approve one bounded mathematical attempt using known tools, without reproof of the hierarchy or spectral theorem.

SCOPE: One fixed anchor and its full J(68,5) x J(956,5) shell; L053 fixed anchor/pairs and Boolean diagonal; nonnegative stabilizer-invariant distinct-triple entries with forbidden-distance zeros only; PSD of this entire anchored matrix. No off-shell PSD, full-incidence zero, actual-label zero or extra scalar condition.

## Preserved startup proposal

The following proposal records the pre-review state. Its pending-coverage wording is superseded by the completed source comparison below; its mathematical target and limitations are retained.

Main gap: arbitrary-center safety at 68 agreements, independently of
67-agreement safety. The proposed intermediate target is one finite
shell feasibility test. Its downstream use is to distinguish obstruction
from the fixed pairs and ordinary distance zeros from obstruction that
depends on the additional entire-incidence zero. This is a changed
hypothesis with a separately testable verdict, not a repetition of L055.

Essential inputs for comparison are L053's exact singleton/pair values,
L054's complete shell dictionary and L055's audited restricted exclusion,
plus foundations/04,09,12 and ATTEMPTS/035,036,037. Reuse adequate primary
coverage; search only for gaps in that coverage or relevant stronger
known results. No reproof of the spectral theorem is proposed.

Proposed scope to review: fix an anchor A and the full J(68,5) x J(956,5)
shell, retain L053's anchor and pair coordinates and the Boolean diagonal,
and allow nonnegative coefficients constant on stabilizer orbits for
distinct triples. Retain zeros caused by a pair at half-distance 1,...,4.
Release the entire-incidence zero; do not replace it with actual-label
nonsingularity zeros. Require the entire anchored shell matrix PSD.
This is deliberately a necessary shell relaxation: feasibility would
not establish a global unordered triple assignment, other principal
matrices, the full SDP, or an RS list. The assessment must specify any
necessary identifications rather than silently imposing extra constraints.

Continuation/abandonment test after separate approval: seek an exact
rational feasible shell certificate or a nonnegative exact dual
contradicting the fixed-pair Schur requirement. A successful shell witness
would park this shell alone as an exclusion diagnostic; an exclusion
would remove dependence on the full-incidence trial zero for this fixed
pair diagnostic. If neither is found in one bounded attempt, preserve the
precise unresolved constraint. Numerical solver status is insufficient.
No proposed calculation has been run in step 180.

Other pair moments, global consistency, representing measures, full SDP
values, a uniform useful bound, and common-center RS realization remain
open. Neither shell verdict alone settles 67/68 safety or the 955–957
bracket. Full matching Mathlib coverage is not checked.

## Completed source comparison — step 181

LITERATURE_REASON: Removing L055's load-bearing entire-incidence zero and dropping the all-anchor small-principal extension requirement changes the assessed hypotheses; this separate review covers exactly the saved shell-only target.

**Primary imports and applicability.** Polak, *Semidefinite Programming
Bounds for Constant-Weight Codes*, IEEE Trans. Inform. Theory 65 (2019),
28–38, DOI 10.1109/TIT.2018.2854800, inspected version
[arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1), 15 March 2017,
Section 1.1 (1)–(3), Proposition 1.1, p. 2, defines union-indexed PSD
matrices. Its complete indicator proof establishes the constant-weight
bound despite the displayed A(n,d) endpoint. The nonnegativity paragraph
retains lower-cardinality diagonals. Section 1.2, p. 3, permits averaging
only when every group image preserves constraints. Fresh inspection
confirms foundations/12; no hierarchy theorem needs reproof. At order
three the anchored shell is a retained principal submatrix, not the full
source program. The application uses binary supports, weight 68 and
distance 10, independently of RS field structure and tuple width.

Schrijver, *New code upper bounds from the Terwilliger algebra and
semidefinite programming*, IEEE Trans. Inform. Theory 51 (2005),
2859–2866, DOI 10.1109/TIT.2005.851748,
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
III.B (65), p. 7, preserves t-s together with permutations of the three
pair distances. The ensuing justification counts triples using all
three symmetric differences and the three-way symmetric difference.
This passage was freshly read. Thus distance multiset alone cannot
identify coefficients. Reuse foundations/04 and step 176's complete
III.A (57)–(59) extension/reset proof and III.B (60)–(67) comparison.
Both included/excluded-anchor PSD families and scalar upper/Frechet
conditions belong to a stronger program. They are not added here;
the qualified complement prefactor in (61) remains unused.

Reuse the inspected spectral inputs in foundations/09: Brouwer–Haemers,
*Spectra of Graphs*, [author preprint](https://homepages.cwi.nl/~aeb/math/ipm/ipm.pdf),
Theorem 2.7.1(i), p. 36, Sections 1.4.7 and 11.2, pp. 19,162–163;
Brouwer–Cioaba–Ihringer–McGinnis,
[arXiv:1709.09011v2](https://arxiv.org/pdf/1709.09011v2), Sections 1.2,
3 and 3.4, pp. 3,10,12. Both Johnson factors satisfy n>=2*5. Coverage
includes every relation and eigenspace, product eigenvectors, positive
multiplicities, the identity relation and constant projector. Schur
congruence inverts only the positive anchor scalar; singular lower
blocks are allowed. Releasing a zero changes coefficients, not these
source hypotheses. No spectral theorem needs reproof.

**Exact approved scope and verification obligations.** Fix one anchor A.
Use L053's rho, p_i and the full shell dictionary in L054. Each shell
index is {A,B}; anchor and repeated-union entries use their lower-order
moments. Distinct-triple coefficients are nonnegative and constant on
stabilizer orbits. Keep only zeros forced by a forbidden pair distance.
In particular the (2,3) product relation is free, not forcibly positive
and not zero by the old trial rule. Use the entire anchored shell matrix.

Represent a triple coefficient by its unordered union when it appears
more than once in this matrix; interchange of B,C cannot change it.
Any identification under another choice of anchor is required only if
that same unordered orbit is also represented in the retained shell
scope. Verify such identifications from the complete L053/L054 region
dictionary and the source permutation condition, rather than merging
all equal-distance triples. Do not require PSD of the other two anchor
principal matrices or construct off-shell moments as part of this test.
A shell witness carries no claim of a global unordered extension.

Reuse the fixed-pair Schur requirement recorded in L055, 4982733184/5
in its normalized constant coordinate. The remaining L055 dual is not
an approved certificate after releasing the zero: its previously checked
columns cover the smaller relation set. Research must check every newly
free column or independently build and verify a feasible witness. Retain
all product modes and exact normalization; neither solver status nor a
preview of spectral signs is evidence. A proposed certificate requires
complete rational checks and a written finite applicability argument.
No free-coefficient reduction, new bound or certificate was derived here.

**Search, duplicates and decision.** Searches on 12 October 2026:
`"constant weight" "fixed distance distribution" "semidefinite" triple`;
`"Schrijver" "Johnson" "shell" semidefinite constant weight codes`;
`"A(1024,10,68)"`; `constant weight codes semidefinite programming
prescribed distance distribution feasibility Schrijver triple variables`;
`"Johnson" "product" "Delsarte" "constant weight" linear programming`.
No exact-parameter verdict was retrieved. Primary Polak and Brouwer–Polak
formulations reappeared; additional search-only leads included ordered
triple distributions, doubly constant-weight LP refinements and spherical
distance-distribution SDP. These leads remain unread, are not theorem
evidence and are unnecessary for this retained necessary slice. No claim
of novelty follows from these searches.

Local comparison read L053's fixed pairs, complete regions, Boolean
cases and principal matrices; L054's shell dictionary; L055's hypotheses,
averaging, relaxed shell equations and dual; ATTEMPTS/035,036,037; and
the ready step-176 assessment. The old stops concern, respectively,
small principals, a fixed product formula and free triples with the
entire-incidence zero. None decides this target. Existing work is retained.

Decision: SPECIALIZE. One bounded shell-only certificate attempt is
ready. An exact feasible witness parks this shell as an exclusion
diagnostic; an exact contradiction removes dependence on the extra
trial zero for these fixed pairs. If neither is obtained, preserve the
specific unresolved constraints and report EXPLORATION. Other pairs,
global extensions, actual-label constraints, full SDP values, uniform
bounds, representing measures and RS realization remain open. The
955–957 bracket and independent 67/68 safety gaps are unchanged.
Full matching Mathlib coverage remains not checked.
