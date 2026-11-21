# L842 — A negative second-ray minor for the dyadic cubic product

## Hypotheses

Let P(w)=1+2w+2w^2+w^3 and
\[
 F_M(z)=\prod_{j=0}^{M-1}P(2^{-j}z),\qquad
 F(z)=\lim_{M\to\infty}F_M(z).
\]
The limit is locally uniform, as established in the analytic part of
L841. Let a_n=[z^n]F(z) be ordinary Taylor coefficients, with a_n=0
for n<0, and define
\[
 D_{(r,2)}=\det[a_{2+j-i}]_{0\le i,j<r}\quad(r\ge1).
\]
No factorial normalization, exponential factor, strict sign assumption,
PF closure or Xi realization is imposed.

## Conclusion

The approved all-rank second-ray inequality is false for this product:
\[
 \boxed{D_{(5,2)}=-\frac{1409024}{2966607}<0.}          \tag{1}
\]
Thus this exact infinite-tail model cannot have nonnegative solid minors
on every positive shift at every rank. This rejects this model's
all-shift ansatz only. It neither refutes RH nor excludes other infinite
products. L841's nonnegative first ray is compatible with (1); its
independent full audit remains pending. The independent analytic,
indexing and exact arithmetic audit of this specialization passed on
6 November 2026, at precisely the scope documented below.

## Proof

### Analytic scope and exact coefficient equations

Only the analytic product setup in L841 is needed, not its first-ray
sign conclusion or L840's finite signs. To check that analytic input
at the scope used here, for each R>0 the sum of compact deviations is
bounded by
\[
 \sum_{j\ge0}\sup_{|z|\le R}|P(2^{-j}z)-1|
 \le 4R+\frac83R^2+\frac87R^3<\infty.
\]
The named compact-product theorem therefore gives an entire limit
and F(0)=1. The source is C. McMullen, *Advanced Complex Analysis*,
Harvard Math213a notes, 2 December 2025,
[primary PDF](https://people.math.harvard.edu/~ctm/home/text/class/harvard/213a/25/html/home/course/course.pdf),
compact-product criterion preceding Theorem3.1, p.80;
Cauchy formula Theorem1.4, pp.10–11, derivative formula (1.2), p.12,
and coefficient bound, p.13. This check isolates the
needed analytic input without claiming a full independent audit of
L841. No universal product or Cauchy theorem is reproved.

For M>=2 the finite products satisfy F_M(z)=P(z)F_(M-1)(z/2).
Taking their locally uniform limits gives
\[
 F(z)=P(z)F(z/2).                                    \tag{2}
\]
Since F(0)=1, its reciprocal H(t)=1/F(-t) is holomorphic on some
disk about zero. A unit-disk nonvanishing assertion is unnecessary
for the following finite coefficient calculation. On a sufficiently
small disk (2) implies
\[
 P(-t)H(t)=H(t/2).
\]
Write H(t)=sum_(n>=0) h_n t^n, with h_0=1 and negative indices zero.
Multiplying these convergent Taylor series gives, for every n>=1,
\[
 (1-2^{-n})h_n=2h_{n-1}-2h_{n-2}+h_{n-3}.            \tag{3}
\]
The divisor 1-2^(-n) is strictly positive. Thus these are exact rational
coefficients of the infinite product's reciprocal, not approximations
from a finite product. The values needed here are
\[
 (h_0,\ldots,h_6)=
 \left(1,4,8,\frac{72}{7},\frac{64}{7},
             \frac{1280}{217},\frac{52736}{13671}\right). \tag{4}
\]
For completeness, the successive recurrence evaluations are
\[
\begin{aligned}
 h_1&=2/(1/2)=4, &
 h_2&=(8-2)/(3/4)=8,\\
 h_3&=(16-8+1)/(7/8)=72/7, &
 h_4&=(144/7-16+4)/(15/16)=64/7,\\
 h_5&=(128/7-144/7+8)/(31/32)=1280/217, &
 h_6&=(2560/217-128/7+72/7)/(63/64)=52736/13671.
\end{aligned}
\]

### The rectangle and the sign

We import the universal Jacobi–Trudi identities from I. G. Macdonald,
*Symmetric Functions and Hall Polynomials*, second edition, Oxford
(1995), [primary book PDF](https://math.berkeley.edu/~corteel/MATH249/macdonald.pdf),
I.2 (2.4)–(2.6), (2.9)/(2.9'), pp.20–23, and I.3 (3.4)/(3.5),
pp.41–42. They use e_0=h_0=1, negative subscripts zero and
H(t)E(-t)=1. They are polynomial identities and permit complex
specialization without any positivity hypothesis or division by a
solid minor.

For each finite F_M, take its 3M elementary variables
2^(-j), 2^(-j)exp(i*pi/3), 2^(-j)exp(-i*pi/3), 0<=j<M.
Their elementary generating function is exactly F_M since
P(w)=(1+w)(1+exp(i*pi/3)w)(1+exp(-i*pi/3)w).
Use the partition lambda=(r,r), whose conjugate has r parts all equal
to 2. The dual formula is the r-by-r determinant with entries
e_(2-i+j), 1<=i,j<=r. The ordinary formula is the 2-by-2 determinant
with rows (h_r,h_(r+1)) and (h_(r-1),h_r). The one-based to zero-based
index change gives precisely a_(2+j-i), with no transpose sign or
factorial. Thus for each finite M and every fixed r>=1,
\[
 \det[a_{2+j-i}^{(M)}]
     =(h_r^{(M)})^2-h_{r-1}^{(M)}h_{r+1}^{(M)},
 \qquad h_n^{(M)}=[t^n]1/F_M(-t).                    \tag{5}
\]

To pass (5) to the limit, choose a small closed disk about zero on
which F(-t) is nonzero. Uniform convergence and its positive minimum
modulus imply uniform convergence of 1/F_M(-t) to 1/F(-t) on that
disk, for all sufficiently large M. The cited Cauchy coefficient bound
gives convergence of each fixed a_n^(M) and h_n^(M). A fixed finite
determinant is a polynomial in finitely many coefficients, so (5)
passes to
\[
 D_{(r,2)}=h_r^2-h_{r-1}h_{r+1}.                    \tag{6}
\]
Here r is fixed during the limit; no uniform-in-r statement, exchange
of rank limits, positivity closure or nonzero-minor assumption occurs.
This is an application of the imported identity, not a new proof of it.

At r=5, (4) and (6) give
\[
\begin{aligned}
 D_{(5,2)}
 &=\frac{1638400}{47089}-\frac{3375104}{95697}\\
 &=\frac{1638400\cdot63-3375104\cdot31}{2966607}
   =-\frac{1409024}{2966607}<0.
\end{aligned}
\]
Both numerator and denominator signs are exact integers; no decimal
threshold or unbounded-rank inference is used. This proves (1).

### Independent finite arithmetic route and certificate

Equation (2) also yields, with p_1=2,p_2=2,p_3=1,
\[
 (1-2^{-n})a_n=\sum_{k=1}^{\min(3,n)}p_k2^{-(n-k)}a_{n-k}.
\]
It gives a_0,...,a_5 equal to h_0,...,h_5 in (4), and
a_6=38848/13671. Hence the original rank-five matrix is exactly
\[
 \begin{pmatrix}
 8&72/7&64/7&1280/217&38848/13671\\
 4&8&72/7&64/7&1280/217\\
 1&4&8&72/7&64/7\\
 0&1&4&8&72/7\\
 0&0&1&4&8
 \end{pmatrix}.
\]
The script `scripts/dyadic-cubic/second_ray_exact.py` evaluates its
complete 120-term Leibniz sum over rational numbers and obtains (1),
independently of computing (6). It also checks reciprocal coefficient
identities through degree 6 and agreement of the two arithmetic routes
for ranks 1 through 5. All five grouped checks pass, with no failures.
The smaller ranks have exact values 8,160/7,1600/49,34816/1519;
these finite positive samples are not used to claim all-rank positivity.
The proof above, not a certificate preview, supplies the analytic and
algebraic justifications for this finite arithmetic.

Reproduce from the active notebook with
`python3 scripts/dyadic-cubic/second_ray_exact.py`.
Full coefficients, matrices and every signed permutation term are in
`scripts/dyadic-cubic/second-ray-exact-certificate.json`.
The achieved value is negative, while the proposed required lower bound
was zero. The coefficient method therefore settles the approved test
negatively and needs no pole asymptotics or remainder estimate.

### Independent audit, 6 November 2026

The audit independently checked the compact-deviation sum, F(0)=1,
and the limit in (2). Choose rho>0 with F(-t) nonzero on the closed
disk |t|<=rho, and put m=min|F(-t)|>0 there. Uniform convergence
gives |F_M(-t)|>=m/2 for sufficiently large M and
\[
 \sup_{|t|\le\rho}|1/F_M(-t)-1/F(-t)|
 \le 2m^{-2}\sup_{|t|\le\rho}|F_M(-t)-F(-t)|\longrightarrow0.
\]
The cited Cauchy bound gives fixed-coefficient convergence. This uses
neither the full unit reciprocal disk nor L841's first-ray signs.
For lambda=(r,r), the ordinary Jacobi–Trudi matrix has size two;
the conjugate partition (2^r) gives size r. Their indices are exactly
those of (5). Negative coefficients remain zero, and specialization
at complex variables imposes no order or positivity condition.
Both (2) and P(-t)H(t)=H(t/2) reproduce the displayed recurrences;
their divisors are nonzero for n>=1. No determinant division occurs
in this argument.

For an independent coefficient computation, the finite polynomial
identity E_M(z)=prod_l(1+x_l z) gives
\[
 n a_n^{(M)}=\sum_{m=1}^n(-1)^{m-1}p_m^{(M)}a_{n-m}^{(M)},
 \qquad p_m^{(M)}=\sum_l x_l^m.
\]
This finite identity follows simply by multiplying E_M by its formal
logarithmic derivative sum_l x_l/(1+x_l z) and comparing coefficients;
it involves no analytic logarithm or exchange of infinite series.
For these variables the unscaled power sum is
c_m=1+2cos(m*pi/3), the periodic integer sequence with residues
(3,2,0,-1,0,2) for m=0,...,5 modulo 6. At each fixed m>=1,
\[
 p_m^{(M)}=c_m\sum_{j=0}^{M-1}2^{-jm}
 \longrightarrow p_m=\frac{c_m}{1-2^{-m}}.
\]
Pass through the finite sum using the already justified convergence
of a_n^(M). For m=1,...,6 the exact limits are
(4,0,-8/7,0,64/31,64/21). The resulting triangular equations give
the displayed a_0,...,a_6 without using their self-similarity recurrence.
Triangular inversion of F(-t)H(t)=1 then gives every displayed h_n:
\[
 h_n=-\sum_{k=1}^n(-1)^k a_kh_{n-k}\quad(n>=1).
\]
All six equations of each original recurrence and all seven inverse
coefficient equations were checked exactly against these independent
values.

The independent script `scripts/dyadic-cubic/audit_second_ray_exact.py`
also evaluates each matrix by rational Gaussian elimination with row
interchanges when needed. Its pivot divisions are only by explicitly
nonzero rational pivots in these finite matrices, and are unrelated
to division by a possibly vanishing symbolic solid minor. Every saved
permutation is checked for exhaustive, nonduplicated coverage. Each
signed term is recomputed with its sign determined by permutation
cycles rather than the original generator's inversion counts; the
full sums agree with elimination and (6). All 153 saved terms are
inspected, including all 120 rank-five terms. All smaller displayed
values, the duplicated rank-five record and the original grouped flags
also agree. Replaying the original generator reproduces the retained
certificate byte for byte. The complete audit report, including each
term and check, is `scripts/dyadic-cubic/second-ray-independent-audit.json`.
Reproduce with `python3 scripts/dyadic-cubic/audit_second_ray_exact.py`.
All 200 checks pass, with no failures; the actual value is (1), strictly
below the required bound zero. This validates the local obstruction,
without asserting any new theorem beyond the checked methods or
extending the audit to L841's full conclusion or actual Xi.

## Mathlib

Full matching Mathlib coverage of this product, the rectangular identity
and its combined negative-minor specialization has not been checked;
no absence claim is made. The classical imported identities and analytic
theorems are cited above. Exact rational coefficient extraction and the
Leibniz determinant sum verify the finite specialization. Classification
is REPRODUCTION of covered methods, not a certified original theorem.
The local informative negative changes the route decision only for this
specified dyadic model. Actual-Xi signs and realization remain open.
