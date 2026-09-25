# L010 — Variable even-run lengths destroy unique inverse extension

## Hypotheses

Let T(n)=n/2 for even positive n and T(n)=(3n+1)/2 for odd positive n.
For positive odd n, let R(n) be the endpoint of its maximal odd shortcut
run followed by its maximal even run, as in L002. Allow the four block
types

\[
\mathcal A=\{(1,1),(2,1),(3,1),(1,2)\}.
\]

An allowed predecessor of a positive odd m is a positive odd n whose
block type lies in this alphabet and whose endpoint is m. It is
extendible if n itself has an allowed predecessor. A depth-K history
ending at m is a tuple (n_0,...,n_K) of positive odd integers with n_K=m
and an allowed block between each successive pair.

## Conclusion

The inverse branches have the following exact conditions, all restricted
to positive odd endpoints m:

\[
\begin{array}{c|c|c|c}
(a,b)&G_{a,b}(m)&\text{exists}&\text{exists and is extendible}\\ \hline
(1,1)&(4m-1)/3&m\equiv1\pmod3&m\equiv1,4\pmod9\\
(2,1)&(8m-5)/9&m\equiv4\pmod9&m\equiv13,22\pmod{27}\\
(3,1)&(16m-19)/27&m\equiv13\pmod{27}&m\equiv13,40\pmod{81}\\
(1,2)&(8m-1)/3&m\equiv2\pmod3&m\equiv2,5\pmod9
\end{array}
\tag{1}
\]

Thus m has an allowed predecessor exactly when 3 does not divide m.
Among the first three rows the extendibility sets are nested, with the
third contained in the second and the second in the first. All three
branches extend exactly when m=13 or 40 modulo 81. In particular, for
each integer t>=0, the endpoint m=162t+13 has these three histories:

\[
\begin{aligned}
&(576t+45,\;216t+17,\;162t+13),\\
&(384t+29,\;144t+11,\;162t+13),\\
&(128t+9,\;96t+7,\;162t+13).
\end{aligned}
\tag{2}
\]

Their block types are respectively ((1,2),(1,1)), ((1,2),(2,1)), and
((1,1),(3,1)). Their penultimate states are distinct. Hence the unique
extendible branch and common-suffix conclusions from the smaller
alphabet in L009 do not extend to this alphabet.

There are at most three depth-one histories and at most five depth-two
histories at every endpoint. The latter bound is sharp: the five
depth-two histories ending at 661 are exactly

\[
(2349,881,661),\quad(1565,587,661),\quad
(521,391,661),\quad(347,391,661),\quad(231,391,661).
\tag{3}
\]

Thus even the old numerical bound of three histories at every depth
fails. This is not a claim that history counts are unbounded as depth
increases. The only allowed predecessor of 1 is still 1; every history
ending there is constant. Forward escape from this alphabet for starts
greater than 1, and universal eventual descent, remain unproved.

## Proof

Solving the endpoint formula of L002 for the starting value gives, for
arbitrary positive a,b,

\[
G_{a,b}(m)=\frac{2^a(2^b m+1)}{3^a}-1.
\tag{4}
\]

If an allowed block exists, its inverse must be (4), and coprimality
of 2 and 3 makes integrality equivalent to 3^a dividing 2^b m+1.
Conversely, under that divisibility put u=(2^b m+1)/3^a. Since m is
positive odd and a,b>=1, u is a positive odd integer. Then
n=2^a u-1 is positive odd with v_2(n+1)=a exactly, and

\[
3^a u-1=2^b m
\]

has 2-adic valuation exactly b. L002 therefore gives the exact maximal
run lengths (a,b) and endpoint m. This proves sufficiency, positivity,
and uniqueness for a fixed type, not merely a formal integer inverse.

Substitution in (4) gives all four formulas and existence classes in
(1). The three even-run-1 existence classes lie inside m=1 modulo 3,
and the first covers that whole class. The new branch covers m=2
modulo 3. Their union is exactly 3 not dividing m. Branches with b=1
are distinct when they coexist, since
G_{a+1,1}(m)+1=(2/3)(G_{a,1}(m)+1). The b=2 branch has no endpoint
in common with them. In particular there are at most three immediate
predecessors, even though the alphabet has four types.

For each existing predecessor n, the union criterion just proved
says that it is extendible exactly when 3 does not divide n.
For a numerator divided by 3^a, divisibility of n by 3 is equivalent
to divisibility of that numerator by 3^(a+1). In the first row of (1),
the existence class has the three lifts m=1,4,7 modulo 9. The
numerators 4m-1 are respectively 3,6,0 modulo 9; discard only 7.
In the second row the lifts are m=4,13,22 modulo 27 and 8m-5 is
respectively 0,18,9 modulo 27; discard only 4. In the third row the
lifts are m=13,40,67 modulo 81 and 16m-19 is respectively 27,54,0
modulo 81; discard only 67. For the new fourth row the lifts are
m=2,5,8 modulo 9 and 8m-1 is respectively 6,3,0 modulo 9; discard
only 8. This proves both directions of every extendibility condition.
Although these are congruences modulo odd numbers, the hypothesis
that m is positive odd has been retained throughout.

Both residues 13 and 22 modulo 27 are 4 modulo 9. Both residues 13
and 40 modulo 81 are 13 modulo 27. Hence the three b=1 extendibility
sets are nested as claimed, and all three branches extend on exactly
the third set. The new b=2 extendibility set is disjoint from all of
them because its endpoints are 2 modulo 3. At m=162t+13, (4) gives
the penultimate states 216t+17, 144t+11, and 96t+7. The first two
are 2 modulo 3 and have the (1,2) predecessors 576t+45 and 384t+29.
The third is 1 modulo 3 and has the (1,1) predecessor 128t+9.
The proved sufficiency of (4) verifies every block in (2), including
exact maximal runs. All states are positive odd and the penultimate
states are distinct for t>=0.

To bound depth-two histories, first take m=2 modulo 3. It has only
one immediate predecessor, and that predecessor has at most three
predecessors. There are therefore at most three depth-two histories.
If m=0 modulo 3 there are none. In the remaining case m=1 modulo 3,
write 2m+1=3^s w with s>=1 and 3 not dividing w. The existing branches
are exactly a=1,...,min(s,3), with b=1. For a<s their predecessors
satisfy

\[
G_{a,1}(m)+1=2^a3^{s-a}w,
\]

so G_{a,1}(m)=2 modulo 3. Each such predecessor consequently has
exactly one predecessor, of type (1,2). If s<=3 there is at most one
remaining branch, a=s, whose predecessor has at most three
predecessors. The total is at most (s-1)+3<=5. If s>3, all three
branches have a<s, and the total is exactly three. These cases prove
the upper bound five without a truncation in endpoint size.

At m=661, formula (4) gives precisely the three immediate predecessors
881,587,391, with types (1,1),(2,1),(3,1). The first two are 2
modulo 3, so their unique predecessors are 2349 and 1565, using (1,2).
Since 391=13 modulo 27, it has all three b=1 predecessors, namely
521,347,231, and no b=2 predecessor. This proves (3) and its
exhaustiveness. Each run is exact by the sufficiency argument above.

At m=1 only the first existence class applies and G_{1,1}(1)=1.
Induction on history depth proves that every history ending at 1 is
constant. The finite histories in (2) and (3) are incoming branches,
not nontrivial forward cycles. In particular they are not counterexamples
to Collatz. They refute the proposed extension of the decoder, while
leaving a bound excluding infinite allowed trajectories above 1 entirely
open. Even a replacement finite multiplicity bound would still require
a link to forward starting height or eventual descent; neither the
old bound three nor the present bound five supplies it.

Verification detail: `python3 scripts/variable-even-inverse/check_branches.py`
checks the inverse and extendibility classes against independent forward
maximal-block iteration. It covers all odd endpoints in a full period
modulo 1458 for depth-two existence, includes every possible first and
second predecessor in its forward search, checks the sharp bound and
fixed point, and verifies lifts of (2). The saved output is
`scripts/variable-even-inverse/result.json`. These are finite arithmetic
checks supporting the proof, not evidence of convergence or infinite
branching.

## Mathlib

Full statement: **not checked**. Supporting valuation, congruence, and
iteration results: **not checked**; no theorem names or direct library
links were verified. L002 and the elementary argument above give the
proof. No claim of literature novelty or absence from Mathlib is made.
