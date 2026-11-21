# One-coordinate theta marginal — working checkpoint, step180

The supplied step179 EXPLORE assessment covers exactly the fixed n=2
marginal of complete L969(5). Main gap: all-index L966(16), with
L030-L032/C032a still open. The positive threshold is J_2(u,v)>=0
everywhere; a proved negative point/region retires only this pointwise
marginal test. No profile change or general-n calculation is included.

Use L019, L966, L967 and audited L969. Write a_r=int A H_r(b),
c_r=int A H_r(h), b=1/4, h=5184, Delta=h-b, q=72 and
gamma=1/[2(c_0+c_1)]. The five factor moments are
m_0=1/2, m_1=2a_0, m_2=4a_1,
v_0=1/2+2Delta c_0, v_1=2c_0+2Delta c_1.

For S=Sym_2, integrating a normalized triple product gives
3 int A(w) Sym_3(f,g,k)(u,v,w) dw
=m_f S(g,k)+m_g S(f,k)+m_k S(f,g).
Repeated factors retain repeated contributions. Applying this to all
four L969(5) terms gives the proposed complete expression

    3J_2 = (d_1 m_1+d_2 m_2) S(B_0,C_0)
           +(d_1 m_0-2d_2 m_1) S(B_1,C_0)
           +d_2 m_0 S(B_2,C_0)
           +d_1 v_0 S(B_1,B_0)+d_2 v_0 S(B_2,B_0)
           -d_2 v_0 B_1(u)B_1(v)
           -2d_1 m_0 S(B_0,C_1)-d_1 v_1 B_0(u)B_0(v).

With E(t)=t exp(qt), L969 gives B_0/E,C_0/E -> g=gamma/(4q),
C_1/E -> k=Delta/(2q), and B_1/E,B_2/E ->0. The proposed limit is

    J_2(t,t)/E(t)^2 -> (d_1 g^2/3)
       [2a_0+(Delta/h)a_1-(2+4Delta)c_0-6Delta c_1].

The positive-series definitions imply c_0>=a_0>0 and c_1>=a_1>0.
If the complete marginal coefficients above check, the bracket is
at most -4Delta c_0-Delta(6-1/h)c_1<0. This uses actual moments,
not floating point normalization or a sign of the total integral.

Completed: all 24 labeled placements agree with the complete marginal;
normalization and moment-domination residuals are zero. Fixed-slice
convergence, continuity and the negative-region implication are proved
in C969a. The exact certificate is
`scripts/li-theta/one-coordinate-marginal-check-180.json`.
The candidate calculation above has become a local negative result,
pending independent audit. No global integral sign or RH conclusion
is established; do not use this working note as a second proof source.
