# Lemma 810: counterexample to the printed uniform staircase bound

## Hypotheses

For an integer d>=2 and a real number 0<tau<1, define the finite sum

\[
 S_d(\tau)=\sum_{k=0}^{d-2}\binom dk
             \tau^{(d-2-k)/2-1}.
\]

The audited assertion is the existence of a finite absolute constant C,
independent of both d and tau, such that S_d(tau)<=C d^(10/3) on this
whole domain. The source is Michel Planat, *Asymptotic Hyperbolicity of
Jensen Polynomials and the Finite-Strip Obstruction for the Riemann
Hypothesis*, Preprints202604.1239v2, posted 20 April 2026, Section 3.3,
embedded Lemma 11 in the proof of Theorem 3.2,
[versioned manuscript](https://www.preprints.org/manuscript/202604.1239/v2).
This audits the inequality transcribed in the prior source assessment;
the later published version and its possibly different text are not used.

## Conclusion

There is no such C. More strongly, for every fixed integer d>=2,
S_d(tau) is unbounded as tau decreases to zero. The printed bound cannot
be used as a uniform input on its stated domain.

This does not disprove a restricted-domain inequality, the source's
downstream hyperbolicity conclusion, or RH. No identification of the
source's polynomial convention with actual Xi is assumed.

## Proof

All summands are positive: the binomial coefficients are positive at
the displayed indices and a positive real base raised to any real power
is positive. At the included endpoint k=d-2 the exponent is -1 and
binom(d,d-2)=d(d-1)/2. Therefore

\[
 S_d(\tau)\ge\frac{d(d-1)}{2\tau}.
\]

For any fixed admissible d the numerator is strictly positive; this
lower bound tends to infinity as tau decreases to zero. The purported
upper bound C d^(10/3) is finite and independent of tau.

An exact admissible family already occurs at d=2. The sum has only k=0,
so, for every integer n>=2, tau=1/n belongs to (0,1) and

\[
 S_2(1/n)=n.
\]

If the claimed C existed, it would give n<=C 2^(10/3) for every integer
n>=2, contradicting the Archimedean property. This also covers any
nonpositive C, since the left side is positive. No numerical sweep,
asymptotic interchange or analytic estimate is required.

The elementary proof is included because validity of this suspect
uniform source claim is the approved audit target. It is a local
counterexample verification, not a claim of a new general theorem.
The obstruction uses the exact quantifiers; silently imposing a
relation between d and tau would change the claim and require separate
assessment. No repair is attempted here.

## Mathlib

Full matching coverage is not checked. No formal verification or
absence claim is made. The proof uses only a binomial endpoint identity,
positivity of real powers, and the Archimedean property.
