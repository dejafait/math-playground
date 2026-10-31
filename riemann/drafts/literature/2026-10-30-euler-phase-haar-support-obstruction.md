# Real Euler-phase multiplier: proposed Fourier-support diagnostic

TARGET: Determine whether liminf_(T->infinity) inf_(P in V_T) ||h_T-P||_(L2(mu_T))>0, where y=T^(1/1000), mu_T is probability Haar measure on the prime torus (S^1)^{p<=y}, h_T(z)=Re product_(p<=y)(1-p^(-1/2)z_p)/(1-p^(-1/2)conjugate(z_p)), and V_T is the complex span of product_(p<=y)z_p^{v_p(a)-v_p(b)} for y-smooth integers a,b<=T^(1/100).
CHECKED: 2026-10-30
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact phase-product search and source-scope comparison in 2026-10-30-euler-product-phase-dual-coverage.md; additionally searched Euler product phase quotient Fourier and Blaschke Haar Dirichlet polynomial approximation. No matching quantitative support statement was located. This is not a novelty claim; Haar Fourier projection and finite tensor products are standard tools.
SOURCE_EVIDENCE: Tao, 245C Notes 2 (6 April 2009), Exercise 15, Lemma 17, Theorem 21, finite-torus proof case and Corollary 22; Tao, Mertens' theorems (11 December 2013), Theorem 1/(3), with its strong o(1) error and Section 1 proof. Primary URLs and exact scope are below. No actual-height equidistribution input is invoked.
COMPARISON: Compact-group Parseval, tensor factorization and classical Mertens product asymptotics cover the tools for a finite-prime spectral computation. They do not determine the real quotient's coefficients outside the specified rational-frequency rectangle. That explicit specialization, including opposite-character cancellation, is the mathematical work still to do.
GAP: Determine the displayed positive liminf or a contrary asymptotic for the exact real multiplier, retaining all primes and arbitrary approximants in V_T. No coefficient law, lower bound or finite-height implication is established in this assessment.
REASON: Source-ready nomination of one independently testable expansion diagnostic after parking the full signed correlation for missing finite-height coverage. A separate approval next turn is required before calculation; no new mathematical result is derived here.
SCOPE: Exactly the stated Haar norm and exponents 1/1000,1/100. T tends to infinity through positive real values. An integer is y-smooth if every prime divisor is <=y, including the integer 1. v_p is its nonnegative integer prime valuation. This is a product-torus problem only; no RH, actual prime-phase distribution, zeta replacement, discarded exceptional mass or weighted transfer is assumed.

## Relevance and bounded test

The main gap is actual-Xi all-degree mixed positivity. The immediate
stopped target is the full-scale correlation of L477's exact residual
with the real Euler-product phase multiplier. This diagnostic asks
whether that multiplier has a nonvanishing spectral tail outside one
specified short rational-frequency rectangle on its full prime torus.
A positive result could obstruct a global uniformly accurate truncation
of that form. It would not obstruct all finite-height or weighted
approximations, evaluate C_B, or imply any statement about RH.

This target is independent of the missing actual-height replacement:
it defines its own Haar norm and asks no sampling theorem. The
numerical exponent 1/100 is a fixed test rectangle, not a claim that
every polynomial of this length has an adequate signed-correlation
formula. L477 and L481 supply motivation and downstream limitations;
they are not mathematical premises for this standalone calculation.

The bounded attempt should compute the exact one-coordinate Fourier
coefficients, justify tensoring over the finite prime set, and control
the mass omitted by this rectangle, including the real-part
symmetrization. A calculation for the complex quotient alone cannot
settle the real target. Every infinite one-coordinate expansion needs
its convergence justification; no fixed-prime limit can replace the
growing-prime calculation.

Continue only if a rigorous positive liminf or a contrary approximation
asymptotic is obtained. A small toy example, a formal coefficient
expansion, or a nonzero tail at each fixed T is insufficient. If neither
threshold is established in the bounded attempt, preserve the reasoning
and park this implementation unless a materially refined test results.
Either outcome concerns this global truncation diagnostic only. The
full |R_T|-weighted error, both signed residual phases, complete
correlation, negative mass and all-height signs remain unresolved.

## Primary theorem hypotheses and inspected cases

**T. Tao, _245C, Notes 2: The Fourier transform_, 6 April 2009,
Section 2, Lemma 17, Theorem 21 and Corollary 22.**
[Primary lecture notes](https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/).
For a compact abelian group with probability Haar measure, characters
are an orthonormal basis of complex L2 and Parseval identifies its
norm with squared Fourier coefficients. Read the finite-torus proof
using Stone--Weierstrass, Lemma 17's translation proof and Exercise 15's
tensor-product statement. For each T the torus here is finite
dimensional; the theorem requires no fixed dimension, and no limit
over T is part of the imported statement. Standard Hilbert-space
orthogonal projection applies to the finite span V_T. These known
results are to be cited rather than reproved. Only the exact rational
factor specialization is proposed for computation.

**T. Tao, _Mertens' theorems_, 11 December 2013, Theorem 1/(3).**
[Primary exposition and proof](https://terrytao.wordpress.com/2013/12/11/mertens-theorems/).
The classical unconditional named theorem gives
sum_(p<=x) log(1-1/p)=-log log x-gamma+o(1) as x->infinity.
The statement and Section 1 proof were inspected, including the
fixed-epsilon cutoff passage and final removal of epsilon. Retain
the strong o(1) form; the displayed harmonic-prime estimate with
O(1) error alone is not a limiting formula for a fixed power block.
No RH or new prime-distribution theorem is needed. Any use for the
particular coefficient products still needs its applicability argument.

The current source-scope review distinguishes this norm problem from
the existing finite-height Hardy-space mismatch, assigned-prime
completion stop, saturation polynomial stops and cubic weighted-mass
failure. None of those results evaluates this exact Fourier rectangle.
No completed duplicate was found in that narrow comparison; no claim
of originality follows. Mathlib matching is not checked, including the
specific Fourier-support asymptotic; absence is not asserted.

## Routing qualification

This is an ordinary finite-factor specialization with a real-part
cancellation issue. Nominate calculation / standard / high after the
required separate source-scope approval. No creative central mechanism
is justified while the full actual-height weighted replacement remains
uncovered. This nomination neither spends nor renews the carried
mathematical exploration budget. No calculation, lemma or script has
been produced for it in this literature-only turn.
