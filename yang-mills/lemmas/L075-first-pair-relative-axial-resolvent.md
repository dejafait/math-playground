# L075 — The first-pair base profile retains an upper Dirichlet correction

## Hypotheses

Keep L026's ordinary dimensionless Hodge coordinates, box (-4,4)^4,
a=8/N with sufficiently fine even N, relative fixed-link boundaries,
and straight lower-rooted forest. Use L070's map (Sz)_s=sTz,
1<=s<N, with Tz(v,w)=z(v)-z(w) on pinned transverse vertices.
Let Delta_E be the three-dimensional relative edge Hodge Laplacian
on the direct sum of components 2,3,4, and Delta_V=T^T T on pinned
transverse vertices. Let G=Delta_V^(-1). In particular Delta_E T=T Delta_V.
Let Sigma_T be the full four-dimensional transverse component covariance.

In the axial coordinate V=R^(N-1), L_V has diagonal 2 and neighboring
entries -1, with zero values at levels 0,N. In E=R^N, the axial
constant edge mode is e_0=N^(-1/2)(1,...,1). E_0 embeds it in full
component 1. C_1:E->V averages adjacent edges, as in L065.
All spectral projections and transposes below use ordinary Euclidean
normalization, including every normal end edge.

Use the actual displacement from L008, not a frozen coefficient.
Writing x_s=-4+as, h_s=x_s rho(x_s), and
beta_a(y)=rho(y_2) {nabla_3^c(x_3 rho(x_3))}(y_3) rho(y_4),
its component 1 is exactly u_(a,1)(s,y)=h_s beta_a(y).
The Psi_24 sector contributes zero to this component. At the central
transverse vertex y=(0,0,0), beta_a(y)=1 for sufficiently small a.

The results concern a linear Gaussian covariance input to L074's
selected first pair. No approximation theorem for L070(9), nonlinear
probe coefficient or signed response is assumed.

## Conclusion

For every eigenvalue lambda>0 of Delta_E put eta=2 asinh(sqrt(lambda)/2).
The complete axial Dirichlet inverse and its linear-profile image are

    R_lambda(s,t)=sinh(min(s,t) eta) sinh((N-max(s,t)) eta)
                         /[sinh(eta) sinh(N eta)],
    f_lambda(s)=sum_(t=1)^(N-1) R_lambda(s,t)t
              =[s-N g_s(lambda)]/lambda,
    g_s(lambda)=sinh(s eta)/sinh(N eta).                 (1)

Thus the exact base-row covariance image, including both end rows, is

    (Sigma_T S z)_s=f_(Delta_E)(s) Tz
                  =T f_(Delta_V)(s) z.                 (2)

For all allowed transverse frequencies and 1<=s<N,

    0<f_lambda(s)<=min{s/lambda, s(N²-s²)/6},
    0<=g_s(lambda)<=C exp[-c(N-s)|q|/N],                (3)

where q is the sine/cosine transverse index of that component. The
constants are independent of q,N. Full component spectra have two
positive sine indices and one possibly zero cosine index; on Tz all
three indices are positive. No zero transverse eigenvalue is used.

With d=as and kappa_a²=lambda/a², the physical profile is exactly

    a³ f_lambda(s)=[d-8 g_s(lambda)]/kappa_a².           (4)

For each fixed transverse index q and sequences with as->d in (0,8),
it tends to

    F_q(d)=[d-8 sinh(kappa d)/sinh(8 kappa)]/kappa²,
    kappa=pi |q|/8.                                    (5)

The replacement by the bulk distance profile d/kappa² fails uniformly
even on compact axial interiors. At s=N/2 its relative omitted part is
exactly sech(N eta/2), tending to sech(pi |q|/2)>0. The actual odd
axial displacement and constant-edge average do not annihilate this
correction: the normalized weighted correction at y=(0,0,0) tends to
the strictly negative number in (10) below for a fixed mode in the
range of T.

For the original trace with its intervening level-dependent path
operator, (11) below is the exact full-spectrum substitute. It retains
the variable displacement inside A_0 and E_0 in their original order.
Equations (2) and (4) cannot remove that intervening operator. They do
not identify the diagnostic with an original coefficient, establish
the required O(N²) bound, give a scaled trace limit, sign or logarithm,
or improve the interacting reflected-error threshold c_box/2.

## Proof

### 1. Verify the component boundary conditions and the inverse

L026's tensor modes give, on component mu in {2,3,4}, an axial vertex
coordinate and transverse edge coordinate in direction mu, with vertex
coordinates in the other two directions. Hence

    Sigma_T=(L_V tensor I+I tensor Delta_E)^(-1).        (6)

Component 1 instead has the axial edge Laplacian; its constant mode
does not turn the axial matrix in (6) into a Neumann matrix. This
distinction also retains the separately pinned upper forest potential.
The tensor incidences commute in distinct coordinates, so their
Hodge identity gives Delta_E T=T Delta_V. This identity includes
normal transverse end edges, since T is the pinned incidence there.

For fixed lambda>0 the homogeneous recurrence of L_V+lambda is
(2+lambda)v_s-v_(s-1)-v_(s+1)=0. Its two solutions vanishing at
opposite endpoints are sinh(s eta) and sinh((N-s)eta), since
2+lambda=2 cosh eta. The numerator in (1) is continuous at s=t.
Its jump equation follows from

    sinh((t+1)eta)sinh((N-t)eta)
      -sinh(t eta)sinh((N-t-1)eta)=sinh(eta)sinh(N eta).

Consequently (L_V+lambda) R_lambda(.,t)=delta_t, including t=1,N-1,
with zero endpoint values. Positive definiteness gives uniqueness.
This extends L041's already proved last-column formula to the full
finite inverse by the same recurrence; no general renormalization or
Green-function theorem is reproved.

For b_s=s the pinned matrix has L_V b=N delta_(N-1). Formula (1)
has R_lambda(s,N-1)=g_s(lambda), exactly L041's last column. Applying
the inverse to (L_V+lambda)b=lambda b+N delta_(N-1) proves its second
formula. Functional calculus in (6), followed by the incidence
intertwining, proves (2).

### 2. Bounds over the complete spectrum

Every entry of R_lambda in (1) is positive, so f_lambda>0. The
subtraction formula gives f_lambda<=s/lambda. At lambda=0 the pinned
solution is p_s=s(N²-s²)/6: direct neighboring differences give
L_V p=b and p_0=p_N=0. Since

    p-f_lambda=lambda (L_V+lambda)^(-1)p>=0

entrywise, the second bound in (3) follows. This zero-parameter
comparison is only a bound; lambda=0 is absent from the transverse
component spectrum. It explicitly retains the cancellation at the
upper end; no last row is deleted.

The full transverse eigenvalues are
lambda_q=4 sum_(j=2)^4 sin²(pi q_j/(2N)). Elementary sine bounds and
eta=2 asinh(sqrt(lambda_q)/2) imply
c|q|/N<=eta<=C|q|/N for every permitted index, and N eta>=c'>0
because at least two indices are positive. The exact exponential form

    g_s=exp(-(N-s)eta) (1-exp(-2s eta))/(1-exp(-2N eta))

proves the third bound in (3) for every level and frequency. Bounds
(3) are not a bound on the signed trace after the residual insertion.

### 3. Physical scaling and a surviving weighted end correction

The unscaled axial/transverse matrix in (6) becomes the physical
operator by division by a², so its physical inverse is a² Sigma_T.
The physical base distance is ab_s=as. Their product is a³ f_lambda;
there is no additional cochain-volume factor in this linear operator
conversion. This proves (4). For fixed q,
kappa_a->kappa=pi |q|/8 and eta/a->kappa. Substitution proves (5),
uniformly in d on [0,8] for that fixed q. This is a fixed-mode limit;
the preceding bounds, not this limit, cover the rest of the spectrum.

At the middle level, N g_(N/2)/(N/2)=2 sinh(N eta/2)/sinh(N eta)
=sech(N eta/2). Thus the relative correction is bounded away from
zero along any fixed-index sequence. In particular a blanket
small-error bulk-profile replacement fails before trace contraction.

Now check the actual coefficient in its actual average order. On
interior axial vertices,

    sqrt(N) e_0^T C_1^T M_(u_(a,1)(.,y))v
                     =sum_(s=1)^(N-1) u_(a,1)(s,y)v_s.  (7)

This follows from C_1 e_0=N^(-1/2)1_V, including its two end-edge
averages. It moves no coefficient through a covariance. The sqrt(N)
is the same normalization occurring before E_0^T in L074. Equation
(7) describes a particular averaged multiplication block, not the
whole residual E_0^T A_0 I_T.

At y=(0,0,0), u_(a,1)(s,y)=h_s. The replacement error in the physical
profile is exactly -8 g_s(lambda)/kappa_a². Therefore the physical
axial integral of this averaged block has error

    B_(N,q)=a sum_s h_s [-8 g_s(lambda_q)/kappa_a²].     (8)

It is realizable on a base-row transverse mode: take the pinned vertex
mode with indices (q_2,q_3,q_4)=(2,1,1), apply T, and select component
2. Its averaged edge value at y=(0,0,0) is nonzero. Indeed the
incidence of sin(2pi j/N) is a nonzero multiple of
cos(2pi(ell+1/2)/N); its adjacent-edge average at j=N/2 is a nonzero
multiple of -cos(pi/N). The other two sine factors are nonzero at
their centers. Divide by this nonzero transverse value when evaluating
(8); this is a linear test input, not either actual probe or a signed
response. Component covariance preserves this mode and its index.

For all sufficiently fine even N, pair levels s,N-s above and below
the middle. Since rho is even and positive in the affine core,

    sum_s h_s g_s
      =sum_(s>N/2) h_s [g_s-g_(N-s)]>0.                (9)

The inequality uses strict increase of g_s in s, h_s>=0 above the
middle, and at least one strictly positive core term. Thus B_(N,q)<0.
Fixed-mode convergence in (5) and the Riemann-sum theorem give

    B_(N,q)-> -8/kappa² integral_0^8
       (d-4)rho(d-4) sinh(kappa d)/sinh(8 kappa) dd <0. (10)

Strictness follows by pairing d with 8-d: the positive half contains
a positive core interval and a strictly increasing hyperbolic factor.
The end correction therefore survives an actual u_1 multiplication
and the normalized constant-edge average. This is an obstruction to
discarding it uniformly, not a nonzero correction to the complete
first-pair heat sum. Other residual terms or transverse/probe sums
can still cancel it.

### 4. Retain the intervening operator in the original trace

Let Z_l=Lambda_l+D^T bar Q_l be L074(10)'s exact centered joint path
operator. It acts separately at each axial level; write its transverse
block as Z_l(t). Its coefficients are the actual exterior columns.
If P_alpha is a complete orthogonal spectral resolution of Delta_E
with eigenvalue lambda_alpha, finite matrix multiplication gives

    (X_l z)_s=(Sigma_T Z_l S z)_s
       =sum_alpha P_alpha sum_(t=1)^(N-1)
                  R_(lambda_alpha)(s,t) t Z_l(t) Tz,
    F_kl=sqrt(N) Tr[G C_(r_k) G E_0^T A_0 I_T X_l].     (11)

This is the original joint direct first pair in L074, with its complete
covariance expanded, not approximated. It retains all transverse
projections, both endpoint placements, levels and end rows. A_0 still
contains the actual variable u_1, all other displacement components,
their stencils and the insertion subtraction. In particular neither
E_0^T A_0 nor Z_l(t) has been replaced by a scalar multiplier.

Even if Z_l were level independent, spatial coefficients could mix
transverse spectral subspaces: the legitimate simplification would
be f_(Delta_E)(s)Z_l T, retaining that order. The actual Z_l(t) also
has level-dependent coefficients; it remains inside the sum in (11).
There is no identity
Sigma_T Z_l S=Z_l Sigma_T S in this calculation.

This finishes the bounded normalization input. The simple physical-
distance replacement is parked; further work must use the complete
kernel (11) or prove a bound for its actual contracted difference.
The centered spatial trace, path/path term, scaled exterior defect,
variable-coefficient and pinned residual remainder, full response and
logarithm remain unresolved. None of the continuum field, reflection-
positivity, infrared or finite positive mass requirements follows.
This is local REPRODUCTION under the unchanged SPECIALIZE assessment;
no progress beyond its inspected sources is claimed.

The finite indexing and normalization check is
`scripts/combined-ward-response/check_first_pair_axial_resolvent.py`:

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/check_first_pair_axial_resolvent.py

Its complete rational certificate is
`scripts/combined-ward-response/first-pair-axial-resolvent-certificate.json`.
All eight cases N=4,6,8,24 and exp(eta)=2,3 check every entry of the
inverse product, the linear-profile identity, both bounds, the
zero-parameter comparison, both end rows, the middle relative factor,
and the normalized average. Every exact error and bound violation is
zero, as required. These are rational operator tests; their lambda
values are not asserted to be actual transverse lattice eigenvalues.
The analytic proof above covers those eigenvalues, their full spectrum
and the actual-weight limit. The finite checks alone prove none of
the response or asymptotic claims excluded above.

## Mathlib

Coverage of the full specialized relative-profile and weighted-test
statement: **not checked**. Supporting finite spectral calculus,
pinned tridiagonal inverses and Riemann sums: **not checked**. No
matching Mathlib theorem or absence claim is asserted. The finite
operator specialization is proved here; the general perturbative
flow and stress-matching sources in the ready assessment are retained
within their recorded qualifications and are not reproved or used to
assign an original response coefficient.
