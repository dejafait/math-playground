# L524 — Endpoint-fixed transport stationarity and its sign test

## Hypotheses

Retain L516's conditional complete form on I=(-a,a), 0<a<A<infinity,
and L522's fixed-nullvector hypotheses. In particular ell=2a>log(2),
v is real, ||v||_2=1, A_a v=0, its left renewal trace is nonzero, and
log(2)!=ell-d_n for each retained prime power of positive weight.
Also assume b>=0 on this one fixed interval's form domain. No
positivity on larger intervals or sign of v is assumed. Write

    c=log(2pi), d_n=log(n), w_n=Lambda(n)/sqrt(n),
    n(s)=exp(-|s|)/(2|s|), Psi(xi)=(1/2)log(1+xi^2),
    k(s)=2cosh(s/2), kappa(t)=exp(-t/2)/(1-exp(-2t)), t>0,
    rho(t)=kappa(t)-n(t), t>0,
    mu_A=nu_rho+sum_(d_n<=2A)w_n(delta_(d_n)+delta_(-d_n))
                            -k(s)1_(|s|<=2A)ds,
    b(f,f)=q_G(f,f)-c||f||_2^2-<f,mu_A*f>.

The even density of nu_rho is rho. All functions are zero extended,
the Fourier transform is integral f(x)exp(-i xi x)dx, and q_G has
multiplier Psi and the killed smooth-core domain Q_I of L515.
Thus A_a=G_I-cI-R_I K_(mu_A)E_I with Dom(A_a)=Dom(G_I).
Both prime shifts, every equality atom, the signed pole, and the
source qualification on the complete-Weil identification remain.
L515 and L521 supply the continuous compact BV representative of v.
Existence, first-zero realization and actual-Xi identification are
not conclusions of this lemma.

Fix one field X as follows. Put b_0=a/2, b_1=3a/4. Let H(t) be zero
for t<=0, one for t>=1, and, for 0<t<1,

    H(t)=exp(-1/t)/[exp(-1/t)+exp(-1/(1-t))].

Set theta(x)=1-H((x^2-b_0^2)/(b_1^2-b_0^2)) and X(x)=x theta(x).
Then X is smooth, equals x on [-b_0,b_0], and vanishes for
|x|>=b_1. All collars in this statement are fixed. For real t
sufficiently close to zero define

    F_t(x)=x+t X(x),       W_t f(x)=sqrt(1+t X'(x)) f(F_t(x)).

This is a family of diffeomorphisms and unitary pullbacks; a group
law is not assumed. The previously saved EXPLORE gate is
`drafts/literature/2026-10-30-weil-endpoint-fixed-transport-coverage.md`.
The direct logarithmic/BV calculation is needed because the inspected
fractional/conformal results in that assessment do not cover it.
The separate conceptual audit below passes this local derivation and
its limited negative sign test under the unchanged hypotheses. The
construction's POTENTIALLY_NEW label does not certify novelty.

## Conclusion

The maps W_t preserve the actual Q_I, uniformly bounded there for
small |t|. For any real continuous compact BV f in Q_I, set

    j(s)=kappa(|s|)-k(s), s!=0,
    K_X(x,y)=(X'(x)+X'(y))j(x-y)/2
                           +(X(x)-X(y))j'(x-y), x!=y,
    R_X(f)=integral_I X'(x)f(x)^2 dx
                         +integral_(I^2) K_X(x,y)f(x)f(y)dxdy,
    Z_X(d;f)=integral_R X(x)[f(x+d)+f(x-d)] Df(dx)
              +(1/2)integral_R X'(x)f(x)[f(x+d)+f(x-d)]dx,
    S_X(f)=-2 sum_(d_n<=2A)w_n Z_X(d_n;f).                 (1)

Here j' is the ordinary derivative off zero. K_X is bounded on
I^2 off the diagonal and can be assigned any value on the diagonal.
All displayed integrals converge absolutely. The two-sided derivative
exists and equals

    d/dt b(W_t f,W_t f) at t=0 = R_X(f)+S_X(f).            (2)

Every prime with d_n>=ell has zero correlation for all sufficiently
small t, including d_n=ell and d_n=2A. No atom is removed before this
support check. For the stipulated nullvector, fixed-interval
nonnegativity gives only the stationarity identity

    R_X(v)+S_X(v)=0.                                     (3)

The continuous contribution R_X has both signs on normalized real
smooth tests with no prime overlaps. More precisely, there are such
sequences f_N^+, f_N^- with

    lim R_X(f_N^+)>0,          lim R_X(f_N^-)<0,
    Z_X(d_n;f_N^+)=Z_X(d_n;f_N^-)=0 for every retained n.  (4)

These are not nullvectors. Thus (4) rules out a universal coefficient
sign or form-monotonicity argument for this field, not an additional
inequality specific to the arithmetic null equation. Equation (3)
does not give S(v)<=P(v)-H(v), and S_X is not S: its variable shift
coefficients differ from dilation in the transition regions. No
independent signed comparison at v was obtained in this attempt.
This fails the approved continuation test; no shrinking-collar limit
is taken. L516/L522's flux gap, family saving, realization and Xi
transfer remain open. This is not a counterexample to their criterion
or to RH.

## Proof

### Finite changes of variables on the actual part domain

Choose t_0>0 so that |t| ||X'||_infinity<1/2 for |t|<=t_0.
F_t is increasing, is the identity outside a compact subset of I,
and maps I onto itself. It is a smooth global diffeomorphism. The
change of variables z=F_t(x) proves ||W_t f||_2=||f||_2.
Put R_t=F_t^(-1) and J_t=R_t'. The reference Levy form gives

    q_G(W_t f,W_t f)
       =(1/2) integral integral
          [sqrt(J_t(y))f(x)-sqrt(J_t(x))f(y)]^2
                                      n(R_t(x)-R_t(y))dxdy. (5)

First use this on smooth compact tests. The inverse maps have
uniformly bounded positive derivatives. Moreover, for s=x-y,
their displacement difference from s is O(|t|min(|s|,1)). This
follows from R_t(z)-z=-t X(R_t(z)), using both the uniform
Lipschitz constant and boundedness of X. Consequently

    n(R_t(x)-R_t(y))<=C n(x-y),
    |sqrt(J_t(x))-sqrt(J_t(y))|
                              <=C|t|min(|x-y|,1).        (6)

For the first bound, the ratio of the distances is bounded above
and below, and their absolute difference is O(|t|); these control
the reciprocal and exponential factors of n separately. The second
bound follows from J_t(z)=1/[1+t X'(R_t(z))] and bounded X''.
Expanding the square in (5) around sqrt(J_t(y))(f(x)-f(y))
and applying (6) gives

    q_G(W_t f,W_t f)<=C q_G(f,f)+C t^2 ||f||_2^2,          (7)

because integral min(s^2,1)n(s)ds is finite. The constants depend
on X and the fixed t_0 only. W_t maps C_c^infinity(I) into itself.
Applying (7) to differences of smooth-core approximations proves
that W_t extends boundedly to Q_I. Its L2 realization is the stated
pullback by unitarity, so this is membership in the actual completed
part domain, not merely finite formal energy. The bounded signed
convolution perturbation does not change that domain.

### Logarithmic energy derivative, including its diagonal term

The change of variables in (5) also justifies differentiation for
every f in Q_I. Here are the necessary dominating bounds. Uniformly
for |t|<=t_0, the derivative in t of R_t(x)-R_t(y) is bounded by
C min(|x-y|,1). Since |n'(s)|/n(s)=1+1/|s|, the derivative of
the kernel in (5) is bounded by C n(x-y). The amplitude in square
brackets and its derivative are each bounded by
C[|f(x)-f(y)|+min(|x-y|,1)|f(y)|]. To see the derivative bound,
differentiate sqrt(J_t(y))(f(x)-f(y)) plus
[sqrt(J_t(y))-sqrt(J_t(x))]f(y); the derivative of the bracket
has the same spatial Lipschitz bound without the factor |t|.
Thus the absolute derivative of the integrand is bounded by

    C n(x-y)[|f(x)-f(y)|^2
                     +min(|x-y|^2,1)(|f(x)|^2+|f(y)|^2)]. (8)

This is integrable by Q_I membership and the preceding kernel
integral. Dominated differentiation applies on both sides of t=0.
At zero, R_t has derivative -X and J_t has derivative -X'. It gives

    Q_X(f):=d/dt q_G(W_t f,W_t f) at zero
      =(1/2) integral integral (f(x)-f(y))
                          [X'(x)f(y)-X'(y)f(x)]n(x-y)
        -(1/2) integral integral (f(x)-f(y))^2
                                  (X(x)-X(y))n'(x-y).    (9)

For a useful simplification put

    D_X(x,y)=-(X'(x)+X'(y))n(x-y)/2
                              -(X(x)-X(y))n'(x-y),
    G X'(x)=integral (X'(x)-X'(y))n(x-y)dy.

The latter integral is absolutely convergent and bounded: near
zero use Lipschitz X', and at infinity use the integrable tail of n.
Near the diagonal the trapezoidal Taylor estimate

    (X(x)-X(y))/(x-y)-(X'(x)+X'(y))/2=O(|x-y|^2)

and n'(s)=-sign(s)(1+1/|s|)n(s) show D_X=O(1).
For |x-y|>=1 it is bounded by C exp(-|x-y|)/|x-y|.
These bounds are uniform in x,y. In particular its absolute kernel
has uniformly bounded row and column integrals.

Algebra in (9), justified first by the integrable mixed difference
terms in (8), gives

    Q_X(f)=(1/2) integral integral (f(x)-f(y))^2 D_X(x,y)
                          +(1/2) integral f(x)^2 G X'(x)dx. (10)

For each x, combining these two finite kernels gives

    integral D_X(x,y)dy+(1/2)G X'(x)=X'(x).               (11)

Indeed, away from y=x their combined integrand is

    -X'(y)n(x-y)-(X(x)-X(y))n'(x-y)
           =d/dy [(X(x)-X(y))n(x-y)].

Integrate with |x-y|>epsilon. The terms at infinity vanish; at
y=x-epsilon and y=x+epsilon the bracket tends respectively to
X'(x)/2 and -X'(x)/2. Their difference is X'(x).
The bounded combined integrand has an integrable limit, proving
(11). Discarding these two inner boundary terms would lose the
load-bearing multiplication term. Since D_X is symmetric, expansion
of (10) now yields the exact bounded quadratic form

    Q_X(f)=integral X'(x)f(x)^2dx
                           -integral integral D_X(x,y)f(x)f(y)dxdy. (12)

This derivation does not take an L2 derivative of W_t f or posit
H1 regularity of the nullvector.

### The continuous signed perturbation and scalar normalization

On the difference interval |s|<=ell<2A, put h(s)=rho(|s|)-k(s).
This is exactly the continuous density in mu_A on that interval.
It is bounded and locally Lipschitz there, with bounded one-sided
derivatives at zero. For example, direct Taylor expansion in the
displayed kernels gives kappa(t)=1/(2t)+O(1),
kappa'(t)=-1/(2t^2)+O(1), while rho has finite value and finite
one-sided derivative at zero. The inverse transforms in (5) keep
both points in I, so the pole cutoff at 2A is never crossed.
There is no missing derivative of its cutoff indicator.

The transformed pairing <W_t f,h*W_t f> has kernel
sqrt(J_t(x)J_t(y)) h(R_t(x)-R_t(y)). Its derivative at zero is
[-(X'(x)+X'(y))h(s)/2-(X(x)-X(y))h'(s)] f(x)f(y).
It is dominated by C|f(x)f(y)| on I^2; f is L1 there. Therefore
the minus sign in b contributes the opposite of this expression.
Combining it with (12) gives R_X in (1), since n+h=kappa-k.
The scalar -c||W_t f||_2^2 is exactly constant and contributes zero.
In particular c was not replaced, and rho and the negative density
of the pole were retained before taking the derivative.

The same Taylor estimate used for D_X proves that K_X is bounded
at its diagonal: the singular terms combine to

    [(X'(x)+X'(y))/2-(X(x)-X(y))/(x-y)]/(2|x-y|),

which is O(|x-y|); the other terms are bounded. Away from the
diagonal the fixed compact difference interval gives a bound as
well. This also establishes absolute convergence in (1).

### Variable-flow BV quotients and the two atomic shifts

The BV input is L521; the constant-shift derivative-measure theorem
used in L522 is Bruno Galerne, *Random fields of bounded variation
and computation of their variation intensity*, Adv. Appl. Probab.
48 (2016), Section 2, Lemma 1 and Theorem 1, pp.951–953
([primary PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/83627D38EAB49283AE917366027E8BE7/S0001867816000604a.pdf/random_fields_of_bounded_variation_and_computation_of_their_variation_intensity.pdf)).
That theorem is not cited as a variable-flow result. The required
extension is justified here, with Df the signed distributional
derivative and V=|Df|(R).

For smooth g, the fundamental theorem of calculus and the change
of variables x->x+s t X(x), 0<=s<=1, give

    ||g o F_t-g||_1/|t|
                   <= ||X||_infinity V_g/(1-|t| ||X'||_infinity), (13)

where V_g=||g'||_1. For a BV f, mollify with a nonnegative smooth
approximate identity. Its derivative is the convolution of Df
with that kernel, so the mollified variations are at most V.
The mollifications converge in L1; composition with the fixed F_t
is bounded on L1 by its inverse Jacobian bound. Passing to the
limit in (13) proves it for f, for each nonzero t. Thus the signed
measures [f(F_t(x))-f(x)]dx/t have uniformly bounded total variation.

For a smooth compact test phi, changing variables gives

    integral phi(x)[f(F_t(x))-f(x)]dx/t
       =integral f(y)[phi(R_t(y))J_t(y)-phi(y)]dy/t
       ->-integral f(y)[X(y)phi'(y)+X'(y)phi(y)]dy
        =integral X(y)phi(y) Df(dy).                       (14)

The Taylor quotient is uniformly bounded on a fixed compact set.
The total variation bound extends this convergence from smooth
tests to all C_0 tests by uniform approximation. Multiplication by
sqrt(1+t X'), followed by its uniform Taylor expansion, proves

    [W_t f-f]dx/t -> M_X:=X Df+(1/2)X'f dx                (15)

weak-* against C_0, with uniformly bounded measure norms.
Also W_t f->f uniformly, by uniform continuity of compact f and
uniform convergence of both F_t and the amplitude to the identity.
These are two-sided statements; no signed measure is replaced by
an ordinary derivative density.

For a fixed signed displacement d, expand the product defining
C_d(t)=integral W_t f(x) W_t f(x+d)dx by changing its first
factor and then its second factor. The first quotient pairs the
measure in (15) with W_t f(.+d); the second pairs it with f(.-d).
The moving tests converge uniformly and are continuous with a
common compact support. The uniform measure norm in (15) therefore
justifies both limits. Their sum is precisely

    C_d'(0)=integral [f(x+d)+f(x-d)] M_X(dx)=Z_X(d;f).     (16)

For real f, C_d(t)=C_(-d)(t); the two atoms thus give -2w_n Z_X.
There are finitely many retained n, so finite summation proves
(2). In particular this is not an unproved interchange over primes.
Since W_t f is supported in [-a,a] for all these t, C_d(t)=0
whenever |d|>=ell, including the support equality. Formula (16)
agrees: Df is supported in [-a,a], and all shifted values of the
continuous f vanish on that closed interval at those displacements.
This includes the cutoff equality 2A. Unlike an outward dilation,
the present map does not move either support endpoint.

For comparison with L522's observable, integration by parts for
continuous BV functions rewrites (16) as

    Z_X(d;f)=integral [X(y)-X(y+d)]f(y+d) Df(dy)
         +(1/2)integral [X'(y)-X'(y+d)]f(y)f(y+d)dy.       (17)

The product rule needed here follows by mollifying the two
continuous BV functions: uniform convergence of the functions,
bounded derivative-measure norms, and their weak-* convergence
pass the smooth product rule to continuous tests. Integrate the
derivative of X(y+d)f(y)f(y+d); its compact support makes its
total integral zero. This gives exactly (17).

For the formal dilation coefficients X(y)=y, (17) becomes
-d integral f(y+d)Df(dy). Integration of D[f(y)f(y+d)]
also gives integral f(y-d)Df=-integral f(y+d)Df. Thus S_X
becomes exactly L522's S, with its stated sign and both shifts.
For our admissible X, the differences of X and X' in (17) vary
in the transition regions. They cannot be replaced by -d and zero.
This check does not make the outward dilation an admissible test.

### Stationarity and the discriminating sign calculation

At the actual nullvector, W_t v belongs to Q_I for both signs of t.
The assumed b>=0 gives b(W_t v,W_t v)>=0 and b(v,v)=0.
The two-sided derivative (2) at this minimum is zero, proving (3).
No assertion of form-norm differentiability or an admissible
generator test was required.

For the fixed field chosen above, X'=1 on the bulk. It is strictly
negative on some nonempty open interval in (b_0,b_1): otherwise
X could not decrease from X(b_0)=b_0>0 to X(b_1)=0. By continuity
choose intervals J_+,J_- compactly inside the positive and negative
derivative regions, respectively, each of length less than log(2)/2.
On J_- one may arrange X'<=-eta for some eta>0. Choose real smooth
bumps chi_+,chi_- supported in these intervals with integral chi^2=1.
For either bump put

    g_N(x)=sqrt(2)chi(x)cos(Nx),  f_N=g_N/||g_N||_2.

The Riemann–Lebesgue lemma for L1(R) gives ||g_N||_2->1 and

    integral X'(x)f_N(x)^2dx -> integral X'(x)chi(x)^2dx.  (18)

The function K_X(x,y)chi(x)chi(y), extended by zero, is in
L1(R^2), since K_X is bounded on I^2. Expanding cos(Nx)cos(Ny)
into the two diagonal frequencies and applying the
Riemann–Lebesgue lemma for L1(R^2) proves

    integral integral K_X(x,y)f_N(x)f_N(y)dxdy ->0.       (19)

Thus the limits of R_X are 1 on J_+ and at most -eta on J_-.
Every nonzero prime displacement is at least log(2), while each
bump has shorter support. For all sufficiently small |t|,
F_t^(-1)(J_+) and F_t^(-1)(J_-) still each have length less than
log(2). Thus every individual prime correlation of each W_t f_N
is identically zero near t=0. This proves the atomic assertion in
(4), retaining all weights and the cutoff. The scalar contributes
zero as before, so these are also opposite signs of the complete
energy derivative on these tests. No change to c or mu_A was used.

This is a coefficient obstruction, not a test of the unknown v:
f_N need not solve any eigen-equation. It shows why positivity of
the logarithmic reference energy, retention of the complete kernel,
and fixation of endpoints cannot by themselves sign R_X for all
test vectors. The actual null equation supplies (3); the prime
term still contains variable, signed BV pairings in (17). No
additional nullvector-specific comparison was established that
converts it to S<=P-H. The approved test explicitly rejects an
identity alone. Accordingly this implementation is parked before
any shrinking-collar argument, without assuming zero trace or
claiming that other arithmetic mechanisms are impossible.

### Independent conceptual audit, 2026-10-30

The prior EXPLORE assessment
`drafts/literature/2026-10-30-l524-transport-conceptual-audit-coverage.md`
covers this audit of (5)-(19). The existing conclusions pass, with
no stronger sign statement and no new mathematical input. This is
verification of the local derivation, not a source-manuscript audit
or an advance beyond the inspected literature. In particular the
complete-Weil identification, nullvector existence, and the imported
domain/renewal results retain their qualifications.

**Actual domain and both parameter directions.** L515's domain is
the completion of the killed smooth core. The translation from its
interval coordinates to I is the unitary form transport checked in
L522; it preserves the measure, scalar and continuous BV representative.
For |t| ||X'||_infinity<1/2, 1/2<F_t'<3/2 and R_t is uniformly
bi-Lipschitz. The exact two-variable substitution in the Levy energy
gives (5), including both square-root Jacobians. If s=x-y, then

    |(R_t(x)-R_t(y))-s|<=C|t|min(|s|,1),
    |R_t(x)-R_t(y)|/|s| is bounded above and below.

The bounded displacement controls the exponential factor of n even
at arbitrarily large separation; bi-Lipschitzness controls 1/|s|.
Thus the first estimate in (6) is global, not a diagonal-only bound.
The second follows by differentiating J_t in space. Decomposing the
amplitude as sqrt(J_t(y))(f(x)-f(y)) plus the Jacobian difference
times f(y) proves (7), since integral min(s^2,1)n(s)ds is finite.
For core approximants f_j, (7) applies to f_j-f_k, while unitarity
identifies the L2 limit with W_t f. Completeness therefore proves
membership in Q_I. No equality between a formal finite-energy class
and that completion is assumed. The inverse pullback obeys the same
bounds and maps the core to itself as well.

For differentiation, the exact formula

    partial_t R_t(z)=-X(R_t(z))/(1+tX'(R_t(z)))

has uniformly bounded value and spatial derivative. Its two-point
difference is consequently O(min(|s|,1)). Both partial_t sqrt(J_t)
and its spatial derivative are uniformly bounded, using bounded
derivatives of the fixed smooth X. With
|n'(r)|=(1+1/|r|)n(r), these statements give exactly (8), whose
integral is bounded by C(q_G(f,f)+||f||_2^2). The bound applies for
both signs of t. Dominated differentiation proves (9) for every
Q_I vector without an L2 derivative of W_t f.

**Algebra and inner boundary.** Writing p=X'(x), q=X'(y), A=f(x)
and B=f(y), the first integrand in (9) uses the identity

    (A-B)(pB-qA)=-(p+q)(A-B)^2/2+(p-q)(A^2-B^2)/2.

The mixed difference terms are integrable by (8). Symmetry converts
the last term into the G X' term of (10). The trapezoidal estimate
there makes D_X bounded near zero; its stated exponential bound
gives finite row and column integrals on the whole line. Thus the
subsequent expansion of (10) is also absolutely justified. In (11),
integrating d_y[(X(x)-X(y))n(x-y)] outside |x-y|<=epsilon yields
the value at x-epsilon minus the value at x+epsilon. Their limits
are respectively +X'(x)/2 and -X'(x)/2, since
epsilon n(epsilon)->1/2. The boundary at infinity vanishes.
The result is +X'(x), verifying both the factor and sign in (12).

**Complete continuous term.** The expansions used in the original
proof have the more explicit forms, as r->0+,

    kappa(r)=1/(2r)+1/4-r/48+O(r^2),
    n(r)=1/(2r)-1/2+r/4+O(r^2),
    rho(r)=3/4-13r/48+O(r^2).

These follow from kappa(r)=exp(r/2)/(2sinh(r)); the corresponding
one-sided derivatives are bounded after subtracting n. The even
extension of rho is Lipschitz, with no need for a two-sided derivative
at zero. Hence h=rho-k has the boundedness and one-sided derivative
bounds used above. For distinct x,y, the increasing inverse map
preserves the sign of their difference, and the diagonal has zero
Lebesgue measure. The transformed signed pairing therefore has the
stated derivative dominated by C|f(x)f(y)| on I^2. Since R_t maps
I onto I and ell<2A, the negative pole density never crosses its
cutoff. Combining it with the reference term indeed uses n+h=j;
it does not omit nu_rho or change the pole sign. The scalar term is
exactly invariant by unitarity. The displayed singular cancellation
in K_X is O(|x-y|), with bounded remaining terms, so K_X belongs to
L-infinity(I^2) up to its arbitrary diagonal values.

**BV measures, products and atoms.** For smooth mollifications of
f, the change of variables x->x+stX(x) bounds the L1 quotient by
||X||_infinity |Df|(R)/(1-|t| ||X'||_infinity). Composition is
bounded on L1 for each fixed t, so L1 approximation proves (13)
for f. The inverse-map Taylor formula against a smooth compact test
gives -integral f(X phi)'=integral X phi Df for either sign of t.
Uniform measure norms extend this to C_0 tests. Inserting the
half-density contributes precisely +(1/2)X'f dx in (15); multiplying
the first quotient by an amplitude tending uniformly to one does
not change its weak-* limit.

Uniform continuity of the compact f gives W_t f->f uniformly.
The exact product difference for C_d has first term (W_t f-f)
times W_t f(.+d), and second term f times (W_t f-f)(.+d).
The latter becomes a pairing against f(.-d) after translation.
Their common compact supports and the uniform measure bound justify
the moving tests and give (16), with a sum of the two shifted values.
The paired atoms contribute -2w_n Z_X, since C_d=C_(-d) for real f.
Both C_d(t) and the right side of (16) vanish for d>=ell: the first
uses fixed supports, the second uses Df supported in [-a,a] and the
zero endpoint values of the continuous f. This explicitly includes
d=ell and d=2A>ell before any term is dropped. The retained sum is
finite for fixed A.

For (17), mollifying continuous compact BV factors gives uniform
function convergence and bounded, weak-* convergent derivative
measures. These suffice to pass the smooth product rule; no product
of distributions is taken. The integral of
D[X(y+d)f(y)f(y+d)] is zero. Moving its last term to the other side
produces X(y)-X(y+d) and (X'(y)-X'(y+d))/2 with exactly the signs
in (17). Formally substituting X(y)=y gives
Z_X=-d integral f(y+d)Df(dy). The same product rule gives
integral f(y-d)Df=-integral f(y+d)Df, so -2w_n Z_X agrees with
L522's w_n d times its difference of shifted tests. This is a
normalization check, not admissibility of a global dilation.

**Stationarity and the precise negative result.** The established
actual-domain paths have b(W_t v,W_t v)>=0 and b(v,v)=0, so their
two-sided derivative is zero. This proves (3) without an H1
generator or a larger-interval hypothesis. For the packet test,
X'=1 on the bulk and X'<=-eta on a smaller transition interval.
The Riemann--Lebesgue lemma applied to chi^2 and X'chi^2 proves
normalization and (18). Applied in R^2 to the integrable function
K_X(x,y)chi(x)chi(y), at frequencies (N,N) and (N,-N) and their
negatives, it proves (19). Thus the limiting signs are +1 and a
number at most -eta. Each support interval has length less than
log(2)/2; the inverse Lipschitz bound 2 keeps its transported length
strictly below log(2), uniformly in N. Every retained prime overlap
is therefore identically zero near t=0. The complete derivative
has both signs on these smooth normalized tests, but none is
asserted to be a nullvector.

The audit certifies only this obstruction to a universal sign for
the chosen field and the conditional stationarity identity. It
does not compare S_X(v) with L522's S(v), prove S<=P-H, justify
shrinking collars, force trace vanishing or give an O(lambda)
family estimate. No first-zero or Xi realization follows. The
existing coefficient-sign route remains parked; a different
nullvector-specific estimate would require its own assessed target.

## Mathlib

Full matching coverage of this variable-transport logarithmic form
and signed atomic BV derivative has not been checked. No absence
claim or Lean verification is made. The named standard input in
(18)–(19) is the Riemann–Lebesgue lemma; constant-shift BV coverage
is cited above, and the variable-flow difference is proved explicitly.
L515/L516/L521/L522 retain their qualifications and source audits.
The separate audit above passes the local calculation under its
stated hypotheses. It does not audit the imported manuscripts or
assert a new discovery beyond the sources checked.
