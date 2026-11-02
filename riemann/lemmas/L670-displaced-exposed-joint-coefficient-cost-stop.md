# Lemma 670: exposed joint coefficients retain excessive denominator charges

## Hypotheses

Use exactly L666's displacement family and L649's full product. Let
q>=1, n=12q+3, M=4q+1=n/3, J=n-1, x=-d=-5/4, R=11/8,
U=R^2=121/64, H_0=27/(10n), t_j=j/n, and

    Z={x} union {x+i*H_0*(r+1/2+e_r): -2q<=r<2q},
    e_r real, |e_r|<=1/8.

Every original residue is one. The same Z serves every angular u.
Retain j=0 and the denominator angle 1/u:

    B_u(v)=product_(0<=j<n) R*(v-t_j*u)/(U-t_j*v/u),
    W_a(u)=B_u(x)/B_u(a),
    G(u,zeta)=R^(-1) sum_(a in Z) W_a(u) H_M(a*zeta/R),
    H_M(v)=sum_(k=0)^(M-1) v^k,
    H=max_(|u|=1) mean_(|zeta|=1) log|G(u,zeta)|.

All means are normalized and all logarithms natural. Use L657's
complete clearing, with no common factor removed:

    A_a(u)=product_(j=1)^J(a-t_j*u),
    C_a(u)=product_(j=1)^J(U*u-t_j*a),
    Q(u)=C_x(u) product_(a!=x) A_a(u),
    K(u,zeta)=R^(-1)[Q(u)H_M(x*zeta/R)
      +sum_(a!=x) (x/a)A_x(u)C_a(u)
           product_(b!=x,a)A_b(u)H_M(a*zeta/R)],
    G=K/Q,     D_ang=MJ,     T=product_(j=1)^J t_j.

Write K_(h,k) for the coefficient of u^h*zeta^k, and

    L_Q=mean_(|u|=1) log|Q(u)|,
    P(zeta)=(x/R) sum_(a in Z) a^(-1)H_M(a*zeta/R),
    p_k=(x/R^(k+1)) sum_(a in Z) a^(k-1).

An extremal support coefficient means the first or last coefficient
when the nonzero exponent support of K is ordered by an injective
homomorphism Z^2 -> R. Define B_ext to be the largest number
log|K_(h,k)|-L_Q furnished by such an extremal coefficient. This is
the zero-binomial-cost use of the cited coefficient theorem on this
specific K. Other clearings, changes of variables, interior coefficients,
and restrictions to a spatial face are not included in B_ext.

## Conclusion

For every displacement vector the two angular endpoint polynomials are

    K_(0,.)=Q(0)P,       K_(D_ang,.)=lc(Q)P,               (1)
    Q(0)=(-x)^J T product_(a!=x) a^J,
    lc(Q)=U^J [(-1)^J T]^(M-1),
    L_Q=J log U+J sum_(a!=x)log|a|.

Put P_n=J log(U/d)-log T and
C_infty=J sum_(a!=x)log|a|-(M-1)log T. For every nonzero
coefficient in these two columns, with rho=273/275,

    log|K_(0,k)|-L_Q <= log(M/R)+k log rho-P_n,
    log|K_(D_ang,k)|-L_Q <= log(M/R)+k log rho-C_infty. (2)

The condition p_(M-1)!=0 holds on an open dense subset of the
displacement cube (relative topology). On this subset the support's
convex hull is exactly [0,D_ang]x[0,M-1]. Consequently

    H >= B_ext,
    B_ext <= log(M/R)-(41/121)(n-1).                   (3)

For any fixed real C, uniformly on that subset,

    B_ext+n/100+C log n
      <= -(3979/12100)n+(C+1)log n+41/121-log(3R)
       -> -infinity.                                 (4)

Thus selecting a support-extremal coefficient of this complete
clearing, in any ordering, cannot certify H>=-n/100-C log n
uniformly. There is an admissible sequence to which this method stop
applies: for each n keep e_r=0 except r=0, and choose e_0 among
1/(8l), 1<=l<=M-1, with p_(M-1)!=0; such a choice always exists.
This sequence is not asserted to violate any lower bound for H.

This is an upper bound on a certified lower value, not an upper bound
on H. Exceptional vectors with p_(M-1)=0 may have different exposed
support and are not covered by the assertion about all extremal
coefficients. Bounds (1)--(2) still apply there. Interior coefficients
with their actual support-order costs, alternative rational clearings,
and direct signed angular arguments remain open. The actual diagonal,
paid localization, Xi realization and mixed signs are not resolved.
This local negative result has not received a separate critical audit;
no originality or RH candidate is claimed.

## Proof

### 1. Assessed sources, overlap and the precise certificate

Reuse the invocation-start EXPLORE assessment
`drafts/literature/2026-11-02-displaced-angular-maximum-linear-rate.md`.
It explicitly covers signed coefficients of the complete joint
numerator with the actual denominator and support-order costs. No new
external theorem is used and no general coefficient theorem is reproved.

Import S. Akhtari and J. D. Vaaler, *Lower bounds for Mahler measure
that depend on the number of monomials*, arXiv:1810.12413v1,
29 October 2018, [Theorem 1.2, p.3; ordering pp.3--4 and proof
pp.8--9](https://arxiv.org/pdf/1810.12413v1). For a nonzero complex
trigonometric polynomial F with finite exponent support
{v_0,...,v_s} in the stated order, the theorem gives

    |F_hat(v_j)| <= binomial(s,j)*exp(mean log|F|).

No integrality, positivity or symmetry is required. For j=0 or s
the binomial factor is exactly one. If a different coefficient is
chosen, its factor cannot be suppressed. The source assessment read
the theorem and its complete multivariable proof; its underlying Boyd
input is imported through that theorem, not independently rederived.

L657 supplies the exact clearing and absolute logarithmic integrability.
Its cited root input is F. Brunault and W. Zudilin, *Many Variations
of Mahler Measures*, ISBN 9781108794459,
[Proposition 1.4, pp.6--7](https://assets.cambridge.org/97811087/94459/excerpt/9781108794459_excerpt.pdf),
including unit-circle roots. For clarity the finite clearing and
denominator charge needed here are verified below. The logarithmic
integrability input is Z. Issa and M. Lalin,
[*A generalization of a theorem of Boyd and Lawton*,
arXiv:1203.5379v1, Remark 3.8 and Theorem 4.1/proof, p.7](https://arxiv.org/pdf/1203.5379v1),
as inspected in the reused assessment. L658 supplies finiteness and
attainment of H. No parameter-uniform root continuity is used.

Since log|G|=log|K|-log|Q| is absolutely integrable, Fubini and
the elementary maximum-versus-mean inequality give

    H >= mean_(u,zeta)log|K|-L_Q
      >= log|K_(h,k)|-log binomial(s,j)-L_Q.            (5)

The last step is precisely the imported theorem. For extremal
support coefficients it proves H>=B_ext. It does not turn an upper
bound for B_ext into an upper bound for H.

L657 already records the constant-angular charge P_n. The additional
work here is the top angular polynomial, support geometry, and the
uniform failure of every exposed coefficient after the exact charge.
L667/L668 concern fixed-angle inverse rows and prescribed inverse
data; they are contrasts, not premises. The retained-monomial phase,
full-circle compensation and L669 fixed-angle stops do not establish
this conclusion and are not used to infer failure of H.

### 2. Exact endpoint polynomials and denominator charge

The poles are distinct: successive nonanchor ordinates differ by at
least 3H_0/4, each is at least 3H_0/8 from zero, and all satisfy
|Im a|<9/20. Hence

    d<=|a|<sqrt(353/200)<273/200=R-1/100.

All M poles and every prescribed moment are present. Dividing the
original products, including j=0, gives the rational continuation

    W_a(u)=(x/a) A_x(u)C_a(u)/(A_a(u)C_x(u)).          (6)

Both at u=0 and at infinity, the two product ratios cancel each
other, giving W_a(0)=W_a(infty)=x/a, including a=x. For infinity,
A_x/A_a tends to 1 and C_a/C_x tends to 1. At zero these ratios
are (x/a)^J and (a/x)^J. No root or grid factor is omitted.
Multiplying (6) by Q gives the displayed K and degree bounds
deg_u K<=D_ang and deg_zeta K<=M-1. Since Q has exact degree
D_ang with nonzero leading coefficient, evaluating G at zero and
infinity gives (1), including the coefficient at u^D_ang even if
an individual spatial coefficient vanishes.

For each factor of C_x, its sole root t_j*x/U has modulus <1, so
its log mean is log U. Each factor a-t_j*u has its root a/t_j
outside the disk, so its log mean is log|a|. The cited root formula
therefore gives exactly L_Q in (1); Q has no circle zeros. Direct
products at zero and of leading coefficients give the other two
identities in (1). Subtracting L_Q gives

    log|Q(0)|-L_Q=-P_n,
    log|lc(Q)|-L_Q=-C_infty.                           (7)

These are the charges of the actual denominator of the complete K.
Possible common factors of K and Q have not been discarded on either
side of (5); the coefficient mechanism is specified for this clearing.

Each summand in p_k has modulus at most R^(-1)rho^k, because
|x/a|<=1 and |a|/R<=rho. Thus

    |p_k| <= (M/R)rho^k,
    Re p_0=(1/R)sum_a d^2/|a|^2>0.                    (8)

In particular the two bottom corners are always nonzero. Equations
(1), (7) and (8) prove (2) without assuming a sign for any other sum.

### 3. All exposed coefficients on a dense admissible set

The top coefficient is

    p_(M-1)=(x/R^M)sum_a a^(M-2).                     (9)

Hold every displacement except e_0 fixed. As a polynomial in e_0,
(9) has degree M-2>=3 and nonzero leading coefficient
(x/R^M)(iH_0)^(M-2). It has at most M-2 real roots. In every
relative neighborhood of every point of the displacement cube one
can vary e_0 within its allowed interval to avoid these finitely many
roots. This proves density; continuity gives relative openness.
Taking all other coordinates zero and the M-1 distinct values
1/(8l) proves the asserted finite-choice sequence without relying on
a numerical nonvanishing test.

When (9) is nonzero, (1) and (8) show that all four corners of the
rectangle are nonzero coefficients of K. All other support exponents
lie inside it, so the convex hull is the whole rectangle. An injective
homomorphism Z^2 -> R has the form (h,k) -> alpha*h+beta*k,
where alpha and beta are nonzero and have irrational ratio. Its
unique maximum and minimum on this rectangle occur at corners.
Therefore every ordered support extremum is a corner. Conversely
each corner can be made such an extremum by a suitable irrational
ratio and choice of signs. No favorable sparsity or canceled corner
is silently presumed. The number s of other support points is
irrelevant precisely because j=0 or s makes binomial(s,j)=1.

### 4. Uniform quantitative failure of this certificate

Every t_j is strictly between zero and one, so -log T>0. For t>1,
integrating 1/v from 1 to t gives log t>(t-1)/t. Consequently

    P_n>J log(121/80)>(41/121)J,
    C_infty>=J(M-1)log(5/4)>(M-1)J/5
             >=4J/5>(41/121)J.                        (10)

These deliberately conservative rational bounds suffice; no Stirling
approximation or numerical logarithm is needed. Since k log rho<=0,
(2), the corner identification, and (10) prove the upper bound in
(3). Substituting M=n/3 gives (4) exactly. Its negative linear term
dominates any fixed multiple of log n, uniformly over the indicated
subset. Even zero binomial cost cannot reach the target; positive
binomial costs for these same endpoint coefficients only reduce their
certificates. This does not analyze nonendpoint coefficients.

For context only, L658 and L661 show why the still-open H target
would be useful: with the true unit-residue diagonal they give

    D<=n*exp(2*(91/5000)n+6)/(3*(137/5000)),
    paid excess >=2H-2log n-32*pi^2/9-log D+n/16.

If H>=-n/100-C log n were proved, their right side would be at least
(61/10000)n-(2C+3)log n-O(1), positive beyond an absolute onset.
This is a conditional explanation, not a new application or a premise
of (1)--(4). The independent support, realization and sign gaps remain.

## Mathlib

Full matching coverage of the multivariable support-order theorem and
this family-specific cost stop has not been checked. The reused source
assessment records supporting
[Mathlib.Analysis.Polynomial.MahlerMeasure](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Polynomial/MahlerMeasure.html),
including `Polynomial.logMahlerMeasure_eq_log_leadingCoeff_add_sum_log_roots`,
`Polynomial.intervalIntegrable_mahlerMeasure`, and
`Polynomial.mahlerMeasure_mul`. These support one-variable root and
product accounting, not the full displaced-family statement. Unknown
coverage is not an absence claim. No formal verification is asserted.
