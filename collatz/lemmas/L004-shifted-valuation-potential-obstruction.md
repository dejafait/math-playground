# L004 — Obstruction to a potential corrected only by v_2(n+5)

## Hypotheses

Let T on positive integers be n/2 for even n and (3n+1)/2 for odd n.
For positive odd n, let R(n) be the endpoint of the maximal initial odd
shortcut run followed by the maximal even run, as in L002. Write v_2(x)
for the exponent of 2 in a positive integer x, and let log be the natural
logarithm. Let F be any real-valued function on the positive integers and set

\[
V_F(n)=\log(n+5)+F(v_2(n+5))
\]

on positive odd integers. There is no boundedness or monotonicity assumption
on F.

## Conclusion

The exact domain of blocks with run lengths (a,b)=(3,1) is n=32t+7,
t a nonnegative integer. On this domain,

\[
R(n)=54t+13>n,\qquad
v_2(n+5)=2,\qquad
v_2(R(n)+5)=1+v_2(3t+1).
\tag{1}
\]

In particular, for every integer s>=0,

\[
n_s=128s+103,\qquad R(n_s)=216s+175,\qquad
v_2(n_s+5)=v_2(R(n_s)+5)=2.
\tag{2}
\]

For every F and every s>=0, the exact potential increment satisfies

\[
V_F(R(n_s))-V_F(n_s)
=\log\frac{216s+180}{128s+108}
\ge\log(5/3)>0.
\tag{3}
\]

Consequently no correction depending only on v_2(n+5), including c v_2(n+5)
for any real constant c, makes this potential decrease on every complete
block outside any finite exception set.

There are also growing blocks that increase the valuation: for
m_s=128s+39 and c>0, with V_c(n)=log(n+5)+c v_2(n+5),

\[
\begin{split}
R(m_s)&=216s+67,\\
v_2(m_s+5)&=2,\qquad
v_2(R(m_s)+5)=3+v_2(3s+1),\\
V_c(R(m_s))-V_c(m_s)
&=\log\frac{216s+72}{128s+44}+c(1+v_2(3s+1))\\
&\ge\log(18/11)+c>0.
\end{split}
\tag{4}
\]

The valuation gain in (4) is unbounded. These are obstructions to decrease
at every single block, not to eventual decrease after a start-dependent
number of blocks, and not a disproof of Collatz.

## Proof

L002 states that a=v_2(n+1), u=(n+1)/2^a, and
b=v_2(3^a u-1), with R(n)=(3^a u-1)/2^b. If a=3, then n=8u-1 with u
positive odd. Exact b=1 is equivalent to
27u-1 congruent to 2 modulo 4, or u congruent to 1 modulo 4. Thus precisely
u=4t+1, t>=0, and n=32t+7 give (a,b)=(3,1). Direct substitution gives

\[
27u-1=108t+26=2(54t+13),\qquad R(n)=54t+13.
\]

The quotient 54t+13 is odd, which confirms maximality of the even run;
L002 also confirms exactly three initial odd steps. Since
R(n)-n=22t+6>0, these are all growing blocks. Further,

\[
n+5=4(8t+3),\qquad R(n)+5=18(3t+1),
\]

and 8t+3 is odd, while v_2(18)=1. This proves (1).

Take t=4s+3. Then (1) gives the endpoints in (2), and more explicitly

\[
n_s+5=4(32s+27),\qquad
R(n_s)+5=4(54s+45).
\]

Both parenthesized factors are positive odd integers, so both valuations
are exactly 2. The terms F(2) therefore cancel without any condition on F.
All quantities inside the logarithm are positive. The integer identity

\[
3(216s+180)-5(128s+108)=8s\ge0
\]

proves (216s+180)/(128s+108)>=5/3. Strict monotonicity of log proves (3).
The equality case s=0 gives the complete block
103,155,233,350,175. As s grows, the starts n_s are unbounded. For each
finite exception set there is therefore a witness outside it, with
potential change at least log(5/3) rather than the required negative change.
This establishes the unrestricted obstruction, including F(e)=ce for every
real c. It does not assume that an arbitrary V_F has finite sublevel sets.

For (4), instead take t=4s+1 in (1). The endpoints have the stated values,
and

\[
m_s+5=4(32s+11),\qquad
R(m_s)+5=72(3s+1)=8\cdot9(3s+1).
\]

This proves the two valuation formulas. The identity

\[
11(216s+72)-18(128s+44)=72s\ge0
\]

gives the logarithmic lower bound in (4), while v_2(3s+1)>=0 gives the
additional lower bound c on the valuation term. For every integer k>=0,
choose s=(4^k-1)/3, an integer because 4 is congruent to 1 modulo 3.
Then 3s+1=4^k and the valuation gain is 1+2k, proving unboundedness.
For s=0 this second family gives the block 39,59,89,134,67.

Verification detail: `python3 scripts/shifted-valuation/check_potential.py`
checks the exact block domain in complete residue periods and the two
parameterized witness families against direct shortcut iteration. Ratio
bounds are checked by integer multiplication, with no floating-point sign
test or sampling of possible functions F. These finite arithmetic checks
do not establish the unrestricted theorem or convergence; the argument
above proves precisely the potential obstruction.

## Mathlib

Full statement: **not checked**. Supporting results on valuations, iteration,
and logarithmic monotonicity: **not checked**; no theorem names or direct
library links were verified. The argument uses L002 and elementary integer
arithmetic. No claim of literature novelty or absence from Mathlib is made.
