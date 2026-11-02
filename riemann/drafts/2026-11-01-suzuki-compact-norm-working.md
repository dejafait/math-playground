# Approved Suzuki compact-norm calculation: working record

Target is exactly the SPECIALIZE assessment supplied at invocation start,
`literature/2026-11-01-suzuki-large-parameter-compact-norm.md`.
Inputs: L001/L005/L018; Suzuki 1907.07302v2 Theorem 1.2 (K-ii)/(K-iii)
and (1.10); DLMF 5.9.13. No new source gate or changed target.

Checkpoint before completing the estimate: use s=16-iu, c=31/2.
DLMF's integral has coefficient between -1 and 0, so
Re psi(s/2)>=log|s/2|-1/8. The differentiated Euler logarithm gives
|zeta'/zeta(s)|<=sum_(n>=2) log(n)n^-16<=1/14.
The real parts of 1/s and 1/(s-1) are positive. Thus the COMPLETE
multiplier should satisfy

    |exp(-2 theta xi'/xi(16-iu))|
      <= [(pi/8) exp(15/56)]^theta (1+(u/16)^2)^(-theta/2).

The proposed base is bounded above by 22/41<1 using
exp(x)<=1/(1-x), 0<=x<1, and pi<22/7. For theta>=2, its integral
should be at most 16 pi (22/41)^theta. Weighted Fourier inversion
would give |K_theta(x)|<=8 exp(31x/2)(22/41)^theta. Causality
restricts K_theta[t] to the square [-t,t]^2; the Hilbert--Schmidt
bound would then give 16T exp(31T)(22/41)^theta uniformly on [0,T].

Remaining checks before claiming this: derivative-series local uniformity,
the digamma coefficient bound, exact Fourier sign/weight and L1 inversion
hypotheses, support reduction on the infinite input interval, and all
constant factors. No complete result claimed at this checkpoint.
This is parameter bookkeeping for known representations, not an Xi sign
estimate or a new kernel construction. No growing-window or fixed-theta
all-window statement is being attempted.

Completed in L618: the listed checks are supplied in the canonical
proof. Its final rational base is 28/41, using only pi<4 (rather than
the sharper 22/41 proposed above with pi<22/7). The complete bound is
16T exp(31T)(28/41)^theta for real theta>=2, with T fixed. This
settles the approved limit by ordinary specialization of known
representations; no independent critical audit or new Xi sign is
claimed. The working proposal above is retained as unfinished-stage
provenance; use L618, not this preliminary note, for the argument.
