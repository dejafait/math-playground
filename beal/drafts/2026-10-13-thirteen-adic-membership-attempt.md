# Thirteen-adic fixed-class membership — bounded attempt

Gate: the prior SPECIALIZE assessment
`drafts/literature/2026-10-13-thirteen-adic-canonical-class-membership.md`
authorizes this REPRODUCTION attempt only. Inputs are L033's K and
normalized dual connecting map, L034's entire modular map, and audited
L062's fixed sigma and global class. No cross-notebook input is used.

Main gap: integer emptiness of the 54a1 branch and remaining signatures.
Intermediate threshold: an exact primitive whole-fiber witness for the
localization of that same class at thirteen, or complete exclusion.
Membership retires this survivor-removal test; exclusion removes only
one known survivor. The all-place intersection and integer lifting
remain independent gaps.

Initial exact observation: for the canonical scalar, t=343/512 is a
thirteen-adic unit and q=169/512 has valuation two. In any primitive
integral triple with these ratios, c is a unit: if c were a nonunit,
the identities force a,b to be nonunits too. Thus v13(q)=4*v13(b)
would have to be divisible by four, which it is not. This rejects only
the canonical scalar, not its connecting class at other scalars.

Work saved before further computation: certify the complete K tensor Q13
algebra and test primitive unit scalar residues with complete regular
fibers. Finite-field factorization, reconstruction and residue fifth-power
comparisons must have exact certificates and lifting proofs. Ramified
branch disks or unmatched class collisions remain unresolved if needed.
Stop after this bounded test if it supplies neither a complete witness nor
complete exclusion; do not promote a finite-precision sample to a decision.

## Completed bounded attempt

The exact witness threshold is met in L064, whose canonical proof retains
all hypotheses and load-bearing residue identities. The entire algebra
and the scalar-3 fiber are both the unramified degree-twelve field; the
fixed canonical class and the scalar-3 class are both the identity.
Common witnesses have b=2, a³=16/575, c¹¹=9216/575. The full certificate
is `scripts/thirteen-adic-membership/membership-certificate.json`, with
16/16 checks passing and no mathematical failures. The initial optional
SymPy probe was unavailable; the completed implementation uses only
standard-library exact arithmetic. A relative-path reporting error in
the first runpy probe was fixed before the completed certificate run.

Outcome NEGATIVE / RESEARCH / REPRODUCTION: the proposed removal of the
known survivor at thirteen fails, although a relevant local membership
input is established. No progress beyond the assessed known methods is
claimed. The canonical-scalar failure remains recorded and is overcome
only at the class level by a different scalar, not by asserting it has
primitive witnesses. The full image and integer lifting remain unresolved.
The continuation is a separate critical application audit of L064;
coverage of that exact audit target is marked REVIEW_REQUIRED.
