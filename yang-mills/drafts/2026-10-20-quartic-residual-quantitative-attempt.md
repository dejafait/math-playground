# Quartic residual rate — working record

Approved target: the complete remainder against exactly L152(8), with
required unnormalized bound O(N^(5/2) log(eN)^2), for i=3,6.
The unchanged EXPLORE assessment is
`literature/2026-10-20-quartic-residual-quantitative-remainder.md`.

Unfinished reasoning saved before completing the estimates:
L151's local projected covariance heat representation can be compared
quantitatively using degree floor(c_delta N) Taylor polynomials up to
heat time b_delta N, choosing b_delta sufficiently small. Interior
polynomial entries agree exactly, including the gradient sandwich.
The operator Taylor error is exponentially small. The outer heat tail
is O(N^-1); the projection's inner tail O(N^-3/2), integrated against
the axial (1+v)^(-1/2) bound up to b_delta N, is also O(N^-1).
This would quantify H_N-H_inf independently of exterior modes.

The remaining intended checks are the exact sine-primitive C^1 rate,
full heat summation using L222/L248's already matched probe matrices,
and all terms of L152(15), with both insertions. No rate is assumed
from qualitative convergence. L150/L151's existing projection-row
bound, after its axial factor N, is the expected dominant
N^(-1/2) log(eN)^(3/4) normalized error. Retain all covariance inputs,
the constant axial prefix, separate exterior derivatives, local parity,
and the single connected factor twelve.

Completion: the argument is now written in
[L254](../lemmas/L254-quartic-residual-quantitative-remainder.md).
It obtains the stronger O(N^(5/2) log(eN)^(3/4)) complete remainder,
relative to its imported inputs. This earlier working record is
preserved; the canonical lemma contains the full proof and qualifications.
Separate critical review remains needed.
