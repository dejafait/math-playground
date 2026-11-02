# Angular anchor-distance mechanism stopped

The approved uniform rate-1/100 lower-distance mechanism fails on the
admissible undisplaced sequence e_r=0. The full proof, explicit complex
approximation coefficients, exact contour certificate and qualifications
are in [L672](../lemmas/L672-angular-anchor-distance-interpolation-countersequence.md).
The upper distance is at most 5*exp(15)*n*exp(-11*n/1000), so the
specified normalized excess loss is unbounded. The separate conceptual
audit in L672 Section 6 has now verified the asymptotic proof and replayed
the complete exact certificate; no Gram-inverse or finite-conditioning
argument is being substituted for it.

WHY IT FAILS: Allowing arbitrary complex auxiliary coefficients lets
phase-centered interpolation in the pole parameter approximate the
anchor exponentially more accurately than the proposed uniform floor.
The contour estimate pays all parameter, angular and finite-grid costs.
The actual residues remain one, and the approximating coefficients are
not their negatives. Hence this stops the sufficient distance route
without showing that c_0, the full spatial polynomial or H is small.
Earlier spatial, ambient-evaluation and clearing stops remain intact.
This complex-linear separation mechanism is now stopped on audited
evidence. A different residue-constrained mechanism requires a specific
independently testable target and matching coverage. The step-36
positive-cone nomination is REVIEW_REQUIRED and asserts no new bound.
