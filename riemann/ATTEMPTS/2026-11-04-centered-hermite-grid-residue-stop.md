# Centered fixed-Gaussian Hermite-grid stop

The approved fixed-a, n=0 strict sign target was tested using exactly the
first three negative-power Laurent coefficients of the full centered
quotient. The canonical statement and proof are
[L764](../lemmas/L764-centered-hermite-grid-residue-moment-obstruction.md).
Its actual-coefficient interval certificate is
`scripts/centered-hermite/residue-moment-382.json`. Step384 independently
audited the argument and reproduced that complete certificate byte for
byte; `scripts/centered-hermite/residue-audit-384.json` records the checks.
L763's earlier squared-budget stop remains separate evidence.

WHY IT FAILS: the requested signs force negative simple-pole residues
at the distinct real H_(d-1) nodes, hence a nonpositive second residue
moment. The actual fourth centered coefficient is rigorously positive,
so that moment is positive for every d>=max{6,ceil(12000000a)}, for each
fixed a>0. This forces a strictly wrong sign at a nonzero prescribed
node. Changing the grid or allowing degree-dependent a is outside this
test; hyperbolicity and RH remain open. Do not extend the moment hierarchy
or repeat finite-degree sampling to reopen this fixed grid.
