# Quartic cutoff symmetrization — 2026-09-13

Draft checkpoint; claims below await final algebra audit. Preserve L157.
Write J=Σ A_n' exp(i(t−π/2)λ_n), P=Σ_(r≠s) i(λ_r−λ_s)z_r bar(z_s).
Then Q'=2 Re(J bar H)+P. The amplitude contribution to R should be
O(N/(MT)), using |B|≤CN and the coefficient bounds for J.
For x=λ_r−λ_s and y=λ_m−λ_n, the phase product PB has kernel x/y;
exchange the two ordered pairs to get (x/y+y/x)/2. This does not
remove denominators. Audit full monomial collection with r=m=k,
s=k+1,n=2k and N=k: coefficient of z_k² bar(z_(k+1))bar(z_(2k))
is x/y+y/x, asymptotic to k log 2. The conjugate monomial is distinct.
Resume by checking the amplitude bound, all monomial multiplicities,
and scope: no time-correlation lower bound or tail failure follows.

Completed as L158. Verified amplitude mean square by applying L156's
argument to T A_n', and verified both ordered contributions to the
repeated-index monomial. Exact rational polynomial regression passed.
The zero-total-frequency kernel is −1; its cutoff-weighted contribution
and the complementary time correlation remain unproved.
