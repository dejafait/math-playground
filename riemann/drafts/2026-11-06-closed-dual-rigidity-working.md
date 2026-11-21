# Closed-dual rigidity: saved working argument

Completed later in this same invocation as L867; the full canonical proof
is `lemmas/L867-all-plane-closed-dual-rigidity.md` relative to the notebook.
All pending checks below are preserved as the earlier working state;
the completed proof uses bounded exponential slices for Liouville.
Independent conceptual audit remains pending.

Invocation target: the exact all-plane domination/period test in
`literature/2026-11-06-actual-g-closed-dual-domination-test.md` (prior EXPLORE).
Essential input L847, including actual G,R,C,F, omega and the compact
graph homotopy. Main gap remains L030-L032/C032a mixed positivity.

Unverified working calculation, saved before final proof checking:
write dx_j=Re(dz_j/z_j), dy_j=Im(dz_j/z_j), eta=(dx_1+i dy_1)
wedge (dx_2+i dy_2), so omega=-F eta. For A=[[a,b],[c,d]],
eta(E_1,E_2)=det A-1+i tr A. A general real two-form has coefficients
p,q,r,s,t,v on dx1dy1, dx1dx2, dx1dy2, dy1dx2, dy1dy2, dx2dy2.
Its evaluation is -p b+q(ad-bc)+r a+s d+t+v c.

On J=0, set d=-a and c=-(1+a^2)/b, for any a and b!=0.
Domination gives q+t+(r-s)a-p b-v(1+a^2)/b=0.
Vary b and a: p=v=0, r=s, t=-q. Thus alpha=Re(gamma eta),
gamma=q-i r. Every pair (U,V)=(det A-1,tr A) is achieved by
A=[[0,-(U+1)],[1,V]], so |gamma|<=|F|, even at F=0.

Remaining checks before claiming the result: d alpha=0 has separate
(2,1) and (1,2) components, apparently implying dbar gamma=0; verify
C1 regularity and injectivity. Then h=-gamma/F is bounded holomorphic
off {F=0}; apply the assessed Lebl SCV Theorem1.6.1 to extend across
every divisor point. F is holomorphic and nonzero at (R,2R).
Apply assessed Liouville on bounded entire exponential slices of h
to obtain a constant c with |c|<=1. If justified, alpha=Re(c omega),
so |integral_T alpha|<=|integral_T omega|, sharply, and this entire
certificate class has no strict gain. Equality gives no graph.

No new sources, numerical scripts, zero census or RH assumption used.
No claim about certificates dominated on a smaller class or nonsmooth
certificates. Final canonical proof and honest checkpoint still pending.
