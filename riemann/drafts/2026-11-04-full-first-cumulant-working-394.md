# Fixed full-first cumulant comparison — working step394

Approved target: test S_(3,5)(B;u)>0 and
|S_(3,5)(K;u)-S_(3,5)(B;u)|<S_(3,5)(B;u)/2 for every u>=0.
Coverage: the unchanged full-first-theta-summand assessment's COVERED_TARGET.
This is reproduction/development of the source's comparison program.

Read L019 and L021; the exact first summand and decay are available.
The source comparison and November4 direct-transfer/compensation stops
are retained. No source sign theorem is assumed. L018 concerns only
downstream Xi normalization; it is not needed for the fixed integral test.

Main gap: actual-Xi all-degree positivity. The fixed relative comparison
could support cumulant reverse regularity; higher orders, effective
smoothing thresholds and exceptional coefficient transfer remain open.
Continue only with a signed base lower bound and relative error <1/2
including zero and infinity. Samples alone are inconclusive. An
unresolved cancellation estimate stops this attempt, without a global ban.

Initial reasoning: derivatives reduce the determinant to the five tails
C_1,...,C_5. A signed cubic combination must be retained. At large u
the matrix approaches rank one after exponential normalization, so
ordinary relative entry errors cannot be mistaken for determinant errors.
Plan: a bounded endpoint/scale diagnostic, then a certified obstruction
or signed estimate if feasible. Save all unfinished calculations here.

## Analytic tail plan after the diagnostic

With x=pi exp(2u), epsilon=1/x, A=4x(2x-3)exp(u/2-x), write
C_(p+1)(B;u)=A(2x)^(-p-1)d_p(x), p=0,...,4. The substitution
q=x(exp(2(v-u))-1) gives

 d_p=integral_0^infinity exp(-q) L^p H dq/p!,
 L=log(1+epsilon q)/epsilon,
 H=(1+epsilon q)^(1/4)(1+epsilon q/(1-3epsilon/2)).

The signed normalized determinant is -det[d_(i+j)]_(i,j=0)^2;
the positive common factor is A^3/(2x)^9. Preliminary expansion:

 d_p=1+a_p epsilon+b_p epsilon^2+O(epsilon^3),
 a_p=(p+1)(5/4-p/2),
 b_p=(p+1)(p+2)(12p^2-40p+15)/96+3(p+1)/2.

Finite differences satisfy Delta^2 a=-1, Delta^3 a=Delta^4 a=0,
Delta^4 b=3. Unit-determinant row/column differences therefore give
the leading signed determinant 2epsilon^3. This is being checked
with explicit derivative remainder bounds, not assumed from the samples.
For n>=2 the same substitution with q=n^2x(exp(2(v-u))-1) gives
an entrywise normalized tail <=330 exp(-3x), x>=4, uniformly p<=4.
The resulting signed cubic error is <=26664660 exp(-3x) if every
full/base normalized entry is <=67. This saved plan was completed in
L767, with full proof and exact rational certificate there; its cutoff
is x>=131072 and its relative bound is <3e-27. The finite-difference
variables remove the leading rank-one cancellation analytically.

## Completed scope and unfinished reasoning

The full fixed test remains incomplete. The diagnostic found sampled
positive base values and a sampled relative error about 0.00042665 at
u=0, but has no rigorous quadrature, roundoff, omitted-summand or
continuum control. It must not justify any compact sign claim.
The tail certificate checks polynomial majorants, exact integrals of
their monomials and rational intervals; its analytic hypotheses are
proved in L767. Earlier dyadic cutoffs failed that enclosure, not the
mathematical sign test. There is no full-domain result or RH candidate.

The unchanged assessment still covers the exact next fixed test. A
further bounded attempt has new input: the effective tail and the
scaled finite-difference determinant. The unresolved job is a compact
signed comparison for pi<=x<131072, including x=pi; L767 also awaits
independent audit. Any numerical enclosure needs its own analytic
remainder and all-summand control. No new creative mechanism or
all-order inference emerged from this reproduction/development step.
