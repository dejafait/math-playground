# Angular Gram entrywise positivity — bounded method stop

The constant-input test on the approved angular Hankel target gives
the exact signed quadratic form and full interior-residue formula in
[C645o](../lemmas/C645o-angular-gram-residues-and-negative-cross-entry.md).
An exact Gaussian-rational certificate at n=12, a=-5/4+i/2 proves
-141/1000 < Re K(-5/4,a) < -140/1000. The common-pole family has
two distinct poles, unit original residues and the prescribed clearance.
The result has not received an independent audit.

WHY IT FAILS: Positive original residues and positive semidefiniteness
of the angular Gram do not make its real entries nonnegative. Thus a
lower bound obtained by dropping its cross terms has a false premise.
The complete signed quadratic form remains nonnegative and may still
meet the required c^2*exp(-n/16) threshold. This witness is neither
an angular countersequence nor an upper bound on the operator norm.
The exact residue formula preserves every interior angular pole and
does not justify the earlier disk-mean shortcut.

This stop concerns entrywise positivity only. A proposed refinement
uses the nonpositive angular Fourier projection, retaining the zeroth
mode and the common-pole principal parts. That calculation remains
within the saved assessment but has not supplied a lower bound.
The inner-input response stop and ellipse-envelope stop also remain
unchanged; none is promoted into a ban on the full angular target.
