# Full four-row locus capacity — bounded working record

Step 516, 2026-10-26. Invocation-start assessment:
`drafts/literature/2026-10-26-full-four-row-capacity-dual-attempt-review.md`
(EXPLORE). This is one mathematical attempt on its exact target.

Main gap: uniform twelve-row exclusion. Intermediate target: a complete
cover of the original (35,522,477,566) exact-rank-one locus with pure
nonnegative support-weight cost below eight additions, or an exactly
realized fractional obstruction of size at least eight. A positive
result could exclude this seed; it would not supply extraction of this
seed, exclude other quadruples, identify the challenge, or improve the
radius. A failed guessed cover alone is not a negative method result.

Inputs read: L109 actual maps and gates; audited C155a and its inherited
L155/L153 qualifications; audited L162, L163 and L164. Reused step 514's
primary theorem comparison and step 515's source traceability. Checked
ATTEMPTS/048–049 and /052–053. No external search or cross-notebook input.
L159–L161 are not premises.

Structural hypothesis H1 (unproved at this checkpoint): the full locus
is covered by L162's family, perhaps together with a coincident-line
boundary. Use C155a to write L=span(x,y), x in V_35, y in V_522. Test
the exact space of pairs with x+y in V_477, then the remaining V_566
condition. Keep separately every case in which the third or fourth
intersection is one of the first two factor lines. No genericity,
base-field sampling or rank-only inference is permitted.

Discriminating evidence: exact linear identities and a complete case
split must prove exhaustion over E=algebraic closure of F_97. If H1
holds, audited L163/L164 may supply a cost-three certificate on the
family; any residual planes need their own certified mask/cost. If H1
fails, preserve the first residual branch before considering a second
structural hypothesis. At most three hypotheses in this step; no
all-mask, all-quadruple or unrestricted solver sweep.

Unresolved at this checkpoint: the dimension/basis of the three-row
pair space, its fourth-row pencil, and all coincident-line branches.
Full-locus identification with L162 is specifically not assumed.

## Completed attempt

H1 succeeds. The canonical full proof is L165. The three-row pair
space has basis (x_0,y_0),(x_1,y_1),(0,e_12). The fourth-row identity
forces t=26 and the e_12 coefficient zero in the distinct-line branch.
The only possible coincident branch is excluded by an injective
four-dimensional restriction of Q_566. Thus the full locus equals
L162's family; audited L163/L164 give one weight of cost 3<8 everywhere.
No second or third structural hypothesis was needed, and no residual
geometric branch is left for this seed. All independent mathematical
gaps listed above remain.

The producer and independent verifier are
`scripts/seven-coordinate/full_four_row_capacity.py` and
`scripts/seven-coordinate/verify_full_four_row_capacity.py`. Their full
certificates share those stems with hyphens and `.json`, the verifier
using `full-four-row-capacity-verification.json`. All 157 verification
checks pass; the complete maps, basis, selected minors, fourth-row
coefficients and forty support records were inspected. No old script
or lemma was changed. This is a local ADVANCE, with separate proof
audit pending; it is not a solution or novelty certification.
