# Rational-stability attempt1757

19 November 2026. In-progress checkpoint for the exact target in
assessment1756, reused unchanged with DECISION SPECIALIZE. Main gap:
L030-L032/C032a actual-Xi all-degree positivity. Intermediate use:
rationalize C033l's finite separator so its residual side has the
argument type required by C033m. No end-to-end certificate is implied.

Inputs read: C033l's hypotheses and complete separation proof,
C032q's signed bounded integration proof, C033i's residual statement,
and C033m's evaluator statement; source-notes1756 and stops1571/1576.
The existing source comparison covers the exact target. The original
finite data n, s_j>0, a_j, epsilon>0 are given, not computed.

Candidate budget to check: put A=max_j |a_j|>0,
tau=min(epsilon/(12*n), A/2), and
d_j=min(s_j/2, epsilon*s_j/(24*n*(1+|a_j|))).
For |q_j-s_j|<=d_j and |b_j-a_j|<=tau, define
D=sum_j (|b_j-a_j|+(2*|a_j|/s_j)*|q_j-s_j|).
Mimica Proposition1.4 gives a probability-transform derivative bound
2/s_j on arguments at least s_j/2. The proposed budget gives D<=epsilon/6.
Check residual error <=D, full signed support error <=2D, and thus
perturbed gap >=epsilon-3D>=epsilon/2. The coefficient at a maximal
|a_j| remains nonzero; density can choose every b_j rational nonzero.

Pending: write the complete signed supremum comparison and rational
choice, verify constants and inherited qualifications, then record a
canonical proof if the test passes. Stop if a moment at zero, a
positive-width restriction, numerical margin or unreviewed theorem
is needed. Atoms and singular width measures remain allowed.

Completion: the candidate budget passes. The full statement, cited
regularity input, signed supremum comparison and proof are now canonical
in C033n, `lemmas/C033n-rational-stability-of-capped-signed-laplace-separators.md`.
The preceding notes preserve the pre-proof checkpoint, not a second
current task or canonical derivation. No stronger assumption was needed;
independent application audit remains pending. Neither the actual
finite data nor a numerical gap was obtained.
