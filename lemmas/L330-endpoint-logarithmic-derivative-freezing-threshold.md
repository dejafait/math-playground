# Lemma 330: endpoint logarithmic-derivative freezing threshold

**Hypotheses.** Let r=2n tend to infinity, a=a_n=sqrt(4π²exp(4r)−25),
c=1/2+1/r and σ=1+1/r. Use K_r, F_r(v,a), B_r(a) and
Z_r(a;c)=∫_ℝ K_r(v)F_r(v,a)dv from L303–L304. Put

V_r=log(r)/sqrt(r),  g(s)=ζ′(s)/ζ(s),
M_r=sup_(|u|≤V_r) |g(σ+i(a+u))|,
E_r=(1+r)²exp(−r/256).

The supremum is finite since σ>1 and the Euler product has no zeros there.
The bounds tested below are the unconditional classical zero-free-region
estimate g(σ+it)=O(log |t|), and its Vinogradov–Korobov improvement
g(σ+it)=O((log |t|)^(2/3)(log log |t|)^(1/3)), uniformly for σ≥1
and sufficiently large |t|. They are cited precisely in the proof.

**Conclusion.** For sufficiently large r, if M_r≤sqrt(r), then

|Z_r(a;c)/B_r(a)−1|
 ≤ C M_r/sqrt(r)+C(r+1)^4 exp(−(log r)²/8).                 (1)

Thus M_r=o(sqrt(r)) would prove Z_r/B_r=1+o(1), and hence a positive
margin exceeding E_r. Neither tested bound proves this hypothesis:
their available envelopes for M_r/sqrt(r) have orders sqrt(r) and
r^(1/6)(log r)^(1/3), respectively. These are envelopes, not lower
bounds on the actual M_r or the actual integral error.

The scale sqrt(r) is sharp for a comparison based only on this derivative
magnitude, nonvanishing and conjugate pairing. For λ≥0 replace ζ by
the entire zero-free function G_(r,λ)(s)=exp(λ(s−σ)). Its square at
σ+ia is 1, its paired factor is exp(2iλv), and exactly

∫_ℝ K_r(v)exp(2iλv)dv
 =exp(−2cλ)(1+λ/r)^r.                                    (2)

For λ=b sqrt(r), fixed b>0, this tends to exp(−b²/2), not 1.
For λ=r^(2/3)(log r)^(1/3), it tends to zero, with logarithm

−(1/2+o(1))r^(1/3)(log r)^(2/3).                           (3)

This model is not the zeta function and has no asserted Dirichlet-series
or functional-equation structure. In fact its integral is positive and,
in both examples, much larger than E_r. It obstructs the stated relative
freezing inference, not endpoint positivity itself. No actual zeta sign,
additional zero-exclusion range, or RH candidate is established.

**Proof.** Absolute Dirichlet convergence and conjugation give
g(conj s)=conj g(s). For real v with |v|≤V_r the quotient of the two
nonzero paired factors has the exact expression

F_r(v,a)/B_r(a)=exp(A_r(v)),
A_r(v)=i∫_0^v [g(σ+i(a+t))+g(σ+i(t−a))]dt.                 (4)

One can verify (4) by differentiating the quotient and using its value
1 at zero; thus no unspecified branch of log ζ is needed. The second
term is conj g(σ+i(a−t)), so |A_r(v)|≤2M_r|v|, and

|F_r(v,a)/B_r(a)−1|≤2M_r|v|exp(2M_r|v|).                  (5)

The first derivative in (4) is
A_r′(0)=2i Re g(σ+ia). Conjugate pairing therefore retains a linear
phase; it does not cancel the first variation or create a modulus
square away from v=0.

L304 proves ∫K_r=1 and, on |v|≤c,
|K_r(v)|≤C sqrt(r)exp(−rv²/4). For large r, V_r<c. Using (5), the
contribution of |v|≤V_r to the absolute relative error is at most

C(M_r/sqrt(r))∫_ℝ |w|exp(−w²/4+2(M_r/sqrt(r))|w|)dw.

If M_r≤sqrt(r), the integral is bounded by the finite constant
∫_ℝ |w|exp(−w²/4+2|w|)dw. This is an integrated variation estimate;
it requires no extra log r loss from taking a supremum over the window.

For the omitted part, L304 gives
∫_(|v|>V_r)|K_r(v)|dv≤C exp(−(log r)²/8).
Also |F_r(v,a)|≤ζ(σ)²≤(r+1)² for every real v and
B_r(a)≥(r+1)^(−2). Consequently

∫_(|v|>V_r)|K_r(v)| |F_r(v,a)/B_r(a)−1|dv
 ≤C[(r+1)^4+1]exp(−(log r)²/8).                            (6)

This tends to zero faster than any inverse power of r. Combining the
two regions and the exact normalization proves (1). In particular,
if M_r=o(sqrt(r)), then Z_r is eventually at least B_r/2, and

(B_r/2)/E_r ≥ exp(r/256)/(2(r+1)^4) →∞.

L303's whole-plane formula then proves the conditional endpoint sign,
using the sufficient margin of L302. It is not necessary for the tail
in (6) to be smaller than E_r: here it is compared with B_r first.
The hypothesis on M_r is not established for the prescribed heights.

For the precise external inputs, E. C. Titchmarsh, *The Theory of the
Riemann Zeta-function*, second edition revised by D. R. Heath-Brown
(1986), [Theorem 3.11, equation (3.11.7), p. 60](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf#page=35),
gives g(s)=O(log |t|) in a region Re s≥1−A/log |t|, for sufficiently
large |t| and a fixed A>0. The same book's
[Section 6.19, p. 135](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf#page=72),
applying Theorems 3.10–3.11 to (6.19.2), gives

g(s)=O((log |t|)^(2/3)(log log |t|)^(1/3))

in a region Re s≥1−A(log |t|)^(−2/3)(log log |t|)^(−1/3).
Only their restriction to Re s≥1 is used here. These are supporting
analytic bounds, not a statement about the present Mellin integral;
no claim that they are the strongest possible bounds is made.

Uniformly for |u|≤V_r,
log(a_n+u)=2r+log(2π)+o(1). The two cited estimates therefore supply
M_r≤C r or M_r≤C r^(2/3)(log r)^(1/3), respectively. Neither verifies
M_r=o(sqrt(r)), or even the premise M_r≤sqrt(r) of (1). In particular
one must not substitute the second growing envelope into (1) as though
its hypothesis held. Direct use of (5) with that envelope has a
non-small exponential majorant; it gives no relative little-o estimate.

Shrinking the window does not repair that direct argument. If
M_r^* is either supplied envelope and one takes a window U_r
with M_r^* U_r=o(1) to force small variation by (4), then
sqrt(r)U_r=o(1), since M_r^*/sqrt(r)→∞. The global maximum
|K_r(v)|≤C sqrt(r), proved from its explicit modulus in L304, gives

|∫_(|v|≤U_r)K_r(v)dv|≤C sqrt(r)U_r=o(1).

The signed kernel integral over the complement is then 1+o(1), not
negligible. This addresses only this pointwise-smallness certificate;
it does not preclude a new signed estimate on that complement.

Finally the scalar inversion formula in L298, at the positive argument
2r+2λ, gives

(1/(2π))∫_ℝ exp(i(2r+2λ)v)(c+iv)^(−r−1)dv
 =exp(−c(2r+2λ))(2r+2λ)^r/Γ(r+1).

Multiplication by the remaining constant in K_r proves (2).
All these integrals are absolutely convergent: the added phase has
modulus one and r>0. The function G_(r,λ) is real under conjugation,
has logarithmic derivative λ, and has modulus 1 on Re s=σ. It thus
respects nonvanishing, the tested linewise derivative control, the
conjugate-pair form, and a stronger linewise modulus bound than needed
in (6). No actual-zeta arithmetic structure is claimed for it.

For λ=o(r), Taylor's formula gives

log[exp(−2cλ)(1+λ/r)^r]
 =−2λ/r−λ²/(2r)+O(λ³/r²).                                 (7)

At λ=b sqrt(r) this tends to −b²/2. At the second chosen λ,
the error O(log r) and 2λ/r are both o(λ²/r), proving (3).
Its negative logarithm is o(r), so the response in (3), divided by
E_r, tends to infinity. The exact model shows why the missed
sqrt(r) threshold matters for freezing, while also showing that a
failed freezing comparison alone does not refute the weaker positive
arithmetic margin required by L302. ∎

The tested derivative-magnitude route is stopped. A theorem using
additional actual-height information, or retaining the full phase in
a different comparison, is not excluded. Even a successful endpoint
comparison would still leave the other low indices and passage to
all heights unresolved.

**Mathlib.** Full statement: not checked. Supporting logarithmic
derivatives, conjugation, gamma/Fourier inversion, Gaussian estimates
and zero-free-region estimates: not checked. No library match or
absence is asserted. The names and direct links for Titchmarsh's
supporting Theorem 3.11 and Section 6.19 are preserved above; neither
is a match for the full statement. L298 supplies scalar inversion,
L303–L304 supply the Mellin representation and kernel/tail bounds,
and the relative estimate, exact model and scope of the obstruction
are proved here.
