# L496 — Uniform finite Euler-phase floor

## Hypotheses

Use the exact Polymath prefactor M_t and alpha of L494 and the real-axis
definitions of L495. In particular, at fixed real t put

    z=(1+i*x)/2, nu=z+(t/2)*alpha(z),
    alpha(z)=1/(2*z)+1/(z-1)+(1/2)*Log(z/(2*pi)),
    b_p=exp(t*log(p)^2/4), A_p=b_p*p^(-nu),
    r_p=|A_p|, E_prod=product_(p<=307, p prime)(1-A_p),
    Theta=arg M_t(z), ell=4*(Theta-arg E_prod)'.

All derivatives are spatial, with t fixed; phases are locally chosen
where the corresponding functions do not vanish. Assume the closed domain

    .16836<=t<=.1718, x>=X=6000284561421.5,
    t*log(x/(4*pi))<=5.17.

Finite decimals denote exact rationals. The base-phase theorem imported
below retains its source-proof qualification; neither the Planat manuscript
nor its underlying Polymath saddle estimates are independently audited here.

## Conclusion

Every Euler factor is nonzero, and uniformly on the stated domain,

    r_p < .32926 < 1 for every prime p<=307,
    |nu'| < .500000000001,
    ell > 24.18022820120389 > 24.18.

This reproduces the scalar phase-floor method and numerical threshold in
Michel Planat, *Collective Contraction in the de Bruijn–Newman Heat Flow:
Off-Zero Logarithmic Derivatives and Certified Barrier Refinements*,
[arXiv:2609.37164v2, 7 October 2026](https://arxiv.org/html/2609.37164v2),
Lemma 6.3 (PDF pp.18–19), Section 6.6 and Proposition 6.8 (pp.22–23),
and Section 6.7 (pp.26–27). The endpoint certificate here is standalone;
no source coefficient ledger, reserve or reported decimal is assumed.
The independent local audit of 2026-10-30 accepts this transcription,
corner reduction and complete arithmetic; Section 5 records its evidence.
No collision exclusion, all-height sign theorem or RH conclusion follows.

## Proof

### 1. Imported base phase and exact Euler loss

Planat v2 Lemma 6.3 states, in precisely this M_t normalization, that

    4*Theta' > log(x/(4*pi))

for x>=6000284561419.5 and .16836<=t<=.2. Our lower height is
two units larger and our time interval is contained in that interval.
Thus this cited conclusion applies including the local closed endpoints.
Only this base-phase theorem is imported; its proof is not reproduced.
It does not already incorporate the Euler-phase loss.

L495's equation (10), obtained by finite product differentiation, gives

    J=sum_(p<=307) log(p)*A_p/(1-A_p),
    ell=4*Theta'-4*Im(nu'*J).                              (1)

We first establish r_p<1 below, so this identity and differentiable local
arguments are legitimate. The nonzero M_t follows from its explicit
prefactor and principal branch at Im(z)>0. For any common upper bound c
for |nu'|, (1) and the triangle inequality give

    ell > log(x/(4*pi))-4*c*sum_p log(p)*r_p/(1-r_p).       (2)

In particular (2) retains the entire Euler loss and the factor four.
It does not substitute the base logarithm for the mollified phase.

### 2. Uniform derivative cap and worst-corner reduction

The exact real part of nu is

    sigma=.5+(t/4)*Lstar(x)-t/(2*(1+x*x)),
    Lstar(x)=log(sqrt(1+x*x)/(4*pi)).                       (3)

Indeed the real parts of 1/(2*z) and 1/(z-1) are respectively
1/(1+x*x) and -2/(1+x*x). The logarithm contributes Lstar/2
to Re(alpha). Also

    alpha'=-1/(2*z^2)-1/(z-1)^2+1/(2*z),
    nu'=(i/2)*(1+(t/2)*alpha').

Since |z|=|z-1|=sqrt(1+x*x)/2>=x/2 and x>6,

    |alpha'|<=1/x+6/x^2<1/(x-6),
    |nu'|<=.5+(t/4)*|alpha'|
          <.5+.1718/(4*(X-6))<.500000000001=c.             (4)

The last rational comparison is recorded in the certificate. From (3),

    sigma_x=(t/4)*x/(1+x*x)+t*x/(1+x*x)^2>0,
    sigma_t=Lstar(x)/4-1/(2*(1+x*x)).                      (5)

The certificate verifies the strict inequality

    log(307)+2/(1+X*X)<Lstar(X).                           (6)

Lstar increases with x and 2/(1+x*x) decreases, so sigma_t>log(p)/4
for every prime p<=307 throughout x>=X. Writing h=log p>0, the
exact heat weight gives

    log r_p=t*h*h/4-sigma*h,
    (log r_p)_x=-h*sigma_x<0,
    (log r_p)_t=h*h/4-h*sigma_t<0.                         (7)

Thus r_p(x,t)<=r_p(X,.16836). Once these corner values are below
one, each h*r/(1-r) is bounded by its corner value, since its
derivative in r is h/(1-r)^2>0. Meanwhile log(x/(4*pi)) increases.
Consequently the right side of (2), with c from (4), is at least

    F0=log(X/(4*pi))
        -4*c*sum_(p<=307) h*r_p(X,.16836)/(1-r_p(X,.16836)). (8)

The reduction actually holds on the enclosing rectangle x>=X,
.16836<=t<=.1718. It therefore covers the constraint t*log(x/(4*pi))
<=5.17 and every closed boundary without an initial-band restriction.
It uses no time derivative of the finite cutoff or of a coefficient ledger.

### 3. Complete rational endpoint certificate

Reproduce from this notebook with

    python3 scripts/heat/finite-euler-phase-floor-certificate.py

The full artifact is
`scripts/heat/finite-euler-phase-floor-certificate.json`.
It stores every prime, logarithm, exponent, radius, denominator and
loss summand, all transcendental-series endpoints and tails, and all
71 comparisons with their actual/required rational bounds and failures.
All operations use exact Fraction arithmetic with outward rounding
to the rational 10^(-70) grid. Printed decimals are directed summaries;
the comparisons use the rational endpoints, not those printed decimals.

Here is a justification of the enclosures used by the program.
Machin's standard identity is pi=16*arctan(1/5)-4*arctan(1/239).
For each arctangent, the alternating series through j=99 has its
value between the partial sum and that sum plus
1/((201)*n^201), where n is 5 or 239. Outward subtraction gives
a pi interval; monotonicity of log then bounds log(4*pi).

For any positive rational q, exact powers of two give q=2^k*v,
1<=v<2. Put u=(v-1)/(v+1), so 0<=u<=1/3. Then

    log(v)=2*sum_(j>=0) u^(2j+1)/(2j+1).

After j=99, the remaining positive sum is at most

    2*u^201/(201*(1-u*u)).

The program bounds powers recursively, rounding outward each time,
and uses the upper next power in this tail. It treats log 2 by the
same series with v=2, and combines k*log 2+log v by signed interval
arithmetic. Hence negative k and rational interval arguments are covered.
In (3) it evaluates Lstar(X) as log(1+X*X)/2-log(4*pi), avoiding
an uncertified square root. Every rational operation is enclosed by
endpoint arithmetic with outward rounding.

To evaluate exp(q), put a=|q|. Positive Taylor terms through degree
180 are bounded recursively and summed outward. The positive tail is
at most

    upper_term_180*(a/181)/(1-a/182),

because every ratio after the first omitted term is at most a/182<1;
this condition is asserted for each argument. Negative q uses reciprocal
endpoints of this positive enclosure. For an interval argument the
program evaluates its two endpoints, using monotonicity. All denominator
intervals are checked away from zero before division.

Trial division through floor(sqrt(p)), computed by integer isqrt,
enumerates exactly the 63 primes in [2,307]. Each composite has such
a divisor; thus no prime is omitted. At the corner, every radius upper
endpoint is below one; the largest is below
.3292598589242600065751. The rational interval (8) is contained in

    [24.18022820120389189144, 24.18022820120389189145].

The computed lower endpoint is strictly above the left displayed bound;
the computed upper endpoint is below the right displayed bound.
In particular F0>24.18022820120389>24.18. All 71 comparisons pass,
with no failures. Equations (2), (4), (7) and (8) prove the conclusion.

### 4. Scope and remaining gaps

This is a source-method reproduction and local uniform specialization,
not a claim of progress beyond the cited phase-floor method. The source
reports 24.18022820120347; the standalone enclosure is slightly larger,
but no optimized threshold or new mechanism is claimed. The statement
retains its imported base-phase qualification. Section 5 independently
audits this local proof and certificate, including L495 (8)-(10) as used
here; the rest of L495's transcription is outside this audit.

Neither the mollified coefficient mass, strict reserve, H1, collision
exclusion, other times nor zero time is established. Those independent
gaps cannot be inferred from a positive phase denominator. No actual
off-line zeta zero or complete proof candidate is produced.

### 5. Independent local audit — 2026-10-30

The audit accepts the stated constants and closed domain without repair.
Its source coverage is the prior SPECIALIZE assessment
`drafts/literature/2026-10-30-l496-independent-audit-coverage.md`, reusing
the inspected primary statements and proof cases recorded in
`drafts/literature/2026-10-30-finite-euler-phase-floor-coverage.md`.
Planat v2 Lemma 6.3 is still imported, not independently proved. Its
lower height, lower time and upper time contain the entire local domain,
including endpoints; its phase is the exact M_t phase used here.

For the local normalization, logarithmic differentiation of L494's M_0
gives alpha, and that of M_t gives alpha+(t/2)*alpha*alpha'. With
z'=i/2, these are precisely L495 (8). Finite differentiation gives
(1-A_p)'=nu'*log(p)*A_p, hence E_prod'/E_prod=nu'*J and (1), with
the minus sign and factor four retained. Both M_t and every Euler
factor are nonzero; argument derivatives are therefore legitimate local
derivatives, independent of the argument branch. No cutoff is varied.

The audited real-part computation gives (3); differentiating it gives
(5) and the equivalent sigma_x=t*x*(x*x+5)/(4*(1+x*x)^2)>0.
The bound 1/x+6/x^2<1/(x-6) has positive difference
36/(x*x*(x-6)). The complete endpoint comparison (6) is strict, so
sigma_t>log(p)/4 uniformly for every listed prime and all x>=X.
Thus both derivatives in (7) are negative. Connecting a point to the
corner within the enclosing rectangle proves the comparison, even if
that path leaves the smaller t*log(x/(4*pi)) domain. The rectangle
itself satisfies every premise actually used. No maximum over a sampled
grid is substituted for this argument. The positive denominator and
monotonicity of r/(1-r) justify (8) uniformly.

The independent consumer, which neither imports nor executes the producer,
is reproduced from the notebook by

    python3 scripts/heat/l496-certificate-audit.py

It reads every load-bearing field of the original JSON and writes
`scripts/heat/l496-certificate-audit.json`, including input/producer/consumer
SHA-256 hashes, all comparisons with exact actual/required values and
failures. The original producer and certificate are preserved unchanged.

Here is why this is a check independent of the producer's PASS flag.
Intervals in the consumer are rational endpoint pairs; sums, differences,
the four product endpoints and reciprocal endpoints give outward bounds.
Signed multiplication handles negative logarithm range-reduction powers.
Its 10^(-90) floor/ceiling rounding is exact integer division. Instead of
the producer's forward recurrences, it encloses the finite logarithm sum
by Horner evaluation of z*sum_(j=0)^99 (z*z)^j/(2j+1), and the exponential
sum by the backward recurrence P=1, P=1+(a/k)*P for k=180,...,1.
Binary interval powering separately checks each omitted log power and
last exponential term (dividing by 180! for the latter). Induction through
these operations encloses the exact finite sums/powers. The consumer
requires those intervals to lie inside the original stored intervals;
containment of a known enclosure proves the stored one valid.

It verifies both exact alternating arctangent sums, the signs and rational
tails, every logarithm transform and exact power-of-two identity, and
every exponential tail ratio and reciprocal denominator. The remainder
inequalities proved in Section 3 then enclose the actual transcendental
values, not merely their truncated sums. Each stored tail is checked
against its exact formula using the now-validated sum/power endpoint.
It checks the Machin combination and every corner/radius/denominator/loss
operation against these primitives. An independent Eratosthenes sieve
matches the complete ordered prime list and all rows, with no duplicates.
The complete loss sum, phase interval and each of the 71 strict comparison
operands are reconstructed; stored booleans are checked only afterward.

All 393 primitive evaluations, 63 prime rows and 71 source comparisons
pass, for 3163 independent checks and zero failures. The scalar lower
endpoint exceeds 24.18 by more than .0002282012038918914497. The largest
radius upper endpoint, at p=2, is below .329259858924260006575019;
the derivative upper bound is below .500000000000007157993852.
Both displayed phase endpoints in Section 3 are confirmed. These are
directed rational bounds, not floating-point agreement or source decimals.

This establishes local verification of the source-method reproduction,
not progress beyond the cited method, a whole-manuscript audit or any
strict coefficient reserve. The independent gaps in Section 4 remain.

## Mathlib

Full matching coverage was not checked and remains unknown. The argument
uses finite-product phase differentiation, elementary logarithm/exponential
monotonicity and series remainder estimates, and the standard Machin
identity. No matching Mathlib theorem or formalization of the imported
base-phase theorem or this rational program is asserted. A rational
certificate is not itself a Lean proof.
