# L011 — First-merge restrictions for non-descending histories

## Hypotheses

Let T(n)=n/2 for even positive n and T(n)=(3n+1)/2 for odd positive n.
Let R be the maximal odd-even block map of L002, and allow the four block
types in the alphabet {(1,1),(2,1),(3,1),(1,2)}.

Let K>=1. A depth-K history (n_0,...,n_K) is non-descending here if n_0>1 and
n_j>=n_0 for every j. This condition compares every state with the initial
state; it does not require n_j>=n_(j-1). All states are positive odd
integers and every successive pair is an exact allowed block.

## Conclusion

For K<=3, any two non-descending depth-K histories ending at the same
integer have identical suffixes (n_1,...,n_K).

For arbitrary K, suppose two such histories have different suffixes.
Let r be their first common index among 1,...,K, and put m=n_r for their
common value there. Then r>=4. Write

\[
2m+1=3^s w,\qquad 3\nmid w.
\]

Necessarily s is 2 or 3. After exchanging the two histories if needed,
their last block types before m are (s-1,1) and (s,1), respectively.
Put y equal to the latter history's state at index r-1. Then

\[
y=2^s w-1\equiv1\pmod3,
\]

and the former history has the following four consecutive states at
indices r-3,...,r:

\[
\left(\frac{32y+7}{3},\quad 4y+1,\quad
\frac{3y+1}{2},\quad m\right).
\tag{1}
\]

Their block types are ((1,2),(1,2),(s-1,1)). In particular, two
consecutive contracting blocks are forced on one side of the first
merge. These are necessary conditions for a failure of suffix rigidity,
not sufficient conditions for two non-descending histories to exist.

This does not prove suffix rigidity for arbitrary depth, bound how much
earlier growth can compensate the forced contractions, or establish
eventual descent from any fixed start. Other block types remain outside
the statement.

## Proof

By L002, the minimum in any complete block is attained at one of its
two endpoints: the odd portion increases and the even portion decreases.
Consequently the non-descent condition in the hypotheses also keeps all
intermediate shortcut states at least n_0. No possible descent inside
a block is omitted by the endpoint test.

Use the exact inverse branches from L010. An odd endpoint that is 0
modulo 3 has no allowed predecessor. An endpoint that is 2 modulo 3
has the unique predecessor

\[
H(m)=\frac{8m-1}{3},
\tag{2}
\]

of type (1,2). At an endpoint that is 1 modulo 3, put
2m+1=3^s w with s>=1 and 3 not dividing w. Its allowed predecessors
are exactly

\[
G_a(m)=2^a3^{s-a}w-1,
\qquad 1\le a\le\min(3,s),
\tag{3}
\]

of types (a,1). These predecessors decrease strictly as a increases,
because G_(a+1)(m)+1=(2/3)(G_a(m)+1).

First consider depth two. If two penultimate states differ, the endpoint
must be 1 modulo 3, by the other two endpoint cases. Any branch a<s in
(3) has predecessor x=G_a(m) congruent to 2 modulo 3. Its only preceding
state is H(x), and

\[
H(x)-x=\frac{5x-1}{3}>0.
\]

Thus the first block of such a depth-two history already descends below
its start. A non-descending depth-two history can use only the branch
a=s, if that branch exists. Its penultimate state is unique. Depth one
is immediate, since the suffix consists only of the common endpoint.

Now suppose two non-descending histories have different suffixes. Once
their states agree at any index, determinism of R makes all later states
agree. Hence their states at index 1 differ, and their first common
index r is at least 2. Truncating each history at r preserves its
non-descent condition. The depth-two result excludes r=2, so r>=3.

At m=n_r, the distinct penultimate states must again be branches of (3).
If a<=s-2, the penultimate state x=G_a(m) is 2 modulo 3, and its forced
preceding state is

\[
H(G_a(m))=2^{a+3}3^{s-a-1}w-3\equiv0\pmod3.
\tag{4}
\]

Equation (4) has no allowed predecessor. Since r>=3 requires a state at
index r-3, such a branch cannot occur. Thus every last branch that can
belong to either history has a>=s-1 as well as 1<=a<=min(3,s).
Two distinct such branches exist only if s is 2 or 3, and they must
be a=s-1 and a=s.

The a=s branch has penultimate state y=2^s w-1. The other branch has
penultimate state

\[
x=3\,2^{s-1}w-1=\frac{3y+1}{2}.
\]

It is 2 modulo 3. Therefore the same history's state at index r-2 is
forced by (2) to be

\[
z=H(x)=4y+1.
\tag{5}
\]

Both y and z have earlier allowed predecessors: y is at index r-1>=2
and z is at index r-2>=1. L010's endpoint-union criterion gives
3 not dividing either y or z. Since z=4y+1, residue y=2 modulo 3
would make z divisible by 3; hence y=1 modulo 3 and z=2 modulo 3.
The state at index r-3 is consequently the unique predecessor H(z),
which is (32y+7)/3. This establishes (1) and its exact block types
using the necessary and sufficient inverse conditions in L010.

If r=3, the first two states of this history would be H(z) and z.
The inequality H(z)>z just proved for every positive z contradicts
non-descent from its start. Thus r>=4. In particular no different
suffixes can occur for K<=3, as claimed.

The argument stops at the forced contractions. When r>3 there can be
earlier blocks that increase the orbit enough for these two contractions
to remain above its initial state. Proving that simultaneous realization
with the companion history is impossible would require a new argument;
it is not a consequence of (1).

Verification detail: `python3 scripts/nondescending-suffix/check_histories.py`
independently iterates the shortcut map to check both forced-tail families
and the histories (973,365,137,103) and (71,121,91,103). The second
history is non-descending; the first is excluded by its initial
contraction, illustrating the depth-three obstruction. The same script
screens every four-type word through depth six by exact endpoint
congruences and non-descent inequalities. It reports no distinct-suffix
pair. That finite screen supplements this proof and is not an
all-depth theorem. Its output is saved in
`scripts/nondescending-suffix/result.json`.

## Mathlib

Full statement: **not checked**. Supporting valuation, congruence, and
iteration results: **not checked**; no theorem names or direct library
links were verified. The proof uses L002, L010, and elementary arithmetic.
No claim of novelty or absence from Mathlib is made.
