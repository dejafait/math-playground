# Joint two-prime cubic attempt — step 232 (working checkpoint)

Approved target: identify every fixed log-2/log-3 cosine coefficient,
prove bilateral summability, and decide the torus-density sign.
Coverage reused: literature/2026-10-18-joint-two-prime-cubic-density-attempt.md.
Main gap remains global mixed positivity; actual/global realization,
clipping, capped nondegeneracy and L413's full-error margin remain independent.

The fixed-rational interface and common denominator h=1/(AB), for
2^j3^k=A/B reduced, appear to transfer L433's physical proof unchanged
apart from constants depending on the fixed pair. Resonance is exactly
B dividing mnq for A/B and A dividing mnq for B/A.

Working algebra (not yet canonical or verified): for p=2,3 let
b_p(d)=1 for d<=0, and p^(-d)(1+(1-1/p)d) otherwise;
B_p(j)=sum_(s,v>=0)(s+1)p^(-2s-3v)b_p(s-v+j).
Its bilateral generating function should be
Q_p(u)=p^7(p-1)^2 u^3/[(u-1)(u-p)^2(p^2u-1)^2(p^3-u)].
The proposed joint density is Re(Q_2(sqrt(2)e^(i theta))
Q_3(sqrt(3)e^(i phi)))/(B_2(0)B_3(0)), not the product
of the two real parts. Joint absolute convergence must precede this.

On |u|=sqrt(p), X=Re u,Y=Im u, define
A_p=p+1-2X, B_p^*=p^3+p^(-2)-2X,
C_p=p^3+1-(p^2+1)X, D_p=(p^2-1)Y.
Candidate identity: Q_p=p^3(p-1)^2(C_p+iD_p)/(A_p^2(B_p^*)^2).
For p=2,3, the squared maximal |D_p/C_p| should be 18/31 and
48/121; their product 864/3751<1/4. If verified, this gives
Re(Q_2 Q_3)>Re(Q_2)Re(Q_3)/2>0 everywhere.

Next within this attempt: check the exact identities and write the
complete convergence, physical-tail and sign arguments canonically.
No new law or actual sine limit is contemplated. No physical asymptotic
will be summed over growing characters.

## Completed attempt

The working formulas above were verified and promoted to the full proof
in [L434](../lemmas/L434-joint-log-two-three-cubic-positive-torus-density.md).
That canonical file contains the complete physical passage, joint
majorant, rational identity and global sign. All 19 exact checks pass;
the certificate is `scripts/discriminant/joint_two_prime_cubic_density_certificate.json`.
The local density is >1/194400, so this stronger positive-measure
obstruction is stopped, pending separate critical audit. This draft is
retained as the pre-lengthy-work checkpoint, not an alternative proof.
Current status and the sole next action are in PROGRESS.md.
