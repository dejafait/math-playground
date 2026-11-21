# Lemma 763: fixed Gaussian unshifted Turan budget obstruction

## Hypotheses

Use the actual completion xi of L018 and the moments of L021. Put

    gamma_j = j! M_(2j)/(2j)!,
    Theta(z) = sum_(j>=0) gamma_j z^j/j! = xi(1/2+sqrt(z)).

The last expression denotes the entire series, independent of the square-root
branch. In particular gamma_0=M_0>0 and gamma_2=M_4/12>0. Fix a real
a>0, independent of the integer degree d. For a series F define

    g_d^*(F;X) = sum_(j=0)^d binom(d,j) F^(j)(0) X^(d-j),
    Q_d^(a)(X) = g_d^*(Theta(z) exp(-a z^2);X).

Use the physicists' Hermite basis

    H_m(x) = m! sum_(r=0)^floor(m/2) (-1)^r (2x)^(m-2r)/(r!(m-2r)!).

## Conclusion

For d>=2 the normalized left side of O'Sullivan's sufficient Turan
criterion, applied to Q_d^(a)(2sqrt(a)x), is exactly

    B_d(a) = sum_(j=2)^d [d binom(d,j)/(2^j j! a^j)] (gamma_j/gamma_0)^2.

The criterion requires B_d(a)<1. But

    B_d(a) >= d^2(d-1)/(16a^2) (gamma_2/gamma_0)^2.

Consequently it fails for every integer d>=D(a), where

    D(a) = max{2, ceil((32a^2 gamma_0^2/gamma_2^2)^(1/3))}.

Thus no fixed a>0 satisfies this particular sufficient budget in every
unshifted degree. In any degree where the strict budget holds,
it is necessary that a> d sqrt(d-1) gamma_2/(4gamma_0).
These statements do not assert failure of hyperbolicity, failure of any
other sufficient criterion, or failure of RH. No input root signs are used.

## Proof

The imported criterion is Cormac O'Sullivan, *Zeros of Jensen polynomials
and asymptotics for the Riemann xi function*, arXiv:2007.13582v2,
9 December 2020, [Theorem 8.1, equation (8.1)](https://arxiv.org/html/2007.13582v2#S8):
for real c_k, a degree-d polynomial sum_(k=0)^d c_k H_k has simple real
zeros if

    sum_(k=0)^(d-2) 2^k k! c_k^2 < 2^d (d-1)! c_d^2.

The paper attributes this theorem to Turan (1959), Theorem III; that original
proof is not independently audited here. We use the criterion as stated,
without a reproof or any assertion of necessity. Its application to the
actual coefficients at a=1 is O'Sullivan's (8.2). The only specialization
needed here is the positive-parameter normalization and a retained term.

Expansion of the Gaussian gives, by a finite coefficient calculation,

    g_m^*(exp(-a z^2);X)
      = sum_(r=0)^floor(m/2) m! (-a)^r X^(m-2r)/(r!(m-2r)!)
      = a^(m/2) H_m(X/(2sqrt(a))).

Leibniz's rule, or O'Sullivan's Lemma 3.4/(3.3), therefore gives

    Q_d^(a)(2sqrt(a)x)
      = sum_(j=0)^d binom(d,j) gamma_j a^((d-j)/2) H_(d-j)(x).

All identities are finite; no integral or infinite-series interchange is
needed. The source HTML's intermediate Gaussian expansion in section 3.2
displays X^(d-j), whereas the defining reciprocal Jensen polynomial gives
X^(d-2j). The calculation above fixes this power directly and agrees with
the source's resulting Hermite identity and (3.6).

Thus c_(d-j)=binom(d,j)gamma_j a^((d-j)/2), and c_d=gamma_0 a^(d/2)>0.
The change of variable is real and invertible, so preserves real-rootedness.
Divide the criterion by its positive right side and set k=d-j. For j>=2
the resulting summand is

    [2^(d-j)(d-j)! binom(d,j)^2 gamma_j^2 a^(d-j)]
       /[2^d(d-1)! gamma_0^2 a^d]
      = [d binom(d,j)/(2^j j! a^j)] (gamma_j/gamma_0)^2.

This proves the exact budget formula. Every term is nonnegative. Retaining
j=2 gives the asserted lower bound. For d>=2, d-1>=d/2, hence

    B_d(a) >= d^3 gamma_2^2/(32a^2 gamma_0^2).

The definition of D(a) makes this at least one for every d>=D(a), including
equality, which already violates the strict criterion. Positivity of the
two actual coefficients is unconditional by L021. Solving the retained-term
strict inequality for a gives the final necessary condition. This is a
symbolic obstruction to the budget alone, not a zero certificate.

## Mathlib

Not checked. Availability of a full matching theorem in Mathlib is unknown.
The finite algebra above is supplied explicitly; no formal verification is
claimed. General reference: https://leanprover-community.github.io/mathlib4_docs/ .
