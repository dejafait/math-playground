# Bounded saved-affine quotient attempt

STEP_ID: beal-2026-10-16-253-separated-eleven-quotient-attempt

RESEARCH / REPRODUCTION under the unchanged prior SPECIALIZE assessment
`drafts/literature/2026-10-16-separated-eleven-supported-unit.md`.
Exact target: Construct a supported norm-square unit in V_S whose valuation parities at the two rational eleven-adic degree-one factors are unequal.

## Saved before calculation

The main gap is primitive integer emptiness. One separating unit could
add an independent restriction to L077's two directions; further pruning
from fourteen to eleven, the localized class kernel, rank and integer
lifting remain independent gaps. Inputs are L033, L041, L069, L073,
L074, L076 and audited L077; L046/L071 supply the existing dyadic
comparison. There is no cross-notebook input or class-number assumption.

Use the same degree-36 D=Q[k,t], m(k) from L069 and
f(t)=t^3-t^2+t+1, theta=8-14t+6t^2, as in L077. The ordered
degree-one eleven-adic primes have (k,t) residues (8,6),(2,6).
Enumerate exactly i<j among the 1774 saved affine elements in
`scripts/separated-eleven-unit/affine-certificate.json`, at most
1,572,651 quotients z_i/z_j. No coefficient-box enlargement is allowed.

First screen exact absolute norm ratios: the fully stripped outside
factors of the two integer norms must coincide. For every survivor,
compute the quotient and inverse exactly in the basis k^i t^j,
0<=i<12, 0<=j<3. Verify their product is one and test that every
coefficient denominator is supported at 2,11. Passing certifies both
elements in Z[k,t,1/22] and hence actual S-unit support in maximal rings.
Failure of this sufficient order certificate alone does not prove
maximal-ring nonsupport; retain such cases explicitly as unresolved.

For each certified quotient z, compute n=N_D/K(z) by the ratio of the
saved relative norms and form u=z/n. Verify N(u)=n^(-2), with n^(-1)
the explicit square root. The same support follows from norms of
S-units. Certify the ordered valuations AFTER this correction, using
simple-root Hensel lifts of m at 8,2 and f at 6. If a value vanishes
at available precision, increase precision only up to the saved cap of
128 eleven-adic digits; otherwise retain an unresolved valuation.
Both quotient orientations have the same parities, since inversion
negates integer valuations. Save all pairs passing the norm screen,
exact quotient/inverse coefficients and all verification failures.

A certified corrected quotient with unequal parities meets this
intermediate target. Exhaustion without one stops this finite quotient
strategy; it proves neither universal parity equality nor nonexistence
of another witness. Preserve ATTEMPTS/032–034. No full unit basis,
class-group value or primitive integer solution is assumed. Exact
support/norm identities specialize the previously inspected Milne ANT
v3.08 norm definition and Proposition 4.1, pp.68–69; no general theorem
is reproved. Mathlib coverage is not checked.

## Result and complete rejection criterion

All 1,572,651 pairs were screened and none passed. The 1774 saved
absolute norms have 1774 distinct outside-support factors. The full
partition and empty survivor list are in
`scripts/separated-eleven-unit/quotient-certificate.json`; reproduce with
`python3 scripts/separated-eleven-unit/check_quotients.py`.
The selected `/summary` was inspected in full with the shared JSON
inspector. There are no arithmetic failures or unresolved screened pairs.

Here is the precise reason this rejects every quotient in the declared
family, rather than merely failing to produce a sufficient certificate.
For each row write the nonzero integer absolute norm as

    |N_D/Q(z_i)|=2^a_i 11^b_i r_i,   gcd(r_i,22)=1,   r_i>0.

Norm multiplicativity gives the absolute norm of z_i/z_j as the ratio
of these numbers. This ratio is supported at 2 and 11 if and only if
r_i/r_j is so supported. Since numerator and denominator here are
both prime to 22, that is equivalent to r_i=r_j (reduce the fraction
to lowest terms). An actual S_D-unit has supported rational norm by
the principal-ideal norm formula, using positive residue degrees and
zero valuations outside S_D. Thus r_i!=r_j rigorously excludes the
quotient as an S_D-unit. This argument allows arbitrary cancellation
of outside ideals; no ideal support is inferred from norm support.
All distinct-index pairs have unequal r_i, so the necessary condition
fails throughout. Inversion gives the reciprocal norm and has the same
failure. Diagonal quotients are one and cannot separate parities.
Nor can directly applying the specified scalar correction rescue these
rejected pairs: for z=z_i/z_j, n=N_D/K(z) and u=z/n, norm transitivity
and [D:K]=3 give N_D/Q(u)=N_D/Q(z)^(-2). An outside prime with nonzero
exponent in the latter norm ratio retains a nonzero exponent after
multiplication by -2. Thus the corrected element also cannot be an
S_D-unit. This does not exclude more general products or other norm
corrections; it settles the declared quotient/correction strategy only.

The script reads the complete prior certificate, checks its fixed field
polynomials and candidate uniqueness, reconstructs every relative norm
from its actual affine coefficients and recomputes all 1774 absolute
norms as exact multiplication determinants. Each agrees with both
previously saved tower norms. It fully strips 2 and 11, rechecks each
saved factor/exponent pair, partitions the entire list and tests every
i<j. The independent partition count agrees with the pair count; all
groups are singletons. The certificate hashes the complete input file.
No quotient reached the inverse, scalar-correction or ordered-valuation
stage. Those checks were not performed and no unsupported stage is
claimed complete. The final replay script contains only the executed
screen and its checks.

Required certified separating units: one. Obtained: zero. L077's bound
remains fourteen versus required eleven; no class-kernel, rank or integer
conclusion follows. This is EXPLORATION, mathematical exploration usage
2/3, not a beyond-source advance or a universal obstruction. No lemma,
PROOF.md modification or DAG edge is warranted.

## Reassessment after two unproductive affine attempts

Stop the affine-element and affine-quotient mechanism, preserving
ATTEMPTS/034 and the new ATTEMPTS/035. Do not enlarge the coefficient
box or form longer products under a new name. The unchanged assessment
also covers supported-principal-ideal certificate attempts. A materially
different continuation is to fix just I=Q_8 R_8 in O_D, where Q_8 and
R_8 are respectively the degree-one and ramified degree-two maximal
primes over L041's base place k=8 modulo 11 (L073). Seek one exact
principal-generator certificate for this fixed ideal, then verify its
support, scalar norm correction and ordered parities. This is a proposed
certificate target, not an assertion that I is principal, that a generator
exists, or that its correction already meets the target. No ideal powers,
larger list, class-group completeness or parity conclusion is assumed.
A verified separating witness continues the route; failure to certify
this one ideal must retain its exact obstruction and cannot assert
nonexistence of other units. The localized class contribution and
primitive integer lifting remain unresolved.
