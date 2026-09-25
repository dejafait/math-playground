# Mixed growing-word starting-size test, 2026-09-25

## Gap, intermediate target, and relevance

Universal eventual descent below each positive start greater than 1 remains
unproved. The intermediate target for this one step is a lower bound
g(K) tending to infinity for every positive start whose first K complete
blocks belong to {(2,1),(3,1)}. Such a bound would exclude infinite growth
confined to this alphabet. It would not control other block types, mixed
growth and contraction, or return below the original start.

The existing overview, DAG, lemmas L002–L004, attempt records, and history
were inspected. L003 settles a single repeated block type, while L004
refutes a correction depending only on v_2(n+5). Neither decides a uniform
starting-size bound for mixed words. All prior work is retained. The primary
[source](https://mathprize.net/posts/collatz-conjecture/) was rechecked on
2026-09-25 and still states the universal positive-integer target.

The concrete test is exact enumeration of all words of lengths K<=12,
using modular inverses rather than a cutoff on starting integers, followed
by independent shortcut iteration of the resulting representatives. Record
the minimum positive start for each length and test whether the sharp
single-type bound 2^(3K+1)-5 survives mixing. A finite counterexample would
abandon that particular bound. Continuing toward a weaker divergent bound
requires a concrete arithmetic invariant or inequality; growth of finitely
many computed minima or a density estimate alone is insufficient.

## Saved reasoning before calculation

L002 gives F_2(n)=(9n+5)/8 with domain n=11 modulo 16 and
F_3(n)=(27n+19)/16 with domain n=7 modulo 32. For a word
w=(a_1,...,a_K), a_i in {2,3}, put S_j=sum_{i<=j} a_i,
D_j=S_j+j, C_0=0, and

    C_j = 3^(a_j) C_(j-1) + (3^(a_j)-2^(a_j)) 2^(D_(j-1)).

The proposed endpoint is (3^(S_K)n+C_K)/2^(D_K). Its being odd suggests
the single residue

    n = 3^(-S_K)(2^(D_K)-C_K) modulo 2^(D_K+1).

The main proof obligation is that this final congruence forces every
intermediate block to have the prescribed maximal run lengths; mere
integrality of an affine composition must not be mistaken for legality of
the itinerary. Exact domains, positivity, the least positive representative,
and both directions of the congruence criterion need checking before the
enumeration can be interpreted.

This is one bounded discovery turn. No infinite-length claim or complete
candidate is asserted by the saved calculation.

## Saved assessment after the finite-word test

The first exact run checked all 8,190 nonempty words through length 12.
The minima are 7, 91, 603, 603, 15099, 56487, 1096359, 1096359,
5188263, 63613607, 108977319, 108977319. Thus the single-type formula
does not extend to mixing, and the minima need not strictly increase at
each length. These finite values do not decide whether the minima tend
to infinity.

The same affine calculation gives a narrower analytic target without
extrapolating these data. For a fixed word w, write its endpoint map as
(P n+C)/Q, with P odd, Q=2^D, P>Q, and C odd and positive. The integer
H_w(n)=(P-Q)n+C should satisfy

    H_w(R^K(n)) = (P/Q) H_w(n)

whenever this word is realized. Repeating it m times should therefore be
equivalent to 2^(mD+1) dividing H_w(n), by the finite-word congruence.
Since H_w(n)>0, this would give an exact finite repetition bound and rule
out eventual periodicity of an infinite itinerary in this alphabet.
The proof must establish sufficiency as well as the necessary valuation
loss. This bound is uniform in the repetition count for a fixed word;
it is not yet uniform over arbitrary words of a given total length.

## Completed assessment

[L005](../lemmas/L005-mixed-growing-word-congruences.md) proves the exact
residue criterion, including legality of all intermediate blocks, and the
proposed repetition criterion in both directions. The number of copies
is exactly floor((v_2(H_w(n))-1)/D). Thus an infinite itinerary in this
alphabet, if one exists, must be aperiodic after every starting position.
This is a restricted mathematical input, not universal eventual descent.

The achieved starting bound is n>=(2^(mD+1)-C)/(P-Q) for m copies of
one fixed w. The actual intermediate target needs a bound uniform over
all words of total length K. The coefficients vary with w, and applying
this inequality with m=1 even to w=(2,...,2) gives a right side tending
to -5. It therefore does not meet the requested threshold. The old sharp
single-type bound also fails for mixed words: the exact start 603 realizes
(2,3,2,2), below 8187. This failed transfer is preserved in the
[attempt record](../ATTEMPTS/005-single-type-bound-for-mixed-words.md).

The [script](../scripts/mixed-growing-words/check_words.py) and its
[output](../scripts/mixed-growing-words/result.json) retain all minima
and minimizing words through length 12. Direct iteration checked 24,570
representatives and lifts for 8,190 words, 4,368 odd starts in complete
common residue periods, and 7,905 fixed-word repetition cases, totaling
1,041,704 shortcut transitions. The repetition cases include the first
failed copy and long constructed prefixes. These are arithmetic checks;
the proof of eventual-periodic exclusion is independent of enumeration.

This one-step outcome is ADVANCE for the fixed-word repetition exclusion,
with zero consecutive exploration turns lacking an advance or informative
negative. The uniform least-start question remains open, and no complete
candidate exists. The two one-letter words give H_2(n)=n+5 and
H_3(n)=11n+19; together they identify concrete arithmetic information
for a later test of a potential on arbitrary switches between the types.
No successful potential or control of those switches is asserted here.
