# Corollary C028p: arbitrary positive theta dilation companion cost floor

## Hypotheses

Use the full kernel K of L019, the probability measure of C028o,

    Z=2*integral_0^infinity K(u)du,
    dmu(u)=K(|u|)du/Z on R,

and the actual centered monic polynomial Q_d and last-column,
subdiagonal companion A_d of C028h, for integers d>=3. In particular,
C028a and C028h give fixed actual constants S_2,S_3>0 and

    Q_d(x)=x^d-a_d*x^(d-2)+b_d*x^(d-3)+lower-degree terms,
    a_d=binom(d,2)*S_2,
    b_d=2*binom(d,3)*S_3.

For d=3 there are no lower-degree terms. The degree d-1 coefficient
is zero. All statements concern these actual coefficients, without
RH, hyperbolicity or simple-root assumptions.

Let p_n be the monic orthogonal polynomials for mu, with

    h_n=integral p_n^2 dmu,
    beta_n=h_n/h_(n-1)>0, n>=1,
    T_n=sum_(k=1)^n beta_k.

For any s>0, allowed to depend arbitrarily on d, define

    G_d(s)=(integral (s*u)^(i+j)dmu(u))_(0<=i,j<d),
    G_d(s)=S_d(s)^T*S_d(s),
    B_d(s)=S_d(s)*A_d*S_d(s)^(-1),
    K_d(s)=||(B_d(s)-B_d(s)^*)/(2i)||_1.

The Cholesky factor is upper triangular with positive diagonal;
the norm is the Schatten trace norm. No translation, tilt, truncation,
changed measure shape, fitted roots, unknown symmetrizer, recurrence
asymptotic or bounded condition number is assumed. Write H_d for the
total absolute imaginary root height of C028b, with multiplicities.

## Conclusion

For every integer d>=3 and every s>0,

    H_d <= K_d(s),
    K_d(s) >= c*d,
    c=min{sqrt(S_2)/2, 4*S_3/(27*S_2)}>0.                 (1)

More precisely, write p_j^(s)(x)=s^j*p_j(x/s) and expand

    Q_d=p_d^(s)+sum_(j=0)^(d-1) alpha_(d,j)(s)*p_j^(s).

Then the full cost, retaining every residual, is

    K_d(s)^2=sum_(j=0)^(d-2)
        s^(2j-2d+2)*(h_j/h_(d-1))*alpha_(d,j)(s)^2.       (2)

The top residuals are exactly

    alpha_(d,d-1)=0,
    alpha_(d,d-2)=s^2*T_(d-1)-a_d,
    alpha_(d,d-3)=b_d.                                  (3)

Their two contributions alone force (1). Thus no positive scale
sequence s_d makes this prescribed full-theta companion cost o(d).
This stops the dilation family's proposed upper payment of C028b's
height criterion. It does not lower-bound H_d, produce any nonreal
root or resolve RH. It is a finite specialization of a known method,
not a new general companion theorem. Independent audit1715 below
confirms the stated all-scale stop.

## Proof

### Imported interface and applicability

Gerhard Schmeisser, *Estimates for the Imaginary Parts of the Zeros of
a Polynomial*, Mathematica Balkanica 16 (2002), 203-217,
[Lemmas 1, 4, 5, pp.211-213, and Theorem 1 proof, pp.213-214](https://www.math.bas.bg/infres/MathBalk/MB-16/MB-16-203-217.pdf),
supplies the orthogonal-polynomial companion representation and its
imaginary-part trace norm. For a real monic f=p_d+sum a_j*p_j in a
monic orthogonal basis of a positive measure with infinite support
and all moments, the correction entries are
-a_j*sqrt(h_j/h_(d-1)). In the real case with a_(d-1)=0, its Hermitian
imaginary part has two possible nonzero eigenvalues +/-I/2, where
I^2=sum_(j=0)^(d-2) a_j^2*h_j/h_(d-1). Its trace norm is I.
Lemma 1 bounds total absolute imaginary eigenvalue parts by that
norm, including algebraic multiplicities. No real-root premise is
imposed. These general results are imported, not reproved.

NIST [DLMF 18.2(iv), equations 18.2.11_4-18.2.11_8, and
18.2.21](https://dlmf.nist.gov/18.2) supplies the monic recurrence,
norm ratios and even-measure parity used in C028o. The already saved
assessment1712 and source-notes1694/approval1696 cover these exact
interfaces. The additional work here is the arbitrary-scale norm
specialization and a finite two-residual inequality. C028o's
fixed-scale divergence is a comparison, not a premise for a uniform
conclusion.

L019 gives a strictly positive density and integrable superexponential
domination. As verified in C028o, Z is finite and positive, mu has
all absolute moments, and every nonempty interval has positive mass.
Thus all h_n are finite and positive. For each s>0, the image measure
nu_s of mu under u->s*u has the same properties, including infinite
support. Every nonzero polynomial has positive squared integral for
nu_s, so G_d(s) is positive definite and its stated Cholesky factor
exists. The imported hypotheses hold separately in every degree and
at every positive scale. No uniform moment bound in s is required.

### Actual coordinates and full cost at scale s

The scaled monic polynomials p_j^(s) are orthogonal for nu_s and have
squared norms

    h_j^(s)=s^(2j)*h_j.                                 (4)

For column monomial coordinates v, the norm is
v^*G_d(s)v=||S_d(s)v||_2^2. The upper triangular S_d(s)^(-1) has
as its columns the monomial coefficient vectors of
p_j^(s)/sqrt(h_j^(s)): those columns are orthonormal, have successive
degrees, and have positive leading coefficients. Uniqueness of
Gram-Schmidt identifies them. Hence orthonormal coordinates are
S_d(s)v. The quotient multiplication map f->x*f modulo Q_d has
matrix A_d in monomial coordinates by C028h's companion convention,
and therefore has exactly B_d(s) in these orthonormal coordinates.
This is an identification of the specified norm, not merely an
isospectral matrix substitution.

Evenness gives the recurrence

    u*p_n=p_(n+1)+beta_n*p_(n-1),
    p_0=1, p_1=u.

At scale s its orthonormal Jacobi part has zero diagonal and symmetric
off-diagonals s*sqrt(beta_j). Reduction modulo Q_d changes only the
last column, giving the imported representation

    B_d(s)=J_d(s)-v_d(s)*e_(d-1)^T,
    (v_d(s))_j=alpha_(d,j)(s)*sqrt(h_j^(s)/h_(d-1)^(s)).

Here indices run from 0 to d-1 and J_d(s) is real symmetric. Both
Q_d and p_d^(s) have vanishing degree d-1 coefficient, so
alpha_(d,d-1)=0. Consequently v_d(s) is real and perpendicular to
the last coordinate. The imported real-case formula gives trace
norm ||v_d(s)||_2; using (4) gives exactly (2), with every summand
included. Lemma 1 gives H_d<=K_d(s), since Q_d is the real translate
of the normalized reciprocal polynomial in C028b. Translation and
nonzero normalization preserve imaginary parts and multiplicities.

### Exact quadratic and cubic residuals

C028o's finite recurrence computation gives

    p_d(u)=u^d-T_(d-1)*u^(d-2)+lower-degree terms.

Parity says p_n(-u)=(-1)^n*p_n(u). In particular p_d has no term
of degree d-3, and p_(d-2) has no term of degree d-3. After scaling,
the degree d-2 coefficient of p_d^(s) is -s^2*T_(d-1), while these
two parity vanishings persist. Comparing the leading coefficients
in the expansion, in descending order, first gives
alpha_(d,d-1)=0, then alpha_(d,d-2)=s^2*T_(d-1)-a_d.
At degree d-3 neither p_d^(s) nor the already determined
alpha_(d,d-2)*p_(d-2)^(s) contributes. The vanished degree d-1
residual contributes nothing either. The remaining monic polynomial
p_(d-3)^(s) therefore has coefficient alpha_(d,d-3)=b_d.
These statements include d=3, where p_0^(s)=1 and p_1^(s)=x.
This proves (3); no symmetric-reference replacement of b_d was made.

In (2) the two relevant norm factors are exactly

    s^(-2)*h_(d-2)/h_(d-1)=1/(s^2*beta_(d-1)),
    s^(-4)*h_(d-3)/h_(d-1)
        =1/(s^4*beta_(d-1)*beta_(d-2)).

All other summands in (2) are nonnegative. Thus, with
T=T_(d-1), beta=beta_(d-1), gamma=beta_(d-2),

    K_d(s)^2 >= (s^2*T-a_d)^2/(s^2*beta)
                   + b_d^2/(s^4*beta*gamma).             (5)

For d=3 these are all summands. For larger d (5) is only a lower
bound; no small retained diagnostic would upper-bound the full cost.

### Uniform inequality over every positive scale

All of T,beta,gamma are positive, and the two distinct indices d-1
and d-2 occur in T because d>=3. Hence

    T/beta>=1,
    T^2/(beta*gamma)>=(beta+gamma)^2/(beta*gamma)>=4.      (6)

Set t=s*sqrt(T)/d>0, A=a_d/d^2 and B=b_d/d^3. Direct substitution
in (5), retaining every power of d and s, gives

    K_d(s)^2/d^2 >= (T/beta)*(t^2-A)^2/t^2
                        + (T^2/(beta*gamma))*B^2/t^4
                  >= (t^2-A)^2/t^2+4*B^2/t^4.           (7)

The exact binomial factors give, for every d>=3,

    0<A=(S_2/2)*(1-1/d)<=S_2/2,
    B=(S_3/3)*(1-1/d)*(1-2/d)>=2*S_3/27>0.              (8)

There are two exhaustive scale ranges. If t^2>=S_2, then A<=t^2/2,
so t^2-A>=t^2/2>0. The first term of (7) is at least

    (t^2-A)^2/t^2 >= t^2/4 >= S_2/4.

If t^2<=S_2, its second term is at least

    4*B^2/t^4 >= 4*(2*S_3/27)^2/S_2^2
                 =16*S_3^2/(729*S_2^2).

Both arguments hold at the common boundary. The smaller of these
positive constants bounds (7) for every t>0, hence every s>0.
Taking nonnegative square roots proves (1), with onset d=3 and
without optimizing a grid, assuming a recurrence limit, or exchanging
any infinite sums or limits. The scale transformation is legitimate
for each d because T>0 and is independent of s.

### Consequence and limits

For any positive sequence s_d, (1) gives liminf K_d(s_d)/d>=c>0.
The required upper payment K_d(s_d)=o(d) is therefore impossible
within this dilation family. C028b's equivalence concerns the actual
H_d, whose only comparison here is H_d<=K_d(s_d). It cannot be
reversed: this floor yields neither H_d>=c*d nor any off-line zero.
Actual H_d=o(d), compact limiting mass, signed cancellation and
actual-Xi positivity remain unresolved. The stronger fixed-scale
divergence in C028o is preserved, and no scope beyond the nominated
positive dilations of the full measure is claimed here.

### Independent proof audit1715 — 19 November 2026

This audit uses unchanged assessment1713, separately approved by1714
before invocation. The Schmeisser/DLMF interfaces above are reused;
no new source scope or general theorem is asserted. The local inputs
are L019's kernel and moment domination, C028a/h's exact centered
coefficients and companion convention, C028o's finite recurrence
calculation, and C028b for the interpretation of H_d. The earlier
fixed-scale and diagonal-metric floors are not used as all-scale bounds.

For each fixed d>=3 and s>0, positivity of the full density and finiteness
of every moment make G_d(s) positive definite. Let E=S_d(s)^(-1).
Then E^T*G_d(s)*E=I. Column j of E has degree j and positive leading
coefficient, so it is the coefficient vector of
p_j^(s)/sqrt(h_j^(s)), not of an unnormalized monic polynomial.
Monomial coordinates c=E*z therefore give orthonormal coordinates
z=S_d(s)*c. Multiplication and reduction modulo Q_d give exactly
z'=S_d(s)*A_d*E*z. This verifies the specified similarity and all its
columns, not merely an isospectral representation.

The scaled orthonormal recurrence gives internal symmetric entries
s*sqrt(beta_j). At the final column the unreduced extra term is
p_d^(s)/sqrt(h_(d-1)^(s)); setting Q_d=0 replaces it by the negative
of the stated residual vector v_d(s). Thus B_d(s)=J_d(s)-v_d(s)*e^T,
where e is the final unit vector and J_d(s) is real symmetric.
Comparison of the degree d-1 coefficient gives v_d(s)^T*e=0.
If r=||v_d(s)||_2>0, the Hermitian imaginary part on the orthonormal
pair (v_d(s)/r,e) is

    [ 0  i*r/2; -i*r/2  0 ].

It vanishes on the perpendicular complement. Its two eigenvalues
are r/2 and -r/2, giving trace norm r. If r=0 the whole imaginary
part is zero. Together with h_j^(s)=s^(2j)*h_j this independently
checks (2), including the exponent 2j-2d+2 and the absence of a
missing factor two. The imported eigenvalue majorization applies
without normality or diagonalizability and counts all multiplicities.

The recurrence coefficient of u^(d-2) in p_d is -T_(d-1), while
parity removes its u^(d-1) and u^(d-3) terms. The coefficient of
x^(d-2) after scaling is therefore -s^2*T_(d-1). The vanished
degree d-1 expansion coefficient cannot affect the next two terms;
p_(d-2)^(s) has no x^(d-3) term either. Descending comparison gives
precisely s^2*T_(d-1)-a_d and b_d, with their signs as in (3).
For d=3 specifically, p_3^(s)=x^3-s^2*(beta_1+beta_2)*x,
Q_3=x^3-3*S_2*x+2*S_3, and the residuals multiply p_1^(s)=x
and p_0^(s)=1. The complete squared cost is then

    (s^2*(beta_1+beta_2)-3*S_2)^2/(s^2*beta_2)
        +4*S_3^2/(s^4*beta_2*beta_1).

In every degree the same two distinct indices are d-1 and d-2;
their norm ratios are exactly those in (5). All remaining terms
in (2) are nonnegative and are dropped only for a lower bound.

To check (7) directly, s^2=d^2*t^2/T and a_d=d^2*A give
(s^2*T-a_d)^2/(d^2*s^2*beta)=(T/beta)*(t^2-A)^2/t^2.
Similarly b_d=d^3*B gives
b_d^2/(d^2*s^4*beta*gamma)=T^2*B^2/(beta*gamma*t^4).
Since d>=3, both positive beta and gamma occur in T; hence T/beta>=1
and T^2/(beta*gamma)>=4. No recurrence estimate or limiting argument
enters these inequalities. The exact degree factors give A<=S_2/2
and B>=2*S_3/27, with equality in the latter at d=3.

The positive half-line is exhausted by t^2>=S_2 and t^2<=S_2.
In the first range, A<=t^2/2 makes the first retained term at least
t^2/4>=S_2/4. In the second, 1/t^4>=1/S_2^2 makes the second at
least 16*S_3^2/(729*S_2^2). Both checks include the boundary.
Taking the square root of the smaller bound yields exactly
c=min{sqrt(S_2)/2,4*S_3/(27*S_2)}. It is strictly positive by the
actual constants in C028a. The substitution covers every s>0 for
each d because T>0; no grid, asymptotic recurrence input, or scale
restriction has been inserted. Thus the conclusion holds already at d=3.

Finally Q_d(y)=P_d(y-b_1), P_d=R_d/gamma_0, with b_1 real and
gamma_0 nonzero. Its root multiset has the same imaginary heights
as R_d, including multiplicities. This checks H_d<=K_d(s) in its
stated direction. Neither that comparison nor the cost floor implies
a lower bound on H_d. Verdict: no defect found; retain stop1713 for
exactly this positive-dilation family. This audit validates a local
known-method specialization without adding a new estimate or resolving
compact mass, signed cancellation, H_d=o(d), or actual-Xi positivity.

## Mathlib

Not checked. Full matching coverage of the specified scaled Gram
similarity and its uniform two-residual floor is unknown. Supporting
orthogonal-polynomial and matrix statements are imported from the
precise sources above. No formal verification or absence claim is made.
