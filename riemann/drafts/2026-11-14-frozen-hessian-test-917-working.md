# Frozen Hessian diagnostic917 — working checkpoint

Approved scope: assessment915, unchanged EXPLORE target supplied at startup.
Only W(t)=d^2det_(A_*)[A_*',A_m(x_*-t)] is being tested.
No higher differential or alternative weight is authorized in this step.

Inputs read: C466a density/normalization; C466b scalar-law localization,
recurrences and singular-endpoint proof; assessment914 completed915
determinant and Schur sources; stop915. Rank-one results are not
silently applied to the corank-two stratum.

Provisional calculation, not yet audited: write n=m-2, B the invertible
leading n block, and choose the monic degree-n P whose coefficient
vector (with last coordinate zero) is in ker A_*. The Hankel rank and
top-n-row test also put zP in ker A_*; hence the frozen moment functional
annihilates P z^j for 0<=j<=n+2. In the kernel basis P,zP the compression
of A_*' is diag(0,kappa), kappa=[P(partial)^2 p]'''(x_*).
The change-of-basis determinant is one. The expected Hessian formula is
W(t)=det(B) kappa a(x_*-t), where a=P(partial)^2 p.

Planned checks: prove the rank/kernel statements and this coefficient
including its normalization; verify a(x_*)=a'(x_*)=a''(x_*)=0 for
a=P(partial)^2p, endpoint order W=O(t^3), flat other endpoint,
and the exact two contractions using C466b's matrix recurrences.
Both candidate balances appear to vanish, since the kernel compression
of LA_*+A_*L^T and NA_*+A_*N+A_* is zero and det diag(0,kappa)=0.
If kappa is zero the whole functional is zero; otherwise ODE uniqueness
should show W nonzero and positive H should force both signs.
No nonzero actual kappa or contact existence is assumed or established.

Main goal remains L030-L032/C032a all-degree actual-Xi positivity.
A nonzero signed balance would have addressed only simultaneous-contact
forcing. If the zero balances survive checking, stop this weight and
preserve the precise obstruction; do not escalate derivative order.

Completion917: the calculation and endpoint checks are now written in
[C466i](../lemmas/C466i-frozen-hessian-corank-two-zero-balances.md).
Both balances are exactly zero, and kappa!=0 is necessary and sufficient
for this weight's nonvanishing. The completed proof is conditional and
awaits separate conceptual audit; the provisional reasoning above is
retained as a checkpoint, not separate canonical evidence.
