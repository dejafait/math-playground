# L008 — Exact endpoint density and its finite-interval boundary term

## Hypotheses

Use the positive-integer shortcut map T and complete-block map R of L007.
Only block types (2,1) and (3,1) are allowed. For an integer K>=1, let
E_K be the set of positive odd endpoints admitting an allowed history of
depth K, with no upper bound on the starting integer. For real X>=0 put

\[
A_K(X)=\#\{m\in E_K:m\le X\}.
\]

A pair (s,r), with 0<=r<3^s, denotes the positive odd integers congruent
to r modulo 3^s. The parity restriction is part of this notation.

## Conclusion

The set E_K is the disjoint union of 2^(K-1) such classes. An exact
recursive description is

\[
\mathcal C_1=\{(2,4)\},\qquad
\mathcal C_{K+1}=
\left\{\left(s+a,\left[2^{-(a+1)}
 (3^a r+3^a-2^a)\right]_{3^{s+a}}\right):
 (s,r)\in\mathcal C_K,\ a\in\{2,3\}\right\}.
\tag{1}
\]

Brackets mean the least nonnegative residue; the negative power denotes
a modular inverse, which exists. Every class in (1) includes all of its
positive odd members, without an additional lower cutoff. Its exponent
s lies between 2K and 3K-1. The natural density among all positive integers
is exactly

\[
\delta_K=\frac1{18}\left(\frac4{27}\right)^{K-1}.
\tag{2}
\]

For each (s,r) in C_K, let e_(s,r) be its least positive odd representative
and q_(s,r)=2*3^s. Then, for all real X>=0,

\[
A_K(X)=\sum_{(s,r)\in\mathcal C_K}
 \left(1+\left\lfloor\frac{X-e_{(s,r)}}{q_{(s,r)}}\right\rfloor\right),
\qquad
|A_K(X)-\delta_KX|<2^{K-1}.
\tag{3}
\]

In a complete common period of length 2*3^(3K-1), there are exactly
4^(K-1) endpoint residues.

For an integer N>=1, every allowed depth-K history starting at most N
has its endpoint below

\[
X_K(N)=\left(\frac{27}{16}\right)^K(N+5).
\]

At this cutoff (3) gives

\[
A_K(X_K(N))<\frac{3(N+5)}{8\,4^K}+2^{K-1}.
\tag{4}
\]

The density contribution tends to zero at fixed N, but this upper bound
does not become less than one. The boundary term cannot simply be
discarded: at K=4 and N=175,

\[
1453\in E_4,\qquad 1453<X_4(175)=\frac{23914845}{16384},
\qquad \delta_4X_4(175)=\frac{135}{512}<1.
\tag{5}
\]

Thus the boundary error here is at least 377/512. In particular the
density-only upper estimate A_K(X_K(N))<=delta_K X_K(N) is false.
These conclusions do not decide whether the true count eventually
vanishes for each fixed N, or whether all infinite allowed itineraries
are excluded. They also do not prove universal eventual descent.

## Proof

L007 says that a positive odd m has an allowed predecessor exactly when
m=4 modulo 9, proving C_1. Its two inverse branches can equivalently be
written as the forward expressions

\[
F_2(n)=\frac{9n+5}{8},\qquad
F_3(n)=\frac{27n+19}{16}.
\tag{6}
\]

They are complete blocks only on their exact domains. We retain those
domains by using both directions of the predecessor criterion in L007.

Suppose that (s,r) describes one class of E_K and fix a in {2,3}.
An endpoint m of an appended type-(a,1) block whose predecessor is in
this class must satisfy

\[
2^{a+1}m-(3^a-2^a)\equiv 3^a r\pmod{3^{s+a}}.
\tag{7}
\]

Conversely, let m be any positive odd integer satisfying (7). Reduction
modulo 3^a gives the integrality condition for G_a(m) in L007: m=4
modulo 9 when a=2, or m=13 modulo 27 when a=3. The sufficiency part
of that lemma ensures a positive odd predecessor n=G_a(m) with the
exact allowed run lengths. Dividing (7) by 3^a gives n=r modulo 3^s.
The inductive description of E_K puts n in E_K, so appending its block
puts m in E_(K+1). This proves exact coverage, including positivity and
the absence of missing initial terms. Solving (7) for m gives (1).

For a fixed a, distinct old classes give disjoint new classes because
G_a(m) is single valued and the old classes are disjoint. If a positive
odd m were in a new class for a=2 and also one for a=3, both of its
predecessors would belong to E_K. Since K>=1, each predecessor would
itself have an allowed predecessor. L007 excludes two extendible
branches at one endpoint. Thus the classes for different appended types
are also disjoint. Every class is nonempty (it has infinitely many
positive odd members), so their number doubles at each extension.
Starting from one class proves the number 2^(K-1). The initial exponent
is 2; every extension adds either 2 or 3, giving 2K<=s<=3K-1.

A class with exponent s, restricted to odd integers, has period 2*3^s
and exactly one residue in that period. Its density among all integers
is 1/(2*3^s). Disjointness therefore gives the density as the sum of
these quantities. Each extension replaces one contribution by 1/9
and 1/27 times that contribution. The initial density is 1/18, so
induction proves (2). All periods divide 2*3^(3K-1). Multiplying that
common period by (2) gives exactly 4^(K-1), proving the complete-period
count without any probabilistic independence assumption.

More explicitly, e_(s,r)=r if r is odd, and r+3^s if r is even.
This formula also handles r=0; always 0<e_(s,r)<q_(s,r). The positive
members of the class are precisely e_(s,r)+q_(s,r)t for integers t>=0.
Consequently its count up to X is the summand in (3). This formula is
zero when X<e_(s,r), because X>=0 and e_(s,r)<q_(s,r).
The difference between the summand and X/q_(s,r) is

\[
1-\frac{e_{(s,r)}}{q_{(s,r)}}-
 \left\{\frac{X-e_{(s,r)}}{q_{(s,r)}}\right\},
\]

where braces denote fractional part. It lies strictly between -1 and 1.
Summing over the 2^(K-1) classes proves (3). In particular, the density
limit at fixed K has not been interchanged with a limit in K; (3)
retains an explicit error that depends on K.

For the endpoint cutoff, the two exact shifted identities from (6) are

\[
F_2(n)+5=\frac98(n+5),\qquad
F_3(n)+5=\frac{27}{16}(n+5)-\frac94.
\]

Both are strictly less than (27/16)(n+5) for positive n. Iteration along
an allowed history with start n_0<=N therefore gives
m+5<(27/16)^K(n_0+5)<=X_K(N), in particular m<X_K(N).
Also

\[
\delta_KX_K(N)
=\frac{N+5}{18}\left(\frac4{27}\right)^{K-1}
 \left(\frac{27}{16}\right)^K
=\frac{3(N+5)}{8\,4^K}.
\]

Combining this identity with (3) proves (4). An upper bound below one
would force the nonnegative integer A_K(X_K(N)) to be zero, excluding
every such start. The displayed bound exceeds one for all K>=1; its
density contribution alone is insufficient.

For the explicit boundary witness, the exact block domains in L007 are
n=11 modulo 16 for type (2,1), and n=7 modulo 32 for type (3,1).
The successive starts 603,679,1147,1291 have the prescribed residues
for the word (2,3,2,2). Substitution in (6) gives the successive endpoints

\[
603,\quad679,\quad1147,\quad1291,\quad1453.
\]

Thus 1453 belongs to E_4. Direct integer comparison gives
1453*16384=23805952<23914845, proving the strict cutoff inequality in
(5). The displayed value of delta_4 X_4(175) follows from (4)'s density
identity. Hence A_4(X_4(175))>=1 and its error over the density term is
at least 1-135/512=377/512. Notice that this path starts at 603>175:
counting all histories at a possible endpoint cutoff also includes paths
that do not start below N. This is a sufficient overcount, not an equality
with the number of permitted starts below N.

The restricted target still requires a least-start bound tending to
infinity uniformly over all length-K words. Eventual vanishing of this
endpoint count would be a sufficient stronger estimate; it is not obtained
here. Nor does failure of the upper bound in (4) to shrink show that the
true count fails to vanish. The result rules out dropping the boundary
term, leaving its residue-offset control unresolved.

Verification detail: `python3 scripts/endpoint-count/check_count.py`
compares the recursive classes with direct forward maximal-block iteration
over complete common periods for K=1,...,4, tests finite-interval errors,
and checks the first two representatives of every class through K=10 by
backward reconstruction followed by direct forward iteration. It evaluates
(5) using exact rational arithmetic. The output is stored in
`scripts/endpoint-count/result.json`. These checks supplement the proof;
they establish no infinite-depth exclusion.

## Mathlib

Full statement: **not checked**. Supporting congruence, finite-union count,
floor-function, and iteration results: **not checked**; no theorem names
or direct library links were verified. L007 and the elementary argument
above supply the mathematical proof. No claim of literature novelty or
absence from Mathlib is made.
