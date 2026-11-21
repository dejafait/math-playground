# Finite Levy sign/mass test working1553

18 November 2026. One mathematical attempt under the unchanged SPECIALIZE
assessment1552. Main gap: L030-L032/C032a actual-Xi all-degree positivity.
Fixed target: global sign and finite mass of either ell_2-ell_1 or its
negative. A passing direction could later support finite-activity
comparison; full J_eta cancellation and unsmoothed realization stay open.
Stop a direction on a rigorous wrong sign or divergent mass; preserve an
inconclusive bound rather than promote a grid to a theorem.

Read C032j in full, C032m/q hypotheses and interfaces, source-notes1552,
and stops1302/1551. Existing notebook changes are extensive and preserved;
the initial notebook-only status output was too large. No sibling reads.

Exact algebra to investigate: put u_sigma=t/(1+4*sigma*t) and
K(u)=sqrt(u)*H(u). Then ell_sigma(t)=t^(-3/2)*K(u_sigma).
Thus a global decreasing K on (0,1/4) would suffice for ell_2>=ell_1,
but this monotonicity has not been proved or imported. Its zero-endpoint
derivative needs cancellation control: leading derivative equivalents
cancel in K', so they cannot alone supply its sign or an integrable
bound for the difference. Retrieve the already assessed counting/error
proof cases before attempting that estimate. Individual infinity tails
are covered and integrable. This was the initial unresolved checkpoint.

The already assessed Proposition B.1 proof was retrieved at its fixed-v1
URL. Its separate j=0,1 counting and displacement bounds control errors
relative to the full Gaussian main integral I, not merely its leading
equivalent. They give K'(u)=-1/(8*sqrt(pi)*u)+O(u^(-1/2)*log(1/u)).
Integrating K' between u_2 and u_1 gives
ell_2-ell_1=(1/(2*sqrt(pi)))*t^(-1/2)+O(log(1/t)).
This proves absolute integrability at zero and stops the reverse order.
Compactness of transformed time gives an integrable t^(-3/2) bound
at infinity; no unsmoothed large-time substitution is made.

The same retained finite-zero/counting inputs give K'<0 on
[1/200,1/4]: the selected real zero pays at least (12/25)*exp(-q*u)
in -(H/2+u*H'), whereas the absolute high-zero tail costs less than
(1/100)*exp(-q*u). Hence ell_2-ell_1>0 for t>=1/192.
The complete derivation and exact elementary bounds are in C032s.
No mathematical script or numerical grid was needed. Global sign in
the remaining bounded interval is unresolved; no actual law comparison,
signed positive output, full cancellation or RH result is claimed.
