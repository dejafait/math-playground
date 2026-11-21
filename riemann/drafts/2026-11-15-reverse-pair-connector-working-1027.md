# Straight reverse pair connector — working1027

Approved target: test the unchanged connector in nomination1025/review1026
(EXPLORE at invocation start). One proof attempt, with no source refresh.
Main gap remains L030–L032/C032a actual-Xi all-degree positivity. A local
signed collision contribution would address C467i's face defect only;
triple junctions, outer faces, global assembly and Xi transfer stay open.

Saved before completing the proof. C467i/audit1025 gives a regular
coefficient trajectory at e(x,x,y), a smooth third root q3 and a quadratic
factor with alpha=O(t), gamma=-2t+O(t²). Put qc=x-alpha/2 and
b²=(alpha²-4gamma)/(4t), smoothly extended by b(0)=sqrt(2).
C467e(14) gives the exact quadratic reconstruction P(v). Therefore

    m=P(qc)+t b² Pi3+i qc,
    d=sqrt(t) D,   D=b(i-Pi2-q3 Pi3),
    w=P(q3)+i q3.

All of m,D,w are smooth in (t,x,y) down to zero; their initial values
are ix,i sqrt(2),iy. This avoids assuming smooth individual roots at
zero. For Z=(m-sd,m+sd,w), J=m_x w_y-m_y w_x and W=w-m, the exact
spatial coefficient is

    C=-F(Z) det(Z_x/i,Z_s/i,Z_y/i)
     =-8i s² d³ (W²-s²d²)² exp(-H(Z)) J.

Thus C=s² t^(3/2) G with G continuous and
G(0,x,s,y)=16 sqrt(2) exp(-H0-2beta(ix)-beta(iy))(y-x)^4.
On a compact separated rectangle near (0,1/32), this has a strict
positive sector. A uniform perturbation of G would prove the sector
through s=0 by exact factorization, not normalized-phase continuity.

Orientation check: in dt dx ddelta dy, chamber faces at delta=0 are
minus the positive trace and plus the negative trace. In dt dx ds dy,
the connector has plus its s=1 trace and minus its s=-1 trace. These
cancel exactly with the original chamber orientations. The same global
minus normalization makes the connector spatial coefficient C positive.

Remaining checks before writing the canonical result: all coefficients
of 2i F dm wedge (s dd+d ds) wedge dw; signed time and x/y side terms
with arbitrary smooth scalar tests; integrability at t=0 and zero
initial connector mass; complete uniform-domain and phase arguments.
No result is claimed from this interim note alone. No numerical or
symbolic script is needed for the explicit identities.

Completed1027: the full proof is now canonical in
`lemmas/C467j-actual-h-reverse-straight-pair-connector.md`. It supplies
the uniform sector with c=1/2, exact face matching, every mixed
coefficient and the tested identity with all time/lateral terms.
Spatial initial mass is O(t^(3/2)). The local result awaits an
independent conceptual audit; this working note is not a second proof.
