# Lemma 974: a complete triangular common-terminal eta error budget

## Hypotheses

Use the actual Xi paired nodes beta_j=alpha_j^(-2) of L024,
with all multiplicities and L026's zero geometry. Fix a finite real
A>0 with sum_j |beta_j|<=A. Use the unconditional definitions and
identity in L964(5),(7): for each integer k>=1,

    P_k(z)=sum_{h=0}^{floor((k-1)/2)}
                  (-1)^h binom(k,2h+1)(z/4)^h,
    a_k(z)=P_k(z)(1+z/4)^(-k/2),     H_k(z)=a_k(z)^2,
    lambda_k=sum_j beta_j H_k(beta_j).

The branch in a_k is analytic on |z|<4 and normalized by a_k(0)=k.
The lambda_k are ordinary zeta Li coefficients, without division by k.
Squares are algebraic. For u>0 define the full off-diagonal sum

    Q_u(k)=sum_j beta_j^2 H_k(beta_j)/(beta_j+u).

For an integer n>=3 set u=eta_n=1/(64*9^n), fixed throughout all
inner indices 1<=k<=n, and define

    E_n(k)=Q_u(k)-lambda_k,
    J_n=(n-1)E_n(2)-(n-2)E_n(1),
    T_n=sum_{k=2}^{n-1}(n-k)
                    [E_n(k+1)-2E_n(k)+E_n(k-1)],
    B_n=|J_n|+|T_n|.

No RH, negative Li coefficient, real-node hypothesis, finite head,
effective tail modulus, or sign of Q_u(k) is assumed.

## Conclusion

All node sums used below are absolute and real at each fixed n,k,u.
The two initial errors are retained exactly, and for every n>=3,

    B_n <= A*(n^2+119/648) < 16*A*n^2.                    (1)

This pays an absolute polynomial regularization budget only. The
unregularized signed cumulative forcing remains uncontrolled; neither
an all-index Li lower bound, positivity of Q_u(k), nor RH follows.
The calculation is a specialization of known finite summation and
analytic estimates, classified REPRODUCTION, not a claim of novelty.
Written in step202 and independently audited in step203, 10 November
2026. The statement, hypotheses and constants survived unchanged.

## Proof

### Complete subtraction and its two parts

L026 gives |beta_j|<1/16 and Re(beta_j)>0, while L024 supplies
the mass bound. Consequently, for each node z and u>0,

    |z+u|>=u,               |z+u|>=|z|.                  (2)

Use L964(9)-(10)'s unconditional analytic estimates at index k:

    |H_k(z)|<=9^k                     (|z|<=1/4),
    H_k(0)=k^2,
    |H_k(z)-k^2|<=8*9^k*|z|           (|z|<=1/8).       (3)

These estimates use neither L964's negative-margin hypothesis nor
its margin-dependent eta. Their standard inputs are the Cauchy
formulas [DLMF 1.9.30-31](https://dlmf.nist.gov/1.9.E31) and the
analytic Taylor theorem [DLMF 1.10.1](https://dlmf.nist.gov/1.10.E1),
version 1.2.8, already specialized in L964 on the radius-1/4 circle.
There is no need to reprove them or the imported paired Li identity.

For each fixed k,u, (2)-(3) give

    sum_j |beta_j H_k(beta_j)| <=9^k A,
    sum_j |beta_j^2 H_k(beta_j)/(beta_j+u)| <=9^k A.       (4)

Thus both sums defining E_n(k) are absolute. Subtracting gives
L964(12)'s exact complete eta error at this common u:

    E_n(k)=-u sum_j beta_j H_k(beta_j)/(beta_j+u)
          =-k^2 F_u+r_k,                               (5)
    F_u=u sum_j beta_j/(beta_j+u),
    r_k=-u sum_j beta_j[H_k(beta_j)-k^2]/(beta_j+u).

Each split series is absolute, with explicit bounds

    sum_j |u beta_j/(beta_j+u)| <=A,
    sum_j |u beta_j[H_k(beta_j)-k^2]/(beta_j+u)|
          <=8*u*9^k sum_j |beta_j|.

The first bound uses |beta_j+u|>=u. The second uses both (3)
and |beta_j|/|beta_j+u|<=1. Therefore, for the one fixed terminal n,

    |F_u|<=A,
    |r_k|<=A*9^(k-n)/8,               1<=k<=n.          (6)

Conjugation preserves the paired beta multiset with multiplicities
and H_k has real coefficients, as established in L964's unconditional
paired construction. All denominators respect conjugation and are
nonzero by (2). Absolute convergence therefore makes all these sums
real. The absolute bounds would hold without this last observation.
No interchange of an n-limit with a zero sum has been used.

For completeness, the exact first two errors in (5) can also be written
without remainder notation. P_1=1 and P_2=2 give

    E_n(1)=-u sum_j beta_j/
                         [(beta_j+u)(1+beta_j/4)],
    E_n(2)=-4*u sum_j beta_j/
                         [(beta_j+u)(1+beta_j/4)^2].     (7)

These are the same absolutely convergent expressions, at u=eta_n,
not at eta_1 or eta_2. No positive initial margin is asserted.

### Finite triangular summation with both endpoints

Import finite summation by parts,
[DLMF 2.10.9-10](https://dlmf.nist.gov/2.10.ii), web edition
inspected 10 November 2026 in the saved source comparison. It is an
identity for finite complex sequences, so its use does not require
real phases, a positive measure, or a convergent infinite Fourier sum.
The following short specialization checks the exact endpoints.

Put d_k=E_n(k+1)-E_n(k) for 1<=k<=n-1. Then

    T_n=sum_{k=2}^{n-1}(n-k)(d_k-d_{k-1})
       =sum_{k=2}^{n-1}d_k-(n-2)d_1
       =E_n(n)-(n-1)E_n(2)+(n-2)E_n(1)
       =E_n(n)-J_n.                                   (8)

Indeed every d_k with 2<=k<=n-2 has coefficient
(n-k)-(n-k-1)=1; d_(n-1) has coefficient 1 and d_1
has coefficient -(n-2). For n=3 the sum consists of
d_2-d_1, which gives the same formula. This is a finite
identity; all node sums were already proved absolute in (4)-(6).

Define only for the remainder calculation

    j_r=(n-1)r_2-(n-2)r_1.

Substitution of (5) in J_n and (8) yields exactly

    J_n=-(3n-2)F_u+j_r,
    T_n=-(n-1)(n-2)F_u+r_n-j_r.                        (9)

Both coefficients of F_u have nonnegative magnitude for n>=3,
and their sum is n^2. Thus (6) and the triangle inequality give

    B_n<=n^2|F_u|+|r_n|+2|j_r|
       <=A*n^2+(A/8)*[1+2(n-1)9^(2-n)
                                  +2(n-2)9^(1-n)].    (10)

This bounds both |J_n| and |T_n| separately through (9); it
does not merely bound the potentially cancelling sum J_n+T_n.

The positive sequences (n-1)9^(2-n) and (n-2)9^(1-n),
for n>=3, decrease: their successive ratios are respectively
n/[9(n-1)]<=1/6 and (n-1)/[9(n-2)]<=2/9. Evaluating
their maxima at n=3 therefore bounds the bracket in (10) by

    1+4/9+2/81=119/81.

This proves the first inequality in (1). Finally 119/648<1
and n^2>=9, so n^2+119/648<n^2+1<16*n^2. Since A>0,
the requested strict comparison follows.

### Relevance, reuse and limitations

The prior SPECIALIZE assessment for this exact B_n test is
`drafts/literature/2026-11-10-triangular-eta-error-review-201.md`.
The proof reuses L964's analytic and paired-identity inputs and
standard finite summation. Its local addition is the complete
terminal-n budget (10), including exact initialization. It makes
no originality claim beyond the sources checked. L972's successful
fixed-index movement bound and L973's RH-conditional convexity
obstruction are comparisons, not premises of this calculation.

The polynomial error can be paid in a future all-epsilon
subexponential Li lower-bound argument, if its independent signed
forcing estimate is established. L968 supplies the cited downstream
criterion. Equations (8)-(10) alone give no such forcing estimate:
rewriting an unknown lambda_n as its cumulative second differences
does not bound it below. All-n signs, the complete L966 inequality
R_n<=N_n, and any further change of parameters or unsmoothing remain
separate obligations. No theta resolvent partial fractions, finite
head replacement, numerical zeros, or RH-dependent bounded phases
enter (1). All nodes and all multiplicities remain in every sum.

### Independent proof audit, step203

The audit accepts (1)-(10) within the previously approved SPECIALIZE
scope. It checks the unconditional portions of L964 directly, rather
than importing its negative-margin conclusion. In particular its
binomial bound on the radius-1/4 disk gives |H_k|<=9^k, and the
Cauchy geometric remainder on |z|<=1/8 is
9^k*4|z|/(1-4|z|)<=8*9^k|z|. The actual nodes satisfy the stricter
|beta|<1/16. From alpha=x+iy with |x|>4 and |y|<1/2,
Re(beta)=(x^2-y^2)/(x^2+y^2)^2>0. Both denominator inequalities
in (2) therefore hold without RH.

For convergence, (4) dominates both original sums by 9^k|beta|.
The split constant term is dominated by |beta|, while the remainder
term is dominated by 8*u*9^k|beta|. These are separate summable
majorants at every fixed n and k. With u=1/(64*9^n), the latter
constant is exactly 9^(k-n)/8. No tail estimate uniform as n tends
to infinity is required or used. Conjugation preserves multiplicity
and each rational summand; it licenses reality after absolute
convergence. The lambda normalization is exactly L964(7)'s ordinary
Li normalization, also used in the audited downstream L968.

The finite identity (8) has coefficients -(n-2) at d_1 and 1
at every d_k for 2<=k<=n-1, including n=3. Applying it to the
quadratic part -k^2 F_u gives -(3n-2)F_u in J_n and
-(n-1)(n-2)F_u in T_n. Their absolute coefficient bounds add to
(3n-2)+(n-1)(n-2)=n^2. The exact first two errors in (7) follow
from H_1(z)=(1+z/4)^(-1) and H_2(z)=4(1+z/4)^(-2);
both use the same terminal u. No diagonal-in-index substitution
or assumed positive initial value enters the audit.

The remaining endpoint bounds are
|j_r|<=(A/8)[(n-1)9^(2-n)+(n-2)9^(1-n)] and
|r_n|<=A/8. Each geometric-polynomial sequence decreases from
n=3 by the ratios displayed in the proof. Thus the full bracket
is at most 1+4/9+2/81=119/81, yielding exactly 119/648 after
multiplication by 1/8. The strict comparison to 16*n^2 follows
for all n>=3. This checks the separate absolute budgets, rather
than only |J_n+T_n|, and finds no missing endpoint or constant.

No repair, new mathematical input or stronger conclusion is needed.
This is verification of a local reproduction, not a new result beyond
the checked sources. The direct mathematical inputs in the DAG remain
L024, L026 and L964; L968 is a downstream use, and L972/L973 remain
comparisons. A future signed-forcing mechanism still needs independent
coverage and proof. Mathlib coverage remains unknown.

## Mathlib

Full matching coverage of this common-terminal eta error budget has
not been checked and is unknown; no Mathlib theorem is imported.
General finite-summation, complex-field, Cauchy or summability support
would not alone certify the complete-sum normalization and explicit
constant in (1). Reference portal:
[Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
