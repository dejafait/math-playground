# Quadratic Grunsky calculation1314

Invocation-start SPECIALIZE assessment1312 is supplied and reused unchanged.
The main gap is L030-L032/C032a actual-Xi all-degree positivity. This
attempt is confined to the prescribed five-coefficient rational family,
first three full columns and one necessary compatibility test against
the fixed1307 boxes. No analytic realization or all-degree sign is assumed.

Work checkpoint before exact computation: import Teo's degree-m Faber
composition identity. With g(Z)=Z+sum_(j=1)^5 b_j Z^(-j), the candidate
Faber polynomials are Phi1(w)=w, Phi2(w)=w^2-2b1 and
Phi3(w)=w^3-3b1*w-3b2. Verify their full negative Laurent coefficients
and the support bounds 5m before taking any column products.

Planned necessary test: eliminate only tau,d2,d3 using strict positivity
of the first defect row, and retain the resulting exact polynomial
conditions. Apply weighted-column Cauchy-Schwarz to the first two
columns. Test this relaxation using S3^2/(S2*S4) from the unchanged
outer boxes. Passing a relaxation establishes neither formal feasibility
nor unit-disk univalence; do not add a parameter sweep if it is inconclusive.

The actual-input boxes are conditional on L037's documented arithmetic
contracts, as imported in C030z calculation1307. All larger blocks,
initialization, singular cases and actual analytic identification remain
open. The earlier fixed-linear and positive-diagonal-linear stops stand.
No cross-notebook input, new quadrature, rescaling or degree change.

Completed result: C031a is canonical for the full support proof, complete
six equations, exact three-polynomial reduction, guards and conditional
actual-box Cauchy test. Certificate1314 retains every coefficient and
verification residual; all12 checks pass. The test is inconclusive for
formal feasibility and univalence. No extra necessary test or sweep was
performed. The small-tau continuation is only a REVIEW_REQUIRED source
nomination; its mathematics was not attempted here.
