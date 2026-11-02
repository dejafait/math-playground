# Lemma 667: every individual finite-residue recovery row has excessive Mahler cost

## Hypotheses

Use exactly L666's independently displaced family and L649's complete
product. Thus q>=1 is an integer, n=12q+3, M=4q+1=n/3, N=M-1=4q,
x=-d=-5/4, R=11/8, U=R^2, H_0=27/(10n), and

    Z={x} union {x+i*H_0*(j+1/2+e_j): -2q<=j<2q},
    e_j real, |e_j|<=1/8.

Every original residue is one; no symmetry is imposed. Retain every
t_j=j/n, 0<=j<n, and the conjugated angular denominator:

    B_u(v)=product_(j<n) R*(v-t_j*u)/(U-t_j*v/u),
    W_a(u)=B_u(x)/B_u(a).

At the fixed angle u=-1 put z_a=a/R, w_a=W_a(-1), and

    c_k=R^(-1) sum_(a in Z) w_a z_a^k,       0<=k<=N,
    G(zeta)=sum_(k=0)^N c_k zeta^k,
    m(-1)=mean_(|zeta|=1) log|G(zeta)|.

The circle measure is normalized. Let nu be the actual degree of G;
nonvanishing is verified below, so 0<=nu<=N. Define the exact finite
Lagrange row at each original node by

    ell_a(z)=product_(b in Z, b!=a) (z-z_b)/(z_a-z_b)
            =sum_(k=0)^N ell_(a,k) z^k,
    S_a(nu)=sum_(k=0)^nu |ell_(a,k)| binomial(nu,k),
    B_row=max_(a in Z) [log|w_a|-log R-log S_a(nu)].

This specifies the tested transfer precisely: recover one residue
from all M moments, apply the classical degree-indexed coefficient
bound and the triangle inequality, and choose the best residue row.
It allows the true degree and exact row coefficients, not merely an
upper estimate for an inverse matrix norm. It does not exploit extra
zero coefficients within that degree or signed combinations of rows.

## Conclusion

All the rows and logarithms above are defined, and the full exact
moment identities and their coefficient-to-Mahler consequences are

    w_a=R sum_(k=0)^N ell_(a,k)c_k,
    m(-1)>=B_row.                                      (1)

Nevertheless the certified value in (1) satisfies, uniformly over
every independent displacement vector,

    S_a(nu)>=(25/18)^N,       0<|w_a|<=1,
    B_row<=-log R-(n/3-1)log(25/18)
          <=-7n/75+7/25-log R.                         (2)

The anchor row has the stronger cost S_x(nu)>=(25/9)^N.
In particular, for every fixed real C,

    B_row+n/100+C log n
       <=-n/12+C log n+7/25-log R -> -infinity.         (3)

Thus this exact individual-residue recovery followed by the
coefficientwise triangle bound cannot certify the approved benchmark
m(-1)>=-n/100-C log n, for any absolute C and uniform onset. Choosing
another row, or taking a nonnegative weighted average of the resulting
inequalities, does not repair this transfer.

This is an upper bound on the **certified lower value B_row**, not an
upper bound on m(-1). It supplies no admissible countersequence to
the benchmark, no obstruction to signed combinations of rows or a
direct full-root argument, and no conclusion about H, Xi signs or RH.
All spatial roots, boundary roots, multiplicities and the actual leading
factor remain part of m(-1). The actual squared-residue diagonal D is
not replaced or estimated in this proof. The new local cost calculation
has not received a separate critical audit; no originality is claimed.

## Proof

### 1. Source scope and the distinct test

The unchanged invocation-start EXPLORE assessment is
`drafts/literature/2026-11-02-displaced-full-spatial-fixed-angle.md`.
It explicitly covers finite recovery at the actual nodes, with full
moment, normalization and coefficient-to-Mahler costs. Its source
readings are reused; no further literature search is needed here.

Import the classical complex-polynomial coefficient bound as stated
in S. Akhtari and J. D. Vaaler, *Lower bounds for Mahler measure that
depend on the number of monomials*, arXiv:1810.12413v1 (29 October
2018), [equation (1.3), p.1](https://arxiv.org/pdf/1810.12413v1):
for a nonzero degree-nu complex polynomial P,

    |coefficient_k(P)|<=binomial(nu,k)*Mahler(P),
    Mahler(P)=exp(mean log|P|),       0<=k<=nu.

Their Theorem 1.1, p.2, supplies the stronger term-count formulation;
that improvement is not assumed here because no favorable nonzero
support pattern is established. The primary univariate proof was read
in the reused assessment. No arithmetic or coefficient sign hypothesis
is required, and no general coefficient theorem is reproved here.

The finite inverse convention is W. Gautschi, *On inverses of
Vandermonde and confluent Vandermonde matrices*, Numerische Mathematik
4 (1962), 117--123, [Section 2 and Theorem 1, pp.118--119](https://www.cs.purdue.edu/homes/wxg/selected_works/section_01/016.pdf).
Its matrix has columns (1,z_a,...,z_a^N)^T and distinct complex nodes;
its maximum row-sum upper bound retains products of all node gaps.
The exact row identity below is the necessary specialization of this
inverse to the prescribed family. A large *upper bound* for its norm
would not establish a method obstruction: here we lower-bound the
actual cost of every row instead.

Use the full polynomial root formula, F. Brunault and W. Zudilin,
*Many Variations of Mahler Measures*, ISBN 9781108794459,
[Propositions 1.4--1.5, pp.6--7](https://assets.cambridge.org/97811087/94459/excerpt/9781108794459_excerpt.pdf),
already inspected in the reused assessment chain. For actual leading
coefficient gamma and every root alpha with multiplicity, it gives

    mean log|P|=log|gamma|+sum_alpha log max(1,|alpha|),

including boundary roots and the constant-polynomial case. It justifies
the finite logarithmic mean; no logarithmic L2 transfer is assumed.

L649's ambient coisometry loses family information; it does not compute
these finite rows. L660 stops a single phase-neutral monomial, L665
stops an inherited o(1) approximation and an absolute contour cost,
and L666's scalar sampling attempts leave a signed energy uncontrolled.
Those are comparisons, not premises for the cost bound below. L666
specifies the exact admissible family; its quadrature and later diagonal
deformation assertions are not used. The proof verifies the required
family geometry directly. L658, L661 and L664 are downstream context
only: this step does not reprove or assume their response conclusions.

### 2. Geometry and complete-product magnitudes

Two consecutive nonanchor ordinates have gap at least 3H_0/4, and
the nearest nonanchor ordinate has distance at least 3H_0/8 from zero.
Thus the M nodes are distinct. Every nonanchor ordinate y obeys

    |y|<=H_0*(2q-3/8)<2qH_0=27q/(5n)<9/20.

This also holds for the anchor y=0. Consequently every node has
|a|>=d and |a|^2<d^2+(9/20)^2=353/200<(273/200)^2.
This verifies the inherited radius restriction R-1/100=273/200.
For any distinct a,b in Z,

    0<|a-b|<9/10;

if a=x, the upper bound improves to 9/20. No lower gap is silently
replaced by a dimension-independent quantity.

For each t=t_j, U-dt>U-d=41/64>0 and d-t>1/4. Exact division
of every factor of the prescribed product at u=-1 gives

    w_(x+i*y)=product_(j<n) (1+i*b_j*y)/(1-i*A_j*y),
    A_j=1/(d-t_j),       b_j=t_j/(U-d*t_j).

In particular the j=0 factor is included, with b_0=0. Moreover

    A_j-b_j=(U-2*d*t_j+t_j^2)/[(d-t_j)(U-d*t_j)]>0,

because the numerator equals U-d^2+(d-t_j)^2 and U-d^2=21/64.
All A_j are positive and b_j are nonnegative. Hence each modulus
ratio is sqrt((1+b_j^2*y^2)/(1+A_j^2*y^2))<=1 and nonzero.
Their finite product satisfies 0<|w_a|<=1, with w_x=1. This bound
uses the actual conjugated-angle product, not surrogate weights or
positivity of its complex values.

### 3. Exact all-moment recovery and degree qualifications

The Lagrange polynomial ell_a is defined because all nodes are
distinct; it equals one at z_a and zero at every other node. Substituting
the finite moment definitions gives, without any infinite interchange,

    R sum_(k=0)^N ell_(a,k)c_k
      =sum_(b in Z) w_b ell_a(z_b)=w_a.

This is the explicit inverse row with all M moments. If G were the
zero polynomial, every left side would vanish, contradicting w_x=1.
Thus the true degree nu is defined. The imported complete-root formula
shows that m(-1) is finite, including in the presence of spatial circle
roots or degree drops. Let mathcalM=exp(m(-1))>0.

The imported coefficient inequality applied with degree nu gives
|c_k|<=binomial(nu,k)*mathcalM for 0<=k<=nu; the other coefficients
are exactly zero. Apply the triangle inequality to the exact row:

    |w_a|<=R sum_(k=0)^nu |ell_(a,k)| |c_k|
          <=R*S_a(nu)*mathcalM.

Every S_a(nu) is finite and positive: its constant summand is nonzero,
as calculated next. Taking logarithms and the maximum over all rows
proves (1). This allows the true degree and therefore is no weaker
than the commonly used bound obtained by replacing nu with N. It
still pays for internal zero coefficients in the degree envelope;
a further sparsity-sensitive transfer is not evaluated here.

### 4. A lower bound on the actual transfer cost

The constant coefficient of the exact inverse row has modulus

    |ell_(a,0)|=product_(b!=a) |z_b|/|z_a-z_b|
               =product_(b!=a) |b|/|a-b|.

The factors R cancel exactly. There are N factors; each is greater
than (5/4)/(9/10)=25/18 by Section 2. Since binomial(nu,0)=1,

    S_a(nu)>=|ell_(a,0)|>=(25/18)^N.

For a=x the same proof gives (25/9)^N. This is a lower bound on
the exact positive sum S_a(nu), not merely on a loose upper estimate
for it. Every additional binomial-weighted summand is retained and
can only increase that cost. Combining this with |w_a|<=1 proves
the first bound for B_row in (2), for every row including the best one.

For t>1 the integral expression log t=integral_1^t dv/v gives
log t>=(t-1)/t. At t=25/18 it yields log(25/18)>=7/25. Since
N=n/3-1, the second bound in (2) follows. Finally

    7/75-1/100=1/12,

which proves (3) and the uniform mismatch with the permitted loss.
Any nonnegative weighted sum of the inequalities
|w_a|<=R*S_a(nu)*mathcalM yields a lower value that is a weighted
average of |w_a|/(R*S_a(nu)), with weights proportional to the positive
S_a(nu). It cannot exceed the largest individual lower value.

Signed combinations *before* taking absolute values can cancel large
row coefficients and are not covered by this argument. The actual
weights' phases and unit original residues could matter to such a
combination. Neither the finite inverse itself nor the full fixed-angle
target is declared impossible. This distinction is essential: replacing
B_row by m(-1) in (2) or (3) would reverse the logical content of the
calculation and produce an invalid counterexample.

## Mathlib

Reuse the official
[MahlerMeasure module](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Polynomial/MahlerMeasure.html)
coverage checked on 2 November 2026 in the unchanged assessment.
`Polynomial.norm_coeff_le_choose_mul_mahlerMeasure` is the exact
supporting degree-indexed coefficient inequality;
`Polynomial.logMahlerMeasure_eq_log_leadingCoeff_add_sum_log_roots`
supports the complete-root interpretation. The nonzero hypotheses
needed for the analytic integral were verified above despite Lean's
totalized logarithm. Full matching coverage for this family-specific
inverse-row cost and its method limitation has not been checked;
neither absence nor a formal verification is asserted.
