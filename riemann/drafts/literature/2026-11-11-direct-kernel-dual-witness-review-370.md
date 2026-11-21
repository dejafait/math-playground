# Direct complete-residual dual-witness test — nomination pending approval

TARGET: Test the direct complete-kernel minimax threshold at TV exp(sqrt(n)) by a continuum complex-TV dual witness.
CHECKED: 2026-11-11
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse step370's completed direct-kernel-minimax-review-369.md comparison, six recorded queries, scoped duplicate/failure searches and inspected contracts; no separate search or mathematics for this nomination.
SOURCE_EVIDENCE: Sion(1958) Theorem3.4 p174 https://msp.org/pjm/1958/8-1/pjm-v8-n1-p14-p.pdf; Boyd–Vandenberghe(2004) Examples3.24/3.26 pp92-93 https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf; Shapiro manuscript Theorem2.3 p6/Lemma6.1 pp27-28 https://optimization-online.org/wp-content/uploads/2008/07/2028.pdf. Full inspected hypotheses, proof qualifications and complex discrete comparison are in review369 step370.
COMPARISON: Known minimax/support-function tools support the certificate framework; no inspected theorem pays the structured complete-kernel asymptotic rate. The complex discrete Haar theorem is not imported. Taylor/defect stops and unpaid scalar/spectral tails do not decide this objective.
GAP: Produce a quantitative witness for the actual target direction at the original complex coefficient-l1 cap; exact duality alone does not decide the threshold.
REASON: The complete-residual source comparison is finished; nominate one bounded mathematical test after separate next-turn source approval. This document establishes no dual identity, lower bound or optimizer.
SCOPE: Integer n>=2; complete C997c kernel, I=[7/4,9/4], E=[15/8,17/8], z_star=1+i/8, gamma_(j,n)=15/8+j/(4n), j=0,...,n; arbitrary complex coefficients with sum|A_j|<=exp(sqrt(n)). Only this fixed grid and budget are covered.

The objective remains

    E_n=inf_(sum|A_j|<=exp(sqrt(n)))
          sup_(c in I)|k_n(c,z_star)-sum_j A_j k_n(c,gamma_(j,n))|.

The main gap is L030-L032/C032a actual-Xi positivity, L966/L968 signed
forcing and unpaid L984(H). This point-bridge test is an intermediate
resource for signed slope selection; it leaves independent transfer
gaps unresolved. Neither exact duality nor a certificate framework
alone counts as solving the quantitative test.

After separate approval, attempt one continuum complex-TV separating
witness mechanism for this complete residual. Import the general
duality tools by precise citation; verify the real scalar pairing,
coefficient support function, compactness/continuity and every
interchange needed for the chosen certificate. A weak lower certificate
does not require claiming a full strong-duality identity. Retain the
complex modulus coefficient cap; do not substitute a real l1 cap,
coefficient energy, normalized response norm or a different data
direction. No unproved Haar or nonvanishing assumption is available.
Use only the portion of the generic machinery needed to test a
quantitative bound, rather than adding a framework lemma as an end.

A decisive negative certificate makes E_n exp(n/64) unbounded on an
unbounded integer subsequence. A positive resolution would require
E_n<=C exp(-n/64) uniformly eventually with the same coefficient cap
and C independent of n. Fixed finite examples can discriminate a
witness construction, but cannot establish either asymptotic result.
If a primal upper certificate is considered, it must additionally pay
the complete slope continuum, including endpoints; a sampled upper
fit or fixed-n convergence theorem supplies no growing-n mesh rate.
No such certificate is supplied by this nomination.

If the attempt yields only a formal dual reformulation or an unpaid
kernel-specific tail, record EXPLORATION and preserve the reasoning;
repeat only with a concrete new quantitative input, informative
obstruction or materially refined witness. A lower bound for this
grid and budget does not stop larger subexponential budgets or general
band measures. Preserve stops314/315/340/341/364/367 on their scopes.

Essential input ID is audited C997c(1),(4)-(6). C997q supplies complete
notation; its(1)-(2) were checked directly in C997r369, but the proposed
direct objective does not require the rest of its unaudited proof.
Keep both beta terms, both windows, K's -1 and all zeros; do not divide
through g_n. C997a(8), selected/both-sign transfer, assay/reconstruction,
complements/regulators, L993, L984(H), L966/L968 forcing and actual-Xi
positivity remain open. Mathlib full matching coverage is unknown.
No cross-notebook input or RH candidate. Separate approval remains
pending; no mathematical work is invoked in step370.
