# Square and actual-Jensen transfer — attempt1383

Approved target and source scope: assessment
`drafts/literature/2026-11-17-jensen-correlation-transfer-second-moment-1381.md`,
SPECIALIZE, saved before invocation. This is one REPRODUCTION research
attempt using C019j(1), C019k(3), and C019l(4)--(21)/(1)--(3).
It addresses signed-mean transfer, not all-degree positivity.

Checkpoint before the canonical write-up: use C019l's exact elementary
functions a_n,f_n,V and its uniform S_d=-V+O(X^(-3/4)) on the closed
band. For the square each ordered pair enters on
[max(X,r_m,r_n),sqrt(2)*X], where U_d(r_k)=k^2; keep the actual floor.
The sum phase has second derivative >=1/(4X), so its entire channel
costs O(X). For m!=n, eta=log(n/m), the unshifted difference has
F'=(1+(pi/8)*Y/d)*eta and F''=(pi/8)*eta/d. Integration by parts with
the checked amplitude variation costs O(1/(sqrt(m*n)*|eta|)); the
classical sum costs O(sqrt(X)*log X). The diagonal costs O(X*log X).
The pointwise reduction error in the square integrates to O(sqrt(X)).

For P(Y)=(-1)^d A_d(-T^2/Y^2)/N_d^norm(T^2/Y^2), the two existing
uniform comparisons give |P-S_d|<=epsilon_d with
epsilon_d=O(1/log d+X^(-1/4))=O(1/log X). On
D=[X,sqrt(2)*X-h], both Y and Y+h lie in the closed band.
Integral Cauchy--Schwarz should pay each cross term by
epsilon_d*sqrt(B)*O(sqrt(X*log X)); the error-error term costs
B*epsilon_d^2. Thus the full product cost is O(X/sqrt(log X)),
whose ratio to B*log X tends to zero.

Remaining work at that initial checkpoint: write and inspect the complete
square specialization, finite-sum expansion, both channels and every
error term in canonical C019m; assemble C019l's negative coefficient
at one common onset, then validate documentation. No new literature
coverage, effective onset, quantitative ordered sample count, root
deficit, bulk separation or RH conclusion is claimed.

## Completed attempt

The full proof is now canonical in C019m (1)--(21); this note retains
the initial partial reasoning without duplicating its full proof.
Both square channels, exact unshifted entry intervals and all three
normalized product-error terms are paid. The resulting product error
is O(X/sqrt(log X)), below any fixed portion of the B*log X margin
eventually. C019l's leading coefficient transfers with its O(X*log log X)
remainder. This is a relevant local advance classified REPRODUCTION.
All quantitative root-count and global gaps above remain unresolved.
The separate conceptual audit is nominated as REVIEW_REQUIRED in
`drafts/literature/2026-11-17-jensen-correlation-transfer-audit-1383.md`.
