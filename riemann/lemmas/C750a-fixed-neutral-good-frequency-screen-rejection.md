# C750a: A fixed neutral witness rejects the coarse good-frequency screen

## Hypotheses

Put T=4log(3), I=(0,T). Use smooth zero extensions and the Fourier
convention F_f(t)=integral_I f(x)exp(-itx)dx. Define

    w(t)=Re psi(1/4+it/2)-log(pi)
         -2 sum_(2<=n<81) Lambda(n)n^(-1/2)cos(t log(n)),
    E={t in R:w(t)>=1},
    M=max(0,sup_(t in R)(-w(t))),
    Ncal={0!=f in C_c^infinity(I;C):
          integral_I exp(x/2)f(x)dx=integral_I exp(-x/2)f(x)dx=0},
    c_E=inf_(f in Ncal) integral_E |F_f(t)|^2dt
                         / integral_R |F_f(t)|^2dt.

All prime powers below 81 are retained. The delay log(81)=T has zero
overlap on supported tests. This is the complete neutral smooth symbol
of L744(6), after exact cancellation of its pole product; its Fourier
cosines represent the finite translation quadratic form on these tests.
No claim for arbitrary unsupported functions is needed.

Use L750's smooth construction, rescaled exactly as approved in
`drafts/literature/2026-11-13-neutral-good-frequency-fixed-witness-861.md`:

    eta(s)=exp(-1/s) for s>0, and 0 for s<=0,
    theta(s)=eta(s)/(eta(s)+eta(1-s)), delta=T/40,
    chi(x)=theta((x-delta)/delta)*theta((T-delta-x)/delta),
    phi_k(x)=chi(x)sin(k*pi*x/T), k=1,3,
    a= integral_I exp(x/2)phi_3(x)dx
       / integral_I exp(x/2)phi_1(x)dx,
    f=phi_3-a*phi_1.

The ratio defining a is exact. Its numerical enclosure does not define
an approximately neutral replacement. Named analytic inputs are
Plancherel's theorem and the digamma recurrence and sector-remainder
formulas specified below. The elementary outward interval implementation
assumes IEEE binary64 operations, no fast-math and no floating contraction.

## Conclusion

M is finite, f belongs to Ncal, and the real interval-box certificate gives

    2.60469 < ||f||_2^2 < 2.63863,
    integral_J |F_f(t)|^2 dt/(2*pi) > 0.10416,
    w(0) < -36.06981,

where the fixed rational set retained by the test is

    J=[-1/2,1/2] union [45/32,47/32] union [-47/32,-45/32]
      subset {w<1}.

In particular the following deliberately weaker rational statement holds:

    c_E <= 317/330 < 36/37 <= M/(M+1).                    (1)

Thus the strict screen c_E>M/(M+1) fails for this window and complete
symbol. This is REPRODUCTION: local specialization of a known witness
and validated-integration methods, not a discovery beyond the assessed
sources. It supplies no negative Weil energy, weighted observation
estimate, global assembly, Xi realization or RH conclusion. The separate
conceptual audit865 below accepts (1) under the stated arithmetic model.

## Proof

### Exact admissibility and the complete symbol

Flatness and smoothness of eta at zero, and the strictly positive
denominator defining theta, give the smooth cutoff used in L750.
Here chi is supported on [delta,T-delta], equals one on
[2delta,T-2delta] and is symmetric about T/2. Its support is compactly
contained in I. Both odd sine modes are symmetric about T/2. Since
phi_1 is nonnegative and strictly positive on an open subinterval,
its positive exponential moment is strictly positive. This also
follows from the certified lower bound below.

The exact definition of a gives M_+(f)=0. For either odd mode,
substitution x=T-y gives M_-(phi_k)=exp(-T/2)M_+(phi_k).
It follows that M_-(f)=0 exactly. On the plateau chi=1, the two
sine modes are linearly independent: dividing by sin(pi*x/T)>0,
their ratio is 3-4sin^2(pi*x/T), which is not constant there.
Thus f is nonzero, real and belongs to Ncal, which also permits
complex functions. A single real witness upper-bounds its infimum.

Write m(t)=Re psi(1/4+it/2)-log(pi). L744(8), using the cited
digamma remainder, gives

    |m(t)|<=A+log(2+|t|), A=2+8sqrt(2)/3+log(4*pi),
    |m(t)-log(|t|/(2*pi))|<=2/t^2 for |t|>=1.

For |t|<=1, m(t)>=-A-log(3). For |t|>=1,
m(t)>=-log(2*pi)-2>=-A-log(3). The arithmetic sum has absolute
value at most Cprime=2 sum_(2<=n<81) Lambda(n)/sqrt(n), which is
finite. Consequently 0<=M<=A+log(3)+Cprime<infinity. No numerical
global minimizer is used. The enclosure for w(0) below gives M>36.

### Validated spatial and Fourier integrals

The full certificate is `scripts/good-frequency/fixed-witness-863.json`,
produced by `scripts/good-frequency/fixed-witness-863.cpp`. The latter
includes the elementary interval implementation in
`scripts/corrected-ims/certificate-315.cpp` with its old main renamed
and never called. No old moment, norm, quadrature, energy or sign value
is imported. L750 Proof3 and its independent step317 audit justify that
implementation's elementary bounds. The present program also checks
that every reduced sine/cosine argument lies in [-4,4].

Every addition, subtraction, multiplication and division encloses its
real result by nextafter rounding. Positive logarithms use binary range
reduction and the atanh series; exponentials use a Taylor series after
range reduction and squaring; sine and cosine use reduced Taylor series;
pi uses Machin's identity. Square-root endpoints are checked by outward
squaring. The inherited absolute remainder allowances are respectively
2^-180 for the logarithm series, 2^-100 for the exponential base series,
2^-160 and 2^-150 for sine/cosine, and 2^-300 for arctangent.
For x<-100 the exponential range [0,4e-44] contains its true value.
There is no unvalidated special-function call in the certificate.

All integrations here use real interval boxes, rather than Simpson
remainders or analyticity across the flat joins. For an interval panel
[u,v], evaluating an integrand on the full panel gives a range [l,h]
and hence its integral belongs to (v-u)[l,h]. This is the monotonicity
of the integral, with no regularity beyond that of these smooth
integrands. See Johansson, *Numerical integration in arbitrary-precision
ball arithmetic*, arXiv:1802.07942v1 (22 February 2018), Section2,
callback contract and step2, [primary text](https://arxiv.org/html/1802.07942v1).
The analytic-ellipse branch is not used, so flat joins cause no omission.

Use s=x/T, with chi(Ts)=theta(40s-1)theta(39-40s). Partition [0,1]
into 32768 exact equal panels. Multiplying their whole-panel mode
ranges by exp(Ts/2), width 1/32768 and T encloses the exact moments:

    M_+(phi_1) in [9.295414377128647, 9.303227520914010],
    M_+(phi_3) in [4.135436274082027, 4.151305210060418],
    a in [0.44451629983093577, 0.44659711139663650].        (2)

These displayed binary64 endpoints are nearest-decimal renderings;
the rational enlargements used in (1) are strictly outside them.
Use 8192 spatial panels, with each full-panel f range evaluated using
the interval (2). Their squared ranges, summed with width T/8192,
give the norm enclosure

    N=||f||_2^2 in [2.604692568641510,2.638624687699511].   (3)

Correlation of a with the exact moments is not needed for these
enclosures: the one exact a belongs to (2), so independent interval
evaluation contains its integrands. Exact neutrality was proved before
using its enclosure.

For real t, symmetry gives F_f(t)=exp(-itT/2)G(t), where

    G(t)=integral_0^T f(x)cos(t(x-T/2))dx

is real. For each exact frequency panel K_j=[j/32,(j+1)/32], evaluate
cos(t(x-T/2)) on the full Cartesian product of K_j and each spatial
panel. Summing the resulting integral intervals encloses G(t) for
every t in K_j, simultaneously. Squaring that real range and
multiplying by 2/(32*2*pi) encloses the Fourier mass on K_j union
(-K_j). The factor two uses evenness of |F_f|^2. Adjacent panels
share endpoints only; the single endpoint at zero has measure zero.
The saved t endpoints are the exact nominal dyadic endpoints; the
internal evaluation boxes are enlarged outward and do not change
the integration lengths or count shared regions twice.

### Sublevel certification with the full prime sum

The program examines the panels in [0,16] in increasing order,
retaining only those with an interval upper bound for w strictly
below 1, and stops as soon as the approved rejection comparison holds.
This selects a subset of the bad set; it does not identify the whole
good set or optimize the witness. The retained indices are exactly
0,...,15,45,46, so their reflected union is J above. Every retained
upper bound for w is less than 0.086; the largest is below
0.085506 on [45/32,46/32]. Evenness of w certifies the negative panels.

For the digamma term the program uses z=1/4+it/2 and recurrence

    psi(z)=psi(z+256)-sum_(j=0)^255 1/(z+j),
    psi(Z)=log(Z)-1/(2Z)+R(Z),
    |R(Z)|<=sec^3(arg(Z)/2)/(12|Z|^2)<1/(4|Z|^2).

Here Re(Z)>0 and every recurrence denominator is nonzero. The sector
factor is retained using |arg(Z)|<pi/2. Thus the computed real
main term is enlarged by 1/(4|Z|^2), including the case t=0.
These are [DLMF5.5.2](https://dlmf.nist.gov/5.5.E2),
[5.11.2](https://dlmf.nist.gov/5.11.E2) and its
[complex remainder qualification in5.11(ii)](https://dlmf.nist.gov/5.11#ii),
in the version recorded in assessment861. A bare asymptotic truncation
would not suffice.

Trial division and integer powers produce exactly the following
31 nonzero prime-power weights:

    2,3,4,5,7,8,9,11,13,16,17,19,23,25,27,29,31,32,
    37,41,43,47,49,53,59,61,64,67,71,73,79.

For n=p^k the weight is log(p)/sqrt(n). Each is included with the
external factor two and its full cosine range. Their individual
intervals are in the certificate's prime_powers field. There is no
prime-only, first-shift or truncated-digamma approximation. In particular

    w(0) in [-36.069818986094134,-36.069811371577060].       (4)

The certificate records every retained panel's w range, centered
Fourier range and paired mass, and every skipped panel through the
stopping point. Summing the 18 paired masses gives

    B_J in [0.10416476087553357,0.13947032386036706].       (5)

Every retained range, all 31 prime-power records and the scalar
enclosures (2)-(5) were inspected in full, rather than inferred from
a JSON preview. The program's failure list is empty. There is no
frequency-tail estimate: Plancherel supplies total mass N exactly,
and only nonnegative bad mass is retained in the required direction.

### Comparison in the rejection direction

Since J subset E-complement, (3)-(5) and Plancherel imply

    p_E(f)=integral_E |F_f|^2 dt/(2*pi*N)
          <=1-B_J/N
          <=1-0.104/2.64
          =317/330.

The denominator uses an UPPER bound for N; the numerator uses a LOWER
bound for B_J. Equation (4) implies M>=36, so monotonicity gives
M/(1+M)>=36/37. Finally 317*37=11729<11880=36*330. Taking the
infimum over Ncal proves (1). The tighter computed one-sided upper
bound is 0.960523085621, compared with the certified lower threshold
0.973023871365. No upper bound for M is substituted in this rejection
direction.

For context only, the coarse lower form comparison is
E(f)/||f||^2 >= (M+1)p_E(f)-M. Rejecting a sufficient lower estimate
does not sign E(f) itself. Non-neutral poles, other windows, signed
weighting, global coverage and actual-Xi mixed positivity remain open.

Reproduction from the notebook directory:

```sh
clang++ -O2 -std=c++17 -ffp-contract=off scripts/good-frequency/fixed-witness-863.cpp -o /private/tmp/riemann-good-frequency-863
/private/tmp/riemann-good-frequency-863 > scripts/good-frequency/fixed-witness-863.json
```

The include causes a compiler warning about an implicit return in the
renamed, unused old main; that function is never invoked. The executed
main exits normally only after producing the full certificate. This
is an informal computational proof under the stated arithmetic model,
not an independent implementation or a formal proof.

### Independent conceptual audit — 14 November 2026, step865

The unchanged SPECIALIZE assessment audit863, separately approved864,
covers this exact audit. The proof above, L744(6)-(8), L750 Proof1/3
and its step317 audit, the executed wrapper and inherited elementary
source were inspected. Existing source coverage is reused; no new
positivity theorem is imported. The audit accepts (1), including its
complete-symbol interpretation, with no change of witness or bound.

**Exact domain and normalization.** Flatness of eta at zero and positivity
of eta(s)+eta(1-s) give a smooth compactly supported f. Reflection of
each odd sine mode gives exactly M_-=exp(-T/2)M_+, so the ratio of exact
integrals cancels both moments. Positivity of M_+(phi_1) and nonconstant
sin(3u)/sin(u) on the plateau justify admissibility independently of
the certificate. Numerical a is an enclosing interval, never the
definition of f. For the Fourier convention used here, Plancherel
identifies the real part of the overlap at delay log(n) with the cosine
integral divided by 2pi. Thus L744(6) gives precisely the coefficient
-2log(p)/sqrt(n) for n=p^k; neutrality removes exactly the pole product.
No delay n>=81 has nonzero overlap, including the boundary delay 81.
No unsupported test class or assumed positive form enters this step.

**Actual arithmetic domains.** The nonmutating guards and replay are
reproducible with `python3 scripts/good-frequency/audit-865.py`.
The generated `instrumented-865.cpp`, `domains-865.json`, `replay-865.json`
and `audit-summary-865.json` are all in `scripts/good-frequency/`.
The instrumented output equals the original certificate in every field.
All intervals stayed finite and ordered, divisions stayed away from zero,
and binary64 round-to-nearest, preserved subnormals and exact binary
range-reduction scalings passed. Compilation uses -ffp-contract=off
without fast-math. The inherited old main and its FFT, Simpson and
derivative-jet machinery are not executed by this witness.

The largest reduced trigonometric modulus is 3.2000299090497326<4;
the largest arctangent modulus is 0.20000000000000007<1/4; reduced
exponential modulus is at most 0.12499999999999961<1/8; logarithm
base arguments stay in [1,2]. Integer selection of a trigonometric
period need not be correctly rounded: any chosen integer is valid
once its interval subtraction contains the exact multiple of 2pi
and the resulting whole interval meets the checked Taylor domain.
Machin's formula and its interval arctangents enclose pi. Square-root
endpoint squaring checks validate both endpoints, with sqrt used only
as a starting guess. Clamping theta to [0,1] and squared mass to a
nonnegative lower endpoint is valid for the actual functions.

Exact rational checks reproduce all five remainder comparisons in
L750(9). They also check the binary64 constant stored as 4e-44:
that exact positive rational times sum_(j=0)^256 100^j/j! exceeds 1.
Since that positive partial sum is below exp(100), the early return
[0,4e-44] encloses exp(x) for every x<-100. All 264 such calls are
covered; the actual exponential inputs range from about -2048.000001
to 2.197225. The Taylor error proof does not rely on agreement with
a sampled special-function implementation.

Every one of the 48 symbol calls uses the shift 256. For Z=256+1/4+it/2,
Re(Z)>0 and |arg(Z)|<pi/2, while each recurrence denominator has
real part at least 1/4. The cited DLMF remainder is bounded by
(2sqrt(2)/12)/|Z|^2<1/(4|Z|^2). The code encloses Re log(Z) as
log((Re Z)^2+(Im Z)^2)/2 and Re(1/Z) by its real rational expression,
then uses the interval upper bound on that last remainder. The small
negative outward endpoint -2^-1074 in the frequency evaluation at zero
does not violate this right-half-plane argument. No real-axis-only
remainder or uncharged recurrence tail is used.

**Whole-panel mass and complete records.** The exact spatial variable
s ranges over nominal dyadic panels; their inflated evaluation intervals
contain every true point. Multiplication by the enclosing T and nominal
panel width encloses the actual integral, including for signed ranges.
It does not integrate the enlarged interval. Both mode evaluations may
forget their dependence on a or T without losing containment. Centering
at T/2 removes the odd imaginary integrand by the exact reflection
symmetry. Hence the real full-panel G range can be squared for every
frequency in that nominal panel. The factor 2/(32*2pi) accounts for
the reflected pair exactly once; shared endpoints have measure zero.

All 18 retained records, all 29 skipped records, all 31 prime-power records
and all scalar bounds were inspected in full. Independent integer
factorization checks each base p and n=p^k exactly once. Retained
indices are 0 through 15, 45, 46, and every upper symbol bound is below 1
(the maximum is 0.08550545708377989). The skipped cells need no sign
conclusion: they are omitted from a lower bound on bad mass. Exact
rational checks of every stored Fourier range, nominal paired width,
pi interval and squared-mass enclosure pass; the accumulated bad-mass
interval contains the sum of those per-panel interval endpoints.

**Sided comparison and verdict.** Exact binary-rational comparison gives
b>13/125, N_upper<66/25 and -w(0)_upper>36. The computed U upper bound
and threshold lower bound enclose 1-b/N_upper and m0/(1+m0) in the
correct directions, and all 23 audit checks pass. Taking the infimum
over neutral f can only decrease p_E(f). Therefore (1) follows with
317/330<36/37, as already proved above. M's global finiteness uses
L744(8), not a finite frequency search; Plancherel pays the entire
Fourier mass, so there is no missing frequency tail. This verifies a
local obstruction to the strict coarse screen, not a negative-energy
test or global impossibility theorem. The replay uses the same
arithmetic implementation with independent rational/factorization
checks; it is not an independent numerical library or Lean proof.

## Mathlib

Full matching Mathlib coverage of this complete-symbol constrained
mass certificate has not been checked; no absence claim is made.
Plancherel, integral monotonicity and the cited digamma identities
are the standard analytic inputs. No Lean verification is claimed.
