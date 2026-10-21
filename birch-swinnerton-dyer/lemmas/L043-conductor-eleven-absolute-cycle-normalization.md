# L043 — Conductor-eleven normalization from full absolute cycles

## Hypotheses

Let E/Q be the minimal curve y^2+y=x^3-x^2-10x-20, with
[a_1,a_2,a_3,a_4,a_6]=[0,-1,1,-10,-20], conductor N=11 and
Delta=-11^5. Let f=sum a_n exp(2 pi i n z) be its normalized newform,
omega_E its minimal differential, and Omega(E)=integral_E(R) |omega_E|
the total real period. Use L039's audited arithmetic, complete integral
relative presentation M, twelve oriented generators g_0,...,g_11, and
integral quotient coordinates (e_1,e_2,e_3). Use its full-relative line

\[
I(\{\alpha,\beta\})=\operatorname{Re}\left(2\pi i\int_\alpha^\beta f(z)\,dz\right)
=\beta\phi(\{\alpha,\beta\}),\qquad
\phi=(5/2,5,1),\quad \beta\ne0.
\]

Apply L038's complete integral relative identification to L039's lattice
witnesses, and L029's full-relative line criterion to L039's arithmetic,
operators and exact dual kernel. These applications are already audited
in L039 and are reused here; no absolute-only or rational-lattice
replacement is made. Use only L040's published exact-model optimality import: the model
is 11a1 and is the X_0(11)-optimal quotient. Retain that published
complete-isogeny-class/two-period computational qualification. Neither
L040's twist ratio nor L041's normalization is a recovery premise.
Use L028's oriented symbols and integral-generator denominator convention.
For its downstream ordinary application, p>=5 is good ordinary and p!=5.

New evidence is `scripts/conductor-eleven/absolute-cycles/certificate.json`.
The separate full arithmetic replay is adjacent `verification.json`;
fresh complete L039 structural/dual replay is in `upstream-replay/`.
Reproduce from the notebook root:

```bash
python3 scripts/conductor-eleven/absolute-cycles/build_certificate.py
python3 scripts/conductor-eleven/absolute-cycles/verify_certificate.py
```

These are fixed-instance witnesses, not a universal software theorem.
The separate critical audit of the assembly and programs passes below. No rank,
Sha, central/twist nonvanishing or coefficient hypothesis is assumed.

## Conclusion

In this entire integral relative lattice, the boundary is
delta(x_1,x_2,x_3)=x_3([0]-[infinity]). Hence

\[
H_1(X_0(11),\mathbf Z)=\ker\delta
=\mathbf Z e_1\oplus\mathbf Z e_2,\qquad
\phi(\ker\delta)=(5/2)\mathbf Z.
\]

The primitive image functional is (2/5)phi on this full absolute kernel.
An independently oriented period enclosure for gamma={0,-1/2} is

\[
I(\gamma)\in
\frac{[-357250659363083,-357250659362982]}{281474976710656}
\subset(-\infty,0),\qquad \phi(\gamma)=-5.
\tag{1}
\]

Consequently beta>0 and the exact full-relative normalization is

\[
F=I/\Omega(E)=\phi/5.
\tag{2}
\]

All twelve generator values are

\[
(-1/5,1/5,0,1,1/2,-1/2,-1,-1,-1/2,1/2,1,0).
\tag{3}
\]

Their least common denominator is 10=2*5. Thus C=0 in L028/L027's
convention for every retained p; in particular v_p(F({infinity,r}))>=0
for every rational r. This supplies the already-known fixed-model
normalization by a different, twist-free production mechanism. It is
known-algorithm reproduction, not progress beyond the cited mathematics
or a new BSD case. It supplies no nonzero coefficient, rational point,
uniform optimality/normalization procedure or arbitrary-curve rank equality.

## Proof

**Imported homology and arithmetic inputs.** Import Stein, *Modular
Forms, a Computational Approach*, GSM 79 (2007),
[equation (3.2.1) and Theorem 3.7, p.40](https://wstein.org/books/modform/stein-modform.pdf#page=54).
At weight two the entire torsion-free integral relative module identifies
with relative homology, and the boundary kernel with integral absolute
homology. Boundary orientation is [end]-[start]. L038/L039's complete
presentation meets these hypotheses; every integral quotient coordinate,
source relation and saturated relation is retained.

Import Cremona, *Algorithms for Modular Elliptic Curves*, corrected
second edition (1997),
[Proposition 2.2.3, pp.16--17](https://johncremona.github.io/book/fulltext/chapter2.pdf#page=10).
For reduced p_j/q_j, its condition (2) is equivalence precisely when
q_2=u q_1 modulo N and u p_2=p_1 modulo gcd(q_1,N), for a unit u
modulo N. This includes infinity=(1,0). At prime N=11 every cusp is
equivalent to zero=(0,1) when 11 does not divide q: take u=q^(-1)
modulo 11, and the second condition is modulo one. Otherwise p is a
unit and the cusp is equivalent to infinity by u=p modulo 11. The two
classes are distinct, since equivalence from zero to infinity would
require 0=u modulo 11. This proves completeness of the two cusp classes,
not merely a classification of the saved endpoints.

L039 independently proves minimality, conductor, multiplicative reduction
at 11 and modularity of this exact model. For Fourier coefficients import
Cremona's same book,
[Section 2.6, pp.24--26, prime-power recurrences and Euler factors](https://johncremona.github.io/book/fulltext/chapter2.pdf#page=18).
At good primes use a_p=p+1-#E(F_p); at the multiplicative prime use the
nodal count, giving a_11=1. Prime powers obey
a_(p^k)=a_p a_(p^(k-1))-p a_(p^(k-2)) for p!=11 and a_(11^k)=1;
coprime coefficients multiply. These are imported, not inferred from a
finite numerical bound or from the previously computed twist value.

**Full boundary kernel and primitive image.** With cusp rows ordered
(zero,infinity), the reduced raw boundary row, measured in
[infinity]-[zero], is h=(1,-1,0,0,0,0,0,0,0,0,0,0).
Indeed g_0 goes from 0 to 1/11, g_1 from infinity to 0, g_2 from 0
to 1, and g_i for 3<=i<=11 from -1/(i-1) to 0. The endpoint units
for the first endpoint of g_3,...,g_11 are respectively
(6,4,3,9,2,8,7,5,10); all other units are one. The certificate checks
both congruences on all 24 endpoints. The full raw boundary has rows
(-h,h), so no cusp direction was discarded in using this reduced row.

Write Pi and Q for L039's certified integral projection and section,
and K for its saturated raw relation columns. Full replay gives
h A^t=0 on all 24 source relations and h K=0 on all nine saturated
columns. Moreover hQ=B=(0,0,-1) and B Pi=h on all twelve generators.
Thus delta is exactly the stated integral quotient boundary. In these
coordinates a complete integer normal-form witness is

\[
T=\begin{pmatrix}0&1&0\\0&0&1\\-1&0&0\end{pmatrix},\qquad
T^{-1}=\begin{pmatrix}0&0&-1\\1&0&0\\0&1&0\end{pmatrix},\qquad
BT=(1,0,0).
\]

Both inverse products are the identity over Z. For any integral x, put
y=T^(-1)x; then Bx=y_1. Therefore the entire kernel consists exactly
of the last two columns of T, with arbitrary integral coefficients.
They are e_1,e_2, lifted by raw g_9,g_10 under Q. This proves the full
integral kernel and its splitting; rational dimension alone is not used.

The two functional values are (5/2,5). Clearing denominator two gives
(5,10), whose gcd is five, with Bezout witness (1,0). Both values are
divisible by 5/2 and the first attains it. Therefore their entire image
is (5/2)Z, and the normalized image values (1,2) give surjectivity to Z.
This is the full absolute image, not the integral plus-eigensublattice.

**Independent oriented period.** The cycle gamma=-g_3 has oriented
endpoints (0,-1/2), coordinates (0,-1,0) and phi(gamma)=-5.
The matrix M=(-5,-1;11,2) has determinant one, lies in Gamma_0(11)
and sends 0 to -1/2. Import Cremona,
[Propositions 2.10.1--2.10.2, pp.34--35, equation (2.10.5)](https://johncremona.github.io/book/fulltext/chapter2.pdf#page=28).
Its basepoint-independent oriented period at alpha=(-2+i)/11, with
M alpha=(-5+i)/11, gives

\[
I(\gamma)=\sum_{n\ge1}\frac{a_n}{n}e^{-2\pi n/11}
\left(\cos(-10\pi n/11)-\cos(-4\pi n/11)\right).
\tag{4}
\]

The source identifies this with the cusp cycle's period even though the
Fourier evaluation uses interior endpoints. Both interior endpoints and
the cusp/matrix orientation are checked by exact rational arithmetic.

Use Wuthrich, *Numerical modular symbols for elliptic curves*,
[arXiv:1608.06423v2, Lemma 4 with its full proof, pp.5--6](https://arxiv.org/pdf/1608.06423v2#page=6).
Its bound |a_n|<=n and full geometric remainder apply at height 1/11.
For the two series in (4), after T=64 the absolute omitted error is at
most 2 r^(65)/(1-r), where r=exp(-2 pi/11). We use this explicit bound
from the proof, rather than just its asymptotic truncation prescription.

All arithmetic below is rational with outward scale D=2^48. Machin's
identity pi=16 atan(1/5)-4 atan(1/239), with 32 terms and the adjacent
alternating partial sums for each atan, bounds pi. The checker verifies
the exact tangent identity; the principal branch follows since
0<4 atan(1/5)-atan(1/239)<4/5<pi/2. For the two endpoints of
h=2 pi/11, 0<h<1, degree-40 exponential partial sums and their adjacent
sums bound exp(-h). Monotonicity reverses the endpoints. Every conversion
to scale D rounds its lower endpoint down and upper endpoint up.

For each residue j=0,...,5, reduce cosine arguments modulo 11 and use
cos(-theta)=cos(theta). For j>0 the interval for theta=2 pi j/11 has
midpoint t and radius rho. The sum P=sum_(k=0)^24 (-1)^k t^(2k)/(2k)!
has error at most |t|^50/50! by Taylor's theorem of degree 49 (the
degree-49 coefficient is zero). The derivative bound |sin|<=1 adds
rho for moving from t to any enclosed theta. Thus the entire cosine
interval is P+[-epsilon,epsilon], epsilon=|t|^50/50!+rho, rounded
outward; j=0 is exactly one. The certificate saves every full rational
polynomial/error value, not a floating-point cosine.

All 18 primes through 64 have complete point-count evidence. The verifier
independently exhausts every y for every x, rather than sharing the
producer's quadratic-character method. It checks the nodal count at 11,
every factorization and every prime-power recurrence for all 64 Fourier
coefficients. The exact coefficients, all six cosine intervals, all 64
powers, differences, weighted terms and partial sums are replayed.
The final finite sum is
[-357250659363073,-357250659362992]/D; the full two-series tail is
bounded outward by 10/D. Adding it proves (1), whose upper endpoint is
strictly negative. This is independent of any elliptic AGM magnitude,
twist value, normalized symbol or guessed sign. As I(gamma)=beta*(-5),
it proves beta>0.

**Period magnitude and entire relative normalization.** Import the
full period-lattice equality c Lambda_f=Lambda_E stated before
Proposition 5.1 in
[Cremona's appendix to Agashe--Ribet--Stein, *The Manin constant*](https://wstein.org/papers/ars-manin/html/node13.html).
Lambda_f is the image of all integral absolute cycles; Lambda_E uses
the minimal Neron differential. Optimality is L040's exact-model
published Theorem 5.2 import, retaining its computational qualification.
Import Cesnavicius, *The Manin constant in the semistable case*,
Compositio Math. 154 (2018), 1889--1920,
[arXiv:1703.02951v3, Theorem 2.13, pp.8--9](https://arxiv.org/pdf/1703.02951v3#page=8).
The new optimal quotient has H=Gamma_0(11) and exact squarefree conductor
11; for every prime p, p^2 does not divide 11. The theorem gives
ord_p(c)=0 at every prime, including two, so |c|=1. Thus the two full
period lattices agree, irrespective of a choice of sign for c.

Import the total-period convention of Cremona,
[Section 2.8, p.30, following (2.8.9)](https://johncremona.github.io/book/fulltext/chapter2.pdf#page=24).
For either real lattice type the total real period is twice the least
positive real part of a full period. Here Delta<0 gives one real
component, nonrectangular type, and Omega is also the least positive
purely real period. Its full real projection still has generator Omega/2.
Keeping that factor, the full absolute image computed above gives

\[
\operatorname{Re}\Lambda_f=I(\ker\delta)
=\beta(5/2)\mathbf Z=\operatorname{Re}\Lambda_E
=(\Omega(E)/2)\mathbf Z.
\]

Equality of these positive-generated subgroups and beta>0 imply
beta*(5/2)=Omega/2, hence beta/Omega=1/5. L039 identifies I=beta phi
on the entire relative module already, so (2) holds on every relative
path, not just on the kernel. No plus-projection index or isogeny scale
has been silently set to one.

Applying (2) to all twelve integral generator coordinates proves (3).
Complete replay checks all 24 source relations and all nine saturated
relations again after scaling. The reduced denominators include both
two and five; their least common multiple is ten. Every integral relative
path is an integral combination of these generators, so its F value
lies in (1/10)Z. For p>=5, p!=5, all values are p-integral. L028's
already justified lambda-plus convention identifies S(r)=F({infinity,r}),
and its finite-generator argument supplies C=0 at every level.

**Evidence and qualifications.** The complete new verifier imports no
producer. It binds the three L039 inputs by their actual hashes, runs
fresh complete structural/dual replay, and checks every new witness and
interval described above. Its adjacent report has no failures. The source
theorems and published optimality qualification are mathematical premises,
not verified by the scripts. A provisional raw-boundary sign assertion
failed during development; `development-failure-01.json` preserves the
actual endpoint row and producer hash. The corrected boundary normal form
above uses the same absolute kernel and cycle; no failed output is used.

Only after this recovery and complete replay, compare with audited L041.
`comparison.json` binds both certificates and checks the independently
recovered scalar and all twelve values. They agree. L041 is a final
comparison, not a mathematical input to recovery, and its twist value is
unused. This matches an existing result by a known alternate mechanism;
the separate critical review below passes without a mathematical correction. No inference
about complex order, rational rank, Sha or the main BSD gap follows.

**Separate critical audit (2026-10-10).** The prior SPECIALIZE assessment
covered precisely this assembly and its finite witnesses. Full L043,
both new programs, L039's arithmetic/instance proof and prior audit,
L040's exact-model optimality import, and the complete parent source
comparison were inspected. The named theorems above are reused with
their hypotheses; no new optimality argument or source theorem is claimed.
Reproduce from the notebook root:

```bash
python3 scripts/conductor-eleven/absolute-cycles/audit_certificate.py
```

The complete report is
`scripts/conductor-eleven/absolute-cycles/critical-audit/audit.json`.
Before execution the audit copies and hashes fifteen input/program/report
files under its `originals/`, with notebook-relative paths preserved;
`pre-replay-manifest.json` records their hashes. This includes both original
programs, this audit program, original full reports and the development
boundary-sign failure. All fifteen files remain byte-identical after the
audit. Fresh outputs go only in the new audit directory.

The complete fresh replay has 983 successful checks and no failures. Its
entire summary and check list equal the original report. Fresh upstream
structural/dual replay checks every orbit, relation, normal-form operation,
inverse and path. The entire fresh structural report equals its original,
including all sixty paths and 218 segments; the audited L039 arithmetic
proof supplies the independently established model/conductor hypotheses.
Thus reuse of its integral identification is supported by complete replay,
not by a report-success flag or a rational dimension count.

For the new boundary, each cusp witness satisfies both equivalence
congruences, and the classification proof covers all rational endpoints.
End minus start gives g_0 boundary [infinity]-[zero], g_1 its negative,
and zero on the other ten generators. This checks the correction against
geometry and preserves the failed provisional opposite sign. Both inverse
products for T and T^(-1) and BT=(1,0,0) hold over Z. For every integral
x, its transformed first coordinate is Bx; setting it to zero leaves
exactly the two free integral columns e_1,e_2. Their image (5/2,5), with
the checked gcd and Bezout witness, proves the full primitive image.
In particular no unnoticed index or restriction to plus homology remains.

For orientation, det(M)=1, M(0)=-1/2 and the exact interior endpoints
are as written above. The primitive of 2 pi i f(z) dz is
sum_(n>=1) (a_n/n) exp(2 pi i n z), so end minus start gives exactly
the cosine difference in (4). Every coefficient, prime-power recurrence,
finite interval and rounding operation in the original program is replayed.
Machin's tangent identity and principal branch, decreasing alternating
exponential bounds, and cosine Taylor/Lipschitz errors all have the domains
stated above. The all-n coefficient bound is the imported theorem, not
the finite check |a_n|<=n for n<=64. Both omitted Fourier series are
covered by the full geometric bound.

To test the repeated-rounding calculation independently,
`critical-audit/independent-fourier.json` records a second complete rational
enclosure. It uses forty alternating arctangent terms, a 2^64 grid for pi
and r, degree-fifty exponential bounds with the adjacent degree-fifty-one
sum, and degree-sixty cosine polynomials. At cosine midpoint t and radius
rho the error is |t|^62/62!+rho, since the degree-sixty-one coefficient
vanishes. The already fully verified coefficients a_1,...,a_64 are reused;
their correctness is not claimed to follow from a second point-count
algorithm here. Every power is computed directly as [r_lo^n,r_hi^n].
All products and sums then use exact rational endpoints, with no
intermediate dyadic rounding. The omitted error is bounded by
2 r_hi^65/(1-r_hi), strictly positive and at most 1/2^48. The file saves
all elementary bounds, all 64 terms and partial sums, and the exact full
tail and period endpoints. Outward conversion at the original scale gives

\[
I(\gamma)\in
\frac{[-357250659363036,-357250659363035]}{281474976710656}
\subseteq\frac{[-357250659363083,-357250659362982]}{281474976710656}
\subset(-\infty,0).
\]

Consequently the independent sign test passes without using any twist or
normalized symbol. Negative Delta gives the nonrectangular real lattice:
its purely real generator is Omega, but the projection of the full lattice
has generator Omega/2. Squarefree conductor and the identified optimal
minimal model meet the stated Manin-constant theorem at every prime,
including two. Equality of full lattices with |c|=1 and beta>0 therefore
gives beta/Omega=1/5. All twelve relative values, both sets of relations,
and their least common denominator ten are verified. The valuation
conclusion C=0 retains p>=5 and p!=5 explicitly.

Seven separately saved altered certificates are rejected at their intended
checks: quotient-boundary sign, index-two kernel transform, missing Bezout
primitivity, reversed cycle orientation, final Fourier term, omitted tail,
and doubled normalization scale. These are targeted robustness checks,
not a universal software-soundness proof. Only after recovery, complete
replay and the independent sign calculation does the audit open L041's
certificate: current byte bindings, scalar and all twelve values agree.
L041 remains a final comparison, not an input to normalization.

The audit has no unexpected failures and requires no mathematical
correction. It validates the previously unaudited fixed input as a
reproduction of the cited mechanism. Published optimality retains its
complete-isogeny-class/two-period computational qualification, Mathlib
coverage remains unchecked, and no arbitrary-curve production or BSD
rank, Sha, coefficient or complex-order conclusion is added.

## Mathlib

Full matching fixed conductor-eleven boundary/image/oriented-period
certificate: not checked. Supporting integral modular-symbol homology,
optimal-period equality, semistable Manin constant, real-component period
factor and Fourier enclosure coverage: not checked. Unknown availability
is not absence. The precise named sources above and L039's audited local
arithmetic supply the mathematical inputs; no Mathlib result certifies
the new program artifacts or removes the published-source qualification.
