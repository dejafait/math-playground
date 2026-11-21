# Actual theta cubic Gaussian pair — step540

The approved actual-moment test is established in
[L805](../lemmas/L805-actual-theta-two-node-gauss-interlacing-obstruction.md),
with full exact-rational evidence at
`scripts/theta-gauss/two-node-certificate-540.json`.
This is a new local specialization of standard quadrature, not a new
Gaussian theorem or a claimed discovery beyond the checked literature.

WHY IT FAILS: The exact positive two-node rule reproduces the actual
cubic, but its reference cubics have an empty second interlacer
intersection. The certified upper-minus-lower gap is at most
-195.451439, strictly below the required zero. The first intersection
does pass. Positive weights and cubic exactness therefore do not rescue
this sufficient common-interlacing premise. Known real-rootedness of
the particular actual cubic is compatible with the obstruction.

Preserve the full-support and Favard stops; this result neither assumes
nor strengthens them into a global ban. Repeating this failed pair
needs a materially changed representation and a new source gate.
Independent audit of L805 passed in step542 (106 checks, no defect),
with evidence in `scripts/theta-gauss/audit-certificate-542.json` and
full qualifications in the canonical proof. All-degree mixed positivity,
other representations and degree-uniform control remain open.
