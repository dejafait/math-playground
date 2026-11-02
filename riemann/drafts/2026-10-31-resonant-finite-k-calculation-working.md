# Finite-K resonant packet: bounded calculation checkpoint

Approved target and scope: the COVERED_TARGET in
`literature/2026-10-31-resonant-finite-k-relaxation.md`; no family enlargement.
Inputs are L473 (6) and L578 (3), (6)--(9), with the audited independent
path-constant selector. Existing unfinished work is preserved.

Main gap: actual-Xi all-degree positivity and unbounded-height initial
signs. Intermediate test: decide the unchanged clipped threshold 1/288
for the finite-K-only mixture. A uniform strict upper bound stops this
larger family; a passing law would supply only a covariance bulk, leaving
all fourth constraints, derivative-preserving correction and Hardy/Xi
transfer unresolved. Source coverage is ready EXPLORE and reused.

Candidate finite-data obstruction (not yet independently audited):
the covariance mass entry forces p(A^2+C^2)/2<=1, hence pAC<=1.
L578's W envelope is AC(-7/2-(9/2)cos(theta+phi)). Center its positive
arc at pi, writing the centered angle as v in [-pi,pi]. The arc lies
in |v|<1, since cos(1)<=13/24<7/9. On that interval Taylor's upper
bound cos(v)<=1-v^2/2+v^4/24<=1-(4/9)v^2 gives W_+<=AC(1-2v^2)_+.
Thus E W_+<=2AC/(3pi sqrt(2)) and E Q<=pAC/(72pi sqrt(2)).
Using pi>3 and sqrt(2)>7/5 gives E Q<5/1512<1/288 when pAC>0;
zero product gives E Q=0. Must check Taylor, arc, exact integral,
mass equality and every endpoint before canonicalizing.

This uses only a necessary entry of K, not density domination or a
moment-cone sufficiency claim. No numerical construction is necessary
if the candidate uniform obstruction passes. No new source is needed.

Completed: the full analytic proof and all degeneracies are now canonical
in L579. The bound passes the within-turn calculation; a separate critical
audit is outstanding. The finite-K family is stopped subject to that audit,
and no parameter retry or enlarged family was explored. No mathematical
script ran; documentation validation is recorded separately.
