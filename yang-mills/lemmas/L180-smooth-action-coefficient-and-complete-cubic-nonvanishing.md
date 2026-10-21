# L180 — Smooth-action coefficient and complete residual/action cubic nonvanishing

## Hypotheses

Keep L179's exact hypotheses: SU(2), all-face relative box D=(-4,4)^4,
a=8/N through admitted even meshes, straight direction-1 lower-rooted
forest, complete compact L008 displacement u, both actual L010 probes
i=3,6 at tau=1/16, and bare expansion at fixed mesh before refinement.
Import L179(1)-(8), including its established ordered, two-level limit,
both generator orders and controlled degree/mass removal. Set ell=x_1+4.
Write H_k=V_k for its transverse physical lift; H_(k,1)=0 on the
compact generator support, without imposing an upper forest value.
Use its q_l=d^*d A_l and real symmetric full heat coefficients c_(i;kl).

Import the precisely matching physical forms B_(i,G) of L140(1),
B_(i,R) of L145(1), P_(i,D) of L132(1), and diagnostic D_i of
L080(1)-(2). Their normalization is the same A_k=f_k/sqrt(lambda_k)
and c_(i;kl)=exp[-(lambda_k+lambda_l)/16]q_i(A_k,A_l), including
both inverse weights. L008 gives div u=0 and compact support.
Use L028's actual incidence, clover and endpoint compositions.

For numerical signs only, import L141(1), L082(1), L133's conclusion,
L144's conclusion, L146's conclusion and L174(3). These are complete
continuum intervals, including omitted heat modes. The heat intervals
retain their qualified L039 IEEE binary64 addition/multiplication/FMA,
no-overflow and underflow premises and source moment/time qualifications.
No independent upstream heat, processor or BLAS audit is claimed here.
The new finite stencil check and interval recombination use rational
arithmetic exclusively. No external Ward or renormalization theorem is
specialized beyond the saved assessment's scope.

## Conclusion

The smooth-action coefficient is exactly

    K_(i,Vmix)=-3 g_G [B_(i,G)-D_i-B_(i,R)/2+P_(i,D)/2],    (1)

where g_G is L140(2)'s negative scalar, enclosed in L141. In particular,
under the imported heat qualifications,

    414 < K_(3,Vmix) < 588,
    696 < K_(6,Vmix) < 989.                               (2)

L179(8)'s complete residual/action coefficient therefore satisfies

    84730 < lim a^3[-kappa_0(f_(3,0),r_1,S_3)] < 101038,
   -46188 < lim a^3[-kappa_0(f_(6,0),r_1,S_3)] < -36845.   (3)

Thus neither actual-probe cubic limit vanishes, subject to the stated
upstream qualifications. The complete term has positive triplet and
negative shear coefficient. This resolves the assessed isolated-term
vanishing test; it does not evaluate the complete L011 response or its
compensation, finer powers/logarithm, finite matching, interacting
reflected error <=c_box/2, continuum axioms or infrared finite mass.
There is no Yang--Mills candidate. This is local standard-method
REPRODUCTION, not a claim of progress beyond the sources checked.

## Proof

### 1. Contract the full frozen generator in the existing trace order

Work first at a fixed positive mass epsilon in L179(6). Its kernels
are absolutely summable, and Gamma S has finite range, so Fourier
contraction of the ordered Q J Q Gamma S density is justified.
Summing all axial offsets r in L179(4) sets the *stencil* axial
frequency theta_1 to zero. This does not identify the two physical
levels xi and eta in L179(5), or shorten either long prefix profile.

Use unitary edge-center and plaquette-center phases, with Fourier
fields exp(i theta dot z). Let p_nu=2sin(theta_nu/2),
e_nu=cos(theta_nu/2), v_nu=b_nu e_nu, and lambda_4=sum p_nu^2.
L028's compositions give exactly

    L=lambda_4 I-p p^T,
    K(b)=i E [(v dot p)I-p v^T],  E=diag(e_nu^2),
    Gamma(b)=[L K(b)+K(b)^* L]/2.                       (4)

Indeed D_(rho nu) has centered symbol i(p_rho A_nu-p_nu A_rho).
Its four-plaquette clover multiplies by e_rho e_nu; the endpoint
average multiplies by e_nu. Summing b_rho gives K in (4), with both
unequal filters retained. Incidence adjunction gives L. Because the
phases are unitary, the transpose in physical coordinates becomes
the conjugate transpose at frequency theta, with the existing order
preserved. No continuum replacement of these filters is made.

At theta_1=0, p_1=0 and e_1=1. Put X_nu=p_nu^2 and
lambda=sum_(nu=2)^4 X_nu. For transverse mu, row 1 of L K is zero
in column mu, whereas row 1 of K^* L is

    i b_1 p_mu [lambda e_mu^2-sum_(nu=2)^4 X_nu e_nu^2].

Thus, including the half in Gamma,

    Gamma_(1,mu)=i b_1 p_mu
                     [sum_nu X_nu^2-lambda X_mu]/8,
    Gamma_(1,1)=0.                                      (5)

All transverse components of b have canceled in this row. Formula
(5) uses both orders in (4); keeping just one would change it.
The endpoint *sum* S in L179 has centered symbol 2e_mu. Meanwhile
J_j has symbol 2i sin(theta_j), with its stated forward-minus-backward
sign. The scalar resolvent has symbol (lambda+epsilon)^(-1).
Consequently for transverse j,mu, the density in its exact order is

    T_(j,mu)[G_epsilon,b]
      =-(b_1/2) integral sin(theta_j) sin(theta_mu)
              [sum_nu X_nu^2-lambda X_mu]/(lambda+epsilon)^2. (6)

Every integral here and below uses normalized measure on [-pi,pi]^3.
The off-diagonal j!=mu entries vanish by independent angle reflection.
For the diagonals put

    n_mu=-X_mu(1-X_mu/4)
                      sum_(nu!=mu)X_nu(X_nu-X_mu).

Their full polynomial pairing is

    sum_mu n_mu=-(1/4)sum_(mu<nu)X_mu X_nu(X_mu-X_nu)^2.  (7)

To check (7), pair the ordered (mu,nu) and (nu,mu) terms before
summing: their sum is -X_mu X_nu(X_mu-X_nu)^2/4.
The common denominator (lambda+epsilon)^2 is permutation invariant;
there are three equal diagonal integrals and three equal unordered-pair
integrals. Therefore (6)-(7) give

    T_(j,mu)[G_epsilon,b]=(b_1/2) delta_(j,mu) g_epsilon,
    g_epsilon=-(1/4) integral
           X_2 X_3(X_2-X_3)^2/(lambda+epsilon)^2.        (8)

The component-1 column is zero by (5), as well as by H_(k,1)=0.
No row, physical face, exterior mode or path filter has been omitted.

There is also a finite rational check from the original integer-tail
definitions, independent of the centered-symbol derivation. Define
D_(rho nu,z) by the oriented four-link curl, its clover by the average
of its four translates z+a e_rho+b e_nu, a,b in {0,-1}, and K by
half the clovers at both link endpoints. Form L=D^T D, then the
entire row [L K+K^T L]/2 for each of four constant b basis vectors.
Sum its axial offsets and close with both actual S endpoints. For
b_1 and transverse mu its raw Laurent polynomial is precisely

    (z_mu-z_mu^(-1))/8
                      [sum_nu X_nu^2-lambda X_mu],
    X_nu=2-z_nu-z_nu^(-1);                              (9)

all other b/component cases give zero. This equals (5) times S after
restoring its unitary phases. The script named in section 4 checks all
16 complete rows and the full polynomial identity (7), coefficient by
coefficient over rational numbers; it does not sample angles.

### 2. Remove mass only after evaluating the fixed-mass functional

Define the full upper-action form

    B_(i,V)=sum_(k,l)c_(i;kl) integral_D ell u_1(x)
                    H_(k,T)(x) dot integral_(x_1)^4 q_(l,T)(eta,y) d eta dx.
                                                               (10)

It is absolutely convergent: the smooth mode q_l, H_k and their
derivatives have polynomial amplitude bounds in the mode indices,
the upper integral has length at most 8, and L179's complete
Gaussian heat majorant is summable against every such polynomial.
Insert (8) in L179(5)-(6), retaining q_l at eta throughout. Exactly

    K_(i;epsilon)=-3g_epsilon B_(i,V).                  (11)

This step changes no normalization: the -6 in L179 and the half in
(8) combine to -3; no additional color or outside factor is introduced.

For lambda>0,

    0<=X_2 X_3(X_2-X_3)^2/[4(lambda+epsilon)^2]
                      <=(X_2-X_3)^2/16<=lambda^2/16.   (12)

The right side is bounded on the torus and the limit extends by zero
at the origin. Dominated convergence proves g_epsilon->g_G as epsilon
decreases to zero, with g_G *exactly* L140(2)'s scalar. This verifies
mass removal for the contracted expression, rather than assuming that
epsilon may be set to zero in an uncontracted singular trace.
L179(7)'s already established mesh/degree/mass transfer and (11) now
give K_(i,Vmix)=-3g_G B_(i,V). Neither a mesh-dependent mass nor an
exchange of the two long axial sums was used.

### 3. Reduce the actual upper-action form without losing its face term

Write F_l=d A_l and let delta_(l,j)=sum_(b=2)^4 partial_b F_(l,jb),
the transverse positive action row in L140. Because mixed derivatives
of the physical lower primitive commute, curl_T H_l=curl_T A_l, and

    q_(l,j)=delta_(l,j)-partial_1 F_(l,1j),
    partial_1 H_(l,j)=F_(l,1j),  j=2,3,4.              (13)

These are smooth mode identities, including the constant axial mode;
they assert no smooth extension of the actual pinned forest jump.
Integrating the first identity in (13) all the way to the upper face
gives

    integral_(x_1)^4 q_(l,j)(eta,y) d eta
       =h_(l,j)(x)+partial_1 H_(l,j)(x)-U_(l,j)(y),     (14)

where h_l is precisely L140's full upper transverse-action primitive
and U_l=F_(l,1T)(4,y) is L080's positive upper-curvature row.
The endpoint term U_l is retained even though u is supported in the
interior. L080's diagnostic is the contraction of that boundary row
against the interior H, not a boundary integral of u.

Insert (14) in (10). Symmetry c_(i;kl)=c_(i;lk) identifies its first
term with B_(i,G) and its last term with -D_i, using exactly their
established normalizations. For the middle term set

    t_i(x)=sum_(k,l)c_(i;kl) H_(k,T)(x) dot H_(l,T)(x).

Absolute heat convergence justifies differentiating this sum. Its
contribution is (1/2)integral ell u_1 partial_1 t_i. Compact support
of u removes the boundary term. Since partial_1 ell=1 and
partial_1 u_1=-div_T u by L008,

    (1/2)integral ell u_1 partial_1 t_i
       =-(1/2)integral (u_1+ell partial_1 u_1)t_i
       =-B_(i,R)/2+P_(i,D)/2.                          (15)

Equations (14)-(15) prove B_(i,V)=B_(i,G)-D_i-B_(i,R)/2+P_(i,D)/2,
and hence (1). These identities can first be proved at finite exterior
cutoff and then passed to the full series by the same derivative/heat
majorants. Both probe sectors and the transition region remain; no
coordinate-swap deletion is needed. In particular the derivative of
ell and the actual upper endpoint must both be kept.

### 4. Import complete heat intervals and perform exact recombination

Use exactly the following full continuum intervals from the stated
canonical inputs; decimals denote exact rationals.

| i | B_(i,G), L144 | D_i, L082 | B_(i,R), L146 | P_(i,D), L133 |
| --- | --- | --- | --- | --- |
| 3 | (2408.3740053,2408.3740056) | (-237.289643,-237.289642) | (1228.1260684,1228.1260686) | (2359.1,2359.2) |
| 6 | (5174.7326818,5174.7326826) | (-98.877430,-98.877429) | (451.5469823,451.5469825) | (703.6,703.7) |

All four physical definitions have been matched in (10)-(15) before
using any interval. Taking the signed endpoints in (15) gives

    3211.150613 < B_(3,V) < 3211.2006144,
    5399.63661955 < B_(6,V) < 5399.68662145.             (16)

L141 gives -0.061<g_G<-0.043. Both intervals (16) are positive, so
multiplying them by -3g_G gives the exact rational enclosing pairs

    (414238429077/1000000000, 5738766723/9765625),
    (13931062478439/20000000000, 19762853034507/20000000000).

They lie strictly inside (2)'s simpler intervals. Finally import
L174(3)'s K_T intervals (84000,100000) and (-47000,-38000), and
L146's K_R intervals (-74.916,-52.809) and (-27.545,-19.416).
L179(8), using L172's already assembled E,E coefficient, is exactly
K_T+K_Vmix-6K_R. Independent interval addition gives

    (84731092429077/1000000000, 986690876098/9765625),
    (-923739017521561/20000000000, -736931746965493/20000000000).

These lie strictly inside (3) and exclude zero. Dependencies between
the imported quantities may widen this addition, but cannot invalidate
its inclusion. There is no extra outside factor three in this response.

Run, from the active notebook,

    python3 scripts/combined-ward-response/check_smooth_action_coefficient.py

The complete certificate is
`scripts/combined-ward-response/smooth-action-coefficient-certificate.json`.
It stores all 17 actual/required Laurent polynomial comparisons, their
complete coefficient errors, imported interval values, exact resulting
endpoints and every failure. All comparisons and inclusions pass with
zero failures. These checks verify the new algebra and recombination,
not L179's analytic limits or the upstream heat arithmetic. The latter
remain the explicit cited hypotheses of this result.

The intermediate test succeeds: the complete isolated residual/action
term has a qualified nonzero cubic coefficient for both actual probes.
Thus this term must be retained when comparing the other response jets;
its nonvanishing refutes only its proposed cubic-scale removal. It
neither refutes nor proves Yang--Mills, and supplies no uniform interacting
bound, finer remainder or complete compensation. The new reduction and
factor signs have received the bounded critical audit below; the imported
upstream premises and the distinction from the full response remain.

### 5. Independent critical audit of the local reduction

The separate 2026-10-14 audit checks (1)-(3), conditional on precisely
the hypotheses above. It does not audit L179's limit estimates,
L172/L174's preceding contractions or the upstream heat certificates.
No local mathematical correction was needed.

An independent raw-symbol computation uses four Laurent variables z_j,
with row D_(rho,nu)=(z_rho-1)A_nu-(z_nu-1)A_rho. Its adjoint sends
each z_j to z_j^(-1). Form all six rows before computing D*D. For
each displacement basis vector, the generator is constructed directly
as E M C D, with endpoint factor (1+z_nu)/2 and clover factor
(1+z_rho^(-1))(1+z_nu^(-1))/4. Multiplying the two matrix orders
separately, taking their half-sum, closing with 1+z_mu, and only then
setting z_1=1 independently reproduces every complete saved row in (9).
This is the axial stencil-offset sum, not identification of xi with eta.
The audit retains both individual orders on disk, including all zeros.
It imports no production checking code. Every coefficient in the saved
actual and required polynomials, and every recorded error coefficient,
is checked, rather than relying on their saved pass flags.

The hand check of the remaining torus integration is as follows. From
(4), at p_1=0 the LK row has zero transverse entries. The K*L row
has i b_1 p_mu[lambda e_mu^2-sum_nu X_nu e_nu^2], giving (5).
Multiplication by the endpoint sum and J yields (6) with its minus
sign. Angle reflection kills precisely j!=mu; pairing the two ordered
mu,nu numerators gives -X_mu X_nu(X_mu-X_nu)^2/4. Permutation
symmetry equates the three diagonal integrals and three pair integrals,
so their factors cancel and give (8), including its half. The single
-6 in L179(5) therefore gives -3g_epsilon, without any additional
color factor. Bound (12) proves mass removal by dominated convergence;
the full smooth-mode heat majorant justifies the separate physical sums.

The endpoint and IBP check uses the canonical definitions, not numerical
agreement. L140 defines delta_j=sum_b partial_b F_jb and its upper
primitive h; L080 defines U=F_1T(4) with positive orientation.
Since H_T=A_T-grad_T Phi and partial_1 Phi=A_1, its transverse
curl equals that of A and partial_1 H_T=F_1T. Thus d*d A has
transverse row delta-partial_1 F_1T, proving (14) with -U.
L080's D uses U_k H_l; symmetry of the real full c exchanges k,l
and matches it to the U_l H_k contraction here. The same exchange
matches L140's h_k H_l to h_l H_k. L145's B_R has weight u_1,
and L132's P_D has weight ell div_T u. Consequently the derivative
term is exactly

    (1/2) integral ell u_1 partial_1 t
      =-(1/2) integral u_1 t
         -(1/2) integral ell partial_1 u_1 t
      =-B_R/2+P_D/2.

Here compact support removes only the IBP boundary term, not U.
The lower-weight derivative equals one, and divergence freedom uses
the full transition-region displacement. These statements hold first
for every finite mode cutoff, including its constant axial mode, and
then for the complete sums by the stated derivative heat bounds.
All matched c and H definitions retain both covariance inverse weights;
no restriction of either actual probe is introduced by this audit.

For rational recombination the independent audit checks every imported
interval against its canonical conclusion statement and enumerates all
128 endpoint corners per probe in the seven independent variables
g_G,B_G,D,B_R,P_D,K_R,K_T. Both expressions are affine in each
variable separately, so their extrema on the input box occur at these
corners, as follows by successively interpolating each coordinate.
The resulting hulls reproduce all exact endpoints in section 4 and
lie strictly within (2)-(3). Treating correlated inputs independently
can widen the box but preserves inclusion. The numerical signs remain
conditional on the original complete heat/IEEE premises.

Reproduce this separate audit from the active notebook with

    python3 scripts/combined-ward-response/audit_smooth_action_coefficient.py

The full evidence is
`scripts/combined-ward-response/smooth-action-coefficient-audit-certificate.json`:
17 complete polynomial comparisons, both generator orders, all 256
endpoint corners, input hashes, actual/required hulls and zero failures.
This validates the local application of the imported results. It is
REPRODUCTION and supplies no new mathematical discovery beyond the
checked sources, no processor verification and no full-response or
Yang--Mills conclusion.

## Mathlib

Full matching coefficient/response theorem: **not checked**. Supporting
finite Fourier convolution, unitary phase changes, polynomial identities,
dominated convergence, compact-support integration by parts and rational
interval arithmetic: **not checked**. Unknown coverage is not absence.
Reuse the unchanged [assessment](../drafts/literature/2026-10-12-cubic-residual-action-cubic-scale.md).
No new external theorem is imported or reproved; the new specialization
is necessary to contract the actual two-level functional while retaining
its upper action endpoint and exact filters.
