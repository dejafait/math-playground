# Lemma 562: global determinant certificate for the fixed reciprocal model

## Hypotheses

Retain exactly L561's constants and definitions:

    A=2^20, b=1/4, a=A+ib, m=270, r=256,
    P_*(z)=(1-z^2)^m(1-z^2/a^2)(1-z^2/conjugate(a)^2),
    p_*(x)=(1/(2*pi)) integral_R exp(iux)/P_*(iu) du,
    H_k(p;x)=(-1)^(k(k-1)/2) det[p^(i+j)(x)]_(i,j=0)^(k-1).

Use L561's density, regularity, transform identification and negative
first polynomial sign, under their stated hypotheses. The source inputs
for ordered determinants are S. Sra, *On some positivity properties of
the Riemann Xi function*, v2 (29 October 2026), Appendix C.1 Lemma C.1,
printed p.18, and Appendix C.4 Lemma C.6, printed p.21:
https://suvrit.github.io/papers/riem-xi/riem-xi-v2.pdf.
Only those finite Wronskian criteria are used, not its Xi certificate.

The elementary algebra inputs are the standard named Jacobi--Trudi
identity, the semistandard-tableau branching rule for Schur functions,
and the Weyl dimension formula for their specialization at all ones.
Precise reference: I. G. Macdonald, *Symmetric Functions and Hall
Polynomials*, second edition (1995), I.3 (3.1)/(3.4), pp.40--42,
Examples 1/4, pp.44--45, and I.5 (5.9)/(5.12), pp.71--73; tableau
conventions are in I.1, p.5:
https://math.berkeley.edu/~corteel/MATH249/macdonald.pdf.
Their exact forms and required bounds are given below. These finite
polynomial identities allow repeated and complex letters; the partition
is zero-padded to m=270 for the dimension formula. They are known
identities, not new mathematics claimed here.

## Conclusion

For every real x and every integer 1<=k<=256,

    H_k(p_*;x)>0.                                      (1)

Consequently p_* is strictly PF256: for every such k and every pair of
strictly increasing real k-tuples x_1<...<x_k and y_1<...<y_k,

    det[p_*(x_i-y_j)]_(i,j=1)^k>0.                      (2)

Together with L561 this gives a positive even C^542 probability density
whose bilateral transform is 1/P_* on |Re z|<1, satisfying (2), while

    P_*'(A)^2-P_*(A)P_*''(A)<0.                         (3)

Thus these fixed-model properties refute the generic implication
from strict PF256 of a reciprocal density to the first Laguerre sign of
its reciprocal polynomial at every real argument. The point A is outside
the transform strip; no bilateral integral there is asserted. There is
no application to Xi, no RH conclusion, and no higher-polynomial-sign
claim. The separate conceptual audit recorded below verifies this model
certificate and its load-bearing L561 inputs. It does not certify
originality or audit any source claim about Xi itself.

## Proof

### A uniform Schur comparison

For a finite alphabet X define h_n(X) by

    product_(v in X) (1-vt)^(-1)=sum_(n>=0) h_n(X)t^n,
    h_0=1, h_n=0 for n<0.

For a partition lambda of length at most k, padded by zeros, the
Jacobi--Trudi identity states

    s_lambda(X)=det[h_(lambda_i-i+j)(X)]_(i,j=1)^k.     (4)

Equivalently s_lambda is the sum of monomials over semistandard tableaux
of shape lambda: entries weakly increase across rows and strictly
increase down columns. The skew version has the same definition on
lambda/mu. In particular all its coefficients are nonnegative integers.
Splitting an ordered alphabet X,Y according to the entries in X gives
the branching identity

    s_lambda(X,Y)=sum_(mu subset lambda)
                     s_mu(X) s_(lambda/mu)(Y).        (5)

Indeed the boxes with entries in X form a Young subdiagram mu; the
remaining boxes carry a skew tableau with entries in Y. This argument
is a polynomial identity, so (5) holds for complex evaluations too.
The Weyl dimension specialization is

    D_lambda=s_lambda(1,...,1 [m times])
      =product_(1<=i<j<=m)
          (lambda_i-lambda_j+j-i)/(j-i)>0,             (6)

for length(lambda)<=m, with zero padding to m. These named identities
are used only for finite alphabets and finite partitions. Formula (6)
also follows by taking the all-ones limit in the Schur bialternant
formula; it involves no asymptotic in lambda or an infinite alphabet.

If nu is obtained from lambda by a valid removal of one box from row
i<=r, divide the factors in (6). Those with j<i increase by at most

    (i-j+1)/(i-j),

because lambda_j-lambda_i+i-j>=i-j. Those with j>i decrease and remain
positive, because nu is still a partition. The product of the increasing
bounds is i (including i=1), so

    D_nu/D_lambda<=i<=r.

For any subpartition mu of lambda, with l=|lambda|-|mu|, boxes can be
removed successively at outer corners until reaching mu. Consequently

    D_mu/D_lambda<=r^l.                                (7)

There are at most binomial(l+r-1,r-1) such mu: their row deficits form
an r-tuple of nonnegative integers with sum l. A skew tableau with two
available letters has at most 2^l possible fillings. Thus for epsilon>0,

    |s_(lambda/mu)(i epsilon,-i epsilon)|
       <=(2 epsilon)^l.                               (8)

Applying (5), (7), and (8), and extending the finite nonnegative bound
to a series, gives, if 2r epsilon<1,

    |s_lambda(1^m,i epsilon,-i epsilon)/D_lambda-1|
      <=sum_(l>=1) binomial(l+r-1,r-1)(2r epsilon)^l
       =(1-2r epsilon)^(-r)-1.                         (9)

Set d=A-1=1048575 and epsilon=b/d=1/(4d). Bernoulli's inequality gives

    (1-2r epsilon)^r>=1-2r^2 epsilon,
    2r^2 epsilon=32768/1048575<1/2.

It follows from (9) that the relative error is at most

    beta=32768/1015807<33/1000<1,
    theta=1-beta=983039/1015807>0.                      (10)

The evaluation in (9) is real: complex conjugation interchanges the
last two letters, and s_lambda is symmetric, as also follows from (4).
By homogeneity, for the fixed alphabet

    V=(d,...,d [m times], ib,-ib),

every partition of length at most r therefore satisfies

    s_lambda(V)>=theta d^|lambda| D_lambda>0.          (11)

This is uniform in the number of boxes of lambda. In particular it
does not lose control when the spatial variable below tends to infinity.
The empty partition is included; its exact value is 1 and the same
weaker bound applies. No finite-order transform classification is used.

### The causal factor and its derivative determinants

Write e_c(x)=exp(-cx) for x>=0 and e_c(x)=0 for x<0, for Re c>0.
Let convolution always be on R and put

    K=A^2+b^2,
    q=K e_1^{*m}*e_a*e_conjugate(a),
    N=m+1=271.

These convolutions are absolutely convergent and real, since
conjugation exchanges the last two factors. Their absolute values are
bounded by the corresponding convolution with the real parts of their
rates. In particular q is integrable with absolute exponential moments
of orders less than 1. For x>0 expansion of each exponential inside
the finite simplex convolution gives

    q(x)=K exp(-Ax) R(x),
    R(x)=sum_(n>=0) h_n(V) x^(n+N)/(n+N)!.             (12)

To verify the coefficient, write each rate as A-v. A term with powers
n_1,...,n_(m+2) has simplex integral x^(n+N)/(n+N)!, where n=sum n_j;
summing its product of v_j powers gives h_n(V). The interchange follows
from the absolutely convergent exponential series on each compact
simplex. Since |v|<=d,

    |h_n(V)|<=binomial(n+m+1,m+1)d^n.

This bound proves local uniform convergence of (12) and all its
derivatives. In particular R is entire and q is analytic for x>0.
Near zero q(x)=K x^271/271!+O(x^272). Its zero extension is C^270,
with derivatives of orders 0 through 270 vanishing at zero. Those
derivatives decay exponentially times a polynomial at infinity: this
follows either by finite partial fractions in the convolution transform,
whose rates are 1,a,conjugate(a), or by differentiating its finite
exponential-polynomial expression. Thus derivatives through order 255
are in both L1 and L2 on R, with no support-edge delta terms.

For k<=r the binomial triangular change of derivatives under the
factor exp(-Ax) gives

    H_k(q;x)=K^k exp(-kAx) H_k(R;x),   x>0.            (13)

Here each triangular matrix has diagonal 1, so it introduces no sign
or determinant factor. Reverse the rows of the derivative determinant
of R to cancel the sign in H_k. With i,j=0,...,k-1 the resulting matrix
has entries

    M_ij=R^(k-1-i+j)(x)
        =sum_(l>=0) h_(l-i)(V)
                    x^(l+N-k+1-j)/(l+N-k+1-j)!.       (14)

Terms with a negative factorial index mean zero, as obtained by
differentiating a polynomial. For any ordered indices
0<=l_1<...<l_k define lambda_s=l_(k+1-s)-k+s, s=1,...,k.
These form a nonnegative partition. Transposing and reversing both
orders in the first minor gives precisely (4), so

    det[h_(l_s-i)(V)]_(i=0,...,k-1;s=1,...,k)
       =s_lambda(V)>0.                                (15)

For the second minor put L_s=l_s+N-k+1. Since N-k+1>=16,
these are distinct nonnegative integers. Factoring the row and column
powers of x in that minor gives, for every x>0,

    det[x^(L_s-j)/(L_s-j)!]_(s=1,...,k;j=0,...,k-1)
      = x^(sum L_s-k(k-1)/2) / product_s L_s!
          * product_(s<t)(L_t-L_s)>0.                 (16)

Indeed the remaining entries are the falling factorials (L_s)_j,
monic polynomials of successive degrees j. This also treats j>L_s:
both the falling factorial and the derivative entry then vanish.

Apply the finite Cauchy--Binet identity to (14) truncated at l<=J,
then let J tend to infinity. Each matrix entry converges absolutely
by the bound following (12), so the determinants converge. Every
summand in the minor expansion is positive by (15)--(16); in particular
the term l_s=s-1 is positive and appears for J>=k-1. Hence the limit
is strictly positive. This proves

    H_k(q;x)>0      (x>0, 1<=k<=256).                  (17)

There is no unproved cancellation estimate in this limit. The finite
determinant expansions consist of positive terms and converge to the
finite determinant. More quantitatively, let q_0=K e_1^{*m}*e_A*e_A,
so its alphabet in (12) is (d^m,0,0). Replacing (15) by (11) in the
same expansion proves the genuine global comparison

    H_k(q;x)>=theta H_k(q_0;x)>0    (x>0, k<=256).     (18)

This comparison concerns causal derivative determinants on their open
support. It does not apply Lemma C.6 across the support edge of q.

### From the causal factor to all real centers

For |Re z|<1, absolute Fubini in the defining convolutions gives

    integral_R exp(-zx) q(x) dx
       =K/((1+z)^m(a+z)(conjugate(a)+z)).              (19)

Writing check(q)(x)=q(-x), multiply (19) at z and -z. The result is
1/P_*(z). Thus Fourier uniqueness for L1 functions, and continuity,
together with L561's transform identification, give

    p_*(x)=(q*check(q))(x)=integral_R q(t)q(t-x) dt.   (20)

For 0<=i,j<=255 differentiation can be distributed between these two
factors: both have integrable continuous derivatives through order
255. For example use the equivalent integral q(x+u)q(u), differentiate
i times there, and transfer each of the subsequent j derivatives by
integration by parts, or use convolution of the corresponding L1 weak
derivatives. No individual factor is differentiated more than 255
times in the final formula, which is

    p_*^(i+j)(x)=(-1)^j
                  integral_R q^(i)(t)q^(j)(t-x) dt.   (21)

The weak-derivative argument justifies mixed orders up to 510 without
assuming q is globally C^510. Each right side is continuous: the two
factors are L2 and L2 translation is continuous. L561 gives the
classical C^542 representative, so the weak and classical derivatives
agree everywhere. Exponential decay and the zero traces already proved
justify all boundary terms in the alternative integration argument.

On the interval (0,infinity) put f_j=(-1)^j q^(j), j=0,...,k-1.
For every prefix of length l<=k its Wronskian is exactly

    det[f_j^(i)]_(i,j=0)^(l-1)=H_l(q;x)>0.

Sra v2 Lemma C.1 therefore implies

    det[f_i(t_s)]_(i=0,...,k-1;s=1,...,k)>0
                            whenever 0<t_1<...<t_k. (22)

The transpose of this displayed matrix is the source's evaluation
matrix; transposition leaves the determinant unchanged. If an ordered
tuple has a nonpositive entry, the determinant of the zero-extended
functions is instead zero, because that column is zero. We do not
claim a strict Chebyshev criterion at the support boundary.

The column signs in (21) cancel the defining sign of H_k(p_*;x).
The additional row and column signs converting q^(i) to f_i cancel
each other. Expanding the two finite determinants and applying Fubini
gives the Andreief determinant identity, here in ordered form:

    H_k(p_*;x)
      = integral_(t_1<...<t_k)
          det[f_i(t_s)]_(i,s) det[f_j(t_s-x)]_(j,s)
            dt_1...dt_k.                              (23)

The usual 1/k! over R^k disappears on the ordered chamber, since the
product is symmetric in the t_s. Absolute integrability follows by
expanding the finite determinants: each factorized one-variable
integral of |f_i(t)f_j(t-x)| is finite by Cauchy--Schwarz. Thus (23)
does not assume a sign in order to justify its interchange.

For every fixed real x the integrand is nonnegative everywhere on
this chamber. It is strictly positive on the nonempty open set
max(0,x)<t_1<...<t_k, by (22) for both tuples. It is continuous there,
so its integral is strictly positive. This proves (1), including x=0
and both unbounded directions, without joining separate endpoint bounds.

Finally L561 gives p_* in C^542, which exceeds C^(2r-2)=C^510.
Applying exactly Sra v2 Lemma C.6 to (1) proves (2). L561's normalized
first sign is less than -31 and P_*(A)>0, giving (3).

### Verification and scope

The only new fixed-model mathematical claim is the global comparison
and its assembly above. The Schur identities, Cauchy--Binet and Andreief
are known algebraic identities; the last two uses are justified by
finite truncation or absolute integration as specified. The repeated
alphabet, factor normalizations and numerical margin are specialized
here because the inspected finite-order criterion does not itself
certify this model. No new universal theorem is claimed.

`python3 scripts/reciprocal-pf256/global_comparison.py` checks the exact
margin and the dimensional/regularity thresholds in this proof, saving
`scripts/reciprocal-pf256/global-comparison-certificate.json`.
All nine scalar checks passed; the full bounds and empty failure list
were inspected. These checks do not independently audit (4)--(23); the proof
of global positivity is analytic, not a sample of determinants.
These analytic points and the retained L561 inputs received the separate
conceptual audit below. The script's historical "unaudited" scope and
L561's partial-certificate output describe what those scripts establish;
neither script purports to decide the global analytic claim.

### Independent conceptual audit — 31 October 2026

The audit used the preexisting SPECIALIZE coverage in
`drafts/literature/2026-10-31-l561-l562-global-certificate-audit-coverage.md`.
It checked (4)--(23), rather than inferring their validity from the
scalar certificate. No mathematical failure was found. The following
details make the uniformity, limits and signs explicit.

For (7), a valid row-i removal changes each earlier-row factor in (6)
from D to D+1, where D=lambda_j-lambda_i+i-j>=i-j. Its ratio is at
most (i-j+1)/(i-j). The product over j<i telescopes to i. Later-row
factors decrease but stay strictly positive, including after a last
box is removed. Every intermediate partition between lambda and mu
still has at most r rows. Thus the bound r^l applies to every mu,
independently of the initial row lengths. The deficit count in (9)
overcounts admissible subpartitions; the two-letter tableau count
overcounts admissible fillings. Both are safe absolute upper bounds.
The term l=0 is exactly D_lambda. Bernoulli's inequality applies since
2r epsilon=128/1048575 lies in (0,1), with r(2r epsilon)<1/2.
Consequently (11) holds for every finite partition in the required
length range, not merely partitions checked to some finite size.

The expansion (12) has m+2 exponential factors, giving N=m+1=271.
For any fixed derivative order its coefficient bound is a polynomial
in n times d^n divided by a shifted factorial, so absolute convergence
is uniform on compact x-sets. In (14) put l=n+i; the added terms l<i
vanish by h_(l-i)=0. For (15), after transposition and both reversals
the entry in row s, column j (one-based) is
h_(l_(k+1-s)-k+j)=h_(lambda_s-s+j). The two reversal signs cancel.
The l_s=s-1 minor has lambda empty. In (16), L_s>=16, and the
falling factorial is zero whenever j>L_s; there is no division by a
negative factorial. Factoring powers for x>0 is legitimate even if an
individual exponent is negative. The total exponent in that minimal
minor is k(N-k+1)>0, and its Vandermonde is strictly positive.

For each cutoff J the finite product matrix in (14) satisfies
Cauchy--Binet exactly. Its entries tend absolutely to the displayed
derivatives, hence its determinant tends to H_k(R;x). All summands
are positive. The fixed minimal minor supplies a strictly positive
lower bound for all J>=k-1. Applying (11) term by term uses theta
only once in each Schur minor, not theta^k. The same entry convergence
for q_0 then proves (18). Neither strictness nor convergence assumes
an unknown bound uniform over unbounded x; the proof applies separately
to every x>0 with one partition comparison valid for all x.

For the analytic transfer, finite partial fractions of q give an
exponential polynomial on (0,infinity) with rates 1,a,conjugate(a).
Every derivative there has exponential decay times a polynomial.
The Taylor zero of order 271 at the origin makes its zero extension
C^270, with zero traces through that order. In particular each weak
derivative D^j q, j<=255, is the ordinary zero-extended derivative,
belongs to L1 intersect L2, and has no delta mass. The mass in (19)
at z=0 is K/(a conjugate(a))=1. Multiplying (19) at z and -z has
numerator K^2=|a|^4 and is exactly 1/P_*(z). The absolute exponential
moments justify this multiplication by convolution and Fubini.
Fourier uniqueness therefore identifies (20) everywhere by continuity.

More explicitly, for 0<=i,j<=255, the distributional convolution rule
gives D^(i+j)(q*check(q))=(D^i q)*(D^j check(q)). This can be justified
by first regularizing both L1 factors with compact smooth mollifiers,
using the ordinary derivative rule, and passing to distributions and
to the convolution of their L1 derivatives. Reflection gives
D^j check(q)(u)=(-1)^j q^(j)(-u), so the result is exactly (21).
The L2 translation estimate

    |integral q^(i)(t)[q^(j)(t-x-h)-q^(j)(t-x)] dt|
      <= ||q^(i)||_2 ||q^(j)(.-h)-q^(j)||_2 -> 0

makes its right side continuous. Since L561 independently gives the
C^542 representative, equality of distributions implies equality
of these classical derivatives at every real x. This argument never
differentiates either causal factor to order 510 across its edge.

The functions f_j are analytic on (0,infinity). Their prefix
Wronskians have column sign product (-1)^(l(l-1)/2), exactly the
sign in H_l(q), so every required prefix is strictly positive there.
Sra C.1 applies on that open interval. At a nonpositive evaluation
point all f_j are zero, so the zero-extended evaluation determinant
is zero. In (21) the column sign product cancels the sign defining
H_k(p_*). Replacing both derivative families by f introduces two
further sign products whose product is one.

To verify (23), expand both finite determinants. Every absolute term
integrates as a product of k integrals of |f_i(t)f_j(t-x)|, each finite
by L2 Cauchy--Schwarz. Fubini and the finite permutation sum therefore
apply before any positivity is invoked. The product of determinants
is symmetric under simultaneous permutations of the t_s; diagonals
have measure zero, giving the ordered-chamber formula without an
extra factorial. For each real x one may choose a strictly ordered
tuple above max(0,x) and a small neighborhood preserving that order.
Both determinants are continuous and positive on that neighborhood,
so the nonnegative integrand has strictly positive integral. This
includes x=0 and requires no cutoff in either direction.

Finally 2r-2=510<=542 verifies Sra C.6's global differentiability
hypothesis, and (23) verifies all its strict differential signs.
The source is used only for C.1/C.6, not for a numerical Xi certificate.
L561's density/normalization/transform/first-sign inputs were separately
checked in its retained-input audit. Thus both the strict PF256 claim
and the negative first polynomial sign at A survive this review.

Both existing exact scripts were replayed: 9/9 global-comparison and
13/13 partial-model scalar checks passed. The complete global bounds,
checks and failures, and the exact partial-model first-sign, density
and failures fields were inspected using
`python3 ../scripts/loop/inspect_json.py <certificate> --pointer <field> --full`.
In particular beta=32768/1015807<1, theta=983039/1015807>0, and the
normalized first sign is strictly below -31. These reproduce known
local values; the analytic audit above is what validates the global
model obstruction. L561's optional origin/tail estimates are not
needed for, or promoted by, this audit.

## Mathlib

Full matching coverage for this fixed-model certificate, the Schur
comparison and finite-order strictness transfer has not been checked.
Availability is unknown. No formal verification or absence is claimed.
Reference: https://leanprover-community.github.io/mathlib4_docs/.
