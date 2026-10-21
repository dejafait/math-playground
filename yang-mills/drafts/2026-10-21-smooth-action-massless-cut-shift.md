# Massless static comparison — bounded working record

Approved target: Test the ordered static bound
|U_i^0(F^0)-a^(-3)K_(i,Vmix)|<=C_i N^(5/2)log(eN)^2 against exactly
L179(7), for both actual probes. Reuse the unchanged EXPLORE assessment
in literature/2026-10-20-smooth-action-ordered-static-rate.md.

The main gap remains the interacting reflected error <=c_box/2 and the
independent continuum/infrared requirements. This attempt isolates the
moving axial cut inside the approved ordered comparison. L178's local
generator forces |r-s|<=R at a closing vertex (s,X), so replacing
1_(t>r) by 1_(t>s) changes only a fixed-width axial strip. A useful
partial threshold is O(N^(5/2)) with a polynomial exterior-mode envelope;
it would leave the literal triangular trace for boundary transfer,
transverse freezing and identification with exactly L179(7).

Initial calculation, subsequently completed below: sum J_j against the right Green
column before taking absolute values. The exact sine basis suggests
||G(X,.)||_2<=C sqrt(N) and ||J_j G(.,U)||_2<=C uniformly for all
transverse vertices, including end rows. Cauchy--Schwarz would bound
the ordered transverse contraction with m by C a^3 p(l)sqrt(N).
There are O(N^4) closing/strip choices, M<=N, and A^gen h has a
polynomial O(1) bound on its compact support. This gives N^(5/2).
Check the pointwise inverse diagonal, all rectangular indices and the
full heat envelope before recording any conclusion.

Essential inputs: L156 L159 L175 L178 L179 L256. Targeted duplicate
search found only L179's fixed-mass/fixed-degree cut-strip argument,
not this massless finite-N estimate. ATTEMPTS/030/038/045 remain intact.
Abandon this factorization if it needs to move m through J or G, omit
source/end rows, extend the rough upper forest jump smoothly, or use
L179's qualitative fixed-mass convergence at a varying mass. The complete
static threshold is not established by this strip estimate alone.

Completed: [L257](../lemmas/L257-massless-static-moving-cut-comparison.md)
proves the cut error O(N^(5/2)) uniformly at zero mass, including its
polynomial heat envelope. The complete finite sine basis gives
G_(XX)<=6 and (G^2)_(XX)<=3N, while the end-edge energy inequality
gives ||J_j G delta_U||^2<=24. The proof and exact triangular
comparison are canonical in L257. Its separate critical audit is
pending; no claim of discovery beyond the inspected sources is made.

The full approved static rate remains open. Continue on the same
unchanged assessed target, using L257 to account for the moving cut;
the retained triangular trace still needs boundary transfer, transverse
freezing and raw/full-heat matching against exactly L179(7). No new
assessment or preapproval is created. No earlier work is discarded.
