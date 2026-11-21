# Normalized-height moment application — working note, step126

Gate: reuse the supplied SPECIALIZE assessment
`literature/2026-11-08-normalized-height-moment-order.md` unchanged.
Main gap remains L030–L032/C032a. Only the all-j normalized moment
comparison is being attempted; no signed Fourier claim is authorized.

Working reduction, not yet a checked conclusion: set u=s+t, v=s-t,
k=2Phi, q_s(t)=k(s+t)k(s-t), Z(s)=integral q_s. The Jacobian is 2.
Writing h_j(s)=integral t^(2j)q_s/Z(s), the candidate identity is
m_(2j)(y)=2^(2j) E_(mu_y) h_j(s), where on s>0 the density mu_y
is proportional to s^2 sinhc(2ys)Z(s). Check all factors and Fubini.

L309's W'' is even and strictly increasing in |u|, under its retained
L037 arithmetic contracts. Hence the ratio of the |t| densities at
s2>s1>=0 should be strictly decreasing. The ratio of the mu_y densities
at y2>y1>=0 should be strictly increasing. Check the latter with the
covered DLMF coth identity, interpreting its zero endpoint by continuity.
Use the cited likelihood-ratio theorem for weak order; justify strict
polynomial order separately by the two-copy covariance identity and
finite moments. L898's fixed-polynomial exponential domination should
pay all normalization and endpoint interchanges.

Continue only if both ratio directions, strictness and the y=0 limit
are fully justified; stop if a Fourier-sign premise is needed. L309's
curvature certificate is not independently replayed. L312 and L898's
cross-endpoint obstruction remain limitations, not mathematical inputs
to an oscillatory conclusion. No new mathematics beyond this target.

Completion: the factors and both strict ratio directions are checked in
canonical L902, with fixed-j domination and y=0 treated directly. This
note preserves the initial reasoning; L902 is the final proof. The
continuation is its first scoped audit, not an oscillatory extension.
