# Lemma 668: inverse-weight interpolation already has excessive point-evaluation cost

## Hypotheses

Use L649's complete product and exactly L666's independently displaced
family. Thus q>=1 is an integer, n=12q+3, M=4q+1=n/3, N=M-1,
x=-d=-5/4, R=11/8, U=121/64, H_0=27/(10n), t_j=j/n, and

    Z={x} union {x+i*H_0*(r+1/2+e_r): -2q<=r<2q},
    e_r real, |e_r|<=1/8.

Every original residue is one. No symmetry is imposed. Keep every
grid factor, including j=0, and the conjugated denominator angle:

    B_u(v)=product_(0<=j<n) R*(v-t_j*u)/(U-t_j*v/u),
    W_a(u)=B_u(x)/B_u(a),       z_a=a/R,       w_a=W_a(-1),
    c_k=R^(-1) sum_(a in Z) w_a*z_a^k,       0<=k<=N,
    G(zeta)=sum_(k=0)^N c_k*zeta^k,
    m(-1)=mean_(|zeta|=1) log|G(zeta)|.

The circle mean is normalized. Let F be the unique polynomial of
degree at most N interpolating F(z_a)=1/w_a at all M nodes, and set

    F(z)=sum_(k=0)^N f_k*z^k,
    S_N=sum_(k=0)^N binomial(N,k)*|f_k|,
    B_signed=log(M/R)-log S_N.

Existence, nonzero denominators and finiteness of these logarithms
are verified below; degree drops are allowed.

## Conclusion

The full finite-moment identity and its Mahler consequence are

    sum_(k=0)^N f_k*c_k=M/R,       m(-1)>=B_signed.       (1)

For every q>=5 and every allowed independent displacement vector,

    log S_N >= (n+1)/56,
    B_signed <= log(M/R)-(n+1)/56.                       (2)

Consequently no absolute C and onset can make

    S_N <= (M/R)*exp(n/100)*n^C                          (3)

hold uniformly. Indeed even the undisplaced sequence e_r=0 has

    (log S_N-n/100)/log n
        >= (11*n/1400+1/56)/log n -> infinity.           (4)

This is a lower bound on the prescribed **complete cost** and an
upper bound on the lower value B_signed certified by that cost. It
is not an upper bound on m(-1). It stops this particular simultaneous
inverse-weight interpolation functional, despite allowing all signed
row cancellations before taking absolute values. It does not stop
other polynomial data, a transfer using additional knowledge of G's
zero coefficients or actual degree, or a direct full-root argument.
The true fixed-angle bound, angular maximum, actual diagonal D,
support, Xi realization and all-degree signs remain unresolved.
This local specialization has not received a separate critical audit;
no originality or RH candidate is claimed.

## Proof

### 1. Source scope and the distinct functional

Reuse the unchanged invocation-start EXPLORE assessment
`drafts/literature/2026-11-02-signed-finite-deweighting-cost.md`.
It explicitly permits this prescribed simultaneous interpolant,
its normalization check and admissible point-evaluation lower tests.
L649 provides the definitions and L666 the family only; their other
claims are not needed. L667's individual-row obstruction is a contrast,
not a premise: signed row cancellation is retained in F. The scoped
comparison also retains the earlier ambient, monomial, scalar,
inherited-anchor and absolute-contour stops without extending them.

Import complex polynomial interpolation at distinct nodes from
C. de Boor, *Divided Differences*, Surveys in Approximation Theory 1
(2005), 46--69, version dated 21 December 2004,
[Proposition 7 and its proof, p.48](https://surveys-in-approximation-theory.com/papers/2/2.pdf).
The assessment inspected its divisibility/uniqueness argument and the
later complex Cauchy representations. Only finite interpolation is
used here, with no new analytic contour or inverse-norm theorem.

Import the classical complex-polynomial coefficient inequality in
S. Akhtari and J. D. Vaaler, *Lower bounds for Mahler measure that
depend on the number of monomials*, arXiv:1810.12413v1,
29 October 2018, [equation (1.3), p.1](https://arxiv.org/pdf/1810.12413v1):
if P is a nonzero complex polynomial of degree nu, then

    |coefficient_k(P)| <= binomial(nu,k)*exp(mean log|P|),
    0<=k<=nu.

No coefficient integrality or positivity is required. Reuse the
complete-root interpretation from F. Brunault and W. Zudilin,
*Many Variations of Mahler Measures*, ISBN 9781108794459,
[Propositions 1.4--1.5, pp.6--7](https://assets.cambridge.org/97811087/94459/excerpt/9781108794459_excerpt.pdf):
for actual leading coefficient gamma and all roots alpha counted
with multiplicity,

    mean log|P|=log|gamma|+sum_alpha log max(1,|alpha|).

This includes boundary roots and constant polynomials. These are
already inspected source inputs, not reproved general theorems.
The family-specific work is the exact normalization and the actual
inverse-data lower bound; interpolation existence alone supplies
neither. No numerical interpolation or condition-number estimate
is used as evidence.

### 2. Admissibility and the complete inverse data

Successive nonanchor ordinates have gap at least 3H_0/4, and their
distances from zero are at least 3H_0/8. They and the anchor are
therefore distinct. Every ordinate y satisfies

    |y|<=H_0*(2q-3/8)<2q*H_0<9/20,
    |x+i*y|^2<d^2+(9/20)^2=353/200<(273/200)^2.

Thus all nodes obey |a|<R-1/100 and |z_a|<1. Each t_j is in [0,1),
so d-t_j>1/4 and U-d*t_j>41/64. Direct division in the prescribed
product at u=-1 gives, for a=x+i*y,

    w_a=product_(0<=j<n) (1+i*b_j*y)/(1-i*A_j*y),
    A_j=1/(d-t_j),       b_j=t_j/(U-d*t_j).

The j=0 factor is present: b_0=0 and A_0=1/d. All these factors
are nonzero, w_x=1, and

    A_j-b_j
       =(U-2*d*t_j+t_j^2)/[(d-t_j)*(U-d*t_j)]>0,

because U-2*d*t+t^2=U-d^2+(d-t)^2 and U-d^2=21/64.
Consequently A_j>b_j>=0 and the exact inverse modulus is

    1/|w_a|=product_(0<=j<n)
                  sqrt((1+A_j^2*y^2)/(1+b_j^2*y^2)).   (5)

Every factor on the right is at least one. No phase is discarded
in F or in (1); only the modulus of its required value is used to
lower-bound its cost.

### 3. Identity, degree drops and normalization

Distinctness of the M nodes and finiteness of 1/w_a give the
interpolant F of degree at most M-1. Its anchor value is one, so
S_N>0. Substitution and finite summation give exactly

    sum_(k=0)^N f_k*c_k
       =R^(-1) sum_(a in Z) w_a*F(z_a)=M/R.

In particular G cannot be identically zero. If its actual degree
is nu<=N, the imported complete-root formula makes m(-1) finite,
even with circle roots. The coefficient inequality gives

    |c_k|<=binomial(nu,k)*exp(m(-1)),       0<=k<=nu;
    c_k=0,                                nu<k<=N.

For 0<=k<=nu, binomial(nu,k)<=binomial(N,k). Hence

    M/R = |sum_(k=0)^N f_k*c_k| <= S_N*exp(m(-1)),

which proves (1). This uses precisely the cost nominated in (3),
not an assertion that it is an optimal transfer when nu<N or when
additional coefficients vanish. If (3) held, (1) would indeed give
m(-1)>=-n/100-C log n with the advertised normalization.

For any interpolation node, |z_a|<1 and binomial(N,k)>=1 give

    1/|w_a|=|F(z_a)|
       <=sum_(k=0)^N |f_k|*|z_a|^k
       <=sum_(k=0)^N |f_k| <= S_N.                      (6)

All coefficients, including zeros due to degree drops, remain in
the complete cost. Inequality (6) is valid after arbitrary signed
cancellations in the coefficients of F.

### 4. An outer node forces a larger exponential rate

Choose the existing node indexed by r=2q-1 and write its positive
ordinate as y_*. For q>=5,

    y_*>=H_0*(2q-5/8)>=2/5,

since the second inequality is equivalent to 48q>=231. This
selection is admissible for every independent displacement vector;
no symmetry or special choice of its other entries is needed.

For grid points satisfying 1/2<=t_j<=3/4,

    A_j>=4/3,       b_j<=48/61.

The second bound follows because t/(U-d*t) is increasing for
0<=t<1, with derivative U/(U-d*t)^2. Since A_j>b_j, the function
(1+A_j^2*s)/(1+b_j^2*s) is increasing for s>=0. Thus

    (1+A_j^2*y_*^2)/(1+b_j^2*y_*^2)
       >= (1+(4/3)^2*(2/5)^2)/(1+(48/61)^2*(2/5)^2)
       = 26884225/23004225 > 7/6.                       (7)

The last comparison is exact:
6*26884225-7*23004225=275775>0. Other factors in (5) are
at least one and are not replaced by an unproved cancellation.
For n=12q+3, the selected integer grid indices are precisely

    6q+2 <= j <= 9q+2,

so their number is 3q+1=(n+1)/4. Finally

    log(7/6)=integral_1^(7/6) dt/t >=1/7.

Taking logarithms in (5), using (7) on these indices, and then (6),
gives

    log S_N >= log(1/|w_(x+i*y_*)|)
              >= ((n+1)/8)*log(7/6) >=(n+1)/56.

This proves (2). Since M/R=8n/33 and 1/56-1/100=11/1400,
for any fixed real C the excess over the required logarithmic cost
is at least

    log S_N-[log(M/R)+n/100+C log n]
       >=11*n/1400+1/56-(C+1)*log n-log(8/33)
       -> infinity.

Thus (3) fails for every C and onset. Formula (4) follows as well.
The obstruction is present already in the prescribed data, before
any interpolation-coefficient estimate, and is uniform over the
family. It does not say that G has small Mahler measure; the value
certified by (1) can be far smaller than the true mean. In particular
the undisplaced case is compatible with L664's positive baseline.

## Mathlib

Reuse the official [MahlerMeasure module](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Polynomial/MahlerMeasure.html)
coverage recorded in the prior assessment.
`Polynomial.norm_coeff_le_choose_mul_mahlerMeasure` supports the
degree-indexed coefficient bound, and
`Polynomial.logMahlerMeasure_eq_log_leadingCoeff_add_sum_log_roots`
supports the complete-root interpretation. G's nonzero hypothesis
was checked above; Lean's totalized logarithm is not used to remove
it. Full matching coverage of this specific inverse-data cost stop
has not been checked. No absence or formal verification is asserted.
