# Bessel background and quartet compatibility — 2026-09-27

Working note for the exact target in the saved
[SPECIALIZE assessment](literature/2026-09-27-count-and-positive-kernel-model.md).
The target retains every conclusion of L354, including its literal
consecutive-real-zero gap bound. No condition may be weakened to
complete this test.

The main unresolved claim remains actual-theta positivity at every
required low Laguerre level. This diagnostic asks whether adding a
smooth strictly positive Fourier kernel to the coarse count and gap
data eliminates L354's negative first-sign mechanism. A model would
stop that generic sufficiency argument; failure of this ansatz alone
would not settle the generic implication or any actual-zeta sign.

The assessed ansatz is a normalized imaginary-order Bessel transform
times the single-quartet polynomial in L354. The imported counting
theorem suggests H(z)=K_(iz/2)(2π)/K_0(2π), whose Fourier density is
proportional to exp(−2π cosh(2u)). The calibration, exact gaps and
kernel positivity still require checks. The polynomial multiplier
corresponds to a fourth-order differential operator on this density;
its whole-line sign must be proved, not sampled.

Continue only if the same parameters meet the count, order, small-zero,
gap, kernel and normalized first-sign requirements. A rigorous failure
of any literal condition stops this implementation. This is the second
turn after one unresolved source-review turn; no full model, negative
result or extension of actual-zeta positivity is yet asserted.

## Work saved before the finite certificate

Write q=2π, v=q cosh(2u), and k(u)=exp(−v). Direct differentiation
gives k''/k=4(v²−v−q²) and
k''''/k=16[v⁴−6v³+(7−2q²)v²+(6q²−1)v+q⁴−4q²].
The modified density is proportional to
k''''+2(A²−b²)k''+(A²+b²)²k. Expanding in y=v−q≥0
gives a lower bound for k''''/k from a positive quadratic minus a
linear term. This should give strict positivity uniformly for A>40,
0<b<1/4, independently of the displacement eventually chosen for
the negative Laguerre sign.

For exact gaps, set χ=π² and
S(ν)=Σ_(j≥0) χ^j/[j!(1+iν)_j]. The Bessel connection and series
formulas in Paris (1.2), (2.1) give its real sign from sin θ(ν),
where θ=Im log Γ(1+iν)−ν log π−arg S(ν). For ν≥100,
|S−1|≤exp(χ/ν)−1 and |S'|≤χ exp(χ/ν)/ν².
The standard complex digamma remainder gives a usable lower bound
θ'(ν)≥log(ν/π)−14/ν². Its integral on a proposed gap is the
analytic tail test. The finite test will use sign-changing brackets,
not assume that numerical root lists contain every zero.

Additional supporting formulas were read from DLMF 5.11.1–5.11.2
and §5.11(ii), https://dlmf.nist.gov/5.11, for explicit remainder
bounds within this already assessed target. Lagarias's Theorems 2.1
and 4.1 and Paris's (1.2)/(2.1) were reopened to check normalizations.
This does not change the saved target or its prior assessment.

## Completion

The full construction is proved in
[L355](../lemmas/L355-positive-kernel-count-and-gap-first-sign-countermodel.md).
The shifted fourth-derivative polynomial has linear coefficient
−12q²+14q−1; completing its quadratic lower bound gives
k''''/k>−33000. Together with k''/k>−28 this makes the modified
kernel strictly positive for every A>40 and 0<b<1/4.

The gap proof avoids an ineffective large-index cutoff. The phase
estimate covers all ν≥100, and the saved 80 sign brackets cover
every lower gap. Each bracket is checked by outward arithmetic
with explicit series and gamma remainders. Neither uniqueness
within a bracket nor completeness of a numerical zero list is used.
The count, simplicity, order and small-zero exclusion are supplied
by the cited spectral theorem and their explicit specialization.

The parameters used in L354's negative-sign construction fall
within the uniform kernel-positive range. Thus every exact target
condition is met, under L037's contracts for the finite gap check.
This is an informative negative result for the strengthened generic
sufficiency claim, not a new actual-zeta sign or an RH candidate.
The next target requires a separate literature turn.
