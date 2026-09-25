# L006 — A growing two-block return of both shifted valuations

## Hypotheses

Let T(n)=n/2 for even positive n and T(n)=(3n+1)/2 for odd positive n.
For positive odd n, let R(n) be the endpoint of its maximal initial odd
shortcut run followed by its maximal consecutive even run, as in L002.
Write (a,b) for those exact run lengths. For a positive integer x, let
v_2(x) be the exponent of 2 in x. Define

\[
J(n)=\bigl(v_2(n+5),v_2(11n+19)\bigr).
\]

Both entries are positive integers for positive odd n. Let F be any
real-valued function on pairs of positive integers, and set

\[
V_F(n)=\log(n+5)+F(J(n)),
\]

where log is the natural logarithm. No boundedness, monotonicity, or
separability of F is assumed.

## Conclusion

For every integer s>=0, define

\[
n_0=8192s+4699,\quad n_1=9216s+5287,\quad n_2=15552s+8923.
\tag{1}
\]

These are successive complete-block endpoints, with exact block types
(2,1) and (3,1), respectively. They satisfy

\[
n_0<n_1<n_2,\qquad
J(n_0)=(5,2),\quad J(n_1)=(2,6),\quad J(n_2)=(5,2).
\tag{2}
\]

For every F, the two-block potential increment is therefore

\[
V_F(n_2)-V_F(n_0)
=\log\frac{15552s+8928}{8192s+4704}
\ge\log(93/49)>0.
\tag{3}
\]

At least one of these two blocks has potential increment at least
(1/2)log(93/49). Consequently no F makes V_F nonincreasing on every
(2,1) and (3,1) block outside a finite exception set. In particular,
the proposed correction c v_2(n+5)+d v_2(11n+19) fails for every pair
of real coefficients c,d, including all nonnegative coefficients.

The repeated pair in (2) is not a repeated integer. This obstruction
does not exclude later compensation, more arithmetic information, or an
infinite aperiodic itinerary in the two-type alphabet, and does not refute
the Collatz conjecture.

## Proof

First derive exact block domains from L002. For a=2, write n=4u-1
with u positive odd. Exact b=1 means 9u-1 is congruent to 2 modulo 4,
so u is congruent to 3 modulo 4. Thus precisely n=11 modulo 16
has block type (2,1), with

\[
R(n)=\frac{9n+5}{8}.
\tag{4}
\]

For a=3, write n=8u-1 with u positive odd. Exact b=1 means 27u-1
is congruent to 2 modulo 4, so u is congruent to 1 modulo 4. Thus
precisely n=7 modulo 32 has block type (3,1), with

\[
R(n)=\frac{27n+19}{16}.
\tag{5}
\]

These congruences force the exact odd and even run lengths, not just
integrality of the endpoint expressions.

Put x=n+5 and y=11n+19=11x-36, with x'=R(n)+5 and
y'=11R(n)+19. Equations (4) and (5) give the joint shift identities

\[
\begin{array}{c|cc}
(a,b)&x'&y'\\ \hline
(2,1)&9x/8&9(y+4)/8\\
(3,1)&(27x-36)/16&27y/16.
\end{array}
\tag{6}
\]

On the first domain, x is divisible by 16, so v_2(x)>=4 and
v_2(y)=2. On the second domain, n=32t+7 gives x=4(8t+3)
and y=32(11t+3), so v_2(x)=2 and v_2(y)>=5.
This explains why switching can transfer valuation between the shifts.

For the family (1), n_0 is congruent to 11 modulo 16. Substitution
in (4) gives n_1. It is congruent to 7 modulo 32, so substitution
in (5) gives n_2. Hence both complete blocks are legal with the exact
claimed maximal run lengths. Their endpoint differences are

\[
n_1-n_0=1024s+588>0,\qquad
n_2-n_1=6336s+3636>0.
\]

All three integers are positive and odd. To compute their valuations,
write u=256s+147, which is positive and odd. Then

\[
\begin{split}
n_0+5&=32u,\\
n_1+5&=36u,\\
11n_1+19&=36(11u-1)=64\cdot9(176s+101),\\
n_2+5&=9(27u-1)/4=32\cdot9(54s+31).
\end{split}
\tag{7}
\]

The factors u, 176s+101, and 54s+31 are odd. Thus the first
valuations of n_0,n_1,n_2 are 5,2,5, and the second valuation of
n_1 is 6. If x has valuation 5, then y=11x-36 is 4 times an
odd integer, so its valuation is 2. Apply this to n_0 and n_2 to
complete (2). In particular, no valuation of zero or nonpositive
integer occurs.

The two correction values at the initial and final endpoints agree,
regardless of F. They therefore cancel in V_F(n_2)-V_F(n_0).
Since all shifted sizes are positive, the exact identity

\[
49(15552s+8928)-93(8192s+4704)=192s\ge0
\]

gives their ratio at least 93/49. Strict monotonicity of log, and
93/49>1, give (3). The sum of the two individual potential increments
is (3), so at least one is at least half its positive lower bound.

For any finite exception set of starts, choose s sufficiently large
that n_0 and n_1 both exceed every element of that set. One of the
two permitted blocks then violates even nonincrease outside the set.
This proves the unrestricted obstruction. It does not require finite
sublevel sets for an arbitrary F. When F(p,q)=cp+dq, the individual
increments are explicitly

\[
\begin{split}
V_F(n_1)-V_F(n_0)&=\log(9/8)-3c+4d,\\
V_F(n_2)-V_F(n_1)&=\log\frac{15552s+8928}{9216s+5292}+3c-4d.
\end{split}
\]

Their sum is positive for every c,d; there is no feasible coefficient
choice. The achieved sign is the opposite of the negative increment
required on both blocks, by a uniform amount.

For example s=0 has full shortcut path

    4699, 7049, 10574, 5287, 7931, 11897, 17846, 8923.

The repeated valuation pair records much less information than the
integer state. The argument uses only these two blocks and makes no
claim that the pair return or block word repeats indefinitely.

Verification detail: `python3 scripts/joint-valuation/check_potential.py`
checks the two block domains and all four identities (6) by direct
shortcut iteration on 1,024 odd starts. It also checks 261 members of
(1), including large integer parameters, with all exact valuations and
the rational bound in (3). The output is saved in
`scripts/joint-valuation/result.json`. No floating-point sign test or
sampling of possible functions F is used. These finite checks support
the arithmetic; the proof above establishes the unrestricted statements.

## Mathlib

Full statement: **not checked**. Supporting valuation, iteration, and
logarithmic monotonicity results: **not checked**; no library theorem
names or direct links were verified. The proof uses L002 and elementary
integer algebra. No claim of literature novelty or absence from Mathlib
is made.
