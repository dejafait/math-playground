# L058 — Complete prime-five cancellation in the swapped root

## Hypotheses

Use L055's 25 intact triples (J_i,H_i,a_i), with a_i=2 for i<24
and a_24=166504412, in exactly L057's order
6,1,2,3,4,5,0,7,8,...,24. Each word is the formal affine map
W_i=(OOEO)^{J_i}O^{H_i}E^{a_i}, where O(x)=(3x+1)/2 and E(x)=x/2.
There is no assumed actual integer itinerary or permuted real-system witness.
Keep K=397573379, N=630138897 and Delta=2^N-3^K.
Let Phi_pi be the unshifted integer numerator of this chronological word.
The prior SPECIALIZE assessment is
`drafts/literature/2026-10-11-swapped-root-five-adic-cancellation.md`.

## Conclusion

Both nonzero integers Phi_pi and Delta have prime-five valuation exactly 1.
Consequently the reduced denominator of the unique unshifted rational root
Phi_pi/Delta is **not divisible by 5**. Its reduced numerator is also not
divisible by 5. This stops the prime-five nonintegrality diagnostic for this
one order, without proving integrality or an actual cycle. It preserves
L056's literal-order exclusion and L057's uniform-modulo-five stop.

This is local REPRODUCTION of inspected affine and valuation machinery,
not progress beyond those general sources or a Collatz resolution.
The separate critical audit below found no defect in this scope. Other factors, orders,
allocations, permuted guards, integer/parity/primitive realization, entry,
unrestricted cycles, divergence and universal eventual descent remain open.

## Proof

### Imported law and its applicability

Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational Collatz
cycles*, Acta Arithmetica 78 (1997), 227–239, DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4) and Lemma 2, pp. 228–229](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf),
gives the chronological integer affine numerator and fixed-point expression
for a nonempty binary word with nonzero fixed-point denominator. The prior
assessment inspected the statement and printed proof cases. Only that formal
identity is imported; rational parity and integer realization are unused.

L056 supplies each integral offset

\[
C_i=\frac{23\,3^{H_i}(27^{J_i}-16^{J_i})}{11}
       +(3^{H_i}-2^{H_i})16^{J_i},\quad
k_i=3J_i+H_i,\quad D_i=4J_i+H_i+a_i.
\]

Thus W_i(x)=(3^{k_i}x+C_i)/2^{D_i}. For the stated order pi, set
t_j=sum_{l<j}D_pi(l) and u_j=sum_{l>j}k_pi(l). The imported law gives

\[
\Phi_\pi=\sum_{j=0}^{24}C_{\pi(j)}2^{t_j}3^{u_j},\qquad
W(x)=\frac{3^Kx+\Phi_\pi}{2^N}.
\]

All 25 triples occur once, with the large tail attached to index 24;
the count totals are unchanged. L055 proves Delta>0 from its strictly
positive logarithmic difference, independent of order. Every C_i>0 because
J_i,H_i>0, 27>16 and 3>2; each weight is positive. Hence Phi_pi>0.
Both inputs to the valuation comparison are therefore nonzero. The unique
root is Phi_pi/Delta in coordinate x, without the shift +23/11. No
two-word closure converse or permuted height guards are used.

### Complete modulo-25 computation

Since 11*16=1 modulo 25, the offset above may be reduced using the unit
inverse 16. There is no inversion of Delta. The following are the least
nonnegative residues modulo 25 for every chronological contribution.
The power columns are 2^{t_j} and 3^{u_j}.

| j | pi(j) | C | power 2 | power 3 | contribution |
|---:|---:|---:|---:|---:|---:|
|0|6|4|1|11|19|
|1|1|16|1|22|2|
|2|2|5|9|23|10|
|3|3|11|4|11|9|
|4|4|7|2|12|18|
|5|5|21|4|14|1|
|6|0|5|22|19|15|
|7|7|2|23|8|18|
|8|8|8|23|24|16|
|9|9|2|4|3|24|
|10|10|3|24|24|3|
|11|11|5|6|19|20|
|12|12|19|24|1|6|
|13|13|14|1|18|2|
|14|14|12|6|1|22|
|15|15|15|17|16|5|
|16|16|5|16|16|5|
|17|17|1|18|7|1|
|18|18|21|2|9|3|
|19|19|6|23|4|2|
|20|20|5|16|19|20|
|21|21|16|24|13|17|
|22|22|15|7|12|10|
|23|23|21|12|14|3|
|24|24|19|6|1|14|

Each row is obtained from the displayed integer offset and exact prefix
and suffix counts; modular powers use their full exponents. For example,
j=1 has t_1=3040 and u_1=397570571; j=6 has t_6=6357 and
u_6=397567694. At j=24, t_24=306970748 and u_24=0, with the
large tail included in D_24=323168149 and in total N. All exact
exponents and complete intermediate triples are stored in the certificate.
The contribution representatives sum to 265. Therefore Phi_pi=15 modulo 25.

For the denominator, 2^20=3^20=1 modulo 25. Exact integer reduction gives
N=17 and K=19 modulo 20, and 2^17=22, 3^19=17 modulo 25.
Thus Delta=5 modulo 25. Both residues reduce to zero modulo 5,
agreeing with L057. Since neither is zero modulo 25, both valuations are
exactly 1; no higher-power calculation is required.

### Cancellation rule and verification

For prime p and nonzero integer numerator and denominator, the rational
valuation is their valuation difference, and reduction cancels the smaller
multiplicity. Precise supporting source:
[Mathlib PadicVal.Basic at commit 2da3ab0a20dc0c66f56a557e37df39f7d36cb953](https://github.com/leanprover-community/mathlib4/blob/2da3ab0a20dc0c66f56a557e37df39f7d36cb953/Mathlib/NumberTheory/Padics/PadicVal/Basic.lean),
`padicValRat.defn`, `padicValInt_dvd_iff` and
`Rat.num_or_den_zero_padicVal`. Their full statements/proofs were inspected
in the reused assessment. The prime hypothesis is met by 5, and positivity
above excludes the zero conventions. Hence the rational valuation is 1-1=0,
and coprimality of the reduced pair leaves neither member divisible by 5.
No assertion about other primes follows.

Reproduce with
`python3 scripts/postspell-word-count/test_swapped_root_five_adic_cancellation.py`.
Full evidence:
`scripts/postspell-word-count/swapped-root-five-adic-cancellation-certificate.json`.
It preserves the source SHA-256, complete allocation/order/counts, both
moduli 5 and 25, all 50 chronological records, comparison operands and
failures. All 67 comparisons pass; the complete allocation, modulo-25 trace,
comparison list and empty failures were inspected. The modulo-25 trace
already implies the modulo-five residues by reduction, so no preview or
success flag alone supplies a load-bearing claim.

The second evaluation starts from single-letter triples (3,1,2) and
(1,0,2), builds OOEO in chronological order, then uses binary repeated
composition for J_i,H_i,a_i. Concatenating (A,C,Q) followed by (B,D,R)
gives (BA,BC+QD,RQ), by the imported law. The binary loop's invariant is
that accumulated power followed by the current base to the remaining
exponent equals the originally requested power. Odd-bit accumulation,
base squaring and integer halving preserve it; all factors within a
powering call are powers of one map. Reduction respects the additions
and multiplications. This route does not use the closed offset or division
by 11. Every row triple agrees with the closed formula, and the final
composed triple (17,15,22) agrees with the full weighted sum and count
powers. This is two arithmetic implementations within this attempt,
not the later independent critical audit.

The approved cap was e<=8; the decisive equality occurs at e=2 and
terminates the test. There are no new orders, factors or guard tests.
The inherited published computational qualifications remain, with no
integer-cycle theorem applied to this rational root. Universal descent
and the restricted exclusion through 24 are unchanged.

### Separate critical audit (2026-10-11)

The prior SPECIALIZE assessment
`drafts/literature/2026-10-11-swapped-root-cancellation-audit.md`
approves this exact audit. Independent verification found no defect.
L055 supplies the complete allocation and positive Delta, L056 supplies
positive integral offsets in the unshifted coordinate, and L057 fixes
the intact swap (0,6). Each triple appears once and the large final tail
remains on index 24. Thus the denominator and totals remain unchanged.
Integrality of C_i follows from 27=16 modulo 11; positivity follows from
J_i,H_i>0. The imported formal affine identity applies without integer
parities or permuted height guards. The tested fixed point is Phi_pi/Delta,
not its shifted coordinate or a different cyclic rotation. These checks
supply all nonzero and coordinate hypotheses of the cited valuation rule.

Reproduce the independent audit with
`python3 scripts/postspell-word-count/audit_swapped_root_five_adic_cancellation.py`.
Its complete evidence is
`scripts/postspell-word-count/swapped-root-five-adic-cancellation-audit-certificate.json`.
It imports no generator functions. For each m in {5,25}, it represents
O and E by their values on every element of Z/mZ, using the unit inverse
of 2. Both maps are bijections because 2 and 3 are units. Composing their
four value tables chronologically builds OOEO. For a permutation f and
an element x, the orbit of x returns to x and has no earlier repeated
point: applying the inverse to a first repetition proves this assertion.
If its cycle length is c, the e-th iterate is precisely the cycle entry
at e modulo c. This evaluates each J_i,H_i,a_i without binary affine
powering or expanding the enormous word. It is valid on the composite
ring Z/25Z; no field assumption is made.

For every word or accumulated prefix of length D, its full value table f
recovers Q=2^D, C=Q f(0), A=Q(f(1)-f(0)) modulo m. The imported affine
law implies Q f(x)=Ax+C. The audit checks that identity at all m residues,
and composes later maps on the left. This reconstructs every row and
chronological state independently of both original arithmetic routines.
The choice of O or E is prescribed by the formal word, never inferred
from the parity of a residue representative. Delta is never inverted.

An additional independent offset check computes the least residue R of
23*3^H*(27^J-16^J) modulo 11m. Its divisibility by 11 is checked in
every row. Since the integer expression and R differ by a multiple of
11m, their quotients by 11 agree modulo m. Adding the second offset term
therefore verifies C_i without the original inverse of 11. Small unit
power cycles computed by successive integer multiplications evaluate the
powers, and fresh sums of the full integer counts give every prefix and
suffix exponent. Every weighted contribution is then compared with the
independently composed total.

All 436 comparisons pass, with no failures. They include complete equality
of every original certificate field, all 67 original comparison records,
the source digest, all 50 chronological records, all parameters and
exponents, summary and failure list. Every entry of the written 25-row
table also agrees. The complete two-modulus traces, written table and
empty failures were inspected. The representative sum is 265, the
modulo-25 total triple is (17,15,22), and the modulo-five triple is (2,0,2).
All written example exponents, the final length 323168149 and the count
residues (N mod20,K mod20)=(17,19) agree.

Inspection of the original generator confirms its chronological triple
rule, closed-offset reduction and binary-power invariant above. Its
actual execution stops at exponent 2; this audit evaluates only 5 and 25.
The residues 15 and 5 are each divisible by 5 and not by 25. Thus both
nonzero integer valuations are 1, and the cited reduced-pair law removes
5 from both numerator and denominator. This verifies Attempt 028's stop
for prime-five exclusion of this single order; higher powers of 5 cannot
reverse it. Other factors are not tested, and no integrality, permuted
real-system feasibility or actual Collatz cycle follows. This is a local
REPRODUCTION audit of the existing negative result, not a new general
mathematical result. The direct inputs, published qualifications and
Mathlib limitations are unchanged.

## Mathlib

The cited pinned source supports general prime valuation/divisibility and
coprime rational reduction. Full coverage of this particular 25-word
allocation and computation was not checked; no Lean build was run.
Supporting machinery is not a formal verification of this certificate.
