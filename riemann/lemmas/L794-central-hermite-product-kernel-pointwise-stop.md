# Lemma 794: the prescribed degree-six Hermite product kernel is not pointwise PSD

## Hypotheses

Use the completion convention of L018, the actual strictly positive theta
kernel K of L019, and the moments of L021. Write

    m_j = M_(2j) = integral_0^infinity u^(2j) K(u) du, 0<=j<=6,
    gamma(j) = j! m_j/(2j)!, R_j = gamma(j)/gamma(0),
    P_6(x) = sum_(j=0)^6 (-1)^j binom(6,j) R_j x^j.

This is the actual normalization: L776 gives
G(w)=xi(1/2+sqrt(w)/2)/8=sum a_j w^j with
a_j=m_j/(8*4^j*(2j)!), hence gamma(j)=8*4^j*j!*a_j.
Only that normalization, not a Fredholm or zero-location premise, is used.
All m_j are finite and strictly positive.

Normalize P_6 to the monic polynomial x^6+c_1 x^5+...+c_6. Define its
formal Newton sums s_0=6 and s_k through k=10 by Newton's identities,
without any real-root assumption. Let H_ij=s_(i+j), 0<=i,j<=5.

The construction is fixed as follows. Treat m_0,...,m_6 as independent
formal variables and collect each rational H entry. Choose the least
nonnegative integer N for which m_6^N clears every variable denominator.
If every cleared entry is homogeneous of total moment degree N, replace
each monomial c product_(ell=1)^N m_(a_ell) by

    c Sym(product_(ell=1)^N u_ell^(2a_ell)),
    Sym(f) = (1/N!) sum_(sigma in S_N) f(u_(sigma(1)),...,u_(sigma(N))).

Apply this rule linearly to define the real symmetric matrix polynomial F.
The repeated-index monomial is a multiset; averaging all permutations
counts repetitions and therefore makes the definition unambiguous.

## Conclusion

The construction exists, N=10 is least, and every cleared entry has
total moment degree 10. With the actual theta product retained,

    m_6^10 H = integral_([0,infinity)^10) F(u) product_(ell=1)^10 K(u_ell) du.

Every entry is absolutely integrable. For the fixed integer vector

    w=(-152988,4638,113,0,0,0)^T

one has exactly

    w^T F(1,1,1,1,1,1,1,1,1,4) w = -1281831933403422720 < 0.

Thus F is not pointwise positive semidefinite. Negativity occurs on a
nonempty open set of positive distinct variables, including within the
strictly ordered chamber, where the actual product K is positive.
This is an obstruction only to direct pointwise signing of this prescribed
representation. It does not show H is indefinite or its integral negative,
does not dispute known degree-six hyperbolicity, and does not resolve RH.

## Proof

**Exact coefficients and Newton identities.** The m_0 factors cancel on
monic normalization, and the remaining coefficients are

    c_k=(-1)^k binom(6,k) [(6-k)!/(12-2k)!]/[6!/12!] m_(6-k)/m_6,
    (c_1,...,c_6)=(-132 m_5,5940 m_4,-110880 m_3,
                   831600 m_2,-1995840 m_1,665280 m_0)/m_6.

Use the standard named Newton identities. For the Newton-sum and
Hermite-matrix conventions see Nathanson,
*The Hermite-Sylvester criterion for real-rooted polynomials*,
[arXiv:1911.01745v2](https://arxiv.org/pdf/1911.01745v2), pp.1–2,
Newton-sum definitions (Theorem1 pp.2–4 supplies the Hermite criterion,
whose PSD conclusion is not an input; Lemmas1–2 concern interpolation,
not the recurrence). Specifically,

    s_k + sum_(j=1)^(k-1) c_j s_(k-j) + k c_k = 0, 1<=k<=6;
    s_k + sum_(j=1)^6 c_j s_(k-j) = 0, 7<=k<=10.

These polynomial identities hold regardless of root locations or
multiplicities. No root-evaluation square formula is needed.

Give c_j weight j. Induction in these recurrences shows that each monomial
of s_k has weighted c-degree k, and thus has at most k coefficient factors.
Each c_j contributes only the variable denominator m_6 and a numerator
moment of index at most 5. Consequently the only variable denominator
in s_k is a power m_6^r with r<=k, and each rational monomial has total
moment degree zero. Therefore m_6^10 clears all s_0,...,s_10 and produces
homogeneous polynomials b_k=m_6^10 s_k of degree 10.

The coefficient of c_1^k in s_k is (-1)^k: the c_1 s_(k-1) term gives
this inductively, and no c_j with j>=2 can produce the same monomial.
For k=10 this yields 132^10 m_5^10/m_6^10. Since the variables are
independent and no other coefficient uses m_5, that term cannot cancel.
Thus no smaller exponent clears s_10, proving minimality. Moreover each
monomial of b_k has moment-index weight sum a_ell=60-k, since a product
of r coefficients of total c-weight k has numerator index 6r-k and
the remaining 10-r factors are m_6. This additional weight check is
not needed to assume any positivity.

**Integral identity.** A monomial product of ten moments is the integral
of the corresponding ten-variable product of powers against product K.
Its absolute integral is finite by L021. A variable permutation preserves
the product measure and domain, so every summand in its permutation
average has the same integral. Taking the finite average gives exactly
the original moment monomial, with no extra factorial. Finite linear
combination proves the asserted matrix identity. The triangle inequality
and the finite absolute monomial integrals justify all uses of Fubini
and all averaging. This verifies the actual theta identity rather than
substituting an atomic moment law. No Andreief Gram factor is assumed.

**One-outlier specialization and exact witness.** For an exponent
multiset with e_a occurrences of a, sum e_a=10, polarization on
(1,...,1,t) gives exactly (1/10) sum_(a=0)^6 e_a t^(2a): each of
the ten slots is the outlier in precisely 9! of the 10! permutations.
Let f_k(t) be this specialization of the polarization of b_k. Then
F_ij(1,...,1,t)=f_(i+j)(t). Only k<=4 is needed by w. The recurrence gives,
on putting a=132m_5/m_6, b=5940m_4/m_6,
c=110880m_3/m_6 and d=831600m_2/m_6,

    s_0=6, s_1=a, s_2=a^2-2b,
    s_3=a^3-3ab+3c,
    s_4=a^4-4a^2 b+2b^2+4ac-4d.

Multiplying by m_6^10 and applying the preceding outlier rule yields
the complete required polynomials:

    f_0 = 6t^12,
    f_1 = (66/5)t^10+(594/5)t^12,
    f_2 = -1188t^8+(17424/5)t^10+(16236/5)t^12,
    f_3 = 33264t^6-235224t^8+(2273832/5)t^10+(137808/5)t^12,
    f_4 = -332640t^4+5854464t^6-27285984t^8
          +(222469632/5)t^10-(36713952/5)t^12.

Direct substitution of the stated integer w gives

    w^T F(1,...,1,t) w
      = 4752[-893830t^4+23068724t^6-121938843t^8
             +206347856t^10-28504137t^12].

This finite identity can be checked from w_0^2 f_0+2w_0w_1 f_1+
(2w_0w_2+w_1^2)f_2+2w_1w_2 f_3+w_2^2 f_4. For t>=1 the sum
of absolute values of the four lower coefficients in brackets is
352249253. Hence the expression is at most

    4752 t^10 (352249253-28504137 t^2).

Since 16*28504137=456066192>352249253, this is negative for all
t>=4. Evaluation at t=4 gives the exact integer in the conclusion.
The negative leading coefficient supplies an independent tail
certificate; neither a numerical eigenvalue nor a plot is used.

**Positive distinct open set.** F is a polynomial, so w^T F(u)w is
continuous. Its strict negativity at (1,...,1,4) persists in an open
ball contained in the positive orthant. For sufficiently small epsilon>0,
(1,1+epsilon,...,1+8epsilon,4) lies in that ball and has ten strictly
increasing coordinates. A smaller ball about that point stays in both
the negative ball and the strictly ordered positive chamber. It is
nonempty and has positive Lebesgue measure. L019 gives K>0 there, so
the scalar integrand w^T F(u)w product K(u_ell) is negative there as well.
Other regions may compensate it; no sign of the full integral follows.

**Reproduction and source qualification.** The full Laurent polynomials
s_0,...,s_10, cleared polynomials, one-outlier coefficients, rational
leading-matrix LDL witness, integer witness and exact threshold are
saved in `scripts/central-hermite/product-kernel-496.json` by
`python3 scripts/central-hermite/product_kernel_496.py`. The proof above
establishes the construction and sign without relying on a preview or
the software's assertion of PSD failure. The source assessment is
`drafts/literature/2026-11-05-central-hermite-product-kernel-test.md`;
it found no adequate match for this precise representation, not evidence
of originality. Newton identities and polarization are conventional;
only this representation's obstruction is established locally. L766
concerns a different Toeplitz matrix and is not a mathematical input.

**Independent audit, step498.** All claims above were checked under
`drafts/literature/2026-11-05-central-hermite-product-kernel-audit.md`.
An independent coefficient calculation uses C(z)=1+sum_(j=1)^6 c_j z^j
and the formal identity sum_(k>=1) s_k z^k=-z C'(z)/C(z).
Multiplying by C proves that this identity has precisely the two Newton
recurrences displayed above, so it assumes no root location. Equivalently,
expanding the formal logarithm gives, for k>=1,

    s_k = k sum_(e_1+2e_2+...+6e_6=k)
          (-1)^r (r-1)!/(e_1!...e_6!) product_(j=1)^6 c_j^(e_j),
    r=e_1+...+e_6.

For each fixed k this is a finite sum and r>=1. It follows by extracting
the z^k coefficient of -k log C: the r-th term of -log C has coefficient
(-1)^r/r and the multinomial coefficient is r!/(product e_j!).
Thus it is independent of the recurrence implementation in step496.
Direct coefficient division also simplifies the monic constants to
(-1)^j 12!/[j!(12-2j)!], confirming the six constants above.

`python3 scripts/central-hermite/product_kernel_audit_498.py` compares
every collected Laurent and cleared coefficient through k=10, every
one-outlier coefficient and the entire saved leading matrix with this
partition expansion. It separately checks the five printed f_k, both
witnesses and all fields of the negative-witness certificate. The first
three leading-matrix LDL pivots are exactly
6, 22374/25, -1198687248/113; the rational witness is w/113.
All 27 exact checks passed, with complete actual/required comparisons in
`scripts/central-hermite/product-kernel-audit-498.json`.

The written audit also checks what the calculation cannot: m_6>0 makes
the actual normalization legal, while formal variable independence
establishes minimality without cancellation; every polarized monomial
uses exactly ten finite moments with indices at most six, so absolute
Fubini applies; precisely 9! permutations send any fixed slot to the
outlier, including when exponents repeat; and strict negativity persists
after perturbing the nine repeated coordinates into the ordered chamber.
For t>=1, each lower power is at most t^10, and
16*28504137=456066192>352249253 proves the claimed t>=4 bound.
No mathematical defect was found. The citation above was corrected to
separate Newton's identities from Nathanson's interpolation lemmas.
This verifies the existing local obstruction, not a new hyperbolicity
theorem, an integrated sign or an advance beyond the checked sources.

## Mathlib

Full matching coverage for this particular nonlinear Newton-sum
polarization and negative witness is not checked; availability is unknown.
The argument uses Newton identities, finite polynomial algebra, finite
permutation averaging, absolute Fubini and continuity. No Mathlib theorem
is claimed to supply the complete result. Reference:
https://leanprover-community.github.io/mathlib4_docs/.
