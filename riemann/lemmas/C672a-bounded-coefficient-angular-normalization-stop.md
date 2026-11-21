# Corollary 672a: bounded coefficients and exterior anchor values do not prevent angular cancellation

## Hypotheses

Use the undisplaced instance of L666, as in L672. Thus q>=1 is an
integer, n=12q+3, K=2q, h=27/(10n), x=-d=-5/4, R=11/8,
U=R^2 and t_j=j/n for 0<=j<n. The nonanchor nodes are

    y_r=h*(r+1/2), a_r=x+i*y_r, -K<=r<K.

Retain the complete rational continuation

    W_a(u)=(x/a)*product_(j=1)^(n-1)
                    [(x-t_j*u)/(a-t_j*u)]
                    *[(U*u-t_j*a)/(U*u-t_j*x)],
    W_x(u)=1.

All original residues in L666 remain one. The coefficients below are
auxiliary multipliers of these angular functions, not modified residues
in the original joint norm or its diagonal D. Put

    Q(z)=product_(r=-K)^(K-1)(z-i*y_r),
    lambda_r=exp(-(4/3)*i*n*y_r)*Q(0)/[(-i*y_r)*Q'(i*y_r)],
    beta_r=-lambda_r,
    T_n(u)=1+sum_(r=-K)^(K-1) beta_r*W_(a_r)(u).

These are exactly L672's interpolation coefficients and its residual,
with Q used here to avoid confusion with L688's Taylor polynomial.

## Conclusion

For every q>=1, the same coefficients at every angle satisfy

    |beta_j|=|beta_(-j-1)| < 2/[3*(2*j+1)], 0<=j<K,
    sum_r |beta_r| < (4/3)*(1+log K).                    (1)

In particular every nonanchor coefficient has modulus less than one.
At all the n-1 exterior points u_l=x/t_l, 1<=l<n, the rational
function T_n is regular and

    T_n(u_l)=1.                                        (2)

Nevertheless L672's audited uniform estimate gives

    max_(|u|=1) |T_n(u)| <= 5*exp(15)*n*exp(-11*n/1000). (3)

Consequently, for the proposed arc delta=1/90000,

    max_(|theta|<=delta) |T_n(-exp(i*theta))|
                      /exp(-n/1000)
                 <= 5*exp(15)*n*exp(-n/100) -> 0.       (4)

Thus even all of (1), the exact rational angular family, an unchanged
anchor coefficient, and every exterior normalization (2) cannot imply
the proposed angular-arc lower bound. This is an obstruction to a
relaxation of the inverse-Taylor argument. It is not a counterexample
for L688's prescribed multipliers P_n(a), for the joint resolvent V,
or for RH. No polynomial of degree floor(sqrt(n)), or polynomial with
subexponential coefficient observation cost, is asserted to realize
these beta_r together with value one at x. That lost polynomial
constraint is essential to any continuation of that approach.

This corollary specializes an existing audited counterexample and
adds its elementary coefficient-size and normalization checks. It is
not a new angular approximation theorem or certified original result.
The new checks have not received a separate critical audit. H/support,
L683's transfer audit, actual-Xi realization and signs remain open.

## Proof

### 1. Scope and inherited input

The invocation-start EXPLORE assessment is unchanged:
`drafts/literature/2026-11-03-inner-spatial-rational-response.md`.
The approved target is the original-D joint norm estimate. The present
bounded attempt was to obtain its sufficient inverse-Taylor arc bound
by propagating from exterior anchor values, using the subexponential
node-value bound. Testing the necessary relaxation led to L672, rather
than assuming that rational nonvanishing gives a quantitative bound.

Import precisely L672's coefficients (4), contour identity (5), and
the uniform angular error proved at the end of its Section 4. Its
Section 6 separately audits that estimate, including the complete
contour certificate. The displayed L2 conclusion alone would not
justify (3); the stronger uniform estimate in its proof does. That
audited result is reused, not recomputed from a certificate preview.
Its analytic import is the standard finite Cauchy residue theorem,
also recorded in L664 as R. W. Howell and J. H. Mathews, *Complex
Analysis*, [Section 8.1, Theorems 8.1.5 and 8.1.7](https://complexanalysis.org/web/sec_residue-thm.html).
No new source theorem, interpolation remainder, or general norm
comparison is assumed or reproved here.

L688's fixed-angle zero, L687's polynomial-zero cost and L686's
sparse-support lower bound do not settle this relaxation: (3) controls
the whole circle, but uses auxiliary coefficients. They are comparisons,
not mathematical inputs to (1)--(4). The bounded local duplicate check
found L672 describing its interpolation weights as possibly large;
its stated stop did not require or give (1). This does not establish
novelty beyond the sources checked.

### 2. Every interpolation coefficient is bounded

The phase factor in lambda_r has modulus one. Directly differentiating
Q at a distinct node, and canceling all powers of h, gives for j>=0

    |lambda_j|=|lambda_(-j-1)|=b_(K,j),
    b_(K,j)=product_(l=0)^(K-1)(l+1/2)^2
                  /[(j+1/2)*(K-1-j)!*(K+j)!].          (5)

Indeed the absolute differences from node j+1/2 to all other integer
half-nodes have product (K+j)!*(K-1-j)!. The extra denominator
factor is j+1/2, and Q(0) supplies the squared positive half-nodes.
Symmetry gives the same magnitude at -j-1. None of these factors
vanishes.

Let b_K=b_(K,0). The formula yields b_1=1/2 and, for K>=1,

    b_(K+1)/b_K=(K+1/2)^2/[K*(K+1)]
                 =1+1/[4*K*(K+1)].                    (6)

Using 1+s<=exp(s) and the telescoping sum of 1/[l*(l+1)],

    b_K <= (1/2)*exp((1/4)*(1-1/K))
          <= (1/2)*exp(1/4) < 2/3.                    (7)

The last strict inequality follows from
exp(1/4)=sum_(m>=0) (1/4)^m/m! < sum_(m>=0)(1/4)^m=4/3.
This also covers K=1; our family uses K>=2. For 0<=j<K, (5) gives

    b_(K,j)/b_K
       =[1/(2*j+1)]*product_(l=1)^j (K-l)/(K+l)
       <=1/(2*j+1),                                   (8)

with the empty product equal to one. Equations (7)--(8) prove the
first bound in (1). Summing the two symmetric halves and using
1/(2j+1)<=1/(j+1) gives

    sum_r |beta_r| < (4/3)*sum_(l=1)^K 1/l
                   <=(4/3)*(1+log K).

The last inequality follows by comparing 1/l, l>=2, with the
integral of 1/t on [l-1,l]. Thus no large-coefficient hypothesis is
responsible for the existing whole-circle cancellation.

### 3. Check every exterior normalization and its denominators

Fix 1<=l<n and put u_l=x/t_l, a negative real number of modulus
greater than d>1. For every nonanchor a=x+i*y_r and every j>=1,
the denominator a-t_j*u_l has nonzero imaginary part y_r. Also

    U*u_l-t_j*x=x*(U/t_l-t_j)!=0,

because U>1>t_j*t_l. The factor x/a is finite. Hence W_a is
regular at u_l, and its numerator factor x-t_l*u_l is zero.
It follows that W_a(u_l)=0 for every nonanchor a. The anchor is
the rationally canceled constant W_x=1, proving (2).

The same argument applies to any multipliers independent of u,
including the actual P_n(a) in L688 with P_n(x)=1. It therefore
explains exactly which normalization is shared by the attempted
filter and the counterexample. It does not identify their multipliers.

### 4. Apply the complete angular estimate and compare rates

The coefficients and undisplaced nodes are exactly those in L672.
Its Section 4 proves the uniform error in (3) for every |u|=1,
before passing to normalized L2. Apply that result with the sign
beta=-lambda. Restriction to the smaller arc can only decrease the
maximum. Dividing by exp(-n/1000) leaves the exponent

    -11*n/1000+n/1000=-n/100,

which proves (4). The right side tends to zero along n=12q+3,
uniformly over the whole circle already in (3). This is not a
finite-height sample or a zero at one angle.

The failed inference would discard the relation between all multiplier
values and one low-degree, low-cost polynomial in the pole parameter.
Bounds on those values and continued angular normalizations alone are
too weak. The actual unit-residue full-cube norm and the fixed P_n arc
bound remain undecided; auxiliary multipliers are not admissible
displacements or original residues.

## Mathlib

Full matching coverage of this family-specific coefficient bound and
normalization obstruction has not been checked. Supporting facts are
finite-product differentiation at simple roots, factorial products,
the exponential series, a harmonic-sum integral bound and L672's
already audited uniform interpolation estimate. No matching Lean
theorem or formal verification is claimed; unknown coverage is not
evidence of absence.
