# Direct frozen fourth-moment test1448 — work saved

Gate: unchanged EXPLORE assessment1447, exact TARGET in its header.
Main gap: L030--L032/C032a actual-Xi all-degree positivity. Test only
the original fixed-Z prime-times-M^2 fourth moment, not a new source
transplant or the stopped whole Gallagher energy. Existing work preserved.

Attempt in progress: write M^4=sum r_s s^(-1/2-it), with four
unshifted individual tapers. Keep repeated primes in P_Z^2. For large d,
every witness prime exceeds R=L^4, so k=vs uniquely recovers the prime
product v (including squares) and s. Expected full coefficient norm
is O(ell^4/q^2)=O(q^2), using the already inspected absolute-alpha
convolution and PNT bounds. This is only a diagonal estimate.

Proposed finite high-height localization: K=104 normalized box
convolutions with total support radius B/4, convolved with the indicator
of [X-B/4,sqrt(2)X+B/4]. The resulting weight is one on J and supported
in [X-B/2,sqrt(2)X+B/2], a positive-height interval. Its transform decays
as C_K B(1+B|xi|)^(-K). Frequencies separated by at least X^(-99/100)
should then cost O(X^(.964)q^2), using support N<=XL^4/25 and Cauchy.
Check every exponent, support and endpoint before using this reduction.

Equal-s blocks should be bounded by G.16 applied to P_Z^2, whose grouped
prime-product frequencies have integer support <=X/25. The remaining
near unequal-s correlation has to retain its signs. An unevaluated
correlation or a failed absolute upper bound is not success or refutation.
No conclusion on that remaining form has yet been obtained.

## Completed attempt

Full hypotheses, proof, source specialization and qualifications are now
canonical in C020l. The exponent is 241/250=.964, so the far term divided
by Bq^2 is O(X^(-9/250)). Repeated prime squares are paid separately
before using the distinct-pair coefficients. Equal-s blocks are paid
by G.16; the unshifted r_s have been bounded directly, without borrowing
shifted c_s correlations. The compact weight has only positive-height
support and retains its translated Fourier phase.

The near unequal-s signed form C020l (5) remains unbounded. Its relevant
integer width is O(L^4 X^(1/100)); this localization is not a counting or
cancellation theorem. No asymptotic lower bound refuting the target,
nor a paid upper bound for this form, has been obtained. Record
EXPLORATION/REPRODUCTION, with one mathematical exploration attempt.
Do not revive the exhausted absolute budgets. Audit the new reduction
before using it; a new REVIEW_REQUIRED nomination preserves that handoff.
