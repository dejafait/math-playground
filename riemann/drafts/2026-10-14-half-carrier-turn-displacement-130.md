# Half-carrier-turn scalar test — step 130

Approved target and prior SPECIALIZE coverage:
`literature/2026-10-14-half-carrier-turn-displacement.md` (unchanged).
Main gap: global mixed positivity, with actual negative-Bcal clipped
signed mean unresolved. Intermediate target: decide the exact scalar
fourth displacement at the phase-defined half turn. Downstream use:
necessary scalar check for the proposed opposite-phase frozen-jet pairing.
Continue that implementation only if the complete coefficient vanishes
and the remainder is little-o(log^4 H); abandon if it is positive.

Inputs inspected: L389's zero-safe f=-sigma Z_Hardy and ordinary first
fourth-moment envelope; L390's actual gamma phase bounds; L383's
small-offset carrier-ratio passage. Reused the supplied primary source
comparison and checked the step-99 sign-symmetry stop. No source refresh
or new moment theorem is needed. Existing notebook edits are preserved.

Work checkpoint before final write-up: put ell=log H, h=2pi/ell.
The exact delta is h+O(ell^-2). If w bounds that error, FTC/Holder and
Fubini on the fixed strip |v|<=w give integral |f(t+delta)-f(t+h)|^4
<=2w^4 integral_[H/2,3H] |f'|^4 = O(H); harmless absolute constants
are suppressed here. Thus the quartic statistic replacement costs
O(H ell^3), using the scalar fourth moment O(H ell^4).

For k shifted factors choose positive/negative orientations (a,b) equal
to (0,0),(1,0),(1,1),(2,1),(2,2). Their Hardy phase ratios are
(-1)^k+O(ell^-1). Bui--Hall Proposition 3 then gives individual
coefficients c_0=c_4=1/(12 zeta(2)), c_1=c_2=c_3=1/(4pi^2 zeta(2)).
The complete binomial coefficient is (pi^2-3)/pi^4>0. Detailed exact
integrations, error budgets and qualifications are now canonical in
L412; the separate critical audit remains pending. This is a reproduction/specialization, not a new moment theorem.

No derivative displacement, response-product transfer, clipped signed
mean, regulator choice, total pencil margin or RH consequence follows.
