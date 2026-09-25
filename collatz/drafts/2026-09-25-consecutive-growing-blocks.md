# Consecutive growing-block test, 2026-09-25

## Gap, proposed target, and prior evidence

The main gap is universal eventual descent below every positive start greater
than 1. This step tests the existing checkpoint's proposed arithmetic
restriction on consecutive complete blocks. L001 concerns bounded shortcut
time; L002 gives exact single-block feasibility but does not establish
compatibility between successive blocks. Both results and their failed
attempts were inspected, and their work is preserved. There is no local
duplicate of the consecutive-block claim. No literature novelty is claimed.

The primary [MathPrize statement](https://mathprize.net/posts/collatz-conjecture/)
was rechecked on 2026-09-25 and still requires every positive integer to reach 1.

The intermediate target is an exact description of starts whose first K
complete blocks all have run lengths (a,b)=(2,1). A restriction bounding K
independently of the start could help an argument forcing compensation within
a fixed number of complete blocks, although other growing block patterns and
the total additive correction would remain unresolved. If every K is possible
for arbitrarily large starts, that proposed fixed-block descent mechanism
must be abandoned. The required sign is negative somewhere within the first K
blocks for every start outside a finite set; a growing endpoint and no earlier
descent refute it. A bound depending on the start would not meet that threshold.

## Saved reasoning to check

For a (2,1) block, L002 gives R(n)=(9n+5)/8, and its domain is n=11 modulo 16.
Translation by the affine fixed point suggests

\[
R(n)+5=\frac98(n+5).
\]

Thus K consecutive such blocks should be equivalent to
2^(3K+1) dividing n+5, with candidate endpoints

\[
n_j=9^j2^{3(K-j)+1}t-5\quad(0\le j\le K),
\qquad n_0=2^{3K+1}t-5.
\]

The proof must check both directions, exact maximality of every odd and even
run, positivity, and absence of descent at intermediate shortcut times. It
must distinguish arbitrarily long finite prefixes from one infinite positive
orbit. Multiplying t by an arbitrary modulus q may also keep all block
endpoints in residue -5 modulo q, testing whether a finite residue correction
could repair a bounded-block endpoint certificate.

The intended bounded check compares the formulas with direct shortcut
iteration and enumerates the first few complete residue periods. It is an
indexing and arithmetic check, not a convergence or density argument.

## Completed assessment

[L003](../lemmas/L003-consecutive-growing-blocks.md) proves the exact
equivalence, endpoint formula, and strict growth at every positive shortcut
time through the K blocks. There is exactly one residue class modulo
2^(3K+1), and it contains arbitrarily large positive starts. Thus finite
compatibility places no uniform upper bound on the number of repeated
growing blocks. For each fixed start, however, the exact repetition count
is floor((v_2(n+5)-1)/3). The sharp least possible start for K repetitions
is 2^(3K+1)-5. This size cost does not supply the uniform compensation
threshold or any subsequent descent estimate.

The q-scaled construction keeps all block endpoints in residue -5 modulo q.
Its corrected logarithmic change exceeds j log(9/8)>0 at every endpoint
1<=j<=K, whereas the proposed sufficient certificate requires a negative
change at one of them. The [failed attempt](../ATTEMPTS/003-bounded-complete-block-descent.md)
records this strengthened obstruction. The corrected-potential claim is
restricted to block endpoints; the plain size obstruction also covers
intermediate times.

The [direct-iteration check](../scripts/consecutive-blocks/check_prefix.py)
passed 37,448 odd starts in full residue periods, 2,048 parameterized
witnesses, and 384,036 shortcut transitions, with
[output](../scripts/consecutive-blocks/result.json) retained. These checks
include exiting the predicted maximal repeated prefix. They verify finite
arithmetic and indexing, not the unrestricted proof or universal convergence.

This one-turn test concludes NEGATIVE and leaves no unfinished calculation.
Stop fixed-block descent and finite residue corrections at block endpoints.
The exact loss of three powers of 2 from n+5 suggests a different mechanism:
an unbounded valuation correction to size. Such a correction falls outside
both finite-residue obstructions, but other block types may increase the
valuation and its global feasibility is unresolved. No complete candidate
proof or disproof exists. Consecutive exploration turns without an advance
or informative negative remain zero.
