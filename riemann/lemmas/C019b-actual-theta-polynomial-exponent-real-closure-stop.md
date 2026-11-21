# Corollary C019b: real-axis closure excludes the fixed polynomial-exponent family

## Hypotheses

Let K be the full theta kernel of L019, extended evenly as justified
in C019a. Let I=[-1/10,1/10]. Consider even polynomials P with real
coefficients such that P(0)=0, every zero of P' is real (with arbitrary
multiplicity), and P(iu) tends to minus infinity as real |u| tends to
infinity. The value P(iu) is real for real u.

## Conclusion

There is no sequence of these polynomials P_n for which exp(P_n(iu))
converges uniformly on I to K(u)/K(0). Thus the normalized actual
kernel is outside the uniform closure on this fixed interval of this
specified exponent family. This is a necessary local approximation
obstruction, not an assertion about the zeros of Xi or RH.

## Proof

**Every allowed profile is absolutely monotonic.** Decay excludes a
constant P. Write deg P=2d, d>=1, and let a be its leading coefficient.
Since P' is odd and has only real zeros, it factors as

    P'(z)=c z^(2m+1) product_(j=1)^N (z^2-r_j^2),
    c=2d a, m>=0, r_j>0, m+N=d-1.

Here the positive roots r_j are listed with multiplicity; N=0 is allowed
and its product is 1. The odd multiplicity at zero is exactly 2m+1.
These exhaust the degree 2d-1, so the factorization includes all repeated
and zero-root cases. The leading term on the imaginary axis is
a(-1)^d u^(2d). Decay therefore implies a(-1)^d<0, equivalently
c(-1)^(d-1)>0.

The definition F_P(x)=-P(i sqrt(x)) is a real polynomial in x, since
P is even. For x>0 differentiation and the factorization give

    F_P'(x)=(-i/(2 sqrt(x))) P'(i sqrt(x))
           =(c/2)(-1)^(m+N) x^m product_(j=1)^N (x+r_j^2)
           =(c/2)(-1)^(d-1) x^m product_(j=1)^N (x+r_j^2).

This is also a polynomial identity, hence holds at zero. Its scalar
factor is strictly positive and all its coefficients are nonnegative.
Since F_P(0)=0, integration shows every coefficient of F_P is
nonnegative too. Every derivative of every order, including order zero,
is consequently nonnegative for x>=0; derivatives above the degree
are zero. Thus F_P is absolutely monotonic on [0,1/100), with no
degree bound or simple-root assumption.

**The given convergence transfers through the real logarithm.** Suppose
for contradiction that the sequence in the conclusion exists. Set
q(u)=K(u)/K(0). L019 gives positivity for u>=0; C019a gives evenness
and continuity, so q is strictly positive on I. By compactness its
minimum mu is strictly positive. Uniform convergence gives
q_n(u)=exp(P_n(iu))>=mu/2 on I for all sufficiently large n. The real
logarithm has derivative at most 2/mu on [mu/2,infinity), and hence

    sup_I |log q_n-log q| <= (2/mu) sup_I |q_n-q| -> 0.

For real u, log q_n(u)=P_n(iu), without a complex branch choice.
Substitute u=sqrt(x), 0<=x<=1/100, and negate. It follows that the
absolutely monotonic polynomials F_(P_n) converge uniformly, in
particular pointwise on [0,1/100), to the finite function

    F_K(x)=-log(K(sqrt(x))/K(0)).

Apply the one-variable case of A. G. Konheim and B. Weiss,
*Functions which operate on characteristic functions*, Pacific J.
Math. 15(4) (1965), 1279--1293, Section 2, definition and Lemma 3,
pp.1283--1284:
[publisher PDF](https://msp.org/pjm/1965/15-4/pjm-v15-n4-p15-s.pdf).
The lemma states closure under finite pointwise limits of absolutely
monotonic functions on 0<=x<a (in several variables; use dimension
one and a=1/100). Its definition includes order zero. All these
hypotheses were verified above. No assertion at the right endpoint
is needed; no operator-on-characteristic-functions hypothesis from
other parts of the paper is used. This imports the known closure
theorem, rather than reproving it or differentiating a uniformly
convergent sequence.

**The actual cubic coefficient contradicts closure.** Use C019a's
holomorphic even germ

    G(z)=log(K(-iz)/K(0)), h=G', a_j=h^(j)(0).

Near zero the even series gives

    G(z)=a_1 z^2/2! + a_3 z^4/4! + a_5 z^6/6! + O(z^8).

Substituting z=i sqrt(x) first for small nonnegative x, and using the
unique real logarithm of the positive kernel, gives

    F_K(x)=-G(i sqrt(x))
          =a_1 x/2 - a_3 x^2/24 + a_5 x^3/720 + O(x^4).

Even analyticity makes this an analytic germ in x at zero; the square
root causes no regularity loss. In particular F_K'''(0)=a_5/120.
The independently audited strict rational enclosure in C019a is

    -1548.74555 < a_5 < -1548.74554 < 0.

Therefore F_K'''(0)<0, contrary to absolute monotonicity. Even an
interior-only formulation of the closure conclusion would contradict
this: the analytic third derivative stays negative on a sufficiently
short positive interval. The linear and quadratic coefficients are
positive by C019a's a_1>0 and a_3<0; it is precisely the cubic
coefficient that fails. This comparison uses the audited data through
order six, not another numerical computation or a higher-order test.

**Qualifications and use.** This specializes a known closure theorem
and existing certified actual-kernel derivatives. It strengthens the
local route obstruction from exact matching of complex jets to the
specified real uniform approximation family, without claiming novelty
beyond the sources checked. It does not exclude other exponent classes,
other approximation topologies, or other sufficient constructions.
Global tails, complex transform convergence, actual-Xi all-degree
algebraic-square positivity, initialization, singular blocks and
identification remain unresolved. No RH assumption is used.

**Independent fixed audit1333 (17 November 2026).** The all-degree
factorization and limit argument were replayed against L019, audited
C019a and the previously inspected Konheim--Weiss statement. An odd
nonzero polynomial P' has odd multiplicity at zero; its other real
roots occur in opposite pairs with equal multiplicity. Counting these
roots gives 2m+1+2N=2d-1, including d=1 and N=0. Substitution into
-i P'(i sqrt(x))/(2 sqrt(x)) contributes the sign
(-i)i^(2m+1)(-1)^N=(-1)^(m+N). The decay condition gives exactly
c(-1)^(d-1)>0. Thus the displayed nonnegative-coefficient assertion
holds in every permitted degree and does not require simple roots.
The identity extends polynomially to x=0, so no division by sqrt(x)
at the origin is used.

The minimum mu exists and is positive because L019 supplies strict
positivity on [0,1/10] and C019a supplies evenness and continuity.
Both arguments of the logarithm lie in [mu/2,infinity) eventually;
the stated Lipschitz bound therefore applies to every u in I.
The substitution x=u^2 uses only u>=0, a subset of I, and gives a
finite pointwise limit on exactly the half-open source domain.
Konheim--Weiss Section 2 Lemma 3 is imported with n=1, a=1/100;
order-zero nonnegativity has been checked as well as all derivatives.
Neither a value of a derivative at the right endpoint nor convergence
of the derivatives of F_(P_n) is assumed. The source's general
closure theorem is not reproved in this audit.

For the coefficient check, h=G' means that a_5=h^(5)(0)=G^(6)(0).
The three substitutions (i sqrt(x))^2=-x, its fourth power=x^2,
and its sixth power=-x^3 give the displayed expansion with its outer
minus sign. Hence the cubic Taylor coefficient is a_5/720 and its
third derivative is 3!a_5/720=a_5/120. The holomorphic logarithm
agrees with the real logarithm on a sufficiently short positive
real-u interval: both exponentiate to the same positive function,
are continuous, and agree at zero. The even germ then gives an
analytic x-series, so the negative derivative also persists at
interior positive x if the closure theorem is used only there.
The strict a_5 enclosure is the already independently certified input
of C019a; its numerical producer was not rerun or recertified here.

All nominated proof obligations pass. This completes the previously
pending proof audit, with no mathematical repair, new numerical
evidence, stronger approximation claim or new general theorem.
It validates only this fixed-family stop and retains every independent
gap listed above. The primary source inspection is reused from
assessment1331 and its approved predecessors, not claimed as fresh
retrieval. Full matching Mathlib coverage remains unchecked.

## Mathlib

Full matching coverage for this actual-theta closure exclusion and
Konheim--Weiss Lemma 3 has not been checked. Supporting smooth-series
and Gaussian results are recorded in L016; they do not supply the full
closure theorem. Unknown coverage is not evidence of absence.
