# Lemma 684: fixed central displacement support cannot suppress the joint response

## Hypotheses

Use L666's family. Thus q>=1 is an integer, n=12q+3,
M=4q+1=n/3, x=-d=-5/4, R=11/8, U=121/64, alpha=27/10,
h=alpha/n, and t_j=j/n for 0<=j<n. The original unit-residue nodes are

    Z_e={x} union {x+i*h*(m+1/2+e_m): -2q<=m<2q},
    e_m real, |e_m|<=1/8.

Keep the full products, including j=0 and the denominator angle 1/u:

    B_u(v)=product_(0<=j<n) R*(v-t_j*u)/(U-t_j*v/u),
    W_a(u)=B_u(x)/B_u(a),
    F_(n,e)(u,z)=sum_(a in Z_e) W_a(u)/(R-a*z),
    D_(n,e)=mean_(|u|=1) sum_(a in Z_e) |W_a(u)|^2/(U-|a|^2),
    V_(n,e)=max_(|u|=|zeta|=1) |F_(n,e)(u,zeta/32)|.

The mean is normalized. A single displacement vector is used for all
u and z. Fix an integer L>=1 independently of n, require 2q>=L,
and restrict only the displacement support:

    e_m=0 whenever m is outside {-L,-L+1,...,L-1}.          (1)

The 2L remaining displacements are independent; no symmetry is assumed.
They may depend arbitrarily on n within their permitted cube. The
unshifted lattice outside (1), and every original unit residue, remain.

## Conclusion

For each fixed L there are b_L>0 and N_L<infinity such that, for every
admissible n>=N_L and every vector satisfying (1),

    V_(n,e) >= b_L.                                      (2)

More precisely, with sigma^2=137/5000, uniformly over that cube,

    V_(n,e)/[n*exp(-n/48)*sqrt(D_(n,e))]
      >= b_L*sqrt(3*sigma^2)*exp(-3)
                    *n^(-3/2)*exp(79*n/30000) -> infinity. (3)

Consequently the approved norm bound holds with c=1 after an onset
depending on L for this subfamily. Neither b_L nor N_L is asserted
uniform in L. No estimate for displacement support growing with n is
proved. In particular (2)--(3) do not establish the approved bound on
the full cube, whose permitted support grows linearly with n.

The proof supplies an explicit fixed-L convergence error, but its
positive limiting minimum is noneffective. This is a local subfamily
advance, not an RH candidate or a resolution of H/support, realization
or mixed signs. The result has not had a separate critical audit.
The POTENTIALLY_NEW classification records the prior bounded comparison,
not certified originality beyond the sources checked.

## Proof

### 1. Scope, known inputs and the distinction from fixed-angle cancellation

Reuse the unchanged invocation-start EXPLORE assessment
`drafts/literature/2026-11-03-inner-spatial-rational-response.md`.
This is an intermediate estimate inside its exact family and norm
target. The relevant local search found no fixed-central-support
angular-arc result in L664/L666/L669--L671 or the displaced-family
working and source records. That search does not establish novelty.

L669 allows arbitrarily high cancellation at u=-1 with its constants
and number of controls depending on the order. It does not imply
cancellation on a fixed arc. L682 controls only the highest spatial
moment. The L649/L650 recovery stops and L666's parked scalar-energy
derivative are not inputs to a lower bound here. No absolute error is
subtracted from an unproved relative-energy estimate.

We use the audited contour bounds in L664 Sections 2--4 and the audited
diagonal envelope in L661, equation (3). The standard contour input is
R. W. Howell and J. H. Mathews, *Complex Analysis*, online edition,
[Section 8.1, Theorems 8.1.5 and 8.1.7](https://complexanalysis.org/web/sec_residue-thm.html),
as already inspected and specialized in L664. The change needed here
is an explicit angular perturbation charge and replacement of its
spatial polynomial by a bounded holomorphic resolvent; both are
justified below. No quadrature or general sampling theorem is reproved.

We also use the standard identity theorem for holomorphic functions:
zeros accumulating inside a connected open domain force the function
to vanish identically, and the extreme value theorem on a compact
set. The exact analytic functions, accumulation point and compact set
are specified in Section 4. The elementary logarithm-series bounds
below make the new finite-n uniformity explicit; they are not claims
of a new general approximation theorem.

L666 proves |a|<R, distinct nonzero nodes and positive denominators
in D throughout its whole displacement cube, so they hold under (1).
The anchor contributes 64/21 to D. All the norms and ratios here are
finite, and D is strictly positive.

### 2. The undisplaced response on a fixed angular arc

Put r=1/32, delta_*=1/90000 and

    u_theta=-exp(i*theta),    |theta|<=delta_*.

We claim that for n>=183, uniformly in this arc and |z|<=r,

    |F_(n,0)(u_theta,z)-1/(R-x*z)|
                              <=1000*n*exp(-n/6000).     (4)

Here 0 means that every displacement is zero. In L664 take its grid
spacing h'=2h=27/(5n) and its offset delta=1/4. The two positive
grids are h*(2l+1/2) and h*(2l+3/2), 0<=l<q, together with their
negatives. These are exactly the present 4q undisplaced nonanchor
nodes. The anchor is separate and has residue one.

Use L664's positively oriented y-rectangle

    Gamma_n=boundary([-Y_n,Y_n]+i[-b,c]),
    Y_n=q*h', b=1/50, c=1/200,
    omega=2*pi/h',
    K(y)=i*omega/[exp(i*omega*y-pi*i/2)-1]
                       +i*omega/[exp(i*omega*y+pi*i/2)-1].

Its poles inside are exactly those 4q nonanchor ordinates, with
residue one and no boundary poles. On its closed interior write
a=x+i*y. L664's explicit bounds give

    |a|>=123/100>1,       |a|<4/3<R.

For every |u|=1 the denominators a-t_j*u and U*u-t_j*x are
nonzero on a neighborhood of this rectangle. Also U*u-t_j*a is
nonzero there. The resolvent 1/(1-a*z/R) is holomorphic in y and

    |1/(1-a*z/R)| <= 1/(1-1/33)=33/32<33              (5)

for |z|<=r. Thus the same residue theorem gives the exact identity

    F_(n,0)(u,z)=1/(R-x*z)
       +(1/(2*pi*i*R)) integral_(Gamma_n)
                     W_(x+i*y)(u)*K(y)/(1-(x+i*y)*z/R) dy. (6)

There is no infinite spatial sum or remainder in (6).

Here is a uniform charge for changing the angular variable. Directly
differentiate the rational continuation of the complete product:

    d_theta log W_a(u_theta)
      =sum_j [-i*t_j*u_theta/(x-t_j*u_theta)
               +i*t_j*u_theta/(a-t_j*u_theta)
               +i*U*u_theta/(U*u_theta-t_j*a)
               -i*U*u_theta/(U*u_theta-t_j*x)].          (7)

The notation means W'/W and does not require a global logarithm.
The j=0 terms cancel in this derivative; the constant x/a factor
is still in W. The four absolute bounds per j are at most

    4, 100/23, 363/107, 121/41,

respectively, whose sum is strictly less than 15: the last three
are less than 9/2, 7/2 and 3. These estimates use |u|=1,
|x|=5/4, 123/100<=|a|<4/3 and U=121/64. Since W is nonzero
throughout this domain, integrating the real part of (7) gives

    |W_a(u_theta)|<=exp(15*n*|theta|)*|W_a(-1)|.         (8)

Apply L664's contour estimates to (6), using (5) in place of its
bound 33 for the full spatial polynomial. Its upper/side contribution
has bound (2376/5)*n*exp(-n/3000), and its complete lower-edge
tail starting at frequency 2 has bound
(792/5)*n*exp(-n/3000). These are L664 (13) and (15); their
proofs use only holomorphy and that same bound 33 for the spatial
factor. The lower-edge frequency 1 has coefficient
cos(2*pi*delta)=cos(pi/2)=0, exactly. Thus no frequency-shift term
is missing. At the perturbed angle each entire edge estimate acquires
at most exp(15*n*|theta|), by (8). The constants sum to
3168/5<1000, and

    1/3000-15*delta_*=1/6000.

This proves (4). All estimates hold on the moving complete rectangle,
not just at endpoint samples. The same vector and exact node census
are used for all angles. The proof imports L664's previously checked
edge bounds, not a new numerical certificate or a continuity assertion
with an n-dependent neighborhood.

### 3. Uniform local-node expansion, with the finite-n error paid

On the annulus d/U<|u|<d define the holomorphic function

    kappa(u)=alpha*integral_0^1
                    [1/(d+v*u)-v/(U*u+d*v)] dv.          (9)

The denominators are nonzero there, uniformly on compact subannuli
and v in [0,1]. Integration and differentiation in u are therefore
valid there, for instance by uniform local Taylor expansion. For
|u|=1 put

    A_j(u)=1/(d+t_j*u), B_j(u)=t_j/(U*u+d*t_j),
    kappa_n(u)=(alpha/n)*sum_j(A_j(u)-B_j(u)).

Then |A_j|<=4, |B_j|<=64/41<2 and |kappa(u)|<=6*alpha.
For real |t|<=L, exact product division gives

    W_(x+i*alpha*t/n)(u)
          =product_j (1-i*alpha*t*B_j(u)/n)
                            /(1-i*alpha*t*A_j(u)/n).     (10)

For n>=8*alpha*L both logarithm-series arguments have modulus
at most 1/2. The series at 1 satisfies
|log(1+w)-w|<=|w|^2 for |w|<=1/2, since
sum_(k>=2)|w|^k/k<=|w|^2/[2*(1-|w|)]. Consequently its finite sum
ell_n(t,u), whose exponential is (10), obeys

    |ell_n(t,u)-i*kappa_n(u)*t|<=20*alpha^2*L^2/n.       (11)

This includes all n factors. For the integrand in (9), differentiation
in v has modulus at most

    16+U/(U-d)^2 = 16+7744/1681 < 21.

Integrating the Lipschitz error separately over each interval
[j/n,(j+1)/n] gives the uniform left-sum bound

    |kappa_n(u)-kappa(u)|<=21*alpha/(2*n).

Define the finite, explicit constants

    A_L=20*alpha^2*L^2+(21/2)*alpha*L,
    E_L=A_L*exp(6*alpha*L+1),
    C_0=1/[R*(1-r)],
    C_1,L=r*alpha*L/[R^2*(1-r)^2],
    J_L=C_0*E_L+exp(6*alpha*L)*C_1,L.

For n>=max(8*alpha*L,A_L), (11) yields

    |W_(x+i*alpha*t/n)(u)-exp(i*kappa(u)*t)|<=E_L/n.    (12)

Indeed the exponent difference has modulus at most A_L/n, and
|exp(w)-1|<=|w|*exp(|w|). The factor exp(6*alpha*L) bounds
|exp(i*kappa(u)*t)|. No convergence uniform in a growing L is
inferred by suppressing these constants.

For the actual local nodes t=m+1/2+e_m and their undisplaced
counterparts t=m+1/2, one has |t|<L and |a|<R. Therefore, for
|z|<=r,

    |1/(R-a*z)|<=C_0,
    |1/(R-a*z)-1/(R-x*z)|<=C_1,L/n.

Combining these inequalities with (12) gives, for each such node,

    |W_a(u)/(R-a*z)-exp(i*kappa(u)*t)/(R-x*z)|<=J_L/n.  (13)

Set tau_m=m+1/2, and for e in the compact cube [-1/8,1/8]^(2L)
define the entire function of w

    Phi_e(w)=1+sum_(m=-L)^(L-1)
               [exp(i*w*(tau_m+e_m))-exp(i*w*tau_m)].    (14)

The exact difference F_(n,e)-F_(n,0) has precisely these 2L node
replacements, with unchanged unit residues. Subtract the paired
approximations (13), sum them, and use (4). Uniformly in e, the
fixed arc and |z|<=r, for n satisfying the preceding onsets and
2q>=L, one obtains

    |F_(n,e)(u,z)-Phi_e(kappa(u))/(R-x*z)|
      <=epsilon_L(n),
    epsilon_L(n)=1000*n*exp(-n/6000)+4*L*J_L/n -> 0.    (15)

The limit in (15) is for each fixed L. Both the exponential lattice
error and the complete finite-replacement error have been charged.

### 4. Escape from cancellation on an entire arc

The phase in (9) is not constant near u=-1. Its derivative there is

    kappa'(-1)=alpha*integral_0^1
            v*[-1/(d-v)^2+U/(U-d*v)^2] dv < 0.          (16)

All denominators are positive in the displayed real comparison.
For v>0 the bracket is strictly negative because

    R*(d-v)<U-d*v,

which is equivalent to (d-R)*(R+v)<0. Here d<R. Thus the
analytic arc theta -> kappa(-exp(i*theta)) has nonzero derivative
at zero and contains infinitely many distinct values accumulating
at kappa(-1).

For every e, Phi_e(0)=1. If Phi_e(kappa(u_theta)) vanished for
every |theta|<=delta_*, its zeros would have the just described
finite accumulation point in the complex plane. The identity theorem
for the entire function Phi_e would make it identically zero,
contradicting Phi_e(0)=1. Hence

    mu_L = min_(e in [-1/8,1/8]^(2L))
                 max_(|theta|<=delta_*)
                         |Phi_e(kappa(u_theta))| > 0.    (17)

To justify the uniform strict inequality, the expression inside the
maximum is jointly continuous on the product of two compact sets.
Its maximum over theta is continuous in e, since the difference
between two maxima is bounded by the uniform difference of the
functions. The extreme value theorem gives an attained minimum in
e; the preceding zero-exclusion argument rules out value zero there.
Pointwise nonvanishing alone, without these compactness hypotheses,
would not suffice. No quantitative lower estimate for mu_L is claimed.

Evaluate (15) at the one permitted boundary point z=r, real. Its
limiting common factor is 1/(R+d*r)>0. After a fixed-L onset such
that epsilon_L(n)<=mu_L/[2*(R+d*r)],

    V_(n,e) >= max_(|theta|<=delta_*) |F_(n,e)(u_theta,r)|
            >= mu_L/[2*(R+d*r)] =: b_L > 0.             (18)

This proves (2). It uses only a subset of the joint observations,
without assuming that one angle works for every e. In this subfamily
the spatial resolvent has a common leading factor; the decisive new
point is the fixed angular arc, not a claimed new spatial positivity.
No symmetric pairing or positive signed cross term is used.

### 5. The original diagonal and the precise remaining gap

Use only L661 (3), with kappa_env=91/5000 and sigma^2=137/5000.
The L666 family is admissible and has exactly M=n/3 unit residues,
so its original squared-residue sum is M. Thus

    D_(n,e)<=n*exp(2*kappa_env*n+6)/(3*sigma^2).

Consequently

    n*exp(-n/48)*sqrt(D_(n,e))
       <=exp(3)/sqrt(3*sigma^2)
                    *n^(3/2)*exp(-79*n/30000),

since 1/48-91/5000=79/30000>0. Combine with (18) to obtain (3).
The lower expression in (3) tends to infinity for fixed b_L>0,
so it eventually exceeds one after a further L-dependent onset.
No estimate on D's mixed terms is involved: D retains its defining
positive separate-term diagonal throughout.

The remaining obstruction to applying this argument to the full cube
is explicit. The support may then have L=2q proportional to n;
(17) gives no rate for mu_L, and J_L grows exponentially in L.
The available error in (15) need not be smaller than its limiting
main term in that regime. It is invalid to interchange the fixed-L
limit and the minimum over the growing cube. L669's increasing-control
fixed-angle construction is therefore not contradicted or globally
excluded. No admissible normalized countersequence to the full joint
norm is supplied either.

L683's implication from a uniform full-family norm bound remains a
separate, unaudited transfer; it is not used in proving (2)--(3).
H/support and the actual-Xi realization and sign gaps remain open.
No numerical screen or mathematical script is a proof premise here.

## Mathlib

Full matching coverage for this fixed-central-support rational family,
its uniform arc estimate and its comparison with the original D has
not been checked. The standard analytic identity theorem, compact
extreme value theorem and logarithm-series estimates are the supporting
mathematics; no specific Lean theorem or formalization is claimed.
Unknown full coverage is not evidence of absence. L664 and L661 retain
their existing source and Mathlib qualifications.
