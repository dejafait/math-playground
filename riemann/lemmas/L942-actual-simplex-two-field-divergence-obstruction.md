# Lemma 942: two natural simplex-gradient fields cannot certify the actual density crossing

## Hypotheses

Use L019's actual positive kernel K and exactly L938(5)–(10), including
all 34 rows, twelve labelled factors, factorials and the M_0^12
normalization. Write k(x)=K(sqrt(x)) and h(x)=k'(x)/k(x). L938 proves
that k is analytic on a neighborhood of [0,8]; in particular the
definition of h at zero uses that analytic extension, not division
by sqrt(x) at zero. Set

    Delta={t_i>0: sum_(i=1)^12 t_i=1},
    w(t)=product_i t_i^(-1/2),
    G_E(t)=product_i k(E t_i), W_E(t)=w(t)G_E(t), 1/4<=E<=4.

The measure dt is dt_1...dt_11 with t_12=1-sum_(i=1)^11 t_i,
exactly as in L938(9). Let Pbar be L940(1)'s full arithmetic average;
this includes its factorial denominators. For a symmetric polynomial
F in twelve variables define the tangential field

    (X_F)_i=t_i(partial_i F-sum_j t_j partial_j F).                (1)

On the simplex it has sum_i (X_F)_i=0 and vanishes normally at each
coordinate face. If F is homogeneous of degree d, the sum in (1)
is dF on all of R^12. Let Q=sum_i t_i^2. The field family tested here is

    X=c X_Pbar+d X_Q, c,d in R.                                  (2)

Thus components have degree at most 13, the field is equivariant,
and the coefficients are rational when c,d are rational. The two
letters c,d in (2) denote scalar coefficients, not a homogeneity degree.
No coefficient bound is imposed. This family is a proper restriction
of the approved class of all equivariant face-preserving polynomial
fields of component degree at most 13.

For any such field define T_E X=div_Delta(W_E X)/W_E in the above
independent-coordinate chart. Use the following normalization of the
radial integrand:

    D_E(t)=(17+E sum_i t_i h(E t_i)) Pbar(t).                      (3)

No contact, PSD, realization, parameter endpoint, zero-location or RH
premise is made. The finite computation below uses integers and
rational interval arithmetic only; it does not assume a Decimal or
floating-point transcendental rounding contract.

## Conclusion

The exact radial and zero-flux identities are

    v'(E)=E^16/2^12 integral_Delta W_E(t) D_E(t) dt,
    integral_Delta W_E T_E X dt=0.                               (4)

The second identity holds for every polynomial field in the full
approved face-preserving tangential class, not just (2). Both integrals
are absolutely convergent, uniformly on the specified E interval.
Consequently a residual

    D_E+T_E X-a(E)Pbar >= epsilon>0                               (5)

on the entire interior simplex and energy interval would imply
v'(E)>0 at each zero of v in that interval, with the stated orientation.

However, no field (2) satisfies (5), for any real affine a, or even
any scalar function a defined at E=1/4, and any epsilon>0. Two exact
interior algebraic zeros of Pbar and a vertex limit give a positive
three-point combination annihilating both tested field columns, the
scalar columns and the radial column. Its radial value is exactly
zero, whereas strict positivity would require a positive value.

This rules out only (2). It supplies neither an obstruction to all
degree-13 fields nor a sign for v' at zeros of the integrated density.
The zeros used in this proof are zeros of Pbar on the simplex, not
asserted zeros of v. The actual crossing claim and RH remain open.
The construction and finite certificate have not received a separate
later proof audit.

## Proof

### Unnormalized differentiation and the measure

Permuting the twelve coordinates preserves the chart measure dt:
Euclidean hyperplane measure is sqrt(12) dt, and permutations are
isometries. Averaging the labelled polynomials in L938(9) therefore
gives exactly

    v(E)=E^17/2^12 integral_Delta W_E(t) Pbar(t) dt.               (6)

There is no extra 12!, orbit multiplicity, or probability normalizer.
Every zero-index factor in the original rows is still present.

By positivity and analyticity, k has a positive minimum on [0,5],
and k,k' are bounded there. Hence G_E and its first E and simplex
derivatives are bounded uniformly on the closed domain. The E
derivative is G_E sum_i t_i h(E t_i), including at t_i=0. The
polynomial Pbar is bounded, and w is integrable by the Euler beta
integral with twelve parameters 1/2. Thus w times one constant
dominates the integrand and its E derivative on a neighborhood of
[1/4,4]. Dominated differentiation of (6), including the E^17
prefactor, proves the first part of (4). Equivalently the positive
prefactor E^17/2^12 can be used with D_E/E. We fix (3) throughout
this attempt; no normalizer derivative has been dropped.

### Intrinsic divergence, the source dictionary and every face

Write partial_j^chart=partial_j-partial_12 on an ambient extension.
For a tangential field the chart components are X_1,...,X_11. Since
sum_(j<=11) X_j=-X_12, the product rule gives

    T_E X=div_chart X - (1/2) sum_(i=1)^12 X_i/t_i
                              + E sum_(i=1)^12 X_i h(E t_i).     (7)

Here div_chart X means sum_(j<=11) partial_j^chart X_j. The formula
is independent of the chosen ambient extension of the restricted
field. A polynomial vanishing on its coordinate face is divisible
by that coordinate in the simplex chart. For the twelfth face use
t_12=1-sum_(j<=11)t_j. Therefore X_i/t_i extends polynomially to the
closed simplex for every i. The right side of (7) is continuous and
bounded there, uniformly in E. It follows already that W_E T_E X
is absolutely integrable with an integrable multiple of w as majorant.

The known singular-face framework is Sebastian Andres, *Diffusion
Processes with Reflection*, TU Berlin dissertation (2009), Section3.2,
Proposition3.7 and its complete proof, printed pp54–55, PDF pages64–65
([primary thesis](https://d-nb.info/994899424/34)). Its C^1 vector
field must have zero normal component on every face. To check the
specialization explicitly, put y_j=sum_(i<=j)t_i, 1<=j<=11. The map
from (t_1,...,t_11) to y is triangular with determinant one. The
transformed field is Y_j=sum_(i<=j)X_i. Its normal components on
y_1=0, y_j=y_(j-1), and y_11=1 are, up to the fixed normalizing
constants, X_1, X_j, and -X_12 respectively. All vanish. The twelve
gaps are precisely the t_i, and the source parameters are N=11,
beta=6, since beta/(N+1)-1=-1/2. G_E is a uniformly C^1 multiplier.
This chart, multiplier and its corners require a local check; the
following is that check, not a new general integration-by-parts theorem.

For 0<delta<1/12 truncate at every face:

    Delta_delta={sum t_i=1, t_i>=delta for every i}.

Apply the ordinary divergence theorem in the eleven-dimensional
chart to W_E X, which is smooth on this truncated polytope. On
t_i=delta, i<=11, the boundary flux density in the ten remaining
independent coordinates is -W_E X_i. On t_12=delta the outward
normal is (1,...,1)/sqrt(11); its dot product with the chart field is
-X_12/sqrt(11), while the face area element is sqrt(11) times that
ten-coordinate measure. Thus the same formula -W_E X_12 applies.
Since |X_i|<=C t_i and G_E is uniformly bounded, the absolute value
of each integrated face flux is bounded by

    C delta^(1/2) integral_(sum_(j!=i)t_j=1-delta, t_j>=delta)
                                      product_(j!=i) t_j^(-1/2) dt
    <= C delta^(1/2) (1-delta)^(9/2)
                                      Gamma(1/2)^11/Gamma(11/2).

All constants can be chosen independently of E. The larger simplex
integral on the right includes every intersection with the other
faces and is finite. Intersections of truncated faces themselves
have zero ten-dimensional face measure. This treats endpoint faces,
all internal gap faces, and their intersections; no mass at corners
is omitted. All twelve fluxes tend to zero. Dominated convergence
for the volume integral, justified by (7), proves the second part
of (4). No componentwise all-direction Stein-class assertion is needed.

At a zero of v, (6) gives integral W_E Pbar=0. Integrating (5) and
using (4) gives integral W_E D_E>=epsilon integral W_E>0. The positive
factor E^16/2^12 establishes the crossing implication in the conclusion.

### The exact harmonic polynomial behind the natural field

Let B=sum_i(t_i partial_ii+(1/2)partial_i), acting on ambient
polynomials. Then

    B Pbar=0.                                                    (8)

Here is an algebraic proof retaining the full original normalization.
For L938's homogeneous polynomial P(A_0,...,A_6), set
A_n(r)=sum_(j=0)^n r^j A_(n-j)/j!. Modulo degree seven in the formal
variable z, sum_n (-1)^n A_n(r) z^n/A_0 is the original series times
exp(-rz). The formal logarithm therefore changes S_1 alone, leaving
S_2,...,S_6 and their H2 determinant unchanged. A_0(r)=A_0. L938(5)
therefore yields the polynomial identity

    sum_(k=1)^6 A_(k-1) partial_(A_k) P=0.                       (9)

The formal calculation can be made in the localization at A_0;
the resulting polynomial identity follows because that localization
is injective. It assumes no analytic logarithm or zero-free domain.

The linear map sending a monomial with twelve labelled A factors
to the full symmetrization of product_i t_i^k_i/(2k_i)! sends P to
Pbar. For each k>=1,

    (t partial_tt+(1/2)partial_t) t^k/(2k)!
                                      =t^(k-1)/(4(2k-2)!).

Applying this identity in each slot intertwines B with one quarter
of the operator in (9), including repeated exponents and every zero
slot. This proves (8). The script also checks every coefficient in
(9) by direct lowering of the 34 original rows, independently of
this formal-log explanation.

For reference, the Dirichlet mean-zero operator with parameters
alpha_i=1/2 is Gan–Röllin–Ross, *Dirichlet approximation of equilibrium
distributions in Cannings models with mutation*, arXiv:1602.07010v3
(8 December 2016), Lemma3.1, equations(3.1)–(3.3), p8
([primary version](https://arxiv.org/pdf/1602.07010v3)). All its
parameters are positive here. We use its operator normalization,
not the half-sized diffusion generator; actual-theta mean zero
comes from the separately justified multiplier calculation above.
For the field (1), (7) at G_E=1 gives the ambient expression

    T_0 X_F = B F-sum_(i,j)t_i t_j partial_ij F-6 sum_i t_i partial_i F,

where T_0 denotes div(w X)/w, not evaluation of (3) at zero energy.
This formula follows as well by substituting (1) into the chart
product rule. Euler's identities for a homogeneous polynomial of
degree r give the last two sums as r(r-1)F and rF. Using (8), r=12,
and B Q=3, respectively, gives

    T_E X_Pbar=-204 Pbar+E sum_i (X_Pbar)_i h(E t_i),
    T_E X_Q=3-14Q+2E[sum_i t_i^2 h(E t_i)-Q sum_i t_i h(E t_i)].  (10)

Thus the natural Pbar-gradient has no independent polynomial
divergence at a zero of Pbar. That is the specific weakness tested.

### Two algebraic zeros and the full-kernel responses

Put s_m(q)=mq+12-m and t_m(q)=(q^m,1^(12-m))/s_m(q). For m=1,4,
write H_m(q)=Pbar(q^m,1^(12-m))=N_m(q)/d_m. The exact coefficients,
in increasing order, are

    d_1=1140694410240000,
    N_1=(1485,-2562,9415,-9996,6795,-2002,-63);
    d_4=501905540505600000,
    N_4=(-3717,287497,-3221575,10631299,-5542978,-29318198,
         69213634,-63981834,29038487,-6214019,451605,13111,-1632).

These are reconstructed directly from L938's rows by

    H_m(q)=sum_alpha c_alpha/[F_alpha binomial(12,m)]
                       sum_(I subset {1,...,12}, |I|=m) q^(sum_(i in I)k_i),
    F_alpha=product_i (2k_i)!.

The subsets are of labelled slots. No extra multinomial is inserted.
The two-block failures recorded in L941 motivated the choices, but
its global root census is not a premise: only the following local
root and derivative enclosures are used and independently verified.

Let r_1,r_4 be the unique roots in the respective rational intervals

    J_1=[4005736209821/2199023255552,
                         2002868104911/1099511627776],
    J_4=[595384720506775/4503599627370496,
                         74423090063347/562949953421312].

Both numerator polynomials have positive value at the left endpoint
and negative value at the right endpoint, and their derivatives are
strictly negative throughout these intervals. Therefore the
intermediate value theorem and strict decrease prove existence,
uniqueness and simplicity. J_1 is contained in (3/2,2), while J_4
is contained in (541/4096,271/2048). These specifications define
exact real algebraic numbers, not rational midpoint substitutions.

Fix E=1/4. At t=t_m(r_m), Pbar(t)=0 and all coordinates are positive.
Euler's identity and the two-block derivative convention give

    A_m := (T_E X_Pbar)(t_m(r_m))
         = E r_m H_m'(r_m)/s_m(r_m)^12
                    *[h(E r_m/s_m(r_m))-h(E/s_m(r_m))],
    B_m := (T_E X_Q)(t_m(r_m)).                                  (11)

The exact-rational full-kernel enclosures proved below give

| quantity | lower bound | upper bound |
|---|---:|---:|
| h(E r_1/s_1)-h(E/s_1) | -187/1000 | -186/1000 |
| h(E r_4/s_4)-h(E/s_4) | 298/1000 | 299/1000 |
| A_1 | 8.00 * 10^(-26) | 8.01 * 10^(-26) |
| A_4 | -1.18 * 10^(-26) | -1.17 * 10^(-26) |
| B_1 | 1779/1000 | 1780/1000 |
| B_4 | 1445/1000 | 1446/1000 |

All table endpoints are exact rationals; the inequalities are weak
enclosures with strict margins from zero. These are full-kernel
values, not a monotonicity assumption about h or sampled polynomial
approximations. In particular A_1>0>A_4 and B_1,B_4>1.

### Boundary limit and the exact dual combination

At a vertex e_i, Pbar=0: every original row has at least three
positive exponent slots. Both X_Pbar and X_Q vanish there. By (7)
the residual has a continuous boundary extension, and (10) gives

    D_E(e_i)=0, (T_E X_Pbar)(e_i)=0, (T_E X_Q)(e_i)=-11.          (12)

If (5) holds with a single positive epsilon at all interior points,
its vertex limit also satisfies that same inequality. At energy 1/4
the radial and scalar columns vanish at all three selected points.
Define the following exact real weights, using (11):

    w_1=-A_4, w_4=A_1,
    w_vertex=((-A_4)B_1+A_1 B_4)/11.                             (13)

All are strictly positive. These expressions, with the specified
algebraic roots and full theta functions, are exact coefficients;
they are not rational approximations chosen to almost annihilate
columns. Their positivity is certified by the rational bounds above.
Equations (11)–(13) give identically

    w_1 A_1+w_4 A_4=0,
    w_1 B_1+w_4 B_4-11 w_vertex=0.

Hence the positive combination of (5) at these two interior points
and the vertex limit has left side zero for every c,d,a. Its right
side is epsilon(w_1+w_4+w_vertex)>0, a contradiction. The dual
annihilates the two field columns in (2) only. Extra field columns
are not annihilated by this argument.

### Exact finite verification and error allowances

Reproduction command:

    python3 scripts/heat/l938-simplex-gradient-obstruction-65.py

The complete certificate is
`scripts/heat/l938-simplex-gradient-obstruction-65.json`. It records
input hashes, all row reconstructions, all lowering coefficients,
root endpoints and their polynomial values, every derivative Bernstein
coefficient, all four kernel/derivative evaluations and tails, exact
dual expressions, outward rational bounds, checks and failures.
All 21 recorded checks pass with no failures. They validate the
finite algebra and displayed inequalities; the chart, boundary and
integral arguments are the analytic proof above.

For completeness the rational enclosure algorithm and its bounds
are specified here. Starting from the two sign-changing intervals
[3/2,2] and [541/4096,271/2048], perform exactly forty rational
bisections preserving the endpoint signs. To certify the derivative
sign, convert N_m'(l+(r-l)y) to the Bernstein basis on 0<=y<=1.
If its power coefficients are b_j and its degree is n, its Bernstein
coefficients are sum_(j<=i) b_j binomial(i,j)/binomial(n,j). Every
one is negative in the saved record. The nonnegative Bernstein
basis functions sum to one, proving the stated whole-interval sign.

All subsequent operations enclose rational intervals outward on the
dyadic grid 2^(-160). Bounds on a square root use integer square
roots after multiplying by 2^320, with the upper integer increased
by one; exact squaring checks both endpoints. Pi is enclosed using
Machin's identity pi=16 arctan(1/5)-4 arctan(1/239) and one hundred
terms of each alternating arctangent series, with the next term as
error bound. The identity follows from tan(4 arctan(1/5))=120/119
and tan(4 arctan(1/5)-arctan(1/239))=1, with the angle in (0,pi/2).

For exp(x), x>=0, divide x by a power of two until y<=1/8. Sum
the positive Taylor series through degree 64. The remaining sum is
at most

    (y^65/65!)/(1-y/66).

Repeated interval squaring restores exp(x); negative arguments use
reciprocals of positive intervals. Monotonicity gives interval
endpoint bounds. These steps use only rational operations and their
explicit remainders. No library exponential or square-root accuracy
assumption enters.

For u=sqrt(x), with 0<u<=1/4 for all four enclosures, set
z_n=pi n^2 exp(2u). Direct differentiation of L019's normally
convergent series gives

    K(u)=exp(u/2) sum_(n>=1)(8z_n^2-12z_n)exp(-z_n),
    K'(u)=exp(u/2) sum_(n>=1)(-16z_n^3+60z_n^2-30z_n)exp(-z_n).

Retain n=1,2,3,4. Since 3n^2<=z_n<=8n^2, exp(u/2)<2 and
exp(3)>20, the absolute summands are bounded respectively by
1216 n^4 20^(-n^2) and 24544 n^6 20^(-n^2). The inequality exp(3)>20
already follows from its positive Taylor polynomial through degree
eight; exp(1/2)<2 is also enclosed by the stated algorithm. For n>=5
successive majorants have ratio at most 3/20^11, using (6/5)^6<3.
Thus the entire omitted tails are bounded by

    T_K =1216*5^4/[20^25(1-3/20^11)],
    T_K'=24544*5^6/[20^25(1-3/20^11)].

The K tail is nonnegative by L019 and lies in [0,T_K]; the derivative
tail lies in [-T_K',T_K']. Each enclosed K is strictly positive, so
division gives a valid bound h(x)=K'(sqrt(x))/(2sqrt(x)K(sqrt(x))).
Finally (11) and (10) are evaluated by outward rational operations
over the entire algebraic root intervals. This proves the table
without asserting that a midpoint is a root or omitting any theta term.

The identities (4), (7) and the Dirichlet operator are local
specializations of known calculus and source methods. The finite
two-field obstruction is local progress on the approved attempt;
the saved literature search does not certify originality. It gives
no evidence of a full-class dual obstruction and does not authorize
enlarging the degree, energy interval or multiplier class.

## Mathlib

Full coverage of this actual-theta weighted-simplex specialization
and its two-field obstruction has not been checked; availability
is unknown. Supporting Dirichlet, divergence, formal-log and interval
arithmetic coverage also has not been checked here. The rational
script is an explicit finite certificate, not a Lean formalization
or an independent verification of the Python runtime.
