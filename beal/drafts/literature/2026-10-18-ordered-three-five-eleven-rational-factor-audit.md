# L095 critical-audit coverage

TARGET: Critically audit L095's two-system rational-factor reduction, including exceptional denominator valuations and both converses.
CHECKED: 2026-10-18
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the bounded exact/stronger-statement searches in 2026-10-18-ordered-three-five-eleven-rational-factor.md; read histories 316–317 and the L095 proof for audit scope, finding no intervening independent audit or changed theorem requirement.
SOURCE_EVIDENCE: Reused inspected Putz (2024), DOI 10.5463/thesis.832, Section 5.2 p.165 and pp.167–173, and Pacetti–Villagra Torcomian Theorems A–C pp.4–5 through the prior assessment; read L093 including its application audit, and L095's hypotheses, claimed systems and proof-input declarations. No fresh external retrieval or certificate replay was performed.
COMPARISON: The prior assessment covers the unchanged coefficient-one cover and elementary reduced-root methods; L095 adds no modular or curve-classification input. Its exact two-system equivalence is not supplied by the inspected sources and must be independently checked rather than imported.
GAP: L095's unbounded exceptional valuations, exact complementary equation, integrality and both primitive converses remain unaudited; neither system's emptiness nor the other algebra branches are settled.
REASON: Coverage is adequate for this narrowly scoped independent audit, using the prior search rather than repeating discovery; EXPLORE permits checking an uncovered elementary specialization without asserting originality or correctness.
LITERATURE_REASON: The saved target changed from constructing a rational-factor reduction to independently auditing newly written L095; this separate review compares its actual inputs with the ready prior coverage, as required by the pending gate.
SCOPE: Exactly TARGET, with L093 and the original positive primitive A^3+B^5=C^11 as inputs; elementary rational-root, gcd, valuation, unique-factorization and polynomial-identity methods, including the full supporting certificate. No branch exclusion, curve-point classification or new global theorem is approved.

## Reused primary comparison and source limits

The ready assessment
`2026-10-18-ordered-three-five-eleven-rational-factor.md` records the
queries, versions, primary passages and inspected proof cases. Its
coverage is reused unchanged; this turn does not claim to have reopened
those external sources. P. H. C. Putz, *Enumeration of local and global
étale algebras applied to generalized Fermat equations*, VU Amsterdam
thesis (2024), version of record, DOI
[10.5463/thesis.832](https://doi.org/10.5463/thesis.832),
[primary PDF](https://research.vu.nl/ws/portalfiles/portal/367784086/Thesis_CasperPutz.pdf),
Section 5.2 p.165 supplies the exact cover. Propositions 5.18–5.20,
pp.168–169, supply L093's necessary algebra interface under the
coefficient-one substitution; L093's recorded independent application
audit retains every coordinate-divisor case. Its computational
Proposition 5.20 remains imported without replay.

Putz's Remark 5.13 p.167 and global cases pp.170–173 do not supply a
coefficient-one rational-factor exclusion. In particular Proposition
5.27's (10,1) exclusion retains special coefficient hypotheses. The
prior assessment also inspected A. Pacetti and L. Villagra Torcomian,
*On the generalized Fermat equation of signature (5,p,3)*,
[author-hosted 42-page version](https://sweet.ua.pt/apacetti/papers/3rp.pdf),
Theorems A–C pp.4–5: their prime exceptions include 11, with additional
conditional hypotheses in C. Those statements cannot replace this
audit. The author's GFE/3511.m local-family routines supply no inspected
global rational-root solver. Dahmen's thesis p.24 remains an unread
provenance lead, nonessential because the cover is available in Putz.
No new theorem from that lead is used.

## Audit-input comparison, not an audit verdict

Reading L095 to identify its methods finds four tasks already inside
the prior scope: (i) rational direct factor versus reduced rational root
using the polynomial Chinese remainder theorem and L093's etaleness;
(ii) denominator valuations using both original power equations;
(iii) exact polynomial and integer-factorization steps; and (iv)
reconstruction with positivity, reducedness and primitivity. The
standard named inputs are the Chinese remainder theorem for coprime
polynomial factors over a field and unique factorization in Z. Their
use needs no new classification theorem. The solution-specific
specializations still require proof checking; readiness does not certify
their correctness. An elementary independent reconstruction is justified
because no matching coefficient-one two-system theorem was found in the
reused bounded comparison, and the new proof is the object being audited.

L094 is context only, not an essential mathematical input. Histories
316–317 distinguish the source comparison and original construction;
no completed independent audit is recorded there. Historical affine and
fixed-tuple stops concern other mechanisms and are not being reopened.
The thirteen-check certificate was not replayed or treated as evidence
for the valuation arguments in this literature turn. Full Mathlib
coverage of L095 and supporting declarations remains **not checked**;
no absence or formal-verification claim is made.

## Bounded next audit and decision test

The main gap remains global elimination and integer power lifting for
residual signatures. The intermediate target is to secure or correct
this exact rational-factor equivalence. If valid, it supplies explicit
simultaneous power systems for future branch analysis; it leaves other
global factors and the emptiness of these two systems independent.

For the separate research audit, retain L093, the original positive
primitive equation and proposed L095, and inspect the complete relevant
identity certificate. Check all denominator cases at 3 and 5, including
unbounded cancellation when v3(n)=1 or v5(n)=1, zero valuation of s,
primes dividing C including eleven, both complementary cube equations
and both converses. Compare the full certificate with the actual
identities and hypotheses; a passing finite check cannot substitute for
unbounded arguments. Accept the exact equivalence only after these
checks, or give a concrete defect and its scope. A defect may permit a
local correction; otherwise park the defective reduction. No emptiness,
irreducibility, complete field list, height bound, abc, GRH or global
integer lift may be assumed. This turn performs only the coverage review,
with no mathematical audit verdict, new lemma or calculation.
