# Corollary919t: root-aligned paired-lobe density need not be log-concave

## Hypotheses

For P(t)=t^4+t^2, I=[2/3,7/10], 0<rho<1 and a in I, put

    c=3a/2,
    W_(rho,a)(t)=rho^(3/2)[log cosh((t-c)/rho)
                              +log cosh((t+c)/rho)],
    K_(rho,a)(t)=exp(-P(t)-W_(rho,a)(t)),
    F_(rho,a)(z)=integral_0^infinity K_(rho,a)(t)cos(zt)dt.

Import C919s's base-quartic first-zero certificate, including its
explicit CPython integer/Fraction and libmpdec rounding contracts.
Those contracts remain assumptions; this proof neither reruns nor
formally verifies them. All perturbation and series estimates below
are analytic, without new numerical quadrature or parameter fitting.

## Conclusion

There is rho_*>0 such that for every 0<rho<rho_* there exists
a=a_rho in I for which x=pi/a is the simple least positive real zero
of F_(rho,a). For each such pair, K is positive, even and smooth,
(log K)''<0 everywhere, and for every integer m>=0 and B>0,

    exp(B|t|)|K^(m)(t)| -> 0 as |t| -> infinity.

The density

    H(u,v)=sin(xv) sum_(j>=0)
      [K(u+v+2ja)-K(u+v+(2j+1)a)],   u>=0, 0<v<a,

is strictly positive and smooth in the interior. Its defining series
and all its derivative series converge locally uniformly. At the fixed
interior point u=v=a/4 it satisfies

    H H_uu-H_u^2 >= b d/(4 sqrt(rho)) > 0,                 (1)

where the constants, independent of rho and a, are

    b=exp(-P(7/20))-exp(-2)>0,
    d=exp(-P(21/20))>0.

Consequently the stated kernel and first-zero hypotheses do not imply
joint log-concavity of this paired-lobe density. This stops that
generic sufficient premise only. It proves nothing adverse about
log-concavity of the marginal itself or of any actual-Xi kernel, and
does not prove or disprove first-zero preservation or RH. The marginal
identity, actual-Xi applicability and iteration are not premises of
this obstruction and are not established here. Conceptual audit2263
independently checked the analytic estimates and root alignment below,
retaining C919s's software contracts as assumptions; it found no
mathematical repair necessary. This is an audited conditional
obstruction, not an unconditional software verification or RH candidate.

## Proof

### Imports and scope of the specialization

C919s, under its explicit software contracts, supplies the following
weakened bounds for F_0(y)=integral_0^infinity exp(-P(t))cos(yt)dt:
with alpha=147/32 and beta=37/8,

    F_0(y)>3/10000                  (0<=y<=alpha),
    F_0(beta)<-1/1000,
    F_0'(y)<-1/25                   (alpha<=y<=beta).       (2)

Specifically, its complete first147 interpolation cells have margin
greater than0.00031823; the beta endpoint is below-0.00146124;
and the derivative on the final cell is below-0.04522430249.
Thus (2) is an import of checked interval inequalities, not an
assumption inferred from a plotted zero. No other conclusion of
C919s is used, and its fixed marginal curvature test is not repeated.

Use the named intermediate value theorem. Differentiation under the
integral uses K. Conrad, *Differentiating under the integral
sign*, author-hosted30-page version inspected21November2026,
Theorem12.3 p16:
https://kconrad.math.uconn.edu/blurbs/analysis/diffunderint.pdf .
For dominated convergence use T. Tao, *245B, notes0: A quick review
of measure and integration theory*,1January2009, Theorem3(4)-(5):
https://terrytao.wordpress.com/2009/01/01/245b-notes-0-a-quick-review-of-measure-and-integration-theory/ .
The summable majorants below also justify ordinary termwise
differentiation of series, by the uniform derivative-series theorem.
For the curvature test use S. Boyd and L. Vandenberghe,
*Convex Optimization*, Cambridge2004, corrected printing2009,
Section3.5.1 p105: for positive C2 f on an open convex domain,
log-concavity requires f Hess(f)-grad(f)grad(f)^T to be negative
semidefinite. Direct text:
https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf .

These standard tools were assessed in notes2260. They do not supply
the root alignment or the singular derivative-series estimate; those
are the necessary specializations proved here. Tuck's sine positivity
and Prekopa's marginal theorem motivate the proposed mechanism, but
neither is a mathematical input to this counterexample. In particular
no marginal theorem is applied without joint log-concavity.

### Admissibility and uniform transform perturbation

Write V=P+W and q=sqrt(rho), and, with c=3a/2, define

    A_(rho,a)(t)=tanh((t-c)/rho)+tanh((t+c)/rho),
    B_(rho,a)(t)=sech^2((t-c)/rho)+sech^2((t+c)/rho).

Evenness and smoothness follow from the displayed real formulas.
Since 0<=log cosh z<=|z| for real z, for t>=0 we have

    0<=W(t)<=q(|t-c|+|t+c|)<=q(2t+3a),
    |W'(t)|<=2q,             W''(t)=q^(-1)B_(rho,a)(t).

The last equality is an exact derivative, with rho fixed. Therefore

    V''(t)=12t^2+2+q^(-1)B_(rho,a)(t)>=2.                 (3)

As V is even, V'(0)=0, and integrating (3) gives V'(t)>=2t
for t>=0. Hence K is strictly decreasing on[0,infinity), even
though K'(0)=0. Also (log K)''=-V''<0 everywhere.

For every fixed rho>0 all derivatives of tanh are polynomials in
tanh (differentiate using tanh'=1-tanh^2), and so are bounded on R.
It follows that V'=P'+O_rho(1), V''=P''+O_rho(1),
V'''=P'''+O_rho(1), V''''=24+O_rho(1), and all higher
derivatives of V are O_rho(1), uniformly in a in I and real t.
Repeated differentiation of exp(-V) gives exp(-V) times a finite
polynomial in V',...,V^(m). Thus, for every m, some finite
C_(m,rho), uniform in a, satisfies

    |K^(m)(t)|<=C_(m,rho)(1+|t|)^(3m) exp(-P(t)).          (4)

For example the degree bound follows by assigning degree at most3j
to V^(j) in each term of total derivative weight m; this is a coarse
bound, not a claim that higher derivatives of V grow polynomially.
The constants in (4) may diverge as rho decreases. Quartic decay
proves the asserted weighted limits and all polynomially weighted
exponential integrability, for every fixed m and B. In particular
F_(rho,a) is entire by domination on each compact complex z disk.

For t>=0, 1-exp(-W)<=W and K<=exp(-P) give

    |K_(rho,a)(t)-exp(-P(t))|
       <=q(2t+21/10)exp(-P(t)).                           (5)

Define the finite, positive constants

    M_j=integral_0^infinity t^j(2t+21/10)exp(-P(t))dt,
    j=0,1.

Differentiation of F with respect to its real frequency is justified
by t exp(-P(t)), independently of a and rho. Since |cos|,|sin|<=1,
(5) implies the bounds, uniform in real y and a in I,

    |F_(rho,a)(y)-F_0(y)|<=q M_0,
    |F_(rho,a)'(y)-F_0'(y)|<=q M_1.                       (6)

### Exact alignment and exclusion of every earlier zero

Choose rho small enough that

    q M_0<1/10000,                 q M_1<1/100.            (7)

Equations (2) and (6) then give, for every a in I,

    F_(rho,a)(y)>2/10000           (0<=y<=alpha),
    F_(rho,a)(beta)<-9/10000,
    F_(rho,a)'(y)<-3/100           (alpha<=y<=beta).        (8)

Each such transform consequently has exactly one zero in
(alpha,beta), it is simple, and it is its least positive real zero.
Existence follows from the endpoint signs; uniqueness and simplicity
follow from the strict derivative bound; positivity on[0,alpha]
and monotonicity before that zero exclude all earlier positive zeros.
No assertion about its other real or complex zeros is needed.

Now let

    J=[pi/beta,pi/alpha]=[8pi/37,32pi/147].

The elementary Archimedean bounds 223/71<pi<22/7 show J is
strictly inside I. For fixed rho satisfying (7), the real function

    Q_rho(a)=F_(rho,a)(pi/a)

is continuous on J: its integrand is continuous in a and dominated
by exp(-P(t)). At the left endpoint its value is negative by (8),
and at the right endpoint positive. The intermediate value theorem
provides a_rho in the interior of J with Q_rho(a_rho)=0.
Equation (8) then makes pi/a_rho precisely the simple least positive
zero. This does not require a continuous choice of a_rho, a root
branch, or differentiability with respect to rho at0.

### Local derivative convergence and positivity of the density

For fixed rho>0 set

    S_(rho,a)(s)=sum_(n>=0)(-1)^n K_(rho,a)(s+na).

For s in any fixed compact real interval and a in I, the argument
s+na grows at least linearly in n for all sufficiently large n.
Equation (4) bounds the absolute value of every term of every fixed
s-derivative series by C(1+n)^(3m)exp(-c_1 n^4), with C,c_1>0
independent of s,a and n. The finitely many remaining n have a
uniform bound by continuity on a compact set. These majorants are
summable. The uniform derivative-series theorem therefore makes S
smooth in s and permits every stated termwise derivative. The same
majorants and the smooth sine factor give all local u,v derivative
series for H, including on a neighborhood of the chosen interior
point. This argument is for fixed rho; it makes no false unscaled
C2 convergence assertion as rho goes to0.

Absolute convergence permits grouping adjacent n, so

    S_(rho,a)(s)=sum_(j>=0)[K(s+2ja)-K(s+(2j+1)a)].

For s=u+v>0 each bracket is strictly positive by (3).
Also sin(pi v/a)>0 for0<v<a. Hence H>0 throughout its stated
domain. The open interior (0,infinity)x(0,a) is convex.

### Full scaled second-derivative estimate at the fixed lattice

At u=v=a/4 write s_a=a/2 and t_n=(n+1/2)a. To display explicit
summable bounds, put

    l_n=(2n+1)/3,             r_n=7(2n+1)/20,
    M[R]=sum_(n>=0) R(r_n)exp(-P(l_n))

for each polynomial R with nonnegative coefficients. Since
l_n<=t_n<=r_n, P is increasing on[0,infinity), and R is
nondecreasing there, M[R] bounds sum R(t_n)exp(-P(t_n))
uniformly in a in I. Every such series is finite by quartic decay.
Use the following constants only for the lattice estimates:

    N_0=M[1],
    N_W=M[2t+21/10],
    N_1=M[P'(t)+2],
    N_2=M[(P'(t)+2)^2+P''(t)].

Let

    T(a)=sum_(n>=0)(-1)^n exp(-P(t_n)).

Equation (5) and |V'|<=P'+2 give

    |S_(rho,a)(s_a)-T(a)|<=q N_W,
    |S_(rho,a)(s_a)|<=N_0,       |S_(rho,a)'(s_a)|<=N_1.  (9)

The base series is positive with the quantitative lower bound

    T(a)>=exp(-P(a/2))-exp(-P(3a/2))
         >=exp(-P(7/20))-exp(-2)=b>0,                    (10)

because every subsequent paired bracket is positive. The last strict
inequality follows from 7/20<1 and P strictly increasing there.

Exact differentiation gives

    q K''(t)={q[(P'(t)+q A_(rho,a)(t))^2-P''(t)]
                         -B_(rho,a)(t)}K(t).             (11)

The absolute value of the sum of the regular q-multiplied terms in
(11) is at most q N_2. At the lattice points the remaining factor is

    B_(rho,a)(t_n)=sech^2((n-1)a/rho)
                         +sech^2((n+2)a/rho).

The first term equals1 exactly when n=1; it then contributes
+K_(rho,a)(3a/2) to the alternating sum of -B K. For all n!=1,
|(n-1)a|>=2/3, while (n+2)a>=4/3 for every n>=0.
The inequality sech^2 z<=4exp(-2|z|), obtained from
cosh z>=exp(|z|)/2, therefore bounds all the other terms together
by

    4 N_0[exp(-4/(3rho))+exp(-8/(3rho))].

This controls the complete infinite complement, including the second
sech term at n=1; it is not a finite-lattice approximation. At
c=3a/2<=21/20, (5) also gives

    |K_(rho,a)(c)-exp(-P(c))|<=(21/5)q.

Consequently, uniformly for a in I,

    |q S_(rho,a)''(s_a)-exp(-P(3a/2))|<=E_2(rho),         (12)
    E_2(rho)=q(N_2+21/5)
              +4N_0[exp(-4/(3rho))+exp(-8/(3rho))] -> 0.

Thus the singular second derivative has been isolated with an
explicit vanishing error. Equation (12) does not exchange a limit
with an unbounded derivative series without a majorant.

### Determinant sign and what it excludes

In taking u derivatives, a,rho and x=pi/a are fixed parameters.
At u=v=a/4, sin(xv)=sin(pi/4), so exactly

    D_rho(a):=(H H_uu-H_u^2)(a/4,a/4)
       =(1/2)[S_(rho,a)(s_a)S_(rho,a)''(s_a)
                                     -S_(rho,a)'(s_a)^2].

Equations (9) and (12) imply the full uniform error bound

    |q D_rho(a)-(1/2)T(a)exp(-P(3a/2))|<=E(rho),         (13)
    E(rho)=(1/2)[N_0 E_2(rho)+q N_W+q N_1^2] -> 0.

For example, subtract the two products by writing
S(qS''-exp(-P(c)))+(S-T)exp(-P(c)); its absolute value is
at most N_0 E_2+q N_W because exp(-P(c))<=1. The squared
first derivative costs at most q N_1^2. This proves (13) without
requiring convergence of S' or cancellation in its square.

By (10) and c<=21/20, the limiting term in (13) is at least
b d/2. Since E(rho) tends to0, there is a positive threshold
rho_C such that E(rho)<b d/4 whenever0<rho<rho_C. Together
with (7), for instance take any positive rho_* less than

    min{1, rho_C, (1/(10000 M_0))^2, (1/(100 M_1))^2}.

This gives q D_rho(a)>b d/4 uniformly over I, proving (1)
for every aligned a_rho constructed above. The threshold is
existential, with explicit convergent integrals/series and errors;
no numerical value of rho_* or sampled curvature is claimed.

As H is positive and C2 near the fixed interior point,
partial_u^2 log H=(H H_uu-H_u^2)/H^2>0 there. The cited Hessian
criterion rules out joint log-concavity. All hypotheses of the
proposed generic implication, including the exact first-zero
condition, hold under the stated inherited software contracts.
The counterexample concerns this representation's joint curvature,
so it does not assert failure of any conclusion obtainable after
integrating v by some different argument.

### Conceptual audit2263: quantifiers, complete tails and scope

21 November2026. This audit reproduces the analytic argument under
the unchanged hypotheses. It imports only C919s's three cell bounds,
not its marginal conclusion, a numerical zero approximation, or any
assumption about the other zeros. It does not rerun the certificate.

**Inherited inequalities and alignment.** The complete first147
interpolation cells in C919s cover [0,147/32], endpoints included;
their minimum margin exceeds 0.00031823, hence exceeds 3/10000.
Its beta endpoint upper bound -0.00146124 is below -1/1000, and
its whole-final-cell derivative bound -0.04522430249 is below -1/25.
Thus all of (2), including the entire earlier interval, is available
under the stated arithmetic contracts. Combining these strict bounds
with q M_0<0.0001 and q M_1<0.01 gives respectively the uniform
margins 0.0002, -0.0009 and -0.03 in (8). These are actual whole
interval bounds; there is no interpolation of the perturbed transform.

The Archimedean bounds give

    pi>223/71>37/12,        pi<22/7<1029/320,

where the inner rational comparisons reduce to 2676>2627 and
7040<7203. Consequently 8pi/37>2/3 and 32pi/147<7/10.
The endpoints of J are ordered since beta>alpha. For every fixed
rho obeying (7), dominated continuity applies to Q_rho on this
entire compact interval. Its left and right signs are negative and
positive respectively, uniformly by (8). IVT therefore gives an
interior a_rho. For that same parameter, positivity up to alpha and
strict decrease throughout [alpha,beta] exclude every smaller zero
and give simplicity. This proves the quantifier order
"every sufficiently small rho, some a_rho"; neither a continuous
selection nor a derivative of a_rho is used anywhere downstream.

**All derivative orders.** For fixed rho, a derivative of order j>=1
of W is rho^(3/2-j) times two bounded real functions obtained by
differentiating log cosh; their bounds are translation-independent.
Each monomial in the mth derivative of exp(-V) has total derivative
weight m in V',...,V^(m). Giving V^(j) the coarse growth degree 3j
therefore bounds the product by a constant times (1+|t|)^(3m).
Since W>=0, multiplication by exp(-P) gives (4), uniformly over I.
For a compact set |s|<=R and n sufficiently large,
s+na>=n/3 and |s+na|<=R+7n/10. Thus every mth derivative series
has a summable majorant of the form C(1+n)^(3m)exp(-n^4/81),
with the finitely many other terms bounded separately. Sine-factor
derivatives introduce only powers of x=pi/a, which are bounded on I.
This establishes every local mixed derivative of H. Constants may
depend on rho here. No uniform unscaled C2 limit is inferred.

**Uniform scaled tail.** At t_n=(n+1/2)a, the exact singular part
of q S'' is the sum of

    -(-1)^n K(t_n)[sech^2((n-1)a/rho)
                            +sech^2((n+2)a/rho)].

The n=1 first summand equals +K(3a/2); its sign is positive.
The absolute sum of the remaining first summands, n!=1, is at most
4 exp(-4/(3rho)) sum_(n!=1) K(t_n). The absolute sum of ALL second
summands, including n=1, is at most
4 exp(-8/(3rho)) sum_(n>=0) K(t_n). Both sums are bounded by N_0.
This accounts for the complete infinite complement without any
cancellation or finite cut-off. The regular part has absolute sum
at most q N_2, since |P'+q A|<=P'+2 at the positive lattice.
Finally (5) at c<=21/20 bounds |K(c)-exp(-P(c))| by 21q/5.
These bounds reproduce precisely (12), with constants independent
of a and rho. Each defining M[R] converges because its summand is
a polynomial in n times exp(-P((2n+1)/3)).

**Nonvanishing limit and determinant.** The first positive pair in
T is at least b: a/2<=7/20 and 3a/2>=1, so its two terms have
the required lower and upper bounds. Every remaining paired term
is positive. Also exp(-P(3a/2))>=d>0. With a and rho fixed when
differentiating u, sin^2(xv)=1/2 at v=a/4. Subtracting the product
limits as in (13) costs at most N_0 E_2+q N_W, and the first
derivative square costs at most q N_1^2. After multiplication by
1/2 these are exactly E(rho). Thus q D>=bd/2-E(rho)>bd/4
for all a in I once rho is sufficiently small. Combining this
threshold with (7) is legitimate because all constants are finite,
positive where required, and independent of a. In particular the
same estimate holds for every root-aligned choice, without choosing
a to optimize curvature. The existential threshold is sufficient;
no effective rho value or numerical curvature certificate is asserted.

Absolute convergence and strict decrease of K justify positivity of
each paired difference for s=u+v>0. Hence the positive smooth H is
eligible for the cited Hessian criterion on the convex open strip.
Positive u-direction log curvature there disproves joint
log-concavity, irrespective of the other Hessian entries. It gives
no sign for the curvature of an integral in v. Marginal identity,
actual-Xi applicability, iteration and all-degree transfer remain
unresolved. The direct mathematical input remains C919s alone;
Tuck/Prekopa and earlier failed tests are comparisons, not premises.
The audit supplies no new theorem beyond the conditional C919t result
and makes no stronger novelty or Mathlib-coverage claim.

## Mathlib

Full matching Mathlib coverage has not been checked and is not
asserted absent. No Mathlib theorem is an input. The named standard
calculus and Hessian tools above supply supporting mathematics;
they do not themselves prove (2), root alignment, or the specialized
scaled-lattice estimate. The bounded literature comparison2260 found
no matching theorem, which is not a claim of certified originality.
