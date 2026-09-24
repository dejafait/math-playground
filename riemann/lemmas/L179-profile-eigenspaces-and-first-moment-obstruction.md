# Lemma 179: profile eigenspaces and first-moment obstruction

**Hypotheses.** Use T, N, h, B, E_B and b from L173, c from L177,
and d=Ub from L178, where (Uv)(x)=sqrt(2)v(2/x)/x on [1,2].
For any fixed real C¹ profile v define

F_v(t)=N^(−1/2) Σ_(N≤n≤2N) v(n/N) exp(i(t−π/2)log(n/N)),
p=(b+d)/2, q=(b−d)/2,
ε_N=N^(−1/4)+N^(−1/2)log(2N).

All sums have integer indices and closed endpoints. Write
θ(t)=2π[a log(a/N²)−a−1/8], a=(t−π/2)/(2π), so c=exp(iθ).
The norm ||H||₂ means (E_B|H|²)^(1/2).

**Conclusion.** For each such fixed profile,

||F_v−c conjugate(F_Uv)||₂=O_v(ε_N).                 (1)

In particular Up=p, Uq=−q, and with
X=Re(exp(−iθ/2)F_p), Y=Im(exp(−iθ/2)F_q),

||exp(−iθ/2)F_b−(X+iY)||₂=O(ε_N),                 (2)
E_B|F_b|=E_B sqrt(X²+Y²)+O(ε_N).                  (3)

Put ρ=∫_1^2 b(x)d(x)dx, α=(1+ρ)/2, β=(1−ρ)/2.
Then 0<ρ<1, α+β=1, and

E_B X²=α+o(1), E_B Y²=β+o(1), E_B XY=o(1).       (4)

These phase relations and second-moment data alone allow both a first
absolute moment equal to 1 and a first absolute moment tending to zero.
This is a statement about inference from those data, not about the actual
Dirichlet sums. In particular no improved universal upper bound below
1, and no positive universal lower bound, follows from these data alone.

**Proof.**

L177 gives ||D_y−Q_y||₂=O(N^(1/4)) uniformly in fixed y, and the
pointwise estimate P_y−cD_y=O(log(2N)). Since |c|=1, their triangle
inequality gives ||P_y−cQ_y||₂=O(N^(1/4)+log(2N)).
Repeat the exact Abel calculation in L178 with v in place of b.
Minkowski's integral inequality bounds the normalized error by

N^(−1/2)(|v(2)|+∫_1^2|v'(x)|dx) O(N^(1/4)+log(2N)).

The finite dual coefficient is v(2N/k), including both endpoints,
so the main term is c r conjugate(F_Uv), where
r=sqrt(a)/(sqrt(2)N)=1+O(N^(−1/2)) uniformly on B.
The finite square calculation used in L173, valid for every bounded
fixed C¹ profile w, gives

E_B|F_w|²=∫_1^2 w²+O_w(N^(−1)+N log(2N)/h).       (5)

Indeed its diagonal is a Riemann sum, and each off-diagonal integral
is bounded by 2/(h|log(n/m)|); summing
1/|log(n/m)|≤2N/|n−m| yields the stated error.
As Uv is C¹, (5) controls the scalar replacement in L² by O_v(N^(−1/2)).
This proves (1). This argument uses the square bound in L177 explicitly;
it does not upgrade an L¹ estimate to L² without justification.

L178's involution gives Up=p and Uq=−q. If A=exp(−iθ/2)F_p
and D=exp(−iθ/2)F_q, (1) becomes
||A−conjugate(A)||₂=O(ε_N) and
||D+conjugate(D)||₂=O(ε_N).
Thus ||A−X||₂ and ||D−iY||₂ are O(ε_N). Adding gives (2).
The reverse triangle inequality and normalized Cauchy–Schwarz give (3).

The real involutive isometry U is self-adjoint: its inverse and adjoint
both equal U. Alternatively ∫pq=(∫b²−∫d²)/4=0 directly.
L178 gives ∫b²=∫d²=1, hence ∫p²=α and ∫q²=β.
Positivity gives ρ>0. Equality ρ=1 in Cauchy–Schwarz would force b=d
almost everywhere, which contradicts the nonconstant ratio
 d(x)/b(x)=x³/(2sqrt(2)) in L178. Thus β>0.

Equation (5) gives E_B|F_p|²=α+o(1) and E_B|F_q|²=β+o(1).
The same ordered-pair bound, now with coefficients p(n/N)q(m/N),
gives the Hermitian cross moment

E_B F_p conjugate(F_q)=∫_1^2 pq+O(N^(−1)+N log(2N)/h)=o(1).

Rotation leaves this product unchanged. The L² errors above and
Cauchy–Schwarz, together with bounded second moments, replace A,D by
X,iY in every displayed second moment. Since X conjugate(iY)=−iXY,
this proves (4).

To delimit the inference precisely, on an abstract probability space
let S,R be independent signs taking ±1 with equal probabilities. Set
X=sqrt(α)S, Y=sqrt(β)R. Then EX²=α, EY²=β, EXY=0,
and sqrt(X²+Y²)=1 identically. For any prescribed phase θ, define
A_p=exp(iθ/2)X, A_q=i exp(iθ/2)Y, A_b=A_p+A_q.
These satisfy A_p=c conjugate(A_p), A_q=−c conjugate(A_q) exactly,
and the Hermitian moments above, but E|A_b|=1.

For the opposite behavior, take an independent event I of probability
η>0 and multiply both X and Y by 1_I/sqrt(η). All three second
moments remain identical, while E sqrt(X²+Y²)=sqrt(η), which tends
to zero if η tends to zero. The transform identities remain exact.
These examples can also be realized on the normalized interval B by a
measurable partition and the specified deterministic θ(t). They are not
asserted to have the arithmetic sum representation. They show precisely
why the phase relations and second moments alone cannot decide decay.
Cauchy–Schwarz supplies the common upper bound 1+o(1), attained by the
first model. ∎

## Scope, verification

The symmetric component is approximately real after rotation and the
antisymmetric component approximately imaginary. Their contributions to
absolute value combine as a Euclidean norm, not as signed cancellation.
Additional arithmetic information about the joint amplitudes is needed.
Last-block first-moment decay, uniform integrability, cutoff covariance
and RH remain unproved; the overall argument is unchanged.

Verification is analytic: the uniform L² Abel error, scalar replacement,
profile involution, cross-moment estimate, rotation signs and both exact
probability models are checked above. No numerical certificate is used.

**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
