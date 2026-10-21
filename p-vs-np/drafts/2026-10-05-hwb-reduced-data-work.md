# HWB reduced data — saved construction reasoning

Approved target: construct polynomial-size, polynomial-degree reduced original-axiom data for L027's HWB ER family without OBDDs. Ready assessment: `drafts/literature/2026-10-05-hwb-reduced-data-without-obdds.md` (EXPLORE before invocation). This is one research attempt; preserve Attempts 017/019.

Proposed representatives over the free F₂ ring: prefix-weight polynomials q_(0,0)=1, out-of-range q=0, q_(i,j)=q_(i-1,j)(1+x_i)+q_(i-1,j-1)x_i. Use these two summands for u,v and 1+q_(i,j) for w. Selector t_j=q_(n,j)x_j, successive OR value R_j=sum_(l<=j)t_l, d_j=1+R_j, h=R_n. They have degree at most n+1 and shared O(n²) construction. Disjoint Boolean weight cases justify sums; no claim of formal multilinearity is needed.

Accumulator test: P_m=x_1...x_m. Initial a_0=P_1, after z_0 still P_1. Row i=1 stays P_1. For i>=2, retain P_(i-1) until u_(i,i-1), where its true-on-all-one sign is NOT u and the product enforces x_i=1; thereafter retain P_i through the row. All later selectors, OR gates and h retain P_n. This requires a full all-assignment case proof, not an on-all-one check.

Local relation candidate for each AND: delta_i=r_i+r_a r_b, J=t_(x_1)+t_(NOT x_1), H_i=delta_i J with the indicated right multiplication. L027 records J(A)=(1+x_1)+x_1=1 formally; hence H_i(A)=delta_i and H_i(0)=0. Proposed bound h=2n+3. Original clauses are permitted; this does not give Boolean-only witnesses or arbitrary-ER data. No unreduced value correction is being attempted.

The unfinished obligations above were completed in canonical L028. Its complete formal proof, bounds and qualifications supersede this saved reasoning; `scripts/hwb-reduced-data/data-results.json` contains the finite certificates and failures. The next independent critical audit is pending separate scope approval. No further mathematical step is undertaken in this invocation.
