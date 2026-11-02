# Lemma 633: full arithmetic spectral extraction in Gram coordinates

## Hypotheses

Let N>=1, L>0, and let a be an arbitrary vector in C^N, fixed during
every differentiation. Use L623's full positive Gram form
Gamma=a^*G_N a and L624's analytic arithmetic form B_N(q;a), with
its complete divisor sum and analytic C_N(q). Define F_(N,L), S
and Q_(N,L)=5040 Re S F_(N,L)(0) by L629's six-subset leading-pole
prescription, exactly as in L632 (2) with N in place of 2. In
particular q_I=(z_i,z_j,-z_k,-z_l)/L. Combine the six terms and
continue through collisions before differentiation.

The proposed application has N=floor(exp(L/100)) and L tending to
infinity. The identities below hold at each fixed N,L. They neither
assume nor prove a coefficient-uniform bound as N grows. L629's
qualified Xi transfer and the independent-audit qualifications of
the local arithmetic inputs remain unchanged.

For an exponent tuple m put A_m(y)=det(y_i^(m_j)), and define

    K(y)=-A_(7,2,1,0)(y)/2-7 A_(6,3,1,0)(y)/6
                  +7 A_(5,3,2,0)(y)/2+35 A_(4,3,2,1)(y)/2,
    H(y)=partial_y2 partial_y4 K(y),
    y_*=(1/2,1/2,-1/2,-1/2),
    sigma=(1,1,-1,-1),    d_j=sigma_j partial_yj.

This is L632's explicit spectral polynomial: H is homogeneous of
degree eight, H(y_*)=1, and H(-pi y)=H(y), where pi interchanges
the first and last pairs. The scalar analytic input behind this
polynomial is the probability-Haar U(4) HCIZ identity, with factor
12, in C. McSwiggen, *A new proof of Harish-Chandra's integral
formula*, [arXiv:1712.03995v3, (2), Theorem 1 and Section 3.4/(24)](https://arxiv.org/html/1712.03995v3).
L632's determinant extraction is reused; HCIZ is not reproved here.
The arithmetic factors are the already assessed Hughes--Young
factors, [arXiv:0709.2345v2, (12)--(17), pp. 4--5](https://arxiv.org/pdf/0709.2345v2#page=4),
specialized in L624. No moment theorem, positivity of a differentiated
orbit integral, or RH hypothesis is assumed.

## Conclusion

There is a finite, exact spectral formula

    Q_(N,L)(a)=Re { [B_N(d/L;a)]_(degree<=8) H }(y_*).       (1)

The brackets mean the Taylor differential polynomial through degree
eight at q=0. Thus (1) does not assert an infinite-order operator
on arbitrary entire functions. All arithmetic tails and normalization
derivatives are present in its coefficients.

Every matrix entry in (1) has the full-tail finite-moment evaluation
in Section 2 below. For the real triangular Gram-basis change V
defined in Section 3, V^*G_N V=I. Write mathsf Q for the real
symmetric matrix of Q, and

    E=V^* mathsf Q V-I,
    v_n=n^(-1/2),
    rho_(N,L)=max_(1<=n<=N) sum_(m<=N)|E_nm| v_m/v_n.

Then the exact sufficient bound is

    Q_(N,L)(a)>=(1-rho_(N,L))Gamma.                        (2)

In particular a uniform bound rho_(N,L)<=rho_*<1/2 at the stated
growing N would prove the approved target with
epsilon=1/2-rho_*. No such bound is proved here. An oversized row
bound would be inconclusive, not a negative direction of mathsf Q.
This is a finite arithmetic specialization of the reused spectral
identity and Gram basis, not a signed-margin result or novelty claim.

## Proof

### 1. Finite spectral extraction for arbitrary N

By L624, B_N is analytic near zero at each fixed N and symmetric
within each of its two argument pairs. L629's degree count shows
that only its Taylor polynomial P of degree at most eight can
contribute to Q: a degree k arithmetic term and degree r exponential
term have degree k+r-4 after the four cross differences, so the
order-four observer requires k+r=8. This is an exact coefficient
identity after cancellation, not a uniform Taylor remainder estimate.

Apply the finite differential polynomial P(d/L) to
det(exp(z_i y_j))/Delta(z). On each determinant monomial it inserts
P of the four assigned signed z coordinates divided by L. The two
confluent derivatives partial_y2 partial_y4 at y_* collect the
within-pair permutations into (z_j-z_i)(z_l-z_k), with the
permutation sign. Division by Delta(z) gives precisely 1/D_I.
Pair symmetry of P is needed at this step. Thus the six-subset
expression with P equals the finite differentiated multiplied HCIZ
identity, as in L632's confluence proof. The quotient has its
removable continuation at z collisions; no zero Vandermonde is
cancelled after singular substitution.

The degree-four z extraction of the scalar multiplied kernel is
K, so commuting only finitely many derivatives gives (1). The
factor 5040 and the probability-Haar factor 12 are already included
in K. In particular constant amplitude gives Q=Gamma. Fixed-N
analyticity suffices for every operation above; no uniform-in-N
interchange or extension of the N=2 translation series is needed.

### 2. Closed prime-power factors and the full geometric tail

Fix a prime p. Put x=1/p and

    A=p^(-alpha), B=p^(-beta), C=p^(-gamma), D=p^(-delta),
    s_e(A,B)=sum_(k=0)^e A^k B^(e-k),    s_(-1)=0.

For e>=0 define the normalized exponent-increase factor

    R_e = [sum_(j>=0) s_(j+e)(A,B)s_j(C,D)x^j]
                        /[sum_(j>=0) s_j(A,B)s_j(C,D)x^j].

These are the factors when the first divisor-function exponent is
increased. The opposite orientation interchanges (A,B) with (C,D).
For |Re q_j|<1/4 the sums and their fixed derivatives converge
absolutely, by L624's geometric domination. Exactly,

    R_0=1,
    R_e=P_e/(1-x^2 ABCD),                       e>=1,
    P_e=s_e(A,B)-x AB(C+D)s_(e-1)(A,B)
                      +x^2 (AB)^2 CD s_(e-2)(A,B),        (3)

where the last term is absent when e=1. All numerator coefficients
are rational, and all exponent vectors are nonnegative integers.

Here is a derivation including the boundary cases. The denominator
of the defining ratio is

    (1-x^2 ABCD)/[(1-xAC)(1-xAD)(1-xBC)(1-xBD)],

as in L624 (5). For A!=B the unnormalized e=1 numerator is

    [A^2/((1-xAC)(1-xAD))
           -B^2/((1-xBC)(1-xBD))]/(A-B).

Putting it over the common denominator leaves A+B-xAB(C+D).
Analytic continuation includes A=B. The recurrence
s_(j+e)=(A+B)s_(j+e-1)-AB s_(j+e-2), valid for e>=2,
passes through the absolutely convergent sum. It gives
R_e=(A+B)R_(e-1)-AB R_(e-2). The e=2 numerator therefore is
s_2-xAB(C+D)s_1+x^2(AB)^2 CD, and (3) follows by recurrence
for all e>=3. This also proves the formula without dividing by
A-B at a collision. At q=0,

    p^(-e/2)R_e(0)=p^(-e/2)(1+e(p-1)/(p+1)),             (4)

exactly the complete zero-shift kernel of L623.

For matrix indices m,n let g=gcd(m,n), h=m/g and k=n/g. A prime
power p^e dividing k uses (3) in its displayed orientation; a prime
power dividing h uses the pair-swapped orientation. Their product,
divided by sqrt(hk), is the (m,n) arithmetic coefficient. Primes
not dividing hk cancel exactly with C_N(q). This is L624's
full-tail identity, including the diagonal case h=k=1.

Expand the finite numerator product as

    sum_b c_b exp(-L b dot q),

where b is the sum of its exponent vectors weighted by log p/L.
The coefficients c_b are real rational numbers, of both signs in
general. Let P(hk) be the distinct primes dividing hk, and let
J_p be independent auxiliary geometric random variables with

    Pr(J_p=j)=(1-p^(-2))p^(-2j),       j>=0,
    W=sum_(p|hk) J_p log p/L,
    Z_hk=product_(p|hk)(1-p^(-2))^(-1).

They express denominators only; they do not assert positivity of
the signed numerator or of Q. Formula (1) gives the matrix entry

    mathsf Q_mn = Z_hk/sqrt(hk)
           sum_b c_b E[H(y_*-sigma b-sigma W)].           (5)

For hk=1 this is H(y_*)=1. Each expectation in (5) is exactly a
polynomial in moments E[W^j], j<=8. The infinite geometric sums
converge with every such polynomial factor, so (5) retains every
tail index. It is not numerical truncation at a large j.

For x=p^(-2), the normalized geometric moments satisfy

    m_0=1,
    m_j=x/(1-x) sum_(r=0)^(j-1) binom(j,r)m_r,   j>=1.    (6)

Indeed shifting the summation index gives
m_j=x sum_(r=0)^j binom(j,r)m_r for j>=1. Moments of W follow
by the finite binomial convolution over its independent summands.
For each b, equivalently use

    E[H(y_*-sigma b-sigma W)]
      =sum_(j=0)^8 E[W^j]/j!
          ((-sum_i sigma_i partial_yi)^j H)(y_*-sigma b).

These identities require no uniform moment bound in N. Interchanging
m,n swaps the pairs in every b. L632's H(-pi y)=H(y), together
with -pi y_*=y_* and pi sigma=-sigma pi, makes (5) unchanged.
All quantities are real. Hence mathsf Q is real symmetric and
represents the original real quadratic form for all complex a.

### 3. Normalize the complete Gram form before estimating rows

Use L627's orthonormal polynomials at each prime. With t=p^(-1/2),

    c_p=(1-t^2)^3/(1+t^2),
    r_p=2t/(1+t^2),   s_p=(1-t^2)/(1+t^2),
    phi_(p,0)=1,
    phi_(p,1)=(z-r_p)/s_p,
    phi_(p,e)=z^(e-2)(z-t)^2/sqrt(c_p),        e>=2.

For n<=N let Phi_n be their tensor product with e=v_p(n).
Its monomials have indices dividing n. Let V_mn be the coefficient
of z^m in Phi_n, using the finite-prime monomial convention of L627.
Thus a=Vy is an invertible triangular change on the original
coefficient space, and L627's full-tail isometry gives

    a^*G_N a=sum_(n<=N)|y_n|^2,          V^*G_N V=I.        (7)

No divisor-output coordinate has been deleted in (7). V is a
different matrix from L623's finite inverse convolution, which is
not used here.

The local shifted measure also explains the cancellation used to
choose these coordinates. Put A'=t p^(-alpha), B'=t p^(-beta),
C'=t p^(-gamma), D'=t p^(-delta). On the unit circle set

    dmu_(p,q)(z)=D_p(q)^(-1) dm(z)
           /[(1-A'z)(1-B'z)(1-C'z^(-1))(1-D'z^(-1))],

where dm is probability Haar measure. Its integral is exactly one:
the absolutely convergent Fourier expansion gives D_p(q) before
normalization. Consequently the (0,0) entry of the shifted form
in the fixed phi basis is exactly one at every q. For general
complex shifts this measure is complex, and no positivity follows.
The full transformed arithmetic entries factor over these local
integrals with phi_(p,v_p(m)) and the conjugate fixed polynomial
phi_(p,v_p(n)). This is just the same absolutely convergent
finite-prime Parseval identity underlying L624/L627.

Finally E=V^*mathsf Q V-I is Hermitian. For v_n>0,

    2|y_n||y_m| <= (v_m/v_n)|y_n|^2+(v_n/v_m)|y_m|^2.

Multiplying by |E_nm| and summing, using |E_nm|=|E_mn|, proves
|y^*Ey|<=rho_(N,L)||y||^2. Combining with (7) gives (2) for
arbitrary complex y, including the zero vector. This elementary
weighted-row sufficient test is applied after exact Gram
normalization; L622's stopped unscaled row test is not being reused.

### 4. Bounded computational screen and its limits

Run from the active notebook:

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/full_gram/growing_n_spectral_probe.py

The full output is `scripts/full_gram/growing_n_spectral_probe_certificate.json`.
The script constructs H with rational determinant arithmetic,
checks H(y_*)=1, checks its pair-exchange/reflection symmetry,
reproduces all nine exact N=2 coefficients, and compares (3) to
its recurrence for every prime power used in the finite screen.
The geometric moments (6) are rational and have no cutoff.

The screen uses N=2,4,8,16,32,64 and L=100 log(N+1/2), so the
exact real parameters obey floor(exp(L/100))=N. Logarithms, matrix
entries, the basis change and eigensolver use floating arithmetic.
The smallest generalized eigenvalue previews decrease from about
0.99480847 to 0.95415890. The largest weighted-row previews over
those six tests lie between 0.1830 and 0.2183, below the required
0.5 threshold in those floating outputs. The certificate retains
every tested matrix, all eigenvalues, all row values and the
minimum coefficient directions, together with diagnostic residuals.

These values are not interval enclosures, certified finite
inequalities, or evidence for a uniform onset. No negative direction
of the actual inequality was found in this bounded screen. No fixed
epsilon for growing N was established. In particular the proved
normal form and successful exact diagnostics do not pass the signed
margin test by themselves. A uniform estimate of the complete
normalized matrix, or a genuine coefficient obstruction, is still
required. Pointwise Xi signs, other observers, and the local and
external source audits remain independent open obligations.

## Mathlib

Full matching coverage for this full-arithmetic spectral extraction,
Gram-normalized matrix and growing-N row estimate was not checked
and remains unknown. HCIZ is the precisely cited reused analytic
input; L624's arithmetic factors and L627's torus/orthogonality
identities are used with their stated hypotheses. Formula (2) has
the elementary proof above and is not asserted to be a new Schur
bound. The rational diagnostics and floating screen are not Lean
certificates or an independent critical audit of this result.
