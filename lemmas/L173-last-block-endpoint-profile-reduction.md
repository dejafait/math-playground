# Lemma 173: last-block endpoint profile reduction

**Hypotheses.** Use the frozen sums and block definitions of L169 and
variance V of L170, with H=T^(3/4), J=ceil(T/H), h=T/J,
N=sqrt(T/(2π)), and T sufficiently large. Write B=[2T−h,2T],
E_B for normalized integration on B, u_*=2−h/(2T), and
Z_*=S_(J−1)⁰/sqrt(V(u_*)). Define on 1≤x≤2

b_u(x)=exp(π²/16)(2π)^(3/4) x^(−2)
       exp(−(log x−(log u)/2)²)/sqrt(V(u)),
b(x)=b_2(x),
F_T(t)=N^(−1/2) Σ_(N≤n≤2N) b(n/N) exp(i(t−π/2)log(n/N)).

All sums include precisely the integers in the indicated closed interval.

**Conclusion.** The first absolute moment obeys

|E_B|Z_*|−E_B|F_T|| ≤ C T^(−1/4).                       (1)

Consequently it tends to zero if and only if E_B|F_T| tends to zero.
Moreover

E_B|F_T| ≤ 1+O(T^(−1/4)log T).                          (2)

For N≤y≤2N put P_y(t)=Σ_(N≤n≤y) exp(i(t−π/2)log(n/N)).
Then the exact identity and upper bound are

F_T(t)=N^(−1/2)[b(2)P_(2N)(t)
                      −∫_N^(2N) b'(y/N)P_y(t)dy/N],    (3)

E_B|F_T| ≤ N^(−1/2)[b(2)E_B|P_(2N)|
                +∫_N^(2N) (−b'(y/N))E_B|P_y|dy/N].    (4)

In particular sup_(N≤y≤2N) E_B|P_y|=o(sqrt(N)) is sufficient
for vanishing in (1). This sufficient condition is unproved here.
The elementary second-moment bounds for these partial sums yield only
O(sqrt(N)), not the required little-o estimate.

**Proof.**

L170's amplitude formula and T=2πN² give exactly
Z_*(t)=N^(−1/2)Σ b_(u_*)(n/N) exp(i(t−π/2)log(n/N)).
The positive continuously differentiable function V has positive minimum
on [1,2]. Thus b_u(x) and its u derivative are bounded on [1,2]².
Since |u_*−2|=h/(2T), every coefficient of Z_*−F_T has modulus
at most C N^(−1/2)h/T. The diagonal in its averaged square is
O((h/T)²). The two integrated endpoints of each distinct frequency pair
give a bound 2/(h|log(m/n)|). For completeness,

1/|log(m/n)| ≤ 2N/|m−n|  (N≤m,n≤2N, m≠n),

by the mean value theorem, so summing over the O(N) choices for the
smaller index and all positive differences gives O(N²log(2N)).
This includes both orders. Consequently

E_B|Z_*−F_T|² ≤ C(h/T)²[1+N log(2N)/h].

Here h lies between T^(3/4)/2 and T^(3/4), and the bracket is bounded.
Normalized Cauchy–Schwarz and ||z|−|w||≤|z−w| prove (1).
In particular the small motion of the last midpoint cannot by itself
change whether the first absolute moment vanishes.

The same finite square calculation for F_T gives an off-diagonal
O(N log(2N)/h). A bounded-derivative mesh comparison, including at most
two incomplete boundary cells and any endpoint sample, gives

N^(−1)Σ b(n/N)²=∫_1^2 b(x)²dx+O(N^(−1))=1+O(N^(−1)).

The last equality is exactly L170's formula for V(2). Thus
E_B|F_T|²=1+O(T^(−1/4)log T), and Cauchy–Schwarz proves (2).
The upper-bound notation in (2) means at most 1+C T^(−1/4)log T;
no claim of a matching first-moment asymptotic is intended.

For every integer n in the window, the fundamental theorem of calculus
states b(n/N)=b(2)−∫_n^(2N)b'(y/N)dy/N. Multiplying by its phase
and interchanging a finite sum with this integral proves (3), including
integer endpoints (values at finitely many y do not affect the integral).
Logarithmic differentiation gives

b'(x)/b(x)=[−2−2log x+log 2]/x<0  (1≤x≤2).

The triangle inequality followed by finite-interval integration gives
(4). Its nonnegative weights total b(2)+∫_1^2(−b'(x))dx=b(1),
so its right side is bounded by b(1)N^(−1/2) sup_y E_B|P_y|.
This proves the sufficient condition without asserting its necessity.

Finally the same ordered frequency bound, now with unit coefficients,
shows uniformly in y

E_B|P_y|² ≤ C[N+N²log(2N)/h]=O(N).

Cauchy–Schwarz gives only E_B|P_y|=O(sqrt(N)). Substitution in
(4) is O(1). This calculation provides no decaying upper bound and no
positive lower bound for the actual first moment. ∎

## Scope, verification, and formalization obligations

This completes the endpoint-profile reduction part of the last-block
analytic question. The finite probe's decline has neither been proved
to continue nor disproved. Arithmetic phase cancellation remains the
missing estimate; the block B still moves with T. Uniform integrability,
cutoff covariance and RH remain unproved. No random independent-phase
model or infinite-time averaging is substituted for this block.

Verification is analytic: the N normalization, positive lower bound for
V, coefficient derivative, both oscillatory endpoints, ordered harmonic
sum, Riemann mesh endpoints, exact integral normalization, derivative
sign and finite Abel identity are explicit. Formalization would require
these finite-sum and compact integral bounds. No numerical certificate
is needed.

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
