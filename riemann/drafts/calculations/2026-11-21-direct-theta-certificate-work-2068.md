# Direct theta coefficient certificate — work2068

Approved target: certify c0,c2,c4,c6, each width <=2^-40, by the
prior SPECIALIZE assessment2066. This is a known-method reproduction.
Main gap remains actual-Xi all-degree mixed positivity. The four inputs
may support a later L530 degree-six test; that test is outside this step.

Plan saved before execution: take X=16, N=4, and derive a uniform C4
bound for the finite integrands. Select an even power-of-two Simpson
panel count <=2^18 from that bound; use <=100 Decimal digits. Separate
spatial, theta-index, quadrature, and arithmetic errors. Preserve bounds
and failures if the cap or final width test fails. All initial-root,
collision, all-degree and Xi-transfer questions remain unresolved.

Use Romik1902.06330v3 (1.7)/(3.3), retrieved to confirm the exact
summands and normalization; reuse the saved literature comparison.
No reproof of the coefficient identity. Existing unfinished work and
centered-series stop2065 are preserved. No cross-notebook input.

Derived bounds before integration (pending replay): write a=pi*n^2,
g_n=(2a^2*x^2-3a*x)e^(-a*x), u=(x-1)/(x+1), v=(x+1)^(-3/2).
For x>=1, x^q e^(-a*x)<=e^(-a) for q<=2. Leibniz on g gives
G_r=sum_(n=1)^4 20^(-n^2)[A^r(2A^2+3A)
+r A^(r-1)(4A^2+3A)+binom(r,2)A^(r-2)4A^2], A=22n^2/7;
omit terms whose derivative order is unavailable. Here pi>3,
pi<22/7 and e^3>20. For w=u^k*v, start V_r=(3/2)_r/2^(r+1)
and convolve k times with U_s=s!/2^s, s=0,...,4. This bounds every
w derivative on the whole interval, since u<=1 and
|u^(s)|=2s!/(x+1)^(s+1) for s>=1. M4=6 sum binom(4,r)G_r W_(4-r)
bounds the complete finite f_k fourth derivative. The rational bounds
are below 51612 for all k=0,2,4,6; with 2^18 panels the largest Simpson
error is below 4.611e-14, inside the width budget.

All summands are positive. Dropping w<=1 and using 4sqrt2<6,
2pi^2<20 bounds omitted-index integral n>=5 by
120 sum n^4 e^(-3n^2)(1/(3n^2)+2/(9n^4)+2/(27n^6))
<=80 sum n^2 20^(-n^2)<=4000/20^25 (successive ratios <1/2).
For x>=16, successive n^4 e^(-3n^2*x) ratios <=16e^(-9x)<1/2;
the full spatial integrand is <=240x^2e^(-3x), with integral
<=240*20^(-16)*(16^2/3+32/9+2/27). These majorants also justify
sum/integral use by positivity and integrability. Gamma integrals are
integer cases of the imported DLMF identity.

Completed: all four intervals passed, largest width <4.615e-14 against
2^-40. Canonical proof: C530a; full execution evidence:
`scripts/pollaczek/direct-theta-coefficients-2068.json`. The preliminary
M4 bounds above are conservative (the executed V_0=1/2 bounds yield
smaller constants). No failed cap, width, positivity or runtime test.
Independent audit remains pending; no downstream diagnostic performed.
