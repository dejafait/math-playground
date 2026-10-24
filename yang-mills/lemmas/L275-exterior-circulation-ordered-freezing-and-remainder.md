# L275 — Ordered freezing and the complete exterior-circulation remainder

## Hypotheses

Use exactly E_(i,N)^f and K_(i,f) in L123(2)--(5), and the two
literal whole-grid words U_i^b(epsilon,delta) in L274(3). Retain the
relative SU(2) cube, actual probes i=3,6, admitted sufficiently large
even N, a=8/N, tau=1/16, straight lower-rooted direction-1 forest,
ordinary stored coordinates and bare-first expansion. Keep both mixed
orientations, every original axial level, all source/end rows, constant
component indices, staggered filters and full heat sums. Import all
upstream qualifications; this is not their separate critical audit.

Continuum h_k,b_k,q_k,C_k,F_k and the complete ordered generator
H(x,theta)=sum_r T_r(theta)u_(rho(r))(x)C_r(theta) have precisely
L123(1)'s conventions, so g=H D. Let lambda=sum_mu |t_mu|^2 and
t_mu=exp(i theta_mu)-1 on the three-dimensional torus. Define

    P_delta=t t*/(lambda+delta), Q_delta=I-P_delta,
    A_epsilon=D/(lambda+epsilon),
    B_epsilon=D D*/(lambda+epsilon).

Symbols here use integer lower-vertex indices on each component grid.
Every component-center shift remains in its original finite stencil.
For positive masses set

    W_(kl;epsilon,delta)(x,theta)
      =tr_F[A_epsilon C_l* P_delta F_k D H
                    +B_epsilon F_l* P_delta C_k Q_delta H],
    K_i(epsilon,delta)
      =sum_(k,l)c_(i;kl) integral_D (x_1+4)
              integral_T W_(kl;epsilon,delta)(x,theta) dtheta dx. (1)

The torus measure is dtheta/(2pi)^3. The heat coefficients in (1)
are the full continuum coefficients of L120(2). This definition keeps
both projection positions in the second word. No regularized projection
is treated as idempotent.

## Conclusion

At epsilon=N^(-1/2), delta=N^(-2/3),

    |U_i^b(epsilon,delta)-a^(-3)K_i(epsilon,delta)|
                                      <=C_i N^(9/4),          (2)
    |K_i(epsilon,delta)-K_(i,f)|
               <=C_i[epsilon log(e/epsilon)+delta^(3/4)].       (3)

Consequently, with L274(5) counted once,

    |E_(i,N)^f-a^(-3)K_(i,f)|
                              <=C_i N^(5/2)log(eN).           (4)

This is stronger than the approved N^(5/2)log(eN)^2 component budget.
It is a local quantitative specialization of polynomial localization,
Fourier inversion and elementary trace estimates, with no source-level
novelty claim. It neither evaluates K_(i,f) nor audits L272--L274.
The separate critical audit in proof section 6 accepts this rate relative
to its imported premises. Complete transverse-H
and L011 quantitative assembly, other pending audits, interacting
reflected-error control, continuum axioms and infrared positive mass
remain unresolved. No complete-solution candidate is asserted.

## Proof

### 1. Match interior raw scalars without smoothing their zero extensions

L111(1) gives H_s=sum_r T_r M_(u_(a,rho(r),s)) C_r. Both endpoints
of its nonzero stencils lie in a common fixed physical compact subset
of the transverse box. There is also a fixed axial collar where H_s=0.
L028 proof section 1 supplies globally smooth compact u_a with uniform
C^m bounds for each fixed m and ||u_a-u||_(C^m)<=C_m a^2. Choose fixed
smooth transverse cutoffs chi_0,chi_1 with chi_0=1 in a neighborhood
of all these generator endpoints, chi_1=1 near supp(chi_0), and both
supports strictly interior. The neighborhoods have fixed positive
physical width, uniformly in s and sufficiently large N.

For one normalized scalar raw array w_raw among h_(k,a)=f_k/a^2,
b_(k,a)/a,q_(k,a)/a, write w(x) for h_k,b_k,q_k, respectively. At
every existing row in supp(chi_0), at the original level s<N,

    |w_raw(s,y)-w(x_(s,y))|<=C a p(k),
    |w_raw(s,y)|+|w(x_(s,y))|<=C p(k).                (5)

For b,q this is L248(3)--(8)'s unaveraged raw-link comparison applied
to the four signed traversal slots, not its endpoint-averaged diagnostic.
For h, use exactly L123(10): the transverse prefix cancels by Dd=0,
so h_(k,a)=delta_mu A_(k,a,nu)-delta_nu A_(k,a,mu). The integral formula
for a difference at its actual shifted edge, followed by L222(3), gives
error <=C[a||A_k||_(C^2)+a^2(1+|k|)^2]<=C a p(k).
The mode derivatives in both inputs give polynomial C^m bounds for
the continuum scalars, for every fixed m. Enlarge the fixed polynomial
p throughout. The allowed component-1 constant axial index is retained
in L248's exact prefix formula. No value at the separately pinned upper
forest row is used.

On the whole grid define smooth samples and pasted samples by

    w_sm(s,y)=chi_1(x_y) w(x_(s,y)),
    w_p(s,y)=w_sm(s,y)+chi_0(x_y)[w_raw(s,y)-w_sm(s,y)]. (6)

The raw array here is L274's bounded zero extension. Pasted and raw
arrays agree near generator support; (5) and chi_1=1 on supp(chi_0)
give ||w_p-w_sm||_infinity<=C a p(k) globally. These statements make
no regularity assertion about w_raw or w_p at a face.

Rebuild Cbar,Fbar in L274(2) using these arrays and keep H_s unchanged.
Call the resulting traces U_p,U_sm. To compare U^b with U_p, apply
L274(9)--(15)'s geometric inverse polynomials on the same infinite edge
and vertex spaces, with its common degree

    m=ceil(312 N^(2/3)log(eN)).

All inverse errors are at most N^(2/3)(eN)^(-24). Every polynomial
path starting at a generator endpoint has total length <=3m+r_*;
this is o(N), so it remains in the neighborhood where chi_0=1.
Thus the complete polynomial traces for raw and pasted arrays agree
exactly, including all intermediate and input indices. All arrays
in (6) have the same polynomial sup bounds. L274's trace count,
rank(H_s)<=C N^3 and a^2 sum_s s<=32, therefore gives

    |U^b-U_p|<=C_i N^3[xi_(epsilon,m)
                          +epsilon^(-1)xi_(delta,m)]
                                                <=C_i N^(-10). (7)

This is an estimate of the genuine remote raw-row contribution before
interior matching. It does not cut off a true covariance source.

Telescope U_p-U_sm in its two original local coefficient positions.
Bounded stencil multiplicity gives O(a p(k)) operator errors in Cbar
and Fbar. All remaining factors except A_epsilon are contractions or
bounded fixed stencils, and

    ||A_epsilon||<=C epsilon^(-1/2),
    ||B_epsilon||<=1.

Cycle only to finite-rank H_s and use its trace norm <=C N^3. Sum
the full polynomial heat envelope and the original a^2 s weight. Then

    |U_p-U_sm|<=C_i a N^3 epsilon^(-1/2)
                                         <=C_i N^(9/4).       (8)

The second word even has error O(N^2). The local error bounds apply
globally to the pasted difference in (6), so no inverse output or
projection input has been assumed compact in (8).

### 2. A closed Fourier trace estimate with all component orders retained

We prove the needed estimate rather than invoking a kernel first
absolute moment. Put r=|theta| on [-pi,pi]^3; lambda is comparable
to r^2. The derivative bounds for t,D and lambda imply, uniformly
in 0<epsilon,delta<=1,

    ||A_epsilon||_(L2)<=C,
    ||partial A_epsilon||_(L1)<=C,
    ||B_epsilon||_(Linfinity)<=1,
    ||partial B_epsilon||_(L1)<=C,
    ||P_delta||_(Linfinity),||Q_delta||_(Linfinity)<=1,
    ||partial P_delta||_(L2)+||partial Q_delta||_(L2)<=C. (9)

Here norms of matrix symbols may be Frobenius norms with fixed
dimension constants. Explicitly,

    |A_epsilon|<=C r/(r^2+epsilon),
    |partial A_epsilon|<=C/(r^2+epsilon),
    |partial B_epsilon|<=C r/(r^2+epsilon)<=C/r,
    |partial P_delta|+|partial Q_delta|
                                  <=C r/(r^2+delta)<=C/r.

Integrating their indicated powers with volume element C r^2 dr
proves (9), including the origin; away from the origin the estimates
are bounded on the compact torus. All other convolution factors
are the actual fixed finite stencils, with bounded symbols and first
derivatives. None has been commuted through another component matrix.

Expand Cbar_l*,Fbar_k,H_s, or Fbar_l*,Cbar_k,H_s, into their finite
scalar-multiplier/stencil sums. Each term has three scalar multipliers:
one exterior curvature, one exterior path scalar and one displacement
scalar. Cycle it to the displacement multiplier M_u, on its scalar
vertex grid. In the first word there is exactly one A_epsilon and
one P_delta; in the second there is exactly one B_epsilon, one
P_delta and one Q_delta. All fixed stencils keep their original order,
including adjoints and rectangular selectors.

If all multiplier frequencies are zero, the closed convolution symbol
is the frozen word. With arbitrary multiplier frequencies it is an
ordered product of the same convolution symbols at translated torus
arguments. Let I(zeta_1,zeta_2) be its torus integral, where zeta_1,
zeta_2 are the two exterior multiplier frequencies and the displacement
frequency is -zeta_1-zeta_2. Fourier inversion of the sampled multiplier
at each insertion gives this conservation rule; each intervening symbol
argument is theta plus a partial sum of these frequencies. Every
coefficient of a zeta in those partial sums is 0 or +/-1.

For any such arguments, differentiation of this closed symbol integral
with respect to either frequency is uniformly bounded. In the first
word: a differentiated A has bounded L1 norm; a differentiated local
stencil is controlled by ||A||_(L1); and a differentiated P is paired
with A by

    integral |A_epsilon(theta+v)|
                    |partial P_delta(theta+w)| dtheta
       <=||A_epsilon||_(L2)||partial P_delta||_(L2)<=C. (10)

The two shifts v,w are independent: Cauchy--Schwarz is translation
invariant. All other factors are bounded. In the second word use
bounded B and the L1 bounds for its derivative and for projection
derivatives (L2 implies L1 on the normalized torus). These checks
cover differentiation of every factor in both original words. Integrate
along torus geodesics for the two exterior frequencies to obtain

    |I(zeta_1,zeta_2)-I(0,0)|
                         <=C(|zeta_1|_T+|zeta_2|_T),           (11)

uniformly in both masses. Smoothness at positive mass justifies each
differentiation. Inequalities (9)--(10), rather than a limiting
differentiation at mass zero, give the uniform constant.

For completeness, if f is a fixed smooth compact function and
f_a(y)=f(-4+a y), let hat(f_a)(zeta)=sum_y f_a(y)exp(-i y.zeta).
For the mode-dependent functions in (6), uniformly in level s,

    ||hat(f_a)||_(L1)<=C p(k),
    integral |zeta|_T |hat(f_a)(zeta)| d zeta<=C a p(k),
    ||hat(u_a)||_(Linfinity)<=C a^(-3).              (12)

The first two follow directly from Poisson summation: the continuous
Fourier transform has integrable (1+|eta|) weight by six integrations
by parts, and each aliased argument obeys
|zeta|_T<=a|eta|. The factor a^(-3) in the sampled transform cancels
the volume change d zeta=a^3 d eta. Translation of the physical
origin changes only unit phases. Fixed C^6 bounds of the cutoff
mode functions give the polynomial constants. The last bound in
(12) needs only sup|u_a|<=C and at most C a^(-3) nonzero samples.
Poisson summation and Fourier inversion here are their standard
smooth compact-function identities; the decay just proved makes
the uses absolutely convergent.

More explicitly, each expanded term can be written
Tr[M_u K_1 M_f K_2 M_h K_3], with K_j ordered convolution
products. Empty products are identities; their compatible component
dimensions may differ. Its integrated symbol is

    I(zeta_1,zeta_2)=integral_T tr[
       K_1(theta+zeta_1+zeta_2) K_2(theta+zeta_2) K_3(theta)] dtheta.

This gives the partial sums used above explicitly, while preserving
every factor within each K_j. The exact trace formula integrates

    hat(u_a)(-zeta_1-zeta_2) hat(f_a)(zeta_1)
                hat(h_a)(zeta_2) I(zeta_1,zeta_2)

against normalized measure on both frequency tori. It follows either
by inserting the two inverse Fourier formulas in the finite-rank
trace or by momentum conservation in its kernel sum. At positive
masses all convolution symbols are bounded and the three multipliers
have finite support, so these operations are justified by finite sums
and absolutely integrable Fourier factors. Replacing I by I(0,0)
gives exactly sum_y u_a(y)f_a(y)h_a(y) times the frozen symbol
integral, by Fourier inversion of the pointwise product.

Equations (11)--(12) bound the trace difference by

    C a^(-3)[(C a p(k))(C p(l))
                              +(C p(k))(C a p(l))]
                                      <=C a^(-2)p(k)p(l).      (13)

The argument is entrywise after the finite selector expansion, so
it proves the matrix rectangular trace estimate with its original
orders and signs. No component matrices were interchanged to use
scalar commutativity. Sum (13) over that fixed expansion, both words,
the original a^2 s weights and all finite-mesh heat pairs. If F_N
denotes the exactly frozen common-index trace, this proves

    |U_sm-F_N|<=C_i N^2.                              (14)

Since chi_1=1 on generator support, the two exterior cutoffs disappear
from F_N's local density: their product is multiplied by u_a. There
is no leftover cutoff contribution to its coefficient.

### 3. Match the full heat density and quadrature with the same coefficient

The frozen F_N has continuum h_k,b_k,q_k at x_(s,y), the actual u_a
there and c_(i;kl,a), with exactly the symbols in (1). L248(10)--(11)
supplies for the same two probe matrices, with c0=tau/16,

    |c_(i;kl,a)-c_(i;kl)|
       <=C_i a(1+|k|+|l|)^4 exp[-c0(|k|^2+|l|^2)],
    |c_(i;kl,a)|+|c_(i;kl)|
                      <=C_i exp[-c0(|k|^2+|l|^2)].    (15)

The torus integral of each frozen word and its first physical
derivatives is bounded by C p(k)p(l), uniformly in both masses:
use ||A_epsilon||_(L1)<=C for the first word and bounded B for
the second. Differentiation acts only on smooth h,b,q,u. All allowed
constant indices retain the same bounds. The entire omitted continuum
label sum is O_i(a), since an omitted pair has |k|+|l|>=N and its
polynomially weighted Gaussian tail is bounded by 1/N times a
convergent higher polynomially weighted Gaussian series. Thus (15),
the O(a^2) smooth displacement error and the union of the compact
displacement supports give total density error O_i(a).

For the normalization and counting, the frozen expression is exactly

    F_N=a^2 sum_(s=1)^(N-1) s sum_(y in Z^3)
                 sum_(retained k,l)c_(i;kl,a)
                     integral_T W_(kl;epsilon,delta)^a(x_(s,y),theta),
                                                               (16)

where the superscript a changes only u to u_a. Hence multiplication
by a^3 makes its weight a^4(as), with as=x_1+4. This is the ordinary
four-dimensional cell rule. Compact displacement support and the
uniform first physical derivative bounds above make its quadrature
error O_i(a). The complete density matching error is also O_i(a)
after this normalization. We conclude

    |F_N-a^(-3)K_i(epsilon,delta)|<=C_i N^2.          (17)

This includes the full triplet average and both shear polarizations
through their original heat matrices in (15). It neither replaces
an upper pinned potential by a smooth value nor changes an axial
endpoint weight. Combining (7),(8),(14),(17) proves (2).

### 4. Remove the frozen masses and identify exactly L123(2)

Set P_0=P and Q_0=Q almost everywhere. Uniformly on the normalized
three-dimensional torus, direct radial integration gives

    ||A_epsilon-A_0||_(L1)<=C epsilon log(e/epsilon),
    ||B_epsilon-B_0||_(L1)<=C epsilon,
    ||P_delta-P||_(L2)+||Q_delta-Q||_(L2)
                                             <=C delta^(3/4). (18)

Indeed |A_epsilon-A_0|<=C epsilon/[r(r^2+epsilon)], whose
radial integral is C epsilon integral r/(r^2+epsilon) dr.
For B the bound is C epsilon/(r^2+epsilon). The nonzero projection
difference eigenvalue is delta/(lambda+delta); its squared integral
is at most C delta^2 integral_0^C r^2/(r^2+delta)^2 dr
<=C delta^(3/2), by splitting at sqrt(delta). These estimates include
the singular origin as an integrable point, without a principal value.

First change epsilon to zero while holding delta fixed in (1): all
other factors are bounded. Next telescope each displayed projection
position to its exact massless counterpart. In the first word use
the uniform L2 norm of A_0 and (18); in the second use bounded B_0
and L1<=L2 for either projection error. The two second-word errors
are distinct and both are included. Full heat envelopes and the
bounded physical volume then prove (3), provided K_i(0,0)=K_(i,f).

To check that identity, at zero projection mass only, insert L123(1)

    beta_l*=Q C_l* P, alpha_k=P F_k D Q, g=H D.

In the first summand of L123(2), adjacent exact P and Q collapse,
and DQ=D. Rectangular trace cyclicity then gives

    tr_E[lambda^(-1)Q beta_l* alpha_k g]
                    =tr_F[D/lambda C_l* P F_k D H].

In the second summand, alpha_l*=Q D* F_l* P and beta_k=P C_k Q,
while QD*=D*. The same cyclicity gives

    tr_E[lambda^(-1)Q alpha_l* beta_k g]
                    =tr_F[D D*/lambda F_l* P C_k Q H]. (19)

These are precisely the two terms in (1), with no factor change.
In particular, Q remains between C_k and H in the second term.
Equations (19) hold away from zero frequency; the established absolute
bounds justify their integrated use. This proves the required identity
and (3).

At the schedule, (3) times a^(-3) is O_i(N^(5/2)log(eN)). Add
(2) and L274(5) once to obtain (4). L274's already combined response
comparison includes the complete f,f, axial level and endpoint errors;
they are not re-added. The complete other/other outside factor 3 is
absent throughout, as required for this component.

### 5. Scope and traps

The only confinement of true remote raw coefficients is the uniform
polynomial comparison (7); genuine inverse tails remain in its operator
error. The pasted coefficient difference is globally O(a), and only
the smooth sampled words enter the Fourier argument. Projection and
one-circulation resolvent derivatives are paired in the complete
closed trace, at possibly different arguments; neither a separate
first absolute kernel moment nor a uniformly bounded derivative of
the projection symbol is assumed. Every matrix selector remains in
its original order. P_delta,Q_delta are contractions, not projections.
All estimates are uniform finite inequalities before the mass schedule
is chosen; no qualitative fixed-mass limit is evaluated at varying mass.

This completes one RESEARCH / REPRODUCTION attempt under the unchanged
invocation-start EXPLORE assessment
`drafts/literature/2026-10-24-exterior-circulation-quantitative-remainder.md`.
The reproof here is the target-specific Fourier trace calculation:
L123's qualitative limits and the ready literature do not supply this
uniform coefficient-freezing rate or its raw-row application. The
standard general Fourier and spectral identities are used only with
the explicitly verified smoothness, support and integrability above.
No novelty beyond the sources checked is claimed. Section 6 supplies
the separate audit of this argument; the imported premises retain
their independent audit obligations.

### 6. Separate critical audit, 2026-10-24

**Verdict.** The audit accepts (2)--(4), relative to the stated imported
premises, for both actual probes. This is RESEARCH / REPRODUCTION,
actual task proof_audit under the invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-24-exterior-circulation-rate-critical-audit.md`.
It validates this quantitative specialization locally, with no claim
of progress beyond the sources checked. In particular it does not
independently audit L272--L274 or discharge any construction gap.

**Raw rows and support.** L111(1) puts the displacement multiplier on
the vertex grid, between its original T_r and C_r stencils; it is
exactly the smooth u_a sampled there. L028 section 1 supplies the
uniform compact support and C^m estimates. Thus the two cutoff
neighborhoods can contain every generator endpoint with fixed clearance.
The L274 polynomial path length 3m+r_* is o(N) at the stated degree,
so every coefficient occurrence in each entire closed polynomial path
lies where pasted and raw arrays agree. Equality is for the whole
trace, including its possible input endpoints. True inverse tails
remain in the uniform operator errors. The same sup envelopes apply
to raw and pasted coefficients, so (7) follows from the imported
polynomial errors and rank count, without differentiating a raw array.

For (5), L123(10) removes the prefix from the transverse curl exactly.
L222(3), followed by the integral finite-difference formula and the
bounded component-center shifts, gives its O(a p(k)) value error.
L248(4)--(8) compares each unaveraged link before the four signed
traversals form b,q; it retains the component-1 zero axial index.
These uses are confined to supp(chi_0) and levels s<N. Since chi_1=1
on supp(chi_0), (6) then has a globally O(a p(k)) pasted-minus-smooth
difference, including the cutoff transition. The exact upper pinned
forest value is never replaced. Finite stencil norms, the finite-rank
H_s trace bound and ||A_epsilon||<=C epsilon^(-1/2) give
C_i a N^3 epsilon^(-1/2)=O_i(N^(9/4)); the B_epsilon word costs only
O_i(N^2). The full original a^2 sum_s s is bounded. No inverse output
has been declared compact for this estimate.

**Closed trace and independent shifts.** Expanding the finite selectors
leaves exactly two exterior scalar multipliers and the displacement
multiplier, on compatible integer-index grids. For
Tr(M_u K_1 M_f K_2 M_h K_3), write its kernels at x,y,z. Inserting
f_y=integral hat(f)(zeta_1) exp(i y.zeta_1) and the analogous h_z
shows that the three convolution momenta are
(theta+zeta_1+zeta_2, theta+zeta_2, theta), while the u frequency is
-zeta_1-zeta_2. This verifies both signs and the two free frequency
variables in the displayed exact trace formula. Finite multiplier
supports and bounded positive-mass symbols justify the kernel/Fourier
calculation. Adjoint symbols and rectangular selectors remain in each
K_j's original order. At zero exterior frequencies the resulting
coefficient product is exactly the common-index frozen density.

Here are explicit integrability checks behind (9), with a fixed upper
radial cutoff R and constants absorbing finite matrix dimensions:

    ||A_epsilon||_2^2 <= C integral_0^R r^4/(r^2+epsilon)^2 dr <= C,
    ||partial A_epsilon||_1
                       <= C integral_0^R r^2/(r^2+epsilon) dr <= C,
    ||partial P_delta||_2^2+||partial Q_delta||_2^2
                       <= C integral_0^R r^4/(r^2+delta)^2 dr <= C.

The derivative of B_epsilon is bounded by C r/(r^2+epsilon),
so its L1 norm is also uniform. A differentiated fixed stencil costs
only its bounded derivative and ||A_epsilon||_1 in the first word.
A differentiated P_delta in that word pairs with A_epsilon by
translation-invariant L2 Cauchy--Schwarz, irrespective of their two
shifts. Differentiating A itself uses its L1 derivative norm and a
bounded projection. In the second word B is bounded and differentiation
of either P_delta or Q_delta uses its L1 derivative norm; differentiation
of B uses the bound just given. These exhaust all placements and
establish (11) uniformly for arbitrary independent shifts. No mass-zero
differentiation, projection derivative supremum or separate absolute
first kernel moment is used.

For the general Fourier identities, import T. Tao, *245C, Notes 2:
The Fourier transform*, 6 April 2009, section 3, inversion (11),
Exercises 38, 50, 53--54
(https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/),
and N. D. Elkies, *Theta functions and weighted theta functions of
Euclidean lattices, with some applications*, March 2009 draft,
section 2, Theorem 2 (26), proof (28)--(32), printed pp. 9--11
(https://people.math.harvard.edu/~elkies/aws09.pdf).
Only their smooth Schwartz inversion/scaling and Poisson identities
are imported, not a trace theorem. The cutoff coefficient functions
are smooth compact functions with uniform level-wise C^6 bounds
polynomial in the mode labels. They therefore meet these hypotheses.

In angular convention, put hat(f_c)(eta)=integral f(x)exp(-i x.eta)dx.
For b=(-4,-4,-4) and f_a(y)=f(b+a y), Poisson gives

    hat(f_a)(zeta)=a^(-3) sum_(m in Z^3)
      exp[i b.(zeta+2pi m)/a] hat(f_c)((zeta+2pi m)/a).

This is the required scaling determinant and origin phase. Six
integrations by parts give decay C p(k)(1+|eta|)^(-6), whose first
absolute frequency moment is integrable in dimension three. In each
alias cell |zeta|_T<=|zeta+2pi m|=a|eta|. Changing variables cancels
a^(-3) and proves both L1 bounds in (12), with normalized angular
measures. The u transform bound follows from its sample count.
Tao's 2pi convention is converted by eta=2pi xi; Elkies's opposite
sign is converted by reflection. These standard identities need no
reproof. Applying the two frequency moments to (11) gives precisely
a^(-3)O(a)=O(N^2), with the original matrix factors untouched.

**Density, coefficient identity and error budget.** L248(10)--(11)
compares exactly the two full heat matrices, including the four-square
triplet average and both shear polarizations. L222 supplies the
all-retained-label modal bounds; the full Gaussian envelope dominates
every fixed polynomial introduced above. Omitted labels have size at
least N and hence contribute O(a) to the normalized density. Its first
physical derivatives are uniformly bounded after this heat summation,
since only the smooth coefficients are differentiated. The union of
displacement supports is compact, so all four-dimensional endpoint
cells are included in the O(a) cell-rule error. The identity

    a^3 (a^2 s)=a^4(as),  as=x_1+4,

verifies (16)--(17) with no extra box-length, color or orientation
factor. At generator support both exterior cutoffs equal one.

The radial calculations in (18) give respectively
O(epsilon log(e/epsilon)), O(epsilon) and O(delta^(3/4)). They are
integrable estimates over the complete torus, including its origin.
For the first frozen word telescope covariance mass before projection
mass and pair A_0 with the projection error in L2. For the second,
telescope its two distinct projection slots with bounded B_0. Thus
neither regularized projection is used as an idempotent.

Independently substituting beta_l*=Q C_l* P,
alpha_k=P F_k D Q and g=H D in L123(2), the first product reduces to
lambda^(-1)Q C_l* P F_k D Q H D. Cycle its last D to the front and
use DQ=D at both adjacent occurrences to obtain the first word in
(19). The second reduces to
lambda^(-1)Q D* F_l* P C_k Q H D; the same cycle and QD*=D*
give the second word in (19), with the Q between C_k and H retained.
The established absolute integrability permits these identities away
from the single zero-frequency point to identify the full coefficient.
Both original mixed orientations are present and the outside factor 3
of the later other/other group remains unapplied.

At the schedule the new allowances are N^(-10), N^(9/4), N^2 and
N^2 for localization, pasted matching, smooth freezing and full
heat/quadrature respectively. This verifies (2). Frozen mass removal
costs at most C_i N^(5/2)log(eN), verifying (3)'s use in (4).
Finally add the combined imported L274(5) allowance once. Its f,f,
level and endpoint terms are already included, and are not separately
added to either mixed word. Every allowance fits (4), with a common
sufficiently-large-mesh threshold for the two probes. This acceptance
is conditional on those imported complete bounds; it is not an audit
of their proofs, a full L011 rate, or an interacting conclusion.

## Mathlib

Full matching ordered exterior-circulation quantitative remainder:
**not checked**. Supporting Fourier inversion, Poisson summation,
Plancherel/Holder inequalities, finite-rank trace bounds, matrix spectral
calculus and cell quadrature: **not checked**. Unknown availability is
not absence. This informal proof is not a formal verification or an
interacting Yang--Mills construction.
