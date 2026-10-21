# Quartic residual: covariance reduction and unfinished joint first order

The unchanged approved target is the complete quartic residual response
for both actual probes, under
`literature/2026-10-12-quartic-residual-insertion-cubic-scale.md`.
The main construction gap remains the interacting reflected error
<=c_box/2 and the independent continuum/infrared requirements.

This bounded attempt isolates the third difference in L150(11),
K^0:U^0:(C-C^0), without dropping either insertion subtraction or
the other two differences from the full target. Its intermediate test
is whether the local covariance remainder, after inversion-even pieces
are removed, reduces uniformly to the explicit axial slope
((s+t)/2-j_*) P_inf. This would replace an uncomputed covariance
asymptotic by a fixed local tensor in the joint first-order calculation.

Starting inputs: L149, L150, L085 and L114; L028 supplies the retained
smooth exterior bounds through L150. L010/L011/L017/L018/L026 conventions
and L019's compensation constraint remain unchanged. The prior source
assessment is reused; no further literature step is needed. Local
drafts and ATTEMPTS/009, /011 and /036 contain no completed first-order
covariance comparison. Those failure records are preserved.

Completed result: [L151](../lemmas/L151-quartic-residual-covariance-slope-reduction.md)
proves this reduction with uniform o(1) local covariance error and
o(a^-3) summed contraction error. Its proof retains the exact L085
covariance, the L150 single-row projection comparison, the complete
axial resolvent, and both full spectra. A projected heat representation
with an integrable uniform tail justifies the local limit. The
stationary co-closed comparison and absolute-value kink are
inversion-even; only the explicit axial slope remains from this term.

The continuation stays within the same exact approved target. Retain
L151's slope contraction jointly with the two differences K-K^0 and
U-U^0 and both insertion subtractions. Essential inputs are now
L149 L150 L151 L085 L114, with L028's smooth exterior control retained.
The slope contraction is parity-even as a whole and cannot be dropped
by repeating L150. No actual-probe value, continuum exterior-jet
expansion, joint cancellation or full limit interchange is assumed.

Continue if the complete signed first-order contraction is proved
zero with a controlled remainder, a nonzero actual-probe coefficient
is established, or a discriminating obstruction changes the mechanism.
Abandon any repetition of frozen parity or the absolute local count
that only recovers bounded cubic-scaled values. The present reduction
gives no quantitative rate beyond little-o for its error and no
finer-power or logarithmic control. All other response jets, full
compensation, finite matching, interacting reflected bound and
continuum/infrared requirements remain open. No candidate exists.
