# Projective pole transport — saved attempt

The approved target is the literal projective/monomial transport in
`drafts/literature/2026-10-20-projective-pole-transport.md`.
Inputs: C012a, L099, L100, L102 and foundations/02. No cross-notebook input.

The main gap is arbitrary-center 67/68 safety in the 955–957 bracket.
The intermediate test asks whether the whole translated-pole family can
inherit L100's cap through one code isometry. Continue only on complete
domain/code/whole-family verification; abandon this mechanism if a necessary
condition excludes every eligible map. Other arbitrary centers remain open.

Proof plan saved before the final write-up: if (aX+b)/(cX+d) permutes H,
then (aX+b)^1024-(cX+d)^1024 is a scalar multiple of X^1024-1.
The first two interior coefficients, nonzero binomial factors in
characteristic 65537, force ab=cd=0 and hence scaling or inversion.
Their code multipliers are respectively constant or constant times X^63;
uniqueness follows by applying a diagonal code automorphism to 1 and X^63.
For each case, clearing denominators in proposed center equality gives a
polynomial of degree at most 70, vanishing on all 1024 points. Its value
at the preimage of 3 is nonzero because the source c is nonzero.

The completed canonical outcome, all qualifications and full proof are in
[L103](../lemmas/L103-projective-pole-transport-obstruction.md). This is an
obstruction to the assessed transport, not a fiber bound or RS boundary
improvement. No mathematical script is required: the exhaustion and
finite-domain identity test are symbolic. A separate critical audit remains
pending; the saved plan above is not a second proof or dependency index.
