# Four-anchor cross-difference test stopped

2026-10-16, step 254.

WHY IT FAILS: The [complete analytic pass](../drafts/2026-10-16-four-anchor-cross-difference-attempt.md)
uses L067's arbitrary-pair interpolation identities and all four proposed
anchors. Every pair cross-difference has a known degree-five factor;
the gated value at a proves the residual cubic nonzero. The supplied
root constraints force at most three residual zeros with multiplicity,
short of the four required for contradiction. The four-row minor
identity is automatic, while restored-weight evaluations are exactly
the existing L064 pair comparisons. No additional coefficient
incompatibility or qualifying quartet was obtained. This stops the
approved root-count/automatic-minor mechanism, not coexistence or the
main problem. Reopening needs a specific further coefficient restriction
with all singular branches, not a formal resultant, more label samples,
or repetition of L080's fixed assignment. The interval is unchanged;
no new lemma is claimed.
