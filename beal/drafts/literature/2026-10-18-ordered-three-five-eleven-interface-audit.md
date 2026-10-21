# L093 — proposed critical application audit

TARGET: Critically audit L093's cited coefficient-one application, entire product factors and ramification scope for ordered (3,5,11).
CHECKED: 2026-10-18
DECISION: IMPORT
SEARCH_EVIDENCE: Reuse the unchanged primary scope and duplicate comparison in drafts/literature/2026-10-18-ordered-three-five-eleven-coverage.md and the executed-target assessment in drafts/literature/2026-10-18-ordered-three-five-eleven-algebra-import.md; no broader theorem is requested.
SOURCE_EVIDENCE: Putz (2024), DOI 10.5463/thesis.832, Section 5.2 p.165, equation (5.2) and Propositions 5.18–5.20 pp.168–169; primary version-of-record statements and full relevant proof cases inspected at https://research.vu.nl/ws/portalfiles/portal/367784086/Thesis_CasperPutz.pdf .
COMPARISON: Audit only the existing known-result specialization in L093; the source covers coefficient one and the complete two-adic products but supplies no global exclusion here.
GAP: Independent critical application review of L093 is outstanding; no global elimination or integer lifting is covered.
REASON: An audit of a cited application uses the same exact hypotheses and sources; no new mathematical result, source algorithm replay or extension to terminal exclusions is proposed.
SCOPE: Approved KNOWN_IMPORTED proof audit of the unchanged target; approval completed in the separate literature turn beal-2026-10-18-310-interface-audit-coverage-approval.
LITERATURE_REASON: Supervisor requires separate approval of the newly written continuation; review its source scope without executing the mathematical audit or expanding the target.

Check the exact source definition of S and gcd(ax,by,cz), the coordinate
interchange (B,A,C), nonzero coordinates and odd pairwise coprime
coefficients (1,1,1). Check s lies strictly between zero and one and the
source discriminant gives etaleness of the entire degree-eleven quotient.
Retain all real and two-adic factors, including the two degree-four copies.
Check that Proposition 5.19 covers coordinate divisors and the infinity
chart, and retain the computational-import qualification for 5.20.
Do not audit or claim an independent proof of the source computation.
Do not use the narrower Theorem 5.1 or infer global irreducibility.

Inputs: L093 and Putz's cited propositions. L029 and L002 are context,
not required inputs. No other local lemma, cross-notebook theorem,
abc, GRH, field list or integer-power lift is assumed. Pass only if the
whole stated necessary interface follows; record and repair any mismatch.
This assessment does not itself perform the independent audit.
Mathlib coverage remains not checked.

## Separate coverage approval — 2026-10-18

Reused both named assessments and checked L093 and histories 308–309.
The import already exists; this continuation requests its critical audit,
not a duplicate lemma. Reopened the version-of-record primary PDF at
printed pp.165,168–169 (PDF pages 171,174–175), reading the definition
of S, equation (5.2), all three proposition statements and their complete
proofs. Proposition 5.18 assumes nonzero pairwise coprime coefficients
and membership in S; 5.19 additionally excludes primes dividing
3·5·11·abc. Its proof handles no coordinate divisor, x, y and z,
the last through the reciprocal polynomial. Proposition 5.20 adds odd
abc, lists the entire three products including both degree-four factors,
and cites Algorithm 2.74 with local_algebras.m. Section 5.3 then
explicitly returns to the special coefficient set C.

These inspected passages cover the proposed audit's source needs.
No new theorem search, computational replay or original reproof is
needed. The source's expensive coefficient-one search warning remains
recorded in the reused coverage assessment; this audit neither reopens
that search nor extends terminal exclusions. The next research turn
must independently check L093's application and record pass or repair.
This is coverage approval only: no audit verdict or new mathematical
input is claimed. Reaffirming the existing IMPORT decision is STALLED
under the shared outcome rule, although the separate approval gate is
now satisfied. No lemma, script, PROOF.md or DAG.md changed.
