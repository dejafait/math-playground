# L168 — The fourth ordered trace has a nonzero cubic limit

## Hypotheses

Keep precisely L167's hypotheses: SU(2), the relative fixed-link cube
D=(-4,4)^4, a=8/N through sufficiently fine admitted even meshes,
the direction-1 straight lower-rooted forest, the complete compact
L008 displacement, and both actual L010 probes at tau=1/16. Expand
at fixed mesh before refinement. All matrices use ordinary stored
coordinates. Full tensors precede forest restriction; both residual
subtractions, all action faces, normal end links, upper jump, constant
axial mode and full heat spectrum remain.

Let X_i be exactly L167(1), including its coefficient -1. Import the
continuum modes and heat coefficients of L080 and L145, with

    V_(k,nu)=f_(k,nu)/sqrt(lambda_k)
        -partial_nu integral_(-4)^(x_1)
                         f_(k,1)(r,x_T)/sqrt(lambda_k) dr,
                                                  nu=2,3,4,
    B_(i,R)=sum_(k,l)c_(i;kl) integral_D u_1 V_k dot V_l,
    g_G=-(1/4) integral_(T^3) XY(X-Y)^2/(X+Y+Z)^2.       (1)

The torus measure is normalized. X,Y,Z are respectively
4 sin^2(theta_2/2), 4 sin^2(theta_3/2), 4 sin^2(theta_4/2).
Use L145's established identity K_(i,R)=g_G B_(i,R).
Numerical signs/enclosures below additionally import L146's complete
heat inclusion with its stated IEEE binary64, underflow and upstream
moment/time qualifications. The analytic limit identity does not
require that numerical model.

## Conclusion

For both actual probes the fourth trace has the finite real limit

    lim_(a->0) a^3 X_i=(3/2)g_G B_(i,R)=(3/2)K_(i,R).   (2)

Under L146's numerical qualifications,

    -112.374 < lim a^3 X_3 < -79.2135,
    -41.3175 < lim a^3 X_6 < -29.124.                    (3)

Thus this complete ordered trace does not vanish at cubic scale.
It has no additional outside factor 3. It is only one part of
-kappa_0(f_(i,0),r_1,S_3): the second and third bulk traces and
L158/L159's two mixed branches still lack scaled limits/coefficients.
There is no complete-response sign, nonvanishing or compensation
conclusion. Other jets, finer powers/logarithm, finite matching,
interacting error <=c_box/2, continuum axioms and infrared finite
positive mass remain unresolved. This is local standard-method
progress and reuse of an already enclosed physical form, without a
claim of novelty beyond the sources checked.

## Proof

### 1. Establish the local half-line limit before freezing the trace

L167(3) gives the exact bulk order, with a subcubic remainder,

    X_i=sum_(k,l,c)c_(i;kl,a)
       Tr[B_(h_k t_c) Ghat_v Dhat^T B_(ell_b t_c) Fhat Ahat]
                                                       +O_i(N^2). (4)

The upper contribution is O(N log(eN)) and all three smooth-column
subtractions are included in that remainder. No action face has
been omitted. Fix k,l first. The row e in the entry expansion of
(4) belongs to a fixed compact interior enlargement S of the
support of A. The two vertex indices are endpoints of e and f.
For fixed offsets about e, as its physical midpoint tends to x,

    h_(k,e)/a -> V_(k,nu)(x),
    (ell_b)_(l,f)/a -> V_(l,mu)(x),                    (5)

uniformly on S. Only nu,mu=2,3,4 remain: the interior axial forest
columns are exactly zero. This is the actual forest lift, not the
unretracted relative mode. L150 section 2 gives its uniform smooth
extension and polynomial mode bounds; L080(5),(8)--(10) gives its
fixed-mode convergence and retains the constant prefix. Equivalently,
the same convergence for the unaveraged transverse edge follows by
the midpoint quadrature of that exact prefix and one transverse
incidence difference. All finite endpoint shifts in (5) tend to x.

Let g_4 be the infinite unscaled scalar Z^4 Green kernel, extended
diagonally to link components. Freeze u at x in the actual centered
endpoint/clover stencil and call its dimensionless generator K^0(u).
Define the translation-invariant symmetric residual principal part

    A^0(u)=(L^0 K^0(u)+(K^0(u))^T L^0)/2.               (6)

Here K_a has scale a^-1 in stored coordinates; (6) is the local
limit of a A, not of A. L018(2) and L028's compositions justify
this assertion: the finitely many coefficients u_a tend to u(x),
their neighbor differences tend to zero, and a Q_3,a Q_6 tend to
zero on each fixed stencil. Both subtractions remain in the finite
matrix throughout this limiting argument. L164(5) and L166(7)
give uniform local convergence of Sigma and its differences to
g_4. Consequently, for fixed offsets,

    a(Sigma A)_(z,e) -> (g_4 A^0(u(x)))_(z-e,nu).        (7)

This order also follows by transposing A Sigma, since both finite
matrices are symmetric; commutation is not assumed.

Now use the actual prefix in F A. Its input component is 1 and it
sums every edge below its output vertex w. L166(5), after multiplication
by a, bounds each summand by C[r^-4+N^-4]. For bounded w-e, the
axial tail farther than J from e is at most C J^-3+C N^-3,
uniformly over e in S. The lower root is distance at least cN
from this compact observation, while the upper end is not part of
the prefix. First truncate at J, apply (7), and then let J tend to
infinity. This proves, uniformly on S at each bounded offset,

    a(F A)_(w,e) -> (Phi_- g_4 A^0(u(x)))_(w-e,nu),     (8)

where Phi_- sums component-1 edges at w_1-j-1/2, j>=0, with
the transverse coordinate of w fixed. Its half-line is retained.
The axial sum in (8) is absolutely convergent; no low-frequency
or constant-mode deletion is involved. The all-Dirichlet vertex
Green difference in L167(9) likewise converges locally to
g_4 D^T, by its heat-image argument: with both indices bounded
about a compact point, nonidentity images are separated by cN
and contribute O(N^-3).

### 2. Control every omitted spatial offset and the full heat sum

The normalized entry product in (4) is bounded, up to a fixed
polynomial p(k)p(l) and endpoint/color multiplicities, by

    a (r^-3+N^-3)(1+m)^-3,
    r=1+dist(e,f),  m=|e_T-f_T|.                       (9)

This is precisely L167(8)--(12): each exterior column supplies a,
and F A supplies a^-1. The infinite decaying product is summable
over all four-dimensional f-e. Indeed its axial sum is at most
C(1+m)^-2, and its transverse shell sum is at most
C sum_(m>=0)(1+m)^-3. Thus its tail outside any fixed offset ball
tends to zero. The finite constant part has total at most
C N^-2 log(eN), tending to zero. These bounds are uniform in e,
including every action input row and normal end link; the observation
alone is compact. Multiplying by a^3 and summing the O(N^4)
observation rows turns the factor a in (9) into a bounded Riemann
sum, since a^4 |S| is bounded.

For a fixed offset ball, (5),(8) and the vertex Green convergence
are uniform on S and have smooth physical limiting coefficients.
The sum a^4 over each component's midpoint grid therefore converges
to the corresponding integral on D. The preceding summable tails
permit removing the spatial ball afterwards. This proves the
existence of a local stationary coefficient for (4) without imposing
any rate of coefficient freezing on its unbounded prefix.

L156(8) bounds the entire mode sum with p(k)p(l), uniformly in mesh.
Its heat tails tend uniformly to zero; L080(6) gives fixed-pair
coefficient convergence to c_(i;kl). Therefore finite-mode limits
followed by removal of the full heat tails are justified. The only
remaining task is to compute the absolutely convergent local
coefficient; this computation cannot replace the preceding finite-box
and tail estimates.

### 3. The centered prefix has an essential half-weight

Use component-center Fourier phases on the infinite grid. Put

    d_j=2 sin(theta_j/2), eta_j=cos(theta_j/2),
    lambda=sum_(j=1)^4 d_j^2, P=I-dd^T/lambda.

The centered symbols of D and g_4 are respectively i d and
lambda^-1. The complete frozen endpoint/clover stencil in (6) has
symbol i W, where, for nu,kappa=1,...,4,

    W_(nu kappa)=eta_nu^2 [delta_(nu kappa)
             sum_rho u_rho eta_rho d_rho-u_kappa eta_kappa d_nu]. (10)

The endpoint average contributes eta_nu and the ordered clover
contributes eta_rho eta_nu. Equation (10) includes their unequal
component filters. It follows directly from L009(3)/L028's complete
composition; no individual filter is commuted through P. Hence

    (g_4 A^0)_c=(i/2)(P W-W^T P).                     (11)

At a constant scalar exterior vector H, B_(H t_c) has centered
symbol 2 eta_nu H_nu J_c in component nu, where J_c z=[t_c,z].
The other B factor is 2 eta_mu E_mu J_c. In SU(2),
Tr(J_c^2)=-2 and sum_(c=1)^3 Tr(J_c^2)=-6. There is no additional
color factor after this sum.

To evaluate Phi_- in the absolutely convergent local product,
first damp its j-th prefix input by rho^j, 0<rho<1. Its centered
symbol from component 1 to vertices is

    p_rho(theta_1)=exp(-i theta_1/2)/(1-rho exp(-i theta_1)). (12)

The half-edge phase follows from the actual inputs w_1-j-1/2.
The damped kernels obey the same axial absolute-sum bound used
in (8),(9). Dominated convergence in those sums therefore recovers
the undamped local trace as rho increases to 1. For fixed rho,
the Fourier product is integrable: W=O(|d|), so (11)=O(|d|),
and D^T g_4=O(|d|^-1); all other filters are bounded. Fourier
multiplication/diagonal inversion follows from the l2 Parseval
identity for each fixed rho: the damped prefix has operator norm
at most (1-rho)^-1, g_4 A^0 has bounded symbol O(|d|), and
D^T g_4 has square-integrable symbol O(|d|^-1) in four dimensions.
The undamped prefix-A kernel need not be l2; its limit is justified
by the absolutely summable product (9), rather than by an l2 bound
uniform in rho.

The scalar component coefficient inside the trace is

    4 eta_nu eta_mu (-i d_mu/lambda) p_rho(theta_1)
                                      (g_4 A^0)_(1 nu). (13)

Apart from p_rho, (13) is real and even under simultaneous reversal
of all four angles. The imaginary part of p_rho is odd, so its
integral is zero. Its real part is

    (1-rho) cos(theta_1/2)
                     /[1-2rho cos(theta_1)+rho^2].       (14)

On [-pi,pi] this is a positive approximate identity of ordinary
mass tending to pi, hence normalized mass tending to 1/2.
For clarity, compare it with the Poisson kernel
(1-rho^2)/[1-2rho cos(theta_1)+rho^2]: their ratio is
cos(theta_1/2)/(1+rho), tending to 1/2 near zero, and the mass
outside every neighborhood of zero tends to zero. The transverse
integral of the remaining bounded part of (13) is continuous at
theta_1=0 by dominated convergence; the sole origin point is
irrelevant. Thus (14) keeps exactly half of its zero-axial-frequency
value. Treating the prefix as only its odd principal-value part
would wrongly lose this term.

### 4. Contract the zero-axial-frequency tensor and identify the form

At theta_1=0 let lambda_T=sum_(j=2)^4 d_j^2 and
S=sum_(j=2)^4 d_j^2 eta_j^2/lambda_T. In this paragraph lambda=lambda_T.
Since d_1=0, eta_1=1 and P_(1 nu)=0 for transverse nu,
the exact row of (11) is

    (g_4 A^0)_(1 nu)=(i u_1/2)d_nu(eta_nu^2-S),
                                            nu=2,3,4.  (15)

Its (1,1) entry is zero. Inserting (15) into (13) and the half-weight
from (14) yields, before color contraction,

    u_1 eta_nu eta_mu d_mu d_nu(eta_nu^2-S)/lambda.      (16)

Every off-diagonal mu!=nu integral vanishes by reversing theta_mu:
all its other factors are even in that angle. Coordinate permutation
makes the three diagonal integrals equal. Denote one by

    J=integral_(T^3) X_nu eta_nu^2(eta_nu^2-S)/lambda,
    X_nu=d_nu^2.                                      (17)

Their sum is the weighted variance

    sum_nu X_nu eta_nu^4/lambda
               -(sum_nu X_nu eta_nu^2)^2/lambda^2
      =sum_(mu<nu) X_mu X_nu(eta_mu^2-eta_nu^2)^2/lambda^2.

As eta_nu^2=1-X_nu/4, permutation symmetry gives exactly

    J=(1/16) integral_(T^3) XY(X-Y)^2/(X+Y+Z)^2
      =-g_G/4 > 0.                                   (18)

The origin extension is bounded and irrelevant; the integrand is
strictly positive on an open set. This matches L145(2)'s scalar
without a new numerical calculation. Restore the color sum -6,
the two physical exterior limits (5), the mode coefficients and
the Riemann integral. Equations (16)--(18) give

    lim a^3 X_i=-6 J sum_(k,l)c_(i;kl)
                       integral_D u_1 V_k dot V_l
                =(3/2)g_G B_(i,R).

This proves (2). The coefficient -1 of X_i was already reversed
by the exact forest identity in L167(7); (4) has coefficient +1.
It is not reversed again here. The endpoint factors 2, prefix
half-weight 1/2, symmetric residual factor 1/2 and color sum -6
have each been applied once. No two-action 1/2 or other/other
outside factor 3 belongs to this trace.

Finally L146's qualified full intervals for K_(3,R) and K_(6,R)
are (-74.916,-52.809) and (-27.545,-19.416). Multiplication by
3/2 proves (3). The physical forms, constant prefixes, transition
regions and complete heat tails are exactly those in (1), so this
import does not substitute a different probe or the G physical form.
This completes one trace's limit test and leaves the four other
retained traces and the complete-response question open.

## Mathlib

Full matching result and supporting discrete prefix/kernel coverage:
**not checked**. Unknown is not absence. Reuse the unchanged ready
[target assessment](../drafts/literature/2026-10-12-cubic-residual-action-cubic-scale.md).
No new external theorem is imported or rederived. Fourier/Parseval,
dominated convergence and midpoint Riemann sums are applied only
after their bounds and limiting orders are justified above. L167's
ordered forest identity and subcubic errors, L166's normalized residual
kernel, L164's relative Green comparison, L150/L080's actual exterior
limits and L156's full heat summability are the finite-box inputs.
L009/L028/L018 fix the generator and residual; L145/L146 supply only
the already established scalar/form identity and qualified complete
physical enclosures. The half-line localization and its retained
half-weight are proved because these differ from an undamped full-grid
parity test. No mathematical script or new certificate is needed.
