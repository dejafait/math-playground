# L080 — Prime-five nonintegrality of both redistributed-H survivors

## Hypotheses

Use L079's indexed table: L055's 25 pairs, with only H_0=39 and
H_24=32670622 substituted. Set B=9250245, K=397573379 and N=630138897.
For each t in {0,1}, use literal chronological order 0,...,24 and
b_i=0 for i<=22, b_23=t, b_24=B-t, a_i=2+18b_i.
Let Phi(t), Delta=2^N-3^K and the formal unshifted row-0 cyclic root
n_0(t)=Phi(t)/Delta have exactly L078's definitions. No feasibility,
integer itinerary or actual Collatz orbit is assumed.

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-18-redistributed-h-survivor-mod25.md`.

## Conclusion

The complete integer pairs satisfy

\[
(\Phi(0),\Delta)\equiv(16,5),\qquad
(\Phi(1),\Delta)\equiv(7,5)\pmod {25}.
\]

For each t, v_5(Phi(t))=0 and v_5(Delta)=1. Thus the reduced
denominator of n_0(t) contains exactly one factor of 5; both roots
are nonintegral and Delta does not divide either numerator.

This is local REPRODUCTION of the assessed affine/divisibility machinery,
with fresh finite arithmetic, not progress beyond the checked general
results. The separate critical audit below found no defect. It supplies the
two arithmetic certificates only: no full-table assembly, actual-word application,
survivor feasibility, other-table exclusion or universal eventual descent
is proved here. Both original-table rational witnesses remain valid.

## Proof

### Imported pair and coordinate

Reuse Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational
Collatz cycles*, Acta Arithmetica 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
The prior assessment inspected the primary hypotheses and printed
induction cases. Import only the formal affine identity and fixed point
for a nonempty binary word with nonzero denominator. Later maps act on
the left; no parity-realization converse or rotation-gcd theorem is used.

In L078's notation, with O(n)=(3n+1)/2 and E(n)=n/2, put

\[
k_i=3J_i+H_i,\quad d_i(t)=4J_i+H_i+a_i(t),\quad
T_i(t)=\sum_{j<i}d_j(t),\quad U_i=\sum_{j>i}k_j,
\]
\[
F_i=\frac{23\,3^{H_i}(27^{J_i}-16^{J_i})}{11}
       +(3^{H_i}-2^{H_i})16^{J_i},\qquad
\Phi(t)=\sum_{i=0}^{24}F_i2^{T_i(t)}3^{U_i}.
\tag{1}
\]

L078 already proves that the concatenation of
(OOEO)^{J_i}O^{H_i}E^{a_i(t)} has map
(3^K n+Phi(t))/2^N, and that its fixed point is the **unshifted**
row-0 input n_0(t)=s_0(t)-23/11=Phi(t)/Delta. Its identity applies
to test roots without assuming their guards. L079 certifies all the
table data needed there, in particular positive Lambda. Consequently
Delta>0, while each F_i and each weighted term is a positive integer
by L078. Both integers being valued are nonzero. The word is nonempty.
These are the source's required qualifications.

Fresh sums of the changed table give sum J=66061058,
sum H=199390205 and sum a=166504460, hence the stated K,N for
both t. The unchanged totals do not identify any old numerator.
In particular d_0=73, k_0=63 and k_24=125665459.
The respective last-pair lengths are

| t | a_23 | a_24 | d_23 | d_24 | T_24 |
|---:|---:|---:|---:|---:|---:|
|0|2|166504412|144041959|323168150|306970747|
|1|20|166504394|144041977|323168132|306970765|

Every closing tail is included in d_24 and N.

### Complete residues and independent composition

All entries below are least nonnegative residues modulo 25.
The integer quotient in (1) can be evaluated using 11^{-1}=16
modulo 25, since 11*16=1 modulo 25. Delta is never inverted.
For i<=23 the displayed powers and contributions are the same for
both t; the last row explicitly displays the two values as t=0 / t=1.

| i | F_i | 2^{T_i} | 3^{U_i} | F_i 2^{T_i}3^{U_i} |
|---:|---:|---:|---:|---:|
|0|19|1|21|24|
|1|16|17|17|24|
|2|5|3|3|20|
|3|11|18|21|8|
|4|7|9|7|16|
|5|21|18|4|12|
|6|4|24|7|22|
|7|2|24|24|2|
|8|8|24|22|24|
|9|2|2|9|11|
|10|3|12|22|17|
|11|5|3|7|5|
|12|19|12|3|9|
|13|14|13|4|3|
|14|12|3|3|8|
|15|15|21|23|20|
|16|5|8|23|20|
|17|1|9|21|14|
|18|21|1|2|17|
|19|6|24|12|3|
|20|5|8|7|5|
|21|16|12|14|13|
|22|15|16|11|15|
|23|21|6|17|17|
|24|4|3 / 7|1|12 / 3|

These evaluate every term of (1). Their representative sums are
341 and 332, giving Phi(0)=16 and Phi(1)=7 modulo 25.
For example the changed final row uses F_24=4 and U_24=0;
its two full prefix exponents in the preceding table give 2^{T_24}
equal to 3 and 7. The changed first row has F_0=19 and
U_0=397573316, giving its contribution 24. All interior rows are
freshly weighted with the changed prefixes and suffixes.

Both denominator powers are recomputed for each t. Since
2^20=3^20=1 modulo 25 and (N mod20,K mod20)=(17,19),
they are 2^N=22 and 3^K=17. Thus Delta=5 modulo 25.

Independently evaluate the imported affine law using triples (A,F,Q)
for maps (An+F)/Q. If (A,F,Q) is followed by (C,G,R), their
triple is (CA,CF+QG,RQ). Compose the single-letter triples
O=(3,1,2), E=(1,0,2); OOEO has triple (27,23,16).
Binary composition powers of this block, O and E give each row
without using formula (1), division by 11, or any modular division.
At every powering iteration, the accumulated power composed with
the current base raised to the remaining exponent is the requested
power; odd-bit accumulation and squaring preserve this invariant.
Reduction modulo 25 commutes with all these integer operations.

All 50 row triples agree with
(3^{k_i},F_i,2^{d_i(t)}) modulo 25. Composing them in chronological
order gives final triples (17,16,22) and (17,7,22), independently
agreeing with both complete sums and denominator powers. The final
even tail remains in each last row and final denominator.

Reproduction command:
`python3 scripts/postspell-word-count/test_redistributed_h_survivors_mod25.py`.
The complete certificate is
`scripts/postspell-word-count/redistributed-h-survivors-mod25-certificate.json`.
It records source hashes, every actual pair/allocation/tail, all raw
prefix and suffix exponents, every row triple, every composition state,
all contributions, actual/required modulus, comparison operands and
failures. All 65 checks pass, with no failures. Both full 25-row
traces and the empty failure list were inspected with the shared JSON
inspector. Actual and required precision are exactly modulus 25.
No other parameter, modulus, prime, permutation or feasibility test
is performed.

### Interpret the residues

Reuse the assessed prime-power cancellation rule, supported by
[Mathlib PadicVal.Basic](https://github.com/leanprover-community/mathlib4/blob/2da3ab0a20dc0c66f56a557e37df39f7d36cb953/Mathlib/NumberTheory/Padics/PadicVal/Basic.lean)
at commit 2da3ab0a20dc0c66f56a557e37df39f7d36cb953,
`padicValInt_dvd_iff`, `padicValRat.defn`, and
`Rat.num_or_den_zero_padicVal`. The ready assessment inspected their
hypotheses and proofs; here p=5 is prime and both represented integers
are positive. Residues 16 and 7 are nonzero modulo 5, so both numerator
valuations are zero. Delta=5 modulo 25 has exact valuation one.
Therefore reduction of each rational quotient leaves exactly one factor
5 in its denominator. In particular neither quotient is integral.
No general valuation theorem is reproved.

This calculation succeeds for both approved candidates and stops here.
It can support a later L078 application to this table, but that assembly
and any actual-word consequence are outside this bounded step. Common
zero residues and the old permutation cancellation stops are not being
used as exclusions or overridden. No assertion about all individual
junctions or survivor feasibility is made. Independent universal gaps
remain open; this is not a complete Collatz candidate.

### Independent critical audit — 2026-10-18, step 309

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-18-redistributed-h-survivors-mod25-critical-audit.md`.
This RESEARCH/REPRODUCTION audit found no defect in either certificate
or its nonintegrality interpretation. It validates a local mathematical
input, not a new general theorem or a complete Collatz candidate. The
primary affine and valuation imports cited above are reused; no general
theorem is reproved and no new source hypothesis is introduced.

**Premises and coordinate.** The independently transcribed 25 pairs
match L055 exactly, before making only L079's two H replacements.
All J_i>=2 and H_i>=3; each tested allocation is nonnegative integral
with total B, and every tail is at least 2 and congruent to 2 modulo 18.
The fresh totals are those displayed above. In particular the full word
is nonempty and the final tail enters N in both cases. L079's audited
strict bound 10584/10^14<Lambda supplies Delta>0; reduction modulo 25
alone is not used to infer that sign. L078's positive integral F_i and
positive weights supply Phi(t)>0. Thus both valuations are of nonzero
integers, independently of feasibility or actuality.

L078's formula (8) gives 3^{k_i} eta_i=F_i at each row and its formula
(7) gives n_{i+1}=c_i(n_i+eta_i), where n_i=s_i-23/11. Hence the row
map used here is exactly the unshifted map. Its complete chronological
composition tests the input of indexed row 0; it does not test s_0,
a different cyclic cut, or an asserted minimum. L078 explicitly supplies
this identity for test roots without feasible J guards. No survivor
existence or parity converse is needed.

**Independent complete finite evidence.** Run
`python3 scripts/postspell-word-count/audit_redistributed_h_survivors_mod25.py`.
The audit reads but does not import or execute the constructor and leaves
its certificate unchanged. It uses generic 2x2 matrix multiplication,
with M_O=[[3,1],[0,2]] and M_E=[[1,0],[0,2]], retaining all entries
modulo 25. For a triple (A,F,Q), the corresponding matrix is
[[A,F],[0,Q]]; following this map by another multiplies its matrix
on the left, reproducing the cited chronological affine composition.
Direct multiplication of the four letters gives
M_B=M_O M_E M_O M_O=[[2,23],[0,16]] modulo 25.

For each of O,E,B, the audit explicitly records all powers from 0
through 20 by successive multiplication and verifies M^20=I.
Associativity therefore permits M^e=M^{e mod 20} for every nonnegative
e used here. This is a verified finite implementation shortcut, not
an assumed period or a new general coding theorem. Each row is evaluated
as M_E^{a_i} M_O^{H_i} M_B^{J_i}, in that order. Scalar cycles from
successive multiplication separately verify 2^20=3^20=1 modulo 25.
For an additional comparison, the audit computes the coordinate-form
integer offset modulo 25 as

\[
16\bigl(23\,3^{k_i}-12\,3^{H_i}2^{4J_i}
                    -11\,2^{H_i+4J_i}\bigr)\pmod {25},
\]

using only the verified unit 11*16=1 modulo 25. This is exactly the
expanded L078 (8). No inverse of Delta, 5, or any nonunit is used.
The original constructor's binary-power loop was also inspected: its
accumulated power followed by the current base to the remaining exponent
is invariant; odd-bit accumulation and squaring preserve it, and integer
halving terminates for these nonnegative exponents. The independent
matrix implementation uses none of that loop.

All 50 saved row records are compared field by field against the new
calculation: pairs, allocations, tails, raw k_i,d_i,T_i,U_i, offsets,
both weights, contributions, row triples and before/after composition
states. Both complete traces were also read with the shared JSON inspector.
Every printed residue-table entry and both printed last-pair length rows
agree. All original 65 comparison records have equal operands; their
failure list is empty and the three mathematical source hashes match.
The new audit additionally checks the claimed numerator residues explicitly.
The representative sums are 341 and 332; full chronological matrices
have triples (17,16,22) and (17,7,22). Both count evaluations give
(N mod20,K mod20)=(17,19), 2^N=22, 3^K=17 and Delta=5 modulo 25.

The complete audit certificate is
`scripts/postspell-word-count/redistributed-h-survivors-mod25-audit-certificate.json`.
All 1104 checks pass with no failures. It preserves every actual/required
comparison, all matrix/scalar cycles and both independently reconstructed
25-row traces; the full cycles and empty failure list were inspected.
Actual and required modulus are both exactly 25. This is finite exact
arithmetic evidence, not a formal Lean verification or a numerical preview.

**Interpretation and boundary.** Since 16 and 7 are nonzero modulo 5,
and Delta is 5 modulo 25, the cited prime/nonzero valuation rules apply
with exact numerator valuations zero and denominator valuation one.
Consequently both reduced denominators retain exactly one factor of 5.
This justifies both nondivisibility claims without assuming any other
factor cancels or survives. The constructor's branches for other residues
are not needed: these two actual residues are independently verified.
No parameter, factor or modulus expansion was made. The old common-zero
and complete-cancellation failures concern different data and remain valid.
Both original rational witnesses remain intact. This audit adds no
feasibility, full-table assembly or actual-word conclusion; all universal
gaps remain open. It changes no direct mathematical dependency or argument,
so DAG.md and PROOF.md are unchanged.

## Mathlib

The pinned declarations above support divisibility and cancellation for
nonzero integers and rationals under prime hypotheses. Full matching
Mathlib coverage for this changed table and its finite evaluations is
not checked. No Lean build, formal certificate or absence claim is made.
