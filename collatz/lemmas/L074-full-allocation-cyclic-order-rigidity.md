# L074 — Full-allocation cyclic-order rigidity

## Hypotheses

Keep exactly L055's 25 indexed integer pairs J_i,H_i, for 0<=i<=24.
Let b_i be nonnegative integers with sum b_i=9250245, and attach
a_i=2+18b_i to indexed row i. Let pi be any permutation of {0,...,24}.
Suppose real s_0,...,s_25 satisfy s_25=s_0, s_k>=540/11, and,
for every chronological position 0<=k<=24,

\[
s_{k+1}=2^{-a_{\pi(k)}}\left(G_{\pi(k)}s_k-Q_{\pi(k)}\right)+23/11,
\quad G_i=(27/16)^{J_i}(3/2)^{H_i},
\quad Q_i=(12/11)(3/2)^{H_i}+1,
\tag{1}
\]
\[
4J_{\pi(k)}\log2\le\log s_k+\log(11/4).
\tag{2}
\]

These are precisely the endpoint/domain/own-input J conditions of L051.
Each outgoing row retains its indexed pair and allocated tail throughout
any permutation or rotation. Logarithms are natural. No H guard, seed,
minimum location, distinguished large-tail row, integrality, actual-word,
residue, parity, exact-valuation or primitive/count-ray premise is imposed.

## Conclusion

The cyclic order pi is a rotation of 0,1,...,24. More precisely, rotating
to any smallest designated junction makes the order exactly 0,1,...,24.
Every nonidentity order after that rotation has a strictly failed own-input
J guard at its first displaced row, with left-minus-right margin greater
than 629441541677/50000000000>12.58.

This is local RESEARCH/REPRODUCTION under the prior SPECIALIZE assessment
`drafts/literature/2026-10-17-full-allocation-cyclic-order-rigidity.md`.
It extends the allocation scope of a known local method; no originality
beyond the inspected literature is asserted. The separate critical audit
below found no defect. Neither a downstream integer exclusion nor an actual-word
consequence is assembled here. Both literal rational witnesses remain
valid. Other pair tables, unrestricted cycles, entry, divergence and
universal eventual descent remain unresolved.

## Proof

### Allocation and order preserve the full cyclic product

For indexed row i put

\[
\eta_i=\frac{23}{11}-\frac{12}{11}(16/27)^{J_i}
                    -(16/27)^{J_i}(2/3)^{H_i},
\qquad c_i=2^{-a_i}G_i.
\]

Since J_i,H_i>0, both subtracted factors are positive and their sum
is strictly less than 12/11+1=23/11. Thus 0<eta_i<23/11.
With n_k=s_k-23/11>=47, the exact coordinate identity in (1) is

\[
n_{k+1}=c_{\pi(k)}(n_k+\eta_{\pi(k)}).
\tag{3}
\]

The standard formal affine-word input is Halbeisen–Hungerbuehler,
*Optimal bounds for the length of rational Collatz cycles*, Acta Arithmetica
78 (1997), 227–239, DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
The ready assessment inspected the theorem and essential induction cases.
Only the real affine identity is imported. Every row is a nonempty formal
postspell word with nonnegative integer exponents; arbitrary chronology
concatenates those words. No parity or integer-realization converse is used,
and no general affine coding theorem is reproved here.

The complete L055 table gives sum J_i=66061058 and sum H_i=199390205.
For every admitted allocation,

\[
\sum_i a_i=50+18\cdot9250245=166504460,
\quad K=\sum_i(3J_i+H_i)=397573379,
\quad N=\sum_i(4J_i+H_i+a_i)=630138897.
\]

Each row occurs once, so prod c_i=3^K/2^N=e^{-Lambda}, independently
of allocation and order. L055's audited count-dependent enclosure gives
Lambda=N log2-K log3>lambda_-=10584/10^14>0. In particular the
formal fixed-point denominator is nonzero. Multiplying (3), including
the final edge, and cancelling the positive product of the n_k gives

\[
\Lambda=\sum_{k=0}^{24}\log(1+\eta_{\pi(k)}/n_k).
\tag{4}
\]

For m=min_k n_k>=47, log(1+x)<x for x>0 and eta_i<23/11 imply
Lambda<575/(11m). Hence the smallest shifted junction obeys

\[
s_{\min}<\frac{575}{11\lambda_-}+\frac{23}{11}
=\frac{7187500000030429}{14553}<500000000000<e^{27}.
\tag{5}
\]

The exact rational comparisons and the final exponential comparison
are the certified calculations in L069 (6)–(7): its positive sum
sum_(q=0)^40 27^q/q! already exceeds 500000000000. We import those
numerical inequalities, not L069's restricted-tail exclusion. Equations
(3)–(4) check their applicability anew to every allocation here. The
analytic inputs are the positive-real logarithm identity and exponential
series, NIST DLMF [4.5.1](https://dlmf.nist.gov/4.5.E1) and
[4.2.19](https://dlmf.nist.gov/4.2.E19), as assessed and specialized in
L069. Thus log s_min<27 without locating that minimum or assuming growth.

### A domain-valid comparison for every allocated tail

For a real input s>=540/11 set n=s-23/11>=47. Directly from the
definitions, G_i eta_i=(23/11)G_i-Q_i, and therefore

\[
G_i s-Q_i=G_i(n+\eta_i)>0.
\tag{6}
\]

L073 establishes this domain-sign comparison for the same fixed pairs;
it is a rowwise statement independent of chronology and early support.
Since every a_i>=2, comparison at the same actual input gives

\[
2^{-a_i}(G_i s-Q_i)+23/11
\le \tfrac14(G_i s-Q_i)+23/11
=c_i^*s+81/44-(3/11)(3/2)^{H_i}
<c_i^*s,\qquad c_i^*=G_i/4.
\tag{7}
\]

For the strict sign, every H_i>=40>=5 and
(3/11)(3/2)^5=729/352>648/352=81/44, as in L069's tail-2
comparison. The potentially positive offset of the actual large-tail
map is never discarded. Instead (6) permits replacing that map by the
tail-2 upper comparison, whose offset is negative. Every application is
at an actual input satisfying the assumed domain; no hypothetical
comparison trajectory is required to stay in the domain.

### Rotation and complete first-displacement coverage

Choose a minimum occurrence q and rotate inputs by k -> (q+k) mod 25,
carrying the outgoing row with each input. The old closing edge remains
an edge, and the new closing edge is the old edge from q-1 to q.
Thus all equations and own-input guards survive, even when junction
values repeat. Write pi and s again for the rotated tuple. By (5),
log s_0<27.

If pi is not the identity, let k be its first displaced position.
Then k<=23 and j=pi(k)>k: all rows less than k have already been used,
and agreement through position 23 would force the final position too.
Every preceding row is literal. Applying (7) at each of its actual
inputs, with all actual junctions positive, gives

\[
\log s_k<27+A_k\log3-D_k\log2,
\quad A_k=\sum_{i<k}(3J_i+H_i),
\quad D_k=\sum_{i<k}(4J_i+H_i+2).
\tag{8}
\]

The empty prefix k=0 is included. Crucially D_k uses comparison tails
2, not an unsupported sign claim about the actual tails. All allocated
tails were retained in the full product (4).

Use L069's certified bounds with S=10^12, ell=693147180559 and
u=1098612288669: log2>ell/S, log3<u/S and log(11/4)<2.
Define M_(k,j)=4J_j ell-29S-A_k u+D_k ell. These expressions depend
only on the fixed pairs and the tail-2 comparison prefixes, so they are
exactly L069 (9), with no changed operands. L069 certifies all 24
weakest cases M_(k,k+1)>0 and strict increase of the J_i; hence for
every 0<=k<j<=24,

\[
M_{k,j}\ge M_{k,k+1}\ge12588830833540>0.
\tag{9}
\]

This imports the complete certified finite inequality, not a preview
or a sample. Its final prefix has A_23=144318712, D_23=162928789;
its smallest case is (0,1). No allocation-dependent quantity enters
this table. From (8) and the outward bounds,

\[
4J_j\log2-(\log s_k+\log(11/4))
>\frac{M_{k,j}}{S}
\ge\frac{629441541677}{50000000000}>12.58.
\tag{10}
\]

Thus the non-strict own-input guard (2) fails at the first displaced
row. Every nonidentity permutation has such a position, so the minimum
rotation must be literal. Reversing that rotation proves the conclusion.
This uses neither the literal rejection step of L069 nor L073's
early-support exclusion. It does not assert feasibility of an arbitrary
literal allocation or add any integer or actual-word conclusion.

The only new step needed for this full-simplex specialization is (7)
and its application to arbitrary-tail prefixes, together with the explicit
full-budget product match. No new numerical certificate or recalculation
of the already audited finite margins is needed. Those load-bearing
inequalities and their complete proof were read in L069; the new uniform
coverage is the symbolic argument above, not enumeration of allocations.

### Independent critical audit — 2026-10-17, step 269

This audit uses the prior SPECIALIZE assessment
`drafts/literature/2026-10-17-full-allocation-cyclic-order-critical-audit.md`.
The construction assessment's inspected primary statements, essential proof
cases and duplicate/failure comparison remain applicable. No additional
external theorem is imported. The verdict verifies this local reproduction;
it is not a new theorem beyond the inspected sources.

**Hypotheses and product.** L051's endpoint and non-strict J guard match
(1)–(2) exactly; its H/seed and count-ray hypotheses are not used. L055's
complete table has positive J,H, minimum H=40, strictly increasing J,
sum J=66061058 and sum H=199390205. For the entire integer simplex,
sum a=50+18*9250245=166504460, giving precisely the stated K,N.
A permutation preserves every summand and each tail remains attached to
its indexed pair. Thus the count-dependent L055 Lambda enclosure applies
without its original allocation, root, minimum or guard conclusions.

The two subtractions in eta have sum strictly between zero and 23/11.
Hence 0<eta<23/11, and G eta=(23/11)G-Q verifies (3) with the
actual allocated tail. Every n is at least 47. Multiplying all 25 edges,
including closure, cancels identical positive incoming and outgoing
products, even with coincident junctions. Taking logarithms gives (4).
For m=min n, each summand is less than eta/n<23/(11m); the positive
lower bound on Lambda gives (5) in the stated direction. The exact
rational bound and positive exp(27) partial sum were independently
rechecked through the existing L069 audit program. No integer-cycle,
minimum-location or growing-row premise enters.

**Arbitrary-tail comparison.** At every actual s>=540/11, n>=47 and
G>0 make Gs-Q=G(n+eta)>0. Since a>=2, multiplication by
2^(-a)<=1/4 proves the first comparison in (7). The tail-2 offset is
exactly 23/11-Q/4=81/44-(3/11)(3/2)^H. It is strictly negative
because H>=40>=5 and 729/352>648/352. This proves the strict endpoint
bound for every tail, including a=2 and the maximum 166504412, without
assigning a sign to the actual arbitrary-tail offset. L073 supplies this
rowwise domain-sign precedent; its literal order, early-support premise
and exclusion are not used. The comparison multipliers G/4 are positive.
Induction applies at actual inputs, so the upper comparison trajectory
need not satisfy the domain or any guard.

**Rotation and exhaustive coverage.** At a chosen minimum q, replace the
position-k input and row by their old (q+k) mod 25 occurrences. The old
closing edge remains an edge; the new closing edge is the old edge q-1
to q. Every endpoint, attached tail and own-input guard is retained.
This works for any minimum occurrence, without assuming uniqueness.
After rotation log s_0<27. A nonidentity permutation first differs at
k<=23 with j=pi(k)>k, since all smaller rows have been used. Each
preceding row is therefore indexed i<k in literal order, though its
actual tail may be arbitrary. Applying (7) at those actual inputs gives
(8) with exactly the tail-2 comparison totals A_k,D_k. At k=0 the
empty-prefix bound is already strict by (5); at k=23 the preceding
rows are exactly 0 through 22. No displaced-row endpoint or suffix
estimate is required.

Since A_k,D_k>=0 and J_j>0, replacing log3 by u/S and log2 by
ell/S bounds the prefix height above and the guard's left side below
in the required directions. Together with log(11/4)<2, their difference
is strictly greater than M_(k,j)/S, including the empty prefix. For
fixed k, M_(k,j)-M_(k,k+1)=4(J_j-J_(k+1))ell>=0. All 24 complete
weakest records were inspected, and all 300 records recomputed exactly.
They cover every 0<=k<j<=24, with minimum 12588830833540 at (0,1).
The final prefix has A_23=144318712 and D_23=162928789, and scaled
left/right operands 85945478764125031844 and 45616708760840061277.
Thus every first displacement fails its own non-strict J guard by more
than 629441541677/50000000000>12.58. The first-displacement partition,
not permutation sampling, proves completeness. Neither L069's literal
rejection nor its restricted-tail hypotheses are imported.

**Exact evidence and scope.** Read and ran the existing independent program
`python3 scripts/postspell-word-count/audit_permuted_last_pair.py`.
It does not import the construction program. Its separately transcribed
table is compared with canonical L055; direct prefix sums and every pair
operand are recomputed. Its exact 160-term positive logarithm sums and
integrated remainders verify the L055 Lambda and grid-log inputs, using
opposite endpoints for N log2-K log3. The analytic inputs remain the
assessed DLMF 4.6.4, 4.5.1 and 4.2.19; this is no new logarithm or
affine-coding theorem. All 387 checks pass, with zero failures. The full
certificate remains
`scripts/postspell-word-count/permuted-last-pair-audit-certificate.json`.
The complete weakest records, exact Lambda endpoints, exponential total
and summary were inspected; finite monotonicity covers every larger-row
case. The program also checks L068's boundary margin for its original
audit; that check is not used by L074.

No defect, changed premise, stronger conclusion or missing direct input
was found. The existing DAG requires no change; in particular L069 and
L073 supply only the identified inequalities and domain-sign precedent.
No preview, pass flag or scalar ordering theorem substitutes
for the symbolic argument. Both rational witnesses and Attempts 026–031
remain valid. No integer exclusion or actual-word consequence is assembled;
other pairs, entry, unrestricted cycles, divergence and universal descent
remain unresolved.

## Mathlib

Full matching theorem coverage is unchecked. Basic finite-product,
logarithm monotonicity and affine-composition results could support a
formalization; no matching Mathlib theorem for this prescribed table and
guard system is asserted. Unknown coverage is not evidence of absence.
