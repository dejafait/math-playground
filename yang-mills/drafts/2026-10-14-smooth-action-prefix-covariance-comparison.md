# Smooth-action prefix covariance comparison

Unfinished reasoning saved before the detailed proof. Reuse the unchanged
ready cubic-residual/action assessment. The main gap is the interacting
reflected error <=c_box/2 and subsequent continuum/infrared construction.
The bounded intermediate test is to replace only the left K in L175(2)
by Y=M tensor G, keeping m J F A^gen M_h S in its exact order, and
control that replacement at o(N^3). This would expose the explicit
min(s,t) axial weight for a later signed limit. Continue if the error is
subcubic; abandon this comparison if it only repeats O(N^3), moves a
variable multiplier, or cuts off the action column.

L156 gives D=Y-K=(L_D tensor I+I tensor Delta_T)^(-1)(I tensor G),
0<=D<=Y. The scalar spectrum suggests Tr D<=C N^4 log(eN).
For a positive H<=Y replacing the left K, the two factors should obey
||X_H||_HS<=C a p(k) sqrt(Tr H) and
||Z_H||_HS^2=Tr(H m_j J_j K J_j^T m_j)
<=Tr(Y m_j J_j Y J_j^T m_j)<=C p(l)^2 N.
Together with the whitened generator bound C N this predicts error
O(N^(5/2) sqrt(log(eN))) for H=D. This has not yet been claimed as
a proved result in this saved paragraph.

The same single covariance comparison may permit uniform removal of
the low transverse sector of Y: with P_b selecting max(q_2,q_3,q_4)<=b,
Tr[M tensor (P_b G)]<=C N^4 b. The proposed normalized error is
C sqrt(b/N), which would let b=floor(delta N) be removed after the
mesh limit. This acts only on the first covariance, not F or the heat
columns. The action multipliers must stay in place.

Relevant proofs inspected: L175, L159, L156, L026; L172/L174 fix only
the later comparison, lim a^3 V_i=6K_(i,R)-K_(i,T). The targeted recent
smooth-action drafts and histories contain domination K<=Y but no
subcubic equality comparison in this order. ATTEMPTS/009, /011, /036,
/037 remain applicable. No new external theorem, source lookup or
novelty claim is needed. Full matching Mathlib coverage is not checked.

Both signed-limit identification and evaluation remain open, as do
other response jets, full compensation and all finer asymptotics.

Completed: [L176](../lemmas/L176-smooth-action-prefix-covariance-mass-comparison.md)
proves the positive ordered-trace estimate and the subcubic replacement.
The low-sector idea is implemented by the smoother transverse resolvent
G_epsilon: its complete difference has trace at most
(3 pi/32) N^5 sqrt(epsilon) after tensoring with M. The normalized
signed-trace error is O(epsilon^(1/4)), uniformly in N, in addition to
the vanishing O(N^(-1/2) sqrt(log(eN))) replacement error. No numerical
script or heat enclosure is needed for these analytic bounds.
This is a covariance comparison, not an evaluated limit. The unmodified
F and all original coefficients remain in the fixed-mass trace. The
same ready target continues; no assessment has been changed or approved
during this research step.
