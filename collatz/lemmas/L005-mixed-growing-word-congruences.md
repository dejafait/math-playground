# L005 — Mixed growing words and their exact repetition bound

## Hypotheses

Let T(n)=n/2 for even positive n and T(n)=(3n+1)/2 for odd positive n.
For positive odd n, let R(n) be the endpoint of the maximal initial odd
shortcut run followed by the maximal even run, as in L002.

Let w=(a_1,...,a_K) be a nonempty word with each a_i in {2,3}.
Realizing w means that the first K complete blocks have run lengths
(a_1,1),...,(a_K,1). Put S_0=D_0=C_0=0, and for 1<=j<=K put

\[
S_j=\sum_{i=1}^j a_i,\qquad D_j=S_j+j,\qquad
C_j=3^{a_j}C_{j-1}+(3^{a_j}-2^{a_j})2^{D_{j-1}}.
\]

Write P=3^(S_K), Q=2^(D_K), D=D_K, and C=C_K. For positive odd n define
H_w(n)=(P-Q)n+C. For positive integers x, v_2(x) is the exponent of 2
in x. A copy of w contains K complete blocks, or D shortcut steps.

## Conclusion

The positive odd starts realizing w are exactly the single residue class

\[
n\equiv P^{-1}(Q-C)\pmod{2Q}.
\tag{1}
\]

Here P is odd, so its modular inverse exists. The least nonnegative
representative r_w is odd and positive, and is the least positive start
realizing w. On this class,

\[
R^j(n)=\frac{3^{S_j}n+C_j}{2^{D_j}}
\quad(0\le j\le K).
\tag{2}
\]

Every positive-time shortcut state in this prefix is strictly greater than
the original start.

The integers P-Q and C are positive and odd. For every m>=1, the first
mK blocks realize m successive copies of w if and only if

\[
2^{mD+1}\mid H_w(n).
\tag{3}
\]

Consequently the exact number of initial complete copies of w is

\[
\left\lfloor\frac{v_2(H_w(n))-1}{D}\right\rfloor,
\tag{4}
\]

which is finite for each fixed positive odd n. A start realizing m copies
necessarily satisfies the fixed-word bound

\[
n\ge\frac{2^{mD+1}-C}{P-Q}.
\tag{5}
\]

In particular, an infinite itinerary confined to {(2,1),(3,1)} cannot be
eventually periodic. Aperiodic infinite itineraries in this alphabet are
not excluded. Formula (5) tends to infinity for fixed w as m increases;
it does not give a bound tending to infinity uniformly over all words of
a given total length.

## Proof

L002 gives the complete-block formula

\[
F_a(x)=\frac{3^a x+3^a-2^a}{2^{a+1}}
\]

when the exact block lengths are (a,1). For a=2, write x=4u-1 with u
odd. Exact even-run length 1 is equivalent to 9u-1=2 modulo 4,
or u=3 modulo 4. Thus this domain is x=11 modulo 16, and
F_2(x)=(9x+5)/8. For a=3, write x=8u-1. Exact even-run length 1
is equivalent to 27u-1=2 modulo 4, or u=1 modulo 4. Thus this domain
is x=7 modulo 32, and F_3(x)=(27x+19)/16. These conditions also give
the exact odd-run lengths, since u is odd. Equivalently, for a in {2,3},
the exact domain is

\[
3^a x+(3^a-2^a)\equiv2^{a+1}\pmod{2^{a+2}}.
\tag{6}
\]

Indeed (6) gives 9x+5=8 modulo 16 or 27x+19=16 modulo 32,
whose solutions are exactly the two domains just derived.

Composing these affine formulas on a legal prefix gives (2) and the
recurrence for C_j. Since the last endpoint is odd, (2) at j=K implies

\[
3^{S_K}n+C_K\equiv2^{D_K}\pmod{2^{D_K+1}},
\tag{7}
\]

equivalently (1). It remains to prove that the final congruence implies
legality of every intermediate block, rather than only integrality of the
formal composition.

We prove sufficiency by induction on word length. For length one it is
(6). For length j>1 assume its version of (7), and write
U=3^(S_(j-1))n+C_(j-1), q=2^(D_(j-1)), a=a_j, and c=3^a-2^a.
The numerator in (7) is 3^a U+cq. Since D_j=D_(j-1)+a+1, it is
divisible by 2q. Reduction modulo 2q, using that c is odd, gives

\[
3^a U\equiv q\pmod{2q},\qquad
U\equiv q\pmod{2q}.
\]

The second assertion follows because an inverse of the odd number 3^a
is odd and hence fixes the residue q modulo 2q. It is precisely (7)
for the first j-1 letters. The induction hypothesis therefore supplies
that legal prefix, with positive odd endpoint x=U/q. Dividing the
length-j congruence by q now gives (6) for x, so the final block also
has its prescribed exact run lengths. This proves sufficiency and (2).

For j>=1, C_j is positive and odd: this is true for the first summand
C_1=3^(a_1)-2^(a_1), and subsequent recurrences multiply an odd number
by an odd number and add an even number. Thus Q-C is odd, its product
with P^(-1) modulo 2Q is odd, and r_w is not zero. All positive members
of (1) are r_w+2Qt with t>=0. This proves the least-start assertion.

Each factor 3^a/2^(a+1) is greater than 1 for a=2 or 3, and each
additive term in F_a is positive. Thus every prescribed block endpoint
is strictly larger than its block start. The odd shortcut steps strictly
increase a positive integer; the single even step ends above the block
start. Hence every state after the start in each block lies above it,
and (2)'s increasing block starts imply the prefix growth assertion.
The same multiplier comparison gives P>Q. Since P is odd and Q is
even, P-Q is odd, and H_w(n) is a positive even integer for odd n.

For m successive copies of w the formal affine composition has numerator
P^m n+B_m and denominator Q^m, where

\[
B_m=C\sum_{i=0}^{m-1}P^{m-1-i}Q^i
    =C\frac{P^m-Q^m}{P-Q}.
\]

Apply the already proved finite-word criterion to the word w repeated
m times. It is realized exactly when

\[
P^m n+B_m\equiv Q^m\pmod{2Q^m}.
\tag{8}
\]

Multiplication by P-Q is invertible modulo 2Q^m and rewrites (8) as

\[
P^m\bigl((P-Q)n+C\bigr)
\equiv Q^m(P-Q+C)\pmod{2Q^m}.
\]

The right side is zero modulo 2Q^m because P-Q+C is even.
Since P^m is odd and invertible, this is exactly (3). This establishes
both directions, including all intermediate maximal-run conditions.
Equivalently the affine identity

\[
H_w((Pn+C)/Q)=(P/Q)H_w(n)
\]

shows the valuation loss of D at each realized copy. Since H_w(n)>0
is even, its valuation is finite and at least 1. The largest nonnegative
m allowed by (3) is therefore (4). Also (3) implies
H_w(n)>=2^(mD+1), which rearranges to (5).

If an infinite allowed itinerary were eventually periodic, some positive
odd block endpoint would begin arbitrarily many copies of one fixed
nonempty word w. Formula (4) at that endpoint is finite, a contradiction.
This rules out eventual periodicity of the block labels, not merely
cycles of the integer states; it does not restrict aperiodic labels.

For comparison with the stronger target, define mu_K as the minimum r_w
over all 2^K words of length K. The sought uniform starting-size estimate
is mu_K tending to infinity. Such an estimate is equivalent to excluding
all infinite allowed itineraries: the sets of starts admitting K blocks
are nested, and bounded mu_K would eventually have a constant minimum
realizing every length. This equivalence is an unproved restricted target,
not a consequence of (5). In (5), P,Q,C vary with w; one cannot hold
them fixed while allowing all length-K words. For example, if w consists
of K copies of 2, its coefficients are P=9^K, Q=8^K,
C=5(9^K-8^K), so the m=1 bound is only

\[
n\ge\frac{2\,8^K}{9^K-8^K}-5,
\]

whose right side tends to -5. Thus this particular bound supplies no
uniform divergent lower estimate, even in that special case.

Nor does the sharp single-type starting bound survive mixing. The start
603 realizes w=(2,3,2,2), with block endpoints

\[
603,\ 679,\ 1147,\ 1291,\ 1453.
\]

Their successive starting residues are 11 modulo 16, 7 modulo 32,
11 modulo 16, and 11 modulo 16, so the exact domains above verify the
word. Yet 603<2^(3*4+1)-5=8187. This is a finite counterexample to
extending that particular bound, not to an unspecified divergent bound
or to Collatz.

Verification detail: `python3 scripts/mixed-growing-words/check_words.py`
enumerates all words through length 12, checks their least representatives
and two positive lifts by direct shortcut iteration, and compares both
directions of (1) over complete common residue periods for lengths 1–3.
It also compares (4) with direct iteration, including the first failed
copy, for words of lengths 1–4 and both small and constructed long-prefix
starts. The exact output is stored in `scripts/mixed-growing-words/result.json`.
These finite checks do not establish a bound for arbitrary aperiodic words;
the unrestricted congruence and repetition claims are proved above.

## Mathlib

Full statement: **not checked**. Supporting modular-inverse, valuation,
iteration, and finite-geometric-sum results: **not checked**; no library
theorem names or direct links were verified. The proof uses L002 and
elementary integer algebra. No claim of literature novelty or absence
from Mathlib is made.
