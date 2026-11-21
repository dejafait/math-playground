# Boundary metric working note2010

Completed this turn: the canonical full proof and coefficient bounds are
in C029n, with `scripts/pollaczek/tilted-boundary-metric-2010.json`.
The original unfinished algebra below is retained as the checkpoint.
It led to an exact incompatibility, not a metric or an RH claim.

Approved scope: assessment2009, N=6 only. Status: unfinished exact
compatibility test; no coefficient sign or degree is yet certified.

Write a_k=6!/((6-k)!6^k) beta_k. Conditional on a_6!=0, use descending
basis (p_5,...,p_0), C=H-6e_1 c^T, c_j=a_(6-j)/a_6. The positive
diagonal scaling has squared diagonal entries
(693/256,315/128,35/16,15/8,3/2,1); D_6=1.
The scaled basis J has successive off-diagonals
sqrt(55/2),sqrt(18),sqrt(21/2),sqrt(5),sqrt(3/2).

Set v_j=6c_j D_j/D_1 and A=J-e_1 v^T. In blocks A=(alpha,b^T;c,B),
alpha=-v_1, c=sqrt(55/2)f_1, b=(sqrt(55/2)-v_2,-v_3,...,-v_6),
and B is the symmetric bottom-right 5 by 5 block of J. The proposed
G=(g,y^T;y,I_5) has g=1+2z_1, y=(z_2,...,z_6).
Its complete compatibility equations are

    (B-alpha I)y+g b=c,
    y_i b_j-b_i y_j=0, 1<=i<j<=5.

For b!=0 the latter force y=lambda b. The last two rows of the first
equation force g=lambda=0 if

    K=b_4(Bb)_5-b_5(Bb)_4
     =sqrt(3/2)(v_5^2-v_6^2)-sqrt(5)v_4 v_6

is nonzero, contradicting c!=0. Algebraically

    K=36 sqrt(3/2)/(a_6^2 D_1^2) * Q,
    Q=(3/2)a_1^2-a_0^2-(5/2)a_2 a_0.

Remaining checks: verify these identities directly, certify a_6!=0 and
Q!=0 using exact source u_0,...,u_8 (all odd terms retained), and prove
every enclosure including the pi and sqrt(2) bounds. No inertia test is
needed if incompatibility is established. A standard-library Fraction
certificate will use elementary finite arctangent bounds, not Arb or a
new unassessed numerical theorem. Any result is only for this ansatz at
N=6; eventual variants and actual-family uniform index remain open.
