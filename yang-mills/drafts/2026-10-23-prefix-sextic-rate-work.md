# Retained prefix sextic: ordered quadratic-covariance attempt

Started 2026-10-23. Gate: the unchanged EXPLORE assessment
`drafts/literature/2026-10-23-prefix-sextic-quantitative-remainder.md`.
Exact target: Prove that L202's complete retained prefix sextic
|E[J_i rho_H]| is at most C_i N^(5/2)log(eN)^2 for both actual probes.

Main gap: ultraviolet-uniform interacting reflected control, continuum
axioms and finite positive infrared mass. This selected rate could supply
the sextic component of a quantitative joint cubic probe-jet estimate;
the independent co-closed response rate, transverse-H rate and upstream
qualifications remain unresolved. Essential inputs: L182 L183 L186 L194
L200 L202, with L198 fixing the grouping and L193/L211 only its context.

Startup overview and DAG were supplied and used. Scoped status shows
existing unfinished L260--L263 and audit/source work; preserve it. The
ready assessment, history/240 and ATTEMPTS/039,041,044,045 distinguish
the old modal HS improvement and failed global-energy, cyclic,
factorwise-covariance and rough-prefix-smoothness mechanisms.

## Working calculation, initially unverified

Use L194(12), retaining all three action derivative placements. Test the
two-color quadratic prefix bracket before the separate HS bounds in
L202(8). Split b=[z,q phi]/2-[D phi,q phi]/4. The direct part retains
L182/L186's O(||y||_infinity N^3 log(eN)^(1/4)) count.

For the pure-prefix part compare its complete quadratic coefficient
tensor under K tensor K with Y tensor Y, where K=Phi S Phi^T and
Y=U tensor G, U_st=min(s,t), G=Delta_T^(-1). This is positive tensor
comparison of a norm, never an entrywise comparison or independence
of prefixes within one color. Under Y, each fixed spatial direction
has an exactly separated covariance product.

Candidate counts to check in full: transverse directions give
sum_(s,t)U_st^2=O(N^4) times a full transverse product sum O(N^3),
using paired bounds dGd*=O((1+r)^(-3)+N^(-3)) and
qGq*=O((1+r)^(-1)+N^(-1)). Axial directions give
sum_(e,f)|dUd*| |qUq*|=O(N^2), including the upper row, times
Tr(G^2)=O(N^4). Thus the pure-prefix norm would be
O(||y||_infinity N^(7/2)), improving the modal exponent to 3/2.

Remaining checks before any claim: prove the three-dimensional mixed
Dirichlet bound at every normal end edge by the full heat image/spectral
argument of L200; spell out the entire pinned axial covariance; apply
positive tensor comparison to each actual color order; then retain the
full signed derivative and complete a^2-weighted heat expansion.
Continue only if these counts are uniform and the final exponent is at
most 5/2 with the allowed logs. Otherwise preserve the precise excessive
bound without asserting growth or transferring Q_3's different rate.

## Completed attempt

Canonical full proof:
[L264](../lemmas/L264-prefix-sextic-joint-covariance-rate.md).
The full image/spectral argument gives the required three-dimensional
mixed-difference bound on every normal end edge. In the axial sector,
the pinned increment covariance has identity bulk, -1 upper strips
and upper diagonal n; its absolute entry sum is 4n. Thus the two
candidate second-moment counts above hold with all rows retained.
The resulting modal norm is O(N^(3/2)), and L194's unchanged complete
signed derivative gives O(N^(5/2)sqrt(log(eN))) for both probes.

The old N^(11/4)sqrt(log(eN)) allowance has been sharpened, not
interpreted as actual growth. The new allowance divided by the
requested N^(5/2)log(eN)^2 is O(log(eN)^(-3/2)). No rough tilt,
covariance or prefix is commuted, smoothed or made independent.
Checks are the complete analytic contraction, all-boundary heat sum,
pinned axial covariance and final exponent/heat count in L264;
no numerical certificate or mathematical script is used as proof.

Outcome ADVANCE / REPRODUCTION, actual task proof_attempt. This is a
local standard-method estimate; no originality or full-group claim is
made. Separate critical audit is pending with a newly proposed
REVIEW_REQUIRED assessment. The current continuation and routing are
recorded only in PROGRESS.md; all prior unfinished work is preserved.
