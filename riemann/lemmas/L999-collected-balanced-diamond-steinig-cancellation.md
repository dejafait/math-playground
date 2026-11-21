# Lemma 999: exact cancellation of the balanced collected coefficient

## Hypotheses

Let n>=1 be an integer. Let K_n be the nonnegative integer vectors
k=(k_1,...,k_(2n)) with sum_j j*k_j=2n and
1<=|k|=sum_j k_j<=n. For positive-length vectors put

    c(k)=(-1)^(|k|-1) (|k|-1)! / prod_j k_j!,
    w(k)=prod_j (j!)^(-k_j).

Let H_n consist of ORDERED pairs (k',k'') of nonnegative vectors,
each with weighted sum n, each of positive length, with
|k'|+|k''|<=n. Extend these vectors by zeros through coordinate 2n.
In commuting formal variables Y_1,...,Y_(2n), define exactly

    T_n(Y)=2n sum_(k in K_n) c(k)w(k)Y^k
       +n^2 sum_((k',k'') in H_n)
          c(k')c(k'')w(k')w(k'')Y^(k'+k''),
    b_n(ell)=[Y^ell]T_n(Y),
    C_n=sum_ell |b_n(ell)|.

All contributions to a full exponent vector are collected before
absolute values, including across families; ordered pairs and all
factorial weights are retained. H_1 is empty. This is the formal
observable in review297, not an optimized arithmetic representation.

## Conclusion

For every integer m>=1, set n=3m and
ell=(m,m,m,0,...,0). Then

    b_(3m)(ell)=(-1)^m * 3*binom(2m,m)/12^m,                (1)
    |b_(3m)(ell)|<=3^(1-m).                                (2)

The complete collected coefficient is therefore exponentially
DECAYING, although the magnitude A_m of this vector's first-family
summand is exponentially growing as shown in L998. More exactly,

    A_m=6m*(3m-1)!/(m!)^3 *12^(-m),
    b_(3m)(ell) / [(-1)^(3m-1) A_m]
       =-1/binom(3m-1,m).                                  (3)

L998 is a comparison only, not a premise of (1)-(3).
This rejects the use of that particular balanced witness as a
positive-rate lower bound for C_n. It does NOT decide the limsup
log(max(1,C_n))/n, bound all other coefficients, or pay L984(H).

## Proof

### Source and scope

The finite c,w,K,H definitions are imported from O. Ramaré,
*On Bombieri's asymptotic sieve*, author preprint dated
28 October 2009, Section 2, (12)-(18), Lemma 4, printed pp8-9:
[primary preprint](https://ramare-olivier.github.io/Maths/V12BombieriSieve.pdf).
The prior SPECIALIZE assessment is
drafts/literature/2026-11-10-collected-diamond-steinig-rate-test-review-297.md;
the completed source comparison is review296. The source does not
assert (1), or a canonical collected norm theorem. The calculation
below is an elementary finite coefficient specialization, not a
reproof of the Diamond-Steinig arithmetic identity or a prime estimate.
No originality beyond the checked sources is asserted.

### Exact connection to formal logarithms

To extract ell=(m,m,m,0,...), set Y_j=0 for j>=4 and write

    E(t)=1+Y_1 t+Y_2 t^2/2+Y_3 t^3/6,
    F(t)=log E(t).

These are formal series over Q[Y_1,Y_2,Y_3]; coefficient extraction
at any fixed t-degree involves only finitely many terms. In
log(1+S)=sum_(r>=1) (-1)^(r-1)S^r/r, the coefficient of Y^k
is c(k)w(k)t^(sum j*k_j). Hence the coefficient of Y^ell in
2n[t^(2n)]F(t) is the first-family coefficient. Indeed ell has
length n, so the only contributing log term has r=n, which is
included in K_n; omitted higher-length terms cannot contribute.

Likewise the coefficient of Y^ell in n^2([t^n]F(t))^2 is the
entire second-family coefficient. Each factor has positive length
and weighted sum n; any contributing pair has total length |ell|=n,
so satisfies the prescribed cutoff. Multiplication sums over ordered
pairs, including coincident ones exactly once at their ordered index;
there is no symmetry quotient. Consequently

    b_n(ell)=[Y^ell] {2n[t^(2n)]F+n^2([t^n]F)^2}.          (4)

This extraction statement is only needed for this ell. No general
claim about cancellation outside the length cutoff is assumed.

### A finite cubic identity

Work in the algebraic closure of Q(Y_1,Y_2,Y_3). Factor
E(t)=prod_(i=1)^3 (1-x_i t), allowing roots with multiplicity.
The elementary symmetric functions of x_1,x_2,x_3 are

    e_1=-Y_1, e_2=Y_2/2, e_3=-Y_3/6.

For p_j=sum_i x_i^j, formal logarithmic expansion gives
[t^j]F=-p_j/j. Equation (4) thus extracts the coefficient
of Y^ell in p_n^2-p_(2n). The elementary identity

    p_n^2-p_(2n)=2 sum_(i<j)(x_i*x_j)^n                  (5)

retains all cross terms. If q_n denotes the sum on the right
without its factor 2, then

    G(u)=prod_(i<j)(1-x_i*x_j*u)
        =1-e_2 u+e_1*e_3 u^2-e_3^2 u^3
        =1-Y_2 u/2+Y_1*Y_3 u^2/6-Y_3^2 u^3/36,
    q_n=-n[u^n]log G(u).                                  (6)

The middle equality follows by multiplying the three factors:
their first, second and third elementary symmetric functions are
e_2, e_1*e_3, e_3^2 respectively. These are polynomial identities,
so the splitting-field calculation implies identities in the original
coefficient ring; no analytic convergence or choice of roots is used.

Put A=-Y_2 u/2, B=Y_1*Y_3 u^2/6 and D=-Y_3^2 u^3/36.
In log(1+A+B+D), a term containing Y_1^m must use B exactly m
times. This already supplies Y_3^m, so it must use D zero times.
It must then use A exactly m times to supply Y_2^m. The u-degree
is m+2m=3m, as required. The sole contributing log term therefore
has length 2m, and its complete coefficient is

    [Y_1^m Y_2^m Y_3^m u^(3m)]log G
       =(-1)^(2m-1)*(2m-1)!/(m!)^2 *(-1)^m/12^m
       =(-1)^(m+1)*(2m-1)!/((m!)^2*12^m).                 (7)

By (4)-(6), multiply (7) by -2n=-6m to obtain
(-1)^m*6m*(2m-1)!/((m!)^2*12^m), which equals (1).
The binomial theorem gives binom(2m,m)<=2^(2m); this proves (2).
The first-family term has magnitude A_m and sign (-1)^(3m-1).
Division of the two explicit factorial expressions yields (3),
including its minus sign. Thus the full ordered split sum is
accounted for, rather than discarded or estimated by its absolute sum.

### Interpretation and limitations

Formal equal-vector collection retains the number of log factors,
|ell|=n, and hence the mu convolution multiplicity in the source's
shorthand. No vectors are merged by weighted degree alone, and no
zero-degree factor, cancellation of mu*1, arithmetic-function
independence, or evaluation at numerical Y_j is used. Equation (1)
is solely a coefficient identity. No actual arithmetic norm follows.

The declining single coefficient cannot lower-bound C_n at a positive
exponential rate. Other vectors could still carry positive rate;
conversely, this calculation does not give a uniform upper bound.
L984(H), actual factor norms, signed correlations, Laguerre transfer,
prime powers, endpoints, compensation, both complements and regulator/
infinite-zero control remain unpaid. This is no RH candidate.

Exact finite diagnostics, separate from the general proof, are saved
by `python3 scripts/diamond_steinig/collected_mass_299.py` in
scripts/diamond_steinig/collected_mass_299_certificate.json. They
enumerate complete C_n for n<=12 and all ordered pairs, and check
(1) against direct split summation for m<=30. Finite samples are
not the proof of (1) and do not establish C_n's asymptotic rate.

## Mathlib

Full matching coverage for (1)-(3) and the collected norm is unchecked
and unknown. Formal logarithms, symmetric polynomials and the binomial
theorem are supporting standard mathematics; no matching Mathlib
theorem name has been verified. No absence claim is made.
