# L057 — Fixed-allocation permutation stops uniform prime-five exclusion

## Hypotheses

Use the 25 intact triples (J_i,H_i,a_i) in L055, indexed 0 through 24,
with a_i=2 for i<24 and a_24=166504412. Keep
K=397573379 and N=630138897. Each triple denotes the formal affine
word W_i=(OOEO)^{J_i}O^{H_i}E^{a_i}, where
O(x)=(3x+1)/2 and E(x)=x/2. No integer itinerary is assumed.

For a permutation pi, concatenate W_pi(0),...,W_pi(24) chronologically,
and let Phi_pi be its integer affine numerator in the unshifted coordinate
x. The fixed-point denominator is Delta=2^N-3^K, as in L056.
The approved SPECIALIZE assessment is
`drafts/literature/2026-10-11-fixed-allocation-permutation-mod-five.md`.

## Conclusion

For the explicit order

```text
6 1 2 3 4 5 0 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
```

Phi_pi=0 modulo 5, and Delta=0 modulo 5. Thus the statement that
modulo 5 excludes every permutation of this multiset is false. L056's
literal-order nonintegrality remains valid. The zero residue does not
prove that Phi_pi/Delta is integral, or even that all powers of 5 cancel.
It establishes no real-system guards after permutation, parity, valuation,
residue or primitive realization, actual cycle or universal descent.

This is a local REPRODUCTION specialization of known affine arithmetic,
and a NEGATIVE result for the proposed uniform diagnostic. It is not a
claim of originality beyond inspected sources. The separate critical audit
below found no defect within this fixed-multiset diagnostic scope.

## Proof

### Imported affine law and applicability

Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational
Collatz cycles*, Acta Arithmetica 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239,
[section 2, Lemma 2 and equations (2)–(4), pp. 228–229](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf),
gives the integer affine numerator and chronological concatenation rule.
L056 records its inspected hypotheses and the local compressed offsets.
We use only its formal affine identity, for a nonempty word of length N
and K odd letters. No rational parity theorem or integer-cycle conclusion
is imported. Delta>0 was certified in L055 and is unchanged by permutation
of intact triples. The general coding theorem needs no reproof here.

Use L056's integral offsets, with k_i=3J_i+H_i and D_i=4J_i+H_i+a_i:

\[
A_i=3^{k_i},\quad Q_i=2^{D_i},\quad
C_i=\frac{23\,3^{H_i}(27^{J_i}-16^{J_i})}{11}
       +(3^{H_i}-2^{H_i})16^{J_i}.
\]

These define W_i(x)=(A_i x+C_i)/Q_i. Integrality of the quotient
follows from 27=16 modulo 11. For position j set
t_j=sum_{l<j}D_pi(l) and u_j=sum_{l>j}k_pi(l). The imported rule gives

\[
\Phi_\pi=\sum_{j=0}^{24} C_{\pi(j)}2^{t_j}3^{u_j}.
\tag{1}
\]

All triples occur exactly once, including the intact large-tail row 24;
therefore the total exponents remain K,N. Since N=1 and K=3 modulo 4,
and 2^4=3^4=1 modulo 5, Delta=2-2=0 modulo 5.

### Complete chronological calculation

Because 11=16=1 and 23=3 modulo 5, exact reduction of the integral
offset gives

\[
C_i=3\,3^{H_i}(2^{J_i}-1)+(3^{H_i}-2^{H_i})\pmod5.
\tag{2}
\]

This uses the unit 11 modulo 5; it does not divide an arbitrary
nonunit. Reduce exponents in A_i,Q_i and (2) modulo 4. The following
table lists every position in the proposed chronology, with all residues
in {0,1,2,3,4}. The last column is C_i 2^{t_j}3^{u_j} modulo 5.

| j | i=pi(j) | A_i | C_i | Q_i | 2^{t_j} | 3^{u_j} | term |
|---:|---:|---:|---:|---:|---:|---:|---:|
|0|6|2|4|1|1|1|4|
|1|1|3|1|4|1|2|2|
|2|2|4|0|1|4|3|0|
|3|3|3|1|3|4|1|4|
|4|4|3|2|2|2|2|3|
|5|5|3|1|3|4|4|1|
|6|0|1|0|4|2|4|0|
|7|7|3|2|1|3|3|3|
|8|8|2|3|3|3|4|1|
|9|9|3|2|1|4|3|4|
|10|10|2|3|4|4|4|3|
|11|11|1|0|4|1|4|0|
|12|12|4|4|4|4|1|1|
|13|13|2|4|1|1|3|2|
|14|14|3|2|2|1|1|2|
|15|15|1|0|3|2|1|0|
|16|16|1|0|3|1|1|0|
|17|17|3|1|4|3|2|1|
|18|18|3|1|4|2|4|3|
|19|19|1|1|2|3|4|2|
|20|20|1|0|4|1|4|0|
|21|21|3|1|3|4|3|2|
|22|22|4|0|1|2|2|0|
|23|23|3|1|3|2|4|3|
|24|24|4|4|2|1|1|4|

For example, at j=1 the prefix consists of row 6, so t_1=3040;
u_1=K-2691-117=397570571. Hence the power residues are 1 and 2,
and the term is 2. At j=6, t_6=6357 and u_6=397567694,
but C_0=0 makes the term zero. From j=7 onward the prefix contains
the same first seven triples as the literal order, so its total exponents
and every remaining weighted term agree with L056.

The 25 nonnegative term representatives sum to 45, yielding
Phi_pi=0 modulo 5 by (1). This is an explicit witness, so no exhaustive
search over all 25! permutations is needed to refute uniform nonvanishing.
There is no converse integrality implication: 5 divides both integers,
but their valuations and all other denominator factors remain untested.

### Finite certificate and its verification scope

Reproduce with
`python3 scripts/postspell-word-count/test_fixed_allocation_permutation_mod_five.py`.
The full certificate is
`scripts/postspell-word-count/fixed-allocation-permutation-mod-five-certificate.json`.
It records the canonical allocation SHA-256, every intact triple, exact
prefix/suffix exponents, all 25 composition states, the literal order,
the six tested swaps, every comparison and all failures. The complete
parameter array, witness trace and empty failures array were inspected.

The bounded search tested swaps (0,1) through (0,6), stopping at the
first zero; it did not claim complete order coverage. All 60 comparisons
pass. Binary repeated composition evaluates each word from (27,23,16),
(3,1,2) and (1,0,2), and agrees with every offset from (2). The first
triple is the direct four-letter OOEO triple recorded in L056. For triples
(A,C,Q) followed by (B,D,R), the imported rule is
(BA,BC+QD,RQ). The usual binary-exponent invariant retains the exact
number of repetitions. Sequential application of this rule yields
(2,0,2) modulo 5 for the complete permuted word; separately (1) gives
the same numerator. Modular reduction commutes with all these integer
additions and multiplications, so giant itinerary expansion is unnecessary.
The saved transcription check
`scripts/postspell-word-count/fixed-allocation-permutation-written-table-check.json`
compares the complete written table with the complete chronological
certificate, verifies all 25 index multiplicities and the term sum 45;
all three comparisons pass. This is a transcription check; the separate
independent critical audit is recorded below.
The certificate supplements the explicit calculation above; it does not
replace the mathematical implication or assert any actual input parities.

The inherited published computational and external Lean qualifications
of L055/L056 remain unchanged. No integer-cycle lower bound is applied
to a rational root here. The restricted actual-cycle exclusion remains
through 24, while other allocations/branches, entry, unrestricted cycles,
divergence and universal eventual descent remain unresolved.

### Separate critical audit (2026-10-11)

The prior SPECIALIZE assessment
`drafts/literature/2026-10-11-fixed-allocation-permutation-audit.md`
approved exactly this audit. Independent review found no defect in the
proof or its limited implication. L055's complete indexed allocation and
positive Delta and L056's unshifted integer offsets are the mathematical
inputs. Permuting intact triples preserves K,N and Delta, without assuming
that the permuted real-system guards or any integer parities hold. The
imported formal affine law has precisely this scope. The complete written
table has each index once, with a_24=166504412 still attached to row 24.

The independent implementation is
`python3 scripts/postspell-word-count/audit_fixed_allocation_permutation.py`;
its full evidence is
`scripts/postspell-word-count/fixed-allocation-permutation-audit-certificate.json`.
It imports no generator functions and uses a different arithmetic
representation: the values of each formal map on all five elements of
F_5. Because 2 and 3 are units, O(x)=3(3x+1) and E(x)=3x modulo 5
are permutations. OOEO is built from its four letters in chronological
order. For each point x, follow a permutation until it first returns to x.
Bijectivity makes this a finite cycle, and the e-th iterate at x is the
cycle entry indexed by e modulo its length. This computes every full
J_i,H_i,a_i exponent exactly, including the large tail, without binary
triple composition or expansion of the huge word.

For a word of length D with residue map f, recover
Q=2^D, C=Q f(0), A=Q(f(1)-f(0)) modulo 5. The imported affine law
gives Q f(x)=Ax+C, and the implementation verifies this at all five
residues. Later maps act on the left. Thus each recovered triple and each
chronological composition state is independently computed in the same
unshifted convention as (1). This reduction is valid for formal affine
maps; the branch choice is prescribed, not chosen from residue parity.
Division by 2 here is division by a unit; no division by Delta occurs.

Fresh exact sums of the literal k_i,D_i compute every prefix and suffix
exponent. Period-four arrays independently evaluate (2) and every term
of (1). The audit compares all fields of the original certificate,
including both complete 25-state traces, all parameters and exact
exponents, all 60 original comparison records, the six swaps, source
digest and failure list. It also compares both sides of the complete
written-table certificate. The generator's table parsing, intact tail
assignment, triple composition, binary-power invariant, first-zero stop
and failure recording were inspected. In its powering loop, the
accumulated power times the current base to the remaining exponent is
the original requested power; the odd-bit update and halving preserve
this invariant. All these maps are powers of the same base within each
call, so the composition order in that invariant is valid.

All 79 audit comparisons pass, with no failures. The six recorded swap
numerators are 2,4,4,3,1,0; the first zero is exactly swap (0,6).
The complete allocation, witness trace, written table, swap records and
empty failure array were additionally inspected from the audit evidence.
The witness total triple is (2,0,2), its term sum is 45, and the literal
order still has term sum 44 and numerator 4. The claimed j=1 and j=6
exponents agree exactly. For j>=7 only the prefix/suffix exponents and
weighted contributions agree with the literal order; the accumulated
numerator states need not agree and are not identified.

One zero order refutes uniform nonvanishing without enumeration of all
orders. No valuation comparison or full cancellation follows, and no
integral root or permuted real witness is asserted. This is an independent
REPRODUCTION audit of an existing negative result, not a new theorem or
stronger exclusion. L055/L056, the restricted exclusion through 24, both
recorded method stops and all unresolved universal gaps remain unchanged.
The direct mathematical inputs and published/formalization qualifications
are unchanged.

## Mathlib

Full matching Mathlib/Lean coverage for this explicit multiset calculation
was not checked. Unknown coverage is not evidence of absence. The argument
uses the cited affine theorem and elementary exact modular arithmetic;
the Python certificate is not a Lean proof or a verified integer cycle.
