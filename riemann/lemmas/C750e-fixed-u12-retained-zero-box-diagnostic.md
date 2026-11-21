# C750e: Fixed U12 retained-zero box diagnostic is inconclusive

## Hypotheses

Use T=4log3, delta=T/40, chi and phi_k from C750a, and exactly the ten
complex coordinates e_(p,j) in C750c Proof5/(15), ordered p=1,2 and
j=1,...,5. All moments and projections are exact integrals and original
L2 projections. Put f=sum c_(p,j)e_(p,j), c in C^10, and use the
Euclidean norm of these original coefficients. Reuse L753's audited
time-zero identity and L018's zero coordinates/multiplicities. Import
the already audited C750d bound at H=3000000000000, without reproof:

    |R_H(c)|<=epsilon_* ||c||_2^2,
    epsilon_*=4550000000015183/28125000000000000000000000000000.

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-11-14-neutral-finite-subset-gram-879.md`, completed
in review880. This is one REPRODUCTION calculation using its published
coarse intervals, not a new positivity result or a new zero computation.

The external computational input is the ten isolated simple Hardy-Z
roots printed for `real_roots 0 0.0 50.0 -verbose` in the
[Arb2.23.0 real_roots example](https://arblib.org/examples.html#real-roots-c).
The exact table and source/flag comparison are in assessment879. Use the
[root-isolation contract](https://arblib.org/arb_calc.html#subdivision-based-root-finding),
the [pinned example](https://raw.githubusercontent.com/fredrik-johansson/arb/2.23.0/examples/real_roots.c)
and [pinned isolator, flag1 and verbose cases](https://raw.githubusercontent.com/fredrik-johansson/arb/2.23.0/arb_calc/isolate_roots.c).
This is a cited computational input, not an independently replayed root
certificate. Hardy-Z conversion uses [DLMF25.10.1](https://dlmf.nist.gov/25.10.E1),
Titchmarsh, second edition1986, equation4.17.2, p89.
The [pinned interval printer](https://raw.githubusercontent.com/fredrik-johansson/arb/2.23.0/arb_calc.h)
and [arf faithful-rounding contract](https://arblib.org/arf.html#input-and-output)
require outward transport of printed endpoints; they do not justify
assuming those endpoints equal the internal ones.

For omission through H import Platt--Trudgian, *The Riemann hypothesis
is true up to 3 times10^12*, [2004.09765v1, Theorem1 and Section2, p2](https://arxiv.org/pdf/2004.09765v1).
The theorem reaches3000175332800>H. For height zero use
[DLMF25.2.3](https://dlmf.nist.gov/25.2.E3), Apostol1976, equation27,
p292, and the alternating-series test as specialized below. Neither
source asserts RH at unbounded height.

The numerical qualification is IEEE binary64 round-to-nearest with
subnormals, outward nextafter interval operations, no fast-math and no
floating contraction. Elementary functions reuse
`scripts/neutral-exact-schur/elementary-875.hpp` with its finite-series
remainders and runtime domain guards, as justified in C750c Proof3-5.
Complete moment/Gram intervals are reused from
`scripts/neutral-exact-schur/certificate-875.json`, with their original
65536-subinterval Simpson remainder and rounding semantics intact.
Only those input intervals are reused; no old energy or sign is used.

## Conclusion

The one prescribed whole-box evaluator fails to certify a retained Gram
margin above epsilon_*. All100 projected sample intervals contain zero;
all120 raw sample intervals also contain zero. Each sector's Gram entry
boxes admit the zero matrix. The shifted interval LDL tests stop at
their first pivots, with outward enlarged enclosures

    [-1.617777777783177e-16, 1.853448647923949],
    [-1.617777777783177e-16, 2.893604309841618].           (1)

This is an informative stop for this fixed box certificate, which is
parked without data/root refinement, precision retry or window/mode
change. It establishes no negative exact form, singularity, failure of
the ten actual roots to suffice, or failure of RH. The uncertainty-box
zero samples are not claimed to be attainable by actual roots. No
finite positive compression or infinite-complement estimate is proved.
This known-method diagnostic has not had an independent conceptual audit.

## Proof

### Exact coordinates and the comparison that would suffice

C750c Proof1/5 proves both moments of every e vanish, including over C,
and proves its exact basis and original-L2 projection statements.
Write the Fourier transform as in L753. Let gamma_1,...,gamma_10 be
the ten distinct positive roots in the admitted, disjoint transported
intervals. They are simple by the isolation input and are below H.
The retained sum is

    G(c)=sum_(r=1)^10 (|F(gamma_r)|^2+|F(-gamma_r)|^2).  (2)

For each real ordinate t, F#(t)=conj(F(t)), for arbitrary complex f.
Thus all omitted zeros with 0<|height|<=H contribute nonnegative
modulus squares by the cited verified-height theorem. Both signs and
all multiplicities are included; subtract each retained simple zero
once. Additional zeros/multiplicities remain in the omitted part, and
no complete finite census is needed. Endpoint zeros at H would also
have nonnegative contributions: the verified range strictly exceeds H.

There is no height-zero nontrivial zero. Indeed for real 0<s<1 the
alternating numerator eta(s)=sum_(n>=1)(-1)^(n-1)n^(-s) is positive:
its even partial sums are sums of positive pairs and are at least
1-2^(-s)>0; the alternating-series test gives their limit. DLMF25.2.3
gives zeta(s)=eta(s)/(1-2^(1-s)), whose denominator is strictly negative.
L018 confines nontrivial zeros to this open strip. This is an elementary
specialization of the cited formula, not an extra zero-free theorem.

L753 supplies absolute convergence, so the retained, omitted-through-H
and strictly-above-H parts can be split without an ordering ambiguity.
Use modulus squares only through H. Above H retain the possibly nonreal
products F(z)F#(z), paid absolutely by C750d. Consequently

    E(f)>=G(c)-epsilon_*||c||_2^2.                      (3)

A retained Gram lower margin strictly above epsilon_* in these exact
coordinates would suffice for positive E on this finite space. It would
not establish an infinite complement, non-neutral signs, all-degree
mixed positivity or global assembly. Those independent gaps remain.

### Complex pairing and exact reflection blocks

The p=1 basis functions are real symmetric about T/2; the p=2 functions
are real antisymmetric. C750c proves projection preserves these parities.
For a symmetric basis function define the real amplitude

    A_e(t)=integral_0^T e(x)cos(t(x-T/2))dx.

For an antisymmetric basis function define

    B_e(t)=integral_0^T e(x)sin(t(x-T/2))dx.

Reflection cancels the other integral exactly. Hence
F_e(t)=exp(-itT/2)A_e(t) in the first sector and
F_e(t)=-i exp(-itT/2)B_e(t) in the second. A_e(-t)=A_e(t) and
B_e(-t)=-B_e(t). Put a=sum_j c_(1,j)A_(1,j)(t) and
b=sum_j c_(2,j)B_(2,j)(t), which may both be complex. The two signs give

    |a-ib|^2+|a+ib|^2=2|a|^2+2|b|^2.

Thus (2) has two real symmetric five-by-five blocks

    G_p=2 sum_(r=1)^10 v_(p,r) v_(p,r)^t,              (4)

where v_1 contains the A amplitudes and v_2 the B amplitudes. Cross-sector
entries vanish exactly after pairing, including for complex coefficients.
The ten-coordinate coefficient norm in (3) is unchanged. This is not
an L2-normalized eigenvalue comparison.

### One fixed integration workload and complete finite uncertainties

Before calculation, `drafts/2026-11-14-neutral-finite-subset-work-881.md`
fixed binary64 arithmetic and32768 equal full-window panels. Reflection
reduces the actual work to16384 panels on 0<=s=x/T<=1/2. On each exact
dyadic s panel evaluate

    chi(Ts)=theta(40s-1)theta(39-40s),
    phi_k(Ts)=chi(Ts)sin(k*pi*s),
    cos(t*T*(s-1/2)) for odd k,
    sin(t*T*(s-1/2)) for even k.

Multiply the full-panel interval ranges and sum, with factor2T/32768.
The integrands are symmetric about1/2 after the indicated parity choice,
so this encloses the full-window amplitudes. For every panel and every
t in the whole transported root interval, its integral lies between
panel width times the lower and upper range. This is the direct-box
case of Johansson, *Numerical integration in arbitrary-precision ball
arithmetic*, [1802.07942v1, Section2, callback contract and step2](https://arxiv.org/html/1802.07942v1#S2).
No complex analyticity across cutoff joins or point-value quadrature
accuracy is assumed. T, pi, cutoff values, oscillatory factors and all
rounding are enclosed. The elementary trigonometric reduction subtracts
an integer multiple of the interval2pi; its guarded reduced arguments
remain within[-4,4], the finite-series domain, even though unreduced
phases are larger. No uncertified system trigonometric function is used.

The published endpoints have size between10 and50 and were printed to
15 significant digits. The faithful rounding allowance is at most
10^-13 per endpoint. Transport each printed endpoint outward by the
larger exact allowance10^-12, with its binary division/rounding enclosed.
The shortened strings themselves are dyadic, and their binary64 values
are exact. The actual outward frequency intervals, all120 raw amplitudes,
all100 projected amplitudes and both complete Gram blocks are saved in
`scripts/neutral-finite-subset/certificate-881.json`. This uses the ten
coarse intervals only, without refinement or replacement.

Reconstruct each exact moment ratio and each two-by-two original-L2
projection from the complete saved moment/Gram intervals of875. Copying
their endpoints in hexadecimal into `inputs-881.hpp` preserves their
binary64 values exactly. Denominators and projection determinants are
checked away from zero. The exact functions are defined by the integrals,
not by midpoint moment values. Linear combination of the raw amplitudes
with the enclosing coordinates covers moment, ratio and projection
uncertainty. Apply (4) with interval multiplication and interval squares
on the diagonal. Thus every finite-input, integration and arithmetic
error is already included in the resulting entry boxes; no missing
quadrature or moment-error term is set to zero.

### Error norms, thresholds and the failed tests

Let M be the rational midpoint matrix of one saved interval block and
R its entrywise radius matrix. An actual Hermitian G in the boxes obeys
||G-M||_2<=max_i sum_j R_ij: symmetry makes the row and column bounds
equal, and ||D||_2<=sqrt(||D||_1||D||_infinity). Gershgorin bounds the
least eigenvalue of M below by min_i(M_ii-sum_(j!=i)|M_ij|). These named
finite-dimensional bounds import no sign information. Subtract the
entire error norm, then compare with epsilon_* as required by (3).
The exact-rational checker gives the following outward-enlarged values:

| sector | finite matrix error norm upper | fully paid lower bound | required strict lower |
| --- | --- | --- | --- |
| symmetric | <7.358417468407717 | >-7.096955617726796 | epsilon_*>1.617777777783176e-16 |
| antisymmetric | <10.672793713144083 | >-10.566177573596788 | same epsilon_* |

The negative lower estimates do not imply negative eigenvalues. As a
second standard sufficient test, perform natural-order interval LDL on
G_p-epsilon_*I, stopping before division by any pivot overlapping zero.
Both tests stop immediately at (1). In addition all50 sample boxes per
sector contain zero, so their product uncertainty model admits the zero
samples, and all Gram entry boxes admit the zero matrix. These boxes
therefore cannot alone certify a positive uniform margin. This is a
loss of information by interval enclosure; it is not a proof that zero
samples or zero Gram are attainable at the actual ten ordinates.

Reproduce the single workload and its independent rational accounting:

```sh
clang++ -O2 -std=c++17 -ffp-contract=off scripts/neutral-finite-subset/certificate-881.cpp -o /private/tmp/riemann-neutral-subset-881
/private/tmp/riemann-neutral-subset-881 > scripts/neutral-finite-subset/certificate-881.json 2> scripts/neutral-finite-subset/run-881.log
python3 scripts/neutral-finite-subset/check-881.py
```

All177 exact-rational accounting checks pass: original coordinates,
projection determinants, all100 sample combinations, all50 Gram entries,
transport allowances, disjointness/cutoff and the unchanged tail constant.
The full rational bounds, pivots and explicit positivity failures are
in `scripts/neutral-finite-subset/check-881.json`, including the source
certificate hash. This checks accounting, not an independent integration
implementation or a conceptual audit. No positive or negative exact
energy, exact singular kernel or candidate RH resolution is claimed.
The prescribed fixed test is finished; no rescue retry is authorized.

## Mathlib

Full matching coverage of this supported Weil-form specialization and
numerical diagnostic has not been checked. Finite Hermitian Gram matrices,
the spectral theorem, Gershgorin/induced-norm bounds, interval integration
and the positive-definite LDL criterion are supporting mathematics; no
complete Mathlib theorem or formally checked numerical certificate is
claimed. Imported analytic inputs retain the hypotheses stated above.
