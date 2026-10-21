# Variable-table rigidity attempt — step 279

The approved target is the exact TARGET in
`drafts/literature/2026-10-17-variable-table-cyclic-order-criterion.md`.
This is a RESEARCH proof attempt under its prior SPECIALIZE decision.
The main gap remains universal eventual descent. A portable sufficient
order test could reduce later tables to literal-order analysis; literal
integer exclusion and every universal gap would still need separate work.

Working construction, not yet a critically audited theorem: choose rational
lambda>0 with lambda<=N log2-K log3, and a rational T with
23r/(11lambda)+23/11<=exp(T). Require negative tail-2 offsets and rational
logarithm bounds ell<=log2, log3<=u, log(11/4)<=v, with ell>0.
For each k=0,...,r-2 define literal tail-2 prefix counts A_k,D_k.
The proposed finite tests are
4J_(k+1)ell-T-v-A_k u+D_k ell>0.
All these operands depend only on table/budget and certificate constants.

The intended proof uses every actual cyclic endpoint to bound a minimum,
then compares arbitrary tails at actual lower-domain inputs before
propagating literal-prefix bounds. A first displacement has j>k; increasing
J makes k+1 the weakest rejection test. Both cyclic cuts and each outgoing
row's own input must be retained. No comparison-trajectory domain, minimum
location, H/seed, primitive/count-ray or realization premise is available.

The continuation/abandonment test is an explicit sufficient implication
plus recovery of L074 using the complete L069 benchmark inequalities.
Abandon or narrow if an inequality has an unjustified sign or the benchmark
fails. A failed test would establish neither nonrigidity nor feasibility.
No other table or signed-offset alternative is being investigated.

## Completed attempt

The canonical statement, full proof, qualifications, source citations and
Mathlib status are now in L075. The sufficient-test and audited-benchmark
continuation test passed; no new table was searched. The existing benchmark
audit returned 387 exact checks with zero failures. This is local
REPRODUCTION and awaits a separate critical audit, not verification of a
Collatz candidate. The pending next assessment is
`drafts/literature/2026-10-17-variable-table-cyclic-order-critical-audit.md`.
