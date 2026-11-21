# Supplied Li margin to a mixed witness — working checkpoint, step160

Invocation-start target and EXPLORE coverage are unchanged: assess a
degree D(n,epsilon,A) for L030 from lambda_n<=-epsilon and
sum|beta_j|<=A, using L026 geometry and no separations. Main gap:
actual-Xi all-degree mixed positivity. This is one mathematical attempt;
no negative actual Li coefficient is being asserted.

Read L018/L024-L026/L030/L032/C032a and L895's hypotheses,
head construction and qualifications, plus step158's recorded direct
Li-index import stop. Preserve all pre-existing notebook changes.

Unfinished mechanism (not yet a proved lemma): put
P_n(z)=sum_{k=0}^{floor((n-1)/2)} (-1)^k binom(n,2k+1)(z/4)^k
and a_n(z)=P_n(z)(1+z/4)^(-n/2). Pairing Lagarias's rational
observable should give lambda_n=sum_j beta_j a_n(beta_j)^2.
The proposed regularization is q_eta(z)=a_n(z)/sqrt(z+eta).
Its discrepancy is -eta*z*a_n(z)^2/(z+eta). Splitting a_n(z)^2
as n^2 plus an O(z) remainder may make the n^2 term favorable
in real part for Re z>0, leaving an upper error O(eta*A).
This one-sided sign is the intended replacement for unavailable
uniform two-sided tail approximation. All constants and pairing
normalizations still need proof.

L026 suggests a tangent disk containing every beta_j: since
Re(beta)/|beta|^2=x^2-y^2>63/4 for alpha=x+iy,
|beta-2/63|<2/63. A Taylor disk centered at 2/63 with a
slightly larger radius might avoid -eta and permit explicit
polynomial truncation with a degree depending only on the inputs.
Need prove branch choices, contour supremum, tail bound, algebraic
square error, real coefficients, complete multiplicity accounting,
and a total upper error strictly below epsilon/2. Stop if an
unknown separation, extra mass-tail modulus or RH sign is needed.

Next within this attempt: verify exact pairing and derive explicit
regularization/truncation constants before making any result claim.

## End-of-attempt disposition

The unfinished mechanism above is now resolved in the full, unaudited
proof in [L964](../lemmas/L964-supplied-li-margin-explicit-mixed-witness.md).
It uses c=1/16, an explicit analytic supremum and a one-sided comparison;
the total upper error is less than epsilon/4. No mathematical script or
numerical evidence is needed for the analytic estimate. The next
invocation should independently audit that proof under the unchanged
target and previously saved source assessment. This is a conditional
transfer, not a supplied negative Li coefficient or an RH resolution.
