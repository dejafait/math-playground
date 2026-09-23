# Lemma 178: weighted dual profile and involution

**Hypotheses.** Use T, N, h, B, E_B, b, F_T and Z_* from L173,
and a=(t−π/2)/(2π), c and Q_y from L177. Put

C=exp(π²/16)(2π)^(3/4)/sqrt(V(2)),
d(x)=sqrt(2)b(2/x)/x  (1≤x≤2),
G_T(t)=N^(−1/2) Σ_(N≤k≤2N) d(k/N) exp(−i(t−π/2)log(k/N)).

**Conclusion.** With all sums over integers and closed endpoints,

E_B|F_T−cG_T|=O(N^(−1/4)+N^(−1/2)log(2N))=o(1).       (1)

In particular E_B|Z_*| tends to zero if and only if E_B|G_T| does.
The explicit fixed coefficient is

d(x)=C x/(2sqrt(2)) exp(−(log x−log(2)/2)²),
d(x)/b(x)=x³/(2sqrt(2)).                              (2)

The profile operator (Uv)(x)=sqrt(2)v(2/x)/x is an involutive
isometry of real L²([1,2],dx). Thus ∫d²=∫b²=1. Both b and d
are positive smooth profiles bounded above and below by positive
constants. The transform retains a sum of order N terms and does not
by itself prove decay of its normalized first absolute moment.

**Proof.**

Write R_y=P_y−cQ_y. L177 gives a bound
E_B|R_y|≤C_0(N^(1/4)+log(2N)) uniformly over fixed y∈[N,2N].
Insert this in the exact Abel identity of L173. The triangle inequality
and Tonelli applied to |b'(y/N)||R_y(t)| give total error at most

N^(−1/2) [|b(2)|+∫_1^2|b'(x)|dx]
 C_0(N^(1/4)+log(2N)).                               (3)

These finite sums and integrals are measurable and bounded for each T;
no t-dependent truncation or expectation of a supremum is used.
For any k in the fixed interval [N,2N], membership in Q_y is precisely
y≥2N²/k. Interchanging the finite dual sum and the y integral, its
coefficient is therefore

b(2)−∫_(2N²/k)^(2N) b'(y/N)dy/N=b(2N/k).

This also holds at k=N and k=2N when those are integers: a singleton
integration endpoint has measure zero. Consequently the substituted
expression equals exactly

c(t) N^(−1/2) Σ_(N≤k≤2N) (sqrt(a)/k)b(2N/k)
                      exp(−i(t−π/2)log(k/N))
= c(t) r(t) G_T(t),  r(t)=sqrt(a)/(sqrt(2)N).          (4)

On B, a=2N²−δ with 0<δ≤h/(2π)+1/4=O(N^(3/2)), so
sup_B|r−1|=O(N^(−1/2)). To control this scalar replacement without
a trivial pointwise loss, expand the averaged square of G_T. Since d
is bounded, its diagonal is O(1). For distinct k,l, the phase integral
has normalized modulus at most 2/(h|log(k/l)|). Using
1/|log(k/l)|≤2N/|k−l| and summing differences gives

E_B|G_T|²≤C_1[1+N log(2N)/h]=O(1).

Cauchy–Schwarz now yields E_B|(r−1)G_T|=O(N^(−1/2)). Combining
with (3) proves (1). Since |c|=1, the reverse triangle inequality
transfers first moments; L173's comparison to Z_* completes the claimed
equivalence.

For (2), log(2/x)−log(2)/2=−(log x−log(2)/2), so the Gaussian
factor is unchanged by reflection. The remaining powers give
sqrt(2)x^(−1)(2/x)^(−2)=x/(2sqrt(2)). This proves both formulas.
For any real square-integrable v, direct substitution gives U(Uv)=v
almost everywhere and, with z=2/x,

∫_1^2 |Uv(x)|²dx=∫_1^2 (2/x²)|v(2/x)|²dx
                       =∫_1^2 |v(z)|²dz.

L173 supplies ∫b²=1. Smoothness and strict positivity follow from the
explicit formulas and compactness. In fact b decreases, whereas
xd'(x)/d(x)=1−2log x+log 2≥1−log 2>0, so d increases.
This is a different coefficient profile, not an identical sum. Applying
U twice returns b; the transformation of coefficients provides no
contracting norm and no first-moment bound tending to zero. This last
observation concerns what the displayed identities establish, not an
impossibility theorem for other cancellation arguments. ∎

## Scope, verification

The weighted dual representation completes the specified Abel step.
The remaining cancellation estimate, uniform integrability, cutoff
covariance and RH are unproved. No overall argument changes.
Analytic verification checks the fixed-y error integration, both integer
endpoints, exact scalar factor, harmonic square bound, Gaussian reflection,
derivative sign and Jacobian of the isometry. No numerical certificate is
needed.
**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
