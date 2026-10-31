# Complete-residual moment test with L479: working checkpoint

The invocation-start target and unchanged ready EXPLORE assessment are
`literature/2026-10-29-l477-residual-moment-interpolation-coverage.md`.
Use audited L479, the exact L477 residual and L316's actual phase.
Preserve all existing notebook changes and L478's failed termwise test.

Main gap: actual-Xi all-degree mixed positivity. Intermediate test:
the complete moment quotient must reach c T(log T)^3 to reject the
fixed square as a little-o approximation via L477 (4). Independent
negative-mass saving and all-height signs remain unresolved.

Unfinished reasoning, not yet a certificate: in the charge-two integral
put D=sum log(M/i) over its four indices. Its phase derivative is
at least D+O(T^-2); a nonzero coefficient forces D>=1/M. First
derivative integration with endpoints retained should cost O(1/D).
The coefficient numerator is at most D^4, and dyadic sums suggest
total cost O(M^2)=O(T). The two nonchirped squares are nonnegative;
L479 would then yield I_2>=c T(log T)^8.

For an upper bound, group exact equal ratio and product frequencies.
Distinct logs have separation >=1/M^2. A triangular time majorant
formed by convolving two intervals has a squared-sinc transform;
direct finite integration may remove the logarithmic loss of absolute
first-denominator sums. Check this explicitly before use. This is a
special-purpose elementary substitute for the unread Montgomery--Vaughan
displays, not an imported stronger theorem. Combine only proved full
I_2 bounds with |R|<=C M for a complete I_4 upper bound; compare the
certified quotient to T(log T)^3, without bounding the true quotient
above merely because this certificate is weak.

Continue only with a sufficient quotient or a precise refined remainder.
Any new fourth-moment mechanism beyond the saved finite-expansion scope
needs a separate source assessment. No external source was retrieved.

Completed: full proofs and qualifications are canonical in
`../lemmas/L480-complete-residual-second-moment-and-fourth-moment-gap.md`.
The complete I_2 is comparable to T(log T)^8. The sufficient I_4 upper
scale is T(log T)^18; the available supremum certificate only gives
T^2(log T)^8. This closes a local input, not the L1 threshold. The
new result is pending its first critical audit under the same coverage.
