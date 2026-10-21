# Complete quartic response: quadratic gauge-jet test

Approved target: determine whether L011's complete quartic probe-jet
response kappa_0(f_(i,2),r_0) has a finite a^3-scaled limit for both
actual L010 probes. Reuse the unchanged EXPLORE assessment in
`drafts/literature/2026-10-16-complete-quartic-probe-jet-scale.md`.

The main gap remains the interacting reflected bound <=c_box/2 and
the continuum/infrared construction. This bounded attempt tests the
entire quadratic gauge-jet term <b,B_i b> in L212(4). If its response
is o(N^3), remove it from the complete cubic-scale question, leaving
the co-closed quartic and the two other complete gauge corrections.
Do not transfer the original isolated flow summands.

Saved before verification: b=[Hz,Vz]/2, H=I-D Phi/2, V=q Phi.
L212(5) suggests

    Cov(<b,B_i b>,r)=E[<B_i b,db[2SAz]>]=Q_(1,i,N)/2,

where Q_1 is precisely L184's first placement, not Q_3 or its whole
quartic. Check this factor independently by differentiating the
two-color covariance minor for E[<b,B_i b>] under the normalized
quadratic tilt. L186 then gives O(N^(5/2)), below the cubic threshold.
Continue if the two derivations agree with all four signed minors;
abandon this identification if a factor, projection, or derivative
of either pinned prefix is missing. No O(N^3) estimate or limit for
the complete L212 sum is assumed. Preserve ATTEMPTS/010 and 039–045.

Completed: [C212a](../lemmas/C212a-quadratic-gauge-jet-response-subcubic.md)
proves the factor 1/2 by both the single-polynomial directional tilt
and an independent two-crossing color contraction followed by the
normalized covariance tilt. All four signed minors match L184(6).
L186 applies with unchanged actual maps and retained upper row,
giving O(N^(5/2)) and a zero cubic limit for this entire term.
The remaining response is the covariance with the joint polynomial
in C212a(3), up to this subcubic error. No estimate of that joint
polynomial or new flow-endpoint interchange is established. No
mathematical script or actual-probe numerical measurement was used.
