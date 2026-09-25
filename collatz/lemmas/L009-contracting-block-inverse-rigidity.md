# L009 — Forced inverse decoding with a contracting block

## Hypotheses

Let T(n)=n/2 for even positive n and T(n)=(3n+1)/2 for odd positive n.
For positive odd n, let R(n) be the endpoint of its maximal initial odd
shortcut run followed by its maximal even run, as in L002. In this statement
the allowed run lengths are (1,1), (2,1), and (3,1).

An allowed predecessor of a positive odd m is a positive odd n whose
allowed block ends at m. It is extendible if it itself has an allowed
predecessor. A depth-K history ending at m, for K>=1, is a tuple
(n_0,...,n_K) of positive odd integers with n_K=m and an allowed block
from n_(i-1) to n_i at each step.

## Conclusion

The allowed predecessors and their exact existence and extendibility
conditions are as follows. All congruences apply to positive odd m.

\[
\begin{array}{c|c|c|c}
a& G_a(m)&\text{exists}&\text{exists and is extendible}\\ \hline
1&(4m-1)/3&m\equiv1\pmod3&m\equiv1\pmod9\\
2&(8m-5)/9&m\equiv4\pmod9&m\equiv22\pmod{27}\\
3&(16m-19)/27&m\equiv13\pmod{27}&m\equiv13\pmod{81}
\end{array}
\tag{1}
\]

Thus m has an allowed predecessor exactly when m=1 modulo 3. The three
extendibility classes are pairwise disjoint, so at most one predecessor
can extend. More explicitly, put s=v_3(2m+1), where v_3 is the exponent
of 3 in a positive integer, and w=(2m+1)/3^s. The only possible
extendible branch has a=s. It exists and extends exactly when

\[
s\in\{1,2,3\},\qquad 2^s w\equiv2\pmod3.
\tag{2}
\]

For every K>=1 and positive odd m there are at most three depth-K
histories ending at m. All such histories agree in n_1,...,n_K; only
their earliest state can differ. The bound three is attained, including
at depth two by

\[
(161,121,91),\qquad(107,121,91),\qquad(71,121,91).
\tag{3}
\]

The added block has exact domain n=1 modulo 8 and endpoint
R(n)=(3n+1)/4. It strictly contracts for n>1 but fixes 1. The only
allowed predecessor of 1 is 1; consequently every history ending at 1
is constant. In particular, no allowed history from a start greater
than 1 reaches 1.

Backward size need not decrease even along the extendible branch:

\[
G_1(m)-m=\frac{m-1}{3},\quad
G_2(m)-m=-\frac{m+5}{9},\quad
G_3(m)-m=-\frac{11m+19}{27}.
\tag{4}
\]

For instance, G_1(19)=25 is extendible and exceeds 19. The multiplicity
bound therefore supplies no uniform inverse contraction. There are
histories of every depth at 1. Excluding infinite allowed trajectories
from starts greater than 1, and proving universal eventual descent,
remain unresolved; neither follows from (1) or (2).

## Proof

On a block of type (a,1), L002 gives

\[
m=\frac{3^a n+3^a-2^a}{2^{a+1}},\qquad
n=G_a(m)=\frac{2^a(2m+1)}{3^a}-1.
\tag{5}
\]

Since 2 is coprime to 3, integrality requires 3^a to divide 2m+1.
Conversely, for positive odd m with this divisibility, set
u=(2m+1)/3^a. This is a positive odd integer. Then n=2^a u-1 is
positive and odd, with v_2(n+1)=a exactly. Moreover

\[
3^a u-1=2m,
\]

whose 2-adic valuation is exactly 1. The maximal-block statement of
L002 now proves that n has exactly the run lengths (a,1), with endpoint
m. This proves sufficiency, including positivity and all small cases.
It also proves that there are no other predecessors of a given type.

For a=1,2,3, respectively, the divisibility conditions are
m=1 modulo 3, m=4 modulo 9, m=13 modulo 27. These classes are nested
inside the first, proving the existence column of (1) and the union
criterion. When several branches exist they are distinct: (5) gives
G_(a+1)(m)+1=(2/3)(G_a(m)+1), which is strictly smaller.

For the added forward domain write n=2u-1, with u positive odd.
Exact even-run length 1 means 3u-1=2 modulo 4, hence u=1 modulo 4.
It follows that n=1 modulo 8, and the converse holds by L002. Formula
(5) yields R(n)=(3n+1)/4, so R(n)-n=(1-n)/4 as asserted.

By the union criterion already proved, an existing predecessor n is
extendible exactly when n=1 modulo 3. Clearing denominators in each
branch, with one extra factor of 3 in the modulus, gives

\[
\begin{aligned}
G_1(m)\equiv1\pmod3
&\iff 4m-1\equiv3\pmod9
 \iff m\equiv1\pmod9,\\
G_2(m)\equiv1\pmod3
&\iff 8m-5\equiv9\pmod{27}
 \iff m\equiv22\pmod{27},\\
G_3(m)\equiv1\pmod3
&\iff 16m-19\equiv27\pmod{81}
 \iff m\equiv13\pmod{81}.
\end{aligned}
\tag{6}
\]

For each line the last congruence implies the corresponding existence
condition in (1). Sufficiency from (5) then supplies a positive odd
predecessor; its residue 1 modulo 3 supplies an earlier allowed
predecessor. Thus (6) proves both directions, without assuming that an
integral inverse automatically has the correct maximal run lengths.
The modular multipliers are invertible; for example 8*22=14 modulo 27
and 16*13=46 modulo 81 check the stated residues directly.

The first extendibility class is 1 modulo 9. The other two are 4
modulo 9 and hence disjoint from it. Those two are distinct modulo 27,
with residues 22 and 13. This proves pairwise disjointness. The change
of alphabet matters: extendibility here uses the new endpoint condition
1 modulo 3, so the old two-letter extendibility congruences are not
being reused unchanged.

For the valuation description, (5) says that an allowed branch exists
exactly when 1<=a<=min(3,s). If a<s, then

\[
G_a(m)+1=2^a3^{s-a}w
\]

is divisible by 3. Its predecessor is consequently -1 modulo 3 and
cannot extend. If a=s is allowed, that predecessor equals 2^s w-1;
it is 1 modulo 3 exactly when the second condition in (2) holds.
If s=0 no branch exists, and if s>3 all allowed branches have a<s
and fail to extend. This proves (2) with these boundary cases retained.

The multiplicity assertion follows by induction on K. At K=1, (1)
gives at most three histories, all with the same last state. For K>=2,
any history passes through an extendible predecessor n_(K-1) of m,
because n_(K-2) is its predecessor. Disjointness in (6) makes that
n_(K-1) unique if it exists. Apply the induction hypothesis to the
depth-(K-1) histories ending there and append m. The result has at
most three histories, all sharing n_1,...,n_K. This also justifies
decoding every block except the earliest one.

To check sharpness, at m=121 formula (5) gives predecessors 161,107,71
of types (1,1),(2,1),(3,1). Each has the exact run lengths by the proved
existence criterion. Since 121=1 modulo 8, its type-(1,1) block ends
at (3*121+1)/4=91. This proves all three depth-two histories in (3).
These are different incoming histories, not an integer orbit cycle.

At m=1 only the first existence class holds, and G_1(1)=1. Induction
on depth proves that every history ending at 1 is constant. In the
original shortcut dynamics this block is 1,2,1, consistent with the
target's time-zero convention. Formula (4) follows by subtracting m
from the three expressions in (1). The example m=19 belongs to the
first extendibility class and has G_1(19)=25>19, demonstrating the loss
of monotone inverse size even away from the fixed point.

The achieved statement is a bound on histories at each endpoint and
an exact decoder, not a time bound or a least-start estimate. The
relevant remaining restricted claim is that every start greater than
1 eventually uses a block outside this alphabet. A Collatz proof would
imply that claim because no such allowed history can enter 1. This
lemma proves neither restricted escape nor sufficient compensation
toward the universal eventual-descent criterion.

Verification detail: `python3 scripts/contracting-inverse/check_branches.py`
compares (1) with independent forward maximal-block iteration through a
complete odd residue period modulo 162. It also checks finite mixed-word
histories, their common suffixes, (2), (3), and the fixed point by exact
integer arithmetic. The output is saved in
`scripts/contracting-inverse/result.json`. These checks supplement the
unrestricted proof and make no infinite-trajectory claim.

## Mathlib

Full statement: **not checked**. Supporting valuation, congruence and
iteration results: **not checked**; no theorem names or direct library
links were verified. L002 and the elementary argument above provide the
proof. No claim of literature novelty or absence from Mathlib is made.
