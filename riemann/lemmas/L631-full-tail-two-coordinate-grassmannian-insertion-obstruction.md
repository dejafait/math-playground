# Lemma 631: full-tail N=2 obstructs a scaled multiplicative orbit insertion

## Hypotheses

Use L623's full Gram form and L624's analytic arithmetic form at N=2,
with arbitrary complex a=(a1,a2), held fixed during differentiation.
All r=2^j, j>=0, are retained, and C_2(q)=D_2(q)^(-1) is differentiated.
Initially |Re q_j|<1/4. Set tau=log(2)/L for L>0; treating tau as an
independent parameter defines the fixed-N diagnostic polynomial below.

For I={i<j} subset {1,2,3,4}, |I|=2, write its complement J={k<l} and

    D_I(z)=product_(u in I,v in J)(z_u-z_v),
    ell_I(z)=(sum_I z-sum_J z)/2,
    q_I(z)=(z_i,z_j,-z_k,-z_l)/L,
    S=-1/2 (partial_z1-partial_z2)^2 partial_z3 partial_z4.

L629's complete leading germ and signed form are

    F_(2,L)(z;a)=sum_I exp(ell_I(z)) B_2(q_I(z);a)/D_I(z),
    Q_(2,L)(a)=5040 Re (S F_(2,L))(0).

The six terms are combined and extended across collisions before
differentiation, as in L629. Only that finite algebraic prescription is
used here; L629's analytic Xi transfer and its audit qualifications are
not strengthened. No sign, zero-free or RH hypothesis is imposed.

Let P be a Haar rank-two orthogonal projection on C^4, R=I-P, and
Z=diag(z1,z2,z3,z4). The proposed multiplicative insertion is

    F_tilde(z;a)=1/12 integral exp(tr(Z(P-I/2)))
          B_2(eig(PZP|range(P))/L,
                       -eig(RZR|range(R))/L;a) dP,          (1)
    Q_tilde(a)=5040 Re (S F_tilde)(0).

Each pair of eigenvalues is unordered. The symmetric analytic function
in (1) is defined holomorphically near Z=0 through matrix traces and
exponentials, not by choosing analytic eigenvalue branches. In particular
the formula in Section 1 below expresses it using tr(exp(-W)),
exp(-tr(W)) for the two compressed matrices. Compactness of the
projection space gives a common neighborhood and bounded derivatives.
No weighted-localization theorem or positivity of this insertion is
assumed.

The named orbit input is C. McSwiggen, *A new proof of Harish-Chandra's
integral formula*, [arXiv:1712.03995v3, (2), Theorem 1 and Section 3.4](https://arxiv.org/html/1712.03995v3),
with normalized Haar measure. Its real distinct-spectrum HCIZ formula
and analytic extension across repeated spectra were inspected in the
prior source comparison. Section 2 gives the necessary confluent
specialization; it does not reprove HCIZ or assume an amplitude rule.

## Conclusion

The scalar normalization passes: replacing B_2 by a constant Gamma
in either expression gives Q=Q_tilde=Gamma. The actual arithmetic
insertion fails. With u=a1 conjugate(a2), exactly

    Q_(2,L)(a)=|a1|^2+|a2|^2+sqrt(2) Re(u) P(tau),       (2)
    Gamma=|a1|^2+|a2|^2+(4 sqrt(2)/3) Re(u),

where the ascending coefficients of the degree-eight polynomial P are

    k       [tau^k] P
    0        4/3
    1       -16/9
    2       -385/27
    3       -14/27
    4        15680/81
    5       -227269/243
    6        914228/243
    7       -7929146/729
    8        34439992/2187.                              (3)

For the insertion (1), the cross coefficient starts instead at
4/3-(8/9)tau. Consequently

    [tau] {Q_(2,L)-Q_tilde}
                   =-(8 sqrt(2)/9) Re(a1 conjugate(a2)). (4)

In particular a=(1,1) disproves identity as a function of tau. More
generally, no expression

    5040 Re S {1/12 integral exp(tr(Z(P-I/2)))
                                     H(P,tau Z;a) dmu(P)}_(z=0) (5)

can equal (2) on an open tau interval for every a, if mu is fixed,
H has no tau dependence except its second argument, and H is
holomorphic in that argument near zero with locally integrable uniform
Taylor domination. Its signed extraction has degree at most four
in tau, whereas (2) has nonzero degree eight when Re(u) is nonzero.
Haar measure with the normalized full-tail amplitude in (1) satisfies
these hypotheses.

This stops the specified multiplicative insertion, including the
class (5). It neither proves nor refutes Q_(N,L)>=Gamma/2 for growing
N, supplies a negative direction, nor excludes representations with
spectral derivatives, additional tau dependence or varying measures.
N=2 is a diagnostic for a universal identity, not the large-L growing
family. Nonzero polynomial discrepancy rules out identity on any open
interval, including the interval with floor(exp(L/100))=2; it does not
assert a discrepancy at every isolated L. The result is a local,
independently unaudited obstruction, not a certified novelty claim.

## Proof

### 1. Close the infinite tail before differentiating

Put x=1/2, t=1/sqrt(2), X=2^(-alpha), Y=2^(-beta),
U=2^(-gamma), V=2^(-delta). Let

    h_j(X,Y)=sum_(e=0)^j X^e Y^(j-e),  h_(-1)=0,
    D=sum_(j>=0) h_j(X,Y)h_j(U,V)x^j,
    S_L=sum_(j>=0) h_(j+1)(X,Y)h_j(U,V)x^j,
    S_R=sum_(j>=0) h_j(X,Y)h_(j+1)(U,V)x^j.

These series and all fixed derivatives converge locally uniformly on
the stated shift domain: h_j and its derivatives are bounded by a
polynomial in j times 2^(rho j) on compact sets with rho<1/4.
The recurrence h_(j+1)=(X+Y)h_j-XY h_(j-1) therefore gives

    S_L=(X+Y)D-x XY S_R,
    S_R=(U+V)D-x UV S_L.

The scalar D is L624's D_2(q), and is analytic and nonzero there by
its explicit product formula. Solving the two equations gives

    R_L=S_L/D=(X+Y-x XY(U+V))/(1-x^2 XYUV),
    R_R=S_R/D=(U+V-x UV(X+Y))/(1-x^2 XYUV).              (6)

The denominator is nonzero on this domain. The two convolution
vectors at r=2^j are exactly

    A_(alpha,beta)(a;2^j)
       =a1 t^j h_j(X,Y)+a2 1_(j>=1)t^(j-1)h_(j-1)(X,Y),

and the analogous expression for the second pair and conjugate a.
Both diagonal sums equal D. The two off-diagonal sums equal t S_L
and t S_R. Multiplying by the full analytic C_2=D^(-1) proves

    B_2(q;a)=|a1|^2+|a2|^2+t(u R_L+conjugate(u) R_R).   (7)

Thus (6) already incorporates every normalization derivative and every
tail coordinate. At zero, R_L=R_R=4/3, giving the Gamma in (2).
No truncated tail or constant normalization has entered this argument.

In dimensionless variables w=(log 2)q, write

    r(w)=[exp(-w1)+exp(-w2)
             -(exp(-w1-w2-w3)+exp(-w1-w2-w4))/2]
                                  /[1-exp(-sum w)/4].    (8)

This is R_L; R_R interchanges the two pairs. Direct differentiation
at zero gives

    r(0)=4/3,   grad r(0)=(-4/9,-4/9,2/9,2/9).          (9)

In particular the pair average has first jet

    (r(w)+r(w3,w4,w1,w2))/2
                          =4/3-(sum w)/9+O(|w|^2).     (10)

### 2. Scalar HCIZ normalization and the first mismatch

For lambda nonzero and real initially, define

    F_lambda(z)=sum_I exp(lambda ell_I(z))/D_I(z),
    eta(P,Z)=tr(Z(P-I/2)).

The cited U(4) HCIZ formula has factor 1!2!3!=12. Conflate its
second spectrum to (lambda/2,lambda/2,-lambda/2,-lambda/2).
The limiting determinant has columns

    exp(lambda z/2), z exp(lambda z/2),
    exp(-lambda z/2), z exp(-lambda z/2).

Its Laplace expansion over the first two columns, divided by Delta(z),
is F_lambda. The two internal spectral differences cancel with the
column differences in the limit, leaving the four cross differences
lambda^4. Hence, with probability Haar measure,

    F_lambda(z)=lambda^4/12 integral exp(lambda eta(P,Z)) dP.
                                                               (11)

The analytic extension in the source handles repeated z; alternatively
the six-term collision cancellation gives the same continuation.
The factors and signs in (11) can be checked at real lambda>0 before
analytic continuation. We use it only near lambda=1. Since
F_lambda(z)=lambda^4 F_1(lambda z), homogeneity of S gives

    5040 S F_lambda(0)=lambda^8,
    5040 S {1/12 integral exp(lambda eta) dP}_(z=0)=lambda^4.
                                                               (12)

Here 5040 S F_1(0)=1 is L629's constant-amplitude coefficient;
the exact polynomial replay in Section 3 also checks it. This proves
the constant-amplitude normalization of both formulas.

Pair interchange in (8) replaces the full six-term germ at z by
the original one at -z: interchange I with its complement in the
sum. Because S has even order four, their signed values coincide.
For (1), the same equality follows by changing P to I-P and z to -z.
All Taylor coefficients are real for real tau. Thus only Re(u)
survives in both signed extractions, for all complex a. Their cross
coefficient can be computed from the pair average (10).

In the six-term sum, sum w=2 tau ell_I. Equations (10)-(12) therefore
give the first coefficient of its cross polynomial as

    -(2/9) partial_lambda(lambda^8)|_(lambda=1)=-16/9.

In (1), sum w=tau(tr(PZ)-tr(RZ))=2 tau eta(P,Z).
Differentiation under the compact orbit integral is justified by
the common analytic neighborhood noted in the hypotheses. Its first
coefficient is instead

    -(2/9) partial_lambda(lambda^4)|_(lambda=1)=-8/9.

Together with the factor 2t=sqrt(2) in (7), this proves (4).
The missing lambda^4 in a multiplicative insertion is an orbit-volume
factor, not a tail error. Keeping the scalar HCIZ normalization alone
does not keep this factor when amplitudes change the exponential.

### 3. Exact full signed polynomial

For completeness the whole N=2 diagnostic, not merely its first jet,
can be calculated by L629's finite polynomial prescription. Define
r_nu=[w^nu]r(w). With nu=(a,b,c,d), a>=b and c>=d, it gives

    [tau^k]P=5040 sum_(|nu|=k) w_(nu,2) r_nu,
    0<=k<=8.                                            (13)

There is no missing Taylor remainder: the four cross denominators
lower homogeneous z degree by four, and S extracts degree four.
An arithmetic degree k>8 cannot contribute. This is the scaling
argument in L629, applied to the analytic exact formula (8).

Here is an explicit finite rational recipe for every r_nu in (13).
Let d_j be the coefficient of s^j in 1-exp(-s)/4 and v_j the
coefficient of its reciprocal. Then

    d_0=3/4,  d_j=-(-1)^j/(4 j!) for j>=1,
    v_0=4/3,  v_k=-(4/3) sum_(j=1)^k d_j v_(k-j).       (14)

The numerator in (8) is sum_b c_b exp(-b dot w), with

    (c_b,b)=(1,1000),(1,0100),(-1/2,1110),(-1/2,1101).

Expand exp(-b dot w) and (sum w)^j. Exactly

    r_nu=sum_b c_b sum_(0<=mu<=nu)
          [product_i (-b_i)^mu_i/mu_i!]
          v_(|nu-mu|) |nu-mu|!/product_i (nu_i-mu_i)!.   (15)

Equations (13)-(15), together with L629 (5)-(7), prove (3) by
finite rational arithmetic. The reproducible certificate is

    python3 scripts/full_gram/grassmannian_n2_test.py

It writes `scripts/full_gram/grassmannian_n2_certificate.json`.
There are 175 pair-symmetric rows. The first method contracts (15)
against the alternant-based weights. The independent polynomial
replay constructs each six-subset numerator of L629 (5), sums it
with its coefficient r_nu at each arithmetic degree, divides by
Delta(z) by exact polynomial division, and multiplies back. It then
extracts -2[2011]+[1111] directly. This reuses the two different
algebraic implementations in `scripts/full_gram/signed_germ.py`;
it does not rerun an analytic transfer or a numerical Haar integral.
Both methods agree at every degree 0 through 8; pair interchange
also agrees at every degree, and (14)'s inverse convolution is
checked at each degree. No unexpected verification failure occurred.

For the load-bearing highest degree, the direct quotient has

    [2011]=109/688905,  [1111]=287029/91854,
    5040(-2[2011]+[1111])=34439992/2187 != 0.            (16)

The full rows, quotient polynomials, selected degree-eight
contributions and all extraction coefficients are in the certificate.
The complete extraction coefficients and all nonzero degree-eight
contributions were inspected, not inferred from a preview.
The first coefficient also has the independent analytic calculation
in Section 2. These are exact identities, not numerical positivity
evidence or a separate critical audit of the new result.

### 4. Scope of the multiplicative-insertion obstruction

Under the hypotheses in (5), expand

    H(P,tau Z;a)=sum_(k>=0) tau^k H_k(P,Z;a),

where H_k is homogeneous of z degree k. The local domination permits
integration and four differentiations termwise. Multiplication by
exp(eta), whose degree-r term has r>=0, contributes to S only if
k+r=4. The result is consequently a polynomial of tau degree at
most four. Equations (2) and (16), for a=(1,1), contradict equality
of polynomials on any open interval. This proves the asserted class
obstruction, without evaluating unspecified higher coefficients of
the candidate (1).

This argument does not preclude differentiating spectral parameters
and their Vandermonde factors before integration or coalescence.
Nor does it exclude a tau-dependent measure or amplitude beyond
the scaling in (5), or an approximate comparison sufficient for a
half-margin. None of those mechanisms is proved here. The infinite
tail is closed exactly for this fixed N only; no coefficient-uniform
growing-N estimate, control of other observers, or pointwise Xi sign
follows. The constant-amplitude match and the fixed-N mismatch are
both retained; no RH candidate is asserted.

## Mathlib

Full matching Mathlib coverage for this N=2 signed polynomial and
scaled multiplicative-insertion obstruction was not checked and is
unknown. HCIZ is the precisely cited external input; its confluent
specialization and the arithmetic closure are justified above.
The rational certificate checks the finite algebra only. There is
no Lean certificate or completed independent critical audit, and
no claim that the external Xi-transfer manuscripts were audited.
