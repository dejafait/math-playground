# Step765 — bounded half-factor block attempt, unfinished

Approved scope: `drafts/literature/2026-11-13-theta-half-factor-asymptotic-block-764.md`.
Main gap: L030-L032/C032a actual-Xi all-degree mixed positivity. Test only
the formal centered additive half-factor's power sums through degree four.
Retain all existing work; no degree sweep or root premise.

Choose fixed coefficient-asymptotic order K=4 before expansion. Reuse
O'Sullivan 2007.13582v2 Theorem1.4 and its previously assessed proof,
Arizmendi-Perales Propositions3.4/3.6/Lemma4.1 and Nathanson Theorem1.
Theorem1.4 was retrieved to fix the exact prefactor, not to reopen review.

Let gamma(n)=n!m_n/(2n)!, h=gamma(d-1)/gamma(d)>0 and
q_j=gamma(d-j)/(gamma(d) h^j), j=0,...,4. Then q_0=q_1=1.
Centered elementary coefficients are
e_k=binom(d,k)h^k sum_{j=0}^k binom(k,j)(-1)^(k-j)q_j.
For k=2,3,4 the inner expressions are q_2-1,
q_3-3q_2+2, q_4-4q_3+6q_2-3.

Tentative half-factor equations: b_1=0, b_2=e_2/2, b_3=e_3/2,
b_4=e_4/2-v e_2^2/8 with v=(d-2)(d-3)/(d(d-1)). Thus
s_2=-e_2, s_3=3e_3/2, s_4=(1+v)e_2^2/2-2e_4.
These require complete algebraic verification and controlled cancellation.

Heuristic prediction only: s_2/(d h^2)->1/2,
s_3/(d h^3)->1/2, s_4/(d h^4)->1, with block determinant->1/8.
No sign theorem yet. Need show finite-offset gamma errors remain o(d)
after the fourth-moment cancellation, without differentiating remainders.
Continue to eventual negative minor or eventual PSD; stop if K<=8 fails.

No new central creative mechanism is established by this diagnostic.
Uniform full-factor roots, shifted/mixed signs and global assembly remain open.

## Completion

The unfinished derivation above is retained as the initial checkpoint.
Its algebra and error obligations are now resolved in C795a,
`lemmas/C795a-formal-half-factor-eventual-hermite-block-positivity.md`.
K=4 suffices; the normalized block is eventually positive definite,
with limiting determinant 1/8. This retires the selected detector only.
Exact auxiliary algebra is in `scripts/central-jacobi/half-factor-block-765.json`.
A separate conceptual audit remains pending; no creative mechanism or
full-factor conclusion is added here.
