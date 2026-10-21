# L123 — The exterior-circulation remainder has a cubic-scaled limit

## Hypotheses

Use exactly E_(i,N)^f=R_H,tr-R_H,tr^D in L110(1), SU(2), both actual
L010 probes i=3,6, the straight lower-rooted direction-1 forest, all-face
relative fixed-link box D_box=(-4,4)^4, admitted even N, a=8/N and
tau=1/16. Take the bare small-coupling coefficient at fixed mesh before
refinement. Norms and transposes are in ordinary stored coordinates.
Keep all interior axial levels, transverse end rows, both exterior and
generator orientations and the complete heat sum.

Import L110's exact decomposition

    A_k=A_k^f+A_k^D,
    A_k^f=Pcal C_k Qcal,       A_k^D=Pcal F_k D Qcal,
    C_k=B_b^T M_(f_k) B_q-B_q^T M_(f_k) B_b,
    F_k=B_q^T M_(b_k)-B_b^T M_(q_k),

with D the transverse circulation, original two-edge paths B_b,B_q,
and f_k=D v_k, b_k=B_b v_k, q_k=B_q v_k from L088. At each level
P is the relative gradient projection, Q=I-P, and

    K_g(s,t)=min(s,t)P,
    (K_h)_ts=[(L_D+Delta_T)^(-1)]_ts Q.

Use L111(1)'s complete ordered generator G_tr=a^-1 H D, and L120(2)'s
continuum modes A_k, prefix Phi_k, lifted field V_k, and coefficients
c_(i;kl). Thus V_(k,mu)=A_(k,mu)-partial_mu Phi_k; the prefix includes
the component-1 constant axial mode. Define the transverse two-form

    h_(k,mu nu)(x)=partial_mu A_(k,nu)(x)
                         -partial_nu A_(k,mu)(x), 2<=mu<nu<=4,
    b_(k,mu nu)(x)=V_(k,mu)(x)+V_(k,nu)(x),
    q_(k,mu nu)(x)=-V_(k,mu)(x)+V_(k,nu)(x).

The continuum letters b_k,q_k below denote these limits, not finite
stored coefficients. For theta in [-pi,pi]^3 use the lower-vertex
symbols of the original infinite-grid stencils. Put t_mu=e^(i theta_mu)-1,
lambda=sum_mu |t_mu|^2, P(theta)=t t^*/lambda and Q(theta)=I-P(theta)
for lambda>0. The circulation symbol is
D(theta)y=(t_mu y_nu-t_nu y_mu)_(mu<nu). Write B_b(theta),B_q(theta)
for the exact path symbols; equivalently use L088(11) and the unitary
component-center phases, with the same phases on every factor. Set

    C_k(x,theta)=B_b^* diag(h_k(x)) B_q
                             -B_q^* diag(h_k(x)) B_b,
    F_k(x,theta)=B_q^* diag(b_k(x))-B_b^* diag(q_k(x)),
    beta_k=P C_k Q,             alpha_k=P F_k D Q,
    g(x,theta)=sum_r T_r(theta) u_(rho(r))(x) C_r(theta) D(theta).
                                                               (1)

Here the finite list r, signs and endpoint/clover stencils T_r,C_r
are exactly L111(1). The C_r generator stencil is distinct from C_k.
No component filter has crossed a projection. Values at theta=0 may
be assigned arbitrarily in the integrals below.

## Conclusion

The real functional

    K_(i,f)=sum_(k,l)c_(i;kl) integral_(D_box) (x_1+4)
      integral_([-pi,pi]^3) tr{lambda^-1 Q
          [beta_l^* alpha_k+alpha_l^* beta_k] g}
                                      dtheta/(2pi)^3 dx          (2)

is absolutely convergent in the spatial integral, torus integral and
complete exterior heat sum. For both actual probes,

    a^3 E_(i,N)^f -> K_(i,f).                                  (3)

The f,f term in the exact three-term expansion is O(N^2), hence has
zero cubic-scaled limit. Both mixed terms remain in (2). Replacing
only K_h by (L_D+Delta_T+epsilon)^(-1)Q in the complete remainder,
denoted E_(i,N,epsilon)^f, obeys the uniform estimate

    a^3 |E_(i,N)^f-E_(i,N,epsilon)^f|
                                      <=C_i sqrt(epsilon),
                      0<epsilon<=1.                            (4)

The value and sign of (2) are not evaluated. This supplies the last
separately retained transverse-H error limit; assembly with the other
placement coefficients and the complete other/other coefficient is
not performed here. In particular no compensation with -12 gamma D_i,
N^2 remainder, logarithmic coefficient, other-jet cancellation,
interacting error <=c_box/2, continuum axioms, reflection positivity,
infrared control or finite positive mass is established. The outside
factor 3 of the complete group is not applied in (2).

## Proof

### 1. Expand the actual remainder and isolate its extra mesh factor

L110's finite identity, including L099's use of symmetry of c_(i;kl,a)
to retain both generator orientations, gives exactly

    E_(i,N)^f=sum_(k,l,s,t)c_(i;kl,a) min(s,t)
      Tr_T[(K_h)_ts {(A_l^f(s))^T A_k^D(t)
                     +(A_l^D(s))^T A_k^f(t)
                     +(A_l^f(s))^T A_k^f(t)} G_tr(t)].          (5)

The middle P was absorbed using P A_k^f=A_k^f and P A_k^D=A_k^D;
this is an adjacent projection identity, not commutation. Expansion
of the transposed generator orientation exchanges k,l and the two
mixed terms. Keeping their sum and the f,f term therefore preserves
the full original orientation convention and its single factor 1/2.

L110(4), L111(1) and L088's heat bound give, for one fixed polynomial p,

    ||A_k^f(s)||<=C a^2 p(k),  ||A_k^D(s)||<=C a p(k),
    ||G_tr(s)||<=C/a,
    sum_(k,l)|c_(i;kl,a)|p(k)p(l)<=C_i.                         (6)

All levels and transverse rows are covered. The f,f block in (5),
including min(s,t) and G_tr, has norm at most C N a^3 p(k)p(l).
L095(14) gives sum_(s,t)||(K_h)_ts||_1<=C N^4. The trace-ideal
inequality therefore bounds its complete heat sum by C_i a^3 N^5,
which is O(N^2). Each mixed block instead has norm at most
C N a^2 p(k)p(l)<=C' a p(k)p(l). This is the extra factor absent
from the D,D core of L099/ATTEMPTS/030.

### 2. Remove covariance mass uniformly at cubic scale

For R_lambda=(L_D+lambda)^(-1), L099's positive resolvent argument gives

    R_lambda-R_(lambda+epsilon)>=0 entrywise,
    sum_t (R_lambda-R_(lambda+epsilon))_st
                         <=epsilon/[lambda(lambda+epsilon)].  (7)

Indeed the resolvent identity is epsilon R_lambda R_(lambda+epsilon),
both matrices have nonnegative entries, and their row sums are bounded
by 1/lambda and 1/(lambda+epsilon), respectively, by L095(13).
Every transverse block of the difference of the two K_h's is positive
semidefinite by the joint transverse spectral decomposition. Thus

    sum_(s,t)||(K_h-K_h,epsilon)_ts||_1
      <=(N-1) Tr_Q[epsilon/(Delta_T(Delta_T+epsilon))]
      <=C N^4 sqrt(epsilon).                                  (8)

For completeness the last step uses the exact relative shell bounds
lambda>=4r^2/N^2 and multiplicity <=C r^2, r>=1. The transverse trace
is bounded by C epsilon N^4 sum_(r>=1)(r^2+epsilon N^2)^(-1)
<=C' N^3 sqrt(epsilon), by comparison with the integral on [0,infinity).
No low physical mode is omitted. Equations (5)--(6),(8), and a<=1 give
C_i a N^4 sqrt(epsilon) for the full error before cubic scaling;
a^4 N^4=8^4 proves (4). The same positive row-sum bounds apply to
K_h,epsilon itself, so the f,f term stays O(N^2) uniformly in epsilon.
This proves a cubic-scale mass estimate, not an unsupported choice of
epsilon depending on N inside a fixed-mass theorem.

### 3. Verify the normalized exterior curvature and path coefficients

Set on the actual finite transverse spaces

    beta_(k,a)(s)=A_k^f(s)/a^2,
    alpha_(k,a)(s)=A_k^D(s)/a,       g_a(s)=a G_tr(s).

Their norms are bounded by Cp(k), Cp(k), C. The needed coefficient
regularity follows from the actual forest lift, not smoothness of a
zero-extended field. L028(9)--(11) and L080(5),(8) give on interior levels

    v_(k,a,mu)/a=A_(k,a,mu)-delta_(mu,a) Phi_(k,a),
    Phi_(k,a)(s,y)=a sum_(ell=0)^(s-1)
                A_(k,a,1)(-4+(ell+1/2)a,y),
    A_(k,a)=f_k/sqrt(lambda_(k,a)).                            (9)

Here delta is the physical incidence difference at the correct edge
center. The relative vertex potential vanishes on transverse boundary
vertices. Consequently the finite transverse incidence identity D d=0
cancels its prefix exactly, including the transverse end rows:

    f_(k,a,mu nu)/a^2
       =delta_(mu,a) A_(k,a,nu)-delta_(nu,a) A_(k,a,mu).         (10)

Tangential boundary values in (10) are the original zero sine samples;
no missing link is filled with a new value. The relative mode functions
have smooth sine/cosine extensions. Their fixed derivatives have bounds
polynomial in k, since the physical eigenvalues have a uniform positive
gap. The integral formula for a finite difference therefore gives
O(a p(k)) changes of (10) between existing neighbors, including axial
neighbors s,s+1 with 1<=s<N-1. At fixed labels (10) converges uniformly
on compact interiors to h_k in the hypotheses. This also fixes its sign.

For the path coefficients, an axial difference of (9) uses one prefix
summand; a transverse difference differentiates a prefix of physical
length at most 8. These facts, or L090(6)'s already established neighbor
bounds, give O(a p(k)) differences of b_(k,a)/a and q_(k,a)/a on existing
rows. L080's exact cosine prefix sum and L120's actual-path convergence
give their compact-interior limits b_k,q_k in (1), with the constant
axial mode retained. Fixed staggered shifts change these limits by zero.
The normalized curvature and path coefficients are bounded globally
on the existing rows; no extension through the upper pinned potential
is used.

P and Q are fixed contractions independent of s. Bounded stencil
multiplicity now gives

    ||beta_(k,a)(s+1)-beta_(k,a)(s)||
     +||alpha_(k,a)(s+1)-alpha_(k,a)(s)||<=C a p(k),
    ||g_a(s+1)-g_a(s)||<=C a.                                (11)

The last estimate uses L111's actual smooth displacement. Also g_a(s)
vanishes in fixed physical axial collars. These facts allow differences
of products ending in g_a to be extended by zero at s=0,N. They do not
assert a zero upper boundary value for beta or alpha.

### 4. Sum the massive axial kernel before the local transverse limit

Fix epsilon>0. Suppress the a subscript and put

    H_(kl;st)=[beta_l(s)^T alpha_k(t)
                              +alpha_l(s)^T beta_k(t)]g_a(t).

The mixed part of (5) after mass insertion is exactly
a^2 sum_(k,l,s,t)c_(i;kl,a) min(s,t) Tr_T[(K_h,epsilon)_ts H_(kl;st)].
By (11), boundedness, and |min(s,t)-s|<=|t-s|,

    ||a^2 min(s,t) H_(kl;st)-a^2 s H_(kl;ss)||
                               <=C a^2 p(k)p(l)|t-s|.          (12)

The term from the coefficient difference is bounded by
C a^3 s p(k)p(l)|t-s| and as<=8. This includes s near the ends,
where H_(kl;ss)=0; no boundary term has been dropped.

The positive massive axial kernel is bounded by the infinite kernel
exp(-kappa|t-s|)/(2 sinh kappa), 2 cosh kappa-2=lambda+epsilon.
For fixed epsilon its first offset moment is bounded uniformly over
0<=lambda<=12. Positivity of each transverse block consequently gives

    sum_(s,t)(1+|t-s|)||(K_h,epsilon)_ts||_1<=C_epsilon N^4.

This is the same scalar recurrence and domination used in L099,
proof section 3. Insertion of (12) costs O_(i,epsilon)(a^2 N^4),
hence O_(i,epsilon)(N^2). When H_(kl;ss) is nonzero, s is a distance
>=cN from both axial ends. The Dirichlet row sum then differs from
1/(lambda+epsilon) by at most C_epsilon exp(-c_epsilon N), from the
boundary-deficit recurrence. After the polynomial row and level counts
this error is still exponentially small. Thus, with
C_(epsilon,N)=(Delta_T+epsilon)^(-1)Q,

    a^3 E_(i,N,epsilon)^f
      =a^4 sum_(k,l,s)c_(i;kl,a)(as)
           Tr_T[C_(epsilon,N)
             {beta_l(s)^T alpha_k(s)+alpha_l(s)^T beta_k(s)}g_a(s)]
                  +O_(i,epsilon)(N^-1).                       (13)

The f,f term is included in the error using section 1. The identity
a^3 a^2 s=a^4(as) fixes the normalization; there is no additional
factor 8, 3 or 1/2. Equal axial levels occur only after this estimate.

### 5. Control the finite transverse projections before freezing

First fix exterior labels k,l. In (13) replace every P, including those
inside beta and alpha, by P_delta=T(Delta_0+delta)^(-1)T^T; replace
every Q by I-P_delta. Here T is the relative gradient and Delta_0=T^T T.
L097, proof section 4, gives for 0<delta<=1

    ||P-P_delta||_HS<=C N^(3/2) sqrt(delta).                    (14)

Its proof uses [delta/(lambda+delta)]^2<=delta/lambda and the full
relative inverse trace <=C N^3. All these projection replacements
are contractions. The other normalized factors in (13) have bounded
operator norms, with the inverse norm at most epsilon^-1 and ambient
dimension O(N^3). Telescoping and Hilbert--Schmidt Cauchy--Schwarz
give per-level error C_epsilon p(k)p(l) N^3 sqrt(delta). Since
a^4 sum_s(as)N^3 is bounded, the complete normalized error is
C_epsilon p(k)p(l) sqrt(delta), uniformly in N. No projection
operator-norm gain or termwise filter commutation is used.

For fixed epsilon,delta, approximate each inverse by the geometric
polynomial from L097/L099 on [0,12]:

    p_(z,m)(x)=(12+z)^(-1) sum_(j=0)^m [1-(x+z)/(12+z)]^j,
    sup |p_(z,m)(x)-(x+z)^(-1)|
                              <=z^-1[12/(12+z)]^(m+1).         (15)

The finite spectral theorem and bounded incidence norms give uniform
operator errors. Telescoping (13) bounds their normalized trace error
by C_(epsilon,delta) p(k)p(l) times those errors, uniformly in N.
This imports the established approximation, with its hypotheses
verified for the normalized f and D factors above, rather than a
new assertion about singular operator-norm approximation.

For fixed degrees all factors have finite range. A transverse collar
of that range has O(N^2) rows per level, including the staggered end
rows. Bounded entries make its contribution to (13) O_(epsilon,delta,m)
(a^4 N^2 sum_s as)=O_(epsilon,delta,m)(N^-1). For other rows, each
closed walk samples only existing interior stencils. Wherever it meets
g_a, the displacement places it in a fixed compact interior set for
sufficiently large N. Section 3's neighbor bounds permit freezing all
coefficients at one physical point on that walk, at an error
O_(k,l,epsilon,delta,m)(a) per normalized diagonal entry. Their uniform
fixed-mode limits are exactly (1). The normalized total error tends
to zero. The coefficient fields are only evaluated on this compact
set; zero extensions at faces and the separately pinned upper level
are never frozen as smooth fields.

For a constant-coefficient finite-range convolution, its diagonal
matrix trace is the torus integral of its matrix symbol: expand its
finite Fourier polynomial and integrate, retaining only the zero shift.
Riemann sums in all four physical coordinates in (13) therefore give
the integral of the frozen product, with weight x_1+4. There is no
parity cancellation premise. Send polynomial degrees to infinity
at fixed epsilon,delta, using (15); then send delta to zero using
(14). The frozen projection symbols converge almost everywhere and
are uniformly bounded. At fixed epsilon the remaining inverse is
bounded by epsilon^-1, so dominated convergence identifies the result
as (2) with lambda^-1 replaced by (lambda+epsilon)^-1. This proves
the fixed-pair, fixed-mass limit in the actual pinned box.

### 6. Restore heat tails and remove the mass

L080(4)--(6) and L120(6) give coefficient convergence at fixed pairs
and a uniform Gaussian heat majorant in k,l. The estimates of sections
1--2, also for the massive covariance, give modewise normalized bounds
Cp(k)p(l). Thus the omitted exterior heat pairs are uniformly bounded
by the tail of a summable Gaussian times a fixed polynomial. This
justifies fixed-pair truncation before the limits in section 5 and its
removal afterwards. Both actual probes, including their average-of-
squares and clover forms, use these same coefficients and bounds.

In (1), beta,alpha and g are bounded by Cp(k), Cp(k), C on the torus
and the compact physical support of g. Also lambda>=4|theta|^2/pi^2
on [-pi,pi]^3. Consequently the absolute integrand in (2) is bounded
by C p(k)p(l)/lambda, integrable in three dimensions. This proves
absolute convergence after the Gaussian heat sum. The symbols of real
stencils satisfy O(-theta)=overline(O(theta)); the same is true for
their adjoints and ordered products. Integration over the symmetric
torus therefore makes (2) real. Reality does not assert a sign or zero.

Dominated convergence sends the massive continuum functional to (2)
as epsilon decreases to zero. Combining its fixed-epsilon finite-box
limit with (4) gives

    limsup_N |a^3 E_(i,N)^f-K_(i,f)|
      <=C_i sqrt(epsilon)+|K_(i,f,epsilon)-K_(i,f)| -> 0.

This proves (3) with the stated order of limits. The argument does not
borrow a two-circulation moment for an unsandwiched kernel, assume
negligible cubic boundary errors, or transfer L099's D,D estimate to
cubic scale. It uses the extra exterior-circulation factor in (6),
which is precisely why that formerly insufficient mass estimate now
closes for this remainder.

This is RESEARCH / REPRODUCTION under the unchanged EXPLORE assessment
`drafts/literature/2026-10-10-other-other-cubic-leading-scale.md`.
The finite contraction, generator, positive scalar resolvent estimates,
projection estimates and polynomial method are imported from the cited
local results. The new applicability work is the normalized exterior
curvature, the extra cubic-scale mass gain and its fixed-mass trace
limit. This is local standard-method progress, with no originality
claim beyond the sources checked. No numerical coefficient is used.

## Mathlib

Full matching pinned remainder limit: **not checked**. Supporting finite
spectral, trace-ideal, relative cochain, Fourier-polynomial, Riemann-sum
and dominated-convergence coverage: **not checked**. Unknown coverage
is not absence. No general Ward or flow-finiteness theorem is assigned
to this isolated group's coefficient.
