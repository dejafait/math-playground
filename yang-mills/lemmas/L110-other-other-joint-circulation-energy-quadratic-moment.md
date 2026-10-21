# L110 — Joint circulation energy has a summable quadratic axial moment

## Hypotheses

For the finite-trace statements use exactly L099's R_H,tr, both actual
L010 probes i=3,6, SU(2), L018's residual, the straight lower-rooted
direction-1 forest, relative all-face pinned box (-4,4)^4, admitted even
N, a=8/N and tau=1/16. Take the bare small-coupling coefficient at
fixed mesh before refinement. All coordinates and norms are ordinary
stored ones. Keep every axial level, pinned transverse row, heat mode,
both generator orientations and both coefficient levels. Import

    R_H,tr=sum_(k,l)c_(i;kl,a) Tr(K_h A_l^T K_g A_k G_tr),
    A_k=Pcal Omega_k Qcal, K_g=(min(s,t)) tensor P,

from L099(2), with Omega_k, its path maps B_b,B_q and its exterior
rows f_k,b_k,q_k as in L088(3). Write D=Cc for the transverse
circulation. These are the original two-edge paths, not centered
replacements. The finite relative cochain identity gives Pcal D^T=0.

The second statement concerns a separately defined infinite-grid
energy kernel. It does not replace any finite covariance. On Z^3,
in periodic unshifted phases, set t_mu=exp(i theta_mu)-1 for
mu=2,3,4 and define the three-plane circulation by

    (D(theta)y)_(mu nu)=t_mu y_nu-t_nu y_mu, mu<nu,
    lambda=sum_mu |t_mu|^2, theta in [-pi,pi]^3.

For integer axial offset j and lambda>0 put

    kappa=2 asinh(sqrt(lambda)/2),
    r_lambda(j)=exp(-kappa |j|)/(2 sinh kappa),
    E_j(theta)=r_lambda(j) D(theta) D(theta)^*.

Set E_j(0)=0. Let e_j(z) be the inverse Fourier coefficient of
this periodic 3-by-3 matrix, using normalized measure
(2pi)^(-3) dtheta and exp(i z dot theta). Frobenius matrix norms
are used below. Distances in Z^3 are dimensionless.

For the commutator statement let b be a real scalar function on
a Z^3 satisfying |b(ax)-b(ay)|<=a L |x-y|. It multiplies all three
plaquette components at the same integer index. Let Lambda_N be
any finite set of at most C_0 N^3 indices, and R_Lambda restrict
output rows to those indices. This common-index scalar assumption
is part of the statement; different actual staggered coefficients
have not been identified with b.

## Conclusion

Define the exact finite operators

    C_k=B_b^T M_(f_k) B_q-B_q^T M_(f_k) B_b,
    F_k=B_q^T M_(b_k)-B_b^T M_(q_k),
    A_k^f=Pcal C_k Qcal, A_k^D=Pcal F_k D Qcal.

Then

    A_k=A_k^f+A_k^D,
    R_H,tr=R_H,tr^D+E_(i,N)^f,
    R_H,tr^D=sum_(k,l)c_(i;kl,a)
                    Tr(K_h (A_l^D)^T K_g A_k^D G_tr),
    |E_(i,N)^f|<=C_i N^3.                              (1)

The error is cubic-bounded, not shown to have zero a^3 limit. Thus
it must still be retained when computing a coefficient.

For the infinite-grid kernel there is a universal finite C such that

    Q_j=(sum_z |z|^2 ||e_j(z)||_F^2)^(1/2)
                                  <=C(1+|j|)^(-3/2),
    sum_(j in Z) Q_j < infinity.                        (2)

In particular, for its convolution operator E_j,

    sum_j ||R_Lambda [M_b,E_j]||_HS
                   <=C a L sqrt(|Lambda_N|)
                   <=C sqrt(C_0) a L N^(3/2).          (3)

Both circulations and the unregularized covariance are inside this
kernel before taking quadratic sums. Equation (2) is compatible with
L109's divergent separate absolute first moments. It is a bulk input
for a joint coefficient-error estimate, not such an estimate for the
actual pinned trace. The unsandwiched P factors, generator placement,
staggered coefficient differences and physical-boundary comparison
remain to be controlled. No O(N^3) bound for R_H,tr^D, a^3 limit,
coefficient value or compensation with L084 follows here. Other jets,
finer powers/logarithm, matching, interacting error <=c_box/2,
continuum axioms, reflection positivity and infrared/finite positive
mass remain unresolved.

## Proof

### 1. Keep the complete circulation placement and bound its actual error

L088(3), with its original paths, is exactly

    Omega_k=C_k+F_k D-D^T F_k^T.

Multiplying by Pcal on the left and Qcal on the right removes only
the last term, by Pcal D^T=0. This proves the first equality in (1)
without commuting a multiplier with a projection or covariance.
The finite selectors have bounded multiplicity. L088(5) therefore
gives, at every level s including all transverse end rows,

    ||A_k^f(s)||<=C a^2 p(k),
    ||A_k^D(s)||<=C a p(k),
    sum_(k,l)|c_(i;kl,a)|p(k)p(l)<=C_i.                 (4)

Enlarge the same fixed polynomial p if needed. L099's full finite
generator has ||G_tr(s)||<=C/a. For each of the three products in
the difference between the full trace and the D,D trace, at least
one alternating factor is A^f. Since 0<=min(s,t)<=N, their blocks
after the generator obey

    ||min(s,t) (A_l(s))^T P A_k(t) G_tr(t)||
                   <=C p(k)p(l) N a^2
                   <=C' p(k)p(l) a.                  (5)

Here each A is the selected f or D factor. For f,f the bound follows
as well since a<=1 at sufficiently fine meshes. The placement and
level of G_tr in (5) are unchanged. L095(14) proves on the actual
pinned transverse spaces

    sum_(s,t)||(K_h)_ts||_1<=C N^4.

The block trace inequality and (5) bound each complete difference
trace by C p(k)p(l) a N^4=O(p(k)p(l)N^3). Sum using (4) to prove
(1). This retains all heat modes and the full min(s,t). It does not
delete the cubic error from the limiting coefficient.

### 2. Identify the unregularized infinite energy kernel

For lambda>0, r_lambda is the infinite-line inverse of the scalar
axial difference Laplacian plus lambda. This is the kernel used in
L098(8), now without a mass parameter. Its specialization is valid
pointwise for every lambda>0: away from j=0 the recurrence is
(2+lambda)r(j)-r(j-1)-r(j+1)=0 because
2 cosh kappa=2+lambda; at zero it is one because
(2 cosh kappa-2 exp(-kappa))/(2 sinh kappa)=1. Exponential decay
gives the unique inverse kernel, for instance by the positive
spectral lower bound lambda and the recurrence. Thus E_j sandwiches
this exact scalar covariance between D and D^*. No small transverse
frequency is removed. The undefined unsandwiched zero-frequency
inverse is replaced only in E_j by its continuous zero extension.
Since D annihilates gradients, the infinite-grid co-closed covariance
has the same sandwich: D(r_lambda(j) Q)D^*=E_j. This identity concerns
the constant-coefficient infinite grid only.

Write rho=sqrt(lambda), n=|j|. For 0<rho<=sqrt(12),

    rho/2<=kappa<=rho,
    2 sinh kappa=rho sqrt(rho^2+4),
    d kappa/d lambda=1/(rho sqrt(rho^2+4)).             (6)

The first inequality follows by integrating the derivative of
2 asinh(rho/2), which lies between 1/2 and 1 on this interval.
Consequently

    |r_lambda(j)|<=C rho^-1 exp(-n rho/2),
    |d r_lambda(j)/d lambda|
       <=C (rho^-3+n rho^-2) exp(-n rho/2).            (7)

For precision, the logarithmic derivative of its prefactor is
-(lambda+2)/(lambda(lambda+4)); its exponential contributes
-n/(rho sqrt(rho^2+4)). These give (7) uniformly through the entire
nonzero transverse spectrum, rather than only a continuum expansion.

### 3. Bound the complete quadratic moment before the axial sum

Set B(theta)=D(theta)D(theta)^*. The actual periodic incidence
entries give, with fixed matrix dimension,

    ||B||_F<=C rho^2,
    ||partial_(theta_mu) B||_F<=C rho,
    |partial_(theta_mu) lambda|<=2 rho.                (8)

Indeed ||D||_F<=C rho and each first derivative of D is bounded.
Also partial_mu lambda=2 sin(theta_mu), whose magnitude is at most
2|t_mu|. Product differentiation, (7) and (8) yield

    ||E_j(theta)||_F<=C rho exp(-n rho/2),
    ||partial_(theta_mu) E_j(theta)||_F
                        <=C(1+n rho)exp(-n rho/2).    (9)

These are estimates for the full matrix with both circulations,
not for separate projected alternating factors. The first proves
continuity at zero. The second is the weak derivative on the whole
torus: integrate by parts outside a ball of radius delta around
zero. Its additional boundary term is bounded by C delta^3 times
the test function supremum, since E_j=O(delta) and the sphere has
area O(delta^2). It tends to zero. The derivative is integrable by
(9), and periodic boundary faces cancel. This also justifies the
Fourier integration by parts below without differentiability at zero.

On the cube [-pi,pi]^3,

    (2/pi)|theta|<=rho<=|theta|.

For n>=1, (9) and integration over an enclosing Euclidean ball give

    integral ||nabla E_j||_F^2 dtheta/(2pi)^3
       <=C integral_0^(sqrt(3)pi) r^2(1+n r)^2
                                             exp(-2n r/pi) dr
       <=C' n^-3.                                    (10)

The substitution v=n r bounds the last integral by n^-3 times
the finite integral of v^2(1+v)^2 exp(-2v/pi) on [0,infinity).
For n=0, (9) bounds the integral by a constant. Thus the uniform
bound is C(1+n)^-3. No axial cutoff or inverse mass is present.

By weak integration by parts the Fourier coefficients of each
partial_mu E_j are -i z_mu e_j(z), with the sign determined by the
exp(i z dot theta) convention. The Fourier-series Plancherel theorem,
applied entrywise to E_j and its L2 weak derivatives, then gives

    sum_z |z|^2 ||e_j(z)||_F^2
        =integral ||nabla E_j||_F^2 dtheta/(2pi)^3.     (11)

Equations (10)--(11) prove (2), since the series of
(1+|j|)^(-3/2) is finite. This is a specialization of the standard
Plancherel theorem; the required weak regularity and the full axial
sum have been proved here for this particular covariance sandwich.

### 4. State the coefficient error this moment actually controls

The output-restricted commutator has matrix entries

    ([M_b,E_j])_(x,y)=(b(ax)-b(ay)) e_j(x-y),
                                       x in Lambda_N, y in Z^3,

up to the harmless sign of the convolution displacement. Therefore

    ||R_Lambda [M_b,E_j]||_HS^2
       <=a^2 L^2 sum_(x in Lambda_N) sum_y
                          |x-y|^2 ||e_j(x-y)||_F^2
       =a^2 L^2 |Lambda_N| Q_j^2.

Sum its square-root bound over every j and use (2) to prove (3).
For unbounded b this formula first defines the commutator on finitely
supported inputs; its finite Hilbert--Schmidt bound defines the
claimed restricted extension. It does not require an absolute first
moment or uniform operator-norm smallness of a projection commutator.

### 5. The finite-trace transfer is still an obligation

Equation (1) leaves the actual D,D trace with both F coefficients,
the middle gradient projection P, min(s,t) and G_tr in their original
order. Cyclicity exposes circulation on both sides of a covariance
only when the intervening generator is handled in that order. Its
filters and variable multipliers cannot be deleted by writing E_j.
Nor is E_(s-t) the Dirichlet axial or finite transverse covariance;
reflected/image terms and relative component boundaries remain.
Equation (3) treats one scalar bulk commutator, not these pinned or
staggered products. In particular it does not prove a cubic bound
for the D,D core or discard E_(i,N)^f at cubic scale.

This one joint-energy attempt supplies a relevant local input and
keeps its transfer gaps explicit. It is RESEARCH / REPRODUCTION under
the unchanged complete other/other EXPLORE assessment
`drafts/literature/2026-10-10-other-other-cubic-leading-scale.md`.
The finite contraction and scalar axial inverse are imported;
the detailed derivative proof is needed because neither L099's
fixed-mass localization nor L109's first absolute moment test supplies
this unregularized, axially summable quadratic estimate. The result
uses standard Fourier and finite-trace methods, with no claim of
originality beyond checked sources. No numerical coefficient of an
actual probe is used; L084/L082's comparison qualifications remain.

## Mathlib

Full matching axially summable energy-kernel moment and pinned-trace
remainder: **not checked**. Supporting Fourier Plancherel, weak
derivative, Hilbert--Schmidt, finite cochain and trace-ideal coverage:
**not checked**. Unknown availability is not absence. No general
Ward/flow theorem is used to give this isolated group's coefficient.
