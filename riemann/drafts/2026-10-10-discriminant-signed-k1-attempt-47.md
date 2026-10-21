# Signed k=1 specialization — working step 47

Approved target and prior SPECIALIZE coverage:
`drafts/literature/2026-10-10-discriminant-unequal-orientation-projection.md`.
Main gap: global actual-theta mixed positivity. The intermediate test is
the complete k=1 mean in L390, at o(log^4 H). Success supplies one
square-moment harmonic only; k=0, k=2, beta positivity and the global
sign/count gaps remain independent.

One bounded proof attempt, reusing the modified-Gonek and Bourgain
inputs already assessed. No extra literature turn or mathematical
script. Narrow checks found the step-45 absolute rectangle failure,
not a completed signed four-factor calculation. Preserve that failure.

Working plan, not yet an established result: conjugate the k=1 complex
integrand and put s=1/2+it. Reflect its four Hardy jets consistently;
the remaining carrier is chi(1-s). A fixed response head twist
r=a/b enters as r^(s-1/2). Rewrite r^s F(s) as a^s times a Dirichlet
series supported at indices bn. The modified-Gonek theorem then has
integer gamma scale a and additive phase exp(-2 pi i bn/a).
Absolute summation of the resulting four-divisor coefficients should
cost H log^3 H after the derivative log normalizations, rather than
H log^4 H. All coefficients from Omega, Omega' and L must retain
bounded variation before partial summation.

Connector test: interpolate Bourgain's 13/84 bound toward the absolute
right line, retaining Cauchy derivative circles of radius 1/log H and
the chi(1-s) modulus H^(sigma-1/2). Seek a uniform exponent <1 for
all four factors on the connector. Stop if this or the slow-weight
passage fails; a surviving leading term must be retained.

Pending obligations: exact conjugation/functional-equation signs;
ordinary order-two coefficients; coefficient sums and both gamma
phases; uniform primitive bound on [H,V], H<=V<=2H; sharp endpoint
control; then full-head removal using L390 and L389 norm budgets.
No RH, simplicity, noncoincidence, phase independence or D sign.

## Completed bounded attempt

Canonical L391 records the complete proof: conjugation leaves exactly
chi(1-s); integer-support encoding permits the cited fixed-integer
modified-Gonek theorem. The absolute sum of its signed output is
O(H log^(d+3) H), and the actual normalized coefficients have size
and total variation O(log^(-d) H). This gives fixed-head O_N(H log^3 H).
The interpolated subconvex connector exponent is at most 2/3, strictly
below one, with Cauchy disks retaining all ordinary jets. The harmonic's
own full-tail bound is C eta_N H log^4 H; fixed N first, then N to
infinity, proves the complete o(H log^4 H) statement.

Outcome: ADVANCE, local REPRODUCTION of known-source tools, not a new
moment theorem or RH progress. No mathematical script was needed.
The proof and its L390 physical input require a separate critical
audit. The earlier O(H^2) absolute horizontal certificate remains
preserved: this improvement evaluates that edge with a signed theorem.
