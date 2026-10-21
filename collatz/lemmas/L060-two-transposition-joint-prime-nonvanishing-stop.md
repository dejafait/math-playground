# L060 — Two transpositions stop joint prime nonvanishing

## Hypotheses

Use L055's 25 indexed intact triples (J_i,H_i,a_i), with a_i=2 for
0<=i<24 and a_24=166504412. Each denotes the formal word
W_i=(OOEO)^{J_i}O^{H_i}E^{a_i}, where O(x)=(3x+1)/2 and E(x)=x/2.
The totals are K=397573379 and N=630138897. No actual integer itinerary
or permuted real-system guards are assumed. For a chronological order pi
let Phi_pi be its integer affine numerator in the unshifted coordinate,
and Delta=2^N-3^K its fixed-point denominator.

The approved SPECIALIZE assessment is
`drafts/literature/2026-10-11-joint-prime-two-transposition-test.md`.
The tested family consists exactly of orders obtained from the literal
order by zero, one or two position transpositions among indices 0 through
23, with position 24 fixed. Only moduli 5 and 431 are tested.

## Conclusion

Swapping positions (0,8) and then (7,12) gives the order

```text
8 1 2 3 4 5 6 12 0 9 10 11 7 13 14 15 16 17 18 19 20 21 22 23 24
```

For this order Phi_pi and Delta are both zero modulo 5 and modulo 431.
Thus the proposed joint nonvanishing diagnostic fails even in the
specified two-transposition family. One witness suffices; exhaustive
nonvanishing is false, and no exhaustive permutation claim is made.

This is a local REPRODUCTION of known affine arithmetic and a NEGATIVE
result for this diagnostic, not progress beyond the inspected general
machinery. Common zeros establish neither full factor cancellation,
integrality, permuted real guards, integer/parity/valuation/primitive
realization nor an actual cycle. L055's real witness, L056's literal-order
exclusion, L057's prime-five stop, L058's single-order cancellation and
L059's single-order exclusion remain valid. Entry, unrestricted cycles,
divergence and universal eventual descent remain unresolved. Separate
critical audit below found no defect within this fixed-witness diagnostic scope.

## Proof

### Imported affine rule and its applicability

Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational
Collatz cycles*, Acta Arithmetica 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4) and Lemma 2, pp. 228–229](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf),
supplies the formal affine numerator and chronological concatenation
rule, and the fixed point for a nonempty word with nonzero denominator.
The saved assessment inspected the primary hypotheses and induction.
Our word is nonempty, with length N and K odd letters. L055's positive
N log2-K log3 gives Delta>0, unchanged by intact-triple permutations.
Only the formal affine identity is used; no parity theorem is imported.
No reproof of the general formula is needed. The local calculation uses
L056's integral offsets and L057's order-sensitive specialization:

\[
k_i=3J_i+H_i,\quad D_i=4J_i+H_i+a_i,\quad
A_i=3^{k_i},\quad Q_i=2^{D_i},
\]
\[
C_i=\frac{23\,3^{H_i}(27^{J_i}-16^{J_i})}{11}
       +(3^{H_i}-2^{H_i})16^{J_i}.
\]

The quotient is integral since 27=16 modulo 11. Thus
W_i(x)=(A_i x+C_i)/Q_i. For position j put
t_j=sum_{l<j}D_pi(l), u_j=sum_{l>j}k_pi(l). Then

\[
\Phi_\pi=\sum_{j=0}^{24}C_{\pi(j)}2^{t_j}3^{u_j},\qquad
W_\pi(x)=\frac{3^Kx+\Phi_\pi}{2^N}.
\tag{1}
\]

The displayed order is obtained by the specified two disjoint swaps;
it contains every index exactly once and fixes 24. Therefore the original
sum J_i=66061058, sum H_i=199390205 and sum a_i=166504460 remain
unchanged and give K,N as stated. In particular the large tail remains
attached to row 24. The unique root is Phi_pi/Delta in the unshifted
coordinate; this calculation does not concern s=n+23/11 or B alone.

### Complete two-modulus calculation

For m=5 or 431 put R_i=(27^{J_i}-16^{J_i}) mod (11m), choosing the
least nonnegative representative. Both the integer difference and 11m
are divisible by 11, so R_i is divisible by 11 and
(27^{J_i}-16^{J_i})/11=R_i/11 modulo m. Ordinary integer division
of R_i therefore gives C_i by the displayed formula, without a nonunit
inverse. Use this to compute the residues in the following two complete
tables. Write T_j=C_i 2^{t_j}3^{u_j} mod m. The last column is the
running integer numerator c_j after composing through position j;
start at (a,c,q)=(1,0,1) and update to
(A_i a,A_i c+q C_i,Q_i q) modulo m. All representatives are least
nonnegative. The complete raw exponents, lifted quotients, triples and
three-component states are also saved in the certificate below.

Modulo 5:

| j | i | C_i | 2^{t_j} | 3^{u_j} | T_j | c_j |
|---:|---:|---:|---:|---:|---:|---:|
|0|8|3|1|1|3|3|
|1|1|1|3|2|1|2|
|2|2|0|2|3|0|3|
|3|3|1|2|1|2|1|
|4|4|2|1|2|4|0|
|5|5|1|2|4|3|2|
|6|6|4|1|2|3|3|
|7|12|4|1|3|2|1|
|8|0|0|4|3|0|1|
|9|9|2|1|1|2|0|
|10|10|3|1|3|4|3|
|11|11|0|4|3|0|3|
|12|7|2|1|1|2|1|
|13|13|4|1|3|2|1|
|14|14|2|1|1|2|0|
|15|15|0|2|1|0|0|
|16|16|0|1|1|0|0|
|17|17|1|3|2|1|3|
|18|18|1|2|4|3|1|
|19|19|1|3|4|2|4|
|20|20|0|1|4|0|4|
|21|21|1|4|3|2|1|
|22|22|0|2|2|0|4|
|23|23|1|2|4|3|4|
|24|24|4|1|1|4|0|

Modulo 431:

| j | i | C_i | 2^{t_j} | 3^{u_j} | T_j | c_j |
|---:|---:|---:|---:|---:|---:|---:|
|0|8|51|1|8|408|51|
|1|1|216|337|144|128|315|
|2|2|47|9|149|101|308|
|3|3|231|24|12|154|30|
|4|4|346|4|217|352|331|
|5|5|113|8|324|247|273|
|6|6|355|18|144|406|216|
|7|12|87|6|8|297|100|
|8|0|400|216|288|277|107|
|9|9|373|144|162|316|123|
|10|10|412|243|81|131|370|
|11|11|419|3|16|286|167|
|12|7|274|290|298|371|191|
|13|13|37|149|330|39|281|
|14|14|177|162|337|118|76|
|15|15|235|2|6|234|285|
|16|16|394|337|192|157|214|
|17|17|361|220|288|221|115|
|18|18|17|108|110|252|178|
|19|19|211|324|4|202|420|
|20|20|322|96|144|391|179|
|21|21|310|1|1|310|226|
|22|22|180|3|192|240|402|
|23|23|299|9|36|332|94|
|24|24|55|9|1|64|0|

The contribution sums are 45=9*5 and 6034=14*431. By (1),
Phi_pi=0 at both moduli. For example, at m=431 position 0 has
k_8=9539 and u_0=397563840, giving C_8=51 and T_0=51*8=408.
At position 1 the prefix length is D_8=10771, giving
216*337*144=128 modulo 431; its running numerator is
24*51+337*216=315 modulo 431. At the last position
t_24=306970748 and D_24=323168149, whose sum is N. Its term is
55*9=64 modulo 431 and its running numerator is
36*94+9*55=3879=9*431. Thus the last intact large-tail word is included.

Independently, direct modular powers give

\[
2^N=3^K=2\pmod5,\qquad 2^N=3^K=108\pmod{431}.
\]

Hence Delta is zero at both moduli. The final composed triples are
(2,0,2) modulo 5 and (108,0,108) modulo 431, agreeing with the weighted
numerators and total powers. This proves the two common-zero assertions.
The proposed diagnostic asserts that every allowed order has a nonzero
numerator at one of the two denominator-zero moduli. The displayed order
is in that family and contradicts this assertion. No converse to the
integer-divisibility condition Phi_pi=Delta*n is asserted.

### Certificate, search coverage and limits

Reproduce with
`python3 scripts/postspell-word-count/test_joint_prime_two_transpositions.py`.
Full evidence is
`scripts/postspell-word-count/joint-prime-two-transposition-certificate.json`.
It retains the complete allocation and source SHA-256, every compressed
word's lifted and division-free evaluations at both moduli, all search
records, complete 25-position witness traces, comparisons and failures.
The complete witness traces, complete parameters and empty failures were
inspected, not merely their summaries.

Division-free evaluation builds OOEO from its four single-letter triples,
then uses binary repeated composition of OOEO, O and E. After each binary
bit the accumulated power represents the consumed binary prefix:
squaring doubles it, and appending the base on a one bit adds one.
This verifies the full exponents without expanding the enormous word.
Every word agrees with the independently lifted closed offset. For each
tested order, chronological composition uses these division-free triples,
whereas the weighted sum uses closed triples, independent suffix A
products and prefix Q products. For the witness, raw sums of k_i,D_i
also independently supply all power exponents in the two written tables.
Reduction modulo m commutes with all the integer additions and products.
No modular division by Delta or 11 is performed.

The enumerator visits the identity, then each one-position-swap order,
then each ordered pair of swaps; each swap is an unordered pair of
distinct positions in 0,...,23. This includes overlapping, repeated and
both orders of swaps. The set key is the full indexed order, including
position 24, rather than a modular map. Before the common-zero stop it
processed 2354 sequences: 2290 distinct orders and 64 duplicates. All
4580 per-order modular comparisons agree, and all 165 recorded input,
word, exponent, denominator and witness checks pass, with no failures.
The search is not exhaustive and no conclusion uses minimality of the
witness. An exhaustive negative answer was unnecessary once it was found.

The written tables are checked in full against the complete witness trace
by `python3 scripts/postspell-word-count/check_joint_prime_written_tables.py`.
All 10 transcription comparisons pass, including both 25-row tables,
intact multiplicities, term sums and common-zero conclusions. Complete
evidence is `scripts/postspell-word-count/joint-prime-written-table-check.json`;
it was inspected in full. This checks transcription, not independent
mathematical correctness or critical review.

For clarity, all sequences would number 1+276+276^2=76453. The optional
distinct-order exhaustion threshold is 1+binom(24,2)+2binom(24,3)
+3binom(24,4)=36203: two identical swaps cancel, two sharing one index
give a three-cycle, and two disjoint swaps give a pair of disjoint
transpositions. Conversely every three-cycle is a product of two swaps
on its support, and every such disjoint pair is its two swaps. These
disjoint cycle types give the count. This elementary family bookkeeping
serves only a hypothetical exhaustion branch; the witness proof requires
no count theorem or full enumeration.

The prior single-order results L058 and L059 are contrasts and regression
checks, not additional premises for this common-zero implication. Inherited
published computational and external Lean qualifications remain unchanged;
no cycle-count bound is applied to arbitrary rational roots. The restricted
actual-cycle exclusion remains through 24. The separate critical audit below
checks this evidence independently; the original implementation and its
transcription check alone are not that audit.

### Independent critical audit — 2026-10-12

The approved audit assessment is
`drafts/literature/2026-10-11-joint-prime-witness-audit.md`.
The complete statement, imported affine hypotheses, unshifted coordinate,
all 25 canonical input pairs and prescribed tails, the two complete written
tables, both original programs and all their certificate fields were
reviewed. Attempts 027–029 and the audited L059 comparison concern distinct
claims; none is overridden. No defect was found. This certifies the local
method stop, without a new general theorem or a further allocation exclusion.

The independent verifier is
`python3 scripts/postspell-word-count/audit_joint_prime_witness.py`;
its full evidence is
`scripts/postspell-word-count/joint-prime-witness-audit-certificate.json`.
It does not import or execute either original program, or overwrite their
evidence. The entire allocation is independently transcribed and compared
with L055, including every index and the last tail. The count sums remain
66061058, 199390205 and 166504460, giving the same K,N.

Here is the different arithmetic representation and its justification.
For each m in {5,431}, 2 is a unit with inverse (m+1)/2, since
2((m+1)/2)=m+1. Work with normalized pairs (alpha,beta), representing
x -> alpha*x+beta in Z/mZ. If f follows g, their pair is
(alpha_f*alpha_g, alpha_f*beta_g+beta_f). The maps O and E have pairs
(3/2,1/2) and (1/2,0), where these divisions use this verified unit.
Compose O,O,E,O in the stated chronology, then its J_i-th power,
O's H_i-th power and E's a_i-th power. Right-to-left binary powering
maintains base^remaining composed with accumulator equal to the original
power: an odd bit transfers one base to the accumulator, squaring the
base and halving the residual exponent preserve the identity. Every map
here is a power of the same base within that powering call, so the needed
commutation holds. The identity accumulator handles exponent zero.

For a word of length D, multiply both normalized coordinates by 2^D
to recover (A,C,Q) modulo m. Because 2^D is a unit, this recovers exactly
the reduction of its integer affine triple; it does not divide by Delta
or assume integer parities. Composing the normalized words and recovering
with each full prefix length independently checks every previous and
resulting three-component state. Raw sums of the separately transcribed
D_i,k_i give every prefix/suffix exponent. Lifted differences modulo 11m
and their integer quotients, closed offsets, weighted terms and their sums
are recomputed and compared with these normalized evaluations. All 25 rows
at each modulus agree, including every stored word and witness-trace field.
The original left-to-right power loop is also valid: consuming a bit doubles
the represented exponent and adds one precisely when the bit is one.

The verifier reconstructs only the original 2354-sequence prefix, using
full indexed orders for equality. It checks all 2290 distinct recorded
orders and all 4580 modular comparisons, including their complete sequence,
order and residue records. Exactly 64 sequences are duplicates. The sole
common-zero order in this recorded prefix is its last distinct order,
with the claimed swaps; this fact is bookkeeping, not a minimality theorem.
No order after that prefix is evaluated. Every original check's name,
actual and required values, all failures, complete key sets, source hash
and summary agree with independent reconstruction. Both complete written
tables and all ten original transcription comparisons agree as well.

The separate certificate records 250 audit comparisons with zero failures,
including the entire original 165-check array, and retains all 4580
independent per-order comparisons. The unreduced sums are exactly 45
and 6034. Final triples are (2,0,2) and (108,0,108), respectively.
The totals, powers, large closing tail and chronology therefore give
precisely the asserted common zeros. The optional full-family count has
the four disjoint cycle types already described above; the actual coverage
2354/76453 sequences and 2290/36203 orders is explicitly partial.

The positive-Delta input is independently checked using 64 exact rational
terms for each log(x), x=2,3. With z=(x-1)/(x+1), the lower sum is
2 sum_{j=0}^{63} z^(2j+1)/(2j+1), and its positive remainder is less than
2z^129/[129(1-z^2)]. Indeed the remainder equals
2 integral_0^z t^128/(1-t^2) dt, and bounding the denominator by
1-z^2 gives that upper bound, strictly for 0<z<1. Using opposite endpoints
in N log2-K log3 gives exact bounds strictly inside
(10584/10^14,10585/10^14), saved in full. Thus Delta>0, independently
of floating-point cancellation. Permutation preserves these totals.

One family member with both numerator residues zero refutes the specified
uniform nonvanishing assertion. Primality, exhaustive enumeration and
witness minimality are unnecessary. Common zeros provide no valuations,
complete cancellation or integrality; the permuted real guards and actual
integer/parity/valuation/primitive realization remain unverified. All other
allocations, entry, unrestricted cycles, divergence and universal descent
remain unresolved. The imported qualifications and unchecked full Mathlib
coverage are unchanged. The argument and its direct mathematical inputs
are unchanged by this audit.

## Mathlib

Full matching coverage for this literal allocation, bounded family and
certificate was not checked; unknown coverage is not evidence of absence.
The proof uses the inspected published affine law and exact elementary
modular arithmetic. No Lean build or formal verification is claimed.
