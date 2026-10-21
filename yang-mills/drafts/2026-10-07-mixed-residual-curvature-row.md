# Mixed residual curvature-row test

STEP_ID: YM-20261007-079-mixed-residual-curvature-row

Reuse the unchanged SPECIALIZE assessment in
`literature/2026-09-26-current-target.md`. Main gap: the full interacting
response and its ultraviolet logarithm remain uncontrolled. Intermediate
target: test L062's six distinct-row terms with the actual mixed residual,
starting from the separated upper-curvature source. Downstream use:
reduce the mixed a²-scale coefficient to terms that really require a new
rough potential/residual estimate. Continue if the separated-source norm
gives a strictly subleading complete subgroup; otherwise retain the
failed bound without inferring signed growth.

Duplicate/failure checks: L054 handles upper/upper residual blocks;
L061 and L062 retain all differentiated curvature/potential zeros.
L041 already proves ||A_0 Sigma r_d||_2=O(a^5). ATTEMPTS/017–018
exclude rough-product smallness and unweighted noise localization,
but neither excludes using this separated upper source. No extra
literature or reproof of flow renormalizability is needed.

Unfinished reasoning: in L062's coordinates take the two distinct-row
terms with V' on row 1 and U' on row 2 or 3. Extend L026's transverse
link variance upper bound to pinned end edges using its exact incidence
argument. Combined with the full Hodge gap, this should give
||Sigma r_b||+||Sigma r_q||=O(a^-3/2), while a curvature row has norm
O(a^-1). Pairing with the separated residual source would bound V'_11
by O(a^4) and V'_12,V'_13 by O(a^7/2). L062's heat columns and complete
axial H/J norms then test the two determinant sums. The other four
terms must remain; no extension of L054's compressed form bound is
assumed. Verify all endpoint cases and every determinant monomial
before claiming a bound.

Completed: [L063](../lemmas/L063-mixed-residual-curvature-row-bound.md)
proves that both terms with V' on row 1 have total O(a^-3/2) absolute
bound. Their a²-scaled contribution vanishes. Together with L062 this
leaves the four placements (j,k)=(1,2),(1,3),(2,3),(3,2), with U' on
row j and V' on row k. The full proof, endpoint justification and
qualifications are canonical in L063. No script or source refresh was
needed. The original six-term estimate is only partially resolved;
there is no bound for these remaining four terms or full mixed limit.

Continuation within the unchanged response target: estimate those four
terms jointly, retaining the rough residual on upper potential/difference
rows. Essential inputs are L018, L028, L041, L054, L058, L060–L063;
L011/L019 remain necessary for complete-response assembly and L059/C057a
for conditional comparisons. A mixed analogue of the upper/upper form
bound is still an unresolved assumption, not an available estimate.
