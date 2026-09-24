# Lemma 228: coprime divisor-phase discrepancy

**Hypotheses.** Use the interior box, J=[j0,j1], h and R of L221,
the square-root cells of L225, and C,B_0,L of L227. For each integer
triple a,c,d put v=cd and let D be the real interval of b in [N,2N]
for which

alpha(b)=sqrt(avb-R)>=j0, beta(b)=sqrt(a(v+1)b+R-1)<=j1.

All assertions are for sufficiently large N. Sums over b in D mean
integers. Define the periodic endpoint discrepancy

r_e(b)={alpha(b)/e}-{beta(b)/e}-1_{beta(b)/e is an integer},
P=sum_(a,c,d) (phi(a)/a) sum_(b in D) sum_(e|a) mu(e) r_e(b).

**Conclusion.** With fixed scale constants,

C-B_0=P+O(N³).                                           (1)

Consequently C-B_0=o(B_0) if and only if P=o(B_0). No such
bound for P is asserted. The endpoint atom and every divisor of a
are retained, so (1) does not impose a coprimality independence assumption.

**Proof.**

On L225's candidate interval the cell length ell=beta-alpha is
positive and less than 3/4, and alpha,beta=2N²+O(h).
The cells wholly contained in J form the interval D, explicitly

[(j0²+R)/(av), (j1²-R+1)/(a(v+1))] intersect [N,2N].

L221's strict interior margins show that both displayed endpoints
are strictly inside [N,2N] eventually. Its length is O(h/N+1)
and positive eventually: the leading length is comparable to h/N,
whereas the endpoint subtractions are O(1/N).

A cell containing a selected integer in J but not wholly contained
in J crosses one of j0,j1. At either endpoint t, such a b satisfies
alpha(b)<=t<=beta(b), hence lies in the closed interval

[(t²-R+1)/(a(v+1)), (t²+R)/(av)].

Its length is O(1/N), by direct subtraction and t=O(N²).
It contains O(1) integers. This also covers exact equality at the
closed endpoints of J. Since each cell contains at most one integer,
replacing C by the count over open cells wholly contained in J
costs O(1) per triple, or O(N³) after weighting and summing.
The weights phi(a)/a are at most one. Selected cells are precisely
those of L225; a cell meeting J has b in its candidate interval,
so no additional selected cells enter this replacement.

For real alpha<beta and a positive integer e, the number of multiples
of e strictly in (alpha,beta) is

ceil(beta/e)-floor(alpha/e)-1
 = (beta-alpha)/e+{alpha/e}-{beta/e}-1_{beta/e is an integer}. (2)

The formula holds at integer lower and upper endpoints. For each
positive integer m, finite Möbius inversion gives
1_{gcd(a,m)=1}=sum_(e|a,e|m) mu(e). Summing (2) over e|a
and using sum_(e|a) mu(e)/e=phi(a)/a shows that the coprime
open-cell count is exactly

ell(b) phi(a)/a + sum_(e|a) mu(e) r_e(b).                 (3)

Thus the replacement count equals P+V, where

V=sum_(a,c,d) (phi(a)/a)² sum_(b in D) ell(b).

It remains to compare this real cell-length benchmark with B_0.
On the full real candidate range the same rationalization as in
L225 gives ell=O(1), and differentiation gives exactly

ell'(b)=a/(2 beta)-av ell/(2 alpha beta)=O(1/N).

For any interval I and a continuously differentiable function f on I,
the difference between sum_(n in I) f(n) and integral_I f(x) dx
is bounded by a constant times sup_I |f|+integral_I |f'|.
To see this, compare each full unit subinterval with its value at
one integer endpoint using the integral of |f'|; the at most two
partial end intervals and the possible final integer contribute
O(sup |f|). This proof applies equally to integer endpoints.
Apply it with I=D. Since length(D)=O(h/N+1), the error is O(1).

Extend the integral to all real b, but replace ell(b) by the length
of (alpha(b),beta(b)) intersect J. The only difference is at the
two crossing ranges bounded above; their lengths are O(1/N)
and the integrand is O(1). The support remains inside [N,2N]
by the same interior margins. Fubini for this bounded nonnegative
region now identifies the extended integral as

integral_J [ (m²+R)/(av) - (m²-R+1)/(a(v+1)) ] dm
 = integral_J [m²/(av(v+1))+R/(av)+(R-1)/(a(v+1))] dm.

Open or closed real boundaries have zero area. Since
m²=4N^4+O(N²h), L=length(J)=O(h), av(v+1) is comparable
to N^5, and R is comparable to h, this equals

4N^4 L/[av(v+1)] + O(h²/N³+Rh/N³)
 = 4N^4 L/[av(v+1)] + O(1).

Therefore V=B_0+O(N³): multiplying by (phi(a)/a)² gives
exactly L227's separated benchmark, with no statistical substitution.
Together with (3) and the boundary replacement this proves (1).
L227 gives B_0>=cN²h/log N, so N³/B_0=O(log N/sqrt(N))
tends to zero, proving the stated equivalence.

## Qualifications and verification

This is a reduction with a negligible remainder, not a cancellation
estimate. Bounding each r_e by its absolute value discards the precise
arithmetic information sought. In particular the e=1 phase alone does
not describe the coprime count. Neither divisor truncation nor removal
of the endpoint atoms is justified here. Other progression estimates,
the signed comparison and RH remain unproved.

Analytic checks establish boundary costs, the derivative identity,
finite Möbius inversion, bounded-region Fubini and the benchmark error.
`python3 scripts/heat/check_coprime_cell_inversion.py` verifies strict
open-cell divisor inversion with exact integer radicands, including
square endpoints. It does not establish asymptotic distribution.

**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
