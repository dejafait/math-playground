# Quartic stationarity calculation: preserved reasoning

Approved scope: the uncorrected B of L473 Section 4 only, with first
marginal B_0=(epsilon,v,k epsilon). The supplied SPECIALIZE assessment
is reused; no new source search or packet-family retry is needed.

For a translation-invariant Borel C2 path law with finite fourth moments
of F,F',F'', integrate the ordinary derivative of F^3 F' over [0,1].
Young's inequality bounds both endpoints and the complete integrand;
stationary derivative-jet distributions give Fubini and equal expected
endpoints. This yields E[F^3 F''+3F^2(F')^2]=0 without differentiating
an expectation. Derivative evaluations are continuous on the specified
path space, so path-law translation invariance gives their stationarity.

For B_0, epsilon^2=1, hence the integrand is k+3v^2. Its expectation
is -1/12+3/12=1/6. All three coordinates are bounded, supplying the
required finite fourth moments for a hypothetical path extension.
This rejects only that uncorrected first marginal and consequently its
uncorrected six-coordinate extension. It says nothing about L473's
corrected total law, whose rare component must be retained in quartics.

Full proof and qualifications will be stored canonically in L580;
this working note preserves the bounded reasoning, not a new action list.
