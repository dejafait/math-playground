# L012 — Exact paired backward transitions with separate starting thresholds

## Hypotheses

Use the maximal-block map R and alphabet
{(1,1),(2,1),(3,1),(1,2)} of L010. Suppose two non-descending histories
as in L011 first meet at index r with different suffixes. Keep their
starting values separate. In L011's notation, r>=4, s is 2 or 3,
y=B_(r-1), and the other history contains

\[
(A_{r-3},A_{r-2},A_{r-1},A_r)
=\left(\frac{32y+7}{3},4y+1,\frac{3y+1}{2},m\right),
\qquad B_r=m.
\]

Here y=1 modulo 3 and the final types are (s-1,1) and (s,1).

## Conclusion

Necessarily

\[
v_3(2y+1)=1,\qquad y\equiv1\pmod9,
\qquad v:=B_{r-2}=\frac{4y-1}{3}\equiv1\pmod3,
\qquad A_{r-3}=8v+5.
\tag{1}
\]

Thus B_(r-2) to B_(r-1) is the contracting block (1,1), and the
paired states (8v+5,v) still have indices one apart.

For any positive odd v=1 modulo 3, all simultaneous predecessors
P=G_(a,1)(8v+5), q=G_(b,1)(v) are given by this table. The letters
a,b in the table are the two odd-run lengths; both even-run lengths
are 1.

| (a,b) | Necessary and sufficient condition on v | P in terms of q |
| --- | --- | --- |
| (1,1) | v=1 modulo 3 | 8q+9 |
| (2,1) | v=1 modulo 9 | (16q+17)/3 |
| (3,1) | v=1 modulo 27 | (32q+31)/9 |
| (1,2) | v=4 modulo 9 | 12q+13 |
| (1,3) | v=13 modulo 27 | 18q+19 |

All entries give positive odd predecessors with exact maximal runs.
If these are the states A_(r-4), B_(r-3) in the original histories,
q must have an allowed predecessor, so 3 does not divide q. When
r>=5, P must also have a predecessor, so 3 does not divide P.
Further extension is governed by the same exact inverse conditions.

More generally, there is an exact affine transition and inequality test
for any fixed pair of earlier words, described in the proof below.
The one-block offset requires an additional inverse on the B side
before comparing either history with its own start. These rules do
**not** prove that every pair eventually fails an inequality. They
establish neither all-depth suffix rigidity nor universal descent.

## Proof

### The additional forced contraction

L011 supplies the displayed tail and r>=4. By L010, an odd integer
has an allowed predecessor exactly when it is not divisible by 3.
The state A_(r-3) has a preceding state, since r-3>=1. But

\[
\frac{32y+7}{3}=\frac{16(2y+1)}3-3
\]

would be divisible by 3 if 9 divided 2y+1. Since y=1 modulo 3,
we obtain v_3(2y+1)=1. L010 then leaves only the odd-run-1 inverse
of y, namely v=(4y-1)/3. Substitution gives A_(r-3)=8v+5.

The condition on 2y+1 leaves y=1 or 7 modulo 9. In the latter
case v=0 modulo 3, impossible because B_(r-2) has a predecessor.
Thus y=1 modulo 9 and v=1 modulo 3. Both v and 8v+5 are therefore
1 modulo 3. The forward block v to y has type (1,1) by the exact
inverse criterion, and y=(3v+1)/4<v because v>1. The hypothesis
y>=B_0>1 ensures v>1. This contraction does not compare y with B_0.

### The five simultaneous inverse choices

At endpoints 8v+5 and v, only even-run-1 inverses are available.
Their existence conditions from L010 are

\[
3^a\mid16v+11,\qquad 3^b\mid2v+1,
\qquad a,b\in\{1,2,3\}.
\tag{2}
\]

Since 16v+11=8(2v+1)+3, both numbers cannot be divisible by 9.
Consequently min(a,b)=1. With v=1 modulo 3 understood, the other
divisibilities give precisely the five rows in the table: respectively
v=1 modulo 9 or 27 for a=2 or 3, and v=4 modulo 9 or 13 modulo 27
for b=2 or 3. These conditions may overlap with the (1,1) row;
the table lists branches, not disjoint endpoint classes.

Put q=2^b(2v+1)/3^b-1 and substitute
2v+1=3^b(q+1)/2^b in
P=2^a(16v+11)/3^a-1. This gives the five displayed expressions.
L010 proves that the divisibilities suffice for positive odd inverse
states and exact maximal runs. Applying its endpoint-union criterion
once more proves the asserted extra conditions on P and q. The table
describes arithmetic admissibility; non-descent is imposed separately
below.

### The exact transition rule at later pairs

Represent every state in each already constructed suffix by an affine
function p*t+c, where t ranges over nonnegative integers, p is
positive and even, and c is positive and odd. The two initial families
can be taken as

\[
\begin{array}{c|c|c}
s&y&m\\\hline
2&48t+43&54t+49\\
3&96t+7&162t+13.
\end{array}
\tag{3}
\]

Indeed L011 writes y=2^s w-1 with w odd, 3 not dividing w, and
m=(3^s w-1)/2 odd. Together with y=1 modulo 3 these give
w=11 modulo 12 for s=2 and w=1 modulo 12 for s=3. Taking their
least positive representatives proves (3), including exhaustiveness.
The initial suffixes are (4y+1,(3y+1)/2,m) and (y,m); they have
lengths two and one.

For a candidate inverse of type (a,b), put f=2^(a+b), d=3^a,
e=3^a-2^a. L010 gives the inverse (f*n-e)/d. At n=p*t+c,
its integrality condition is the single linear congruence

\[
fp\,t\equiv e-fc\pmod d.
\tag{4}
\]

Let g=gcd(fp,d). There is no solution if g does not divide e-fc.
Otherwise division by g gives one residue class t=rho modulo d/g.
Both coordinates' moduli are powers of 3; hence their classes are
compatible exactly when the two residues agree modulo the smaller
modulus. When compatible, let rho be the least nonnegative residue
for the larger modulus M and substitute t=rho+M*u in every state
of both suffixes. The chosen inverse coordinates then become affine
integer functions of u>=0. L010 ensures positivity, oddness, and the
exact block types; all other suffix states remain valid by substitution.
This proves necessity, sufficiency, and exhaustiveness of each step.

Each simultaneous step adds one block to both suffixes, preserving
their one-block length difference. If the A suffix now has length K,
the B suffix has length K-1. To test a pair of original depth-K
histories, apply one further admissible inverse only on B and restrict
the parameter class again. The resulting A_0 and B_0 are independent
starting thresholds, not the current paired endpoints or their minimum.

For each history with state functions p_j*t+c_j, its complete
non-descent conditions are exactly

\[
p_0t+c_0\ge3,\qquad
(p_j-p_0)t+(c_j-c_0)\ge0\quad\text{for every }j.
\tag{5}
\]

Intersect the conditions for both histories with integer t>=0.
A positive coefficient gives a lower bound, a negative coefficient
an upper bound, and a zero coefficient a constant check. Thus (5)
is an exact integer interval test, retaining both separate starts
and all earlier states. It is a decision procedure for each finite
word pair, not a bound on the necessary word lengths.

### Scope and verification

This specializes the standard finite-word inverse arithmetic already
proved in L010. Its literature basis is recorded in the prior assessment:
Rozier, *Parity Sequences of the 3x+1 Map on the 2-adic Integers and
Euclidean Embedding*, INTEGERS 19 (2019), A8,
[Lemma 1 and Theorem 1, pp. 2–4](https://math.colgate.edu/~integers/t8/t8.pdf#page=2).
Those are supporting parity-word results, not a match for a two-start
descent theorem. The present step is a reproduction/specialization of
that machinery; no literature novelty is claimed.

`python3 scripts/paired-state/check_pairs.py` checks the five-row table
by direct shortcut iteration and applies (3)–(5) to all coupled classes
through depth 11. Every equal-depth class through depth eight is also
checked at parameters 0 and 17 by independent shortcut iteration.
The saved `scripts/paired-state/result.json` contains no surviving
non-descending pair in these finite depths. The number of coupled
classes grows, and no invariant or shorter-history reduction has
been proved. An empty finite search is not an all-depth implication.

## Mathlib

Full paired-state statement: **not checked**. Supporting congruence,
valuation, affine iteration, and interval results: **not checked**.
No Mathlib theorem name or direct library link was verified; no absence
from Mathlib is asserted. The source link above supports the standard
arithmetic, not library coverage or the unresolved descent assertion.
