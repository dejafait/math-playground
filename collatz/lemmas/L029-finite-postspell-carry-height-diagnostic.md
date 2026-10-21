# L029 — Finite postspell carry diagnostic for initial height

## Hypotheses

Use the shortcut map and actual words W(J,H)=(OOEO)^J O^H E^2,
with J>=2,H>=3. Fix a finite list of K>=1 such labels. Require a
positive root N congruent to 20 modulo 27, all actual input parities,
and an odd endpoint after every word, including the last. No preceding
word, least-root restriction or infinite realization is assumed.

Compress to odd-to-odd accelerated steps. A word has valuation list
(1,2,1)^J followed by H-1 copies of 1 and one 3. Let a_0,...,a_(s-1)
be the concatenated list; s=sum(3J+H), q_i=sum_(j<i) a_j, and Q=q_s.
In particular Q=sum(4J+H+2)>=13K. Define C_0=0 and
C_(i+1)=3C_i+2^q_i. Set M_0=0; for i>=1 let M_i be the representative
in [1,3^i) of 2^(-q_i) C_i modulo 3^i. Define t_i by

    2^a_i M_(i+1)=3M_i+1+t_i 3^(i+1).

## Conclusion

Set r=sum_(i<s) t_i 2^q_i, epsilon=(1-M_s) mod 2 in {0,1},
R=r+2^Q epsilon, and let j be the representative in {0,...,26} of
(20-R) (2^(Q+1))^(-1) modulo 27. Then the least positive guarded
residue-20 root of this fixed list is

    N_min=R+2^(Q+1)j.                                      (1)

All its positive guarded roots are N_min+27*2^(Q+1)b, b>=0.
Consequently this fixed list admits a root N<2^K exactly when

    r<2^K, M_s is odd, and r=20 modulo 27.                  (2)

A positive carry with q_i>=K suffices to prove N>=2^K for every
root of this list. More generally it suffices that t_i 2^q_i>=2^K
for some i. This is a diagnostic, not a proof that such a carry is
forced or that (2) is impossible for the full word language.

## Proof

### Sources and specialization

Reuse the ready EXPLORE assessment
`drafts/literature/2026-10-06-postspell-full-height-lower-bound.md`.
Import the finite endpoint and carry identities and 0<=t_i<2^a_i
from Sodelin, *Route F checkpoint — bounded-alphabet endpoint-residue
gate*, claim F-BOUNDED-ALPHABET-ENDPOINT-GATE-001,
[sections 1–3, equations (1)–(9)](https://raw.githubusercontent.com/Sodelin/Collatz-Conjecture-Work/main/proof-search/routes/F_bounded_alphabet_endpoint_residue_gate.md).
The finite arguments and both carry-sign cases were inspected on
2026-10-06, live main; no immutable revision or checked formal build
is asserted. Only finite identities are used, not the infinite
equivalence or a claim that structured words force late carries.

Finite input-parity coding is imported as in L020 from
Bernstein–Lagarias, *The 3x+1 Conjugacy Map*, author manuscript
15 February 1996,
[section 1, pp. 1–3, equations (1.3)–(1.5) and its reduction-modulo-2^d permutation statement](https://websites.umich.edu/~lagarias/doc/bernstein.pdf).
L020 also supplies residue-20 preservation for these actual words.
The proof below specializes these inputs to exact final parity and
the proposed height threshold; it does not reprove general coding.
It is REPRODUCTION, with no claim of progress beyond those sources.

In OOEO, the first odd step is followed immediately by an odd input,
the second by exactly one even input and then an odd input, and the
third by an odd input in the next block or O run. Thus its accelerated
valuations are 1,2,1. The last O of the final run is followed by
exactly two even steps and an odd endpoint, so its valuation is 3.
This verifies the stated compression, including the last word.

### Carry digits and the exact parity lift

Put r_i=(2^q_i M_i-C_i)/3^i. This is integral by the defining
congruence, including r_0=0. Substitution of the two recurrences gives

    r_(i+1)=r_i+t_i 2^q_i.

This identity retains the entire offset C_i. The carry bounds imply
0<=r_i<2^q_i by induction: the upper bound at the next step is at
most (2^q_i-1)+(2^a_i-1)2^q_i=2^q_(i+1)-1.
Here a_0=1, so M_1=2 and t_0=1. Hence r=r_s>=1.

For an actual root N, its odd accelerated endpoint x_s satisfies
2^Q x_s=3^s N+C_s. The endpoint congruence gives
x_s=M_s+3^s ell, where ell>=0 since 0<M_s<3^s and x_s>0.
Therefore N=r+2^Q ell. Conversely, finite parity coding of the
complete shortcut word gives a unique root class modulo 2^Q.
The imported coding and CRT give an actual root, whose preceding
identity identifies that class as r modulo 2^Q. Thus this necessary
class is also sufficient for all Q input parities.

The endpoint of r+2^Q ell equals M_s+3^s ell. It is odd precisely
when ell=epsilon modulo 2. Its exact-valuation root class is therefore
R modulo 2^(Q+1), and 1<=R<2^(Q+1). Imposing residue 20 modulo 27
gives exactly (1) and its positive lifts, by coprimality. The first
letter of each following word forces odd internal endpoints; the
extra endpoint parity forces the last tail exact. Positivity is
preserved by actual shortcut steps, and L020 gives residue 20 at
every word boundary. This establishes every guard, not just affine
integrality at the final endpoint.

Since 2^Q>2^K, either epsilon=1 or j>=1 forces N_min>2^K.
When epsilon=j=0, N_min=r; j=0 is then exactly r=20 modulo 27.
This proves (2). Nonnegative carry contributions give the stated
sufficient height bounds directly.

### Unresolved forcing obligation

The digit blocks t_i 2^q_i occupy disjoint binary positions
q_i,...,q_(i+1)-1. Thus r<2^K means that all positions at or above
K in these blocks vanish. Equivalently, t_i=0 when q_i>=K and
t_i<2^(K-q_i) when q_i<K (the latter may be automatic).
No estimate here forbids this pattern together with the two other
guards in (2). For a suffix of zero carries, the representatives
obey 2^a_i M_(i+1)=3M_i+1. Oddness of each M_i follows from the
next such equation, but at the final endpoint it must be imposed
separately. These facts do not bound the suffix length.

L023's fixed-endpoint uniqueness is not used as a height estimate:
it neither bounds the moving M_i nor allows one to assume a preceding
word at the initial root. L022's failed affine lower bound and L024's
valuation replenishment remain intact. Excluding (2) uniformly is
still the full proposed intermediate target; it is not an established
input. Universal entry, other word types and later compensation would
remain unresolved even if it were excluded.

### Test at the first complete boundary after the last carry

This is the second bounded attempt at the same height target, using
L023's actual B-endpoint obstruction. The following applicability
calculation explains why that obstruction supplies no contradiction
at the proposed boundary. It does not disprove the height bound or
rule out other uses of inverse rigidity. Recomputing the particular
inverse and its residue is needed to test the missing hypothesis;
no general coding or uniqueness theorem is reproved.

Suppose the three exceptional-root conditions (2) hold. By the
already proved diagnostic, r itself is a positive actual guarded
root for the entire list, with every tail exact. Let h be the last
index with t_h>0, which exists since t_0=1. For every i>=h+1,
r_i=r. The actual accelerated orbit x_i of r satisfies

    2^q_i x_i=3^i r+C_i=2^q_i M_i,

so x_i=M_i at every such index. Thus zero carries identify the
representatives with the existing orbit; they do not produce a
second orbit. Let b be the first complete word boundary with
accelerated index at least h+1. It exists because s is a boundary.
Then m=x_b=M_b is positive, odd and 20 modulo 27. If b=s there
is no subsequent word to use. The incoming actual W exists even
when its beginning precedes h+1; its earlier states need not be
canonical representatives.

Write W(J,H) for this incoming word and y for its state after B^J.
L020 gives y=20 modulo 27 and

    2^H(4m+1)=3^H(y+1).

The only possible input of a single B ending at m is

    x=(16m-23)/27,
    x+1=2^(2-H) 3^(H-3)(y+1).                 (3)

Here x is a positive integer: m=20 modulo 27 makes the quotient
integral, and positivity and oddness give m>=47, hence x>=27.
The identity modulo 16 gives x=11 modulo 16. In fact this is an
actual B predecessor, not merely an integral inverse. For
x=16a+11 its four successive states are

    24a+17, 36a+26, 18a+13, 27a+20=m,

with the required odd, odd, even, odd input parities. All are
positive. Nevertheless this B history fails the residue guard
needed by L023. If H=3, (3) gives x=(y-1)/2=23 modulo 27.
If H>=4, then v_3(y+1)=1 and (3) gives
v_3(x+1)=H-2>=2, whereas x=20 modulo 27 would require valuation 1.
In neither case is x=20 modulo 27.

Consequently the incoming W and the actual B into m are compatible:
the latter starts outside the required residue class. At an internal
B endpoint in a subsequent word, the B history does have residue-20
input, but there is no W ending at that same state supplied by the
chain; L023 already excludes such an incoming W. Having passed
through an earlier W endpoint is not having a W end at this state.
At the original root no preceding W is assumed at all. These checks
retain the earliest-boundary exception and distinguish a common
endpoint from merely lying on a common orbit.

This tests the proposed boundary application for all J>=2,H>=3,
without a parameter screen or an assumption of an infinite chain.
It supplies no root-controlled carry position or uniform height
margin. The two sufficient incoming histories required for the
contradiction are not furnished by the zero-carry suffix. The
exceptional-root conjunction (2) and the height target stay open.

## Mathlib

Full finite postspell carry diagnostic, and supporting finite coding,
CRT and carry arithmetic coverage: **not checked**. No matching
declaration, absence result or formal verification is asserted.
