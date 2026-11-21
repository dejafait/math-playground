# One-sided dual attempt: saved intermediate reasoning

The invocation-start EXPLORE target is the exact TARGET in
`literature/2026-11-06-oriented-one-sided-dual-period-test.md`.
Main gap: L030-L032/C032a actual-Xi all-degree mixed positivity.
Input: L847's actual F, omega, graph planes and compact Stokes;
L867's six-coefficient evaluation is reused, not its absolute-bound
classification. No cross-notebook input or new source search.

At a fixed point write L867's coefficients as p,q,r,s,t,v.
The upper-only J=0 test gives
`-p b-v(1+a^2)/b+(r-s)a+q+t <= 0` for every real a and b!=0.
Both signs of unbounded b force p=0; both signs as b tends to zero
force v=0; all a force r=s and q+t<=0. Set h=-(q+t)>=0.
For every (U,V)=(det A-1,tr A), the remaining test is
`q U+r V-h <= |F| sqrt(U^2+V^2)`.
Scaling (U,V) in the coefficient direction yields |q-ir|<=|F|.
Conversely these conditions suffice, by Cauchy-Schwarz and h>=0.
This retains all F and J zeros, with no orientation reversal.

Thus alpha=Re(gamma eta)-h dy1 wedge dy2, gamma=q-ir, with gamma,h
real-coordinate C1 and h>=0. Closedness gives, for j=1,2,
`r_xj=q_yj`, `(q+h)_xj=-r_yj` in logarithmic coordinates.
It does not directly give holomorphic gamma. In particular a smooth
negative q(x1,x2) supported in a radial region whose tori avoid F=0,
with r=0 and h=-q, illustrates an exact zero-period component.
This example is only a diagnostic, not an independently certified lemma.

Unresolved at this checkpoint: prove a global period upper bound or
construct a global strict-gain form under these equations and the actual
F bound. A possible approach is angular Fourier analysis of the closure
system, retaining its zero mode and every actual divisor. No Fourier
classification or period theorem is claimed yet. A local ansatz does
not meet the target; no RH or graph-existence conclusion is available.

Completion: the exact reduction, closure equations, period threshold,
radial-independent subclass stop and global C1 counterexample to a
holomorphic reduction are now proved in canonical L868. The full period
question remains open; this working note preserves the intermediate
state and is not a second proof source. No Fourier argument was used.
