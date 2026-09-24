# Endpoint coefficient-weighted Gram test — 2026-09-24

Gap and target: test the specified weighted sampling bound
||G_N||op V_N²=o(N) for the actual coupled endpoint samples.
It would imply D_N=o(1), hence positive endpoint margins outside
a subset of sample indices of density zero. Exceptional samples,
the remaining low Laguerre indices and global mixed positivity
would still be unresolved. Continue if the exact weighted norm
and moving-vector cost meet this threshold; stop this certificate
if a lower bound on its optimal budget already exceeds it.

Redundancy review: read GOAL.md, PROGRESS.md, the entire PROOF.md
overview and global DAG, then inspected the existing changes and
relevant proofs. L344–L345 stop separate-frequency derivative
certificates, and L346 stops an unweighted full-support sampling
operator combined with its absolute truncation bound. The proposed
weights are a distinct test because they enter the sampling Gram
matrix. L335 supplies a Liouville-twisted numerator, but no recorded
result uses its normalized value to test this weighted operator.
The September 21 admission condition is superseded by GOAL.md;
all mathematical evidence, identifiers and prior work are retained.

Unfinished reasoning saved before completing the proof: L335 gives
S_r[λ]=−ζ(2)²/(4r)+O(r^(-2)). At σ=1+1/r the twisted denominator
is (ζ(2σ)/ζ(σ))²=ζ(2)²/r²+O(r^(-3)). Absolute reciprocal-series
convergence should therefore identify the Liouville evaluation of
L332's fully grouped relative coefficients as −r/4+O(1).
Removing b_r(1,1)=O(1/r) should leave nonconstant coefficient
mass at least r/4−O(1). For any positive summable frequency
weights w, every nonempty sampling Gram matrix has diagonal
W=Σw, so ||G||op≥W. Cauchy–Schwarz gives
W||b/sqrt(w)||_2²≥(Σ|b|)². Exact vector telescoping should
make the moving-vector variation no smaller than any one of
these vector norms. This suggests a normalized certificate of
order at least N, rather than o(1), even with optimal weights.
The twisted quotient, full ratio grouping, infinite-vector
convergence and possible interval partitions still need review.
This is an obstruction to a bound, not a lower bound on D_N.
No RH candidate; zero consecutive unresolved exploration turns
preceded this test.

Completed assessment — 2026-09-24: NEGATIVE.
[L347](../lemmas/L347-endpoint-weighted-gram-mass-obstruction.md)
proves the normalized Liouville identity with every reduced-ratio
collision retained. Its nonconstant evaluation is −r/4+O(1),
so Σ_(p≠q)|b_r(p,q)|≥r/4−O(1). Every nonempty weighted sampling
Gram matrix has diagonal W=Σw. This identity and Cauchy–Schwarz
force ||G_N||op V_N²≥(N−K)² for the proposed maximum weights
and every other admissible positive weight system. The target
was o(N). Even the stronger certificate using each prefix's
optimal norm in exact vector Abel summation has normalized
budget at least cN, against D_N=o(1) or the fixed threshold 1/4.
Independent weights on arbitrary sample-interval partitions
cannot repair the comparison. No frequency truncation or sample
spacing estimate is needed for this new obstruction.

WHY IT FAILS: the [canonical proof](../lemmas/L347-endpoint-weighted-gram-mass-obstruction.md)
shows that normalization by the small Liouville-twisted zeta square
forces large total mass in the actual grouped coefficients.
The diagonal of the weighted Gram matrix times the squared
coefficient-vector norm always dominates that mass squared.
Positive weights can redistribute this cost but cannot remove it,
and exact vector telescoping preserves the obstruction. Thus the
operator/vector norm separation already fails before estimating
any Gram off-diagonal entry. The Liouville character is used only
to measure coefficient mass; no realization at a_n, lower bound
on the actual sampled mean, or negative Laguerre coefficient is
asserted. This stops the stated norm certificate, not a signed
estimate using the actual coefficients and phases together.

The two joint sampling tests now have independent obstructions.
The following direction changes the sampled function by an
explicit signed subtraction: retain L332's polynomial
P(log(jk))/r at σ=1+1/r as an exact divisor expression. Its
logarithmic-derivative formula and normalized Liouville remainder
provide a concrete test of whether this removes the order-r
obstruction. This is not another weight optimization. Even if
the obstruction disappears, both the explicit term and the
remainder would need control at the prescribed a_n; L330's
failure of magnitude-only derivative bounds remains relevant.
The sole current action is in PROGRESS.md.

The endpoint margin, global low-index gap and all established
sign/exclusion ranges are unchanged. STATUS remains IN_PROGRESS;
no RH candidate and zero consecutive unresolved exploration
turns. Analytic verification covers absolute convergence of
the twisted quotient, the d² cancellation during ratio grouping,
the normalized asymptotic, infinite-vector domains, the optimal
sampling norm, and every prefix and partition in vector Abel
summation. No numerical experiment or library lookup is needed
for this inequality. Full Mathlib coverage is not checked;
the recorded supporting theorem names and direct links are
preserved in L347. All prior unfinished work remains intact.
