# Lemma 206: fixed-prime-band joint divisor bound

**Hypotheses.** Use L202's actual box F_N with fixed t>0, and L205's
m0=floor(sqrt(abcd))+1 and selected set S_D. Fix real cutoffs
2<=z<Y independently of N; D is the product of primes at most z.
Let B_(z,Y) count tuples of S_D for which some prime z<p<=Y divides
both m0 and ab.

**Conclusion.** For each fixed prime p,

#{tuple in F_N: p divides m0 and a}/#F_N -> 1/p²,
#{tuple in F_N: p divides m0 and b}/#F_N -> 1/p².       (1)

Consequently

limsup_(N->infinity) B_(z,Y)/#F_N
 <= 2 sum_(z<p<=Y) 1/p² <= 2/floor(z).                (2)

The bound is independent of fixed Y after taking the limit. It does
not assert uniformity in Y or control L205's whole T_z.

**Proof.**

Write A=2N²-2tN^(3/2), B=2N²-tN^(3/2), and let P_N count
pairs (a,b) with 11N/10<=a<=6N/5 and A<=ab<=B. For each a,
its number of b values is

q_a=tN^(3/2)/a+O(1).

L202 proves P_N is comparable to N^(3/2) and #F_N=P_N².
For fixed p the number of these pairs with p dividing b is
P_N/p+O_p(N): count multiples in each b interval, with bounded
rounding error per a. The number with p dividing a is also
P_N/p+O_p(N). Indeed, for g(y)=1/y on the a interval, grouping
consecutive integers in blocks of length p gives

sum_(a: p divides a) 1/a = (1/p) sum_a 1/a + O_p(1/N).

Within a complete block the variation of g is O_p(N^(-2));
there are O(N) blocks and at most two incomplete end blocks,
whose contributions are O_p(1/N). Multiply by tN^(3/2) and
include the O(N) errors from q_a. Thus the proportion of tuples
of F_N with p dividing either specified factor a or b separately
tends to 1/p.

We next prove the extra conditional factor 1/p for m0. Fix an
allowed triple a,c,d. On either the full b interval, or its
progression b=r+pj (using consecutive allowed integer j), consider

f(j)=sqrt(acd(r+sj))/p,

where s=1 for the full interval and s=p for a progression. The
origin r may be shifted to its first allowed value. The number n
of terms is comparable to sqrt(N)/s, for fixed p. On its full
real interval,

f'''(y)=3 sqrt(acd) s³ / (8p(r+sy)^(5/2)).             (3)

All factors are comparable to N, so for fixed p and s its
magnitude is between positive constant multiples of 1/N, uniformly
in the triple. For each fixed nonzero integer k the named
third-derivative test recorded in foundations, applied to kf,
gives

|sum_j e(kf(j))|/n = O_(t,p,k)(N^(-1/12)) = o(1).      (4)

Here s is either 1 or p and is fixed. The implied bound is uniform
over triples and over the residue r.

To pass from (4) to interval counts needs no assumption about
boundary points. Continuous periodic piecewise linear upper and
lower approximations to an interval indicator can be chosen with
integrals within any epsilon of its length: replace each endpoint
jump by a linear ramp of width at most epsilon/4, treating a closed
or half-open endpoint by the corresponding upper or lower ramp.
Their Fourier coefficients are O_(epsilon,p)(k^(-2)) by integrating
on their finitely many linear pieces twice. Their series converge
uniformly and equal the functions by Fejér's theorem. Truncate the
series first, then use (4), then let epsilon decrease. This proves
uniform interval frequencies equal to interval length on the unit
circle.

For x=sqrt(abcd), the exact event p divides floor(x)+1 is

frac(x/p) in [(p-1)/p,1).

This equivalence includes integer x: the left endpoint qualifies,
whereas the right endpoint, identified with zero, does not. The
preceding interval argument handles both endpoints. Hence the
frequency of p dividing m0 is 1/p+o(1), uniformly on each full
slice and each b progression modulo p.

For tuples with p dividing a use the full slices and sum their
uniform error over those triples. For tuples with p dividing b
use the residue-zero b progression for every triple. The pair
counts already proved show in both cases that the restricted
population is (1/p+o(1))#F_N. Multiplying by the uniform conditional
frequency proves (1).

If a prime divides ab it divides a or b. The union bound, (1),
and S_D contained in F_N give the first inequality of (2), since
only finitely many primes are being summed. For M=floor(z),

sum_(integers n>z) 1/n² <= integral_M^infinity x^(-2) dx = 1/M.

Replacing the prime sum by this integer sum proves the second.

## Precise remaining obstruction

Define R_(z,Y) to count tuples of S_D with a common prime p>Y
of m0 and ab. Then

T_z <= B_(z,Y)+R_(z,Y).

Thus (2) leaves the iterated tail quantity

lim_(Y->infinity) limsup_(N->infinity) R_(z,Y)/#F_N

uncontrolled. Even proving that quantity is zero would require
an additional argument. All common primes are at most 2N by
L202, but (4) does not permit putting Y=2N into (2).
For example on a b progression of step p, n is comparable to
sqrt(N)/p only while rounding is negligible. When p is comparable
to sqrt(N), it can have bounded length. There is then no
slice equidistribution consequence of the fixed-p proof.
This identifies a limitation of this method on the actual slices,
not a counterexample to the desired T_z estimate.

## Qualifications and verification

The finite-band estimate concerns actual integer factor tuples and
exact rounding, not independent random residues. It establishes a
scoped part of large-prime deletion only. Full coprimality, the
specified T_z threshold, totient selection, and RH remain unproved.
Analytic verification checks the integer interval errors, weighted
residue count, derivative (3), uniformity before summing slices,
and the order of the three fixed-parameter limits. No numerical
population evidence is used.
**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
