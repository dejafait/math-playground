# Target and conventions

Source checked on 2026-09-24 and rechecked on 2026-09-25: [MathPrize, Collatz conjecture](https://mathprize.net/posts/collatz-conjecture/), the page dated 2021-07-07. Its mathematical statement agrees with local GOAL.md. Prize adjudication is separate and is not part of this notebook's correctness criterion.

For positive integers define

\[
C(n)=\begin{cases}n/2&2\mid n,\\3n+1&2\nmid n.\end{cases}
\]

The exact target is

\[
\forall n\in\mathbb Z_{>0}\quad\exists k\in\mathbb Z_{\ge0}\quad C^k(n)=1.
\]

The time zero convention includes the starting value 1. A disproof must give a positive integer whose orbit is rigorously shown never to reach 1 (for example, a proved cycle avoiding 1); a long finite excursion is insufficient.

For the descent test use the shortcut map

\[
T(n)=\begin{cases}n/2&2\mid n,\\(3n+1)/2&2\nmid n.\end{cases}
\]

Each even shortcut step is one C step; each odd shortcut step is two C steps, since 3n+1 is even. Thus T iterates form a subsequence of C iterates. The only omitted states are 3n+1 for positive odd n, all at least 4, so an occurrence of 1 cannot be omitted. Consequently reaching 1 under T and under C are equivalent. The T cycle through 1 is 1,2; the C cycle is 1,4,2. Throughout, log means the natural logarithm.

Universal strict descent below the starting integer, with an unbounded time allowed, would suffice: if for every n>1 some T iterate is smaller than n, strong induction proves that every n reaches 1. Conversely reaching 1 gives such descent. This is a target-equivalent criterion, not an established mathematical input.

## Mathlib

Coverage: **not checked** for these Collatz conventions or the full target. The shortcut equivalence is proved above; no library theorem is assumed.
