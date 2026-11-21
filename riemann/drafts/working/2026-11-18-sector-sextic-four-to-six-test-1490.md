# Fixed saved-pair test1490 — work in progress

Authorized target: Test whether C020o's saved polynomial pair yields a rational nonnegative-coefficient sextic (4,6) witness by monic normalization and rational translation, using C020w and exact multiplicity-aware counts.

Assessment1488/review1489 is EXPLORE and was supplied at invocation start.
The main gap remains actual-Xi all-degree positivity and unpaid unbounded
exceptional-root loss. This finite witness would only delimit a generic
sector-preserver contraction shortcut. Actual-factor correspondence,
paid loss, signs, all degrees, initialization and overlap remain open.

Test only q=1+z+5z^2/18 and C020o's displayed P,F=h^2+1. Independently
check TP=F. Count P by an exact squarefree Sturm certificate retaining
multiplicities, and use F>=1. Test the single rational translation x+1
and normalization by 154449; certify every coefficient and commutation
with T. If any restriction fails, record that failure for this
conversion only. No sweep or inverse-positivity retry is planned.

Preservation may be imported from audited C020w after checking the exact
sector roots of q; its zero/two-count conclusion is not applicable to
the four-count input. C020o's inverse moments are unnecessary and are
not being audited here. Full matching Mathlib coverage is unchecked.

Completed: the single shift 1 succeeds. All 15 rational checks pass;
the full pair, Sturm recurrence, positive scales, infinity signs, gcd,
counts and coefficient/bound fields were inspected. The new canonical
result is [C020x](../../lemmas/C020x-sector-sextic-four-to-six-witness.md).
It gives counts (4,6), a monic rational input with minimum coefficient
1, and the real-axis output lower bound 1/154449. The full independent
Sturm certificate is
`scripts/quartic-differential/sector-sextic-four-to-six-1490.json`.
The canonical proof also gives a shorter exact count using IVT and
C020w: the input has at least two real roots, and the zero/two-nonreal
branches contradict its real-root-free image. This does not presume
the four-count from a single negative evaluation.

This is local progress beyond the saved pair, not a certified novel
result beyond the sources checked. No C020o inverse moments were used
or audited. Independent audit of C020x is still required before the
notebook overview labels it audited; no actual-Xi conclusion follows.
