# Signed full-circle endpoint test — step 138

Invocation target: Assess whether some fixed L696 centered-gap profile satisfies limsup_(q->infinity) [mean_(|u|=1)log|c_(0,12q+3)(u)|]/(12q+3)>=0, with the original unit masses, fixed anchor and exact finite endpoints.

The unchanged invocation-start EXPLORE assessment is
`literature/2026-11-03-centered-gap-scalar-complete-log-lower.md`.
This is one mathematical attempt, not another source review. The main
gap remains actual-Xi mixed positivity; the possible downstream use is
the scalar lower comparison for the full spatial mean. H, support and
realization remain independent gaps.

Inputs read: L666's exact rational product (6); L657's clearing and
precise logarithmic-integrability/root-formula imports; L694/L696's
fixed real summable capped profile and centered prescription; L699's
audited reflection interface and exact scalar charge formula; L701
Sections 1--4 for the signed finite-endpoint method. Do not assume
L699's conditional common-sign hypothesis or extend L701's local limit
to the unit circle. The step-129 unpaid-charge, step-131/133 common-sign
and step-135/137 microscopic-pairing stops have been checked. They do
not settle the scalar target. Existing unfinished work is preserved.

Keep d=5/4, R=11/8, U=121/64, A=27/10, Y=9/20,
n=12q+3, -2q<=m<2q, all unit masses, anchor, j=0, inverse denominator
angle, cap 1/8, fixed l1 shifts and all downstream M=n/3 moments.
All profile choices precede n.

Bounded test: start from the exact product, examine its two outer
endpoint contributions on the full angular circle, and pay any interior
or transition contribution before using logarithmic charge. Continue
only with a sublinear deficit on an unbounded subsequence or a new
signed estimate that changes the route. Stop at the first unpaid
normalized remainder, transition cancellation or linear loss. Neither
a local limit nor generic Jensen accounting is a successful test.

Initial calculation in progress: the unit-circle product has a smooth
large-n phase obtained by a Riemann sum, but its modulus derivative in
the ordinate is not the monotone bulk-disk phase used in L701. In
particular at the real angular points the outer nodes are suppressed.
Whether the actual signed response is also suppressed there must be
checked before claiming any obstruction. No scalar rate, endpoint
expansion or mathematical conclusion has yet been established.

## Saved calculation before verification

At u=-1 write alpha(t)=t/(U-d*t), beta(t)=1/(d-t). The exact factor
is (1+i*alpha*y)/(1-i*beta*y). Here 0<=alpha<beta, beta<=4,
alpha<=64/41, and beta^2-alpha^2>=16/121. Thus for
2/5<=|y|<=9/20 each factor's squared modulus is at most
1-32/6413, and the entire product is at most exp(-16*n/6413).
This covers whole outer bands, including the actual finite endpoints
for n>=63. It is the reverse of L701's interior-disk endpoint growth.

For any fixed capped l1 profile, the real-variable kernels
F_n(s)=W_(x+i*A*s/n)(-1) have |F_n|<=1, |F_n'|<16 and converge
on compact s sets to exp(i*Omega*s), where
Omega=A*[log(5)-4/5+(121/100)*log(121/41)]. Combining L690's
unshifted scalar limit with l1 dominated differences gives
R*c_(0,n)(-1) -> 1+sum_m exp(i*Omega*(m+1/2))*(exp(i*Omega*e_m)-1).
This is a signed statement; it is not an absolute summation of the
undisplaced oscillatory comb. L690 is a newly needed local input,
already covered by the reused scalar assessment's local comparison.

The proposed selection check is that 11/2<Omega<6<2*pi, so its alias
tau=Omega/(2*pi)-1 lies in (-1/8,0). At that point the exact Picard
equation has Q(tau)=0 and Phi(tau)=1. Subtracting its linear term
from the displayed signed correction should bound that correction
by pi*Omega*sum e_m^2 < 2*pi^2*r*||e||1. Choose the allowed Lev
coefficient constant larger before fixing the width, hence r smaller.
A scaled-cutoff Fourier estimate must first justify a width-uniform
bound on ||Q||A and hence ||e||1; the previously stated finiteness
alone is not sufficient. This selection and the constants are being
checked. If valid, the exact signed interior remainder survives while
the entire retained outer band is exponentially small. No angular
integral or scalar charge lower bound follows from a single point.

## Completed attempt

The proposed selection and signed remainder estimate are proved in
L702, `lemmas/L702-centered-gap-global-endpoint-remainder.md`.
The proof fixes the cutoffs first, bounds the prescribed data uniformly
in its width in the Wiener norm, enlarges the valid coefficient constant
once, and then fixes the resulting positive gap and profile before n.
At the alias of Omega the exact Picard equation controls the signed
correction by 2*pi^2*r*E<=1/8. The l1 difference limit uses L690 only
for the unshifted finite scalar; it does not sum a nonconvergent comb.

For this admissible class the actual signed scalar eventually has
modulus at least 3/(4R) at -1. The whole outer-band envelope is at
most n/(3R)*exp(-16n/6413), and the omitted signed interior has
modulus at least 1/(2R). Their ratio is at least
3*exp(16n/6413)/(2n), contradicting the required relative o(1)
remainder for a direct full-circle endpoint expansion. This is a new
informative obstruction to the tested expansion, not a lower bound
for the angular integral or a refutation of the existential scalar
target. No claim is made for every previously selected Picard profile.

The exact certificate
`scripts/one-sided-hankel/centered-gap-global-endpoint-138.json`
passes all 12 checks; its complete frequency bounds and check array
were inspected with the shared JSON inspector. The analytic proof has
not had a separate critical audit. Outcome NEGATIVE; stop this direct
global extension and retain central/transition contributions as an
unresolved requirement. Prior stops and partial work are preserved.
No mathematical EXPLORATION attempt or budget reset is claimed.
