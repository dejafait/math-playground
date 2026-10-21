# L066 — Prime-five nonintegrality of the changed-tail survivor

## Hypotheses

Use L055's complete literal J_i,H_i table, in index order 0,...,24,
with L065's tails a_23=20, a_24=166504394 and all other a_i=2.
The formal words are W_i=(OOEO)^{J_i}O^{H_i}E^{a_i}, where
O(x)=(3x+1)/2 and E(x)=x/2. Keep K=397573379, N=630138897.
Let n_0=s_0-23/11 be L064's exact unshifted cyclic root, as used
in L065. Actual integer parities or orbit realization are not assumed.
The prior SPECIALIZE assessment is
`drafts/literature/2026-10-13-survivor-prime-five-diagnostic.md`.

## Conclusion

For the complete chronological integer numerator Phi and denominator
Delta=2^N-3^K, Phi=21 and Delta=5 modulo 25. Their prime-five valuations
are respectively 0 and 1. The reduced denominator of n_0=Phi/Delta
therefore contains exactly one factor of 5, and n_0 is not an integer.
No actual positive integer cycle realizes this literal allocation.

This is a local REPRODUCTION of inspected affine/divisibility machinery,
not a new general theorem. L065's positive rational real-system witness
remains valid; other allocations, integer/parity/residue/exact-valuation
and primitive-orbit realization, unrestricted cycles, divergence and
universal eventual descent remain unresolved. The separate critical audit
below found no defect in this literal-allocation scope.

## Proof

### Imported formula and changed-coordinate applicability

Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational Collatz
cycles*, Acta Arithmetica 78 (1997), 227–239, DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf),
supplies chronological integer affine composition and its unique fixed
point for a nonempty binary word with nonzero denominator. The prior
assessment inspected the statement and essential proof cases. We import
only formal affine identities, with later maps on the left; rational
parity claims and integer-itinerary sufficiency are unused. No general
coding reproof is needed. L056 supplies the compressed offset

\[
k_i=3J_i+H_i,\quad D_i=4J_i+H_i+a_i,\quad A_i=3^{k_i},\quad Q_i=2^{D_i},
\]
\[
F_i=\frac{23\,3^{H_i}(27^{J_i}-16^{J_i})}{11}
       +(3^{H_i}-2^{H_i})16^{J_i},\qquad
W_i(x)=(A_i x+F_i)/Q_i.
\tag{1}
\]

All F_i are positive integers: J_i,H_i>0 and 27>16, 3>2 give
positivity; 27=16 modulo 11 gives integrality. Even tails change D_i,
not F_i. Set t_i=sum_{j<i}D_j and u_i=sum_{j>i}k_j. The imported law gives

\[
\Phi=\sum_{i=0}^{24}F_i2^{t_i}3^{u_i},\qquad
W(x)=(3^Kx+\Phi)/2^N,\qquad \Delta=2^N-3^K.
\tag{2}
\]

The complete table and actual tails have sums J=66061058, H=199390205,
a=166504460, hence sum k_i=K and sum D_i=N. L064 supplies
0<Lambda=N log2-K log3, so Delta>0. Also Phi>0 by (2).
Thus the source nonempty-word and nonzero-denominator hypotheses hold.

For the explicit coordinate match, write P_i for L064's prefix product
called C_i there, and retain its c_i=A_i/Q_i and eta_i. Multiplying
its eta_i by A_i yields

\[
A_i\eta_i=
(23\,3^{3J_i+H_i}-12\,3^{H_i}16^{J_i}-11\,2^{H_i}16^{J_i})/11=F_i.
\]

Therefore the exact unshifted endpoint n_(i+1)=c_i(n_i+eta_i)
is precisely (1) at every index. With B=sum eta_i/P_i, and
P_i=3^{sum_{j<i}k_j}/2^{t_i}, each term satisfies

\[
3^K\eta_i/P_i=F_i2^{t_i}3^{u_i}.
\]

Summing gives Phi=3^K B and hence
Phi/Delta=B/(2^N/3^K-1)=n_0=s_0-23/11.
This match includes D_23=144041977 and D_24=323168131; in particular
t_24=306970766, not the old-tail prefix. No shifted-root integrality
or old allocation numerator residue is transferred.

### Complete finite evaluation

All following entries are least nonnegative residues modulo 25.
Here 11 has unit inverse 16. Reduce (1) with that inverse and evaluate
the full integer exponent sums in (2). Never invert Delta.

| i | F_i | 2^{t_i} | 3^{u_i} | contribution |
|---:|---:|---:|---:|---:|
|0|5|1|7|10|
|1|16|9|14|16|
|2|5|6|1|5|
|3|11|11|7|22|
|4|7|18|19|19|
|5|21|11|18|8|
|6|4|23|19|23|
|7|2|23|8|18|
|8|8|23|24|16|
|9|2|4|3|24|
|10|3|24|24|3|
|11|5|6|19|20|
|12|19|24|1|6|
|13|14|1|18|2|
|14|12|6|1|22|
|15|15|17|16|5|
|16|5|16|16|5|
|17|1|18|7|1|
|18|21|2|9|3|
|19|6|23|4|2|
|20|5|16|19|20|
|21|16|24|13|17|
|22|15|7|12|10|
|23|21|12|14|3|
|24|19|14|1|16|

Every row is specified by (1)–(2) and the complete L055 table with the
stated changed tails. For example, the final row has J=30998279,
H=32670621, t_24=306970766, u_24=0, so the two powers are 14 and 1,
the offset is 19, and the contribution is 16. The representatives sum
to 296, proving Phi=21 modulo 25. The power periods 2^20=3^20=1
modulo 25 and (N mod20,K mod20)=(17,19) give
2^N=22 and 3^K=17, proving Delta=5 modulo 25.

Reproduce the full certificate with
`python3 scripts/postspell-word-count/test_survivor_prime_five.py`.
Evidence is `scripts/postspell-word-count/survivor-prime-five-certificate.json`.
It retains source hashes, all parameters, complete prefix/suffix exponents,
25 offsets/contributions and both triples for each row, all chronological
composition states, comparison operands, actual/required modulus and failures.
All 38 comparisons pass; the full trace, comparison list and empty failures
were inspected. Required and actual precision are both modulus 25;
no new order, other modulus, factor search or guard calculation occurs.

The second evaluation uses division-free triples. For (A,F,Q) followed
by (B,G,R), the imported law gives (BA,BF+QG,RQ).
Build OOEO by the four single-letter triples (3,1,2),(3,1,2),(1,0,2),
(3,1,2), obtaining (27,23,16); raise it to J_i, O to H_i and E to
a_i by binary composition. In each powering call, accumulated power
followed by current base to the remaining exponent equals the originally
requested power. Odd-bit accumulation, squaring and halving preserve
this invariant, since all these factors are powers of one map. Thus
this evaluates the entire word without expanding or sampling it.
Modular reduction respects the additions and multiplications. Every
resulting row agrees with (1); full composition gives (17,21,22),
agreeing with the independent weighted sum and total powers.
These are two implementations within this attempt, not a separate audit.

### Nonintegrality and exact surviving factor

The prime 5 is prime, and both integers are nonzero as proved above.
Phi=21 modulo 25 implies 5 does not divide Phi; Delta=5 modulo 25
implies v_5(Delta)=1. The cancellation rule used in L058 has precise
support in [Mathlib PadicVal.Basic, commit 2da3ab0a20dc0c66f56a557e37df39f7d36cb953](https://github.com/leanprover-community/mathlib4/blob/2da3ab0a20dc0c66f56a557e37df39f7d36cb953/Mathlib/NumberTheory/Padics/PadicVal/Basic.lean),
`padicValRat.defn`, `padicValInt_dvd_iff` and
`Rat.num_or_den_zero_padicVal`; the reused assessment inspected their
statements/proofs and nonzero qualifications. Reduction cancels the
smaller prime multiplicity, here zero, so the reduced denominator has
valuation exactly one at 5. Equivalently, if Phi/Delta were an integer m,
Phi=m Delta would force 5 to divide Phi, a contradiction.

Any actual integer cycle with this literal formal word would satisfy
W(n)=n, forcing n=Phi/Delta by Delta!=0. Consequently it cannot exist.
No converse asserting that a rational root realizes the word is required.
The proof applies no primitive integer-cycle threshold to reals and
supplies no claim about other allocations or universal descent.

### Independent critical audit — 2026-10-13

The prior SPECIALIZE assessment
`drafts/literature/2026-10-13-survivor-prime-five-critical-audit.md`
authorizes this exact audit. The written proof and complete finite evidence
were independently checked, with no defect found. This is REPRODUCTION
of the existing local exclusion, not a new mathematical obstruction.

The input audit checks all 25 J,H rows against L055 and the exact tail
statement against L065. All three original source hashes match current
L055, L064 and L065 byte for byte. The original certificate and generator
are preserved; their hashes are retained in the audit certificate.
In particular D_23=4*16452748+78230965+20=144041977,
D_24=4*30998279+32670621+166504394=323168131,
and t_24=306970766. The sum t_24+D_24 gives N=630138897.
The full totals, not just these final rows, are checked.

The coordinate review uses L064's definitions in its exact-root passage.
Substitution gives A_i eta_i=F_i as displayed above: combining the two
16^{J_i} terms in (1) changes -23/11+1 to -12/11. Since
P_i=3^{sum_(j<i)k_j}/2^{t_i} and eta_i=F_i/3^{k_i}, the expression
3^K eta_i/P_i removes exactly the prefix and current odd exponents,
leaving u_i. Thus each
summand of 3^K B equals its summand in Phi. L064's root formula then
gives Phi/Delta=n_0=s_0-23/11. The changed tails enter every relevant
prefix and the closing product; none enters F_i. L064's already audited
bound 10584/10^14<Lambda<10585/10^14 applies to the unchanged K,N,
so Delta>0. Every F_i is a positive integer and all weights are positive,
so Phi>0. No H guard, seed, parity or integer-cycle bound is needed here.

Reproduce the independent arithmetic audit with
`python3 scripts/postspell-word-count/audit_survivor_prime_five.py`.
Its full certificate is
`scripts/postspell-word-count/survivor-prime-five-audit-certificate.json`.
It uses homogeneous matrices [[A,F],[0,Q]], acting on the projective
coordinate x as (Ax+F)/Q. Ordinary matrix multiplication therefore places
the later map on the left. It builds OOEO as O*E*O*O and each complete
word as E^a*O^H*(OOEO)^J. Left-to-right binary powering maintains
acc=base^(processed binary prefix): the next bit b replaces acc by
acc^2*base^b. This differs from the original generator's right-to-left
triple powering. That original implementation also has a valid invariant:
if the accumulated exponent is r, the current base exponent is q and
the remaining exponent is e, then r+qe is the original exponent.
Accumulating an odd bit and replacing q,e by 2q,floor(e/2) preserves it.
All factors in one powering call are powers of the same map. Both
implementations retain the order between different maps.

For an independent compressed-offset check, let R be the least residue
of 23*3^H*(27^J-16^J) modulo 275. Its integer numerator is divisible
by 11, so R is too, and their quotients differ by a multiple of 25.
Thus R/11 is the required quotient residue without using a modular
inverse. Adding the other term in (1) evaluates F_i. Scalar powers are
computed from complete unit cycles by successive multiplication, whereas
the original uses modular pow. The lift 275 serves only exact division
at modulus 25; it tests no additional denominator factor or precision.

All 125 audit comparisons pass with empty failures. They reconcile every
original certificate field, including all parameters, all 25 complete
trace records, the 38 original comparisons with both operands, every
written table entry, source hashes and summary. Complete traces, lifted
division values, word/accumulated matrices, reconstructed comparisons,
written table and failure lists were inspected. The contributions sum
to 296, and the final matrix has triple (17,21,22). The checked periods
2^20=3^20=1 modulo 25 and the full count residues give Delta=22-17=5.
The original inverse check 11*16=1 modulo 25 is also correct.

Finally, the nonzero premises above permit the cited valuation rule.
The residues imply v_5(Phi)=0 and v_5(Delta)=1. Their gcd has no factor
5, so exactly one factor 5 survives in the reduced denominator.
Alternatively, an integer root would give Phi=n_0 Delta, contradicting
these residues. Actual integer closure implies this formal fixed-point
equation, without requiring its converse. This confirms only L066's
literal allocation; L065's rational witness, earlier order/factor stops
and every universal gap remain intact. No dependency or theorem
statement changes are required, and Mathlib limitations remain unchanged.

## Mathlib

The pinned source supports prime valuations and coprime rational reduction.
Full matching coverage of this specific allocation and its finite evaluation
was not checked. No Lean build or formal verification of the certificate
was performed; supporting declarations do not formalize this tuple.
