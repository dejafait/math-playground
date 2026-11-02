# Angular grouping: constant energy comparison fails

The approved detector was tested through a proposed constant-factor
comparison between its full constant-input energy and the sum of
the energies of ordinate groups of length 1/n.
[L647](../lemmas/L647-angular-cluster-block-coercivity-stop.md)
constructs admissible common-pole families with positive integer residues,
M<=n/3 and singleton groups for every partition origin, for which the
full/group energy ratio tends to zero. The analytic construction is
author-checked and awaits a separate audit.

WHY IT FAILS: Positive coefficients can cancel the leading full response
at every maximizer of its angular exponential profile. The angular
energy concentrates at precisely those finitely many maxima. Keeping
all cross terms gives vanishing relative energy even though the poles
occupy distinct bins. This rules out a uniform positive constant in
the proposed comparison. Both absolute energies still grow exponentially,
so it neither refutes the detector nor rules out an exponential-loss
comparison at rate 1/16. C645o's entry-sign warning and L646's exact-output
restriction remain separate stops; neither grouping in general nor RH
is refuted.
