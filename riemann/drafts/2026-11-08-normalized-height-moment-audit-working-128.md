# L902 audit working record — step128

Approved target and coverage are the supplied unchanged
`literature/2026-11-08-normalized-height-moment-audit.md` (SPECIALIZE).
One mathematical audit only; L309 curvature arithmetic is an inherited
contract, not a replay target. The main gap remains L030–L032/C032a.

Independent reconciliation of the change of variables:
Phi(u)Phi(v)=k(u)k(v)/4, p²=4s², q^(2j)=2^(2j)t^(2j),
and the absolute Jacobian is 2. Thus the full-plane coefficient is
2^(2j+1); evenness in s adds the final factor 2 in L902(3).
At j=0 this gives A_0=4N_y; division gives m_(2j)=2^(2j)E_mu[h_j].

For the conditional ratio, the r derivative of log Q_s(r) is
-V'(s+r)+V'(s-r). Its s derivative is
-V''(s+r)+V''(s-r), giving exactly L902(5), with negative sign.
Even strictly increasing V'' in absolute argument makes the integrated
bracket positive for r>0, including s_1=0. No improper-integral
differentiation is needed for this ratio calculation.

For the height ratio the derivative is [F(2y_2s)-F(2y_1s)]/s.
The inspected DLMF identity is used at positive arguments only; its
uniformly summable extension supplies F(0)=1. It remains strictly
positive at y_1=0. Neither argument infers strictness from continuity.

Both two-copy identities expand to E[gR]-E[g]E[R]. Conditional
absolute integrability is bounded by 2h_j(s_2)+2h_j(s_1); height
absolute integrability follows from 0<h_j<=h_j(0) and E[T]=1.
Positive densities give null diagonals and strictly negative products
off them. Hence neither probability normalization loses strictness.

The fixed-j double-integral majorant in L902(2) is independent of y,
including y=1/2. Expand the fixed polynomial in |u|+|v| and factor
the exponential to obtain finite L019 moments. For the auxiliary
conditional integrals, on |s|<=S both |s+t| and |s-t| are at least
|t|-S; L019's decay therefore gives a locally uniform integrable
majorant with every fixed polynomial in t. A_0(y)>=A_0(0)>0
allows dominated continuity to pass to normalized moments. No j-uniform
bound, infinite-degree interchange or curvature-certificate replay.

Result: the nominated conditional comparison passes; no mathematical
error was found. Canonical audit qualifications and details are in L902.
This verifies a local input, not a strengthening beyond the sources or
a Fourier sign. No mathematical script or numerical test is needed.
