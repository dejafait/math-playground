# Fixed allocation J-guard rigidity attempt — 2026-10-12

Approved target: determine whether L055's literal order is the only
permutation of its first 24 intact triples, row 24 fixed last, satisfying
all J guards and cyclic endpoints of L051. Prior SPECIALIZE coverage is
`drafts/literature/2026-10-12-fixed-allocation-j-guard-order-rigidity.md`.
Main gap: universal eventual descent. Potential downstream use is L056's
literal nonintegrality, not part of this step. H/seed and all integer,
parity, exact-tail and primitive realization questions remain independent.

Checkpoint before calculation: every eligible first row dominates (8,40,2),
so the L055/L062 geometric bound can be justified uniformly, giving
s_0<20 billion and h_0<24. With a=2 the shifted endpoint is
s_next=c*s+81/44-(3/11)(3/2)^H<c*s, since every H>=40>=5 and
(3/11)(3/2)^5=729/352>648/352=81/44. Thus an unchanged literal
prefix yields h_k<24+sum_{i<k}log c_i. At the first displaced position
k, the new row j must have j>k. Strictly increasing J_j makes j=k+1
the hardest guard to reject. Need certify all 23 such weakest margins
(equivalently all 276 eligible pairs), using L055's audited outward
log2/log3 bounds. This is a proposed calculation until checked.

Continue only if all strict margins are positive; otherwise stop this
sufficient comparison without asserting nonrigidity. The minimum and
root use all 25 endpoint equations, retaining the large last tail.
Attempts 027–030 are modular stops; Attempt 031 rejects one chronology.
None provides this uniform guard verdict. No prime route is reopened.

Completed: the bound and all 276 strict comparisons succeeded. The full
proof is canonical in L063; the full certificate is
`scripts/postspell-word-count/fixed-allocation-order-rigidity-certificate.json`.
The smallest exact margin is 779441541677/50000000000>15.58. Literal
existence is imported from L055, establishing uniqueness in the approved
subsystem. Separate critical audit is pending; downstream arithmetic was
not assembled. No unresolved scratch calculation is being promoted to proof.
