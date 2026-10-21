# Sharp mollified carrier attempt — step 64

Approved target and prior coverage: `literature/2026-10-11-mollified-carrier-diagonal.md` (SPECIALIZE, unchanged at invocation).
Main gap: global actual-theta mixed positivity. Seek a finite fixed-N carrier diagonal with normalized error o(1), for a later complete signed discriminant mean; no sign or limiting coefficient is assumed.

In-progress reasoning, not yet a proved result: reflect f=-R^(-1) B, B=zeta(1/2-i tau), before taking ordinary derivatives. With L=Log(2+tau) and R'/R=i Omega, the physical carrier cancels exactly:

    K E = (1/2)[h_2/L^2+(2 Omega/L^2+1/L)h_1
                 +((Omega/L+1/2)^2+i Omega'/L^2)h_0]^2,
    h_j=zeta^(j)(1/2-i tau).

On Im tau=11/20 the h_j have absolutely convergent series. The coefficient of n^(-1/2+i tau) in the bracket is

    V_n(tau)=(Omega/L+1/2-log(n)/L)^2+i Omega'/L^2.

Expand the holomorphic mollifier product, retaining indices a,b<=Y=H^(1/100), and the two response indices r,s<=N. The exact zero-frequency condition is mn b=rs a; hence mn<=N^2 Y. The desired Q_N(H) is the real integral of this finite collision sum on [H,2H], divided by 2H.

Checks to finish: absolute convergence with V_m V_n and their derivatives on the top edge; integration by parts for every nonzero log(mn b/(rs a)); both original and diagonal connectors. Near a collision the nonzero integer difference gives reciprocal frequency O_N(Y). The top coefficient mass should be O_N(Y^(21/20)); connectors should be O_N(H^(1/3)Y^(31/20)) using L391's reflected subconvex/Cauchy bound. Each is o(H). No moving cutoff is differentiated in tau. Only the gate-approved reduction is attempted; its finite sum's limit, balanced term, total sign, common-zero bounds and RH remain unresolved.

## Completed attempt

The full proof is now canonical in [L396](../lemmas/L396-sharp-mollified-carrier-diagonal.md). The provisional variable-coefficient plan above was simplified by weighted freezing before the contour shift. Audited L395 bounds its error by O(1/log H), making the remaining Dirichlet coefficients constant in height and the diagonal purely arithmetic. Complete off-diagonal and connector errors are respectively O_N(H^(-1959/2000)) and O_N(H^(-3907/6000)). All meet o(1); no limiting coefficient or sign is claimed. Separate critical review remains pending.
