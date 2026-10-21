# Four-branch finite-jet attempt — step 377

Approved target: Determine a finite-jet formula for the normalization-quotient length at a four-preimage span-two collision, retaining arbitrary nonlinear normal jets.

Main gap: universal primitive Hodge realization. Intermediate target:
complete order-three tail and exact degree-two image. Downstream use:
conditional local contributions to the actual image's normalization quotient.
Continue if the full tail follows and the finite map retains normal linear
functions; otherwise abandon this cutoff with the missing hypothesis.

Inputs: L118, L120, L121 and the pre-existing SPECIALIZE assessment
`literature/2026-10-18-actual-four-branch-normalization-jets.md`.
L122/L125 and ATTEMPTS/070--072 are comparisons, not four-branch inputs.
No local duplicate four-branch calculation was found in the scoped search.
Existing changes and unfinished work are preserved.

Provisional calculation: the projectivized four tangent complex planes
are disjoint lines in P^3. Derksen--Sidman gives H^1(I(d))=0 for d>=3,
hence all tangent restrictions surject there. Complete filtered lifting
should give rho(m^3)=product n_i^3. Target jets have dimension 24;
constants contribute one dimension and linear restrictions four. If
E2 is the quadratic tangent image and N the quadratic restrictions of
linear forms annihilating the tangent span, the expected formula is
length=19-dim(E2+N)=7+dim(coker(E2+N)).

Check remaining details: exact four-factor completion; full block jet
map and elimination of nonzero linear rows; tangent quadric rank; honest
distinction between arbitrary formal branch jets and actual geodesic jets.
Do not assume a generic arrangement or actual jet realization. A common
connection may constrain actual second jets; this attempt retains them
as coefficients and does not silently replace them by free geometric data.

Completed: the full proof is canonical in
`lemmas/L126-four-branch-normalization-finite-jet-formula.md` (not repeated
here). The tail and finite map pass the stated continuation test. The
two tangent cases have quadratic cokernel dimensions three and two;
normal jets remain an explicit rank in the actual length formula. The
formal tests show dependence for the relaxed smooth complex-branch
problem, not for actual geodesic branches. Actual normal-jet constraints,
collision occurrence and F existence are unresolved. Separate critical
audit is the next target and requires coverage approval.
