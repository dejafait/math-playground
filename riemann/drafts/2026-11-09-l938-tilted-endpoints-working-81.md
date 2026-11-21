# Fixed tilted endpoint test — step81

Approved TARGET: Test the fixed b=1/10 tilted primitive U_b(E)=integral_0^E exp(bt)v(t)dt at E=1/4 and E=4 using unchanged L938 data and a degree-32 exponential Taylor enclosure, with no refinement.

Prior SPECIALIZE assessment79, separately approved step80. RESEARCH /
REPRODUCTION / calculation. Main gap L030–L032/C032a remains all-degree
actual-Xi mixed positivity. Seek strict negative/positive endpoint contrast;
it could supply compact sign data for a later domain-correct primitive
variation argument. Stop without refinement on any unresolved/opposite
sign. Global variation, tail join, parameter signs, contacts and realization
remain separate gaps.

Inputs read: L938's complete representation, 34 rows, interpolation and
beta/telescope/integer integration proof; step50 and step75 audit notes and
step75 full audit code through inherited coefficient/endpoint checks.
Existing coarse pointwise and ratio stops do not decide this integral.
All original artifacts and unfinished work are preserved. No cross-notebook
input. Reuse ready primary Taylor/exponential coverage; no new literature.

PENDING calculation, not sign evidence: write Z=293/(540*2^36*17!).
L938(9),(16) imply |v-v_p|/pi^6 <=12 epsilon 8^11 Z t^17,
and |v_p|/pi^6 <=8^12 Z t^17 on [0,4]. Bound exp(t/10)<3/2
by its positive series with geometric tail. The two integrated allowances
are (3/2)*12 epsilon 8^11 Z E^18/18 and
(3/2)*(E/10)^33/33! *8^12 Z E^18/18.
Use e^bt(v-v_p)+(e^bt-T32)v_p exactly, so no cross term is dropped.
All quantities here are proposed for verification, not computed results.

For exact multiplication in the factorial basis let
S_m=sum_(j=0)^min(32,m) R_(m-j) binom(17+m,j)10^(32-j),
with absent R coefficients zero. Then the exact center divided by pi^6
is sum_m S_m E^(18+m)/(18+m)! /(C^12*10^32).
Load all selected coefficients and constants in the script; verify inherited
input hashes, all audit flags and exact dimensions. Save full rational
centers/errors and outward decimal inclusions. Neither theta nodes nor
transcendental libraries will be rerun; inherited arithmetic trust remains.

Completion: the fixed test passed without refinement. Full proof and
qualifications are canonical in L947; exact certificate and reproduction
script are scripts/heat/l938-tilted-endpoints-81.json and the matching .py.
Both errors are paid; the full summaries and exact selected constants were
inspected. Independent direct and Horner signed rational accumulations
agree at both endpoints. Earlier PENDING text preserves the work checkpoint
and is superseded by this completion. No global primitive theorem follows.
