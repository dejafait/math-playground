# Prescribed identity-cost Riccati calculation1956

Research under the unchanged SPECIALIZE assessment1954. The target is
only the actual C029b companion and the prescribed stabilizing solution;
no changed state cost or spectral premise is used. Stops1948/1949/1951
remain intact and do not supply this calculation.

Working argument, saved before final write-up: put A=exp(b_1)F(1),
u=sqrt(1+A^2)+A, l=1/u. For any unit eigenvector v of the positive
solution X with eigenvalue x, the CARE gives x^2=2x v^T M v+1.
Since |v^T M v|<=A, l<=x<=u. The upper-left block G has the same
spectral enclosure, so B=G^(1/2) C G^(-1/2) satisfies
||B||_F^2 >= (l/u)||C||_F^2=l^2||C||_F^2.

All d-1 subdiagonal entries of C are one. Its centered last diagonal
entry is zero; Newton's degree-two identity (or direct multiplication)
gives tr(C^2)=-(1-1/d)(b_2-b_1^2). For real B,
||(B-B^T)/(2i)||_F^2=(||B||_F^2-tr(B^2))/2.
Thus the proposed exact lower bound for the full trace norm is

    (k_d^R)^2 >= [l^2(d-1)+(1-1/d)(b_2-b_1^2)]/2.

The right side can be negative at small d; use its positive part when
taking square roots. The asymptotic lower bound is l/sqrt(2) for
k_d^R/sqrt(d). Need final checks of the direct trace computation,
similarity factors, source hypotheses, and degree scale. A cost floor
or growth of this upper majorant does not lower-bound H_d. No RH
resolution is asserted. Final proof will be canonical in C029d.

Finalized in C029d during step1956: the direct trace computation,
positive-part convention and sufficient onset are written out there.
This draft preserves the working argument, not a second proof or a
separate dependency record. Independent audit remains pending.
