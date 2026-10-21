# Two-block witness — step 353 working record

The pre-invocation EXPLORE assessment is
`drafts/literature/2026-10-19-two-block-order-pair-witness.md`.
This is one proof attempt on its exact target, not a source-review turn.
Existing unfinished work and Attempts 018/030 are preserved.

Main gap: unrestricted SAT decision/separation. Intermediate target:
retain the original product of width-three diagrams in orders A·B and
B·A, with both blocks unbounded, and construct a Boolean/commutator
affine-ABP witness with one fixed polynomial in the original L087 M.
Its downstream use is extending the restricted W₂ interface; arbitrary
orders, general ER data and SAT transfer remain independent gaps.
Continue on both formal identities and a complete original-M ledger;
abandon this mechanism on Boolean-only equality or exponential copying.

Saved before the full write-up: let I,J be the two block-boundary state
sets, each of size at most three. Exact path cutting suggests
f=Σ_i a_i b_i and g=Σ_j c_j d_j, with a_i,d_j on A and b_i,c_j on B.
Prefix-to-boundary factors are indicator-terminal diagrams and suffix
factors retain original terminal labels. For each i,j use L035 on the
x-only graphs b_i c_j,d_j, giving C_ij. Use L026/L071's post-compilation
component for U_ij=a_i d_j+P_ij and V_ij=b_i c_j+Q_ij after substitution.
The proposed summand is a_i C_ij+U_ij b_i c_j+P_ij V_ij. It substitutes
to a_i b_i c_j d_j+P_ij Q_ij. The sum of the latter products is in the
single increasing multilinear A·B space and has Boolean value fg, so
L026 injectivity would make it zero under the promise. This identity
and all boundary/copying claims still require the canonical write-up.

Relevant proof reads: L026 complete; L035 complete including its audit;
L071 value/K/P/W graph construction and post-compilation audit;
L087 hypotheses/B/M. The prior source comparison and the exact local
search supply no duplicate full two-block theorem. No L085, cross-notebook
input, new external source, semantic tester or path unfolding is used.

Completed: the canonical construction and complete proof are in
`lemmas/L091-two-block-order-pair-affine-abp-witness.md`. The saved proposal
above is superseded by that proof, without removing the working record.
Both formal identities close with a polynomial original-input ledger.
This is an informal result pending separate critical audit, not executable
verification. The only continuation is the proposed audit recorded in
PROGRESS.md and its matching REVIEW_REQUIRED assessment.
