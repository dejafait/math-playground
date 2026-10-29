# C103b — Conditional d35 full-simplex actual-word exclusion

## Hypotheses

Let T(n)=n/2 for even positive integers and T(n)=(3n+1)/2 for
odd positive integers. Letters O and E prescribe actual input parities
for T. Take all 25 indexed pairs (J_i,H_i) in the literal order of
L055's table, changing only H_0=40 to 5 and H_24=32670621 to
32670656. Use no other assertion of L055.

Let b_0,...,b_24 be nonnegative integers with sum b_i=B=9250245
and b_0=0. Set

\[
a_i=2+18b_i,\quad W_i=(OOEO)^{J_i}O^{H_i}E^{a_i},\quad
D_i=4J_i+H_i+a_i,\quad q_i=\sum_{j<i}D_j,\quad N=q_{25}.
\]

Suppose W_0...W_24 is actual at a positive odd integer n_0>1
and T^N(n_0)=n_0. Define n_i=T^{q_i}(n_0) for 0<=i<=25.
Require each junction n_i, 0<=i<25, to be positive odd and
congruent to 20 modulo 27, and require every final even tail to be
exact. Thus n_25=n_0. Repeated periods and coincident junctions are
allowed. No minimum, seed, primitive-period, first-return or ordering
of heights is assumed. All logarithms below are natural.

## Conclusion

No such closed actual concatenation exists for any allocation in the
entire stated integer simplex conditional on b_0=0.

This is a local RESEARCH/REPRODUCTION specialization under the prior
SPECIALIZE assessment
`drafts/literature/2026-10-25-c103a-conditional-actual-word-transfer.md`.
It applies existing mathematics to a restricted language; it claims
no discovery beyond the inspected sources. Its separate step482 critical
audit below found no defect within these hypotheses, relative to the
audited inputs. It is not a complete Collatz candidate.

## Proof

Suppose such a concatenation exists. Keep its literal cut, all indexed
pairs, the allocation and each individual tail fixed. The full table
has minimum J equal to 8. After the two H changes its minimum H is
5, and every other H is at least 72. Thus J_i>=2 and H_i>=3
at every row. Nonnegative integrality gives a_i>=2 and
a_i congruent to 2 modulo 18, without any restriction on how many
coordinates have positive budgets.

The time intervals [q_i,q_{i+1}) partition the given chronological
word. Consequently W_i is actual at n_i, and its output is precisely
n_{i+1}; for i=24 this is n_25=n_0, also positive odd. This is
L041's represented actual-word setting with r=25. Use only its
occurrencewise necessities, not its length bound, global cycle bounds,
cyclic minimum choice or seed. Those finite necessities apply to
arbitrary independent exact tails a_i>=2 at the original cut.

Put kappa=23/11 and s_i=n_i+kappa for 0<=i<=25. If a positive
integer n_i=20+27k is odd, then k is an integer with k>=0 and
odd; hence k>=1 and n_i>=47. Therefore

\[
s_i\ge540/11>0\quad(0\le i<25),\qquad s_{25}=s_0.
\tag{1}
\]

At row i let y_i=T^{4J_i}(n_i) and
z_i=T^{4J_i+H_i}(n_i). L041's section "Each occurrence's own
prefix and the transfer to the next" gives

\[
y_i+1=(27/16)^{J_i}s_i-12/11,\qquad
z_i=(27/16)^{J_i}(3/2)^{H_i}s_i
       -(12/11)(3/2)^{H_i}-1,\qquad
n_{i+1}=z_i/2^{a_i}.
\tag{2}
\]

Define G_i=(27/16)^{J_i}(3/2)^{H_i} and
Q_i=(12/11)(3/2)^{H_i}+1, exactly as in C103a. Adding kappa
to the final identity in (2) yields

\[
s_{i+1}=2^{-a_i}(G_i s_i-Q_i)+\kappa
\quad(0\le i<25).
\tag{3}
\]

Both negative terms are inside the tail division and the shift is
outside. Every row is retained, including row24's closing equation.
The identities use the assigned a_i individually, not just their sum.

The same L041 occurrencewise passage supplies the necessary guards

\[
4J_i\log2\le\log s_i+\log(11/4),\qquad
2^{H_i}\le y_i+1<(27/16)^{J_i}s_i.
\tag{4}
\]

Its arbitrary-tail necessity argument uses the actual identity
2^{H_i}(2^{a_i}n_{i+1}+1)=3^{H_i}(y_i+1), with a_i>=2,
odd output and H_i>=3; it imposes no upper bound on a_i or
condition on other rows' budgets. Thus it applies here also when
b_i=0. All members of the second chain in (4) are positive.
Strict monotonicity and the product rule for the logarithm give

\[
H_i\log2<\log s_i+J_i\log(27/16).
\tag{5}
\]

The strict sign comes from the positive 12/11 subtraction in (2),
not from changing the non-strict first comparison in that chain.
The J guard in (4) stays non-strict. Both guards use row i's
own input s_i.

Now apply audited C103a to this single real tuple (s_0,...,s_25).
Its indexed data are identical. The original nonnegative integer
allocation still has sum B and b_0=0, with exactly the tails
a_i=2+18b_i. Equation (1) is its lower domain and closure;
(3) is its entire endpoint system; (4)'s J guard and (5) are
its two guard families with the required signs. Every premise matches
without rotating, changing a coordinate, projecting to a different
tail allocation, or adding a minimum or seed. C103a says no such
tuple exists, which is the required contradiction.

This substitution covers every permitted allocation at once. Any
zero budget gives tail2 and leaves the occurrence, its equations and
guards in place. In particular, if b_24=0 then a_24=2 and
n_25=n_0 is still odd, so the imported arbitrary-tail necessity and
closing equation apply. Full budget on a single row j in 1,...,24
also meets the same premises; full budget on row0 is outside the
explicit b_0=0 hypothesis. Repeated periods or coincident junctions
leave the 25 chronological intervals distinct as occurrences; neither
L041's local necessities nor C103a requires distinct junction values.
No boundary or allocation within the stated simplex is omitted.

### Sources, overlap and qualifications

L041 supplies the occurrencewise identities and necessary guards;
L055 supplies only its table; audited C103a supplies the conditional
real-system exclusion. This is a hypothesis specialization, requiring
no reproof of the general finite affine theorem or certificate replay.
The precise upstream finite affine reference is Halbeisen–Hungerbuehler,
*Optimal bounds for the length of rational Collatz cycles*, Acta
Arithmetica 78 (1997), 227–239, DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp.228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
Its finite-word affine machinery is imported through L041 and the
audited real-system inputs. No parity-coding or realization converse
is used. The analytic qualifications of C103a and its audited inputs
are unchanged; no external formal verification is claimed.

The prior assessment checked known results, duplicates and recorded
failures. C101b is the narrower last-pair application, not an exclusion
input for this expanded support domain. Attempt032's failed sufficient
package and both d0 witnesses supply no premise and remain preserved.
No argument here establishes b_0=0, the residue/exact-tail language,
this literal table or an entry/order reduction for arbitrary cycles.
Row0 support, order exhaustion, entry, other tables, unrestricted
cycles, divergence and universal eventual descent remain unresolved.

### Independent critical audit — 2026-10-25, step482

This RESEARCH/REPRODUCTION proof audit uses the unchanged prior SPECIALIZE
assessment `drafts/literature/2026-10-25-c103b-actual-word-transfer-critical-audit.md`.
It checks the complete C103b statement and proof against L041's hypotheses,
word-local proof and corresponding audit, all 25 L055 pairs, and C103a's
complete statement and step478 audit. C103a's analytic exclusions remain
imported from its audited inputs; this is not a fresh certificate replay
or a reproof of the primary affine theorem cited above.

**Data, occurrences and original cut.** Inspection of the complete table
confirms integer J_i>=8. Changing only H_0 to 5 and H_24 to 32670656
leaves H_i>=3 at every index (all H_i for i>0 are at least 72).
The allocation gives integer a_i>=2 with a_i congruent to 2 modulo 18.
Thus r=25 and every local parameter satisfy L041's hypotheses. Each
D_i is positive; the cumulative q_i specify distinct consecutive time
intervals, even if their endpoint values coincide. Actuality of the
concatenation supplies the required parities on every such interval.
The final output n_25=n_0 is odd and positive just like every other
output. No inference about a least period or distinct values is needed.

L041 introduces a minimizing cyclic relabeling in its separate seed
argument. That choice is not an input to the later occurrencewise
identities: the displayed derivation uses only the current word's
J,H,a,n_i,n_{i+1} and actual parities. Its valuation argument and its
own-word audit are independent of any ordering of the n_i. Hence these
necessities apply with the literal indexing here. In particular neither
L041's seed nor L055's original-table minimum is silently imported.

**Lower domain and all endpoints.** Positivity in n_i=20+27k forces
k>=0, and oddness forces k odd, so k>=1. Thus n_i>=47 and
s_i>=47+23/11=540/11. The same shift at both ends gives s_25=s_0.
L041's exact prefix and tail identities give (2) at each original
occurrence. Expanding the endpoint required by C103a gives

\[
2^{-a_i}\bigl((27/16)^{J_i}(3/2)^{H_i}s_i
 -(12/11)(3/2)^{H_i}-1\bigr)+23/11.
\]

This is precisely n_{i+1}+23/11 from (2), not an upper bound on it.
Both negative terms remain divided by the assigned 2^{a_i}; the outer
shift is unchanged. This comparison includes i=24 and does not replace
the individual tails by their total budget.

**Guard hypotheses and signs.** To check the arbitrary-tail premise
explicitly, in L041's identity
2^H(2^a n_{i+1}+1)=3^H(y+1) the factor 2^a n_{i+1}+1 is
odd for every allowed a. Thus v_2(y+1)=H and y+1=2^H u with
u positive odd. For H>=3 the integer 11*2^(H-2)u+3 is odd,
so 11y+23=4(11*2^(H-2)u+3) has valuation exactly 2.
The affine identity in the inspected L041 passage then gives
v_2(11n_i+23)=4J+2. Positivity implies
11s_i=11n_i+23>=2^(4J+2), which is exactly the non-strict
J guard after taking logarithms. No strictness is added at equality.

Also u>=1 gives 2^H<=y+1. The identity
y+1=(27/16)^J s_i-12/11 gives the strict upper comparison,
since 12/11>0. All quantities being logged are positive. Consequently
H log2<log s_i+J log(27/16), exactly the strict H guard of
C103a, at this outgoing row's own input. Equality in the first
comparison does not affect this strict conclusion. This checks the
imported necessity argument rather than asserting a coding converse.

**Full domain and boundary check.** C103a requires real coordinates;
the shifted integer coordinates satisfy that requirement without any
extra realization assertion. Its data, nonnegative integer allocation,
sum B, b_0=0, lower domain, closure, all endpoints and both guard
families have now been matched on one unchanged tuple. There is no
support restriction on this application of C103a.

For any b_i=0, a_i=2 still satisfies every checked hypothesis; the
word and its guard are not deleted. This includes b_24=0, where the
closing identity has divisor 4 and odd output n_0. The full budget on
any one row j=1,...,24 gives a_j=166504412 and all other tails 2;
the argument has no upper-tail assumption and includes each of these
allocations. Full budget on row0 is excluded by the explicit b_0=0
premise, and an all-zero allocation cannot have the required positive
sum B. Arbitrary multiple recipients are covered by the quantified
rowwise argument. Repetitions and coincident junctions do not alter any
premise of the real exclusion or the time-interval argument.

**Verdict and limitations.** The contradiction with audited C103a is
valid for exactly C103b's stated conditional actual-word class. No
repair, narrowing, new premise or dependency change is necessary.
The direct inputs remain L041, L055 (table only) and C103a, as recorded
in DAG.md. C101b is only a narrower precedent, and Attempt032 and the
d0 witnesses supply no premise. This audit secures the existing local
application; it establishes neither b_0=0 nor an entry or language
reduction for arbitrary cycles. Row0 support, order exhaustion,
unrestricted cycles, divergence and universal descent remain open.
The argument is unchanged, so PROOF.md and DAG.md are unchanged; this
canonical verdict supersedes PROOF.md's pending-audit wording for C103b.

## Mathlib

Full matching coverage for this actual-word specialization is unchecked,
not known absent. Supporting affine, valuation or logarithm facts do
not alone constitute a matching theorem. No Lean verification or
external Lean build is claimed.
