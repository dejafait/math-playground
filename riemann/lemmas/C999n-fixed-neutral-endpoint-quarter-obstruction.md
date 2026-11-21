# C999n: A fixed neutral endpoint obstruction to the quarter comparison

## Hypotheses

Use C744v/w's complete D,S,T, C744z Sections1-3's complete U,
C999k's unchanged reference R, C999l's predictor convention and
C999m Sections1-4/18's Z_T, d_n and F. Thus ell=log(3)/2,
R has head H on raw modes0:511 and diagonal h(k_n)/2 thereafter,
H=Mhat-.00024 I-(100/307)(Chat+.0046 I), with the exact dyadic
Mhat,Chat stored as m0,cov00 in
`scripts/separation-seven/complete-covariance-532.npz`.
Decimal constants .00024 and .0046 in this definition are exact rationals.

Retain the inherited analytic-response and IEEE754/Decimal contracts,
whole-neutral-core and unreplayed c_* qualifications. This result is
conditional on those same contracts; it does not audit them as a whole.
No RH, H2 existence/slack, complementary positivity or endpoint relation
is assumed. Assessment579, completed in step580 before invocation,
licenses this one fixed-band REPRODUCTION calculation, not a new general
inverse theorem or a claim of originality.

Import Friedrich, Gunther and Klotz, *A generalized Schur complement
for non-negative operators on linear spaces*, arXiv:1708.01545v1,
Definition4.1/Lemma4.2 p5, (4.1)-(4.2) p6, Corollary6.5 and its full
proof p11, [pinned PDF](https://arxiv.org/pdf/1708.01545v1).
For a positive pair (A,B), Corollary6.5 identifies the supremum of
|<By,x>|^2/<Ax,x> with <omega(A,B)y,y>, with its stated convention
at zero denominators. The required positive-pair specialization is
checked below. No reproof of that theorem is needed.

## Conclusion

**Step583 audit:** Section4 upholds step581 under the stated inherited
contracts. There is a specified nonzero
rational complex free endpoint pair y, supported on512:1023 at both
independent endpoints, such that its EXACT neutral completion satisfies

    F(0,y)-||y||_tail^2/4 < -.11797 < 0.                 (1)

The free coordinates have zero imaginary parts. This is an admissible
complex pair, without a reflection or parity constraint between endpoints.
The physical coefficients at0,1 are exact moment ratios, generally
irrational, rather than rounded coefficients declared neutral.

Thus the sufficient assertion F(0,y)>=||y||_tail^2/4 fails. This stops
that quarter-allocation assembly with the unchanged R and predictor.
It does not refute the actual minimized triple form: Q_min>=F is a
lower comparison and F<0 supplies no upper sign for Q_min. C999m's
mixed-quarter bound is unaffected. No smooth negative triple, off-line
zero, RH conclusion or complete RH candidate is obtained.

## Proof

### 1. Frozen data and the correct one-sided inverse bound

The full integers specifying the free pair and trial are respectively
`free_numerators` and `trial_numerators` in
`scripts/separation-seven/endpoint-complement-locator-581.npz`.
Their common denominator is2^40. The archive, generator and input hashes
are pinned in `scripts/separation-seven/endpoint-complement-locator-581.json`
and the certificate record. The first512 free entries are y_f and the
last512 are y_h. All1024 entries are nonzero; both endpoints are allowed
independently. Define f=Z_T y_f and h=Z_T y_h by C999m(1), using its
exact ratios r_n. This makes both moments zero algebraically. Raw
support is {0,1} union512:1023. At x=0 the predictor g=0 exactly.

Let t have the1024 dyadic trial entries on raw modes0:1023 and vanish
elsewhere. No neutrality requirement applies to t. It belongs to
Dom(R^(1/2)); C999k gives R>=.239999 I. The full forcing is
rho=Tf+T*h in L2, not a projection or prefix replacement.

Apply the cited corollary with X=Dom(R^(1/2)), reference form A,
Y=C, and Bz the functional induced by z rho. The square-root range
condition of a positive pair is satisfied by R^(-1/2)rho, which exists
since R is positive coercive and rho in L2. Its omega scalar is the
complete pairing <R^-1rho,rho>. Therefore this particular trial gives

    <R^-1rho,rho> >= |<rho,t>|^2/<Rt,t>.                (2)

The denominator is strictly positive as enclosed below. We evaluate
<rho,t> against the full operators, not a truncated rho substituted
into the inverse. Finite support of t means only its pairing uses
rows0:1023. All unused variational directions can only increase the
left side of(2). Consequently no inverse-output tail estimate is
required for this LOWER bound. In particular no lower endpoint of
C999k's earlier inverse UPPER-bound expression is used.

### 2. Complete entries on the changed finite range

The generator assembles all entries with row0:1023 and input columns
{0,1} union512:1023. Its local endpoint matrix is D+S, whose form
equals L on these exactly neutral endpoints; it includes no moment
penalty in its saved `local_matrix`. Both full T orientations are
retained. The endpoint expression is

    E=< (D+S)f,f>+<(D+S)h,h>-2 Re<Uf,h>.

It is Q_actual(f,0,h). Matrices are real; quadratic and cross pairings
use ordinary conjugate-transpose conventions, agreeing here with the
inherited first-slot-linear convention.

Every translation is evaluated by C744w Section3's unequal-index and
equal-index formulas, including the constant mode. For zero delay
use the exact identity matrix. All16 active separation7 prime powers
are included. The334 separation14 prime powers are independently
regenerated by integer tests 3^13<n^2<3^15 and trial division and
compared entry-for-entry with the recorded list in stop546. The power
2187 has exactly zero delay and weight log(3)/sqrt(2187).
All signed products are combined before any quotient or square.

The full single-cell response is C744w(11), using the64-term exact
psi recurrence and its assessed remainder(12); the equal-index sum
is summed through j=65535 with correction1/(2c_65536). The
exponentially weighted response retains j=0:63; the cross continuous
operators retain j=1:7 with their complete paid operator tails. These
are representations with remainder bounds, not changed operators.
No differentiated digamma asymptotic is used.

Here are deliberately loose UNIFORM absolute entry errors for these
new finite rectangles:

    local D+S: .001;     T, T*, U: .000001.             (3)

The justification is supplied explicitly rather than transferring
old512-column accumulated matrix errors. For 0<=n,m<=1023,
normalization nu_n nu_m<4, and, at unequal indices,

    (n^2+m^2)/|n^2-m^2|<1024,
    |k_n-k_m|>=pi/ell>5.7.

C744w(12)'s r(k) is everywhere <.000058. Its off-diagonal response
error(13), including normalization, is at most
4*.000058/5.7 <.000041. The diagonal response remainder before
normalization is
c_J^-2+2k_n^2[1/(6c_J^3)+c_J^-4]<6e-9, J=65536;
after normalization it is <4.8e-8. The D remainder is <.000058.
Adding the following arithmetic allowances and exponentially small
remainders leaves the local error strictly below .001, including
n=m=0. Symmetrizing the local center preserves this error bound.

Constants are formed with80-digit Decimal operations and rounded
once to binary64; pi is checked by the Machin80-term enclosure.
Each delay error is <1e-16, including all334 remote delays; zero
is symbolic. Every weight error is <1e-16. The certificate checks
all remote constants and their full weight sum<53. Continuous
coefficients use Decimal powers of 3^(1/4), with integer exponents,
not a library exponential. The single-cell exponential coefficients
also use Decimal powers, rather than assuming a library power bound.

The exact arithmetic ledger of C744w Section4 applies entrywise:
|x| is now smaller than its assessed207000 limit, and its sine/cosine
argument bound10^-14(1+k_n) still holds. With the displayed1024
ratio, each normalized shift error from argument evaluation is less
4*1025*10^-14; multiplying by the complete weight sum<53 gives
<2.2e-9. Denominator/input rounding contributes <53*1e-11;
334-term summation, normalization, products and equal-index formulas
leave the complete prime-entry error <1e-7. The small continuous
part, including its <1e-24 omitted operator norm at separation7
(and a still smaller bound at14), keeps the cross-entry error below
.000001. Constant-mode and exact zero-delay cases avoid division.

For local entries, C744w Section4's recurrence/arctangent bounds,
64 exponential terms and the same denominator ratio bound give
<1e-7 arithmetic error. The65536-term positive diagonal sum has
normalized value<20 and gamma_65536<8e-12, giving <2e-10 rounding
error. Real logarithms are evaluated with Decimal; there is no
library logarithm/digamma accuracy premise. These estimates and the
preceding analytic errors prove(3). They do not assert that the old
assembled512-column norm totals apply here.

For the reference denominator the saved head center approximates
its exact rational definition with entry error <1e-10: both original
dyadic input matrices have entries below400, and the complete
binary64 rational assembly is checked. The tail reference diagonal
h(k_n)/2 has error <.00005, using r(k)<.000058 plus the arithmetic
allowance. These loose bounds are adequate; no inverse is computed
by the verifying script.

### 3. Full scalar enclosures and propagation

The verifying script reconstructs both exact low coefficients with
directed Decimal intervals, from the frozen dyadic free coordinates
and the exact r_n formulas. Their total L1 differences from the
saved physical coefficient centers are each <1e-12; the full
intervals are in the certificate. Write these differences as delta_f,
delta_h, and the exact coefficient L1 bounds as l_f,l_h,l_t.
They satisfy l_f,l_h<1.442 and l_t<.987.

All saved entry centers have magnitude<400. For a scalar center
x*Ay with dimensions<=1024, charge an absolute error
10^-8||x||_1||y||_1. Indeed the two dot products obey the inherited
gamma bound, and 400[(1+gamma_1024)^2-1]<1e-8. This also covers
the scalar conversion; no factorization/eigenvalue accuracy is used.
The script checks all relevant entries, not samples. No overflow
or problematic underflow occurs.

In addition to these dot allowances, (3) pays endpoint error

    .001(l_f^2+l_h^2)+2*.000001*l_f*l_h
    +401[delta_f(2l_f+delta_f)+delta_h(2l_h+delta_h)
           +2(delta_f*l_h+delta_h*l_f+delta_f*delta_h)].

The forcing-pairing error is at most

    .000001*l_t(l_f+l_h)+401*l_t(delta_f+delta_h).

The reference-energy error, beyond its dot allowance, is

    1e-10||t_head||_1^2+.00005||t_tail||_2^2.

These estimates include all changed-range entries, orientations,
low corrections and their signed sums; they are scalar estimates
for this frozen pair, not an unproved uniform operator bound.
Tail weights d_n and the weighted free norm are evaluated directly
with directed Decimal, not the locator's library logarithms.

The full record `scripts/separation-seven/endpoint-complement-certificate-581.json`
reports, rounding OUTWARD here to fewer digits,

    E < .723746547,
    .591722 < <Rt,t> < .591741,
    |<rho,t>|^2/<Rt,t> > .5917169000,
    ||y||_tail^2 > 1.0000000000,
    E-|<rho,t>|^2/<Rt,t>-||y||_tail^2/4
        < -.1179703534 < -.11797.

The denominator is enclosed strictly above0; its UPPER endpoint
is used for the quotient LOWER bound. The numerator uses the
lower squared-absolute pairing enclosure. By(2), subtracting this
quotient gives an upper bound on the ORIGINAL difference in(1).
The nonzero free vector and positive norm are both checked. This
proves(1) under the stated contracts. The reported two-sided interval
for the finite-trial upper expression is not a two-sided enclosure of
F itself; its lower endpoint is not used or asserted for F.

The locator's eigenvector merely selected the frozen integers; the
proof does not use its eigenvalue, minimum property or solve accuracy.
Its JSON remains explicitly uncertified and retains its unpaid-error
warnings; this separate certificate pays them for this frozen vector
under the stated entry ledger. No tuning of band, R, predictor or
quarter constant was performed. An independent conceptual audit of
the ledger and one-sided specialization is still required.

Reproduce from the notebook, using the saved frozen archive for verification:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/separation-seven/endpoint-complement-certificate-581.py

The generator can reproduce entry centers and propose integers, but
its library eigensolver need not return identical frozen integers
on every platform. The saved integer arrays, not a regenerated
proposal, specify this result. Full evidence includes every integer,
entry center, check, enclosure and content hash.

### 4. Separate conceptual audit — step583, 12 November2026

The invocation-start SPECIALIZE581, separately approved582, covers this
audit. The frozen free/trial integers, supports, reference, predictor and
quarter constant are unchanged. This is REPRODUCTION: validation of an
existing local obstruction, not a new source-level theorem. The historical
pending-audit statements in Section3 and certificate581 describe their
original status and are superseded here. All inherited analytic-response,
IEEE754/Decimal, whole-neutral-core and unreplayed c_* qualifications
remain. No additional positivity premise is introduced.

**Exact domains and direction.** C999m(1) gives the ratio of each of
the two exponential moments to the corresponding parity-low moment.
The free entries are exact dyadics; recomputing both low coefficients
from these ratios annihilates BOTH moments algebraically. These finite
cosine endpoints belong to V0 and the finite trial belongs to V, the
form domain of R. The predictor is exactly zero here. Bounded T and T*
give the full rho in L2. C999k's positive coercive R therefore satisfies
the cited Friedrich-Gunther-Klotz positive-pair hypothesis with square-root
image R^(-1/2)rho. Corollary6.5 applies to the finite trial in that same
form domain. Its denominator is positive and its quotient is a LOWER
bound for the full inverse pairing. No neutrality of the trial, projected
inverse identity, inverse-output truncation or three-cell sign is needed.
The sign of the subtraction then gives precisely the upper bound used
in (1). It gives no upper bound for Q_min.

**Complete entries and changed range.** The audit replays the generator
only through entry assembly, before its neutral locator, solves,
eigenvectors or file writes. Every saved local, T, T*, U and D entry
agrees exactly, including all514 physical columns, all1024 forcing rows,
constant/equal-index cases and the exact zero-shift identity. A separate
prime-base enumeration uses integer powers and integer square roots;
it recovers all334 remote powers and the unique zero delay2187.
Directed enclosures verify every actual generator delay and weight,
its strict overlap and its nonzero sign where appropriate. All16
separation7 powers remain those of C744v. The continuous factors are
the integrals of exp(-c_j x) and exp(c_j y), with prefactor
exp(-(s-1)ell c_j); their order reverses for the adjoint. Thus no
continuous term or orientation is inferred merely from numerical symmetry.

For unequal indices the maximum cancellation ratio is attained at
(1023,1022): (1023²+1022²)/(1023²-1022²)<1024. The minimum frequency
gap exceeds5.71920. The directed ledger gives

    max r(k) < .000057097552,
    off-diagonal normalized response error < .000039933931,
    diagonal error before normalization < 5.125617e-9,
    omitted exponential response < 2.117e-34,
    omitted separation7 continuous operator norm < 1.465e-25.

The latter bound is
1/[3^49 sqrt(3) (33/2)(1-3^-6)], from the row/column-integral
bound starting at j=8; separation14 has a smaller tail. For the
exponential single-cell suffix use
8*3^-64/[(1-1/3)(128.5)^2], a larger normalization than needed.
Neither bound differentiates the digamma asymptotic.

C744w Section4's arithmetic estimates extend here because |k delta|
is smaller than its original limit and the same cancellation ratio
bound holds. The complete remote sine/cosine argument contribution is
<2.141e-9. Denominator/input rounding contributes <53e-11; summing334
normalized shifts, each bounded in magnitude by1 before its weight,
costs less gamma_334*53<2e-12 beyond the individual evaluation errors.
The equal-index formula is bounded directly: ell-|delta| has absolute
error <2e-16 before elementary rounding, the cosine multiplier has
size at most ell/2, and the sine quotient has divisor at least2k_1.
For n=m=0 only the normalized overlap remains; for zero delay the
identity is symbolic. Normalizations, weights, products and the seven
continuous rank-one terms therefore fit the claimed prime/continuous
arithmetic allowance <1e-7, well inside the cross-entry cap1e-6.

For the local response, the64-term recurrence error, bounded divided
difference denominator and exponential arithmetic retain C744w's1e-7
allowance. The positive diagonal sum has normalized value <20: at
zero, sum c_j^-2<=5 and normalization2/ell<4; at positive indices
use sum1/(c_j²+k²)<=1/k²+pi/(4k) and k>=k_1. Hence the65536-term
rounding cost remains <2e-10. Adding the D error, off-diagonal bound,
eight times the diagonal error and elementary allowance is a conservative
uniform bound <.000097173<.001. This covers the constant mode and the
symmetrized saved local center. The reference-tail error is
<(max r+1e-7)/2<.000028599<.00005. Thus the changed-range entry ledger
is justified independently of the old512-column accumulated norm totals.

**Complete scalar evidence.** The audit verifies every entry of the
reference head against its EXACT rational definition, using integer
rational arithmetic on m0,cov00. The largest assembly discrepancy is
<6.954e-15<1e-10. It also recomputes all six load-bearing matrix
products as exact rational sums of the saved dyadics. Each lies in
its original dot enclosure; the theoretical two-dot allowance is
400(2gamma_1024+gamma_1024²)<9.095e-11<1e-8.
All coordinate shapes and integer conversions are checked. The exact
neutral coefficient errors remain <2.966e-23 and <1.428e-23, with
L1 norms <1.442 at each endpoint and <.987 for the trial. Thus Section3's
coefficient perturbation estimates pay the full signed forms, including
both low corrections, without a rounded-neutrality premise.

Reconstructing the head energy directly from the rational reference
definition and retaining the original entry/coordinate allowances gives
the following outward-rounded independent enclosures:

    E < .723746464,
    .5917288538 < <rho,t> < .5917345442,
    .5917226470 < <Rt,t> < .5917407510,
    |<rho,t>|²/<Rt,t> > .5917169569,
    ||y||_tail² > 1.000000000002,
    E-|<rho,t>|²/<Rt,t>-||y||_tail²/4 < -.1179704934.

The last line is again an upper bound for the original F-minus-quarter
expression, not a lower enclosure for F. Its strictly negative upper
endpoint confirms (1), including the original weaker -.11797 claim.

Reproduce without changing earlier artifacts:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/separation-seven/endpoint-quarter-audit-583.py

The full certificate is `scripts/separation-seven/endpoint-quarter-audit-583.json`.
All1420 checks pass, with no failures. It records every constant check,
all neutral ratios and tail weights, exact scalar numerators/denominators,
complete scalar intervals, source/archive hashes and preservation checks.
The original certificate is replayed in full before independent scalar
reconstruction. Entry replay reuses the reviewed generator and elementary
routines; it is not a second independent transcendental implementation.
Its agreement alone is not analytic verification: the analytic error
and case analysis above, with the inherited contracts, supply that link.
No inverse/eigenvalue/FFT accuracy is assumed or tested.

The sufficient unchanged quarter assembly is stopped. The actual triple
form, the independently audited mixed quarter, other separations,
C744q margin, H2 slack/existence, non-neutral coverage and global
actual-Xi positivity retain their previous status. This is neither an
RH candidate nor a disproof.

## Mathlib

Full matching coverage for this fixed signed endpoint obstruction is
not checked. No Mathlib theorem is claimed absent. The only general
inverse-pairing theorem used is the precisely cited Corollary6.5;
its positive-pair applicability is checked above. General Schur or
inverse-order results alone do not supply the sign(1).
The step583 audit does not change this unchecked full-matching status.
