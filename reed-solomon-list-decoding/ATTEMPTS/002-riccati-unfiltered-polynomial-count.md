# A polynomial count of all small-characteristic Riccati solutions

Tested on 2026-09-25: use reciprocal differences and polynomial pole
cancellation to bound all degree-less-than-k solutions of
aP'+bP^2+cP+d=0 by a polynomial in k and the coefficient degrees,
uniformly over fields of a fixed odd characteristic. Such a bound could
control a branch before imposing agreement.

## WHY IT FAILS

The [full result](../lemmas/L009-riccati-divisors-and-unfiltered-counts.md)
gives an exact divisor test, but also constructs a superpolynomial
number of polynomial solutions with first derivative order one,
dependent-variable degree two, and X-degree linear in the message
cutoff. Thus an unfiltered polynomial count for this class is false;
the issue is not merely an inefficient estimate for divisor numbers.
This does not supply a large list around one received word, reject
geometric overcovers followed by agreement filtering, or disprove the
grand challenge. The pole-cancellation classification is retained.
