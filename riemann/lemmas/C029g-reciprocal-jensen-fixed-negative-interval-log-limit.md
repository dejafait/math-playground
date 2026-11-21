# Corollary C029g: reciprocal Jensen fixed negative-interval log limit

## Hypotheses

Use the actual positive coefficients and scaled ordinary Jensen family
of C028f, with exactly its normalization:

    b_0=1, b_j>0,
    F(u)=sum_(j>=0) b_j u^j/j!,
    U_d(u)=sum_(j=0)^d binom(d,j)b_j (u/d)^j,
    P_d(x)=sum_(j=0)^d binom(d,j)b_j x^(d-j),   d>=3.

Integers d tend to infinity. F is the fixed actual entire function of
order 1/2 identified in C028f. Use its audited, degree-independent
constants K>=1, B=K*3^(3/4)/log2, C=4B, with

    |U_d(u)|<=F(|u|),       log F(r)<=K r^(3/4)  (r>=1),
    n_d(t):=#{u:U_d(u)=0, |u|<=t}<=B t^(3/4)   (t>=1),
    sum_(U_d(u)=0, |u|>R) 1/|u|<=C R^(-1/4)   (R>=1).

Every root count and sum retains algebraic multiplicities. No RH,
real-rootedness, simple-root assumption, zero-free negative interval,
finite type at order 1/2 or effective value of K is assumed. P_d is
the uncentered reciprocal polynomial; U_d is not the real translate
Q_d occurring in the signed-height identity.

Set I=[-2,-1]. Integrals are with respect to real Lebesgue measure.
Logarithms of moduli are defined off polynomial zeros, with arbitrary
values assigned on that finite null set.

## Conclusion

With the fixed finite constant

    D=K*6^(3/4)+2^(3/4)*B*(6+log2),

every integer d>=3 satisfies

    integral_I |d^(-1) log|P_d(x)/x^d|| dx <= D d^(-1/4).   (1)

In particular the displayed integral tends to zero. The bound includes
whole neighborhoods of every real root, both interval endpoints and
all repeated roots. It is a classical-method specialization, with no
claim of progress beyond the inspected general methods. Its constant
is existential through K, not an effective numerical certificate.

This is a fixed-interval statement. It supplies no full-window signed
payment, no vanishing compact nonreal-root mass, no bound H_d=o(d),
and no RH conclusion. The separate audit1970 below accepts this bound
under the unchanged input contracts.

## Proof

### Imported inputs and the specific specialization

The sole direct notebook input is C028f, including its separate
audit1518. Its actual normalization and order input are from Cormac
O'Sullivan, *Zeros of Jensen polynomials and asymptotics for the Riemann
xi function*, arXiv:2007.13582v2, 9 December 2020,
[Introduction (1.2), Section 3.1, Theorem 3.1 and Corollary 3.2](https://arxiv.org/html/2007.13582v2#S3.SS1).
No RH-dependent hyperbolicity conclusion is imported.

We also use the standard named Jensen formula in Min Ru, *Nevanlinna
Theory*, undated author-hosted notes,
[Theorem A1.1.1 and Corollary A1.1.3, printed pp.1-2](https://www.math.uh.edu/~minru/log.pdf).
For a holomorphic g on a neighborhood of the closed radius-rho disk,
with g(0)!=0 and no boundary zeros, its needed pole-free case is

    sum_(g(u)=0, |u|<rho) log(rho/|u|)
      =(1/(2pi)) integral_0^(2pi) log|g(rho exp(i theta))| dtheta
         -log|g(0)|,

counting all multiplicities. The statement and its boundary cases were
already inspected for C028f; assessment1966/review1967 explicitly
approve reuse here. The formula and order theorem are not reproved.

Those inputs do not themselves state a real-interval L1 limit.
The specialization below supplies the finite-factor integral bounds,
the reciprocal scaling and the logarithmic root weights. In particular
it does not infer a one-dimensional trace from planar L1 convergence,
assume a median's asymptotic size or discard root neighborhoods.

### Reciprocal coordinates and finite logarithmic factors

The coefficient definitions give, for x!=0,

    P_d(x)/x^d=U_d(d/x).                                  (2)

P_d is monic of degree d and P_d(0)=b_d>0. Also U_d has degree d
and U_d(0)=1. Thus neither polynomial has an origin root. Inversion
x->d/x has nonzero derivative away from zero; (2)'s nonvanishing
prefactor therefore gives a bijection z=d/u between their root
multisets, preserving each multiplicity. Factoring the monic P_d gives

    log|P_d(x)/x^d|=sum_(P_d(z)=0) h_z(x),
    h_z(x)=log|1-z/x|=log|x-z|-log|x|,                    (3)

almost everywhere on I. These are real logarithms of moduli, with
no choice of a logarithm across any root.

### Entire one-dimensional singular neighborhoods

Write s_+=max(s,0). Since 1<=|x|<=2 on I, the triangle inequality
gives, for every complex z and almost every x in I,

    (h_z(x))_+<=log(1+|z|),
    (-h_z(x))_+<=log2+(-log|x-z|)_+
                   <=log2+(-log|x-Re z|)_+.

For the last inequality, |x-z|>=|x-Re z| and the positive part is
monotone. The isolated points at which the right side is infinite
are harmless. Translation and nonnegativity show

    integral_I (-log|x-Re z|)_+ dx
       <=integral_R (-log|s|)_+ ds
        =2 integral_0^1 (-log s) ds=2.

Because I has length one, these estimates prove absolute integrability
and the uniform bound

    integral_I |h_z(x)| dx<=log(1+|z|)+log2+2.             (4)

It holds when z is real, at either endpoint, and as nonreal z approaches
the interval. No neighborhood is removed, and repeating a factor
repeats its cost, as required for algebraic multiplicity.

For |z|<1/2 there is the sharper estimate

    integral_I |h_z(x)| dx<=2|z|.                         (5)

Indeed set r=|z/x|<1/2. The inequalities
1-r<=|1-z/x|<=1+r imply
|h_z(x)|<=-log(1-r)<=2r<=2|z|. The middle bound follows by
integrating 1/(1-t)<=2 over 0<=t<=r. This argument assumes no
reality of z, and it has no logarithm branch issue.

### Small reciprocal-polynomial roots and large-root logarithmic weights

Fix a degree d. Partition the U_d roots into the strict outer group
|u|>2d and the closed inner group |u|<=2d. The outer group corresponds
exactly to |z|<1/2. By (5) and C028f's complete strict tail,

    sum_(|u|>2d) integral_I |h_(d/u)(x)| dx
       <=2d sum_(|u|>2d) 1/|u|
       <=2d C(2d)^(-1/4)=2^(3/4) C d^(3/4).             (6)

The inner group includes the threshold |z|=1/2. Because there are
only finitely many root moduli, choose rho in (4d,6d) avoiding all of
them. Jensen's formula applies to the entire U_d: U_d(0)=1, and the
chosen circle has no zeros. The common growth bound gives

    sum_(|u|<rho) log(rho/|u|)
       <=log F(rho)<=K(6d)^(3/4).                        (7)

Every term in this Jensen sum is nonnegative. For 0<|u|<=2d,

    1+d/|u|=(|u|+d)/|u|<=3d/|u|<rho/|u|.

Consequently (7) pays the full logarithmic moment, even for roots
arbitrarily close to u=0:

    sum_(|u|<=2d) log(1+d/|u|)<=K(6d)^(3/4).             (8)

There is no need for an unproved uniform lower bound on |u|. Using
(4), (8) and C028f's closed-disk count at t=2d gives

    sum_(|u|<=2d) integral_I |h_(d/u)(x)| dx
       <=K(6d)^(3/4)+(2+log2) B(2d)^(3/4).              (9)

All radii used in the C028f growth, count and tail bounds are at least
one because d>=3. Roots on |u|=2d are included in (9); none is lost
in (6). Roots on |u|=rho are excluded by the choice of rho, including
any multiple roots. Its possible dependence on d affects no constant.

### Summation and the degree limit

Each factor in (3) is integrable by (4), and there are exactly d
factors. Thus the triangle inequality under a finite sum, (6) and (9)
give

    integral_I |log|P_d(x)/x^d|| dx
      <=[K*6^(3/4)+2^(3/4)*(C+(2+log2)*B)] d^(3/4)
       =D d^(3/4),

where C=4B. Divide by d>0 to prove (1); the degree-independent finite
D then implies convergence to zero. No infinite root sum, convergence
of individual roots, limit under an integral or uniform pointwise
lower bound on P_d has been used. Logarithmic spikes at real roots
are allowed and were fully integrated before taking the degree limit.

The downstream comparison is with C029f's positive-real region, not
an input from C029f. C028d's full signed-height identity concerns a
translated reference and the whole line; (1) does not estimate its
remaining complement. The local limit therefore leaves C028b's
RH-equivalent height and C029f's fixed-q obstruction unchanged.

### Separate proof audit1970 (2026-11-20)

Independently replayed (1) under assessment1968, separately approved
in1969. The bound passes without changing its statement, constant or
mathematical inputs. This verifies a local classical specialization;
it does not establish a theorem beyond the inspected source methods.

Direct substitution in the finite coefficients gives
U_d(d/x)=sum_j binom(d,j)b_j x^(-j)=P_d(x)/x^d.
The leading coefficients are respectively b_d/d^d and 1, and their
constant coefficients are 1 and b_d. Thus each has exactly d nonzero
roots. At u!=0, the map d/u is analytic with derivative -d/u^2!=0;
the identity P_d(d/u)=(d/u)^d U_d(u) preserves the order of every
zero. This checks both the scaling and all multiplicities, rather
than merely comparing root locations. Monicity then gives (3).

For the general factor estimate, the two parts must be bounded
separately. The upper modulus bound |1-z/x|<=1+|z| gives the positive
part in (4), since |x|>=1. Also
(-h_z)_+=(log|x|-log|x-z|)_+<=log2+(-log|x-z|)_+.
Replacing |x-z| by the smaller |x-Re z| increases this last bound.
Its positive logarithmic singularity is supported on an interval of
radius one and its full real-line integral is exactly 2. Hence the
bound includes an entire neighborhood even for a multiple real root
at an endpoint. Assigning values at the finitely many singular points
does not discard any positive-measure set. Summing these two positive
part estimates proves absolute integrability and precisely (4).

For the small-factor estimate, 0<=r=|z/x|<1/2 implies
log(1+r)<=-log(1-r)<=2r. Both signs of h_z are therefore covered
by (5). The strict outer group |u|>2d is exactly this case under
z=d/u. Its total cost is
2d*C*(2d)^(-1/4)=2^(3/4)*C*d^(3/4).
The equality case |u|=2d is instead in the closed inner group, so
the argument uses no unproved strict bound at a threshold root.

For that inner group, finiteness of the root multiset supplies a
radius rho in (4d,6d) without a boundary root. The imported Jensen
formula applies because U_d is entire and U_d(0)=1, with no pole or
origin correction. Its boundary logarithmic mean is bounded above
by log F(rho)<=K*(6d)^(3/4). All included root weights are positive.
Every inner root satisfies
log(1+d/|u|)<=log(3d/|u|)<log(rho/|u|).
Thus the complete logarithmic moment in (8), including arbitrarily
small nonzero u and each repeated factor, is paid by the same Jensen
sum. The closed count is at most B*(2d)^(3/4). Equation (4) then
adds exactly (2+log2)*B*(2d)^(3/4) to this moment bound. All calls
to the growth, count and tail inputs have radius at least one.

Adding the two groups yields
K*6^(3/4)+2^(3/4)*(C+(2+log2)*B)
=K*6^(3/4)+2^(3/4)*B*(6+log2)=D,
using C=4B. The triangle inequality is applied to exactly d
integrable factors before division by d. The only degree limit is
D*d^(-1/4)->0 with fixed finite D. No infinite root sum, degree
limit inside an integral, real-rootedness or pointwise lower bound
is used. The sole direct notebook input remains C028f, including
audit1518; this bounded audit does not recertify its upstream Xi
identification. C028b/d and C029f remain context, not new inputs.
The full-window and RH-equivalent conclusions remain unproved.

## Mathlib

Not checked. Full matching real-interval uniform-family coverage is
unknown, as is the available combination of supporting Jensen and
Lebesgue logarithmic-integrability results. No absence or formal
verification is claimed. The informal argument above explicitly checks
scaling, singular integrability, multiplicities, boundary radii, the
logarithmic moment, the constants and the sole final degree limit.
Audit1970 adds no claim of formal coverage or formal verification.
