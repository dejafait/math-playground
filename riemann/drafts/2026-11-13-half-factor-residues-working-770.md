# Two-pole finite specialization — step770, working record

Approved target: certify both residues of L825's original-coordinate
Q_3/Q_2 using the existing actual coefficient enclosures. Main gap:
L030-L032/C032a actual-Xi all-degree mixed positivity. Downstream use:
adjacent-factor induction would require independent uniform interlacing
before forward convolution; shifted/mixed/global steps remain unpaid.

The prior SPECIALIZE assessment is
`drafts/literature/2026-11-13-half-factor-two-residue-test-768.md`.
Read L825 in full, L019/L021 definitions, L795 normalization, relevant
L791 and L778 analytic/error-contract ranges, the step631 checker and
step768's source comparison including proof cases and degeneracies.
Existing common-symbol, common-measure and within-degree detector stops
are contrasts, not premises. No cross-notebook input or new evaluator.

Pending: inspect complete relevant coefficient/audit evidence and hashes,
then exact rational root/residue enclosures. With a=u_2/2<0, b=u_3/2,
c=v_3/2, denominator roots are +/-sqrt(-a). Polynomial division gives
Q_3/Q_2=y+((b-a)y+c)/(y^2+a); at a root r, the residue is
(b-a)/2+c/(2r). This identity will be checked algebraically in the
certificate. Keep the linear part; apply the cited strict criterion only
after simple real poles and nonzero residues establish coprimality.

Test: two negative enclosures certify only this pair and retire this
diagnostic. A positive enclosure stops this strict route; exact zero is
cancellation, while a zero-straddling enclosure is inconclusive. No sweep,
coordinate change or precision campaign follows. Full Mathlib unchecked.

Completed: C825a records strict negative signs for both residues and this
pair's strict interlacing. The complete new certificate passes 54 checks
with no failures; source hashes and relevant input enclosures were checked.
The script uses exact Fraction endpoints and a fixed six-place square
bracket, with full polynomial identities rather than sample substitutions.
No sweep or new uniform claim follows. Separate audit is newly nominated
with REVIEW_REQUIRED; this working record is retained for recovery.
