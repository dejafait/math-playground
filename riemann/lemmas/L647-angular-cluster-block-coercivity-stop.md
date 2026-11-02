# Lemma 647: microscopic grouping has no uniform constant energy comparison

## Hypotheses

Use the saved angular family with n>=5, x=-d=-5/4, R=11/8,
U=R^2, eta=1/100 and t_k=k/n, 0<=k<n. The finite common pole
set Z contains x; its poles are distinct, have Re(a)=x and
|a|<=R-eta, and carry positive integer original simple-pole residues
r_a with M=sum r_a<=n/3. For |u|=1 define

    b_(u,t)(v)=R*(v-t*u)/(U-t*v/u),
    B_(n,u)(v)=product_(k<n) b_(u,k/n)(v),
    W_(n,a)(u)=B_(n,u)(x)/B_(n,u)(a),
    q_(n,u)(zeta)=sum_a r_a W_(n,a)(u)/(R*zeta-a).

Here u=i exp(i theta); the denominator therefore retains the conjugated
angle. Use C645g's normalized circle measure, H^2, strictly negative
H^2_- and largest Hankel norm. The same poles and residues serve every
angle. Partition the ordinate axis into half-open intervals of length
1/n, with any origin, and let G denote the nonempty groups of poles.
Write q_G for the corresponding partial sum and define

    E_n=mean_u ||q_(n,u)||_2^2,
    D_n=sum_G mean_u ||q_G||_2^2.                         (1)

The spatial L2 norm and the angular mean both use normalized measure.
The full energy E_n includes every within-group and cross-group term.

## Conclusion

There is an admissible sequence of these families, with a fixed finite
number of distinct poles and growing integer residues, such that
every group is a singleton, for every choice of interval origin, and

    E_n/D_n -> 0.                                       (2)

Consequently no uniform positive constant c can give E_n>=c D_n for
all sufficiently large n and all admissible families. Grouping at
scale 1/n does not justify that constant-factor comparison, even when
all groups are separated by more than 1/n.

This is only a stop on that sufficient shortcut. In fact the same
sequence has a positive, well-defined rate F_* satisfying

    lim_(n->infinity) log(sqrt(E_n))/n
      =lim_(n->infinity) log(sqrt(D_n))/n
      =F_*>1/10000000.                                  (3)

Thus its full constant-input response grows exponentially. It is NOT
a countersequence to the requested angular operator bound
c exp(-n/32). The cancellation in (2) has zero exponential rate:
log(E_n/D_n)/n tends to zero. In particular this result does not rule
out an exponential-loss comparison at the required squared rate 1/16,
or any other treatment of the complete signed energy.

The construction below is existential and exact. It uses all maximizers
of one explicitly defined analytic function, without assuming their
number, uniqueness or nondegeneracy. It supplies no effective onset.
The proof is author-checked and has not received a separate conceptual
audit. No certified novelty, Xi realization, sign theorem or RH solution
is claimed.

## Proof

### 1. Scope, normalization and the tested shortcut

The unchanged invocation-start
[EXPLORE assessment](../drafts/literature/2026-11-02-rotation-averaged-anchor-line-hankel.md)
covers the same common-pole family and angular Fourier/residue test.
The scoped duplicate search checked the C645 angular results, L646,
their associated 2 November attempts and the saved grouping continuation;
no prior constant block-coercivity obstruction was identified there.
C645o's negative cross entry and L646's exact-recovery stop are preserved.
Only C645g's normalization and C645o's full constant-input energy identity
are mathematical local inputs here; neither its residue sign certificate
nor any unproved general lower bound is used.

The operator convention is imported from L. Baratchart, S. Chevillard
and T. Qian, *Minimax principle and lower bounds in H2-rational
approximation*, J. Approx. Theory 206 (2016), 17--47, preprint v2,
24 March 2015, [Section 4, (17)--(19)](https://arxiv.org/pdf/1501.01161v2),
[DOI](https://doi.org/10.1016/j.jat.2015.03.004).
Scalar Fourier orthogonality/Parseval is imported from A. Levitt,
*Analyse de Fourier et applications*, version retrieved 2 November 2026,
[Theorem 1.3/Exercise 1.2 and Theorem 1.11/Corollary 1.12, printed
pp.6,8](https://www.imo.universite-paris-saclay.fr/~antoine.levitt/blog/fourier/article.pdf).
These are the primary statements inspected in that assessment; none is
reproved or asserted to evaluate (2).

Every rotated grid lies in |v|<1, whereas |a|>=d>1. All grid and
symbol denominators are nonzero on their boundary circles. For a finite
admissible family the exterior expansions converge uniformly in both
angles. The normalization therefore gives

    H_(q_(n,u)) 1=q_(n,u),
    ||1/(R*zeta-a)||_2^2=1/(U-|a|^2),
    E_n=sum_(a,b) r_a r_b mean_u[W_(n,a) conjugate(W_(n,b))]
                                      /(U-a*conjugate(b)).       (4)

The constant-factor comparison in the conclusion is a proposed
sufficient reduction, not a consequence of (4). The proof below uses
the complete vector q throughout; it never deletes a negative cross
term or replaces a signed energy by its diagonal.

### 2. An angular profile with finitely many strictly positive maxima

Fix epsilon=1/10000 and a0=x+i*epsilon. For |u|=1 put

    ell(v,t,u)=1/(v-t*u)+t/(U*u-t*v),
    L(v,u)=integral_0^1 ell(v,t,u) dt,
    F(u)=integral_0^1 log|b_(u,t)(x)/b_(u,t)(a0)| dt,
    z(u)=-i L(a0,u).                                    (5)

All functions are well defined. On the vertical segment v=x+i*y,
0<=y<=1/100, one has |v|<=63/50 and

    |v-t*u|>=d-t>=1/4,
    |U*u-t*v|>=U-63/50>5/8,
    |ell(v,t,u)|<=4+8/5<6,
    |partial_v ell(v,t,u)|<=16+64/25<20.                (6)

For v=x the combined expression for ell is

    ell(x,t,u)=(U-t^2)/[(x-t*u)*(U-t*x/u)].

If u=exp(i phi), the real part of its denominator is

    -d*(U+t^2)-t*(U+d^2)*cos(phi)
       <=-(d-t)*(U-d*t)<0.

Thus Re ell(x,t,u)<0 for every t in [0,1]. For 0<=t<=1/4,
bound the two real parts separately:

    Re[1/(x-t*u)]<=-(d-t)/(d+t)^2<=-4/9,
    Re[t/(U*u-t*x)]<=t/(U-d*t)<=16/101.

Their sum is <-1/4. Integrating first over [0,1/4] and then its
complement, and using (6) along the short vertical segment, gives

    Re L(x,u)<=-1/16,
    Re L(a0,u)<=-1/16+20*epsilon<-1/32,
    1/32<Im z(u)<=|z(u)|<6.                             (7)

At u=i a direct imaginary-part calculation yields

    Im ell(x,t,i)
      =t*(U-d^2)*(U-t^2)/[(d^2+t^2)*(U^2+d^2*t^2)]>0
                                                        (t>0).

On t in [1/4,1/2], use U-d^2>1/4, U-t^2>3/2,
d^2+t^2<2 and U^2+d^2*t^2<5. Consequently

    Im L(x,i)>3/1280.

Integration of the logarithmic derivative in v gives the exact identity

    F(u)=Re[-i integral_0^epsilon L(x+i*y,u) dy].         (8)

Together with (6), this proves

    F(i)>3*epsilon/1280-10*epsilon^2
         =43/320000000>1/10000000.                       (9)

Also F(1)<0. Indeed, for every t the squared modulus of b_(1,t)(x+i*y)
is

    U*((d+t)^2+y^2)/[(U+d*t)^2+t^2*y^2].

It is strictly increasing in y^2, because the numerator in its
derivative, apart from the positive factor U, is

    (U+d*t)^2-t^2*(d+t)^2
       =(U-t^2)*(U+2*d*t+t^2)>0.

This also covers t=0. Therefore each logarithmic ratio in F(1) is
negative.

For clarity, the analytic regularity used next is uniform. The integrands
ell(x+i*y,t,u), for 0<=y<=1/100 and 0<=t<=1, are holomorphic in u
on 3/4<|u|<6/5: their possible inner poles have modulus at most
(63/50)/U<3/4 and their outer poles have modulus at least d>6/5.
Integration preserves local uniformly convergent power series.
Equation (8) makes F(exp(i phi)) real analytic. It is nonconstant by
(9) and F(1)<0. Its derivative has isolated zeros: a nonzero real
analytic function has an isolated zero at the first nonzero Taylor
coefficient, and an accumulation of zeros would make it identically
zero by the identity theorem. Compactness of the circle then implies
that the maximizer set is finite. Denote it by

    A={u_1,...,u_K},   F_*=max_(|u|=1) F(u)>1/10000000.  (10)

It is nonempty. No unique or quadratic maximum is assumed.

### 3. Positive coefficients cancelling at every maximizer

Enumerate A in increasing angular order. Write beta_j=Im z(u_j)>1/32.
Recursively choose a nonnegative integer k_j such that

    h_j=(2*k_j+1)*pi/beta_j > 2+sum_(l<j) h_l,
    c_j=exp(-h_j*Re z(u_j))>0.

Such a choice always exists. Define the entire exponential polynomial

    P(w)=product_(j=1)^K (1+c_j*exp(h_j*w))
        =sum_(S subset {1,...,K}) alpha_S*exp(s_S*w),
    s_S=sum_(j in S) h_j,   alpha_S=product_(j in S) c_j. (11)

Empty sums and products give s_empty=0 and alpha_empty=1. All
coefficients are positive, and P(z(u_j))=0: its j-th factor is 1-1.
For distinct subsets, let j be their largest differing index. Then

    |s_S-s_T|>=h_j-sum_(l<j) h_l>2.                     (12)

This separation will make the groups singletons. P is not the zero
function, since P(w)>0 for real w.

We will also need that P(z(u)) is not identically zero on any angular
arc. The absolutely uniformly convergent Laurent expansion is

    L(a0,u)=1/a0+sum_(k>=1)
          [u^k/a0^(k+1)+a0^(k-1)*u^(-k)/U^k]/(k+1).   (13)

It follows by expanding the two denominators in (5) and integrating
t^k; the ratios are at most 1/|a0|<1 and |a0|/U<1. The coefficient
of u is 1/(2*a0^2), so z is nonconstant and holomorphic on the same
annulus. If P(z(u)) vanished on an arc, its holomorphic extension would
vanish identically. The connected image of that annulus under z would
then lie in the discrete zero set of the nonzero entire function P,
and hence be a singleton, a contradiction. This uses only the standard
identity theorem and zero isolation, not a saddle-point assertion.

### 4. Admissible common poles and integer residues

Put C=sum_S alpha_S, s_max=sum_j h_j, and, for all sufficiently large n,

    N_n=floor(n/(6*C)),
    a_(S,n)=a0+i*s_S/n,
    r_(S,n)=floor(N_n*alpha_S),
    Z_n={x} union {a_(S,n): S subset {1,...,K}},  r_x=1.   (14)

All numbers in (11) are fixed before n varies. Thus N_n tends to
infinity, all r_(S,n) eventually are positive integers, and
r_(S,n)/N_n tends to alpha_S. The empty-subset residue is exactly N_n.
For sufficiently large n, epsilon+s_max/n<=1/100, and therefore

    |a_(S,n)|<=63/50<R-eta,
    M_n=1+sum_S floor(N_n*alpha_S)<=1+n/6<=n/3.          (15)

The last inequality holds for n>=6. All poles have the required real
part and avoid every grid for every u. Their mutual ordinate gaps
exceed 2/n by (12). Their distance in ordinate from x is at least
epsilon>1/n eventually. Hence every interval of length 1/n contains
at most one pole, independently of its origin. These are simple poles
with positive integer residues, not repeated or higher-order poles.
If a sequence for every n>=5 is wanted, use Z_n={x}, r_x=1 before
this finite existential onset. None of these choices depends on u.

### 5. Uniform full-symbol limit and concentration of angular mass

Let W_0,n=W_(n,a0) and

    F_n(u)=log|W_0,n(u)|/n,
    Zeta_n=mean_u |W_0,n(u)|^2,
    dmu_n(u)=|W_0,n(u)|^2 dmu(u)/Zeta_n,

where dmu is normalized angular measure. Uniform continuity of the
integrands in (5) on the compact t,u sets gives uniform convergence
of their left Riemann sums. In particular F_n tends uniformly to F,
and n^(-1) sum_(k<n) ell(a0,k/n,u) tends uniformly to L(a0,u).
Their first derivatives in t are bounded on these compact sets, so
the errors could also be bounded by a constant times 1/n.

For each fixed offset s_S, integration along the vertical segment
and (6) give, uniformly in u,

    W_(n,a_(S,n))(u)/W_0,n(u)
      =exp(-i*s_S*[n^(-1) sum_(k<n) ell(a0,k/n,u)]
                                              +O(s_S^2/n))
      -> exp(s_S*z(u)).                                 (16)

This equality uses the integral of the logarithmic derivative of each
nonvanishing factor along that segment; no branch of log B is assumed.
There are only finitely many fixed offsets, so convergence is uniform
over S as well. Equation (6) bounds the exponent remainder by
10*s_S^2/n once the segment lies in the stated strip.

Remove only the anchor from the sum and factor its remaining full
response exactly as

    q_cluster(u,zeta)=N_n W_0,n(u) A_n(u,zeta),
    A_n(u,zeta)=sum_S [r_(S,n)/N_n]
         [W_(n,a_(S,n))(u)/W_0,n(u)]/(R*zeta-a_(S,n)).

The spatial denominators have modulus at least R-63/50>0. Rounding
in (14) has error at most 1/N_n per coefficient. Thus (16) implies
uniform convergence on both boundary circles:

    A_n(u,zeta) -> A(u,zeta)=P(z(u))/(R*zeta-a0).         (17)

In particular the squared spatial norms converge uniformly to
g(u)=|P(z(u))|^2/(U-|a0|^2), a continuous nonnegative function
vanishing on every point of A.

The probability measures mu_n concentrate on A in the following
precise elementary sense. For any open neighborhood V of A, the
maximum of F on its compact complement is strictly below F_*.
Choose gamma>0 for which that maximum is at most F_*-gamma.
A fixed open arc about a maximizer has F>F_*-gamma/4. Uniform
convergence of F_n, with error at most gamma/8, then bounds the
mass outside V divided by the mass on that arc by

    [1/mu(arc)]*exp(-n*gamma).

This tends to zero. For any continuous g vanishing on A, choose V
where |g| is arbitrarily small, and bound it on the complement.
It follows that integral g dmu_n tends to zero. Applying this to
the uniform limit of the norms in (17) proves

    mean_u ||q_cluster||_2^2/(N_n^2 Zeta_n)
       =integral ||A_n(u,.)||_2^2 dmu_n(u) -> 0.         (18)

For later use the same elementary upper/lower arc bounds give

    lim log(Zeta_n)/(2*n)=F_*>0.                         (19)

Indeed the upper bound uses sup F_n<=F_*+o(1); a fixed arc on which
F>F_*-gamma gives the lower bound, followed by gamma decreasing to zero.
These arguments do not exchange a limit with an uncontrolled angular
integral or assume a nondegenerate stationary point.

### 6. The full signed energy, the anchor, and the absolute rate

The anchor contribution is q_x=1/(R*zeta-x), with squared norm
K_x=1/(U-d^2). It has not been discarded. The triangle inequality
in the joint angular/spatial Hilbert space gives

    E_n<=2 mean_u ||q_cluster||_2^2+2 K_x.

By (18)--(19), E_n/(N_n^2 Zeta_n) tends to zero. Since the group
containing a0 is a singleton of residue N_n, its contribution yields

    D_n>=N_n^2 Zeta_n/(U-|a0|^2).

This proves (2), including every cross term. Also (16), bounded
residue ratios, and uniform spatial clearance give
D_n<=C_1 N_n^2 Zeta_n+K_x for a fixed finite C_1. Because
log N_n/n tends to zero, (19) proves the asserted rate for D_n
and the upper rate bound for E_n.

Here is the needed lower rate bound for E_n, so that a relative
cancellation is not mistaken for an absolute counterexample. Fix
0<gamma<F_*/4. By Section 3, every neighborhood of a maximizer
contains a point with P(z(u)) nonzero. Choose a closed arc of positive
length on which both F>F_*-gamma and ||A(u,.)||_2>c_gamma>0.
Uniform convergence in (17) makes ||A_n(u,.)||_2>=c_gamma/2 there
for large n; uniform convergence of F_n makes
|W_0,n(u)|>=exp(n*(F_*-2*gamma)). Thus, on that same arc,

    ||q_(n,u)||_2
       >=N_n |W_0,n(u)| ||A_n(u,.)||_2-||q_x||_2
       >=(c_gamma/4) N_n exp(n*(F_*-2*gamma))

for all sufficiently large n. The last step is valid since the
exponent is positive. Integrating its square gives the lower rate
F_*-2*gamma for sqrt(E_n). Letting gamma decrease to zero proves
(3). Positivity of E_n also follows directly from its nonzero
distinct simple-pole residues. Consequently its logarithm is valid.

### 7. Verification and exact scope of the method stop

The rational constant checks in (6)--(9) and (15), including actual
and required bounds, are reproduced by
`python3 scripts/one-sided-hankel/angular-cluster-coercivity-check.py`.
The complete arithmetic record is
`scripts/one-sided-hankel/angular-cluster-coercivity-check.json`.
Those checks do not replace the analytic construction, uniform
convergence or concentration proof above. No angular sample, numerical
maximizer list or finite-n matrix is used as evidence for (2).

The failed shortcut is a uniform constant lower comparison with the
sum of group energies. This is stronger negative evidence than one
negative Gram entry, but it stops neither clustering in general nor
the required full-energy threshold. Equation (3) explicitly leaves
an exponential-loss comparison untouched. The arbitrary-family
detector, actual-Xi layer isolation, other poles, census/clearance,
simultaneous realization, matching upper bounds and signs remain open.

## Mathlib

Full matching coverage for this positive-integer-residue angular
concentration construction has not been checked. No absence claim is
made. Supporting ingredients are normalized Fourier orthogonality,
finite rational Hardy symbols, the complex identity theorem,
uniform Riemann-sum convergence, compactness and Hilbert-space norm
inequalities. The inspected primary sources above cover the operator
and Fourier conventions, not this quantitative grouping comparison.
