# L034 — Cyclic minimum count and a two-postspell parameter cutoff

## Hypotheses

Let T(t)=t/2 for even positive integers and T(t)=(3t+1)/2 for
odd positive integers. O and E designate the actual input parities,
with the word and junction conventions of L020/L021.
For i=1,2 let J_i>=2, H_i>=3 and a_i>=0 be integers with
a_i congruent to 2 modulo 18; in particular a_i>=2. Put

\[
W_i=(OOEO)^{J_i}O^{H_i}E^{a_i},\qquad
D_i=4J_i+H_i+a_i,\qquad N=D_1+D_2.
\]

Suppose n>1 is a positive odd integer congruent to 20 modulo 27,
the concatenation W_1 W_2 is actual at n, its junction
x=T^{D_1}(n) is positive, odd and congruent to 20 modulo 27,
and T^N(n)=n. These are conditional hypotheses, not an assertion
that the unresolved affine divisibility condition has a solution.
No first-return, distinct-junction, primitive-period or least-root
assumption is imposed.

## Conclusion

The cyclic list T^t(n), 0<=t<N, has exactly

\[
\boxed{M=J_1+J_2+2}
\]

strict local-minimum occurrences. Occurrences are indexed by time,
so repeated values are retained. Consequently every actual closed
word under these hypotheses necessarily satisfies

\[
\boxed{J_1+J_2\ge90.}
\]

Thus the region J_1+J_2<=89 is excluded for all the allowed H_i,a_i.
The converse is not asserted, and the bound is not claimed optimal.
Closure with larger parameters, other cycles, divergent orbits and
universal eventual descent remain unresolved.

## Proof

### Exact cyclic count

Write u_t=T^t(n) and index u_t and its input letter modulo N,
using closure. Both branch maps preserve positivity. At an O input,
T(u_t)-u_t=(u_t+1)/2>0; at an E input,
T(u_t)-u_t=-u_t/2<0. It follows that

\[
u_t<u_{t-1}\ \hbox{and}\ u_t<u_{t+1}
\quad\Longleftrightarrow\quad
\hbox{the input letters at }t-1,t\hbox{ are }E,O.
\]

There are no flat steps. This is exactly the local-minimum notion
in the cited cycle definitions, equivalently the starts of maximal
odd runs following maximal even runs.

Each copy of OOEO contains one E, immediately followed by its
last O. This accounts for J_i transitions E to O in W_i. Between
successive copies the last O is followed by the next initial O;
after the last copy the last O is followed by O^{H_i}. Neither
boundary introduces an additional E to O transition. The transition
from that final odd run to E^{a_i} is O to E. Within E^{a_i}
all letters are E, so there are no E to O transitions there.

At the W_1 to W_2 junction the last letter of the nonempty first
tail is E and the first letter of W_2 is O, giving exactly one more
minimum. At the cyclic W_2 to W_1 junction the same holds, giving
one further minimum at time zero. These account for every E in the
cyclic word and every possible E to O transition. Hence M=J_1+J_2+2.
The runs are maximal: each internal even run has length one, the
two tail runs have lengths a_1,a_2, and all of them have O on
either side. In particular the closing junction is included once,
not omitted or counted twice. The count does not depend on whether
x=n or whether any minimum value occurs repeatedly.

### Imported cutoff and repeated periods

Christian Hercher, [*There are no Collatz m-Cycles with m <= 91*](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf),
*Journal of Integer Sequences* 26 (2023), Article 23.3.5,
Definitions 1/5/6, printed pp. 2–4, and Theorem 23, pp. 15–16,
excludes nontrivial positive shortcut cycles with at most 91 local
minima. The map and strict odd/even run extrema agree with those
above. Import that theorem, including its published verification
height 695*2^60, continued-fraction bounds and odd-step bound;
no independent numerical certification or reproof is claimed.
The ready SPECIALIZE assessment is
`drafts/literature/2026-10-07-two-postspell-local-minima.md`.

The represented cycle is nontrivial: n is in neither {1,2}, and
the shortcut orbit of either member of {1,2} stays in that set.
An actual closed orbit containing n therefore cannot be the
trivial cycle, even represented repeatedly.

For clarity, the theorem can be applied to the primitive period,
so the restriction does not depend on a permissive interpretation
of represented cycles. Let p be the least positive return time of
n. It exists since N is a return time. Determinism gives
u_{t+p}=u_t for every t>=0. Divide N=rp+s, 0<=s<p. Then
u_N=u_s=n, and minimality of p forces s=0. Thus N=rp for an
integer r>=1. The input parities and the strict-minimum indicator
also repeat every p steps, including their cyclic closing boundary.
If m_0 counts minima in the primitive period, the N-period count
is exactly M=r m_0. The primitive cycle is still positive and
nontrivial. Hercher's theorem gives m_0>=92, hence M>=92 and
J_1+J_2>=90. No particular repeat factor, or distinctness of the
two named junctions, was assumed.

The occurrence convention also agrees with John Simons and Benne
de Weger, [*Theoretical and computational bounds for m-cycles of the 3n+1 problem*](https://deweger.net/papers/%5B35a%5DSidW-3n%2B1-v1.44%5B2010%5D.pdf),
v1.44, 31 August 2010, section 1.2, printed p. 2, which expressly
allows nonminimal return periods and treats repetitions of {1,2}
as trivial. The primitive-period argument above retains all such
representations without substituting that source's weaker cutoff.

This is REPRODUCTION: an elementary exact count specializes a known
cycle theorem to the local word syntax. It is a useful local necessary
restriction, not a new general cycle cutoff or progress beyond the
inspected published theorem. It supplies neither positive closure
nor an all-parameter exclusion.

### Separate critical audit

On 2026-10-07 a separate audit checked the complete proof against the
preapproved actual-closure scope and the cited primary definitions and
Theorem 23. It found no defect in the cyclic E-to-O count, positivity,
nontriviality, return-time divisibility or boundary-sensitive repetition
of the minimum indicator. The published numerical inputs remain imported,
without independent computational certification. No stronger restriction
or existence claim was established. The detailed review record is
`drafts/2026-10-07-two-postspell-minimum-cutoff-audit.md`.

## Mathlib

Full matching result (this count and cutoff specialization), Hercher's
91-minimum theorem, and supporting finite-period results: **not checked**.
No matching declaration or absence from Mathlib is asserted.
