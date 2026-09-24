# Lemma 337: a positive completion of the endpoint small-prime phases

**Hypotheses.** Let r tend to infinity through real values. Use the
endpoint weights and twisted sums of L335:

W_r(j,k)=(jk)^(−1/2)(1−log(jk)/(2r))_+^r,
J_r={j≥1: j<exp(3r/4)},
S_r[ω]=Σ_(j,k≥1)W_r(j,k)ω(j)conjugate(ω(k)),
T_r[ω]=Σ_(j,k∈J_r)W_r(j,k)ω(j)conjugate(ω(k)).

Define the completely multiplicative real function ω_r by

ω_r(p)=−1 for primes p≤r, and ω_r(p)=+1 for primes p>r.

Put

G_r(s)=∏_(p≤r)(1−p^(−s))/(1+p^(−s)),
g_r=G_r(1)=∏_(p≤r)(p−1)/(p+1)>0,
E_r=(1+r)²exp(−r/256).

**Conclusion.** Both full and interior sums satisfy

S_r[ω_r]=4r g_r²[1+O((log r)³/sqrt(r))],
T_r[ω_r]=4r g_r²[1+O((log r)³/sqrt(r))].               (1)

In particular, writing γ for Euler's constant,

S_r[ω_r] ∼ T_r[ω_r]
           ∼ 4exp(−4γ)ζ(2)² r/(log r)^4 >0.          (2)

For all sufficiently large r both sums are at least 2/r³, hence
their positive margins dominate E_r. No numerical starting r is
asserted. Formula (1) and this weaker polynomial lower bound do not
require Mertens' theorem; that standard input is used only in (2).

The completion ω_r and the full Liouville assignment of L335 agree
on every prime at most r, but the latter gives both sums
−ζ(2)²/(4r)+O(r^(−2)). Thus even exact agreement with the Liouville
phases on these primes cannot force a negative value uniformly over
the remaining prime phases. In particular a phase neighborhood
constraining only those primes is not such a certificate.

These statements concern test assignments, not the actual assignment
ω(m)=m^(−ia_n) at a_n=sqrt(4π²exp(4r)−25), r=2n. They do not
locate a negative value at those coupled pairs, assert a negative
Laguerre coefficient, or extend a sign or zero-exclusion range.

**Proof.** For Re s>1 absolute convergence, complete
multiplicativity and geometric-series multiplication give

F_r(s):=Σ_(m≥1)ω_r(m)m^(−s)=ζ(s)G_r(s).              (3)

Indeed the Euler factor for a prime at most r is (1+p^(−s))^(−1),
and for a larger prime it is (1−p^(−s))^(−1). All products and
Dirichlet series here converge absolutely. Also
|F_r(σ+iv)|≤ζ(σ) whenever σ>1.

Set c=1/2+1/r, σ=1+1/r, w=1/r+iv, and use L304's kernel

K_r(v)=Γ(r+1)(2r)^(−r)exp(2r(c+iv))
                           ·(c+iv)^(−r−1)/(2π).

L298's scalar inversion, summed by exactly the absolutely convergent
interchange in L303, gives

S_r[ω_r]=∫_ℝ K_r(v)F_r(1+w)²dv.                     (4)

The integral of the absolute majorant is finite: it is bounded by
ζ(σ)² times a constant depending on r times
∫(c²+v²)^(−(r+1)/2)dv. The square in (4) is an analytic square,
not a modulus square, because ω_r is real and both Dirichlet
factors have the same coefficients and the same argument. No
conditionally convergent series at Re s=1 is used.

We control the varying finite product before expanding (4). For
Re s≥1 its factors have no zero or pole, and logarithmic
differentiation gives

G_r'(s)/G_r(s)=2Σ_(p≤r)(log p)p^(−s)/(1−p^(−2s)).

Since |1−p^(−2s)|≥1−p^(−2)≥3/4, for r≥2 we have

|G_r'(s)/G_r(s)|
 ≤(8/3)Σ_(p≤r)(log p)/p
 ≤(8/3)(log r)Σ_(2≤m≤r)1/m
 ≤C(log r)².                                         (5)

The constant is absolute; harmonic integral comparison proves the
last inequality. Integrating an analytic logarithm along the segment
1+tw, 0≤t≤1, stays in Re s≥1. Put V=log(r)/sqrt(r). Uniformly for
w=1/r+iv, |v|≤V, equation (5) gives

G_r(1+w)/g_r=1+O(|w|(log r)²),                        (6)

because |w|(log r)²=O((log r)³/sqrt(r)) tends to zero and
|exp(z)−1|≤|z|exp(|z|). This estimate is uniform across all changes
in the finite set of primes as r increases.

As checked in L335 using the simple pole and integral comparison,
H(w)=wζ(1+w) is analytic in a fixed disk about zero, with H(0)=1.
Consequently H(w)=1+O(|w|) there. Applying this to (3) and (6)
proves on the whole window |v|≤V that

|F_r(1+w)²−g_r²/w²|
                     ≤C g_r²(log r)²/|w|.            (7)

In particular we have kept the pole; replacing F_r by a finite
value at the center would not give this estimate.

L304 proves, for r large,

|K_r(v)|≤C sqrt(r) exp(−rv²/4) for |v|≤c,
∫_(|v|>V)|K_r(v)|dv=O(exp(−(log r)²/8)).              (8)

Since |w|=sqrt(r^(−2)+v²), an elementary change of variable gives

∫_(|v|≤V)|K_r(v)|/|w| dv
 ≤2C sqrt(r)∫_0^V dv/sqrt(r^(−2)+v²)
 =O(sqrt(r)log r).                                   (9)

For example split the last integral at 1/r; its two contributions
are at most 1 and log(rV). Equations (7)–(9) bound the integrated
local error by O(g_r² sqrt(r)(log r)³).

We also need a relative, rather than just absolute, tail estimate.
For N=floor(r), all factors (m−1)/(m+1), m≥2, belong to (0,1).
Multiplying over every integer only decreases the prime product:

1≥g_r≥∏_(m=2)^N(m−1)/(m+1)
        =2/[N(N+1)]≥2/[r(r+1)].                      (10)

On the entire vertical line, |F_r(σ+iv)|≤ζ(σ)≤r+1 and
|w|^(−2)≤r². Thus (8) bounds the tails of both terms in (7),
without asserting (7) outside its window, by

O(r² exp(−(log r)²/8)).                               (11)

By (10) this is o(g_r² sqrt(r)); the exponential of minus a
positive multiple of (log r)² beats every fixed power of r.
Combining (4), (7)–(11) yields

S_r[ω_r]=g_r² I_r+O(g_r² sqrt(r)(log r)³),
I_r=∫_ℝ K_r(v)/(1/r+iv)²dv.                          (12)

It remains to evaluate the pole-square contribution with its sign.
For z=c+iv the elementary Laplace identity is

(z−1/2)^(−2)=∫_0^∞ t exp(−(z−1/2)t)dt.

The double integral against |K_r(v)| is finite, since
∫|K_r|=O(1) and ∫_0^∞ t exp(−t/r)dt=r². Fubini and L298's
scalar inversion at 2r−t therefore give exactly

I_r=∫_0^(2r) t Q_r(t)dt,
Q_r(t)=exp(t/2)(1−t/(2r))^r.                          (13)

Indeed the inner integral is
∫K_r(v)exp(−(z−1/2)t)dv=Q_r(t) for 0≤t<2r, and zero
for t≥2r. This is a positive continuous integral; it is not an
assumed sign of the original twisted sum.

The logarithm inequality log(1−x)≤−x−x²/2 gives
0≤Q_r(t)≤exp(−t²/(8r)). For 0≤t≤r the convergent logarithm
series gives the more precise bound

0≤−log Q_r(t)−t²/(8r)
  =rΣ_(k≥3)(t/(2r))^k/k
  ≤t³/(12r²).                                       (14)

It follows from 1−exp(−u)≤u that replacing Q_r by the Gaussian
on this interval costs at most

(12r²)^(−1)∫_0^∞ t⁴ exp(−t²/(8r))dt=O(sqrt(r)).

The Gaussian integral over t>r, with the additional factor t, is
4r exp(−r/8). Since ∫_0^∞ t exp(−t²/(8r))dt=4r, (13)–(14)
prove

I_r=4r+O(sqrt(r)).                                   (15)

Together with (12) this is the first asymptotic in (1).

L303's omitted-index estimate uses only the absolute weights and
therefore applies to this unit assignment as well:

|T_r[ω_r]−S_r[ω_r]|=O(r exp(−9r/128)).                (16)

By (10) this is o(g_r² sqrt(r)), proving the second part of (1).
For sufficiently large r, (1) and (10) give, for each sum,

value ≥2r g_r²≥8/[r(r+1)²]≥2/r³.

Since r³E_r→0, this proves the asserted margin comparison without
any prime-distribution theorem.

To express the leading term only in r, use the standard named
Mertens third theorem recorded in foundations. Algebra gives

g_r=[∏_(p≤r)(1−1/p)]² · ∏_(p≤r)(1−1/p²)^(−1)
    ∼ exp(−2γ)ζ(2)/(log r)².                         (17)

The second product tends to ζ(2) by the absolutely convergent Euler
product at 2. The first uses only Mertens' unconditional main term;
no RH-dependent error estimate is involved. Substituting (17) into
(1) proves (2).

Finally L335 evaluates the full Liouville completion as negative by
order 1/r. It shares all the specified small-prime phases with ω_r,
while (1) is eventually positive. This directly disproves a uniform
negative implication from those small-prime constraints, including
one with an error allowance of order E_r. It does not estimate the
remaining phases of m^(−ia_n) or transfer either test assignment to
the prescribed growing heights. The actual endpoint arithmetic
margin and the low-index Laguerre signs remain unproved. ∎

**Mathlib.** Full statement: not checked. Coverage of the finite
Euler-product asymptotic, uniform pole expansion, Laplace identity,
and Mertens third theorem is not checked. The full argument above
uses L298's proved scalar inversion, L303's absolute cutoff bound,
L304's kernel estimates, and L335's local pole analysis and negative
comparison; none is asserted to match a library theorem.

The supporting nonvanishing theorem inherited through L335 was
recorded as present in L001:
[`riemannZeta_ne_zero_of_one_lt_re`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#riemannZeta_ne_zero_of_one_lt_re).
It was not rechecked and is supporting coverage for the earlier
Liouville argument, not a match for this positive-completion result.
Mertens' standard named theorem is stated in Ross G. Pinsky,
*Probabilistic Proofs of Some Generalized Mertens' Formulas Via
Generalized Dickman Distributions* (2018),
[equation (1.1), p. 2](https://arxiv.org/pdf/1809.04888#page=2),
which was checked as a mathematical reference, not a Mathlib source.
No full match or absence from checked library sources is claimed.
