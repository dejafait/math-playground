# Variable-table last-pair attempt — completed

The saved pre-work reasoning below is preserved. The attempt established
L077's sufficient data tests and recovered the full L068 benchmark;
canonical proof is `lemmas/L077-variable-table-sufficient-last-pair-cutoff.md`.
The finite certificate passes 17 rational and 11 integer checks, with
complete relevant evidence inspected. No new table or integer/order/support
assembly was attempted. Separate critical audit is proposed, with its new
scope still REVIEW_REQUIRED. The general affine and analytic machinery
and t=0,1 survivors are imported, without an originality claim.

## Preserved working checkpoint

Approved target: Assess a variable-table sufficient last-pair cutoff under literal endpoint/domain/J guards, with L068's rejection of t>=2 as the benchmark.
Prior scope: `drafts/literature/2026-10-17-variable-table-last-pair-cutoff.md` (SPECIALIZE before invocation).

Main gap is universal eventual descent. The bounded target is a portable
sufficient cutoff; it could reduce the last-pair allocations left after L076.
Order assembly and integer exclusion of survivors remain independent gaps.

Inputs read: complete audited L068 and its ready original assessment;
L051 endpoints/J guard and pointwise shift; L055 table/Lambda; L064
changed-tail root/domain and survivor facts. The ready source comparison
covers known affine algebra and positive-real analytic bounds. Histories
211/213 preserve the failed optional <-4 probe; required rejection is
<-3.79. Prior real witnesses and prime failures do not answer this target.

Working derivation to finish/check: write p=r-2, q=r-1, x=2^(-18t),
C=C_q(0), A=sum_(j<q)eta_j/C_j(0), D=2^N/3^K-1. Then
n_0=(A+eta_q/(Cx))/D and n_q=eta_q/D+CA(1+D)x/D;
early incoming prefixes through p do not depend on t. All eta are positive.
The unchanged tail-2 rows before p have multiplier >=19683/8192>2.
A certified e<=min(eta_0,eta_q) and positive Lambda enclosure with
lambda_+<1 can ensure every input n>47 by e(1-lambda_+)/lambda_+>=47.
No growth of either varying row is needed uniformly.

At integer cutoff tau<=B, certify incoming prefix lower bounds L_i>0
for i<=q, a rational Q>= (23/11) sum_i 1/L_i, and
U>=Q/lambda_-+Q+23/(11L_q), U<=exp(T). This bounds
s_q/C_q<U. With prefix exponents k_q,d_q at tau, require
T+k_q*u-(d_q+4J_q)*ell+v<0 using certified lower log2=ell,
upper log3=u and upper log(11/4)=v. This is data-only and should
force the final guard to fail for every integer tau<=t<=B by monotonicity.
Do not infer any passing guard when a sufficient test fails.

Continuation/abandonment test: finish the sign/domain/closure proof and
recover all L068 t>=2 with e=2, tau=2, existing Lambda bounds,
L_0=1, L_i=10^8*2^(i-1), Q=(23/11)(1+2/10^8), T=24 and old
normalized upper U. If any required comparison cannot be justified,
record that obstruction rather than silently transferring fixed-table data.
B=0 and B=1 with tau=2 have empty rejection intervals; there is no
boundary assertion or feasibility claim. General endpoints and r=3 remain.
