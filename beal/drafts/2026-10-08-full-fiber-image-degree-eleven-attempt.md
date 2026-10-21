# Full-fiber image comparison through the degree-eleven factor

2026-10-08. Approved target and assessment are unchanged: determine whether
L036's D makes L035's I_pow a proper subset of I_fiber, retaining all
isomorphisms and collisions. This is one bounded REPRODUCTION attempt.
The main gap is global emptiness of the five surviving twists and the
remaining signatures. Equality would stop this particular power filter;
strictness could supply an input to a later certified global intersection.

Checkpoint before calculation: L038 identifies the entire algebra as
Q5 x U_11. A whole-fiber isomorphism therefore supplies a point whose
coordinates jointly generate U_11. Since the curve is quadratic in y,
its x-coordinate must have degree eleven. Test whether L034's necessary
monic equation F(x,s)=h^3+Js-(x-16)^11 s^2 prevents such a point at
integral s congruent to 0 or 1728, and forces 11 to divide -v5(s) for
nonintegral s. If both hold, every compatible scalar already lies in D,
so the same point and isomorphism would prove equality of the images.

Pending obligations: exact residue factors at 0 and 3; every factor and
multiplicity retained; treatment of x=16 without asserting a universal
single-coordinate fiber presentation; exclusion of negative-valuation x
by a rational Hensel root; integrality of valuations in U_11. No finite
precision cutoff, global witness, class list or equality is assumed.
Reuse the Hensel hypotheses and primary citations already recorded in
L036 and L038–L039. Inputs: L034–L036, L038 and L039; L037 supplies the
comparison interpretation. ATTEMPTS/008–011 remain preserved.

## Completed bounded attempt

The canonical full proof is
[L040](../lemmas/L040-primitive-five-full-fiber-image-equality.md).
Both integral branch residues give two coprime blocks of degree six.
For nonintegral scalars the reciprocal polynomial has a unique small
rational root; the degree-eleven point cannot use it, and its integral
x-coordinate satisfies 11 v5(x-16)=-v5(s). Unramifiedness makes the latter
valuation integral. Hence all compatible scalars are in D, proving
I_pow=I_fiber with the same point and isomorphism. No class enumeration
or Cohen elimination is required.

The exact coefficient script and certificate are under
scripts/full-fiber-image-comparison/. All 15 checks passed, and the
complete relevant residue and valuation coefficient evidence was
inspected. This is RESEARCH / NEGATIVE / REPRODUCTION: an informative
stop for the proposed additional local filter, not global exclusion or
claimed novelty beyond the checked sources. ATTEMPTS/012 records the
stop and its limited scope. A separate critical audit must check this
new specialization; it is not performed or approved in this attempt.
