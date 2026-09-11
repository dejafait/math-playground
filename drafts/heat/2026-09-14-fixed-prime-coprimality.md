# Fixed-prime coprimality checkpoint — 2026-09-14

The current Next action is split at a fixed prime cutoff. Proposed scoped
result: for every fixed integer D>=1, a positive proportion of every
L203 slice has interior phase and gcd(m0,D)=1. This does not yet give
gcd(m0,ab)=1.

Proof plan: apply L204's third-derivative argument to P4/D, use a
continuous triangle in each residue interval (r+I)/D for which
 gcd(r+1,D)=1. Its mean is (3/32)phi(D)/D. The uniform o(1)
root approximation transfers the selected points to the exact m0
without crossing an integer boundary. All limits keep D fixed.

Resume here: check the Fourier minorant normalization and the transfer
from P4 to sqrt(abcd), then state the remaining large-prime count with
an explicit threshold. Claims in this checkpoint are unproved until
written and verified in the lemma.

Completed in L205: the period-D triangle average and exact integer
transfer are proved. The fixed-prime selection is established; the
large-prime remainder is explicitly unproved. See PROGRESS.md for the
single current action. No growing-D limit is justified by this step.
