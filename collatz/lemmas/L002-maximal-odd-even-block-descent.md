# L002 — Exact descent condition for a maximal odd-even block

## Hypotheses

Let T on positive integers be n/2 for even n and (3n+1)/2 for odd n.
Let n be positive and odd. For a positive integer x, write v_2(x) for the
unique nonnegative integer e such that x=2^e y with y odd. Set

\[
a=v_2(n+1)\ge1,\qquad u=(n+1)/2^a,\qquad
b=v_2(3^a u-1).
\]

Thus u is positive and odd. A complete block consists of the maximal initial
run of odd shortcut steps followed by the maximal consecutive run of even
steps, ending at the next odd integer R(n).

## Conclusion

The two run lengths are exactly a and b, with b>=1, and

\[
R(n)=T^{a+b}(n)=\frac{3^a u-1}{2^b}
     =\frac{3^a n+3^a-2^a}{2^{a+b}}.
\]

Strict descent somewhere in this complete block is equivalent to strict
descent at its endpoint, and the exact condition is

\[
R(n)<n
\quad\Longleftrightarrow\quad
(2^{a+b}-3^a)u>2^b-1.
\tag{1}
\]

In particular, 2^(a+b)>3^a is necessary; dropping the additive term in R(n)
does not establish the full condition (1).

For every prescribed pair of positive integers a,b there are infinitely many
positive odd starts having exactly these run lengths. More precisely, the
permitted u form the single odd residue class

\[
u\equiv (3^a)^{-1}(1+2^b)\pmod{2^{b+1}}.
\tag{2}
\]

For every a>=2, the attainable choice b=1 makes the block strictly growing.
For example, for every integer t>=0,

\[
n=16t+11,\qquad (a,b)=(2,1),\qquad
R(n)=18t+13>n.
\tag{3}
\]

Consequently, requiring descent during the first complete block for every
sufficiently large odd start is impossible. This excludes that proposed
sufficient criterion, not descent after later blocks or the Collatz target.

## Proof

For 0<=j<=a define n_j=3^j 2^(a-j)u-1. For j<a, the factor 2^(a-j) is even,
so n_j is positive and odd. At j=a, the value 3^a u-1 is positive and even,
since 3^a u>=3 and is odd. We have n_0=n and, for j<a,

\[
T(n_j)=\frac{3n_j+1}{2}
      =3^{j+1}2^{a-j-1}u-1=n_{j+1}.
\]

Induction gives T^j(n)=n_j through j=a. This proves both the formula for the
first even value and maximality of the odd run: no earlier state is even.

Write 3^a u-1=2^b w with w positive odd. The preceding paragraph ensures
b>=1. Starting at n_a, the next b iterates are 2^(b-1)w,...,w: the starting
state and every state before w are even, and w is odd. Thus this even run
has exactly length b, and R(n)=w. Substitution of u=(n+1)/2^a yields the
second endpoint formula.

Multiplying R(n)<2^a u-1 by positive 2^b and rearranging gives

\[
3^a u-1<2^{a+b}u-2^b
\quad\Longleftrightarrow\quad
(2^{a+b}-3^a)u>2^b-1,
\]

proving (1). Its right side is positive because b>=1, so descent requires
2^(a+b)-3^a>0. In the alternative formula

\[
R(n)=\frac{3^a}{2^{a+b}}n+
     \frac{3^a-2^a}{2^{a+b}},
\]

the additive term is strictly positive. The leading multiplier alone
therefore is not the stated exact descent test. In logarithmic form the
necessary exponent threshold is b>a log_2(3/2); condition (1) retains the
additional correction. At n=1, a=b=u=1, R(n)=1 and (1) reads 1>1, correctly
failing strict descent.

Every odd shortcut step from a positive x increases it by (x+1)/2. Hence the
odd portion of the block strictly increases from n. The even portion
strictly decreases to R(n), its smallest value on that portion. If R(n)>=n,
no state in the block is below n; if R(n)<n, the endpoint itself witnesses
descent. This proves the claimed equivalence for the whole block.

Now fix arbitrary positive a,b. Exact valuation b means

\[
3^a u-1\equiv 2^b\pmod{2^{b+1}}.
\]

Since 3^a is odd, it is coprime to 2^(b+1), so multiplication by 3^a is a
bijection on residue classes modulo 2^(b+1). This proves (2), including its
uniqueness. The inverse and 1+2^b are odd, so the class is odd. Let r be its
least positive representative. For every t>=0, take u=r+2^(b+1)t and
n=2^a u-1. Then u is positive odd, v_2(n+1)=a, and the displayed congruence
forces v_2(3^a u-1)=b exactly. These starts are distinct and unbounded.
Thus no deterministic lower bound on b in terms of a alone can exceed 1.

For b=1 and a>=2, the leading multiplier is 3^a/2^(a+1), which equals 9/8
at a=2 and increases by a factor of 3/2 whenever a increases by 1. It is
strictly larger than 1. The positive additive term then gives R(n)>n for
every start in the residue class (2). These attainable growth multipliers
are unbounded as a increases, whereas strict descent requires (1).
For the explicit family (3), u=4t+3 gives

\[
3^2u-1=36t+26=2(18t+13),
\]

with odd 18t+13. Thus a=2, b=1, and R(n)-n=2t+2>0. Taking t arbitrarily
large rules out every finite exception cutoff for first-block descent.
Nothing here controls the subsequent block lengths on these starts.

Verification detail: `python3 scripts/maximal-block/check_block.py` compares
the identities, maximal run lengths, exact descent condition, and attainable
residue classes with direct shortcut iteration. Its finite checks address
algebra and indexing; the proof above establishes the unrestricted claims.

## Mathlib

Full statement: **not checked**. Supporting results on valuations, modular
inverses, and iteration: **not checked**; no theorem names or direct library
links were verified. The proof is elementary and self-contained; no claim
of novelty or of nonexistence in Mathlib is made.
