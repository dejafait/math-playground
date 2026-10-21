# Ordered (3,5,11) — proposed cited algebra interface

TARGET: Import Putz's degree-eleven Belyi-algebra restrictions at infinity, two and primes outside {3,5,11} for positive primitive A^3+B^5=C^11.
CHECKED: 2026-10-18
DECISION: IMPORT
SEARCH_EVIDENCE: Reuse the completed exact-signature comparison in drafts/literature/2026-10-18-ordered-three-five-eleven-coverage.md; the interface is stated explicitly in Putz's thesis and has no matching local import.
SOURCE_EVIDENCE: Putz (2024), DOI 10.5463/thesis.832, Section 5.2 p.165, Propositions 5.18–5.20 pp.168–169 (statements and full proofs), and Theorem 2.72 p.68 (hypotheses), https://research.vu.nl/ws/portalfiles/portal/367784086/Thesis_CasperPutz.pdf .
COMPARISON: The general propositions permit (1,1,1); Theorem 5.1 and its terminal exclusions do not cover that coefficient triple.
GAP: No global algebra elimination, complete enumeration or integer power lifting follows from this necessary interface.
REASON: A precise citation and applicability check suffice; no original reproof, new ramification calculation or mathematical script is needed.
SCOPE: Proposed KNOWN_IMPORTED application only, requiring separate approval before invocation; retain the entire product algebra and all source qualifications.

Use phi(t)=(3t^2+t+1)^5(1−5t), s=B^5/C^11, and source coordinates
(x,y,z)=(B,A,C), coefficients (1,1,1). The proposed application matches
positive nonzero coordinates, 0<s<1, the source gcd condition and odd
pairwise coprime coefficients. This comparison is not an executed import.

The requested cited interface is the entire degree-eleven etale algebra
Q[t]/(phi(t)−s), real completion R×C^5, unramified outside {3,5,11},
with unramified two-adic factor degrees among (10,1), (5,3,2,1),
(4,4,2,1). Each degree denotes the unramified extension of Q2 of that
degree, retaining multiplicity. Global irreducibility is not asserted.

Proof coverage inspected: 5.18 treats the three real intervals separated
by the branch values. The proof of 5.19 retains p not dividing xyz and
each of p|x, p|y, p|z, including the infinity chart. Its cited 2.72
requires monic integral f, unit leading coefficient of g, unit radical
discriminant and resultant, a prime-to-p common ramification index,
and positive parameter valuation divisible by that index. Import 5.19
itself; do not silently claim a fresh check of its normalizations.
Proposition 5.20 cites Algorithm 2.74 and `local_algebras.m`; cite its
computational conclusion without claiming independent replay or exact
realization of every listed possibility. No new proof is requested.

Inputs: original positive primitive equation and the primary propositions.
L029 may close unit cases separately; L002 is downstream context only.
No GRH, abc, class/rank data, complete field list or feasible Hunter
search is assumed. This necessary interface could support a separately
assessed global restriction. Continue only if all hypotheses and product
factors match; abandon any signature exclusion from this interface alone.
Mathlib full matching coverage and supporting declarations: not checked.
