# Step508 — fixed L106 tuple guard calculation

Approved target and unchanged SPECIALIZE assessment:
`drafts/literature/2026-10-26-l106-own-input-guard-test.md`.
Main gap: universal descent; this test addresses only whether one audited
endpoint witness survives necessary own-input guards. No full-guard or
actual-word conclusion is an input. Duplicates/failures checked in L106,
L105, Attempt032/033 and the step504/506/507 records; no guard verdict found.
Downstream use: all50 passes would obstruct exclusion by this full real
relaxation; a failed necessary guard filters out the fixed allocation
before any realization work. Support/order exhaustion, entry, integer
realization and divergence remain independent unresolved gaps.

Candidate discriminating calculation: use L106's original tuple at cut3.
Rows3 through23 have tail2 and c_i>2. The first22 numerator terms
(inputs3 through24) therefore have reciprocal-prefix sum<2. By exact
closure, the final three reciprocal prefixes (inputs0,1,2) are
c0*c1*c2*exp(Lambda), c1*c2*exp(Lambda), c2*exp(Lambda).
Check each product<1 using small integer powers. With eta_i<23/11,
exp(Lambda)<2 and D>10584/10^14 from L104 at identical K,N,
the prospective bound is s3<8*(23/11)/(10584/10^14)+23/11.
Compare this with row3's own J3=52 threshold (4/11)*2^208.
One strict failure ends the test; no other guard verdict is needed.

Pending: exact operands, prefix counts, rational comparison and canonical
proof. Preserve all unfinished work and the endpoint-only counterexample.
If this fails to certify a margin, record inconclusive rather than feasibility.

Completed: the three product exponent pairs are (218,464),(335,616),
(364,673), with numerator power upper exponents350,536,584 respectively.
The exact cap is2300000000030429/14553<10^12, strictly below row3's
required threshold. C106a contains the complete proof; the certificate
`scripts/postspell-word-count/l106-row3-guard-failure-certificate.json`
passes92 checks. Complete cut3 prefixes, products and rational bounds
were inspected. The calculation stops at this one certified failure;
no other guard is tested. Separate critical audit remains pending.
