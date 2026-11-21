# Step517: finite-horizon detector development (working record)

The exact target and prior EXPLORE scope are supplied by
`literature/2026-11-11-effective-two-cell-detector-length-515.md`.
Main gap: actual-Xi positivity, with non-neutral coverage and assembly
still independent. A length certificate would permit a finite-window
sign certificate to exclude a specified off-line zero; no such sign is
assumed established.

Read C744r completely, unconditional L742(8)-(12), and L744(1),(6),(8).
Reused the ready source comparison, the C744r audit, and the signed
Gram-dual/removed-zero-remainder stops. No cross-notebook input.

Planned bounded test: assume nonnegative admitted two-cell sections
through K cells and restrict C744r(9)-(12) to t in [0,(K-1)ell].
For the same complete coefficients a_z set p=i z0, G=sum a_z/(s-iz)
and J_H(s)=integral_0^H h(t)exp(-st)dt. The analytic function to test is
(s-p)(G-J_H), with its selected pole removed. On Re(s)>1/2 its
tail has an explicit exp(-(Re(s)-1/2)H) bound using sum|a_z|.

Potential continuation certificate: a finite chain of disks in Re(s)>0,
ending at p and avoiding all other poles, together with a numerical
upper bound on the complete absolute coefficient sum and a positive
lower bound on |a_z0|. Hadamard's three-circle theorem is standard
complex analysis inside the approved scope. Check whether its elementary
disk iteration yields an actual finite H while keeping C744r's strict
budget constants unchanged. These numerical certificates are additional
data, not supplied by T,delta,Delta or qualitative discreteness.

Continue only for a full conditional length formula with every such
datum displayed. Otherwise stop at the first unpaid inequality.
Do not turn qualitative tail convergence or pole isolation into a
computed constant. No lemma or effective bound has yet been established
at this working checkpoint.

Completion: the bounded disk-chain test produced the conditional formula
recorded canonically in C744s, without supplying numerical mass/residue
or all-other-pole clearance certificates. All proof details are in the
canonical lemma, not this interrupted-work record. Step517 stops there;
its separate audit nomination is REVIEW_REQUIRED.
