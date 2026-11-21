# Joint two-shift arithmetic realization: fixed-bump exclusion

9 November 2026, step28. The one approved projection test is complete
in [L934](../lemmas/L934-joint-two-shift-fixed-bump-projection.md),
pending separate application review. It controls the full joint span,
including every moving complex coefficient pair, using audited L933.

## WHY IT FAILS

The specified joint dictionary at N=floor(T^(1/5)), with just the two
shifts +/-1/log T, has squared projection of the fixed L637 unit bump
O(T^(-11/40)/log T), uniformly in X. Thus the minimum L2 error tends
to one and eventually exceeds every fixed tolerance below one. This
excludes that exact unsigned realization mechanism, rather than merely
showing an insufficient upper bound on a possible certificate. It does
not refute RH, an alternative bump or dictionary, or signed transfer.
Preserve the earlier step11 and step21 failures: no combined operator
contraction was proved or needed here. Complete the separate review
before treating this new application as audited. Do not automatically
enlarge lengths or shift sets or repeat the completed calculation;
reopening needs materially new input and its own covered bounded test.

Audit update, 9 November 2026, step30: the first separate application
audit passes in canonical L934. The provisional stop is now retained
under the named imports, with the same bound and parameter scope.
No signed form was tested and no dictionary enlargement was performed.
