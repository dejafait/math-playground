# L169 — The second ordered trace has a nonzero cubic limit

## Hypotheses

Keep L166's precise hypotheses: SU(2), the relative fixed-link cube
D=(-4,4)^4, a=8/N through sufficiently fine admitted even meshes,
the straight direction-1 lower-rooted forest, L008's complete compact
displacement, both actual L010 probes at tau=1/16, and the bare
expansion at each fixed mesh before refinement. Work in ordinary
stored coordinates with full tensors before forest restriction.
Both residual subtractions, every action face and normal end link,
the upper jump, constant axial mode and full heat spectrum remain.

Let Y_i be exactly L166(1), including its coefficient -12. Use
L161's N=T_S(ell,.,.), with T_S(x,x,x)=S_3(x), and L163's exact
exterior split N=N_b+N_top. For each exterior color c let
J_c z=[t_c,z], with t_c=i sigma_c/2. Thus J_c is real antisymmetric,
Tr(J_c^2)=-2 and sum_c Tr(J_c^2)=-6.

Import L145's actual transverse continuum forest columns V_k,
coefficients c_(i;kl), and established identity

    B_(i,R)=sum_(k,l)c_(i;kl) integral_D u_1 V_k dot V_l,
    K_(i,R)=g_G B_(i,R),
    g_G=-(1/4) integral_(T^3) XY(X-Y)^2/(X+Y+Z)^2.       (1)

The torus measure is normalized; X,Y,Z are respectively
4 sin^2(theta_2/2), 4 sin^2(theta_3/2), 4 sin^2(theta_4/2).
The physical columns include the entire lower prefix and its
constant axial mode. Numerical intervals below additionally import
L146's full heat inclusions with the stated IEEE binary64,
underflow, upstream moment and time-rule qualifications. The
analytic limit identity does not require that numerical model.

## Conclusion

For both actual probes the entire second ordered trace has limit

    lim_(a->0) a^3 Y_i=-3 g_G B_(i,R)=-3 K_(i,R).         (2)

Under L146's numerical qualifications,

    158.427 < lim a^3 Y_3 < 224.748,
     58.248 < lim a^3 Y_6 <  82.635.                      (3)

Thus this trace does not vanish at cubic scale. Its coefficient
-12 is included once; no additional outside factor 3 belongs here.
The third ordered bulk trace and the two mixed branches still lack
scaled limits/coefficients, so neither a limit nor vanishing for the
complete cubic residual/action response follows. Full compensation,
other jets, finer powers/logarithm, finite matching, interacting
reflected error <=c_box/2, continuum axioms and infrared finite
positive mass remain unresolved. This is local standard-method
progress with reuse of established enclosures, not a novelty claim
beyond the inspected literature and not a Yang--Mills candidate.

## Proof

### 1. Localize the exact bulk order with the undifferenced prefix

L166(3) gives, with both its upper contribution and its smooth-
residual subtraction included in the subcubic error,

    Y_i=-12 sum_(k,l,c)c_(i;kl,a)
              Tr[Sigmahat Ahat B_(h_k t_c) Fhat N_b]
                                                +O_i(N^2). (4)

Fix k,l,c first. The residual input e and each adjacent endpoint v
belong to a fixed compact interior enlargement S. L168(5)--(7)
establish, uniformly there at each bounded offset and physical
midpoint x,

    h_(k,e)/a -> H_nu=V_(k,nu)(x),
    (ell_b)_(l,f)/a -> E_mu=V_(l,mu)(x),
    a(Sigma A)_(z,e) -> (g_4 A^0(u(x)))_(z-e,nu),       (5)
    A^0(u)=(L^0 K^0(u)+(K^0(u))^T L^0)/2.

Here g_4 is the infinite unscaled Z^4 scalar Green kernel copied
to link components. H_1=E_1=0: interior axial forest columns are
exactly zero. The normalized residual a A tends to A^0, with
both subtractions still in the finite matrix; their normalized
finite-stencil limits are zero. No commutation of Sigma and A is
used. The componentwise actual endpoint/clover filters are those
of L168, including their unequal factors.

The prefix in (4) is F itself, not F A. For a vertex w and link y
at bounded offsets about e, it sums the component-1 Green entries
below w. L166(11) bounds the axial summands outside distance J of
e by a total C/J+C/N. Indeed the decaying term is a one-dimensional
tail of (1+|n|)^-2, and at most N constant terms N^-2 remain.
The lower root is distance >=delta N from e. Truncate at J, use
L164(5)'s uniform local Green convergence, and then let J tend to
infinity. Consequently, uniformly at every bounded offset,

    F_(w,y) -> (Phi_- g_4)_(w-y,1),                    (6)

with zero entries for input components other than 1. Phi_- sums
edges at w_1-j-1/2, j>=0. The axial sum is absolutely convergent;
no upper half-line, frequency cutoff or constant-mode deletion is
substituted. This is a different prefix limit from L168(8), and
the undifferenced tail above justifies it directly.

At bounded offsets about e all action stencils are interior. The
exact Wilson cubic in L048(4), equivalently L164(7), then gives

    a^-1 (N_b)_(y,z) -> N^0(E)_(y-z),
    N^0(E)=T_S(E t_c,.,.) on the infinite grid.         (7)

The frozen exterior is constant. This is the full action tensor,
with its trilinear normalization; no selected plaquette monomial
or gauge-restricted tensor replaces it.

The complete entry product in (4), after finite endpoint/color
counts, is bounded by a polynomial mode factor times

    C a [r^-4+N^-4]/(1+m),
    r=1+dist(e,z),  m=|e_T-z_T|.                       (8)

This is precisely L166(5),(12)--(15): Sigma A supplies a^-1,
B_h supplies a, and N_b supplies a. The decaying product is
summable on Z^4. Its axial sum is <=C(1+m)^-3; the transverse
shell count O((1+m)^2) leaves a summable (1+m)^-2 majorant.
Its tail outside a fixed four-dimensional offset ball tends to
zero. The finite constant part sums to O(N^-1), as L166(14)
shows. Thus, after multiplication by a^3 and summation over
O(N^4) residual rows, the tail has limsup bounded by a function
of the offset radius tending to zero. This is a normalized tail
bound, not merely the O(N^3) bound for the complete trace.

For a fixed offset ball, (5)--(7) give uniform local convergence.
The remaining factor a^4 summed over each component's midpoint
grid converges to its physical integral. Removing the offset ball
afterwards is justified by (8). All boundary action rows lie in
that controlled tail for large N, and L166 separately retains the
upper exterior with O(N^2) error. Both subtractions are retained
in (4)--(5) and its proved error; neither needs a new assumption.

L156(8)'s full heat summability and its polynomial mode estimates
give uniform summable majorants for all these steps. L080 gives
fixed-pair coefficient convergence. Finite heat sums may therefore
be used first and all heat tails removed last. It remains to
compute the absolutely convergent local coefficient of (4).

### 2. Evaluate the prefix without losing its half-weight

Use component-center Fourier phases, with

    d_j=2 sin(theta_j/2), eta_j=cos(theta_j/2),
    lambda=sum_j d_j^2, P=I-dd^T/lambda.

L168(10)--(11) supplies the exact normalized residual symbol

    M^0=g_4 A^0=(i/2)(P W-W^T P),
    W_(nu kappa)=eta_nu^2 [delta_(nu kappa)
          sum_rho u_rho eta_rho d_rho-u_kappa eta_kappa d_nu]. (9)

It is imaginary and odd under simultaneous reversal of all angles,
and ||M^0||<=C|u|sqrt(lambda). The endpoint map has component
symbol 2 eta_nu H_nu J_c. The constant-exterior action tensor
has ||N^0(E)||<=C|E|sqrt(lambda): L164(7)'s exterior-circulation
term is zero, while each remaining term has a rough circulation
and bounded finite-stencil filters.

Its full symbol is also imaginary and odd in component-center
phases. To see this without assigning parity to monomials, use
L164(11)'s exact signed inversion of the entire Wilson cubic.
A constant exterior changes sign under link inversion; the two
rough signs multiply to +1. Hence the constant-exterior quadratic
operator changes sign under spatial inversion. Its real finite-
stencil coefficients then give the asserted imaginary odd symbol.
This argument applies to every component and ordered plaquette.

Damp the j-th prefix input by rho^j, 0<rho<1. Its centered symbol is

    p_rho(theta_1)=exp(-i theta_1/2)/(1-rho exp(-i theta_1)). (10)

For fixed rho, Fourier diagonal inversion is justified by an l2
pairing: M^0 times the endpoint map has bounded symbol, and
p_rho N^0/lambda has square-integrable symbol, bounded near the
origin by C_rho/sqrt(lambda) in four dimensions. The undifferenced
g_4 alone is not l2, and no such assertion is needed. The damped
prefix kernel satisfies the same absolute axial and transverse
bounds as (6),(8). Dominated convergence in the complete kernel
product thus identifies the undamped local coefficient with the
limit of these Fourier expressions as rho increases to 1.

Apart from p_rho, the closed scalar/color Fourier contraction is
real and even under simultaneous angle reversal: (9) and N^0
are imaginary odd, while the endpoint and lambda^-1 are real
even. The imaginary part of p_rho therefore integrates to zero.
Its real part is

    (1-rho)cos(theta_1/2)
                   /[1-2rho cos(theta_1)+rho^2].         (11)

As proved in L168(14), this positive approximate identity has
normalized mass tending to 1/2 and selects theta_1=0. The
remaining scalar integrand is bounded uniformly by
C|u||H||E|, from the two sqrt(lambda) factors above. For every
nonzero transverse angle it is continuous in theta_1 at zero;
dominated convergence makes its transverse integral continuous
there as well. These are the hypotheses needed to apply the
approximate identity. Thus the actual half-line retains half the
zero-axial-frequency contraction, rather than only an odd
principal-value contribution.

### 3. Obtain the relevant action row by exact polarization

At theta_1=0 a rough field is independent of the axial coordinate.
For a (1,j) plaquette its signed traversal variables are

    (z, E_j t_c+y, -z', -E_j t_c-y),

where z,z' are the two axial rough links, separated by one positive
transverse step, and y is the transverse rough link. L048(4)'s
exact polynomial gives on this array

    q_3=z dot[(E_j t_c+y) cross z'].

The part with one exterior and two rough slots is consequently
-E_j z dot J_c z'; it has two axial rough links and no transverse
rough link. Since the coefficient with one exterior in
S_3(E+t x) is 3 t^2 T_S(E,x,x), its quadratic tensor is

    T_S(E,x,x)=-(1/3)sum_(v,j) E_j x_1(v) dot J_c x_1(v+j)

for its component-1 row/column at theta_1=0. The two symmetric
combined-index entries are -E_j J_c/6 in the positive-step
placement and +E_j J_c/6 in the reverse placement. Their symbol is

    N^0_(11)=-(i/3)sum_(j=2)^4 E_j eta_j d_j J_c,
    N^0_(1,nu)=0,                         nu=2,3,4.    (12)

Planes not containing direction 1 cannot contribute to this row.
This calculation includes the 1/3 polarization factor and both
spatial orientations. It neither assumes the action is curvature-
only nor transfers a color normalization from a two-action term.

At theta_1=0 put lambda_T=sum_(j=2)^4 d_j^2 and
S=sum_(j=2)^4 d_j^2 eta_j^2/lambda_T. L168(15) gives

    M^0_(1,nu)=(i u_1/2)d_nu(eta_nu^2-S),  nu=2,3,4,
    M^0_(11)=0.                                        (13)

The relevant closed trace has scalar component M^0_(1,nu),
endpoint 2 eta_nu H_nu, prefix p_rho/lambda, and action row
(12), with the two color factors J_c. Equations (12)--(13) and
the prefix half-weight therefore give, before color contraction,

    (u_1/6)sum_(nu,j) H_nu E_j
        eta_nu eta_j d_nu d_j(eta_nu^2-S)/lambda_T.      (14)

For j!=nu, reversal of theta_j makes this integrand odd; all
remaining factors are even in that coordinate. Thus only j=nu
survives. Transverse permutation symmetry makes its three
diagonal integrals equal to

    J=integral_(T^3) d_nu^2 eta_nu^2(eta_nu^2-S)/lambda_T
      =-g_G/4.                                         (15)

The last equality is L168(17)--(18)'s exact weighted-variance
identity with the same complete filters. No new torus enclosure
is required. Its bounded origin extension does not affect the
integral.

Restore sum_c Tr(J_c^2)=-6 and the outside coefficient -12 of
(4). Equation (14) then has total coefficient

    (-12)(-6)(1/6)J=12J=-3g_G.

Finally restore H=V_k, E=V_l, the midpoint integral and the full
heat coefficients. Their physical form is precisely (1), giving
(2). The signs, endpoint factor 2, symmetric residual factor 1/2,
prefix half-weight 1/2, action polarization 1/3 and color sum
have each been included once in (12)--(14). There is no additional
two-action 1/2 or complete-other/other outside factor 3.

L146's qualified intervals for K_(3,R), K_(6,R) are respectively
(-74.916,-52.809) and (-27.545,-19.416). Multiplication by -3,
with endpoints reversed, proves (3). The continuum limit proof
is analytic; only these numerical signs and intervals inherit
the upstream computer-assisted qualifications. The other three
retained limits and the complete-response test remain open.

## Mathlib

Full matching theorem and supporting relative-prefix/kernel
coverage: **not checked**. Unknown is not absence. Reuse the
unchanged ready [target assessment](../drafts/literature/2026-10-12-cubic-residual-action-cubic-scale.md).
No new external theorem is imported or rederived. L166 supplies
the exact bulk order, subcubic errors and summable product; L168
the residual/exterior local limits, full filters and half-weight
calculation; L164/L048 the exact Wilson cubic and inversion;
L156/L080 the full heat control and continuum coefficients; and
L145/L146 the matching physical form and qualified enclosures.
The undifferenced prefix limit and the needed action row are
proved here because the different ordered placement requires them.
Parseval, dominated convergence and midpoint Riemann sums are
used with the explicit bounds and limiting orders above. No
mathematical script or finite-mesh extrapolation is used.
