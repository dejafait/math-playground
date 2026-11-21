# Opposed-frequency full-law attempt932 — working record

Approved target: continuation930, unchanged EXPLORE scope. One analytic
attempt at the actual K(r), x=B'(1), using C466a/C466k and their inherited
L018/external qualifications. No numerical certificate, contour change,
finite-core replacement or extra PF/Gaussian-mixture input is used.

Main gap: L030-L032/C032a actual-Xi all-degree positivity. The intermediate
test is K(r)>=0 for every real r; a negative value at one nonzero r stops
the pointwise marginal mechanism. Passing the slice leaves the full
two-frequency sign, determinant integration, all orders/all x and Xi
transfer unpaid. Identity or symmetry alone is not a sign result.

Local reading completed: full C466a/C466k, L018, nomination929's completed
primary-source and duplicate/failure comparison, and stop927/audit929.
The approved convolution, inversion and bilinear determinant assessments
are reused without fresh browsing. Existing notebook changes are retained.

Preliminary algebra to verify in full: write F(t)=A_x(1+it). For N=3,
Andreief and C466k's polynomially weighted inversion suggest
D_3(p;x)=1/(6(2pi)^3) integral Delta(t_1,t_2,t_3)^2 product F(t_j) dt.
Use t_1=t+a, t_2=t+b, t_3=t-a-b; absolute Jacobian 3.
The squared real Vandermonde is
(a-b)^2(2a+b)^2(a+2b)^2, equal to 4r^6 at (a,b)=(r,0).
Polynomial absolute integrability follows from the fixed-line bound.

Prospective conditional identity: q(u)=h(1)e^(-u)p(u), S=3x,
Z(S)=(q*q*q)(S)>0. A specific continuous conditional density on
u>0, v>0, u+v<S is q(u)q(v)q(S-u-v)/Z(S).
K(r) should be 2pi exp(3x)/h(1)^3 times Z(S) times the expectation
of exp(-ir(U_1-U_3)) under this law. Complex convolution/inversion,
pointwise continuity, exact constants and positive normalizer still
require the full write-up. The conditional variables are dependent;
the independent-difference square formula cannot be applied as stated.

Sign work in progress: no all-r factorization or negative witness has
been found. A partial sign mechanism now being checked is
K(r)*|h(1+ir)|^2 -> 2pi*p(3x)>0 as |r| tends to infinity.
The pointwise normalized integrand tends to
exp(3ixt)/h(1+it), whose integral is known exactly by C466k(7).
The load-bearing unfinished obligation is uniform absolute domination.

Proposed domination split: let b(v)=log|h(1+iv)|, an even smooth function.
C466a's sector expansion suggests b(v)=k*sqrt(v)*log(v)+ell*sqrt(v)
+(7/8)*log(v)+C+O(log(v)/sqrt(v)), k=1/(4sqrt(2)), with eventual
positive derivative and b''(v)=O(log(v)/v^(3/2)). Set
E_r(t)=b(t+r)+b(t-r)+b(t)-2b(r).
For |t|<=epsilon*r, use the symmetric second-derivative bound to absorb
the deficit in b(t). For epsilon*r<=|t|<=2r, use the strictly positive
continuous expression sqrt(1+s)+sqrt(|1-s|)+sqrt(s)-2 for s>0.
For |t|>=2r, eventual monotonicity gives E_r(t)>=b(t).
The intermediate uniform expansion must include s=1, where one argument
vanishes; large-argument asymptotics cannot be used there without a
compact-range bound. These checks are unfinished here.

If completed, this is only eventual positivity with an existential
onset. It cannot pass the all-r slice test, and it supplies neither an
effective finite interval nor a negative actual density minor.

Completion932: the full proof is now canonical in C466l. It uses the
explicit part's second derivative and a bound on remainder values,
not the provisional differentiated-remainder assertion above. The
large-t argument uses only monotonicity of sqrt(t)*log(t), not b.
The uniform middle-range expansion explicitly includes a=0. The
result is local and eventual strict positivity, with no all-r sign
or effective onset. The conditional iid-mixture square shortcut is
excluded by support; it is not a negative K witness. The next audit
scope is nominated separately as REVIEW_REQUIRED. Earlier unfinished
reasoning is preserved here; use C466l for the actual proof.
