# Favorable quadratic-penalty subsequences — 2026-09-11

Tested assertion: every fixed monotone strip quartet product with summable reciprocal squares admits penalties decreasing to zero and maximizing zeros with upward contribution tending to zero.

Outcome: false. [Lemma 75](../lemmas/L075-hidden-satellites-obstruct-all-penalty-subsequences.md) gives a fixed product with upward contribution greater than 1 at every maximizer for every positive penalty.

WHY IT FAILS: linear selection in squared-coordinate/height space excludes points strictly below consecutive-center chords. Such excluded points can nevertheless be higher than the left center and arbitrarily close to it. They therefore supply a uniformly positive local upward interaction at every selectable center while never becoming selectable themselves. Reciprocal-square summability allows these sparse pairs. The finite-window lower limit over all indices cannot be restricted to the selected indices. Additional information beyond these generic product and strip hypotheses is necessary; this is not a counterexample to RH.
