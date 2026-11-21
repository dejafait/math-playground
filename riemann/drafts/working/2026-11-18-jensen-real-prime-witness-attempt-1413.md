# Fixed real source-prime witness — attempt1413

Completed partial attempt, 18 November 2026. One mathematical attempt under unchanged
EXPLORE assessment1409; no source refresh or witness optimization.
Main gap: L030–L032/C032a actual-Xi all-degree positivity. The approved
target remains the full quotient (N1). A lower bound cBq^2 would stop
the proposed O(B) pair moment; an O(B) quotient would stop this witness.
Neither follows from a selected resonant slice. Independent density,
ordered-interval, root-map and bulk-separation gaps remain.

Inputs read: C019p's coefficient algebra, C019u's moving-coefficient
setup, C019x's cutoffs and harmonic mass, and all of C019y. Separate
stops1407/1408 and attempt1412 are preserved. No actual-P transfer
contract is being used without its original qualifications.

Checkpoint before further reasoning: for every witness pair v=p1*p2
and s<=R, p_j>R and v>N_* force the two large primes into distinct
sources of G_(vs). Moreover N_*<sqrt(X)/2 eventually, whereas
p_j>=sqrt(X)/10. Thus each source multiplier is in {1,2,3,4}.
This should group the complete zero-frequency numerator, including
C019y (16), through the correlations
K_j=sum_(r<=R/j) c_r conjugate(c_(jr))/(jr), with
j in {1,2,3,4,6,8,9,12,16}. Entry indicators must remain exact.

Unfinished: write and verify the full grouping, establish only bounds
that retain the finite taper, and identify whether any sign or norm
threshold has actually been paid. The other terms in C019y (5),
including both unequal-index sums and actual-P residual, remain open.

## Second checkpoint: full-resonance mechanism, not yet a conclusion

The four original factors permit removal of the fixed primes 2 and 3
with a controlled taper error. With omega extended by its positive
part, each insertion changes a taper by at most log(2^a3^b)/ell.
The untapered local four-factor polynomial is exactly
(1-z)(1-p^(-ih)z), of degree two. An intended weighted coefficient
norm estimate is ||c-tilde(c)||_(l2(1/n))=O(ell), while
||c||+||tilde(c)||=O(ell^2). This would give all nine required
correlations K_j=rho(j)K_1+O(ell^3), where rho is multiplicative,
rho(2)=-6/13, rho(4)=1/13, rho(3)=-4/11, rho(9)=1/22,
and rho(8)=rho(16)=0. The comparison uses finite coefficients,
not a reciprocal at the critical line. Boundary support must be
included by extending the coefficient arrays by zero.

If this estimate holds, PNT at fixed proportional endpoints reduces
the full resonant numerator to a scalar integral. Put
A=log(2), u_a(x)=max(0,log(min(2,10*sqrt(x/(2*pi))/a))).
Then f(x)=sum_(1<=a,b<=4) rho(ab)u_a(x)u_b(x), and the proposed
formula is N0=(16*K1*X/q^2)*(integral_1^sqrt(2) f(x) dx+o(1)).
This integral appears negative, so the dyadic slice cancellation
would not cancel the whole resonant numerator. This is a working
prediction only until every norm, floor and scalar-sign bound is
verified. The full quotient remains dependent on the other channels.

## Completion and remaining test

The predicted full-resonance reduction and sign are proved in
[C019z](../../lemmas/C019z-real-prime-witness-full-resonant-sign.md),
with all small-prime powers and support-boundary errors included.
The complete resonant numerator is negative of order Bq^2, and the
resonant denominator is positive of order Bq^2. This pays the former
first-unpaid expression C019y (16), in aggregate with its selected
slice. It does not pay the other signed terms in C019y (5).

The scalar script uses exact rational arithmetic, including series
remainders and outward rounding; all eight required comparisons pass.
Its first run failed only when serializing very large rational integers.
Outward rational rounding on the stated 10^(-12) grid fixed this
serialization failure while preserving enclosures. The final complete
load-bearing values were inspected, and the certificate establishes
I<-19/10000 against the required I<-1/1000. This is a scalar-integral
certificate, not a numerical check of the full quotient or RH.

Continuation: retain exactly the original fixed witness and use C019z
(3) together with C019y (5). The signed unequal-index term O(G,J),
the three other numerator channels, O(J,J), the denominator's A^2
channel and E_P remain unpaid. A full cBq^2 lower bound or O(B)
upper bound is still the decision test. C019t's transfer remains
qualified and unaudited; C019y/z also need later independent review.
The new complete resonant evaluation supplies a materially refined
continuation on the same ready target, without free optimization or
new source assumptions. No EXPLORATION-budget reset is claimed.
