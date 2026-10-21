# L025 — Bounded coalescence obstruction on residue 47 modulo 243

## Hypotheses

On positive integers use the shortcut map T(n)=n/2 for even n and
T(n)=(3n+1)/2 for odd n. Let S be the positive integers congruent to
20 modulo 27. Fix an integer L>=1. Let n be any positive integer with

\[
n\equiv47\pmod{3^{L+3}},\qquad n\equiv-1\pmod{2^{L+1}},
\qquad n>12^L.                                      \tag{1}
\]

Both clocks below count shortcut steps, including zero. No convergence
hypothesis, least bad root, or restriction on the companion's word beyond
its actual parities is assumed.

## Conclusion

There are no c in S and integers 0<=s,t<=L such that

\[
0<c<n,\qquad T^s(c)=T^t(n).                         \tag{2}
\]

For each L the roots (1) form an unbounded arithmetic progression inside
47 modulo 243. Consequently there are no integers L>=1 and N>=1 giving
the bounded coalescence cover in the approved target, even with a finite
base exception. This refutes that proposed cover, not Collatz. The roots
and congruence modulus vary with L; no infinite positive orbit follows.

## Proof

### Sources and the additional argument

The prior assessment is
`drafts/literature/2026-10-05-residue47-bounded-coalescence.md`.
The [Sodelin ancestor obstruction, node
B-S20-ANCESTOR-DEPTH-OBSTRUCTION-001, exact positive-integer statement and
simultaneous case](https://raw.githubusercontent.com/Sodelin/Collatz-Conjecture-Work/main/proof-search/lemmas/Bounded_Ancestor_Depth_Obstruction.md)
was inspected on 2026-10-05. It motivates the CRT roots but proves only
ancestor and direct-descent obstructions; its coalescence extension is
not imported. The inspected unrefined Mersenne no-go likewise does not
cover parameter-dependent companions here.

We use finite parity coding from Olivier Rozier, *Parity Sequences of
the 3x+1 Map on the 2-adic Integers and Euclidean Embedding*, INTEGERS
19 (2019), A8, [Definition 1, Lemma 1 and proof, pp. 2–3](https://math.colgate.edu/~integers/t8/t8.pdf#page=2):
integers in the same class modulo 2^h have the same first h input parities.
This applies also to negative integers via the source's 2-adic map.
Its restriction to all ordinary integers is the signed shortcut map used
below. The standard affine coding is not reproved. The new work here is
its two-path specialization and anchor comparison, especially the actual
prefix of length s-t; neither inspected obstruction supplies that step.
No originality claim beyond the recorded bounded search is made.

### Shifted affine word and the slope cases

By (1), the first L inputs on the n path are odd. Indeed, for 0<=j<=L,

\[
y_j=T^j(n)=(3/2)^j(n+1)-1,
\]

and for j<L the displayed value is odd since 2^(L+1) divides n+1.
Suppose (2) holds. Reverse its actual c path from y_t. The inverse even
branch is E(y)=2y; the inverse odd branch is O(y)=(2y-1)/3, admitted only
when y=2 modulo 3. Reversing an actual path retains all these guards.
In shifted coordinates z=y+1 these branches are respectively 2z-1 and
(2/3)z. If a of the s inverse branches are O, their composition gives

\[
c+1=\lambda(n+1)-d,\qquad
\lambda=\frac{2^s3^t}{2^t3^a},\qquad 0\le d\le2^s-1.       \tag{3}
\]

The bound on d retains every offset: initially d=0, an E branch changes
d to 2d+1 and an O branch changes d to 2d/3. Induction in the inverse
length j bounds d between 0 and 2^j-1 in both cases. The factors in
lambda follow by multiplying those same shifted coefficients. These
identities hold for the selected word independently of its guards.

If lambda>1, its expression in (3), with a,t<=L, gives
lambda-1>=1/(2^t3^a)>=6^(-L). Therefore (1) and (3) imply

\[
c-n=(\lambda-1)(n+1)-d
>2^L-(2^s-1)>0,
\]

contrary to (2). If lambda=1, unique factorization gives s=t=a. Every
inverse branch is then O, so d=0 and c=n, again contrary to (2). Thus
lambda<1. Since a<=s, if s<=t then
lambda=(3/2)^(t-s) 3^(s-a)>=1. Consequently s>t. If also a<=t, (3)
would give lambda>=2^(s-t)>1. Hence

\[
h=s-t>0,\qquad b=a-t>0,\qquad
\lambda=2^h/3^b,\qquad b\le L.                      \tag{4}
\]

These cases include s=0 and t=0 and include the possible equal-slope
case; none is discarded by a strict-slope search rule.

### Transfer only the justified prefix to the anchor

Evaluate the same rational affine inverse word at the formal anchor
endpoint Y_t=(3/2)^t(47+1)-1, and denote its output by c0. Thus

\[
c_0+1=48\lambda-d,\qquad
c-c_0=\lambda(n-47)=2^h3^{L+3-b}u,
\quad u=(n-47)/3^{L+3}\in\mathbb Z.                  \tag{5}
\]

Since b<=L, (5) proves that c0 is an integer, c0=c modulo 27, and
c0=c modulo 2^h. Since lambda<1 and d>=0, it also proves c0<47.
An integer less than 47 and congruent to 20 modulo 27 is either 20
or nonpositive (the next smaller possibility is -7).

Extend T to all integers by the same even and odd formulas. Every
nonpositive integer stays nonpositive under this map: even inputs
halve, and odd inputs at most -1 map to at most -1. The orbit of 20 is

\[
20,10,5,8,4,2,1,2,1,\ldots,
\]

so it stays at most 20. It follows that T^h(c0)<=20.

Let F be the forward affine composition of the s branch symbols from
the actual c path. It is the rational inverse of the inverse word used
in (5), so F(c0)=Y_t as an affine identity. By c0=c modulo 2^h and
finite parity coding, the first h=s-t symbols of F are the actual
signed T path at c0. Only these h symbols are asserted actual at the
anchor. After them the value is x=T^h(c0)<=20. The remaining t symbols
are treated merely as rational affine maps; no further parity or
integrality at the anchor is assumed.

For any real x<=M with M>=0, each formal forward branch is at most
(3M+1)/2: x/2<=M/2<=(3M+1)/2 and (3x+1)/2<=(3M+1)/2.
Starting from M=20 and applying this upper bound t times gives

\[
F(c_0)\le21(3/2)^t-1<48(3/2)^t-1=Y_t,
\]

contradicting the affine identity. This proves (2) impossible.

### Quantifiers, checks and limits

The moduli 3^(L+3) and 2^(L+1) are coprime. The Chinese remainder
theorem gives a full residue class modulo their product satisfying the
two congruences in (1), and its positive members are unbounded. Since
L+3>=4, every such root is 47 modulo 243 and, once positive, is of the
form 47+243k with k>=0. Given any proposed N, choose a member larger
than both N and 12^L. This contradicts the requested cover. There is
no assumption that the same companion word works on the entire family:
the contradiction applies to each actual pair of words at each root.

Reproduce finite transcription checks with
`python3 scripts/bounded-coalescence/check.py`; full inverse trees are
saved to `scripts/bounded-coalescence/certificate.json`. The checked
horizons are 1,4,8,12,20, with respectively 6,84,708,3592,60828 inverse
nodes across all n-side times, and no companions satisfying (2). Each
node checks the offset and slope formulas; every smaller-slope node
checks the integer anchor transfer and the justified prefix parities.
The script retains both empty paths and enumerates both guarded inverse
branches without size pruning. These are finite transcription checks,
not the proof of the all-L statement or of completeness at larger L.

A longer, root-dependent clock can leave the all-odd prefix. Neither
that possibility, convergence on this cylinder, nor universal eventual
descent is resolved. L013–L018 motivate the cylinder's relevance but are
not mathematical premises of this obstruction. The source ancestor
obstruction is likewise motivation rather than a dependency.

## Mathlib

Full bounded residue-20 coalescence obstruction: **not checked**.
Supporting finite parity coding, congruences, CRT, and affine iteration:
**not checked**. The direct published citation supplies the parity input;
unknown Mathlib coverage is not a claim of absence. No Lean check ran.
