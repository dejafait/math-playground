# Attempt 060 — linear expanded-support generators for the paired reachable space

Step 549, completed 2026-10-29. The complete original-coordinate proof and
finite evidence are canonical in
[L127](../lemmas/L127-paired-reachable-generator-support-obstruction.md).
The ready step-548 EXPLORE assessment was reused. The newly written
uniform obstruction still requires a separate conceptual audit.

**WHY IT FAILS (pending that audit).** Restricting full E_N to the paired
reachable K_N does not remove every expensive parameter direction:
K_N's original A_f projection is onto F₂^N, by the triangular matrix
binom(i,ell) mod 2. Any K_N generating family therefore has an invertible
N-row projected minor. L126's audited individual-row support bound can
charge one distinct row for each of those N parameters, giving total
support at least 2(1+sqrt(2))^k, whose ratio to S=16*2^k+20 diverges.
Neither K_N=E_N nor combined parameter-block surjectivity is assumed.
The independently received N=4 deficit (rank 7 versus dimension 9 at
weight <=4) is only a finite discriminant; it is not the asymptotic
argument. All original coordinates and earlier stopped routes remain.
No general-chain or unrestricted complexity conclusion is asserted.

Step 551, 2026-10-29: the separate conceptual audit in L127 §7 validates
every uniform bridge and the exact original-coordinate qualifications.
Both complete finite certificates are reproduced and compared in
`scripts/batched-incidence/output-551/`. The provisional stop is now
audited. This adds no obstruction for arbitrary zigzags or other row
spaces; the old pending-audit wording above records the step-549 state.
