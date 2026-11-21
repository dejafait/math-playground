# Compact logarithmic-theta confluence attempt — step612

Approved target: Q_3 for T(x,y)=H(x-y), H(v)=e^v K(e^v)/m_0,
e^v in [1/4,2], cap 2048 terminal intervals. Main gap remains
actual-Xi all-degree mixed positivity. Prior EXPLORE coverage is
`drafts/literature/2026-11-05-log-theta-confluent-compact-test.md`.
Local definitions inspected: L019, L021 and L795; L016 supplies
uniform differentiated-series background. L738 and step502 are
contrasts, not sign inputs. Existing unfinished work is preserved.

Working plan (not yet a result): put u=e^v, a_n=pi n^2 e^(2u),
D=u d/du. Then F=m_0 H=u exp(u/2) sum_n (8a_n^2-12a_n)exp(-a_n).
Differentiate finite summands with the exact polynomial recurrence
P_0=u(8a^2-12a),
P_(j+1)=u partial_u P_j+2ua partial_a P_j+(u/2-2ua)P_j.
Check through j=4 and bound every infinite differentiated tail.
The factor exp(u/2-a_1)>0 can be removed before evaluation.
Mixed columns have factors (-1)^j, so the normalized determinant
is minus the ordinary derivative Hankel determinant. For ell=log H,
its signed value should be ell'''^2-ell''ell''''-2ell''^3;
this identity still needs exact checking in the implementation/proof.

Use rigorous directed decimal intervals (or an available rigorous
backend), exact polynomial recurrences and a proved geometric tail.
No numerical m_0 integration is needed if its positive normalization
is canceled exactly. A negative point stops the test; otherwise a
complete cover proves only the compact condition. Save unresolved
cells at the cap. No extension to global TN3 or Xi signs is approved.

Downstream use: retain or reject one local theta input for a later
signed mechanism. Lower oscillation, unbounded integral interface,
global minors and all-degree transfer remain unresolved. Subsequent
work needs its own matching assessment; a positive scan cannot
justify extending the domain by itself.

Completed attempt: L821 contains the full proof and qualifications.
The implementation instead factors m_0 H=u exp(u/2-c) B and bounds
the derivatives of B; this avoids large exponential-derivative
cancellations in the initial P_j plan. The exact recurrence, uniform
tail majorants through order four and outward arithmetic produced a
105-cell complete cover with Q_3>1/5 and no unresolved cells.
Full evidence: `scripts/log-theta/confluent_compact_612.json`.
The first expanded B_0 wide-box enclosure crossed zero; its identical
positive factorization repaired this implementation issue, which is
retained in the certificate. No negative point was found. This is
local compact progress, not global TN3, an independent audit, a claim
of literature novelty or progress across the remaining signed bridge.
