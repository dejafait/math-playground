# L031 — Two-postspell integer closure already enforces the guards

## Hypotheses

Use T(t)=t/2 for even positive integers and T(t)=(3t+1)/2
for odd positive integers. For i=1,2 fix integers J_i>=2, H_i>=3,
a_i>=0 with a_i congruent to 2 modulo 18. Thus a_i>=2. Put
W_i=(OOEO)^(J_i) O^(H_i) E^(a_i). Use L020's constants

\[
D_i=4J_i+H_i+a_i,\quad q_i=2^{D_i},\quad A_i=3^{3J_i+H_i},
\]
\[
C_i=\frac{23\,3^{H_i}(27^{J_i}-16^{J_i})}{11}
       +(3^{H_i}-2^{H_i})16^{J_i}.
\]

Set q=q_1q_2, A=A_2A_1, C=A_2C_1+q_1C_2 and Delta=q-A.
No least-root, primitive-period, first-return or unequal-junction
assumption is imposed.

## Conclusion

There exists a positive shortcut cycle represented by the actual
concatenation W_1 W_2, with starting integer n>1 and positive odd
junction x=T^(D_1)(n), both congruent to 20 modulo 27, if and only if

\[
\boxed{\Delta>0\quad\hbox{and}\quad \Delta\mid C.}       \tag{1}
\]

If (1) holds, its starting integer is uniquely n=C/Delta. Both
final tails are exact: writing z_1=T^(4J_1+H_1)(n) and
z_2=T^(D_1+4J_2+H_2)(n), one has v_2(z_i)=a_i.
In addition the automatically satisfied boundary identities are

\[
v_2(11n+23)=4J_1+2,\quad v_2(11x+23)=4J_2+2,
\]
\[
v_3(2^{a_1}x+1)=H_1+1,\quad
v_3(2^{a_2}n+1)=H_2+1.                    \tag{2}
\]

This is an exact reformulation, not a cycle exclusion: no proof that
(1) always fails, or parameter family satisfying it, is supplied.
The boundary guards do not impose an additional condition on a
positive integer closed root of this prescribed word. Divergence,
other cycle languages and universal entry remain unresolved.

## Proof

### Imported finite coding and its integrality specialization

L020 supplies positive integral C_i and the affine single-word
formulas; L021 supplies their composition with both offsets. Their
displayed identities are identities of the formal affine branch
compositions O(t)=(3t+1)/2 and E(t)=t/2: the input residue assumption
is used for endpoint membership, not for the affine calculation.
Thus those identities apply at any actual positive input. Import
finite input-parity coding as inspected in the saved assessment:
Bernstein–Lagarias, *The 3x+1 Conjugacy Map*, author manuscript dated
15 February 1996, [section 1, pp. 1–3, equations (1.3)–(1.5) and
the reduction-modulo-2^d permutation statement](https://websites.umich.edu/~lagarias/doc/bernstein.pdf).
For this shortcut convention the actual input string W_1 W_2
has exactly one starting class r modulo q. This is the finite
statement only; no infinite positive-integer realization is imported.
The single-word affine identities are also inspected inputs from
Sodelin, node AC-POSTSPELL-GUARDED-ROOT-DESCENT-001,
[Postspell_Guarded_Root_Descent.md, sections 2–3](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/proof-search/lemmas/Postspell_Guarded_Root_Descent.md),
live main inspected 2026-10-04, without an immutable revision or
checked Lean build. No new general coding proof is needed.

By named CRT, since q is coprime to 27, choose a positive integer
b in the coded class and congruent to 20 modulo 27. Its word is
actual, so L021 applies directly and its integer endpoint implies
q divides Ab+C. Since A is odd, it is invertible
modulo q; the congruence At+C=0 modulo q has exactly one class.
It is consequently the same class r. Thus, for positive integers t,

\[
q\mid At+C\quad\Longleftrightarrow\quad
W_1W_2\text{ is actual at }t.                         \tag{3}
\]

The justification of (3) uses the complete imported coding statement
and identification of its class. It does not presume that an
arbitrary rational affine value satisfies the input parities.

### Closure and automatic junction guards

If an actual positive closed word exists, its endpoint formula gives
qn=An+C, or Delta n=C. Positivity of C forces Delta>0, and
integrality of n forces Delta to divide C. This proves necessity.

Conversely suppose (1). Then n=C/Delta is a positive integer with
qn=An+C. By (3) its complete word is actual. All states stay
positive because each actual shortcut branch preserves positivity.
The affine formula gives its last state as n. The first input
letter and the first letter after the W_1 boundary are O, so n
and x are odd. Actual final halvings give z_1=2^{a_1}x and
z_2=2^{a_2}n; their odd endpoints make both tails exact.

It remains to check residue membership without assuming it of n.
For either word let t be its actual start, y its B^(J_i) endpoint
and m its final endpoint. The inspected identities give

\[
16^{J_i}y=27^{J_i}t+
               23(27^{J_i}-16^{J_i})/11,
\qquad 2^{H_i}(2^{a_i}m+1)=3^{H_i}(y+1).       \tag{4}
\]

The quotient in the first identity is integral. Multiplying by 11
and reducing modulo 27 yields 11y=-23 modulo 27, because
16^{J_i} is invertible there. Since 11*20=-23 modulo 27, y=20
modulo 27, regardless of t. Reducing the second identity modulo
27, using H_i>=3, gives 2^{a_i}m=-1 modulo 27.
As 2^9=-1 modulo 27, 2^18=1 modulo 27; hence a_i=2 modulo 18
gives m=20 modulo 27. Apply this to both incoming words to obtain
x congruent to n congruent to 20 modulo 27.
Since n is positive and odd in that class, n>=47>1. Therefore every
guard in the stated cycle target holds. The trivial shortcut cycle
{1,2} is excluded. No claim of primitiveness is used, and x=n
is permitted.

### Exact boundary valuations, without assuming E^2 transport

For the same word, m is odd and a_i>=2. From (4),
v_2(y+1)=H_i because 2^{a_i}m+1 is odd. Write y+1=2^{H_i}u
with u positive odd. Then

\[
11y+23=4(11\,2^{H_i-2}u+3)
\]

has exact dyadic valuation 2, since H_i>=3. The first identity
in (4) also gives
16^{J_i}(11y+23)=27^{J_i}(11t+23), so
v_2(11t+23)=4J_i+2. Finally y=20 modulo 27 implies
v_3(y+1)=1. Taking 3-adic valuations in the second identity
of (4) gives v_3(2^{a_i}m+1)=H_i+1. Applying these calculations
to the two words proves (2). This specialization treats the
independent a_i directly; it never imports L024's E^2 endpoint
transport for arbitrary tails.

All these valuation conditions follow after (1) has already forced
the actual closed orbit. Hence they furnish no separate exclusion
from the closed-root divisibility test. The approved attempt stops
at the known closure/integrality obstruction. It performs no finite
parameter enlargement, and numerical emptiness would not prove
the unbounded exclusion.

This result is REPRODUCTION of finite affine/parity machinery in
the exact guarded scope. It establishes no progress beyond the
inspected general coding and cycle-closure inputs, and makes no
originality claim.

## Mathlib

Full guard reduction and supporting finite parity coding, affine
composition, modular inverses and valuations: **not checked**.
No matching declaration or absence from Mathlib is asserted.
