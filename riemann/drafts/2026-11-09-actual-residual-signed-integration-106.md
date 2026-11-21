# Fixed signed-residual attempt — working record, step106

Completed: canonical proof, fixed-test stop and execution qualifications
are in `lemmas/L953-fixed-actual-residual-quadrature-endpoint-stop.md`.
The provisional reasoning below is preserved as the pre-execution record.

Approved target: Test whether signed evaluation of L948's actual common-residual response J_p(k-p;8), with a complete integration error and unchanged second-order remainder, can certify v(8)>0.

Main gap: L030–L032/C032a all-degree mixed positivity. This fixed endpoint
input could remove one obstacle to a positive tail from8; interval coverage,
the infinite join, outer mass and independent signs remain open. Stop this
fixed test on zero inclusion, excessive error, unpaid evaluation or
infeasible execution; no parameter refinement. Assessment104 SPECIALIZE
is reused, with the explicit current instruction approving mathematics.

For t in[-1,1], y=(1+t)/2, define
A(t)=y^11 [k(8(1-y))-p(8(1-y))] Q_<=1411(8,y).
Then L948(5)'s prefix integral is pi^5*8^17 times
integral_-1^1 A(t)/sqrt(1-t^2) dt: dy/sqrt(y(1-y)) equals
dt/sqrt(1-t^2). The 4096-node first-kind rule is
pi/4096 sum_j A(cos((2j+1)pi/8192)). Thus its density-scale
interval is pi^6*8^17/4096 times that signed sum.

On ellipse rho=3/2, |y|,|1-y|<=25/24=:a. The energy argument
8(1-y) belongs to L938's energy ellipse, so |k|<10^9.
Using its exact Chebyshev coefficients, |p|<=sum_l |d_l| rho^l.
For t_(k,l)=8^l f_(k,l), let
H=sum_(k,l<=1411) |t_(k,l)| a^(l+6).
Then M=a^11(10^9+sum |d_l|rho^l)H bounds |A| on the full ellipse.
All sums are finite exact rationals. This uses no complex epsilon bound.

Imported Trefethen ATAP8.2 gives a degree8191 projection error
delta=2M rho^-8191/(rho-1). Positive Gaussian weights with mass pi
and exactness through8191 give quadrature error <=2pi delta.
In density units it is <=2pi_+^6*8^17 delta. Complete pointwise
complement is epsilon*pi_+^6*T_8 from L952, and the unchanged
second-order payment is L952's U_2. Every finite-evaluation error
is retained in the signed sum. No sign has yet been established.

Execution will retain all4096 node/residual/polynomial/response intervals,
hash input artifacts, and inspect all checks and full final evidence.
Inherited theta, prefix and full-polynomial execution contracts persist.
