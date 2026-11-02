# Inverse-parameter polynomial attempt — step 50

The invocation-start EXPLORE assessment is
`drafts/literature/2026-11-02-inverse-parameter-polynomial-separator.md`.
This is one mathematical attempt at its exact TARGET, with all of L666's
factors and normalized angular pairing. Existing unfinished work is
preserved. No external source refresh or cross-notebook input is needed.

Main gap: actual-Xi all-degree mixed positivity. The intermediate target
is a real polynomial action with the prescribed degree, three values,
closed-segment signs, and angular cost at rate 1/100. A successful action
could separate the positive cone; original unit-residue H, support and Xi
realization would remain independent gaps. Continue only with a complete
construction/cost or a useful exact restriction; park this polynomial
class if exact infeasibility or an unavoidable rate above 1/100 is proved.

## Reasoning checkpoint before further work

Write J=n-1, r=d/R=10/11, and define the finite Blaschke product

    b(v)=product_(1<=j<=J) (v-t_j/R)/(1-(t_j/R)*v).

L666's full rational identity factors exactly as

    W_a(u)=(x/a)*b(R*u/a)/b(R*u/x).

The j=0 factor remains x/a. On the actual angular circle the fixed
denominator b(R*u/x) is finite and nonzero: its zeros have modulus
t_j/R<1, whereas |R*u/x|=11/10, below every pole R/t_j.
If b(v)=sum_(k>=0) beta_k v^k, the exterior parameter action therefore
has coefficients determined by all angular moments of
conjugate(psi(u))/b(R*u/x). On compact subsets of |a|>tau, the expansion
converges uniformly in u; L2-to-L1 makes coefficient extraction valid.

The next calculation must retain possible zero beta_k. A polynomial
preimage cannot be obtained by dividing by coefficients whose nonvanishing
has not been proved. Weighted L2 control, including any free Fourier
modes, is also still unpaid. The circle attenuation from L674 alone
does not exclude degree n: it supplies a necessary condition only.

Compared the exact source-covered target with C645o/C645p, L668, L673
and the finite-polar stop; their different scoped obstructions do not
settle this polynomial class. L674's separate audit remains outstanding.
No polynomial feasibility, uniform inverse bound, or RH candidate has
been claimed at this checkpoint.

## Completed analytical direction

The coefficient identity gives an exact finite-polynomial range test:
with lambda=R/x=-11/10, p_(k+1)=beta_k*lambda^k*m_k. If beta_k=0,
that polynomial coefficient must vanish. Otherwise its required angular
moment is m_k=p_(k+1)/(beta_k*lambda^k). Taking
conjugate(psi)=b(lambda*u)*sum m_k*u^(-k) realizes every such polynomial
throughout |a|>tau. Extra Fourier modes are allowed for other preimages;
no assertion that this explicit preimage is the minimum-norm one is made.

For the actual grid, factorwise angular extrema and convexity in t_j/R
give min|b(lambda*u)|>=(23/22)^J. Cauchy's coefficient bound on |v|=1/2
and concavity in t_j/R give |beta_k|<=(19/26)^J*2^k. Thus any degree-m
polynomial action with P(1)=1, even without the sign and zero conditions,
requires

    ||psi||_2 >= (6/5)*(299/209)^J / ((11/5)^m-1).

For m<=3n/7, this is greater than
(1254/1495)*exp((1503/97790)*n), whose exponent exceeds 1/100.
This excludes low-degree actions only, not the full degree-at-most-n
target. It is a refined continuation restriction, not a general cone stop.

The cubic P(w)=w*(11*w-10)*(3-2*w) satisfies all three values. For
w=1/(1-i*t), |t|<=9/25, its real part is
(1+6*t^2-83*t^4)/(1+t^2)^3>0. The first three beta coefficients are
nonzero for every n>=15 in the family, so the displayed exact inverse
exists. Every inverse of this cubic has norm at least
30*(23/22)^J*(n*R)^J/J! >= 30*(23/8)^J. No cost-budget construction
has been found. Full proofs and source qualifications are canonical in
`lemmas/L675-inverse-parameter-polynomial-range-and-degree-cost.md`;
the higher-degree, full-cost problem remains open. All 19 exact arithmetic
checks passed and their complete output was inspected. This does not
constitute a separate critical audit of L675.
