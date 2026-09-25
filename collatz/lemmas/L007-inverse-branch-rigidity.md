# L007 — At most one extendible inverse branch

## Hypotheses

Let T(n)=n/2 for even positive n and T(n)=(3n+1)/2 for odd positive n.
For positive odd n, let R(n) be the endpoint of its maximal initial odd
shortcut run followed by its maximal even run, as in L002. Only complete
blocks with lengths (2,1) or (3,1) are allowed in this statement.

An allowed predecessor of a positive odd integer m is a positive odd n
whose allowed block ends at m. A predecessor is extendible if it itself
has an allowed predecessor. An allowed history of depth K>=1 ending at m
is a tuple (n_0,...,n_K) of positive odd integers with n_K=m and an
allowed block from n_(i-1) to n_i for each i=1,...,K.

Write

\[
G_2(m)=\frac{8m-5}{9},\qquad G_3(m)=\frac{16m-19}{27}.
\]

These are only formal rational expressions until the conditions below
hold; integrality and the exact block lengths must both be checked.

## Conclusion

For every positive odd m, its allowed predecessors are exactly

\[
\begin{array}{c|c|c}
\text{block type}&\text{predecessor}&\text{condition}\\ \hline
(2,1)&G_2(m)&m\equiv4\pmod9\\
(3,1)&G_3(m)&m\equiv13\pmod{27}.
\end{array}
\tag{1}
\]

Thus m has at least one allowed predecessor exactly when m=4 modulo 9.
The conditions for an extendible predecessor are exactly

\[
\begin{array}{c|c}
\text{predecessor}&\text{condition for existence and extendibility}\\ \hline
G_2(m)&m\equiv76\pmod{81}\\
G_3(m)&m\equiv175\pmod{243}.
\end{array}
\tag{2}
\]

These two classes are disjoint: their residues modulo 27 are 22 and 13.
In particular, at most one allowed predecessor of m is extendible.
If both immediate predecessors exist, G_2(m) is never extendible.

For every K>=1 and positive odd m, there are at most two allowed histories
of depth K ending at m. If there are two, their states n_1,...,n_K agree;
only n_0 differs, with the first block of type (2,1) in one history and
(3,1) in the other. In any history of depth at least two, the final block
is forced to be (2,1) when m=76 modulo 81, and (3,1) when m=175 modulo
243. Repeating this rule decodes every block except possibly the earliest
one. Failure of both conditions in (2) means that no history of depth two
exists at that endpoint.

Each such history satisfies the elementary backward size bound

\[
n_0<\left(\frac89\right)^K m.
\tag{3}
\]

Consequently every fixed positive endpoint has bounded backward depth.
Neither (2), the multiplicity bound, nor (3) gives a lower bound on the
starting integer tending to infinity with K when the endpoint is allowed
to vary. Infinite aperiodic forward itineraries remain unexcluded.

## Proof

L002 gives R(n)=(3^a n+3^a-2^a)/2^(a+1) on a block of type (a,1).
For a=2 write n=4u-1 with u positive odd. Exact even-run length 1 means
9u-1=2 modulo 4, equivalently u=3 modulo 4. Thus the exact domain is
n=11 modulo 16, and the endpoint is (9n+5)/8. For a=3 the same argument
with n=8u-1 gives 27u-1=2 modulo 4, equivalently u=1 modulo 4. The
exact domain is n=7 modulo 32, and the endpoint is (27n+19)/16.
Both conditions retain maximality of the odd and even runs.

Solving these two affine equations for n gives G_2 and G_3. Integrality
of G_2 requires 8m=5 modulo 9, equivalently m=4 modulo 9; integrality
of G_3 requires 16m=19 modulo 27, equivalently m=13 modulo 27.
For sufficiency, positive odd m in the first class has the unique form
m=18t+13 with integer t>=0. Then G_2(m)=16t+11 is positive odd and
in the exact (2,1) domain. Positive odd m in the second class has the
form m=54t+13 with integer t>=0, giving G_3(m)=32t+7 in the exact
(3,1) domain. Their endpoints are m by substitution. This proves (1)
with no omitted small positive exceptions.

The second congruence class in (1) is contained in the first, so the
union of possible endpoints is precisely the positive odd integers
congruent to 4 modulo 9. In particular, all such endpoints are 1
modulo 3. When both predecessors exist, write m=54t+13. Then

\[
G_2(m)=48t+11\equiv2\pmod3,\qquad G_3(m)=32t+7.
\tag{4}
\]

The first cannot itself be an allowed endpoint, proving the asserted
terminal branch. This also shows directly that the two predecessors
are distinct; their difference is 16t+4>0.

More precisely, once G_2(m) exists, (1) says that it has a predecessor
if and only if G_2(m)=4 modulo 9. Clearing the denominator gives

\[
8m-5\equiv36\pmod{81}
\quad\Longleftrightarrow\quad
8m\equiv41\pmod{81}
\quad\Longleftrightarrow\quad
m\equiv76\pmod{81}.
\]

The final congruence already implies m=4 modulo 9, so it also implies
existence of G_2(m). By (1), its positive odd value then has a positive
odd predecessor, establishing both directions of the first line of (2).
Similarly,

\[
G_3(m)\equiv4\pmod9
\quad\Longleftrightarrow\quad
16m-19\equiv108\pmod{243}
\quad\Longleftrightarrow\quad
m\equiv175\pmod{243}.
\]

Here the last congruence implies m=13 modulo 27, ensuring that G_3(m)
exists. It proves the second line. The inverses used in these congruences
exist since 8 and 16 are coprime to the respective powers of 3; one may
check 8*76=41 modulo 81 and 16*175=127 modulo 243 directly.
The two classes reduce to distinct residues modulo 27, proving disjointness
and the forced final-block rule.

We prove the history multiplicity statement by induction on K. For K=1,
(1) gives at most two histories, with the common last state m. If there
are two, their block types are the two different types in (1).
For K>=2, any depth-K history passes through an extendible predecessor
p=n_(K-1) of m: its own predecessor is n_(K-2). Equation (2) forces
this p to be unique whenever it exists. Every depth-K history is
therefore obtained by appending m to a depth-(K-1) history ending at
this same p. By induction there are at most two. If there are two, the
induction hypothesis says they differ only in their earliest state and
first block type. Appending the common m preserves exactly that assertion.
This also justifies recursive decoding, without assuming any independence
of successive congruences.

For example, the two immediate histories at m=13 start at 11 and 7.
At depth two, both (251,283,319) and (167,283,319) are legal: their
initial block types are different, and their common last block is (2,1).
Thus the multiplicity bound does not assert full injectivity at the
earliest state. At m=175 both immediate predecessors 155 and 103 exist,
but only 103 has an earlier predecessor, namely 91.

Finally, when defined on positive odd integers, both inverse maps are
strictly less than (8/9)m: for G_2 this follows from its subtraction of
5/9, and for G_3 from 16/27<8/9 and subtraction of 19/27. Applying
this along K inverse steps proves (3). Since n_0>=1, it implies
m>(9/8)^K, bounding K for each fixed m. This is a bound in terms of
the last endpoint, not the starting integer. An infinite forward path
would have increasingly large endpoints, each with its own finite and
nearly unique past, so there is no contradiction.

The missing quantitative threshold is still a bound mu_K tending to
infinity, where mu_K is the least positive start realizing any K allowed
blocks, as in the comparison in L005. Equation (3) instead bounds n_0
from above in terms of an unrestricted m. The exact branching result
supplies no such uniform lower estimate. It constrains collisions between
finite histories but neither excludes all infinite allowed itineraries
nor proves eventual descent for Collatz.

Verification detail: `python3 scripts/inverse-branches/check_branches.py`
compares (1) and (2) against direct maximal-block iteration over a complete
odd residue period modulo 486. It also constructs mixed words through
length eight and checks their full backward histories and the multiplicity
and size bounds using exact integer arithmetic. The output is saved in
`scripts/inverse-branches/result.json`. These finite checks supplement
the proof and are not evidence of convergence.

## Mathlib

Full statement: **not checked**. Supporting modular-arithmetic and
iteration results: **not checked**; no theorem names or direct library
links were verified. The proof uses L002, elementary congruences, and
finite induction. No claim of literature novelty or absence from Mathlib
is made.
