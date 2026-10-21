# Five-adic norm-slice comparison — working attempt

Approved target: decide whether L035's whole-fiber-compatible image equals
the norm-[121] slice of its unrestricted image. Prior SPECIALIZE assessment:
drafts/literature/2026-10-12-five-adic-norm-slice-image.md.

Main gap remains global integer emptiness of the 54a1 branch. Try a cardinality
separation, using L038's entire Q5 x U_11 algebra, L033's connecting function,
and L034/L040's complete map and degree-eleven necessity. This is one test of
the approved comparison, not a new target or an assumed class enumeration.

Unfinished reasoning saved before calculations: near 2T, f is a unit and its
derivative in x is -231, also a unit at five. Variation x=16+5z may produce all
principal-unit classes in each unramified factor. For compatible fibers,
integral scalar residue one is already excluded by L038's two coprime
degree-six blocks; test squarefreeness and chart validity at residues two
and four. For negative scalar valuation, L040 forces n=11k. Scaling x-16
by 5^k may force a rational simple Hensel root because raising to eleven
is bijective on F_(5^11)^*. This would exclude that entire region.

Nothing in this paragraph is yet claimed proved. Required checks are the
full nonintegral argument, complete reduction cases, uniform fifth-power
precision including exceptional points, and a rigorous unrestricted lower
bound versus whole-fiber upper bound. Stop/reassess if only samples or an
unimplemented formal sentence remain. No global units, class value,
other-place compatibility or integer lifting is assumed.

## Completed outcome

The working obligations above are discharged in canonical L060
(lemmas/L060-five-adic-norm-slice-strictness.md); no duplicate proof is
kept here. Outcome ADVANCE / REPRODUCTION: 0<|I_fiber|<=600<5^10<=|S_N|.
The standard-library certificate passes 25 checks. The initial optional
SymPy probe was unavailable and was replaced by exact modular polynomial
arithmetic. All negative scalars are excluded uniformly; the upper
bound retains both integral residues and all isomorphisms. Strictness
is nonconstructive at the level of an individual excluded class.
No global exclusion follows; independent critical audit is pending.
