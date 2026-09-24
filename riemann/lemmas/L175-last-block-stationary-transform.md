# Lemma 175: last-block stationary transform

**Hypotheses.** Use T, N, h, B, E_B and P_(2N) as defined in L174.
Put a=(t−π/2)/(2π) and e(v)=exp(2πiv). Define the finite sum

D_T(t)=Σ_(a/(2N)≤k≤a/N) (sqrt(a)/k)e(−a log(k/N)),

with integer k and closed endpoints.

**Conclusion.** Uniformly for every t in B,

P_(2N)(t)=e(a log(a/N²)−a−1/8)D_T(t)+O(log(2N)).       (1)

This includes integer and arbitrarily near-integer endpoint slopes. Hence

|E_B|P_(2N)|−E_B|D_T||=O(log(2N))=o(sqrt(N)).           (2)

The proposed o(sqrt(N)) first moment for the full endpoint is therefore
equivalent to that for D_T. The dual sum still has Θ(N) terms with
positive amplitudes bounded above and below by absolute constants.
Moreover

E_B|D_T|²=N+O(N²log(2N)/h+sqrt(N)log(2N)+log²(2N)+1). (3)

In particular its normalized second moment tends to one. The transform
and Cauchy–Schwarz give only O(sqrt(N)) for its first moment, not little-o.
No nonvanishing first-moment conclusion is asserted.

**Proof.**

For each fixed t set f(x)=a log(x/N) on [N,2N]. L174's parameter
bounds give N²/2≤a≤2N². Apply the C^4 B-process in foundations to
−f, with interval length parameter M=N, phase size Q=a, and amplitude
one. Indeed (−f)''=a/x² is comparable to a/N², while the absolute
third and fourth derivatives are 2a/x³ and 6a/x⁴. Their comparison
constants are uniform in t. The error is

O(N/sqrt(a)+log(2+a/(2N)))=O(log(2N)).

Conjugating the transform and replacing its negative integer frequency
by −k yields stationary points x_k=a/k for a/(2N)≤k≤a/N.
The amplitude and phase are exactly

1/sqrt(|f''(x_k)|)=sqrt(a)/k,
f(x_k)−kx_k−1/8=a log(a/(kN))−a−1/8.

Factoring out e(a log(a/N²)−a−1/8) proves (1).
The cited theorem is uniform at endpoint slopes; no inverse distance to
an integer is inserted. Even if one uses starred endpoint sums instead,
there are at most two changed primal terms of modulus one and at most
two changed dual terms of modulus at most 2N/sqrt(a)≤2sqrt(2).
Thus either convention gives (1) with the same error order. This also
accounts for jumps of the displayed dual sum at endpoint crossings.

The factor extracted in (1) has modulus one, proving (2) by the reverse
triangle inequality and normalized integration. The number of k is
a/(2N)+O(1)=Θ(N), and N/sqrt(a)≤sqrt(a)/k≤2N/sqrt(a).
After dropping the common phase, the dual logarithmic phase is
−a log(k/N); its second derivative is a/k²=Θ(1), and its third
has size Θ(1/N). These are the same derivative scales as the primal
sum, with curvature sign reversed. Its moving frequency interval must
not be replaced by an independent-phase or infinite-time average.

For (3), write the error in (1) as R with |R|≤C log(2N). Then

||D_T|²−|P_(2N)|²|≤2|P_(2N)||R|+|R|².

L174 gives E_B|P_(2N)|≤C sqrt(N) and its exact square-mean estimate.
Integration proves (3). Since h is comparable to N^(3/2), the error
is o(N). Cauchy–Schwarz thus supplies only E_B|D_T|≤(1+o(1))sqrt(N).
This is an equivalence of the remaining first-moment problems and an
audit of these bounds, not an impossibility theorem for other uses of
the dual phases. ∎

## Scope, verification

This completes the requested full-endpoint transform with uniform
little-o error. It does not address every truncated endpoint in L173,
nor prove uniform integrability, cutoff covariance or RH. The overall
argument is unchanged.

Analytic verification checked all four derivatives, the sign under
conjugation, the exact stationary point and common phase, the closed
endpoint convention, uniform error constants and the transfer of square
means. No numerical
claim or computational certificate is used.

**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
