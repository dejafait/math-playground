# Lemma 456: lower-band fixed-circle freezing obstruction

## Hypotheses

Assume the zeta specialization of OpenAI, *The Quasi-Riemann
Hypothesis: A Zero-Free Half-Plane Re s > 7/8*, September 30, 2026,
Theorem 1.1, at commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a`.
Retain the [external-input register's qualifications](../foundations/2026-10-quasi-riemann-input.md):
the pole at 1 is allowed, the boundary is not excluded, and the
manuscript and formal import closure have not been independently
audited here. No stronger boundary or RH premise is used.

Let r tend to infinity through positive reals, m be a positive even
integer, and set

    7/8 <= alpha=m/r <= 31/32,
    h=9/2+m/(2r), a=sqrt(4*pi^2*exp(4r)-h^2)>0,
    c=m/(2r), sigma=1/2+c, A=m!/(2r)^m,
    S=sum_{j,k>=1}(jk)^(-1/2)(1-log(jk)/(2r))_+^m
                                      exp(ia log(k/j)),
    B=|zeta(sigma+ia)|^2, delta=1/8.

For the certificate obstruction, consider the following particular
method. Fix a real center b>1 independently of height. Use concentric
disks about b+it with radii

    0<R0<R1<R2<R3<b-7/8, R0<b-1,

an Euler-normalized logarithm bounded by O(1) on R0, and an
O(log t) bound on R2 obtained by Borel--Caratheodory on R3.
Reserve a fixed positive Cauchy radius rho about 15/16+it by
requiring R1>=b-15/16+rho. The tested interpolation exponent is

    theta=log(R1/R0)/log(R2/R0).

## Conclusion

On the complete changed band, uniformly for sufficiently large t,

    |log zeta(sigma+it)| <= C(log t)^(2/3),
    |zeta'/zeta(sigma+it)| <= C(log t)^(2/3),           (1)

where the logarithm is the normalized analytic branch constructed
below. In particular

    exp(-Cr^(2/3)) <= B <= exp(Cr^(2/3)).              (2)

The full arithmetic sum has the exact identity

    S=integral_R K(v)F(v)dv+Rp, integral_R K(v)dv=1,
    K(v)=A exp(2r(c+iv))(c+iv)^(-m-1)/(2*pi),
    F(v)=zeta(sigma+i(a+v)) zeta(sigma+i(v-a)),
    Rp=2A Re[exp(2r(1/2+ia))(1/2+ia)^(-m-1)
                                             zeta(1+2ia)]. (3)

All integrals in (3) converge absolutely. Both poles are retained.
Writing Ecentral=integral_{|v|<=delta} K(v)(F(v)/B-1)dv,

    S/B-1=Ecentral+Erest,
    |Erest| <= C exp(-r/512+Cr^(2/3))+2exp(-r^2).     (4)

Thus the non-Euler normalization, both residues and all relative
tails can be controlled; the central comparison is unresolved.
If M=sup_{|u|<=delta}|zeta'/zeta(sigma+i(a+u))| and
p=M/sqrt(r), its magnitude certificate is

    |Ecentral| <= C p integral_R |w|exp(-w^2/4+2p|w|)dw. (5)

The available (1) gives only p=O(r^(1/6)); it does not verify
p=o(1), or even p<=1 eventually. It cannot be substituted into
L330's conditional small-p conclusion.

Moreover every fixed-disk configuration in the Hypotheses satisfies
theta>1/2 at the closed endpoint alpha=7/8. Hence no choice of
these fixed radii and fixed real center obtains the sufficient
fixed power theta<1/2. This is a failure of this certificate, not
a lower bound for the actual M, an actual relative error, or S.
No negative arithmetic value, positive sign band or RH consequence
is proved. This local known-method calculation has not received a
separate critical audit of all its conclusions; no originality is claimed.
The separate audit recorded in L457 validates the full logarithm disk
and inversion used there, without auditing this fixed-center obstruction.

## Proof

The prior [lower-band assessment](../drafts/literature/2026-10-23-lower-band-relative-mellin-coverage.md)
authorizes precisely this threshold test. The source mechanism is
Titchmarsh--Heath-Brown, *The Theory of the Riemann Zeta-function*,
second edition (1986), Theorem 14.2 and proof, pp. 336--337, and
Section 14.3, pp. 338--339, as already inspected and specialized in
L452. Its printed RH hypothesis is not assumed here. Only named
Borel--Caratheodory, Hadamard three-circles and Cauchy inequalities
are reused, with new disks checked below. Inversion uses the L303
mechanism and [DLMF 1.14.20](https://dlmf.nist.gov/1.14.E20);
the pole and Stirling inputs are [DLMF 25.2](https://dlmf.nist.gov/25.2)
and [DLMF 5.11.3](https://dlmf.nist.gov/5.11.E3). The necessary
changed-domain argument is given rather than importing L452's
old derivative conclusion outside its strip.

**Normalized logarithm and complete domain.** Here c lies in
[7/16,31/64], sigma in [15/16,63/64], and
log a=2r+log(2*pi)+O(exp(-4r)) uniformly, since h is bounded.
Take the center 2+it and radii, in units of 1/256,

    R0=255/256, R1=273/256, R2=284/256, R3=286/256.

The R3 disk has minimum real part 226/256>7/8, and for large
positive t misses the pole. It has a slightly larger zero-free,
pole-free disk as a neighborhood. Normalize its analytic logarithm
f_t at the center using L452's Euler logarithm on Re s>1. The
whole R0 disk has real parts at least 257/256>1, so connectedness
and the center normalization identify f_t with that bounded Euler
logarithm there. On R3, L452's proved fractional-part formula gives
|zeta(s)|<=Ct uniformly. Borel--Caratheodory on R3 and R2,
whose gap is 2/256, gives max_{R2}|f_t|<=C log t.
Three-circles consequently bounds max_{R1}|f_t| by C(log t)^theta.
The exact integer comparison

    273^3=20346417 < 20567280=255*284^2

proves theta<2/3. For every sigma in the required strip,
|2-sigma|<=272/256; its radius-1/256 Cauchy circle therefore
fits R1, including equality. Cauchy's estimate proves the second
bound (1), and the logarithm bound proves its first. Constants
are uniform in sigma and t; derivatives of different branches agree.
Taking real parts gives both modulus bounds (2), and the same
exp(+-Cr^(2/3)) bounds at every positive height in [a/2,3a/2].
No reciprocal Euler series at sigma<1 is used.

For every real t, including zero, the formula proved in L452,

    zeta(s)=s/(s-1)-s integral_1^infinity {u}u^(-s-1)du,

gives |zeta(sigma+it)|<=C(1+|t|). Indeed sigma>=15/16
and |sigma+it-1|>=1/64. This is also the growth input for contours.

**Full inversion and residues.** Apply scalar inversion at
2r-log(jk) on Re z=1, as in L303. Its full Fubini majorant is
A exp(2r) zeta(3/2)^2/(2*pi) times the finite integral of
(1+v^2)^(-(m+1)/2). Thus it yields the full sum S, including
its zero weight when jk=exp(2r). Shift the resulting vertical
integral to c. For fixed parameters and T>2a+2, the preceding
growth formula bounds the product on horizontal edges by O_a(T^2).
Their integrals are O_{r,m,a}(T^(1-m)), tending to zero; m>=6
eventually uniformly. On the shifted line the product is
O((1+a+|v|)^2), giving absolute integrability for m>2.
Only z=1/2+ia and z=1/2-ia are crossed, with unit zeta pole
residue; their contributions are conjugates and sum to Rp in
(3), with a plus sign. Zero is not crossed. Scalar inversion
alone at 2r on the positive line c gives integral K=1.
These fixed-parameter limits precede all uniform estimates.

**Kernel and every relative tail.** Rechecking L454's modulus
calculation uses only 2rc=m and the compact positive c interval.
Positive-real Stirling gives

    |K(v)|=P0(1+(v/c)^2)^(-(m+1)/2), P0<=C sqrt(r).

For |v|<=c, log(1+(v/c)^2)>=v^2/(2c^2) yields
|K(v)|<=C sqrt(r)exp(-rv^2/4), since m=2rc and c<1/2.
For |v|>c, split off 2^(-m/4); the remaining power has a
uniform integrable majorant for m>=6. Hence integral |K|<=C,
and splitting the inner Gaussian into two factors gives

    integral_{|v|>delta}|K(v)|dv<=C exp(-r/512).

The outer mass fits this estimate because (7/32)log 2>1/512.
For delta<|v|<=a/2 both absolute shifted heights lie in
[a/2,3a/2]. Equation (1), conjugation and (2) therefore give
|F/B-1|<=C exp(Cr^(2/3)). This proves the first term in (4).

For |v|>q=a/2>=1, including the neighborhoods of v=+-a,
the all-height growth bound gives |F(v)|<=Cv^2, while c<1
gives |K(v)|<=C sqrt(r)|v|^(-m-1). The complete relative
integral of |K|(|F|/B+1) is at most

    C sqrt(r)exp(Cr^(2/3))
           [q^(2-m)/(m-2)+q^(-m)/m] <= exp(-r^2)

eventually: log q=2r+O(1), m>=7r/8, so its logarithm is
at most -(7/4)r^2+O(r)+O(r^(2/3))+O(log r).
Finally A<=1 since m!<=m^m and c<1. The all-height growth
formula at 1+2ia gives |zeta(1+2ia)|<=Ca; thus the sum of
both relative residue moduli is at most
C exp(r)a^(-m)exp(Cr^(2/3))<=exp(-r^2), by the same
quadratic exponent. This proves (4) without discarding either
pole or applying a large-height bound at shifted height zero.
There is one common onset for all these uniform inequalities.

**The unresolved central term.** Nonvanishing and differentiation
of F(v)/B, with value one at zero, give for |v|<=delta

    F(v)/B=exp(i integral_0^v [g(sigma+i(a+u))
                                      +g(sigma+i(u-a))]du).

Conjugation bounds each summand by M, and therefore
|F/B-1|<=2M|v|exp(2M|v|). The Gaussian bound and the
substitution w=sqrt(r)v give (5), exactly the integrated
variation mechanism of L330. It holds for every finite p, but
its usual small-error conclusion requires p=o(1). The envelope
from (1) gives only p<=Cr^(1/6), which grows. For example,
the integral in (5) is at most C(1+p)exp(4p^2), by completing
the square separately on each half-line. Substitution of that
envelope gives a bound of the form C exp(Cr^(1/3)), not o(1).
Neither this upper envelope nor the fact that it grows establishes
anything negative about the actual central term. L330's exact
zero-free paired model independently explains why an O(sqrt(r))
magnitude estimate alone would still not imply relative freezing;
its endpoint model is not transplanted as an actual-zeta example.

**All fixed real centers.** Put d=b-1>0. For the prescribed
certificate at sigma*=15/16,

    R0<d, R2<d+1/8, R1>=d+1/16+rho,
    (d+1/16)^2-d(d+1/8)=1/256>0.

Thus R1^2>R0 R2. Taking logarithms gives
2 log(R1/R0)>log(R2/R0), and theta>1/2. Even if all radius
margins and rho tend to zero for a fixed center, the limiting
exponent is bounded below by

    log((d+1/16)/d)/log((d+1/8)/d)>1/2.

Indeed the ratio decreases when R0 or R2 increases and increases
when R1 increases. Moving the center to infinity makes this
lower bound tend to 1/2; it does not give a fixed exponent below
1/2. Height-dependent centers and margins would also change all
growth, Euler, Borel--Caratheodory and Cauchy constants, and are
not decided by this fixed-parameter argument. Nonconcentric or
strip interpolation and a complete moving-saddle comparison are
also outside this obstruction. The exact closed endpoint belongs
to the target domain (take r=8m/7 for even m), so it cannot be
removed by rounding or by an interior-band argument.

The explicit exponent check and disk margins are certified by
`python3 scripts/lower-band/check_fixed_circle_threshold.py`, writing
`scripts/lower-band/fixed-circle-threshold-certificate.json`.
That exact finite arithmetic checks the displayed constants, not
the analytic proof, source premise, or actual values of S.

## Mathlib

Matching coverage for this full lower-band bound, relative-tail
specialization and certificate obstruction has not been checked;
absence is not asserted. Supporting Borel--Caratheodory,
three-circles, Cauchy, inversion, residue and Stirling APIs were
not checked here. L452 records its supporting Euler-log theorem
and the external artifact `OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re`;
the artifact is not asserted to be locally built or part of Mathlib.
