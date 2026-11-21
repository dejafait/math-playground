# Three-width variation control — review1875 of nomination1874

TARGET: Assess whether quantitative ECT interpolation estimates can certify sum_i |a_i|<=2 for C034j's exact three-width matching solution with C033w's residual transform, without assuming conditioning or changing the laws.
CHECKED: 2026-11-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1875 completed bounded quantitative interpolation, conditioning, signed-weight/TV and exact-expression searches; checked overlap1797 and cost-stop1798 as well as1789/1747 and stops1839/1843/1847/1866. Queries and actual reads are in drafts/literature/2026-11-20-laplace-three-width-variation-source-notes-1875.md; no novelty is inferred.
SOURCE_EVIDENCE: Reused1838/1745 and checked de Boor, Divided Differences, SAT1(2005), pp60-61, Proposition43 with proof, Corollary(44), determinant formula(45), https://pages.cs.wisc.edu/~deboor/sat/papers/2/2.pdf ; reused1797/1838 and checked Rump, Acta Numerica19(2010), internal p53, Theorem10.2/proof(10.8)-(10.9), https://www.tuhh.de/ti3/rump/intlab/ActaNumerica2010.pdf ; inspected Cuyt--Ibrahimoglu--Yaman2011 Sections1.1-1.3 pp1917-1918, DOI10.1063/1.3636987, author PDF and scope in source-notes1875.
COMPARISON: ECT alone gives no cap. Rump already covers conditional verified solution bounds, but1798's scalar implementation remains stopped. De Boor supplies an analytic determinant tool after a checked monotone reparametrization using C034b/i's now-audited margins; polynomial Lebesgue estimates do not directly bound this transposed weight problem. No inspected source gives cap2 for the exact residual.
GAP: The analytic specialization must justify its change of variable, quantitative determinant/cofactor bounds and compact-excision residual allowance, then compare with sum_i |a_i|<=2. These obligations, actual weights, conditioning and feasibility remain unproved; no small residual or determinant identity is asserted here.
REASON: The saved changed target required its first quantitative comparison. Review1875 resolves that source gate and nominates one analytic cap test, avoiding the duplicate solver setup and stopped evaluator. No mathematics is derived; the new continuation receives separate approval before research.
LITERATURE_REASON: Essential coefficient-control coverage was missing from qualitative assessment1872; reuse1838/1745/1797 while checking the changed cap target and de Boor application scope.
SCOPE: Exact C034j widths (1,3/2,2), columns (1,k(1,sigma),k(2,sigma)), M^T a=(1,m(1),m(2))^T, and C033w's unchanged qualified laws and removed Levy interval. No full-observation matching, global inverse-Laplace theorem, source-wide validation or actual-Xi realization is included.

Literature-only review1875 completes this nomination. Full source scope,
essential proof cases, duplicate/failure evidence and unpaid application
obligations are in
[source-notes1875](2026-11-20-laplace-three-width-variation-source-notes-1875.md).
The analytic test in
[assessment1875](2026-11-20-laplace-three-width-analytic-cap-test-1875.md)
needs separate approval before research. No coefficient bound is derived.
Do not repeat unchanged ECT discovery or audit1874 to fill a quota.

The intermediate use would be testing whether the verified algebraic
solution belongs to C033w's capped class for the two selected observations.
The main L030-L032/C032a positivity gap, full observations, signed
height/cancellation and actual-Xi realization would still be independent.

Continuation test: find a criterion with checkable input bounds for this
exact solution and the cap2 threshold, or document why available qualitative
prefix signs and residual information do not suffice. If essential
conditioning or residual bounds cannot be supplied, preserve that obstacle
and nominate an independently testable target rather than repeating scalar
allocation or an unsigned enclosure. Failure of this particular three-site
solution to meet cap2 would not exclude other width supports or prove a
positive full minimax gap. No such failure has been found here.

Essential local inputs are C034j/audit1874, C033w and C034b/i with their
existing audits; preserve the analytic/law interface C032m/n, C033l/C032q
and C034c/h, C034d/e/f. Retain all labels/conjugates/multiplicities,
ordinate0 exclusion, gamma>14, strict strip/count, displacement zero
through100, real zero in (14,15), reciprocal-square tail, heat positivity,
separate fixed-j=0,1 errors, both fixed-v1 sources, zero drift/killing
and half-variance. Signs are on [1,2]; the larger interval supplies
regularity only. C034g remains unused. Source-wide/finite-zero validity
and matching Mathlib coverage remain unverified; no global Sobolev bound.

The finite interpolation input does not yet provide a bounded new central
signed-height or realization mechanism. That absent interface blocks a
justified creative nomination here; routine quantitative interpolation is
not relabeled creative. Preserve the existing discovery and route stops.
