# Lemma 875: Gaussian failure of the printed shifted-Wronskian sign

## Hypotheses

Let dmu(u)=pi^(-1/2)exp(-u^2)du on R and m_j=int_R u^j dmu(u).
Set D_n=det(m_(j+k))_(0<=j,k<=n). Let p_n be its degree-n
orthonormal polynomial with positive leading coefficient. For r functions,
use W(f_1,...,f_r;z)=det(f_k^(j-1)(z))_(1<=j,k<=r), taking complex
derivatives before evaluating at z. In particular W(f;z)=f(z).

The audited statement is Dimitar K. Dimitrov, *Lee-Yang measures and
wave functions*, [arXiv:1311.0596v1](https://arxiv.org/pdf/1311.0596v1),
4 November 2013, Section2 (3),(5),(6), pp4-5; Theorem2 p6;
Section3.3 p9. Theorem2 asserts, under its even-moment, positive-Hankel
and growth assumptions, that real Fourier zeros are equivalent to
W(p_2,...,p_n;ix)<0 for every real x!=0 and integer n>=2.
This lemma tests the statement literally, with its own polynomial and
Wronskian conventions; it does not assume that criterion.

## Conclusion

This Gaussian satisfies every stated Theorem2 hypothesis and has entire,
zero-free Fourier transform F_mu(z)=exp(-z^2/4). Nevertheless,

    W(p_2;ix)=-(2x^2+1)/sqrt(2)<0,
    W(p_2,p_3;ix)=(4x^4+3)/sqrt(6)>0                 (x real).

Thus n=2 passes, and n=3, x=1 gives 7/sqrt(6)>0 where the printed
criterion requires a strictly negative value. Its necessity direction
cannot be imported as printed in this version. No corrected criterion,
failure of any other theorem, actual-theta sign or conclusion about RH
is asserted. The bounded audit stops at this first mismatch.

## Proof

### Cited classical inputs and applicability

Import Hermite orthogonality, norms and positive leading coefficients
from NIST DLMF [Table18.3.1](https://dlmf.nist.gov/18.3#T1), the Hermite
coefficient formulas [18.5.18](https://dlmf.nist.gov/18.5#E18), and the
Gaussian cosine transform, the n=0 case of
[18.17.23](https://dlmf.nist.gov/18.17#E23). These primary formulas were
inspected on 6 November 2026. They are standard inputs, not new results
being reproved. The local calculation is needed to test the suspect
source normalization rather than use its criterion as a premise.

DLMF18.17.23 at n=0 reads
int_0^infinity exp(-v^2/2)cos(vy)dv=sqrt(pi/2)exp(-y^2/2)
for real y. Substitute v=sqrt(2)u, y=x/sqrt(2). Evenness kills the
sine part of the full Fourier integral with phase exp(-ixu), yielding
F_mu(x)=exp(-x^2/4), including F_mu(0)=1.

For any fixed M and nonnegative integer j,

    |u|^j exp(-u^2+M|u|)
      <= exp(M^2/2)|u|^j exp(-u^2/2)

is integrable. It bounds the Fourier integrand and each derivative
uniformly for |z|<=M. Dominated differentiation makes F_mu entire;
the identity theorem extends the real-axis formula to all complex z.
The exponential has no zeros, so the condition that all Fourier zeros
are real holds (the zero set is empty). No contour shift is used.

### Exact source hypotheses

The measure is a positive, even probability Borel measure, supported on
all of R. All moments are finite by the preceding domination. Comparing
Taylor coefficients of the justified entire transform gives

    m_(2k+1)=0,   m_(2k)=(2k)!/(4^k k!)>0  (k>=0).

For every n and every nonzero real vector a=(a_0,...,a_n),

    sum_(j,k=0)^n a_j a_k m_(j+k)
       = int_R (sum_(j=0)^n a_j u^j)^2 dmu(u)>0.

Indeed a nonzero polynomial has finitely many real zeros and the density
is strictly positive everywhere. The real moment matrix is positive
definite, hence its determinant D_n is strictly positive, including
D_0=1. This verifies (3) for every required index, not just n=2,3.

For k>=1 the exact moment is the product

    m_(2k)=product_(j=1)^k ((2j-1)/2) <= k^k.

Consequently 0<=m_(2k)^(1/(2k))/(2k)<=1/(2sqrt(k)), which tends to
zero. This verifies (5), interpreting the source's symbol mu_(2k)
there as the moments m_(2k) defined immediately before it. If moment
determinacy is needed, the same bound gives
sum_(k>=1) m_(2k)^(-1/(2k))>=sum_(k>=1) k^(-1/2)=infinity;
the standard named Carleman criterion therefore gives uniqueness.
No assumption on every positive quadratic exponential moment is part
of Theorem2. In fact this Gaussian fails that different assumption when
b>=1; Newman's stronger introductory hypothesis is not being invoked.
The paper explicitly replaces that restriction in Sections1-2.

### Positive-leading normalization and the two determinants

DLMF's H_n has weight exp(-u^2), squared norm sqrt(pi)2^n n! and
leading coefficient 2^n. Thus, for the specified probability measure,

    p_n(z)=H_n(z)/sqrt(2^n n!).

These are orthonormal, with positive leading coefficients. This is also
the convention forced by the source's (6): the coefficient of z^n in
its numerator determinant is D_(n-1)>0, and its denominator is the
positive square root of D_(n-1)D_n. Uniqueness of orthonormal polynomials
with positive leading coefficient therefore identifies the conventions.
No column sign or index is changed.

Using only H_2(z)=4z^2-2 and H_3(z)=8z^3-12z from DLMF18.5.18,

    p_2(z)=(2z^2-1)/sqrt(2),
    p_3(z)=(2z^3-3z)/sqrt(3).

The singleton determinant gives the stated negative n=2 expression.
For n=3, the rows are value and first derivative, so

    W(p_2,p_3;z)
       = [(2z^2-1)(6z^2-3)-4z(2z^3-3z)]/sqrt(6)
       = [12z^4-12z^2+3-8z^4+12z^2]/sqrt(6)
       = (4z^4+3)/sqrt(6).

Substitution z=ix uses (ix)^4=x^4, proving strict positivity for every
real x and the explicit violating x=1. Evaluation is after differentiation
in z; differentiating the composed functions p_j(ix) would use another
convention. The printed proof's indices n+1,n+2,n+3 do not license
changing the theorem's literal W(p_2,...,p_n). They are not used to
repair the result. No degrees beyond n=3 are tested.

This finite source-integrity obstruction removes a possible erroneous
import. It gives no independent positivity estimate for the actual Xi
measure and leaves the notebook's main mixed-positivity gap open.

## Mathlib

Full matching coverage of this source-specific audit was not checked.
The cited DLMF identities and the named Carleman criterion are external
inputs; no claim of Mathlib absence or formal verification is made.
