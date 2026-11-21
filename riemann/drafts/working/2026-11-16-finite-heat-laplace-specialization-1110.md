# Fixed-degree heat–Laplace specialization — working1110

Approved target: assessment1108, unchanged. One conditional mathematical
specialization; no actual heat-block sign assertion or all-order limit.

Inputs read: L018/L024-L026/L030; comparison1108's complete tool and
failure inventory; L033/L038/L041 as duplicate contrasts. Main gap is
actual-Xi Q(q)>=0 in all degrees. Proposed canonical identifier C030a
will be checked for availability before writing.

Preserved argument in progress: put lambda_j=alpha_j^2 and
a_j=Re(lambda_j). L026 gives a_j>63/4 and
a_j>=(63/65)|lambda_j|. Thus sum a_j^(-r)<infinity for r>=1
from L024, without RH. The nonnegative majorant
G(t)=sum exp(-a_j t) controls the real smooth heat trace.
With u_i(x)=x^i/i!, beta/gamma normalization gives
integral integral u_i(x)u_j(y) H(x+y)=S_(i+j+2), and its
absolute majorant integral is sum a_j^(-i-j-2).

Remaining verification before claiming the bridge: apply Sra C.2 to
the exact strict all-positive-time B_(d+1) premise. Apply Andreief
twice on [epsilon,R], keeping 1/(n!)^2 on full Cartesian powers.
The two monomial determinants and heat determinant give an integrable
full integrand by permutation expansion and the pairwise majorants.
On ordered chambers both Vandermondes are positive. A fixed compact
positive contribution must prove strictness, not entry convergence
alone. Verify symmetry/Sylvester and the c0,c1 mixed coefficient.

Continue if all these finite statements hold; abandon any unsupported
strictness or all-order inference. Independent signing, common-graph
realization and global RH remain unresolved. No new sign mechanism
has yet been justified. This working note is not a completed proof.

Completed later in the same step: the full argument is canonical in
`lemmas/C030a-finite-heat-laplace-mixed-form-transfer.md`; all four
applicability obligations were discharged under the explicit finite
premise. The original partial reasoning above is preserved. A separate
conceptual audit is nominated with REVIEW_REQUIRED; it has not occurred.
