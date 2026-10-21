# Changed-tail order rigidity — unfinished attempt

Approved target: Determine whether L063's first-displacement comparison forces the literal order for L065's changed-tail multiset when row 24 is fixed last.

Main gap: universal eventual descent. The intermediate order statement could extend L066's literal nonintegrality obstruction; no integer assembly is attempted here. Prior SPECIALIZE coverage is drafts/literature/2026-10-13-changed-tail-order-rigidity.md.

Essential inputs read: L051 endpoint/J guard, L055 full table and count-dependent intervals, L063 complete method/audit, L064 changed-tail literal endpoint/J existence, L065 attached-tail specification. L062's exp(24) bound will be used only after its relevant proof is read. Attempts 027–031 and histories 179/181/197 remain preserved.

Working idea, not yet certified: row 23 has J>=8,H>=80,a=20, so its multiplier is at least 3^104/2^132. Compared with 3^64/2^74 the ratio is 3^40/2^58. Exact comparison of that ratio with 1 should retain the old uniform c>10^8 bound for every possible first row. All other eligible rows have a=2,J>=8,H>=40. Thus the geometric root majorant may be unchanged. A first displacement has k<=22 and a literal prefix containing no row 23, so L063's prefix exponents/margins may be reused with explicit applicability.

Continuation test: prove the new multiplier bound, positive cyclic root/domain and minimum uniformly over suffixes, and every eligible strict J rejection. Stop if any needed bound or margin fails or is inconclusive, without implying feasibility. Integer/parity/residue/exact-valuation, H/seed and primitive realization are not premises. No verdict yet.

## Completed bounded attempt

The new multiplier ratio 3^40/2^58 is strictly greater than 1; hence every eligible first multiplier exceeds the old baseline. The uniform root/domain/minimum proof and every first-displacement guard now succeed. The canonical full proof is [L067](../lemmas/L067-changed-tail-j-guard-order-rigidity.md); its exact certificate is scripts/postspell-word-count/changed-tail-order-rigidity-certificate.json. All 276 margins are positive, minimum 779441541677/50000000000>15.58; 15 rational and 8 integer checks pass with no failures. Supporting operands and every weakest case were inspected completely. This finishes the approved target, with separate critical audit pending and no downstream integer assembly. The unfinished notes above preserve the pre-calculation reasoning; their pending language is superseded by this completion.
