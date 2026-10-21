# Step 289 — bounded residual-prime attempt

Completed. The approved target is the exact prime search through 10000,
followed, only if successful, by one nonmonic Dedekind verdict for L077.
Coverage is the unchanged SPECIALIZE assessment
`literature/2026-10-17-residual-prime-dedekind-test.md`.
Inputs are audited L067/L077, the full original H, signed discriminant
and complete step-286 division certificate. Preserve all original bytes.

The main gap is rank equality in analytic rank at least two. This local
target could identify whether one prime needs an order correction before
unit/class arithmetic. It cannot give global maximality or a Selmer bound.
One producer and one independent replay, each capped at 180 seconds
internally and 181 externally, and total new output at most 67108864
bytes. No retries, enlarged search or overorder iteration. No divisor or
incomplete evidence parks this route; only a fully replayed verdict permits
a local continuation. No L026 or cross-notebook premise is used.

Outcome: the least residual prime is 31 and the complete gcd is T^2+24,
so L077's order is not 31-maximal. Both fixed stages and all 14243 replay
checks pass. The canonical proof and qualifications are in C077a;
`scripts/residual-prime-289/verification-report.json` retains the complete
replay result. No extension of this finite contract was attempted.
