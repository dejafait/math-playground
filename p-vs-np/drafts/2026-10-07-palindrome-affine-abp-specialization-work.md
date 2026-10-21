# Palindrome F₂/affine-ABP specialization — saved reasoning

Approved target: the exact nested-sandwich circuit-to-ABP test in the existing SPECIALIZE assessment, `drafts/literature/2026-10-07-polynomial-degree-circuit-abp-obstruction.md`.

The main gap remains unrestricted SAT decision. The intermediate test concerns only identical formal output in the free F₂ ring. Nisan's Theorems 1/4 already give the palindrome mechanism; this step reproduces it with the changed field/model and full encoding. No new literature approval or IPS realization is assumed.

Planned applicability argument: for an N-vertex affine-edge DAG in topological order, let C be its constant coefficient matrix, A_0,A_1 its variable matrices, K=I+C+...+C^(N-1), and G_a=A_a K. A word a_1...a_d has coefficient e_s K G_(a_1)...G_(a_d)e_t, by its unique decomposition into constant runs separated by chosen variable terms. The middle-cut coefficient matrix factors through F₂^N. For P_k=sum_(|w|=k) w rev(w), that matrix is a reversal permutation and has rank 2^k over F₂, so N>=2^k. Constant-edge cancellation does not require real coefficients or characteristic zero.

Explicit normalization should give 1+2kN vertices, O(kN²) linear edges and O(kN² log(kN+2)) bits: initial row e_s K G_a, subsequent transition matrices G_a, designated coordinate t in the last layer. This is the degree-component/constant-closure construction underlying Raz–Shpilka Lemma 2 Steps 2–5; no formula unfolding is used. The recurrence circuit has 5k+3 nodes, syntactic degree 2k and O((k+1)log(k+2)) bits. k=0 is the constant 1 boundary case.

Continue if the cut factorization and normalization retain these bounds; narrow or abandon upon a field-specific failure or superpolynomial normalization. Independent unresolved obligations: general L025 data, changing certificates, every-certificate hardness, arbitrary-circuit identity checking, ER lower bounds and decision transfer. L017/L018/L032 are receiving-model context, not mathematical inputs to this lower bound. Preserve Attempt 016 and all prior artifacts.

Status: the complete proof is now canonical in `lemmas/L033-polynomial-degree-palindrome-affine-abp-obstruction.md`. Its k=0 circuit uses only a constant node; for k>=1 the count is 5k+3. This saved outline is retained as unfinished-work provenance, not independent evidence. A separate critical audit is pending.
