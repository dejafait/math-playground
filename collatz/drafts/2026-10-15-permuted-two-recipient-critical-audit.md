# L071 independent audit working record — step 241

Approved target: Critically audit L071's all-order two-recipient endpoint/domain/J exclusion over 1<=t<=9250244.

Prior SPECIALIZE coverage is `drafts/literature/2026-10-15-permuted-two-recipient-critical-audit.md`.
The main gap is universal eventual descent. This intermediate audit could
support a separately assessed actual-word application; other allocations,
entry, unrestricted cycles and divergence remain independent gaps.

Read the full L071 proof, L051's exact domain/endpoint/J conventions,
L055's complete table/counts and affine formula, L069's product/comparison
proof and independent audit, and L070's complete proof and independent
audit. Attempts 026/031 and history 239 retain their scopes. Existing work
is preserved. No new primary source coverage is required for this target.

Initial symbolic review: substituting n=s-23/11 yields c(n+eta) at
every edge, with 0<eta<23/11 and n>=47. All 25 factors cancel under
closure. Rotation must carry outgoing rows with inputs. Before the first
displaced k<=23 only fixed rows <=22 occur; their tails are <=20 and
H>=40. The changed-tail sign comparison and D_23 must be checked with
exact arithmetic. Increasing J makes j=k+1 weakest, covering all 300
pairs and every nonidentity permutation. The remaining literal order
matches L070's full closed interval, including final tail 2.

Completed: the separate audit found no defect. The full proof and
qualifications are in L071's independent critical-audit section, rather
than duplicated here. The independent program
`scripts/postspell-word-count/audit_permuted_two_recipient.py` passes 355
exact checks, with all complete arithmetic evidence in
`scripts/postspell-word-count/permuted-two-recipient-audit-certificate.json`.
All 24 weakest records, complete Lambda endpoints, exponential total,
boundary tails and summary were inspected. The written audit establishes
full parameter/order coverage; finite checks alone do not.

No defect required a mathematical correction. This verifies the existing
local reproduction and adds no allocation theorem or actual-word bridge.
The original construction certificate, all prior work and recorded stops
are preserved. The mathematical argument and DAG are unchanged, so the
overview was not edited solely to refresh audit-status wording.
