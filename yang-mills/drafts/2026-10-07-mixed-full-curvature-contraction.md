# Mixed cubic full-curvature contraction — working record

STEP_ID: YM-20261007-077-mixed-full-curvature-contraction

Reuse the unchanged SPECIALIZE assessment
`literature/2026-09-26-current-target.md` for the complete response target.
The main gap is the ultraviolet-uniform interacting response. The bounded
intermediate test is the signed contraction of L060's bulk gradient cross
block in L058's complete mixed cubic group, with both actual observables.
Its downstream use is to remove an obstruction to an a^2-scale estimate
before attempting the logarithm. Continue if exact algebra removes that
block in the full contraction or gives a sufficient bound; otherwise
retain it as an unresolved signed term, not a growth conclusion.

Duplicate/failure check: L048 already contracts all cubic pairs; L052
uses tilted determinant contractions for top/top, and L054 already uses
the full curvature d in that group. L058–L059 retain the mixed fluctuation
and observable corrections. L060 and ATTEMPTS/018 stop localization of
eta against links, not algebraic regrouping before contraction. The
specialization here is to mixed top/transverse pairs, not a reproof of
Gaussian tilting or a new general cancellation theorem.

Working identity: C=sum_e d_e dot (u_v cross u_w)/2, since d=eta+Tu/N
and (u_v-u_w) dot (u_v cross u_w)=0 pointwise. Under any color-diagonal
quadratic tilt, E[CY] should equal -3/2 times the sum of 3-by-3 cross
covariance determinants between (d_e,u_v,u_w) and each increasing
triple of a transverse plaquette. Differentiating twice must retain all
three same-row mixed derivatives and all six different-row derivatives.
At the original law Cov(d_e,x_T(s))=-g_s(Delta_T)(I-P), because
Cov(u,x_T(s))=s G T^T and L060's -(s/N)P cancels exactly.

To verify: signs and factor, preservation of every transverse plaquette
and pinned row, exact row-operation identity throughout the tilt, and
whether the remaining kernel has a uniform concatenated bound. Even
successful cancellation does not by itself estimate the differentiated
signed sum. No a^2 mixed coefficient or complete logarithm is claimed.

Completed: L061 proves the exact determinant formula, its three same-row
and six different-row derivative terms, and the covariance cancellation
by a row operation valid throughout the tilt. The remaining base kernel
is -g_s(Delta_T)(I-P), with squared concatenated norm after multiplication
by Delta_T^(1/4) at most 1/2. This is a weighted estimate only; small
transverse eigenvalues prevent inferring uniform unweighted localization
from it. The signs, inverse derivative orders, endpoint covariance and
complete spectral bound were checked analytically in the canonical proof.

The required a^2-scale estimate remains open. Continue under the same
target and unchanged assessment by estimating L061's full nine-term sum;
do not drop the two observable derivatives, recondition the fixed
polynomial M, or combine overlapping quartic groups twice. The next
estimate must use the actual exterior columns and rough residual blocks,
not an assumed localized covariance. All independent gaps above remain.
