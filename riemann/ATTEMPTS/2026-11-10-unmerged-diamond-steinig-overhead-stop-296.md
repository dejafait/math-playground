# Unmerged Diamond–Steinig overhead at linear order

10 November 2026. The approved test asked whether the exact unmerged
coefficient mass at nu=n has zero exponential limsup rate. The test
is negative: [L998](../lemmas/L998-unmerged-diamond-steinig-mass-exponential-lower-bound.md)
proves a strictly positive lower rate log(9/4)/3 using an admissible
single coefficient for every n divisible by three. Both partition
families and all source factorial weights are retained.

WHY IT FAILS: taking absolute values before collection incurs an
exponential coefficient cost. Therefore this representation does not
automatically preserve arbitrary subexponential termwise error budgets
toward L984(H). This is a coefficient obstruction only: it supplies no
lower bound for actual signed arithmetic errors and excludes neither
compensating factor estimates nor cancellation before collection.
The source's exponential upper bound alone had not settled this test;
the new lower bound does. Preserve all older stops. Any continuation
must introduce an independently testable cancellation mechanism or
different arithmetic input; repeating the unmerged test needs new input.
