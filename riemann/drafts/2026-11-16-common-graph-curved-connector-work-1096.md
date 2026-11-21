# Curved common-graph connector — working record1096

Invocation target: the exact EXPLORE target in nomination1094/review1095.
This saves unfinished reasoning; it is not a certified result.

Completion note: the resulting construction, all four exact coefficients,
signed determinant and full bounds are now written canonically in
`lemmas/C468f-common-graph-curved-lower-connector.md`. They await a
separate conceptual audit. The tentative reasoning below is preserved
as the interruption checkpoint, not a second proof or an approval.

Main gap: L030–L032/C032a actual-Xi all-degree positivity. The bounded
intermediate test changes only the lower connector's real graph. A
matched local construction could support signed assembly; other faces,
relative deformation and Xi transfer remain independent obligations.

Inputs read: C467e(13)–(26), C467z(6)–(12)/audit1083,
C467p(6)–(18)/audit1049, C467l's actual root limits and C467m's
root/weight estimates. Prior joint affine stop1092/audit1094 is retained.
No essential new source has been identified. Standard smooth pullback
and regular ODE tools are reused from review1095.

Proposed construction: on the smooth physical graph W(t,q)=p_c(t,q)+iq,
solve chi_t+b_c dot D_q chi=0 with chi(0,q)=product f(q_j) by the
regular backward flow on an enlarged compact q box. Define
Theta(t,u)=chi(t,Im Y(t,u)) and phi(t,x,s,h)=chi(t,Q_p(t,x,s,h)).
The backward path need not stay in the original chamber image: this
is an auxiliary extension used to define a particular scalar, not a
claim that every candidate has that trace. Original outer faces impose
no additional prescribed values. Need verify this distinction and the
closed-domain continuity and endpoint/permutation identities explicitly.

Tentative algebra to check: with c=x+h/3, I=sum q_j, q=q_3,
alpha=q_2-q_1 and v=s alpha/2,
det D_(x,s,h) Q_p=alpha h N/(2 Q_t'(q)), where C467p(12)–(14)
give N>0 for t,h>0. Thus the physical graph sector would give the
correct common-minus spatial sign, including its zeros by continuity.

Tentative full-mass bounds: put lambda=h+sqrt(t). Actual roots obey
alpha comparable to sqrt(t), beta_g and alpha+beta_g comparable to
lambda. Simple-root differentiation with bounded coefficient derivatives
gives |Q_x|+|Q_h|<=C/(alpha lambda), |Q_s|<=C alpha;
the actual root ODE gives |Q_t|<=C/alpha. The new graph is smooth,
so these also bound its columns. The original weight should satisfy
|F(W(t,Q_p))|<=C s^2 alpha^2 lambda^4. Hadamard's inequality would
then give |A|<=C s^2 alpha lambda^2,
|B_c|<=C s^2 lambda^2/alpha, |U|+|V|<=C s^2 alpha lambda^3.
Bounded physical derivatives of chi would make each of
|A phi_t|, |B_c phi_s|, |U phi_x|, |V phi_h| <= C_f s^2 lambda^2.
This would prove joint L1, even though it is weaker than the old
affine bounds. No bound or face identity is imported from that old map.

Continue only after checking the signed determinant, undivided equation,
original endpoints and all four terms. A proved conflict stops this
replacement; inability to bound a term is inconclusive. Boundary form
limits require their own dominating bounds. Do not infer an old triangle
match, global Stokes identity, common physical vertex value or RH result.
