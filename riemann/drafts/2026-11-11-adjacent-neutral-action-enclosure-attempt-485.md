# Exact action enclosure attempt, step485

The ready EXPLORE assessment is unchanged:
`drafts/literature/2026-11-11-adjacent-neutral-weighted-section-certificate-482.md`.
Main gap: L030-L032/C032a actual-Xi positivity. The approved intermediate
target remains a positive common L2 margin for C744i(6); its downstream
use is nearest-neighbor neutral interaction control. Remote, non-neutral,
odd and global propagation gaps are independent.

The current attempt attacks C744j(8)-(9)'s action/covariance enclosure.
Retain ell=log(3)/2, exact complex moment constraints, full unshifted
energy, the complete Hankel kernel and n=2 partial reflection. No RH,
collar, shifted denominator, H2 cap or cross-notebook input is used.
The supplied step483 assessment and step482/484 failures are reused.
C744i Section7, C744j, L741 Sections2-3 and L744(6) were checked for
normalization; this is not an independent audit of those whole results.

Work in progress: write q_0(t)=(exp(t/2)/(sinh(t)/t)-1)/t and
h_0(t)=k_1(t)-1/(2t)=(exp(-3t/2)/(sinh(t)/t)-1)/(2t).
On the complex disk |t|<=2, a geometric bound for sinh(t)/t-1
permits Cauchy bounds for their rational Taylor coefficients. Seek
degree 96 uniform remainders small enough to charge in operator norm.
Integrate the resulting polynomial kernels exactly; retain the
Carleman action as a polynomial plus p(-x)log((ell+x)/x). This avoids
the unenclosed backward recurrence and inner quadrature in step484.
The outer products still have endpoint logarithms and a reflection
jump. They must be enclosed before any positive matrix claim.

Discriminating test: derive and check a full-head L2 action error below
10^-22, including all 255 coordinates jointly, then retain its explicit
finite-matrix/covariance perturbation charge. If that fails, record the
unpaid term. A positive full certificate requires both Schur lower
bounds after every error; only an exactly neutral smooth ratio>=1/2
refutes the fixed target. No diagnostic agreement counts as an enclosure.

## Completed attempt

The result is canonical in C744k. The exact action representation keeps
all singular logarithms and the reflection jump, while rational degree 96
Taylor kernels have a joint 255-column action error below 5.22e-24.
The exact moment-tail correction and kernel replacement together cost
less than 1e-19 in the fixed floor0.72/rho0.95 Schur test. The 19 exact
arithmetic checks pass in `scripts/adjacent-neutral/action-enclosure-485.json`.
This is an analytic enclosure, not an enclosure of the old floating
locator or the new exact finite matrices. It is a known-tool local
specialization and remains independently unaudited.

The unresolved calculation is now explicit: integrate the products of
the piecewise polynomial/log action columns in C744k(10), enclose exact
moments and constants, subtract the finite projection covariance, and
certify both Schur matrices. The representation may involve large
cancelling coefficients g(-v); ordinary floating-point evaluation is
not licensed. C744k(3) pays only its stated analytic perturbations.
An exact finite Schur lower bound 1/25 would suffice, with a remaining
full-form margin exceeding 1/30. Neither bound is established here.

Continue the same approved target using C744j(1)-(9) and C744k(1)-(12),
with C744i(6)/(11) and L741/L743/L744 as the unchanged normalization
inputs. No changed target or new assessment was introduced. Prior
Carleman and degree 128 stops remain, and all independent global gaps
stay open. PROOF.md's assembly remains unchanged because no full
two-sign margin has been added to it.
