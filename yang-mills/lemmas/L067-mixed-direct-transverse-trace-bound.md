# L067 — The actual direct transverse path/path trace is bounded

## Hypotheses

Keep L064's exact fixed-mesh SU(2) Gaussian coefficient, ordinary
dimensionless coordinates, straight lower-rooted forest, actual residual
A_0, both original probe matrices, tau=1/16, and sufficiently fine admitted
even meshes a=8/N. Use its complete exterior expansion c_(i;kl), actual
alternating right path Q_l, pinned upper endpoint sum E_+, and multiplier
g_k(e)=(Th_k)_e. Retain every upper edge and every right transverse
plaquette at all axial levels 1<=s<N. Take the small-coupling coefficient
at fixed mesh before refining the mesh.

Let I_T insert full Hodge link components 2–4 and
Sigma_T=I_T^T Sigma I_T. This is the inverse **four-dimensional** component
Hodge block. Write Delta_E for the **three-dimensional** transverse edge
Laplacian in K_1, D for its edge-to-plaquette incidence, and
P=TGT^T, G=(T^T T)^(-1), on the corresponding pinned transverse spaces.
E_0 is L041's normalized constant axial component-1 embedding.

## Conclusion

Restrict only the right forest lift in L064(16) to its direct transverse
summand. Its exact trace is

    W_X^dir=sqrt(N) G E_0^T A_0 I_T Sigma_T,
    S_kl^dir=-Tr[K_1 Q_l (W_X^dir)^T E_+^T M_(g_k)].       (1)

There is a fixed polynomial p, independent of N, such that

    |S_kl^dir| <= C p(k)p(l),
    |sum_(k,l) c_(i;kl) S_kl^dir| <= C_i                 (2)

for both probes. Thus this summand is O(1), below the required O(N²)
threshold, and its a²-scaled value tends to zero. All modes, actual
path coefficients, covariance weights, endpoints and heat factors are
retained in their original order. No limit of the unscaled trace or
logarithmic coefficient is asserted.

The right axial-path summand, the first pair and other endpoint
monomials of L064 remain unresolved. The five terms removed at a² scale,
other cubic pairs, measure, insertion/flow jets and nonlinear forest
compensation remain necessary for the full response and logarithm.
Finite matching, the reflected error <=c_box/2, continuum fields,
full reflection positivity, infrared control and finite positive mass
remain open. This is local standard-method reproduction/specialization,
not a result beyond the sources assessed for the full response.

## Proof

### 1. Keep the ordered trace and isolate its actual columns

L018's quadratic transfer, L026's block-diagonal Hodge law and L064(15)
give the first identity in (1): L_u=sqrt(N)E_0^T and
L_u Sigma=sqrt(N)G E_0^T, while the direct right lift is I_T^T.
The second identity is precisely L064(16) with that right summand.
It is a linear decomposition of a quadratic covariance block, not
replacement of the cubic vertices by Hodge polynomials.

For each retained upper edge e define

    x_(l,e)=Sigma_T Q_l^T K_1^T delta_e,
    y_(k,e)=sqrt(N) g_k(e) E_0 G E_+^T delta_e.

Cyclicity of finite rectangular traces and symmetry of A_0 give exactly

    S_kl^dir=-sum_e <y_(k,e), A_0 I_T x_(l,e)>.             (3)

No multiplier is commuted with a covariance or residual. L064(13)–(14)
and the full Hodge gap in L026 give, uniformly in e,

    ||x_(l,e)||_2 <= C a^-1 p(l),
    ||x_(l,e)||_(L²_a) <= C a p(l),                       (4)

where ||z||_(L²_a)=a²||z||_2 on four-dimensional component grids.
Indeed ||Sigma_T||<=C a^-2, ||Q_l||<=C a p(l),
||K_1||<=C, and ||delta_e||=1. These are global estimates, including
the source neighborhood and every pinned end row.

### 2. The forcing is smooth away from its upper-face source

Choose fixed nested compact interior neighborhoods of all nonzero rows
and input stencils of A_0. Their distance from each face is positive,
uniformly for sufficiently fine a, by L028's coefficient support.
Additional finitely many shifts used below also lie in these neighborhoods.

L064 gives (K_1)_s=-g_s(Delta_E)(I-P)D^T. Since DT=0 and
Delta_E commutes with P, the exact transpose at each level is

    (K_1^T delta_e)_s=-D g_s(Delta_E) delta_e.              (5)

This removes P algebraically before estimation. It does not project
Q_l or a general cubic derivative onto a transverse subspace.

Here is the full-mode local bound in (5). A transverse edge component
has one normalized cosine index in 0,...,N-1 and two sine indices in
1,...,N-1. Each product mode and its source evaluation at any retained
edge have magnitude at most C N^-3/2. This includes normal end edges;
fixed tangential rows evaluate to zero. For its eigenvalue lambda_q,
put eta_q=2 asinh(sqrt(lambda_q)/2). L026's sine bounds give
c a|q|<=eta_q<=C a|q| and |q|>=sqrt(2). The exact Dirichlet last-column
inverse is L041(8),

    g_s(lambda_q)=sinh(s eta_q)/sinh(N eta_q).

On a physical axial interval separated from the top by delta>0, its
smooth extension and m-th physical derivatives are bounded by
C_m(1+|q|)^m exp(-c delta |q|). The transverse product extension has
the usual derivative bound C_m N^-3/2(1+|q|)^m. Applying the actual
unscaled D introduces an additional factor at most C a|q|, because
every difference of a sampled sine/cosine mode is bounded by its
physical derivative times a. The shifts in this statement are exact
incidence shifts, not a continuum replacement of D.

Each differentiated summand in (5) is consequently bounded by

    C_m a⁴(1+|q|)^(m+1) exp(-c delta |q|).

The sum over all allowed three-dimensional indices is uniformly
bounded by the convergent sum over the full integer orthant. Therefore
(5) has, on those neighborhoods, an exact sampled smooth extension
b_(e,a) satisfying

    ||b_(e,a)||_(C^m) <= C_m a⁴                           (6)

for every fixed m, uniformly in every source e. All axial levels and
transverse modes have been retained; only the observation region is
separated from the source.

The actual path coefficients t_l,2 and t_l,3 also have local smooth
extensions with C^m norm at most C_m a p_m(l), for any fixed m and
some fixed polynomial p_m. This higher-derivative version of L062(11)
can be checked directly from L028(11): before retraction, v_l is a
times a normalized physical sine/cosine mode divided by sqrt(lambda_l).
Its C^m norms have polynomial mode bounds by the positive physical
gap. For the axial prefix, the exact sum of a nonconstant cosine mode
at edge centers is

    sum_(r=0)^(s-1) cos[(r+1/2)theta]
                      =sin(s theta)/(2 sin(theta/2)).

For theta=pi l_1/N, l_1>=1, the prefactor a/(2 sin(theta/2))
is at most C/l_1. For the zero axial mode, a times the prefix length
is as=-4+as+4, a linear physical coordinate. Thus the prefix potential
has smooth polynomial derivative bounds. Its transverse unscaled
difference contributes a factor a by the integral difference formula.
The direct transverse field is already O(a). Finite signed two-link
paths preserve these bounds, with fixed physical shifts. This argument
uses only interior axial levels; the separately pinned upper potential
is never interpolated across its jump. Global path norms in (4) still
include the pinned rows.

Q_l^T is the sum of the adjoint two-link path maps, with coefficients
t_l,2 and -t_l,3 in their actual positions. On the interior neighborhood
each is a finite signed shift of the coefficient times b_(e,a).
It therefore follows from (6), with the product rule and without
commuting a coefficient through a covariance, that the local source

    f_(l,e)=Q_l^T K_1^T delta_e

has an exact smooth extension satisfying

    ||f_(l,e)||_(C^m) <= C_m a⁵ p_m(l).                   (7)

### 3. Prove the mesh-uniform interior estimate needed here

Each component of x=x_(l,e) satisfies, on the interior neighborhood,

    L_a x=F,  L_a=a^-2 Delta_4,  F=a^-2 f_(l,e),          (8)

where Delta_4 is the standard sum of scalar second differences there.
The relative boundary conditions affect the global inverse in (4),
but not these interior rows. By (7), all fixed physical forward
differences of F have local L²_a norm at most C_m a³ p_m(l).
Forward differences are divided by a; their bounds follow by repeated
integral difference formulas applied to (7).

For clarity, the finite-difference interior regularity and interpolation
used next are proved here with uniform constants. This short reproof is
needed for the actual mesh-dependent source and four-dimensional norm
normalization; no physical boundary regularity theorem is assumed.

Let w solve L_a w=H on a fixed interior region, and let chi be samples
of a smooth cutoff supported there. Summation by parts with chi²w,
including both ends of each edge in its support, gives the identity

    sum_j ||partial_(j,a)(chi w)||²_(L²_a)
      = <chi² w,H>_(L²_a)
        +a⁴ sum_(j,v) |partial_(j,a)chi(v)|² w(v)w(v+a e_j).

To check it, on one edge write chi(v)=c, chi(v+a e_j)=d,
w(v)=u, w(v+a e_j)=v'. The difference between
(d v'-c u)² and (v'-u)(d² v'-c²u) is (d-c)² u v'.
Divide by a² and sum. The cutoff has compact interior support, so
no physical-boundary term is present. Adjacent products are bounded
by half the sum of the two squares. Thus, on any smaller region where
chi=1, the first-difference norm is at most

    C (||w||_(L²_a,larger)+||H||_(L²_a,larger)).           (9)

This follows from Cauchy–Schwarz and 2uv<=u²+v², with uniformly
bounded physical derivatives of chi. The same identity applies to
real and imaginary parts if needed.

The constant-coefficient operator in (8) commutes with all forward
differences. Apply (9) to each difference of w, with successively
smaller fixed neighborhoods. At induction level j, the norm of that
j-th difference on the larger neighborhood is available from the
previous level, and its equation has the j-th difference of H on
the right. A finite choice of nested cutoffs, and sufficiently small
a so that their finitely many shifts remain inside the larger set,
therefore proves

    sum_(|alpha|<=8) ||partial_a^alpha x||_(L²_a,inner)
           <= C (||x||_(L²_a,global)
                    +sum_(|alpha|<=7)
                         ||partial_a^alpha F||_(L²_a,outer))
           <= C a p(l).                                 (10)

The final p absorbs the finitely many polynomials from (7). This
explicit induction needs no estimate at the boundary or at the source.

Take another smooth cutoff equal to one on the entire stencil
neighborhood of A_0 and supported in the inner region. Extend its
product with x by zero to its staggered infinite component grid.
The exact discrete product rule, bounded cutoff derivatives and (10)
bound all its physical difference norms through order eight by C a p(l).
Use its lattice Fourier transform on the Brillouin cube [-pi/a,pi/a]^4,
and inverse continuous Fourier integral as an interpolant. Fourier
inversion makes its values at the grid points exactly the original
samples. Discrete Plancherel identifies the transform L² norm with
the L²_a norm. On that cube,

    |(exp(i a xi_j)-1)/a| >= (2/pi)|xi_j|.

Consequently its continuous Fourier H^8 norm is bounded by the sum
of the difference norms in (10). Cauchy–Schwarz in the Fourier
integral bounds every physical derivative of order m<=5 in supremum
norm: the remaining integral
integral_R4 |xi|^(2m)(1+|xi|²)^(-8) dxi is finite, since
8-m>=3>4/2. The constant is independent of the Brillouin cutoff.
This proves the existence of an exact sampled smooth extension X of
x on the stencil neighborhood, with

    ||X||_(C^5) <= C a p(l).                             (11)

The band-limited inverse integral is smooth at each mesh. Multiplying
it by a fixed smooth cutoff equal to one on the stencil neighborhood
gives a global compact smooth extension with the same bound. Applying
A_0 to that extension's samples is therefore exactly applying it to
the original I_T x. The other component is inserted as zero.

### 4. Apply the actual residual and sum every endpoint and heat mode

L028 proves for arbitrary smooth inputs on the coefficient neighborhood
that A_0=a² N_a and ||N_a X||_infinity<=C a²||X||_(C^5).
It retains both generator compositions, all coefficient derivatives,
the actual triplet average of squares and shear clovers. By (11),

    ||A_0 I_T x_(l,e)||_infinity <= C a⁵ p(l),
    ||A_0 I_T x_(l,e)||_2 <= C a³ p(l).                   (12)

The last bound counts O(a^-4) nonzero full-link rows. Outside the
compact coefficient enlargement these rows are exactly zero.

For the other column, E_+^T delta_e is the sum of the two pinned
vertex evaluations, with an evaluation zero when the endpoint is
on a face. L041(11), using the full transverse vertex spectrum,
gives (G²)(v,v)<=CN uniformly. Triangle inequality therefore yields
||G E_+^T delta_e||<=C sqrt(N), including both end-edge cases.
Since E_0 is an isometry and L064(3) gives |g_k(e)|<=a p(k),

    ||y_(k,e)||_2 <= C sqrt(N) a p(k) sqrt(N)
                         <= C' p(k).                    (13)

There are exactly 3N(N-1)² retained transverse upper edges before
any zero-row identifications, hence O(N³). Substitute (12)–(13)
in the exact signed column sum (3), use aN=8, and obtain

    |S_kl^dir| <= C N³ a³ p(k)p(l) <= C' p(k)p(l).

This estimate bounds absolute values after preserving the trace's
actual composition. It needs no further signed cancellation.

Finally L062/L064's complete heat coefficients satisfy
sum_(k,l) |c_(i;kl)| p(k)p(l)<=C_i for any fixed polynomial p:
B^rel_i is uniformly bounded, the physical eigenvalues have a
quadratic lower bound in their full mode indices, and a polynomial
times exp[-tau(lambda_k+lambda_l)] is summable. Thus the polynomial
enlargement required in (10)–(11) does not truncate or change the
external expansion. This proves both claims in (2).

The analytic checks are the direct-summand transfer and trace order,
the exact deletion of P only in (5), all source end-edge modes,
the positive transverse gap, physical axial separation, the actual
prefix formula and local path adjoint positions, the four-dimensional
L²_a normalization, compact cutoff identities, all eight difference
orders, exact grid interpolation and its C^5 bound, the complete
residual consistency, all pinned endpoint columns and the full heat
sum. No mathematical script or finite numerical preview is needed.

This result uses the actual composed source to avoid L066's unrestricted
packet obstruction; it does not contradict that norm lower bound.
It is a partial estimate toward the full response, with the independent
gaps stated above. An O(1) bound alone assigns no logarithmic coefficient
or finite limit. The two-channel reflected-error threshold remains
unchanged.

### 5. Independent critical audit, 2026-10-08

The separate audit YM-20261008-085-mixed-direct-trace-audit checked the
full argument against its input formulas and found no defect within
this summand's scope. It establishes no stronger estimate.

Transposition of W_X^dir gives Sigma_T I_T^T A_0 E_0 G sqrt(N).
Inserting delta_e on both sides of the trace yields exactly (3),
including its minus sign and the multiplier in y. L018's quadratic
transfer and L026's component-diagonal covariance justify this; higher
cubic vertices are not transferred without their lifted rows. The
constant axial component-1 mode has inverse G because its axial
Neumann eigenvalue is zero. Hence E_0^T Sigma=G E_0^T without another a.

In (5), D(I-P)=D removes the gradient projection before estimation.
Two transverse mode evaluations give N^-3, and the unscaled D gives
a|q|, yielding a^4. Axial physical derivatives give eta_q/a<=C|q|.
The two positive transverse vertex indices exclude a zero mode even
when the edge's cosine index is zero. Fixed tangential source rows
vanish; normal end-edge evaluations satisfy the same bound. The exact
prefix formulas concern s<N and never interpolate the pinned top jump.
Their polynomial derivative bounds cover every order required in (7).

At induction level j in (10), the equation for partial_a^alpha x has
right side partial_a^alpha F, |alpha|=j, and the cutoff energy identity
bounds order j+1 on the smaller region. Iterations j=0,...,7 therefore
require only seven forcing derivative orders for eight solution orders.
All shifted equation rows lie in the nested neighborhoods. The global
norm is four-dimensional a^2||x||_2. No forcing derivative estimate is
used near its upper-face source. At m=5 the radial large-frequency
integrand in the Fourier bound is O(r^(3+10-16))=O(r^-3), uniformly
integrable. The cutoff interpolant agrees exactly on every input
stencil of A_0, so L028 applies without a sampling discrepancy.

L041(11) includes all pinned endpoint columns; two evaluations use the
triangle inequality, not independence. Equation (13) is O(aN p(k)),
and the endpoint count times (12) is O(N^3 a^3 p(l)). Both are uniform
because aN=8. The physical mode gap and bounded B^rel in L028/L062
give a summable heat majorant with the enlarged polynomial for both
probes. Constants may depend on the fixed support, box, displacement
and tau, but not N or the source edge.

This is an internal analytic audit, not independent computer
verification. It confirms the existing O(1) bound only. The other
right-lift summand has an adjoint axial-prefix source not estimated
here; its smoothness or localization is not assumed. No complete mixed
limit, full logarithm or interacting-error conclusion is added.

## Mathlib

Coverage of the full direct-transverse trace bound: **not checked**.
Supporting finite trace algebra, spectral calculus, lattice Fourier
inversion/Plancherel, Cauchy–Schwarz, exact discrete product identities
and Fourier Sobolev estimates: **not checked**. No matching theorem or
absence claim is made. The mesh-uniform interior argument is supplied
in full rather than assuming a continuum boundary theorem applies.
General flow renormalizability and stress matching remain the precise
primary-source imports in the reused literature assessment.
