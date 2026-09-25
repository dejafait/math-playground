# Maximal odd-even block descent audit, 2026-09-25

## Gap, scope, and prior work

The gap is universal eventual descent below each positive start greater than 1.
This step follows the saved checkpoint: replace a fixed number of shortcut
steps by a block containing the entire initial odd run and all the even steps
immediately following it. Such a block may have unbounded length, so L001 does
not already refute descent at its endpoint. The existing lemma, failed attempt,
and unfinished notebook changes were inspected and are preserved. There is no
local result for this block map. No claim of literature novelty is intended.

The primary [MathPrize statement](https://mathprize.net/posts/collatz-conjecture/)
was rechecked on 2026-09-25 and still concerns every positive integer reaching 1.

## Intermediate target and discriminating test

Write an odd start uniquely as n=2^a u-1 with a>=1 and u positive odd. Derive
the first even iterate, the length b of the following even run, and the next
odd endpoint R(n). Seek the exact condition R(n)<n, and test whether the
arithmetic relation defining b forces that inequality for all sufficiently
large odd starts. If it does, convergence of the finite exceptions would
complete a strong-induction route. If arbitrarily large noncontracting blocks
exist, stop the every-block contraction proposal and identify the missing
compensation between successive blocks. Even starts already descend in one
shortcut step. An average contraction or merely a leading multiplier below 1
does not meet the exact endpoint inequality.

The bounded test will compare the symbolic formula with direct shortcut
iteration and use congruences, rather than sampling alone, to determine which
run-length pairs (a,b) can occur. Any claimed unrestricted result requires a
proof including maximality of both runs and the additive term in R(n).

## Saved reasoning to check

Candidate first even iterate: 3^a u-1. Candidate b: v_2(3^a u-1), and candidate
endpoint R(n)=(3^a u-1)/2^b. Algebra suggests the exact strict-descent condition
(2^(a+b)-3^a)u>2^b-1. The checks needed were the borderline starting value 1,
signs, and whether arbitrary prescribed positive a,b are possible by solving
one congruence for odd u modulo 2^(b+1).

## Completed assessment

[L002](../lemmas/L002-maximal-odd-even-block-descent.md) proves the endpoint
formula, exact maximality of both runs, and the descent condition. The
positive additive term (3^a-2^a)/2^(a+b) in R(n) is retained. Strict descent
requires b>a log_2(3/2), with the full inequality above controlling the
additional correction. Yet every positive pair a,b is attained infinitely
often: multiplication by odd 3^a is invertible modulo 2^(b+1). In particular,
b=1 is possible for arbitrarily large a, producing unbounded leading growth
multipliers instead of the required contraction.

The explicit family n=16t+11 has run lengths (2,1) and endpoint 18t+13. Its
positive difference 2t+2 contradicts the required negative difference for
arbitrarily large starts. The odd part increases and the even part decreases
to this endpoint, so these starts do not descend anywhere within the block.
No finite exception cutoff repairs the every-block proposal.

The [direct-iteration check](../scripts/maximal-block/check_block.py) passed
21,482 parameter cases and 703,428 shortcut transitions; its
[output](../scripts/maximal-block/result.json) includes contracting, expanding,
and equality examples. The grid is deliberately parameterized by a,u and is
not a density estimate. It checks the proof's algebra, not universal
convergence. Mathlib coverage remains explicitly not checked.

This one-turn assessment concludes NEGATIVE and leaves no unfinished
calculation. Stop automatic contraction during the first complete block.
The result determines single-block feasibility only; it establishes no
independence or compensating behavior for successive run lengths. An
argument using several blocks must address which expanding blocks can occur
consecutively. The affine map for (2,1) supplies a concrete way to test a
bounded number of such blocks. No complete candidate proof or disproof is
proposed, and this negative result resets consecutive exploration turns to
zero.
