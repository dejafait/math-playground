# Marked-octic three-adic image attempt

2026-10-23. The unchanged prior SPECIALIZE assessment is
`drafts/literature/2026-10-23-marked-octic-three-adic-point-image.md`.
Work only on its exact TARGET; completed work is REPRODUCTION.

The main gap is global supported class/unit arithmetic and rational/integer
point control. The intermediate target is the full Q3 fake point image
in L114's single scalar quotient. A proper subset would supply a later
membership filter; equality stops additional pruning at this place.
Incomplete field, quotient, chart or realization evidence leaves the
image unresolved. Independent global gaps need not be settled here.

Inputs are L113's actual G and smooth charts and L114's entire fake map,
norm fiber and both infinity conventions. The ready assessment and its
reused complete Bruin–Stoll Section 4 extraction supply known methods.
Local scoped searches found no duplicate Q3 instance. L119's label failure,
L120's eleven-adic equality and ATTEMPTS/050–052 remain relevant comparisons;
no backend probe, cross-notebook input or L117 transport is needed.

## Saved reasoning before certification

Write G(t)=P(t²). The unique Hensel root u0=2 mod 3 of P gives
G=3025(t²−u0)(t⁶+b4*t⁴+b2*t²+b0). Compute coefficients from the
constant end: b0=−2673/(3025*u0),
b2=(b0+39204/3025)/u0, b4=(b2−76230/3025)/u0.
Their valuations should be 5,4,2. The reciprocal scale r=3/theta
then gives an Eisenstein degree-six polynomial; the other factor is
the unramified quadratic omega²=u0. This is an exact factor model,
not a deduction from residue degrees alone.

Proposed square labels are (r^a*(-1)^b,3^c*(1+omega)^d).
One common rational nonsquare unit and the scalar 3 should remove
the two norm-kernel directions, leaving H3 a singleton. Verify their
actual residues and all norm/scalar orbits before concluding equality.

For integral t, units have G=2 mod 3 and multiples of three have
v3(G)=5. Both are nonsquares. For q=1/t in 3 Z3, the reversed
polynomial divided by 3025 is a principal square unit, and q*theta
has positive valuation in both fields, giving identity fake class.
Retain both infinity rows separately and an exact finite realization.
These universal estimates still require exact certificate checks.

## Completed result

The canonical full proof is L121,
`lemmas/L121-marked-octic-three-adic-point-image.md`. All proposed
factor, norm/scalar, chart and realization claims above are verified
there. The complete certificate is
`scripts/pair-genus-two/marked-octic-three-adic-image-certificate.json`:
39 arithmetic checks pass, no failures; image/ambient=1/1. This is a
NEGATIVE result for extra pruning at three, by reproduction of known
methods. No global class has been evaluated and no integer solution
excluded. A separate independent critical audit is the continuation;
its assessment is REVIEW_REQUIRED, not approved during this attempt.

Unresolved: verification of the proposed local calculation; globally,
supported units, ordinary S-class two-torsion, surviving-cover points,
degree-nine root recovery, remaining factors, both L095 systems and
minus-eleven. Preserve unfinished L108. No Beal exclusion is proposed.
