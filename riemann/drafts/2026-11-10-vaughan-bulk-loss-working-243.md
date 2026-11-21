# Vaughan bulk derivative test — working record, step243

Target: Test whether first- and second-derivative Vaughan Type I/II bounds can pay B_n on exp(n)<m<=exp(2*n), retaining exact degree averaging, compensation and fixed-order remainder costs.

Prior gate: unchanged SPECIALIZE assessment in drafts/literature/2026-11-10-prime-laguerre-bulk-phase-test-review-241.md, separately approved in step242. Actual task: calculation; intended classification REPRODUCTION. No source refresh or new mechanism is being approved here.

Main gap: L030-L032/C032a actual-Xi positivity and L966/L968 forcing; L984(H) is unpaid. Intermediate target B_n would cover one bulk block only; the low and high logarithmic complements remain independent. Inputs L981/L982/L984 are context, not a block estimate. No cross-notebook input or RH assumption.

Continue only if these named tools reach the every-epsilon subexponential threshold, or leave a precisely identified removable loss. Stop this mechanism if their hypotheses fail decisively or the complete bound retains a positive exponential rate. A large upper envelope is not a lower bound for B_n or its remainder.

Checked prior stops: step233 nonpositive-lobe pair, step235 automatic averaging, step240 criterion-only payment. Reused review240's primary contracts and checked exact observable headers. Those stops do not decide this arithmetic test. Pre-existing notebook changes are preserved.

Completed: the canonical proof is [L985](../lemmas/L985-vaughan-bulk-slow-phase-and-fixed-order-loss.md). It checks the finite connection formula, compact scaled domain, Bessel correction and additive error, all three explicit phase derivatives, coefficient-aware Cauchy with diagonal/near diagonal, strict Vaughan support, partial summation and both compensating pieces. No mathematical script or numerical certificate was needed.

Decision: NEGATIVE on this specified estimate chain. Type I T is comparable to 1, Type II differenced T to h/n; the cited tests give no power saving. Restored absolute majorants retain rate 1, including fixed-order remainder costs. These are upper envelopes, not lower bounds for B_n or its error. L984(H), complementary ranges and actual-Xi positivity remain open. Separate source review is required for centering the decomposition before absolute values; no new centered mathematics is derived here. Preserve existing changes; PROOF.md's argument is unchanged.
