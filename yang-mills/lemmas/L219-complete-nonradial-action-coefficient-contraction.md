# L219 — The complete nonradial action coefficient in existing E and R forms

## Hypotheses

Keep exactly L216–L218's SU(2) relative cube D=(-4,4)^4, admitted
meshes a=8/N, straight lower-rooted direction-1 forest, both actual
L010 probes i=3,6 at tau=1/16, and bare coefficient before refinement.
Import the established coefficient formulas L216(6),(8),(9) and
L217(3)–(6), including their complete boundary-collar, Green-tail,
half-fiber and heat-sum justifications. This contracts those limits;
it does not replace a finite-box covariance or repeat their limit proofs.
All colors, both residual subtractions, constant modes and full heat
sums remain in these imported statements.

Use L025's symmetric quartic tensor K with its original response
factor -24. Write h_(i,ab)=mathcal P_(i,ab) for the one-color physical
exterior matrix in L216(8). It is real symmetric. It agrees exactly
with sum_(k,l)c_(i;kl)V_(k,a)V_(l,b) in L134 and L145:
L008's whitened matrix entry is
<f_k,B_i f_l>=q_i(f_k/sqrt(lambda_k),f_l/sqrt(lambda_l)), and the
lower-rooted lifts and both heat weights are the same. No further
color factor or covariance-tilt factor is inserted.

Let K_(i,E) be L101/L134's complete cumulative coefficient and
K_(i,R)=g_G B_(i,R) be L145's complete reverse coefficient, with

    B_(i,R)=integral_D u_1 sum_(a=2)^4 h_(i,aa),
    g_G=-(1/4) integral XY(X-Y)^2/(X+Y+Z)^2 dtheta/(2pi)^3,
    X=4 sin^2(theta_2/2), Y=4 sin^2(theta_3/2),
    Z=4 sin^2(theta_4/2).

These are the established full physical forms, not finite-cutoff
numerical approximations. No numerical sign premise is needed here.

## Conclusion

For both actual probes the exact coefficient identities are

    P_i=-3 K_(i,E),
    A_i^dm=-(3/2) K_(i,R),
    A_i^nr=P_i+A_i^dm=-3 K_(i,E)-(3/2) K_(i,R).        (1)

Consequently L218's complete cubic coefficient can be written as

    mathcal L_i=Lambda_i+K_(i,T)+K_(i,Vmix)
          +3[K_(i,oo)-K_(i,E)]-(15/2)K_(i,R)+12 gamma D_i. (2)

The E contribution cancels exactly with the E term inside
3K_(i,oo). Equation (2) is not asserted to vanish or have either
sign. The remaining linked heat-form/scalar comparison is unevaluated.
Even zero would leave smaller powers, logarithms, finite matching,
a cutoff-uniform coupling expansion, reflected error <=c_box/2,
continuum axioms and infrared finite mass unresolved. No Yang–Mills
candidate is supplied. The separate critical audit in proof section 7
accepts this local reduction relative to its imported limit inputs.

## Proof

### 1. Contract the entire local tensor over all colors

Use traversal order (mu,nu,-mu,-nu), where 2<=mu<nu<=4. For a
real symmetric four-by-four matrix V, put a color Kronecker delta
on its entries, as in both L216 and L217. The exterior matrix is
U_(lc,md)=delta_cd sigma_l sigma_m h_(i,n_l n_m), with
sigma=(1,1,-1,-1). Direct contraction gives

    -24 K:U:V = h_(i,mu mu) H_mu:V
              +h_(i,nu nu) H_nu:V+h_(i,mu nu) H_cross:V, (3)

where M:V=sum_(l,m) M_lm V_lm includes both ordered off-diagonal
entries, and

    H_mu = [ 1 2 1 2 ]    H_nu = [ 0 2 6 2 ]
           [ 2 0 2 6 ]           [ 2 1 2 1 ]
           [ 1 2 1 2 ]           [ 6 2 0 2 ]
           [ 2 6 2 0 ],          [ 2 1 2 1 ],

    H_cross = [  0  3  0 -3 ]
              [  3  0 -3  0 ]
              [  0 -3  0  3 ]
              [ -3  0  3  0 ].                         (4)

Here is a finite algebra derivation fixing every color and factorial.
For y_l in R^3 let q be L025(3)–(4), with bracket minus the vector
cross product. Set

    D_mu=sum_c (partial_(1c)-partial_(3c))^2,
    D_nu=sum_c (partial_(2c)-partial_(4c))^2,
    D_cross=2 sum_c (partial_(1c)-partial_(3c))
                         (partial_(2c)-partial_(4c)).

Substituting the simultaneous cubic BCH recurrence and using
sum_c |[e_c,v]|^2=2|v|^2 gives the quadratic polynomials

    D_mu q=-(1/6)[|y_1+y_3|^2
                 +4(y_1+y_3) dot (y_2+y_4)+12 y_2 dot y_4],
    D_nu q=-(1/6)[|y_2+y_4|^2
                 +4(y_1+y_3) dot (y_2+y_4)+12 y_1 dot y_3],
    D_cross q=-(y_1-y_3) dot (y_2-y_4).                (5)

The same formulas can be checked without BCH by multiplying the four
exponential series: the degree-four coefficient of -4 times their
normalized trace, plus |sum y_l|^4/96, is exactly q. This is a finite
polynomial identity; no limiting or Gaussian argument is involved.
For D_V=sum_(l,m,c)V_lm partial_(lc)partial_(mc), the symmetric-tensor
convention gives D_V D_U q=24K:U:V. Applying D_V to (5), where
D_V(sum H_lm y_l dot y_m)=6 H:V, proves (3)–(4). Thus the three
colors and the factor -24 have already been used once.

For the following contractions introduce traversal columns

    k=(1,1,1,1), A=(1,0,-1,0), B=(0,1,0,-1),
    t_mu=(1,0,1,0), t_nu=(0,1,0,1).

Then the same matrices are

    H_mu=kk^T+k t_nu^T+t_nu k^T-3 BB^T,
    H_nu=kk^T+k t_mu^T+t_mu k^T-3 AA^T,
    H_cross=3(AB^T+BA^T).                             (6)

### 2. Match the complete plateau to E before integrating

All four L216 dipoles sum to zero. Therefore the plateau matrix
annihilates k on both sides. Only the last terms of (6) survive.
Use component-center phases, d_a=2 sin(theta_a/2),
eta_a=cos(theta_a/2), lambda=sum_(a=2)^4 d_a^2. The two dipole
combinations A and B, after removal of the common plane-center
phase, have respective row amplitudes

    2i eta_nu d_mu,       2i eta_mu d_nu.

Thus the plane contribution to (3), inside its normalized torus
integral, is

    -12 m_E/lambda^2 * [
       h_(i,mu mu) eta_mu^2 d_nu^2
      +h_(i,nu nu) eta_nu^2 d_mu^2
      -2 h_(i,mu nu) eta_mu eta_nu d_mu d_nu].         (7)

Sum all three transverse planes. With E=diag(eta_a), this is

    -12 (m_E/lambda) Tr[h_i E(I-dd^T/lambda)E].       (8)

L134 proof section 1, especially (6), contracts the exact L101
path functional to 4(m_E/lambda) times this same trace. The
exterior normalization was matched in the hypotheses. Hence (8)
is exactly minus three times that functional, pointwise before
physical integration and the full heat sum. Absolute convergence
from L216 and L134 permits those operations and proves P_i=-3K_(i,E).
In particular the whole m_E is retained: its cumulative W_a, moving-cut
u_1 term and both insertion subtractions are not removed. No physical
integration by parts or affine-core replacement is used here.

### 3. Obtain the full frozen residual symbol with its original filters

For this section theta has four components, lambda_4=sum_(a=1)^4 d_a^2,
eta_a=cos(theta_a/2), f_a=eta_a^2, v_a=u_a(x)eta_a, and
P=I-dd^T/lambda_4 is the four-dimensional co-closed projection.
Symbols refer to input/output link centers. Converting from the
lower-vertex convention is a diagonal unitary phase change; all
selector phases below are converted with it.

The exact endpoint average on output a contributes eta_a. The
ordered (rho,a) clover contributes eta_rho eta_a. Consequently the
frozen dimensionless generator in L217(3) has symbol iR, where

    R_ab=f_a[(v dot d) delta_ab-d_a v_b].

This retains the unequal output filters eta_a^2; it is the same
ordered-stencil calculation as L118(9), applied to all four directions.
Since C^*C=lambda_4 P and Sigma_infinity=lambda_4^(-1)I, L217's
W_x in component-center coordinates is

    W_c=iQ,
    Q=(P R-R^T P)/(2 lambda_4).                     (9)

Q is a real antisymmetric matrix. Equation (9) follows from the
symmetrized generator before any selector is contracted; neither
order is deleted. The insertion subtractions do not appear in this
normalized local symbol because L217 already bounded and removed
their contribution here. They remain in the plateau symbol above.

For rigor at zero frequency, write F=diag(f_a)=I-diag(d_a^2)/4
and R=F R_0, R_0=(v dot d)I-dv^T. Then
P R_0=R_0^T P=(v dot d)P. Thus the numerator in (9) is O(|d|^3),
and Q=O(|d|) as d tends to zero, uniformly for bounded u. Define
Q(0)=0. Q is bounded and continuous on the closed frequency cube,
with the centered endpoint phases understood; no unbounded inverse
operator is being assumed.

### 4. Keep both mixed half-fibers and their endpoint half-weights

Fix a transverse plane mu<nu. After removing the common plane-center
phase, its direct selector rows are

    d_1=e^(-i theta_nu/2)e_mu^T,
    d_2=e^( i theta_mu/2)e_nu^T,
    d_3=-e^( i theta_nu/2)e_mu^T,
    d_4=-e^(-i theta_mu/2)e_nu^T.                    (10)

To compute the already absolutely convergent half-fibers in L217,
first give their axial links r=-1,-2,... the weights rho^(-r-1),
0<=rho<1. Their common axial amplitude is

    s_rho(theta_1)=e^(-i theta_1/2)/(1-rho e^(-i theta_1)). (11)

Each prefix row w_l has component 1 only; its scalar entry is the
scalar coefficient of d_l times i d_(n_l) s_rho. This follows from
the actual endpoint difference end minus start and the axial-link
centers r+1/2. Thus the last included axial link is -1, not zero.
The traversal combinations in (6) become

    k_d=i z, z=-d_nu e_mu^T+d_mu e_nu^T,   k_w=0,
    A_d=2eta_nu e_mu^T,    B_d=2eta_mu e_nu^T,
    (t_mu)_d=-i d_nu e_mu^T, (t_nu)_d=i d_mu e_nu^T,
    A_w=2i eta_nu d_mu s_rho e_1^T,
    B_w=2i eta_mu d_nu s_rho e_1^T,
    (t_mu)_w=d_mu d_nu s_rho e_1^T,
    (t_nu)_w=-d_mu d_nu s_rho e_1^T.                (12)

The local direct/mixed matrix is exactly d W d^* - d W w^* - w W d^*.
By (6),(9),(12), every direct/direct contraction in (3) is zero:
its diagonal terms are real-row quadratic forms in iQ, while each
remaining symmetric cross term is twice the real part of a purely
imaginary scalar. This is a contraction-specific identity, not
vanishing of W or of the individual ordered generator.

For H_mu the two mixed terms sum to

    -2 Re(s_rho) [d_mu d_nu z Q e_1
                               -12 eta_mu^2 d_nu Q_(nu,1)].       (13)

For H_nu the bracket is

    -d_mu d_nu z Q e_1-12 eta_nu^2 d_mu Q_(mu,1),

and for H_cross it is

    12 eta_mu eta_nu[d_nu Q_(mu,1)+d_mu Q_(nu,1)].   (14)

These follow by inserting (12) into (6); in particular H_mu has
only k_d W (t_nu)_w^*-3B_d W B_w^* in its d W w^* orientation.
The second orientation is its conjugate and gives the factor 2 in
(13). There is no second, additional mixed factor afterward.

Here is a controlled evaluation of (11), including its real endpoint
mass. With normalized one-dimensional torus measure,

    Re(s_rho)=(1-rho)cos(theta_1/2)
                    /[(1-rho)^2+4rho sin^2(theta_1/2)].            (15)

It is nonnegative on [-pi,pi]. It is the Poisson kernel
(1-rho^2)/(1-2rho cos(theta_1)+rho^2) multiplied by
cos(theta_1/2)/(1+rho). The Poisson kernel has integral one by its
geometric Fourier series; its integral outside any neighborhood of
zero tends to zero by the displayed denominator. Therefore for any
continuous F on this interval,

    integral Re(s_rho)F -> F(0)/2.                  (16)

The masses are uniformly bounded. The bracket functions (13)–(14)
are continuous in all four angles by the bound after (9), so (16)
can be integrated over the transverse angles, by bounded convergence.
There is no singular principal-value substitution. Independently,
L217's absolute spatial half-fiber convergence implies that its
Abel-weighted sums tend to the original sums: bound the tail by the
absolute tail and take rho to one on the finitely many retained
levels. Thus this evaluation gives precisely L217's two half-fibers,
not a different prefix prescription.

Combining -2 in (13) with the half in (16) replaces each bracket
by its negative at theta_1=0. Both original orientations are retained.
At that frequency set X_a=d_a^2, lambda=sum_(a=2)^4 X_a and
T=(sum_(a=2)^4 X_a^2)/lambda. Equation (9) gives

    Q_(a,1)=u_1 d_a(X_a-T)/(8lambda),  a=2,3,4.     (17)

Indeed R_(a,1)=-f_a d_a u_1, R_(1,a)=0, and projection subtracts
d_a sum_b f_b X_b/lambda; sum_b f_b X_b=lambda-(sum_b X_b^2)/4.
All transverse displacement components have disappeared by this exact
frequency evaluation, not by an unsupported spatial reflection.

### 5. Contract all planes and identify the existing scalar

The off-diagonal physical coefficient from (14),(17) is odd in
both theta_mu and theta_nu, times a function even in each angle.
It is bounded, and its torus integral is zero. The diagonal coefficient
multiplying h_(i,mu mu), for one plane, is

    u_1/[8lambda] * [
       X_mu X_nu(X_mu-T)+(12-4X_mu)X_nu(X_nu-T)].     (18)

This is the negative of (13)'s bracket: z Q e_1=-d_nu Q_(mu,1)
+d_mu Q_(nu,1), and 12eta_mu^2=12-3X_mu. This fixes the sign.
For a fixed output direction mu the other two plane directions have
equal integrals by permutation symmetry of the complete torus.
The resulting coefficient, independent of mu, is therefore

    c_dm=integral [XY(X-T)+(12-4X)Y(Y-T)]/(4lambda),
    lambda=X+Y+Z, T=(X^2+Y^2+Z^2)/lambda.            (19)

All integrands here are bounded at the origin and absolutely integrable.
Define

    I_0=integral Y(Y-T)/lambda,
    I_1=integral XY(X-T)/lambda,
    J=integral XY(X-Y)^2/lambda^2.

Permutation symmetry gives I_0=0: three equal copies sum to the
integral of [(X^2+Y^2+Z^2)-lambda T]/lambda=0. The analogous
integral with XY(Y-T) equals I_1 by X/Y exchange. Consequently
(19) gives c_dm=3I_0-(3/4)I_1.

To evaluate I_1, its numerator over lambda^2 is
XY[XY+XZ-Y^2-Z^2]. The integral of XY(XZ-Z^2) vanishes by
X/Z exchange. Averaging XY(XY-Y^2) with its X/Y exchange leaves
-(1/2)XY(X-Y)^2. Thus I_1=-J/2=2g_G, where the last equality
is precisely L145(2)'s existing scalar. It follows that

    c_dm=3J/8=-(3/2)g_G.

The physical factor remaining from (18) after plane summation is
integral_D u_1 sum_a h_(i,aa)=B_(i,R), with the same complete
heat coefficients as L145. Hence A_i^dm=-(3/2)K_(i,R), proving
(1). This scalar equality is an integrated permutation identity;
no pointwise proportionality to L145's integrand is claimed.
Substitution into L218(2) proves (2). In particular -6K_(i,R)
in that assembly and the new -(3/2)K_(i,R) total -(15/2)K_(i,R),
while the R still inside K_(i,oo) has not been subtracted again.

### 6. Exact checks, source scope and remaining review

Run `python3 scripts/combined-ward-response/joint_action_color_contraction.py`.
The full certificate is
`scripts/combined-ward-response/joint-action-color-contraction-certificate.json`.
It compares every coefficient of the twelve-variable quartic from BCH
against independent multiplication of the four SU(2) exponential series
(216 nonzero coefficients; zero difference polynomial). It checks all
48 entries of (4) independently by exact differential contraction.
It also checks (13)–(14) in 24 exact complex-rational finite-prefix
fixtures, including every displacement component and plane, with all
six direct/mixed defects zero per fixture. Finally the difference
between (19) and 3J/8, after multiplication by 8lambda^2 and summing
all six coordinate permutations, is the zero polynomial. All checks
pass; the complete selected check arrays and difference polynomials
were inspected, not only a preview. The script proves finite algebra
and checks signs; the all-frequency identities and Abel-limit transfer
are justified analytically above. It evaluates neither actual probe.

The unchanged ready assessment is
`drafts/literature/2026-10-16-complete-residual-coefficient-cubic-assembly.md`.
Its inspected primary flow/Ward results do not compute this bare
forest coefficient. L025 already supplies the quartic, L216–L217 the
complete limits, L134 the E tensor, and L145 the R scalar and heat form;
none previously identifies their present relation. The work is this
finite contraction and the applicability comparison, classified local
REPRODUCTION without a novelty claim beyond the sources checked.
No external theorem is reproved. ATTEMPTS/011–012's raw-loop/Wick
norm failures and ATTEMPTS/022's different frozen-trace failure remain
intact. No termwise forest invariance or interval overlap is used.

The separate audit below checks the normalization, original lower-vertex/
center phase conversion, both half-fibers ending at -1, uniform Abel
evaluation at the origin, and exact identification of both heat forms.
Upstream analytic and any later imported IEEE premises remain imported;
no recursive certification or complete-response sign is claimed.

### 7. Separate critical audit, 2026-10-17

This audit accepts (1) and its substitution (2) without correction,
relative to the stated L216/L217 limit inputs. It does not audit all
earlier estimates recursively or decide the remaining compensation.
The unchanged ready complete-coefficient assessment covers this test;
no external result or new source scope is introduced.

**Color and tensor normalization.** L025(4) defines K as the fully
symmetric fourth derivative divided by 24, and L025(6) assigns -24
to precisely this pairing class. For a quartic q=K y^4, applying
two constant second-order differential operators gives 24K:U:V,
including repeated coordinate indices. In particular D_cross has
the displayed factor 2 because h_mu,nu enters both ordered exterior
entries. Applying D_V to a single-color quadratic and summing three
colors gives 6H:V. For example the first line of (5) therefore gives
coefficients 1 on (1,1),(3,3),(1,3),(3,1), 2 on all ordered
mu/nu entries, and 6 on (2,4),(4,2), exactly H_mu in (4).
The other lines give H_nu and H_cross with the same convention.
There is no remaining color, Wick or tilt factor. The production
polynomial checker was inspected and replayed: all 216 coefficients
match independent exponential multiplication, all 48 differential
entries match the displayed matrices, and the full difference
polynomial and failure list are empty. This replay is distinguished
from the independent all-frequency checker described below.

**Raw stencil and selector phases.** Here is a direct check of the
ordered filters underlying L118(9), retaining all four directions.
Put z_a=exp(i theta_a/2), e_a=z_a^2, and consider the coefficient
of u_rho with output component a!=rho. The original site clover and
endpoint average, acting on the lower-vertex circulation row, give

    K^raw_(ab)[u_rho]
      =[(1+e_a)(1+e_rho^(-1))(1+e_a^(-1))/8]
         [(e_rho-1)delta_ab-(e_a-1)delta_(rho,b)].       (20)

The rho=a term is zero. Multiplying (20) by z_a^(-1) on output
and z_b on input yields exactly
i eta_a^2 eta_rho[d_rho delta_ab-d_a delta_(rho,b)],
which is the u_rho coefficient of iR. The same conversion gives
C^*C=lambda_4 P. Inserting this before both scalar inverse factors
gives i(P R-R^T P)/(2lambda_4), with the minus sign coming from
the adjoint of iR. Thus (9) has the correct sign and denominator.

For the plane (mu,nu), raw direct selectors have lower offsets
0,e_mu,e_nu,0, component directions mu,nu,mu,nu and signs
1,1,-1,-1. Multiplying their input center phases and dividing by
the common plane phase z_mu z_nu gives (10). The four raw vertex
differences are e_mu-1, e_mu(e_nu-1), e_nu(1-e_mu), 1-e_nu;
here e denotes the Fourier phase, not the unit vector in the preceding
offset list. They sum to zero. The same plane conversion gives
i d_(n_l) times the scalar direct row, as used in (12).
The axial-link center at lower level r is r+1/2, so the last link
r=-1 contributes z_1^(-1). For R finite the exact geometric identity is

    (1-z_1^(-2)) sum_(r=-R)^(-1) z_1^(2r+1)
       =z_1^(-1)(1-z_1^(-2R)).                       (21)

Weighting r=-1-n by rho^n gives (11). This verifies the actual
half-fiber, including its endpoint, rather than selecting a Fourier
prescription after taking a limit. L216's negative-exponent dipole
transform conjugates all these transverse phases together; its real
even m_E and symmetric bilinear contraction give the same (7).

**Independent complete Laurent checks.** Run
`python3 scripts/combined-ward-response/joint_action_critical_audit.py`.
The full certificate is
`scripts/combined-ward-response/joint-action-critical-audit-certificate.json`.
It uses exact rational Laurent coefficients and i^2=-1, imports no
production contraction routines, and compares every coefficient of
each difference, rather than values at selected frequencies. All
100 checks pass: 64 entries of (20)'s conversion for the four
displacement basis vectors, 12 raw endpoint rows, 18 complete
direct/mixed contractions over the three transverse planes, three
finite geometric identities and three zero-axial residual entries.
The direct/mixed test treats all six real entries of Q and both
real components of the prefix amplitude as independent variables.
It therefore verifies the cancellation and (13)–(14) for arbitrary
skew Q and complex prefix amplitude. Every saved difference
polynomial is empty, and the full failure list is empty. Required
defect count is zero. These checks support finite identities only;
the following analytic argument is essential for the infinite prefix.

**Abel transfer and its uniform bound.** From F-I=O(|d|^2),
R_0=O(|d|), and ||P||<=1, the numerator PR-R^TP in (9) is
O(|d|^3), uniformly for bounded u. Thus Q=O(|d|), including
the common origin, and all brackets (13)–(14) are bounded continuous
functions of the four angles. No singular inverse norm is used.
For 0<=rho<1, the real kernel (15) is nonnegative and at most
the Poisson kernel divided by 1+rho; its mass is therefore <=1.
Outside |theta_1|<delta its mass tends to zero, while the continuous
factor cos(theta_1/2)/(1+rho) at zero tends to 1/2. Splitting a
continuous bracket into its value at zero and a uniformly small
remainder inside this interval proves (16). Compactness of the
transverse frequency cube makes the argument uniform in its three
parameters. Boundedness also permits the physical integration and
the imported absolutely convergent heat sum. The imaginary part
of s_rho has already canceled between the two orientations by
(13)–(14); it is not discarded using a principal-value rule.

Independently L217(13),(15) give an absolute infinite fiber tail
C/R for each endpoint row. An Abel weight lies between zero and
one, so the omitted Abel tail has the same bound. On the finitely
many retained levels the weights tend to one. This identifies the
Abel value with the original two spatial sums in L217(6). Together
the mixed factor -2 and endpoint mass 1/2 give the negative bracket
at theta_1=0. Direct computation from the full residual numerator
2lambda_4^2 Q=lambda_4(R-R^T)-dd^TR+R^Tdd^T also verifies
(17); no transverse displacement survives at that frequency.

**Scalar and actual-probe applicability.** In (19), the identity
sum_a X_a(X_a-T)=0 proves I_0=0 only after the equal permutation
integrals are identified. X/Z exchange cancels the XZ-Z^2 part
of I_1, and X/Y averaging gives I_1=-J/2. These operations are
valid on bounded integrands, including the origin by continuity.
They prove c_dm=3J/8=-(3/2)g_G; the production check's complete
six-permutation numerator also vanishes identically. This is an
integral identity, not equality of the unsymmetrized integrands.

L008(8),(11) give beta_(i;kl)=q_i(f_k/sqrt(lambda_k),
f_l/sqrt(lambda_l)). Therefore L216(8)'s exterior matrix is exactly
sum_(k,l)c_(i;kl)V_k V_l^T in L134 and L145, including both inverse
square roots, exp[-tau(lambda_k+lambda_l)], the same one-color q_i,
and the lower-rooted lift with its constant axial mode. L101(4),(5)
uses the identical m_E of L216(5), including its moving-cut endpoint
and cumulative subtractions. L134(6) then matches (8) with ratio -3.
L145(1),(2) matches the remaining u_1 Tr(h_i) form and scalar with
ratio -3/2. Both identifications hold for each full probe, before any
numerical enclosure. Lastly L218(2) contains -6K_R once; adding the
new -(3/2)K_R gives -(15/2)K_R, leaving the R within K_oo intact.
This accepts the stated reduction without assigning a value, sign
or vanishing to the remaining linked combination.

## Mathlib

Full specialized action-coefficient identity: **not checked**. Supporting
finite polynomial differentiation, trigonometric Fourier conversion,
Poisson-kernel approximation and permutation-invariant integration:
**not checked**. Unknown coverage is not absence. The necessary finite
algebra and approximate-identity argument are given above; no matching
Mathlib theorem or new external source result is assumed.
