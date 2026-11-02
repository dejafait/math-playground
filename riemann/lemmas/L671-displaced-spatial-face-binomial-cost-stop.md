# Lemma 671: the complete spatial face loses at least a fixed linear rate

## Hypotheses

Use L666's exact displaced family. Thus q>=1 is an integer,
n=12q+3, M=4q+1=n/3, J=n-1, x=-d=-5/4, R=11/8,
U=121/64, H_0=27/(10n), t_j=j/n, and

    Z={x} union {x+i*H_0*(r+1/2+e_r): -2q<=r<2q},
    e_r real, |e_r|<=1/8.

Every original residue is one, the same poles serve all angles, and
every grid factor including j=0 and the denominator angle 1/u remains:

    B_u(v)=product_(0<=j<n) R*(v-t_j*u)/(U-t_j*v/u),
    W_a(u)=B_u(x)/B_u(a),
    G(u,zeta)=R^(-1) sum_(a in Z) W_a(u) H_M(a*zeta/R),
    H_M(v)=sum_(k=0)^(M-1) v^k,
    H=max_(|u|=1) mean_(|zeta|=1) log|G(u,zeta)|.

All means are normalized; logarithms are natural. Use precisely
L657's clearing, with no canceled factor removed:

    A_a(u)=product_(j=1)^J(a-t_j*u),
    C_a(u)=product_(j=1)^J(U*u-t_j*a),
    Q(u)=C_x(u) product_(a!=x) A_a(u),
    K_0(u)=R^(-1)[Q(u)+sum_(a!=x) (x/a)*A_x(u)*C_a(u)
                                      *product_(b!=x,a) A_b(u)],
    G(u,0)=c_0(u)=K_0(u)/Q(u),
    D_ang=MJ,
    L_Q=mean_(|u|=1) log|Q(u)|
       =J log U+J sum_(a!=x) log|a|.

For the complete bottom spatial face K_0 define the exact certificate

    B_face=max_(0<=h<=D_ang, [u^h]K_0!=0)
      {log|[u^h]K_0|-log binomial(D_ang,h)-L_Q}.

This is the ordinary one-variable degree-index coefficient transfer.
It is not a support-index bound, a coefficient of a different clearing,
or a root estimate for the complete spatial polynomial.

## Conclusion

K_0 has exact degree D_ang and is nonzero for every allowed vector.
The certificate is applicable to the full spatial logarithmic maximum:

    H >= B_face.                                             (1)

However, for every h, including the endpoints, uniformly on the
entire displacement cube,

    |[u^h]K_0| <= exp(L_Q)*(M/R)*(4/5)^J
                                      *binomial(D_ang,h),      (2)
    B_face <= log(M/R)+J log(4/5)
            < log(M/R)-J/5.                                  (3)

In particular, for every fixed real C,

    B_face+n/100+C log n
      < -(19/100)n+(C+1)log n+1/5-log(3R) -> -infinity.        (4)

Thus this face transfer cannot prove H>=-n/100-C log n uniformly.
The stop applies even to the undeformed admissible sequence e_r=0,
where L664 separately proves a much stronger bound for H. It is an
upper bound for the exact certified value B_face, not an upper bound
for H or a counterexample to its target inequality.

No exceptional-support or symmetry condition is needed in (2)--(4).
The assertion concerns this complete clearing with its actual
degree-index cost. Sparse support-index estimates, other clearings,
signed root estimates and direct angular estimates are not decided.
Support, Xi realization and actual mixed positivity remain independent.
This local method obstruction is unaudited and supplies no RH candidate
or certified claim of originality beyond the sources compared.

## Proof

### 1. Sources, overlap, and applicability of the face transfer

Reuse the invocation-start EXPLORE assessment
`drafts/literature/2026-11-02-displaced-angular-maximum-linear-rate.md`.
Its inherited univariate comparison is
`drafts/literature/2026-11-02-displaced-full-spatial-fixed-angle.md`.
Import S. Akhtari and J. D. Vaaler, *Lower bounds for Mahler measure
that depend on the number of monomials*, arXiv:1810.12413v1,
29 October 2018, [equation (1.3), p.1; Theorem 1.1, p.2, and
Section 2, pp.4--5](https://arxiv.org/pdf/1810.12413v1).
The classical degree-index inequality recorded there states that a
nonzero complex polynomial P of degree D satisfies

    |[u^h]P| <= binomial(D,h)*exp(mean_u log|P(u)|).

No integrality, coefficient sign or root separation is required.
The inherited assessment inspected the univariate proof, including
endpoint indices. This known inequality is imported, not reproved.
The family-specific work below bounds its actual normalized
coefficients; a generic coefficient lower bound does not supply that
upper bound or decide whether this particular certificate is useful.

The spatial Jensen input, including boundary roots, is F. Brunault
and W. Zudilin, *Many Variations of Mahler Measures*, ISBN
9781108794459, [Proposition 1.4, publisher excerpt pp.6--7](https://assets.cambridge.org/97811087/94459/excerpt/9781108794459_excerpt.pdf).
L657 imports this formula and the absolute logarithmic integrability
input from Z. Issa and M. Lalin, *A generalization of a theorem of
Boyd and Lawton*, [arXiv:1203.5379v1, Remark 3.8 and Theorem 4.1
with proof, p.7](https://arxiv.org/pdf/1203.5379v1), 24 March 2012.
L658 gives finiteness and attainment of H. These source comparisons
are ready; no additional theorem or general-theorem reproof is used.

L670's endpoint identity gives

    [u^D_ang]K_0=lc(Q)*p_0,
    p_0=(x/R) sum_(a in Z) 1/a,
    Re p_0=(1/R) sum_(a in Z) d^2/|a|^2>0.                    (5)

Here lc(Q)=U^J[(-1)^J product_(j=1)^J t_j]^(M-1)!=0.
The identity also follows immediately from W_a(infinity)=x/a:
in (x/a)A_x C_a/(A_a C_x), both ratios tend to one.
This checks the only endpoint identity used here, without repeating
the prior endpoint-cost estimates or upgrading L670's full audit
status. Equation (5) proves exact degree D_ang. Since Q has no
angular circle zeros, log|c_0| is integrable, including the finitely
many possible circle zeros of K_0.

For each circle u with c_0(u)!=0, the cited spatial root formula
gives m(u)=mean_zeta log|G(u,zeta)|>=log|c_0(u)|.
At c_0(u)=0 the same inequality holds with right side -infinity.
The nonzero full spatial slices and integrability of m are supplied
by L657. Integration and maximum-versus-mean therefore give

    H >= mean_u m(u) >= mean_u log|c_0(u)|
       =mean_u log|K_0(u)|-L_Q
       >= log|[u^h]K_0|-log binomial(D_ang,h)-L_Q.              (6)

Taking the finite maximum proves (1). No spatial moment is removed
from H; choosing c_0 is only a sufficient lower certificate for it.
No uniform root-motion estimate or exchange of a growing-degree
limit with an integral occurs.

L670 concerns exposed joint coefficients on a dense set, whereas
this test restricts to the spatial face before applying the
one-variable bound to every angular index. L667/L668's inverse costs
and L669's fixed-angle countersequence are contrasts, not inputs.
The existing full-circle stop is preserved: (6) is a sufficient
transfer, not an assertion that full-circle averaging must work.

### 2. A coefficient envelope for each paired block

For a polynomial F(u)=sum_h f_h u^h, write
F^abs(v)=sum_h |f_h|v^h, where v is a formal variable. For
polynomials with nonnegative real coefficients use coefficientwise
order. The finite convolution formula and triangle inequality give

    (F_1 F_2)^abs <= F_1^abs F_2^abs,
    (F_1+F_2)^abs <= F_1^abs+F_2^abs.                         (7)

These are finite algebraic identities/inequalities, not a cited
norm-comparison theorem. Coefficientwise order is preserved by
multiplication by a polynomial with nonnegative coefficients.

L666's family bounds give d<=|a|<R-1/100=273/200 for every pole.
In particular

    |a|/U <= (273/200)/(121/64)=2184/3025 < 3/4,
    1/|b| <=4/5.                                            (8)

For any poles a,b and any 0<t<1, consider one normalized pair

    F_(a,b,t)(u)=(u-t*a/U)*(b/|b|-t*u/|b|).

Its constant, middle and top coefficient moduli are respectively
bounded by

    t|a|/U <=3/4,
    |b/|b|+t^2*a/(U|b|)| <=1+(3/4)(4/5)=8/5,
    t/|b| <=4/5.

Since 3/4<=4/5, these three inequalities say exactly

    F_(a,b,t)^abs(v) <= (4/5)(1+v)^2.                       (9)

Every remaining normalized linear A factor satisfies

    (b/|b|-t*u/|b|)^abs(v) <=1+v.                           (10)

The pair estimate uses the actual two coefficients and the triangle
inequality for its middle coefficient. It assumes no positivity of
the original complex coefficients. There is no binomial factor yet;
that factor appears on multiplying all retained factors in (9)--(10).

### 3. Exact normalization and all indices

Set E=exp(L_Q)=U^J product_(b!=x)|b|^J. The anchor term is

    Q/E=(C_x/U^J) product_(b!=x) (A_b/|b|^J).

There is at least one nonanchor pole, since M>=5. Choose one such
b. Pair its J normalized A factors with the J factors of C_x/U^J,
using the same t_j in each pair. This uses J instances of (9).
There are (M-2)J unpaired normalized A factors, each covered by
(10). Equations (7), (9) and (10) yield

    (Q/E)^abs <= (4/5)^J(1+v)^(2J+(M-2)J)
              = (4/5)^J(1+v)^D_ang.                         (11)

For a nonanchor a write its exact numerator term as

    N_a=(x/a)A_x C_a product_(b!=x,a) A_b.

Dividing by E, with every normalization factor accounted for, gives

    N_a/E=(x/a)*(d/|a|)^J
          *(A_x/d^J)*(C_a/U^J)
          *product_(b!=x,a)(A_b/|b|^J).                     (12)

The leading scalar in (12) has modulus (d/|a|)^(J+1)<=1.
Pair C_a/U^J with A_x/d^J using (9), and use (10) for the
(M-2)J remaining factors. Thus each of the M-1 nonanchor terms
obeys exactly the same envelope as (11). This accounts for the
j=0 factor x/a; it has not been replaced by a free residue.

Finally K_0=R^(-1)(Q+sum_(a!=x)N_a), so (7) gives

    (K_0/E)^abs <= (M/R)(4/5)^J(1+v)^D_ang.                 (13)

The binomial theorem at every 0<=h<=D_ang proves (2), including
zero coefficients. For a nonzero coefficient, subtracting the
prescribed log binomial(D_ang,h) and L_Q gives the first
inequality in (3). This is an upper bound for the exact certificate
after its full cost, even though the proof bounds its coefficients
by absolute envelopes. No such upper envelope is used to infer a
lower bound for the signed response.

### 4. Comparison with the required rate

Integrating 1/t on [1,5/4] gives log(5/4)>1/5. Therefore
J log(4/5)<-J/5. Substituting J=n-1 and M=n/3 in (3)
proves (4). The strictly negative linear coefficient 19/100 exceeds
any fixed logarithmic allowance at an absolute eventual onset for
that fixed C, uniformly over all displacement vectors. The undeformed
sequence e_r=0 is admissible for every q and suffices as a witness
to the failure of this certificate. In fact the estimate is stronger:
it stops the certificate on the entire allowed family.

This is only a transfer stop. In particular the strong undeformed
H bound from L664 is compatible with a very negative B_face, since
(1) is one-sided. L664 is a comparison and is not used to prove
(1)--(4). No new bound for H, arbitrary support or Xi signs follows.

## Mathlib

The inherited assessment records supporting results in
[Mathlib.Analysis.Polynomial.MahlerMeasure](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Polynomial/MahlerMeasure.html),
including `Polynomial.logMahlerMeasure_eq_log_leadingCoeff_add_sum_log_roots`,
`Polynomial.intervalIntegrable_mahlerMeasure`, and
`Polynomial.mahlerMeasure_mul`, and the degree-index bound
`Polynomial.norm_coeff_le_choose_mul_mahlerMeasure`. These support the imported
one-variable accounting, not the entire family-specific envelope or
its use in the full spatial mean. Full matching coverage has not
been checked, and unknown coverage is not evidence of absence.
No formal verification is asserted.
