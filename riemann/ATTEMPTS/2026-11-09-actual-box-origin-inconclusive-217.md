# Fixed actual-box origin sufficient test — inconclusive

9 November 2026, step217. The prior EXPLORE assessment was
`drafts/literature/2026-11-09-actual-box-origin-feasibility-test.md`.
One exact interval calculation used only its fixed panel0 ratio boxes
and L917/L921's existing finite coefficients. The source endpoints,
ratio bounds, symbolic coefficient checks, retained constraint list,
direction bounds and six signed numerator terms are saved in
`scripts/heat/actual-box-origin-217.json`; reproduction is
`python3 scripts/heat/actual-box-origin-217.py`.

WHY IT FAILS: The leading logarithmic block is certified positive,
so L921's first-two-row reduction is legitimate without excluding
zero coordinates or singular cases by assumption. But the interval
for the resulting origin numerator has a negative lower endpoint
and positive upper endpoint, inside [-8.897e-38,1.328e-37]. Its
required lower bound is zero. This sufficient test therefore pays
no origin sign. The remaining third null row and all 29 PSD-minor
conditions are retained, but were not used to narrow this interval;
failure of the stronger sufficient bound cannot decide feasibility
or sign on the full target set. No counterexample or impossibility
of another method is claimed. Do not infer an actual contact from
these data. The fixed bounded attempt stops without refinement,
changed boxes, a new support family or an automatic follow-up search.

Canonical coefficient/null-row mathematics remains L917/L921; L918's
full residual stays unaudited. Its compact sign and actual flux,
initialization/equality, other panels/degrees and global continuation
remain open. This record is EXPLORATION/REPRODUCTION, with no new
mathematical advance or progress beyond the sources checked.
