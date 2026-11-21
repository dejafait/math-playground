# Arithmetic multiplier projection — working step 260

The gate-approved target and fixed objects are those in
drafts/literature/2026-11-04-dirichlet-multiplier-bump-projection-scope.md,
COVERED_TARGET. Main gap: actual-Xi all-degree mixed positivity.
The test is uniform vanishing projection at N=floor(T^(1/10)); a
rigorous nonvanishing subsequence would instead leave this dictionary
worth examining. Neither outcome pays signed transfer or local margins.

Saved before completing the proof: put b_n=c_n/sqrt(n),
B_d=sum_(k<=N/d) b_(dk), C_d=sum_(k<=N/d) b_(dk) log k.
The full BCR logarithmic form appears to equal
sum_d phi(d)[(A+2 sum_(p|d) log p/(p-1))|B_d|^2
-2 Re(C_d conjugate(B_d))], A=log(t/(2pi))+2 gamma.
The divisor identity for log k gives C_d=sum_r Lambda(r)B_(dr).
A finite weighted Schur estimate should give ||C||_phi<=2 log N
||B||_phi: use h_d=1/sqrt(phi(d)), row sum <=4 log N,
column sum <=log N, and
sum_(r<=N) Lambda(r)/r <=2 log N via log(N!).
Möbius inversion and Cauchy--Schwarz suggest
||c||_2^2<=N^2 sum phi(d)|B_d|^2, which is ample here.

Still unchecked at this checkpoint: exact divisor differentiation and
complex conjugations, uniform smooth partition for the BCR theorem,
normalization B=max sqrt(n)|c_n| and its quadratic remainder, and
the final ratio. L637's imported undifferentiated Riemann--Siegel
formula already gives |Z|<=C T^(1/4) on [T,3T]; no new convexity
source is necessary. Expected numerator bound is
C N T^(1/2)||c||_2^2/log T, against denominator
c T log T ||c||_2^2/N^2. These are provisional calculations,
not a verified projection theorem.

Existing L639 is a jet-space comparison, not an input to this argument.
The prior source assessment records the duplicate/failure comparison;
this step does not reopen the stopped jet or TV-envelope mechanisms.

## Completed attempt

The provisional argument above is completed in canonical L737,
lemmas/L737-arithmetic-multiplier-bump-projection.md. The exact logarithmic
identity and finite weighted Schur argument give F_A>=(A-4 log N)Q;
Möbius inversion gives ||c||_2^2<=N^2 Q. Fixed source length exponent
1/8, with zero padding, supplies the uniform charged remainder
O_epsilon(N T^(57/160+epsilon)||c||_2^2). Relative to the required
T log T ||c||_2^2/N^2 scale this is
O_epsilon(T^(-11/32+epsilon)/log T). The resulting squared projection
bound is O(T^(-1/5)/(log T)^2), uniformly in X.

Outcome: NEGATIVE for this dictionary's realization, conditional only
on the named standard imports as stated; separate conceptual audit
pending. No computational evidence is substituted for the finite
identities or analytic estimates. The ready target and source scope
are unchanged for that audit. No new external theorem was needed.
