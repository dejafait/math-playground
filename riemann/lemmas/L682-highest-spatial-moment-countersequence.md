# Lemma 682: the highest original spatial moment fails the proposed scale

## Hypotheses

Use L666's family with **zero displacements**. For each integer q>=1 put

    n=12q+3, M=4q+1=n/3, k=M-1=4q,
    x=-d=-5/4, R=11/8, U=R^2=121/64, alpha=27/10, h=alpha/n,
    Z={x} union {x+i*h*(m+1/2): -2q<=m<2q}.

All original residues are one; the same Z is used for every |u|=1.
Keep every grid factor, including j=0, and the denominator angle 1/u:

    t_j=j/n,
    B_u(v)=product_(0<=j<n) R*(v-t_j*u)/(U-t_j*v/u),
    W_a(u)=B_u(x)/B_u(a),
    c_k(u)=R^(-1) sum_(a in Z) W_a(u)*(a/R)^k,
    D=mean_(|u|=1) sum_(a in Z) |W_a(u)|^2/(U-|a|^2).

The mean is normalized. This is an admissible sequence in the complete
independent-displacement cube |e_m|<=1/8, by taking every e_m=0.
In particular all denominators in D are positive. No spatial coefficient,
original residue or angular observation weight is changed.

## Conclusion

Uniformly in |u|=1, for every n=12q+3>=15,

    |sum_(a in Z\{x}) W_a(u)*(a/R)^k|
                       <=(8/5)*n*exp(32-7n/200),                 (1)
    max_(|u|=1)|c_k(u)|
      <=R^(-1)*[(10/11)^(n/3-1)+(8/5)*n*exp(32-7n/200)].       (2)

Consequently the original normalized ratio satisfies

    max_|u|=1 |c_k(u)| / [n*exp(-n/32)*sqrt(D)]
      <=(sqrt(21)/11)*[(11/(10n))*exp(-n/2400)
                         +(8/5)*exp(32-3n/800)] -> 0.           (3)

There is therefore no absolute C>0 and uniform sufficiently large-q
onset for the proposed highest-moment lower bound on the full L666
family. The failure already occurs on this fixed, undisplaced sequence;
no optimized or n-dependent perturbations are needed.

This is a counterexample to one sufficient coefficient certificate,
not to a lower bound for the full spatial logarithmic maximum H, to
support or realization, or to RH. In particular, another spatial
coefficient can be much larger. The separate conceptual audit of
3 November 2026 accepts (1)--(3), including independent enclosures
of every sample (Section 6). The original POTENTIALLY_NEW label
describes the bounded prior source comparison, not certified
originality. The audit is REPRODUCTION; there is no RH candidate.

## Proof

### 1. Source scope, overlap and the particular test

The invocation-start EXPLORE assessment is
`drafts/literature/2026-11-02-displaced-highest-spatial-moment.md`.
It covers this exact highest prescribed moment, original D and the
alternative of an admissible countersequence. L666 supplies the family,
admissibility and rational continuation. L669's fixed-angle stop,
L670/L671's clearing costs and the parked c_0 deformation route are
comparisons, not inputs to the estimate below. No bound for c_0 or
auxiliary positive weights is substituted for the original moment.

Import the Cauchy residue theorem from NIST DLMF v1.2.8 (15 September
2026), [Section 1.10(iv), (1.10.8)](https://dlmf.nist.gov/1.10#E8),
with its preceding finite-singularity and positive-orientation
hypotheses; and the logarithm series from
[Section 4.6(i), (4.6.1), (4.6.4)](https://dlmf.nist.gov/4.6).
For the C^2 linear-interpolation error M*h^2/8, use University of
Illinois CS450 Spring 2025, Chapter 7, slide "Error for Global
Polynomial Interpolant", [PDF p.14](https://relate.cs.illinois.edu/course/cs450-s25/file-version/9b3a009d3abd3160be3746d4f083e6fe166b6f54/pdfs/cs450_s25_chap07l_300dpi.pdf),
the stated n=2 specialization. All pole, convergence and derivative
hypotheses are checked below. These are imported tools, not reproofs.
The new calculation is the finite-family specialization and its
quantitative bound, rather than a reproof of general rational quadrature.
The prior rational-norm comparisons supply no such diagonal estimate.

For context only, the intended downstream endpoint transfer was the
known polynomial Mahler formula and leading-coefficient bound:
F. Brunault and W. Zudilin, *Many Variations of Mahler Measures*,
ISBN 9781108794459, Propositions 1.4--1.5 pp.6--7 and Lemma 1.6 p.8,
[publisher excerpt](https://assets.cambridge.org/97811087/94459/excerpt/9781108794459_excerpt.pdf).
That theorem is not needed for the negative (1)--(3). We do not infer an
upper bound for H from an upper bound for one of its coefficients.

### 2. Exact lattice contour, with the radial power retained

The undisplaced poles are distinct: successive lattice ordinates
have gap h, and the nearest are at distance h/2 from the anchor.
Their absolute ordinates are at most (2q-1/2)*h<9/20. Hence
|a|^2<353/200<(273/200)^2=(R-1/100)^2 for each nonanchor pole;
the anchor satisfies the same upper bound. This directly checks
the L666 admissibility and positive diagonal denominators needed here.
L666's quadrature theorem and its unproved signed-energy bound are
not used. Direct division of its B factors supplies (4), including j=0.

Put b=9/100, r=9/20 and

    A_n=2q*h=r-27/(20n).

For fixed |u|=1, let Gamma_n be the positively oriented boundary of
the rectangle a=x+s+i*y, |s|<=b, |y|<=A_n. On the larger rectangle
|s|<=b, |y|<=r we have

    |a|>=d-b=29/25>1,
    |a|^2<=(d+b)^2+r^2=19981/10000<9/4.

Define the rational function and meromorphic lattice kernel

    F_n(a,u)=(a/R)^k product_(j=0)^(n-1)
                  [(x-t_j*u)/(a-t_j*u)]
                  *[(U*u-t_j*a)/(U*u-t_j*x)],
    K_n(a)=1/[1+exp(2*pi*(a-x)/h)].                              (4)

This is exactly W_a(u)*(a/R)^k where a is an original pole, with
the j=0 factor x/a included. It extends holomorphically to a
neighborhood of the closed larger rectangle: |a-t_j*u|>=|a|-1>0,
and |U*u-t_j*x|>=U-d>0. It is also nonzero there, since
|U*u-t_j*a|>=U-3/2=25/64>0 and x-t_j*u never vanishes.

The poles of K_n inside Gamma_n are precisely
a_m=x+i*h*(m+1/2), -2q<=m<2q. They are simple, with residue
-h/(2*pi). None is on Gamma_n; its horizontal heights are integer
multiples 2q*h, not half-integer multiples. The residue theorem gives

    sum_m F_n(a_m,u)=(i/h) integral_(Gamma_n) F_n(a,u)*K_n(a) da. (5)

The original anchor x is not a kernel pole and remains a separate term.

On a horizontal edge, exp(2*pi*i*y/h)=1, so

    |K_n(a)|<=exp[-(2*pi/h)*max(s,0)].

On either vertical edge, the reverse triangle inequality gives
the same bound with a factor 2. Indeed
2*pi*b/h=pi*n/15>=pi>3, so exp(-2*pi*b/h)<1/2. Uniformly on
the complete contour, using pi>3 and alpha=27/10,

    |K_n(a)|<=2*exp[-(20/9)*n*max(s,0)].                       (6)

### 3. A compact bound for the continuum exponent

For the larger rectangle define real-valued functions

    f(t;a,u)=log|[(x-t*u)/(a-t*u)]*[(U*u-t*a)/(U*u-t*x)]|,
    g(a,u)=integral_0^1 f(t;a,u) dt+(1/3)*log(|a|/R),
    Psi(s,y,u)=g(x+s+i*y,u)-(20/9)*max(s,0).                   (7)

We establish the following **complete boundary** bound:

    Psi(s,y,u)<=-2385744893/62500000000 < -7/200,              (8)

for all |u|=1, on s=+-b, |y|<=r and on |y|=r, |s|<=b.
It is a rational certificate with explicit error bounds between its
samples. The reproduction command is

    python3 scripts/one-sided-hankel/highest-spatial-contour-certificate.py

Its full output is
`scripts/one-sided-hankel/highest-spatial-contour-certificate.json`.
It records all 12,558 rational sample upper bounds, 78 rows, mesh
coverage, every rounding/tail charge, the maximum and 17 arithmetic
checks. All pass/fail decisions use integers or exact rational numbers;
the displayed decimal in its console summary is not used for a bound.

#### Exact values and series errors

For |z|<1 set S(z)=sum_(j>=1) Re(z^j)/[j*(j+1)]. The uniformly
convergent logarithm series, integrated on 0<=t<=1, gives

    g(a,u)=(1/2)log(d^2/|a|^2)+(1/6)log(|a|^2/U)
             +S(u/a)-S(u/x)+S(x/(U*u))-S(a/(U*u)).             (9)

Every series argument has modulus less than 9/10 on the complete
larger rectangle. In fact 1/|a|<=25/29<9/10, 1/d=4/5,
d/U=80/121 and |a|/U<96/121. Thus each tail after degree 100
has absolute value at most

    (9/10)^101 / [101*102*(1-9/10)].                          (10)

Parametrize both angular semicircles by

    u=epsilon*(1-v^2)/(1+v^2)+i*2v/(1+v^2),
    -1<=v<=1, epsilon in {-1,1}.                              (11)

At rational s,y,v, all arguments and squared moduli in (9) are rational.
For the finite S sums the script uses scale S_0=10^40, floors each
input coordinate to a multiple of 1/S_0 and floors each real and
imaginary coordinate after multiplication. The stored input's sum of
absolute coordinates is less than 3/2, checked for every sample.
If e_j bounds each coordinate error in the computed jth power, then

    e_0=0, e_(j+1)<=(3/2)e_j+3/S_0,
    e_j<=6*((3/2)^j-1)/S_0.

Here the input-coordinate errors contribute at most 2/S_0 against
true powers of modulus <=1, and the final floor contributes 1/S_0.
Since sum_(j=1)^100 1/[j*(j+1)]<1 and the displayed e_j bound
is increasing, the power errors in the finite weighted sum total
at most e_100. Each of its 100 integer divisions adds less than
1/S_0. The finite weighted sum therefore has error at most

    [6*((3/2)^100-1)+100]/S_0 < 10^(-20).                    (12)

The four instances of (10) and (12) are added in absolute value;
their total is less than 10^(-6). No signed numerical error is canceled.

For any positive rational z, the script scales z by a power of two
into [1,2]. On that interval, w=(z-1)/(z+1) lies in [0,1/3], and

    log z=2*sum_(j=0)^31 w^(2j+1)/(2j+1)+T,
    0<=T<=2*w^65/[65*(1-w^2)].                              (13)

It uses the same enclosure for log 2 and reverses endpoints when
multiplying by a negative scaling exponent. Thus both log terms in
(9) have rational enclosures. After adding the upper errors, each
sample upper bound is rounded **up** to a multiple of 10^(-12).

#### All gaps between samples

Write A=|a|. Differentiation of the nonvanishing factors in (7) is
valid throughout the larger rectangle. Either second position
derivative, in s or y, obeys

    |g_ss|, |g_yy|
       <=integral_0^1 [1/(A-t)^2+t^2/(U-t*A)^2]dt+1/(3*A^2)
       <=625/116+4096/3025+625/2523 < 8.                     (14)

For example, the first integral is 1/[A*(A-1)], and the second is
at most integral_0^1 (U-t*A)^(-2)dt=1/[U*(U-A)]. These bounds
use 29/25<=A<3/2, with no angular sign assumption.

For each of the four angular logarithms log|1-t*rho*exp(+-i*theta)|,
the absolute first and second theta derivatives, integrated in t,
are at most rho/(1-rho). This follows by bounding the derivatives
by t*rho/(1-t*rho) and t*rho/(1-t*rho)^2, respectively, and then
by the integral of rho/(1-t*rho)^2. The four upper rho values are
4/5, 25/29, 96/121 and 80/121. Their sum of bounds is

    B=4+25/4+96/25+80/41=65769/4100.

In (11), |theta'(v)|<=2 and |theta''(v)|<=4 on either semicircle.
Consequently

    |g_vv|<=8*B=131538/1025<130.                            (15)

The damping in Psi is constant on a vertical side and linear on
each horizontal half s<=0 or s>=0. Thus (14)--(15) also bound the
needed second derivatives of Psi; the horizontal grid includes s=0,
so no interpolation interval crosses its nondifferentiable kink.

Conjugation gives Psi(s,-y,conjugate(u))=Psi(s,y,u). It suffices to
use y>=0 and both complete semicircles. The mesh is:

- vertical sides: s=-b,b; y=3j/100, 0<=j<=15;
- horizontal side: y=r; s=-b+3j/100, 0<=j<=6;
- both signs in (11), v=j/80, -80<=j<=80.

The standard linear-interpolation remainder is at most
sup|f''| times the square of the interval length divided by 8.
Applying it in the position and v variables successively bounds
the function on every mesh rectangle by its largest corner value plus

    (8/8)*(3/100)^2+(130/8)*(1/80)^2=2201/640000.             (16)

No mixed derivative is needed: each interpolation is a convex
combination of endpoint values. The two semicircles cover the whole
angular circle, including their shared endpoints. The listed position
grids cover the complete boundary, and the script enumerates and
checks this full cover and all sample-list lengths.

The largest rational sample upper bound is
-10402745197/250000000000, at s=0, y=r, epsilon=1, v=8/80.
Adding (16) gives exactly the upper bound in (8). This maximum is
taken over every stored sample, not a selected preview. The script
also checks the derivative, series, interpolation and finite-product
arithmetic used here; its failure list is empty. The proof of the
extension beyond the samples is (14)--(16), not a numerical fit.

### 4. Finite products and the actual n-dependent rectangle

For t in [0,1] on the larger rectangle,

    |partial_t f|<=4+25/4+96/25+80/41<17.                    (17)

The four bounds follow respectively from the clearances d-1=1/4,
|a|-1>=4/25, U-|a|>25/64 and U-d=41/64. In particular the
left Riemann sum satisfies

    sum_(j=0)^(n-1) f(j/n;a,u)
                         <=n*integral_0^1 f(t;a,u)dt+17.

This weaker-than-necessary error follows by integrating the Lipschitz
bound on each interval [j/n,(j+1)/n]; it includes j=0. Since
k=n/3-1 and -log(|a|/R)<=log(R/(d-b))<1, equations (4),(7) give

    log|F_n(a,u)|<=n*g(a,u)+18.                            (18)

To pass from the fixed horizontal height r to A_n, the first
derivative bound is

    |g_y|<=25/4+64/25+25/87=79147/8700<10.                  (19)

It follows directly by differentiating the two a-dependent factor
logarithms and the radial term; the latter contributes at most
1/(3|a|). The path between A_n and r remains in the larger rectangle.
Since r-A_n=27/(20n), the change in n*Psi is at most 27/2.
Vertical sides of Gamma_n are already contained in the certified sides.
Combining (6),(8),(18),(19), everywhere on Gamma_n,

    |F_n(a,u)K_n(a)|<=2*exp(32-7n/200),                    (20)

because 18+27/2=63/2<32. All constants are independent of q and u.

The perimeter is 4*(b+A_n)<=4*(b+r)=54/25, whence

    length(Gamma_n)/h <=(4/5)*n.

Apply this to the exact integral (5) and (20) to prove (1). Adding
the separate anchor, for which W_x=1 and |x/R|=10/11, proves (2).
This bounds the signed sum through its single analytic contour; no
termwise absolute replacement of the lattice sum was made before (5).

### 5. Original diagonal, strict exponent gap and scope of the negative

The original positive diagonal contains the anchor contribution, so

    D>=1/(U-d^2)=64/21.                                   (21)

The elementary identity log(1+t)=integral_0^t (1+v)^(-1)dv and
(1+v)^(-1)>=1-v for v>=0 imply

    log(11/10)>1/10-1/200=19/200,
    (1/3)log(11/10)-1/32>19/600-1/32=1/2400,
    7/200-1/32=3/800.                                     (22)

Use (21)--(22) in (2), observing
(10/11)^(n/3-1)=(11/10)*exp[-(n/3)log(11/10)]. The resulting
upper bound for the ratio is exactly (3), since sqrt(21)/(8R)=sqrt(21)/11.
Both terms tend to zero along all n=12q+3. For any proposed C>0
and onset, the same admissible sequence eventually contradicts the
claimed lower bound. There is no unknown constant or n-dependent
error in this argument.

The preliminary floating screens are preserved in
`scripts/one-sided-hankel/highest-spatial-moment-screen.json` and
`scripts/one-sided-hankel/highest-spatial-contour-screen.json`, with
their scripts alongside. They selected a test, but are not premises:
sampled angular maxima, sampled D and uncertified cancellation cannot
prove (3). The rational certificate and the analytic argument above
replace every numerical inference needed for this countersequence.

Only the highest original coefficient certificate is retired. No
upper estimate for H, support obstruction, off-line zeta zero or
all-degree sign conclusion follows. Degree drops of the full spatial
polynomial are irrelevant to this upper bound for its prescribed
coefficient, and no root or leading factor is discarded.

### 6. Independent conceptual and arithmetic audit

The separate audit uses the unchanged SPECIALIZE assessment
`drafts/literature/2026-11-03-highest-spatial-moment-countersequence-audit.md`.
It verifies the finite residue identity, all-angle extension and
normalization, rather than treating a finite screen as the conclusion.
The finite pole census in Section 2 exhausts K_n's interior poles;
its residue theorem uses no infinite sum or limiting contour theorem.
The holomorphic F_n has no zeros or poles in the closed larger
rectangle. All bounds are uniform for the same undisplaced family
and every u on the circle. In particular moving A_n toward r does
not move an original pole through the contour in any asserted
application: (5) is applied separately for each n.

The derivative proof in (14)--(15) controls the two real coordinates
of each interpolation rectangle. Successive linear interpolation
uses convex endpoint weights, so its error is their sum (16), with
no mixed-derivative hypothesis. Both signs of (11) and conjugation
cover all angles and both horizontal edges; the split at s=0 avoids
the only damping kink. The finite-product charge 17, missing radial
power charge 1 and height charge 27/2 total 63/2<32. The factor 2
from K_n and perimeter/h<=4n/5 give precisely (1). The anchor is
added once, and its positive contribution alone establishes (21).
The strict gaps 1/2400 and 3/800 in (22) give the ratio limit with
uniform constants; no diagonal upper bound is needed.

Run

    python3 scripts/one-sided-hankel/highest-spatial-contour-audit.py

The complete evidence is
`scripts/one-sided-hankel/highest-spatial-contour-audit.json`.
The program first copies and executes the entire original certificate
program in a temporary directory, preserving the original files. All
fields of the replay match the original JSON; source and certificate
hashes are recorded. It also rechecks every one of the 17 stored exact
arithmetic comparisons, all row maxima and the independently enumerated
78-row, 12,558-sample cover.

Independently of the original fixed-point error formula, it encloses
each sample with rectangular complex intervals at scale T=10^60.
For a real interval represented by integer endpoints [l,h]/T,
addition and subtraction use outward endpoints, and multiplication
takes the minimum and maximum of the four integer endpoint products,
dividing by T with floor and ceiling respectively. Division by a
positive integer also rounds outward. The complex multiplication
(ac-bd,ad+bc) uses those real operations. Starting with outward-rounded
rational arguments and the exact power 1, induction encloses every
complex power and its divided real part. Summing 120 powers then
adding the two-sided error

    (9/10)^121/[121*122*(1-9/10)]

encloses each S value without using (12). The independent real-log
interval uses 40 odd-power terms, tail 2*w^81/[81*(1-w^2)], and
power-of-two scaling with endpoint reversal for negative shifts.
The signs in (9), the radial logarithm and damping are retained in
these interval operations. All resulting lower and upper sample
endpoints are saved, including their grid coordinates and common scale.

Every original saved sample upper bound is strictly larger than its
independent interval upper endpoint. Thus this is a check of all
load-bearing samples, not selected witnesses or the aggregate flag.
Taking the maximum over the full original list and adding (16)
reproduces (8), with exact margin

    -7/200 - (-2385744893/62500000000)
                  =198244893/62500000000>0.

There are no failed sample, mesh, arithmetic or replay comparisons.
The independent interval calculation verifies the certificate values;
Sections 2--5 supply the analytic extension and finite-n proof. This
audit validates the existing target-specific negative, without adding
a theorem about full H or about the Riemann hypothesis.

## Mathlib

Full Mathlib coverage of this family-specific lattice-contour estimate,
the rational certificate and countersequence has not been checked.
No absence claim is made. The reused assessment records the supporting
Mahler results
`Polynomial.logMahlerMeasure_eq_log_leadingCoeff_add_sum_log_roots` and
`Polynomial.norm_coeff_le_choose_mul_mahlerMeasure` in
[Mathlib's MahlerMeasure documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Polynomial/MahlerMeasure.html).
They support the intended downstream polynomial transfer, not the
negative proved here. The scripts give exact arithmetic certificates;
the separate conceptual audit is Section 6. Neither is a Lean
formalization, and no additional Mathlib coverage claim is made.
