# L061 — Fixed joint witness cancels both tested denominator primes

## Hypotheses

Use L055's complete 25 indexed triples (J_i,H_i,a_i), with a_i=2
for i<24 and a_24=166504412. Each denotes the formal affine word
W_i=(OOEO)^{J_i}O^{H_i}E^{a_i}, where O(x)=(3x+1)/2 and E(x)=x/2.
Fix exactly L060's chronological order, obtained by swapping positions
(0,8) and (7,12) in the literal order:

```text
8 1 2 3 4 5 6 12 0 9 10 11 7 13 14 15 16 17 18 19 20 21 22 23 24
```

The totals are K=397573379 and N=630138897. Let Phi_pi be the
unshifted integer affine numerator and Delta=2^N-3^K. No actual integer
itinerary or permuted real-system guard is assumed. The prior SPECIALIZE
assessment is `drafts/literature/2026-10-12-joint-witness-prime-square-test.md`.
Only moduli 25 and 185761 are approved here.

## Conclusion

Both positive integers Phi_pi and Delta have valuation exactly one at
each of the primes 5 and 431. In particular

\[
\Phi_\pi\equiv20,\quad\Delta\equiv5\pmod{25},\qquad
\Phi_\pi\equiv2586,\quad\Delta\equiv40514\pmod{185761}.
\]

The reduced denominator of Phi_pi/Delta is divisible by neither 5 nor
431; its reduced numerator is divisible by neither prime either. Thus
these two primes cannot exclude integrality of this fixed root: the
approved strict denominator-over-numerator valuation test fails.

This is a local REPRODUCTION of the inspected affine and cancellation
machinery, and a NEGATIVE result for this diagnostic. It supplies no new
general theorem beyond the sources checked. It does not prove integrality,
permuted real guards, integer/parity/exact-tail/primitive realization, or an
actual cycle. Other primes, orders and allocations, entry, unrestricted
cycles, divergence and universal eventual descent remain unresolved.
L055's real witness and the earlier single-order exclusions remain valid.
The separate critical audit below found no defect within this fixed-order
two-prime scope.

## Proof

### Imported formulas, coordinate and nonzero obligations

Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational
Collatz cycles*, Acta Arithmetica 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf),
gives the integer chronological affine numerator and the fixed-point
formula for a nonempty formal binary word with nonzero denominator.
The prior assessment inspected its statement and relevant induction cases.
Here length=N, odd-letter count=K, and the last branch is composed on the
left. Only this affine identity is imported; no parity-realization theorem
is applied, and no general reproof is needed.

L056 supplies the positive integral unshifted offsets, and L057 supplies
their chronological permutation specialization. Put

\[
k_i=3J_i+H_i,\quad D_i=4J_i+H_i+a_i,\quad A_i=3^{k_i},\quad Q_i=2^{D_i},
\]
\[
C_i=\frac{23\,3^{H_i}(27^{J_i}-16^{J_i})}{11}
      +(3^{H_i}-2^{H_i})16^{J_i}.
\tag{1}
\]

Since 27=16 modulo 11, the quotient is an integer. Since J_i,H_i>0,
both summands are positive, so C_i>0. For position j put
t_j=sum_{l<j}D_pi(l) and u_j=sum_{l>j}k_pi(l). The imported rule gives

\[
\Phi_\pi=\sum_{j=0}^{24}C_{\pi(j)}2^{t_j}3^{u_j},\qquad
W_\pi(x)=\frac{3^Kx+\Phi_\pi}{2^N}.
\tag{2}
\]

Every weight is positive, so Phi_pi>0. Every intact triple occurs once,
including row 24 with its full tail; the allocation sums remain
sum J_i=66061058, sum H_i=199390205 and sum a_i=166504460, giving
the stated K,N. L055's audited bound
N log(2)-K log(3)>10584/10^14>0 therefore still proves Delta>0.
Thus both valuation inputs are nonzero and the unique root is Phi_pi/Delta,
in the unshifted x coordinate. The shifted junction x+23/11 and auxiliary
quantity B are not being tested. L060's common zeros are retained and
independently recovered by the calculations below.

### Complete finite evaluations at exactly the two squares

All entries below are least nonnegative residues modulo the specified m.
Let T_j=C_pi(j) 2^{t_j}3^{u_j} modulo m. Let c_j be the numerator
constant of the composed prefix ending at position j, before dividing
by its accumulated power of 2. Starting at (A,c,Q)=(1,0,1), appending
the word (a,d,q) gives

\[
(A,c,Q)\longmapsto(aA,\;ac+Qd,\;qQ)\pmod m.
\tag{3}
\]

The offsets are evaluated without nonunit modular division. Compute
R_i=(27^{J_i}-16^{J_i}) modulo 11m, with 0<=R_i<11m.
The integer difference is divisible by 11, so 11 divides R_i and
(27^{J_i}-16^{J_i})/11=R_i/11 modulo m. Substitute this integer
quotient in (1). The program retains every R_i and R_i/11.
The powers in (1) and (2) use the unreduced integer exponents with exact
modular repeated squaring; no unproved order reduction is used.

For an independent evaluation of the same formal words, compose the
letter triples O=(3,1,2), E=(1,0,2) by (3). OOEO gives (27,23,16).
Power this block J_i times, then append O^{H_i} and E^{a_i} using binary
powering of affine triples. This evaluation uses neither (1) nor division
by 11. The left-to-right binary loop starts with the identity; consuming
a bit doubles the exponent represented by the accumulator, and appending
the base for a one bit adds one. By induction on the consumed bits the
accumulator is the requested power. Formula (3) is valid under reduction
because it uses only sums and products. This explains the implementation
specialization, without reproving the imported general coding theorem.
All 25 word triples and all composed prefix powers agree with the lifted
offset route, at each square. Neither route divides by Delta.

For m=25:

| j | i | C_i | 2^{t_j} | 3^{u_j} | T_j | c_j |
|---:|---:|---:|---:|---:|---:|---:|
|0|8|8|1|1|8|8|
|1|1|16|23|2|11|22|
|2|2|5|7|18|5|18|
|3|3|11|17|1|12|11|
|4|4|7|21|17|24|5|
|5|5|21|17|24|18|22|
|6|6|4|6|17|8|8|
|7|12|19|6|18|2|16|
|8|0|5|19|3|10|16|
|9|9|2|21|16|22|20|
|10|10|3|1|3|9|18|
|11|11|5|19|18|10|23|
|12|7|2|1|1|2|16|
|13|13|14|1|18|2|1|
|14|14|12|6|1|22|15|
|15|15|15|17|16|5|20|
|16|16|5|16|16|5|0|
|17|17|1|18|7|1|18|
|18|18|21|2|9|3|6|
|19|19|6|23|4|2|14|
|20|20|5|16|19|20|4|
|21|21|16|24|13|17|11|
|22|22|15|7|12|10|19|
|23|23|21|12|14|3|4|
|24|24|19|6|1|14|20|

The unreduced sum of the 25 listed T_j is 245, hence Phi_pi=20 modulo 25.
The final composed triple is (17,20,22). Independently, using the full
integer exponents, 3^K=17 and 2^N=22 modulo 25; Delta=22-17=5.

For m=185761=431^2:

| j | i | C_i | 2^{t_j} | 3^{u_j} | T_j | c_j |
|---:|---:|---:|---:|---:|---:|---:|
|0|8|14705|1|183614|7735|14705|
|1|1|1509|149032|7471|183734|16262|
|2|2|15132|171978|176428|130263|135211|
|3|3|33418|148288|76730|166951|112090|
|4|4|116285|21554|12285|89569|27915|
|5|5|104846|121981|185223|123082|16651|
|6|6|161980|122853|89792|42213|145463|
|7|12|87|167234|110344|117960|144916|
|8|0|38328|173909|76575|92511|7865|
|9|9|125363|100136|168252|180905|162610|
|10|10|121954|30844|44474|37197|38729|
|11|11|31020|49568|2602|52868|165671|
|12|7|155865|100282|51587|130102|138111|
|13|13|176747|122984|40844|57362|77861|
|14|14|149734|76449|163255|14341|174200|
|15|15|40749|140508|171113|9716|161479|
|16|16|114609|130499|151904|36361|111412|
|17|17|124058|92023|52870|167449|120795|
|18|18|134058|50104|138892|74384|32503|
|19|19|32536|38683|153440|183808|14212|
|20|20|90832|96|128582|108572|131634|
|21|21|20998|146110|26292|151591|117889|
|22|22|160512|62067|138974|161865|124961|
|23|23|184336|70693|44429|78343|33281|
|24|24|74618|38799|1|18597|2586|

The unreduced sum of the 25 listed T_j is 2417479, hence Phi_pi=2586
modulo 185761. The final composed triple is (16917,2586,57431).
Independently 3^K=16917 and 2^N=57431 modulo 185761; their difference
is 40514. The large final tail enters Q_24 and 2^N in full, even though
u_24=0 and the tail does not alter C_24.

### Primality, exact valuations and reduced denominators

The valuation/divisibility and rational cancellation rules are the
previously inspected supporting results in
[Mathlib PadicVal.Basic, commit 2da3ab0a20dc0c66f56a557e37df39f7d36cb953](https://github.com/leanprover-community/mathlib4/blob/2da3ab0a20dc0c66f56a557e37df39f7d36cb953/Mathlib/NumberTheory/Padics/PadicVal/Basic.lean):
`padicValInt_dvd_iff` (lines 633–644), `padicValRat.defn` (181–200),
and `Rat.num_or_den_zero_padicVal` (342–350). The former requires a prime
base and treats zero separately; the rational formula requires a nonzero
rational represented by an integer numerator and denominator. It gives
the valuation difference, while coprimality of the reduced pair prevents
both reduced multiplicities being positive. Their complete proofs and
enclosing hypotheses were inspected in the saved assessment. These are
known cancellation rules, not new mathematical claims here.

The prime hypotheses are certified by complete trial division. For 5,
floor(sqrt(5))=2 and the remainder at divisor 2 is 1. For 431,
20^2<431<21^2 and the remainders at every integer divisor 2 through 20 are

```text
d:  2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
r:  1 2 3 1 5 4 7 8  1  2 11  2 11 11 15  6 17 13 11
```

All are nonzero. Every composite positive integer has a divisor between
2 and its square root, so both bases are prime. Both Phi_pi and Delta
were proved positive above. At p=5 their square residues are 20=4p and
5=p; at p=431 they are 2586=6p and 40514=94p. In each case both residues
are divisible by p and nonzero modulo p^2. Therefore, by the cited
divisibility rule, both integer valuations equal exactly one.

The nonzero rational Phi_pi/Delta has valuation 1-1=0 at each prime.
For its coprime reduced numerator and positive reduced denominator,
the cited coprimality rule says at least one multiplicity is zero; equality
of the multiplicities then makes both zero. Equivalently the gcd cancels
exactly one factor of each prime from both original integers. Hence the
reduced denominator and numerator contain neither tested prime. This
removes these two obstructions only; it does not test every denominator
factor or assert that the reduced denominator equals one.

### Certificate and verification limits

Reproduction command:
`python3 scripts/postspell-word-count/test_joint_witness_prime_squares.py`.
Full evidence is in
`scripts/postspell-word-count/joint-witness-prime-square-certificate.json`.
It retains the canonical input paths/hashes, all triples and counts, exact
order/swaps, positive/nonzero mathematical justifications, every trial
divisor, all lifted differences/quotients and both word triples, all 25
unreduced prefix/suffix exponents, weights, terms, previous/resulting states,
unreduced sums, denominator powers, all 223 comparisons and the empty
failure array. Both complete word/trace evaluations and the primality
evidence were inspected, not merely a preview. All 223 checks pass.

The actual and required bounded precision are both two. At this precision
the two denominator primes cancel completely; no higher-power test or
further order search is performed. These two implementations are within
this calculation, not a later independent critical audit. No permuted real
guards or actual integer/parity/exact-tail/primitive realization were checked.
Inherited source qualifications persist; no integer-cycle threshold is
applied to this rational root. The restricted exclusion through 24 words
and the universal eventual-descent gap are unchanged.

### Separate critical audit — 2026-10-12

The prior SPECIALIZE assessment
`drafts/literature/2026-10-12-joint-witness-two-prime-cancellation-audit.md`
approved this audit. Review of the complete statement, cited hypotheses,
generator, certificate and both written tables found no defect. This is
local REPRODUCTION verification of the existing negative diagnostic, not a
new theorem beyond the checked sources or an additional cycle exclusion.

The independent verifier is
`python3 scripts/postspell-word-count/audit_joint_witness_prime_squares.py`;
the complete evidence is
`scripts/postspell-word-count/joint-witness-prime-square-audit-certificate.json`.
It neither imports nor executes the original generator and preserves its
certificate. All 25 pairs are independently transcribed from L055 and
compared to that canonical table. The prescribed tails, unchanged totals,
two swaps and all four original input hashes agree. All parameters are
positive, so the positive-integral-offset argument above applies.

For independent arithmetic, use normalized affine pairs (alpha,beta) for
x -> alpha*x+beta over Z/mZ, m in {25,185761}. Since m is odd,
2 has inverse (m+1)/2. If f follows g, composition is
(alpha_f alpha_g, alpha_f beta_g+beta_f). Thus O and E are respectively
(3/2,1/2) and (1/2,0), using this unit. Compose the actual letter sequence
O,O,E,O, then raise it to J_i, follow it by O to the H_i and E to the a_i.
Right-to-left binary powering maintains base^remaining composed with the
accumulator equal to the desired original power. Transferring an odd bit,
squaring the base and halving the remaining exponent preserve the identity;
the identity accumulator also handles exponent zero. Within each call all
maps are powers of the same base, so they commute as needed by this invariant.

For a length-D word, multiplying both normalized coordinates by 2^D
recovers its integer numerator coefficients (A,C), with denominator 2^D.
The denominator is a unit modulo each m; this representation is therefore
equivalent to the integer affine reduction. It never divides by Delta or
presupposes actual parities. Recovery after every prefix independently
checks both previous and resulting triples in every stored transition.
Raw sums of the transcribed D_i,k_i give every full prefix/suffix exponent.
The separately recomputed lifted remainders and quotients give every closed
offset, which agrees with normalized letter composition. Every weighted
contribution, unreduced sum, total power and final triple agrees as well.
The original left-to-right powering loop is valid by its consumed-bit
invariant already stated above; the independent evaluator uses a different
representation and traversal.

Every original certificate key and scalar entry is compared, including all
223 original comparisons (names, actual and required values), the failure
array and summary. Both complete written 25-row tables match independent
output, as do all printed trial divisors and remainders. There are 4060
audit comparisons and zero failures. The original complete evaluation and
comparison fields, independent normalized words/prefixes, written tables,
exact positivity bounds and empty failure array were inspected in full.
The actual and required precision are both two. The sums remain 245 and
2417479, and the final triples remain (17,20,22) and (16917,2586,57431).

The nonzero denominator premise is also checked independently with exact
rational logarithm intervals. For x=2,3 and z=(x-1)/(x+1), use the lower
sum 2 sum_{j=0}^{63} z^(2j+1)/(2j+1). Its positive remainder is
2 integral_0^z t^128/(1-t^2) dt, strictly less than
2z^129/[129(1-z^2)]. Opposite interval endpoints give bounds for
N log2-K log3 strictly inside (10584/10^14,10585/10^14), with all rational
endpoints saved. Hence Delta>0. Positivity of every C_i and every weight
in (2) separately gives Phi_pi>0, so the rational input is nonzero.

Complete trial division through floor(sqrt(p)) proves both bases prime.
The nonzero square residues give v_5(Phi_pi)=v_5(Delta)=1 and
v_431(Phi_pi)=v_431(Delta)=1. Apply the cited valuation and reduced-pair
rules with these prime and nonzero hypotheses: the rational valuation is
zero, and at least one of its two reduced multiplicities is zero, hence
both are zero. The audit does not take the gcd of modular representatives
as a substitute for the gcd of the original integers. This verifies both
the reduced numerator and denominator conclusions.

Attempt 030's stop is confirmed. No new order, higher power, other factor
or permuted real-system guard was tested. The two primes cannot decide this
root's integrality; cancellation of every denominator factor, integer/parity/
exact-tail/primitive realization and an actual cycle do not follow. Other allocations and all
universal gaps remain open. The argument and its direct mathematical
inputs are unchanged; full matching Mathlib coverage and a Lean build
remain unchecked.

## Mathlib

The pinned supporting valuation/divisibility/coprimality results are cited
above with their hypotheses. Full matching coverage for this literal
allocation, its two residues and its certificate was not checked. Unknown
availability is not evidence of absence. No Lean build or formal verification
of this specialization is claimed.
