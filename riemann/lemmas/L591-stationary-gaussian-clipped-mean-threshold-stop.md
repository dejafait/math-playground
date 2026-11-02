# Lemma 591: the specified stationary Gaussian bulk misses the clipped threshold

## Hypotheses

Let G be a centered real stationary Gaussian process with covariance

    E[G(s)G(t)]=r(s-t),
    r(d)=integral_(-1/2)^(1/2) cos(ud) du.

Use its smooth version and ordinary derivatives, and put

    X=G(0), Y=G'(0), Z=G''(0), Q=(XZ-Y^2)_+.

There are no factorial-divided derivatives, amplitude rescaling,
conditioning, first-height/second-height independence assumptions,
bounded-path hypotheses or actual-Hardy/Xi identifications. The
one-height covariance is exactly L473 (7), with the angular-frequency
normalization of L473 (6). No arithmetic moment theorem in L473 is
used in this result.

## Conclusion

The expectation is finite and has the certified rational enclosure

    0 <= E Q < 1/360 < 1/288,
    1/288-1/360=1/1440.                                  (1)

In fact it has the explicit upper bound

    E Q <= -3/20+(1/6)sqrt(5/6) < 1/360.                 (2)

Consequently this fixed Gaussian law cannot supply the nominated
clipped mean exceeding 1/288. This is a specialization of known
Gaussian/quadratic-form methods, not a general Gaussian expectation
theorem or a novelty claim. It neither rules out non-Gaussian
stationary/periodic bulks nor proves a sign for any actual-Xi
observable. Bounded paired support, finite-C_I covariance reserve,
fourth/probability assembly and nonlinear actual-Xi transfer remain
independent. The separate finite-dimensional certificate audit in
Section 4 passes; the external source proofs remain imported.

## Proof

### 1. Imported regularity and exact covariance

For existence, smoothness and joint Gaussianity of the ordinary
derivatives, import Naomi Feldheim, Ohad Feldheim, Benjamin Jaye,
Fedor Nazarov and Shahaf Nitzan, *On the probability that a stationary
Gaussian process with spectral gap remains non-negative on a long
interval*, [arXiv:1801.10392v2, Section 2, pp.2--3](https://arxiv.org/pdf/1801.10392v2).
Only the compact-spectrum preliminary facts are used; their
persistence theorem's spectral-gap premise is not asserted here.
Their Fourier convention is exp(2*pi*i*x*y). Push forward Lebesgue
measure on [-1/2,1/2] by u -> u/(2*pi) to obtain exactly r above.
This is a finite symmetric compactly supported spectral measure.
The imported derivative covariance rule therefore applies through
order two, with ordinary angular-frequency derivative factors iu.

The joint covariance is L473 (7):

    Sigma = [[1,0,-1/12],
             [0,1/12,0],
             [-1/12,0,1/80]].                            (3)

Thus the value/second-derivative covariance is negative. Retaining
it is essential. The determinant of the (X,Z) block is
1/80-1/144=1/180, and det Sigma=1/2160>0. The first two leading
principal minors are 1 and 1/12, so Sigma is positive definite.
In particular the nonsingular real Gaussian setting applies.
Also, by Cauchy--Schwarz,

    E|XZ-Y^2| <= sqrt(E X^2 E Z^2)+E Y^2
               =1/sqrt(80)+1/12 < infinity.              (4)

### 2. Specializing the Gaussian quadratic-form reduction

Import the central real Gaussian quadratic-form reduction from
J. P. Imhof, *Computing the distribution of quadratic forms in normal
variables*, Biometrika 48 (1961), 419--426,
[DOI 10.1093/biomet/48.3-4.419](https://doi.org/10.1093/biomet/48.3-4.419),
[published institutional scan](https://access.archive-ouverte.unige.ch/access/metadata/4a7195a7-be6d-4605-8f1e-94ff4b638b8d/download),
Section 1, equation (1.1), p.419. It reduces a real symmetric form
with nonsingular Gaussian covariance to a signed weighted sum of
independent chi-squares. The variables here are centered, so no
noncentrality is present. No even-multiplicity finite-expression
formula from Section 2, characteristic-function branch or numerical
inversion rule is invoked. The following computes the specific
whitening and eigenvalues rather than reproving that theorem.

Let U,V,W be independent N(0,1) variables. The centered Gaussian
vector

    (U, V/sqrt(12), -U/12+W/sqrt(180))                    (5)

has covariance (3): in particular its final variance is
1/144+1/180=1/80. It therefore has the same law as (X,Y,Z).
Under (5) the unclipped form is

    -U^2/12+UW/sqrt(180)-V^2/12.

The symmetric matrix of the (U,W) form is

    M=[[-1/12, 1/(2sqrt(180))],
       [1/(2sqrt(180)), 0]].

Its trace is -1/12, determinant is -1/720, and its eigenvalues are

    a=(3/sqrt(5)-1)/24,
    -b=-(3/sqrt(5)+1)/24.                                (6)

Indeed the discriminant is 1/144+1/180=1/80. Orthogonally
diagonalizing M preserves the independent standard-normal law of
(U,W), and its independence from V. Hence, for independent standard
normals N_1,N_2,N_3,

    XZ-Y^2 has law a N_1^2-b N_2^2-N_3^2/12.             (7)

Both signs in (6) are strict because 9>5. More specifically,

    0<a<1/60, b>1/12.                                   (8)

For the upper bound on a, the equivalent inequality
3/sqrt(5)<7/5 follows by squaring positive quantities:
225<245. The bound on b is equivalent to 3/sqrt(5)>1,
which follows from 9>5. The positive-part function is increasing.
Equations (7)--(8) therefore give the pointwise comparison under
this coupling

    (a N_1^2-b N_2^2-N_3^2/12)_+
      <= (N_1^2/60-(N_2^2+N_3^2)/12)_+.                 (9)

### 3. Direct evaluation of the comparison integral

Only the comparison form in (9), not the original three unequal
weights, is evaluated. Its expectation is an elementary
three-dimensional Gaussian integral. This is within the assessed
direct-integration specialization; a general positive-part moment
formula needs no reproof or numerical implementation here.

Write (N_1,N_2,N_3)=R Theta. In spherical coordinates the standard
Gaussian density factors as a radial factor proportional to
R^2 exp(-R^2/2) dR and uniform surface probability on S^2. Thus R
and Theta are independent, E R^2=3, and Theta_1 is uniform on
[-1,1]. The last assertion follows from the surface area element
dphi d(Theta_1), whose azimuthal integral is 2*pi. The origin has
zero Gaussian measure and causes no coordinate exception in the
integral. All integrands after clipping are nonnegative, so Tonelli
justifies the separation; they are also bounded by R^2/60 and
hence integrable.

Since Theta_2^2+Theta_3^2=1-Theta_1^2, the expectation on the
right of (9) is exactly

    3 integral_0^1 (s^2/60-(1-s^2)/12)_+ ds
      =3 integral_c^1 (s^2/10-1/12) ds,
    c=sqrt(5/6).                                        (10)

The clipping endpoint c is retained. Since c^3=(5/6)c,
the last integral equals

    (1/10)(1-c^3)-(1/4)(1-c)
      =-3/20+c/6.                                       (11)

Finally c<11/12 because c^2=120/144<121/144 and both
quantities are positive. Consequently

    -3/20+c/6 < -3/20+11/72=1/360.

Together with nonnegativity, (4), (9)--(11) prove (1)--(2).
No sampling, approximate integration, infinite-product interchange
or actual-height limit is part of this certificate. The positive
gap 1/1440 is exact; it excludes only the stipulated covariance
and Gaussian-law scalar target.

### 4. Independent certificate audit (31 October 2026)

The audit reuses the inspected compact-spectrum and quadratic-form
statements cited above; it checks their application and every step
(3)--(11), not the external manuscripts' proofs. L473 (6)--(7) is the
only direct local mathematical input. Its arithmetic moment results,
L586's cone construction and L590's separate obstruction are not
premises of this scalar proof.

First, with covariance r(s-t), differentiating in the two arguments
gives factors (iu)^j(-iu)^k. On the symmetric unit-length frequency
interval, the moments of orders zero, two and four are respectively
1, 1/12 and 1/80, and the odd moments vanish. This gives exactly (3),
including E[XZ]=-1/12, for ordinary derivatives. The source's
2*pi convention is converted by pushing the measure forward, keeping
its total mass one; it does not insert an extra density factor into r.
Compact spectral support is the regularity premise used. No gap around
frequency zero is needed. The leading principal minors 1, 1/12 and
1/2160 are positive, so the nonsingular-covariance hypothesis holds.
Equation (4) verifies absolute integrability before any expectation
comparison.

Second, (5) has all six covariance entries of (3), so centered joint
Gaussianity identifies the vector's law. Inserting it into XZ-Y^2
gives exactly the displayed quadratic form, with cross coefficient
1/sqrt(180), hence matrix entry 1/(2sqrt(180)). The characteristic
polynomial of its two-by-two matrix is

    lambda^2+lambda/12-1/720.

Its discriminant is 1/80; its two roots are precisely a and -b
in (6). The orthogonal change acts on (U,W) only, so the untouched
V remains independent. This checks the independent chi-square
representation (7), with no missing multiplicity or scaling factor.
The comparisons in (8) follow by squaring positive quantities:
9>5 gives a>0 and b>1/12, and 225<245 gives a<1/60.
Each squared normal is nonnegative, so replacing these coefficients
as in (9) increases the entire form before applying its increasing
positive-part function. No comparison of signed expectations is
substituted for that pointwise inequality.

Third, the angular marginal has density 1/2 on [-1,1]. Its evenness
converts that probability integral to the integral on [0,1] with
density one; the radial expectation contributes the separate factor
3. The comparison integrand is bounded by R^2/60, and R and the
uniform angle are independent. Thus the separation in (10) is both
Tonelli-valid and finite. The angular polynomial is s^2/10-1/12,
which changes sign at c=sqrt(5/6), strictly inside (0,1). Its value
at the endpoint is zero; retaining or deleting this singleton cannot
affect the integral. Direct antiderivative evaluation gives

    3 [s^3/30-s/12]_c^1
      =-3/20+c/4-c^3/10=-3/20+c/6.

Finally 5/6=120/144<121/144 proves c<11/12 without numerical
rounding. The rational calculations are

    -3/20+11/72=1/360,
    1/288-1/360=1/1440>0.

All asserted inequalities, the clipping endpoint and the strict
threshold margin therefore pass. No correction to (1)--(11) is
needed. This audit certifies a known-method specialization for this
fixed Gaussian covariance only; it supplies no broader Gaussian
exclusion, periodic-path realization, actual-height limit or RH sign.

## Mathlib

Full matching coverage for this stationary Gaussian jet and clipped
expectation specialization has not been checked. No absence claim
is made. The proof uses cited real Gaussian regularity/reduction
and explicit finite-dimensional algebra and integration; no Lean
formalization or formal verification is asserted.
