# Shifted-valuation potential test, 2026-09-25

## Gap, intermediate target, and relevance

The unresolved claim is universal eventual descent below every positive
start greater than 1. The checkpoint proposes testing
V_c(n)=log(n+5)+c v_2(n+5), with one constant c>0, for strict decrease on
every complete maximal odd-even block from odd n>1, or outside a finite
exception set. This is a new test: L001 and L003 exclude finite residue
corrections, while v_2(n+5) is unbounded. L002 supplies the exact complete
block map. The existing lemmas, attempts, and latest working notes were
inspected; they contain no result deciding this correction. All prior work
is retained, and no literature novelty is claimed.

If such a positive c existed, V_c would have finite sublevel sets on odd
positive integers, since V_c(n)>=log(n+5). Strict decrease at each block
outside a finite set would force entry to that set; proving its members
converge would remain necessary. This would address the main gap through a
termination certificate. The source statement was rechecked at
[MathPrize](https://mathprize.net/posts/collatz-conjecture/) on 2026-09-25;
it retains the universal positive-integer target.

The discriminating test is the exact sign of

\[
\Delta_c(n)=\log\frac{R(n)+5}{n+5}
 +c\bigl(v_2(R(n)+5)-v_2(n+5)\bigr).
\]

L003 gives log(9/8)-3c on a (2,1) block, requiring
c>log(9/8)/3. This local compensation is insufficient unless every other
block also has negative increment. A family of growing blocks with unchanged
valuation would defeat every c, and even every correction depending only on
that valuation. A growing family with increasing valuation would directly
defeat positive c. If either exists above every cutoff, stop this potential
route. Only an exact compatible global inequality would justify continuing
toward a proof using this form.

## Saved reasoning before verification

For a block with (a,b)=(3,1), write n=32t+7 (t>=0). L002 suggests
R(n)=54t+13. Then n+5=4(8t+3) always has valuation 2, whereas
R(n)+5=18(3t+1) has valuation 1+v_2(3t+1).

In particular t=4s+3 should give
n=128s+103, R(n)=216s+175, and valuation 2 at both endpoints. These
arbitrarily large witnesses would make every valuation-only correction
cancel, leaving positive logarithmic growth. The subfamily t=4s+1 should
instead give n=128s+39, R(n)=216s+67 and endpoint valuation at least 3.
The proof must check exact maximal run lengths, both valuations, positivity,
and a quantitative increment against the required negative sign.

The finite check will compare these formulas with direct shortcut iteration,
including at least one full residue period, and use integer comparisons for
the logarithmic ratio bounds. It will not test convergence or substitute
sampling of c for an unrestricted argument.

## Completed assessment

[L004](../lemmas/L004-shifted-valuation-potential-obstruction.md) proves both
families and the exact domain n=7 modulo 32 for (3,1) blocks. On the
valuation-preserving family, every F(v_2(n+5)) cancels and the increment is
at least log(5/3)>0. This is incompatible with the required negative sign
for every c, including the range c>log(9/8)/3 that works on (2,1) blocks.
The second family has increment at least log(18/11)+c for c>0 and permits
unbounded valuation gains. Finite exceptions cannot help because both
families have unbounded starts. The obstruction concerns one block; it
does not establish an infinite growing orbit or exclude later compensation.

The [direct-iteration check](../scripts/shifted-valuation/check_potential.py)
passed 8,192 odd starts across 512 residue periods and 568 parameterized
witnesses, totaling 35,038 shortcut transitions. Its
[output](../scripts/shifted-valuation/result.json) records the checks, which
use exact integer ratio comparisons and include valuation gains up to 65.
The unrestricted conclusions follow from the proof, not from these counts.

This one-turn test concludes NEGATIVE and stops potentials of this form
that must decrease at every block. There is no unfinished calculation or
complete candidate proof. Consecutive exploration turns without an advance
or informative negative remain zero. The
[attempt record](../ATTEMPTS/004-shifted-valuation-potential.md) preserves
the scope of the failure.

The result motivates a different question about the starting-size cost of
mixed growing block words. L003 gives a sharp exponentially growing least
start for a single repeated block type, whereas this step shows why one
valuation does not track all growing types. A lower bound tending to infinity
uniformly over words in (2,1) and (3,1) would rule out an infinite trajectory
confined to this restricted alphabet. It is not established here, need not
bound the word length independently of the start, and would still leave
other block types and compensation across growing and contracting blocks
unresolved. This is a reason for bounded discovery, not a claim that a route
to universal descent has been found.
