# Moving-saddle complement attempt1363 — 17 November 2026

Approved target: assessment1362's exact lower-semicircle complement on
d^(-1/2)<=q-q_e(d)<=2*d^(-1/2), relative to |Z_d(q)|.
Main gap: L030-L032/C032a actual-Xi all-degree positivity; a successful
complement estimate could support a separate growing phase-barrier count.
No root count, every-degree sign theorem or global closure is attempted.

Reused coverage: drafts/literature/2026-11-17-jensen-moving-saddle-complement-1362.md
(EXPLORE, supplied before invocation). C019c/C019d supply exact conventions
and derivative algebra, not conclusions outside their fixed windows.
Stops1345/1355/559 were checked and remain preserved. No extra literature
assessment is required for retrieval of the already assessed primary inputs.

Initial proof plan, not yet a result: alpha is comparable to d^(-1/4).
Retain the exact phase derivative U=(A+1)(cos(alpha)-cos(beta)) on both
beta<alpha and beta>alpha, outside distance ell_q/2 from alpha. Seek a
bound of order 1/(d alpha^2) for the normalized near-endpoint complement;
division by the Gaussian angular scale (d alpha)^(-1/2) would give
O((d alpha^3)^(-1/2)). All phase second derivatives, amplitude derivatives,
four near-interval boundary terms and the distant exterior still need
verification. This is a proposed bound, not evidence that it holds.

Continuation test: obtain a uniform vanishing majorant including the
endpoint theta=0, with all source hypotheses at one common onset.
Abandon this implementation if a retained term prevents that conclusion;
failure of a majorant alone would not refute the target limit.

## Completed calculation, superseded by canonical C019h; later audit pending

Put s=epsilon_0/2, u=1-s, v=1+s, b=theta_0/2. On the endpoint
interval 0<=beta<=u*alpha, the exact derivative has modulus at least
k_minus*alpha^2, k_minus=(1-u^2)/2. On v*alpha<=beta<=b it has
modulus at least k_plus*beta^2, k_plus=(1-v^(-2))/2. Direct angular
differentiation gives |phi''|<=4*max(alpha,beta). The amplitude and
its actual theta derivative have uniform fixed bounds B0,B1, because
Re(1/2+w)>=1/2+Tr/2 throughout the fixed small-angle interval.

One finite integration by parts on each interval, retaining all four
boundary terms, gives |J_near|<=K2/(d*alpha^2)+K1/(d*alpha).
The fixed exterior gives |J_far|<=C*T*exp(-gamma*d). Exact division
by |Z_d| multiplies these bounds by sqrt(d*|D_q|/(2*pi)). Thus the
proposed bound succeeds with O(d^(-1/8)) uniformly on the entire band.
The canonical C019h proof gives the positive K1,K2 and each unsimplified
endpoint/remainder term; no numerical experiment was needed. This is
an established-method specialization outside the source's stated
vanishing-complement range, not a root count or a verified RH candidate.
