# Logarithmic L2 test: working checkpoint (step150)

The unchanged SPECIALIZE target in the step149 assessment is active.
Main gap: L030-L032/C032a actual-Xi mixed positivity. The bounded test
is the first-two-real-zero L-image off-diagonal Gram entry; nonzero
certification would reject only this metric. No root or Gram certificate
has yet been produced. Preserve all prior stops and unfinished work.

From the exact L906 series and L019, W(x)=w(e^x)=K(x)/4 for x>=0.
L906 inversion makes W even; hence L020 gives the full transform
integral W(x) exp(i alpha x) dx = Xi(alpha)/2, with the local Xi
convention. This reconciles the kernel without trusting a printed
Mellin prefactor. Absolute convergence for every fixed complex alpha
comes from L906's superexponential bounds. Details will be canonical.

For a real zero alpha the full transform vanishes, so the primitive
has both lower- and upper-tail representations. To establish L2 for
L u_alpha it is essential to bound q=W'/W, not just W. On x>=0 put
v=pi exp(2x)>=pi>3. The n=1 term gives
W>=exp(x/2) v^2 exp(-v), since 2v^2-3v>=v^2.
The differentiated series has |P1(v n^2)|<=10(v n^2)^3 for v n^2>=3.
The sum n^6 exp(-v(n^2-1)) is uniformly finite for v>=3.
This should give |q|<=C exp(2x), with inversion giving the other end.
Need explicit series constants, primitive tails and endpoint integral
bounds before claiming convergence. Root-index certification remains
unperformed; default Python has no flint, mpmath or scipy.

Only the approved normalization/convergence/Gram specialization is
being attempted. Stop at a failed prerequisite; no metric substitution,
unverified decimal roots, numerical quadrature or RH claim is allowed.

## Completion checkpoint

The provisional reasoning above is superseded by the canonical L908
proof with all final constants and complete endpoint arguments. The
remaining numerical phase stopped at missing certified root isolation:
Python3.15 and Python3.12 lacked python-flint, and both bounded package
attempts found no matching distribution. No root certificate or initial
128-bit Gram pass was produced. Resume only with a rigorous implementation.
The new critical-audit nomination awaits separate approval.
