# Lemma 770: an explicit uniform fourth-order complete-theta comparison

## Hypotheses

Let u>=0 and let m>=16000 be an integer. Use L019's complete kernel

\[
 K(v)=\sum_{n\ge1}(8\pi^2n^4e^{9v/2}-12\pi n^2e^{5v/2})
                         e^{-\pi n^2e^{2v}},\qquad v\ge0,
\]

and its full first summand

\[
 x(v)=\pi e^{2v},\quad H(v)=8\pi e^{5v/2-x(v)},\quad
 B(v)=H(v)(x(v)-3/2),\quad F_0(v)=H(v)x(v).
\]

For F equal to K, B or F_0, retain the factorial convention

\[
 C_m(F;u)=\frac1{(m-1)!}\int_0^\infty t^{m-1}F(u+t)\,dt,
 \qquad S_{4,m}(F;u)=\det[\partial_u^{i+j}C_m(F;u)]_{i,j=0}^3.
\]

Use L769's exact signed integral, polynomial P, polynomials q_j,
and lower factor S_(4,m)(B;u)>(19/72)S_(4,m)(F_0;u)>0.
L769 and the present fixed-order result passed the separate step401
conceptual audit recorded below.

## Conclusion

For every integer m>=16000 and every real u>=0,

\[
 \frac{|S_{4,m}(K;u)-S_{4,m}(B;u)|}{S_{4,m}(B;u)}
 <2^{-117}<\frac12.                                      \tag{1}
\]

In particular S_(4,m)(K;u)>S_(4,m)(B;u)/2>0 on this entire
domain. The onset 16000 is a deliberately coarse sufficient value;
no optimality, smaller-onset failure or result for other orders is claimed.
All theta terms, coalescing integration points, mixed small/large
heights and u depending on m are included. No numerical grid or
pointwise large-m asymptotic is an input.

This is fixed-order smoothing control, not all-degree positivity of Xi,
unshifted Jensen hyperbolicity, an exceptional-coefficient transfer or
an RH candidate. It is an explicit quantitative development of the
known full-first-term/cumulant comparison program. Relevant precedent
is John Nuttall, *Basic Wronskians in the Riemann Hypothesis*, author
report, Theorem3.1, Section3/(3.2)–(3.12), printed pp.5–6,
https://publish.uwo.ca/~jnuttall/basicRH.pdf; and *Cumulants, the
Riemann Hypothesis, and Similar Problems*, author manuscript,
Sections4.2–4.3, pp.9–12, and Theorem5.6/Section5.5.3, pp.17–19,
https://publish.uwo.ca/~jnuttall/cumanal_a.pdf. The latter theorem is
for a different Theta1 kernel. These are method comparisons, not
imports of a full-B uniform bound or of the source's conjectures.
The pre-existing step398 assessment found no matching effective theorem
in the inspected sources; that search is not an originality certificate.
The explicit perturbation and localization bounds below are therefore
necessary, rather than supplied by citation. Standard Newton divided
differences are used with their elementary justification, solely to pay
the coalescing-point cancellation.

## Proof

### 1. The exact error and a positive reference measure

Put p=m-4. L769 gives, on 0<t_1<t_2<t_3<t_4, with v_l=u+t_l,
x_l=pi exp(2v_l) and H_l=H(v_l),

\[
 W=\left(\prod_l t_l^p H_l\right)\Delta(t)>0,
 \qquad Z=\int W\Delta(x)\prod_lx_l\,dt>0,
\]

where Delta(z)=prod_(i<j)(z_j-z_i). Define

\[
 f_j(x)=\sum_{n\ge1}n^2e^{-(n^2-1)x}q_j(n^2x),\quad
 E(x)=\det[f_j(x_l)]_{j=0,\ldots,3;l=1,\ldots,4}
                           -\Delta(x)P(x).
\]

The exact relative error and the full-base lower bound imply

\[
 \frac{|S_{4,m}(K;u)-S_{4,m}(B;u)|}{S_{4,m}(B;u)}
 \le\frac{72}{19}\,\mathbb E_\nu
          \frac{|E(x)|}{\Delta(x)\prod_lx_l},               \tag{2}
\]

where nu is the probability measure with density
Z^(-1)W Delta(x) prod_l x_l on the ordered region. L769 justifies
the differentiations, six required derivatives, complete theta sum,
absolute convergence and determinant-integral formula. Below we bound
the integrand of (2) uniformly and then bound the probability of its
low-height region. No favorable cancellation of the numerator is assumed.

### 2. Compact reciprocal coordinates retain the alternant

Set y_l=1/x_l and, for 0<y<=1/3, set

\[
 h_j(y)=y^4q_j(1/y),\qquad
 r_j(y)=\sum_{n\ge2}n^2e^{-(n^2-1)/y}y^4q_j(n^2/y).
\]

Extend r_j and its first three derivatives to zero by zero; the
bounds in the next section justify this C^3 extension. The four h_j are

\[
\begin{aligned}
 h_0&=y^3-(3/2)y^4,\\
 h_1&=-y^2+(5/2)y^3,\\
 h_2&=y-(9/2)y^2+(5/2)y^3,\\
 h_3&=-1+(15/2)y-(23/2)y^2+(5/2)y^3.
\end{aligned}                                             \tag{3}
\]

There are six pairs of nodes, so
Delta(x)prod_l x_l=Delta(y)prod_l y_l^(-4), with positive
sign. Column scaling gives the exact identity

\[
 \frac{E(x)}{\Delta(x)\prod_lx_l}
 =\frac{\det[(h_j+r_j)(y_l)]-\det[h_j(y_l)]}{\Delta(y)}.
                                                               \tag{4}
\]

For any four distinct real nodes, Newton column elimination replaces
the evaluation determinant divided by Delta(y) with the determinant
whose kth column, k=0,1,2,3, consists of the divided differences
g_j[y_1,...,y_(k+1)]. Indeed the Newton interpolation basis has kth
polynomial prod_(i=1)^k(y-y_i), whose triangular evaluation matrix
has determinant Delta(y). For g in C^3, repeated Rolle's theorem
applied to g minus its interpolation polynomial on k+1 nodes gives

\[
 |g[y_1,\ldots,y_{k+1}]|\le\frac1{k!}\sup_I|g^{(k)}|,    \tag{5}
\]

where I contains the nodes. For k=0 this is evaluation; for k>0
the interpolation polynomial's kth derivative is k! times its leading
coefficient, the divided difference. This also proves the bound for
arbitrarily close nodes; continuity gives their confluent limits.

Suppose the four h_j have divided differences bounded by H_* and
the four r_j by R_* on I. Expand the determinant difference by
its nonempty subsets of perturbation columns, and then each determinant
by its 4! permutation terms. Equations (4)–(5) give

\[
 \left|\frac{E(x)}{\Delta(x)\prod_lx_l}\right|
 \le24\sum_{k=1}^4\binom4k H_*^{4-k}R_*^k.               \tag{6}
\]

There is no inverse minimum separation in this bound.

### 3. Complete theta derivative bounds, with explicit constants

The absolute coefficient sum of each q_j is at most 23. Thus from
(3), for k<=3 and 0<=y<=1/3,

\[
 \frac{|h_j^{(k)}(y)|}{k!}\le6\cdot23<2^8=:H_* .         \tag{7}
\]

Here every contributing monomial has degree at most four and
binom(b,k)<=6, while y^(b-k)<=1 when b>=k.

For b in {0,1,2,3,4}, a=n^2-1 and n>=2, write
g(y)=y^b exp(-a/y). Its first three derivatives, after removing the
common exponential, are

\[
\begin{aligned}
 g'e^{a/y}&=b y^{b-1}+a y^{b-2},\\
 g''e^{a/y}&=b(b-1)y^{b-2}+(2b-2)a y^{b-3}+a^2y^{b-4},\\
 g'''e^{a/y}&=b(b-1)(b-2)y^{b-3}
 +(3b^2-9b+6)a y^{b-4}+(3b-6)a^2y^{b-5}+a^3y^{b-6}.
\end{aligned}                                             \tag{8}
\]

For 0<y<=1/3, all displayed powers are bounded in absolute value
by y^(-6). The third-derivative coefficient sum is at most
24+18n^2+6n^4+n^6<=4n^6; the same bound covers derivatives
of orders zero, one and two. Each monomial of r_j has coefficient
c_(jd)n^(2d+2), d<=4, and b=4-d. Therefore, putting x=1/y>=3,

\[
 |r_j^{(k)}(y)|\le92\sum_{n\ge2}n^{16}x^6e^{-(n^2-1)x},
 \qquad 0\le k\le3.                                    \tag{9}
\]

For a>=3, maximization of x^6 exp(-a x/2) on x>0 gives
(12/(ae))^6<=4^6. Hence the right side of (9) is at most

\[
 92\,2^{12}\sum_{n\ge2}n^{16}e^{-(n^2-1)x/2}.
\]

At x>=3 the ratio of consecutive summands is bounded by
(3/2)^16 exp(-15/2)<657/1000<2/3. To verify the numerical
inequality without rounding, use e>27/10, obtained from the positive
exponential series through degree five, and (27/10)^7>1000.
The complete infinite series is consequently bounded by three times
its n=2 term. Since 92*2^12*3*2^16<2^37, we have

\[
 |r_j^{(k)}(y)|<2^{37}e^{-3x/2},\qquad x=1/y\ge3.        \tag{10}
\]

The termwise derivatives in (8) are uniformly summable on [0,1/3]
after zero extension, as (9) is bounded by the summable series at
x=3 after the preceding split. Each individual term and each of
its first three derivatives tends to zero at zero. Uniform convergence
therefore proves the asserted C^3 extension and termwise differentiation;
(10) also shows all these derivative limits are zero. No theta term
has been truncated.

Globally use R_*=2^37 in (6). Since H_*+R_*<2^38,

\[
 |E(x)|/(\Delta(x)\prod_lx_l)<24(2^{38})^4<2^{160}       \tag{11}
\]

for every ordered x_l>=pi. If all four x_l>=A:=128, their reciprocal
nodes lie in [0,1/128]. Equations (5) and (10), using e>2, permit
R_*=2^37 exp(-192)<2^(-155). In (6), R_*<=H_*, so

\[
 |E(x)|/(\Delta(x)\prod_lx_l)
 \le24\cdot15 H_*^3R_*<2^{-122}<2^{-120}.                \tag{12}
\]

The strict bounds hold regardless of relative heights or their
separation. Points on a diagonal have zero integration measure, and
the divided-difference formulation remains bounded as they coalesce.

### 4. Uniform suppression of a low coordinate

Write x0=pi exp(2u)>=pi. Changing variables t_l=(1/2)log(x_l/x0)
in the positive reference measure gives, up to a positive constant,

\[
 \prod_{l=1}^4\left[\log(x_l/x0)^p x_l^{5/4}e^{-x_l}\right]
 \prod_{i<j}(\log x_j-\log x_i)(x_j-x_i),\qquad x_l\ge x0.
                                                               \tag{13}
\]

For this calculation H_l x_l dt_l=H_l dx_l/2 and
H_l is a constant times x_l^(5/4) exp(-x_l); Delta(t) is
2^(-6)Delta(log x). The omitted powers of two and other constants
cancel on normalization. The density is symmetric and nonnegative,
so pass to the unordered region with the compensating factor 4!.
All integrals are finite by the original decay. The probability of
min_l x_l<=A is unchanged.

If x0>=A this event has probability zero (the boundary has measure
zero). Otherwise fix any three coordinates a_1,a_2,a_3>=x0.
The conditional density of the remaining coordinate x, up to its
normalization, is

\[
 \phi(x)=\log(x/x0)^p x^{5/4}e^{-x}
            \prod_{i=1}^3|x-a_i|\,|\log x-\log a_i|,
 \quad x\ge x0.                                          \tag{14}
\]

Its integral is positive and finite. Among
[2A,3A], [4A,5A], [6A,7A], [8A,9A], choose an interval I
whose distance from each a_i is at least A/4. Such an interval
exists: expanding each of the four intervals by A/4 leaves them
pairwise disjoint, and each of three a_i can belong to at most one
expanded interval. The interval I has length A and lies above x0.

For any x in [x0,A] and z in I,

\[
 \frac{|x-a_i|}{|z-a_i|}\le37.                            \tag{15}
\]

Indeed |x-z|<=9A and |z-a_i|>=A/4. Also
|log z-log a_i|>=1/37. If a_i>=z, use
log(a_i/z)>=log(1+1/36)>=1/37; if a_i<z, use
-log(1-(z-a_i)/z)>=(z-a_i)/z>=1/36. Thus

\[
 \frac{|\log x-\log a_i|}{|\log z-\log a_i|}
 \le1+37\log(9A/\pi)<223.                               \tag{16}
\]

For the last strict inequality, pi>3 gives 9A/pi<384 and
e^6>(27/10)^6>384. Each pair of factors in (15)–(16) therefore
costs less than 37*223=8251<2^14, and three pairs cost less than 2^42.

Let L=log(A/x0). For x0<A, L>0 and

\[
 \frac{\log(x/x0)}{\log(z/x0)}
 \le\frac{L}{L+\log2}<\frac89.                           \tag{17}
\]

Here L<=log(128/pi)<4, since e^4>(27/10)^4>128/3, and
log2>1/2 follows from e<4. Moreover x^(5/4)<=z^(5/4) and
exp(z-x)<=exp(9A)<2^2304, again by e<4. Combining these estimates,

\[
 \phi(x)\le2^{2346}(8/9)^p\phi(z)
 \quad(x\in[x0,A],\ z\in I).                            \tag{18}
\]

Integrating in z over its interval of length A, then in x over an
interval of length at most A, proves

\[
 \int_{x0}^A\phi(x)\,dx
 \le2^{2346}(8/9)^p\int_I\phi(z)\,dz.
\]

Divide by the full conditional integral. Integrating over the fixed
three coordinates and applying the union bound to the four coordinates
gives, with no independence assumption,

\[
 \nu\{\min_lx_l\le128\}\le2^{2348}(8/9)^p.               \tag{19}
\]

One can equivalently multiply the conditional integral inequality by
the other-coordinate factors in (13) and use Tonelli; no conditional
probability on a diagonal is required. All the bounds are independent
of the conditioning points and x0. Thus mixed configurations and
moving u are included, rather than discarded by a fixed-u limit.

### 5. Explicit onset and conclusion

For m>=16000, p=m-4>=15996=6*2666. The exact inequality
(8/9)^6=262144/531441<1/2 gives from (19)

\[
 \nu\{\min_lx_l\le128\}<2^{2348-2666}=2^{-318}.          \tag{20}
\]

Using (11) on this event and (12) on its complement, (2) is less than

\[
 \frac{72}{19}\left(2^{-120}+2^{160}2^{-318}\right)
 =\frac{72}{19}\left(2^{-120}+2^{-158}\right)
 <2^{-117}<\frac12.
\]

This proves (1). The positive base is L769's result, and multiplying
by it gives the claimed positive complete-K determinant. The proof
is uniform in every integer above the stated onset, not an interpolation
from selected smoothing levels.

### Verification and qualifications

`python3 scripts/cumulant-comparison/uniform-fourth-order-constants-400.py`
checks the polynomial derivative recurrences and all finite rational
constant inequalities used above. Its full certificate is
`scripts/cumulant-comparison/uniform-fourth-order-constants-400.json`.
It does not numerically evaluate an infinite determinant or replace
the analytic proof of (4), (13), or the conditional integral bound.
The elementary estimates 27/10<e<4 and pi>3, elementary calculus,
Newton interpolation/Rolle and finite determinant expansion are the
only supporting standard facts. No additional paper theorem is imported.
The exact kernel and signed integral used here are those of L019 and
L769; the cited source comparisons and fixed r=3 precedent are not premises.
The subsequent step401 review checks this proof and L769 together;
the finite certificate alone does not supply that analytic audit.

### Critical review — 2026-11-04, step401

Accepted with the stated quantifiers and M4=16000. The audit checked
L769's normalization, signed integral and positive lower factor first.
Equation (2) follows by the triangle inequality in the numerator and
that lower factor in the denominator; no signed error is replaced by
a positive integrand without paying its absolute value. The positive
reference measure has finite, nonzero normalizing constant.

In the reciprocal change, each of the six pairs contributes a minus
sign and three powers of each y_l enter the pair denominators.
Together with prod_l x_l this gives precisely prod_l y_l^(-4) and
positive total sign. Multiplying each evaluation column by y_l^4
therefore proves (4) with no missing scale. The Newton transformation
is linear in each function and keeps the same nodes for h_j and r_j.
Consequently the perturbation-column expansion really is (6), even
when nodes are arbitrarily close. Rolle's theorem needs only C^k for
column k; those hypotheses follow from the full-series bounds, not
from a finite theta truncation.

For (9), division of the coarse derivative coefficient bound by n^6
gives 24/n^6+18/n^4+6/n^2+1<=4 for all n>=2; the maximum is at n=2.
Every y-power is at least -6 and y<=1, so the proposed majorant has
the correct direction. After splitting the exponential, the supremum
over x>=3 of each derivative term is bounded by a constant times
n^16 exp(-3(n^2-1)/2). The ratio test used in the proof bounds this
entire series. Uniform convergence of the functions and derivatives
through order three, including their zero extensions, proves C^3
regularity on the closed interval. This checks the infinite-sum
justification and the high-coordinate bound, not just its constants.
The elementary inequalities e>27/10 and e<4 are sufficient throughout;
the upper bound follows already from n!>=2^(n-1) for n>=1 and the
geometric majorant e<3. No decimal enclosure is used.

In (13), H_l x_l dt_l=H_l dx_l/2, confirming exponent 5/4.
The paired Vandermonde factors are nonnegative on the unordered
region, so Tonelli applies. For every fixed triple, the four intervals
expanded by A/4 are pairwise disjoint; at most three are blocked.
The resulting distance lower bound makes both denominators in
(15)–(16) nonzero, even for unbounded conditioning coordinates.
Triangle inequalities then give those two ratios uniformly.
The logarithmic weight comparison uses only x0>=pi and x0<A;
its numerator is zero at x=x0 since p>=15996. The case x0>=A
has zero low-coordinate probability and needs no division by L.

One may avoid conditional probabilities entirely: for each triple,
the comparison to its free interval bounds the low-coordinate
integral by the full one times the same constant. Multiplying by
the nonnegative other-coordinate factors and applying Tonelli gives
the marginal bound. This remains valid when other coordinates
coincide, because those factors are then zero. Four marginal bounds
give (19) without independence or any unproved distributional claim.
All constants are independent of the triple, m and u. This is why
mixed configurations and moving heights are covered.

For every m>=16000, p>=6*2666 and (8/9)^6<1/2 imply (20).
The final expression divided by 2^-117 is exactly
(9/19)(1+2^-38)<1. Thus the claimed strict bound and positivity
hold for every larger integer, including u=0. The replay of
`scripts/cumulant-comparison/uniform-fourth-order-constants-400.py`
passed all 112 exact finite checks; the full final-bound and failure
fields were inspected. The script source and all checks were reviewed
at their finite scope; the analytic arguments above supply the
infinite quantifiers. No mathematical defect or required bound change
was found. No new theorem input or dependency was introduced.

This is acceptance of a relevant local fixed-order input, classified
as reproduction for the audit. It neither certifies originality nor
settles general-order smoothing, exceptional indices or RH.

## Mathlib

Full matching coverage, Newton divided-difference support and the
multivariable integral/probability specialization were not checked.
Availability is unknown, not established absent. This is an informal
analytic proof with an exact finite constant check, not a Lean proof.
