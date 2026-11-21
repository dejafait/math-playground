# Singular Hermite limit transfer: source assessment2005

TARGET: Audit the conditional transfer from Hermite negative index at most one to at most two distinct nonreal zeros of the nonzero compact limit, allowing singular approximants.
CHECKED: 2026-11-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searches for locally uniform limits with bounded distinct nonreal zeros and Hermite negative index; scoped Pollaczek duplicate/failure checks, with source details below. No originality claim.
SOURCE_EVIDENCE: https://rtca2023.github.io/pages_Paris/files_m5/rag-ihp.pdf Theorem1.1 and complete proof pp3-4; https://math.berkeley.edu/~avizeff/complex_analysis_S26/lecture_23.html Rouché theorem and full proof, April22,2026. Reuse source-review2001 for Hermite multiplicity qualifications and convergence-source-review2004 for Kuznetsov p568.
COMPARISON: Classical Hermite root counting and Rouché supply the inputs; the separate task is their explicit conditional applicability to distinct zero counts under compact convergence, including singular polynomials. This is standard specialization, not a new central mechanism.
GAP: Write the finite-disjoint-disc applicability argument and check all quantifiers, nonzero limit, actual degree, real coefficients, and distinct versus algebraic counting. No uniform index estimate is supplied or licensed.
REASON: The supervisor requires a different target after repeated recovery. Singular distinct-root transfer is independently testable without runtime or finite-weight identities; it identifies the root-count hypothesis that a future central mechanism must establish.
SCOPE: Nonconstant real polynomials p_j of their actual degrees, j tending to infinity, converging uniformly on every compact subset of C to an entire F not identically zero; their ordinary Newton-sum Hermite matrices have negative index at most one eventually. Test the conclusion that F has at most two distinct zeros in C\R. Repeated roots and arbitrary nullity are allowed; no bound on nonreal algebraic multiplicity is proposed.

## Primary theorem coverage

Daniel Plaumann, *Real Algebraic Geometry*, IHP lectures, October2023,
Theorem1.1 pp3-4: for a monic real polynomial, Hermite rank counts
distinct complex roots and signature counts distinct real roots.
The inspected proof treats repeated roots with positive multiplicities,
using independent evaluation vectors and real/imaginary parts for
conjugate roots. It includes the singular case. Its signed decomposition
records one negative direction per distinct conjugate pair. Monic
normalization and actual degree must be checked in the specialization.
This is the same source as review2001, not a fresh mathematical discovery.

Berkeley's *Complex analysis, lecture2*, Lecture23, April22,2026,
Rouché theorem (unnumbered, immediately following the argument-principle
example): analytic functions on a bounded domain and its boundary,
with strict perturbation domination on the piecewise smooth boundary,
have equal zero counts with multiplicity. Read the complete proof:
relative perturbation stays in the right half-plane, contributes no
argument increment, and the argument principle gives equality.
The planned application must use discs with analytic neighborhoods and
zero-free boundaries. The source does not require simple zeros.
No general theorem reproof is needed.

## Comparison and precise deferred test

Compared three mechanisms against the recorded stops:

1. Retry degree24 certified inertia: parked by runtime-park2003;
   no changed runtime evidence permits reopening.
2. Finite-weight summability specialization2004: exact known limit
   already covered; source URLs repaired, but current recovery routing
   explicitly requires a different action. No mathematical disproof of
   this unfinished specialization is asserted.
3. Conditional distinct-root transfer with singular Hermite matrices:
   selected. Tests a separate analytical interface, without installing
   packages or deriving Jensen-weight identities.

Next research should test finitely many distinct nonreal limit zeros
using disjoint discs wholly outside R, simultaneously control their
boundaries from compact convergence, and compare the distinct counts
with the imported Hermite theorem. This is a proposed applicability
check, not a proof performed in this literature turn. Continue only
if every disc and eventual-index quantifier is justified; otherwise
record the failed hypothesis. Root collision cannot simply be ignored.

Potential use: specify whether simplicity is actually needed for a
future one-pair mechanism. The actual tilted family would still require
its uniform negative-index bound; finite numerical evidence supplies
none. Kuznetsov's exact compact limit may be imported from p568 as
recorded2004, without redoing the parked summability target. Conversion
of a distinct-count conclusion into RH, including imaginary-axis and
symmetry cases, is outside this assessment and needs separate coverage.
L030-L032/C032a remain open; C028b/d/f/C029j are context only.

Scoped local checks: source-notes2000, inertia-source-review2001,
convergence-source-review2004, named Pollaczek ATTEMPTS and current
November20 Pollaczek histories. The notes record no completed singular
limit-transfer proof. Search absence does not certify novelty.
Queries: `polynomials locally uniform limit bounded number distinct
nonreal zeros Hurwitz Hermite matrix negative index`;
`site.jirka.org/ca Rouché Hurwitz theorem`;
`Kuznetsov Meixner zeros Jensen 2008`.

Access qualifications: Coste's already-inspected source timed out on
reaccess; Plaumann was accessible and suffices, so no dependent source
block remains. Toronto MAT354 residue/Rouché PDF returned almost no
extracted theorem text; screenshot references had no image payload.
It is not imported. DLMF1.10 contained neither searched theorem name;
DLMF25.10 provides symmetry context only and is not an input to this
narrow transfer target. Other search hits remain unread leads. No
upstream source audit or new mathematical conclusion is claimed.
Mathlib full-result/supporting coverage unchecked. No lemma, DAG,
PROOF or mathematical script changes in this source-review step.
