# Oriented block permutation attempt — step 365

Approved target: the unchanged TARGET in
`drafts/literature/2026-10-20-oriented-block-permutation-witness.md`
(EXPLORE, supplied before invocation). No new source search is needed.

Main gap: unrestricted SAT decision/separation; arbitrary-order W₂ and
general ER data remain open. Intermediate target: a polynomial-full-bit
original-fg witness for logarithmically many supplied contiguous blocks,
each independently preserved or reversed. Downstream use: a restricted
witness supplier combining the previous two order promises.

Read the relevant L092 boundary/sorting proof, L093 nonzero reversal
construction, L085 paired recurrence, L035 complete graph construction,
L026 ordered injectivity and L087 original B/M convention. Attempts
018/030 and all existing unfinished work are preserved. No duplicate
combined statement was identified in the ready assessment.

Checkpoint before full proof: keep the original boundary factors during
sorting. For block j use a weighted graph v_j for e_j or rev(e_j), and
the nonzero correction J_j(B)=e_j+v_j. L085 supplies
W_j(B)=d_j v_j+P_j without a zero premise. The proposed local correction
is U_j=W_j+d_j J_j. Insert U_j in L092's additive reduction contexts;
only the full residual sum may be set to zero. No correction becomes a
commutator input. This is unfinished reasoning until its complete
reception and ledger are written in the canonical result.

Continue if singleton/scalar endpoints, both identities, all independent
boundary choices and copies, annotation, bit time and structural path
degree fit one polynomial in unchanged M. Stop this composition on a
blockwise-zero premise, placeholder-bearing commutator input, failed
endpoint case, path enumeration or superpolynomial copying. No scripts,
implementation or finite graph certificate are planned for this proof
attempt; the all-size proof must carry these obligations.

Completed: the full proof is now in canonical L094. The local U identity,
single-order global residual, singleton/scalar reception and complete
independent-copy ledger meet the approved threshold informally. The
bound is K 9^b(M+b+2)^12≤K'(M+2)^16 bits, K'(M+2)^48 bit time,
and structural path degree at most 2q−1. Separate critical audit remains
pending; this work record is not a second proof or approval of that audit.
