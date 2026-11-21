# Step547 — first post-exact Gaussian error working note

Target and gate: unchanged TARGET in drafts/literature/2026-11-05-theta-first-post-exact-gauss-defect.md (SPECIALIZE saved before invocation). One conventional polynomial calculation; no numerical script.

Main gap: actual-Xi all-degree mixed positivity. The bounded intermediate target is the exact positive-x transition of E_(n,2n+1). A possible downstream use is a one-sided comparison at independently established reference barriers; neither reference geometry nor margins is supplied here.

Calculation in progress: put s_n=sum_i v_i, q_n(v)=v^n-s_n v^(n-1)+..., h_n=int q_n^2 dnu and alpha_n=int v q_n^2 dnu/h_n. Gaussian exactness through 2n-1 and monicity give Delta(v^(2n))=h_n and Delta(v^(2n+1))=h_n(alpha_n+2s_n), by subtracting q_n^2 and (v+2s_n)q_n^2 respectively. Both residuals have degree<=2n-1, including n=1. All quantities are finite and positive under actual full theta support. No derivative-sign premise or unaudited conclusion of L806 is used.

Pending verification and canonicalization: retain the exact L795 coefficients; the ratio of their positive magnitudes at orders 2n and 2n+1 is (4n+2)(4n+1). Thus the candidate factorization is h_n*(2n+1)!/(4n+2)!*x^(2n)*[(4n+2)(4n+1)-(alpha_n+2s_n)x]. Check strictness, x=0 multiplicity, n=1 and the actual-law hypotheses. This working note is not a completed independent audit.

Continuation test: a complete all-n transition formula passes this target. Park barrier use until independent reference values/margins and degree-uniform mixed-positivity transfer are supplied. Preserve L795/L796/L805 and derivative-sign-only stops. Classification is REPRODUCTION of covered finite polynomial tools, not a claim beyond checked literature or RH progress.

Completion: the calculation and all pending local cases above are now written in lemmas/L807-theta-gauss-first-post-exact-error-transition.md. The independent audit remains pending; this working note preserves the derivation checkpoint.
