# Corollary C029k: fixed-minor polynomial companion regularization stop

## Hypotheses

Use exactly C028d's actual centered reciprocal Jensen polynomials and
C028f's positive entire-function majorant:

    b_0=1, b_j=gamma_j/gamma_0>0,
    F(u)=sum_(j>=0) b_j u^j/j!,
    P_d(x)=sum_(j=0)^d binom(d,j)b_j x^(d-j),
    Q_d(y)=P_d(y-b_1)=y^d+sum_(k=1)^d c_(d,k)y^(d-k),
    log F(r)<=K_0*r^(3/4) for every r>=1,

where K_0>=1 is fixed, b_1>0 is fixed, and d ranges through integers
d>=3. These are existing actual-family inputs. All polynomial roots
retain their algebraic multiplicities. Define the real d-by-d monomial
Frobenius companion A_d to have subdiagonal entries 1, last column
(-c_(d,d),-c_(d,d-1),...,-c_(d,1))^T, and all other entries zero.
For real y and epsilon>0 put M_d(y)=yI_d-A_d and, off the finite
exceptional set consisting of zero and real roots of Q_d, put

    t_d(y)=(1/d)log|Q_d(y)|-log|y|,
    R_(d,epsilon)(y)
      =(1/(2d))log det(M_d(y)^T M_d(y)+epsilon^2 I_d)-log|y|,
    D_(d,epsilon)(y)=R_(d,epsilon)(y)-t_d(y).

Assign arbitrary finite values on the exceptional set when integrating.
Integrals use unscaled Lebesgue measure dy. There is no RH,
hyperbolicity, simplicity, normality, randomness, root-separation or
condition-number assumption, and no similarity change to A_d.

## Conclusion

Let I=[b_1+1/4,b_1+1/2]. For every fixed finite K>0 and every d>=3,

    integral_I |R_(d,d^(-K))-t_d|dy
      >= 1/4-C_F*d^(-1/4)-K*log(d)/(4d),                 (1)
    C_F=4K_0*((1/2)^(1/4)-(1/4)^(1/4)).

In particular, with the same positive constant for every fixed K,

    liminf_(d->infinity) integral_I |R_(d,d^(-K))-t_d|dy >= 1/4. (2)

For every fixed finite A>=1, the analogous liminf over [-Ad,Ad]
is also at least 1/4. Thus no fixed polynomial cutoff epsilon=d^(-K)
meets nomination1993's vanishing unscaled window-error prerequisite for
this specified companion. This is a known-method specialization and a
route obstruction, not a bound on H_d, a solution of the signed-payment
problem, or evidence of an actual off-line zero. The independent
audit1998 below accepts this specialization under its stated contracts.

## Proof

### Imported finite identities and the reason for specialization

Reuse the SPECIALIZE coverage prepared in assessment1994 and separately
rechecked in source-URL review1995. Nicholas J. Higham, *What Is a
Companion Matrix?*, 23 March 2021,
[opening definition and identity (*)](https://nhigham.com/2021/03/23/what-is-a-companion-matrix/),
gives det(yI_d-A_d)=Q_d(y) for exactly the subdiagonal/last-column
convention above. This polynomial identity includes all multiplicities;
no diagonalizability is needed.

Oliver Knill, *Cauchy-Binet for pseudo-determinants*, author manuscript
dated 10 June 2014,
[Section 5, Theorem 7 and Corollary 9, printed pp.16-17; exterior-power
proof in Section 6, pp.18-19](https://people.math.harvard.edu/~knill/graphgeometry/papers/bi.pdf),
supplies the ordinary determinant identity for a real matrix B:

    det(I+z B^T B)=sum_P z^|P| det(B_P)^2,

where the sum is over all square minors, including the size-zero minor
with determinant 1. No rank or invertibility assumption is imposed.
Only this ordinary determinant assertion is imported, not any
pseudo-determinant assertion. Applying it with B=M_d(y) and
z=epsilon^(-2), and multiplying by epsilon^(2d), gives

    G_(d,epsilon)(y):=det(M_d(y)^T M_d(y)+epsilon^2 I_d)
      =sum_(k=0)^d epsilon^(2(d-k))
          sum_(S,T subset {1,...,d}, |S|=|T|=k)
             det(M_d(y)[S,T])^2.                         (3)

All sums are finite and all terms are nonnegative. This verifies every
epsilon power, including the empty term epsilon^(2d) and the unique
full-size term Q_d(y)^2. In particular G is strictly positive for all
real y. The cited identities do not give the actual-family estimate
(1); the selected minor and coefficient/factorial comparison below are
the required local specialization. No general theorem is reproved.

### The selected minor and the nonnegative discrepancy

Choose S={2,...,d}, T={1,...,d-1}. Since T omits the last column,
no companion coefficient occurs in this minor. Number its rows and
columns by i,j=1,...,d-1. Its entry in position (i,j) is -1 when j=i,
y when j=i+1, and zero otherwise. Thus it is upper bidiagonal, its
determinant is (-1)^(d-1), and its squared determinant is exactly 1.
Its k=d-1 contribution in (3) is epsilon^2. Keeping that contribution
and separately the full-size contribution proves

    G_(d,epsilon)(y)>=epsilon^2,
    G_(d,epsilon)(y)>=Q_d(y)^2.                           (4)

Off the finite exceptional set, canceling the common -log|y| gives

    D_(d,epsilon)(y)=(1/(2d))log G_(d,epsilon)(y)
                         -(1/d)log|Q_d(y)|>=0.           (5)

The functions are measurable and integrable on every bounded interval:
G is a strictly positive continuous function with its logarithm bounded
on each compact interval; polynomial logarithms have only locally
integrable logarithmic singularities, including repeated roots; and
log|y| is locally integrable. Consequently arbitrary finite null-set
values do not affect any integral or the almost-everywhere sign (5).

### Uniform actual-polynomial upper bound on the fixed interval

For y in I set x=y-b_1, so 1/4<=x<=1/2 and dy=dx. Every term in
P_d(x) is positive. The exact factorial comparison is

    binom(d,j)=(d)_j/j!<=d^j/j!   (0<=j<=d).

Using positivity again to extend the finite sum to the entire series,

    0<Q_d(y)=P_d(x)
      =x^d sum_(j=0)^d binom(d,j)b_j x^(-j)
      <=x^d sum_(j=0)^d b_j(d/x)^j/j!
      <=x^d F(d/x).

Since d/x>=1, the recorded growth estimate applies and gives uniformly
on this closed interval

    (1/d)log Q_d(y)<=log x+K_0*x^(-3/4)*d^(-1/4).        (6)

In particular I contains neither zero nor a real root of Q_d. This
argument retains the j! in F; replacing F by the wrong coefficient
series would invalidate the growth comparison.

### Polynomial cutoff and unscaled integration

Fix any finite K>0 and take epsilon=d^(-K). The first inequality
in (4) gives (1/(2d))log G>=log(epsilon)/d=-K log(d)/d.
Combining with (5)-(6), on I one obtains

    |R_(d,d^(-K))(y)-t_d(y)|=D_(d,d^(-K))(y)
      >=-log x-K_0*x^(-3/4)*d^(-1/4)-K log(d)/d.         (7)

The lower bound need not be positive at the smallest degrees; that
does not affect its validity. Integrate (7) with dy=dx. The interval
has length 1/4, and elementary antiderivatives give

    integral_(1/4)^(1/2) -log x dx
      =[-x log x+x]_(1/4)^(1/2)=1/4,
    integral_(1/4)^(1/2) x^(-3/4) dx
      =4*((1/2)^(1/4)-(1/4)^(1/4)).

These equalities prove (1). Its two explicit error terms tend to zero
for each fixed K, proving (2). No uniform onset for unbounded K and no
interchange of an integral with a limiting function is asserted.

Finally, for any fixed A>=1, I is contained in [-Ad,Ad] for all
integers d>=max(3,ceil((b_1+1/2)/A)). The almost-everywhere
nonnegativity in (5) then gives

    integral_[-Ad,Ad] |R_(d,d^(-K))-t_d|dy
      >=integral_I |R_(d,d^(-K))-t_d|dy.

This proves the window consequence. It only rejects the nominated
polynomial-cutoff regularization prerequisite in the given monomial
basis. C028b's H_d=o(d), C029j's signed upper payment and C028e's
exterior assembly remain unresolved. No q=1/(4d), L=2Ad or ordered
limit from that separate assembly has been changed or applied here.

### Independent proof audit1998 (2026-11-20)

Replayed the complete finite specialization under assessment1996,
separately approved in review1997, reusing its inspected Knill and
Higham statements. No formula, constant or hypothesis requires repair.
This verifies a local known-method obstruction, not new mathematics
beyond the cited methods or an independent audit of their source proofs.

For the specified companion, deleting row 1 and column d of yI-A_d
leaves entries -1 on the diagonal and y on the superdiagonal. No last
column coefficient survives. The minor is therefore exactly
(-1)^(d-1) for every real y, even when the full matrix is singular.
In (3), multiplying epsilon^(2d) by epsilon^(-2k) gives
epsilon^(2(d-k)); thus this minor contributes epsilon^2 and the unique
full minor contributes Q_d(y)^2. These are distinct terms for d>=3.
The empty minor gives epsilon^(2d)>0. Hence the logarithm exists
everywhere and D>=0 almost everywhere, without any rank assumption.

C028d supplies precisely Q_d(y)=P_d(y-b_1). On I the variable is
x=y-b_1 in [1/4,1/2], so each coefficient term is positive and the
Jacobian is one. Dividing the coefficient estimate by x^d leaves
binom(d,j)b_j x^(-j), bounded by b_j(d/x)^j/j!, including j=0,d.
This is the same F as C028f, with its one fixed K_0 and d/x>=1.
Dividing K_0(d/x)^(3/4) by d gives exactly
K_0 x^(-3/4)d^(-1/4). In particular Q_d>0 on I, while b_1>0
excludes the reference singularity there. No root avoidance is
assumed elsewhere; finite multiplicities give locally integrable
logarithmic singularities, and arbitrary finite exceptional values
change neither the integral nor its sign almost everywhere.

The determinant floor gives log(epsilon)/d=-K log(d)/d, with no
extra factor two. The primitive at 1/2 is (log 2)/2+1/2 and at
1/4 is (log 2)/2+1/4. Their difference is exactly 1/4. Integrating
the growth error gives C_F as stated; integrating the cutoff error
multiplies it by the length 1/4. Both errors vanish for each fixed
finite K>0, with no claim of an onset uniform in K.

For each fixed finite A>=1, the positive interval I is inside the
window once Ad>=b_1+1/2. The global almost-everywhere nonnegative
discrepancy permits restriction to I before taking liminf. The measure
is dy throughout; dividing by the window length would be a different
claim. Thus the fixed-K and fixed-A window quantifiers survive.
C028d and C028f are the only direct local mathematical inputs; no DAG
change is needed. The audit parks only the specified monomial-basis
polynomial cutoff, leaving signed payment and H_d=o(d) open.

## Mathlib

Not checked. Full matching theorem availability is unknown. General
determinant, Cauchy-Binet, finite-sum and integration facts would be
supporting results, not evidence that this exact actual-family
asymptotic is formalized. No absence or formal verification is claimed.
