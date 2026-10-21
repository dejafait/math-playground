# Affine-plane affine-system rank attempt

Approved target: Determine whether L072's sixteen-support family can be realized by an L010 equality pencil for any bijective H-labeling over F_(97^20).
Reused ready assessment: `drafts/literature/2026-10-12-affine-plane-equality-realization.md` (EXPLORE).

Main local gap: exclude sixteen actual bad parameters; fifteen is required.
Intermediate target: resolve the affine-system rank drops in L078's twelve
V0 equations, and determine whether surviving ratios fix their normalized
directions uniquely. A branch-complete necessary test could eliminate
the syndrome seeds before enforcing the other thirty-six equations.
Independent triangle/extraction and challenge-definition gaps remain.

Inputs inspected: L072's full blocks, L077's shortening proof, full
quadrilateral formula and reconstruction, and L078's full matrix and
determinant proof. The unchanged literature assessment covers this
label-only necessary quotient test; no fresh source search is needed.
ATTEMPTS/020, /027 and /028 remain relevant: neither positive label
sampling, incidence alone nor forced zero coefficients closes the gap.
L073–L078 remain unaudited; no family decision is assumed.

Continuation test: a uniform rank/consistency restriction with a concrete
remaining all-label closure test justifies continuing. A surviving tuple
does not prove a realization; it needs all 48 identities and the original
moment matrix. If rank analysis supplies neither a new restriction nor
a testable reduction, record EXPLORATION and reassess this mechanism.

Unfinished reasoning: L078's matrix M has five affine equations in
d1,d2,d3. Its maximal minors vanish exactly on R=0, but its coefficient
rank, affine consistency and distinctness were not decided. Investigate
these complete branches before using a generic inverse or dropping a
singular system. Normalize only V0,h0,d0 on the syndrome line.

Interim exact evidence: the complete producer and independent original
twelve-equation replay find 847,570 R-zero tuples; 8,648 are inconsistent
rank drops, 166,898 unique solutions have collisions, and 672,024 have
twelve distinct finite nonvertical directions. Full certificates are
`scripts/triangle-incidence/affine-plane-affine-rank*.csv/json/jsonl`.
The replay brute-forces all 81,450,625 admissible four-ratio tuples and
uses the original twelve-by-eleven augmented system, not the reduced
matrix. No H-labeling has been enumerated.

Unfinished closure observation: all 48 singleton tuples in L077's
complete incidence certificate are permutations of the same four
disjoint sets defining A,B,C,D, twelve per set. Thus all right sides
can be computed from these four ratios. Recover V1,V2,V3 from L077's
three quadrilaterals using h0,d0 and e1,e2,e3; check all sixteen
directions for distinctness and all 48 equations. This is still a
necessary-system test, with no sufficiency or moment realization claim.

Completed: L079 records an UNVERIFIED CANDIDATE exclusion of the exact
family. All 672,024 distinct V0 solutions fail: 209,214 force a collision
among sixteen directions, and 462,810 violate a quadrilateral equation.
The independent Python witness replay checks every rejection using the
original L077 incidence table and homogeneous first-slot recovery.
All checks pass with zero failures. The full proofs, algorithms,
qualifications and certificate paths are canonical in
`lemmas/L079-affine-plane-complete-ratio-exclusion.md`.

Outcome ADVANCE / RESEARCH / POTENTIALLY_NEW, actual type calculation.
This is local computational progress, not certified originality or a
global challenge resolution. Next: obtain separate coverage approval
and critically audit L079 with the essential L010/L072/L077/L078 chain;
the exclusion does not require L073–L076's descent. Independent family,
triangle/extraction and challenge-definition gaps remain unresolved.
