# Actual negative-part majorant: restriction test

Approved target: test whether a hypothetical nonnegative harmonic
majorant of L504's actual negative part outside its finite obstacle
forces f=0. Reuse the separately approved SPECIALIZE assessment
`literature/2026-10-30-actual-negative-part-majorant-specialization.md`.
The main gap is actual-Xi all-degree positivity; this attempt can only
decide feasibility of this linear-majorant certificate.

Partial reasoning saved before the full write-up: set h=B+1 and restrict
to y>h. The two functions G(x,h+t) and G(x,h+t)+Re f(x+i(h+t))
are nonnegative harmonic for t>0. ABR 7.26, including its nonnegative
linear term at infinity, suggests H(0,t)<=t H(0,1) for t>=1:
the Poisson factor t/(s^2+t^2) is at most t/(s^2+1).
Thus the real part on the vertical ray has at most linear growth.
Evenness and reality imply f(iy) is real. Compactness handles the
remaining bounded portion of the ray. The Fourier representation
gives exponential growth of order at most one and real-axis decay.

Remaining local checks: use f(z)/(z+i) on both upper quadrants (its
only potential pole is outside the closed upper half-plane), obtain
bounded ray values and invoke Demkowicz 3.9 with order 1<2. Reflection
should give global linear growth; Cauchy estimates and real decay
should then force zero. No extension through the obstacle, boundary
regularity of G, truncation compactness or H_a nonemptiness is assumed.

Continue only if all of these hypotheses follow from the original
definitions. Stop if an additional growth condition on G, an omitted
infinity term or unjustified control of the imaginary part is needed.
No mathematical script or numerical certificate is relevant here.

Completed in `lemmas/L507-actual-negative-part-harmonic-majorant-obstruction.md`.
All listed checks close using the cited inputs; the inequality retains
the infinity term, and f/(z+i) is pole-free on both upper quadrants.
The result is a conditional obstruction, awaiting independent audit.
No inference about actual finite-truncation costs was attempted.
