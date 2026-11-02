# Lemma 661: the half-turn phase census has an excessive absolute contour cost

## Hypotheses

Retain L649's original family: n>=5, x=-d=-5/4, R=11/8,
U=R^2=121/64, eta=1/100, r_*=R-eta=273/200 and t_j=j/n,
0<=j<n. The distinct poles a have Re(a)=x, |a|<=r_*, and
include x. Their original positive integer residues r_a have total
mass M<=n/3. Poles and residues are common to all |u|=1. Define

    B_u(v)=product_(j<n) R*(v-t_j*u)/(U-t_j*v/u),
    W_a(u)=B_u(x)/B_u(a),
    c_k(u)=R^(-1) sum_a r_a W_a(u)(a/R)^k,
    G(u,zeta)=sum_(0<=k<M)c_k(u)zeta^k,
    D=sum_a r_a^2 mean_u |W_a(u)|^2/(U-|a|^2),
    H=max_u mean_zeta log|G(u,zeta)|.

All circle means and L2 norms are normalized. L658 supplies the
finiteness and attainment of H. The full grid and conjugated denominator
angle are retained. No symmetry, spacing or coefficient-integrality
assumption is made for the general envelope below.

For the additional contour assertion restrict n=6q+3>=1210 and set

    A_j=1/(d-t_j),       b_j=t_j/(U-d*t_j),
    phi_n(y)=sum_(j<n) [atan(A_j*y)+atan(b_j*y)]  (real y),
    phi_n(y_l)=pi*l,       -q<=l<=q,
    phi_n(Y_n)=pi*n/6,     Z={x+i*y_l:-q<=l<=q},
    r_(x+i*y_l)=1,         M=2q+1=n/3.                 (1)

Existence, uniqueness and admissibility are proved below; this is a
specific nonuniform census, not an inferred description of every family.
Let Gamma_n be the positively oriented rectangle in the complex y-plane
with Re(y)=+/-Y_n and Im(y)=+/-1/8. On its interior and boundary put

    S_n(y)=product_j [(1+i*A_j*y)(1+i*b_j*y)]
                          /[(1-i*A_j*y)(1-i*b_j*y)],
    K_n(y)=2i*phi_n'(y)/(S_n(y)-1),
    T_M(v)=sum_(0<=k<M)v^k,
    C_n(u)=(1/(2*pi*R))*integral_(Gamma_n)
           |W_(x+i*y)(u) K_n(y)|
           *||T_M(((x+i*y)/R)*zeta)||_2 |dy|.          (2)

The analytic branch of phi_n in (2) is specified in the proof. C_n
is an absolute contour cost, not the norm of the signed integral.
Write sigma^2=137/5000, kappa=91/5000 and rho_0=81/6250.

## Conclusion

For every original admissible family, at every angle and pole,

    |W_a(u)|<=exp(kappa*n+3),
    D<=sigma^(-2)*exp(2*kappa*n+6)*sum_a r_a^2.        (3)

The census (1) is admissible and 0<Y_n<27/100. Its full polynomial
has the exact finite-contour representation

    G(u,zeta)=(1/(2*pi*i*R))*integral_(Gamma_n)
               W_(x+i*y)(u) K_n(y)
               T_M(((x+i*y)/R)*zeta) dy.             (4)

In particular H<=log max_u C_n(u). However, the two short portions
next to just one contour endpoint already give

    C_n(1)>=exp(-rho_0*n-2)/(300*pi*R),
    C_n(1)/(exp(-n/32)*sqrt(D))
        >=c_* n^(-1/2) exp(9*n/100000) -> infinity,   (5)
    c_*=sqrt(3*sigma^2)*exp(-5)/(300*pi*R)>0.

Consequently

    2 log max_u C_n(u)-log D+n/16
                       >=9*n/50000-log n+2log c_*.   (6)

Thus bounding the signed contour (4) by its absolute cost cannot
certify this census as a countersequence to the paid logarithmic
criterion. The exact comparison uses the actual squared-residue D;
it is not obtained by replacing D by the anchor term.

This is a method-specific negative result, with the improved envelope
(3) as an additional input. It supplies neither a lower bound for H
nor an upper bound proving failure of the criterion. In particular
C_n can be much larger than the signed integral. Signed endpoint
cancellation, different contours or phase meshes, arbitrary integer
support, Xi realization, matching upper bounds and all-degree signs
remain unresolved. No RH candidate or certified originality is claimed;
the complete absolute-cost result has not received a separate critical
audit. L662's conceptual audit of 2 November 2026 checks the inputs
used there: (3), census admissibility, (4), and the real-endpoint bound
(13). It does not independently audit the cited source manuscripts.

## Proof

### 1. Scope, sources and the discriminating test

Reuse the unchanged invocation-start EXPLORE assessment
`drafts/literature/2026-11-02-localized-logarithmic-joint-moment.md`.
Its target remains the uniform paid-arc criterion, with the exact
integer census and full spatial polynomial. L658 shows that
2H-log D+n/16 tending to minus infinity would obstruct every allowed
arc. This turn tests that possibility through the prescribed nonuniform
phase coordinate, including its finite endpoints and all spatial modes.

L649 supplies the definitions. L659 supplies the exact single-factor
quartic test and its maximum-modulus extension; the refinement here is
needed for a strict comparison of this endpoint cost with the actual D.
L660's monomial phase stop, C645x's fractional lattice and the finite
logarithmic screen are contrasts, not assumptions or admissible
counterexamples. None of them gives the endpoint estimate (5).

Import the standard residue theorem with the simple-pole rule;
a precise reference already recorded in the notebook's contour source
comparison is R. W. Howell and J. H. Mathews, *Complex Analysis*,
[Section 8.1, Theorems 8.1.5 and 8.1.7](https://complexanalysis.org/web/sec_residue-thm.html).
Use the ordinary maximum modulus principle as in L659. Jensen's
inequality for the concave real logarithm gives
mean log|G|<=log||G||_2; L658's integrability and nonzero slices justify
this application, or equivalently its positive-epsilon limit. No new
general quadrature, inverse-function uniformity, sampling theorem or
Mahler lower bound is imported or reproved. The finite residue identity
below explicitly accounts for all poles in the chosen rectangle.

### 2. Sharper full-family diagonal envelope

For a=x+i*y, y real, L659's single-factor formula uses, for c=Re u,

    N_0=d^2+t^2+2*d*t*c,
    D_0=U^2+d^2*t^2+2*U*d*t*c.

Its ratio bound squared is at most L, for every real y and every
|u|=1, if the following degree-at-most-four polynomial is positive
on [-1,1]:

    F_(t,L)(c)=(L*D_0-t^2*N_0)*(L-1)*D_0*N_0
                    -t^2*(1-c^2)*(L*D_0-U*N_0)^2.     (7)

The leading coefficient of the underlying quadratic in y is positive
for L>1, by the identity checked in L659. Thus (7) proves the bound
for every y, not just for the candidate census. The same holomorphic
factor ratio and maximum modulus principle extend the bound at radius
t to every smaller radius.

Use t=j/128, 1<=j<=128. The exact rational choices L_j, the five
power coefficients of every (7), all cell endpoints and all Bernstein
coefficients are stored in
`scripts/one-sided-hankel/phase-census-endpoint-certificate.json`,
field `/factor_checks`. These are complete certificates on [-1,1].
For a power polynomial sum_(j=0)^4 p_j*c^j on a cell [l,r], the
Bernstein coefficient with index k is exactly

    sum_(i=0)^k [sum_(j=i)^4 p_j*binomial(j,i)*l^(j-i)*(r-l)^i]
                         *binomial(k,i)/binomial(4,i). (8)

Every coefficient is positive, the cells form contiguous full covers,
and their Bernstein basis functions are nonnegative and sum to one.
There are 581 cells and 2905 positive coefficients. An exact replay
checks every coefficient and cover. It also checks each stored quartic
against (7) at five distinct rational arguments, which proves equality
because both degrees are at most four. Thus sampled maxima used only
to propose L_j are not premises of (3).

Put e_j=L_j-1, so 0<e_j<1. The elementary integrated inequality
1/(1+v)<=1-v+v^2 for v>=0 gives

    (log L_j)/2 <= h_j=(e_j-e_j^2/2+e_j^3/3)/2.

The complete rational sums are

    (1/128)*sum_j h_j=13916666837251/768000000000000
                                              <91/5000,
    sum_j h_j=13916666837251/6000000000000 <3.          (9)

Each of the 128 radial subintervals contains at most n/128+1 of
the full grid points. Multiplying their bounds, including t_0=0,
therefore proves the first inequality (3). The pole clearance gives
U-|a|^2>=sigma^2. Square the pointwise bound, multiply by the
original r_a^2 and integrate to obtain the second inequality.

The initial certificate attempted 9/500 in place of 91/5000 and
failed (9). It is preserved in
`scripts/one-sided-hankel/phase-census-endpoint-initial-failed.json`.
The weaker passing value still leaves the strict exponent gap in (5).
No failed inequality or diagnostic value is used as a premise.

### 3. The exact integer census and its finite endpoints

Every A_j is positive and 0<=b_j<2, so phi_n is real, odd and
strictly increasing. To locate its endpoint write

    f_Y(t)=atan(Y/(d-t))+atan(t*Y/(U-d*t)),  Y=27/100.

Both arguments, and hence f_Y, increase on [0,1]. Comparing the
complete n-term left sum to the integral gives

    phi_n(Y)>=n*integral_0^1 f_Y(t)dt-[f_Y(1)-f_Y(0)]. (10)

The bracket is less than pi<4. A separate 128-cell left Riemann
lower bound, computed entirely with rational arithmetic, gives

    integral_0^1 f_Y(t)dt
       >=33735471548097/64000000000000 >11/21>pi/6.    (11)

Here the last inequality uses the classical Archimedes bound pi<22/7.
For clarity, the arctangent lower bounds in this certificate are finite
and rigorous: for 0<=z<=1/2,

    atan z >= sum_(k=0)^7 (-1)^k*z^(2k+1)/(2k+1).

The omitted remainder is the integral of t^16/(1+t^2)>=0.
For 1/2<z<=1 use atan z=atan(1/2)+atan((2z-1)/(2+z));
for 1<z<=27/25 use
atan z=atan(1/2)+atan(1/3)+atan((z-1)/(z+1)).
All reduced arguments are in [0,1/2], and the angle sums stay on
the usual arctangent branch. Each finite rational lower bound is rounded
down to denominator 10^12 before summation. Every argument, raw bound
and outward-rounded value is stored in `/phase_riemann_rows` and replayed.

The rational difference between the middle quantity of (11) and 11/21
is 4444902510037/1344000000000000; its product with 1210 exceeds 4.
Consequently (10) implies phi_n(27/100)>pi*n/6 for n>=1210.
Strict monotonicity and continuity give the unique Y_n in (0,27/100).
Since pi*n/6=pi*(q+1/2), there are unique nodes y_l in (-Y_n,Y_n)
with the phases (1), and no other integer-phase nodes in that interval.
The anchor y_0=0 is included, all 2q+1 nodes are distinct, and their
unit residues have total mass exactly n/3. Finally

    r_*^2-d^2-(27/100)^2=9113/40000>0,

so all poles satisfy the original radius restriction. The census is
fixed before varying u; no angle-dependent replacement of poles occurs.

### 4. The exact contour and all spatial modes

On the simply connected strip |Im y|<1/4 define phi_n as the
analytic primitive, vanishing at zero, of

    phi_n'(y)=sum_j [A_j/(1+A_j^2*y^2)
                                      +b_j/(1+b_j^2*y^2)]. (12)

Its possible singularities are at +/-i/A_j and, for b_j>0,
at +/-i/b_j. They lie outside this strip: 1/A_j=d-t_j>1/4
and 1/b_j>41/64. The primitive agrees with the real arctangents.
Taking the logarithmic derivative and the value at zero verifies
S_n=exp(2i phi_n) there. In particular S_n has no zeros or poles
in the closed rectangle.

For any positive A, |(1+i*A*y)/(1-i*A*y)|<1 in the upper half-plane
and >1 in the lower half-plane. Hence S_n(y)=1 inside the strip
only on the real line. By (12), its solutions there are simple; the
ones inside Gamma_n are exactly y_l, -q<=l<=q. At each of them
K_n has residue one. There are no boundary poles: on the real
crossings y=+/-Y_n one has S_n=-1, and off the real line |S_n|!=1.

The factor W_(x+i*y)(u) is holomorphic on a neighborhood of the
closed rectangle. Indeed Re(x+i*y)<=-d+1/8=-9/8<-1, so its
possible pole locations x+i*y=t_j*u lie outside; its angular
denominators U*u-t_j*x do not vanish. The finite polynomial T_M
is entire in y. The residue theorem therefore gives (4), for every
u and zeta on their circles, without an infinite lattice or an
uncontrolled quadrature limit. This also includes every alias through
the exact kernel rather than dropping any sampling term.

Apply the triangle inequality to the integral of the finite vector
of M coefficients. Its Euclidean norm equals the spatial L2 norm
by finite Fourier orthogonality. Thus ||G(u,.)||_2<=C_n(u), and
Jensen's inequality gives H<=log max_u C_n(u). The costs are finite
and continuous in u, so this maximum exists. The whole T_M, not just
its constant term, remains in the cost (2).

### 5. A mandatory endpoint cost at u=1

At u=1 put A_j^+=1/(d+t_j) and b_j^+=t_j/(U+d*t_j). Direct
division of the original full product gives

    W_(x+i*y)(1)=product_j (1-i*b_j^+*y)/(1-i*A_j^+*y).

At any real 0<=Y<=27/100, using log(1+v)<=v,

    log|W_(x+i*Y)(1)|
       >=-(Y^2/2)*sum_j 1/(d+t_j)^2
       >=-(81/6250)*n-729/31250 >-rho_0*n-1.          (13)

For the second step the decreasing left-sum bound is

    sum_j 1/(d+t_j)^2
        <=n*integral_0^1 dt/(d+t)^2+1/d^2
        =(16/45)*n+16/25.

This is an estimate for the full endpoint product. It does not drop
the endpoint from a limiting integral.

Consider the portion y=Y_n+i*s, |s|<=1/(100n), on the right
vertical side. In the larger strip |Im y|<=1/16 all factors
1+/-i*A_j*y and 1+/-i*b_j*y have modulus at least 3/4.
The partial-fraction form of (12) therefore gives

    |phi_n'(y)|<=(32/3)*n,       |phi_n''(y)|<=(320/9)*n<36n.

For real Y in [0,27/100], the function A/(1+A^2*Y^2), for
4/5<=A<=4, has its minimum at an endpoint of that A-interval.
Both endpoint values at Y=27/100 exceed 3/4. Thus
phi_n'(Y_n)>3n/4, and on the short segment

    |phi_n'(Y_n+i*s)|>=3n/4-36/100>=n/2,
    |phi_n(Y_n+i*s)-phi_n(Y_n)|<=8/75.

Since S_n(Y_n)=-1, it follows that

    |S_n(Y_n+i*s)-1|<=1+exp(16/75)
                        <=1+75/59<3,
    |K_n(Y_n+i*s)|>=n/3.                              (14)

The exponential bound follows from exp(v)<=1/(1-v), 0<=v<1,
by comparing its power series. No complex phase is replaced by a
real approximation in the location of the nodes or the kernel.

Similarly A_j^+<=4/5 and b_j^+<1/3. The logarithmic derivative
of their product is bounded in modulus by 2n on |Im y|<=1/16.
Its factors have no zeros or poles there. Integrating that derivative
along the short segment and using (13) gives

    |W_(x+i*(Y_n+i*s))(1)|>=exp(-rho_0*n-2).          (15)

The spatial factor in (2) has L2 norm at least one everywhere,
because its constant coefficient is one. Retaining this lower bound
does not replace the spatial polynomial in (4). The segment length
is 2/(100n). Restricting the nonnegative integral (2) to it and
using (14)--(15) proves the first inequality (5).

For the actual census, sum r_a^2=M=n/3, so (3) gives

    D<=n*exp(2*kappa*n+6)/(3*sigma^2).

Dividing the endpoint cost by exp(-n/32)*sqrt(D), and using

    1/32-kappa-rho_0=9/100000>0,

proves the second inequality (5) and then (6). This division uses
an upper bound on the actual D in the direction needed for a lower
bound on the normalized contour cost. D itself has not been replaced
by an unsquared, fractional or sampled quantity.

The absolute cost is only an upper bound on the signed response.
Therefore (6) stops this absolute-contour certification mechanism,
not the census itself or the paid-logarithmic target. Establishing
signed cancellation strong enough to overcome this endpoint would
be additional mathematics, not a consequence of the contour identity.

### 6. Verification and qualifications

Reproduction commands, relative to the notebook, are

    python3 scripts/one-sided-hankel/phase-census-endpoint-certificate.py
    python3 scripts/one-sided-hankel/phase-census-endpoint-replay.py

The replay checks all 128 quartic identities, all 581 complete cover
cells and 2905 Bernstein coefficients, all 128 phase rows, outward
rounding, the onset and the strict exponent comparison. Its full
arithmetic evidence is in the sibling replay JSON; the complete relevant
summary/comparison values and empty failures lists were inspected.
These are arithmetic checks, not a separate audit of the analytic proof.

The preliminary `phase-census-diagnostic.json` is explicitly nonrigorous:
it has no error enclosure and computes neither a finite-family H nor D.
Its sampled values are not mathematical premises. The failed stronger
rate certificate remains available, and its comparison logging was
corrected when the passing weaker threshold was selected.

## Mathlib

The reused assessment checked the supporting univariate
[MahlerMeasure module](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Polynomial/MahlerMeasure.html),
including `Polynomial.intervalIntegrable_mahlerMeasure` and
`Polynomial.logMahlerMeasure_eq_log_leadingCoeff_add_sum_log_roots`.
Here finite spatial integrability is inherited from L658; no totalized
logarithm or coefficient-integrality hypothesis replaces it. Full
matching Mathlib coverage for this nonuniform census, rational residue
kernel, exact envelope or absolute-contour obstruction has not been
checked. The rational scripts are not Lean formalizations, and unknown
coverage is not a claim of absence.
