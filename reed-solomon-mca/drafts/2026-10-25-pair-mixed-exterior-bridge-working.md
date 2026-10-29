# Mixed-exterior bridge working checkpoint — step 482

Approved target and source scope are unchanged from
`literature/2026-10-25-pair-mixed-exterior-bridge-review.md`.
Inputs read: L109's full map/kernel argument and L153's original-domain,
rank and scalar-extension proof; prior failures ATTEMPTS/048–049 retained.

Attempt: for A=ker Q_a, B=ker Q_b set T=A intersect B, dim T=t.
Choose W=T direct-sum A_0 direct-sum B_0 direct-sum C, with dimensions
t,3-t,3-t,1+t. Using the imported ordered exterior basis, the common
kernel consists of T wedge W and A_0 wedge B_0: the first quotient
annihilates exactly basis wedges meeting A, the second those meeting B.
Their dimensions sum to 9+t(t+1)/2. L153 gives nine, so t=0; the
remaining basis wedges are exactly A wedge B. The coordinate comparison
and no-cancellation justification are now written in canonical L155.

This is a specialization of inspected exterior-basis/functoriality
theorems, classified REPRODUCTION. No decomposable-locus or gate result
is being asserted. The canonical proof retains every extension,
original support label and all coding qualifications; independent
critical review is the next action recorded in PROGRESS.md.
