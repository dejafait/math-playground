# Lemma 632: an exact full-tail N=2 Vandermonde spectral lift

## Hypotheses

Fix N=2, L>0, tau=log(2)/L, and a=(a1,a2) in C^2. Coefficients
are held fixed in every differentiation. Use L623's full Gamma and
L624's analytic arithmetic form B_2, including every r=2^j and all
derivatives of C_2(q)=D_2(q)^(-1). There is no tail cutoff. Write
s_a=|a1|^2+|a2|^2 and u=a1 conjugate(a2). L631 (7)-(8) gives

    B_2(q;a)=s_a+(u r(w)+conjugate(u) r(w3,w4,w1,w2))/sqrt(2),
    w=(log 2)q,
    r(w)=[exp(-w1)+exp(-w2)
            -(exp(-w1-w2-w3)+exp(-w1-w2-w4))/2]
                                  /[1-exp(-sum w)/4].       (1)

This is an exact closed form of the full arithmetic tail, initially
on |Re q_j|<1/4, not a finite approximation or a frozen C_2.

For I={i<j} in {1,2,3,4}, with complement J={k<l}, set

    D_I(z)=product_(v in I,t in J)(z_v-z_t),
    ell_I(z)=(sum_I z-sum_J z)/2,
    q_I(z)=(z_i,z_j,-z_k,-z_l)/L,
    F(z;a)=sum_(|I|=2) exp(ell_I(z)) B_2(q_I(z);a)/D_I(z),
    S=-1/2 (partial_z1-partial_z2)^2 partial_z3 partial_z4,
    Q_(2,L)(a)=5040 Re (S F)(0).                            (2)

The sum is combined before continuing through collisions, as in
L629. Only its exact leading-germ prescription is used, not a new
application or audit of the asymptotic Xi transfer. No sign, RH,
zero-free, spacing or simplicity hypothesis is assumed.

Let Z=diag(z), Y=diag(y), and let dU be probability Haar measure on
U(4). Define the entire function

    I_4(z,y)=integral exp(tr(Z U Y U*)) dU,
    Delta(y)=product_(i<j)(y_j-y_i),
    y_*=(1/2,1/2,-1/2,-1/2),
    d=(partial_y1,partial_y2,-partial_y3,-partial_y4).

The named input is C. McSwiggen, *A new proof of Harish-Chandra's
integral formula*, [arXiv:1712.03995v3, (2), Theorem 1 and Section 3.4/(24)](https://arxiv.org/html/1712.03995v3).
With this probability normalization its U(4) formula, initially for
real distinct spectra and then analytically continued, is

    Delta(y) I_4(z,y)/12=det(exp(z_i y_j))/Delta(z).       (3)

This standard formula is imported, not reproved. The new local work
is its arithmetic differential specialization. Neither Miglioli's
invariant-polynomial radial identity nor Eynard's regular-spectrum
correlator formula is a premise; no invariant arithmetic symbol or
weighted-localization rule is assumed.

## Conclusion

Define A_(tau,a)=B_2(d/L;a) on Delta(y)I_4(z,y) by the normally
convergent translation series in Section 1 below. Then, as a
holomorphic germ in z at zero,

    F(z;a)=(1/12) {partial_y2 partial_y4
                   A_(tau,a)[Delta(y) I_4(z,y)]}_(y=y_*). (4)

The Vandermonde is differentiated before the repeated spectrum is
substituted. The operator and its normalization are specified without
fitting any extraction coefficients. Replacing B_2 by a constant
Gamma gives exactly Q=Gamma. For the actual amplitude, (4) recovers
L631's whole degree-eight polynomial for arbitrary complex a:

    Q_(2,L)(a)=s_a+sqrt(2) Re(u) P(tau),
    Gamma=s_a+(4 sqrt(2)/3) Re(u),                         (5)

with all nine coefficients of P exactly those of L631 (3).

This passes the nominated fixed-N representation test outside L631's
stopped multiplicative class. It is a local specialization of known
HCIZ, not a new HCIZ theorem or a claim of originality. It neither
proves nor refutes the growing-N bound Q_(N,L)>=Gamma/2, and gives
no positive integral, uniform operator domination, Xi sign or RH
candidate. The result and its local inputs await independent audits.

## Proof

### 1. Define the operator and justify convergence

Write sigma=(1,1,-1,-1), with multiplication of vectors coordinatewise.
For a vector h let T_h f(y)=f(y+h). Let the four pairs (c_b,b) be

    (1,1000), (1,0100), (-1/2,1110), (-1/2,1101).

Put b^s=(b3,b4,b1,b2), and define

    R_L(tau)=sum_b c_b sum_(j>=0) 4^(-j)
                              T_(-tau sigma(b+j(1,1,1,1))),
    R_R(tau)=sum_b c_b sum_(j>=0) 4^(-j)
                              T_(-tau sigma(b^s+j(1,1,1,1))),
    A_(tau,a)=s_a Id+(u R_L(tau)+conjugate(u) R_R(tau))/sqrt(2).
                                                               (6)

On an exponential exp(sum y_i x_i), the first series multiplies it
by r(tau x1,tau x2,-tau x3,-tau x4), and the second interchanges the
two arguments pairs of r. This follows by summing the geometric
denominator in (1). Thus (6) is a precise meaning of B_2(d/L;a)
on the functions used here; no operator inverse on arbitrary entire
functions is asserted.

Here is domination valid before any confluent limit. Choose r0>0
with r0<L/4 and 4 tau r0<log 4, and restrict |z_i|<=r0. For y in
any fixed compact set and any shift in (6), its coordinates have
modulus at most M+tau(j+1). Since U is unitary,

    |tr(Z U Y U*)|<=r0 sum_i |y_i|<=4r0 max_i |y_i|.

The shifted integrand is therefore bounded by a constant times
exp(4r0 tau j). Delta at that shift is bounded by C(1+j)^6.
Every fixed finite collection of z and y derivatives only adds
polynomial factors in j: derivatives of the exponential insert
linear functions of y or z, and derivatives of Delta are polynomials.
Consequently every series needed here is dominated by

    C (1+j)^M 4^(-j) exp(4r0 tau j),

which is summable. The bound is uniform on the specified compact
sets, including repeated z and y. It justifies summation, Haar
integration, the two y derivatives, evaluation at y_*, and the
four z derivatives in either order. Smaller open neighborhoods give
holomorphy. Constants may depend on the fixed L and on a; no
uniformity for growing N is inferred. The full-tail identity (1)
has already been justified by L624/L631, so no new interchange in
its original divisor sum is being assumed.

### 2. Confluence of the multiplied identity

For distinct z near zero apply (6) to the right side of (3), using
the finite determinant expansion. Each determinant monomial assigns
two z coordinates to y1,y2 and the complementary two to y3,y4.
Its multiplier is B_2 of those four signed coordinates divided by L.
Because B_2 is symmetric within each of its two argument pairs, the
multiplier is unchanged under the two permutations within either pair.

Apply partial_y2 partial_y4 and set y=y_*. For the subset I={i<j}
and its complement J={k<l}, the four assignments therefore sum to

    epsilon_I (z_j-z_i)(z_l-z_k)
                          exp(ell_I(z)) B_2(q_I(z);a),

where epsilon_I is the sign of (i,j,k,l). The two differences arise
by subtracting the two possible coordinates inserted by each
derivative; there is no extra factorial. In four variables,

    epsilon_I (z_j-z_i)(z_l-z_k)/Delta(z)=1/D_I(z).

Summing over I proves (4) away from z collisions. The left side of
(4) as expressed by the lift is holomorphic across them by Section 1;
the combined six-term expression has the removable continuation of
L629. Thus the germs agree everywhere near zero. At no point is a
zero Delta(y_*) cancelled after substitution. Coefficients a remain
fixed throughout, so the argument holds for arbitrary complex a.

### 3. Independent spectral extraction and its exact finite size

Define

    K(y)=5040 {S_z[Delta(y) I_4(z,y)/12]}_(z=0),
    H(y)=partial_y2 partial_y4 K(y).

Only the homogeneous degree-four part in z contributes. To compute
it, expand each exponential in the determinant of (3) and use
determinant multilinearity. Repeated exponent columns vanish;
grouping distinct exponents gives the products of the two
alternants divided by the product of their exponent factorials.
Division by Delta(z), of degree six, leaves exactly the decreasing
exponent vectors m=lambda+(3,2,1,0), where lambda is a partition of
4 with at most four parts. This finite homogeneous calculation is
legitimate in the normally convergent exponential series.

Write A_m(y)=det(y_i^(m_j)). With the same Delta orientation,
A_(3,2,1,0)=Delta. Put s_lambda(z)=A_m(z)/Delta(z). Direct polynomial
division gives the following values of the order-four observer:

    lambda       4       31       22       211       1111
    S s_lambda  -1       -1        0         1          1.

Here S on a symmetric quartic is -2[2011]+[1111], including all
derivative factorials, as in L629 (7). It follows exactly that

    K=-A_(7,2,1,0)/2 -7 A_(6,3,1,0)/6
                       +7 A_(5,3,2,0)/2+35 A_(4,3,2,1)/2. (7)

This is a homogeneous polynomial of degree ten, so H is homogeneous
of degree eight. The four terms in (7), after the two derivatives
and evaluation at y_*, contribute -3/32, 7/32, -7/32, and 35/32,
respectively. Thus H(y_*)=1. These are four-by-four determinant
evaluations, also recorded individually in the certificate below.
Thus a constant amplitude gives exactly
Q=Gamma, with the factor 12 and the confluence factors accounted for.

Commuting the justified derivatives gives the useful finite formula

    Q_(2,L)(a)=Re {A_(tau,a) H}(y_*).                     (8)

Every Taylor differential monomial of total order above eight
annihilates H. Thus the degree-eight arithmetic truncation is exact
for this observer, even though (4) is an identity of full germs.
It is not a tail approximation. Equivalently, (6) evaluated on H
is a polynomial in tau of degree at most eight.

For completeness, let pi exchange coordinates 1,3 and 2,4. It is an
even permutation. Alternation and degree ten in (7), followed by
the two derivatives, give H(-pi y)=H(y). Also -pi y_*=y_* and
pi sigma=-sigma pi. Each translated value in R_L H at y_* is
therefore the corresponding value in R_R H at y_*. They are real
for real tau. Equation (8) yields (5), with

    P(tau)=sum_b c_b sum_(j>=0)4^(-j)
                         H(y_*-tau sigma(b+j(1,1,1,1))). (9)

This expression was fixed by the arithmetic amplitude, not by the
nine desired coefficients. It gives a second exact extraction
through spectral variables rather than L629's six-subset weights.

### 4. All nine coefficients, with the complete geometric tail

Let M_k=sum_(j>=0) j^k/4^j, where j^0=1 also at zero. Absolute
convergence and shifting the index give

    M_0=4/3,
    M_k=(1/3) sum_(r=0)^(k-1) binomial(k,r) M_r, k>=1.   (10)

Expand each degree-eight polynomial in (9) in tau and j and replace
j^k by M_k. Equations (7), (9), and (10) are a finite rational
recipe with no tail cutoff. They give, in ascending order,

    (4/3, -16/9, -385/27, -14/27, 15680/81,
                  -227269/243, 914228/243, -7929146/729,
                                             34439992/2187),

exactly L631 (3). In particular the first coefficient retains the
factor missed by the multiplicative orbit insertion, and the last
coefficient is nonzero. At tau=0, (6) has R_L=R_R=(4/3)Id,
so the actual zero-shift form is precisely the full Gamma in (5).

Reproduce the exact arithmetic with

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/full_gram/spectral_lift_n2.py

The script writes `scripts/full_gram/spectral_lift_n2_certificate.json`.
It constructs the five spectral alternants and their exact divisions,
with multiply-back verification. It evaluates (9) using all geometric
moments through degree eight, and independently applies the finite
Taylor operator to H for every one of the 495 multiindices of total
degree at most eight. The latter check reuses only L631's exact
rational amplitude-coefficient routine, not the six-subset weights.
Both evaluations, both argument-pair orientations, and all nine
comparison coefficients agree. Constant amplitude equals one;
every required coefficient discrepancy is zero; no verification
failure occurred. The full diagnostic, normalization, moments, and
five spectral determinant rows were inspected. Full polynomials and
all intermediate translation and Taylor data are retained on disk.

The finite calculation checks the algebra, not the analytic source
manuscript or a positivity assertion. The convergence and full-germ
argument are supplied separately in Sections 1 and 2. No claim about
other observers or the growing-N family has been established here.
The arithmetic translation coefficients already have both signs;
neither Haar measure nor (4) makes the signed extraction positive.
Uniform Gram domination with room for L629's O(Gamma/L) error,
independent input audits and pointwise Xi transfer remain unresolved.

## Mathlib

Full matching Mathlib coverage for this arithmetic spectral lift and
its N=2 signed polynomial was not checked and remains unknown.
The precisely cited HCIZ theorem is the external analytic input;
the arithmetic specialization, confluence and convergence are proved
above. The script is an exact rational check, not a Lean certificate
or an independent critical audit. No new theorem beyond the checked
literature is claimed.
