# C750f: C750c's complete fixed-window form is positive by paper162

## Hypotheses

Set T=4log(3), I=(0,T), a=T/2=2log(3), and b=9/4. Functions
are complex valued, Lebesgue measure is unweighted, and extensions
outside the indicated interval are zero. Put

    D_I={f in L2(I): integral_R log(2+|t|)|F_f(t)|^2 dt<infinity},
    F_f(t)=integral_I f(x)exp(-itx)dx,
    M_sigma(f)=integral_I exp(sigma*x/2)f(x)dx,
    R_f(u)=integral_R f(x+u)conj(f(x))dx,
    m(t)=Re psi(1/4+it/2)-log(pi).

Use precisely the complete form in C750c(1), agreeing on smooth
tests with L744(6):

    E(f)=integral_R m(t)|F_f(t)|^2 dt/(2pi)
         +2Re(M_+(f)conj(M_-(f)))
         -2 sum_(2<=n<81) Lambda(n)/sqrt(n) Re R_f(log n).       (1)

Let H, V=U_6 and W=H intersect V-perp have C750c(2)'s exact
meaning. In particular H is the common kernel of both complex
moments; the orthogonal complement uses the original L2 metric.

The external sign input is bramble_trace, *Source-Gram control and
complete Weil positivity at radius 9/4*, rStation paper162, v1,
15 November 2026, [primary text](https://rstation.ai/problems/riemann_hypothesis/papers/162),
Section1's unnumbered Theorem, Section2 equation(2) and the closed-form
discussion following(7), and Section6 equations(31)-(32). At radius b
it asserts a strictly positive spectral infimum for the Friedrichs
realization of its complete complex form. That form is the closure
of its equation(2) on smooth compact tests in (-b,b).

This is an import of that computer-assisted theorem, not a local
verification of its certificate. Assessment1131 was saved before
this application and has DECISION: IMPORT. The source supplement,
large factorizations and numerical consumers were not replayed here.
The source reviewer reports only partial numerical regeneration;
its report is not a substitute for a full independent replay.

## Conclusion

There exists c_162>0, with no numerical value asserted here, such that

    E(f)>=c_162 ||f||_2^2 for every f in D_I.                  (2)

In particular this holds on H intersect D_I and W intersect D_I,
and on all C750c exact smooth trial spaces. On the neutral domain
the pole product vanishes exactly. Both reflection sectors and
arbitrary complex coefficients are included.

This is KNOWN_IMPORTED local progress, not mathematics beyond the
cited theorem. It supplies a qualitative fixed-window sign and
floor, not an evaluated complementary inverse, a usable numerical
floor, larger-window induction, all-support positivity, actual-Xi
realization or RH. C750c's scalar-floor rejection and its unfinished
U12 numerical diagnostic are preserved. No passing numerical
enclosure for that diagnostic is asserted.

The separate conceptual audit1134 (16 November 2026), under approved
assessment1132, accepts this entire local application. It checks the
complex normalization and the form-domain argument, not the external
computer-assisted theorem's numerical certificate.

## Proof

### 1. Strict support inclusion and centering

There is strict room inside the source interval. Indeed the positive
Taylor terms give

    exp(9/8)>1+9/8+(9/8)^2/2+(9/8)^3/6+(9/8)^4/24
            =300993/98304>3.

Thus a=2log(3)<9/4=b. Define g(y)=f(y+a), zero extended. This is
an L2 isometry from I to (-a,a), and its essential support is
contained in [-a,a], a compact subset of (-b,b). For real t,

    F_g(t)=exp(ita)F_f(t),   |F_g(t)|=|F_f(t)|,
    R_g(u)=R_f(u).                                          (3)

These follow by change of variables; the correlation integrals
exist by Cauchy--Schwarz. The Fourier identity also holds at complex
t because bounded support makes f and g integrable against every
fixed exponential. In particular

    F_g(i/2)=exp(-a/2)M_+(f),
    F_g(-i/2)=exp(a/2)M_-(f),
    F_g(i/2)conj(F_g(-i/2))=M_+(f)conj(M_-(f)).              (4)

The factors in (4) are real and their product is one. Hence
centering preserves the entire pole product, even without
neutrality. It also takes each zero moment to an exact zero moment.

### 2. All terms and the complete prime cutoff

The source equation(2) uses exactly m(t) and dt/(2pi), the Fourier
sign in (3), and the correlation convention in (3). Thus the gamma
term has no added scalar or rescaling. Its pole term is exactly
(4). Its prime term has the same coefficient -2Lambda(n)/sqrt(n)
and real part as (1).

For any |u|>=T the intervals supporting f(x+u) and f(x) have
intersection of measure zero. Therefore R_f(u)=0, including at
u=T, for every L2 function under consideration. The source sum at
radius b consequently reduces to n<exp(T)=81 on these g. In
particular its terms at 81,83,89 vanish; the term at81 is zero
overlap, not an endpoint estimate. The surviving prime powers are
the22 primes below81, the5 further powers4,8,16,32,64 of2, the2
further powers9,27 of3, and25,49: all31 terms of (1). No term
with nonzero von Mangoldt weight below81 is omitted.

It follows that the source expression evaluated at g equals E(f).
The finite-sum conclusion uses support only, not cancellation or
an unproved sign of an individual prime contribution.

### 3. Membership of the whole local logarithmic domain

We must apply the source's closed form to every f in D_I, not
only its smooth tests. Here the strict inclusion in Section1
avoids any boundary trace assumption. Choose a nonnegative real
rho in C_c^infinity(-1,1) with integral one and set

    rho_epsilon(y)=epsilon^(-1)rho(y/epsilon),
    g_epsilon=rho_epsilon*g,  0<epsilon<b-a.

These are smooth compact tests in (-b,b), though generally not
neutral. On the real axis F_(g_epsilon)=F_rho(epsilon*t)F_g(t),
where |F_rho(epsilon*t)|<=1 and F_rho(epsilon*t)->1. Dominated
convergence, using (3) and the definition of D_I, gives

    integral_R log(2+|t|)|F_(g_epsilon-g)(t)|^2 dt ->0.       (5)

Since log(2+|t|)>=log2>0, Plancherel also gives L2 convergence.
L744(8) gives |m(t)|<=A+log(2+|t|) for one finite A; consequently
the gamma pairings converge in (5)'s norm by Cauchy--Schwarz.
The moments on (-b,b) are bounded L2 functionals. Each shift is
an L2 contraction, and there are only finitely many active source
delays on this fixed interval. Thus all pole and prime pairings
also converge. This includes differences of two approximants.

For completeness, the convergence is in the source's closed-form
norm, without first assuming the source sign. Here is an explicit
comparison, checked in audit1134. Put w(t)=log(2+|t|) and

    J(h)=integral_R w(t)|F_h(t)|^2 dt/(2pi),
    A=2+8sqrt(2)/3+log(4pi),
    B=max{A+2log(3), 2+log(6pi)}.

L744(8) implies |m(t)-w(t)|<=B: for |t|<=1 use
|m(t)|<=A+w(t) and w(t)<=log3; for r=|t|>=1 use
|m(t)-log(r/(2pi))|<=2/r^2 and
w(t)-log(r/(2pi))=log(2pi)+log(1+2/r)<=log(6pi).
Thus the gamma form differs from J by at most B||h||_2^2.

Let q_b denote the source smooth form on (-b,b), and set

    P_b=2 sum_(n>=2, log n<2b) Lambda(n)/sqrt(n),
    D=B+4sinh(b)+P_b,   C=D+1.

The sum is finite. A zero-extended shift is an L2 contraction, so
the absolute prime form is at most P_b||h||_2^2. The two exponential
moment functionals each have squared norm
integral_(-b)^b exp(plus-or-minus x)dx=2sinh(b).
Consequently the absolute complete pole product is at most
4sinh(b)||h||_2^2, with no neutrality assumption. Therefore

    |q_b[h]-J(h)|<=D||h||_2^2,
    J(h)+||h||_2^2 <= q_b[h]+C||h||_2^2
                   <= J(h)+(2D+1)||h||_2^2
                   <= [1+(2D+1)/log2]J(h).                  (6)

The last step uses Plancherel and J(h)>=log2||h||_2^2.
These inequalities hold on the smooth core, including differences
of the approximants. They prove equivalence of the shifted source
form norm and J^(1/2), before any positive spectral bound is used.
Thus a sequence epsilon_j decreasing to zero gives g_(epsilon_j)
Cauchy in the norm defining
the Friedrichs form closure. Its L2 limit is g, so g belongs to
that closure, and its closed-form value is precisely the expression
identified in Section2. This argument imports the source closure;
it does not infer domain membership merely from finite L2 norm.
The approximants need not be neutral because every pole term was
retained before taking the limit.

### 4. Applying the external sign and restricting to the neutral space

Let c_162=inf sigma(A_b)>0 as asserted by the cited Theorem. The
lower spectral bound means its closed quadratic form is at least
c_162 times the squared L2 norm throughout its form domain.
Sections1-3 identify E(f) with that form at g, and ||g||_2=||f||_2.
This proves (2). Restriction to H and W gives the stated neutral
conclusions, since both exact moments vanish there. C750c establishes
that its smooth cutoff trials and their finite original-metric
projections belong to D_I and satisfy those moments.

No source Fourier cutoff is identified with W. Neither a middle
Schur margin nor a finite core eigenvalue is assigned to c_162.
The existence of this floor does not make C750c's stopped scalar
certificate succeed: that certificate loses the full inverse
structure. Its numerical low-energy evidence and all its arithmetic
qualifications remain exactly as recorded.

### Separate conceptual audit1134

The audit accepts Sections1-4 under the stated external theorem.
The Taylor sum in Section1 is exact; its strict inequality supplies
the interior mollifier margin. Translation is an isometry for the
unweighted measure, and (4) preserves the complex pole product: the
two moment factors acquire reciprocal real scalings. For L2 zero extensions, a singleton overlap
at u=T has measure zero; all31 surviving prime powers remain. The
logarithmic dominated-convergence majorant in (5) is 4w|F_g|^2,
which is integrable by hypothesis. Formula(6) closes the domain
argument independently of the sign being imported. Bounded moments
and shifts identify the limiting complete form, even though the
approximants need not be neutral or remain in the smaller interval.

The cited source Section2(2), its core paragraph following(7), and
Section6(31)-(32) concern this complete complex closure. The spectral
lower-bound principle applies to its form domain, not just its
operator domain. Restriction to H and W introduces no new domain
claim or omitted pole term. The direct local mathematical inputs
remain L744 and C750c; no new DAG edge is required. This is validation
of a known-result import, not a new positivity mechanism, an effective
constant, independent certificate regeneration or an RH candidate.

## Mathlib

Matching coverage for the imported computer-assisted fixed-support
theorem and this complete supported logarithmic form has not been
checked. Plancherel, dominated convergence, convolution/Fourier
identities and the lower spectral-bound principle are standard
supporting results; no exact Mathlib theorem names or Lean verification
are claimed. The external certificate remains a cited input with the
version and independent-replay limitations specified above.
