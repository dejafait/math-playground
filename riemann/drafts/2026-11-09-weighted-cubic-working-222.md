# Step222 — unfinished fixed-interval norm comparison

The prior EXPLORE gate is `drafts/literature/2026-11-09-d2-flux-weighted-cubic-test.md`.
Only its fixed interval and full-degree d=2 contact test are in scope.
L019/L058/L874 and the inspected standard norm/Schur sources have been
read; L043 and the steps193/199/204/209/213/217 stops were compared.
No earlier work is being replaced. The main gap is all-degree mixed
positivity. A successful comparison would supply only one finite
boundary direction, with initialization, equality and global issues open.

Write y_j=E[u^(2j)], x=u^2, q_j=(-1)^j y_j/(2j)! and q_0=1.
The finite logarithm recurrence gives
S7=7y7/14!-sum_(k=1)^6 S_k q_(7-k).
For p=c0/c2 and q=c1/c2, the three null rows give
S4=-pS2-qS3, S5=-pS3-qS4, S6=-pS4-qS5.
There is no division by a logarithmic principal minor or by c0/c1.
The exact threshold, including the full all-row reduction of B, is
being checked before any size comparison. No sign has been obtained.

For the actual measure x dmu, W=(y_(i+j+1)) for 0<=i,j<=2 and
v=(y4,y5,y6)^T have the usual monic-cubic minimum
delta=y7-v^T W^(-1)v. Actual positive density and L058's finite
moments justify W positive definite; logarithmic H2 supplies no such
justification. This is a known Schur/extremal specialization.

The proposed single density proof uses the first positive theta
summand on u in [1/4,1/2], together with L917's already audited full
mass upper records (to be checked in all panels). No new moment
evaluator is proposed. A monic Legendre minimum on x in [1/16,1/4]
then supplies a coefficient-independent floor. The floor, its exact
required threshold and the first unpaid comparison will be saved.
No interval refinement or actual contact search is authorized.

If the threshold is not controlled by this datum, one fixed Gaussian
comparison may illustrate failure of the explicitly enlarged
density-floor/contact-row sufficient test; it must not be called an
actual theta contact, a negative actual flux or a counterexample to RH.
Nothing in this working note certifies a final result yet.

Completion: the preserved scratch reasoning above is superseded by
the full conditional proof and exact comparison in
`lemmas/L923-fixed-weighted-cubic-floor-and-unpaid-flux-deficit.md`.
The fixed floor is paid; the actual-theta deficit comparison is not.
The Gaussian diagnostic refutes only the explicitly enlarged sufficient
comparison, and its flux is zero. The outcome is EXPLORATION, with no
refinement, actual counterexample or new sign theorem. Full arithmetic
evidence is `scripts/heat/weighted-cubic-floor-222.json`.
