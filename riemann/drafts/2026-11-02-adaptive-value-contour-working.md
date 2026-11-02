# Adaptive value-remainder contour — bounded joint-target attempt

Prepared STEP_ID: 2026-11-02-adaptive-value-contour-research-01.
The unchanged invocation-start EXPLORE assessment is
`literature/2026-11-02-joint-full-grid-polynomial-dual.md`.
This is a mathematical attempt within its finite residue/polynomial scope.

Main gap: actual-Xi all-degree mixed positivity and unbounded-height signs.
Intermediate target: the approved joint full-grid projection at squared
rate 1/16 relative to L649's exact original-residue diagonal. A bound
could supply the sufficient constant-input comparison; Xi realization,
matching upper bounds, signs and inherited audits remain independent.

Keep C645y's full component, L649's normalization, L650's polynomial
response, L651's complete Gram/correction and L653's value interpolant.
Keep n>=5, x=-5/4, R=11/8, eta=1/100, t_j=j/n, common distinct
Re(a)=x poles including x with |a|<=R-eta, positive integer original
residues and M=sum r_a<=n/3. No separation, symmetry or coefficient
integrality is added. N is the number of distinct poles; multiplicities
remain in the response and squared diagonal. All grid factors and
conjugated denominator angles remain.

The supplied assessment and local L649--L653 comparisons are reused.
Relevant full response/contour proofs and the polewise and reflected-
multiplicity failure records were read. The existing sparse bound uses
radius 1/n and costs N log n. L652 is only a pointwise certificate
failure, and L650's separate columns lose a cancellation kept here.
Neither supplies a joint angular obstruction. No new source is needed.

Continuation/abandonment test: obtain uniform squared rate 1/16 on a
quantitatively enlarged family, a full admissible obstruction, or an
explicit remaining contour cost. A large upper cost, single bad angle
or finite screen cannot refute the joint target. Do not invoke new
general approximation input without a separate REVIEW_REQUIRED turn.

## Unfinished reasoning saved before further work

For a regular common disk radius r<=eta/2, the existing residue contour
can be estimated without setting r=1/n. The preliminary envelope is
N*r/(eta-r) * (2R/r)^N * exp(8*n*r) * max_a |W_a(u)|.
Taking r near N/(8n) appears to replace N log n by N log(n/N)+O(N).
The contour radius may be approached through regular values; any
limiting bound must be justified without presuming convergence of the
contours themselves. Node-specific boundary arcs may also retain the
angular weights before the final norm comparison.

Candidate quantitative subfamily: N<=n/384, n>=8192. Check all constants,
the anchor lower bound, the negative-part correction and arbitrary
allowed original multiplicities. This would have fixed positive density
and include arbitrarily close clouds and spread poles; N near n/3
would still be unresolved. This is not yet a proved result or an audit.

## Refined mechanism during this attempt

Use the regularized residue kernel (Q(w)-Q(z))/(w-z), a polynomial
in both variables. This removes the need for the disk contour to stay
strictly inside |z|=R. On its arcs the common-line geometry gives
|w-a|<2R for every node, so the telescoping product identity bounds
the kernel by N(2R)^(N-1). The residue formula remains the same value
interpolant. Assign boundary arcs to their generating node before
taking absolute values, retaining sum_a |W_a(u)| in the bound.

For regular r<=1/16, the preliminary resulting bound is
||s_u||<=N(2R/r)^(N-1) exp(8nr) sum_a |W_a(u)|.
Taking regular radii tending to N/(8n)<=1/24 suggests
K_(n,N)=N exp(N)(22n/N)^(N-1).
Weighted Cauchy--Schwarz uses ell=sum_a 1/r_a and gives the candidate
T= sigma/[R K_(n,N) sqrt(M ell)] against the original D_u.
This preserves the full correction from L651/L653. The resulting
amplitude cost is at most 9n^2 exp(n phi(N/n)),
phi(q)=q[1+log(22/q)]. Thus the N log n term can be removed even for
N of order n, but at q=1/3 this envelope is still far above the target.
The proposed N<=n/384, n>=8192 subfamily requires checking
phi(1/384)<9/320 and 3+2 log n<=n/320, then the anchor/correction.
No obstruction to the full angular projection is inferred.

## Completed bounded attempt

RESEARCH / ADVANCE / POTENTIALLY_NEW; actual task proof_attempt.
The full proof, hypotheses, constants and citations are canonical in
L654. This is a local partial advance, not certified originality or a
complete joint comparison. The ready assessment was reused unchanged.

The regularized residue kernel removes the radial-gap restriction.
Keeping node weights on their own boundary arcs and choosing radii
tending to N/(8n) gives the explicit cost K_(n,N) recorded above for
every admissible distinct count. Weighted Cauchy--Schwarz retains the
original r_a^2 diagonal. The full correction is paid. For N<=n/384,
n>=8192, the squared rate is 1/16 with constant 1/4, pointwise and
after the normalized angular mean. Arbitrarily close clouds, spread
configurations and all allowed original multiplicities are included.

At N near n/3 the remaining upper cost has amplitude exponent
(1+log 66)/3, which cannot supply 1/32 through this envelope. This
does not show that the cost is actually large or that the joint target
fails. L653's stronger sparse-subfamily rate is preserved. Further
small changes to contour constants are not the proposed continuation.

All 21 exact constant checks passed in
`scripts/one-sided-hankel/adaptive-contour-constants.json`; every
actual/required bound in the complete checks array was inspected.
The proof, not this arithmetic certificate, establishes uniformity.
L654 and its inherited analytic inputs remain separately unaudited.

Continue the unchanged joint target for N>n/384 by testing approximate
polynomial value matching on clusters at scale 1/n, retaining the
weighted pairing error and full polynomial norm instead of imposing
exact values at every nearby node. Use L650/L651's complete response,
L653's value targets and L654's explicit cost as comparisons. Require
the full angular rate or a quantified error/cost balance; neither a
single bad angle nor an excessive upper envelope is an obstruction.
No new general approximation theorem is approved by this continuation.
