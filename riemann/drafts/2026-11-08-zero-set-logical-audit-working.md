# Zero-set logical audit working checkpoint — step124

2026-11-08. Approved target: audit the exact strict condition in
`literature/2026-11-08-zero-set-logical-strength-audit.md`.
Main gap remains L030-L032/C032a. No actual theta sign is assumed.

Calculation to preserve: set f=Xi, P(x,y)=|f(x+iy)|^2 and y>0.
L898 gives C_y(x)=P_y/y and A_0(y)>0. At a zero z0=x0+iy0,
P_y=0 and P_yy=2|f'(z0)|^2. Therefore the t derivative of
C_sqrt(t)(x0)/A_0(sqrt(t)) at t=y0^2 is
|f'(z0)|^2/(y0^2 A_0(y0)). It is positive for a simple zero and
zero for every multiple zero, incompatible with strict negativity.
L018 supplies conjugation and 0<|Im z0|<1/2 for nonreal zeros.

Reverse direction: the inspected primary arXiv:1205.2773v1,
Section 2, proof of Theorem 1.1, printed p.4, explicitly establishes
Re(xi'/xi)>0 to the right of every zero. Under RH this applies for
Re s>1/2 at every ordinate. With s=1/2+y-ix, functional symmetry
gives f(x+iy)=xi(s), so P_y=2P Re(xi'/xi)>0. Thus C_y(x)>0;
the conditional assertion is vacuous. Normalizations agree by
Gamma(1+s/2)=(s/2)Gamma(s/2). No |x|>=8 restriction from the
paper's separate zeta/eta theorems applies here.

Remaining before completion: write the full canonical equivalence,
check smoothness/chain rule and exact dependencies, record the scoped
stop, nominate a different uncovered continuation, and validate docs.
No scripts or further sign mechanism are warranted in this attempt.

Completed in canonical
[L901](../lemmas/L901-strict-normalized-defect-zero-set-condition-equivalent-to-rh.md).
The checkpoint above preserves the pre-write reasoning; its remaining-work
sentence is historical, not an additional current action.
