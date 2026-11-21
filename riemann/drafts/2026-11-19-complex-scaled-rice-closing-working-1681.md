# Weighted finite Rice closing — working1681

Ready target: assessment1679/1680, SPECIALIZE, exact A_d(i) only.
Inputs: C048k's entire E and sample values; C048l(7)--(13), (21),
and its unweighted closing bound. No new source or script needed.

Provisional calculation, not yet an audited result: the principal
multiplier has modulus exp(-x log d + pi y/2). On the top-left
subarc c<=x<=c+1/log d this is at least
exp(pi h/2+(log d)/4-1). C048l's actual corner logarithm is
-(pi-1/2+o(1))D. Bound the absolute derivative of its explicit
main term G_d by 4log d, retaining the uniform o(1) error instead
of differentiating it. This would keep the actual log modulus
within 4+o(1) below its corner throughout that subarc. Integration
would give liminf log A_d(i)/h>=pi/2. The uniform multiplier bound
on all three sides and C048l's A_d<=exp(-D) would give the reverse
limsup. Check the derivative, residue signs and full lower comparison
before moving this calculation to a canonical result. This would
stop only this rectangle's absolute budget, not signed cancellation,
all contours, compact zero mass or RH.
