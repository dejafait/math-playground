# Step562: approved envelope-support calculation, working record

The supplied prior SPECIALIZE assessment is
`literature/2026-11-05-theta-laguerre-envelope-support-test.md`.
Only its exact support inequality is being attempted. Inputs read:
L019, L021 and L795. The full-support interlacing and automatic signed
asymptotic import stops are contrasts, not mathematical premises.

Candidate elementary bound to check: write the normalized Laguerre
polynomial as Q_d(z), put h(v)=exp(-v^2)Q_d(v^2), and verify directly
from its finite coefficients that
h''+2v h'+(4d+2)h=0. The energy
h'^2+(4d+2)h^2 then has derivative -4v h'^2 on v>=0.
Initial values h(0)=1,h'(0)=0 would give |Q_d(z)|<=exp(z).
This is a permitted finite-polynomial bound, not a new asymptotic import.

With l=log d, this would bound the left exterior by
m_0 exp(kappa*d/64). A unit interval starting at 3l/8 lies in I_d
eventually. The positive n=1 theta term should bound A_d below by
C_0 exp(9*kappa*d/512-pi*e^2*d^(3/4)), C_0=4pi(2pi-3)>0.
Their exponent gap is at least d/512-o(d).

For u>=3l/4 use K<=C_K exp(9u/2-pi exp(2u)) and
z<=d*u^2/(2l^2). The ratios u^2 exp(-2u) and u exp(-2u)
decrease there eventually; they should absorb both positive terms
into (pi/2)exp(2u). The remaining integral should be bounded by
C_K exp(-(pi/2)d^(3/2))/(pi*d^(3/2)).

Unfinished at save: verify the polynomial ODE and every uniform onset
condition; combine the two ratios to one exp(-c*d). No signed margin,
relative signed error, zero count, or RH statement follows from these
candidate envelope estimates. No mathematical script is needed.

Completion: the coefficient recurrence verifies the ODE, and the two
ratios close with c=1/2048 and a common existential onset. The full
proof and qualifications are now canonical in
`lemmas/L811-theta-laguerre-exponential-envelope-localization.md`.
This earlier partial reasoning is retained as saved; it is not a second
proof or an independent audit. A separate audit is nominated next.
