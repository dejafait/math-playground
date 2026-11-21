# Corollary C030r: the finite-convolution moving basis for conjugate rates

## Hypotheses

Let m>=1, n>=2m and 1<=d<=floor(n/2) be integers. Fix real
a_1,...,a_m,r>0 and b_1,...,b_m. The n rates are

    (q_1,...,q_n)=(a_1+i*b_1,a_1-i*b_1,...,
                   a_m+i*b_m,a_m-i*b_m,r,...,r).

Set A=sum_l |b_l| and I={x>0:x*A<=1/4}. If A=0, I=(0,infinity).
The count d is the basis dimension, not the pair count m. If n=2m,
there are no r entries. Repeated rates, zero phases, all signs of the
real-part contrasts and the closed phase boundary are included.

For Re(q)>0 let e_q(t)=q*exp(-q*t) for t>0 and zero for t<=0, and
let f_b=e_(q_1)*...*e_(q_n). These are complex integrable kernels;
individual e_q are not asserted to be positive probability densities.
Only the interior function f_b(x), x>0, and its ordinary derivatives
are used. Every rate is fixed when x is differentiated.

Use C030q's separately normalized orbital integrals Z_(k,b) and
responses G_(k,b)=-Z'_(k,b)/Z_(k,b), for 0<=k<=n. In particular,

    Z_(k,b)(x)>= (31/32)*Z_(k,0)(x)>0, x in I.          (1)

This proof uses that established floor; it does not need the stronger
response estimate or its full-array proof again.

## Conclusion

Write H_k(x)=[f_b^(u+v)(x)]_(0<=u,v<k), Delta_k=det H_k and
D_k=(-1)^(k*(k-1)/2)*Delta_k, with D_0=Delta_0=1. Put
F_j=product_(h=0)^(j-1) h!, F_0=1, and R=product_l q_l. Then

    D_k(x)=R^k*(F_k*F_(n-k)/F_n)*x^(k*(n-k))*Z_(k,b)(x)>0,
                      0<=k<=n, x in I.                (2)

For each x in I define the real bilinear functional

    L_x(P)=P(partial_x)f_b(x)

on real polynomials in an independent variable z.
The coefficients are frozen when the polynomial acts on f_b; subsequent
parameter differentiation also differentiates any moving coefficients.
Its unique monic orthogonal polynomials P_i(x;z), 0<=i<n, have signed norms

    h_i(x)=L_x(P_i^2)=(-1)^i*D_(i+1)(x)/D_i(x).        (3)

The source normalization is

    Q_i(x;z)=P_i(x;z)/sqrt(|h_i(x)|),
    L_x(Q_i Q_j)=(-1)^i*delta_(ij).                    (4)

Let C_x be the d-by-d matrix of coefficients of Q_0,...,Q_(d-1)
in the ordered monomials 1,z,...,z^(d-1). It is real, lower triangular,
nonsingular and smooth locally at every x in I, and

    C_x H_d(x) C_x^T=diag(1,-1,...,(-1)^(d-1)).        (5)

This is the actual derivative-moment basis of Sra's construction.
Its multiplication diagonal, defined without a positivity assumption by
alpha_i(x)=(-1)^i*L_x(z*Q_i(x;z)^2), satisfies

    alpha_i(x)=(n-2i-1)/x
                  -(G_(i+1,b)(x)-G_(i,b)(x)), 0<=i<d. (6)

The same basis has the parameter equation C'_x=K_x C_x, where

    (K_x)_(ii)=-alpha_i(x)/2,
    (K_x)_(i,i-1)=sqrt(D_(i+1)(x)*D_(i-1)(x))/D_i(x), 1<=i<d,
                                                               (7)

and all other entries vanish. This identifies the source's moving
basis; it is not a norm bound on its evolution.

This is a source-based specialization under assessment1225, established
in attempt1226. Independent conceptual audit1228, under the unchanged
SPECIALIZE assessment1226, passes (2)-(7) with their original hypotheses
and constants. This is REPRODUCTION of the finite interface, with no
claim of originality, a new all-degree theorem or an RH candidate.
No positive-variance inequality, C.9 shift-norm estimate, signed-
smoothing theorem, global PF assertion, x=0 limit, infinite reference
or actual-Xi realization is claimed.

## Proof

### Imported results and the reason for the specialization

S. Sra, *On some positivity properties of the Riemann Xi function*,
[author v3, 2 November 2026](https://suvrit.github.io/papers/riem-xi/riem-xi-v3.pdf),
Lemma C.6/(C.10), pp23-25, proves the determinant identity in (2) for
positive real rates with probability Haar normalization, including
repeats. Lemma C.5, pp22-23, and the C.9 proof through (C.21), pp27-28,
specify the derivative-moment basis and its positive leading coefficients.
Equation (C.17), p27, is the real-rate diagonal identity. Numbering here
is author-v3, not Hub-v1. We import the real-rate determinant theorem;
we do not reprove its HCIZ evaluation or its factorial constant.

For finite orthogonalization we use S. Pozza, M. S. Pranic and
Z. Strakos, *The Lanczos algorithm and complex Gauss quadrature*,
ETNA 50 (2018), 1-19,
[Definitions 1.1-1.2 and Theorem 1.3, p2](https://epub.oeaw.ac.at/0xc1aa5572%200x0039ff98.pdf).
Nonzero leading Hankel determinants through size k+1 give the bilinear
orthogonal polynomials through degree k. No positive measure is required.
The source's determinant index j denotes size j+1; taking k=n-1 here
requires precisely Delta_1,...,Delta_n, all covered by (10).
The finite, bilinear version is the one used here, not existence of an
infinite nondegenerate orthogonal sequence.

The change from real to conjugate rates is outside Sra's stated
hypotheses. Thus analyticity, reality, signed pivots and smooth real
normalization must be justified. The argument below supplies precisely
those checks and the parameter derivative; it does not assume that the
source's probabilistic variance or norm bounds extend.

### Entire dependence and the exact determinant identity

Let S={u in R^(n-1):u_j>=0, sum_(j<n)u_j<=1}, put
u_n=1-sum_(j<n)u_j, and integrate with ordinary (n-1)-dimensional
Lebesgue measure du. Thus vol(S)=1/(n-1)!. For x>0 the defining
convolution, after t_j=x*u_j for j<n, is exactly

    f(x;q)=R*x^(n-1)*integral_S exp(-x*sum_(j=1)^n q_j*u_j)du.  (8)

For the stated rates absolute convergence follows already from
Re(q_j)>0. More generally the right side of (8) defines an entire
function of (x,q_1,...,q_n) in C^(n+1). On each compact parameter set
the exponential is bounded by exp(|x|*max_j |q_j|); every fixed mixed
derivative is a polynomial factor times this exponential and is uniformly
bounded on S. Integration and differentiation therefore commute locally,
by compact domination, or equivalently by locally uniform integration
of the exponential series. In particular all derivative moments used
in H_k, and hence D_k, are entire in the rate variables for fixed x.

For Q=V P_k V*, its diagonal entries are real, nonnegative, at most
one and sum to k. Consequently

    |sum_j q_j Q_jj|<=k*max_j |q_j|.

Probability Haar measure is finite. This bound and the corresponding
bounds on every parameter derivative show that

    Z_k(x;q)=integral_(U(n)) exp(-x*sum_j q_j Q_jj)dV

is also entire in (x,q). Thus, for fixed x>0 and fixed k, the difference
between the two sides of (2), without its positivity assertion, is an
entire function of all n rates. The right side has a polynomial R^k
and a constant factorial denominator; no rate difference is divided out.

For all positive real q_j this difference vanishes by the cited C.10,
because (8) is exactly the source's normalized exponential convolution.
Fix q_2,...,q_n positive real and apply the one-variable holomorphic
identity theorem in q_1: the difference vanishes for every complex q_1.
Now fix any such q_1 and positive real q_3,...,q_n and apply the theorem
in q_2. Continue in this order. Induction gives zero for every complex
rate tuple. This is an identity-theorem argument, not an inference from
continuity on a real subset. It proves (2)'s identity with the exact
unchanged factorial constant. The case k=0 is also the direct identity
1=1, with the empty-product convention.

In particular repeated or zero-phase rates need no limiting quotient.
The continued identity is already defined at those tuples. No complex
probability law, uniqueness of a positive measure, or separate complex
HCIZ theorem is used in this continuation.

### Reality and signed pivots of the actual moments

For the stated family,

    R=r^(n-2m)*product_(l=1)^m (a_l^2+b_l^2)>0.       (9)

The simplex measure in (8) is invariant under permuting its n
barycentric coordinates: permutations among the first n-1 have unit
absolute Jacobian, and swapping u_j with u_n also has unit absolute
Jacobian. These swaps generate all permutations. Conjugating (8) at
real x replaces the rates by their conjugates, which permutes this
multiset. Thus f_b(x) is real for real x, as are all its derivatives.
This proves that L_x and each H_k are real, rather than assuming it
from an orbital identification alone.

For x in I, (1), (2), (9), x>0 and positivity of all factorial constants
give D_k(x)>0 for every k<=n. Hence

    Delta_k(x)=(-1)^(k*(k-1)/2)*D_k(x) != 0.           (10)

Apply the cited finite quasi-definite theorem with k=n-1. Its bilinear
functional is precisely L_x, with moments mu_j=f_b^(j)(x), not a
sesquilinear replacement. It provides monic P_i of degrees i<n.
Their coefficient reality and parameter dependence can be seen directly:
if P_i=z^i+sum_(a<i)c_a z^a, its orthogonality equations are

    H_i(x)*(c_0,...,c_(i-1))^T
                 =-(mu_i,...,mu_(2i-1))^T.           (11)

This is a uniquely solvable real system; its entries are analytic and
its determinant does not vanish. Thus the coefficients are real and
locally real analytic. For i=0 the monic polynomial is 1.

To compute the norm, change from 1,z,...,z^i to
1,z,...,z^(i-1),P_i. This triangular change has determinant one, and
orthogonality makes its Gram matrix the block diagonal matrix with
blocks H_i and h_i. Therefore Delta_(i+1)=Delta_i*h_i. Substitution
of (10) yields (3), with its exact sign and magnitude. In particular
no pivot vanishes. Taking the positive square root of |h_i| gives
(4), hence the lower triangular invertible C_x and (5).

At a boundary point x*A=1/4, each of the finitely many D_k is still
strictly positive. By continuity they remain positive on a real open
neighborhood of that point, which can be chosen within x>0. Equations
(11) and (3) then give analytic monic coefficients and smooth positive
square roots on that neighborhood. Thus parameter derivatives at the
closed boundary are ordinary two-sided local derivatives; no assumption
that the bound (1) holds beyond I is needed. The same reasoning covers
every interior point, zero phases and any repeated-rate tuple. It also
works locally in real family parameters because (8) is analytic and
the determinant floor at the point is strict.

### The multiplication diagonal and the moving parameter

Use z exclusively as polynomial variable. For a polynomial T(x;z)
whose coefficients vary smoothly in x, differentiation of its finite
moment expansion gives

    d/dx L_x(T)=L_x(z*T)+L_x(partial_x T).             (12)

Because P_i is monic, partial_x P_i has degree at most i-1. Its
bilinear product with P_i therefore has zero L_x value. Apply (12)
to T=P_i^2 to obtain h_i'=L_x(z*P_i^2). Consequently

    alpha_i=(-1)^i*L_x(z*Q_i^2)
            =L_x(z*P_i^2)/h_i
            =h_i'/h_i
            =(log(D_(i+1)/D_i))'.                    (13)

The first equality is indeed the diagonal of multiplication by z:
the coefficient of Q_i in zQ_i is its product with Q_i divided by
L_x(Q_i^2)=(-1)^i. For i<d, i+1<n, so the available finite sequence
contains every polynomial needed for this multiplication. There is
no infinite orthogonal-sequence assertion.

In (2) the rates, R and factorial constants are independent of x.
The difference between the adjacent powers of x is

    (i+1)*(n-i-1)-i*(n-i)=n-2i-1.

Take the real logarithmic derivative of their ratio. Positivity has
already justified those logarithms, including at a boundary point by
its open neighborhood. Equation (13) becomes (6), since the remaining
derivative is Z'_(i+1,b)/Z_(i+1,b)-Z'_(i,b)/Z_(i,b).
Each rank retains its own orbital normalizer.

For completeness, the parameter system also agrees with the source
construction, not just its diagonal. Since a parameter derivative
does not raise degree, K=C'_x C_x^(-1) is lower triangular and
partial_x Q_i=sum_(j<=i)K_(ij) Q_j within the first d rows.
Differentiate (4) using (12). For j<i the term containing
partial_x Q_j vanishes by degree, giving

    K_(ij)*(-1)^j=-L_x(z*Q_i*Q_j).                   (14)

If j<=i-2 the right side is zero, because zQ_j has degree at most i-1.
For j=i-1, write ell_j=sqrt(D_j/D_(j+1)) for the positive leading
coefficient of Q_j. The coefficient of Q_i in zQ_(i-1) is
ell_(i-1)/ell_i. Orthogonality therefore makes the right side in
(14) equal to -(ell_(i-1)/ell_i)*(-1)^i. Dividing by (-1)^(i-1)
gives the positive subdiagonal in (7). For j=i the two parameter-
derivative terms coincide, giving 2*K_(ii)*(-1)^i=-L_x(zQ_i^2),
and hence K_(ii)=-alpha_i/2. This proves (7). No variance estimate,
matrix-norm inequality or signed-remainder bound has entered.

### Scope of the completed test

The determinant constant, actual moments, signed pivots, normalization
and evaluation-parameter identity all pass the nominated finite test
and independent conceptual audit1228. The checks below specify the
audit's load-bearing boundary and normalization cases.

The entire-rate identity uses the normalized convolution (8), with
ordinary simplex volume 1/(n-1)!, and probability Haar measure. For
example, when every rate equals q>0, the k=1 constant in (2) is
F_1*F_(n-1)/F_n=1/(n-1)!, exactly the coefficient of
q^n*x^(n-1)*exp(-q*x) in (8); no simplex probability normalization
may be inserted a second time. At k=0 both sides are 1; at k=n the
orbital integral is exp(-x*sum_j q_j) and the factorial ratio is 1.
These are normalization checks of the imported identity, not its
replacement by finite examples. Its general validity follows from
the cited real-rate theorem and the successive uniqueness argument.
The compact domination already stated covers every derivative moment
through order 2n-2 and those needed for parameter differentiation.
Neither a rate-difference denominator nor a distinct-rate assumption
occurs in that continuation.

The actual bilinear functional, not its absolute value, has pivot
Delta_(i+1)/Delta_i=(-1)^i*D_(i+1)/D_i. Thus the positive leading
coefficient is ell_i=sqrt(D_i/D_(i+1)), and the sign division in (14)
gives K_(i,i-1)=ell_(i-1)/ell_i>0. In (12), writing
T=sum_j t_j(x)*z^j gives the finite sum
sum_j [t_j'(x)*mu_j(x)+t_j(x)*mu_(j+1)(x)]. Applying it to Q_i*Q_j
includes both moving-polynomial terms. The second one vanishes only
when j<i by degree; for j=i it supplies the factor 2 on the diagonal.
This verifies the parameter system without a positive-definite
Gram--Schmidt argument or identification of z with the evaluation x.
For i<d<=floor(n/2), Q_(i+1) exists since i+1<n; the first d parameter
rows nevertheless close because differentiation never raises degree.
For d=1 the subdiagonal statement is empty, including n=2.

At x*A=1/4 the floor (1) is strict for all finitely many ranks. Their
determinants therefore stay positive on a common real open neighborhood,
so the square roots, logarithms and both-sided x derivatives used in
(3)-(7) are legitimate there. This does not extend the uniform floor
beyond I. Local variation through repeated rates or b_l=0 is also
nonsingular by the same determinant argument. When n=2m the r factor
in (9) is simply 1. These checks cover the declared parameter boundary
cases without adding a positivity, variance or limiting assumption.

This gives C030q's already audited phase response an identified finite
reference. The whole interval is pointwise covered; no uniform bound
on C_x, C_x^(-1), K_x or its evolution has been established. Positivity
of the signed determinants does not make L_x a positive bilinear functional:
its signs alternate. In particular one cannot import a positive-law
variance bound or C.9's smoothing conclusion from this extension alone.
Actual-Xi supply and phase/degree/time control, signed-complement
payment, all-degree positivity, theta signing and graph realization
remain independent. Prior stop evidence is unaffected.

## Mathlib

Full matching coverage of (2)-(7), the source finite-convolution identity
and this conjugate-rate specialization is unchecked; no absence claim
is made. Holomorphic identity theorems, dominated parameter integration,
finite real linear systems and Gram determinant identities are supporting
mathematics. Exact supporting theorem-name matches were not checked,
and no formal verification is claimed.
[Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
