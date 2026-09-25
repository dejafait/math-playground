# L003 — Exact residue classes for consecutive growing blocks

## Hypotheses

Let T on positive integers be n/2 for even n and (3n+1)/2 for odd n.
For a positive odd n, let R(n) be the endpoint of its maximal odd shortcut
run followed by its maximal even run, as in L002. Denote the two run lengths
by (a,b). Let K be a positive integer.

## Conclusion

The first K complete blocks from a positive odd n all have (a,b)=(2,1)
if and only if

\[
n\equiv-5\pmod{2^{3K+1}}.
\tag{1}
\]

When (1) holds, write n=2^(3K+1)t-5, where t is necessarily a positive
integer. The successive endpoints are

\[
R^j(n)=T^{3j}(n)=9^j2^{3(K-j)+1}t-5
             =\left(\frac98\right)^j(n+5)-5
\quad(0\le j\le K).
\tag{2}
\]

For these starts, every positive-time shortcut state through time 3K is
strictly greater than n. The least positive start with this prefix is
2^(3K+1)-5, and the exact
number of initial consecutive (2,1) blocks for any positive odd n is

\[
\left\lfloor\frac{v_2(n+5)-1}{3}\right\rfloor.
\tag{3}
\]

Consequently no fixed number of complete blocks forces descent below the
start for all sufficiently large odd starts. Even a finite residue correction
cannot force descent at the block endpoints within a fixed number of blocks:
for all positive integers q,K,N and every real-valued function h on residues
modulo q, there are infinitely many odd n>N such that, for
V(n)=log(n)+h(n mod q),

\[
V(R^j(n))-V(n)>j\log(9/8)>0\quad(1\le j\le K).
\tag{4}
\]

The potential claim (4) concerns block endpoints. The uncorrected size claim
also covers all intermediate shortcut states. None of these statements
provides an infinite growing positive orbit or excludes unbounded return
times depending on the start.

## Proof

L002 gives the exact domain and endpoint for a (2,1) block. To specialize it
explicitly, write n=4u-1 with u odd. Exact even-run length 1 means
9u-1=2 modulo 4, equivalently u=3 modulo 4. Thus the domain is exactly
n=11 modulo 16. On that domain,

\[
R(n)=\frac{9n+5}{8},\qquad
R(n)+5=\frac98(n+5),\qquad
R(n)-n=\frac{n+5}{8}>0.
\tag{5}
\]

Equivalently, a (2,1) block occurs exactly when v_2(n+5)>=4. The second
identity in (5) shows that this block decreases v_2(n+5) by exactly 3.
All valuations here are of positive integers, and R(n) remains positive odd.

Suppose the first K blocks have this pattern. Iterating (5) gives
R^j(n)+5=(9/8)^j(n+5). At the start of the last prescribed block its
valuation is v_2(n+5)-3(K-1), which must be at least 4. Hence
v_2(n+5)>=3K+1, proving the necessity of (1).

Conversely assume (1). Since n+5>0, we may write n+5=2^(3K+1)t with t>=1.
Let n_j be the expression on the right of (2). These are odd integers since
3(K-j)+1>=1. They are positive: at j=0, n_0>=11, and the formula gives
n_(j+1)-n_j=(n_j+5)/8>0 whenever j<K. For j<K, the factor
2^(3(K-j)+1) is divisible by 16, so n_j=-5=11 modulo 16.
Therefore (5), with the exact run lengths established above, applies to n_j
and gives R(n_j)=n_(j+1). Induction proves (2), including the identity
with shortcut time 3j. This proves sufficiency and maximality of both runs
in every specified block, without an independence assumption.

Each such block has two odd shortcut steps, both strictly increasing the
current positive value, and then one even step to an endpoint that is
strictly greater than the block's start by (5). Thus every state after the
start within the block is strictly greater than that block's start.
The block starts themselves increase, proving T^s(n)>n for 1<=s<=3K.

For fixed positive odd n, put e=v_2(n+5)>=1. Equivalence (1) holds for every
positive K, so exactly the integers K with 3K+1<=e are possible initial
prefix lengths. Their maximum is (3), with value zero when e<=3.
Also (1) writes every positive start as 2^(3K+1)t-5 with t>=1; the value
t=1 proves the asserted sharp minimum. In particular every fixed n has
only finitely many initial (2,1) blocks. Were an ordinary integer to satisfy
(1) for all K, n+5 would be divisible by arbitrarily large powers of 2 and
therefore would have to be zero. The only such integer is -5, outside the
positive domain. Compatible finite prefixes cannot supply a positive
infinite orbit by a limiting argument.

To prove (4), take arbitrary positive q,K,N, and for each positive integer t
set n=2^(3K+1)qt-5. Formula (2), applied with qt in place of t, gives

\[
R^j(n)=9^j2^{3(K-j)+1}qt-5\equiv n\equiv-5\pmod q
\quad(0\le j\le K).
\]

There is no coprimality restriction on q. For j>=1 the same formula yields

\[
R^j(n)=\left(\frac98\right)^j n
       +5\left(\left(\frac98\right)^j-1\right)
       >\left(\frac98\right)^j n.
\]

The h values cancel, and strict monotonicity of log proves (4).
Taking t arbitrarily large supplies infinitely many distinct n>N.
The sign is positive at every allowed endpoint, whereas the rejected
certificate requires a negative change at at least one endpoint for every
sufficiently large start. A finite exception set or a larger fixed K cannot
repair it. Such a certificate would have been sufficient after finite base
verification, since log(n)+h(n mod q) has finite sublevel sets; this argument
establishes its obstruction rather than assuming its existence.

Verification detail: `python3 scripts/consecutive-blocks/check_prefix.py`
enumerates every odd start in one full residue period for K=1,...,5 and
checks parameterized witnesses for K=1,...,32, q=1,...,16 and
t in {1,2,3,17}. It compares exact run lengths, maximal prefix length,
endpoint formulas, intermediate growth, residues, and the ratio inequality
with direct shortcut iteration. These are finite arithmetic checks; the
proof above establishes the unrestricted claims.

## Mathlib

Full statement: **not checked**. Supporting valuation, iteration, congruence,
and logarithm results: **not checked**; no theorem names or direct library
links were verified. The proof is elementary and self-contained apart from
the proved block description in L002. No claim of literature novelty or of
absence from Mathlib is made.
