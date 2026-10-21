# L059 — Modulo-431 exclusion of the fixed swapped root

## Hypotheses

Use L055's 25 intact triples (J_i,H_i,a_i), indexed 0 through 24,
with a_i=2 for i<24 and a_24=166504412. Use exactly L057's order
6,1,2,3,4,5,0,7,8,...,24. Each triple denotes the formal affine word
W_i=(OOEO)^{J_i}O^{H_i}E^{a_i}, with O(x)=(3x+1)/2 and E(x)=x/2.
The totals remain K=397573379 and N=630138897. Let n_pi be the
unique unshifted rational fixed point of this concatenation.
No actual integer itinerary or permuted real-system guards are assumed.

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-11-swapped-root-mod431-obstruction.md`.
Only modulus 431 and this order are tested.

## Conclusion

The integer affine numerator Phi_pi is 240 modulo 431 and its denominator
Delta=2^N-3^K is 0 modulo 431. Consequently n_pi=Phi_pi/Delta is not
an integer. No positive integer Collatz cycle realizes this exact order
and allocation. The proof does not require primality of 431.

This is a local REPRODUCTION of known affine/divisibility machinery on
a specified input, not a new general theorem or progress beyond that
machinery in the inspected literature. It resolves this allocation's
integrality question after L058's complete prime-five cancellation.
L055's real witness, L056's literal-order exclusion and Attempts 027–028
remain valid. Other orders and allocations, integer/parity/primitive
realization generally, entry, unrestricted cycles, divergence and universal
eventual descent remain unresolved. The separate critical audit below found
no defect within this fixed-allocation scope.

## Proof

### Imported affine formula and specialization

Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational
Collatz cycles*, Acta Arithmetica 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4) and Lemma 2, pp. 228–229](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf),
gives the formal integer affine numerator, chronological concatenation
and fixed point for a nonempty word with nonzero denominator. The saved
assessment inspected its hypotheses and relevant induction cases.
Here the word is nonempty, length N and odd count K. L055's positive
N log2-K log3 is unchanged by an intact-triple permutation, so Delta>0.
Only the formal affine identity is used; no rational parity or integer
realization theorem is imported. The general formula needs no reproof.

L056 supplies integral unshifted offsets

\[
k_i=3J_i+H_i,\quad D_i=4J_i+H_i+a_i,\quad
A_i=3^{k_i},\quad Q_i=2^{D_i},
\]
\[
C_i=\frac{23\,3^{H_i}(27^{J_i}-16^{J_i})}{11}
       +(3^{H_i}-2^{H_i})16^{J_i}.
\]

The quotient is integral because 27=16 modulo 11, and all offsets are
positive. W_i(x)=(A_i x+C_i)/Q_i. At chronological position j, with
index i=pi(j), set t_j=sum_{l<j}D_pi(l) and u_j=sum_{l>j}k_pi(l).
L057's specialization of the imported formula gives

\[
\Phi_\pi=\sum_{j=0}^{24}C_{\pi(j)}2^{t_j}3^{u_j},\qquad
n_\pi=\frac{\Phi_\pi}{2^N-3^K}.
\]

This is the unshifted coordinate, not s=n+23/11. Every intact triple
occurs once; sum J_i=66061058, sum H_i=199390205 and
sum a_i=166504460 give the stated K,N, including the large closing tail.
There is no inference of permuted own-index guards from the literal witness.

### Complete exact modular calculation

All residues below are least nonnegative representatives modulo 431.
To evaluate the quotient in C_i without modular division, compute
R_i=(27^{J_i}-16^{J_i}) mod 4741. Since 4741=11*431 and the
integer difference is divisible by 11, R_i is divisible by 11 and
R_i/11 equals the quotient modulo 431. Then

\[
C_i\equiv23\,3^{H_i}(R_i/11)
 +(3^{H_i}-2^{H_i})16^{J_i}\pmod{431}.
\]

This exact lifted division uses no inverse or primality assumption.
The complete table includes every raw prefix and suffix exponent, both
power residues and every contribution T_j=C_i 2^{t_j}3^{u_j} mod 431.
The last column is the constant numerator c after composing through
position j, starting at (a,c,q)=(1,0,1).

| j | i | t_j | u_j | A_i | C_i | Q_i | 2^{t_j} | 3^{u_j} | T_j | c after j |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|0|6|0|397570688|110|355|144|1|48|231|355|
|1|1|3040|397570571|24|216|32|144|2|144|403|
|2|2|3174|397570353|27|47|290|298|32|383|320|
|3|3|3422|397569948|192|231|72|220|72|281|200|
|4|4|3881|397569187|8|346|2|324|9|396|351|
|5|5|4742|397567758|2|113|110|217|220|224|225|
|6|0|6357|397567694|12|400|288|165|162|183|171|
|7|7|6431|397562629|217|274|2|110|108|208|11|
|8|8|12151|397553090|229|51|337|220|8|112|378|
|9|9|22922|397535121|337|373|298|8|220|67|208|
|10|10|43210|397501270|2|412|149|229|110|231|375|
|11|11|81428|397437494|32|419|384|72|192|47|361|
|12|12|153430|397317340|18|87|36|64|298|345|429|
|13|13|289080|397090965|108|37|192|149|330|39|125|
|14|14|544648|396664460|24|177|149|162|337|118|211|
|15|15|1026153|395860892|128|235|384|2|6|234|325|
|16|16|1933344|394346912|229|394|16|337|192|157|323|
|17|17|3642555|391494455|288|361|24|220|288|221|44|
|18|18|6862841|386120202|128|17|3|108|110|252|141|
|19|19|12930111|375994686|243|211|128|324|4|202|49|
|20|20|24361324|356917414|12|322|220|96|144|391|37|
|21|21|45898630|320974317|144|310|3|1|1|310|35|
|22|22|86476625|253254667|110|180|3|3|192|240|80|
|23|23|162928789|125665458|149|299|1|9|36|332|388|
|24|24|306970748|0|36|55|12|9|1|64|240|

The 25 contribution representatives sum to 5412=12*431+240.
Thus Phi_pi=240 modulo 431. Direct modular exponentiation gives
2^630138897=108=3^397573379 modulo 431, so Delta=0 modulo 431.
Chronological composition finishes at (a,c,q)=(108,240,108),
independently agreeing with both numerator and denominator evaluations.
For example, position 0 gives 355*1*48=231 modulo 431. At position 1,
its running constant becomes 24*355+144*216=403 modulo 431;
its weighted contribution is 216*144*2=144 modulo 431.
The last row's full D_24=323168149 retains the large tail;
306970748+D_24=630138897. Its weighted contribution is 55*9=64.

If n_pi were an integer, Phi_pi=Delta*n_pi would imply Phi_pi=0
modulo 431. The computed residue 240 contradicts this, proving
nonintegrality. Any actual positive integer cycle with the specified
chronological word would be its fixed point, so it too is excluded.
Common zero modulo 5 and equal valuations at 5 do not affect this
independent integer-divisibility contradiction at 431.

### Certificate and verification limits

Reproduce this finite calculation with
`python3 scripts/postspell-word-count/test_swapped_root_mod431.py`.
Complete evidence is
`scripts/postspell-word-count/swapped-root-mod431-certificate.json`.
It saves the source hash, complete allocation and order, every lifted
residue and quotient, all 25 triples, weighted contributions and composition
states, all comparisons and the complete failure list.

The division-free route starts from O=(3,1,2), E=(1,0,2) and builds
OOEO=(27,23,16). Concatenating (a,c,q) followed by (b,d,r) gives
(ba,bc+qd,rq); the later map acts on the left. Left-to-right binary
powering squares the accumulated power and appends the base on a one
bit. After each bit it equals the base raised to the consumed binary
prefix, since squaring doubles that exponent and appending adds one.
This invariant justifies compression of all J,H,a, including the large
tail, using only addition and multiplication modulo 431. Each resulting
word triple is compared with its lifted closed-offset evaluation.
Each prefix/suffix exponent is recomputed from full finite sums and
compared with the running exponents; every partial a,q is checked against
its total powers. Weighted summation and chronological c agree.

All 110 comparisons pass with no failures. The complete 25-record trace,
summary and empty failure array were inspected, rather than just a preview
or saved success flag. The written table is checked in full against that
trace in all 3 transcription comparisons, saved at
`scripts/postspell-word-count/swapped-root-mod431-written-table-check.json`.
This finite implementation check supplements the imported formula,
explicit table and integer contradiction above. It is not by itself a
separate critical audit, a verified Lean proof, a permutation enumeration
or an unrestricted Collatz result. No other factors or powers are tested.

### Separate critical audit (2026-10-11)

The prior SPECIALIZE assessment
`drafts/literature/2026-10-11-swapped-root-mod431-audit.md` approved
exactly this audit. Independent examination found no defect in the
unshifted coordinate, source specialization, complete arithmetic or limited
integer contradiction. L055's allocation and positive Delta, L056's
integral offsets and L057's order remain the mathematical inputs; no new
mathematical input or DAG edge is introduced.

Reproduce the independent verification with
`python3 scripts/postspell-word-count/audit_swapped_root_mod431.py`.
Full evidence is
`scripts/postspell-word-count/swapped-root-mod431-audit-certificate.json`.
The audit imports no code from the original generator, independently
transcribes every J,H pair and checks the transcription against L055.
It retains all tails, including a_24=166504412, and every index exactly
once. All original certificates are read without overwriting them.

For an independent evaluation use normalized affine pairs (alpha,beta)
representing alpha*x+beta over integers modulo 4741. Since
2*2371=1 modulo 4741, O is (3*2371,2371) and E is (2371,0).
Composition f after g is
(alpha_f*alpha_g,alpha_f*beta_g+beta_f). This is evaluation of the
imported formal branch maps in a ring where their denominators are units;
it makes no parity assumption. Recover a length-D integer numerator by
multiplying both normalized coefficients by 2^D and reducing modulo 431.
This recovers (A,C,Q), including C, independently of division by 11.

The audit uses right-to-left binary powers. With accumulator v, current
base b and remaining exponent e, v composed with b^e remains the original
power. An odd step puts one b into v; replacing b by b squared and e by
floor(e/2) preserves the invariant. All powers involved are powers of one
map, so those factors commute; no commutativity of different word maps
is assumed. Chronological accumulation separately places each later word
on the left. This also verifies the direction of every prefix state.
The original generator's distinct left-to-right invariant was checked:
a square doubles the consumed exponent and appending the base adds one.

Every recovered triple agrees with the lifted closed formula. Because
27^J-16^J is divisible by 11, its representative modulo 11*431 is
also divisible by 11, and ordinary integer division gives the quotient
modulo 431. The audit compares all lifted differences and quotients,
prefix/suffix exponents, terms, prior/resulting states, all 110 original
comparison records, allocation, source hash, summary and empty failure
array. Entire-object comparisons include every field and key, not only
stored success flags. It also compares all 25 written rows and all fields
of the three-check transcription certificate. Both certificates agree in
full with the independent recomputation.

The positive denominator input was independently checked without floating
point. For x=2,3 put z=(x-1)/(x+1). The first 64 terms of
2*sum_{j>=0} z^(2j+1)/(2j+1) bound log(x) from below, with remainder
strictly between zero and 2*z^129/(129*(1-z^2)). The series follows by
integrating the geometric expansion of 2/(1-z^2); positivity and a
geometric upper bound justify the remainder. Multiplying lower/upper
bounds with the proper signs gives, by exact rational comparisons,
10584/10^14 < N log2-K log3 < 10585/10^14. Both full rational endpoints
are saved and were inspected. Thus Delta>0; the same K,N survive the swap.

All 128 audit comparisons pass, with no failures. The complete weighted
sum is 5412, Phi_pi is 240 modulo 431, both total powers are 108, and
the final triple is (108,240,108). The full original trace, full independent
comparison and failure data, written table and exact logarithm endpoints
were checked. The integer identity Phi_pi=Delta*n is therefore impossible.
No inverse of Delta or 11, primality assertion, integer realization or
permuted real-system guard is used. The audit preserves L055's real
witness and L058/Attempt 028's prime-five stop. It certifies one existing
local exclusion using known machinery; no new general theorem, other
order exclusion or progress to universal eventual descent is claimed.

## Mathlib

Full matching coverage for this specified huge word and certificate was
not checked. Unknown coverage is not evidence of absence. The proof uses
the inspected published affine formula and elementary modular arithmetic;
no Mathlib build or formal verification is claimed.
