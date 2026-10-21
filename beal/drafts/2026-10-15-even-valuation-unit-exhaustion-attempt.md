# Even-valuation unit exhaustion — working checkpoint

Approved target: derive the exact ideal-class criterion in the saved
SPECIALIZE assessment `drafts/literature/2026-10-15-even-valuation-unit-exhaustion.md`.
Inputs are L033's entire K and L069's entire cubic D/K and unit kernel V.
No cross-notebook input or arithmetic backend is required.

The main gap remains primitive integer emptiness. The bounded target
isolates possible non-unit contributions before L071 can be used in a
complete descent bound. Independent gaps are full Kummer containment in
the all-finite-even space, certified class data, further local filtering,
rank and integer lifting. ATTEMPTS/032 remains in force for the unfiltered
shortcut.

Proposed specialization: import the ordinary ideal-square sequences for
D and K and use relative ideal norm for the vertical maps. Write H_F for
the all-finite-even square classes and W=ker(H_D -> H_K). The desired
sequence is 0 -> V -> W -> ker(Cl(D)[2] -> Cl(K)[2]) -> 0.
The candidate obstruction vanishes because norm on unit square classes
has the scalar section: N(u)=u^3, hence [N(u)]=[u]. For a class lift
(alpha)=a^2 with N(a)=(b), the element epsilon=N(alpha)/b^2 is a unit;
alpha/epsilon then has norm (b/epsilon)^2. Check all choices, fractional
ideals and converse before recording a canonical result.

Continuation test: a necessary and sufficient criterion with controlled
lift choices passes; an unsupported assertion of unit exhaustion fails.
No class-group value or rank conclusion follows from a criterion alone.

Completed: L072 gives the canonical exact sequence and exhaustion
equivalences, including the cubic scalar-unit correction, all lift choices,
the ordinary class-norm section and exact norm-one representatives. The
conditional criterion passes the stated test; no class values or Kummer
containment are claimed. This is REPRODUCTION of the assessed machinery,
not progress beyond the sources checked. A separate critical audit remains
to be approved. No mathematical script was needed or written.
