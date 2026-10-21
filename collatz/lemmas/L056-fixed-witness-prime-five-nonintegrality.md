# L056 — Prime-five obstruction to the fixed rational witness

## Hypotheses

Use the literal ordered 25-row allocation in L055, with
W_i=(OOEO)^{J_i} O^{H_i} E^{a_i}, a_i=2 for 0<=i<24 and
a_24=166504412. Here O(x)=(3x+1)/2 and E(x)=x/2 are formal affine
maps until an actual integer itinerary is justified. The totals are
K=397573379 and N=630138897. Let n_0 be L055's unique unshifted
rational cyclic root, and s_0=n_0+23/11 its shifted junction.

Fix this allocation, rather than all allocations with the same totals.
Reuse the prior SPECIALIZE assessment
`drafts/literature/2026-10-11-fixed-witness-integer-realization.md`.

## Conclusion

The unshifted root n_0 is not an integer: its reduced denominator is
divisible by 5. Consequently there is no actual positive integer Collatz
cycle realizing this literal ordered allocation. L055's positive rational
real-system witness and Attempt 026's real-exclusion stop remain valid.

This is a local REPRODUCTION of known affine/divisibility machinery on a
specified input, not a new general integrality theorem or a Collatz
resolution. It supplies no exclusion of other allocations, count branches
or unrestricted cycles, and no entry, divergence or eventual-descent
estimate. The separate critical audit below found no defect within this
fixed-allocation scope; it establishes no additional allocation exclusion.

## Proof

### Imported integer numerator and the coordinate match

Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational
Collatz cycles*, Acta Arithmetica 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239,
[section 2, Lemma 2 and equations (2)–(4), pp. 228–229](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf),
gives the formal map (3^k x+phi(w))/2^l and unique fixed point
phi(w)/(2^l-3^k) for a nonempty chronological binary word whenever
the denominator is nonzero. Its equation (4) concatenates the integer
numerators with the last map composed on the left. The supplied
assessment inspected the primary statement and relevant induction cases.
Here 0 denotes E and 1 denotes O; the word is nonempty, l=N and k=K.
We use this affine formula only, without importing rational parity or
integer-orbit conclusions. No reproof of the general coding theorem is
needed. The following algebra verifies the local compressed implementation.

For each row put k_i=3J_i+H_i, D_i=4J_i+H_i+a_i and

\[
A_i=3^{k_i},\qquad q_i=2^{D_i},\qquad
C_i=\frac{23\,3^{H_i}(27^{J_i}-16^{J_i})}{11}
       +(3^{H_i}-2^{H_i})16^{J_i}.
\tag{1}
\]

L020 supplies this integral positive offset; L031 explains that its
affine identity is a formal branch-composition identity, with residue
membership hypotheses used elsewhere. Integrality also follows directly
from 27=16 modulo 11. Thus W_i maps x to (A_i x+C_i)/q_i,
without presuming an actual itinerary at x. No two-word closure converse
from L031 is applied to 25 words.

Let t_i=sum_{j<i} D_j and u_i=sum_{j>i} k_j. Importing the finite
concatenation rule on these 25 compressed words gives the integer pair

\[
\Phi=\sum_{i=0}^{24}C_i\,2^{t_i}3^{u_i},\qquad
\Delta=2^N-3^K,
\quad W(x)=\frac{3^K x+\Phi}{2^N}.
\tag{2}
\]

L055 certifies N log2-K log3>0, so Delta>0. Its unshifted root is
exactly Phi/Delta. To check the coordinate explicitly, let c_i, eta_i
and B have L055's definitions. Equation (1) rearranges to

\[
q_i c_i\eta_i
=\frac{23\,3^{3J_i+H_i}-12\,3^{H_i}16^{J_i}
                         -11\,2^{H_i}16^{J_i}}{11}=C_i.
\]

Thus n_{i+1}=c_i(n_i+eta_i)=(A_i n_i+C_i)/q_i.
Composition gives n_25=(3^K/2^N)(n_0+B); its constant term is
Phi/2^N, hence Phi=3^K B. Therefore

\[
\frac{\Phi}{\Delta}
=\frac{B}{2^N/3^K-1}=n_0.
\tag{3}
\]

We are testing n_0, not s_0 or the rational quantity B alone.

### Complete prime-five calculation

The elementary power periods modulo 5 are 2^4=3^4=1. Since
N=1 modulo 4 and K=3 modulo 4,

\[
\Delta=2^N-3^K=2-2=0\pmod5.
\tag{4}
\]

Because 11=16=1 and 23=3 modulo 5, (1) gives

\[
C_i=3\,3^{H_i}(2^{J_i}-1)+(3^{H_i}-2^{H_i})\pmod5.
\tag{5}
\]

Reducing the literal table's exponents modulo 4 gives all the following
least nonnegative residues. The middle columns mean 2^{t_i} and
3^{u_i}; the final column is their product with C_i. Thus every term
of (2), including the last word, is included.

| i | C_i | 2^{t_i} | 3^{u_i} | contribution |
|---:|---:|---:|---:|---:|
|0|0|1|2|0|
|1|1|4|4|1|
|2|0|1|1|0|
|3|1|1|2|2|
|4|2|3|4|4|
|5|1|1|3|3|
|6|4|3|4|3|
|7|2|3|3|3|
|8|3|3|4|1|
|9|2|4|3|4|
|10|3|4|4|3|
|11|0|1|4|0|
|12|4|4|1|1|
|13|4|1|3|2|
|14|2|1|1|2|
|15|0|2|1|0|
|16|0|1|1|0|
|17|1|3|2|1|
|18|1|2|4|3|
|19|1|3|4|2|
|20|0|1|4|0|
|21|1|4|3|2|
|22|0|2|2|0|
|23|1|2|4|3|
|24|4|1|1|4|

For example, row 1 has J_1=15, H_1=72 and t_1=D_0=74;
u_1=K-64-117=397573198. Equations (5) and the power periods
give C_1=1, 2^{t_1}=4 and 3^{u_1}=4, and hence contribution 1.
The same explicit formulas give each displayed entry. The final
column sums to 44, so

\[
\Phi=4\pmod5.
\tag{6}
\]

If Phi/Delta were an integer m, the integer identity Phi=m Delta
would contradict (4)–(6). Equivalently, 5 divides Delta but does not
divide gcd(Phi,Delta), so the reduced denominator retains a factor 5.
Other common factors cannot cancel that factor. Any actual integer
cycle realizing this literal word would satisfy W(n)=n and, since
Delta is nonzero, have n=Phi/Delta. This is impossible. No parity
or valuation sufficiency theorem is necessary for this implication.

### Bounded certificate and exceptional primes

Reproduce with
`python3 scripts/postspell-word-count/test_fixed_witness_integer.py`.
Full evidence is
`scripts/postspell-word-count/fixed-witness-integer-certificate.json`.
It reads L055's literal table and checks its explicit tail statements,
records all 25 rows and the source SHA-256, and verifies the totals.
A sieve through 10000 agrees with a separately implemented trial-division
enumeration: 1229 primes, largest 9973. At each prime all 25 complete
triples and the two whole-word evaluations agree; 34422 checks report
no failures. Complete load-bearing rows at 5, 431 and 5233, the complete
exceptional-prime rows and the empty failures list were inspected.
A separate direct period-four calculation matches all 25 written
prime-five rows to the literal allocation and the main certificate,
with contribution sum 44 and no failures. Its complete table/checks are
`scripts/postspell-word-count/fixed-witness-written-table-check.json`.

The first evaluation uses the imported integer triple rule: if f has
(A,C,Q) and g has (A',C',Q'), g after f has
(A'A,A'C+QC',Q'Q). Binary repeated composition of the OOEO triple
(27,23,16), the O triple (3,1,2) and the E triple (1,0,2) evaluates
the compressed words with no division. The OOEO triple is independently
checked by its four single-letter compositions. Modular reduction
commutes with the additions and multiplications in this rule. Binary
powering retains the exact number of repeated maps, rather than expanding
or sampling the enormous itinerary.

The second evaluation uses (1) and the independent weighted sum (2).
To compute the first quotient of (1), take the least residue R of
F=23*3^H*(27^J-16^J) modulo 11p. Since 11 divides F, 11 divides R;
F-R is a multiple of 11p and therefore F/11=R/11 modulo p.
This is exact integer division, valid also at p=11 using modulus 121;
no inverse of a nonunit is used. Every modular triple is compared with
(3^{k_i},C_i,2^{D_i}) from this second calculation. The whole numerator
is evaluated both by sequential composition and by (2), and the total
A,Q are checked against 3^K,2^N independently.

The bounded output has denominator zeros only at primes 5, 431 and
5233, with numerator residues respectively 4, 240 and 2962. Each is
an obstruction; none is a common-factor-only case. The proof needs only
5, and does not assert that these are all prime divisors of Delta.
At 2 the denominator residue is 1 (Delta is odd), and at 3 it is 2;
neither prime can divide Delta. At 11 the denominator residue is 3 and
the numerator residue is 5, with all 25 lifted-quotient checks passing.
These dispositions do not presume reduced-denominator coprimality.

This completes the approved bounded test, without enlargement or an
allocation search. Published cycle-bound qualifications attached to
L051/L055 remain unchanged; the prime-five argument applies no such
integer-cycle bounds to reals. Their source computations and external
Lean builds have not been independently reverified here.

### Separate critical audit (2026-10-11)

The approved audit reused the primary theorem assessment in
`drafts/literature/2026-10-11-fixed-witness-nonintegrality-audit.md`.
It independently checked the complete argument above, L055's literal
table and root, L020's integral offset and L031's formal convention.
No defect was found. In particular, multiplication of eta_i by A_i gives
exactly (1); the prefix product in L055 cancels to give
3^K eta_i/C_i^(L055)=C_i^(here) 2^{t_i}3^{u_i} term by term.
Here the superscripts distinguish L055's prefix product from this lemma's
integer offset; they are not powers. This verifies the constant-term
and unshifted-root identification without any integer-parity assumption.
L055's already audited positive Lambda supplies Delta>0. The imported
word is nonempty, the fixed point is unique, and the source's rational
parity theorem and L031's two-word converse are not needed.

An independent implementation, importing no generator functions, is
`python3 scripts/postspell-word-count/audit_fixed_witness_integer.py`.
Its complete evidence is
`scripts/postspell-word-count/fixed-witness-integer-audit-certificate.json`.
It represents a triple by the homogeneous matrix [[A,C],[0,Q]], acting
on the column [x,1]. Ordinary matrix multiplication puts the later map
on the left, giving precisely the chronological composition used above.
It builds OOEO from four individual matrices and uses left-to-right
binary powering. After each exponent bit, the matrix equals the base
raised to the integer represented by the bits consumed: squaring doubles
that integer and multiplication by the base adds one. This invariant
justifies every compressed exponent, including the final tail.

Fresh prime enumeration tests previously found prime divisors through
the square root of each candidate. Every composite has such a divisor,
so the resulting list is complete through 10000. All 1229 prime records,
including all 30725 word records and their lifted residues, agree in
full with the saved certificate. All 65158 audit comparisons pass, with
an empty failure list. This checks actual records, not just success flags.
Every lifted residue is divisible by 11; its exact quotient agrees with
the division-free matrix at every prime, including modulus 121 at 11.
No modular inverse is used in either implementation.

The audit also recomputes every printed modulo-five entry directly from
the period-four arrays and matches both complete written-table arrays.
The contribution sum is 44, the denominator residue is 0 and the numerator
residue is 4. Complete denominator cases are exactly (5,0,4), (431,0,240)
and (5233,0,2962) in (prime,denominator,numerator) order within this bound.
The complete exceptional records at 2,3,11 agree as well. Thus the factor
5 survives reduction, and only this literal integer allocation is excluded.
The real witness, other allocations and all universal gaps remain intact.
This is an independent REPRODUCTION audit, with no new general theorem
or stronger prime search. Published and formalization qualifications remain
as stated above and below. The direct mathematical inputs are unchanged.

## Mathlib

Full matching coverage for this literal huge word was not checked;
unknown availability is not evidence of absence. This proof uses an
inspected published affine theorem and exact elementary modular arithmetic.
The certificate is a Python finite-arithmetic check, not a Lean proof
or a formal verification of an integer cycle.
