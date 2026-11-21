# Positive-update variance enclosure stop1928

WHY IT FAILS: The approved two-unit-atom kernel representation pays the
whole-collar update divisor (lower bound >573.530616), but the ensuing
coefficient/Newton-sum variance enclosure contains0, with endpoints near
-22369.279057 and34276.881561. Thus both orientations stop before
normalized residuals, normalized Jacobians or Krawczyk evaluation. Exact
reference variance is positive; this is interval overestimation, not
nonmatching or a negative variance. Full formulas, hypotheses, bounds
and citations are canonical in C028v. Producer/checker certificates are
`scripts/heat/two-site-positive-update-1928.json` and
`scripts/heat/two-site-positive-update-check-1928.json`. All11019 finite
replay/algebra checks pass, conditional on unchanged L917/L037 inputs.
The separate proof/code/evidence audit1930 accepts this conditional
finite claim; see C028v's canonical audit section and
`scripts/heat/two-site-positive-update-audit-1930.json`. Preserve C028t's audited rank
and C028u's Cramer failure. Park repeated natural whole-collar evaluation
after these two inconclusive attempts; a materially different mechanism
and separate source assessment are needed before further matching work.
